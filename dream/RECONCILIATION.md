# Reconciliation — git vs state files

_Generated 2026-08-26 by `scripts/dream/reconcile.py` — deterministic._

## Recent commits (last 15)

| Date | SHA | Subject |
|---|---|---|
| 2026-08-26T17:54:35 | `10c91482` | [WEB] Dashboard fix #4: Folio IV grid rebuilds GRID from runtime KG (linkByFrom for YIELDS) — Case_01 |
| 2026-08-26T17:45:08 | `b11ff4cc` | [WEB] Dashboard fix #3: applyStoryDim preserves x/y so Folio V pipeline no longer collapses to origin — Case_01 |
| 2026-08-26T17:35:45 | `8ab16883` | [WEB] Dashboard fix #2: drop focusNodeAdjacency + emphasis.focus + dispatchAction(highlight) — colours preserved when node focused — Case_01 |
| 2026-08-26T17:25:20 | `b6c58aa7` | [WEB] Dashboard: soft-dim fix + click-empty/Esc clear + new Folio V 'Phase 1 Story' (197/264/16) — Case_01 |
| 2026-08-26T17:25:15 | `febfcb7c` | [EXECUTOR] v1.2: kg_ontology (additive) + KG extended 181→197/248→264/12→16 + ontology-aware --check — Case_01 |
| 2026-08-26T16:33:54 | `47d33c21` | [VALIDATOR] Sprint 6 validator + PROJECT_STATE + progress.json + CHANGE_LOG_CENTRAL — Case_01 |
| 2026-08-26T16:31:33 | `05d75e74` | [EXECUTOR] Doc26 v2.0 + drawio regen (product-root tree) — Case_01 |
| 2026-08-26T16:30:46 | `42562136` | [EXECUTOR] xlsx 12-sheet + RULE_FREEZE v2.0 — Case_01 |
| 2026-08-26T16:29:17 | `18a637f9` | [EXECUTOR] Doc21/22 v1.0: extended with constrains/threatens/mitigated_by + functional variants — Case_01 |
| 2026-08-26T16:27:56 | `1661e5eb` | [EXECUTOR] Doc20 v3.0: product UCs (U.C.7-11) + anatomy for U.C.1-6 + 8 MUCs — Case_01 |
| 2026-08-26T16:23:00 | `8792d5d1` | [ORCHESTRATOR] P1 dashboard: GUI test report — conditional fail (no clear-selection path) — Case_01 |
| 2026-08-26T16:03:00 | `58c6b368` | [WEB] P1 dashboard: graph + audit + one-pager — Case_01 (replaces legacy) |
| 2026-08-26T16:02:57 | `7b962dd2` | [EXECUTOR] P1 knowledge-graph JSON (extract+validate) — Case_01 |
| 2026-08-26T15:20:05 | `c94b8408` | [ORCHESTRATOR] Rename: case-file convention DocNN_Nome.md (95 renames, 0 content diff) |
| 2026-08-26T14:46:47 | `8d1f752b` | [ORCHESTRATOR] Harness: best-practice increments (commands + user AGENTS.md + guardrails + skill pruning) |

## State files behind git

_`PROJECT_STATE.md` declares an older date than the last git touch._

| File | Declared | Last git touch | Drift |
|---|---|---|---|
| 02_CASES/GLOBAL_PROJECT_STATE.md | 2026-08-24 | 2026-08-26 | **2d (medium)** |
| 02_CASES/Case_03_OmniBank_Financial/PROJECT_STATE.md | 2026-04-03 | 2026-08-26 | **145d (high)** |
| 02_CASES/Case_02_SecureBorder_Solutions/PROJECT_STATE.md | 2026-04-04 | 2026-08-26 | **144d (high)** |
| 02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md | 2026-08-24 | 2026-08-26 | **2d (medium)** |

## Hardcoded main-repo paths still referenced

_These will mislead any agent reading case docs as canonical._

