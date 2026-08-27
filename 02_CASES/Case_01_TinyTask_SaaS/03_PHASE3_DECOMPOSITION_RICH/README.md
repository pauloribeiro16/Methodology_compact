---
document_id: AEGIS-P3-RICH-README
title: README — Phase 3 Rich Mode (Case_01)
phase: 3
version: 0.5
created: 2026-08-24
updated: 2026-08-24
author: Fase de Especificação 4 Executor (paulo@methodology.pt)
status: ADJUSTED_FIELDS
case: Case_01_TinyTask_SaaS
tier: MICRO
sibling_of: ../03_PHASE3_DECOMPOSITION/
branch: feature/aegis-p3-case01-rich
sibling_doc: ../03_PHASE3_DECOMPOSITION/
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Implementation Status, Priority, Stakeholders, Reporting]
---

# Phase 3 Rich Mode — Case_01 (TinyTask SaaS)

> Phase 3 Rich Mode — corpus-enriched sibling of legacy `03_PHASE3_DECOMPOSITION/`.
> Pattern: replicate the Phase 1 and Phase 2 Rich Mode successes, apply DEEP enrichment to all Phase 3 documents (13, 13a, 13b, 14, 15, 16, 17 + 23/24/25 + Synthesis + Annexes).
>
> **Fase de Especificação 4 status: ADJUSTED_FIELDS.** All 11 core docs + 2 review reports + synthesis + 2 annexes had 6 columns appended to their index tables. Fase de Especificação 5 will fill the per-card values.

---

## §1 Status Dashboard

| Sprint | Date | Theme | Status |
|--------|------|-------|:------:|
| **Fase de Especificação 0** | 2026-08-24 | Skeleton + lint baseline + 15 placeholders | PASS |
| **Fase de Especificação 1** | 2026-08-24 | Port legacy → Rich siblings + reconciliation | PASS_WITH_FINDINGS |
| **Fase de Especificação 2** | 2026-08-24 | Corpus linkage + NIST anchors + KG chains | PASS_WITH_FINDINGS |
| **Fase de Especificação 3** | 2026-08-24 | Final docs + traceability matrix + README + drawio | **PASS_WITH_FINDINGS** (this sprint) |
| Fase de Especificação 4 | TBD | Adjusted fields per row | ⏳ PENDING |
| Fase de Especificação 5 | TBD | DEEP enrichment (17 fields × N cards) | ⏳ PENDING |
| Validator | TBD | Fase de Especificação 5 self-verification | ⏳ PENDING |

---

## §2 Deliverables Map (Fase de Especificação 0 placeholders)

| Path | Sprint | Status | Lines |
|------|:------:|:------:|------:|
| `13_Use_Cases_Catalog.md` | 0 | SKELETON | ~10 |
| `13a_Use_Case_Relationships.md` | 0 | SKELETON | ~10 |
| `13b_Use_Case_Variability.md` | 0 | SKELETON | ~10 |
| `14_Architectural_Nodes.md` | 0 | SKELETON | ~10 |
| `15_Requirements_Allocation.md` | 0 | SKELETON | ~10 |
| `16_Compliance_Gates_Report.md` | 0 | SKELETON | ~10 |
| `17_Functional_Tree.md` | 0 | SKELETON | ~10 |
| `requirements/23_Functional_Requirements.md` | 0 | SKELETON | ~10 |
| `requirements/24_Non_Functional_Requirements.md` | 0 | SKELETON | ~10 |
| `requirements/23_FR_Review_Report.md` | 0 | SKELETON | ~10 |
| `requirements/24_NFR_Review_Report.md` | 0 | SKELETON | ~10 |
| `25_Risk_Analysis.md` | 0 | SKELETON | ~10 |
| `Phase_3_Functional_Decomposition_Synthesis.md` | 0 | SKELETON | ~10 |
| `annexes/A_Use_Case_Diagrams.md` | 0 | SKELETON | ~10 |
| `annexes/D_KG_Inference_Examples.md` | 0 | SKELETON | ~10 |
| `README.md` | 0 | SKELETON (this file) | this |
| `PROJECT_STATE.md` | 0 | SKELETON | ~200 |
| `RICH_VS_LEGACY.md` | 0 | SKELETON | ~50 |
| `scripts/build_traceability_matrix_rich.py` | 3 | stub | — |
| `scripts/verify_rich.py` | 5 | stub | — |
| `scripts/gen_drawio.py` | 3 | stub | — |
| `validation/LINT_REPORT_BEFORE.md` | 0 | captured | — |
| `validation/RICH_LINT_BASELINE.md` | 0 | drafted | — |
| `validation/SPRINT0_REPORT.md` | 0 | drafted | — |

