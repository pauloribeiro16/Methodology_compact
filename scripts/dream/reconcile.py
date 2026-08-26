#!/usr/bin/env python3
"""reconcile.py — Compare git log vs project state files; surface drift.

The two "ground truths" of the project:
- git history (immutable, objective)
- 02_CASES/GLOBAL_PROJECT_STATE.md, case PROJECT_STATE.md, progress.json
  (subjective, edited by humans and agents, often stale)

Differences between the two = either (a) state files weren't updated after
real work, or (b) the state files describe planned work that never happened.
Both are valuable signals; both are patches the dream proposes but never
applies (P7).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


# --------------------- helpers ---------------------

def run_git(*args: str, cwd: Path | None = None) -> str:
    try:
        out = subprocess.check_output(["git", *args], cwd=cwd or ROOT,
                                      stderr=subprocess.STDOUT, text=True)
        return out
    except subprocess.CalledProcessError as e:
        return e.output
    except FileNotFoundError:
        return ""


def recent_commits(n: int = 15) -> list[dict]:
    raw = run_git("log", f"--pretty=format:%H|%aI|%s", f"-{n}")
    out = []
    for line in raw.splitlines():
        if "|" not in line:
            continue
        sha, iso, subject = line.split("|", 2)
        out.append({"sha": sha[:8], "date": iso[:19], "subject": subject})
    return out


def git_last_touched(rel_path: str) -> str | None:
    out = run_git("log", "-1", "--pretty=format:%aI", "--", rel_path)
    return out.strip() or None


# --------------------- analyses ---------------------

def state_files_audit() -> list[dict]:
    """For each tracked state file, report last-git-touch vs declared Last-Updated."""
    findings = []
    targets = [
        ("02_CASES/GLOBAL_PROJECT_STATE.md", r"\*\*Last Updated:\*\*\s*(\d{4}-\d{2}-\d{2})"),
    ]
    for case in (ROOT / "02_CASES").glob("Case_*"):
        targets.append((str(case.relative_to(ROOT)) + "/PROJECT_STATE.md",
                        r"\*\*Last Updated:\*\*\s*(\d{4}-\d{2}-\d{2})"))
    for rel, pat in targets:
        p = ROOT / rel
        if not p.exists():
            continue
        declared = None
        for line in p.read_text(encoding="utf-8").splitlines()[:20]:
            m = re.search(pat, line)
            if m:
                declared = m.group(1)
                break
        git_iso = git_last_touched(rel)
        git_date = git_iso[:10] if git_iso else None
        if declared and git_date and declared < git_date:
            gap = (dt.date.fromisoformat(git_date) - dt.date.fromisoformat(declared)).days
            findings.append({
                "path": rel,
                "declared": declared,
                "git_last_touched": git_date,
                "drift_days": gap,
                "severity": "high" if gap > 7 else "medium",
            })
    return findings


def global_state_lists_commits() -> list[str]:
    """Cross-reference commit subjects with the case sections in GLOBAL."""
    p = ROOT / "02_CASES" / "GLOBAL_PROJECT_STATE.md"
    if not p.exists():
        return []
    text = p.read_text(encoding="utf-8")
    # crude: find the "Case X:" header blocks and grab the lines that look like
    # status indicators (✅ / ⛔ / ❌)
    return re.findall(r"Case[^\n]*[\u2705\u26D4\u274C\u2B50][^\n]*", text)


def hardcoded_paths_in_state() -> list[str]:
    """Detect outdated main-repo path references that the README warned about."""
    findings = []
    patterns = [
        ("01_IMPLEMENTATION_TOOLS/", "main-repo path not in compact"),
        ("01_PHASE1_CONTEXT_RICH", "typo of 01_PHASE1_CONTEXT_RICH (correct in compact)"),
    ]
    for case_md in (ROOT / "02_CASES").rglob("*.md"):
        try:
            text = case_md.read_text(encoding="utf-8")
        except Exception:
            continue
        for needle, why in patterns:
            if needle in text:
                findings.append(f"{case_md.relative_to(ROOT)}: contains `{needle}` — {why}")
    return findings


def progress_json_consistency() -> list[str]:
    """Flag progress.json files whose 'current_phase' disagrees with the
    status of the highest-numbered phase folder."""
    findings = []
    for case_dir in sorted((ROOT / "02_CASES").glob("Case_*")):
        pj = case_dir / "progress.json"
        if not pj.exists():
            continue
        try:
            d = json.loads(pj.read_text(encoding="utf-8"))
        except Exception:
            continue
        declared = int(d.get("phase") or 0)
        # find highest phase folder present
        present = []
        for child in case_dir.iterdir():
            m = re.match(r"(\d{2})_PHASE\d+", child.name)
            if m:
                present.append(int(m.group(1)))
        if not present:
            continue
        max_present = max(present)
        if max_present != declared:
            findings.append(
                f"{case_dir.name}/progress.json: declared phase {declared} but highest "
                f"phase folder is {max_present:02d} ({[c.name for c in case_dir.iterdir() if c.name.startswith(f'{max_present:02d}_')][0]})"
            )
    return findings


# --------------------- rendering ---------------------

def render(*, commits: list[dict], drift: list[dict],
           hardcoded: list[str], progress_issues: list[str]) -> str:
    today = dt.date.today().isoformat()
    lines = [
        f"# Reconciliation — git vs state files",
        "",
        f"_Generated {today} by `scripts/dream/reconcile.py` — deterministic._",
        "",
        "## Recent commits (last 15)",
        "",
        "| Date | SHA | Subject |",
        "|---|---|---|",
    ]
    for c in commits:
        lines.append(f"| {c['date']} | `{c['sha']}` | {c['subject']} |")

    lines += ["", "## State files behind git",
              "",
              "_`PROJECT_STATE.md` declares an older date than the last git touch._",
              ""]
    if drift:
        lines.append("| File | Declared | Last git touch | Drift |")
        lines.append("|---|---|---|---|")
        for f in drift:
            lines.append(f"| {f['path']} | {f['declared']} | {f['git_last_touched']} | **{f['drift_days']}d ({f['severity']})** |")
    else:
        lines.append("_None this cycle._")

    lines += ["", "## Hardcoded main-repo paths still referenced",
              "",
              "_These will mislead any agent reading case docs as canonical._",
              ""]
    if hardcoded:
        for h in hardcoded:
            lines.append(f"- {h}")
    else:
        lines.append("_None detected._")

    lines += ["", "## progress.json vs phase folder consistency",
              ""]
    if progress_issues:
        for p in progress_issues:
            lines.append(f"- {p}")
    else:
        lines.append("_All progress.json current_phase fields match the highest phase folder._")

    lines += ["", "## Proposed state-file patches (never auto-applied — P7)",
              "",
              "_For each drift item, the proposed edit is to bump the `Last Updated` "
              "header on the affected `PROJECT_STATE.md` to the last git-touch date, "
              "and add a one-line summary of the commits that changed the file since._",
              ""]
    if drift:
        for f in drift:
            lines.append(f"### {f['path']}")
            lines.append("")
            lines.append("```diff")
            lines.append(f"- **Last Updated:** {f['declared']}")
            lines.append(f"+ **Last Updated:** {f['git_last_touched']}  "
                         f"(bumps: {f['drift_days']}d of drift since last state bump)")
            lines.append("+ **Drift note:** run `git log --since=" + f['declared'] + " -- "
                         + f['path'] + "` and summarise in the appropriate status table.")
            lines.append("```")
            lines.append("")
    else:
        lines.append("_No state-file patches proposed this cycle._")

    lines += ["", "---", "", "_Re-run after each `git push` to keep this current._"]
    return "\n".join(lines) + "\n"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", default=str(ROOT / "dream" / "RECONCILIATION.md"))
    args = p.parse_args()

    if not (ROOT / ".git").exists():
        print("reconcile: no .git at repo root — skipping", file=sys.stderr)
        return 1

    commits = recent_commits()
    drift = state_files_audit()
    hardcoded = hardcoded_paths_in_state()
    progress_issues = progress_json_consistency()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(commits=commits, drift=drift, hardcoded=hardcoded,
                          progress_issues=progress_issues), encoding="utf-8")
    print(f"reconcile: wrote {out} (drift={len(drift)}, hardcoded={len(hardcoded)}, "
          f"progress_issues={len(progress_issues)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
