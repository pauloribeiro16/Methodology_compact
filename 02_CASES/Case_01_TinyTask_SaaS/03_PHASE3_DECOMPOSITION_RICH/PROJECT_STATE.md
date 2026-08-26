---
document_id: AEGIS-P3-RICH-STATE
title: Project State — Phase 3 Rich Mode (Case_01)
phase: 3
version: 3.0
created: 2026-08-24
updated: 2026-08-26
author: Sprint 6 Executor (paulo@methodology.pt)
status: REWRITTEN_PRODUCT_BASELINE
case: Case_01_TinyTask_SaaS
tier: MICRO
sibling_of: ../03_PHASE3_DECOMPOSITION/
branch: feature/aegis-p3-case01-rich
sprint: 6
sprint_role: product_baseline_rewrite
sprints_complete: [0, 1, 2, 3, 4, 5, 6]
sprints_pending: []
sprint_in_progress: 6
verdict: PASS_WITH_FINDINGS
sprint6_validator_report: validation/VALIDATOR_SPRINT6.md
sprint6_resolved_findings: [F-S5-02]
sprint6_open_findings: [F-NEW-S6-01 — KG E4 rebuild logged as follow-up]
applicable_regs: [GDPR, CRA]
active_subdomains: 30
freeze_total_rules: 46        # 30 CR + 16 BPR per P2-RICH Doc 11
freeze_total_objectives: 31   # 11 PO + 20 SO per P2-RICH Doc 10
freeze_total_use_cases_l1: 35        # security/compliance U.C.1-6 — preserved
freeze_total_use_cases_functional: 23  # functional U.C.7-11 — Sprint 6 NEW
freeze_total_use_cases_total: 58     # 35 + 23
freeze_total_misuse_cases: 8         # MUC-01..08 — Sprint 6 NEW
freeze_total_use_cases_references: 62  # 35 L1 + 27 L2 expansions (Doc 16 §5B SC2) — unchanged
freeze_total_functional_requirements: 30
freeze_total_non_functional_requirements: 46
freeze_total_risks: 10
freeze_total_threats: 38
freeze_total_nodes: 49
freeze_total_allocations: 30
freeze_total_gates: 30
freeze_total_relationships: 91       # 16 «include» + 8 «extend» + 35 «constrains» + 8 «threatens» + 24 «mitigated by»
freeze_total_constrains_edges: 35
freeze_total_threats_edges: 8
freeze_total_mitigated_by_edges: 24
freeze_total_variants: 26            # V-01..V-18 (security) + V-19..V-26 (functional)
total_detail_cards: 276        # Sprint 5 baseline (35 UC + 49 NODE + 30 DN + 30 GATE + 30 FR + 46 NFR + 48 RISK+THR + 8 SYNTH)
total_cells_sprint5: 3917
fields_per_card_sprint5: 17|12|tiered
schema_columns_sprint6: 7
schema_columns_list: [Primary Actor, Stakeholders, Preconditions, Trigger, Main Success Scenario, Extensions, Postconditions]
annex_schema_columns: 7
annex_schema_columns_list: [Owner, Verification Criteria, NIST Anchors, Dependencies, Risk, Reporting, Maturity]
xlsx_sheets_sprint6: 12
xlsx_total_rows_sprint6: ~480
drawio_vertices_sprint6: 79
drawio_edges_sprint6: 77
# Sprint 6 REWRITTEN_PRODUCT_BASELINE — catalogue reorganised
sprint6_changes:
  - "Doc20 v3.0: 35 U.C.1-6 preserved verbatim; +23 U.C.7-11 functional; +8 MUCs"
  - "Doc21 v1.0: 24 legacy edges preserved; +67 new edges (constrains/threatens/mitigated_by/functional include)"
  - "Doc22 v1.0: V-01..V-18 preserved; +V-19..V-26 functional variants"
  - "RULE_FREEZE v2.0: §5 extended with functional U.C. + MUC freeze"
  - "22_Traceability_Matrix.xlsx: 12 sheets (was 10); +FUNCUC_TO_SECUC +MUC_TO_MITIGATION"
  - "Doc26 v2.0: product-root tree; 79 nodes / 77 edges in drawio (was 42 / 41)"
  - "F-S5-02 RESOLVED (actors catalogue + Primary Actor field)"
  - "F-NEW-S6-01 OPEN — KG E4 incremental rebuild on Deucalion (~14h), human approval required (P7)"
