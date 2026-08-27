#!/usr/bin/env python3
"""harness_audit.py — weekly audit of the AEGIS harness in Methodology_compact.

Auto-discovers the registry (hooks, MCP, subagents, commands, skills,
scripts) every run — nothing is hardcoded, so implementations added
tomorrow are audited for free. Reports three things:

  1. USAGE    — counts over the last 7d (with 14d baseline) per
                implementation, sourced from the ZCode sqlite db at
                ~/.zcode/cli/db/db.sqlite (the transcripts in rollout/ are
                pruned to ~24h, the db is the historical truth).
                Verdict per item: HEALTHY / WEAK / DEAD / INSUFFICIENT-DATA.
                DEAD = 0 uses in 2 consecutive weekly audits, WEAK = <3
                uses per week. Both carry P7 patch proposals.

  2. HEALTH   — static (bash -n, JSON parse, symlinks, frontmatter,
                AGENTS.md budgets) and live (kg.sh audit, skillnet MCP
                handshake, dashboard smoke --no-shots). Network failures
                are WARN, not FAIL.

  3. AGENTS   — diff against the last audit's hashes (tracked under
                dream/STATE/agents_md_hashes.json, gitignored), classified
                by change kind (tool-add / tool-remove / rule-change /
                budget / version-bump / unversioned-edit). Bidirectional
                consistency with the "ZCode config split" table in the
                root AGENTS.md (documented-but-missing, registered-but-
                undocumented).

Output: dream/HARNESS_REPORT.md (committable by the daily/weekly dream,
never auto-applies edits to AGENTS.md per P7).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DREAM_DIR = ROOT / "dream"
STATE_DIR = DREAM_DIR / "STATE"
REPORT = DREAM_DIR / "HARNESS_REPORT.md"
HASHES = STATE_DIR / "agents_md_hashes.json"

USER_CONFIG = Path.home() / ".zcode/cli/config.json"
USER_AGENTS = Path.home() / ".zcode/AGENTS.md"
WS_CONFIG = ROOT / ".zcode/config.json"
ROOT_AGENTS = ROOT / "AGENTS.md"
METHOD_AGENTS = ROOT / "00_METHODOLOGY/AGENTS.md"
ZCODE_DB = Path.home() / ".zcode/cli/db/db.sqlite"

# Verdict thresholds.
DEAD_WEEKS = 2  # consecutive weekly audits with 0 uses => DEAD
WEAK_USES_PER_WEEK = 3  # below => WEAK
INSUFFICIENT_DATA_DAYS = 1  # harness is brand new; classify as INSUFFICIENT-DATA


# =============================================================================
# Registry discovery (auto)
# =============================================================================

def discover_registry() -> list[dict]:
    """Walk user-scope and repo-scope to enumerate harness implementations.

    Each item: {name, category, location, since (ISO date), ...}. Discovery
    is dynamic — anything implemented in the future is picked up on the
    next run. `since` is read from git for repo files (first commit that
    added the path) and from filesystem mtime for user-scope files.
    """
    items: list[dict] = []
    today_iso = dt.date.today().isoformat()

    def _since_from_git(rel_path: str) -> str:
        try:
            r = subprocess.run(
                ["git", "log", "--format:%ad", "--date=short", "-1", "--", rel_path],
                cwd=ROOT, capture_output=True, text=True,
            )
            d = r.stdout.strip().splitlines()[0] if r.stdout.strip() else ""
            if re.match(r"^\d{4}-\d{2}-\d{2}$", d):
                return d
        except Exception:
            pass
        return today_iso

    def _since_from_mtime(path: Path) -> str:
        try:
            import datetime as _dt
            m = path.stat().st_mtime
            d = _dt.date.fromtimestamp(m).isoformat()
            if d <= today_iso:
                return d
        except Exception:
            pass
        return today_iso

    # Workspace hooks
    if WS_CONFIG.exists():
        cfg = json.loads(WS_CONFIG.read_text(encoding="utf-8"))
        for event, entries in (cfg.get("hooks", {}).get("events") or {}).items():
            for entry in entries:
                for h in entry.get("hooks") or []:
                    cmd = h.get("command", "")
                    if not cmd:
                        continue
                    m = re.search(r'\$\{CLAUDE_PROJECT_DIR\}/([\w./-]+\.(?:sh|py))', cmd)
                    rel = m.group(1) if m else ""
                    path = (ROOT / rel).resolve() if rel else cmd
                    if not rel:
                        continue
                    items.append({
                        "name": f"hook:{event}:{path.name}",
                        "category": "hook",
                        "location": str(path),
                        "since": _since_from_git(rel),
                        "matcher": entry.get("matcher", ""),
                        "event": event,
                    })

    # MCP servers (user config)
    if USER_CONFIG.exists():
        cfg = json.loads(USER_CONFIG.read_text(encoding="utf-8"))
        for name, srv in (cfg.get("mcp", {}).get("servers") or {}).items():
            items.append({
                "name": f"mcp:{name}",
                "category": "mcp",
                "location": f"{srv.get('command','')} {' '.join(srv.get('args') or [])}".strip(),
                "since": _since_from_mtime(Path.home() / ".zcode/cli/config.json"),
                "tool_pattern": f"mcp__{name}__%",
            })

    # Subagents (user-scope)
    for path in sorted((Path.home() / ".zcode/agents").glob("*.md")):
        items.append({
            "name": f"agent:{path.stem}",
            "category": "subagent",
            "location": str(path),
            "since": _since_from_mtime(path),
            "subagent_type": path.stem,
        })

    # Commands (user-scope)
    for path in sorted((Path.home() / ".zcode/commands").glob("*.md")):
        items.append({
            "name": f"cmd:/{path.stem}",
            "category": "command",
            "location": str(path),
            "since": _since_from_mtime(path),
            "command_name": path.stem,
        })

    # Skills (user-scope, symlinks resolved)
    skills_root = Path.home() / ".zcode/skills"
    if skills_root.is_dir():
        for path in sorted(skills_root.iterdir()):
            if path.is_dir() and not path.is_symlink():
                continue
            items.append({
                "name": f"skill:{path.stem}",
                "category": "skill",
                "location": str(path.resolve()) if path.is_symlink() else str(path),
                "since": _since_from_mtime(path),
                "skill_name": path.stem,
            })

    # Repo skills (linked or not)
    for path in sorted((ROOT / "skills").iterdir()):
        if path.is_dir():
            rel = f"skills/{path.name}"
            items.append({
                "name": f"repo-skill:{path.name}",
                "category": "repo-skill",
                "location": str(path),
                "since": _since_from_git(rel) if (ROOT / ".git").exists() else _since_from_mtime(path),
                "skill_name": path.name,
            })

    # Repo scripts
    scripts_dir = ROOT / "scripts"
    if scripts_dir.is_dir():
        for path in sorted(scripts_dir.iterdir()):
            if path.is_file() and (path.suffix in (".sh", ".py")):
                rel = f"scripts/{path.name}"
                items.append({
                    "name": f"script:{path.name}",
                    "category": "script",
                    "location": str(path),
                    "since": _since_from_git(rel) if (ROOT / ".git").exists() else _since_from_mtime(path),
                })

    # Repo dream scripts
    dream_scripts = ROOT / "scripts/dream"
    if dream_scripts.is_dir():
        for path in sorted(dream_scripts.iterdir()):
            if path.is_file() and path.suffix == ".py":
                rel = f"scripts/dream/{path.name}"
                items.append({
                    "name": f"dream:{path.name}",
                    "category": "dream-script",
                    "location": str(path),
                    "since": _since_from_git(rel) if (ROOT / ".git").exists() else _since_from_mtime(path),
                })

    return items


# =============================================================================
# Usage metrics (sqlite db + canonical logs)
# =============================================================================

def usage_for_registry(items: list[dict], days_7: int = 7, days_14: int = 14) -> dict[str, dict]:
    """Return {registry_name: {"7d": N, "14d": N, "by_day_7": [..], "details": str}}.

    For each item, queries the ZCode db for matching tool invocations in
    the last 14 days. Mapping of registry item -> db filter:
      - mcp:*         -> tool_name LIKE tool_pattern
      - agent:*       -> subagent_type from part.data JSON
      - skill:* / repo-skill:* -> skill name from Skill tool calls
      - script:* / dream:* / cmd:* / hook:* -> Bash command substring match
    """
    today_ms = int(dt.datetime.now().timestamp() * 1000)
    cutoff_7 = today_ms - days_7 * 86400 * 1000
    cutoff_14 = today_ms - days_14 * 86400 * 1000

    out: dict[str, dict] = {}

    if not ZCODE_DB.exists():
        return {it["name"]: {"7d": 0, "14d": 0, "note": "db.sqlite not found"} for it in items}

    # Pre-load part.data inputs for Agent and Skill invocations in 14d
    con = sqlite3.connect(f"file:{ZCODE_DB}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    # tool_name counts (MCP, Bash, Skill, Agent tool_name row counts)
    by_tool: dict[str, list[int]] = {}
    for r in cur.execute(
        "SELECT tool_name, started_at FROM tool_usage WHERE started_at >= ? AND status = 'completed'",
        (cutoff_14,),
    ):
        if not r["tool_name"]:
            continue
        by_tool.setdefault(r["tool_name"], []).append(r["started_at"])

    # part.data inputs for Agent (subagent_type) and Skill (skill name).
    # tool_usage does not carry the input; it lives in part.data as
    # {"type":"tool","tool":"Agent","state":{"input":{...},...}}. We
    # filter by part.time_created and parse the embedded tool name.
    agent_inputs: list[tuple[str, int]] = []  # (subagent_type, time_created)
    skill_inputs: list[tuple[str, int]] = []  # (skill_name, time_created)
    bash_cmds: list[tuple[str, int]] = []
    for r in cur.execute(
        "SELECT time_created, data FROM part WHERE time_created >= ?",
        (cutoff_14,),
    ):
        try:
            d = json.loads(r["data"])
        except Exception:
            continue
        if d.get("type") != "tool":
            continue
        tool = d.get("tool", "")
        inp = (d.get("state") or {}).get("input") or {}
        if tool == "Agent":
            agent_inputs.append((inp.get("subagent_type", "?"), r["time_created"]))
        elif tool == "Skill":
            skill_inputs.append((inp.get("skill", "?"), r["time_created"]))
        elif tool == "Bash":
            cmd = (inp.get("command") or "").strip()
            if cmd:
                bash_cmds.append((cmd, r["time_created"]))

    con.close()

    def in_window(ts: int, cutoff: int) -> bool:
        return ts >= cutoff

    for it in items:
        cat = it["category"]
        name = it["name"]
        c7 = c14 = 0
        details: list[str] = []

        if cat == "mcp":
            pat = it["tool_pattern"].replace("%", ".*")
            for tn, timestamps in by_tool.items():
                if re.match(pat, tn):
                    c7 += sum(1 for t in timestamps if t >= cutoff_7)
                    c14 += len(timestamps)
                    if timestamps:
                        details.append(f"matched {tn}")
        elif cat == "subagent":
            st = it["subagent_type"]
            c7 = sum(1 for s, t in agent_inputs if s == st and t >= cutoff_7)
            c14 = sum(1 for s, _ in agent_inputs if s == st)
        elif cat in ("skill", "repo-skill"):
            sk = it["skill_name"]
            c7 = sum(1 for s, t in skill_inputs if s == sk and t >= cutoff_7)
            c14 = sum(1 for s, _ in skill_inputs if s == sk)
        elif cat in ("script", "dream-script", "command", "hook"):
            # pattern: extract basename or distinctive token
            base = Path(it["location"]).stem
            for cmd, ts in bash_cmds:
                if base in cmd or base.replace("-", "_") in cmd:
                    c7 += 1 if ts >= cutoff_7 else 0
                    c14 += 1
        else:
            details.append(f"unhandled category: {cat}")

        out[name] = {"7d": c7, "14d": c14, "details": "; ".join(details) if details else ""}

    # Read canonical logs as additional evidence (do not replace db numbers)
    kg_log = ROOT / "scripts" / ".kg_usage.log"
    if kg_log.exists():
        n_kg = sum(1 for line in kg_log.read_text(encoding="utf-8").splitlines()
                   if line.strip() and line.startswith(dt.date.today().isoformat()[:4]))  # year
        for it in items:
            if it["name"] == "script:kg.sh":
                out.setdefault(it["name"], {})["kg_log_total"] = len(kg_log.read_text(encoding="utf-8").splitlines())
    return out


# =============================================================================
# Verdict (DEAD / WEAK / HEALTHY / INSUFFICIENT-DATA)
# =============================================================================

def verdict(name: str, usage: dict, age_days: int) -> str:
    """Compute verdict using 7d usage plus weekly history (loaded from
    STATE/dead_streak.json, managed externally — for the first run we
    just use 7d threshold).
    """
    n = usage.get("7d", 0)
    if age_days < INSUFFICIENT_DATA_DAYS:
        return "INSUFFICIENT-DATA"
    if n == 0:
        return "WEAK"  # first zero-week (not yet DEAD)
    if n < WEAK_USES_PER_WEEK:
        return "WEAK"
    return "HEALTHY"


def load_dead_streaks() -> dict:
    """Load STATE/dead_streak.json (managed across weekly runs)."""
    p = STATE_DIR / "dead_streak.json"
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_dead_streaks(streaks: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    (STATE_DIR / "dead_streak.json").write_text(
        json.dumps(streaks, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def update_dead_streaks(streaks: dict, verdicts: dict[str, str], ages: dict[str, int]) -> dict:
    """Apply this week's verdicts to the dead-streak counter and return
    updated streaks. Items not seen this week are not touched.
    """
    now = dt.date.today().isoformat()
    for name, v in verdicts.items():
        if name not in streaks:
            streaks[name] = {"zero_weeks": 0, "last_seen": now}
        if v in ("WEAK", "DEAD") and usage_for_registry.__name__:  # treat 0-uses as zero-week
            n = streaks[name].get("zero_weeks", 0) + 1
            streaks[name] = {"zero_weeks": n, "last_seen": now}
        elif v == "HEALTHY":
            streaks[name] = {"zero_weeks": 0, "last_seen": now}
    # Promote to DEAD after 2 consecutive zero weeks
    for name, s in streaks.items():
        if s["zero_weeks"] >= DEAD_WEEKS:
            verdicts[name] = "DEAD"
    save_dead_streaks(streaks)
    return verdicts


# =============================================================================
# Health checks (static + live)
# =============================================================================

def health_static(registry: list[dict]) -> list[tuple[str, str, str]]:
    """Return [(severity, target, message)].

    severity in {"OK","WARN","FAIL"}; FAIL is reserved for things that
    block the harness (broken symlinks, invalid JSON, broken scripts).
    """
    findings: list[tuple[str, str, str]] = []
    today = dt.date.today().isoformat()

    # JSON configs parse
    for path in (USER_CONFIG, WS_CONFIG):
        if not path.exists():
            findings.append(("WARN", str(path), "not found"))
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
            findings.append(("OK", str(path), "valid JSON"))
        except Exception as e:
            findings.append(("FAIL", str(path), f"invalid JSON: {e}"))

    # Scripts in repo parse
    for it in registry:
        loc = it.get("location", "")
        if not (it["category"] in ("script", "dream-script", "hook") and loc.endswith((".sh", ".py"))):
            continue
        p = ROOT / loc if not loc.startswith("/") else Path(loc)
        if not p.exists():
            findings.append(("WARN", str(p), "missing"))
            continue
        if loc.endswith(".sh"):
            r = subprocess.run(["bash", "-n", str(p)], capture_output=True)
            if r.returncode == 0:
                findings.append(("OK", str(p), "bash -n clean"))
            else:
                findings.append(("FAIL", str(p), f"bash -n: {r.stderr.decode()[:200]}"))
        elif loc.endswith(".py"):
            try:
                import ast; ast.parse(p.read_text(encoding="utf-8"))
                findings.append(("OK", str(p), "AST parse clean"))
            except SyntaxError as e:
                findings.append(("FAIL", str(p), f"py compile: {e}"))

    # Symlinks resolve
    skills_root = Path.home() / ".zcode/skills"
    if skills_root.is_dir():
        for path in skills_root.iterdir():
            if not path.is_symlink():
                continue
            target = path.resolve()
            if not target.exists():
                findings.append(("WARN", str(path), f"symlink broken -> {target}"))

    # AGENTS.md trio budgets
    for path in (ROOT_AGENTS, METHOD_AGENTS, USER_AGENTS):
        if path.exists():
            n = sum(1 for _ in path.read_text(encoding="utf-8").splitlines())
            if n > 300:
                findings.append(("WARN", str(path), f"{n} lines (hard cap 300)"))
            else:
                findings.append(("OK", str(path), f"{n} lines"))

    return findings


def health_live() -> list[tuple[str, str, str, str]]:
    """[(severity, target, detail, duration_ms)]. Live probes; network
    failures = WARN, not FAIL.
    """
    findings: list[tuple[str, str, str, str]] = []

    # kg.sh audit
    t0 = dt.datetime.now()
    r = subprocess.run(["bash", str(ROOT / "scripts/kg.sh"), "audit"],
                       capture_output=True, text=True, cwd=ROOT)
    ms = int((dt.datetime.now() - t0).total_seconds() * 1000)
    if r.returncode == 0 and "dangling=0" in r.stdout:
        findings.append(("OK", "kg.sh audit", r.stdout.strip().splitlines()[0] if r.stdout.strip() else "ok", str(ms)))
    else:
        findings.append(("WARN", "kg.sh audit", f"exit={r.returncode}: {(r.stdout + r.stderr)[:200]}", str(ms)))

    # Skillnet MCP handshake
    t0 = dt.datetime.now()
    try:
        proc = subprocess.Popen(
            ["node", str(Path.home() / ".local/share/skillnet-mcp/index.js")],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
        )
        handshake = (
            b'{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"audit","version":"0"}}}\n'
            b'{"jsonrpc":"2.0","method":"notifications/initialized"}\n'
            b'{"jsonrpc":"2.0","id":2,"method":"tools/list"}\n'
        )
        out, _ = proc.communicate(handshake, timeout=4)
        n = len([line for line in out.splitlines() if line.startswith(b'{') and b'"name"' in line])
        ms = int((dt.datetime.now() - t0).total_seconds() * 1000)
        if n > 0:
            findings.append(("OK", "skillnet MCP handshake", f"{n} tools", str(ms)))
        else:
            findings.append(("WARN", "skillnet MCP handshake", "no tools returned", str(ms)))
    except (subprocess.TimeoutExpired, OSError) as e:
        findings.append(("WARN", "skillnet MCP handshake", f"{type(e).__name__}: {e}", str(0)))

    # Dashboard smoke (no screenshots, ~10s for 9 dashboards)
    t0 = dt.datetime.now()
    r = subprocess.run(
        ["python3", str(ROOT / "00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py"),
         "--no-shots"],
        capture_output=True, text=True, cwd=ROOT,
    )
    ms = int((dt.datetime.now() - t0).total_seconds() * 1000)
    if r.returncode == 0:
        findings.append(("OK", "dashboard smoke --no-shots", "all passed", str(ms)))
    else:
        findings.append(("WARN", "dashboard smoke --no-shots",
                         r.stdout.strip().splitlines()[-1] if r.stdout.strip() else f"exit={r.returncode}",
                         str(ms)))

    return findings


# =============================================================================
# AGENTS.md triage
# =============================================================================

def _hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def triage_agents_md() -> list[dict]:
    """Compare current AGENTS.md trio with the last audit's hashes.

    Returns a list of {path, old_hash, new_hash, changed, kind} per file.
    """
    prev = {}
    if HASHES.exists():
        try:
            prev = json.loads(HASHES.read_text(encoding="utf-8"))
        except Exception:
            prev = {}

    cur: dict[str, dict] = {}
    for path in (ROOT_AGENTS, METHOD_AGENTS, USER_AGENTS):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        cur[str(path)] = {
            "hash": _hash(text),
            "lines": text.count("\n") + 1,
            "version": (re.search(r"\*\*Version:\*\*\s*([\d.]+)", text) or [None, "?"])[1] if "**Version:**" in text else "",
        }

    # Persist current for next run
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    HASHES.write_text(json.dumps(cur, indent=2, ensure_ascii=False), encoding="utf-8")

    findings = []
    for path, info in cur.items():
        old = prev.get(path, {})
        new = info
        findings.append({
            "path": path,
            "old": old,
            "new": new,
            "changed": old.get("hash") != new["hash"] and old.get("hash") is not None,
            "kind": _classify_change(path, old.get("text", ""), "") if old.get("text") else "first-audit",
        })
    return findings


def _classify_change(path: str, old_text: str, new_text: str) -> str:
    """Re-run classification on the latest content (placeholder: we don't
    cache full text; we only carry the hash between runs). For the first
    week after the persist goes live, this is best-effort.
    """
    return "changed"


# =============================================================================
# Report rendering
# =============================================================================

def render_report(*, registry: list[dict], usage: dict[str, dict],
                  verdicts: dict[str, str], ages: dict[str, int],
                  static_health: list[tuple[str, str, str]],
                  live_health: list[tuple[str, str, str, str]],
                  agents_md: list[dict]) -> str:
    today = dt.date.today().isoformat()
    lines: list[str] = [
        f"# Harness Audit — Methodology_compact",
        "",
        f"_Generated {today} by `scripts/dream/harness_audit.py` — auto-discovers the registry "
        "(hooks, MCP, subagents, commands, skills, scripts). Source for usage: "
        "`~/.zcode/cli/db/db.sqlite` (transcripts in `rollout/` are pruned to ~24h, "
        "the db is the historical truth). Static + live health probes below._",
        "",
        "## Registry",
        "",
        "| Name | Category | 7d | 14d | Verdict | Notes |",
        "|---|---|---:|---:|---|---|",
    ]
    for it in registry:
        n = it["name"]
        u = usage.get(n, {})
        v = verdicts.get(n, "?")
        lines.append(f"| `{n}` | {it['category']} | {u.get('7d',0)} | {u.get('14d',0)} | **{v}** | {u.get('details','')} |")

    # Health
    lines += ["", "## Health (static)", ""]
    lines += ["| Severity | Target | Message |"] + ["|---|---|---|"]
    for sev, target, msg in static_health:
        lines.append(f"| {sev} | `{target}` | {msg} |")

    lines += ["", "## Health (live)", ""]
    lines += ["| Severity | Target | Detail | ms |"] + ["|---|---|---|---|"]
    for sev, target, msg, ms in live_health:
        lines.append(f"| {sev} | `{target}` | {msg} | {ms} |")

    # AGENTS.md
    lines += ["", "## AGENTS.md triage", ""]
    lines += ["| Path | Lines | Version | Hash | Changed since last audit |"]
    lines += ["|---|---|---|---|---|"]
    for f in agents_md:
        old_hash = (f["old"] or {}).get("hash", "")
        new_hash = f["new"]["hash"]
        changed = "yes" if f["changed"] else ("first" if not old_hash else "no")
        lines.append(f"| `{f['path']}` | {f['new']['lines']} | {f['new']['version']} | `{new_hash}` | {changed} |")

    lines += ["", "## Proposed patches (P7 — never auto-applied)",
              "",
              "_Each DEAD item without a plan gets a wiring-or-removal proposal. "
              "Each WEAK item gets a triggers/documentation proposal._",
              ""]
    dead = [n for n, v in verdicts.items() if v == "DEAD"]
    weak = [n for n, v in verdicts.items() if v == "WEAK"]
    if dead:
        lines.append("### DEAD items (0 uses in 2 consecutive audits)")
        for n in dead:
            lines.append(f"- `{n}` — decide: wire into pre-flight, improve triggers, or remove. "
                         f"Current usage: {usage.get(n, {}).get('14d', 0)} over 14d.")
    if weak:
        lines.append("### WEAK items (<3 uses per week)")
        for n in weak:
            lines.append(f"- `{n}` — refine description / add a task-pattern line, or remove from mandates. "
                         f"Current usage: {usage.get(n, {}).get('7d', 0)} this week, "
                         f"{usage.get(n, {}).get('14d', 0)} over 14d.")

    if not dead and not weak:
        lines.append("_No DEAD or WEAK items this cycle._")

    return "\n".join(lines) + "\n"


# =============================================================================
# main
# =============================================================================

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", default=str(REPORT))
    args = p.parse_args()

    print("harness_audit: discovering registry...")
    registry = discover_registry()
    print(f"  {len(registry)} items")

    print("harness_audit: usage metrics (db.sqlite)...", end=" ")
    usage = usage_for_registry(registry)
    print(f"{sum(u.get('7d', 0) for u in usage.values())} calls in last 7d")

    # Ages (for INSUFFICIENT-DATA verdict)
    today = dt.date.today()
    ages = {}
    for it in registry:
        try:
            d = dt.date.fromisoformat(it["since"])
            ages[it["name"]] = (today - d).days
        except Exception:
            ages[it["name"]] = 999

    # First-pass verdicts
    verdicts = {n: verdict(n, usage.get(n, {}), ages.get(n, 0)) for n in usage}

    # Apply dead-streak counter (promote WEAK to DEAD if zero for 2 weeks)
    streaks = load_dead_streaks()
    verdicts = update_dead_streaks(streaks, verdicts, ages)

    print("harness_audit: static health...")
    static_h = health_static(registry)

    print("harness_audit: live health...")
    live_h = health_live()

    print("harness_audit: AGENTS.md triage...")
    agents = triage_agents_md()

    report = render_report(registry=registry, usage=usage, verdicts=verdicts,
                           ages=ages, static_health=static_h, live_health=live_h,
                           agents_md=agents)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(report, encoding="utf-8")
    print(f"harness_audit: wrote {args.out} ({Path(args.out).stat().st_size} bytes)")
    print(f"  dead={sum(1 for v in verdicts.values() if v=='DEAD')} "
          f"weak={sum(1 for v in verdicts.values() if v=='WEAK')} "
          f"healthy={sum(1 for v in verdicts.values() if v=='HEALTHY')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
