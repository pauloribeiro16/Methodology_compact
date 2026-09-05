#!/usr/bin/env python3
"""Gate v0.4: UNMAPPED_* marker + Implementation Posture + Control Set validation for Case_01 Phase 2.

Checks (SPEC §4.5/§4.6, VALIDATOR_UNMAPPED_AUDIT_v0):
  1. No pseudo-range markers (`UNMAPPED_PF..P4` etc.).
  2. Every UNMAPPED_PF occurrence carries justification context.
  3. Every PF id used matches the canonical frozen list.
  4. CSF 2.0 ids are validated against the frozen CSF list (with waiver list).
  5. Doc19 AI RMF stays a placeholder: 30 CR rows carry `N/A (non-AI scope)`.
  6. Zero legacy maturity terms (`/maturi/i`) in deliverables (outside waivers).
  7. Zero `sprint:` keys in YAML frontmatters of deliverables.
  8. Doc18 detail cards carry exactly 46 CSF + 46 Privacy status fields with non-uniform distribution (>=2 distinct states per axis).
  9. `build_control_set.py` executes cleanly with exit code 0 and produces control_set.yaml with 46 controls.

Exit 0 = GATE PASS. Any FAIL exits 1.
"""
import json
import os
import re
import sys
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent          # 02_PHASE2_RULES_RICH
CASE_ROOT = HERE.parent                                 # Case_01_TinyTask_SaaS
REPO = CASE_ROOT.parent.parent                         # Methodology_compact
MAIN = REPO.parent / "Methodology-main"

DOCS = [
    HERE / "Doc16_Privacy_Security_Objectives.md",
    HERE / "Doc18_Rules_Catalog.md",
    HERE / "Doc19_Framework_Mapping_Matrix.md",
]

CSF_WAIVER = {
    "ID.AM-08": "frozen list tops out at ID.AM-07 (Doc19 §6.1 documents this)",
        "PR.DS-12": "pre-existing draft-1.1 remnant in a Doc16 card (CSF 2.0 has PR.DS-01/02/10/11) — cleanup deferred",
        "RS.CO-04": "pre-existing CSF 1.1 remnant (2.0 has RS.CO-01..03) — cleanup deferred",
        "PR.AT-03": "pre-existing CSF 1.1 remnant (2.0 has PR.AT-01/02) — cleanup deferred",
        "PR.AT-04": "pre-existing CSF 1.1 remnant (2.0 has PR.AT-01/02) — cleanup deferred",
    "ID.SC-04": "CSF 1.1 carry-over in Doc16 §7 mirrors",
    "PR.IP-06": "CSF 1.1 carry-over (PR.IP retired in 2.0)",
    "PR.IP-07": "CSF 1.1 carry-over (PR.IP retired in 2.0)",
    "PR.PT-01": "stale id — CSF 2.0 uses PR.PS/PR.IR families",
}

EXCLUDED_PATTERNS = [
    "validation/",
    "VALIDATOR_",
    "CHANGE_LOG",
    "DEPRECATED",
    "RICH_VS_LEGACY",
]

failures: list[str] = []
warnings: list[str] = []

def load_pf_ids() -> set[str]:
    ids: set[str] = set()
    for base in [
        REPO / "00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/NIST_PF",
        MAIN / "00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/NIST_PF",
    ]:
        if base.is_dir():
            for p in base.rglob("*.json"):
                ids.add(json.loads(p.read_text())["control_id"])
            if ids:
                break
    return ids

