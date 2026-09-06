#!/usr/bin/env python3
"""
build_traceability_matrix_rich.py — Phase 3 Rich Mode traceability matrix,
Case_02 (SecureBorder Solutions). PORT-PARITY-2 block F5 port of Case_01's
script of the same name.

Unlike the Case_01 version (frozen tables hard-coded in the script), this port
PARSES the Case_02 artefacts live — no invented content:

  02_PHASE2_RULES_RICH/control_set.yaml      -> RULES sheets (63 controls)
  requirements/Doc29_Functional_Requirements.md -> FR_TO_RULE, FR_TO_UC (84 FRs)
  requirements/Doc30_Non_Functional_Requirements.md -> NFR summary
  Doc21_Use_Cases_Catalog.md §11             -> UC_TO_RULE
  Doc25_Requirements_Allocation.md           -> RULE_TO_NODE allocations
  Doc26_Compliance_Gates_Report.md §5        -> GATES_STATUS
  ../02_PHASE2_RULES_RICH/data/phase2_graph.json -> P2 chain summary

Emits `22_Traceability_Matrix_rich_v0.xlsx` (the legacy
`22_Traceability_Matrix.xlsx` deliverable is NOT touched).

Usage:
  python3 scripts/build_traceability_matrix_rich.py
  python3 scripts/build_traceability_matrix_rich.py --output <xlsx>
"""
from __future__ import annotations

import argparse
import datetime as dt
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

FR_RE = re.compile(r"\bFR-\d{2,3}\b")
NFR_RE = re.compile(r"\bNFR-\d{2,3}\b")
UC_RE = re.compile(r"\bUC-\d{2}\b")
RULE_RE = re.compile(r"\b(?:CR|BPR)-D-\d{2}\.\d-\d{3}\b")
NODE_RE = re.compile(r"\bNODE-(?:SYS|PROC|ROLE)-\d{3}\b")
GATE_RE = re.compile(r"\bGATE-D-\d{2}\.\d-\d{3}\b")

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


# ---------- parsers ----------

def parse_control_set() -> List[dict]:
    cs = yaml.safe_load(read(P2 / "control_set.yaml"))["control_set"]
    return cs["controls"]


def parse_frs() -> Tuple[Dict[str, dict], List[str]]:
    """Doc29 FR table: | FR-ID | Requirement | Source UC | Source NFR | Source Rule | Verification | Priority | NIST |"""
    doc = read(BASE / "requirements" / "Doc29_Functional_Requirements.md")
    frs: Dict[str, dict] = {}
    order: List[str] = []
    for line in doc.splitlines():
        m = re.match(r"^\| (FR-\d{2,3}) \|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|", line)
        if m and m.group(1) != "FR ID":
            fid = m.group(1)
            if fid not in frs:
                order.append(fid)
            frs[fid] = {
                "requirement": m.group(2).strip(),
                "ucs": sorted(set(UC_RE.findall(m.group(3)))),
                "nfrs": sorted(set(NFR_RE.findall(m.group(4)))),
                "rule": m.group(5).strip() if RULE_RE.fullmatch(m.group(5).strip()) else "",
                "verification": m.group(6).strip(),
                "priority": m.group(7).strip(),
            }
    return frs, order


def parse_nfrs() -> Dict[str, dict]:
    """Doc30 NFR table rows: | NFR-NNN | Requirement | Criteria | Source Goals | Source UCs | Priority | NIST |
    Category taken from the enclosing '### 3.x <NAME> (<ABBR>)' section heading."""
    doc = read(BASE / "requirements" / "Doc30_Non_Functional_Requirements.md")
    nfrs: Dict[str, dict] = {}
    category = ""
    for line in doc.splitlines():
        hm = re.match(r"^#{3,4} \d+\.\d+ (.+)$", line)
        if hm:
            category = hm.group(1).strip()
            continue
        m = re.match(r"^\| (NFR-\d{3}) \|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|", line)
        if m and m.group(1) != "NFR ID":
            nfrs[m.group(1)] = {
                "title": m.group(2).strip(),
                "criteria": m.group(3).strip(),
                "goals": sorted(set(re.findall(r"\bAG-D-\d{2}\.\d-\d{3}\b", m.group(4)))),
                "ucs": sorted(set(UC_RE.findall(m.group(5)))),
                "priority": m.group(6).strip(),
                "category": category,
                "rules": sorted(set(RULE_RE.findall(m.group(2) + m.group(3) + m.group(7)))),
            }
    return nfrs


