---
document_id: AEGIS-P3-16
title: Compliance Gates Report
phase: 3
version: 1.0
created: 2026-04-28
updated: 2026-04-28
author: Compliance Lead
status: DRAFT
inputs: [15_Requirements_Allocation.md, 13_Use_Cases_Catalog.md, 11_Rules_Catalog.md]
outputs: [17_Functional_Tree.md, 22_Traceability_Matrix.xlsx]
traceability: AEGIS Class Model → ComplianceGate, GateStatus, VerificationMethod classes
related_documents: 15_Requirements_Allocation.md, 13_Use_Cases_Catalog.md, 00_COMMON/Taxonomy_Reference.md
case_id: CASE-03-OMNIBANK
complexity: Maximum (5 regulations, 38 sub-domains, 62 use cases, 28 nodes, 40 gates)
---

# Compliance Gates Report

**Case:** Case 03 — OmniBank Financial Systems (Maximum Complexity)
**Phase:** 3 — Decomposition & Risk Integration
**Step:** 6 — Compliance Gates Definition

---

## 1. DOCUMENT PURPOSE

This document defines the compliance gates that verify the implementation of the requirements allocation (Doc 15). Each gate represents a verification point where compliance with specific rules is assessed through defined verification methods.

Gates are organized by domain and track, with clear pass/fail criteria and remediation workflows for failures. The dual-loop workflow uses gates to determine when to iterate (incomplete) vs. when to proceed (complete).

---

## 2. GATE DEFINITION STRUCTURE

| Field | Type | Description |
|-------|------|-------------|
| **Gate ID** | string | Unique identifier: `GATE-{Domain}-{Number}` |
| **Gate Name** | string | Descriptive name |
| **Domain** | string | Security domain (D-01 to D-10) |
| **Rules Verified** | list | Rule IDs this gate verifies |
| **Node Verified** | string | Node ID that implements the rule |
| **Verification Method** | enum | TEST, INSPECT, DEMONSTRATE, ANALYZE |
| **Pass Criteria** | text | Specific criteria for gate pass |
| **Fail Criteria** | text | Specific criteria for gate fail |
| **Remediation** | text | Steps to remediate failure |
| **Gate Status** | enum | PASS, FAIL, IN_PROGRESS, NOT_APPLICABLE |

---

## 3. GATE SUMMARY

| Metric | Value |
|--------|-------|
| **Total Gates** | 40 |
| **Domain D-01** | 4 gates |
| **Domain D-02** | 4 gates |
| **Domain D-03** | 4 gates |
| **Domain D-04** | 4 gates |
| **Domain D-05** | 4 gates |
| **Domain D-06** | 4 gates |
| **Domain D-07** | 4 gates |
| **Domain D-08** | 3 gates |
| **Domain D-09** | 4 gates |
| **Domain D-10** | 5 gates |
| **Verification Methods** | TEST: 12, INSPECT: 15, DEMONSTRATE: 8, ANALYZE: 5 |
| **Initial Pass Rate** | 0% (gates not yet verified) |

---

## 4. GATE DEFINITIONS

### 4.1 D-01: Data Protection & Encryption

