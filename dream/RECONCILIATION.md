# Reconciliation — git vs state files

_Generated 2026-09-03 by `scripts/dream/reconcile.py` — deterministic._

## Recent commits (last 15)

| Date | SHA | Subject |
|---|---|---|
| 2026-09-03T16:32:35 | `6470bac1` | [DREAM SELF-TUNE] regression_check: exclude self from recursive --self-test |
| 2026-09-03T16:29:33 | `79e55e76` | [DREAM SELF-TUNE] regression_check.py (Phase 3 watchdog + auto-revert) |
| 2026-09-03T16:29:20 | `2637f60d` | [DREAM SELF-TUNE] auto_tune + stale_archive + run_nightly (Phase 2) |
| 2026-09-03T16:22:41 | `0df528c2` | [DREAM SELF-TUNE] self_tune infrastructure: scope guard + validators + self-test |
| 2026-09-02T23:56:17 | `5c7662c2` | [DREAM 2026-09-02] nightly consolidation (0 amendments, 2 drifts, 1 lesson) |
| 2026-09-01T23:55:57 | `4c8fc9ff` | [DREAM 2026-09-01] nightly consolidation (0 amendments, 2 drifts, 0 lessons) |
| 2026-09-01T13:03:16 | `643e7840` | [ORCHESTRATOR] brief.sh: robust drift regex + 2 new LESSONS entries |
| 2026-08-31T23:56:54 | `3566983e` | [DREAM 2026-09-01] nightly consolidation (0 amendments, 2 drifts, 1 lesson) |
| 2026-08-31T09:48:35 | `7a5384ea` | [ORCHESTRATOR] LESSONS: resolve-pending pattern + harness-audit-effect confirmation |
| 2026-08-31T09:47:00 | `904eb6ba` | [EXECUTOR] Case-side work: dashboard v1.6, Case_02 v1.6 artefacts, project state sync (UI + ontology + scripts) |
| 2026-08-31T09:44:44 | `fc9af460` | [ORCHESTRATOR] Archive one-shot port scripts + LESSONS entry |
| 2026-08-31T09:43:24 | `a5873e2b` | [ORCHESTRATOR] State sync: Case_02/03 PROJECT_STATE + Case_03 progress.json (port campaigns complete) |
| 2026-08-30T23:01:10 | `a5589190` | [HARNESS 2026-08-30] weekly audit (21 healthy, 10 weak, 0 dead, 0 live-probe-failures, 0 cri) |
| 2026-08-28T23:56:40 | `42d6aa76` | [DREAM 2026-08-28] nightly consolidation (1 amendment, 1 drift, 0 lessons) |
| 2026-08-28T14:13:24 | `b0cddb68` | [EXECUTOR+VALIDATOR] port Case_03 Fase 7: PRODUCTION_FLOW v1.0 + flow audit PASS_WITH_NOTES + bookkeeping (progress.json, CHANGE_LOG_CENTRAL 6.2, GLOBAL_PROJECT_STATE 6.5, case PS) — campaign complete — Case_03 |

## State files behind git

_`PROJECT_STATE.md` declares an older date than the last git touch._

| File | Declared | Last git touch | Drift |
|---|---|---|---|
| 02_CASES/Case_03_OmniBank_Financial/PROJECT_STATE.md | 2026-08-28 | 2026-08-31 | **3d (medium)** |
| 02_CASES/Case_02_SecureBorder_Solutions/PROJECT_STATE.md | 2026-08-28 | 2026-08-31 | **3d (medium)** |

## Hardcoded main-repo paths still referenced

_These will mislead any agent reading case docs as canonical._