def parse_uc_rule_coverage() -> Dict[str, List[str]]:
    """Doc21 §11 coverage tables: rows 'CR-D-...' -> UCs listed in the row."""
    doc = read(BASE / "Doc21_Use_Cases_Catalog.md")
    uc_to_rules: Dict[str, List[str]] = {}
    section = ""
    for line in doc.splitlines():
        hm = re.match(r"^#+ .*?(UC-\d{2})", line)
        if hm:
            section = hm.group(1)
        for rid in RULE_RE.findall(line):
            if section:
                uc_to_rules.setdefault(section, [])
                if rid not in uc_to_rules[section]:
                    uc_to_rules[section].append(rid)
    return uc_to_rules


def parse_allocations() -> List[Tuple[str, str, List[str]]]:
    """Doc25: rule -> (allocation rows). Returns (rule, derivation_id, nodes)."""
    doc = read(BASE / "Doc25_Requirements_Allocation.md")
    rows: Dict[str, set] = {}
    for line in doc.splitlines():
        m = re.match(r"^\|\s*(DN-[^|]*|(?:CR|BPR)-D-\d{2}\.\d-\d{3})\s*\|", line)
        if m:
            rid = RULE_RE.search(line)
            nodes = sorted(set(NODE_RE.findall(line)))
            if rid and nodes:
                rows.setdefault(rid.group(0), set()).update(nodes)
    return sorted((r, "", sorted(ns)) for r, ns in rows.items())


def parse_gates() -> List[dict]:
    doc = read(BASE / "Doc26_Compliance_Gates_Report.md")
    gates = []
    seen = set()
    for line in doc.splitlines():
        m = re.match(r"^\| (GATE-D-\d{2}\.\d-\d{3}) \|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|", line)
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            gates.append({
                "gate": m.group(1), "name": m.group(2).strip(), "node": m.group(3).strip(),
                "rules": sorted(set(RULE_RE.findall(m.group(4)))),
                "frs": sorted(set(FR_RE.findall(m.group(4) + m.group(5)))),
                "method": m.group(5).strip(),
            })
    return gates


def parse_p2_graph() -> Tuple[int, int, Dict[str, int], Dict[str, int]]:
    g = __import__("json").loads(read(P2 / "data" / "phase2_graph.json"))
    rels: Dict[str, int] = {}
    for l in g["links"]:
        rels[l["rel"]] = rels.get(l["rel"], 0) + 1
    types: Dict[str, int] = {}
    for n in g["nodes"]:
        types[n["type"]] = types.get(n["type"], 0) + 1
    return len(g["nodes"]), len(g["links"]), rels, types


# ---------- sheet builders ----------