sprint6_per_doc:
  - {file: "Doc20_Use_Cases_Catalog.md", status: "REWRITTEN_PRODUCT_BASELINE", cards: 58, mucs: 8}
  - {file: "Doc21_Use_Case_Relationships.md", status: "EXTENDED_PRODUCT_BASELINE", edges: 91}
  - {file: "Doc22_Use_Case_Variability.md", status: "EXTENDED_PRODUCT_BASELINE", variants: 26}
  - {file: "Doc26_Functional_Tree.md", status: "PRODUCT_ROOT_REWRITE", nodes: 79, edges: 77}
  - {file: "RULE_FREEZE.md", status: "FROZEN_WITH_PRODUCT_BASELINE", version: "2.0"}
  - {file: "22_Traceability_Matrix.xlsx", status: "REGENERATED", sheets: 12}
  - {file: "validation/VALIDATOR_SPRINT6.md", status: "PASS_WITH_FINDINGS", verdict: "PASS"}
sprint5_per_doc:
  - {file: "13_Use_Cases_Catalog.md (renamed Doc20)", cards: 35, cells: 475}
  - {file: "14_Architectural_Nodes.md (renamed Doc23)", cards: 49, cells: 648}
  - {file: "15_Requirements_Allocation.md (renamed Doc24)", cards: 30, cells: 455}
  - {file: "16_Compliance_Gates_Report.md (renamed Doc25)", cards: 30, cells: 445}
  - {file: "Phase_3_Functional_Decomposition_Synthesis.md", cards: 8, cells: 96}
  - {file: "requirements/Doc29_Functional_Requirements.md", cards: 30, cells: 480}
  - {file: "requirements/Doc31_Non_Functional_Requirements.md", cards: 46, cells: 692}
  - {file: "Doc27_Risk_Analysis.md", cards: 48, cells: 626}
related_deliverables:
  - RULE_FREEZE.md (v2.0)
  - CORPUS_LINKAGE.md
  - NIST_ANCHORS.md
  - KG_CHAINS.md
  - 22_Traceability_Matrix.xlsx (Sprint 6 — 12 sheets)
  - 18_Functional_Tree.drawio (Sprint 6 — 79 nodes / 77 edges)
  - validation/SPRINT1_REPORT.md
  - validation/SPRINT5_REPORT.md
  - validation/VALIDATOR_SPRINT6.md
  - validation/SPRINT2_REPORT.md
  - validation/SPRINT3_REPORT.md
  - validation/SPRINT4_REPORT.md
  - validation/SPRINT5_REPORT.md (NEW Sprint 5 — DEEP enrichment completion)
  - validation/RICH_LINT_DEEP.md (NEW Sprint 5 — rich lint post-enrichment)
  - RICH_VS_LEGACY.md (appended §A/§B/§C/§D/§E/§F/§G)
sibling_doc: ../03_PHASE3_DECOMPOSITION/
---

# Project State — Phase 3 Rich Mode (Case 01)

> Case_01_TinyTask_SaaS — Phase 3 Rich Mode (corpus-enriched sibling of legacy `03_PHASE3_DECOMPOSITION/`).
> **Purpose:** single-page snapshot of where Case_01 Phase 3 Rich stands across the 7 sprints. Used by the orchestrator to decide PR readiness, by reviewers to assess scope, and by future sprints to plan dependencies.

---

## §1 Status

| Phase | Legacy | Rich `03_PHASE3_DECOMPOSITION_RICH/` |
|-------|--------|---------------------------------------|
| Phase 1 (Context) | COMPLETE (frozen 2026-04-01) | COMPLETE (Rich sibling 2026-08-06) |
| Phase 2 (Obligations) | COMPLETE (30 obligations + 4 Sprint 6+ = 34, 4 tensions, 46 rules) | COMPLETE (Rich DEEP_ENRICHED 2026-08-07) |
| Phase 3 (Architecture & Rules) | COMPLETE (35 use cases, 30 FRs, 46 NFRs) | **DEEP_ENRICHED** (Sprint 5: 276 detail cards, 3,917 cells) |
| **Aggregate** | Phase 1+2+3 COMPLETE | Phase 3 Rich Mode: **DEEP_ENRICHED** (5 of 7 sprints complete; Validator next) |

