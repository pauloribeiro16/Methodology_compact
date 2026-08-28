---
document_id: AEGIS-CASE02-PORT-CENSUS
title: "Port Census v0 — Case_01→Case_02 upgrade campaign baseline"
phase: META
version: 0.1
created: 2026-08-28
updated: 2026-08-28
author: Orchestrator (port campaign, Fase 0)
status: ACTIVE
---

# Port Census v0 — baseline before the Case_01-campaign port

Meta report (not a deliverable). Measures the exact state of Case_02 P1+P2
(+ transversal findings) before Fase 0 repairs. All counts taken 2026-08-28
on the post-Sprint-9/10 tree. Verification for later fases = re-run these
greps and compare.

## 1. UNMAPPED token census (occurrences, `grep -o`)

| Variant | Occurrences | Files (deliverables) |
|---|---|---|
| UNMAPPED_AIRMF | 91 | Doc19, Doc18 (concentrated) |
| UNMAPPED_PF | 61 | Doc19, Doc18 |
| UNMAPPED_CSF | 20 | Doc19 |
| UNMAPPED_PRIVACY | 13 | Doc19 |
| `UNMAPPED_` bare | 3 | Doc19 |
| **Total** | **188** | Doc19=138, Doc18=35, SPEC=8, Doc16=1, Doc17=1 (+5 in VALIDATOR_BLOCOG, excluded path) |

Target state (per Case_01 `VALIDATOR_UNMAPPED_AUDIT_v0.md` recipe + SPEC §4.6):
UNMAPPED_PRIVACY=0 (retired), UNMAPPED_AIRMF=0 (Case_02 has AI Act → real AI RMF
anchors or justified `N/A (non-AI scope)`), UNMAPPED_PF only element-level with
mandatory justification, UNMAPPED_CSF content-verdicted.

## 2. Sprint frontmatter keys (deliverables, outside validation/)

| File | Keys |
|---|---|
| Doc13_Adjusted_Objectives.md | `sprint: 5`, `sprint_role` (L20–21) |
| Doc16_Privacy_Security_Goals.md | `sprint: 10`, `sprint_10_scope`, `sprint_10_verdict` |
| Doc17_…NIST_Implications.md | `sprint: 10` |
| Doc19_Framework_Mapping_Matrix.md | `sprint: 10` |
| 02_PHASE2 README.md | `sprint: 8`, `sprint_role`, `sprints_complete`, `sprints_pending` |
| 02_PHASE2 PROJECT_STATE.md | `sprints_complete`, `sprints_pending`, `sprint_in_progress` |
| P3: Doc21/24/25/26/27/28 | `sprint_11_scope` (L14) |

Case_01 gate rule: zero `^\s*sprint(_\w+)?\s*:` outside `validation/`,
`VALIDATOR_*`, `CHANGE_LOG`, `DEPRECATED`, `RICH_VS_LEGACY`.

## 3. Legacy maturity vocabulary (`/maturi/i`, deliverables only)

P1: Doc13=76, Doc05=37, Doc08=5, Doc12=3, Doc02=4, Doc07=2, Doc04=2, Doc06=1.
P2: SPEC=55, Doc18=26, Doc17=10, Doc19=11, Doc16=2, Doc20=1, README=16.
00_COMMON: 01_Company_Context=4, 03_Design_Decisions_Log=1. README root=1.
P3: **0** (verified clean). Excluded paths (validation/, RICH_VS_LEGACY) not counted.
P2 frontmatter also carries `total_cells_triple_maturity: 165` and
`frameworks_in_scope: [.., NIST_Privacy_FW_1.1, ..]` (draft PF 1.1 — must become PF 1.0 per SPEC §4.2).

## 4. PG-D-/SG-D- prefix census (deliverables)

Doc13=141, P3 Doc30_Requirements=56, Doc16=41 (incl. Appendix A legacy aliases,
expected), Doc11=3, Doc17=1, PHASE3_PLAN=2. Decision (P7, 2026-08-28): migrate
to `AG-D-XX.X-NNN` with Appendix A alias preservation (Fase 1).