def build_cover(wb, stats: Dict[str, object]) -> None:
    ws = wb.active
    ws.title = "COVER"
    rows = [
        ("Document Title", "Phase 3 RICH Traceability Matrix (v0) — Case_02 SecureBorder Solutions"),
        ("Document ID", "AEGIS-C02-P3-TRACE-MATRIX-RICH"),
        ("Phase", "3"),
        ("Case", "Case_02_SecureBorder_Solutions"),
        ("Status", "GENERATED v0 (PORT-PARITY-2) — pending human review"),
        ("Version", "0.0"),
        ("Generated", dt.datetime.now().strftime("%Y-%m-%d %H:%M")),
        ("Generator", "scripts/build_traceability_matrix_rich.py (parses live artefacts; nothing hard-coded)"),
        ("Source — Rules", "../02_PHASE2_RULES_RICH/control_set.yaml (63 controls: 38 CR + 25 BPR)"),
        ("Source — FR", "requirements/Doc29_Functional_Requirements.md (84 FRs)"),
        ("Source — NFR", "requirements/Doc30_Non_Functional_Requirements.md (56 NFRs)"),
        ("Source — UC", "Doc21_Use_Cases_Catalog.md (flat UC-01..UC-34 id space, RENUMBER 2026-09-05)"),
        ("Source — Allocation", "Doc25_Requirements_Allocation.md"),
        ("Source — Gates", "Doc26_Compliance_Gates_Report.md"),
        ("Source — P2 graph", "../02_PHASE2_RULES_RICH/data/phase2_graph.json (278n/356l)"),
        ("Legacy matrix", "22_Traceability_Matrix.xlsx (untouched, kept alongside)"),
        ("Rules total", stats["rules"]),
        ("FRs parsed", stats["frs"]),
        ("FRs with Source Rule", stats["fr_mapped"]),
        ("FRs with Source Rule '—'", stats["fr_unmapped"]),
        ("NFRs parsed", stats["nfrs"]),
        ("Gates parsed", stats["gates"]),
        ("Rule→node allocations parsed", stats["allocs"]),
    ]
    write_header(ws, ["Attribute", "Value"])
    for r, (k, v) in enumerate(rows, start=2):
        ws.cell(row=r, column=1, value=k).font = LABEL_FONT
        ws.cell(row=r, column=2, value=str(v))
    autosize(ws)


def build_rules(wb, controls: List[dict]) -> None:
    ws = wb.create_sheet("RULES")
    write_header(ws, ["#", "Rule ID", "Kind", "Type", "Sub-domain", "NI", "Priority",
                      "Verification", "Source", "Related goals", "CSF", "PF", "AI RMF", "status_csf"])
    for i, c in enumerate(controls, start=1):
        ws.append([i, c["id"], c["kind"], c["type"], c["sub_domain"], c.get("ni", ""),
                   c.get("priority", ""), c.get("verification", ""), c.get("source", ""),
                   c.get("related_goals", ""), c.get("csf", ""), c.get("pf", ""),
                   c.get("airmf", ""), c.get("status_csf", "")])
    autosize(ws)


def build_fr_to_rule(wb, frs: Dict[str, dict], order: List[str]) -> None:
    ws = wb.create_sheet("FR_TO_RULE")
    write_header(ws, ["#", "FR ID", "Rule (Source Rule col)", "UCs", "NFRs", "Verification", "Priority"])
    for i, fid in enumerate(order, start=1):
        f = frs[fid]
        ws.append([i, fid, f["rule"] or "—", ", ".join(f["ucs"]) or "—",
                   ", ".join(f["nfrs"]) or "—", f["verification"], f["priority"]])
    autosize(ws)


def build_rule_to_fr(wb, frs: Dict[str, dict], controls: List[dict]) -> None:
    ws = wb.create_sheet("RULE_TO_FR")
    write_header(ws, ["#", "Rule ID", "Kind", "FR count", "FRs (via Source Rule)", "Coverage gap?"])
    fr_by_rule: Dict[str, List[str]] = {}
    for fid, f in frs.items():
        if f["rule"]:
            fr_by_rule.setdefault(f["rule"], []).append(fid)
    for i, c in enumerate(controls, start=1):
        frs_of = sorted(fr_by_rule.get(c["id"], []))
        ws.append([i, c["id"], c["kind"], len(frs_of), ", ".join(frs_of) or "—",
                   "GAP — no FR cites this rule" if not frs_of else ""])
    autosize(ws)


def build_uc_to_rule(wb, uc_to_rules: Dict[str, List[str]]) -> None:
    ws = wb.create_sheet("UC_TO_RULE")
    write_header(ws, ["#", "UC id (Doc21 detailed card)", "Rules referenced in card section"])
    for i, (uc, rules) in enumerate(sorted(uc_to_rules.items()), start=1):
        ws.append([i, uc, ", ".join(rules)])
    autosize(ws)