**Branch:** `feature/aegis-p3-case01-rich`
**Base:** `main`
**Working tree:** 20 files modified/added under `03_PHASE3_DECOMPOSITION_RICH/` (3 new docs + 10 placeholder frontmatter updates + 7 untouched); Sprint 4 adds 6-column schema to ~45 tables
**Lint status:** Sprint 0 baseline captured; RICH runner registered clean
**Sprint 0 verdict:** PASS (skeleton layer complete)
**Sprint 1 verdict:** PASS_WITH_FINDINGS (reconciliation freeze — see RULE_FREEZE.md)
**Sprint 2 verdict:** PASS_WITH_FINDINGS (corpus linkage + NIST anchors + KG chains — see SPRINT2_REPORT.md)
**Sprint 3 verdict:** PASS_WITH_FINDINGS (final docs + traceability matrix — see SPRINT3_REPORT.md)
**Sprint 4 verdict:** PASS (schema adjustment — see SPRINT4_REPORT.md)
**Sprint 5 verdict:** PASS_WITH_FINDINGS (DEEP enrichment — see SPRINT5_REPORT.md)
**Phase 3 Rich Mode status:** **DEEP_ENRICHED** (5 of 7 sprints complete; Validator next)

---

## §2 Deliverables

| Path | Status | Sprint | Lines | Description |
|------|:------:|:------:|------:|-------------|
| `README.md` | SKELETON | 0 | ~120 | Orientation, dashboard, schema reminder (Sprint 3 → v1.0) |
| `PROJECT_STATE.md` | RECONCILED | 1 | this file | Project state snapshot — Sprint 1 freeze values |
| `RICH_VS_LEGACY.md` | APPENDED | 1 | ~50 → ~150 | Diff summary (Sprint 1 §A/§B/§C appended) |
| `RULE_FREEZE.md` | FROZEN | 1 | ~430 | Canonical rule + goal + enumeration tables |
| `13_Use_Cases_Catalog.md` | **DEEP_ENRICHED** | 5 | ~954 | 35 UC cards (475 cells) — Sprint 5 deep-fill complete |
| `13a_Use_Case_Relationships.md` | ADJUSTED_FIELDS | 2 | ~10 | Placeholder — Sprint 3 deep |
| `13b_Use_Case_Variability.md` | ADJUSTED_FIELDS | 2 | ~10 | Placeholder — Sprint 3 deep |
| `14_Architectural_Nodes.md` | **DEEP_ENRICHED** | 5 | ~1187 | 49 NODE cards (648 cells) — Sprint 5 deep-fill complete |
| `15_Requirements_Allocation.md` | **DEEP_ENRICHED** | 5 | ~816 | 30 DN cards (455 cells) — Sprint 5 deep-fill complete |
| `16_Compliance_Gates_Report.md` | **DEEP_ENRICHED** | 5 | ~823 | 30 GATE cards (445 cells) — Sprint 5 deep-fill complete |
| `17_Functional_Tree.md` | ADJUSTED_FIELDS | 2 | ~10 | Placeholder — Sprint 3 deep |
| `requirements/23_Functional_Requirements.md` | **DEEP_ENRICHED** | 5 | ~941 | 30 FR cards (480 cells) — Sprint 5 deep-fill complete |
| `requirements/24_Non_Functional_Requirements.md` | **DEEP_ENRICHED** | 5 | ~1381 | 46 NFR cards (692 cells) — Sprint 5 deep-fill complete |
| `requirements/23_FR_Review_Report.md` | ADJUSTED_FIELDS + LEGACY PORTED | 1 | ~370 | Legacy 309 lines verbatim + reconciliation footer; schema in frontmatter |
| `requirements/24_NFR_Review_Report.md` | ADJUSTED_FIELDS + LEGACY PORTED | 1 | ~340 | Legacy 286 lines verbatim + reconciliation footer; schema in frontmatter |
| `25_Risk_Analysis.md` | **DEEP_ENRICHED** | 5 | ~1127 | 48 RISK+THR cards (626 cells) — Sprint 5 deep-fill complete |
| `Phase_3_Functional_Decomposition_Synthesis.md` | **DEEP_ENRICHED** | 5 | ~362 | 8 SYNTH highlight cards (96 cells) — Sprint 5 deep-fill complete |
| `annexes/A_Use_Case_Diagrams.md` | ADJUSTED_FIELDS | 1 | ~10 | Placeholder — Sprint 3 deep |
| `annexes/D_KG_Inference_Examples.md` | ADJUSTED_FIELDS | 1 | ~10 | Placeholder — Sprint 2/3 deep |
| `CORPUS_LINKAGE.md` | NEW | 2 | ~490 | Artefact-to-D-XX.Y mapping (344 artefacts) |
| `NIST_ANCHORS.md` | NEW | 2 | ~290 | NIST CSF 2.0 + PF 1.0 anchors (46+31 rules/goals + 111 card slots) |
| `KG_CHAINS.md` | NEW | 2 | ~245 | 12 KG inference chains with spot-checks |
| `22_Traceability_Matrix.xlsx` | NOT STARTED | 3 | — | Sprint 3 deliverable |
| `scripts/build_traceability_matrix_rich.py` | stub | 3 | — | Placeholder |
| `scripts/verify_rich.py` | stub | 5 | — | Placeholder |
| `scripts/gen_drawio.py` | stub | 3 | — | Placeholder |
| `validation/LINT_REPORT_BEFORE.md` | captured | 0 | — | Legacy Phase 3 baseline |
| `validation/RICH_LINT_BASELINE.md` | drafted | 0 | — | RICH runner baseline |
| `validation/SPRINT0_REPORT.md` | drafted | 0 | — | Sprint 0 completion |
| `validation/SPRINT1_REPORT.md` | NEW | 1 | ~280 | Sprint 1 reconciliation report |
| `validation/SPRINT2_REPORT.md` | NEW | 2 | ~220 | Sprint 2 corpus enrichment report |

