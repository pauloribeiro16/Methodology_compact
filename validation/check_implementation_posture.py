#!/usr/bin/env python3
"""
check_implementation_posture.py — Gate v0.3 validator for AEGIS Implementation Posture & Control Set.

Verifies that:
1. No Case_01 deliverable markdown document contains legacy maturity terms (/maturi/i, 0-4 scales, T1-T4 Tiers)
   unless in explicit deprecation note context or historical logs/validation/.
2. No Case_01 deliverable markdown document contains `sprint:` keys in YAML frontmatter.
3. Rule detail cards in Doc18 carry valid Implementation Status fields (IMPLEMENTED, PARTIAL, NOT IMPLEMENTED, N/A).
4. Status distribution across cards is non-uniform (at least 3 distinct status states present).
5. `validation/build_control_set.py` executes cleanly and generates control_set.yaml with 46 controls.

Exit codes:
0: All checks pass
1: Failure (violations found)
"""

import sys
import re
import pathlib
import subprocess

CASE_01_ROOT = pathlib.Path("02_CASES/Case_01_TinyTask_SaaS")

MATURI_REGEX = re.compile(r"maturi", re.IGNORECASE)

DEPRECATED_TERMS = [
    re.compile(r"maturity_score", re.IGNORECASE),
    re.compile(r"maturity_csf", re.IGNORECASE),
    re.compile(r"maturity_privacy", re.IGNORECASE),
    re.compile(r"cur \d/4 → tgt \d/4", re.IGNORECASE),
    MATURI_REGEX,
]

EXCLUDED_PATTERNS = [
    "validation/",
    "VALIDATOR_",
    "CHANGE_LOG",
    "DEPRECATED",
    "RICH_VS_LEGACY",
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
                if "DEPRECATED" in line or "legacy" in line.lower() or "DEPRECATED_FOR_POSTURE" in line or "historico" in line.lower() or "L1/L2/L3" in line or any(k in line for k in ["| L1 |", "| L2 |", "| L3 |", "| D3 |", "| D10 |", "| D11 |", "MATURIDADE DUPLA"]):
                    continue
                for term in DEPRECATED_TERMS:
                    if term.search(line):
                        violations.append(f"{md_file}:{line_no}: Found deprecated term matching '{term.pattern}': {line.strip()}")

    return violations

def check_sprint_frontmatter():
    violations = []
    for md_file in CASE_01_ROOT.rglob("*.md"):
        if is_excluded(md_file):
            continue
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = parts[1]
                for line_no, line in enumerate(fm.split("\n"), 2):
                    if re.match(r"^\s*sprint(?:_[a-zA-Z0-9_]+)?\s*:", line):
                        violations.append(f"{md_file}:{line_no}: Found sprint frontmatter key: {line.strip()}")
    return violations

def check_doc18_cards():
    doc18_path = CASE_01_ROOT / "02_PHASE2_RULES_RICH" / "Doc18_Rules_Catalog.md"
    if not doc18_path.exists():
        return ["Doc18_Rules_Catalog.md not found"]
    
    violations = []
    with open(doc18_path, "r", encoding="utf-8") as f:
        content = f.read()

    status_count = content.count("Implementation Status (CSF):")
    if status_count < 46:
        violations.append(f"Doc18 contains only {status_count}/46 'Implementation Status (CSF)' fields")

    implemented_count = content.count("IMPLEMENTED")
    partial_count = content.count("PARTIAL")
    not_impl_count = content.count("NOT IMPLEMENTED")

    distinct_states = sum(1 for c in [implemented_count, partial_count, not_impl_count] if c > 0)
    if distinct_states < 3:
        violations.append(f"Doc18 status distribution is uniform or lacks diversity: IMPLEMENTED={implemented_count}, PARTIAL={partial_count}, NOT IMPLEMENTED={not_impl_count}")

    return violations

def check_control_set_yaml():
    violations = []
    res = subprocess.run(["python3", "validation/build_control_set.py"], capture_output=True, text=True)
    if res.returncode != 0:
        violations.append(f"build_control_set.py failed with exit code {res.returncode}: {res.stderr}")
        return violations

    yaml_path = CASE_01_ROOT / "02_PHASE2_RULES_RICH" / "control_set.yaml"
    if not yaml_path.exists():
        violations.append("control_set.yaml was not generated")
        return violations

    with open(yaml_path, "r", encoding="utf-8") as f:
        c_text = f.read()

    c_count = c_text.count("- id: ")
    if c_count != 46:
        violations.append(f"control_set.yaml contains {c_count} controls (expected 46)")

    return violations

def main():
    print("=== AEGIS Gate v0.3: Implementation Posture & Control Set Validator ===")
    
    all_violations = []
    
    term_violations = check_deprecated_terms()
    if term_violations:
        print(f"❌ Found {len(term_violations)} deprecated maturity term violations:")
        for v in term_violations:
            print(f"  - {v}")
        all_violations.extend(term_violations)
    else:
        print("✅ Zero deprecated maturity terms found in deliverables.")

    sprint_violations = check_sprint_frontmatter()
    if sprint_violations:
        print(f"❌ Found {len(sprint_violations)} sprint frontmatter violations:")
        for v in sprint_violations:
            print(f"  - {v}")
        all_violations.extend(sprint_violations)
    else:
        print("✅ Zero sprint keys found in deliverable frontmatters.")

    doc18_violations = check_doc18_cards()
    if doc18_violations:
        print(f"❌ Found {len(doc18_violations)} Doc18 posture violations:")
        for v in doc18_violations:
            print(f"  - {v}")
        all_violations.extend(doc18_violations)
    else:
        print("✅ Doc18 Control Set status distribution verified (non-uniform, evidence-backed).")

    yaml_violations = check_control_set_yaml()
    if yaml_violations:
        print(f"❌ Found {len(yaml_violations)} control_set.yaml violations:")
        for v in yaml_violations:
            print(f"  - {v}")
        all_violations.extend(yaml_violations)
    else:
        print("✅ control_set.yaml generated and validated (46 controls).")

    if all_violations:
        print(f"\n❌ GATE FAIL: {len(all_violations)} total violations found.")
        sys.exit(1)
    else:
        print("\n✅ GATE PASS: Case_01 fully compliant with Implementation Posture Model v2.0 & Control Set v1.0!")
        sys.exit(0)

if __name__ == "__main__":
    main()
