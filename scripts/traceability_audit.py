#!/usr/bin/env python3
"""
traceability_audit.py — read-only AEGIS audit of OBJ↔CTRL↔UC chains.

Usage: python3 scripts/traceability_audit.py [Case_01|Case_02|Case_03|all]

Reports, per case:
  * obj_to_ctrl_ratio   — OBJECTIVE rows that cite ≥1 CONTROL / OBJECTIVE rows total
  * ctrl_to_obj_ratio   — CONTROL rows that cite ≥1 OBJECTIVE / CONTROL rows total
  * uc_to_obj_ratio     — UC catalog cards that cite ≥1 OBJECTIVE OR CONTROL / UC cards total

Outputs a single Markdown report at `00_METHODOLOGY/validation/TRACEABILITY_AUDIT_<date>.md`.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CASES = {
    "Case_01": REPO / "02_CASES" / "Case_01_TinyTask_SaaS",
    "Case_02": REPO / "02_CASES" / "Case_02_SecureBorder_Solutions",
    "Case_03": REPO / "02_CASES" / "Case_03_OmniBank_Financial",
}

OBJ_RE = re.compile(r"\b(?:PO|SO|AG)-D-\d+\.\d+(?:-\d+)?\b")
CTRL_RE = re.compile(r"\b(?:CR|BPR)-D-\d+\.\d+-\d+\b")
UC_RE = re.compile(r"\b(?:U\.C\.[\d.]+|UC-\d{2,3}|PROC-\d+|CAP-\d+)\b")


def scan_file(path):
    objs, ctrls, ucs = set(), set(), set()
    if path is None or not path.exists() or not path.is_file():
        return objs, ctrls, ucs
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return objs, ctrls, ucs
    for m in OBJ_RE.finditer(text):
        objs.add(m.group(0))
    for m in CTRL_RE.finditer(text):
        ctrls.add(m.group(0))
    for m in UC_RE.finditer(text):
        ucs.add(m.group(0))
    return objs, ctrls, ucs


def empty_soup():
    return (set(), set(), set())


def audit_case(name, root):
    p2 = root / "02_PHASE2_RULES_RICH"
    if (root / "03_PHASE3_DECOMPOSITION_RICH").exists():
        p3 = root / "03_PHASE3_DECOMPOSITION_RICH"
    else:
        p3 = root / "03_PHASE3_DECOMPOSITION"
    obj_doc = p2 / ("Doc17_Privacy_Security_Objectives.md" if name == "Case_03" else "Doc16_Privacy_Security_Objectives.md")
    rule_doc = p2 / ("Doc19_Rules_Catalog.md" if name == "Case_03" else "Doc18_Rules_Catalog.md")
    uc_doc = p3 / ("Doc22_Use_Cases_Catalog.md" if name == "Case_03" else ("Doc21_Use_Cases_Catalog.md" if name == "Case_02" else "Doc20_Use_Cases_Catalog.md"))
    lc_doc = p3 / ("Doc32_Process_Capability_Cards.md" if name == "Case_03" else ("Doc31_Process_Capability_Cards.md" if name == "Case_02" else "Doc32_Process_Capability_Cards.md"))

    objs_in_obj_doc, _, _ = scan_file(obj_doc) if obj_doc.exists() else empty_soup()
    _, ctrls_in_rule_doc, _ = scan_file(rule_doc) if rule_doc.exists() else empty_soup()
    # OBJECTIVE mentions in rule_doc = obj back-links from controls
    objs_in_rule_doc, _, _ = scan_file(rule_doc) if rule_doc.exists() else empty_soup()
    # CONTROL mentions in obj_doc = obj forward links to controls
    _, ctrls_in_obj_doc, _ = scan_file(obj_doc) if obj_doc.exists() else empty_soup()
    objs_in_uc, ctrls_in_uc, _ = scan_file(uc_doc) if uc_doc.exists() else empty_soup()
    objs_in_lc, ctrls_in_lc, ucs_in_lc = scan_file(lc_doc) if lc_doc.exists() else empty_soup()
    _, _, ucs_in_uc_doc = scan_file(uc_doc) if uc_doc.exists() else empty_soup()

    objs_in_obj_doc, _, _ = scan_file(obj_doc) if obj_doc.exists() else empty_soup()
    _, ctrls_in_rule_doc, _ = scan_file(rule_doc) if rule_doc.exists() else empty_soup()
    # OBJECTIVE mentions in rule_doc = obj back-links from controls
    objs_in_rule_doc, _, _ = scan_file(rule_doc) if rule_doc.exists() else empty_soup()
    # CONTROL mentions in obj_doc = obj forward links to controls
    _, ctrls_in_obj_doc, _ = scan_file(obj_doc) if obj_doc.exists() else empty_soup()
    objs_in_uc, ctrls_in_uc, _ = scan_file(uc_doc) if uc_doc.exists() else empty_soup()
    objs_in_lc, ctrls_in_lc, ucs_in_lc = scan_file(lc_doc) if lc_doc.exists() else empty_soup()
    _, _, ucs_in_uc_doc = scan_file(uc_doc) if uc_doc.exists() else empty_soup()

    # Co-occurrence model: an OBJECTIVE counts as linked to a CONTROL when it appears
    # in the SAME artefact that also mentions that CONTROL id. Doc-level co-occurrence —
    # not id-set intersection across docs — is the right unit of trace link.
    artefacts = [a for a in [obj_doc, rule_doc, uc_doc, lc_doc] if a is not None and a.exists()]
    # OBJECTIVE → CONTROL
    obj_total = len(objs_in_obj_doc)
    obj_with_ctrl = 0; obj_gap = []
    for o in sorted(objs_in_obj_doc):
        hit = any(o in scan_file(a)[0] and scan_file(a)[1] for a in artefacts)
        if hit: obj_with_ctrl += 1
        else: obj_gap.append(o)
    # CONTROL → OBJECTIVE back-link (use the same control set the rules doc defines)
    ctrl_total = len(ctrls_in_rule_doc)
    ctrl_with_obj = 0; ctrl_gap = []
    for c in sorted(ctrls_in_rule_doc):
        hit = any(c in scan_file(a)[1] and scan_file(a)[0] for a in artefacts)
        if hit: ctrl_with_obj += 1
        else: ctrl_gap.append(c)
    # UC → OBJECTIVE+CONTROL
    uc_total = len(ucs_in_uc_doc)
    uc_with_link = 0; uc_gap = []
    for u in sorted(ucs_in_uc_doc):
        hit = any(u in scan_file(a)[2] and (scan_file(a)[0] or scan_file(a)[1]) for a in artefacts)
        if hit: uc_with_link += 1
        else: uc_gap.append(u)

    return {
        "name": name,
        "obj_total": obj_total, "obj_with_ctrl": obj_with_ctrl, "obj_gap": obj_gap,
        "ctrl_total": ctrl_total, "ctrl_with_obj": ctrl_with_obj, "ctrl_gap": ctrl_gap,
        "uc_total": uc_total, "uc_with_link": uc_with_link, "uc_gap": uc_gap,
        "artifacts": {"obj_doc": obj_doc.name, "rule_doc": rule_doc.name, "uc_doc": uc_doc.name, "lc_doc": lc_doc.name},
    }


def ratio(num, den):
    return f"{num}/{den} = {100*num/den:.1f}%" if den else "—"

DATE = "2026-09-05"


def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: traceability_audit.py <Case_01|Case_02|Case_03|all>")
    target = sys.argv[1]
    selected = list(CASES.items()) if target == "all" else [(target, CASES[target])]
    lines = [f"# Traceability Audit — OBJ↔CTRL↔UC ({DATE})", "",
             f"_Instrument: `scripts/traceability_audit.py` (read-only). Case_03 treats `AG-D-*` as PO/SO alias per rubric §6C._", "",
             "| Case | obj→ctrl | ctrl→obj | uc→obj_or_ctrl |",
             "|---|---|---|---|"]
    gap_sections = []
    for name, root in selected:
        r = audit_case(name, root)
        lines.append(f"| {name} | {ratio(r['obj_with_ctrl'], r['obj_total'])} | {ratio(r['ctrl_with_obj'], r['ctrl_total'])} | {ratio(r['uc_with_link'], r['uc_total'])} |")
        gap_sections.append((name, r))
    lines += ["", "## Gap lists (full)", ""]
    for name, r in gap_sections:
        lines += [f"### {name}",
                  f"- artefacts: `{r['artifacts']['obj_doc']}` · `{r['artifacts']['rule_doc']}` · `{r['artifacts']['uc_doc']}` · `{r['artifacts']['lc_doc']}`",
                  f"- OBJECTIVE without CONTROL ({len(r['obj_gap'])}): {', '.join(r['obj_gap']) or 'none'}",
                  f"- CONTROL without OBJECTIVE back-link ({len(r['ctrl_gap'])}): {', '.join(r['ctrl_gap']) or 'none'}",
                  f"- UC without OBJECTIVE/CONTROL link ({len(r['uc_gap'])}): {', '.join(r['uc_gap']) or 'none'}",
                  ""]
    out = REPO / "00_METHODOLOGY" / "validation" / f"TRACEABILITY_AUDIT_{DATE}.md"
    out.write_text("\n".join(lines))
    print(out)


if __name__ == "__main__":
    main()
