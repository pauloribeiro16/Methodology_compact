# Reconciliation — git vs state files

_Generated 2026-08-28 by `scripts/dream/reconcile.py` — deterministic._

## Recent commits (last 15)

| Date | SHA | Subject |
|---|---|---|
| 2026-08-28T14:13:24 | `b0cddb68` | [EXECUTOR+VALIDATOR] port Case_03 Fase 7: PRODUCTION_FLOW v1.0 + flow audit PASS_WITH_NOTES + bookkeeping (progress.json, CHANGE_LOG_CENTRAL 6.2, GLOBAL_PROJECT_STATE 6.5, case PS) — campaign complete — Case_03 |
| 2026-08-28T14:11:31 | `049ef543` | [EXECUTOR+VALIDATOR] port Case_03 Fase 6: legacy-marker sweep case-wide + gates v0.3 ported (check_unmapped.py + check_implementation_posture_case03.py) — GATE PASS — Case_03 |
| 2026-08-28T13:49:07 | `3dd0f1b2` | [EXECUTOR] port Case_03 Fase 5: Control Set v1 — Doc20 v2.0 (F21/F22/F23 statuses backfilled, traceability with AG-, F24 → Doc21 §1, Annexes A-C), build_control_set.py + control_set.yaml 78 controls (38 CR + 40 BPR) with '**' assert — Case_03 |
| 2026-08-28T13:43:04 | `5e17b5fa` | [EXECUTOR] port Case_03 Fase 4: P2 posture migration — Doc21 §4/§5.1 (78 controls, 177 PARTIAL/57 N/A)/§5.2/§6.4/V4, Doc19 posture fields, SPEC supersession banner — Case_03 |
| 2026-08-28T13:39:58 | `6149d578` | [EXECUTOR+VALIDATOR] port Case_03 Fase 3: UNMAPPED adjudication — AIRMF 140→N/A non-AI-scope (23 CR) + real anchors kept (15 CR), PRIVACY retired, PF gaps justified (7 CR + 7 BPR), Doc20 PT placeholders standardised (51), SPEC §4.6, audit report — Case_03 |
| 2026-08-28T13:32:44 | `bf0969e4` | [EXECUTOR+VALIDATOR] port Case_03 Fase 2b: ontology v2.0-port kg_ontology (DORA branch, posture, invariants) + port validation report + PROJECT_STATE Bloco A summary — Case_03 |
| 2026-08-28T13:31:24 | `cc55eda3` | [EXECUTOR] port Case_03 Fase 2a: P1 posture purge — Doc05 DEPRECATED_FOR_POSTURE, Doc08 158 cells backfilled, Doc13 76 cells, Doc02/04/06/07/14 vocabulary — Case_03 |
| 2026-08-28T13:28:07 | `daf49fda` | [EXECUTOR] port Case_03 Fase 1 fixup: Doc16 inputs xlsx repoint — Case_03 |
| 2026-08-28T13:27:50 | `f3fd04b9` | [EXECUTOR] port Case_03 Fase 1: sprint sweep deliverables + legacy basename→DocNN map (content-based slot map) + dead-dir refs + Docs 16/17/18/20 DRAFT→ACTIVE with 5-reg frontmatter + Doc17 v1.1 (T-005) — Case_03 |
| 2026-08-28T13:25:55 | `6ad9c64d` | [EXECUTOR] port Case_03 Fase 0: adjudications (tensions=5 w/ T-005, AI-C19 kept, PF 1.0, corr-012 registered) + state-chain repair (case PS 3.1, P1 PS/README, P2 PS/README, progress.json) — Case_03 |
| 2026-08-28T13:22:50 | `c7658000` | [EXECUTOR] port Case_03 Fase 0: PORT_census_v0 baseline (262 UNMAPPED tokens, sprint keys, maturi scales, AG- verified, divergences adjudicated) — Case_03 |
| 2026-08-28T13:01:18 | `5608d142` | [EXECUTOR] port Case_02: fix commit count in bookkeeping (13, not 18) — Case_02 |
| 2026-08-28T13:01:10 | `b42602db` | [EXECUTOR+VALIDATOR] port Case_02 Fase 7: PRODUCTION_FLOW v1.0 + flow audit (PASS_WITH_NOTES, mirror refresh) + bookkeeping (progress.json, CHANGE_LOG_CENTRAL 6.1, GLOBAL_PROJECT_STATE 6.4, case PS) — campaign complete — Case_02 |
| 2026-08-28T12:58:11 | `78d895e3` | [EXECUTOR+VALIDATOR] port Case_02 Fase 6: sprint-key sweep (P2/P3/00_COMMON/SPEC) + gates v0.3 ported (check_unmapped.py + check_implementation_posture_case02.py) — GATE PASS — Case_02 |
| 2026-08-28T12:51:11 | `7b9e6e6f` | [EXECUTOR] port Case_02 Fase 5: Control Set v1 — Doc18 v6.0 (F21/F22 posture statuses, F23 traceability, F24 anchors, Annexes A-C), build_control_set.py + control_set.yaml 63 controls with status-parsing fix — Case_02 |

## State files behind git

_`PROJECT_STATE.md` declares an older date than the last git touch._

| File | Declared | Last git touch | Drift |
|---|---|---|---|
| 02_CASES/GLOBAL_PROJECT_STATE.md | 2026-08-27 | 2026-08-28 | **1d (medium)** |

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

- Case_03_OmniBank_Financial/progress.json: declared phase 2 but highest phase folder is 03 (03_PHASE3_DECOMPOSITION)

## Proposed state-file patches (never auto-applied — P7)

_For each drift item, the proposed edit is to bump the `Last Updated` header on the affected `PROJECT_STATE.md` to the last git-touch date, and add a one-line summary of the commits that changed the file since._

### 02_CASES/GLOBAL_PROJECT_STATE.md

```diff
- **Last Updated:** 2026-08-27
+ **Last Updated:** 2026-08-28  (bumps: 1d of drift since last state bump)
+ **Drift note:** run `git log --since=2026-08-27 -- 02_CASES/GLOBAL_PROJECT_STATE.md` and summarise in the appropriate status table.
```


---

_Re-run after each `git push` to keep this current._