All counts (use cases, nodes, allocations, gates, FR, NFR, risks) are **TBD** at Fase de Especificação 0.

---

## §3 Schema Reminder (12/2/3 Field Schema)

The Phase 3 Rich schema follows the 17-field pattern from Phase 2 Rich Mode:

- **12 base fields** (common to all tiers): Use Case ID / Description / Scope / Out-of-Scope / Source Article / NIST CSF Anchors / Verification Criteria / Verification Method / Owner / Status / Dependencies / Risk if not met / Affected Stakeholders — adapted per Phase 3 doc type.
- **2 context fields**: Track tag [T/P/P→T], Level marker (L0/L1/L2/LN).
- **3 Case_01-specific fields**: Regulatory Reporting / External Auditor / Supervisory Body.

`expected_card_columns: 17` in every placeholder frontmatter; `expected_compact_columns: 12` for Sprint-1 reconciliation tables.

---

## §3a Implementation Status

### Status ladder

Per `AGENTS.md` conventions, status escalates: `SKELETON → RECONCILED → CORPUS_ENRICHED → DEEP_ENRICHED`.

| Ladder step | Meaning | Sprint achieved |
|-------------|---------|:---------------:|
| **SKELETON** | Frontmatter + placeholder body | Fase de Especificação 0 |
| **RECONCILED** | Fase de Especificação 1 freeze references + reconciliation footer | Fase de Especificação 1 |
| **CORPUS_ENRICHED** | Real structured content + freeze cross-references | **Fase de Especificação 3 (current)** |
| **DEEP_ENRICHED** | 17-field schema per card (~3,995 cells) | Fase de Especificação 5 |

### Fase de Especificação 3 deliverables (NEW)

- `scripts/build_traceability_matrix_rich.py` — **REAL** implementation. Produces `22_Traceability_Matrix.xlsx` with **10 sheets**:
  1. COVER (29 rows)
  2. FULL_TRACEABILITY (31 rows)
  3. NFR_TO_FR (47 rows)
  4. FR_TO_UC (31 rows)
  5. UC_TO_REGULATION (36 rows)
  6. RULES_SATISFACTION (47 rows)
  7. GATES_STATUS (31 rows)
  8. COVERAGE_DASHBOARD (18 rows)
  9. **RULE_FREEZE** (NEW, 47 rows)
  10. **KG_CHAINS** (NEW, 13 rows)
  - Total: **330 rows** across all sheets.
- `22_Traceability_Matrix.xlsx` — generated (8 legacy sheets mirrored + 2 new).
- `scripts/gen_drawio.py` — **REAL** implementation. Parses Mermaid from `17_Functional_Tree.md` and emits `18_Functional_Tree.drawio` (42 vertices + 41 edges).
- `18_Functional_Tree.drawio` — generated (F-00e RESOLVED in Fase de Especificação 3).
- `scripts/verify_rich.py` — **light stub with `verify_xlsx()` real**. Full DEEP validation arrives in Fase de Especificação 5.
- 11 core docs — real content (~1.7k new markdown lines).
- Annexes A + D — light fill (Mermaid diagrams + 3 KG chains + 10 SPARQL examples).
- `validation/SPRINT3_REPORT.md` completion report.

### Status per artefact

| Artefact | Status | Sprint |
|----------|:------:|:------:|
| `13_Use_Cases_Catalog.md` | CORPUS_ENRICHED | 3 |
| `13a_Use_Case_Relationships.md` | CORPUS_ENRICHED | 3 |
| `13b_Use_Case_Variability.md` | CORPUS_ENRICHED | 3 |
| `14_Architectural_Nodes.md` | CORPUS_ENRICHED | 3 |
| `15_Requirements_Allocation.md` | CORPUS_ENRICHED | 3 |
| `16_Compliance_Gates_Report.md` | CORPUS_ENRICHED | 3 |
| `17_Functional_Tree.md` | CORPUS_ENRICHED (Mermaid added) | 3 |
| `requirements/23_Functional_Requirements.md` | CORPUS_ENRICHED | 3 |
| `requirements/24_Non_Functional_Requirements.md` | CORPUS_ENRICHED | 3 |
| `25_Risk_Analysis.md` | CORPUS_ENRICHED | 3 |
| `Phase_3_Functional_Decomposition_Synthesis.md` | CORPUS_ENRICHED | 3 |
| `annexes/A_Use_Case_Diagrams.md` | CORPUS_ENRICHED (Mermaid) | 3 |
| `annexes/D_KG_Inference_Examples.md` | CORPUS_ENRICHED (KG chains + SPARQL) | 3 |
| `22_Traceability_Matrix.xlsx` | GENERATED | 3 |
| `18_Functional_Tree.drawio` | GENERATED | 3 |
| `RULE_FREEZE.md` | FROZEN | 1 |
| `CORPUS_LINKAGE.md` | ACTIVE | 2 |
| `NIST_ANCHORS.md` | ACTIVE | 2 |
| `KG_CHAINS.md` | ACTIVE | 2 |

