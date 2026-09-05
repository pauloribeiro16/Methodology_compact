---
document_id: AEGIS-P3-24
title: Non-Functional Requirements
phase: 3
version: 1.0
created: 2026-04-28
updated: 2026-04-28
author: Security Architect
status: DRAFT
inputs: [17_Functional_Tree.md, 15_Requirements_Allocation.md, 13_Use_Cases_Catalog.md]
outputs: [22_Traceability_Matrix.xlsx]
traceability: AEGIS Class Model → NonFunctionalRequirement, NFRCategory, MeasurabilityCriterion classes
related_documents: 17_Functional_Tree.md, 23_Functional_Requirements.md, 15_Requirements_Allocation.md
case_id: CASE-03-OMNIBANK
case: Case_03_OmniBank_Financial
complexity: Maximum (5 regulations, 38 sub-domains, 62 use cases, 56 NFRs)
---

# Non-Functional Requirements

**Case:** Case 03 — OmniBank Financial Systems (Maximum Complexity)
**Phase:** 3 — Decomposition & Risk Integration
**Step:** 9 — Non-Functional Requirements Derivation

---

## 1. DOCUMENT PURPOSE

This document defines the Non-Functional Requirements (NFRs) derived from the Use Cases Catalog (Doc 13) and the Functional Tree (Doc 17). NFRs are measurable qualities that the system must exhibit, organized by six categories: Confidentiality, Integrity, Availability, Privacy, Accountability, and Compliance.

Every NFR includes:
1. **Metric** — What is measured
2. **Target** — Expected value
3. **Method** — How to measure (TEST, INSPECT, DEMONSTRATE, ANALYZE)

---

## 2. NFR DEFINITION STRUCTURE

| Field | Type | Description |
|-------|------|-------------|
| **NFR ID** | string | Unique identifier: `NFR-{Category}-{Number}` |
| **NFR Description** | text | Quality attribute statement |
| **Category** | enum | CONF, INT, AVAIL, PRIV, ACC, COMP |
| **Metric** | string | What is measured |
| **Target** | string | Expected value |
| **Method** | enum | TEST, INSPECT, DEMONSTRATE, ANALYZE |
| **Source UC** | string | UC that generates this NFR |
| **Source Rule** | string | Compliance rule this NFR satisfies |
| **Priority** | enum | CRITICAL, HIGH, MEDIUM, LOW |

---

## 3. NFR SUMMARY

| Metric | Value |
|--------|-------|
| **Total NFRs** | 56 |
| **Confidentiality (CONF)** | 12 NFRs |
| **Integrity (INT)** | 10 NFRs |
| **Availability (AVAIL)** | 12 NFRs |
| **Privacy (PRIV)** | 10 NFRs |
| **Accountability (ACC)** | 6 NFRs |
| **Compliance (COMP)** | 6 NFRs |
| **Measurability** | 100% (all NFRs have metric + target + method) |
| **Priority Distribution** | CRITICAL: 22, HIGH: 20, MEDIUM: 10, LOW: 4 |

---

## 4. NON-FUNCTIONAL REQUIREMENTS BY CATEGORY

### 4.1 NFR-CONF: Confidentiality (12 NFRs)

#### NFR-01: Data at Rest Encryption

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-01 |
| **NFR Description** | All personal, financial, and AI training data SHALL be encrypted at rest using AES-256 or stronger |
| **Category** | CONF |
| **Metric** | Encryption coverage percentage |
| **Target** | 100% of applicable data encrypted |
| **Method** | TEST |
| **Source UC** | PROC-39, PROC-41 |
| **Source Rule** | CR-D-01.1-001 |
| **Priority** | CRITICAL |

---

#### NFR-02: Field-Level PII Encryption

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-02 |
| **NFR Description** | PII fields and AI training datasets SHALL have field-level encryption applied |
| **Category** | CONF |
| **Metric** | PII fields encrypted percentage |
| **Target** | 100% of PII fields encrypted |
| **Method** | TEST |
| **Source UC** | PROC-41 |
| **Source Rule** | CR-D-01.1-001 |
| **Priority** | CRITICAL |

