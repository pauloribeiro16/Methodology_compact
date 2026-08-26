#!/usr/bin/env python3
"""adoption_audit.py — Deterministic adoption audit of project conversations.

Reads ZCode rollout transcripts + the canonical signals:
- `scripts/.kg_usage.log` (canonical KG adoption log)
- AGENTS.md mandatory sections (pre-flight, P5, mandatory skills)

Outputs `dream/ADOPTION_REPORT.md` with:
- Per-day activity counts
- KG subcommand distribution
- Mandated skill invocation counts
- Gap signals (pre-flight skipped, P5 impact missing before ID edits, etc.)
- AGENTS.md amendment proposals (NEVER auto-applied — propose-only per P7)
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "dream"))

from transcript_lib import exchanges_for_project, project_metrics  # noqa: E402


# --------------------- canonical signal readers ---------------------

def read_kg_usage_log(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        ts, user, rest = parts[0], parts[1], "\t".join(parts[2:])
        sub = rest.split(maxsplit=1)[0] if rest else ""
        out.append({"ts": ts, "user": user, "subcommand": sub, "rest": rest})
    return out


def read_progress_summary(repo_root: Path) -> dict:
    """Read each case's progress.json phase statuses (deterministic ground truth)."""
    cases_dir = repo_root / "02_CASES"
    out = {}
    if not cases_dir.exists():
        return out
    for case_dir in sorted(cases_dir.glob("Case_*")):
        pj = case_dir / "progress.json"
        if not pj.exists():
            continue
        try:
            d = json.loads(pj.read_text(encoding="utf-8"))
            phases = {}
            for k, v in (d.get("phases") or {}).items():
                phases[k] = {
                    "status": v.get("status"),
                    "gate": v.get("gate"),
                    "completed_at": v.get("completed_at"),
                }
            out[case_dir.name] = {
                "phase": d.get("phase"),
                "phases": phases,
                "active_contracts": d.get("active_contracts") or [],
            }
        except Exception as e:
            out[case_dir.name] = {"error": str(e)}
    return out


# --------------------- amendment proposal mining ---------------------

PROPOSALS = []


def maybe_propose(trigger: bool, *, title: str, rationale: str, patch: str) -> None:
    if trigger:
        PROPOSALS.append({"title": title, "rationale": rationale, "patch": patch})


def mine_amendments(metrics: dict, kg_log: list[dict], progress: dict, repo_root: Path) -> list[dict]:
    PROPOSALS.clear()

    # Proposal 1: low where/domain/nist usage vs hub calls
    where_n = metrics["kg_subcmd"].get("where", 0)
    domain_n = metrics["kg_subcmd"].get("domain", 0)
    nist_n = metrics["kg_subcmd"].get("nist", 0)
    impact_n = metrics["kg_subcmd"].get("impact", 0)
    if impact_n > 0 and where_n == 0 and domain_n == 0:
        maybe_propose(
            True,
            title="Make KG discovery routine in pre-flight, not optional",
            rationale=(f"Across all measured sessions: {impact_n} impact(s) but zero where/domain/nist — "
                       f"the KG is being used only for P5 propagation checks, not for finding things. "
                       f"Add 'if you don't know where to start: kg.sh where <topic>' as an explicit pre-flight step."),
            patch=("Pre-Flight Checklist:\n"
                   "  - [ ] If unsure where a topic lives: `scripts/kg.sh where <topic>` or `domain D-XX`"),
        )

    # Proposal 2: zero skill invocations
    if not metrics["skill_calls"]:
        maybe_propose(
            True,
            title="Skills are pre-flight but never invoked",
            rationale=("Zero `case-context-loader` or `doc-conventions` invocations recorded across "
                       "the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' "
                       "is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect."),
            patch=("Either:\n"
                   "  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`\n"
                   "      so it runs by default; or\n"
                   "  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually."),
        )

    # Proposal 3: pre-flight not visibly used
    maybe_propose(
        metrics["user_messages"] > 5 and metrics["exchanges_with_skill"] == 0,
        title="Document the pre-flight checklist as a tool-call contract",
        rationale=("Pre-flight is text-only; an agent may follow it silently and produce no detectable signal. "
                   "Codifying 'if you didn't run X, your output is invalid' as a self-check rule would make it enforceable."),
        patch=("Add to each pre-flight item: a short machine-checkable assertion. "
                   "E.g. 'If touching an ID-bearing doc: scripts/kg.sh impact <ID> must appear in tool calls of this turn'."),
    )

    # Proposal 4: case-context-loader is the most-needed skill in case work
    case_count = sum(1 for c in progress.values() if "phases" in c)
    if case_count and not metrics["skill_calls"].get("case-context-loader"):
        maybe_propose(
            True,
            title="Invoke case-context-loader at the start of any case session",
            rationale=(f"{case_count} case(s) tracked in 02_CASES/. case-context-loader is the only skill "
                       "that bootstraps a session with the actual current state. Use it before planning case work."),
            patch=("Add to the 'Where to start' section: 'Always start by running case-context-loader — "
                   "the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'"),
        )

    # Proposal 5: hooks vs self-report — kg-reminder is silently firing?
    hook_pj = repo_root / ".zcode" / "config.json"
    if hook_pj.exists():
        cfg = json.loads(hook_pj.read_text(encoding="utf-8"))
        if cfg.get("hooks", {}).get("enabled"):
            maybe_propose(
                True,
                title="Log hook firings for the dream to consume",
                rationale=("The kg-reminder hook fires once per session and the script writes nothing. "
                           "For adoption measurement we need a side-effect log line per fire "
                           "(e.g. `echo \"$(date -Iseconds) kg-reminder\" >> dream/STATE/hook.log`)."),
                patch=("In `kg-reminder.sh`, after `touch \"$SENTINEL\"`, append the same ts to a "
                       "line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder."),
            )

    return PROPOSALS


