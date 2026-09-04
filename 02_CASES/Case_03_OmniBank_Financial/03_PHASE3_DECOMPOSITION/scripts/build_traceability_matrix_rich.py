#!/usr/bin/env python3
"""
build_traceability_matrix_rich.py — Phase 3 Rich Mode traceability matrix,
Case_03 (OmniBank Financial). PORT-PARITY-2 block F5 port of Case_01's script
of the same name, adapted to Case_03's real artefacts (card-based FR/NFR/gate
docs, Doc19 rules catalog after the P2 renumbering):

  02_PHASE2_RULES_RICH/control_set.yaml             -> RULES sheet (78 controls = 38 CR + 40 BPR)
  requirements/Doc30_Functional_Requirements.md     -> FR cards (72), Source Rule / Source UC / Source Node
  requirements/Doc31_Non_Functional_Requirements.md -> NFR cards (12 defined; summary claims 56 — see lint baseline)
  Doc22_Use_Cases_Catalog.md '**Rules:**' lines     -> UC_TO_RULE (62 UC cards)
  Doc26_Requirements_Allocation.md §3 tables        -> RULE_TO_NODE
  Doc27_Compliance_Gates_Report.md gate cards       -> GATES_STATUS (40 gates)
  ../02_PHASE2_RULES_RICH/data/phase2_graph.json    -> P2_GRAPH_SUMMARY

Emits `22_Traceability_Matrix_rich_v0.xlsx` — the legacy
`22_Traceability_Matrix.xlsx` deliverable is NOT touched.

Usage:
  python3 scripts/build_traceability_matrix_rich.py
  python3 scripts/build_traceability_matrix_rich.py --output <xlsx>
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import yaml
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

BASE = Path(__file__).resolve().parent.parent
CASE = BASE.parent
P2 = CASE / "02_PHASE2_RULES_RICH"

RULE_RE = re.compile(r"\b(?:CR|BPR)-D-\d{2}\.\d-\d{3}\b")
UC_RE = re.compile(r"\bUC-\d{2}\b")
NODE_RE = re.compile(r"\bNODE-[A-Z0-9]+(?:-\d{2,3})?\b")

HEADER_FILL = PatternFill(start_color="305496", end_color="305496", fill_type="solid")
HEADER_FONT = Font(bold=True, color="FFFFFF")
LABEL_FONT = Font(bold=True)


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write_header(ws, headers: List[str]) -> None:
    for col, h in enumerate(headers, start=1):
        c = ws.cell(row=1, column=col, value=h)
        c.fill = HEADER_FILL
        c.font = HEADER_FONT
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 30


def autosize(ws, max_width: int = 60) -> None:
    for col_idx in range(1, ws.max_column + 1):
        longest = 0
        for row_idx in range(1, ws.max_row + 1):
            v = ws.cell(row=row_idx, column=col_idx).value
            if v is not None:
                longest = max(longest, min(len(str(v)), max_width))
        ws.column_dimensions[get_column_letter(col_idx)].width = min(max(longest + 2, 10), max_width)


def parse_cards(doc: str, kind: str) -> Dict[str, dict]:
    cards: Dict[str, dict] = {}
    current = None
    for line in doc.splitlines():
        m = re.match(rf"^#### ({kind}-\d{{2,3}}): (.+)$", line)
        if m:
            current = m.group(1)
            cards[current] = {"title": m.group(2).strip(), "fields": {}}
            continue
        if current:
            fm_ = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|", line)
            if fm_:
                cards[current]["fields"][fm_.group(1)] = fm_.group(2)
    return cards


def main() -> int:
    ap = argparse.ArgumentParser(description="Build 22_Traceability_Matrix_rich_v0.xlsx for Case_03.")
    ap.add_argument("--output", default=None)
    args = ap.parse_args()
    out = Path(args.output) if args.output else BASE / "22_Traceability_Matrix_rich_v0.xlsx"

    cs = yaml.safe_load(read(P2 / "control_set.yaml"))["control_set"]
    controls = cs["controls"]

    fr_doc = read(BASE / "requirements" / "Doc30_Functional_Requirements.md")
    fr_cards = parse_cards(fr_doc, "FR")
    nfr_doc = read(BASE / "requirements" / "Doc31_Non_Functional_Requirements.md")
    nfr_cards = parse_cards(nfr_doc, "NFR")

    # UC -> rules from '**Rules:**' lines (Doc22)
    uc_doc = read(BASE / "Doc22_Use_Cases_Catalog.md")
    uc_to_rules: Dict[str, List[str]] = {}
    cur_uc = None
    for line in uc_doc.splitlines():
        m = re.match(r"^## (UC-\d{2}):", line)
        if m:
            cur_uc = m.group(1)
            continue
        rm = re.match(r"^\*\*Rules:\*\*\s*(.+)$", line)
        if rm and cur_uc:
            uc_to_rules[cur_uc] = sorted(set(RULE_RE.findall(rm.group(1))))

    # allocation: Doc26 §3 table rows | Rule ID | desc | Node | rationale | track | anchors |
    alloc_doc = read(BASE / "Doc26_Requirements_Allocation.md")
    rule_nodes: Dict[str, List[str]] = {}
    alloc_rows = 0
    for line in alloc_doc.splitlines():
        m = re.match(r"^\| ((?:CR|BPR)-D-\d{2}\.\d-\d{3}) \|[^|]*\|([^|]*)\|", line)
        if m:
            alloc_rows += 1
            nodes = sorted(set(re.findall(r"\bNODE-[A-Z]+-[0-9.\-]+\b", m.group(2))))
            rule_nodes.setdefault(m.group(1), [])
            for n in nodes:
                if n not in rule_nodes[m.group(1)]:
                    rule_nodes[m.group(1)].append(n)

    # gates: Doc27 cards ('#### GATE-D-XX-NN: Name' — dedicated pattern, GATE- prefix is not FR/NFR-shaped)
    gates: Dict[str, dict] = {}
    current = None
    for line in read(BASE / "Doc27_Compliance_Gates_Report.md").splitlines():
        m = re.match(r"^#### (GATE-D-\d{2}-\d{2}): (.+)$", line)
        if m:
            current = m.group(1)
            gates[current] = {"title": m.group(2).strip(), "fields": {}}
            continue
        if current:
            fm_ = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|", line)
            if fm_:
                gates[current]["fields"][fm_.group(1)] = fm_.group(2)

    # P2 graph summary
    g = json.loads(read(P2 / "data" / "phase2_graph.json"))
    rels: Dict[str, int] = {}
    for l in g["links"]:
        rels[l["rel"]] = rels.get(l["rel"], 0) + 1
    types: Dict[str, int] = {}
    for n in g["nodes"]:
        types[n["type"]] = types.get(n["type"], 0) + 1

    wb = Workbook()

    # COVER
    ws = wb.active
    ws.title = "COVER"
    fr_sr = {fid: c["fields"].get("Source Rule", "") for fid, c in fr_cards.items()}
    fr_mapped = sum(1 for v in fr_sr.values() if RULE_RE.fullmatch(v or ""))
    rows = [
        ("Document Title", "Phase 3 RICH Traceability Matrix (v0) — Case_03 OmniBank Financial Systems"),
        ("Document ID", "AEGIS-C03-P3-TRACE-MATRIX-RICH"),
        ("Phase", "3"),
        ("Case", "Case_03_OmniBank_Financial"),
        ("Status", "GENERATED v0 (PORT-PARITY-2) — pending human review"),
        ("Version", "0.0"),
        ("Generated", dt.datetime.now().strftime("%Y-%m-%d %H:%M")),
        ("Generator", "scripts/build_traceability_matrix_rich.py (parses live artefacts; nothing hard-coded)"),
        ("Source — Rules", "../02_PHASE2_RULES_RICH/control_set.yaml (78 controls: 38 CR + 40 BPR; Doc19_Rules_Catalog.md §4/§5)"),
        ("Source — FR", "requirements/Doc30_Functional_Requirements.md (72 FR cards)"),
        ("Source — NFR", "requirements/Doc31_Non_Functional_Requirements.md (12 NFR cards; doc summary claims 56 — see RICH_LINT_BASELINE.md)"),
        ("Source — UC", "Doc22_Use_Cases_Catalog.md (62 UC cards)"),
        ("Source — Allocation", "Doc26_Requirements_Allocation.md §3"),
        ("Source — Gates", "Doc27_Compliance_Gates_Report.md (gate cards)"),
        ("Source — P2 graph", "../02_PHASE2_RULES_RICH/data/phase2_graph.json (242n/340l)"),
        ("Legacy matrix", "22_Traceability_Matrix.xlsx (untouched, kept alongside)"),
        ("Rules total", len(controls)),
        ("FR cards", len(fr_cards)),
        ("FRs with catalog-rule Source Rule", fr_mapped),
        ("FRs with non-rule Source Rule (article refs / —)", len(fr_cards) - fr_mapped),
        ("NFR cards (defined)", len(nfr_cards)),
        ("UC cards with Rules line", len(uc_to_rules)),
        ("Allocation rows parsed", alloc_rows),
        ("Gates parsed", len(gates)),
    ]
    write_header(ws, ["Attribute", "Value"])
    for r, (k, v) in enumerate(rows, start=2):
        ws.cell(row=r, column=1, value=k).font = LABEL_FONT
        ws.cell(row=r, column=2, value=str(v))
    autosize(ws)

    # RULES
    ws = wb.create_sheet("RULES")
    write_header(ws, ["#", "Rule ID", "Kind", "Type", "Sub-domain", "Priority", "Verification",
                      "Source", "Related goals", "CSF", "PF", "AI RMF", "status_csf"])
    for i, c in enumerate(controls, start=1):
        ws.append([i, c["id"], c["kind"], c["type"], c["sub_domain"], c.get("priority", ""),
                   c.get("verification", ""), c.get("source", ""), c.get("related_goals", ""),
                   c.get("csf", ""), c.get("pf", ""), c.get("airmf", ""), c.get("status_csf", "")])
    autosize(ws)

    # FR_TO_RULE
    ws = wb.create_sheet("FR_TO_RULE")
    write_header(ws, ["#", "FR ID", "Title", "Source Rule", "Source UC", "Source Node", "Verification", "Priority"])
    for i, (fid, card) in enumerate(sorted(fr_cards.items()), start=1):
        f = card["fields"]
        ws.append([i, fid, card["title"], f.get("Source Rule", "—"), f.get("Source UC", "—"),
                   f.get("Source Node", "—"), f.get("Verification", "—"), f.get("Priority", "—")])
    autosize(ws)

    # RULE_TO_FR
    ws = wb.create_sheet("RULE_TO_FR")
    write_header(ws, ["#", "Rule ID", "Kind", "FR count (Source Rule)", "FRs", "Coverage gap?"])
    fr_by_rule: Dict[str, List[str]] = {}
    for fid, sr in fr_sr.items():
        if RULE_RE.fullmatch(sr or ""):
            fr_by_rule.setdefault(sr, []).append(fid)
    for i, c in enumerate(controls, start=1):
        frs_of = sorted(fr_by_rule.get(c["id"], []))
        ws.append([i, c["id"], c["kind"], len(frs_of), ", ".join(frs_of) or "—",
                   "GAP — no FR cites this rule" if not frs_of else ""])
    autosize(ws)

    # UC_TO_RULE
    ws = wb.create_sheet("UC_TO_RULE")
    write_header(ws, ["#", "UC ID", "Rules (Doc22 '**Rules:**' line)"])
    for i, (uc, rules) in enumerate(sorted(uc_to_rules.items()), start=1):
        ws.append([i, uc, ", ".join(rules) or "—"])
    autosize(ws)

    # RULE_TO_NODE
    ws = wb.create_sheet("RULE_TO_NODE")
    write_header(ws, ["#", "Rule ID", "Nodes (Doc26 §3 allocation)"])
    for i, (rid, nodes) in enumerate(sorted(rule_nodes.items()), start=1):
        ws.append([i, rid, ", ".join(nodes) or "—"])
    autosize(ws)

    # GATES_STATUS
    ws = wb.create_sheet("GATES_STATUS")
    write_header(ws, ["#", "Gate ID", "Name", "Domain", "Rules Verified", "UC Verified", "Node Verified", "Method", "Status"])
    for i, (gid, card) in enumerate(sorted(gates.items()), start=1):
        f = card["fields"]
        ws.append([i, gid, card["title"], f.get("Domain", "—"), f.get("Rules Verified", "—"),
                   f.get("UC Verified", "—"), f.get("Node Verified", "—"),
                   f.get("Verification Method", "—"), f.get("Gate Status", "—")])
    autosize(ws)

    # NFRS
    ws = wb.create_sheet("NFRS")
    write_header(ws, ["#", "NFR ID", "Title", "Category", "Source Rule", "Source UC", "Priority"])
    for i, (nid, card) in enumerate(sorted(nfr_cards.items()), start=1):
        f = card["fields"]
        ws.append([i, nid, card["title"], f.get("Category", "—"), f.get("Source Rule", "—"),
                   f.get("Source UC", "—"), f.get("Priority", "—")])
    autosize(ws)

    # P2_GRAPH_SUMMARY
    ws = wb.create_sheet("P2_GRAPH_SUMMARY")
    write_header(ws, ["Metric", "Value"])
    ws.append(["nodes", len(g["nodes"])])
    ws.append(["links", len(g["links"])])
    for t, n in sorted(types.items(), key=lambda x: -x[1]):
        ws.append([f"node type {t}", n])
    for r, n in sorted(rels.items(), key=lambda x: -x[1]):
        ws.append([f"link rel {r}", n])
    autosize(ws)

    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)
    print(f"[ok] wrote {out} with {len(wb.sheetnames)} sheets: {', '.join(wb.sheetnames)}")
    print(f"[stats] rules={len(controls)} frs={len(fr_cards)} fr_mapped={fr_mapped} nfrs={len(nfr_cards)} "
          f"ucs_with_rules={len(uc_to_rules)} alloc_rows={alloc_rows} gates={len(gates)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