---

#### NFR-03: Data in Transit Encryption

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-03 |
| **NFR Description** | All data in transit SHALL be encrypted using TLS 1.3 with HSTS and certificate pinning |
| **Category** | CONF |
| **Metric** | TLS 1.3 enforcement percentage |
| **Target** | 100% of communications use TLS 1.3 |
| **Method** | TEST |
| **Source UC** | PROC-40 |
| **Source Rule** | CR-D-01.2-001 |
| **Priority** | CRITICAL |

---

#### NFR-04: HSM Key Protection

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-04 |
| **NFR Description** | Cryptographic keys SHALL be protected by FIPS 140-3 Level 3 validated HSM |
| **Category** | CONF |
| **Metric** | HSM validation status |
| **Target** | FIPS 140-3 Level 3 validation current |
| **Method** | INSPECT |
| **Source UC** | PROC-02, PROC-04 |
| **Source Rule** | CR-D-01.3-001, BPR-D-01.3-001 |
| **Priority** | CRITICAL |

---

#### NFR-05: AI Model Integrity Protection

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-05 |
| **NFR Description** | AI model artifacts SHALL be protected against unauthorized modification and tampering |
| **Category** | CONF |
| **Metric** | Model integrity validation rate |
| **Target** | 100% of model loads validated |
| **Method** | TEST |
| **Source UC** | PROC-03, CAP-08 |
| **Source Rule** | CR-D-01.4-001 |
| **Priority** | HIGH |

---

#### NFR-06: Privileged Access MFA

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-06 |
| **NFR Description** | All privileged access SHALL require MFA with phishing-resistant authentication |
| **Category** | CONF |
| **Metric** | Privileged access MFA coverage |
| **Target** | 100% of privileged sessions authenticated |
| **Method** | TEST |
| **Source UC** | PROC-43, PROC-45 |
| **Source Rule** | CR-D-03.2-001 |
| **Priority** | CRITICAL |

---

#### NFR-07: Least Privilege Enforcement

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-07 |
| **NFR Description** | System SHALL enforce least privilege with access granted only to minimum required resources |
| **Category** | CONF |
| **Metric** | Quarterly access review completion rate |
| **Target** | 100% of roles reviewed quarterly |
| **Method** | INSPECT |
| **Source UC** | PROC-11, PROC-11.1 |
| **Source Rule** | CR-D-03.3-001 |
| **Priority** | HIGH |

---

#### NFR-08: Immutable Audit Logs

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-08 |
| **NFR Description** | Audit logs SHALL be immutable and protected against tampering or deletion |
| **Category** | CONF |
| **Metric** | Log immutability verification |
| **Target** | 100% of logs cryptographically protected |
| **Method** | ANALYZE |
| **Source UC** | CAP-10 |
| **Source Rule** | CR-D-10.2-001 |
| **Priority** | CRITICAL |

---

#### NFR-09: PII Data Separation

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-09 |
| **NFR Description** | PII-bearing logs SHALL be separated from general logs with access controls |
| **Category** | CONF |
| **Metric** | PII separation and access control coverage |
| **Target** | 100% of PII logs separated and access-controlled |
| **Method** | INSPECT |
| **Source UC** | CAP-10 |
| **Source Rule** | CR-D-10.2-001 |
| **Priority** | CRITICAL |

---

#### NFR-10: AI Training Data Confidentiality

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-10 |
| **NFR Description** | AI training data SHALL be protected against unauthorized access and exfiltration |
| **Category** | CONF |
| **Metric** | Training data access control coverage |
| **Target** | 100% of training data access controlled and logged |
| **Method** | INSPECT |
| **Source UC** | PROC-44, PROC-20 |
| **Source Rule** | CR-D-05.1-001 |
| **Priority** | HIGH |

---