def build_rule_to_node(wb, allocs: List[Tuple[str, str, List[str]]]) -> None:
    ws = wb.create_sheet("RULE_TO_NODE")
    write_header(ws, ["#", "Rule ID", "Nodes (Doc25 allocation tables)"])
    for i, (rid, _dn, nodes) in enumerate(allocs, start=1):
        ws.append([i, rid, ", ".join(nodes)])
    autosize(ws)


def build_gates(wb, gates: List[dict]) -> None:
    ws = wb.create_sheet("GATES_STATUS")
    write_header(ws, ["#", "Gate ID", "Name", "Node", "Rules verified", "FRs", "Method"])
    for i, g in enumerate(gates, start=1):
        ws.append([i, g["gate"], g["name"], g["node"], ", ".join(g["rules"]),
                   ", ".join(g["frs"]) or "—", g["method"]])
    autosize(ws)


def build_nfrs(wb, nfrs: Dict[str, dict]) -> None:
    ws = wb.create_sheet("NFRS")
    write_header(ws, ["#", "NFR ID", "Requirement", "Criteria", "Category", "Source goals (AG)", "Source UCs", "Priority", "Rules referenced"])
    for i, (nid, v) in enumerate(sorted(nfrs.items()), start=1):
        ws.append([i, nid, v["title"], v["criteria"], v["category"], ", ".join(v["goals"]) or "—",
                   ", ".join(v["ucs"]) or "—", v["priority"], ", ".join(v["rules"]) or "—"])
    autosize(ws)


def build_p2_graph(wb, stats: Dict[str, object], rels, types) -> None:
    ws = wb.create_sheet("P2_GRAPH_SUMMARY")
    write_header(ws, ["Metric", "Value"])
    ws.append(["nodes", stats["p2_nodes"]])
    ws.append(["links", stats["p2_links"]])
    for t, n in sorted(types.items(), key=lambda x: -x[1]):
        ws.append([f"node type {t}", n])
    for r, n in sorted(rels.items(), key=lambda x: -x[1]):
        ws.append([f"link rel {r}", n])
    autosize(ws)


def main() -> int:
    ap = argparse.ArgumentParser(description="Build 22_Traceability_Matrix_rich_v0.xlsx for Case_02.")
    ap.add_argument("--output", default=None, help="Output xlsx (default: <P3>/22_Traceability_Matrix_rich_v0.xlsx)")
    args = ap.parse_args()
    out = Path(args.output) if args.output else BASE / "22_Traceability_Matrix_rich_v0.xlsx"

    controls = parse_control_set()
    frs, order = parse_frs()
    nfrs = parse_nfrs()
    uc_to_rules = parse_uc_rule_coverage()
    allocs = parse_allocations()
    gates = parse_gates()
    p2_nodes, p2_links, rels, types = parse_p2_graph()

    fr_mapped = sum(1 for f in frs.values() if f["rule"])
    stats = {
        "rules": len(controls), "frs": len(frs), "fr_mapped": fr_mapped,
        "fr_unmapped": len(frs) - fr_mapped, "nfrs": len(nfrs), "gates": len(gates),
        "allocs": len(allocs), "p2_nodes": p2_nodes, "p2_links": p2_links,
    }

    wb = Workbook()
    build_cover(wb, stats)
    build_rules(wb, controls)
    build_fr_to_rule(wb, frs, order)
    build_rule_to_fr(wb, frs, controls)
    build_uc_to_rule(wb, uc_to_rules)
    build_rule_to_node(wb, allocs)
    build_gates(wb, gates)
    build_nfrs(wb, nfrs)
    build_p2_graph(wb, stats, rels, types)

    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)
    print(f"[ok] wrote {out} with {len(wb.sheetnames)} sheets: {', '.join(wb.sheetnames)}")
    print(f"[stats] {stats}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