---

## §4 Sprint Plan

### Fase de Especificação 0 — Skeleton ✅
- 15 placeholders + 3 orchestration docs + 3 script stubs + 5 lint ports + 1 new runner
- Legacy lint baseline captured; new RICH runner baseline produced

### Fase de Especificação 1 — Reconciliation ✅
- Port legacy `13/13a/13b/14/15/16/17/23/24/25/Synthesis + 4 annexes` → Rich siblings
- Verify cross-document invariants (UC ↔ Node ↔ Allocation ↔ Gate ↔ FR/NFR ↔ Risk ↔ Synthesis)
- Produce `SPRINT1_REPORT.md` (PASS_WITH_FINDINGS; F-00a/b/c/d RESOLVED)

### Fase de Especificação 2 — Corpus linkage + NIST anchors + KG chains ✅
- `CORPUS_LINKAGE.md` (344 artefacts → D-XX.Y mapping)
- `NIST_ANCHORS.md` (46 rules + 31 goals anchored)
- `KG_CHAINS.md` (12 inference chains; 11/12 spot-checks PASS)
- Produce `SPRINT2_REPORT.md` (PASS_WITH_FINDINGS)

### Fase de Especificação 3 — Final docs + traceability matrix ✅ (this sprint)
- README v0.4, RICH_VS_LEGACY.md updated, `22_Traceability_Matrix.xlsx` (10 sheets, 330 rows)
- Implement `build_traceability_matrix_rich.py` (619 lines, REAL) and `gen_drawio.py` (155 lines, REAL)
- 11 core docs + 2 annexes with real content (~1.9k markdown lines)
- `18_Functional_Tree.drawio` generated (F-00e RESOLVED)
- Produce `SPRINT3_REPORT.md` (PASS_WITH_FINDINGS)

### Fase de Especificação 4 — Adjusted fields per row ⏳
- Add 6 new columns to existing tables

### Fase de Especificação 5 — DEEP enrichment ⏳
- 17 fields × N cards
- Frontmatter `status: DEEP_ENRICHED`, `version: 2.0`
- Implement `verify_rich.py`

### Validator — Self-verification ⏳
- Fase de Especificação 5 self-verification (acceptance criteria)

---

## §5 Invariants (to be respected by every sprint)

- ✅ Legacy `03_PHASE3_DECOMPOSITION/` **never modified**
- ✅ No corpus files modified (`00_METHODOLOGY/PREPROCESSING_by_domain/`)
- ✅ No Phase 1, Phase 2 docs modified
- ✅ Card counts and cell counts exclude Effort/Cost/Timeline
- ✅ Document IDs: `AEGIS-P3-RICH-*` (parallel to legacy `ARM-P3-*`)
- ✅ Frontmatter status escalates `SKELETON → RECONCILED → CORPUS_ENRICHED → DEEP_ENRICHED`
- ✅ No git commits by sprint executors (orchestrator owns commits)
- ✅ Legacy data inconsistencies are reported, not silently fixed (the F-00x findings)

---

## §6 See Also

- `PROJECT_STATE.md` — Phase 3 Rich project snapshot
- `RICH_VS_LEGACY.md` — Rich vs legacy diff summary
- `validation/SPRINT0_REPORT.md` completion
- `validation/LINT_REPORT_BEFORE.md` — legacy Phase 3 baseline
- `validation/RICH_LINT_BASELINE.md` — RICH runner baseline (post-port)
- `../03_PHASE3_DECOMPOSITION/` — legacy Phase 3 (read-only)

---

**End of README skeleton (Phase 3 Rich Mode SKELETON)**
