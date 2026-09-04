---
document_id: AEGIS-C02-P3-NIST-ANCHORS
title: NIST CSF 2.0 + PF 1.0 + AI RMF Anchors v0 (Case_02 Phase 3)
phase: 3
version: 0.0
created: 2026-09-04
updated: 2026-09-04
author: PORT-PARITY-2 Executor (generated)
status: GENERATED
case: Case_02_SecureBorder_Solutions
---

> **GENERATED v0 (PORT-PARITY-2) — pending human review.** Mechanically derived from ../02_PHASE2_RULES_RICH/control_set.yaml (csf/pf/airmf/status_csf/status_privacy/status_airmf fields); verify before relying on it.

# NIST Anchors v0 — Case_02 SecureBorder Solutions

Per-rule anchors for all **63 controls** (38 CR + 25 BPR), copied **verbatim** from `../02_PHASE2_RULES_RICH/control_set.yaml` fields `csf`, `pf`, `airmf` (fields 22/24 of the Fase 5 control layout). This doc adds no anchors.

## §1 Per-rule anchors

| Rule ID | CSF 2.0 (`csf`) | PF 1.0 (`pf`) | AI RMF (`airmf`) | status_csf |
|---|---|---|---|---|
| CR-D-01.1-001 | PR.DS-01 | PR.DS-P1;CT.DP-P2 | GOVERN-1.6;MEASURE-2.7;MEASURE-2.5 | PARTIAL |
| CR-D-01.2-001 | PR.DS-02 | PR.DS-P2 | — | PARTIAL |
| CR-D-01.3-001 | PR.DS-01 | PR.DS-P1;CT.DP-P2 | MEASURE-2.7;GOVERN-1.6 | PARTIAL |
| CR-D-01.4-001 | PR.DS-01;PR.DS-02 | PR.DS-P1;CT.DM-P1;CT.DM-P3 | MEASURE-2.6;MEASURE-2.7;MANAGE-2.3 | IMPLEMENTED |
| CR-D-02.1-001 | ID.RA-01; ID.RA-08 | ID.RA-P3;ID.RA-P5 | MEASURE-1.1;MEASURE-2.1;MEASURE-2.3;MAP-3.3;MEASURE-2.7;MANAGE-1.3;MAP-3.2 | PARTIAL |
| CR-D-02.2-001 | PR.PS-02 | UNMAPPED_PF (no PF 1.0 analogue for product patch/OTA update management) | — | PARTIAL |
| CR-D-02.3-001 | ID.RA-08 | ID.IM-P7;GV.PO-P5 | — | PARTIAL |
| CR-D-02.4-001 | ID.IM-02;ID.RA-03 | ID.RA-P3;ID.RA-P4;ID.RA-P5 | MEASURE-2.7;MEASURE-2.11 | PARTIAL |
| CR-D-03.1-001 | PR.AA-01;PR.AA-03;PR.AA-05 | CT.PO-P1 | MAP-3.5;GOVERN-2.1;GOVERN-3.1 | PARTIAL |
| CR-D-03.2-001 | PR.AA-03 | UNMAPPED_PF (no PF 1.0 MFA subcategory) | — | PARTIAL |
| CR-D-03.3-001 | PR.AA-05;PR.AA-01 | CT.PO-P1 | — | PARTIAL |
| CR-D-03.4-001 | PR.PS-01 | CT.DP-P4;CT.PO-P4 | — | PARTIAL |
| CR-D-04.1-001 | DE.AE-02;DE.CM-01;DE.CM-09 | CM.AW-P7 | MEASURE-2.4;MEASURE-3.1;MANAGE-2.3;MANAGE-4.1 | PARTIAL |
| CR-D-04.2-001 | RS.MI-01;RS.MI-02 | PR.PO-P7;CT.DM-P10 | — | PARTIAL |
| CR-D-04.3-001 | RS.CO-02;RS.CO-03 | CM.AW-P7;CM.PO-P2;CM.PO-P1;GV.PO-P5 | MANAGE-2.3;MANAGE-4.3;GOVERN-1.1 | PARTIAL |
| CR-D-04.4-001 | UNMAPPED_PF (no PF 1.0 backup/DR recovery subcategory; CSF IDs corrected to CSF column per Doc19 §1) | UNMAPPED_PF | — | PARTIAL |
| CR-D-05.1-001 | PR.DS-10;ID.AM-03 | CT.PO-P4;CT.DP-P4;ID.RA-P3 | GOVERN-1.4;MAP-2.1;MEASURE-2.11;MAP-2.2 | PARTIAL |
| CR-D-05.2-001 | PR.DS-01;PR.PS-06 | CT.PO-P4;CT.DM-P5 | MEASURE-2.4;MEASURE-4.2;GOVERN-1.4 | PARTIAL |
| CR-D-05.3-001 | PR.DS-10 | CT.DM-P4;CT.DM-P5 | — | PARTIAL |
| CR-D-05.4-001 | — | CT.DM-P1;CT.DM-P6 | — | PARTIAL |
| CR-D-06.1-001 | GV.SC-04; GV.SC-07; ID.RA-10 | ID.IM-P2 | — | PARTIAL |
| CR-D-06.2-001 | GV.SC-09 | ID.IM-P7 | — | PARTIAL |
| CR-D-06.3-001 | GV.SC-05;GV.SC-06 | GV.PO-P5 | — | PARTIAL |
| CR-D-06.4-001 | DE.CM-06;PR.IR-01 | UNMAPPED_PF (no PF 1.0 analogue for physical third-party boundary isolation) | — | PARTIAL |
| CR-D-07.1-001 | PR.PS-06;ID.RA-01 | GV.PO-P2;CT.PO-P4;CT.DP-P2;CT.DP-P5 | GOVERN-4.1;GOVERN-4.3;MEASURE-2.5;MEASURE-2.6;MEASURE-2.7;GOVERN-1.2 | PARTIAL |
| CR-D-07.2-001 | PR.PS-06 | UNMAPPED_PF (no PF 1.0 secure-SDLC subcategory) | — | PARTIAL |
| CR-D-07.3-001 | PR.PS-06;PR.PS-02 | PR.PO-P4 | — | PARTIAL |
| CR-D-07.4-001 | ID.RA-07 | ID.RA-P3 | — | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) |
| CR-D-08.1-001 | PR.AT-01 | GV.AT-P1;GV.AT-P2 | — | PARTIAL |
| CR-D-08.2-001 | PR.AT-02 | GV.AT-P1;GV.AT-P2 | MAP-3.5;GOVERN-2.1;GOVERN-2.2;GOVERN-3.1 | PARTIAL |
| CR-D-08.3-001 | GV.RR-01;PR.AT-02 | UNMAPPED_PF (no PF 1.0 board-training subcategory) | — | PARTIAL |
| CR-D-09.1-001 | GV.PO-01;GV.PO-02 | GV.PO-P1;GV.PO-P5;CM.PO-P1 | GOVERN-1.1;GOVERN-1.3;GOVERN-1.4;GOVERN-1.6;MAP-1.1;MEASURE-2.8;MEASURE-2.9;MAP-3.4 | IMPLEMENTED |
| CR-D-09.2-001 | ID.RA-04;ID.RA-05;GV.RM-06 | ID.RA-P3;ID.RA-P4;ID.RA-P5 | GOVERN-1.1;GOVERN-1.3;GOVERN-1.5;MAP-5.1;MAP-3.1;MAP-3.2;MANAGE-1.2 | PARTIAL |
| CR-D-09.3-001 | ID.AM-01;ID.AM-02;ID.AM-07 | ID.IM-P1;ID.IM-P4;ID.IM-P6;ID.IM-P8 | — | PARTIAL |
| CR-D-09.4-001 | ID.AM-07;GV.OC-03 | ID.IM-P1;ID.IM-P4;ID.IM-P6;ID.IM-P8;CM.PO-P1 | MEASURE-2.4;MEASURE-3.1;GOVERN-1.6;GOVERN-2.1;MEASURE-4.2 | PARTIAL |
| CR-D-10.1-001 | DE.CM-01;DE.CM-09;DE.AE-02 | CM.AW-P7 | MANAGE-4.1;MEASURE-3.1;MEASURE-4.1;GOVERN-1.5;MEASURE-2.4 | PARTIAL |
| CR-D-10.2-001 | PR.PS-04;DE.AE-03;RS.AN-06 | CT.DM-P9 | MEASURE-2.4;MEASURE-3.1;GOVERN-1.6;MEASURE-4.2;GOVERN-1.4;GOVERN-2.1 | PARTIAL |
| CR-D-10.3-001 | UNMAPPED_PF (no PF 1.0 compliance-testing subcategory; CSF IDs corrected to CSF column per Doc19 §1) | UNMAPPED_PF | MEASURE-2.7;MEASURE-2.11;MANAGE-1.2;MEASURE-3.1 | PARTIAL |
| BPR-D-01.1-001 | PR.DS-01;PR.DS-10 | PR.DS-P1;CT.DP-P2 | — | PARTIAL |
| BPR-D-02.1-001 | ID.RA-01;DE.CM-01 | ID.RA-P3;ID.RA-P5 | — | PARTIAL |
| BPR-D-03.1-001 | PR.AA-01;PR.AA-05 | CT.PO-P1 | — | PARTIAL |
| BPR-D-04.1-001 | DE.AE-02;DE.CM-01 | CM.AW-P7 | MANAGE-2.3;MANAGE-4.3 | PARTIAL |
| BPR-D-07.1-001 | PR.PS-06 | GV.PO-P2;CT.PO-P4 | GOVERN-4.1;GOVERN-4.3;MEASURE-2.7 | PARTIAL |
| BPR-D-09.1-001 | GV.PO-01;GV.PO-02 | GV.PO-P1;GV.PO-P5 | GOVERN-1.1;GOVERN-1.4;GOVERN-1.5 | IMPLEMENTED |
| BPR-D-10.1-001 | DE.CM-01;DE.CM-09 | CM.AW-P7 | MANAGE-4.1;MEASURE-3.1;MEASURE-2.4 | PARTIAL |
| BPR-D-07.1-002 | — | — | MANAGE-4.1 | PARTIAL |
| BPR-D-10.5-001 | DE.CM-01 | — | MEASURE-2.6; MEASURE-2.7; MANAGE-4.2 | PARTIAL |
| BPR-D-02.4-001 | ID.RA-03 | ID.RA-P3 | MEASURE-2.6; MEASURE-2.5; MEASURE-2.11 | PARTIAL |
| BPR-D-03.1-002 | — <!-- human oversight is governance, not technical control; no valid CSF 2.0 anchor --> | — | GOVERN-4.2; GOVERN-5.2; MANAGE-2.3 | PARTIAL |
| BPR-D-10.2-001 | — <!-- explainability reporting; no CSF 2.0 anchor --> | — | GOVERN-4.1; MEASURE-2.9 | PARTIAL |
| BPR-D-02.4-002 | ID.RA-03 | ID.RA-P4 | MEASURE-3.1 | PARTIAL |
| BPR-D-04.2-001 | RS.MA-01 | CM.AW-P* | MANAGE-4.3; MEASURE-3.1 <!-- AI RMF 1.0 has only GOVERN/MAP/MEASURE/MANAGE functions; prior non-canonical RSPF function label removed; MEASURE-3.1 (AI system resilience testing) substituted per AI Act Art. 9(6) + Art. 15 resilience-testing anchor --> | PARTIAL |
| BPR-D-05.1-001 | ID.AM-03 | CT.PO-P4 | MANAGE-2.3; MAP-1.3 | PARTIAL |
| BPR-D-01.2-001 | PR.DS-01 | PR.DS-P1;CT.DP-P2 | — | PARTIAL |
| BPR-D-02.5-001 | ID.RA-01;DE.CM-01 | ID.RA-P3;ID.RA-P5 | — | PARTIAL |
| BPR-D-03.5-001 | PR.AA-01;PR.AA-05 | CT.PO-P1 | — | PARTIAL |
| BPR-D-04.5-001 | DE.AE-02;DE.CM-01 | CM.AW-P7 | MANAGE-2.3;MANAGE-4.3 | PARTIAL |
| BPR-D-05.5-001 | PR.DS-10;ID.AM-03 | CT.PO-P4;CT.DP-P4 | MAP-2.1;MAP-2.2;MEASURE-2.11 | PARTIAL |
| BPR-D-06.5-001 | GV.SC-04; GV.SC-07 | ID.IM-P2 | — | PARTIAL |
| BPR-D-07.5-001 | PR.PS-06;PR.PS-02 | PR.PO-P4 | — | PARTIAL |
| BPR-D-08.4-001 | PR.AT-01 | GV.AT-P1;GV.AT-P2 | — | PARTIAL |
| BPR-D-09.5-001 | GV.PO-01;GV.PO-02 | GV.PO-P1;GV.PO-P5 | GOVERN-1.1;GOVERN-1.4;GOVERN-1.5 | IMPLEMENTED |
| BPR-D-10.4-001 | DE.CM-01;DE.CM-09 | CM.AW-P7 | MANAGE-4.1;MEASURE-3.1;MEASURE-2.4 | PARTIAL |