**Status legend:** SKELETON = placeholder only | RECONCILED = Sprint 1 reconciliation done (frontmatter + freeze references) | CORPUS_ENRICHED = Sprint 2 corpus linkage + NIST anchors applied | FROZEN = canonical | APPENDED = existing doc with new sections | stub = NotImplementedError | captured/drafted = validation artefact present | NOT STARTED = future sprint.

---

## §3 Sprint Dashboard

| Sprint | Theme | Output | Status |
|--------|-------|--------|:------:|
| Sprint 0 | Skeleton + lint baseline | 15 placeholders + 3 orch docs + 3 stubs + 5 lint ports + 1 runner + 2 reports | PASS |
| Sprint 1 | Reconciliation (port + freeze) | RULE_FREEZE.md + 15 RECONCILED placeholders + 2 legacy review ports + SPRINT1_REPORT.md | PASS_WITH_FINDINGS |
| Sprint 2 | Corpus linkage + NIST anchors + KG chains | CORPUS_LINKAGE.md + NIST_ANCHORS.md + KG_CHAINS.md + 10 placeholders → CORPUS_ENRICHED | PASS_WITH_FINDINGS |
| Sprint 3 | Final docs + Excel + README v1.0 + RICH_VS_LEGACY | 22_Traceability_Matrix.xlsx (10 sheets, 330 rows) + 18_Functional_Tree.drawio (42 v, 41 e) | PASS_WITH_FINDINGS |
| Sprint 4 | Adjusted fields per row | +6 columns to ~45 index tables; 13 docs → ADJUSTED_FIELDS | **PASS** |
| Sprint 5 | DEEP enrichment | 17\|12 fields × 276 cards = 3,917 cells across 8 docs | **PASS_WITH_FINDINGS** (this sprint) |
| Validator | Self-verification | Acceptance criteria verdict | ⏳ |

