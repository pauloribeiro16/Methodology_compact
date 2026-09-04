#!/usr/bin/env python3
"""Companion to phase1_graph.json for Case_03 — validator v2.1-port (parity with Case_01/02).

Ported from Case_02_SecureBorder_Solutions/scripts/build_p1_dashboard.py v2.4
(campaign PORT-PARITY-2, block F3a) with Case_03 data:
  - 5 regulations (ALL applicable: GDPR, CRA, NIS 2, DORA, AI_Act — DORA branch live)
  - 10 domains, 38 sub-domains (38 active + 0 NOT_ADDRESSED — only AEGIS case)
  - 150 clauses (28 GDPR + 26 CRA + 29 NIS2 + 38 DORA + 29 AI)
  - 76 AdjustedGoal, 9 DataSubjectCategory, 119 EvidenceItems (37 Coverage + 82 Capability)
  - 121 NistControl (79 CSF + 38 PF + 4 AI-RMF — AI-RMF anchors REAL: provider+deployer)
  - 1490 ambiguity cards, 9 audits, 5 tensions (4 mechanically resolved clause pairs)

Gates (per MATURITY_MODEL_CSF_STRICT.md §10 + v2.1-port paridade):
  check_invariants         — graph counts vs pinned EXPECTED
  check_audit_node_ids     — audit node_ids resolve to real graph nodes
  check_phase_c            — maturity gates v2.3 (4 gates)
  check_phase_d            — NistControl framework/function/ID + ALIGNS_TO integrity
  check_ontology_types     — node types vs compact.json@classes
  check_relation_verbs     — link rel vs compact.json@relations
  check_id_patterns        — ID regex mismatches (warning-only; non-fatal like Case_02)
  check_provenance         — missing source[]/id (warning-only)
  check_stale_invariant_counts — invariants vs actual node counts

Usage:
    python3 build_p1_dashboard.py --check                # exit 0 if all checks pass
    python3 build_p1_dashboard.py --check --strict       # same gate set; warnings surfaced
    python3 build_p1_dashboard.py --emit
    python3 build_p1_dashboard.py --summary
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
GRAPH = ROOT / "data" / "phase1_graph.json"
ONTOLOGY = ROOT / "phase1_ontology.yaml"
COMPACT = ROOT / "data" / "phase1_ontology.compact.json"

# Case_03 expected counts (v2.1-port). Counts are pinned by the builder
# (scripts/build_p1_graph.py) and verified by --check; delta != 0 is a goal.
EXPECTED: dict[str, int] = {
    "regulations_total": 5,
    "regulations_applicable": 5,   # GDPR + CRA + NIS 2 + DORA + AI_Act — ALL applicable
    "domains": 10,
    "subdomains_total": 38,
    "subdomains_covered": 38,
    "subdomains_active": 38,       # 38/38 ACTIVE — zero NOT_ADDRESSED (5-reg case)
    "clauses_total": 150,
    "clauses_gdpr": 28,
    "clauses_cra":  26,
    "clauses_nis2": 29,
    "clauses_dora": 38,
    "clauses_aiact": 29,
    "tensions_total": 5,
    "tension_edges_resolved": 4,    # T-005 resolves to 1 clause + non-clause regimes
    "ambiguity_cards_in_scope": 1490,
    "ambiguity_top_cards": 20,
    "evidence_items": 119,
    "evidence_items_capability": 82,     # 38 CSF + 38 PF + 6 AI-RMF (per sd×framework)
    "evidence_items_coverage":   37,     # 38 active − D-07.2 (no clause anchor; CVG-C03-001)
    "evidence_items_capability_csf": 38,
    "evidence_items_capability_pf": 38,
    "evidence_items_capability_airmf": 6,
    "subdomains_with_coverage_evidence": 37,
    "subdomains_withheld_coverage": 1,
    "articles_with_verification": 150,
    "subdomains_with_proportionality": 38,  # Doc13 §4 rows (all 38 active)
    "subdomains_rigorous": 31,              # Doc13 §3: MAX + BUILD_REQUIRED + MUST
    "subdomains_standard": 7,               # Doc13 §3: MAX + INHERITABLE + MUST
    "adjusted_goals": 76,                   # 38 privacy (-001) + 38 security (-002)
    "data_subject_categories": 9,           # Doc04 §2.4
    "systems": 25,                          # Doc04 §1.1 / xlsx SYSTEMS
    "data_stores": 12,                      # Doc04 §2.1 / xlsx DATA_STORES
    "data_flows": 25,                       # Doc04 §2.2 / xlsx DATA_FLOWS
    "third_parties": 33,                    # Doc06 §5 / xlsx THIRD_PARTIES
    "personal_data_categories": 13,         # Doc04 §2.3 / xlsx PERSONAL_DATA
    "stakeholders": 15,                     # ROLES_RACI header roles (1:1 STK placeholder)
    "raci_roles": 15,
    "raci_activities": 65,
    "coverage_gaps": 12,                    # GAP-01..GAP-12
    "nist_controls": 121,                   # 79 CSF + 38 PF + 4 AI-RMF (Doc14 §5)
    "nist_controls_csf":   79,
    "nist_controls_pf":    38,
    "nist_controls_airmf": 4,
    "nist_alignments":     577,             # deduped ALIGNS_TO (3 frameworks)
    "regchain_crosscheck_distinct_csf": 30,
    "regchain_crosscheck_raw_alignments": 142,
}


# ---------------------------------------------------------------------------
# ID patterns (v2.1-port — Case_03-specific; DORA branch live)
# ---------------------------------------------------------------------------
ID_PATTERNS: dict[str, str] = {
    "Stakeholder":          r"^STK-[A-Z]+-\d{2}$",
    "BusinessGoal":         r"^BG-\d{2}$",
    "CoverageGap":          r"^GAP-\d{2,3}$",   # Case_03 canonical: GAP-01..GAP-12 (2-digit; Doc07 §7 / GAPS xlsx)
    "AdjustedGoal":         r"^AG-D-\d{2}\.\d{1}-(001|002)$",
    "RegulatoryClause":     r"^(GDPR|CRA|NIS2|DORA|AI)-C\d{2}$",   # Case_03: 5 regulations, DORA branch live
    "SecurityControlDomain":r"^D-\d{2}\.\d{1}$",
    "Domain":               r"^D-\d{2}$",
    "Regulation":           r"^REG-[A-Z0-9]+$",
    "CompanyContext":       r"^CC-[A-Z]+-\d{4}-\d{3}$",
    "Tension":              r"^T-\d{3}$",                    # T-001..T-005 in Case_03
    "RaciRole":             r"^ROLE-[A-Z0-9]+$",
    "RaciActivity":         r"^ACT-\d{2}$",
    "System":               r"^SYS-\d{2}$",
    "DataStore":            r"^STORE-\d{2}$",
    "DataFlow":             r"^FLOW-\d{2}$",
    "ThirdParty":           r"^[A-Z][A-Za-z0-9_]+$",          # vendor enumeration from Doc06
    "PersonalDataCategory": r"^.+$",                          # names are freeform
    "DataSubjectCategory":  r"^DSC-.+$",                      # DSC-<slug>
    "NistControl":          r"^NIST-[A-Z0-9.\-]+$",
    "NistControlSafe":      r"^NIST-[A-Za-z0-9._\-]{1,80}$",
    "EvidenceItem":         r"^EV-D-\d{2}\.\d{1}-\d{3}$",
    "TierDecision":         r"^TD-[A-Z0-9-]+-(GV|ID|PR|DE|RS|RC|ORG)-\d{3}$",
}


def load_ontology_types() -> set[str]:
    """Return the set of node types declared in the compact.json."""
    data = json.load(open(COMPACT, encoding="utf-8"))
    return set(data.get("classes", {}).keys())


def load_ontology_relations() -> set[str]:
    data = json.load(open(COMPACT, encoding="utf-8"))
    return {r["verb"] for r in data.get("relations", []) if r.get("status") != "deferred"}


# ---------------------------------------------------------------------------
# Gate functions (v2.1-port — same names as Case_01/02 for parity)
# ---------------------------------------------------------------------------

def check_invariants(graph: dict, strict: bool = False) -> list[str]:
    errors: list[str] = []
    inv = graph.get("invariants", {})
    for k, want in EXPECTED.items():
        got = inv.get(k)
        if got != want:
            errors.append(f"Invariant {k}: expected {want}, got {got}")
    return errors


def check_audit_node_ids(graph: dict, strict: bool = False) -> list[str]:
    errors: list[str] = []
    all_ids = {n["id"] for n in graph.get("nodes", [])}
    for a in graph.get("audits", []):
        for nid in a.get("node_ids", []):
            if nid not in all_ids:
                errors.append(f"Audit {a.get('id')} references unknown node id: {nid}")
                return errors  # early-exit on first dangling audit
    return errors


def check_phase_c(graph: dict, strict: bool = False) -> list[str]:
    """v2.3 maturity gates (Gate 1-4). Mirrors Case_01/02."""
    errors: list[str] = []
    sds     = {n["id"]: n for n in graph.get("nodes", []) if n["type"] == "SecurityControlDomain"}
    all_ids = {n["id"] for n in graph.get("nodes", [])}

    # Gate 1: no forbidden maturity scalars on sub-domain
    FORBIDDEN = ("tier", "maturity_cur", "maturity_tgt", "maturity_score", "capability_score")
    hits = [(sid, fk) for sid, n in sds.items() for fk in FORBIDDEN if fk in n.get("attrs", {})]
    if hits:
        sample = hits[:5]
        errors.append(
            f"Gate 1: forbidden maturity scalars on sub-domain scope "
            f"({len(hits)} hits); sample: " +
            ", ".join(f"{sid}.{fk}" for sid, fk in sample)
        )

    # Gate 2: 11 proportionality keys on every active sub-domain
    sd_required_keys = (
        "i", "p", "satisfaction_pattern", "evidence_depth",
        "verification_method", "ownership", "example_controls", "notes",
        "risk_if_not_met", "evidence_ids", "implementation_priority",
    )
    bad = sum(1 for n in sds.values() if n["attrs"].get("active") is True
               and any(k not in n["attrs"] for k in sd_required_keys))
    if bad:
        errors.append(f"Gate 2: {bad} active SecurityControlDomain(s) missing proportionality attrs keys")

    # Gate 3: proportionality_tier non-null on every active sub-domain
    bad = [sid for sid, n in sds.items()
           if n["attrs"].get("active") is True
           and n["attrs"].get("proportionality_tier") is None]
    if bad:
        errors.append(f"Gate 3: {len(bad)} active SecurityControlDomain(s) lack proportionality_tier; sample: {bad[:5]}")

    # Gate 4: citation discipline on every EvidenceItem
    evis = [n for n in graph.get("nodes", []) if n["type"] == "EvidenceItem"]
    bad_src = []
    for n in evis:
        a = n.get("attrs", {})
        sources = a.get("sources") or []
        if not sources:
            bad_src.append((n["id"], "EMPTY_SOURCES"))
            continue
        for src in sources:
            if src.startswith(("Doc", "doc", "§", "OVERLAY")) or " " in src:
                continue
            if src not in all_ids:
                bad_src.append((n["id"], f"UNKNOWN_SOURCE:{src}"))
    if bad_src:
        sample = bad_src[:5]
        errors.append(
            f"Gate 4 (citation discipline) failed on {len(bad_src)} EvidenceItem entries; sample: " +
            ", ".join(f"{eid}[{why}]" for eid, why in sample)
        )

    return errors


def check_phase_d(graph: dict, strict: bool = False) -> list[str]:
    """NistControl framework/function/ID regex/ALIGNS_TO integrity."""
    errors: list[str] = []
    nc_nodes = [n for n in graph.get("nodes", []) if n["type"] == "NistControl"]
    if not nc_nodes:
        return errors
    seen_ids = set()
    for n in nc_nodes:
        a = n.get("attrs", {})
        if a.get("framework") not in ("CSF", "PF", "AI-RMF"):
            errors.append(f"NistControl {n['id']}: framework={a.get('framework')!r} (expected CSF/PF/AI-RMF)")
        if not a.get("control_id"):
            errors.append(f"NistControl {n['id']}: missing control_id")
        if n["id"] in seen_ids:
            errors.append(f"duplicate NistControl id: {n['id']}")
        seen_ids.add(n["id"])
    # ALIGNS_TO integrity
    aligns_to = [l for l in graph.get("links", []) if l["rel"] == "ALIGNS_TO"]
    all_ids = {n["id"] for n in graph.get("nodes", [])}
    for l in aligns_to:
        if l["from"] not in all_ids or l["to"] not in all_ids:
            errors.append(f"ALIGNS_TO dangling: {l['from']} -> {l['to']}")
    return errors


def check_ontology_types(graph: dict, strict: bool = False) -> list[str]:
    """All node types must be declared in compact.json classes."""
    errors: list[str] = []
    declared = load_ontology_types()
    seen_types = {n["type"] for n in graph.get("nodes", [])}
    unknown = seen_types - declared
    if unknown:
        errors.append(f"Node types not declared in ontology: {unknown}")
    return errors


def check_relation_verbs(graph: dict, strict: bool = False) -> list[str]:
    """All link rel verbs must be declared in compact.json relations (active or
    deferred — deferred is allowed; missing entirely is the error)."""
    errors: list[str] = []
    compact = json.load(open(COMPACT, encoding="utf-8"))
    declared = {r["verb"] for r in compact.get("relations", [])}
    seen_verbs = {l["rel"] for l in graph.get("links", [])}
    unknown = seen_verbs - declared
    if unknown:
        errors.append(f"Relation verbs not declared in ontology: {unknown}")
    return errors


def check_id_patterns(graph: dict, strict: bool = False) -> list[str]:
    """Each node.id must match its type's regex pattern."""
    errors: list[str] = []
    by_type: dict[str, list[str]] = {}
    for n in graph.get("nodes", []):
        t = n["type"]
        pat = ID_PATTERNS.get(t)
        if pat and not re.match(pat, n["id"]):
            by_type.setdefault(t, []).append(n["id"])
    for t, ids in by_type.items():
        sample = ids[:5]
        msg = f"ID pattern mismatch for type {t!r}: {len(ids)} violations; sample: {sample}"
        if strict:
            errors.append(msg)
        else:
            # Warning-only by default (don't block P1 gate); gate v2.1-port
            # surfaces them as "warnings" — keep behaviour consistent with Case_01/02.
            print(f"  [warn] {msg}", file=sys.stderr)
    return errors


