---
document_id: AEGIS-P3-13a
title: 13a Use Case Relationships
phase: 3
version: 1.1
created: 2026-04-30
updated: 2026-09-05
author: Security Architect
status: DRAFT
case: Case_02_SecureBorder_Solutions
inputs: [Doc21_Use_Cases_Catalog.md]
outputs: [Doc23_Use_Case_Variability.md, Doc24_Architectural_Nodes.md]
traceability: AEGIS Class Model → UseCaseRelationship, Package classes
related_documents: [Doc21_Use_Cases_Catalog.md, Doc23_Use_Case_Variability.md, Doc31_Process_Capability_Cards.md]
---

# 13a Use Case Relationships — SecureBorder Solutions

**Case:** Case 02 — SecureBorder Solutions (Border Control / Physical Security)
**Phase:** 3 — Use Case Relationships
**Company Profile:** Medium-Large (450 employees), B2G/B2B, GDPR+CRA+NIS2+AI_Act

---

## 1. DOCUMENT PURPOSE

This document defines the structural relationships between use cases in the
SecureBorder Solutions system. Sources: `Doc21_Use_Cases_Catalog.md` v1.3 (catalogue,
73 UCs) and `Doc31_Process_Capability_Cards.md` (lane cards + articulation table).
No relationship below is invented; each is attested in one of those two documents.

**Current ID space (post product-first restructure, see LANE_NAMING_CENSUS_v0.md):**
- **Compliance lane (UC-01..UC-15):** 47 UCs — data-subject rights, security operations,
  identity/access, secure development, governance, AI compliance, training. Re-laned
  ids now use PROC-01..22 and CAP-01..10 (formerly U.C.x.y.1).
- **Product lane (UC-16..UC-36, PKG-8..12):** 26 UCs — the GuardianGate eGate product
  modelled as actor-goal use cases (§6 of Doc21).
- **TOTAL: 73 UCs** (T36/P27/C10 in the catalogue; 63 controls: 38 CR + 25 BPR).
- **Lane cards:** PROC-01..27 (process lane) and CAP-01..10 (capability lane),
  companion cards in Doc31.

---

## 2. PACKAGE STRUCTURE

### 2.1 Package Overview (current space, Doc21 §6 + §7/§9)

| Package ID | Package Name | Purpose | UC Count | Related Lanes |
|------------|--------------|---------|----------|----------------|
| UC-01..UC-15 | Compliance use cases (lane-renamed) | Security & privacy obligations realisation (data subject rights, security ops, IAM, secure dev, governance, AI compliance, training) | 47 | PROC-01..22, CAP-01..10 |
| PKG-8 | Traveller eGate Journey | Document scan, biometric capture/liveness/match, gate decision, referral, privacy notice | 7 | PROC-05, PROC-01 |
| PKG-9 | Operator Referral Desk | Console session, queue triage, manual verification/override, incident flag, shift handover | 5 | PROC-05, PROC-06, PROC-23 |
| PKG-10 | Kiosk Fleet Operations | Provisioning, health monitoring, OTA, tamper response, offline failover | 5 | PROC-24, PROC-08, CAP-02 |
| PKG-11 | AI Model Lifecycle | Training/packaging, signed rollout, rollback, drift/bias review, watchlist sync | 5 | PROC-25, PROC-26, PROC-20 |
| PKG-12 | Administration & Reporting | Kiosk admin config, audit export, SLA dashboard, user/role administration | 4 | PROC-27, PROC-18 |
| **TOTAL** | **6 packages (1 compliance + 5 product)** | | **73 UCs** | PROC-01..27, CAP-01..10 |

**Status:** ✅ Mapped to 73 use cases (47 compliance + 26 product) across the current
id space. Legacy PKG-DP/SEC/IAM/DEV/GOV/AI/TRN package naming is retired; see the
census (`00_METHODOLOGY/validation/LANE_NAMING_CENSUS_v0.md`, Case_02 section) for
per-id mappings.

### 2.2 Lane cards (Doc31, NIST SP 800-218 practice shape)

| Lane | IDs | Anchor cards |
|------|-----|--------------|
| PROCESS | PROC-01..27 | PROC-05 (incident detection & triage), PROC-14 (unified DPIA+FRIA), PROC-26 (drift/bias review) |
| CAPABILITY | CAP-01..10 | CAP-02 (continuous security monitoring), CAP-06 (security awareness training) |

Traceability chain per Doc31: **RULE → CAP → PROC → UC**.

---

## 3. RELATIONSHIP MODEL

### 3.1 Product journey — include/extend/precede (PKG-8)

Sequencing is `«precede»` (the upstream use case must complete before the downstream
starts); optional paths are `«extend»`.