#### NFR-11: Vendor Data Protection

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-11 |
| **NFR Description** | Third-party data processing agreements SHALL include adequate data protection requirements |
| **Category** | CONF |
| **Metric** | Vendor DPA coverage percentage |
| **Target** | 100% of third-party processors with DPAs |
| **Method** | INSPECT |
| **Source UC** | PROC-25, PROC-26 |
| **Source Rule** | CR-D-06.3-001 |
| **Priority** | HIGH |

---

#### NFR-12: Cryptographic Sharding Separation

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-12 |
| **NFR Description** | Cryptographic sharding SHALL separate PII encryption keys from audit log integrity keys |
| **Category** | CONF |
| **Metric** | Key segregation verification |
| **Target** | 100% key segregation between PII and log integrity |
| **Method** | INSPECT |
| **Source UC** | UC-01, CAP-10 |
| **Source Rule** | CR-D-05.3-001, CR-D-10.2-001 |
| **Priority** | CRITICAL |

---

### 4.2 NFR-INT: Integrity (10 NFRs)

#### NFR-01: Vulnerability Remediation SLA

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-01 |
| **NFR Description** | Critical vulnerabilities SHALL be remediated within 72-hour SLA |
| **Category** | INT |
| **Metric** | Critical vulnerability remediation time |
| **Target** | ≤72 hours from identification to remediation |
| **Method** | ANALYZE |
| **Source UC** | PROC-05, PROC-06 |
| **Source Rule** | CR-D-02.1-001, CR-D-02.2-001 |
| **Priority** | CRITICAL |

---

#### NFR-02: Automated Patch Integrity

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-02 |
| **NFR Description** | Patches SHALL be validated for authenticity before deployment |
| **Category** | INT |
| **Metric** | Patch validation coverage |
| **Target** | 100% of patches validated before deployment |
| **Method** | TEST |
| **Source UC** | PROC-06 |
| **Source Rule** | CR-D-02.2-001 |
| **Priority** | HIGH |

---

#### NFR-03: AI Model Checksum Validation

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-03 |
| **NFR Description** | AI models SHALL be validated using cryptographic checksums on every load |
| **Category** | INT |
| **Metric** | Model checksum validation rate |
| **Target** | 100% of model loads validated |
| **Method** | TEST |
| **Source UC** | PROC-03, CAP-08 |
| **Source Rule** | CR-D-01.4-001 |
| **Priority** | HIGH |

---

#### NFR-04: Data Integrity Controls

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-04 |
| **NFR Description** | Data integrity controls SHALL use cryptographic hash functions (SHA-256+) to detect unauthorized modification |
| **Category** | INT |
| **Metric** | File integrity monitoring coverage |
| **Target** | 100% of critical system files and AI artifacts monitored |
| **Method** | TEST |
| **Source UC** | PROC-39, PROC-03 |
| **Source Rule** | BPR-D-01.4-001 |
| **Priority** | HIGH |

---

#### NFR-05: Backup Integrity Verification

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-05 |
| **NFR Description** | Backups SHALL be verified for integrity and restorability quarterly |
| **Category** | INT |
| **Metric** | Backup verification quarterly completion |
| **Target** | 100% of backup types verified quarterly |
| **Method** | DEMONSTRATE |
| **Source UC** | CAP-09 |
| **Source Rule** | BPR-D-04.4-001 |
| **Priority** | MEDIUM |

---

#### NFR-06: SBOM Integrity

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-06 |
| **NFR Description** | Software Bill of Materials SHALL be generated in standard formats (SPDX, CycloneDX) and verified |
| **Category** | INT |
| **Metric** | SBOM generation and verification rate |
| **Target** | 100% of releases have verified SBOM |
| **Method** | INSPECT |
| **Source UC** | CAP-03 |
| **Source Rule** | CR-D-06.2-001 |
| **Priority** | HIGH |

---