# --------------------- rendering ---------------------

def render_report(*, metrics: dict, kg_log: list[dict], progress: dict,
                  proposals: list[dict], repo_root: Path, since: str | None) -> str:
    today = dt.date.today().isoformat()
    lines = [
        f"# Adoption Report — AEGIS Methodology_compact",
        "",
        f"_Generated {today} by `scripts/dream/adoption_audit.py` — deterministic (no LLM)._",
        "",
        "## Activity",
        "",
        f"- **Project exchanges scanned:** {metrics['user_messages']} user messages",
        f"- **Exchanges with KG usage:** {metrics['exchanges_with_kg']}",
        f"- **Exchanges with mandated skill:** {metrics['exchanges_with_skill']}",
        "",
        "## KG subcommand distribution (from session transcripts)",
        "",
        "| Subcommand | Count |",
        "|---|---|",
    ]
    for sub, n in metrics["kg_subcmd"].items():
        lines.append(f"| `{sub}` | {n} |")
    if not metrics["kg_subcmd"]:
        lines.append("| _(none)_ | 0 |")
    lines += ["", "## Mandated skill invocations",
              "",
              "| Skill | Count |",
              "|---|---|"]
    if metrics["skill_calls"]:
        for s, n in metrics["skill_calls"].items():
            lines.append(f"| `{s}` | {n} |")
    else:
        lines.append("| _(none recorded)_ | 0 |")

    lines += ["", "## Canonical KG usage log (`scripts/.kg_usage.log`)",
              ""]
    if kg_log:
        # group by subcommand
        c = collections.Counter(e["subcommand"] for e in kg_log)
        lines.append("| Subcommand | Count |")
        lines.append("|---|---|")
        for k, v in c.most_common():
            lines.append(f"| `{k}` | {v} |")
        lines.append("")
        lines.append(f"_Last entries:_")
        for e in kg_log[-3:]:
            lines.append(f"- `{e['ts']}` `{e['subcommand']} {e['rest']}`")
    else:
        lines.append("_(empty)_")

    lines += ["", "## Case progress snapshot (ground truth)",
              "",
              "| Case | Current phase | Phase statuses |",
              "|---|---|---|"]
    for case, d in progress.items():
        if "error" in d:
            lines.append(f"| {case} | _(read error)_ | {d['error']} |")
            continue
        statuses = ", ".join(f"{k}={v['status']}" for k, v in sorted(d.get("phases", {}).items()))
        lines.append(f"| {case} | {d.get('phase')} | {statuses} |")

    lines += ["", "## AGENTS.md amendment proposals",
              "",
              "_Generated by deterministic signal mining; **never auto-applied** (P7 — human approves)._",
              ""]
    if not proposals:
        lines.append("_No proposals this cycle — adoption signals within tolerance._")
    else:
        for i, p in enumerate(proposals, 1):
            lines.append(f"### {i}. {p['title']}")
            lines.append("")
            lines.append(f"**Rationale:** {p['rationale']}")
            lines.append("")
            lines.append("**Proposed patch:**")
            lines.append("")
            lines.append("```")
            lines.append(p["patch"])
            lines.append("```")
            lines.append("")

    lines += ["---",
              "",
              "_Run with `--since YYYY-MM-DD` to limit the audit window once history accumulates._"]
    return "\n".join(lines) + "\n"


# --------------------- main ---------------------

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--rollout-dir", default=os.path.expanduser("~/.zcode/cli/rollout"))
    p.add_argument("--out", default=str(ROOT / "dream" / "ADOPTION_REPORT.md"))
    p.add_argument("--since", default=None, help="ISO date; only include sessions after this date")
    args = p.parse_args()

    rollout_dir = Path(args.rollout_dir)
    if not rollout_dir.exists():
        print(f"adoption_audit: no rollout dir at {rollout_dir}", file=sys.stderr)
        return 1

    # Build list of exchanges and filter by --since if given
    exchanges = list(exchanges_for_project(str(rollout_dir)))
    if args.since:
        cutoff = args.since
        exchanges = [e for e in exchanges if e.completed_at[:10] >= cutoff]

    metrics = project_metrics(exchanges)
    kg_log = read_kg_usage_log(ROOT / "scripts" / ".kg_usage.log")
    progress = read_progress_summary(ROOT)
    proposals = mine_amendments(metrics, kg_log, progress, ROOT)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_report(metrics=metrics, kg_log=kg_log, progress=progress,
                                 proposals=proposals, repo_root=ROOT, since=args.since),
                   encoding="utf-8")
    print(f"adoption_audit: wrote {out} ({out.stat().st_size} bytes, {len(proposals)} proposals)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
