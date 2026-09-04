#!/usr/bin/env python3
"""
build_p2_dashboard.py — AEGIS Case_02 Phase 2 graph validator (v1.0)

Companion to build_p2_graph.py. Validates:
  * check_invariants        — counts match phase2_ontology.yaml@invariants.counts
  * check_audit_node_ids    — every audit references real nodes
  * check_ontology_types    — every node type is in the ontology class set
  * check_relation_verbs    — every link verb is in the ontology relation set
  * check_id_patterns       — IDs match declared regex patterns
  * check_provenance        — every node/link has a source pointer
  * check_stale_invariant_counts — no stale PROJECT_STATE frontmatter scalars

Usage:
    python3 scripts/build_p2_dashboard.py --check
    python3 scripts/build_p2_dashboard.py --emit   # print graph as JSON
    python3 scripts/build_p2_dashboard.py --summary
    python3 scripts/build_p2_dashboard.py --strict  # exit 1 on WARNING
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAPH = ROOT / "data" / "phase2_graph.json"
COMPACT = ROOT / "data" / "phase2_ontology.compact.json"

# Ontology-derived class set + relation set (loaded from compact.json)
ONTO_CLASSES = set()
ONTO_RELATIONS = set()
ID_PATTERNS: dict[str, str] = {}
EXPECTED_COUNTS: dict[str, int] = {}


def load_ontology() -> None:
        global ONTO_CLASSES, ONTO_RELATIONS, ID_PATTERNS, EXPECTED_COUNTS
        onto = json.loads(COMPACT.read_text(encoding="utf-8"))
        ONTO_CLASSES = set(onto["classes"].keys())
        ONTO_RELATIONS = {r["verb"] for r in onto["relations"]}
        ID_PATTERNS = onto["invariants"]["id_patterns"]
        EXPECTED_COUNTS = onto["invariants"]["counts"]


# ---------------------------------------------------------------------------
# Checks (return list of strings; "" = pass, non-empty = finding)
# ---------------------------------------------------------------------------
def check_invariants(graph: dict) -> list[str]:
        findings = []
        actual = graph["invariants"]["counts"]
        for k, v in EXPECTED_COUNTS.items():
                # Skip "soft" keys: _min (audit-only thresholds) and _with_cr (informational)
                if k.endswith("_min") or k.endswith("_with_cr"):
                        continue
                if k not in actual:
                        findings.append(f"[invariants] MISSING key '{k}'")
                elif actual[k] != v:
                        sev = "ERROR" if k.endswith("_total") or k == "controls_total" else "WARN"
                        findings.append(
                                f"[invariants] {sev} {k}: expected {v}, actual {actual[k]}"
                        )
        return findings


def check_audit_node_ids(graph: dict) -> list[str]:
        findings = []
        node_ids = {n["id"] for n in graph["nodes"]}
        for a in graph.get("audits", []):
                for nid in a.get("node_ids", []):
                        if nid not in node_ids:
                                findings.append(
                                        f"[audit_node_ids] audit {a['id']} references unknown node {nid}"
                                )
        return findings


def check_ontology_types(graph: dict) -> list[str]:
        findings = []
        # Allow CompanyContext as a carry-over from Phase 1 ontology (not redefined in P2)
        allowed_extras = {"CompanyContext"}
        for n in graph["nodes"]:
                if n["type"] not in ONTO_CLASSES and n["type"] not in allowed_extras:
                        findings.append(f"[ontology_types] unknown node type '{n['type']}' for {n['id']}")
        return findings


def check_relation_verbs(graph: dict) -> list[str]:
        findings = []
        for l in graph["links"]:
                if l["rel"] not in ONTO_RELATIONS:
                        findings.append(f"[relation_verbs] unknown verb '{l['rel']}' for {l['from']}→{l['to']}")
        return findings


def check_id_patterns(graph: dict) -> list[str]:
        findings = []
        # Map type -> pattern key
        type_to_pattern = {
                "Obligation": "obligation",
                "PrivacyOperationalObjective": "privacy_objective",
                "SecurityOperationalObjective": "security_objective",
                "ComplianceRule": "compliance_rule",
                "BestPracticeRule": "best_practice_rule",
                "Tension": "tension",
                "NistSubcategory": None,  # multiple (csf/pf); checked below
        }
        for n in graph["nodes"]:
                t = n["type"]
                if t == "NistSubcategory":
                        fw = n.get("attrs", {}).get("framework", "")
                        pat_key = "nist_subcategory_csf" if fw == "CSF" else "nist_subcategory_pf"
                        if not re.match(ID_PATTERNS[pat_key], n["id"]):
                                findings.append(
                                        f"[id_patterns] {n['id']} (NistSubcategory/{fw}) does not match {pat_key}"
                                )
                        continue
                pk = type_to_pattern.get(t)
                if pk and not re.match(ID_PATTERNS[pk], n["id"]):
                        findings.append(f"[id_patterns] {n['id']} ({t}) does not match {pk}")
        return findings


def check_provenance(graph: dict) -> list[str]:
        findings = []
        for n in graph["nodes"]:
                if not n.get("source"):
                        findings.append(f"[provenance] node {n['id']} missing 'source'")
        for i, l in enumerate(graph["links"]):
                if not l.get("source"):
                        findings.append(f"[provenance] link #{i} ({l['from']}→{l['to']}) missing 'source'")
        return findings


def check_stale_invariant_counts(graph: dict) -> list[str]:
        """Cross-check: PROJECT_STATE.md frontmatter may claim stale totals.
        Not a blocking error — just an informational warning if mismatch.
        """
        findings = []
        ps = ROOT / "PROJECT_STATE.md"
        if not ps.exists():
                return findings
        text = ps.read_text(encoding="utf-8")
        # Look for stale scalar: total_obligations: 30
        m = re.search(r"^total_obligations:\s*(\d+)\s*$", text, re.MULTILINE)
        if m and int(m.group(1)) != graph["invariants"]["counts"]["obligations_total"]:
                findings.append(
                        f"[stale_invariant_counts] PROJECT_STATE.md@total_obligations={m.group(1)} but graph says {graph['invariants']['counts']['obligations_total']}"
                )
        return findings


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
CHECKS = [
        ("check_invariants", check_invariants),
        ("check_audit_node_ids", check_audit_node_ids),
        ("check_ontology_types", check_ontology_types),
        ("check_relation_verbs", check_relation_verbs),
        ("check_id_patterns", check_id_patterns),
        ("check_provenance", check_provenance),
        ("check_stale_invariant_counts", check_stale_invariant_counts),
]


def run_all(graph: dict, strict: bool = False) -> int:
        load_ontology()
        rc = 0
        for name, fn in CHECKS:
                findings = fn(graph)
                if findings:
                        print(f"\n[{name}] {len(findings)} finding(s):")
                        for f in findings:
                                print(f"  - {f}")
                                # In non-strict mode, stale_invariant_counts is informational
                                if "stale_invariant_counts" in f and not strict:
                                        continue
                                if strict or f.startswith("[invariants] ERROR"):
                                        rc = 1
                else:
                        print(f"[{name}] PASS")
        return rc


def main() -> int:
        ap = argparse.ArgumentParser(description="Phase 2 graph validator")
        ap.add_argument("--check", action="store_true", help="Run all checks")
        ap.add_argument("--strict", action="store_true", help="Treat WARN as ERROR")
        ap.add_argument("--summary", action="store_true", help="Print counts summary")
        ap.add_argument("--emit", action="store_true", help="Print graph JSON to stdout")
        ap.add_argument("--graph", default=str(GRAPH), help="Graph JSON path")
        args = ap.parse_args()

        graph = json.loads(Path(args.graph).read_text(encoding="utf-8"))

        if args.emit:
                print(json.dumps(graph, indent=2, ensure_ascii=False))
                return 0
        if args.summary:
                counts = graph["invariants"]["counts"]
                print(json.dumps(counts, indent=2))
                print(f"audits: {len(graph.get('audits', []))}")
                return 0
        if args.check:
                rc = run_all(graph, strict=args.strict)
                if rc == 0:
                        print("\n[validator] PASS — Phase 2 graph OK")
                else:
                        print("\n[validator] FAIL — see findings above")
                return rc

        ap.print_help()
        return 1


if __name__ == "__main__":
        sys.exit(main())