#### NFR-07: Configuration Integrity

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-07 |
| **NFR Description** | System configurations SHALL be hardened per CIS Benchmarks and continuously monitored for drift |
| **Category** | INT |
| **Metric** | Configuration compliance percentage |
| **Target** | ≥95% CIS Benchmark compliance maintained |
| **Method** | TEST |
| **Source UC** | PROC-12 |
| **Source Rule** | CR-D-03.4-001, BPR-D-03.4-001 |
| **Priority** | HIGH |

---

#### NFR-08: Change Management Integrity

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-08 |
| **NFR Description** | Production changes SHALL require dual control approval with independent oversight |
| **Category** | INT |
| **Metric** | Dual approval rate for production changes |
| **Target** | 100% of production changes dual-approved |
| **Method** | INSPECT |
| **Source UC** | PROC-30 |
| **Source Rule** | CR-D-07.4-001 |
| **Priority** | CRITICAL |

---

#### NFR-09: AI Training Data Integrity

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-09 |
| **NFR Description** | AI training data SHALL be validated for integrity and representativeness before use |
| **Category** | INT |
| **Metric** | Training data validation rate |
| **Target** | 100% of training datasets validated |
| **Method** | INSPECT |
| **Source UC** | PROC-20, PROC-22 |
| **Source Rule** | CR-D-05.1-001 |
| **Priority** | HIGH |

---

#### NFR-10: AI Decision Traceability

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-10 |
| **NFR Description** | AI decisions SHALL be traceable to inputs, outputs, model version, and decision factors |
| **Category** | INT |
| **Metric** | AI decision log completeness |
| **Target** | 100% of AI decisions logged with full traceability |
| **Method** | INSPECT |
| **Source UC** | CAP-10, PROC-38 |
| **Source Rule** | AI-C09, AI-C10, DORA-C38 |
| **Priority** | CRITICAL |

---

### 4.3 NFR-AVAIL: Availability (12 NFRs)

#### NFR-01: 99.99% Uptime SLA

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-01 |
| **NFR Description** | Critical financial systems SHALL maintain 99.99% uptime (52.6 minutes/year max downtime) |
| **Category** | AVAIL |
| **Metric** | System uptime percentage |
| **Target** | ≥99.99% uptime (≤52.6 min downtime/year) |
| **Method** | ANALYZE |
| **Source UC** | PROC-14 |
| **Source Rule** | CR-D-04.2-001 |
| **Priority** | CRITICAL |

---

#### NFR-02: Disaster Recovery RTO

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-02 |
| **NFR Description** | Disaster recovery SHALL achieve RTO ≤ 4 hours for critical financial systems |
| **Category** | AVAIL |
| **Metric** | Recovery Time Objective achievement |
| **Target** | ≤4 hours for critical systems |
| **Method** | DEMONSTRATE |
| **Source UC** | PROC-14, PROC-16 |
| **Source Rule** | CR-D-04.2-001 |
| **Priority** | CRITICAL |

---

#### NFR-03: Disaster Recovery RPO

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-03 |
| **NFR Description** | Disaster recovery SHALL achieve RPO ≤ 1 hour for critical financial systems |
| **Category** | AVAIL |
| **Metric** | Recovery Point Objective achievement |
| **Target** | ≤1 hour data loss for critical systems |
| **Method** | DEMONSTRATE |
| **Source UC** | PROC-14 |
| **Source Rule** | CR-D-04.2-001 |
| **Priority** | CRITICAL |

---

#### NFR-04: 24/7 SOC Coverage

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-04 |
| **NFR Description** | Security Operations Center SHALL provide 24/7 continuous monitoring and incident response |
| **Category** | AVAIL |
| **Metric** | SOC coverage hours |
| **Target** | 24/7/365 coverage |
| **Method** | DEMONSTRATE |
| **Source UC** | CAP-02 |
| **Source Rule** | CR-D-04.1-001 |
| **Priority** | CRITICAL |

---

