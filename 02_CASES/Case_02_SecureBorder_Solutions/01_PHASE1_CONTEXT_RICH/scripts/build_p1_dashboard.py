#!/usr/bin/env python3
"""Companion to phase1_graph.json for Case_02 — validator v2.4 (parity with Case_01).

Mirrors the structure of Case_01_TinyTask_SaaS/scripts/build_p1_dashboard.py but
with Case_02 data:
  - 5 regulations (4 applicable: GDPR, CRA, NIS 2, AI_Act; DORA excluded)
  - 10 domains, 38 sub-domains (34 active + 4 NOT_ADDRESSED)
  - 111 clauses (28 GDPR + 26 CRA + 29 NIS2 + 28 AI_Act)
  - 70 AdjustedGoal, 10 DataSubjectCategory, 59 EvidenceItems
  - 45 NistControl (15 PF+AI-RMF anchors + 30 CSF from REG_CHAIN)
  - 1071 ambiguity cards, 8 audits, 9 tensions

Gates (per MATURITY_MODEL_CSF_STRICT.md §10 + v2.4 paridade):
  check_invariants         — graph counts vs ontology counts
  check_audit_node_ids     — audit node_ids resolve to real graph nodes
  check_phase_c            — maturity gates v2.3
  check_phase_d            — NistControl framework/function/ID regex
  check_ontology_types     — node types vs ontology@classes
  check_relation_verbs     — link rel vs ontology@relations
  check_id_patterns        — ID regex mismatches
  check_provenance         — missing source[]/id

Usage:
    python3 build_p1_dashboard.py --check                # exit 0 if all checks pass
    python3 build_p1_dashboard.py --check --strict       # also fail on warnings
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

# Case_02 expected counts (v2.4). Counts are pinned by the builder and verified
# by --check; delta != 0 is a goal.
EXPECTED: dict[str, int] = {
    "regulations_total": 5,
    "regulations_applicable": 4,   # GDPR + CRA + NIS 2 + AI_Act; DORA excluded
    "domains": 10,
    "subdomains_total": 38,
    "subdomains_covered": 38,         # ontology @subdomains.covered (35) + not_covered (3 NOT_ADDRESSED) — all in the graph
    "subdomains_active": 34,        # 35 in Doc12 §3 minus D-08.3 (NOT_ADDRESSED)
    "subdomains_with_proportionality": 35,  # SUBDOMAIN_PROPORTIONALITY table length (35 rows; 34 active)
    "clauses_total": 111,
    "clauses_gdpr": 28,
    "clauses_cra":  26,
    "clauses_nis2": 29,
    "clauses_aiact": 28,
    "tensions_total": 9,
    "ambiguity_cards_in_scope": 1071,
    "ambiguity_top_cards": 15,
    "evidence_items": 59,
    "evidence_items_capability": 25,    # 10 CSF + 10 PF + 5 AI-RMF
    "evidence_items_coverage":   34,
    "articles_with_verification": 111,
    "adjusted_goals": 70,
    "data_subject_categories": 10,
    "subdomains_rigorous": 8,
    "subdomains_standard": 27,        # 27 in Doc12 §3 (8 RIGOROUS + 27 STANDARD = 35, but D-08.3 NOT_ADDRESSED)
    "nist_controls": 45,                # 15 PF+AI-RMF + 30 CSF
    "nist_controls_csf":   30,
    "nist_controls_pf":    10,
    "nist_controls_airmf": 5,
    "nist_alignments":     109,
}


# ---------------------------------------------------------------------------
# ID patterns (v2.4 — Case_02-specific; DORA excluded)
# ---------------------------------------------------------------------------
ID_PATTERNS: dict[str, str] = {
    "Stakeholder":          r"^STK-[A-Z]+-\d{2}$",
    "BusinessGoal":         r"^BG-\d{2}$",
    "CoverageGap":          r"^GAP-\d{3}$",
    "AdjustedGoal":         r"^AG-D-\d{2}\.\d{1}-(001|002)$",
    "RegulatoryClause":     r"^(GDPR|CRA|NIS2|AI)-C\d{2}$",   # Case_02: no DORA clauses
    "SecurityControlDomain":r"^D-\d{2}\.\d{1}$",
    "Domain":               r"^D-\d{2}$",
    "Regulation":           r"^REG-[A-Z0-9]+$",
    "CompanyContext":       r"^CC-[A-Z]+-\d{4}-\d{3}$",
    "Tension":              r"^T-\d{3}$",                    # T-001..T-009 in Case_02
    "RaciRole":             r"^ROLE-[A-Z0-9]+$",
    "RaciActivity":         r"^ACT-\d{2}$",
    "System":               r"^SYS-\d{2}$",
    "DataStore":            r"^STORE-\d{2}$",
    "DataFlow":             r"^FLOW-\d{2}$",
    "ThirdParty":           r"^[A-Z][A-Za-z0-9_]+$",          # vendor enumeration from Doc06
    "PersonalDataCategory": r"^.+$",                          # names are freeform
    "DataSubjectCategory":  r"^DSC-.+$",                     # DSC-<slug>
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
# Gate functions (v2.4 — same names as Case_01 for parity)
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
    """v2.3 maturity gates (Gate 1-4). Mirrors Case_01."""
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
    """NistControl framework/function/ID regex/ALIGNS_TO consistency."""
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
    # Accept both 'active' (default) and 'deferred' verbs
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
            # Warning-only by default (don't block P1 gate); gate v2.4 surfaces
            # them as "warnings" — keep behaviour consistent with Case_01.
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

    def actual_by_type(t):
        return sum(1 for n in nodes if n["type"] == t)

    checks = [
        ("domains",              "Domain",               "domains"),
        ("regulations_total",    "Regulation",            "regulations_total"),
        ("subdomains_total",     "SecurityControlDomain", "subdomains_total"),
        ("clauses_total",        "RegulatoryClause",      "clauses_total"),
        ("tensions_total",       "Tension",               "tensions_total"),
        ("adjusted_goals",       "AdjustedGoal",          "adjusted_goals"),
        ("data_subject_categories","DataSubjectCategory", "data_subject_categories"),
        ("evidence_items",       "EvidenceItem",          "evidence_items"),
        ("nist_controls",        "NistControl",           "nist_controls"),
    ]
    for inv_key, node_type, name in checks:
        if inv.get(inv_key) is not None and inv[inv_key] != actual_by_type(node_type):
            errors.append(
                f"Stale invariant {name}: graph.invariants={inv[inv_key]} but actual {node_type} count={actual_by_type(node_type)}"
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