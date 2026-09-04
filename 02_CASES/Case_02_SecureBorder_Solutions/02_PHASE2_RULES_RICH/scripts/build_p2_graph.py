#!/usr/bin/env python3
"""
build_p2_graph.py — AEGIS Case_02 Phase 2 Knowledge Graph builder (v1.0)

Ports Case_01's build_p2_graph.py v1.0 (content wave 2026-08-31, commit 7be0b3b)
to the Case_02 corpus. Campaign PORT-PARITY-2, block F4 (2026-09-04).

Parses (all mechanical; doubtful items go to audit nodes):
  * control_set.yaml        (P2 ROOT canonical; 63 controls: 38 CR + 25 BPR)
  * Doc14_Obligation_Derivation.md      (38 obligations, canonical §3.3 tables)
  * Doc15_Strategic_Tensions_Report.md  (9 tensions: §4.1 table + §4.2-4.4 cards)
  * Doc16_Privacy_Security_Goals.md     (34 PO §3.1 + 55 SO §4.1, canonical tables)
  * Doc19 anchors cross-check via control_set@{csf,pf} (pattern-validated)

Emits:
  * data/phase2_graph.json           (meta, company_context, nodes, links,
                                      invariants, ambiguity, audits — shape
                                      mirrors Case_01's phase2_graph.json)
  * data/phase2_ontology.compact.json (compacted from phase2_ontology.yaml v1.0)

No external dependencies beyond PyYAML. Companion validator
build_p2_dashboard.py --check --strict validates counts + IDs.

Usage:
    python3 scripts/build_p2_graph.py --summary
    python3 scripts/build_p2_graph.py --out data/phase2_graph.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
        from yaml import safe_load as yaml_safe_load
except ImportError:
        yaml_safe_load = None

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent  # 02_PHASE2_RULES_RICH/
DATA_DIR = ROOT / "data"
CONTROL_SET = ROOT / "control_set.yaml"  # P2 ROOT canonical (F4)
ONTOLOGY_YAML = ROOT / "phase2_ontology.yaml"
DOC14 = ROOT / "Doc14_Obligation_Derivation.md"
DOC15 = ROOT / "Doc15_Strategic_Tensions_Report.md"
DOC16 = ROOT / "Doc16_Privacy_Security_Goals.md"  # historic Case_02 name kept
DEFAULT_OUT = DATA_DIR / "phase2_graph.json"
DEFAULT_COMPACT = DATA_DIR / "phase2_ontology.compact.json"

# ---------------------------------------------------------------------------
# Constants (invariants from phase2_ontology.yaml v1.0)
# ---------------------------------------------------------------------------
META = {
        "case_id": "Case_02_SecureBorder_Solutions",
        "phase": 2,
        "schema_version": "1.0",
        "generated_date": "2026-09-04",
        "builder": "build_p2_graph.py v1.0 (Case_02 port, PORT-PARITY-2 F4)",
        "ontology_ref": "phase2_ontology.yaml v1.0",
        "compact_ref": "phase2_ontology.compact.json v1.1",
        "maturity_authority": "00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md v1.0",
}

COMPANY = {
        "id": "CC-SECUREBORDER-2026-001",
        "name": "SecureBorder Solutions B.V.",
        "scale": "medium-large",
        "employees": 450,
        "jurisdiction": "Netherlands (EU)",
        "applicable_regs": ["GDPR", "CRA", "NIS2", "AI Act"],
        "phase1_ontology_ref": "../01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml",
}

# Anchor patterns (mechanical validation of control_set@{csf,pf,airmf} fields)
RE_CSF = re.compile(r"^[A-Z]{2}\.[A-Z]{2}-\d{2}$")            # PR.DS-01
RE_PF = re.compile(r"^[A-Z]{2}\.[A-Z]{2}-[A-Z]\d$")           # PR.DS-P1
RE_AIRMF = re.compile(r"^(GOVERN|MAP|MEASURE|MANAGE)-\d+\.\d+$")  # GOVERN-1.6, MEASURE-2.11
RE_OBL = re.compile(r"OBL-D-\d+\.\d+-\d{3}")
RE_OBJ = re.compile(r"[PS]O-D-\d+\.\d+-\d{3}")
RE_AG = re.compile(r"AG-D-\d+\.\d+-\d{3}")
RE_NA = re.compile(r"N/A|—|^-$", re.I)


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------
def parse_control_set() -> tuple[list[dict], list[dict]]:
        """Parse control_set.yaml (Case_02 flat schema) → (cr, bpr).

        Case_02 control entries are flat rows (no nested trace dict like
        Case_01): obligations/objectives are parsed mechanically from the
        traceability string ("SRC → AG-… → OBL-… → PO/SO-…") and the
        related_goals field. Doubtful parses are collected for audits.
        """
        if yaml_safe_load is None:
                raise SystemExit("PyYAML not installed. Install with: pip install pyyaml")
        raw = yaml_safe_load(CONTROL_SET.read_text(encoding="utf-8"))
        controls = raw["control_set"]["controls"]
        cr, bpr = [], []
        for c in controls:
                trace = c.get("traceability", "") or ""
                ni_raw = str(c.get("ni", "") or "")
                m_ni = re.match(r"^(\d+(?:\.\d+)?)", ni_raw)
                entry = {
                        "id": c["id"],
                        "register": "OBLIGATION" if c.get("kind") == "CR" else "BEST_PRACTICE",
                        "domain": c.get("sub_domain", ""),
                        "title": c.get("description", ""),
                        "ni_value": float(m_ni.group(1)) if m_ni else None,
                        "ni_bucket": "P1" if (c.get("priority") == "P1") else c.get("priority", ""),
                        "legal": [s.strip() for s in (c.get("source", "") or "").split(";") if s.strip()],
                        "phase1_goal": sorted(set(RE_AG.findall(trace))),
                        "obligations": sorted(set(RE_OBL.findall(trace))),
                        "objectives": sorted(set(RE_OBJ.findall(trace))
                                             | set(RE_OBJ.findall(c.get("related_goals", "") or ""))),
                        "related_crs": sorted(set(re.findall(r"CR-D-\d+\.\d+-\d{3}", c.get("related_goals", "") or ""))),
                        "anchors_csf": [s.strip() for s in (c.get("csf", "") or "").split(";")
                                        if RE_CSF.match(s.strip())],
                        "anchors_pf": [s.strip() for s in (c.get("pf", "") or "").split(";")
                                       if RE_PF.match(s.strip())],
                        "anchors_airmf": [s.strip() for s in (c.get("airmf", "") or "").split(";")
                                          if RE_AIRMF.match(s.strip())],
                        "doubtful_anchors": [s.strip() for s in (c.get("csf", "") or "").split(";")
                                             + (c.get("pf", "") or "").split(";")
                                             + (c.get("airmf", "") or "").split(";")
                                             if s.strip() and not RE_NA.match(s.strip())
                                             and not (RE_CSF.match(s.strip()) or RE_PF.match(s.strip())
                                                      or RE_AIRMF.match(s.strip()))],
                        "status_csf": c.get("status_csf", ""),
                        "status_privacy": c.get("status_privacy", ""),
                        "status_airmf": c.get("status_airmf", ""),
                        "verification_method": c.get("verification", ""),
                        "source_doc": "control_set.yaml (Doc18 port, P2 ROOT canonical)",
                        "traceability_raw": trace,
                }
                (cr if entry["register"] == "OBLIGATION" else bpr).append(entry)
        return cr, bpr


def parse_doc14_obligations() -> list[dict]:
        """Parse Doc14 canonical obligation tables.

        Canonical row = first cell OBL id, long title cell, clause-ids cell,
        sub-domain cell (D-XX.Y). Other OBL mention tables (NI recalc, coverage,
        derivation-path) do not match this shape and are ignored.
        """
        result: list[dict] = []
        seen: set[str] = set()
        for line in DOC14.read_text(encoding="utf-8").splitlines():
                if not line.startswith("| OBL-"):
                        continue
                cells = [c.strip() for c in line.split("|")[1:-1]]
                if len(cells) < 4:
                        continue
                if not (len(cells[1]) >= 30
                        and re.search(r"(GDPR|CRA|NIS2|AI)-", cells[2])
                        and re.match(r"^D-\d+\.\d$", cells[3])):
                        continue
                oid = cells[0]
                if oid in seen:
                        continue
                seen.add(oid)
                result.append({
                        "id": oid,
                        "subdomain_id": cells[3],
                        "title": cells[1],
                        "source_clauses": [s.strip() for s in cells[2].split(",") if s.strip()],
                        "ni": cells[4] if len(cells) > 4 else "",
                        "source": f"Doc14 §3.3 canonical table row — {oid}",
                })
        return result


def parse_doc16_objectives() -> tuple[list[dict], list[dict]]:
        """Parse Doc16 §3.1 (PO) + §4.1 (SO) canonical tables.

        Row shape: | ID | title | OBL source | D-XX.Y | reg | risk | assurance |
        owner | verification | PF anchors | AI-RMF anchors |
        """
        text = DOC16.read_text(encoding="utf-8")
        po: list[dict] = []
        so: list[dict] = []
        for line in text.splitlines():
                m = re.match(r"^\| ((?:PO|SO)-D-\d+\.\d+-\d{3}) \|", line)
                if not m:
                        continue
                cells = [c.strip() for c in line.split("|")[1:-1]]
                if len(cells) < 4 or len(cells[1]) < 20 or not re.match(r"^OBL-D-\d+\.\d+-\d{3}$", cells[2]):
                        continue
                oid = m.group(1)
                entry = {
                        "id": oid,
                        "subdomain_id": cells[3],
                        "title": cells[1],
                        "derives_from_obligation": cells[2],
                        "reg_driver": cells[4] if len(cells) > 4 else "",
                        "anchors_pf": [s.strip() for s in (cells[9] if len(cells) > 9 else "").split(",") if s.strip()],
                        "anchors_airmf": [s.strip() for s in (cells[10] if len(cells) > 10 else "").split(",") if s.strip()],
                        "source": f"Doc16 §{'3.1' if oid.startswith('PO') else '4.1'} canonical table row — {oid}",
                }
                (po if oid.startswith("PO") else so).append(entry)
        return po, so


def parse_doc15_tensions(obligations: list[dict]) -> list[dict]:
        """Parse Doc15 §4.1 classification table + §4.2-4.4 cards (9 tensions).

        §4.1 row: | T-NNN | TYPE | **SEVERITY** | **Nature** | Yes/No | overlap | RESOLUTION |
        Card:     #### T-NNN: Title — NATURE  +  | **Sub-Domain** | D-XX.Y (...) |
                                             +  | **Conflicting Obligations** | OBL-… |
                                             +  | **Source Regulations** | … |
        """
        text = DOC15.read_text(encoding="utf-8")
        # §4.1 summary rows
        summary: dict[str, dict] = {}
        sec41 = text.split("### 4.1")[1].split("### 4.2")[0]
        for line in sec41.splitlines():
                m = re.match(r"^\| (T-\d{3}) \|", line)
                if not m:
                        continue
                cells = [c.strip() for c in line.split("|")[1:-1]]
                if len(cells) < 7:
                        continue
                summary[m.group(1)] = {
                        "type": cells[1],
                        "severity": cells[2].strip("*").upper(),
                        "nature": cells[3].strip("*").upper(),
                        "always_active": cells[4].lower() == "yes",
                        "overlap_condition": cells[5],
                        "resolution_approach": cells[6],
                }
        # Cards
        cards: dict[str, dict] = {}
        for m in re.finditer(r"^#### (T-\d{3}): (.+?) — ([A-Z]+)\s*$", text, re.M):
            cards[m.group(1)] = {"title": m.group(2).strip(), "header_nature": m.group(3)}
        for tid, card in cards.items():
                # the card's own attribute table follows its header
                start = text.find(f"#### {tid}:")
                nxt = re.search(r"^#### T-\d{3}:", text[start + 10:], re.M)
                body = text[start: start + 10 + (nxt.start() if nxt else len(text))]
                fm = re.search(r"\|\s*\*{0,2}Sub-Domain\*{0,2}\s*\|\s*(.+?)\|", body)
                card["subdomain_field"] = fm.group(1).strip() if fm else ""
                om = re.search(r"Conflicting Obligations\*{0,2}\s*\|\s*(.+?)\|", body)
                card["obligations_field"] = om.group(1).strip() if om else ""
                rm = re.search(r"Source Regulations\*{0,2}\s*\|\s*(.+?)\|", body)
                card["regs_field"] = rm.group(1).strip() if rm else ""
                dm = re.search(r"Resolution Description\*{0,2}\s*\|\s*(.+?)\|", body)
                card["resolution_description"] = dm.group(1).strip() if dm else ""

        obl_by_sub = {o["subdomain_id"]: o["id"] for o in obligations}
        tensions: list[dict] = []
        for tid in sorted(set(summary) | set(cards)):
                s = summary.get(tid, {})
                c = cards.get(tid, {})
                sub_field = c.get("subdomain_field", "")
                sds = sorted(set(re.findall(r"D-\d+\.\d", sub_field)))
                # explicit OBL refs else sub-domain pairing (C1 GENERATES rule)
                obl_refs = sorted(set(RE_OBL.findall(c.get("obligations_field", ""))))
                if not obl_refs:
                        pairing = [obl_by_sub[sd] for sd in sds if sd in obl_by_sub]
                        obl_refs = pairing
                regs_field = c.get("regs_field", "") or s.get("overlap_condition", "")
                regs = sorted(set(re.findall(r"GDPR|CRA|NIS\s*2|NIS2|AI[_ ]?Act|DORA", regs_field, re.I)))
                tensions.append({
                        "id": tid,
                        "title": c.get("title", tid),
                        "nature": s.get("nature", c.get("header_nature", "")).upper(),
                        "severity": s.get("severity", ""),
                        "type": s.get("type", ""),
                        "always_active": s.get("always_active", False),
                        "overlap_condition": s.get("overlap_condition", ""),
                        "affected_subdomains": sds,
                        "affected_regulations": regs,
                        "resolution_approach": s.get("resolution_approach", ""),
                        "resolution_description": c.get("resolution_description", ""),
                        "generates_from": obl_refs,
                        "source_doc": f"Doc15 §4.1 table + §4 card {tid}",
                        "parse_complete": bool(s) and bool(c),
                })
        return tensions


def collect_nist_subcategories(controls: list[dict]) -> list[dict]:
        """CSF + PF subcategory nodes from pattern-validated control anchors
        (mechanical; mirrors Case_01's Doc19/control_set enumeration)."""
        csf_set, pf_set = set(), set()
        for c in controls:
                csf_set.update(c["anchors_csf"])
                pf_set.update(c["anchors_pf"])
        result = []
        for sub in sorted(csf_set):
                result.append({"id": f"NIST-CSF-{sub}", "control_id": sub, "framework": "CSF",
                               "function": sub.split(".")[0], "source_doc": "control_set.yaml@csf"})
        for sub in sorted(pf_set):
                result.append({"id": f"NIST-PF-{sub}", "control_id": sub, "framework": "PF",
                               "function": sub.split(".")[0], "source_doc": "control_set.yaml@pf"})
        return result


# ---------------------------------------------------------------------------
# Compact ontology emitter (from phase2_ontology.yaml — mechanical)
# ---------------------------------------------------------------------------
def emit_compact() -> dict:
        if yaml_safe_load is None:
                raise SystemExit("PyYAML not installed")
        y = yaml_safe_load(ONTOLOGY_YAML.read_text(encoding="utf-8"))
        kg = y["kg_ontology"]
        compact = {
                "_provenance": {
                        "source_yaml": "02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/phase2_ontology.yaml",
                        "schema_version": 1.1,
                        "generated": META["generated_date"],
                        "generator": "build_p2_graph.py v1.0 (emits from YAML — mechanical)",
                        "phase1_reference": "01_PHASE1_CONTEXT_RICH/data/phase1_ontology.compact.json",
                },
                "classes": {name: {"attrs": list(spec.get("attrs", {}).keys()),
                                   "example": spec.get("example", "")}
                            for name, spec in kg["classes"].items()},
                "relations": [{"verb": r["verb"], "from": r["from"], "to": r["to"],
                               "cardinality": r.get("cardinality", "")}
                              for r in kg["relations"]],
                "enums": kg["enums"],
                "invariants": {"id_patterns": kg["invariants"]["id_patterns"],
                               "counts": kg["invariants"]["counts"]},
                "provenance_rules": {
                        "every_node_must_have_source": True,
                        "every_relation_must_have_source": True,
                        "node_id_pattern_match_class": True,
                        "invariants_are_minimums_not_maximums": True,
                },
                "maturity_model": {
                        "authority": kg["maturity_model"]["authority"],
                        "reference_framework": kg["maturity_model"]["reference_framework"],
                        "crosswalk_authority": kg["maturity_model"]["crosswalk_authority"],
                        "schema_version": kg["maturity_model"]["schema_version"],
                        "generated": kg["maturity_model"]["generated"],
                        "phase1_reference": kg["maturity_model"]["phase1_reference"],
                },
        }
        return compact


# ---------------------------------------------------------------------------
# Graph emitter
# ---------------------------------------------------------------------------
def build_graph() -> dict[str, Any]:
        cr, bpr = parse_control_set()
        obligations = parse_doc14_obligations()
        po_nodes, so_nodes = parse_doc16_objectives()
        tensions = parse_doc15_tensions(obligations)
        all_controls = cr + bpr
        nist_nodes = collect_nist_subcategories(all_controls)

        # BPR → objectives derived transitively via related CRs (Case_02 BPRs
        # name CR ids in related_goals, not objectives). Mechanical closure;
        # links flagged as derived.
        cr_by_id = {c["id"]: c for c in cr}
        for b in bpr:
                derived: set[str] = set()
                for crid in b["related_crs"]:
                        r = cr_by_id.get(crid)
                        if r:
                                derived.update(r["objectives"])
                b["objectives"] = sorted(derived)

        nodes: list[dict] = []
        nodes.append({
                "id": COMPANY["id"],
                "type": "CompanyContext",
                "label": COMPANY["name"],
                "attrs": {
                        "scale": COMPANY["scale"],
                        "employees": COMPANY["employees"],
                        "jurisdiction": COMPANY["jurisdiction"],
                        "applicable_regs": COMPANY["applicable_regs"],
                },
                "source": "phase2_ontology.yaml@company (carried from P1 v2.3)",
        })

        rule_ids_by_obl: dict[str, list[str]] = {}
        for c in all_controls:
                for oid in c["obligations"]:
                        rule_ids_by_obl.setdefault(oid, []).append(c["id"])

        for obl in obligations:
                related = rule_ids_by_obl.get(obl["id"], [])
                obj_addressed = sorted({o for rid in related
                                        for o in (cr_by_id.get(rid, {}).get("objectives", []))})
                nodes.append({
                        "id": obl["id"],
                        "type": "Obligation",
                        "label": f"{obl['id']} ({obl['subdomain_id']})",
                        "attrs": {
                                "subdomain_id": obl["subdomain_id"],
                                "title": obl["title"],
                                "description": obl["title"],
                                "normative_intensity": float(obl["ni"]) if obl["ni"] else None,
                                "priority": "MUST",
                                "verification_method": "TEST + INSPECT",
                                "owner": "Compliance Lead",
                                "risks_if_not_met": "Regulatory non-compliance; market-access risk (CRA certification).",
                                "source_clauses": obl["source_clauses"],
                                "addressed_by_rules": related,
                                "yields_objectives": obj_addressed,
                        },
                        "source": obl["source"],
                })

        for po in po_nodes:
                nodes.append({
                        "id": po["id"],
                        "type": "PrivacyOperationalObjective",
                        "label": f"{po['id']} (PO)",
                        "attrs": {
                                "subdomain_id": po["subdomain_id"],
                                "title": po["title"],
                                "description": po["title"],
                                "derives_from_obligation_id": po["derives_from_obligation"],
                                "nist_csf_anchors": [],
                                "nist_pf_anchors": po["anchors_pf"],
                                "reg_driver": po["reg_driver"],
                                "priority": "MUST",
                                "verification_method": "INSPECT",
                        },
                        "source": po["source"],
                })
        for so in so_nodes:
                nodes.append({
                        "id": so["id"],
                        "type": "SecurityOperationalObjective",
                        "label": f"{so['id']} (SO)",
                        "attrs": {
                                "subdomain_id": so["subdomain_id"],
                                "title": so["title"],
                                "description": so["title"],
                                "derives_from_obligation_id": so["derives_from_obligation"],
                                "nist_csf_anchors": [],
                                "nist_pf_anchors": so["anchors_pf"],
                                "reg_driver": so["reg_driver"],
                                "priority": "MUST",
                                "verification_method": "TEST",
                        },
                        "source": so["source"],
                })

        for c in all_controls:
                ntype = "ComplianceRule" if c["register"] == "OBLIGATION" else "BestPracticeRule"
                nodes.append({
                        "id": c["id"],
                        "type": ntype,
                        "label": f"{c['id']} — {c['title'][:80]}",
                        "attrs": {
                                "subdomain_id": c["domain"],
                                "title": c["title"],
                                "register": c["register"],
                                "normative_intensity": c["ni_value"],
                                "bucket": c["ni_bucket"],
                                "legal": c["legal"],
                                "phase1_goal_id": ", ".join(c["phase1_goal"]),
                                "obligations_addressed": c["obligations"],
                                "objectives_addressed": c["objectives"],
                                "related_crs": c["related_crs"],
                                "anchors_csf": c["anchors_csf"],
                                "anchors_pf": c["anchors_pf"],
                                "anchors_airmf": c["anchors_airmf"],
                                "status_csf": c["status_csf"],
                                "status_privacy": c["status_privacy"],
                                "status_airmf": c["status_airmf"],
                                "verification_method": c["verification_method"],
                                "verification_owner": "CTO Office",
                        },
                        "source": c["source_doc"],
                })

        for t in tensions:
                nodes.append({
                        "id": t["id"],
                        "type": "Tension",
                        "label": f"{t['id']} — {t['title']}",
                        "attrs": {
                                "title": t["title"],
                                "nature": t["nature"],
                                "severity": t["severity"],
                                "type": t["type"],
                                "always_active": t["always_active"],
                                "clause_1": ", ".join(t["affected_regulations"]) or "—",
                                "clause_2": "",
                                "overlap_condition": t["overlap_condition"],
                                "affected_subdomains": t["affected_subdomains"],
                                "affected_regulations": t["affected_regulations"],
                                "resolution_approach": t["resolution_approach"],
                                "resolution_description": t["resolution_description"],
                                "parse_complete": t["parse_complete"],
                        },
                        "source": t["source_doc"],
                })

        for ns in nist_nodes:
                nodes.append({
                        "id": ns["id"],
                        "type": "NistSubcategory",
                        "label": ns["control_id"],
                        "attrs": {
                                "control_id": ns["control_id"],
                                "framework": ns["framework"],
                                "function": ns["function"],
                                "description": f"{ns['framework']} {ns['control_id']} — {ns['function']} function",
                        },
                        "source": ns["source_doc"],
                })

        # ---- Links ----
        links: list[dict] = []
        for c in all_controls:
                for obj_id in c["objectives"]:
                        links.append({
                                "from": c["id"], "to": obj_id, "rel": "MITIGATES",
                                "attrs": {"kind": c["register"],
                                          "derived": c["register"] == "BEST_PRACTICE"},
                                "source": ("control_set.yaml@{traceability,related_goals}"
                                           if c["register"] == "OBLIGATION"
                                           else "derived: BPR@related_goals → CR@objectives (mechanical closure)"),
                        })
                for sub in c["anchors_csf"]:
                        links.append({"from": c["id"], "to": f"NIST-CSF-{sub}", "rel": "MAPS_TO",
                                      "attrs": {"framework": "CSF"},
                                      "source": "control_set.yaml@csf"})
                for sub in c["anchors_pf"]:
                        links.append({"from": c["id"], "to": f"NIST-PF-{sub}", "rel": "MAPS_TO",
                                      "attrs": {"framework": "PF"},
                                      "source": "control_set.yaml@pf"})

        for po in po_nodes + so_nodes:
                links.append({
                        "from": po["derives_from_obligation"], "to": po["id"], "rel": "YIELDS",
                        "attrs": {}, "source": "Doc16 §3.1/§4.1 source-obligation column",
                })

        for t in tensions:
                for oid in t["generates_from"]:
                        links.append({
                                "from": oid, "to": t["id"], "rel": "GENERATES",
                                "attrs": {"severity": t["severity"]},
                                "source": "Doc15 §4 card (Conflicting Obligations / Sub-Domain pairing)",
                        })

        # de-dup links (same from/to/rel triple)
        seen: set[tuple] = set()
        deduped = []
        for l in links:
                k = (l["from"], l["to"], l["rel"])
                if k in seen:
                        continue
                seen.add(k)
                deduped.append(l)
        links = deduped

        # ---- Invariants (mechanical counts) ----
        counts = {
                "obligations_total": len(obligations),
                "po_total": len(po_nodes),
                "so_total": len(so_nodes),
                "objectives_total": len(po_nodes) + len(so_nodes),
                "compliance_rules_total": len(cr),
                "best_practice_rules_total": len(bpr),
                "controls_total": len(all_controls),
                "tensions_total": len(tensions),
                "source_clauses_total": 111,  # phase1_ontology v2.3@case_invariants.total_clauses
                "applicable_regs": len(COMPANY["applicable_regs"]),
                "nist_subcategories_total": len(nist_nodes),
                "nodes_total": len(nodes),
                "links_total": len(links),
        }

        ambiguity = {
                "stats_total": {"S1_high": 0, "S2_medium": 0, "S3_low": 0, "total_cards": 0},
                "source_doc": "Phase 2 carries zero ambiguity cards (ambiguity is a P1 concern; P2 formalises obligations/objectives).",
        }

        # ---- Audits (conditional; Case_01 AUD-P2-001..006 scheme) ----
        audits = []
        cr_without_obl = [c["id"] for c in cr if not c["obligations"]]
        if cr_without_obl:
                audits.append({"id": "AUD-P2-001", "kind": "structural", "node_ids": cr_without_obl,
                               "title": f"{len(cr_without_obl)} CR(s) without obligation linkage",
                               "severity": "high", "source": "control_set.yaml@traceability"})
        trace_shape_fail = [c["id"] for c in all_controls
                            if not c["phase1_goal"] and c["register"] == "OBLIGATION"]
        if trace_shape_fail:
                audits.append({"id": "AUD-P2-002", "kind": "structural", "node_ids": trace_shape_fail,
                               "title": f"{len(trace_shape_fail)} control(s) whose traceability lacks the AG- segment",
                               "severity": "medium", "source": "control_set.yaml@traceability"})
        tensions_incomplete = [t["id"] for t in tensions if not t["parse_complete"]]
        if tensions_incomplete:
                audits.append({"id": "AUD-P2-003", "kind": "structural", "node_ids": tensions_incomplete,
                               "title": f"{len(tensions_incomplete)} tension(s) with incomplete §4.1/card parse",
                               "severity": "low", "source": "Doc15 §4"})
        po_addressed = {o for c in all_controls for o in c["objectives"] if o.startswith("PO-")}
        po_orphan = [p["id"] for p in po_nodes if p["id"] not in po_addressed]
        if po_orphan:
                audits.append({"id": "AUD-P2-004", "kind": "orphan_check", "node_ids": po_orphan,
                               "title": f"{len(po_orphan)} PO(s) without a CR/BPR addressing them",
                               "severity": "medium",
                               "source": "control_set.yaml@{traceability,related_goals} (+ derived BPR closure)"})
        so_addressed = {o for c in all_controls for o in c["objectives"] if o.startswith("SO-")}
        so_orphan = [s["id"] for s in so_nodes if s["id"] not in so_addressed]
        if so_orphan:
                audits.append({"id": "AUD-P2-005", "kind": "orphan_check", "node_ids": so_orphan,
                               "title": f"{len(so_orphan)} SO(s) without a CR/BPR addressing them",
                               "severity": "medium",
                               "source": "control_set.yaml@{traceability,related_goals} (+ derived BPR closure)"})
        # AUD-P2-005 in Case_01's numbering is the ORPHAN-OBLIGATION audit; for
        # numbering parity the obligation orphan check keeps the id AUD-P2-005b
        # when the PO/SO checks fire, else AUD-P2-005 (same as Case_01).
        obl_addressed = {o for c in all_controls for o in c["obligations"]}
        obl_orphan = [o["id"] for o in obligations if o["id"] not in obl_addressed]
        if obl_orphan:
                audits.append({"id": "AUD-P2-005", "kind": "orphan_check", "node_ids": obl_orphan,
                               "title": f"{len(obl_orphan)} obligation(s) without a CR addressing them",
                               "severity": "high", "source": "control_set.yaml@traceability"})
        cr_no_anchor = [c["id"] for c in cr if not c["anchors_csf"] and not c["anchors_pf"]]
        if cr_no_anchor:
                audits.append({"id": "AUD-P2-006", "kind": "nist_alignment", "node_ids": cr_no_anchor,
                               "title": f"{len(cr_no_anchor)} CR(s) without CSF or PF anchors",
                               "severity": "low", "source": "control_set.yaml@{csf,pf}"})
        doubtful = {d for c in all_controls for d in c["doubtful_anchors"]}
        if doubtful:
                audits.append({"id": "AUD-P2-007", "kind": "parse_anomaly",
                               "node_ids": sorted(c["id"] for c in all_controls if c["doubtful_anchors"]),
                               "title": (f"{len(doubtful)} anchor token(s) in control_set csf/pf/airmf fields "
                                         "match no known framework pattern (quoted verbatim; not linked)"),
                               "severity": "low", "source": "control_set.yaml csf/pf/airmf fields"})

        return {
                "meta": META,
                "company_context": nodes[0],
                "nodes": nodes,
                "links": links,
                "invariants": {"counts": counts},
                "ambiguity": ambiguity,
                "audits": audits,
        }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> int:
        ap = argparse.ArgumentParser(description="Build Phase 2 graph JSON for Case_02")
        ap.add_argument("--out", default=str(DEFAULT_OUT), help="Output graph JSON path")
        ap.add_argument("--compact-out", default=str(DEFAULT_COMPACT), help="Output compact ontology path")
        ap.add_argument("--no-compact", action="store_true", help="Skip compact ontology emission")
        ap.add_argument("--summary", action="store_true", help="Print counts summary")
        args = ap.parse_args()

        graph = build_graph()
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8")

        if not args.no_compact:
                compact = emit_compact()
                cout = Path(args.compact_out)
                cout.parent.mkdir(parents=True, exist_ok=True)
                cout.write_text(json.dumps(compact, indent=2, ensure_ascii=False), encoding="utf-8")

        counts = graph["invariants"]["counts"]
        if args.summary:
                print(f"[build_p2_graph] wrote {out}")
                if not args.no_compact:
                        print(f"[build_p2_graph] wrote {args.compact_out}")
                print(f"[build_p2_graph] counts: {json.dumps(counts, indent=2)}")
                print(f"[build_p2_graph] audits: {len(graph['audits'])}")
                for a in graph["audits"]:
                        print(f"  - {a['id']} [{a['kind']}] {a['title']}")
        return 0


if __name__ == "__main__":
        sys.exit(main())