def check_provenance(graph: dict, strict: bool = False) -> list[str]:
    """Every node must have a non-empty source[]. Every link must have source[]."""
    errors: list[str] = []
    for n in graph.get("nodes", []):
        if not n.get("source"):
            errors.append(f"Node {n['id']}: missing source[]")
        if strict and len(n.get("source", [])) < 1:
            errors.append(f"Node {n['id']}: source[] empty")
    for l in graph.get("links", []):
        if not l.get("source"):
            errors.append(f"Link {l.get('from')} -> {l.get('to')} ({l.get('rel')}): missing source[]")
    return errors


def check_stale_invariant_counts(graph: dict, strict: bool = False) -> list[str]:
    """Detect counts in graph.invariants that don't match the actual graph."""
    errors: list[str] = []
    inv = graph.get("invariants", {})
    nodes = graph.get("nodes", [])
    links = graph.get("links", [])

    def actual_by_type(t, framework=None):
        return sum(1 for n in nodes
                   if n["type"] == t
                   and (framework is None or n.get("attrs", {}).get("framework") == framework))

    checks = [
        ("domains",              "Domain",               None, "domains"),
        ("regulations_total",    "Regulation",           None, "regulations_total"),
        ("subdomains_total",     "SecurityControlDomain", None, "subdomains_total"),
        ("clauses_total",        "RegulatoryClause",     None, "clauses_total"),
        ("tensions_total",       "Tension",              None, "tensions_total"),
        ("adjusted_goals",       "AdjustedGoal",         None, "adjusted_goals"),
        ("data_subject_categories", "DataSubjectCategory", None, "data_subject_categories"),
        ("evidence_items",       "EvidenceItem",         None, "evidence_items"),
        ("nist_controls",        "NistControl",          None, "nist_controls"),
        ("nist_controls_csf",    "NistControl",          "CSF",   "nist_controls_csf"),
        ("nist_controls_pf",     "NistControl",          "PF",    "nist_controls_pf"),
        ("nist_controls_airmf",  "NistControl",          "AI-RMF", "nist_controls_airmf"),
        ("systems",              "System",               None, "systems"),
        ("data_stores",          "DataStore",            None, "data_stores"),
        ("data_flows",           "DataFlow",             None, "data_flows"),
        ("third_parties",        "ThirdParty",           None, "third_parties"),
        ("personal_data_categories", "PersonalDataCategory", None, "personal_data_categories"),
        ("stakeholders",         "Stakeholder",          None, "stakeholders"),
        ("raci_roles",           "RaciRole",             None, "raci_roles"),
        ("raci_activities",      "RaciActivity",         None, "raci_activities"),
        ("coverage_gaps",        "CoverageGap",          None, "coverage_gaps"),
    ]
    for inv_key, node_type, framework, name in checks:
        if inv.get(inv_key) is not None and inv[inv_key] != actual_by_type(node_type, framework):
            errors.append(
                f"Stale invariant {name}: graph.invariants={inv[inv_key]} but actual "
                f"{node_type}" + (f"[{framework}]" if framework else "") +
                f" count={actual_by_type(node_type, framework)}"
            )
    return errors


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

