#!/usr/bin/env python3
"""rename_case_files.py — AEGIS Methodology_compact .md rename inside case phases.

Convention (decided by the user 2026-08-26):
  - Deliverables (docs with NN_ or NNx_ prefix): renumbered Doc01..DocNN,
    zero-padded, continuous per case (P1 -> P2 -> P3). PascalCase
    underscores; acronyms (NIST, KG, RICH, CORPUS, CIA) kept in caps.
  - Operational files (governance/validation, UPPER or lowercase, no
    prefix): PascalCase underscores, no Doc prefix.
  - README.md: kept as-is.
  - lint_report_phase3[_rich]_*.md: skipped (auto-generated timestamped
    outputs; snapshot is the safety net).

Usage:
  python3 scripts/rename_case_files.py plan          # write mapping TSV to
                                                   # dream/RENAME_MAPPING.tsv
  python3 scripts/rename_case_files.py apply        # read the TSV and run
                                                   # git mv per line

Idempotent: re-running plan overwrites the TSV; re-running apply skips
entries whose source no longer exists.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "02_CASES"
MAPPING_TSV = ROOT / "dream" / "RENAME_MAPPING.tsv"

# Phase dir roots per case (regex; matches 01_PHASE1_CONTEXT_RICH,
# 02_PHASE2_RULES_RICH, 03_PHASE3_DECOMPOSITION[_RICH]).
PHASE_DIR_RE = re.compile(r"^(\d{2})_PHASE\d+(_[A-Z_]+)$")

# Acronyms kept in upper case inside PascalCase.
ACRONYMS = {"NIST", "KG", "RICH", "CORPUS", "CIA", "DORA", "NIS", "NIS2",
            "CRA", "GDPR", "AI", "AIACT", "QNRCS", "AM", "PM",
            "RACI", "PHASE", "ID", "DOC", "DOCS", "JSON",
            "TEMPLATE", "TEMPLATES", "INDEX"}

# Files that should never be renamed.
SKIP_BASENAMES = {"README.md"}  # lint_report_* matched by suffix below

# Files excluded by suffix (auto-generated lint reports).
LINT_SUFFIX = re.compile(r"^lint_report_phase3(_rich)?_\d{8}_\d{6}\.md$")

# Files classified as operational (PascalCase without Doc prefix).
# These UPPER/lowercase basenames are detected by the absence of an NN_
# prefix. The script then converts to PascalCase_underscore. See
# to_pascal() for the conversion rule.

# Deliverables: basename starts with NN_ or NNx_ (digits + letter optional)
DELIVERABLE_RE = re.compile(r"^(\d{2})([a-z]?)_(.+)\.md$")


def pascal_token(tok: str) -> str:
    """Capitalize a token, keeping acronym all-upper-case.

    Heuristic: if the token is already all-upper and length >= 2, keep it.
    Otherwise, title-case the first letter only and lowercase the rest.
    Multi-word tokens split by inner case ('DocID' -> 'DocId') are
    normalised; single-token lowercase ('tinytask' -> 'Tinytask').
    """
    if not tok:
        return tok
    # If entirely upper and short, treat as acronym.
    if tok.isupper() and tok in ACRONYMS:
        return tok
    if tok.isupper():
        return tok  # unknown acronym: keep caps
    # If contains inner uppercase (CamelCase): split on case boundary.
    parts = re.findall(r"[A-Z][a-z0-9]+|[A-Z]+(?=[A-Z]|$)|[a-z0-9]+", tok) or [tok]
    return "".join(p[:1].upper() + p[1:] for p in parts)


def to_pascal(basename: str) -> str:
    """Convert 'UPPER_SNAKE.md' or 'lower_snake.md' to 'Pascal_Snake.md'."""
    stem = basename[:-3]  # strip .md
    tokens = stem.split("_")
    return "_".join(pascal_token(t) for t in tokens) + ".md"


def case_key(case_dir: Path) -> str:
    """Sortable case name (e.g. 'Case_01')."""
    return case_dir.name


def phase_order_key(phase_dir_name: str) -> tuple[int, str]:
    """Sortable (phase_num, full_name). Phase 1 < 2 < 3."""
    m = PHASE_DIR_RE.match(phase_dir_name)
    if m:
        return (int(m.group(1)), phase_dir_name)
    return (99, phase_dir_name)


def discover_renames(cases_dir: Path) -> tuple[list[tuple[str, str, str, str]], dict]:
    """Return (moves, stats).

    Each move is (old_relpath, new_relpath, family, new_basename).
    Stats is a counter dict for the report.
    """
    moves: list[tuple[str, str, str, str]] = []
    stats: dict[str, int] = {
        "deliverable_renumbered": 0,
        "operational_pascal": 0,
        "skipped_readme": 0,
        "skipped_lint": 0,
        "skipped_already_compliant": 0,
        "skipped_old_equal_new": 0,
    }
    # Per-case deliverable counter
    counters: dict[str, int] = {}

    case_dirs = sorted([d for d in cases_dir.iterdir() if d.is_dir() and d.name.startswith("Case_")],
                       key=case_key)

    for case_dir in case_dirs:
        case_name = case_dir.name
        counters[case_name] = 0
        # Phase directories inside the case
        phase_dirs = sorted(
            [d for d in case_dir.iterdir() if d.is_dir() and PHASE_DIR_RE.match(d.name)],
            key=lambda d: phase_order_key(d.name),
        )
        for phase_dir in phase_dirs:
            for md_path in sorted(phase_dir.rglob("*.md")):
                if not md_path.is_file():
                    continue
                rel = md_path.relative_to(ROOT)
                base = md_path.name

                if base == "README.md":
                    stats["skipped_readme"] += 1
                    continue
                if LINT_SUFFIX.match(base):
                    stats["skipped_lint"] += 1
                    continue

                # Deliverable: NN_ or NNx_
                m = DELIVERABLE_RE.match(base)
                if m:
                    counters[case_name] += 1
                    doc_num = f"{counters[case_name]:02d}"
                    # Convert the stem part (post NN_) via to_pascal logic.
                    raw_rest = m.group(3)  # text after "NN_"
                    # Re-derive new_basename by reusing to_pascal on a
                    # synthetic full basename; to_pascal strips ".md" so
                    # we feed "RAW_REST.md".
                    new_basename = f"Doc{doc_num}_{to_pascal(raw_rest + '.md')}"
                    new_rel = str(md_path.parent.relative_to(ROOT) / new_basename)
                    if new_basename == base:
                        stats["skipped_old_equal_new"] += 1
                        continue
                    moves.append((str(rel), new_rel, "deliverable", new_basename))
                    stats["deliverable_renumbered"] += 1
                    continue

                # Otherwise: UPPER or lowercase without prefix. PascalCase.
                # If already in the new style (PascalCase_underscore.md),
                # skip.
                if re.match(r"^[A-Z][a-zA-Z0-9_]*\.md$", base):
                    # Looks already PascalCase; skip only if all words are
                    # proper tokens. We still apply to_pascal and check
                    # equality.
                    pass
                new_basename = to_pascal(base)
                if new_basename == base:
                    stats["skipped_already_compliant"] += 1
                    continue
                new_rel = str(md_path.parent.relative_to(ROOT) / new_basename)
                moves.append((str(rel), new_rel, "operational", new_basename))
                stats["operational_pascal"] += 1

    return moves, stats


def write_mapping_tsv(moves: list[tuple[str, str, str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("old_path\tnew_path\tfamily\tnew_basename\n")
        for old, new, fam, base in moves:
            f.write(f"{old}\t{new}\t{fam}\t{base}\n")


def apply_mapping(moves: list[tuple[str, str, str, str]], repo_root: Path) -> tuple[int, int]:
    """Apply git mv per line. Returns (applied, skipped)."""
    applied = skipped = 0
    for old, new, _, _ in moves:
        old_abs = repo_root / old
        new_abs = repo_root / new
        if not old_abs.exists():
            skipped += 1
            continue
        if new_abs.exists():
            print(f"  SKIP (target exists): {old} -> {new}", file=sys.stderr)
            skipped += 1
            continue
        # git mv needs the new path to be in the same directory for git
        # to recognise as a rename (not delete+add).
        new_dir = new_abs.parent
        subprocess.run(["git", "mv", str(old_abs), str(new_abs)],
                       cwd=repo_root, check=True)
        applied += 1
    return applied, skipped


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", choices=["plan", "apply"], help="plan: write mapping; apply: git mv per line")
    args = p.parse_args()

    if not CASES.exists():
        print(f"rename_case_files: no 02_CASES at {CASES}", file=sys.stderr)
        return 1

    moves, stats = discover_renames(CASES)

    if args.command == "plan":
        write_mapping_tsv(moves, MAPPING_TSV)
        print(f"rename_case_files: wrote {MAPPING_TSV} ({len(moves)} moves)")
        for k, v in stats.items():
            print(f"  {k}: {v}")
        return 0

    # apply
    if not MAPPING_TSV.exists():
        print(f"rename_case_files: no mapping at {MAPPING_TSV}; run 'plan' first", file=sys.stderr)
        return 1
    moves_from_tsv: list[tuple[str, str, str, str]] = []
    with open(MAPPING_TSV, encoding="utf-8") as f:
        next(f)  # header
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 4:
                moves_from_tsv.append(tuple(parts[:4]))  # type: ignore
    applied, skipped = apply_mapping(moves_from_tsv, ROOT)
    print(f"rename_case_files: applied={applied} skipped={skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