## 5. AI-C19 divergence (D1 removal of 2026-08-13, `feature/remediation-pf-airmf-audit`)

Removal is VALID: SecureBorder is PROVIDER (00_COMMON/01_Company_Context L217);
Art. 26(1) deployer duty falls on the border-control authority. Clause count
AI_Act 29→28, total 112→111. Reference status:

| Site | Status | Action (Fase 0) |
|---|---|---|
| 00_COMMON/phase1_ontology.yaml (frozen legacy copy) | updated with D1 note | none (legacy copy, superseded) |
| Doc14 (L737), Doc15 (L319), Doc18 (L25), Doc19 (L21) | annotations of the D1 decision only | none (legitimate historical notes) |
| **Doc10_Clause_Mapping_Matrix.md L174** | still maps AI-C19 in D-03; header says "29 clauses" | REMOVE AI-C19 row, fix counts |
| **01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml L7,132** | still 112 total / AI_Act 29 | REMOVE AI-C19 clause, 29→28, 112→111 |

## 6. NOT_ADDRESSED set divergence

Canonical set (README L92, Doc09, Doc12): **{D-07.4, D-08.3, D-09.3}**, with
D-07.2 ACTIVE (CRA+NIS 2 partial). Stale wrong-set holders:
- Doc07 frontmatter L13 (`D-07.2, D-07.4, D-09.3`) → fix
- Doc11 §88 (`D-07.2, D-07.4, D-09.3`) → fix
- Doc08 §369 ("No Coverage: D-07.2, D-07.4, D-09.3"; contradicts own L352/357) → fix

## 7. State-chain staleness

- Case PROJECT_STATE.md: header "Last Updated 2026-04-04"; §1.2 AI Act 29 / total 112;
  April doc tables (8/8, 5/5, 9/9, legacy names 00–25); §9 points to
  non-existent dirs `01_PHASE1_CONTEXT/`, `02_PHASE2_RULES/`.
- progress.json: April-frozen (phase entries keyed to legacy doc names, gates
  P1/P2/P3_PASS dated April); `change_log` last entries pre-Sprint-9.
- P1 PROJECT_STATE.md: verdict CONDITIONAL_PASS, F-01 "BLOCKING/disputed",
  "Substitution has NOT occurred", next-steps blocked by O-01 — all superseded
  (F-01 SETTLED 2026-08-10 as MEDIUM by P7 human arbiter; rich folder is the
  working corpus per case README).
- P1 README.md: L108 link→`Doc12_Structured_Compliance_Matrix.md` (should be Doc11);
  L109 link→`Doc13_Proportionality_Profile.md` (should be Doc12); L110 "07c
  PLACEHOLDER" (actually DEEP_ENRICHED); L180 "F-01 DISPUTED / pending
  adjudication" (settled).
- Doc18: Sprint-10 banner paragraph duplicated verbatim (L1+L3) → keep one.

## 8. Frontmatter legacy basenames (`inputs/outputs/related_documents` + prose)

Legacy `NN_*` basenames present in 20 deliverables. Top: Doc19=26, Doc20=26,
Doc12=15, Doc13=13, Doc11=10, Doc03=9, Doc17=8, Doc08=6, Doc16=6, Doc07=5.
Repaired in Fase 1 (full, including cross-phase edges).

## 9. Verified non-issues (for the record)

- P3: zero `/maturi/i`, zero UNMAPPED tokens. Only sprint keys (§2).
- 8-field frontmatter present on every P1/P2 deliverable (exception:
  00_COMMON/02_Regulatory_Mapping_Master.md — DEPRECATED banner, out of port scope).
- Case_01 campaign concepts ABSENT (to be ported): anchoring taxonomy §4.6,
  Control Set v1 + control_set.yaml, gates (check_unmapped / posture),
  PRODUCTION_FLOW.md, F-V-style validation reports for the campaign.

## 10. Census arithmetic note

Occurrence counts via `grep -o` (token-level), not line counts (Doc19: 114
lines vs 138 occurrences). Case_01's audit header (925) vs table sum (869)
discrepancy is NOT replicated here: this census states its counting basis.