#### GATE-D-01-01: AES-256 Encryption at Rest

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-01-01 |
| **Gate Name** | AES-256 Encryption at Rest |
| **Domain** | D-01 |
| **Rules Verified** | CR-D-01.1-001, BPR-D-01.1-001 |
| **Node Verified** | NODE-D-01-01 |
| **UC Verified** | UC-02, UC-06 |
| **Verification Method** | TEST |
| **Pass Criteria** | AES-256 encryption confirmed on all personal/financial/AI data storage; field-level encryption confirmed for PII fields |
| **Fail Criteria** | Unencrypted data at rest found; PII fields without field-level encryption |
| **Remediation** | Enable encryption on storage systems; implement field-level encryption for PII |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-01-02: TLS 1.3 Enforcement

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-01-02 |
| **Gate Name** | TLS 1.3 Enforcement |
| **Domain** | D-01 |
| **Rules Verified** | CR-D-01.2-001, BPR-D-01.2-001 |
| **Node Verified** | NODE-D-01-01 |
| **UC Verified** | UC-03 |
| **Verification Method** | TEST |
| **Pass Criteria** | TLS 1.3 enforced on all internal/external/API communications; HSTS enabled; certificate pinning configured |
| **Fail Criteria** | TLS 1.2 or earlier detected; HSTS not enabled; weak cipher suites in use |
| **Remediation** | Upgrade to TLS 1.3; enable HSTS; configure certificate pinning |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-01-03: HSM Key Management

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-01-03 |
| **Gate Name** | HSM Key Management |
| **Domain** | D-01 |
| **Rules Verified** | CR-D-01.3-001, BPR-D-01.3-001 |
| **Node Verified** | NODE-D-01-01.1 |
| **UC Verified** | UC-04, UC-07 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | HSM-backed key lifecycle confirmed; FIPS 140-3 Level 3 validation; separate keys by classification |
| **Fail Criteria** | Keys not HSM-backed; FIPS validation expired; keys not separated by classification |
| **Remediation** | Migrate to HSM; renew FIPS validation; implement key classification |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-01-04: AI Model Integrity

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-01-04 |
| **Gate Name** | AI Model Integrity |
| **Domain** | D-01 |
| **Rules Verified** | CR-D-01.4-001, BPR-D-01.4-001 |
| **Node Verified** | NODE-D-01-01.2 |
| **UC Verified** | UC-05, UC-08 |
| **Verification Method** | TEST |
| **Pass Criteria** | Integrity checksums validated on every model load; versioning in place; unauthorized modifications detected |
| **Fail Criteria** | Models loaded without integrity check; version control missing; tampering not detected |
| **Remediation** | Implement integrity checksums; add model versioning; configure tampering alerts |
| **Gate Status** | NOT_APPLICABLE |

---

### 4.2 D-02: Vulnerability Management

#### GATE-D-02-01: Vulnerability Scanning

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-02-01 |
| **Gate Name** | Vulnerability Scanning |
| **Domain** | D-02 |
| **Rules Verified** | CR-D-02.1-001, BPR-D-02.1-001, BPR-D-02.3-001 |
| **Node Verified** | NODE-D-02-01 |
| **UC Verified** | UC-09, UC-14 |
| **Verification Method** | DEMONSTRATE |
| **Pass Criteria** | Weekly vulnerability scans executed; Critical/High findings remediated within 72h SLA |
| **Fail Criteria** | Scans not executed weekly; critical vulnerabilities exceed 72h remediation SLA |
| **Remediation** | Automate scan scheduling; prioritize critical remediation; escalate delays |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-02-02: Patch Management

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-02-02 |
| **Gate Name** | Patch Management |
| **Domain** | D-02 |
| **Rules Verified** | CR-D-02.2-001 |
| **Node Verified** | NODE-D-02-01.2 |
| **UC Verified** | UC-10 |
| **Verification Method** | TEST |
| **Pass Criteria** | Automated patch management operational; 72h SLA for critical vulnerabilities met |
| **Fail Criteria** | Patches not automated; critical patches exceed 72h |
| **Remediation** | Implement automated patching; establish SLA monitoring |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-02-03: Vulnerability Disclosure

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-02-03 |
| **Gate Name** | Vulnerability Disclosure |
| **Domain** | D-02 |
| **Rules Verified** | CR-D-02.3-001 |
| **Node Verified** | NODE-D-02-01 |
| **UC Verified** | UC-11 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | Coordinated vulnerability disclosure policy public; ENISA/CSIRT reporting within 24h confirmed |
| **Fail Criteria** | Policy not public; incident reporting exceeds 24h |
| **Remediation** | Publish disclosure policy; establish ENISA/CSIRT reporting channel |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-02-04: TLPT Execution

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-02-04 |
| **Gate Name** | Threat-Led Penetration Testing |
| **Domain** | D-02 |
| **Rules Verified** | CR-D-02.4-001, BPR-D-02.4-001, BPR-D-12.1-001 |
| **Node Verified** | NODE-D-02-02 |
| **UC Verified** | UC-12 |
| **Verification Method** | DEMONSTRATE |
| **Pass Criteria** | Annual TLPT per DORA RTS executed; AI bias testing completed; adversarial robustness validated |
| **Fail Criteria** | TLPT not executed annually; AI bias testing not performed; adversarial testing incomplete |
| **Remediation** | Schedule TLPT; include AI bias testing; conduct adversarial robustness validation |
| **Gate Status** | NOT_APPLICABLE |

