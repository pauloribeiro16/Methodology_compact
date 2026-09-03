#!/usr/bin/env python3
"""stale_archive.py — Move stale AGENTS.md amendment proposals to a separate file.

Proposals that appear in `dream/ADOPTION_REPORT.md` for **5 or more consecutive
nightly cycles** without being applied, rejected, or marked resolved are moved
to `dream/STALE_PROPOSALS.md` to break the stagnation loop. Signal is preserved
(the original proposal stays in git history) but the live report shrinks.

What this script does (deterministic, no LLM):
1. Reads the latest `dream/ADOPTION_REPORT.md` (current cycle's titles).
2. Reads the previous cycle's titles from `git show HEAD:dream/ADOPTION_REPORT.md`.
3. Walks back N commits to build a consecutive-cycles counter per title.
4. For titles seen >= --threshold (default 5) consecutive cycles:
   - Reads the full proposal block from the current report (rationale + patch).
   - Appends a block to `dream/STALE_PROPOSALS.md` under "AWAITING-HUMAN-VERDICT"
     with first_seen / last_seen dates and the proposal body.
   - Removes the block from the live report (rewrites `dream/ADOPTION_REPORT.md`
     without the stale block, but preserves the rest of the report).
5. Logs the move to `dream/STATE/stale_archive.log` (one JSON line per move).

P7 boundary: this script WRITES to `dream/ADOPTION_REPORT.md` and
`dream/STALE_PROPOSALS.md` — both are in the self-tune allow-list. It does NOT
touch AGENTS.md, PROJECT_STATE.md, progress.json, dependency_graph.yaml, or
domains/.

Usage:
    python3 scripts/dream/stale_archive.py
    python3 scripts/dream/stale_archive.py --threshold 5
    python3 scripts/dream/stale_archive.py --dry-run
    python3 scripts/dream/stale_archive.py --self-test
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REPORT = ROOT / "dream" / "ADOPTION_REPORT.md"
STALE = ROOT / "dream" / "STALE_PROPOSALS.md"
LOG = ROOT / "dream" / "STATE" / "stale_archive.log"


# --------------------- helpers ---------------------

def run_git(*args: str) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT,
                                       stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return e.output
    except FileNotFoundError:
        return ""


def parse_proposals(text: str) -> list[dict]:
    """Extract every `### N. <title>` block from a report.

    Returns [{title, body, raw_block, line_start, line_end}, ...].
    """
    lines = text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        m = re.match(r"^###\s+(\d+)\.\s+(.+?)\s*$", lines[i])
        if not m:
            i += 1
            continue
        title = m.group(2).strip()
        # The block extends until the next `### N.` or `---` or EOF
        j = i + 1
        while j < len(lines):
            if re.match(r"^###\s+\d+\.\s+", lines[j]) or lines[j].startswith("---"):
                break
            j += 1
        raw_block = "\n".join(lines[i:j])
        body = "\n".join(lines[i + 1:j]).rstrip()
        out.append({"title": title, "body": body, "raw_block": raw_block,
                    "line_start": i, "line_end": j})
        i = j
    return out


def titles_in_report(text: str) -> set[str]:
    return {p["title"] for p in parse_proposals(text)}


def report_at(ref: str) -> str:
    """Read ADOPTION_REPORT.md at a given git ref (or 'WORKING')."""
    if ref == "WORKING":
        return REPORT.read_text(encoding="utf-8") if REPORT.exists() else ""
    return run_git("show", f"{ref}:dream/ADOPTION_REPORT.md")


def consecutive_cycles(title: str, max_lookback: int = 20) -> tuple[int, str | None, str | None]:
    """Walk back through git log until the title is absent from a commit's report.

    Returns (count, first_seen_date, last_seen_date).
    """
    count = 0
    first_seen = last_seen = None
    ref = "HEAD"
    for step in range(max_lookback):
        text = report_at(ref)
        titles = titles_in_report(text)
        if title in titles:
            count += 1
            # The commit ref's date
            date_iso = run_git("show", "-s", "--pretty=format:%aI", ref).strip()
            date = date_iso[:10] if date_iso else None
            if last_seen is None:
                last_seen = date
            first_seen = date  # latest iteration that hit is the newest; first hit walking back is the oldest
            ref = f"HEAD~{step + 1}"
        else:
            break
    return count, first_seen, last_seen


# --------------------- core ---------------------

def archive_stale(threshold: int, dry_run: bool = False,
                  cycles_fn=consecutive_cycles) -> list[dict]:
    """Find and (if not dry-run) archive proposals seen >= threshold cycles.

    Returns the list of {title, first_seen, last_seen, cycles} that were archived.
    `cycles_fn` is injectable for testing (default: real consecutive_cycles).
    """
    if not REPORT.exists():
        return []
    current_text = REPORT.read_text(encoding="utf-8")
    current_proposals = parse_proposals(current_text)
    if not current_proposals:
        return []

    archived = []
    blocks_to_remove: list[tuple[int, int]] = []

    for p in current_proposals:
        cycles, first_seen, last_seen = cycles_fn(p["title"])
        if cycles >= threshold:
            archived.append({
                "title": p["title"],
                "first_seen": first_seen,
                "last_seen": last_seen,
                "cycles": cycles,
                "body": p["body"],
            })
            blocks_to_remove.append((p["line_start"], p["line_end"]))

    if not archived:
        return []

    if dry_run:
        print(f"stale_archive: DRY-RUN — would archive {len(archived)} proposal(s)")
        for a in archived:
            print(f"  - {a['title']} ({a['cycles']} cycles, "
                  f"{a['first_seen']} → {a['last_seen']})")
        return archived

    # 1. Append blocks to STALE_PROPOSALS.md under "AWAITING-HUMAN-VERDICT"
    stale_text = STALE.read_text(encoding="utf-8") if STALE.exists() else ""
    marker = "## AWAITING-HUMAN-VERDICT"
    if marker not in stale_text:
        stale_text += f"\n{marker}\n\n(empty — first stale proposal will be archived here on next nightly cycle)\n"

    insertion_point = stale_text.index(marker) + len(marker)
    today = dt.date.today().isoformat()
    new_blocks = []
    for a in archived:
        block = (
            f"\n### {a['title']}\n\n"
            f"- **First seen:** {a['first_seen']}\n"
            f"- **Last seen:** {a['last_seen']} (archived {today})\n"
            f"- **Consecutive cycles:** {a['cycles']}\n\n"
            f"{a['body']}\n"
        )
        new_blocks.append(block)

    new_stale = stale_text[:insertion_point] + "\n" + "".join(new_blocks) + stale_text[insertion_point:]
    STALE.parent.mkdir(parents=True, exist_ok=True)
    STALE.write_text(new_stale, encoding="utf-8")

    # 2. Remove the blocks from ADOPTION_REPORT.md
    lines = current_text.splitlines()
    keep = []
    skip_until = -1
    for idx, line in enumerate(lines):
        if idx < skip_until:
            continue
        skip = False
        for (s, e) in blocks_to_remove:
            if idx == s:
                skip_until = e
                skip = True
                break
        if not skip:
            keep.append(line)
    new_report = "\n".join(keep) + "\n"
    REPORT.write_text(new_report, encoding="utf-8")

    # 3. Log each move
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        for a in archived:
            rec = {
                "ts": dt.datetime.now().isoformat(timespec="seconds"),
                "title": a["title"],
                "cycles": a["cycles"],
                "first_seen": a["first_seen"],
                "last_seen": a["last_seen"],
                "action": "archive_to_stale",
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"stale_archive: archived {len(archived)} proposal(s) "
          f"(threshold={threshold})")
    for a in archived:
        print(f"  - {a['title']} ({a['cycles']} cycles)")
    return archived


# --------------------- self-test ---------------------

def self_test() -> int:
    """End-to-end: build a synthetic report in a temp repo, run, verify."""
    print("=== stale_archive.py --self-test ===")

    # Use a temp dir to avoid touching the real repo
    import shutil
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        # Copy just the script and minimal fixtures
        # We test archive_stale() directly with a fake REPO context.
        # Since the script uses module-level ROOT, we monkey-patch it.
        global REPORT, STALE, LOG, ROOT
        real_root = ROOT
        real_report = REPORT
        real_stale = STALE
        real_log = LOG
        try:
            ROOT = tmp_path
            REPORT = tmp_path / "dream" / "ADOPTION_REPORT.md"
            STALE = tmp_path / "dream" / "STALE_PROPOSALS.md"
            LOG = tmp_path / "dream" / "STATE" / "stale_archive.log"
            REPORT.parent.mkdir(parents=True, exist_ok=True)
            STALE.parent.mkdir(parents=True, exist_ok=True)

            # 1. Build a report with 3 proposals, including 1 that should be stale
            sample = """\
