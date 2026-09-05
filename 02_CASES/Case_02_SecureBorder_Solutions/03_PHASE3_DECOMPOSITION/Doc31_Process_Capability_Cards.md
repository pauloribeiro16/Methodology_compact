---
document_id: AEGIS-P3-31
title: Process & Capability Cards — Lane Pilot (Case_02)
phase: 3
version: 1.0
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
inputs: [Doc21_Use_Cases_Catalog.md, Doc18_Rules_Catalog.md, ../../00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/OWASP_SAMM/, ../../00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/OWASP_ASVS/]
outputs: [22_Traceability_Matrix.xlsx]
traceability: RULE → CAP → PROC → UC chain (REALIZATION_CLASS_RUBRIC.md v1.4 §5C)
related_documents: [Doc21_Use_Cases_Catalog.md, Doc18_Rules_Catalog.md]
---

# Process & Capability Cards — Lane Pilot (Case_02)

> **Purpose.** Operational representation for the PROCESS and CAPABILITY lanes
> (rubric `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` v1.4 §5C). Process cards follow
> the NIST SP 800-218 (SSDF) practice/task shape; capability cards follow the C2M2 /
> ArchiMate capability semantics. Traceability chain: **RULE → CAP → PROC → UC**.
> These cards are companions to the catalogue cards in `Doc21_Use_Cases_Catalog.md`
> (same IDs). Piloted set: 4 of 37 re-laned ids (registry: `LANE_NAMING_CENSUS_v0.md`).

## PROC-05 — Incident Detection & Triage

| Field | Content |
|---|---|
| Trigger | Security event raised on the event pipeline (eGate tamper, spoofing attempt, console anomaly, AI drift signal). |
| Activities | 1. SOC receives event via the security event pipeline. 2. Triage against severity matrix. 3. Clearance decision or escalation to containment (PROC-06). 4. False-positive closure with rationale. |
| Roles | SH-INT-008 (SOC Manager) owns triage and clearance decision; SH-INT-009 (Sec Eng) supports escalation. |
| SLA / Timing | 24/7 coverage; critical incidents escalated within minutes per NIS 2 Art. 23 posture. |
| Realises | CR-D-04.1-001, BPR-D-04.5-001 / SO-D-04.1-001. |
| Anchors | SAMM: IR-A (incident detection) · ASVS: V7 (error & logging). |
| Evidence | Triage records; escalation tickets; false-positive closure log. |

## PROC-14 — Unified Impact Assessment (DPIA + FRIA)

| Field | Content |
|---|---|
| Trigger | Prior to launch, annually, or on significant change to biometric AI processing. |
| Activities | 1. DPO initiates the unified assessment. 2. Section A — System Description (shared). 3. Section B — Data Processing Description (shared). 4. Section C — Necessity & Proportionality (shared). 5. Section D — Risk Identification (shared). 6. Section E — Mitigation Measures (shared). 7. Section F — DPIA-specific (GDPR Art. 35(7)) with FRIA-specific outputs (AI Act Art. 27) from the shared sections. |
| Roles | SH-INT-004 (DPO) owns; SH-INT-005 (AI Gov) contributes FRIA content. |
| SLA / Timing | Prior to launch / annual / on significant change. |
| Realises | CR-D-09.2-001 / PO-D-09.2-001 (PO-D-09.2-002, SO-D-09.2-001 downstream). |
| Anchors | SAMM: D-TA-B (threat assessment) · ASVS: V1.1 (secure SDLC). |
| Evidence | Completed DPIA+FRIA dossier with dual outputs; sign-off record. |

## CAP-02 — Continuous Security Monitoring

| Field | Content |
|---|---|
| Owner | SH-INT-008 (SOC Manager). |
| Span | Standing 24/7 unified SOC monitoring covering security + AI post-market metrics. Contributes: PROC-05 (triage), PROC-06 (containment), PROC-18 (authority reporting); U.C.10.x fleet telemetry; SOC competence curriculum (CAP-07). |
| Maturity | Scale A (posture model v1.6, `capability` scale); current/target to be bound to EvidenceItems (P1 Folio VIII) in the next maturity refresh. |
| Realises | CR-D-10.1-001, BPR-D-10.4-001, BPR-D-10.5-001 / SO-D-10.1-001..003. |
| Anchors | SAMM: O-EM-A (environment management, stream A) · ASVS: V7 (logging) — monitoring outcomes. |
| Evidence | 24/7 coverage rosters; monitoring dashboards; post-market AI metric reports. |

## CAP-06 — Security Awareness Training

| Field | Content |
|---|---|
| Owner | SH-INT-003 (CISO). |
| Span | Annual security awareness programme covering GDPR, CRA, NIS 2 topics. Contributes: CAP-07 (role-specific training), CAP-10 (phishing simulation); HR delivery chain. |
| Maturity | Scale A (posture model v1.6, `capability` scale); current/target to be bound to EvidenceItems (P1 Folio VIII) in the next maturity refresh. |
| Realises | CR-D-08.1-001, BPR-D-08.4-001 / PO-D-08.1-001..002. |
| Anchors | SAMM: G-EG-A (education & guidance, stream A) · ISO 27002:2022 A.6.3. |
| Evidence | Completion records; curriculum versions; annual review sign-off. |
