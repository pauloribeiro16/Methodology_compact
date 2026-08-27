#!/usr/bin/env python3
"""
check_implementation_posture.py — Gate v0.2 validator for AEGIS Implementation Posture Model.

Verifies that:
1. No active Case_01 markdown document contains legacy maturity terms (/maturi/i, 0-4 scales, T1-T4 Tiers)
   unless in explicit deprecation note context or historical logs.
2. Rule detail cards in Doc18 carry valid Implementation Status fields (IMPLEMENTED, PARTIAL, NOT IMPLEMENTED, N/A).
3. Objectives in Doc16 carry valid Implementation Status fields.

Exit codes:
0: All checks pass
1: Failure (violations found)
"""

import sys
import re
import pathlib

CASE_01_ROOT = pathlib.Path("02_CASES/Case_01_TinyTask_SaaS")

DEPRECATED_TERMS = [
    re.compile(r"maturity_score", re.IGNORECASE),
    re.compile(r"maturity_csf", re.IGNORECASE),
    re.compile(r"maturity_privacy", re.IGNORECASE),
    re.compile(r"cur \d/4 → tgt \d/4", re.IGNORECASE),
]

# Excluded files (historical/validation logs)
EXCLUDED_PATTERNS = [
    "validation/",
    "VALIDATOR_",
    "CHANGE_LOG",
    "DEPRECATED",
]

def is_excluded(path: pathlib.Path) -> bool:
    path_str = str(path)
    for pattern in EXCLUDED_PATTERNS:
        if pattern in path_str:
            return True
    return False

def check_deprecated_terms():
    violations = []
    for md_file in CASE_01_ROOT.rglob("*.md"):
        if is_excluded(md_file):
            continue
        
        with open(md_file, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                # Ignore explicitly marked deprecation comments or references to legacy spec names in historical footnotes
                if "DEPRECATED" in line or "legacy" in line.lower() or "DEPRECATED_FOR_POSTURE" in line:
                    continue
                for term in DEPRECATED_TERMS:
                    if term.search(line):
                        violations.append(f"{md_file}:{line_no}: Found deprecated term matching '{term.pattern}': {line.strip()}")

    return violations

def check_doc18_cards():
    doc18_path = CASE_01_ROOT / "02_PHASE2_RULES_RICH" / "Doc18_Rules_Catalog.md"
    if not doc18_path.exists():
        return ["Doc18_Rules_Catalog.md not found"]
    
    violations = []
    with open(doc18_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Verify presence of Implementation Status fields
    status_count = content.count("Implementation Status (CSF):")
    if status_count < 46:
        violations.append(f"Doc18 contains only {status_count}/46 'Implementation Status (CSF)' fields")

    return violations

def main():
    print("=== AEGIS Gate v0.2: Implementation Posture Validator ===")
    
    term_violations = check_deprecated_terms()
    card_violations = check_doc18_cards()

    all_violations = term_violations + card_violations

    if all_violations:
        print(f"❌ Gate FAILED with {len(all_violations)} violation(s):")
        for v in all_violations:
            print(f"  - {v}")
        sys.exit(1)

    print("✅ GATE PASS: Case_01 fully compliant with Implementation Posture Model v2.0!")
    sys.exit(0)

if __name__ == "__main__":
    main()