**Sprint 0 verdict:** PASS — skeleton layer complete.
**Sprint 1 verdict:** PASS_WITH_FINDINGS — see `validation/SPRINT1_REPORT.md` and `RULE_FREEZE.md`.
**Sprint 2 verdict:** PASS_WITH_FINDINGS — see `validation/SPRINT2_REPORT.md`, `CORPUS_LINKAGE.md`, `NIST_ANCHORS.md`, `KG_CHAINS.md`.
**Sprint 3 verdict:** PASS_WITH_FINDINGS — see `validation/SPRINT3_REPORT.md`.
**Sprint 4 verdict:** PASS — see `validation/SPRINT4_REPORT.md`.
**Sprint 5 verdict:** PASS_WITH_FINDINGS — see `validation/SPRINT5_REPORT.md` + `validation/RICH_LINT_DEEP.md`.
**Aggregate metric:** 5 of 7 sprints complete (Sprint 5 is the heaviest enrichment sprint).

---

## §3a Schema adjustment (Sprint 4)

**Sprint 4 deliverable:** 6 columns added to ~95% (effectively 100% of in-scope) index tables in 11 core docs + synthesis + 2 annexes; FR/NFR review reports carry the schema in frontmatter only (legacy-port preserved). Total tables extended: **~45** across the folder.

The 6 added columns are:

| Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|-------|-----------------------|----------|----------|--------------|-----------|

Frontmatter `schema_columns: 6` + `schema_columns_list` declared in 15 docs. No row values filled yet — Sprint 5 populates per-card.

Coverage stats (see `validation/SPRINT4_REPORT.md` §2-§3 for full breakdown):

| Doc | Tables extended |
|-----|----------------:|
| `13_Use_Cases_Catalog.md` | 9 |
| `13a_Use_Case_Relationships.md` | 2 |
| `13b_Use_Case_Variability.md` | 1 |
| `14_Architectural_Nodes.md` | 4 |
| `15_Requirements_Allocation.md` | 2 |
| `16_Compliance_Gates_Report.md` | 3 |
| `17_Functional_Tree.md` | 1 |
| `requirements/23_Functional_Requirements.md` | 8 |
| `requirements/24_Non_Functional_Requirements.md` | 8 |
| `25_Risk_Analysis.md` | 2 |
| `Phase_3_Functional_Decomposition_Synthesis.md` | 3 |
| `annexes/A_Use_Case_Diagrams.md` | 0 (schema addendum §A.5) |
| `annexes/D_KG_Inference_Examples.md` | 0 (schema addendum §E) |
| **TOTAL** | **~43 + 2 schema-addendum tables** |

---

## §4 Card counts (Sprint 1 freeze values; Sprint 5 detail-cards to be filled per-doc)

| Artefact | Sprint 1 freeze | Source |
|----------|----------------:|--------|
| **Rules (P2-RICH Doc 11)** | **46** | 30 CR + 16 BPR |
| **Objectives (P2-RICH Doc 10)** | **31** | 11 PO + 20 SO (F-04a/b applied) |
| Use cases L1 cards (Doc 13) | **35** | Doc 13 §3.3 + Doc 16 §5B SC2 |
| Use case references (L1+L2) | 62 | Doc 16 §5B SC2 |
| Packages (Doc 13) | 6 | PKG-DP/SEC/IAM/DEV/GOV/TRN |
| Architectural nodes (Doc 14) | 49 | Doc 14 §8 |
| Requirement allocations (Doc 15) | 30 DN | Doc 15 §4 (1:1 with CR) |
| Compliance gates (Doc 16) | 30 GATE | Doc 16 §5 (1:1 with CR) |
| Functional requirements (Doc 23) | **30** | FR-01..FR-30 (F-00b RESOLVED) |
| Non-functional requirements (Doc 24) | **46** | NFR-01..NFR-46 (F-00b RESOLVED) |
| Risks (Doc 25) | 10 | (verify in Sprint 5) |
| Threats (Doc 25) | 38 | (verify in Sprint 5) |
| **Detail cards (Sprint 5 target)** | **~235** | sum: 30 FR + 46 NFR + 10 R + 38 T + 62 UC + 49 nodes |
| **Total cells (Sprint 5)** | **~3,995** | 17 fields × 235 cards (formula; verify in S5) |