| Relationship | Type | Source |
|---|---|---|
| UC-16 (Scan Travel Document) «precede» UC-17 (Capture Facial Biometric Sample) — chip portrait is the match reference | precede | Doc21 UC-17 preconditions |
| UC-17 «precede» UC-18 (Liveness/PAD) | precede | Doc21 UC-18 preconditions |
| UC-18 «precede» UC-19 (Face Match 1:1) | precede | Doc21 UC-19 preconditions |
| UC-19 «precede» UC-20 (Gate Decision & Release) | precede | Doc21 UC-20 preconditions |
| UC-22 (Privacy Notice & Consent) «extend» UC-16 — same trigger, first interaction screen; runs before biometric processing | extend | Doc21 UC-22 |
| UC-16/UC-17/UC-18/UC-19/UC-20 «extend» UC-21 (Referral to Operator Desk) on any failure/grey-band/watchlist path | extend | Doc21 UC-21 preconditions |
| UC-20 «include» offline store-and-forward per PKG-10 failover when SYS-02 unreachable | include | Doc21 UC-20 §5.3/§6.2 |
| UC-22 «extend» manual officer lane on consent refusal (travel right preserved) | extend | Doc21 UC-22 §5.1 |

### 3.2 Referral → security operations chain

| Relationship | Type | Source |
|---|---|---|
| UC-21 (Referral) → PROC-05 (Incident Detection & Triage) on confirmed impostor / suspected attack | include | Doc21 UC-21 §5.2, §10 annex; Doc31 PROC-05 card |
| PROC-05 «precede» PROC-06 (Incident Response & Containment) on escalation | precede | Doc31 PROC-05 card (step 3b) |
| UC-16/UC-18 failure paths «include» PROC-05 security event raise (event pipeline, CR-D-04.1-001) | include | Doc21 UC-16 §6.2, UC-18 §5.1 |
| UC-26 (Incident Flag & Gate Lock) «include» PROC-05 triage; SOC clearance releases the lock | include | Doc21 UC-26 §4 |
| PROC-06 containment «precede» PROC-07 (Regulatory Notification 24h/72h) when reportable | precede | Doc31 CAP-02 card (contributes chain) |
| UC-25 confirmed impostor «include» PROC-05 + PROC-07 (if reportable) | include | Doc21 UC-25 §5.2 |

### 3.3 Operator flows (PKG-9)

| Relationship | Type | Source |
|---|---|---|
| UC-23 (Console Session, SSO/FIDO2 fail-closed) «precede» UC-24 (Queue Handling & Triage) | precede | Doc21 UC-24 preconditions |
| UC-24 «precede» UC-25 (Manual Verification & Override) | precede | Doc21 UC-25 preconditions |
| UC-21 «include» UC-23..UC-25 — the desk workflow realises the referral | include | Doc21 UC-23 annex (constrained-by UC-21) |
| UC-25 override «include» step-up re-authentication per UC-23 §6.2 | include | Doc21 UC-25 §5.1 |
| UC-26 (Flag & Lock) «extend» UC-24 on attack-pattern work items | extend | Doc21 UC-26 preconditions |
| PROC-23 (Shift Handover & Referral Report) «extend» UC-24 at shift end | extend | Doc21 PKG-9 table; Doc31 PROC-23 card |

### 3.4 Fleet operations (PKG-10)

| Relationship | Type | Source |
|---|---|---|
| PROC-24 (Kiosk Provisioning & Enrolment) «precede» UC-27 (Fleet Health Monitoring) | precede | Doc21 UC-28 §3 (units enrolled + healthy) |
| UC-27 «precede» UC-28 (Signed OTA Firmware Update) — target units must be healthy | precede | Doc21 UC-28 §3 |
| UC-27 tamper indicators «extend» UC-29 (Tamper Alert Response) | extend | Doc21 UC-27 §4 |
| UC-29 «include» PROC-05 (detection/triage) and PROC-06 (containment incl. firmware quarantine) | include | Doc21 UC-29 §10 annex |
| UC-27 offline state «extend» UC-30 (Offline/Failover store-and-forward) | extend | Doc21 UC-30 §1 |
| UC-30 «include» PROC-08 (DR & business continuity) discipline | include | Doc21 UC-30 §10 annex |

### 3.5 AI lifecycle (PKG-11)

| Relationship | Type | Source |
|---|---|---|
| PROC-25 (Model Training & Release Packaging) «precede» UC-31 (Signed Model Rollout) | precede | Doc21 PROC-25 §1 (candidate becomes eligible for rollout) |
| UC-31 «precede» UC-32 (Model Rollback arming — previous version retained) | precede | Doc21 UC-31 §4 |
| PROC-26 (Drift/Bias Monitoring & Review, formerly U.C.11.4.1) «extend» UC-27 — consumes fleet telemetry | extend | Doc21 UC-31..UC-33 drift flow (fleet telemetry precondition) |
| PROC-26 disposition «extend» PROC-25 (retrain) or UC-32 (rollback) | extend | Doc21 UC-31..UC-33 §4 (disposition: tune / retrain / rollback) |
| PROC-26 human bias review «include» PROC-20 (AI Bias Testing & Fairness) — fairness assessment basis | include | Doc31 PROC-26 card; Doc31 CAP-02 span |
| UC-33 (Watchlist Cache Sync) «include» UC-20 — watchlist status is a gate decision input | include | Doc21 UC-20 §4 (watchlist input) |