---

### 4.3 D-03: Access Control

#### GATE-D-03-01: Identity Management

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-03-01 |
| **Gate Name** | Unified Identity Management |
| **Domain** | D-03 |
| **Rules Verified** | CR-D-03.1-001, BPR-D-03.1-001 |
| **Node Verified** | NODE-D-03-01 |
| **UC Verified** | UC-16, UC-20 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | Unified identity management operational; MFA enrolled for all users; HR integration for provisioning/deprovisioning |
| **Fail Criteria** | Identity management fragmented; users without MFA; HR integration not operational |
| **Remediation** | Consolidate identity management; enroll all users in MFA; implement HR integration |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-03-02: MFA Enforcement

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-03-02 |
| **Gate Name** | MFA Enforcement |
| **Domain** | D-03 |
| **Rules Verified** | CR-D-03.2-001, BPR-D-03.2-001 |
| **Node Verified** | NODE-D-03-01.1 |
| **UC Verified** | UC-17, UC-22 |
| **Verification Method** | TEST |
| **Pass Criteria** | MFA enforced for all privileged/remote/AI access; FIDO2 supported for phishing-resistant authentication |
| **Fail Criteria** | Privileged access without MFA; remote access without MFA; FIDO2 not supported |
| **Remediation** | Enforce MFA everywhere; implement FIDO2 |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-03-03: Least Privilege

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-03-03 |
| **Gate Name** | Least Privilege Enforcement |
| **Domain** | D-03 |
| **Rules Verified** | CR-D-03.3-001, BPR-D-03.3-001 |
| **Node Verified** | NODE-D-03-01.2 |
| **UC Verified** | UC-18, UC-18.1 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | Quarterly access reviews executed; least privilege applied; AI platform access reviewed |
| **Fail Criteria** | Access reviews not quarterly; excessive privileges granted; AI access not reviewed |
| **Remediation** | Implement quarterly reviews; reduce privileges; review AI access |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-03-04: Secure Configuration

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-03-04 |
| **Gate Name** | Secure Default Configuration |
| **Domain** | D-03 |
| **Rules Verified** | CR-D-03.4-001, BPR-D-03.4-001 |
| **Node Verified** | NODE-D-03-02 |
| **UC Verified** | UC-19 |
| **Verification Method** | TEST |
| **Pass Criteria** | CIS Benchmarks Level 2 applied; unused services/ports disabled; AI inference endpoints hardened |
| **Fail Criteria** | CIS compliance not verified; unused services enabled; AI endpoints not hardened |
| **Remediation** | Apply CIS benchmarks; disable unused services; harden AI endpoints |
| **Gate Status** | NOT_APPLICABLE |

---

### 4.4 D-04: Incident Response

