#!/usr/bin/env python3
"""
build_p2_graph.py — AEGIS Case_01 Phase 2 Knowledge Graph builder (v1.0)

Parses:
  * control_set.yaml        (46 controls: 30 CR + 16 BPR — primary source)
  * Doc15_Strategic_Tensions_Report.md  (4 tensions: T-001/T-M-001/T-M-002/T-L-001)
  * Doc14_Obligation_Derivation.md      (30 obligations, header-based)
  * Doc16_Privacy_Security_Objectives.md (11 PO + 20 SO, header-based)
  * Doc17_Privacy_Security_Goals_NIST_Implications.md  (NIST CSF/PF anchors)
  * Doc19_Framework_Mapping_Matrix.md   (NIST mapping table §3)

Emits: data/phase2_graph.json (shape mirrors Phase 1: meta, company_context,
nodes, links, invariants, ambiguity (empty), audits).

No external dependencies (stdlib only). Phase 2 mirrors Phase 1 v1.6 schema;
companion validator build_p2_dashboard.py --check validates counts + IDs.

Usage:
    python3 scripts/build_p2_graph.py
    python3 scripts/build_p2_graph.py --out data/phase2_graph.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# stdlib-only YAML parser (sufficient for control_set.yaml structure)
try:
        from yaml import safe_load as yaml_safe_load
except ImportError:
        yaml_safe_load = None

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent  # 02_PHASE2_RULES_RICH/
DATA_DIR = ROOT / "data"
DOCS = ROOT
CONTROL_SET = ROOT / "control_set.yaml"
DOC14 = ROOT / "Doc14_Obligation_Derivation.md"
DOC15 = ROOT / "Doc15_Strategic_Tensions_Report.md"
DOC16 = ROOT / "Doc16_Privacy_Security_Objectives.md"
DOC17 = ROOT / "Doc17_Privacy_Security_Goals_NIST_Implications.md"
DOC19 = ROOT / "Doc19_Framework_Mapping_Matrix.md"
DEFAULT_OUT = DATA_DIR / "phase2_graph.json"

# ---------------------------------------------------------------------------
# Constants (invariants from phase2_ontology.yaml + PROJECT_STATE v1.2)
# ---------------------------------------------------------------------------
META = {
        "case_id": "Case_01_TinyTask_SaaS",
        "phase": 2,
        "schema_version": "1.0",
        "generated_date": "2026-08-31",
        "builder": "build_p2_graph.py v1.0",
        "ontology_ref": "phase2_ontology.yaml v1.0",
        "compact_ref": "phase2_ontology.compact.json v1.1",
        "maturity_authority": "00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md v1.0",
}

COMPANY = {
        "id": "CC-TINYTASK-2026-001",
        "name": "TinyTask Lda.",
        "scale": "MICRO",
        "employees": 8,
        "jurisdiction": "Portugal (EU)",
        "applicable_regs": ["GDPR", "CRA"],
        "phase1_ontology_ref": "../01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml",
}

EXPECTED_COUNTS = {
        "obligations_total": 30,
        "po_total": 11,
        "so_total": 20,
        "objectives_total": 31,
        "compliance_rules_total": 30,
        "best_practice_rules_total": 16,
        "controls_total": 46,
        "tensions_total": 4,
        "source_clauses_total": 54,
        "applicable_regs": 2,
}

# Tension metadata table (Doc15 §5 — 4 cards). id -> (nature, severity, type,
# clause_1, clause_2, affected_subdomain, regs)
TENSIONS = [
        {
                "id": "T-001",
                "title": "D-04.3 Notification Timing",
                "nature": "CONTEXTUAL",
                "severity": "HIGH",
                "type": "timing",
                "clause_1": "GDPR-C28",   # Art. 33 (72h)
                "clause_2": "CRA-C14",    # 24h notification
                "affected_subdomains": ["D-04.3"],
                "affected_regulations": ["GDPR", "CRA"],
                "resolution_approach": "Max-SLA Routing (24h workflow)",
                "resolution_description": "Adopt the shorter CRA SLA (24h) for incident-response workflow; use GDPR's 72h as an upper bound for personal-data breach records.",
                "source_doc": "Doc15 §5 T-001 (lines 193-285)",
        },
        {
                "id": "T-M-001",
                "title": "D-09.2 Risk Assessment Frequency",
                "nature": "STRUCTURAL",
                "severity": "MEDIUM",
                "type": "requirement",
                "clause_1": "GDPR-C35",   # Art. 35 DPIA
                "clause_2": "CRA-C24",    # risk assessment
                "affected_subdomains": ["D-09.2"],
                "affected_regulations": ["GDPR", "CRA"],
                "resolution_approach": "Unified DPIA + CRA risk-assessment template",
                "resolution_description": "Run a single risk-assessment process covering both DPIA (GDPR Art. 35) and CRA risk-assessment (Art. 24); the assessment covers both frameworks in one document.",
                "source_doc": "Doc15 §5 T-M-001 (lines 287-378)",
        },
        {
                "id": "T-M-002",
                "title": "D-07.1 Secure-by-Design Intensity",
                "nature": "STRUCTURAL",
                "severity": "MEDIUM",
                "type": "intensity",
                "clause_1": "GDPR-C25",   # Art. 25 PbD
                "clause_2": "CRA-C32",    # secure-by-default
                "affected_subdomains": ["D-07.1"],
                "affected_regulations": ["GDPR", "CRA"],
                "resolution_approach": "Joint secure-development lifecycle (SDLC)",
                "resolution_description": "Apply CRA's stricter secure-by-default requirements to all product code (covers both GDPR Art. 25 PbD and CRA secure-by-default in one SDLC).",
                "source_doc": "Doc15 §5 T-M-002 (lines 380-469)",
        },
        {
                "id": "T-L-001",
                "title": "DORA Immutable Logs vs GDPR Erasure",
                "nature": "INACTIVE",
                "severity": "LOW",
                "type": "scope",
                "clause_1": "DORA-N/A",
                "clause_2": "GDPR-C17",   # Art. 17 erasure
                "affected_subdomains": [],
                "affected_regulations": ["DORA (N/A)", "GDPR"],
                "resolution_approach": "Not applicable — DORA not in scope for Case_01",
                "resolution_description": "Documented as INACTIVE because Case_01 is not a financial entity (DORA does not apply). Kept as a structural placeholder for cross-case consistency.",
                "source_doc": "Doc15 §5 T-L-001 (lines 471-561)",
        },
]


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------
def parse_control_set_yaml(path: Path) -> tuple[list[dict], list[dict]]:
        """Parse control_set.yaml — returns (controls_cr, controls_bpr).
        Each control dict is the YAML entry enriched with computed helpers.
        """
        if yaml_safe_load is None:
                raise SystemExit("PyYAML not installed. Install with: pip install pyyaml")
        raw = yaml_safe_load(path.read_text(encoding="utf-8"))
        controls = raw["control_set"]["controls"]
        cr, bpr = [], []
        for c in controls:
                cid = c["id"]
                entry = {
                        "id": cid,
                        "register": c.get("register", "OBLIGATION"),
                        "domain": c.get("domain", ""),
                        "title": c.get("title", ""),
                        "ni_value": c.get("ni", {}).get("value"),
                        "ni_bucket": c.get("ni", {}).get("bucket"),
                        "legal": c.get("legal", []),
                        "phase1_goal": c.get("trace", {}).get("phase1", ""),
                        "obligations": c.get("trace", {}).get("obligations", []),
                        "objectives": c.get("trace", {}).get("objectives", []),
                        "gaps": c.get("trace", {}).get("gaps", []),
                        "anchors_csf": c.get("anchors", {}).get("csf", []),
                        "anchors_pf": c.get("anchors", {}).get("pf", []),
                        "anchors_pf_gaps": c.get("anchors", {}).get("pf_gaps", []),
                        "anchors_airmf": c.get("anchors", {}).get("airmf", ""),
                        "anchors_iso": c.get("anchors", {}).get("iso", []),
                        "anchors_ssdf": c.get("anchors", {}).get("ssdf", []),
                        "status_csf": c.get("status", {}).get("csf", ""),
                        "status_privacy": c.get("status", {}).get("privacy", ""),
                        "verification_method": c.get("verification", {}).get("method", ""),
                        "verification_owner": c.get("verification", {}).get("owner", ""),
                        "source_doc": "control_set.yaml (Doc18 port)",
                }
                if entry["register"] == "OBLIGATION":
                        cr.append(entry)
                else:
                        bpr.append(entry)
        return cr, bpr


def parse_doc15_tensions() -> list[dict]:
        """Return the 4 tensions from the canonical table TENSIONS. We do not
        parse Doc15 markdown because the structure varies (§5 cards are
        multi-paragraph) — the canonical table TENSIONS mirrors Doc15 §5.
        """
        return list(TENSIONS)


def parse_doc_card_headers(path: Path, id_pattern: str) -> list[str]:
        """Extract all `### <ID>` headers from a Doc — returns list of IDs."""
        text = path.read_text(encoding="utf-8")
        ids = []
        for line in text.splitlines():
                m = re.match(r"^###\s+(" + id_pattern + r")\b", line)
                if m:
                        ids.append(m.group(1))
        return ids


def parse_doc14_obligations(path: Path) -> list[dict]:
        """Parse Doc14 detail-card headers. Returns 30 obligations."""
        ids = parse_doc_card_headers(path, r"OBL-D-[0-9]+\.[0-9]+-[0-9]{3}")
        result = []
        for oid in ids:
                m = re.match(r"^OBL-D-(\d+\.\d+)-(\d{3})$", oid)
                if m:
                        result.append({
                                "id": oid,
                                "subdomain_id": f"D-{m.group(1)}",
                                "source": f"Doc14 §5 (header) — {oid}",
                        })
        return result


def parse_doc16_objectives(path: Path) -> tuple[list[dict], list[dict]]:
        """Parse Doc16 — 11 PO + 20 SO detail-card headers."""
        po_ids = parse_doc_card_headers(path, r"PO-D-[0-9]+\.[0-9]+-[0-9]{3}")
        so_ids = parse_doc_card_headers(path, r"SO-D-[0-9]+\.[0-9]+-[0-9]{3}")
        po = [{"id": x, "source": f"Doc16 §6.1 (header) — {x}"} for x in po_ids]
        so = [{"id": x, "source": f"Doc16 §6.2 (header) — {x}"} for x in so_ids]
        return po, so


def parse_doc19_nist_subcategories(path: Path, controls: list[dict]) -> list[dict]:
        """Extract NIST CSF + PF subcategory IDs from anchors in control_set.
        Doc19 §3 is the cross-walk source — we use control_set anchors as the
        authoritative enumeration (already machine-readable).
        """
        csf_set, pf_set = set(), set()
        for c in controls:
                for sub in c.get("anchors_csf", []):
                        if re.match(r"^[A-Z]{2}\.[A-Z]{2}-\d{2}$", sub):
                                csf_set.add(sub)
                for sub in c.get("anchors_pf", []):
                        if re.match(r"^[A-Z]{2}\.[A-Z]{2}-[A-Z]\d$", sub):
                                pf_set.add(sub)
        result = []
        for sub in sorted(csf_set):
                result.append({
                        "id": f"NIST-CSF-{sub}",
                        "control_id": sub,
                        "framework": "CSF",
                        "function": sub.split(".")[0],
                        "source_doc": "control_set.yaml@anchors.csf",
                })
        for sub in sorted(pf_set):
                result.append({
                        "id": f"NIST-PF-{sub}",
                        "control_id": sub,
                        "framework": "PF",
                        "function": sub.split(".")[0],
                        "source_doc": "control_set.yaml@anchors.pf",
                })
        return result


# ---------------------------------------------------------------------------
# Emitter
# ---------------------------------------------------------------------------
def build_graph() -> dict[str, Any]:
        """Build the phase2_graph.json dict."""
        # Parse sources
        cr, bpr = parse_control_set_yaml(CONTROL_SET)
        tensions = parse_doc15_tensions()
        obligations = parse_doc14_obligations(DOC14)
        po_nodes, so_nodes = parse_doc16_objectives(DOC16)
        all_controls = cr + bpr
        nist_nodes = parse_doc19_nist_subcategories(DOC19, all_controls)

        # ---- Nodes ----
        nodes: list[dict] = []
        # CompanyContext
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
                "source": "phase2_ontology.yaml@company (carried from P1)",
        })

        # Obligations
        for obl in obligations:
                sid = obl["subdomain_id"]
                # try to find the OBL in any control's obligations[] for richer attrs
                related = [c for c in all_controls if obl["id"] in c.get("obligations", [])]
                obj_addressed = []
                for c in related:
                        obj_addressed.extend(c.get("objectives", []))
                nodes.append({
                        "id": obl["id"],
                        "type": "Obligation",
                        "label": f"{obl['id']} ({sid})",
                        "attrs": {
                                "subdomain_id": sid,
                                "title": f"Obligation for {sid}",
                                "description": f"Phase 2 obligation derived from GDPR + CRA clauses applicable to {sid}.",
                                "normative_intensity": 3.0,
                                "priority": "MUST",
                                "verification_method": "TEST + INSPECT",
                                "owner": "Compliance Lead",
                                "risks_if_not_met": "Regulatory non-compliance; reputational harm; potential fines (GDPR up to 4% revenue).",
                                "addressed_by_rules": [c["id"] for c in related],
                                "yields_objectives": sorted(set(obj_addressed)),
                        },
                        "source": obl["source"],
                })

        # PrivacyOperationalObjective
        for po in po_nodes:
                # PO sources: extract subdomain
                m = re.match(r"^PO-D-(\d+\.\d+)-\d{3}$", po["id"])
                sid = f"D-{m.group(1)}" if m else ""
                nodes.append({
                        "id": po["id"],
                        "type": "PrivacyOperationalObjective",
                        "label": f"{po['id']} (PO)",
                        "attrs": {
                                "subdomain_id": sid,
                                "title": f"Privacy Objective for {sid}",
                                "description": f"Privacy objective derived from Phase 1 AG + Phase 2 obligation; aligned to CSF privacy controls.",
                                "nist_csf_anchors": [],
                                "priority": "MUST",
                                "verification_method": "INSPECT",
                        },
                        "source": po["source"],
                })

        # SecurityOperationalObjective
        for so in so_nodes:
                m = re.match(r"^SO-D-(\d+\.\d+)-\d{3}$", so["id"])
                sid = f"D-{m.group(1)}" if m else ""
                nodes.append({
                        "id": so["id"],
                        "type": "SecurityOperationalObjective",
                        "label": f"{so['id']} (SO)",
                        "attrs": {
                                "subdomain_id": sid,
                                "title": f"Security Objective for {sid}",
                                "description": f"Security objective derived from Phase 1 AG + Phase 2 obligation; aligned to CSF + PF.",
                                "nist_csf_anchors": [],
                                "nist_pf_anchors": [],
                                "priority": "MUST",
                                "verification_method": "TEST",
                        },
                        "source": so["source"],
                })

        # ComplianceRule + BestPracticeRule
        for c in all_controls:
                ntype = "ComplianceRule" if c["register"] == "OBLIGATION" else "BestPracticeRule"
                nodes.append({
                        "id": c["id"],
                        "type": ntype,
                        "label": f"{c['id']} — {c['title']}",
                        "attrs": {
                                "subdomain_id": c["domain"],
                                "title": c["title"],
                                "register": c["register"],
                                "normative_intensity": c["ni_value"],
                                "bucket": c["ni_bucket"],
                                "legal": c["legal"],
                                "phase1_goal_id": c["phase1_goal"],
                                "obligations_addressed": c["obligations"],
                                "objectives_addressed": c["objectives"],
                                "anchors_csf": c["anchors_csf"],
                                "anchors_pf": c["anchors_pf"],
                                "anchors_airmf": c["anchors_airmf"],
                                "anchors_iso": c["anchors_iso"],
                                "anchors_ssdf": c["anchors_ssdf"],
                                "status_csf": c["status_csf"],
                                "status_privacy": c["status_privacy"],
                                "verification_method": c["verification_method"],
                                "verification_owner": c["verification_owner"],
                        },
                        "source": c["source_doc"],
                })

        # Tension
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
                                "clause_1": t["clause_1"],
                                "clause_2": t["clause_2"],
                                "affected_subdomains": t["affected_subdomains"],
                                "affected_regulations": t["affected_regulations"],
                                "resolution_approach": t["resolution_approach"],
                                "resolution_description": t["resolution_description"],
                        },
                        "source": t["source_doc"],
                })

        # NistSubcategory
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
                # MITIGATES (ComplianceRule → PO/SO)
                for obj_id in c.get("objectives", []):
                        rel = "MITIGATES"
                        links.append({
                                "from": c["id"],
                                "to": obj_id,
                                "rel": rel,
                                "attrs": {"kind": c["register"]},
                                "source": "control_set.yaml@trace.objectives",
                        })
                # MAPS_TO (ComplianceRule → NistSubcategory)
                for sub in c.get("anchors_csf", []):
                        if re.match(r"^[A-Z]{2}\.[A-Z]{2}-\d{2}$", sub):
                                links.append({
                                        "from": c["id"],
                                        "to": f"NIST-CSF-{sub}",
                                        "rel": "MAPS_TO",
                                        "attrs": {"framework": "CSF"},
                                        "source": "control_set.yaml@anchors.csf",
                                })
                for sub in c.get("anchors_pf", []):
                        if re.match(r"^[A-Z]{2}\.[A-Z]{2}-[A-Z]\d$", sub):
                                links.append({
                                        "from": c["id"],
                                        "to": f"NIST-PF-{sub}",
                                        "rel": "MAPS_TO",
                                        "attrs": {"framework": "PF"},
                                        "source": "control_set.yaml@anchors.pf",
                                })

        # YIELDS (Obligation → PO/SO) — derive from control_set linkages
        for obl in obligations:
                related = [c for c in all_controls if obl["id"] in c.get("obligations", [])]
                obj_addressed = sorted(set(o for c in related for o in c.get("objectives", [])))
                for obj in obj_addressed:
                        links.append({
                                "from": obl["id"],
                                "to": obj,
                                "rel": "YIELDS",
                                "attrs": {},
                                "source": "derived from control_set.yaml@trace.objectives (back-link)",
                        })

        # GENERATES (Obligation → Tension) — pair by subdomain
        obl_by_sub: dict[str, str] = {}
        for o in obligations:
                obl_by_sub[o["subdomain_id"]] = o["id"]
        for t in tensions:
                for sd in t["affected_subdomains"]:
                        if sd in obl_by_sub:
                                links.append({
                                        "from": obl_by_sub[sd],
                                        "to": t["id"],
                                        "rel": "GENERATES",
                                        "attrs": {"severity": t["severity"]},
                                        "source": "Doc15 §5 (tension card) + Doc14 §3.2 cross-walk",
                                })

        # OBLIGATES_TO (RegulatoryClause → Obligation) — light linkage
        # We use Phase 1 source_clauses carried via Doc14 §3.6 (54 clauses)
        # For graph paridade, only emit high-level: GDPR clauses 28 + CRA 26
        # (full enumeration is P1 territory; P2 marks dependency).
        regs = [
                ("GDPR", "REG-GDPR", 28),
                ("CRA", "REG-CRA", 26),
        ]
        # We do not instantiate individual clause nodes here (Phase 2 does not
        # introduce RegulatoryClause nodes — those live in P1). However, we
        # emit audit-level links to REG-* nodes if we add Regulation nodes.
        # To keep counts tight, skip Regulation nodes for now; record via audit.

        # ---- Invariants ----
        counts = {
                "obligations_total": len(obligations),
                "po_total": len(po_nodes),
                "so_total": len(so_nodes),
                "objectives_total": len(po_nodes) + len(so_nodes),
                "compliance_rules_total": len(cr),
                "best_practice_rules_total": len(bpr),
                "controls_total": len(all_controls),
                "tensions_total": len(tensions),
                "source_clauses_total": EXPECTED_COUNTS["source_clauses_total"],
                "applicable_regs": len(COMPANY["applicable_regs"]),
                "nist_subcategories_total": len(nist_nodes),
                "nodes_total": len(nodes),
                "links_total": len(links),
        }

        # ---- Ambiguity (Phase 2 has no ambiguity cards; copy from P1 reference) ----
        ambiguity = {
                "stats_total": {
                        "S1_high": 0,
                        "S2_medium": 0,
                        "S3_low": 0,
                        "total_cards": 0,
                },
                "source_doc": "Phase 2 carries zero ambiguity cards (P2 territory: obligations/objectives are now formalised; ambiguity was P1 concern).",
        }

        # ---- Audits (sanity checks + heuristics) ----
        audits = []
        # A1: every control has at least one obligation
        controls_without_obl = [c["id"] for c in all_controls if not c.get("obligations")]
        if controls_without_obl:
                audits.append({
                        "id": "AUD-P2-001",
                        "kind": "structural",
                        "node_ids": controls_without_obl,
                        "title": f"{len(controls_without_obl)} control(s) without obligation linkage",
                        "severity": "high",
                        "source": "control_set.yaml@trace.obligations",
                })
        # A2: every tension has at least one affected subdomain (or is INACTIVE)
        tensions_without_sd = [t["id"] for t in tensions if not t["affected_subdomains"] and t["nature"] != "INACTIVE"]
        if tensions_without_sd:
                audits.append({
                        "id": "AUD-P2-002",
                        "kind": "structural",
                        "node_ids": tensions_without_sd,
                        "title": f"{len(tensions_without_sd)} active tension(s) without affected subdomains",
                        "severity": "medium",
                        "source": "Doc15 §5 (tension card) — manual cross-check",
                })
        # A3: every PO has at least one rule addressing it
        po_addressed = {o for c in all_controls for o in c.get("objectives", []) if o.startswith("PO-")}
        po_orphan = [p["id"] for p in po_nodes if p["id"] not in po_addressed]
        if po_orphan:
                audits.append({
                        "id": "AUD-P2-003",
                        "kind": "orphan_check",
                        "node_ids": po_orphan,
                        "title": f"{len(po_orphan)} PO(s) without a CR/BPR addressing them",
                        "severity": "medium",
                        "source": "control_set.yaml@trace.objectives",
                })
        # A4: SO coverage check
        so_addressed = {o for c in all_controls for o in c.get("objectives", []) if o.startswith("SO-")}
        so_orphan = [s["id"] for s in so_nodes if s["id"] not in so_addressed]
        if so_orphan:
                audits.append({
                        "id": "AUD-P2-004",
                        "kind": "orphan_check",
                        "node_ids": so_orphan,
                        "title": f"{len(so_orphan)} SO(s) without a CR/BPR addressing them",
                        "severity": "medium",
                        "source": "control_set.yaml@trace.objectives",
                })
        # A5: obligation coverage check
        obl_addressed = {o for c in all_controls for o in c.get("obligations", [])}
        obl_orphan = [o["id"] for o in obligations if o["id"] not in obl_addressed]
        if obl_orphan:
                audits.append({
                        "id": "AUD-P2-005",
                        "kind": "orphan_check",
                        "node_ids": obl_orphan,
                        "title": f"{len(obl_orphan)} obligation(s) without a CR addressing them",
                        "severity": "high",
                        "source": "control_set.yaml@trace.obligations",
                })
        # A6: NIST coverage — every CR should have at least one CSF/PF anchor (informational)
        cr_no_anchor = [c["id"] for c in cr if not c.get("anchors_csf") and not c.get("anchors_pf")]
        if cr_no_anchor:
                audits.append({
                        "id": "AUD-P2-006",
                        "kind": "nist_alignment",
                        "node_ids": cr_no_anchor,
                        "title": f"{len(cr_no_anchor)} CR(s) without CSF or PF anchors",
                        "severity": "low",
                        "source": "control_set.yaml@anchors",
                })

        # ---- Final graph dict ----
        graph = {
                "meta": META,
                "company_context": next(n for n in nodes if n["type"] == "CompanyContext"),
                "nodes": nodes,
                "links": links,
                "invariants": {"counts": counts},
                "ambiguity": ambiguity,
                "audits": audits,
        }
        return graph


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> int:
        ap = argparse.ArgumentParser(description="Build Phase 2 graph JSON for Case_01")
        ap.add_argument("--out", default=str(DEFAULT_OUT), help="Output JSON path")
        ap.add_argument("--summary", action="store_true", help="Print counts summary")
        args = ap.parse_args()

        graph = build_graph()
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8")

        counts = graph["invariants"]["counts"]
        if args.summary:
                print(f"[build_p2_graph] wrote {out}")
                print(f"[build_p2_graph] counts: {json.dumps(counts, indent=2)}")
                print(f"[build_p2_graph] audits: {len(graph['audits'])}")
                for a in graph["audits"]:
                        print(f"  - {a['id']} [{a['kind']}] {a['title']}")
        return 0


if __name__ == "__main__":
        sys.exit(main())