### 3.6 Administration & reporting (PKG-12)

| Relationship | Type | Source |
|---|---|---|
| UC-34 (Kiosk Admin Configuration, dual control) «precede» fleet serving — baseline config before enrolment | precede | Doc21 UC-34 §1 |
| UC-34 drift alerts «extend» UC-27 | extend | Doc21 UC-34 §4 |
| UC-35 (Audit Export for Authorities) «extend» PROC-18 (Regulatory Notification & Cooperation) — evidence export on authority request | extend | Doc21 §6.0 (SH-EXT-003 requests audit evidence exports) |
| UC-36 (SLA & Fleet Status Dashboard) «include» UC-24 queue telemetry, UC-27 fleet telemetry, UC-30 offline windows | include | Doc21 UC-24 §6.2, UC-27 §4, UC-30 §4 |
| PROC-27 (User/Role Administration for Console) «precede» UC-23 — officer roles/entitlements before console session | precede | Doc21 UC-23 §2.4 (Ops administers via PROC-27) |

### 3.7 Compliance-side relationships (lane ids post-rename)

The pre-existing compliance relationships (UC-01..UC-15, now PROC-/CAP-renamed where
re-laned) remain as recorded in Doc21 §7/§9 and Doc31 cards:

| Relationship | Type | Source |
|---|---|---|
| PROC-01 (DSAR) «precede» PROC-02 (Data Portability Export) | precede | Doc31 PROC-01/PROC-02 cards |
| PROC-01/PROC-02/PROC-04 (Minimisation Review) constrained by CAP-01 (RoPA Maintenance) | constrain | Doc31 PROC-01 card, CAP-01 card |
| PROC-03 (Biometric Breach Notification) «include» PROC-07 (unified 24h/72h notification) | include | Doc31 PROC-03/PROC-07 cards |
| PROC-14 (Unified Impact Assessment DPIA+FRIA) «precede» PROC-19 (AI Conformity Assessment) evidence — dual GDPR Art. 35(7) / AI Act Art. 27 outputs | precede | Doc31 PROC-14 card |
| PROC-19 «precede» PROC-20 (AI Bias Testing); PROC-22 (AI Adversarial Testing) «extend» PROC-20 | precede/extend | Doc31 PROC-19/PROC-20/PROC-22 cards |
| PROC-05/PROC-06/PROC-18 (Regulatory Notification & Cooperation) contribute to CAP-02 (Continuous Security Monitoring) | contribute | Doc31 CAP-02 card |
| CAP-06 (Security Awareness Training) «include» CAP-07 (Role-Specific Training) and CAP-10 (Phishing Simulation) | include | Doc31 CAP-06 card |
| CAP-08 (AI Competence Training) «extend» CAP-06 for AI-facing roles | extend | Doc31 CAP-08 card |
| PROC-12 (Secure Code Review) «include» PROC-13 (Change Management) via CI/CD gates | include | Doc31 PROC-12/PROC-13 cards |
| PROC-16 (Compliance Audit & Reporting) «include» PROC-17 (Vendor Risk Assessment) evidence for supplier audits | include | Doc31 PROC-16/PROC-17 cards |

---

## 4. TRACEABILITY TO DOMAINS

Per Doc31 (RULE → CAP → PROC → UC) and Doc21 §10 (UC to business goals):

| Package / Lane | Business Goals (Doc21 §4) | Sub-Domains (indicative) |
|---|---|---|
| PKG-8 | BG-004, BG-006 | D-01.1–D-01.4, D-03.4, D-05.x |
| PKG-9 | BG-001, BG-003 | D-03.1–D-03.3, D-04.1, D-10.2 |
| PKG-10 | BG-003, BG-005 | D-02.2, D-04.4, D-10.1 |
| PKG-11 | BG-002, BG-004, BG-006 | D-09.2, D-10.1, D-10.2 |
| PKG-12 | BG-003, BG-007 | D-09.3, D-09.4, D-10.2 |
| PROC-01..22 / CAP-01..10 | BG-001..BG-007 | per Doc31 card "Realises" fields (63 rules: 38 CR + 25 BPR) |

---

## 5. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-30 | Security Architect | Initial release — use case relationships (stale 84-UC package view; retired) |
| 1.1 | 2026-09-05 | Executor (product-first restructure) | Rewritten against current id space: 73 UCs (47 compliance U.C.1–7 lane-renamed + 26 product U.C.8–12 / PKG-8..12); replaced PKG-DP/SEC/IAM/DEV/GOV/TRN with PKG-7..12 and PROC-/CAP- lane equivalents; added include/extend/precede model for the product journey (eGate sequence, referral → PROC-05 → PROC-06, operator/fleet/AI/admin flows) and compliance-side lane relationships. Sources: Doc21 v1.3 + Doc31 only. |