#### GATE-D-04-01: SOC Operations

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-04-01 |
| **Gate Name** | 24/7 SOC Operations |
| **Domain** | D-04 |
| **Rules Verified** | CR-D-04.1-001, BPR-D-04.1-001, BPR-D-04.3-001 |
| **Node Verified** | NODE-D-04-01 |
| **UC Verified** | UC-23, UC-29 |
| **Verification Method** | DEMONSTRATE |
| **Pass Criteria** | 24/7 SOC coverage confirmed; AI anomaly detection operational; quarterly exercises executed |
| **Fail Criteria** | SOC not 24/7; AI anomaly detection not working; exercises not quarterly |
| **Remediation** | Ensure 24/7 coverage; fix AI detection; schedule exercises |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-04-02: Business Continuity

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-04-02 |
| **Gate Name** | Business Continuity & DR |
| **Domain** | D-04 |
| **Rules Verified** | CR-D-04.2-001, BPR-D-04.2-001, BPR-D-04.4-001 |
| **Node Verified** | NODE-D-04-02 |
| **UC Verified** | UC-24, UC-27 |
| **Verification Method** | DEMONSTRATE |
| **Pass Criteria** | 99.99% uptime SLA; RTO <= 4h; RPO <= 1h; AI system failover tested; backup verification quarterly |
| **Fail Criteria** | Uptime SLA not met; RTO/RPO exceeded; AI failover not tested; backup verification skipped |
| **Remediation** | Improve redundancy; test failover; verify backups |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-04-03: Universal Notification

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-04-03 |
| **Gate Name** | Universal Incident Notification |
| **Domain** | D-04 |
| **Rules Verified** | CR-D-04.3-001, BPR-D-04.3-001 |
| **Node Verified** | NODE-D-04-03, NODE-CS-01 |
| **UC Verified** | UC-25 (all specializations) |
| **Verification Method** | TEST |
| **Pass Criteria** | 24h universal notification workflow operational; DORA 4h initial met; GDPR 72h met; NIS 2/CRA 24h met; AI Act 15d met |
| **Fail Criteria** | Notification workflow not universal; regulatory SLAs missed |
| **Remediation** | Implement unified workflow; test notification routing |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-04-04: Backup Systems

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-04-04 |
| **Gate Name** | Redundant Backup Systems |
| **Domain** | D-04 |
| **Rules Verified** | CR-D-04.4-001 |
| **Node Verified** | NODE-D-04-02.1 |
| **UC Verified** | UC-26 |
| **Verification Method** | DEMONSTRATE |
| **Pass Criteria** | Redundant backups with automated failover; EU data center distribution; sovereignty controls |
| **Fail Criteria** | Backups not redundant; no failover; data sovereignty not ensured |
| **Remediation** | Implement redundant backups; configure failover; ensure EU data residency |
| **Gate Status** | NOT_APPLICABLE |

---

### 4.5 D-05: Data Lifecycle

#### GATE-D-05-01: Data Minimization

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-05-01 |
| **Gate Name** | Data Minimization |
| **Domain** | D-05 |
| **Rules Verified** | CR-D-05.1-001, BPR-D-05.1-001 |
| **Node Verified** | NODE-D-05-01, NODE-D-05-01.2 |
| **UC Verified** | UC-31, UC-35 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | Data minimization review annual; AI training data relevance/representativeness confirmed; bias proxies not present |
| **Fail Criteria** | Minimization review not annual; AI training data not relevant; bias proxies detected |
| **Remediation** | Conduct annual review; ensure data relevance; remove bias proxies |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-05-02: Retention Enforcement

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-05-02 |
| **Gate Name** | Tiered Retention Enforcement |
| **Domain** | D-05 |
| **Rules Verified** | CR-D-05.2-001 |
| **Node Verified** | NODE-D-05-01 |
| **UC Verified** | UC-32 |
| **Verification Method** | ANALYZE |
| **Pass Criteria** | 10-year retention for financial records (MiFID II); 5-year for operational; 6-month for AI logs; automated deletion on expiry |
| **Fail Criteria** | Retention periods not enforced; automated deletion not working |
| **Remediation** | Implement tiered retention; automate deletion |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-05-03: Cryptographic Erasure

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-05-03 |
| **Gate Name** | Cryptographic Sharding Erasure |
| **Domain** | D-05 |
| **Rules Verified** | CR-D-05.3-001, BPR-D-05.3-001 |
| **Node Verified** | NODE-D-05-01.1, NODE-CS-03 |
| **UC Verified** | UC-33 |
| **Verification Method** | TEST |
| **Pass Criteria** | Erasure completed within 30 days; cryptographic sharding operational; T-002 resolution confirmed (GDPR erasure + DORA logs) |
| **Fail Criteria** | Erasure exceeds 30 days; cryptographic sharding not implemented; T-002 conflict unresolved |
| **Remediation** | Implement crypto sharding; test erasure; verify T-002 resolution |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-05-04: Data Portability

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-05-04 |
| **Gate Name** | Data Export in Machine-Readable Format |
| **Domain** | D-05 |
| **Rules Verified** | CR-D-05.4-001, BPR-D-05.4-001 |
| **Node Verified** | NODE-D-05-01 |
| **UC Verified** | UC-34 |
| **Verification Method** | TEST |
| **Pass Criteria** | Data export within 30 days (GDPR SLA); machine-readable formats (JSON, CSV); AI decisions and credit factors included |
| **Fail Criteria** | Export exceeds 30 days; formats not machine-readable; AI data not included |
| **Remediation** | Automate export process; provide machine-readable formats; include AI data |
| **Gate Status** | NOT_APPLICABLE |

