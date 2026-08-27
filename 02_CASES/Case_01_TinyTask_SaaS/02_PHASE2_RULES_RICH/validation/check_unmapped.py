#!/usr/bin/env python3
"""Gate: UNMAPPED_* marker + frozen-ID validation for Case_01 Phase 2.

Checks (SPEC §4.5/§4.6, VALIDATOR_UNMAPPED_AUDIT_v0):
  1. No pseudo-range markers (`UNMAPPED_PF..P4` etc.).
  2. Every UNMAPPED_PF occurrence carries justification context: either an
     inline '(' after the token, a `justific` word on the same line, or it
     sits in a pipe-joined normalized cell (justification then lives in the
     row's Privacy cell / YAML `unmapped_pf_justification`).
  3. Every PF id used matches the canonical frozen list
     (CONTROLS/NIST_PF/**/*.json; Methodology-main fallback).
  4. CSF 2.0 ids are validated against the frozen CSF list (Methodology-main);
     a documented waiver list covers pre-existing CSF drift (reported as
     warnings, filed for normalisation — see VALIDATOR_UNMAPPED_AUDIT_v0 §5).
  5. Doc19 AI RMF stays a placeholder: every §1 CR row carries
     `pending Case_02/03` and no row carries real AI RMF ids.

Exit 0 = gate pass. Any FAIL exits 1.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent          # 02_PHASE2_RULES_RICH
REPO = HERE.parent.parent.parent                        # Methodology_compact
MAIN = REPO.parent / "Methodology-main"

DOCS = [
    HERE / "Doc16_Privacy_Security_Objectives.md",
    HERE / "Doc18_Rules_Catalog.md",
    HERE / "Doc19_Framework_Mapping_Matrix.md",
]

# Pre-existing CSF drift, documented in VALIDATOR_UNMAPPED_AUDIT_v0 §5
# (CSF 1.1 carry-overs / frozen-list gaps in Doc16 §7 mirrors + Doc19 §6.1).
CSF_WAIVER = {
    "ID.AM-08": "frozen list tops out at ID.AM-07 (Doc19 §6.1 documents this)",
    "ID.SC-04": "CSF 1.1 carry-over in Doc16 §7 mirrors",
    "PR.IP-06": "CSF 1.1 carry-over (PR.IP retired in 2.0)",
    "PR.IP-07": "CSF 1.1 carry-over (PR.IP retired in 2.0)",
    "PR.PT-01": "stale id — CSF 2.0 uses PR.PS/PR.IR families",
}

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
        MAIN / "00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md",
        REPO / "00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_CSF_2.0_subcategories.md",
    ]:
        if cand.exists():
            text = cand.read_text()
            return set(re.findall(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b", text))
    warnings.append("CSF frozen list not found — check 4 skipped")
    return set()


PF_RE = re.compile(r"\b(?:ID|GV|CT|CM|PR)\.(?:IM|BE|RA|DE|PO|RM|AT|MT|DM|DP|AW|AC|DS|MA|PT|IR|PS|AA)-P\d+\b")
CSF_RE = re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b")
RANGE_RE = re.compile(r"UNMAPPED_[A-Z]+\.\.")


def main() -> int:
    pf_ids = load_pf_ids()
    csf_ids = load_csf_ids()
    if not pf_ids:
        print("FAIL: canonical PF id set is empty — CONTROLS/NIST_PF not found")
        return 1

    for doc in DOCS:
        for i, line in enumerate(doc.read_text().splitlines(), 1):
            if RANGE_RE.search(line):
                failures.append(f"{doc.name}:{i} pseudo-range marker: {RANGE_RE.search(line).group(0)}")
            for m in re.finditer(r"UNMAPPED_PF", line):
                tail = line[m.end():].lstrip()
                # divider cells (normalized columns / table cells): justification
                # lives in the row's Privacy cell or YAML field
                if tail.startswith("\\|") or tail.startswith("|"):
                    continue
                # prose mention ("UNMAPPED_PF tokens replaced by ...")
                if tail and tail[0].islower():
                    continue
                if "(" in tail[:200] or re.search(r"justific", line, re.I):
                    continue
                failures.append(f"{doc.name}:{i} UNMAPPED_PF without justification context")
            # PF ids: skip mentions of draft-1.1 ids inside explanatory prose
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

    # 5. AI RMF placeholder uniformity in Doc19 §1 (30 CR rows)
    doc19 = (HERE / "Doc19_Framework_Mapping_Matrix.md").read_text().splitlines()
    cr_rows = [ln for ln in doc19 if re.match(r"^\| CR-D-", ln)]
    with_pending = [ln for ln in cr_rows if "pending Case_02/03" in ln]
    with_real = [ln for ln in cr_rows if re.search(r"\b(?:GOVERN|MAP|MEASURE|MANAGE)-\d+\.\d+", ln)]
    if len(with_pending) != 30:
        failures.append(f"Doc19 §1: expected 30 CR rows with AI RMF placeholder, found {len(with_pending)}")
    if with_real:
        failures.append(f"Doc19: real AI RMF ids present in Case_01 (placeholder-only per SPEC §4.3): {len(with_real)} rows")

    n_pf_tokens = sum(doc.read_text().count("UNMAPPED_PF") for doc in DOCS)
    print(f"PF canonical ids loaded: {len(pf_ids)}")
    if csf_ids:
        print(f"CSF frozen ids loaded: {len(csf_ids)} (waived pre-existing: {len(CSF_WAIVER)})")
    print(f"UNMAPPED_PF occurrences (Doc16+18+19): {n_pf_tokens}")
    seen = set()
    for w in warnings:
        if w.split(":")[0] not in seen or True:
            pass
        print(f"WARN: {w}")
    if failures:
        print(f"\nFAIL ({len(failures)}):")
        print("\n".join("  " + f for f in failures))
        return 1
    print("\nGATE PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