- 02_CASES/CHANGE_LOG_CENTRAL.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/CHANGE_LOG_CENTRAL.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/GLOBAL_PROJECT_STATE.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/README.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_03_OmniBank_Financial/PROJECT_STATE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
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
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_production_flow_audit_v0.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_production_flow_audit_v0.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT0.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT0.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_raci_extension_v1.3_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_ontology_v1.3_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_ontology_v1.5_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/SPRINT1_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_graph_json_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_AFTER_RECONCILE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_graph_extension_v1.4_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
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
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_ontology_v1.4_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/FIX_TIER1_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/SPRINT3_REPORT.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/SPRINT3_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_cross_case_mirror_v0.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/validation/VALIDATOR_SPRINT5.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/validation/SPRINT0_REPORT.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/validation/SPRINT0_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc27_Functional_Tree.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/validation/PORT_census_v0.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/Doc20_NIST_Framework_Inputs.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/Doc16_Privacy_Security_Goals.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/PROJECT_STATE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/Doc19_Framework_Mapping_Matrix.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/SPEC_NIST_MATRIX_UNIFIED.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/README.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/Citation_Index.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/Doc13_Adjusted_Goals.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/PROJECT_STATE.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/Doc12_Proportionality_Profile.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/RICH_VS_LEGACY.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/RICH_VS_LEGACY.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/PRODUCTION_FLOW.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/README.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT3.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT3.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/SPRINT1_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_TIER2.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/P1_production_flow_audit_case02.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_AFTER_RECONCILE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_TIER1.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_TIER1.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_BEFORE.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/LINT_REPORT_BEFORE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT5.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_SPRINT5.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/P1_ontology_port_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/SPRINT3_REPORT.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/SPRINT3_4_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/LINT_REPORT_BEFORE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/VALIDATOR_SPRINT5.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/SPRINT5_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/SPRINT2_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/SPRINT3_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/validation/SPRINT0_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/annexes/PHASE3_PLAN.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/Doc16_Obligation_Derivation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/Doc19_Privacy_Security_Goals_NIST_Implications.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/PROJECT_STATE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/Doc21_Framework_Mapping_Matrix.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/Doc17_Strategic_Tensions_Report.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/SPEC_NIST_MATRIX_UNIFIED.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/RICH_VS_LEGACY.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/README.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc07_Org_Roles_RACI.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc04_Architecture_DataInventory.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/PROJECT_STATE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Corpus_Field_Map.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Corpus_Field_Map.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc06_ThirdParty_Landscape.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc03_Company_Context_Assessment.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc10_Clause_Mapping_Matrix.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc05_Security_Posture.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc11_DORA_ICT_Risk_Framework.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc12_Structured_Compliance_Matrix.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc13_Proportionality_Profile.md: contains `01_IMPLEMENTATION_TOOLS/` — main-repo path not in compact
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc13_Proportionality_Profile.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc08_Regulatory_Applicability.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
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
- 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/validation/P1_ontology_port_validation.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/SPRINT3_4_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/LINT_REPORT_BEFORE.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/VALIDATOR_SPRINT5.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/SPRINT5_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/SPRINT2_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/SPRINT3_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)
- 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/validation/SPRINT0_REPORT.md: contains `01_PHASE1_CONTEXT_RICH` — typo of 01_PHASE1_CONTEXT_RICH (correct in compact)

## progress.json vs phase folder consistency

_All progress.json current_phase fields match the highest phase folder._

## Proposed state-file patches (never auto-applied — P7)

_For each drift item, the proposed edit is to bump the `Last Updated` header on the affected `PROJECT_STATE.md` to the last git-touch date, and add a one-line summary of the commits that changed the file since._

### 02_CASES/Case_03_OmniBank_Financial/PROJECT_STATE.md

```diff
- **Last Updated:** 2026-08-28
+ **Last Updated:** 2026-08-31  (bumps: 3d of drift since last state bump)
+ **Drift note:** run `git log --since=2026-08-28 -- 02_CASES/Case_03_OmniBank_Financial/PROJECT_STATE.md` and summarise in the appropriate status table.
```

### 02_CASES/Case_02_SecureBorder_Solutions/PROJECT_STATE.md

```diff
- **Last Updated:** 2026-08-28
+ **Last Updated:** 2026-08-31  (bumps: 3d of drift since last state bump)
+ **Drift note:** run `git log --since=2026-08-28 -- 02_CASES/Case_02_SecureBorder_Solutions/PROJECT_STATE.md` and summarise in the appropriate status table.
```


---

_Re-run after each `git push` to keep this current._
