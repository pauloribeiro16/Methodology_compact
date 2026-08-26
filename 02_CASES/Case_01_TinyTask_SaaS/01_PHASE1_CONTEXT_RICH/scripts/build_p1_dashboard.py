#!/usr/bin/env python3
"""Companion to phase1_graph.json — inlines the graph into the dashboard HTML.

Usage
-----
    python3 build_p1_dashboard.py --check     # exits 0 if invariants + audit
                                       # node_ids resolve, 1 if invariant
                                       # violation, 2 if dangling audit ref.
    python3 build_p1_dashboard.py --emit      # print the JSON for inlining
    python3 build_p1_dashboard.py --summary   # print a one-line summary

Why a separate script
---------------------
Dashboards in this repo are opened via ``file://`` and cannot fetch external
JSON (no CORS, no fetch). The Phase 1 dashboard embeds the graph as a
``window.PHASE1_GRAPH`` constant injected by this script. The graph itself
is produced by ``build_p1_graph.py``; this script reads that file and runs
the validation gate.

Stdlib only (json, sys, pathlib, argparse). No external deps.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Resolve data/phase1_graph.json relative to this script.
HERE = Path(__file__).resolve().parent
GRAPH_PATH = HERE.parent / "data" / "phase1_graph.json"


def load_graph() -> dict:
    if not GRAPH_PATH.exists():
        print(f"ERROR: graph file not found: {GRAPH_PATH}", file=sys.stderr)
        sys.exit(2)
    with GRAPH_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def check_invariants(graph: dict) -> list[str]:
    """Return a list of invariant violation messages (empty = pass)."""
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

    # Cross-check applicable regulations
    applicable_regs = [n for n in graph.get("nodes", []) if n["type"] == "Regulation" and n["attrs"].get("applicable")]
    if len(applicable_regs) != expected["regulations_applicable"]:
        errors.append(f"applicable regulations: expected {expected['regulations_applicable']}, got {len(applicable_regs)}")

    # Cross-check ambiguity total
    ambig_total = graph.get("ambiguity", {}).get("stats_total", {}).get("cards_in_scope")
    if ambig_total != expected["ambiguity_cards_in_scope"]:
        errors.append(f"ambiguity cards_in_scope: expected {expected['ambiguity_cards_in_scope']}, got {ambig_total}")

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


def cmd_check(graph: dict) -> int:
    inv_errors = check_invariants(graph)
    audit_errors = check_audit_node_ids(graph)
    if inv_errors:
        print("INVARIANT VIOLATIONS:", file=sys.stderr)
        for e in inv_errors:
            print(f"  - {e}", file=sys.stderr)
    if audit_errors:
        print("DANGLING AUDIT REFERENCES:", file=sys.stderr)
        for e in audit_errors:
            print(f"  - {e}", file=sys.stderr)
    if inv_errors:
        return 1
    if audit_errors:
        return 2
    print("OK — invariants pass, audit node_ids resolve.", file=sys.stderr)
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
                       help="Exit 0 if invariants + audit node_ids resolve, "
                            "1 if invariant violation, 2 if dangling audit ref")
    group.add_argument("--emit", action="store_true",
                       help="Print the JSON for inlining into the dashboard")
    group.add_argument("--summary", action="store_true",
                       help="Print a one-line summary as JSON")
    args = parser.parse_args(argv[1:])

    graph = load_graph()
    if args.check:
        return cmd_check(graph)
    if args.emit:
        return cmd_emit(graph)
    if args.summary:
        return cmd_summary(graph)
    return 2  # unreachable


if __name__ == "__main__":
    sys.exit(main(sys.argv))