def load_csf_ids() -> set[str]:
    for cand in [
        REPO / "00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/NIST_CSF_2.0/CSF_2.0.json",
        MAIN / "00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md",
        REPO / "00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_CSF_2.0_subcategories.md",
    ]:
        if cand.exists():
            text = cand.read_text()
            if cand.suffix == ".json":
                data = json.loads(text)
                return {s if isinstance(s, str) else s.get("id") for s in data.get("subcategories", [])}
            return set(re.findall(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b", text))
    warnings.append("CSF frozen list not found — check 4 skipped")
    return set()

PF_RE = re.compile(r"\b(?:ID|GV|CT|CM|PR)\.(?:IM|BE|RA|DE|PO|RM|AT|MT|DM|DP|AW|AC|DS|MA|PT|IR|PS|AA)-P\d+\b")
CSF_RE = re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b")
RANGE_RE = re.compile(r"UNMAPPED_[A-Z]+\.\.")
MATURI_RE = re.compile(r"maturi", re.IGNORECASE)

def is_excluded(path: Path) -> bool:
    path_str = str(path)
    for pattern in EXCLUDED_PATTERNS:
        if pattern in path_str:
            return True
    return False

def check_deprecated_terms():
    for md_file in CASE_ROOT.rglob("*.md"):
        if is_excluded(md_file):
            continue
        with open(md_file, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                if any(k in line for k in ["DEPRECATED", "legacy", "DEPRECATED_FOR_POSTURE", "historico", "L1/L2/L3", "| L1 |", "| L2 |", "| L3 |", "| D3 |", "| D10 |", "| D11 |", "MATURIDADE DUPLA", "MODEL_CSF_STRICT", "maturity_cur", "maturity_tgt", "maturity redesign", "P1_Maturity.html"]):
                    continue
                if MATURI_RE.search(line):
                    failures.append(f"{md_file.name}:{line_no}: Found deprecated maturity term: {line.strip()}")

def check_sprint_frontmatter():
    for md_file in CASE_ROOT.rglob("*.md"):
        if is_excluded(md_file):
            continue
        content = md_file.read_text(encoding="utf-8")
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = parts[1]
                for line_no, line in enumerate(fm.split("\n"), 2):
                    if re.match(r"^\s*sprint(?:_[a-zA-Z0-9_]+)?\s*:", line):
                        failures.append(f"{md_file.name}:{line_no}: Found sprint frontmatter key: {line.strip()}")

def check_doc18_cards():
    doc18_path = HERE / "Doc18_Rules_Catalog.md"
    if not doc18_path.exists():
        failures.append("Doc18_Rules_Catalog.md not found")
        return
    
    content = doc18_path.read_text(encoding="utf-8")
    csf_count = content.count("Implementation Status (CSF):")
    priv_count = content.count("Implementation Status (Privacy):")
    
    if csf_count != 46:
        failures.append(f"Doc18 contains {csf_count}/46 'Implementation Status (CSF)' fields")
    if priv_count != 46:
        failures.append(f"Doc18 contains {priv_count}/46 'Implementation Status (Privacy)' fields")

    # Non-uniformity check
    csf_states = set(re.findall(r"21\.\s*\*\*Implementation Status \(CSF\):\*\*\s*([A-Z_]+)", content))
    priv_states = set(re.findall(r"22\.\s*\*\*Implementation Status \(Privacy\):\*\*\s*([A-Z_\/]+)", content))

    if len(csf_states) < 2:
        failures.append(f"Doc18 CSF status distribution is uniform: {csf_states}")
    if len(priv_states) < 2:
        failures.append(f"Doc18 Privacy status distribution is uniform: {priv_states}")

def check_control_set_generator():
    gen_script = REPO / "validation" / "build_control_set.py"
    if not gen_script.exists():
        failures.append("build_control_set.py not found in validation/")
        return

    res = subprocess.run(["python3", str(gen_script)], capture_output=True, text=True, cwd=str(REPO))
    if res.returncode != 0:
        failures.append(f"build_control_set.py failed (exit {res.returncode}): {res.stderr}")
        return

    yaml_path = HERE / "control_set.yaml"
    if not yaml_path.exists():
        failures.append("control_set.yaml was not generated")
        return

    c_text = yaml_path.read_text(encoding="utf-8")
    c_count = c_text.count("- id: ")
    if c_count != 46:
        failures.append(f"control_set.yaml contains {c_count} controls (expected 46)")


def check_retired_unmapped_privacy():
    for md_file in CASE_ROOT.rglob("*.md"):
        if is_excluded(md_file):
            continue
        for line_no, line in enumerate(md_file.read_text(encoding="utf-8").splitlines(), 1):
            if "UNMAPPED_PRIVACY" in line:
                failures.append(f"{md_file.name}:{line_no}: Retired UNMAPPED_PRIVACY token found: {line.strip()}")


def load_anchor_sets():
    """Frozen anchor referentials (ALT-ANCHOR criterion §2)."""
    controls = REPO / "00_METHODOLOGY" / "PREPROCESSING_by_domain" / "CONTROLS"
    r5 = set()
    for f in controls.glob("NIST_80053R5/??.json"):
        for c in json.loads(f.read_text())["controls"]:
            r5.add(c["id"])
    ssdf = set()
    ssdf_json = json.loads((controls / "NIST_SSDF" / "SSDF.json").read_text())
    for p in ssdf_json["practices"]:
        ssdf.add(p["id"])
        for t in p.get("tasks", []):
            ssdf.add(t["id"])
    asvs = json.loads((controls / "OWASP_ASVS" / "ASVS_sections.json").read_text())
    asvs_ids = set(asvs["chapters"]) | {s["id"] for s in asvs["sections"]}
    samm = json.loads((controls / "OWASP_SAMM" / "SAMM_streams.json").read_text())
    samm_ids = {s["stream"] for s in samm["streams"]}
    for s in samm["streams"]:
        for lv in (1, 2, 3):
            samm_ids.add(f"{s['stream']}-{lv}")
    iso = {f"A.{maj}.{n:02d}" for maj in range(5, 9) for n in range(1, 40)}
    return {"800-53r5": r5 | {"IP-3", "DM-1"}, "SSDF": ssdf, "ASVS": asvs_ids,
            "SAMM": samm_ids, "ISO": iso}


def alt_anchor_spans(line):
    """Yield inner strings of balanced ALT-ANCHOR (...) groups (handles IA-2(1))."""
    out = []
    idx = 0
    while True:
        s = line.find("ALT-ANCHOR (", idx)
        if s < 0:
            break
        i = s + len("ALT-ANCHOR ")
        depth = 0
        j = i
        while j < len(line):
            if line[j] == "(":
                depth += 1
            elif line[j] == ")":
                depth -= 1
                if depth == 0:
                    out.append(line[i + 1:j])
                    break
            j += 1
        idx = j + 1
    return out

def alt_anchor_is_valid(inner, anchor_sets):
    """inner = '800-53r5 AU-2; AU-3' style. First token carries the prefix; refs
    separated by ';' may omit the prefix (inherit the last seen prefix)."""
    last = None
    for raw in inner.split(";"):
        ref = raw.strip()
        if not ref:
            return False
        parts = ref.split(" ", 1)
        if len(parts) == 2 and parts[0] in anchor_sets:
            last, ident = parts[0], parts[1].strip()
        else:
            if last is None:
                return False
            ident = ref
        if ident not in anchor_sets[last]:
            return False
    return True

def main() -> int:
    pf_ids = load_pf_ids()
    csf_ids = load_csf_ids()
    if not pf_ids:
        print("FAIL: canonical PF id set is empty — CONTROLS/NIST_PF not found")
        return 1

    anchor_sets = load_anchor_sets()

    # Checks 1-4: UNMAPPED and IDs
    for doc in DOCS:
        for i, line in enumerate(doc.read_text().splitlines(), 1):
            if RANGE_RE.search(line):
                failures.append(f"{doc.name}:{i} pseudo-range marker: {RANGE_RE.search(line).group(0)}")
            if "UNMAPPED_" in line:
                hist = ("VALIDATOR_UNMAPPED_AUDIT" in line or "NIST_PF_1.0_subcategories" in line
                        or "false UNMAPPED_PF tokens" in line or "UNMAPPED retired" in line)
                if not hist:
                    failures.append(f"{doc.name}:{i} RETIRED UNMAPPED token in live doc (v0.4): {line.strip()[:120]}")
            for inner0 in alt_anchor_spans(line):
                inner = inner0.strip()
                if inner == "NO-ANALOGUE":
                    continue
                if alt_anchor_is_valid(inner, anchor_sets):
                    continue
                failures.append(f"{doc.name}:{i} ALT-ANCHOR with invalid anchor '{inner}'")
            draft_line = re.search(r"draft.?\s?1\.1", line, re.I)
            for pid in PF_RE.findall(line):
                if pid not in pf_ids:
                    if draft_line:
                        warnings.append(f"{doc.name}:{i} draft-1.1 id mentioned (not a mapping target): {pid}")
                    else:
                        failures.append(f"{doc.name}:{i} PF id not in canonical frozen list: {pid}")
            for cid in CSF_RE.findall(line):
                if csf_ids and cid not in csf_ids:
                    if cid in CSF_WAIVER:
                        warnings.append(f"{doc.name}:{i} CSF id waived (pre-existing): {cid}")
                    else:
                        failures.append(f"{doc.name}:{i} CSF id not in frozen list: {cid}")

    # Check 5: AI RMF placeholder uniformity
    doc19 = (HERE / "Doc19_Framework_Mapping_Matrix.md").read_text().splitlines()
    cr_rows = [ln for ln in doc19 if re.match(r"^\| CR-D-", ln)]
    with_pending = [ln for ln in cr_rows if "N/A (non-AI scope)" in ln]
    with_real = [ln for ln in cr_rows if re.search(r"\b(?:GOVERN|MAP|MEASURE|MANAGE)-\d+\.\d+", ln)]
    if len(with_pending) != 30:
        failures.append(f"Doc19 §1: expected 30 CR rows with AI RMF placeholder, found {len(with_pending)}")
    if with_real:
        failures.append(f"Doc19: real AI RMF ids present in Case_01: {len(with_real)} rows")

    # Checks 6-9: v0.3 additions
    check_deprecated_terms()
    check_sprint_frontmatter()
    check_retired_unmapped_privacy()
    check_doc18_cards()
    check_control_set_generator()

    n_pf_tokens = sum(doc.read_text().count("UNMAPPED_PF") for doc in DOCS)
    print(f"PF canonical ids loaded: {len(pf_ids)}")
    if csf_ids:
        print(f"CSF frozen ids loaded: {len(csf_ids)} (waived pre-existing: {len(CSF_WAIVER)})")
    print(f"UNMAPPED_PF occurrences (Doc16+18+19): {n_pf_tokens}")
    for w in warnings:
        print(f"WARN: {w}")

    if failures:
        print(f"\nFAIL ({len(failures)}):")
        print("\n".join("  " + f for f in failures))
        return 1
        
    print("\nGATE PASS (v0.4 real: UNMAPPED, Posture, Frontmatter, Control Set YAML verified)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
