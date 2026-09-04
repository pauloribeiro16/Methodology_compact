#!/usr/bin/env python3
"""
build_p2_graph.py — AEGIS Case_03 Phase 2 Knowledge Graph builder (v1.0)

Ports Case_01's build_p2_graph.py v1.0 (content wave 2026-08-31, commit 7be0b3b)
to the Case_03 corpus. Campaign PORT-PARITY-2, block F4 (2026-09-04).

Parses (all mechanical; doubtful items go to audit nodes):
  * control_set.yaml        (P2 ROOT canonical; 78 controls: 38 CR + 40 BPR —
                             the '**' assert from the posture model §4)
  * Doc15_Obligation_Derivation.md      (38 obligations, canonical tables)
  * Doc16_Strategic_Tensions_Report.md  (4 tension cards TENSION-{H,M,L}-NNN +
                             §4.1 note declaring canonical set T-001..T-005;
                             T-005/TENSION-M-002 analysis lives in P1 Doc11 §4.5)
  * Doc17_Privacy_Security_Objectives.md (AG- id space: §3 privacy rows +
                             §4 security rows — 12 shared; counts audited vs
                             the doc's own §3.5/§4 summaries)
  * Doc20 cross-check via control_set anchors (pattern-classified)

Case_03 traceability chain: Rule → AG (Phase-1 Adjusted Goal) → OBL → clauses.
control_set@related_goals carries AG ids; Doc17 AG rows carry source
obligations — the OBL→Rule back-link is derived mechanically through that chain.

Emits:
  * data/phase2_graph.json           (shape mirrors Case_01's phase2_graph.json)
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
DOC15 = ROOT / "Doc15_Obligation_Derivation.md"
DOC16 = ROOT / "Doc16_Strategic_Tensions_Report.md"
DOC17 = ROOT / "Doc17_Privacy_Security_Objectives.md"
DEFAULT_OUT = DATA_DIR / "phase2_graph.json"
DEFAULT_COMPACT = DATA_DIR / "phase2_ontology.compact.json"

META = {
        "case_id": "Case_03_OmniBank_Financial",
        "phase": 2,
        "schema_version": "1.0",
        "generated_date": "2026-09-04",
        "builder": "build_p2_graph.py v1.0 (Case_03 port, PORT-PARITY-2 F4)",
        "ontology_ref": "phase2_ontology.yaml v1.0",
        "compact_ref": "phase2_ontology.compact.json v1.1",
        "maturity_authority": "00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md v1.0",
}

COMPANY = {
        "id": "CC-OMNIBANK-2026-001",
        "name": "OmniBank Financial Systems S.A.",
        "scale": "large",
        "employees": 5000,
        "jurisdiction": "Germany (EU)",
        "applicable_regs": ["GDPR", "CRA", "NIS2", "DORA", "AI Act"],
        "phase1_ontology_ref": "../01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml",
}

# Anchor patterns — tokens are classified by their OWN pattern regardless of
# which control_set field carried them (C3 BPR rows have PF-style ids in the
# csf field); mismatched/non-matching tokens go to the doubtful audit.
RE_CSF = re.compile(r"^[A-Z]{2}\.[A-Z]{2}-\d{2}$")            # PR.DS-01
RE_PF = re.compile(r"^[A-Z]{2}\.[A-Z]{2}-[A-Z]\d$")           # PR.DS-P1
RE_AIRMF = re.compile(r"^(GOVERN|MAP|MEASURE|MANAGE)-\d+\.\d+$")  # GOVERN-1.6, MEASURE-2.11
RE_OBL = re.compile(r"OBL-D-\d+\.\d+-\d{3}")
RE_AG = re.compile(r"AG-D-\d+\.\d+-\d{3}")
RE_NA = re.compile(r"N/A|—|^-$|^CM\.AW-P\*$", re.I)


def classify_token(tok: str) -> str | None:
        if RE_CSF.match(tok):
                return "CSF"
        if RE_PF.match(tok):
                return "PF"
        if RE_AIRMF.match(tok):
                return "AI-RMF"
        return None


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------
def parse_control_set() -> tuple[list[dict], list[dict]]:
        if yaml_safe_load is None:
                raise SystemExit("PyYAML not installed. Install with: pip install pyyaml")
        raw = yaml_safe_load(CONTROL_SET.read_text(encoding="utf-8"))
        controls = raw["control_set"]["controls"]
        cr, bpr = [], []
        for c in controls:
                trace = c.get("traceability", "") or ""
                related = c.get("related_goals", "") or ""
                # anchors: classify every token in csf/pf/airmf fields by pattern
                raw_toks: list[str] = []
                for field in ("csf", "pf", "airmf"):
                        raw_toks += [t.strip() for t in (c.get(field) or "").replace(",", ";").split(";")]
                anchors = {"CSF": [], "PF": [], "AI-RMF": []}
                doubtful: list[str] = []
                for t in raw_toks:
                        if not t or RE_NA.match(t):
                                continue
                        fw = classify_token(t)
                        if fw and t not in anchors[fw]:
                                anchors[fw].append(t)
                        elif not fw and t not in doubtful:
                                doubtful.append(t)
                goals = sorted(set(RE_AG.findall(related)) | set(RE_AG.findall(trace)))
                entry = {
                        "id": c["id"],
                        "register": "OBLIGATION" if c.get("kind") == "CR" else "BEST_PRACTICE",
                        "domain": c.get("sub_domain", ""),
                        "title": c.get("description", ""),
                        "ni_value": None,  # Case_03 control_set carries no ni field
                        "ni_bucket": c.get("priority", ""),
                        "legal": [s.strip() for s in re.split(r";", (c.get("source", "") or "")) if s.strip()],
                        "phase1_goal": goals,
                        "obligations": [],  # derived via AG chain below
                        "objectives": goals,
                        "native": related.strip().upper() == "NATIVE",
                        "anchors_csf": anchors["CSF"],
                        "anchors_pf": anchors["PF"],
                        "anchors_airmf": anchors["AI-RMF"],
                        "doubtful_anchors": doubtful,
                        "status_csf": c.get("status_csf", ""),
                        "status_privacy": c.get("status_privacy", ""),
                        "status_airmf": c.get("status_airmf", ""),
                        "verification_method": c.get("verification", ""),
                        "source_doc": "control_set.yaml (Doc19 port, P2 ROOT canonical)",
                        "traceability_raw": trace,
                }
                (cr if entry["register"] == "OBLIGATION" else bpr).append(entry)
        return cr, bpr


def parse_doc15_obligations() -> list[dict]:
        """Canonical obligation tables: | OBL | title | clauses | D-XX.Y | NI | cadence | roles |."""
        result: list[dict] = []
        seen: set[str] = set()
        for line in DOC15.read_text(encoding="utf-8").splitlines():
                if not line.startswith("| OBL-"):
                        continue
                cells = [c.strip() for c in line.split("|")[1:-1]]
                if len(cells) < 4:
                        continue
                if not (len(cells[1]) >= 30
                        and re.search(r"(GDPR|CRA|NIS2|AI|DORA)-", cells[2])
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
                        "source_clauses": [s.strip() for s in re.split(r"[;,]", cells[2]) if s.strip()],
                        "ni": cells[4] if len(cells) > 4 else "",
                        "source": f"Doc15 canonical table row — {oid}",
                })
        return result


def parse_doc17_objectives() -> tuple[list[dict], list[dict], list[str]]:
        """Parse Doc17 §3 (privacy AG rows) + §4 (security AG rows).

        Row shape: | AG-D-XX.Y-NNN | description | OBL source(s) | risk | priority |
        CSF anchors | PF anchors | AI RMF anchors |
        Returns (privacy, security_unique, duplicate_ids_in_sec4).
        §4 re-lists the §3 privacy rows; security class = §4 ids not in §3.
        """
        text = DOC17.read_text(encoding="utf-8")
        sec3 = text.split("## 3. PRIVACY OBJECTIVES CATALOG")[1].split("## 4. SECURITY OBJECTIVES CATALOG")[0]
        sec4 = text.split("## 4. SECURITY OBJECTIVES CATALOG")[1]

        def rows(block: str, section: str) -> list[dict]:
                out = []
                for line in block.splitlines():
                        m = re.match(r"^\| (AG-D-\d+\.\d+-\d{3}) \|", line)
                        if not m:
                                continue
                        cells = [c.strip() for c in line.split("|")[1:-1]]
                        if len(cells) < 8 or len(cells[1]) < 20:
                                continue
                        out.append({
                                "id": m.group(1),
                                "title": cells[1],
                                "source_obligations": RE_OBL.findall(cells[2]),
                                "risk_profile": cells[3],
                                "priority": cells[4],
                                "anchors_csf": [s.strip() for s in cells[5].split(",") if RE_CSF.match(s.strip())],
                                "anchors_pf": [s.strip() for s in cells[6].split(",") if RE_PF.match(s.strip())],
                                "anchors_airmf": [s.strip() for s in cells[7].split(",") if RE_AIRMF.match(s.strip())],
                                "source": f"Doc17 §{section} canonical table row — {m.group(1)}",
                        })
                return out

        privacy = rows(sec3, "3")
        sec4_rows = rows(sec4, "4")
        privacy_ids = {p["id"] for p in privacy}
        sec4_ids = {r["id"] for r in sec4_rows}
        # duplicates within §4 (26 ids appear twice — audit-only info)
        id_counts: dict[str, int] = {}
        for line in sec4.splitlines():
                m = re.match(r"^\| (AG-D-\d+\.\d+-\d{3}) \|", line)
                if m and len(m.group(0)) > 0:
                        id_counts[m.group(1)] = id_counts.get(m.group(1), 0) + 1
        dup4 = sorted(k for k, v in id_counts.items() if v > 1)
        security = [r for r in sec4_rows if r["id"] not in privacy_ids]
        # de-dup security by id (first occurrence wins)
        seen: set[str] = set()
        sec_unique = []
        for r in security:
                if r["id"] in seen:
                        continue
                seen.add(r["id"])
                sec_unique.append(r)
        return privacy, sec_unique, dup4


def parse_doc16_tensions(obligations: list[dict]) -> tuple[list[dict], list[str]]:
        """Parse Doc16 tensions: §4.1 summary table + §4.2-4.3 cards + §4.1 note.

        Card ids are used verbatim (TENSION-{H,M,L}-NNN). The §4.1 note declares
        the canonical set as T-001..T-005 and defines T-005 = TENSION-M-002
        (DORA TLPT, analysed in P1 Doc11 §4.5) — emitted as node T-005.
        Returns (tensions, parse_notes) — parse_notes feed AUD-P2-009.
        """
        text = DOC16.read_text(encoding="utf-8")
        notes: list[str] = []
        sec41 = text.split("### 4.1")[1].split("### 4.2")[0]
        summary: dict[str, dict] = {}
        for line in sec41.splitlines():
                m = re.match(r"^\| ((?:TENSION-[HML]-\d{3}|T-\d{3})) \|", line)
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
        cards: dict[str, dict] = {}
        for m in re.finditer(r"^#### (TENSION-[HML]-\d{3}): (.+?) -- ([A-Z_]+)\s*$", text, re.M):
                cards[m.group(1)] = {"title": m.group(2).strip(), "type": m.group(3)}
        for tid, card in cards.items():
                start = text.find(f"#### {tid}:")
                nxt = re.search(r"^#### TENSION-", text[start + 10:], re.M)
                body = text[start: start + 10 + (nxt.start() if nxt else len(text))]
                fm = re.search(r"\|\s*Sub-Domains?\s*\|\s*(.+?)\|", body)
                card["subdomain_field"] = fm.group(1).strip() if fm else ""
                om = re.search(r"\|\s*Obligation IDs?\s*\|\s*(.+?)\|", body)
                card["obligations_field"] = om.group(1).strip() if om else ""
                rm = re.search(r"\|\s*Source Clauses\s*\|\s*(.+?)\|", body)
                card["regs_field"] = rm.group(1).strip() if rm else ""
                resm = re.search(r"\*\*Resolution Type\*\*\s*\|\s*\*\*(.+?)\*\*", body)
                card["resolution_type"] = resm.group(1).strip() if resm else ""

        obl_by_sub = {o["subdomain_id"]: o["id"] for o in obligations}
        tensions: list[dict] = []
        for tid in sorted(set(summary) | set(cards)):
                s = summary.get(tid, {})
                c = cards.get(tid, {})
                sub_field = c.get("subdomain_field", "")
                sds = sorted(set(re.findall(r"D-\d+\.\d", sub_field)))
                obl_refs = sorted(set(RE_OBL.findall(c.get("obligations_field", ""))))
                if not obl_refs:
                        obl_refs = [obl_by_sub[sd] for sd in sds if sd in obl_by_sub]
                regs = sorted(set(re.findall(r"GDPR|CRA|NIS\s*2|NIS2|AI[_ ]?Act|DORA",
                                             (c.get("regs_field", "") or "") + " " + s.get("overlap_condition", ""),
                                             re.I)))
                tensions.append({
                        "id": tid,
                        "title": c.get("title", tid),
                        "nature": s.get("nature", ""),
                        "severity": s.get("severity", ""),
                        "type": s.get("type", c.get("type", "")),
                        "always_active": s.get("always_active", False),
                        "overlap_condition": s.get("overlap_condition", ""),
                        "affected_subdomains": sds,
                        "affected_regulations": regs,
                        "resolution_approach": s.get("resolution_approach", c.get("resolution_type", "")),
                        "resolution_description": "",
                        "generates_from": obl_refs,
                        "source_doc": f"Doc16 §4.1 table + §4 card {tid}",
                        "parse_complete": bool(s) and bool(c),
                        "alias": "",
                })

        # T-005 / TENSION-M-002 from the §4.1 note (canonical-set declaration)
        note_m = re.search(r"`TENSION-M-002` / \*\*T-005\*\* — (.+?), (D-[\d.]+ \+ D-[\d.]+), (MEDIUM|HIGH|LOW|CRITICAL), (STRUCTURAL|CONTEXTUAL)", sec41, re.I)
        t5 = {
                "id": "T-005",
                "title": note_m.group(1).strip() if note_m else "DORA TLPT triennial cycle vs ISO 27001 annual testing cycle (TENSION-M-002)",
                "nature": note_m.group(4).upper() if note_m else "STRUCTURAL",
                "severity": note_m.group(3) if note_m else "MEDIUM",
                "type": "",  # not stated in the note — flagged in AUD-P2-009
                "always_active": True,  # structural tensions are always-active per Doc16 §3.1
                "overlap_condition": (note_m.group(0) if note_m else "")[:200],
                "affected_subdomains": re.findall(r"D-\d+\.\d", note_m.group(2)) if note_m else [],
                "affected_regulations": ["DORA"],
                "resolution_approach": "DESIGN_DECISION",  # §4.1 bullet: structural set "resolved via design decisions"
                "resolution_description": "",
                "generates_from": [],
                "source_doc": "Doc16 §4.1 note (T-005/TENSION-M-002; analysis: P1 Doc11_DORA_ICT_Risk_Framework.md §4.5)",
                "parse_complete": bool(note_m),
                "alias": "TENSION-M-002",
        }
        # pair T-005 to obligations via its sub-domains (mechanical pairing rule)
        t5["generates_from"] = [obl_by_sub[sd] for sd in t5["affected_subdomains"] if sd in obl_by_sub]
        tensions.append(t5)
        notes.append(
                "Doc16 uses a dual tension id space: §4.2-4.3 cards use TENSION-{H,M,L}-NNN; "
                "the §4.1 note declares the canonical case set as T-001..T-005 (matching "
                "phase1_ontology v2.1-port@case_invariants.tensions=5) and defines "
                "T-005 = TENSION-M-002 (DORA TLPT). Card ids are used verbatim as node ids; "
                "T-005 is emitted from the note. The doc's own claim of '7 tensions' was "
                "already corrected by the port campaign (no INACTIVE tensions exist)."
        )
        return tensions, notes


def collect_nist_subcategories(controls: list[dict]) -> list[dict]:
        csf_set, pf_set = set(), set()
        for c in controls:
                csf_set.update(c["anchors_csf"])
                pf_set.update(c["anchors_pf"])
        result = []
        for sub in sorted(csf_set):
                result.append({"id": f"NIST-CSF-{sub}", "control_id": sub, "framework": "CSF",
                               "function": sub.split(".")[0], "source_doc": "control_set.yaml csf field (pattern-classified)"})
        for sub in sorted(pf_set):
                result.append({"id": f"NIST-PF-{sub}", "control_id": sub, "framework": "PF",
                               "function": sub.split(".")[0], "source_doc": "control_set.yaml pf field (pattern-classified)"})
        return result


# ---------------------------------------------------------------------------
# Compact ontology emitter (from phase2_ontology.yaml — mechanical)
# ---------------------------------------------------------------------------
def emit_compact() -> dict:
        if yaml_safe_load is None:
                raise SystemExit("PyYAML not installed")
        y = yaml_safe_load(ONTOLOGY_YAML.read_text(encoding="utf-8"))
        kg = y["kg_ontology"]
        return {
                "_provenance": {
                        "source_yaml": "02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/phase2_ontology.yaml",
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


# ---------------------------------------------------------------------------
# Graph emitter
# ---------------------------------------------------------------------------
def build_graph() -> dict[str, Any]:
        cr, bpr = parse_control_set()
        obligations = parse_doc15_obligations()
        po_nodes, so_nodes, dup4 = parse_doc17_objectives()
        tensions, parse_notes = parse_doc16_tensions(obligations)
        all_controls = cr + bpr
        nist_nodes = collect_nist_subcategories(all_controls)

        # Objective nodes by id (for MITIGATES resolution + AG-chain derivation)
        obj_by_id = {o["id"]: o for o in po_nodes + so_nodes}
        # Objectives' declared anchors (Doc17 rows carry CSF/PF/AI-RMF columns)
        for o in po_nodes + so_nodes:
                n = obj_by_id[o["id"]]
                n["declared_anchors_csf"] = o["anchors_csf"]
                n["declared_anchors_pf"] = o["anchors_pf"]

        # AG-chain: control → AG goals → Doc17 source obligations.
        goals_without_node: set[str] = set()
        rule_ids_by_obl: dict[str, list[str]] = {}
        for c in all_controls:
                obl_set: set[str] = set()
                for gid in c["objectives"]:
                        o = obj_by_id.get(gid)
                        if o is None:
                                goals_without_node.add(gid)
                                continue
                        obl_set.update(o["source_obligations"])
                c["obligations"] = sorted(obl_set)
                for oid in c["obligations"]:
                        rule_ids_by_obl.setdefault(oid, []).append(c["id"])

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
                "source": "phase2_ontology.yaml@company (carried from P1 v2.1-port)",
        })

        for obl in obligations:
                related = rule_ids_by_obl.get(obl["id"], [])
                obj_addressed = sorted({g for rid in related
                                        for g in next(c for c in all_controls if c["id"] == rid)["objectives"]
                                        if g in obj_by_id})
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
                                "risks_if_not_met": "Regulatory non-compliance; financial-entity supervision risk (DORA).",
                                "source_clauses": obl["source_clauses"],
                                "addressed_by_rules": related,
                                "yields_objectives": obj_addressed,
                        },
                        "source": obl["source"],
                })

        for o in po_nodes + so_nodes:
                is_po = o["id"] in {p["id"] for p in po_nodes}
                nodes.append({
                        "id": o["id"],
                        "type": "PrivacyOperationalObjective" if is_po else "SecurityOperationalObjective",
                        "label": f"{o['id']} ({'PO' if is_po else 'SO'})",
                        "attrs": {
                                "subdomain_id": f"D-{o['id'].split('-')[2].split('-')[0]}",
                                "title": o["title"],
                                "description": o["title"],
                                "derives_from_obligation_id": ", ".join(o["source_obligations"]),
                                "risk_profile": o["risk_profile"],
                                "nist_csf_anchors": o["anchors_csf"],
                                "nist_pf_anchors": o["anchors_pf"],
                                "priority": o["priority"],
                                "verification_method": "INSPECT",
                        },
                        "source": o["source"],
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
                                "native": c["native"],
                                "anchors_csf": c["anchors_csf"],
                                "anchors_pf": c["anchors_pf"],
                                "anchors_airmf": c["anchors_airmf"],
                                "status_csf": c["status_csf"],
                                "status_privacy": c["status_privacy"],
                                "status_airmf": c["status_airmf"],
                                "verification_method": c["verification_method"],
                                "verification_owner": "CRO Office",
                        },
                        "source": c["source_doc"],
                })

        for t in tensions:
                attrs = {
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
                }
                if t.get("alias"):
                        attrs["alias"] = t["alias"]
                nodes.append({
                        "id": t["id"],
                        "type": "Tension",
                        "label": f"{t['id']} — {t['title'][:70]}",
                        "attrs": attrs,
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
                for gid in c["objectives"]:
                        if gid not in obj_by_id:
                                continue  # audited (AUD-P2-006)
                        links.append({
                                "from": c["id"], "to": gid, "rel": "MITIGATES",
                                "attrs": {"kind": c["register"]},
                                "source": "control_set.yaml@related_goals (AG ids; NATIVE BPRs excluded by construction)",
                        })
                for sub in c["anchors_csf"]:
                        links.append({"from": c["id"], "to": f"NIST-CSF-{sub}", "rel": "MAPS_TO",
                                      "attrs": {"framework": "CSF"},
                                      "source": "control_set.yaml anchors (pattern-classified)"})
                for sub in c["anchors_pf"]:
                        links.append({"from": c["id"], "to": f"NIST-PF-{sub}", "rel": "MAPS_TO",
                                      "attrs": {"framework": "PF"},
                                      "source": "control_set.yaml anchors (pattern-classified)"})

        for o in po_nodes + so_nodes:
                for oid in o["source_obligations"]:
                        links.append({
                                "from": oid, "to": o["id"], "rel": "YIELDS",
                                "attrs": {}, "source": "Doc17 §3/§4 source-obligations column",
                        })

        for t in tensions:
                for oid in t["generates_from"]:
                        links.append({
                                "from": oid, "to": t["id"], "rel": "GENERATES",
                                "attrs": {"severity": t["severity"]},
                                "source": "Doc16 §4 card (Obligation ID / Sub-Domain pairing)",
                        })

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
                "source_clauses_total": 150,  # phase1_ontology v2.1-port@case_invariants.total_clauses
                "applicable_regs": len(COMPANY["applicable_regs"]),
                "nist_subcategories_total": len(nist_nodes),
                "nodes_total": len(nodes),
                "links_total": len(links),
        }

        ambiguity = {
                "stats_total": {"S1_high": 0, "S2_medium": 0, "S3_low": 0, "total_cards": 0},
                "source_doc": "Phase 2 carries zero ambiguity cards (ambiguity is a P1 concern; P2 formalises obligations/objectives).",
        }

        # ---- Audits (Case_01 AUD-P2 scheme, mechanically computed) ----
        audits = []
        cr_without_chain = [c["id"] for c in cr if not c["obligations"]]
        if cr_without_chain:
                audits.append({"id": "AUD-P2-001", "kind": "structural", "node_ids": cr_without_chain,
                               "title": f"{len(cr_without_chain)} CR(s) whose AG goals resolve to no Doc17 objective (no AG-chain obligation coverage)",
                               "severity": "medium", "source": "control_set.yaml@related_goals → Doc17 §3/§4"})
        tensions_incomplete = [t["id"] for t in tensions if not t["parse_complete"] and t["id"] != "T-005"]
        if tensions_incomplete:
                audits.append({"id": "AUD-P2-002", "kind": "structural", "node_ids": tensions_incomplete,
                               "title": f"{len(tensions_incomplete)} tension card(s) with incomplete §4.1/card parse",
                               "severity": "low", "source": "Doc16 §4"})
        po_ids = {p["id"] for p in po_nodes}
        po_orphan = [p["id"] for p in po_nodes if p["id"] not in {l["to"] for l in links if l["rel"] == "MITIGATES"}]
        if po_orphan:
                audits.append({"id": "AUD-P2-004", "kind": "orphan_check", "node_ids": po_orphan,
                               "title": f"{len(po_orphan)} privacy objective(s) without a CR/BPR addressing them",
                               "severity": "medium", "source": "control_set.yaml@related_goals"})
        so_orphan = [s["id"] for s in so_nodes if s["id"] not in {l["to"] for l in links if l["rel"] == "MITIGATES"}]
        if so_orphan:
                audits.append({"id": "AUD-P2-005", "kind": "orphan_check", "node_ids": so_orphan,
                               "title": f"{len(so_orphan)} security objective(s) without a CR/BPR addressing them",
                               "severity": "medium", "source": "control_set.yaml@related_goals"})
        obl_addressed = {o for c in all_controls for o in c["obligations"]}
        obl_orphan = [o["id"] for o in obligations if o["id"] not in obl_addressed]
        if obl_orphan:
                audits.append({"id": "AUD-P2-005b", "kind": "orphan_check", "node_ids": obl_orphan,
                               "title": f"{len(obl_orphan)} obligation(s) without a CR addressing them (via the AG chain)",
                               "severity": "high", "source": "control_set.yaml@related_goals → Doc17 source obligations"})
        cr_no_anchor = [c["id"] for c in cr if not c["anchors_csf"] and not c["anchors_pf"]]
        if cr_no_anchor:
                audits.append({"id": "AUD-P2-006", "kind": "nist_alignment", "node_ids": cr_no_anchor,
                               "title": f"{len(cr_no_anchor)} CR(s) without CSF or PF anchors",
                               "severity": "low", "source": "control_set.yaml anchors"})
        goals_wo = sorted(goals_without_node)
        if goals_wo:
                audits.append({"id": "AUD-P2-007", "kind": "parse_anomaly",
                               "node_ids": sorted({c["id"] for c in all_controls
                                                   if any(g in goals_without_node for g in c["objectives"])}),
                               "title": (f"{len(goals_wo)} AG goal id(s) referenced by control_set@related_goals "
                                         "have no Doc17 objective row (links withheld; quoted in this audit)"),
                               "severity": "medium", "source": "control_set.yaml@related_goals vs Doc17"})
        doubtful = {d for c in all_controls for d in c["doubtful_anchors"]}
        if doubtful:
                audits.append({"id": "AUD-P2-008", "kind": "parse_anomaly",
                               "node_ids": sorted(c["id"] for c in all_controls if c["doubtful_anchors"]),
                               "title": (f"{len(doubtful)} anchor token(s) in control_set csf/pf/airmf fields "
                                         "match no known framework pattern (quoted verbatim; not linked)"),
                               "severity": "low", "source": "control_set.yaml csf/pf/airmf fields"})
        audits.append({
                "id": "AUD-P2-009",
                "kind": "provenance",
                "node_ids": [t["id"] for t in tensions],
                "title": "Dual tension id space (TENSION-{H,M,L}-NNN cards + canonical T-001..T-005; T-005 from Doc16 §4.1 note, analysis in P1 Doc11 §4.5)",
                "severity": "low",
                "source": "; ".join(parse_notes),
        })
        audits.append({
                "id": "AUD-P2-010",
                "kind": "canonical_count_correction",
                "node_ids": [p["id"] for p in po_nodes] + [s["id"] for s in so_nodes],
                "title": (f"Mechanical canonical counts vs the doc's own summaries: §3 rows={len(po_nodes)} "
                          f"(summary claims 11 — AUD gap), §4 unique-not-in-§3={len(so_nodes)} "
                          f"(summary claims 22); {len(dup4)} AG ids appear twice in §4 tables (deduped)"),
                "severity": "medium",
                "source": "Doc17 §3/§4 canonical tables vs §3.5/§4 summaries",
        })

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
        ap = argparse.ArgumentParser(description="Build Phase 2 graph JSON for Case_03")
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
                        print(f"  - {a['id']} [{a['kind']}] {a['title'][:110]}")
        return 0


if __name__ == "__main__":
        sys.exit(main())
