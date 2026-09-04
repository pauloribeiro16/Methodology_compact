#!/usr/bin/env python3
"""build_control_set.py — Case_03 (port Fase 5).

Generates 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/control_set.yaml
from the Control Set tables in Doc19_Rules_Catalog.md (single source of truth).

Case_03 layout: CR rows 19 cells (17 + F23/F24) or 18 cells (16 + F23/F24);
BPR rows 17 cells (15 + F23/F24). Counts pinned: 38 CR + 40 BPR = 78.
Status parsing validated against the posture enum (the Case_01 '**' defect
is structurally impossible and asserted against).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC20 = ROOT / "Doc19_Rules_Catalog.md"
# PORT-PARITY-2 F4: canonical location is the P2 ROOT (matching Case_01);
# validation/control_set.yaml becomes a byte-identical mirror so the
# check_unmapped + posture gates (which read BUILD.parent/control_set.yaml)
# keep passing unchanged.
OUT = ROOT / "control_set.yaml"
MIRROR = Path(__file__).resolve().parent / "control_set.yaml"

def parse_row(ln):
    cells = [c.strip() for c in ln.split("|")[1:-1]]
    if not cells:
        return None
    rid = cells[0]
    if re.match(r"^CR-D-\d\d\.\d-\d{3}$", rid):
        if len(cells) == 18:
            return dict(id=rid, description=cells[1], sources=cells[2], sub_domain=cells[3],
                        ni=cells[4], priority=cells[5], verification=cells[6], impl=cells[7],
                        related_goals=cells[8], type_line=cells[9], csf=cells[10], pf=cells[11],
                        airmf=cells[12], status_csf=cells[13], status_privacy=cells[14],
                        status_airmf=cells[15], traceability=cells[16], frameworks_ref=cells[17], kind="CR")
        if len(cells) == 19:
            return dict(id=rid, description=cells[1], sources=cells[2], sub_domain=cells[3],
                        ni=cells[4], priority=cells[5], verification=cells[6], impl=cells[7],
                        related_goals=cells[8], type_line=cells[9], case03_specific=cells[10],
                        csf=cells[11], pf=cells[12], airmf=cells[13], status_csf=cells[14],
                        status_privacy=cells[15], status_airmf=cells[16], traceability=cells[17],
                        frameworks_ref=cells[18], kind="CR")
    if re.match(r"^BPR-D-\d\d\.\d-\d{3}$", rid):
        if len(cells) >= 12:
            ref = cells[-1]
            trace = cells[-2]
            ENUM = ("IMPLEMENTED", "PARTIAL", "NOT IMPLEMENTED", "N/A", "—")
            def is_status(v):
                return v.startswith(ENUM)
            statuses_rev = []
            i = len(cells) - 3
            while i >= 0 and len(statuses_rev) < 3 and is_status(cells[i]):
                statuses_rev.append(cells[i])
                i -= 1
            statuses = list(reversed(statuses_rev))
            while len(statuses) < 3:
                statuses.insert(0, "—")
            sc, sp, sa = statuses[-3], statuses[-2], statuses[-1]
            airmf = cells[i] if i >= 0 else "—"
            if sa.startswith("N/A") and not airmf.startswith(("GOVERN","MAP","MEASURE","MANAGE","N/A","—","ID.RA")):
                airmf = sa  # dual-purpose cell (legacy "não mapeado" column)
            return dict(id=rid, description=cells[1], sources=cells[2], sub_domain=cells[3],
                        priority=cells[4], verification=cells[5], related_crs=cells[6],
                        type_line=cells[7], csf=cells[-6] if len(cells) >= 6 else "",
                        pf=cells[-5] if len(cells) >= 5 else "", airmf=airmf,
                        status_csf=sc, status_privacy=sp, status_airmf=sa,
                        traceability=trace, frameworks_ref=ref, kind="BPR")
    return None

def main():
    section = None
    controls, problems = [], []
    for ln in DOC20.read_text(encoding="utf-8").split("\n"):
        if ln.startswith("## 4. COMPLIANCE"):
            section = "CR"
        elif ln.startswith("## 5. BEST PRACTICE"):
            section = "BPR"
        elif re.match(r"^## 6\.", ln):
            section = None
        if section not in ("CR", "BPR"):
            continue
        c = parse_row(ln)
        if not c:
            continue
        for k in ("status_csf", "status_privacy", "status_airmf"):
            v = c[k]
            if not (v.startswith(("N/A", "—", "IMPLEMENTED", "PARTIAL", "NOT IMPLEMENTED"))):
                problems.append(f"{c['id']}: bad {k}={v!r}")
        if "**" in (c["status_csf"] + c["status_privacy"] + c["status_airmf"]):
            problems.append(f"{c['id']}: '**' parsing artifact detected")
        controls.append(c)

    cr = [c for c in controls if c["kind"] == "CR"]
    bpr = [c for c in controls if c["kind"] == "BPR"]
    if problems:
        print("STATUS PARSE PROBLEMS:")
        for p in problems:
            print(" ", p)
        sys.exit(1)
    if len(cr) != 38 or len(bpr) != 40:
        print(f"COUNT MISMATCH: CR={len(cr)} (want 38), BPR={len(bpr)} (want 40)")
        sys.exit(1)

    def y(v):
        return '"' + str(v).replace('"', "'") + '"'

    out = [
        "# AEGIS Control Set — Case_03 (OmniBank Financial Systems) — GENERATED FILE",
        "# Source of truth: Doc19_Rules_Catalog.md §4/§5 (DO NOT EDIT by hand).",
        "# Regenerate: python3 validation/build_control_set.py",
        "# Port Fase 5, 2026-08-28. Statuses = deterministic legacy backfill (posture model §4).",
        "control_set:",
        "  case: Case_03_OmniBank_Financial",
        "  version: 2.0",
        "  total_controls: 78",
        "  obligation_must: 38",
        "  best_practice_should: 40",
        "  regulations: [GDPR, CRA, NIS_2, DORA, AI_Act]",
        "  dora_coverage: via_CSF",
        "  controls:",
    ]
    for c in controls:
        out.append(f"    - id: {y(c['id'])}")
        out.append(f"      kind: {y(c['kind'])}")
        out.append(f"      type: {y('CONTROL — OBLIGATION (MUST)' if c['kind'] == 'CR' else 'BEST-PRACTICE (SHOULD)')}")
        out.append(f"      description: {y(c['description'])}")
        out.append(f"      source: {y(c['sources'])}")
        out.append(f"      sub_domain: {y(c['sub_domain'])}")
        out.append(f"      priority: {y(c['priority'])}")
        out.append(f"      verification: {y(c['verification'])}")
        out.append(f"      related_goals: {y(c.get('related_goals', c.get('related_crs', '')))}")
        out.append(f"      csf: {y(c['csf'])}")
        out.append(f"      pf: {y(c['pf'])}")
        out.append(f"      airmf: {y(c['airmf'])}")
        out.append(f"      status_csf: {y(c['status_csf'])}")
        out.append(f"      status_privacy: {y(c['status_privacy'])}")
        out.append(f"      status_airmf: {y(c['status_airmf'])}")
        out.append(f"      traceability: {y(c['traceability'])}")
        out.append(f"      frameworks_ref: {y(c['frameworks_ref'])}")
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    MIRROR.write_text("\n".join(out) + "\n", encoding="utf-8")
    dist = {}
    for c in controls:
        dist[c["status_csf"]] = dist.get(c["status_csf"], 0) + 1
    print(f"control_set.yaml written: {len(controls)} controls (38 CR + 40 BPR)")
    print(f"  canonical: {OUT}")
    print(f"  mirror:    {MIRROR}")
    print("status_csf distribution:", dist)

if __name__ == "__main__":
    main()
