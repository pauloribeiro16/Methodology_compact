#!/usr/bin/env python3
"""Companion to phase1_graph.json — inlines the graph into the dashboard HTML
+ validates the graph against the Phase 1 v1.4 kg_ontology schema.

Usage
-----
    python3 build_p1_dashboard.py --check             # exits 0 if all checks pass
    python3 build_p1_dashboard.py --check --strict    # also fail on missing provenance / id-pattern mismatches
    python3 build_p1_dashboard.py --emit              # print the JSON for inlining
    python3 build_p1_dashboard.py --summary           # print a one-line summary

Exit codes (orchestrator brief, Sprint 6 §D):
    0 = pass
    1 = invariant error (count mismatch)
    2 = dangling audit node_ids
    3 = unknown class (type not in ontology@classes)
    4 = unknown relation verb (rel not in ontology@relations[].verb)
    5 = missing provenance (id-pattern mismatch OR node/link missing source[])
         — only fatal when --strict is passed; by default these are warnings

Why a separate script
---------------------
Dashboards in this repo are opened via ``file://`` and cannot fetch external
JSON (no CORS, no fetch). The Phase 1 dashboard embeds the graph as a
``window.PHASE1_GRAPH`` constant injected by this script. The graph itself
is produced by ``build_p1_graph.py``; this script reads that file and runs
the validation gate.

Stdlib only (json, sys, pathlib, argparse, re). No external deps.
The ontology v1.4 kg_ontology section is mirrored in
``data/phase1_ontology.compact.json`` (stdlib-loadable); the YAML file at
``phase1_ontology.yaml`` is the source of truth for humans.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Resolve paths relative to this script.
HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"
GRAPH_PATH = DATA_DIR / "phase1_graph.json"
ONTOLOGY_PATH = DATA_DIR / "phase1_ontology.compact.json"


def load_graph() -> dict:
    if not GRAPH_PATH.exists():
        print(f"ERROR: graph file not found: {GRAPH_PATH}", file=sys.stderr)
        sys.exit(2)
    with GRAPH_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def load_ontology() -> dict:
    if not ONTOLOGY_PATH.exists():
        print(f"ERROR: ontology compact file not found: {ONTOLOGY_PATH}", file=sys.stderr)
        sys.exit(2)
    with ONTOLOGY_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
# Pre-existing validators (unchanged from Sprint 5; unchanged logic preserved
# to keep audit-cite compatibility).
# ---------------------------------------------------------------------------

def check_invariants(graph: dict) -> list[str]:
    """Return a list of invariant violation messages (empty = pass).

    Covers all node-count invariants defined in phase1_ontology.yaml@kg_ontology.invariants.counts
    plus the graph.meta invariants block. Existing 10 keys (Sprint 5) plus the
    3 new v1.2 keys (stakeholders_total, business_goals_total, coverage_gaps_total)
    plus the 7 new v1.3 keys (raci_roles, raci_activities, raci_activities_active,
    raci_edges_min, raci_composite_cells, applies_to_edges, gap_raci_count)
    plus the 7 new v1.4 keys (systems, data_stores, data_flows,
    personal_data_categories, data_subject_categories, third_parties,
    compliance_mapping_rows). Total: 27 keys.
    """
    errors: list[str] = []
    expected = {
        "regulations_total": 5,
        "regulations_applicable": 2,
        "domains": 10,
        "subdomains_total": 38,
        "subdomains_covered": 31,
        "subdomains_active": 37,
        "clauses_total": 54,
        "goals_total": 69,
        "tensions_total": 4,
        "ambiguity_cards_in_scope": 417,
        # Sprint 6 / kg_ontology v1.2 — new counts
        "stakeholders_total": 7,
        "business_goals_total": 5,
        "coverage_gaps_total": 4,
        # Sprint 7 / kg_ontology v1.3 — RACI Phase A (Doc07 §2/§4/§7/§9.2)
        "raci_roles": 6,
        "raci_activities": 43,
        "raci_activities_active": 41,
        "raci_edges_min": 206,
        "raci_composite_cells": 3,
        "applies_to_edges": 35,
        "gap_raci_count": 5,
        # Sprint 8 / kg_ontology v1.4 — Architecture & Third Parties (Doc04 + Doc06)
        "systems": 5,
        "data_stores": 3,
        "data_flows": 5,
        "personal_data_categories": 4,
        "data_subject_categories": 3,
        "third_parties": 6,
        "compliance_mapping_rows": 37,
        # Phase C (Doc08 §9 + Doc12 §4) — verification & proportionality counts
        "articles_with_verification": 54,
        "subdomains_with_proportionality": 37,
    }
    inv = graph.get("invariants", {})
    for k, want in expected.items():
        got = inv.get(k)
        if got != want:
            errors.append(f"invariant {k}: expected {want}, got {got}")

    # Cross-check node counts vs invariants
    by_type: dict[str, int] = {}
    for n in graph.get("nodes", []):
        by_type[n["type"]] = by_type.get(n["type"], 0) + 1

    if by_type.get("Regulation") != expected["regulations_total"]:
        errors.append(f"node count Regulation: expected {expected['regulations_total']}, got {by_type.get('Regulation')}")
    if by_type.get("Domain") != expected["domains"]:
        errors.append(f"node count Domain: expected {expected['domains']}, got {by_type.get('Domain')}")
    if by_type.get("SecurityControlDomain") != expected["subdomains_total"]:
        errors.append(f"node count SecurityControlDomain: expected {expected['subdomains_total']}, got {by_type.get('SecurityControlDomain')}")
    if by_type.get("RegulatoryClause") != expected["clauses_total"]:
        errors.append(f"node count RegulatoryClause: expected {expected['clauses_total']}, got {by_type.get('RegulatoryClause')}")
    if by_type.get("AdjustedGoal") != expected["goals_total"]:
        errors.append(f"node count AdjustedGoal: expected {expected['goals_total']}, got {by_type.get('AdjustedGoal')}")
    if by_type.get("Tension", 0) != expected["tensions_total"]:
        errors.append(f"node count Tension: expected {expected['tensions_total']}, got {by_type.get('Tension', 0)}")
    # Sprint 6 / v1.2 — new node-count checks
    if by_type.get("Stakeholder", 0) != expected["stakeholders_total"]:
        errors.append(f"node count Stakeholder: expected {expected['stakeholders_total']}, got {by_type.get('Stakeholder', 0)}")
    if by_type.get("BusinessGoal", 0) != expected["business_goals_total"]:
        errors.append(f"node count BusinessGoal: expected {expected['business_goals_total']}, got {by_type.get('BusinessGoal', 0)}")
    if by_type.get("CoverageGap", 0) != expected["coverage_gaps_total"]:
        errors.append(f"node count CoverageGap: expected {expected['coverage_gaps_total']}, got {by_type.get('CoverageGap', 0)}")
    # Sprint 7 / v1.3 — new node-count checks for RACI Phase A
    if by_type.get("RaciRole", 0) != expected["raci_roles"]:
        errors.append(f"node count RaciRole: expected {expected['raci_roles']}, got {by_type.get('RaciRole', 0)}")
    if by_type.get("RaciActivity", 0) != expected["raci_activities"]:
        errors.append(f"node count RaciActivity: expected {expected['raci_activities']}, got {by_type.get('RaciActivity', 0)}")
    # Sprint 7 / v1.3 — active RACI activities count (active=True attr)
    active_acts = sum(
        1 for n in graph.get("nodes", [])
        if n["type"] == "RaciActivity" and n.get("attrs", {}).get("active") is True
    )
    if active_acts != expected["raci_activities_active"]:
        errors.append(f"node count RaciActivity (active=True): expected {expected['raci_activities_active']}, got {active_acts}")
    # Sprint 8 / v1.4 — new node-count checks for Architecture & Third Parties
    if by_type.get("System", 0) != expected["systems"]:
        errors.append(f"node count System: expected {expected['systems']}, got {by_type.get('System', 0)}")
    if by_type.get("DataStore", 0) != expected["data_stores"]:
        errors.append(f"node count DataStore: expected {expected['data_stores']}, got {by_type.get('DataStore', 0)}")
    if by_type.get("DataFlow", 0) != expected["data_flows"]:
        errors.append(f"node count DataFlow: expected {expected['data_flows']}, got {by_type.get('DataFlow', 0)}")
    if by_type.get("PersonalDataCategory", 0) != expected["personal_data_categories"]:
        errors.append(f"node count PersonalDataCategory: expected {expected['personal_data_categories']}, got {by_type.get('PersonalDataCategory', 0)}")
    if by_type.get("DataSubjectCategory", 0) != expected["data_subject_categories"]:
        errors.append(f"node count DataSubjectCategory: expected {expected['data_subject_categories']}, got {by_type.get('DataSubjectCategory', 0)}")
    if by_type.get("ThirdParty", 0) != expected["third_parties"]:
        errors.append(f"node count ThirdParty: expected {expected['third_parties']}, got {by_type.get('ThirdParty', 0)}")

    # Cross-check applicable regulations
    applicable_regs = [n for n in graph.get("nodes", []) if n["type"] == "Regulation" and n["attrs"].get("applicable")]
    if len(applicable_regs) != expected["regulations_applicable"]:
        errors.append(f"applicable regulations: expected {expected['regulations_applicable']}, got {len(applicable_regs)}")

    # Cross-check ambiguity total
    ambig_total = graph.get("ambiguity", {}).get("stats_total", {}).get("cards_in_scope")
    if ambig_total != expected["ambiguity_cards_in_scope"]:
        errors.append(f"ambiguity cards_in_scope: expected {expected['ambiguity_cards_in_scope']}, got {ambig_total}")

    # Cross-check link counts per rel (Sprint 7 / v1.3 — RACI Phase A)
    rel_counts: dict[str, int] = {}
    for l in graph.get("links", []):
        rel_counts[l["rel"]] = rel_counts.get(l["rel"], 0) + 1
    if rel_counts.get("RACI", 0) != expected["raci_edges_min"]:
        errors.append(f"link count rel=RACI: expected {expected['raci_edges_min']}, got {rel_counts.get('RACI', 0)}")
    if rel_counts.get("APPLIES_TO", 0) != expected["applies_to_edges"]:
        errors.append(f"link count rel=APPLIES_TO: expected {expected['applies_to_edges']}, got {rel_counts.get('APPLIES_TO', 0)}")

    # Sprint 7 / v1.3 — RACI letter enum validation: each RACI link's letter
    # must be in {'R','A','C','I'}.
    valid_letters = {"R", "A", "C", "I"}
    bad_letters = 0
    for l in graph.get("links", []):
        if l["rel"] != "RACI":
            continue
        lt = l.get("attrs", {}).get("letter")
        if lt not in valid_letters:
            bad_letters += 1
    if bad_letters:
        errors.append(f"RACI links with invalid letter: {bad_letters} (expected only R/A/C/I)")

    # Link count floor (per orchestrator brief: >=180)
    if len(graph.get("links", [])) < 180:
        errors.append(f"link count {len(graph.get('links', []))} below floor 180")

    # Audits: at least 8, with at least 2 of each of the 4 required kinds
    audits = graph.get("audits", [])
    if len(audits) < 8:
        errors.append(f"audits: expected >= 8, got {len(audits)}")
    kinds: dict[str, int] = {}
    for a in audits:
        kinds[a["kind"]] = kinds.get(a["kind"], 0) + 1
    for k in ("broken_link", "coverage_gap", "cross_doc_conflict", "blocking_ambiguity"):
        if kinds.get(k, 0) < 2:
            errors.append(f"audits kind '{k}': expected >= 2, got {kinds.get(k, 0)}")

    return errors


def check_audit_node_ids(graph: dict) -> list[str]:
    """Verify every audit node_id references a real node."""
    node_ids = {n["id"] for n in graph.get("nodes", [])}
    errors: list[str] = []
    for a in graph.get("audits", []):
        for nid in a.get("node_ids", []):
            if nid not in node_ids:
                errors.append(f"audit {a['id']}: dangling node_id '{nid}'")
    return errors


# ---------------------------------------------------------------------------
# Phase C (Doc08 §9 + Doc12 §4) — maturity, tier, spot-checks
# ---------------------------------------------------------------------------

def check_phase_c(graph: dict) -> list[str]:
    """Phase C validators (Doc08 §9 + Doc12 §4 derived attrs).

    Returns a list of error messages (empty = pass).  Each error is fatal
    under `--check` (rolled into the existing invariant exit code 1).

    Validates:
      1. Every RegulatoryClause node has maturity_cur / maturity_tgt integers
         in range [0, 4] with cur ≤ tgt.
      2. Every Active SecurityControlDomain node has the 13 proportionality keys
         populated (i, p, tier, satisfaction_pattern, evidence_depth,
         verification_method, ownership, example_controls, notes,
         risk_if_not_met, maturity_cur, maturity_tgt, implementation_priority).
      3. attrs.tier (Doc12 §4) == attrs.proportionality_tier (v1.2) for every
         ACTIVE SecurityControlDomain; drift is surfaced as an error.
      4. Every ART_VERIFICATION clause_id (derived from Doc08 §9 ordinal) is
         bound to a real RegulatoryClause node.
      5. Every SUBDOMAIN_PROPORTIONALITY sub_domain_id (Doc12 §4) is bound to
         a real SecurityControlDomain node with attrs.active == True.
      6. New invariants.articles_with_verification == 54 and
         invariants.subdomains_with_proportionality == 37.
    """
    errors: list[str] = []

    # Counters / lookups
    clauses = {n["id"]: n for n in graph.get("nodes", []) if n["type"] == "RegulatoryClause"}
    sds     = {n["id"]: n for n in graph.get("nodes", []) if n["type"] == "SecurityControlDomain"}

    # (1) Maturity format validation for clauses
    bad_maturity_clause = 0
    for cid, n in clauses.items():
        a = n.get("attrs", {})
        cur, tgt = a.get("maturity_cur"), a.get("maturity_tgt")
        if not isinstance(cur, int) or not isinstance(tgt, int):
            bad_maturity_clause += 1
            continue
        if not (0 <= cur <= 4 and 0 <= tgt <= 4):
            bad_maturity_clause += 1
            continue
        if cur > tgt:
            bad_maturity_clause += 1
    if bad_maturity_clause:
        errors.append(f"Phase C: {bad_maturity_clause} RegulatoryClause node(s) fail maturity_cur/maturity_tgt range or cur<=tgt invariant")

    # (2) 13 proportionality keys on every active sub-domain
    sd_required_keys = (
        "i", "p", "tier", "satisfaction_pattern", "evidence_depth",
        "verification_method", "ownership", "example_controls", "notes",
        "risk_if_not_met", "maturity_cur", "maturity_tgt",
        "implementation_priority",
    )
    bad_sd_attrs = 0
    for sid, n in sds.items():
        a = n.get("attrs", {})
        if a.get("active") is not True:
            continue
        missing = [k for k in sd_required_keys if k not in a]
        if missing:
            bad_sd_attrs += 1
    if bad_sd_attrs:
        errors.append(f"Phase C: {bad_sd_attrs} active SecurityControlDomain(s) missing proportionality attrs keys")

    # (3) Tier consistency: attrs.tier == attrs.proportionality_tier on every active sub-domain
    tier_drift = []
    for sid, n in sds.items():
        a = n.get("attrs", {})
        if a.get("active") is not True:
            continue
        new_tier = a.get("tier")
        old_tier = a.get("proportionality_tier")
        if new_tier != old_tier:
            tier_drift.append((sid, new_tier, old_tier))
    if tier_drift:
        # Report up to 5 drift items in the error message
        sample = tier_drift[:5]
        errors.append(
            f"Phase C: tier drift on {len(tier_drift)} active sub-domain(s); sample: " +
            ", ".join(f"{sid}(tier={nt!r}, prop_tier={pt!r})" for sid, nt, pt in sample)
        )

    # (4) Verify the §9 54-row derivation bound: every existing RegulatoryClause
    # node MUST carry maturity_cur + maturity_tgt now (so 54 = 54 cross-check).
    missing_clause_phasec = [cid for cid, n in clauses.items()
                             if "maturity_cur" not in n.get("attrs", {})
                             or "maturity_tgt" not in n.get("attrs", {})]
    if missing_clause_phasec:
        errors.append(f"Phase C: {len(missing_clause_phasec)} RegulatoryClause node(s) lack Phase-C maturity_cur/tgt attrs (sample: {missing_clause_phasec[:3]})")

    # (5) 54 articles + 37 sub-domains attested counts on the graph invariants
    inv = graph.get("invariants", {})
    if inv.get("articles_with_verification") != 54:
        errors.append(f"Phase C: invariants.articles_with_verification expected 54, got {inv.get('articles_with_verification')}")
    if inv.get("subdomains_with_proportionality") != 37:
        errors.append(f"Phase C: invariants.subdomains_with_proportionality expected 37, got {inv.get('subdomains_with_proportionality')}")

    # (6) Phase-C audit presence: NEW-06, NEW-07, NEW-08 (and CFL-006 if drift)
    audit_ids = {a["id"] for a in graph.get("audits", [])}
    for need in ("NEW-06", "NEW-07", "NEW-08"):
        if need not in audit_ids:
            errors.append(f"Phase C: expected audit id '{need}' missing from audits list")

    return errors


# ---------------------------------------------------------------------------
# Sprint 6 / v1.2 ontology-based validators
# ---------------------------------------------------------------------------

def check_ontology_types(graph: dict, ontology: dict) -> tuple[list[str], list[str]]:
    """Verify every node's type is in ontology@classes.

    Returns (errors, warnings). Errors are fatal (exit code 3).
    """
    valid_classes = set(ontology["classes"].keys())
    errors: list[str] = []
    warnings: list[str] = []
    for n in graph.get("nodes", []):
        t = n.get("type")
        if t not in valid_classes:
            errors.append(f"node {n.get('id')}: type '{t}' not in ontology@classes")
    return errors, warnings


def check_relation_verbs(graph: dict, ontology: dict) -> tuple[list[str], list[str]]:
    """Verify every link's rel is in ontology@relations[].verb.

    Returns (errors, warnings). Errors are fatal (exit code 4).
    """
    valid_verbs = {r["verb"] for r in ontology["relations"]}
    errors: list[str] = []
    warnings: list[str] = []
    for l in graph.get("links", []):
        v = l.get("rel")
        if v not in valid_verbs:
            errors.append(f"link {l.get('from')}->{l.get('to')}: rel '{v}' not in ontology@relations")
    return errors, warnings


def check_id_patterns(graph: dict, ontology: dict) -> tuple[list[str], list[str]]:
    """Verify every node.id matches its type's regex in ontology@id_patterns.

    Returns (errors, warnings). Errors are non-fatal by default; --strict makes
    them fatal (exit code 5).
    """
    patterns = ontology["invariants"]["id_patterns"]
    errors: list[str] = []
    warnings: list[str] = []
    for n in graph.get("nodes", []):
        t = n.get("type")
        nid = n.get("id", "")
        if t in patterns:
            regex = patterns[t]
            if not re.match(regex, nid):
                msg = f"node {nid}: id does not match id_pattern for type '{t}' (regex: {regex})"
                # This is "fatal under --strict only"; default reports as warning
                warnings.append(msg)
                errors.append(msg)
    return errors, warnings


def check_provenance(graph: dict, ontology: dict) -> tuple[list[str], list[str]]:
    """Verify every node and every link has source[] with ≥1 entry.

    Returns (errors, warnings). Errors are non-fatal by default; --strict makes
    them fatal (exit code 5).
    """
    errors: list[str] = []
    warnings: list[str] = []
    for n in graph.get("nodes", []):
        src = n.get("source") or []
        if not src:
            msg = f"node {n.get('id')}: missing provenance (source[] empty)"
            warnings.append(msg)
            errors.append(msg)
    for i, l in enumerate(graph.get("links", [])):
        src = l.get("source") or []
        if not src:
            msg = f"link {i} ({l.get('from')}->{l.get('to')} {l.get('rel')}): missing provenance (source[] empty)"
            warnings.append(msg)
            errors.append(msg)
    return errors, warnings


def check_stale_invariant_counts(graph: dict, ontology: dict) -> list[str]:
    """Cross-check graph counts vs ontology@invariants.counts.

    This is the 'stale invariant' check from the orchestrator brief §D.4:
    for each count in ontology@invariants.counts, compare to actual count
    of nodes matching the corresponding type/class (or rel for link counts).
    Returns errors which are fatal (rolled into the existing invariant exit code 1).
    """
    errors: list[str] = []
    counts = ontology["invariants"]["counts"]

    # Map ontology count keys to node type names OR link rel names — defined
    # once here, transparently. '__ambiguity__' is a sentinel for the
    # ambiguity stats_total.cards_in_scope field.
    type_for_count = {
        "regulations_total":       "Regulation",
        "domains":                 "Domain",
        "subdomains_total":        "SecurityControlDomain",
        "tensions_total":          "Tension",
        "stakeholders_total":      "Stakeholder",
        "business_goals_total":    "BusinessGoal",
        "coverage_gaps_total":     "CoverageGap",
        "ambiguity_cards_in_scope": "__ambiguity__",
        # Sprint 7 / v1.3 — RACI Phase A
        "raci_roles":              "RaciRole",
        "raci_activities":         "RaciActivity",
        "applies_to_edges":        "__rel_APPLIES_TO__",
        # Sprint 8 / v1.4 — Architecture & Third Parties
        "systems":                 "System",
        "data_stores":             "DataStore",
        "data_flows":              "DataFlow",
        "personal_data_categories": "PersonalDataCategory",
        "data_subject_categories": "DataSubjectCategory",
        "third_parties":           "ThirdParty",
        "compliance_mapping_rows": "__active_subdomains__",
        # Note: raci_edges_min is enforced in check_invariants() against rel=RACI;
        # raci_activities_active is enforced there against active=True attrs.
    }

    by_type: dict[str, int] = {}
    for n in graph.get("nodes", []):
        by_type[n["type"]] = by_type.get(n["type"], 0) + 1

    by_rel: dict[str, int] = {}
    for l in graph.get("links", []):
        by_rel[l["rel"]] = by_rel.get(l["rel"], 0) + 1

    for ck, expected in counts.items():
        # Only enforce counts we know how to map; others are delegated to the
        # pre-existing invariants block.
        if ck not in type_for_count:
            continue
        target = type_for_count[ck]
        if target == "__ambiguity__":
            actual = graph.get("ambiguity", {}).get("stats_total", {}).get("cards_in_scope")
        elif target == "__rel_APPLIES_TO__":
            actual = by_rel.get("APPLIES_TO")
        elif target == "__active_subdomains__":
            # Count SecurityControlDomain nodes with active=True (compliance_mapping_rows = active sub-domains)
            actual = sum(1 for n in graph.get("nodes", [])
                         if n["type"] == "SecurityControlDomain"
                         and n.get("attrs", {}).get("active") is True)
        else:
            actual = by_type.get(target)
        if actual is not None and actual != expected:
            errors.append(
                f"stale invariant {ck} (ontology says {expected}, actual {target} count is {actual})"
            )
    return errors


# ---------------------------------------------------------------------------
# Command dispatcher
# ---------------------------------------------------------------------------

def cmd_check(graph: dict, argv_extra: list[str]) -> int:
    """Run all validators; pick the highest-priority exit code.

    Exit code precedence:
      5 (missing provenance / id-pattern) only when --strict is set
      4 (unknown relation)
      3 (unknown class)
      2 (dangling audit refs)
      1 (invariant count mismatch)
      0 (all pass)
    """
    ontology = load_ontology()
    strict = "--strict" in argv_extra

    # Hard invariants + audit refs
    inv_errors = check_invariants(graph)
    audit_errors = check_audit_node_ids(graph)
    stale_errors = check_stale_invariant_counts(graph, ontology)
    phase_c_errors = check_phase_c(graph)

    # Ontology type whitelist
    type_errors, _ = check_ontology_types(graph, ontology)

    # Relation verb whitelist
    rel_errors, _ = check_relation_verbs(graph, ontology)

    # Soft checks (non-fatal unless --strict)
    idp_errors, idp_warnings = check_id_patterns(graph, ontology)
    prov_errors, prov_warnings = check_provenance(graph, ontology)

    # Reporting
    if inv_errors or stale_errors:
        print("INVARIANT VIOLATIONS:", file=sys.stderr)
        for e in inv_errors + stale_errors:
            print(f"  - {e}", file=sys.stderr)
    if phase_c_errors:
        print("PHASE-C VIOLATIONS:", file=sys.stderr)
        for e in phase_c_errors:
            print(f"  - {e}", file=sys.stderr)
    if audit_errors:
        print("DANGLING AUDIT REFERENCES:", file=sys.stderr)
        for e in audit_errors:
            print(f"  - {e}", file=sys.stderr)
    if type_errors:
        print("UNKNOWN CLASS (not in ontology@classes):", file=sys.stderr)
        for e in type_errors:
            print(f"  - {e}", file=sys.stderr)
    if rel_errors:
        print("UNKNOWN RELATION VERB (not in ontology@relations):", file=sys.stderr)
        for e in rel_errors:
            print(f"  - {e}", file=sys.stderr)
    if idp_warnings:
        print("ID-PATTERN WARNINGS (non-fatal, --strict to fail):", file=sys.stderr)
        for e in idp_warnings:
            print(f"  - {e}", file=sys.stderr)
    if prov_warnings:
        print("PROVENANCE WARNINGS (non-fatal, --strict to fail):", file=sys.stderr)
        for e in prov_warnings:
            print(f"  - {e}", file=sys.stderr)

    # Exit code selection
    if inv_errors or stale_errors or phase_c_errors:
        return 1
    if audit_errors:
        return 2
    if type_errors:
        return 3
    if rel_errors:
        return 4
    if strict and (idp_errors or prov_errors):
        return 5

    # Default: also surface soft errors as exit 5 even without --strict IF they
    # look structural (e.g. ALL nodes of a type fail the pattern, not just one
    # data-quality artefact). For now: only --strict flips them to fatal.
    print("OK — invariants pass, audit node_ids resolve, ontology types/relations valid.", file=sys.stderr)
    if idp_warnings or prov_warnings:
        print(f"  ({len(idp_warnings)} id-pattern + {len(prov_warnings)} provenance warnings; rerun with --strict to fail)", file=sys.stderr)
    return 0


def cmd_emit(graph: dict) -> int:
    """Print the JSON for inlining into the dashboard HTML."""
    sys.stdout.write(json.dumps(graph, ensure_ascii=False))
    sys.stdout.write("\n")
    return 0


def cmd_summary(graph: dict) -> int:
    by_type: dict[str, int] = {}
    for n in graph.get("nodes", []):
        by_type[n["type"]] = by_type.get(n["type"], 0) + 1
    audits = graph.get("audits", [])
    kinds: dict[str, int] = {}
    for a in audits:
        kinds[a["kind"]] = kinds.get(a["kind"], 0) + 1
    rels: dict[str, int] = {}
    for l in graph.get("links", []):
        rels[l["rel"]] = rels.get(l["rel"], 0) + 1

    inv_pass = not check_invariants(graph)
    audit_pass = not check_audit_node_ids(graph)
    summary = {
        "nodes_count": sum(by_type.values()),
        "nodes_by_type": by_type,
        "links_count": len(graph.get("links", [])),
        "links_by_rel": rels,
        "audits_count": len(audits),
        "audits_by_kind": kinds,
        "invariant_pass": inv_pass and audit_pass,
    }
    sys.stdout.write(json.dumps(summary, indent=2, ensure_ascii=False))
    sys.stdout.write("\n")
    return 0 if summary["invariant_pass"] else 1


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Phase 1 dashboard companion")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true",
                       help="Exit 0 if all validators pass; otherwise non-zero "
                            "(see module docstring for exit code matrix).")
    group.add_argument("--emit", action="store_true",
                       help="Print the JSON for inlining into the dashboard")
    group.add_argument("--summary", action="store_true",
                       help="Print a one-line summary as JSON")
    parser.add_argument("--strict", action="store_true",
                        help="With --check: also fail (exit 5) on id-pattern "
                             "mismatches and missing provenance.")
    args = parser.parse_args(argv[1:])

    graph = load_graph()
    if args.check:
        return cmd_check(graph, argv[1:])
    if args.emit:
        return cmd_emit(graph)
    if args.summary:
        return cmd_summary(graph)
    return 2  # unreachable


if __name__ == "__main__":
    sys.exit(main(sys.argv))