#### NFR-05: AI System Failover

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-05 |
| **NFR Description** | AI systems SHALL fail over to standby within SLA without data loss |
| **Category** | AVAIL |
| **Metric** | AI system failover time |
| **Target** | AI service recovery within 2 hours |
| **Method** | DEMONSTRATE |
| **Source UC** | PROC-16 |
| **Source Rule** | CR-D-04.2-001 |
| **Priority** | HIGH |

---

#### NFR-06: AI Model Recovery

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-06 |
| **NFR Description** | AI models SHALL be recoverable from immutable backup within 30 minutes |
| **Category** | AVAIL |
| **Metric** | Model restoration time |
| **Target** | ≤30 minutes from checkpoint restore |
| **Method** | DEMONSTRATE |
| **Source UC** | PROC-16 |
| **Source Rule** | CR-D-04.2-001 |
| **Priority** | HIGH |

---

#### NFR-07: Incident Detection Response

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-07 |
| **NFR Description** | Critical security incidents SHALL be detected and escalated within 5 minutes |
| **Category** | AVAIL |
| **Metric** | Mean time to detect (MTTD) |
| **Target** | ≤5 minutes for critical incidents |
| **Method** | ANALYZE |
| **Source UC** | CAP-02, PROC-17 |
| **Source Rule** | CR-D-04.1-001 |
| **Priority** | CRITICAL |

---

#### NFR-08: Patch Deployment Availability

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-08 |
| **NFR Description** | Automated patch deployment SHALL maintain system availability during patching |
| **Category** | AVAIL |
| **Metric** | Patch deployment success rate |
| **Target** | ≥99% of patches deployed without service interruption |
| **Method** | TEST |
| **Source UC** | PROC-06 |
| **Source Rule** | CR-D-02.2-001 |
| **Priority** | HIGH |

---

#### NFR-09: Multi-Region Redundancy

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-09 |
| **NFR Description** | Critical systems SHALL have geographic distribution across EU data centers |
| **Category** | AVAIL |
| **Metric** | Data center redundancy |
| **Target** | ≥2 EU data centers for critical systems |
| **Method** | INSPECT |
| **Source UC** | CAP-09 |
| **Source Rule** | CR-D-04.4-001 |
| **Priority** | HIGH |

---

#### NFR-10: Data Sovereignty Compliance

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-10 |
| **NFR Description** | Data residency SHALL comply with EU data sovereignty requirements for financial data |
| **Category** | AVAIL |
| **Metric** | EU data residency compliance |
| **Target** | 100% of financial data within EU |
| **Method** | INSPECT |
| **Source UC** | CAP-09 |
| **Source Rule** | CR-D-04.4-001 |
| **Priority** | HIGH |

---

#### NFR-11: AI Model Drift Detection

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-11 |
| **NFR Description** | AI model performance drift SHALL be detected within 1 hour |
| **Category** | AVAIL |
| **Metric** | Drift detection time |
| **Target** | ≤1 hour from drift occurrence to detection |
| **Method** | ANALYZE |
| **Source UC** | PROC-50 |
| **Source Rule** | BPR-D-12.2-001 |
| **Priority** | HIGH |

---

#### NFR-12: Automated Retraining Trigger

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-12 |
| **NFR Description** | Automated model retraining SHALL be triggered within 4 hours of drift threshold breach |
| **Category** | AVAIL |
| **Metric** | Retraining trigger time |
| **Target** | ≤4 hours from threshold breach to retraining start |
| **Method** | DEMONSTRATE |
| **Source UC** | PROC-50 |
| **Source Rule** | BPR-D-12.2-001 |
| **Priority** | MEDIUM |

---

### 4.4 NFR-PRIV: Privacy (10 NFRs)

#### NFR-01: Data Erasure Completion

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-01 |
| **NFR Description** | Data erasure requests SHALL be completed within 30 days |
| **Category** | PRIV |
| **Metric** | Erasure request completion time |
| **Target** | ≤30 days from request to completion |
| **Method** | TEST |
| **Source UC** | UC-01, UC-01.1 |
| **Source Rule** | CR-D-05.3-001 |
| **Priority** | CRITICAL |

---