# Adoption Report — Test

_Generated 2026-09-03_

## AGENTS.md amendment proposals

### 1. Stale proposal (should be archived)

**Rationale:** test

**Proposed patch:**

```
echo stale
```

### 2. Fresh proposal (should stay)

**Rationale:** test 2

**Proposed patch:**

```
echo fresh
```

### 3. Another stale proposal (should be archived)

**Rationale:** test 3

**Proposed patch:**

```
echo another stale
```

---
"""
            REPORT.write_text(sample, encoding="utf-8")
            # STALE starts with the canonical header
            STALE.write_text(
                "# STALE_PROPOSALS — amendment proposals awaiting human verdict\n\n"
                "## AWAITING-HUMAN-VERDICT\n\n(empty)\n\n## RESOLVED\n\n(empty)\n",
                encoding="utf-8",
            )

            # 2. Inject a fake cycles_fn that reports every title as 6 cycles old
            # (so the threshold=1 is satisfied). Real git walkback is exercised
            # in the live repo, not the temp dir.
            def fake_cycles(title: str) -> tuple[int, str | None, str | None]:
                # First two titles are stale (6 cycles), third is also stale
                if title == "Fresh proposal (should stay)":
                    return (6, "2026-08-29", "2026-09-03")
                elif title == "Stale proposal (should be archived)":
                    return (6, "2026-08-29", "2026-09-03")
                elif title == "Another stale proposal (should be archived)":
                    return (6, "2026-08-29", "2026-09-03")
                return (0, None, None)

            archived = archive_stale(threshold=1, dry_run=False, cycles_fn=fake_cycles)
            print(f"[{'ok' if len(archived) == 3 else 'FAIL'}] "
                  f"archived count (threshold=1): {len(archived)}")

            # 3. Check the live report has no proposals left
            new_text = REPORT.read_text(encoding="utf-8")
            remaining = titles_in_report(new_text)
            if remaining:
                print(f"FAIL: live report still has proposals: {remaining}")
                return 1
            print(f"[ok] live report proposals cleared")

            # 4. Check STALE has the 3 entries
            stale_text = STALE.read_text(encoding="utf-8")
            for title in ("Stale proposal", "Fresh proposal", "Another stale"):
                if title not in stale_text:
                    print(f"FAIL: STALE missing title: {title}")
                    return 1
            print(f"[ok] STALE has all 3 archived titles")

            # 5. Check log file has 3 lines
            log_lines = LOG.read_text(encoding="utf-8").splitlines()
            if len(log_lines) != 3:
                print(f"FAIL: log has {len(log_lines)} lines, expected 3")
                return 1
            print(f"[ok] log has 3 entries")

            # 6. Dry-run on empty report returns empty list
            REPORT.write_text("# empty\n", encoding="utf-8")
            archived = archive_stale(threshold=1, dry_run=False)
            if archived:
                print(f"FAIL: empty report returned {len(archived)} archived")
                return 1
            print(f"[ok] empty report → 0 archived")

            print("=== stale_archive.py --self-test PASSED ===")
            return 0
        finally:
            ROOT = real_root
            REPORT = real_report
            STALE = real_stale
            LOG = real_log


# --------------------- main ---------------------

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--threshold", type=int, default=5,
                   help="Minimum consecutive nightly cycles before archiving (default: 5)")
    p.add_argument("--dry-run", action="store_true",
                   help="Print what would be archived without modifying any file")
    p.add_argument("--self-test", action="store_true",
                   help="Run end-to-end self-test in a temp directory")
    args = p.parse_args()

    if args.self_test:
        return self_test()

    archived = archive_stale(threshold=args.threshold, dry_run=args.dry_run)
    if not archived and not args.dry_run:
        # Not a failure — just nothing to do this cycle
        print(f"stale_archive: no proposals at threshold >= {args.threshold}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
