#!/usr/bin/env python3
"""
rename_lane_ids.py — LANE NAMING campaign (v1.0)

Renames UC ids to lane ids (PROC-NN / CAP-NN) per the mapping tables in
00_METHODOLOGY/validation/LANE_NAMING_CENSUS_v0.md (registry), per the human
decision of 2026-09-05: UC-* reserved for the TECHNOLOGY lane.

Usage:
  python3 scripts/rename_lane_ids.py <case> --dry-run     # default: dry-run
  python3 scripts/rename_lane_ids.py <case> --apply

Cases: Case_01 | Case_02 | Case_03  (mapping JSONs in scripts/lane_mappings/)

Safety:
  * exact-id replacement only (regex word boundaries; longest-first ordering so
    UC-1 never matches inside UC-10);
  * dotted ids (U.C.1.1.1) escaped literally;
  * wildcards (U.C.8.1.*) untouched — they belong to TECHNOLOGY packages;
  * per-file replacement report; never touches .git, kg, 00_VISUALISATIONS.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MAPS = REPO / "scripts" / "lane_mappings"

CASES = {
    "Case_01": {
        "dir": REPO / "02_CASES" / "Case_01_TinyTask_SaaS" / "03_PHASE3_DECOMPOSITION_RICH",
        "extra": [REPO / "02_CASES" / "Case_01_TinyTask_SaaS" / "03_PHASE3_DECOMPOSITION_RICH" / "scripts"],
    },
    "Case_02": {"dir": REPO / "02_CASES" / "Case_02_SecureBorder_Solutions" / "03_PHASE3_DECOMPOSITION", "extra": []},
    "Case_03": {"dir": REPO / "02_CASES" / "Case_03_OmniBank_Financial" / "03_PHASE3_DECOMPOSITION", "extra": []},
}


def load_mapping(case):
    m = json.loads((MAPS / f"{case}.json").read_text(encoding="utf-8"))
    mapping = m["mapping"]  # old -> new
    # longest-first to avoid prefix collisions
    ordered = sorted(mapping.items(), key=lambda kv: -len(kv[0]))
    return mapping, ordered


def build_patterns(ordered):
    pats = []
    for old, new in ordered:
        esc = re.escape(old)
        # word boundary: not preceded/followed by an id character (alnum, dot, dash, underscore)
        pat = re.compile(r"(?<![A-Za-z0-9._\-])" + esc + r"(?![A-Za-z0-9_\-])")
        pats.append((pat, new))
    return pats


def iter_files(case_cfg):
    for f in sorted(case_cfg["dir"].rglob("*.md")):
        yield f
    for d in case_cfg.get("extra", []):
        if d.exists():
            for f in sorted(d.rglob("*.py")):
                yield f
            for f in sorted(d.rglob("*.json")):
                yield f


def main():
    case = sys.argv[1] if len(sys.argv) > 1 else ""
    apply = "--apply" in sys.argv
    if case not in CASES:
        raise SystemExit(f"usage: rename_lane_ids.py <Case_01|Case_02|Case_03> [--apply]")
    mapping, ordered = load_mapping(case)
    pats = build_patterns(ordered)
    cfg = CASES[case]
    total = 0
    files_changed = 0
    for f in iter_files(cfg):
        if not f.is_file():
            continue  # broken symlinks / odd entries
        try:
            text = f.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        new_text = text
        count = 0
        for pat, new in pats:
            new_text, n = pat.subn(new, new_text)
            count += n
        if count:
            rel = f.relative_to(REPO)
            if apply:
                f.write_text(new_text, encoding="utf-8")
            print(f"{'APPLY' if apply else 'DRY  '} {rel}: {count} replacements")
            total += count
            files_changed += 1
    print(f"---\n{case}: {total} replacements across {files_changed} files "
          f"({'APPLIED' if apply else 'DRY-RUN — use --apply to write'})")
    # verify: no leftover old ids in md (excluding the census/history registry itself)
    leftovers = 0
    for f in iter_files(cfg):
        if not f.is_file():
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if apply:
            for old in mapping:
                if re.search(r"(?<![A-Za-z0-9._\-])" + re.escape(old) + r"(?![A-Za-z0-9_\-])", text):
                    print(f"LEFTOVER: {f.relative_to(REPO)} still contains {old}")
                    leftovers += 1
    if apply:
        sys.exit(1 if leftovers else 0)


if __name__ == "__main__":
    main()