- 02_CASES/CHANGE_LOG_CENTRAL.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/GLOBAL_PROJECT_STATE.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/README.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/PROJECT_STATE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/README.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/README.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/PROJECT_STATE.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/NIST_ANCHORS.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/Doc20_Use_Cases_Catalog.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/TRACEABILITY_AUDIT.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/TRACEABILITY_AUDIT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/PROJECT_STATE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/Doc15_Strategic_Tensions_Report.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/Doc16_Privacy_Security_Objectives.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/Doc14_Obligation_Derivation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/Doc19_Framework_Mapping_Matrix.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/SPEC_NIST_MATRIX_UNIFIED.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/README.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/Citation_Index.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/Doc07_Org_Roles_RACI.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/PROJECT_STATE.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/PROJECT_STATE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/Corpus_Field_Map.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/Doc12_Proportionality_Profile.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/README.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT4.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT4.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/SPRINT2_ENRICHMENT_REPORT_EXISTING.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/SPRINT2_ENRICHMENT_REPORT_EXISTING.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT3.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT3.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT0.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT0.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_raci_extension_v1.3_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_ontology_v1.3_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/SPRINT1_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_graph_json_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_AFTER_RECONCILE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_dashboard_gui_test.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_TIER1.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_graph_extension_v1.2_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_BEFORE.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_BEFORE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/SPRINT4_REPORT.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/SPRINT2_ENRICHMENT_REPORT_NEW.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT5.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/SPRINT5_REPORT.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_ontology_v1.2_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/CORPUS_AUGMENTATION_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/FIX_TIER1_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/SPRINT3_REPORT.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/SPRINT3_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/validation/VALIDATOR_SPRINT5.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/validation/SPRINT0_REPORT.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/validation/SPRINT0_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc27_Functional_Tree.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/Doc20_NIST_Framework_Inputs.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/Doc16_Privacy_Security_Goals.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/PROJECT_STATE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/Doc19_Framework_Mapping_Matrix.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/SPEC_NIST_MATRIX_UNIFIED.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/README.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/Citation_Index.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/PROJECT_STATE.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/Doc12_Proportionality_Profile.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/RICH_VS_LEGACY.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/RICH_VS_LEGACY.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/README.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT3.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT3.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/SPRINT1_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_TIER2.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_AFTER_RECONCILE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_TIER1.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_TIER1.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_BEFORE.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_BEFORE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT5.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT5.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/SPRINT3_REPORT.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/SPRINT3_4_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/LINT_REPORT_BEFORE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/VALIDATOR_SPRINT5.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/SPRINT5_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/SPRINT2_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/SPRINT3_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/SPRINT0_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/annexes/PHASE3_PLAN.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/Doc19_Privacy_Security_Goals_NIST_Implications.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/PROJECT_STATE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/Doc21_Framework_Mapping_Matrix.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/SPEC_NIST_MATRIX_UNIFIED.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/README.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/PROJECT_STATE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Corpus_Field_Map.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc11_DORA_ICT_Risk_Framework.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc13_Proportionality_Profile.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc13_Proportionality_Profile.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/RICH_VS_LEGACY.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/README.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT3.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/SPRINT1_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_TIER2.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_AFTER_RECONCILE.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_AFTER_RECONCILE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/FIX_TIER12_REPORT.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/FIX_TIER12_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_TIER1.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_TIER1.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_BEFORE.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_BEFORE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/SPRINT4_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/SPRINT2_ENRICHMENT_REPORT_NEW.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/SPRINT5_REPORT.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/SPRINT3_4_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/LINT_REPORT_BEFORE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/VALIDATOR_SPRINT5.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/SPRINT5_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/SPRINT2_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/SPRINT3_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/SPRINT0_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)

## progress.json vs phase folder consistency

- Case_03_OmniBank_Financial/progress.json: declared phase 2 but highest phase folder is 03 (03_PHASE3_DECOMPOSITION)

## Proposed state-file patches (never auto-applied — P7)

_For each drift item, the proposed edit is to bump the `Last Updated` header on the affected `PROJECT_STATE.md` to the last git-touch date, and add a one-line summary of the commits that changed the file since._

### 02_CASES/GLOBAL_PROJECT_STATE.md

```diff
- **Last Updated:** 2026-08-24
+ **Last Updated:** 2026-08-26  (bumps: 2d of drift since last state bump)
+ **Drift note:** run `git log --since=2026-08-24 -- 02_CASES/GLOBAL_PROJECT_STATE.md` and summarise in the appropriate status table.
```

### 02_CASES/Case_03_OmniBank_Financial/PROJECT_STATE.md

```diff
- **Last Updated:** 2026-04-03
+ **Last Updated:** 2026-08-26  (bumps: 145d of drift since last state bump)
+ **Drift note:** run `git log --since=2026-04-03 -- 02_CASES/Case_03_OmniBank_Financial/PROJECT_STATE.md` and summarise in the appropriate status table.
```

### 02_CASES/Case_02_SecureBorder_Solutions/PROJECT_STATE.md

```diff
- **Last Updated:** 2026-04-04
+ **Last Updated:** 2026-08-26  (bumps: 144d of drift since last state bump)
+ **Drift note:** run `git log --since=2026-04-04 -- 02_CASES/Case_02_SecureBorder_Solutions/PROJECT_STATE.md` and summarise in the appropriate status table.
```

### 02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md

```diff
- **Last Updated:** 2026-08-24
+ **Last Updated:** 2026-08-26  (bumps: 2d of drift since last state bump)
+ **Drift note:** run `git log --since=2026-08-24 -- 02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md` and summarise in the appropriate status table.
```


---

_Re-run after each `git push` to keep this current._