#### NFR-02: Data Minimization Validation

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-02 |
| **NFR Description** | AI training data SHALL be validated for relevance, representativeness, and freedom from bias proxies |
| **Category** | PRIV |
| **Metric** | Training data validation rate |
| **Target** | 100% of training datasets validated |
| **Method** | INSPECT |
| **Source UC** | PROC-20, PROC-22 |
| **Source Rule** | CR-D-05.1-001 |
| **Priority** | HIGH |

---

#### NFR-03: Retention Policy Enforcement

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-03 |
| **NFR Description** | Data retention SHALL be enforced per tiered policy: 10yr financial, 5yr operational, 6mo AI logs |
| **Category** | PRIV |
| **Metric** | Retention policy compliance |
| **Target** | 100% of data subject to automated retention enforcement |
| **Method** | ANALYZE |
| **Source UC** | PROC-21 |
| **Source Rule** | CR-D-05.2-001 |
| **Priority** | HIGH |

---

#### NFR-04: Data Portability Response

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-04 |
| **NFR Description** | Data subject access requests SHALL be fulfilled within 30 days with machine-readable export |
| **Category** | PRIV |
| **Metric** | DSAR completion time |
| **Target** | ≤30 days for all DSARs |
| **Method** | TEST |
| **Source UC** | UC-02 |
| **Source Rule** | CR-D-05.4-001 |
| **Priority** | HIGH |

---

#### NFR-05: Third-Party Erasure Notification

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-05 |
| **NFR Description** | Third-party processors SHALL be notified of erasure requests within 72 hours |
| **Category** | PRIV |
| **Metric** | Third-party notification time |
| **Target** | ≤72 hours from request to third-party notification |
| **Method** | INSPECT |
| **Source UC** | UC-01 |
| **Source Rule** | CR-D-05.3-001 |
| **Priority** | HIGH |

---

#### NFR-06: Privacy by Design

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-06 |
| **NFR Description** | New processing activities SHALL incorporate privacy by design and default from inception |
| **Category** | PRIV |
| **Metric** | Privacy by design review completion |
| **Target** | 100% of new processing activities have PbD review |
| **Method** | INSPECT |
| **Source UC** | PROC-28 |
| **Source Rule** | CR-D-07.1-001 |
| **Priority** | HIGH |

---

#### NFR-07: DPIA Completion

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-07 |
| **NFR Description** | Data Protection Impact Assessments SHALL be completed before high-risk processing begins |
| **Category** | PRIV |
| **Metric** | DPIA completion rate |
| **Target** | 100% of high-risk processing with completed DPIA |
| **Method** | INSPECT |
| **Source UC** | PROC-34.1 (DPIA) |
| **Source Rule** | GDPR Art. 35 |
| **Priority** | CRITICAL |

---

#### NFR-08: AI Bias Testing

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-08 |
| **NFR Description** | AI systems SHALL be tested for demographic bias across protected attributes before deployment |
| **Category** | PRIV |
| **Metric** | Bias test coverage |
| **Target** | 100% of AI systems tested for bias before deployment |
| **Method** | DEMONSTRATE |
| **Source UC** | PROC-08.2, PROC-37 |
| **Source Rule** | BPR-D-12.1-001 |
| **Priority** | HIGH |

---

#### NFR-09: Human Oversight for AI

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-09 |
| **NFR Description** | High-risk AI decisions SHALL have human oversight with ability to override and escalate |
| **Category** | PRIV |
| **Metric** | Human oversight coverage |
| **Target** | 100% of high-risk AI decisions have human oversight |
| **Method** | INSPECT |
| **Source UC** | UC-49-AI |
| **Source Rule** | AI Act Art. 14 |
| **Priority** | CRITICAL |

---