CHECKS = [
    ("check_invariants",      check_invariants,      True),    # fatal
    ("check_audit_node_ids",  check_audit_node_ids,  True),    # fatal (exit 2 on dangling)
    ("check_phase_c",         check_phase_c,         True),    # fatal
    ("check_phase_d",         check_phase_d,         True),    # fatal
    ("check_ontology_types",  check_ontology_types,  True),    # fatal
    ("check_relation_verbs",  check_relation_verbs,  True),    # fatal
    ("check_id_patterns",     check_id_patterns,     False),   # warning by default
    ("check_provenance",      check_provenance,      False),   # warning by default
    ("check_stale_invariant_counts", check_stale_invariant_counts, True),  # fatal
]


def main(argv: list[str]) -> int:
    strict = "--strict" in argv
    if "--check" in argv:
        graph = json.load(open(GRAPH, encoding="utf-8"))
        all_errors: list[str] = []
        all_warnings: list[str] = []
        for name, fn, fatal in CHECKS:
            errs = fn(graph, strict=strict)
            if errs:
                if fatal:
                    all_errors.extend(errs)
                else:
                    all_warnings.extend(errs)
        if all_warnings:
            print(f"# {len(all_warnings)} warning(s):")
            for w in all_warnings:
                print(f"  [warn] {w}")
        if all_errors:
            print(f"# {len(all_errors)} error(s):")
            for e in all_errors:
                print(f"  - {e}")
            return 1
        print(f"OK — invariants pass, audit node_ids resolve, ontology types/relations valid."
              f" (warnings: {len(all_warnings)})")
        return 0
    if "--emit" in argv:
        sys.stdout.write(json.dumps(json.load(open(GRAPH, encoding="utf-8")), ensure_ascii=False))
        return 0
    if "--summary" in argv:
        g = json.load(open(GRAPH, encoding="utf-8"))
        by_type: dict[str, int] = {}
        for n in g["nodes"]:
            by_type[n["type"]] = by_type.get(n["type"], 0) + 1
        print(json.dumps({"nodes_by_type": by_type, "link_count": len(g["links"])}, ensure_ascii=False))
        return 0
    return main(["--check"])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