---

### 4.6 D-06: Supply Chain

#### GATE-D-06-01: Vendor Risk Management

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-06-01 |
| **Gate Name** | ICT Third-Party Risk Management |
| **Domain** | D-06 |
| **Rules Verified** | CR-D-06.1-001, BPR-D-06.1-001 |
| **Node Verified** | NODE-D-06-01 |
| **UC Verified** | UC-37, UC-41 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | Pre-engagement assessments completed; annual reassessments done; AI model providers assessed |
| **Fail Criteria** | Pre-engagement not done; annual reassessment missed; AI providers not assessed |
| **Remediation** | Implement pre-engagement assessment; schedule annual reassessments; assess AI providers |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-06-02: SBOM Management

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-06-02 |
| **Gate Name** | Software Bill of Materials |
| **Domain** | D-06 |
| **Rules Verified** | CR-D-06.2-001, BPR-D-02.2-001 |
| **Node Verified** | NODE-D-06-02 |
| **UC Verified** | UC-38 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | SBOM generated on every release; SPDX and CycloneDX formats; AI model dependencies included |
| **Fail Criteria** | SBOM not generated; formats not standard; AI dependencies missing |
| **Remediation** | Automate SBOM generation; use standard formats; include AI dependencies |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-06-03: Contractual Security

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-06-03 |
| **Gate Name** | Contractual Security Obligations |
| **Domain** | D-06 |
| **Rules Verified** | CR-D-06.3-001, BPR-D-06.3-001 |
| **Node Verified** | NODE-D-06-01 |
| **UC Verified** | UC-39 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | Security requirements in all contracts; audit rights included; 24h breach notification required; DPA clauses present |
| **Fail Criteria** | Security requirements missing; audit rights missing; breach notification SLA not in contract |
| **Remediation** | Update contract templates; include all security clauses |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-06-04: Concentration Risk

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-06-04 |
| **Gate Name** | Third-Party Concentration Risk |
| **Domain** | D-06 |
| **Rules Verified** | CR-D-06.4-001, BPR-D-06.4-001 |
| **Node Verified** | NODE-D-06-01 |
| **UC Verified** | UC-40 |
| **Verification Method** | ANALYZE |
| **Pass Criteria** | Exit strategies documented for critical vendors; alternative providers identified; data migration plans in place |
| **Fail Criteria** | Exit strategies not documented; no alternative providers; migration plans missing |
| **Remediation** | Document exit strategies; identify alternatives; create migration plans |
| **Gate Status** | NOT_APPLICABLE |

---

### 4.7 D-07: Secure Development

#### GATE-D-07-01: Secure-by-Design

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-07-01 |
| **Gate Name** | Privacy & Security by Design |
| **Domain** | D-07 |
| **Rules Verified** | CR-D-07.1-001, BPR-D-07.1-001 |
| **Node Verified** | NODE-D-07-01 |
| **UC Verified** | UC-42, UC-46 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | CRA secure-by-default standard applied; threat modeling in design; AI ethical design reviews conducted |
| **Fail Criteria** | Secure-by-default not followed; threat modeling skipped; AI ethics not reviewed |
| **Remediation** | Implement secure-by-default; add threat modeling; conduct AI ethics reviews |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-07-02: Secure Coding

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-07-02 |
| **Gate Name** | Secure Coding Standards |
| **Domain** | D-07 |
| **Rules Verified** | CR-D-07.2-001, BPR-D-07.2-001 |
| **Node Verified** | NODE-D-07-01.1 |
| **UC Verified** | UC-43, UC-43.1 |
| **Verification Method** | DEMONSTRATE |
| **Pass Criteria** | SAST/DAST on every commit; OWASP ASVS compliance; High/Critical findings block deployment |
| **Fail Criteria** | SAST/DAST not on every commit; ASVS compliance not verified; critical findings not blocking |
| **Remediation** | Integrate SAST/DAST; enforce ASVS; block on critical findings |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-07-03: CI/CD Security Gates

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-07-03 |
| **Gate Name** | CI/CD Pipeline Security |
| **Domain** | D-07 |
| **Rules Verified** | CR-D-07.3-001, BPR-D-07.3-001 |
| **Node Verified** | NODE-D-07-01.2 |
| **UC Verified** | UC-44, UC-44.1 |
| **Verification Method** | TEST |
| **Pass Criteria** | Security gates on every pipeline run; SAST/DAST/SCA/secrets/IaC all present; AI deployment gates with model signing and bias testing |
| **Fail Criteria** | Gates missing; scans not comprehensive; AI deployment not gated |
| **Remediation** | Add missing gates; enable all scans; implement AI deployment gates |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-07-04: Change Management

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-07-04 |
| **Gate Name** | Formal Change Management |
| **Domain** | D-07 |
| **Rules Verified** | CR-D-07.4-001, BPR-D-07.4-001 |
| **Node Verified** | NODE-D-07-01 |
| **UC Verified** | UC-45 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | Dual control approval; independent oversight; CAB involvement; AI model changes included |
| **Fail Criteria** | Single-person approvals; no oversight; AI changes bypass CAB |
| **Remediation** | Implement dual control; add oversight; include AI changes in CAB |
| **Gate Status** | NOT_APPLICABLE |

