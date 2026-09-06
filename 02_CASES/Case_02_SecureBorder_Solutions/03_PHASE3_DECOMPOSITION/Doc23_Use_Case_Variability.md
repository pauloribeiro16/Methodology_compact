---
document_id: AEGIS-P3-13b
title: 13b Use Case Variability
phase: 3
version: 1.1
created: 2026-04-30
updated: 2026-09-05
author: Security Architect
status: DRAFT
case: Case_02_SecureBorder_Solutions
inputs: [13_Use_Cases_Catalog.md, 13a_Use_Case_Relationships.md]
outputs: [14_Architectural_Nodes.md, 15_Requirements_Allocation.md]
traceability: AEGIS Class Model → UseCaseVariability, VariantPoint classes
related_documents: [13_Use_Cases_Catalog.md, 13a_Use_Case_Relationships.md]
---

# 13b Use Case Variability — SecureBorder Solutions

**Case:** Case 02 — SecureBorder Solutions (Border Control / Physical Security)
**Phase:** 3 — Use Case Variability
**Company Profile:** Medium-Large (450 employees), B2G/B2B, GDPR+CRA+NIS2+AI_Act

---

## 1. DOCUMENT PURPOSE

This document defines the variability mechanisms and configuration options for the SecureBorder Solutions system, enabling customization for different deployment scenarios.

---

## 2. VARIABILITY METADATA

| Attribute | Value |
|-----------|-------|
| variabilityId | UC-VAR-SECUREBORDER-2026-001 |
| completionDate | 2026-04-30 |
| basedOnUseCasesCatalog | UC-SECUREBORDER-2026-001 |
| basedOnRelationships | UC-REL-SECUREBORDER-2026-001 |
| completedBy | Security Architect |
| phase3Step | Use Case Variability |
| companyProfile | Medium-Large (450 employees), B2G/B2B |

---

## 3. VARIATION POINTS

*Placeholder for variation point definitions — variability anchors now recorded in §4 (Lane Variants) and §5 (Product Variants).*

---

## 4. LANE VARIANTS (current id space)

Anchors derived from `Doc31_Process_Capability_Cards.md` cards; no variant is invented.

### 4.1 Process lane variants

| Base UC / Lane id | Variation Point | Variants | Binding |
|---|---|---|---|
| PROC-01 (DSAR) | Request intake channel | V1: web portal submission; V2: email submission (both verified against traveler identity per card step 2) | Card "Trigger": request via DSAR channel — channel is free |
| PROC-03 (Biometric Breach Notification) | Regulatory path | V1: ENISA/CSIRT path (NIS 2 24h early warning); V2: CNPD/DPA path (GDPR 72h breach notification); both can bind (unified PROC-07 24h/72h output) | Doc21 §3 stakeholders SH-EXT-008/009/010; PROC-07 unified card |
| PROC-14 (Unified Impact Assessment) | Regulatory dual-output | V1: DPIA output (GDPR Art. 35(7)); V2: FRIA output (AI Act Art. 27); both produced from shared sections A–E | Doc31 PROC-14 card mermaid (Regulatory outputs branch) |
| PROC-07 (Regulatory Notification) | Recipient variant | V1: NIS 2 CSIRT 24h; V2: DPA 72h; V3: AI Market Surveillance cooperation | Doc31 PROC-07 card |

### 4.2 Product lane variants (PKG-8..12)

| Base UC | Variation Point | Variants | Binding |
|---|---|---|---|
| UC-16..UC-22 journey | Crossing mode | V1: fully automated kiosk crossing (UC-16→UC-20 all-TRUE); V2: assisted referral (UC-21 officer desk; on any failure/grey-band/watchlist path) | Doc21 UC-21 preconditions |
| UC-22 (Privacy Notice & Consent) | Lawful basis | V1: consent-based (consent token captured); V2: non-consent basis (acknowledgement only); consent refusal → manual officer lane | Doc21 UC-22 §4/§5.1 |
| UC-22 | Language availability | V1: selected language render; V2: pictogram flow + printed notice fallback | Doc21 UC-22 §5.2 |
| UC-32/PROC-24 (Kiosk Provisioning) | Provisioning mode | V1: initial site enrolment (TPM-bound identity); V2: re-enrolment after tamper/replacement (UC-29 path) | Doc31 PROC-24 card; Doc21 UC-29 |
| UC-28 (Signed OTA) | Rollout staging | V1: staged rings (cosign-verified, progressive); V2: rollback re-deploy of previous version (UC-31 path) | Doc21 UC-28, UC-30, UC-31 |
| CAP-11 (Offline/Failover) | Connectivity state | V1: online (direct crossing-event emission to SYS-02); V2: offline (signed store-and-forward queue, flush on reconnection) | Doc21 UC-20 §5.3, CAP-11 |
| UC-33 (Audit Export) | Requester variant | V1: scheduled internal export; V2: on-request authority export (SH-EXT-003, WORM STORE-04) | Doc21 §6.0 actor table |

### 4.3 AI model variants (PKG-11)

| Base UC | Variation Point | Variants | Binding |
|---|---|---|---|
| UC-30..CAP-12 model lifecycle | Model version source | V1: fresh training/retraining (PROC-25 release packaging); V2: rollback to retained previous version (UC-31) | Doc21 PROC-25 §1, UC-30 §4 |
| PROC-26 (Drift/Bias Review) | Disposition | V1: threshold tune (governed change); V2: retrain (PROC-25); V3: rollback (UC-31) | Doc21 UC-30..CAP-12 §4 disposition flow |
| UC-18/UC-19 thresholds | Governance-bound parameterisation | PAD/match/grey-band thresholds are governed artefacts under PROC-20 AI model change control | Doc21 UC-18 §9/§10 annex |

---

## 5. CONFIGURATION OPTIONS

*Placeholder for configuration matrix — to be bound at requirements allocation (Doc25).*

---

## 6. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-30 | Security Architect | Initial release — Use case variability for SecureBorder Solutions |
| 1.1 | 2026-09-05 | Executor (product-first restructure) | Added variability anchors in current id space: lane variants for PROC-01 (portal/email), PROC-03 (ENISA/CNPD paths), PROC-14 (DPIA/FRIA dual-output), PROC-07; product variants for U.C.8.x (kiosk vs assisted referral U.C.8.3.2), U.C.10.x provisioning modes; AI model variants (U.C.11.x, PROC-25/26). Sources: Doc21 v1.3 + Doc31 only. Metadata tables (§2) unchanged. |