#### NFR-10: AI Transparency Documentation

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-10 |
| **NFR Description** | AI systems SHALL have transparency documentation including model cards, data sheets, and decision explanations |
| **Category** | PRIV |
| **Metric** | AI transparency documentation completeness |
| **Target** | 100% of AI systems have complete transparency docs |
| **Method** | INSPECT |
| **Source UC** | CAP-07, CAP-07.1 |
| **Source Rule** | CR-D-09.4-001, BPR-D-09.4-001 |
| **Priority** | HIGH |

---

### 4.5 NFR-ACC: Accountability (6 NFRs)

#### NFR-01: Audit Log Retention

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-01 |
| **NFR Description** | Audit logs SHALL be retained per regulatory requirements: minimum 5 years financial, 6 months AI inference |
| **Category** | ACC |
| **Metric** | Log retention compliance |
| **Target** | 100% of logs retained per regulation |
| **Method** | ANALYZE |
| **Source UC** | CAP-10, PROC-38 |
| **Source Rule** | CR-D-10.2-001 |
| **Priority** | CRITICAL |

---

#### NFR-02: Records of Processing

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-02 |
| **NFR Description** | Records of processing activities SHALL be maintained and available for regulatory inspection |
| **Category** | ACC |
| **Metric** | ROPA completeness |
| **Target** | 100% of processing activities documented |
| **Method** | INSPECT |
| **Source UC** | CAP-05 |
| **Source Rule** | CR-D-09.4-001 |
| **Priority** | HIGH |

---

#### NFR-03: Non-Repudiation

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-03 |
| **NFR Description** | System SHALL provide non-repudiation for all significant actions including data access and modifications |
| **Category** | ACC |
| **Metric** | Non-repudiation coverage |
| **Target** | 100% of significant actions with authenticated attribution |
| **Method** | INSPECT |
| **Source UC** | CAP-10 |
| **Source Rule** | CR-D-10.2-001 |
| **Priority** | HIGH |

---

#### NFR-04: Regulatory Reporting

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-04 |
| **NFR Description** | Regulatory compliance reports SHALL be generated per authority requirements within specified timeframes |
| **Category** | ACC |
| **Metric** | Regulatory reporting timely completion |
| **Target** | 100% of required reports submitted on time |
| **Method** | INSPECT |
| **Source UC** | PROC-35 |
| **Source Rule** | CR-D-09.1-001 |
| **Priority** | HIGH |

---

#### NFR-05: AI Decision Logging

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-05 |
| **NFR Description** | AI system decisions SHALL be logged with sufficient detail for regulatory examination and dispute resolution |
| **Category** | ACC |
| **Metric** | AI decision log completeness |
| **Target** | 100% of AI decisions logged with required attributes |
| **Method** | INSPECT |
| **Source UC** | CAP-10, PROC-38 |
| **Source Rule** | AI-C09, AI-C10, DORA-C38 |
| **Priority** | CRITICAL |

---

#### NFR-06: Training Completion Tracking

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-06 |
| **NFR Description** | Security training completion SHALL be tracked and reported for all employees |
| **Category** | ACC |
| **Metric** | Training completion rate |
| **Target** | ≥95% annual training completion |
| **Method** | INSPECT |
| **Source UC** | PROC-31 |
| **Source Rule** | CR-D-08.1-001 |
| **Priority** | MEDIUM |

---

### 4.6 NFR-COMP: Compliance (6 NFRs)

#### NFR-01: Universal Incident Notification

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-01 |
| **NFR Description** | Incident notification SHALL comply with all applicable regulations: DORA (4h initial, 72h follow-up), GDPR (72h), CRA (24h), NIS 2 (24h), AI Act (15d) |
| **Category** | COMP |
| **Metric** | Notification timeline compliance |
| **Target** | 100% of notifications within regulatory SLAs |
| **Method** | TEST |
| **Source UC** | PROC-15 (all specializations) |
| **Source Rule** | CR-D-04.3-001 |
| **Priority** | CRITICAL |

---