---

### 4.8 D-08: Human Factors

#### GATE-D-08-01: Security Awareness Training

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-08-01 |
| **Gate Name** | Security Awareness Training |
| **Domain** | D-08 |
| **Rules Verified** | CR-D-08.1-001, BPR-D-08.1-001 |
| **Node Verified** | NODE-D-08-01 |
| **UC Verified** | UC-48, UC-51 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | 95% annual training completion; role-specific modules; phishing simulations quarterly; AI ethics included |
| **Fail Criteria** | Completion below 95%; no role-specific content; phishing simulations not quarterly; AI ethics missing |
| **Remediation** | Track completion; add role-specific modules; schedule phishing tests; add AI ethics |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-08-02: Security Competence

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-08-02 |
| **Gate Name** | Role-Specific Security Competence |
| **Domain** | D-08 |
| **Rules Verified** | CR-D-08.2-001, BPR-D-08.2-001, BPR-D-12.3-001 |
| **Node Verified** | NODE-D-08-02 |
| **UC Verified** | UC-49, UC-49-AI |
| **Verification Method** | INSPECT |
| **Pass Criteria** | Mandatory certifications for privileged roles; AI human oversight procedures defined; competence tracked annually |
| **Fail Criteria** | Certifications not mandatory; AI oversight not defined; tracking not annual |
| **Remediation** | Make certifications mandatory; define AI oversight; implement tracking |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-08-03: Board Training

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-08-03 |
| **Gate Name** | Management Board Security Training |
| **Domain** | D-08 |
| **Rules Verified** | CR-D-08.3-001, BPR-D-08.3-001 |
| **Node Verified** | NODE-D-08-03 |
| **UC Verified** | UC-50 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | DORA/NIS 2 training completed within 60 days of appointment; quarterly ICT risk reporting established |
| **Fail Criteria** | Training not completed; reporting not quarterly |
| **Remediation** | Schedule training; establish reporting |
| **Gate Status** | NOT_APPLICABLE |

---

### 4.9 D-09: Governance & Documentation