> **Sprint 5 cells formula:** `17 × N_cards`. Sprint 5 will pre-fill exact card counts once per-doc enumeration is complete. The freeze values above are authoritative for Phase 3 planning; downstream counts in the `22_Traceability_Matrix.xlsx` workbook (Sprint 3) will mirror these numbers.

---

## §4b DEEP enrichment (Sprint 5 actual)

> Sprint 5 populated **276 detail cards** (= 35 UC + 49 NODE + 30 DN + 30 GATE + 30 FR + 46 NFR + 48 RISK+THR + 8 SYNTH) across 8 detail-rich docs, totalling **3,917 cells** via formula `17 × N_CH + 12 × N_ML` where N_CH=121 (CRITICAL/HIGH 17-field cards) and N_ML=155 (MEDIUM/LOW 12-field cards).

| Artefact family | Cards | 17-field (CH) | 12-field (ML) | Cells |
|-----------------|------:|--------------:|--------------:|------:|
| UC (Doc 13) | 35 | 11 | 24 | 475 |
| NODE (Doc 14) | 49 | 12 | 37 | 648 |
| DN (Doc 15) | 30 | 19 | 11 | 455 |
| GATE (Doc 16) | 30 | 17 | 13 | 445 |
| SYNTH highlights | 8 | 0 | 8 | 96 |
| FR (Doc 23) | 30 | 24 | 6 | 480 |
| NFR (Doc 24) | 46 | 28 | 18 | 692 |
| RISK + THR (Doc 25) | 48 | 10 | 38 | 626 |
| **TOTAL** | **276** | **121** | **155** | **3,917** |

**Completion:** 5 of 7 sprints complete (Sprint 5 = 71%). Sprint 5 = heaviest sprint per plan; Sprint 6 = Validator self-verification.

**F-register delta:**
- F-00e **RESOLVED** (uniform 17/12-field schema verified across 276 cards)
- F-S1-01..07 INFORMATIVELY RESOLVED via Doc 14/16 cards (orphan-ref mappings in card Source fields)
- F-S2-02/03 RESOLVED (FR-16/FR-23 remap)
- F-S5-01/02 NEW (lint naming gap + Actor/Regulation regex mismatch)

---

## §4a Corpus / NIST / KG state (Sprint 2 freeze)

| Metric | Value | Source |
|--------|------:|--------|
| Artefacts linked to D-XX.Y | **344/344 (100%)** | CORPUS_LINKAGE.md §1-§9 |
| D-XX.Y subdomains covered | 24 / 38 (63%) — empty cells have no artefact by design | CORPUS_LINKAGE.md §10 |
| Rules anchored to NIST CSF 2.0 | **46/46 (100%)** | NIST_ANCHORS.md §1 |
| Rules anchored to NIST PF 1.0 | 27/46 (59%) — technical BPRs (RBAC, FIDO2, CA-2) omit PF per Doc 11 | NIST_ANCHORS.md §1 |
| Goals anchored to NIST CSF 2.0 | 27/31 (87%) — 4 SOs intentionally blank per Doc 10b §4 | NIST_ANCHORS.md §2 |
| Goals anchored to NIST PF 1.0 | 27/31 (87%) | NIST_ANCHORS.md §2 |
| Per-artefact card slot rows | 35 UC + 27 FR + 46 NFR = **108** | NIST_ANCHORS.md §3 |
| KG chains documented | **12** | KG_CHAINS.md §1 |
| KG edges (EXTRACTED / INFERRED) | **15 / 3** | KG_CHAINS.md §1 |
| KG spot-checks (PASS / FAIL) | **11 / 1** (1 fuzzy-fail replaced) | KG_CHAINS.md §5 |
| KG contamination nodes (F-S1-09) | 14 (REPORT, deferred to Sprint 5 re-run in isolation) | RULE_FREEZE.md §4 |

---

## §5 Branch