#### NFR-02: ISMS Coverage

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-02 |
| **NFR Description** | Information Security Management System SHALL cover all 5 applicable regulations (GDPR, CRA, NIS 2, DORA, AI Act) |
| **Category** | COMP |
| **Metric** | Regulatory coverage in ISMS |
| **Target** | 100% of applicable regulations in ISMS scope |
| **Method** | INSPECT |
| **Source UC** | CAP-05, UC-52-DORA |
| **Source Rule** | CR-D-09.1-001 |
| **Priority** | CRITICAL |

---

#### NFR-03: IPSARA Unified Assessment

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-03 |
| **NFR Description** | Risk assessments SHALL unify DPIA, FRIA, cybersecurity, and ICT risk per unified IPSARA methodology |
| **Category** | COMP |
| **Metric** | IPSARA assessment completion |
| **Target** | 100% of trigger events assessed via IPSARA |
| **Method** | INSPECT |
| **Source UC** | PROC-34, PROC-34.1, PROC-34.2 |
| **Source Rule** | CR-D-09.2-001 |
| **Priority** | CRITICAL |

---

#### NFR-04: Annual TLPT

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-04 |
| **NFR Description** | Threat-Led Penetration Testing SHALL be executed annually per DORA RTS including AI systems |
| **Category** | COMP |
| **Metric** | TLPT completion |
| **Target** | Annual TLPT executed with all scope elements |
| **Method** | DEMONSTRATE |
| **Source UC** | PROC-08, PROC-08.1, PROC-08.2 |
| **Source Rule** | CR-D-02.4-001 |
| **Priority** | CRITICAL |

---

#### NFR-05: Vendor Risk Assessment

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-05 |
| **NFR Description** | ICT third-party providers SHALL be assessed pre-engagement and annually for DORA, NIS 2, and GDPR compliance |
| **Category** | COMP |
| **Metric** | Vendor assessment completion |
| **Target** | 100% of critical vendors assessed pre-engagement and annually |
| **Method** | INSPECT |
| **Source UC** | PROC-24, UC-37-DORA |
| **Source Rule** | CR-D-06.1-001 |
| **Priority** | HIGH |

---

#### NFR-06: AI Act Conformity

| Field | Value |
|-------|-------|
| **NFR ID** | NFR-06 |
| **NFR Description** | High-risk AI systems SHALL conform to AI Act requirements including conformity assessment, technical documentation, and ongoing monitoring |
| **Category** | COMP |
| **Metric** | AI Act conformity status |
| **Target** | 100% of high-risk AI systems conformant |
| **Method** | DEMONSTRATE |
| **Source UC** | PROC-19, PROC-34.2, CAP-07 |
| **Source Rule** | AI Act Art. 14, Art. 28, Art. 73 |
| **Priority** | CRITICAL |

---

## 5. NFR INTERDEPENDENCIES

| NFR | Depends On | Relationship |
|-----|------------|--------------|
| NFR-08 (Immutable Logs) | NFR-12 (Crypto Sharding) | Crypto sharding enables log immutability |
| NFR-02 (RTO ≤4h) | NFR-03 (RPO ≤1h) | RPO supports RTO achievement |
| NFR-01 (Erasure 30d) | NFR-12 (Crypto Sharding) | Crypto sharding resolves T-002 |
| NFR-05 (AI Decision Logging) | NFR-10 (AI Traceability) | Traceability enables accountability |
| NFR-01 (Notification SLA) | NFR-04 (24/7 SOC) | SOC coverage enables SLA compliance |

---

## 6. MEASUREMENT METHODS

| Method | Description | When Used |
|--------|-------------|-----------|
| **TEST** | Automated technical testing | Encryption, MFA, patches, data operations |
| **INSPECT** | Document review and configuration audit | Policies, training, documentation |
| **DEMONSTRATE** | Operational demonstration or exercise | SOC coverage, DR tests, pentests |
| **ANALYZE** | Data analysis and trend monitoring | Logs, metrics, availability reports |

---

## 7. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-28 | Security Architect | Initial creation — 56 NFRs across 6 categories |

---

**Next Step:** Proceed to 25_Risk_Analysis.md for risk cycle execution.