## §2 Anchor counts per CSF 2.0 Function

Counting the **first** CSF id of each control's `csf` field (a control may cite several subcategories; multi-anchor counting is TODO(human) if desired):

| Function | Controls anchored |
|---|---:|
| GOVERN (GV) | 8 |
| IDENTIFY (ID) | 12 |
| PROTECT (PR) | 26 |
| DETECT (DE) | 8 |
| RESPOND (RS) | 3 |
| (none/other) | 6 |

## §3 Status distributions (verbatim control_set.yaml values)

| Field | Value | Count |
|---|---|---:|
| status_csf | PARTIAL | 58 |
| status_csf | IMPLEMENTED | 4 |
| status_csf | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | 1 |
| status_privacy | PARTIAL | 23 |
| status_privacy | IMPLEMENTED | 39 |
| status_privacy | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | 1 |
| status_airmf | PARTIAL | 13 |
| status_airmf | N/A (non-AI scope) | 29 |
| status_airmf | IMPLEMENTED | 13 |
| status_airmf | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | 8 |

## §4 Flags (unmapped / N-A anchors)

- Controls whose `csf` field contains `N/A`: none.
- Controls whose `pf` field carries `UNMAPPED_PF (…)` justification: ['CR-D-02.2-001', 'CR-D-03.2-001', 'CR-D-04.4-001', 'CR-D-06.4-001', 'CR-D-07.2-001', 'CR-D-08.3-001', 'CR-D-10.3-001'].
- Controls with no AI RMF anchors (`airmf` = `—`, `N/A (non-AI scope)` placeholder is the legal form): 29 of 63.
- Note: `check_unmapped.py` (P2 gate) enforces the frozen PF/AI-RMF vocabularies over these values; it re-verified PASS on 2026-09-04 with this doc in scope.

## §5 Sources

- `../02_PHASE2_RULES_RICH/control_set.yaml` — fields `csf`, `pf`, `airmf`, `status_csf`, `status_privacy`, `status_airmf`
- PF/AI-RMF frozen vocabularies: `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/NIST_PF/`, `.../NIST_AI_RMF/`