#### GATE-D-09-01: Unified ISMS

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-09-01 |
| **Gate Name** | Unified ISMS |
| **Domain** | D-09 |
| **Rules Verified** | CR-D-09.1-001, BPR-D-09.1-001 |
| **Node Verified** | NODE-D-09-01 |
| **UC Verified** | UC-52 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | ISMS covers all 5 regulatory frameworks; AI governance included; documentation retained 10+ years |
| **Fail Criteria** | ISMS not unified; frameworks missing; AI governance not included; retention too short |
| **Remediation** | Unify ISMS; add missing frameworks; include AI governance; extend retention |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-09-02: IPSARA Assessment

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-09-02 |
| **Gate Name** | IPSARA Unified Risk Assessment |
| **Domain** | D-09 |
| **Rules Verified** | CR-D-09.2-001, BPR-D-09.2-001, BPR-D-09.3-001 |
| **Node Verified** | NODE-D-09-01.1 |
| **UC Verified** | UC-53, UC-53.1, UC-53.2 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | IPSARA combines DPIA/FRIA/cybersecurity/ICT risk; new systems assessed before go-live; AI-specific risks quarterly |
| **Fail Criteria** | Assessments not unified; new systems go live without assessment; AI risks not quarterly |
| **Remediation** | Unify assessments; assess before go-live; quarterly AI risk reviews |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-09-03: Asset Inventory

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-09-03 |
| **Gate Name** | Comprehensive Asset Inventory |
| **Domain** | D-09 |
| **Rules Verified** | CR-D-09.3-001 |
| **Node Verified** | NODE-D-09-01 |
| **UC Verified** | UC-54 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | Automated discovery operational; AI models/training data/endpoints/inference in inventory; monthly reconciliation |
| **Fail Criteria** | Discovery not automated; AI assets missing; reconciliation not monthly |
| **Remediation** | Implement automated discovery; include AI assets; monthly reconcile |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-09-04: AI Traceability Documentation

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-09-04 |
| **Gate Name** | AI Governance Documentation |
| **Domain** | D-09 |
| **Rules Verified** | CR-D-09.4-001, BPR-D-09.4-001 |
| **Node Verified** | NODE-D-09-01.2 |
| **UC Verified** | UC-55, UC-55.1 |
| **Verification Method** | INSPECT |
| **Pass Criteria** | Model cards updated on every release; AI decision logs retained; IEEE 7000 transparency reports published |
| **Fail Criteria** | Model cards not updated; decision logs missing; transparency reports not published |
| **Remediation** | Update model cards; retain decision logs; publish transparency reports |
| **Gate Status** | NOT_APPLICABLE |

---

### 4.10 D-10: Monitoring & Audit

#### GATE-D-10-01: AI-Powered Threat Detection

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-10-01 |
| **Gate Name** | 24/7 AI-Powered Monitoring |
| **Domain** | D-10 |
| **Rules Verified** | CR-D-10.1-001, BPR-D-10.1-001, BPR-D-12.2-001 |
| **Node Verified** | NODE-D-10-01 |
| **UC Verified** | UC-57, UC-61 |
| **Verification Method** | TEST |
| **Pass Criteria** | 24/7 monitoring operational; AI threat detection calibrated monthly; anomalies escalated within 5 minutes |
| **Fail Criteria** | Monitoring not 24/7; AI detection not calibrated; escalation too slow |
| **Remediation** | Ensure 24/7 coverage; calibrate AI detection; improve escalation |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-10-02: Immutable Audit Logs

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-10-02 |
| **Gate Name** | Immutable Audit Logs |
| **Domain** | D-10 |
| **Rules Verified** | CR-D-10.2-001, BPR-D-10.2-001 |
| **Node Verified** | NODE-D-10-02, NODE-CS-03 |
| **UC Verified** | UC-58 |
| **Verification Method** | ANALYZE |
| **Pass Criteria** | Immutable logs confirmed; PII separation with access controls; cryptographic sharding for integrity; 5-year retention (financial), 6-month (AI inference) |
| **Fail Criteria** | Logs mutable; PII not separated; crypto sharding not implemented; retention not met |
| **Remediation** | Make logs immutable; separate PII; implement crypto sharding; ensure retention |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-10-03: AI Model Drift Detection

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-10-03 |
| **Gate Name** | AI Model Performance Monitoring |
| **Domain** | D-10 |
| **Rules Verified** | BPR-D-12.2-001, CR-D-10.1-001 |
| **Node Verified** | NODE-D-10-01.1 |
| **UC Verified** | UC-61 |
| **Verification Method** | ANALYZE |
| **Pass Criteria** | Drift detection hourly; automated retraining triggered within 4h of threshold breach; rollback procedures tested |
| **Fail Criteria** | Drift detection not hourly; automated retraining not triggered; rollback not tested |
| **Remediation** | Implement hourly drift detection; automate retraining triggers; test rollback |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-10-04: Penetration Testing

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-10-04 |
| **Gate Name** | Annual Penetration Testing |
| **Domain** | D-10 |
| **Rules Verified** | CR-D-10.3-001, BPR-D-10.3-001 |
| **Node Verified** | NODE-D-02-02 |
| **UC Verified** | UC-59 |
| **Verification Method** | DEMONSTRATE |
| **Pass Criteria** | Annual pentest executed; red team for AI systems; adversarial robustness testing; findings remediated within 30 days |
| **Fail Criteria** | Pentest not annual; red team not for AI; adversarial testing missing; remediation too slow |
| **Remediation** | Schedule annual pentest; include AI red team; add adversarial testing; speed remediation |
| **Gate Status** | NOT_APPLICABLE |

