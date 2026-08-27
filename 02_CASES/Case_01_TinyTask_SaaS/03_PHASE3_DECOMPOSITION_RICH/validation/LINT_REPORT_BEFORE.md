---
document_id: AEGIS-P3-RICH-LINT-BEFORE
title: Lint Report Baseline (Case_01 Phase 3 Rich Mode)
phase: 3
version: 1.0
created: 2026-08-24
updated: 2026-08-24
author: Fase de Especificação 0 Executor
status: BASELINE
case: Case_01_TinyTask_SaaS
branch: feature/aegis-p3-case01-rich
sibling_doc: ../03_PHASE3_DECOMPOSITION/
---

# Lint Report Baseline (Case_01 Phase 3 Rich Mode)

> **Baseline snapshot** captured by running `scripts/run_phase3_lints.py` against the **legacy** `03_PHASE3_DECOMPOSITION/` folder, before any Rich sibling content is populated.
> Fase de Especificação 5 will compare this baseline against the final DEEP-enriched state.

---

## §1 Snapshot metadata

| Field | Value |
|-------|-------|
| Date captured | 2026-08-24 |
| Runner used | `scripts/run_phase3_lints.py --case "TinyTask SaaS"` (legacy mode) |
| Target folder | `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/` |
| Output dir | `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/validation/` |
| Companion JSON | `lint_report_phase3_20260824_111655.json` |
| Companion MD | `lint_report_phase3_20260824_111655.md` |
| Console log | `_lint_run.log` |

---

## §2 Fase de Especificação 0 Fase de Especificação 0 Baseline results (legacy)

| Metric | Count |
|--------|-------|
| Passed | 7 |
| Failed | 0 |
| Warnings | 11 |
| **Total** | **7** |

All 7 Phase 3 lints pass against the legacy folder (use_cases, relationships, variability, nodes, allocation, gates, functional_tree). Warnings are non-blocking; they reflect legacy data-quality issues that the Rich Mode Fase de Especificação 1 reconciliation will surface as findings F-00a..F-00f.

---

## §3 Per-lint metrics (legacy baseline)

### Use Cases Catalog (Doc 13)

- total_use_cases: 29
- total_packages: 6
- priority_distribution: {} (empty — legacy may carry `Priority:` only via columns not parsed by lint regex)
- with_actors: 27
- with_regulation: 17
- with_description: 23
- relationships_include: 0
- relationships_extend: 0
- variability_specializations: 0
- variability_alternatives: 0
- variability_options: 0
- orphan_use_cases: 29 (warning)
- documents_found: 2 (rglob matches Catalog + Review Report under legacy)

### Use Case Relationships (Doc 13a)

- total_relationships: 0
- include_relationships: 0
- refine_relationships: 0
- extend_relationships: 0
- orphan_use_cases: 0
- documents_found: 2
- has_sufficient_data: False (warning)

### Use Case Variability (Doc 13b)

- total_specializations: 0
- total_alternatives: 0
- total_options: 0
- regulations_with_variants: 2 (GDPR, CRA)
- documents_found: 2
- has_sufficient_data: False (warning)
- UCs in variability doc but not in use cases catalog: UC-TINYTASK-2026 (warning)

### Architectural Nodes (Doc 14)

- total_nodes: 0 (the regex looks for `NODE-(TECHNOLOGY|...)-NNN` format; legacy may use a different schema)
- by_type: {} / by_track: {}
- with_source_uc: 1
- documents_found: 2
- has_sufficient_data: False
- Nodes reference UCs not found in Doc 13: UC-TINYTASK-2026 (warning)

### Requirements Allocation (Doc 15)

- total_allocations: 51
- unique_rules_allocated: 30
- unique_nodes_allocated: 0
- unique_uc_sources: 0
- by_verification: {} / by_allocation_type: {}
- documents_found: 2
- No use case source references found (warning — legacy carries UC references in different syntax)

### Compliance Gates (Doc 16)

- total_gates: 41
- with_node_ref: 0
- with_uc_ref: 0
- with_evidence: 3
- documents_found: 2
- No target node references found (warning); no source UC references found (warning)

### Functional Tree (Doc 17)

- total_nodes_in_tree: 0
- levels_found: {L1: 34, L2: 38, L3: 49, ROOT: 9}
- mermaid_diagrams: 1
- subdomains_covered: 10
- uc_sources: 0
- track_tags: 0
- documents_found: 2
- has_sufficient_data: False
- No node ID references / track tags (warning)

---

## §4 Observations carried forward

- **Total allocations / gates exist in legacy** (51 / 41) but lack UC source references and node IDs — likely a legacy schema divergence. Fase de Especificação 1 reconciliation must address.
- **29 orphan UCs** in legacy Doc 13 — relationships table appears to live in Doc 13a but the Doc 13 content does not cross-reference. Fase de Especificação 1 must add cross-doc consistency check.
- **`UC-TINYTASK-2026`** appears in 13a/13b/14 as a placeholder convention not present in legacy Doc 13. Fase de Especificação 1 must either port it to Doc 13 or document why it is excluded.
- **`documents_found: 2`** in every legacy lint = the rglob is matching both the Catalog and the Review Report under the legacy folder. The new RICH runner (with explicit `doc_path`) reports `documents_found: 1`, confirming the F-00f mitigation works.

---

## §5 Fase de Especificação 0 → Fase de Especificação 1 acceptance

| # | Criterion | Status |
|---|-----------|--------|
| 1 | Legacy Phase 3 lints run cleanly (baseline) | PASS (7/7 PASSED, 11 warnings) |
| 2 | Lint output captured to JSON + MD + console log | PASS |
| 3 | Fase de Especificação 0 skeleton does not modify legacy | PASS (verified by separate `git diff` — see SPRINT0_REPORT.md) |
| 4 | Legacy data-quality observations recorded | PASS (§4 above; carried to Fase de Especificação 1) |

**Fase de Especificação 0 baseline verdict:** PASS — legacy Phase 3 lints pass; data-quality observations recorded for Fase de Especificação 1.

---

**End of Fase de Especificação 0 Baseline Lint Report**