- **Branch:** `feature/aegis-p3-case01-rich`
- **Base:** `main`
- **Status:** Sprint 4 complete (ADJUSTED_FIELDS); Sprint 5 next
- **Working tree:** untracked new files in `03_PHASE3_DECOMPOSITION_RICH/`; Sprint 4 schema applied to ~45 tables
- **Pre-push hook:** lints run locally via `.hooks/pre-push-evals`
- **Branch workflow:** see `docs/BRANCH_WORKFLOW.md` and root `AGENTS.md`
- **Commits:** none created by Sprint 4 Executor (orchestrator owns commits)

---

## §6 Constraints Respected

| Constraint | Status |
|------------|--------|
| Don't modify legacy `03_PHASE3_DECOMPOSITION/` | PASS (verified: git diff empty) |
| Don't modify Phase 1 or Phase 2 docs | PASS |
| Don't modify any corpus files | PASS (no PREPROCESSING changes) |
| Match project YAML frontmatter conventions | PASS (AEGIS-P3-RICH-* IDs) |
| No git commits by executors | PASS |
| 17 fields per detail card (planned) | PASS — schema reminder in README §3 |
| Document IDs: `AEGIS-P3-RICH-*` | PASS — 15 placeholders + 3 orch docs |
| Frontmatter status: `ADJUSTED_FIELDS` | PASS — all 13 docs updated (Sprint 4) |

---

## §7 Open Findings (F-register at Sprint 2)

| ID | Severity | Description | Status |
|----|----------|-------------|:------:|
| F-00a | INFO | Legacy `13_Use_Cases_Catalog.md` carries `U.C.X.Y.Z` MaaS format (not flat UC-XX). Sprint 5 preserves the MaaS format. | **RESOLVED** |
| F-00b | INFO | Legacy counts (35 UCs / 30 FRs / 46 NFRs vs 62 / 60 / 45 stale summaries). | **RESOLVED** |
| F-00c | INFO | Sprint 1 needs to surface any node IDs that don't trace back to UC source (orphan check). | **RESOLVED** (1 KG-level orphan reported F-S1-09) |
| F-00d | INFO | Sprint 1 needs to verify all gate IDs in `16_Compliance_Gates_Report.md` have status; legacy may carry TBDs. | **RESOLVED** (SC1 stale 38-rule claim resolved → 46 freeze) |
| F-00e | INFO | Sprint 5 must ensure all FR/NFR/Risk cards uniformly use the 17-field schema. | **RESOLVED** (Sprint 5: 276 cards uniform 17/12-field) |
| F-00f | INFO | Sprint 0 must NOT silently merge legacy + Rich via the runner; `--rich` flag and `doc_path` param. | **CLOSED** (Sprint 0) |
| F-S1-01..07 | MEDIUM/LOW | 7 orphan CR-D refs in legacy Phase 3 (D-02.4/06.4/07.3/07.4/08.3/09.3/10.1). | INFORMATIVELY RESOLVED (Sprint 5: Doc 14/16 cards carry explicit Source mapping; P7 formal close still required) |
| F-S1-08 | LOW | Doc 08 has 34 OBLs post-Sprint 6+ fix; Doc 11 has 30 CR; the 4 added OBLs lack matching CR entries. CARRIED from Phase 2 F-07/F-08/F-09. | CARRIED (follow-on contract) |
| F-S1-09 | INFO | 14 Case_02 contamination nodes in Graphify KG (AI Act, Biometric, Border Control AI, IPSARA, FRIA). NOT in markdown source. | OPEN (Sprint 5 KG re-run in isolation) |
| F-S1-10 | INFO | Doc 11 §8 "StrategicTension Resolution: 3" cosmetic. Carried from Phase 2 F-08. | CLOSED |
| F-S1-11 | INFO | Doc 16 SC3 "8 complex UCs refined to L2" — confirmed against §5B. No drift. | CLOSED |
| **F-S2-01** | INFO | KG node `fr_29_universal_notification` label mismatch (Doc 23 §3 FR-29 is Training, not Notification). Labelling artefact. NOTE in KG_CHAINS.md CH-09. | NOTED |
| **F-S2-02** | LOW | Doc 23 §3 maps FR-16 (regulatory notification) → CR-D-01.1-001; semantically belongs to CR-D-04.3-001. Legacy drift. Sprint 5 should re-map. | **RESOLVED** (Sprint 5: FR-16 card Source updated) |
| **F-S2-03** | LOW | Doc 23 §3 maps FR-23 (SBOM) → CR-D-02.1-001; semantically belongs to CR-D-06.2-001. Legacy drift. Sprint 5 should re-map. | **RESOLVED** (Sprint 5: FR-23 card Source updated) |
| **F-S5-01** | LOW | Lint 13 expects legacy `## 5.` / `## 6.` section headers; Rich docs use `## §N`. Cannot fix without modifying lint contract. | OPEN (Sprint 5 NEW) |
| **F-S5-02** | LOW | Lint 13 reports "0 actors defined" + "N orphan UCs"; regex `Actors?:` does not match our `**Owner:**` field. By design (Owner is field 8 in UC 17-field schema). | OPEN (Sprint 5 NEW) |
| **F-S2-04** | LOW | KG edge source_location format uses row numbers; spot-check fuzzy-fails when not verbatim. Replace with §-anchored semantic locators. | OPEN (Sprint 5) |