---

#### GATE-D-10-05: AI Adversarial Robustness

| Field | Value |
|-------|-------|
| **Gate ID** | GATE-D-10-05 |
| **Gate Name** | AI Adversarial Robustness Testing |
| **Domain** | D-10 |
| **Rules Verified** | BPR-D-12.4-001, CR-D-02.4-001 |
| **Node Verified** | NODE-D-02-01.1 |
| **UC Verified** | UC-60 |
| **Verification Method** | DEMONSTRATE |
| **Pass Criteria** | Quarterly adversarial testing per MITRE ATLAS; data poisoning/model evasion/model inversion tested; critical vulnerabilities remediated within 30 days |
| **Fail Criteria** | Testing not quarterly; attack types missing; remediation too slow |
| **Remediation** | Schedule quarterly tests; cover all attack types; speed remediation |
| **Gate Status** | NOT_APPLICABLE |

---

## 5. GATE STATUS SUMMARY

| Domain | Pass | Fail | In Progress | Not Applicable | Total |
|--------|------|------|-------------|----------------|-------|
| D-01 | 0 | 0 | 0 | 4 | 4 |
| D-02 | 0 | 0 | 0 | 4 | 4 |
| D-03 | 0 | 0 | 0 | 4 | 4 |
| D-04 | 0 | 0 | 0 | 4 | 4 |
| D-05 | 0 | 0 | 0 | 4 | 4 |
| D-06 | 0 | 0 | 0 | 4 | 4 |
| D-07 | 0 | 0 | 0 | 4 | 4 |
| D-08 | 0 | 0 | 0 | 3 | 3 |
| D-09 | 0 | 0 | 0 | 4 | 4 |
| D-10 | 0 | 0 | 0 | 5 | 5 |
| **TOTAL** | **0** | **0** | **0** | **40** | **40** |

---

## 6. REMEDIATION WORKFLOW

### 6.1 Gate Failure Protocol

```
1. Gate FAIL detected
2. Notify responsible party (Node owner)
3. Create remediation ticket
4. Execute remediation within SLA:
   - CRITICAL gates: 7 days
   - HIGH gates: 14 days
   - MEDIUM gates: 30 days
   - LOW gates: 90 days
5. Re-verify gate
6. If PASS → Update gate status
7. If FAIL → Escalate to CISO
```

---

## 7. STOP CONDITION VERIFICATION — ALL SC

| SC | Description | Gates Verified | Status |
|----|-------------|---------------|--------|
| SC1 | Rule Coverage — Every rule maps to ≥1 UC | All 63 rules via gates | ✅ PASS |
| SC2 | Relationship Completeness — All UCs have relationships | 48 relationships defined | ✅ PASS |
| SC3 | Detail Sufficiency — Complex UCs (NI=3) have detailed flows | Pending Iteration 2 | IN_PROGRESS |
| SC4 | Variability Complete — All regulation-specific scenarios covered | 14 specializations defined | ✅ PASS |
| SC5 | Risk Residual — All risks acceptable | Pending Risk Cycle | PENDING |

---

## 8. NEXT STEPS

1. **Functional Tree (Doc 17)** — Define functional decomposition
2. **Functional Requirements (Doc 23)** — Derive FRs from gates and nodes
3. **Non-Functional Requirements (Doc 24)** — Derive NFRs from gates and nodes
4. **Risk Analysis (Doc 25)** — Execute Risk Cycle to verify SC5

---

## 9. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-28 | Compliance Lead | Initial creation — 40 compliance gates across 10 domains |

---

## 10. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Compliance Lead | [TBD] | | |
| CISO | [TBD] | | |
| Data Protection Officer | [TBD] | | |
| AI Governance Lead | [TBD] | | |

---

**Next Step:** Proceed to 17_Functional_Tree.md to define functional decomposition.