Full details in `RULE_FREEZE.md §9` + `validation/SPRINT2_REPORT.md §5`. Findings are **non-silent**: each is reported in the sprint that observes it and tracked here. None blocks Sprint 3.

---

## §8 Sprint 4 → Sprint 5 Handoff

**Sprint 4 (DONE, PASS):**
- 6 columns appended to ~45 index tables across 11 core docs + synthesis + 2 annexes (annexes carry §A.5/§E schema-addendum tables).
- Frontmatter `status: CORPUS_ENRICHED` → `ADJUSTED_FIELDS` for 13 docs (11 + synthesis + 2 annexes); FR/NFR review reports `RECONCILED` → `ADJUSTED_FIELDS` (frontmatter only, legacy-port preserved).
- `schema_columns: 6` + `schema_columns_list` declared in all 15 docs.
- `RICH_VS_LEGACY.md` §F appended.
- Legacy `03_PHASE3_DECOMPOSITION/` and `02_PHASE2_RULES/` untouched.

**For Sprint 5 (DEEP enrichment) — Executor/Validator:**
- Populate the 6 new columns per row in every index table (~43 tables × average ~6 rows of empty cells).
- For each of ~235 detail cards (30 FR + 46 NFR + 10 R + 38 T + 62 UC + 49 nodes), expand to the 17-field schema (per `expected_card_columns: 17`).
- Implement `scripts/verify_rich.py` end-to-end.
- Resolve F-S1-01..F-S1-07 orphan refs in Doc 14/15/16 ports.
- Re-run Graphify on Case_01 in isolation (Case_02 ontology disabled) to remediate F-S1-09 contamination. **CARRIED from Sprint 1 → Sprint 5.**
- Re-map FR-16/FR-23 in Doc 23 §3 (F-S2-02/F-S2-03).
- Run Validator sub-agent → `validation/VALIDATOR_SPRINT5.md`.
- Surface F-00e (uniform 17-field schema verification) as RESOLVED.

---

## §9 Cross-references

- `README.md` — orientation + status dashboard + schema reminder
- `RICH_VS_LEGACY.md` — Rich vs legacy diff summary
- `validation/SPRINT0_REPORT.md` — Sprint 0 completion
- `validation/LINT_REPORT_BEFORE.md` — legacy Phase 3 baseline
- `validation/RICH_LINT_BASELINE.md` — RICH runner baseline
- `../03_PHASE3_DECOMPOSITION/` — legacy Phase 3 (read-only)
- `../02_PHASE2_RULES_RICH/` — Phase 2 Rich (input for Phase 3 Rich)
- `../../../00_METHODOLOGY/AGENTS.md` — root methodology
- `../../../01_IMPLEMENTATION_TOOLS/lints/phase3/` — Phase 3 lint source (5 ported in Sprint 0)

---

**End of Sprint 4 Project State (v0.5) — Phase 3 Rich Mode ADJUSTED_FIELDS**
