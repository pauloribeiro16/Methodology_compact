---
document_id: AEGIS-P3-23
title: Functional Requirements
phase: 3
version: 1.0
created: 2026-04-28
updated: 2026-04-28
author: Security Architect
status: DRAFT
inputs: [17_Functional_Tree.md, 15_Requirements_Allocation.md, 13_Use_Cases_Catalog.md]
outputs: [22_Traceability_Matrix.xlsx]
traceability: AEGIS Class Model → FunctionalRequirement, FRDomain, VerificationMethod classes
related_documents: 17_Functional_Tree.md, 24_Non_Functional_Requirements.md, 15_Requirements_Allocation.md
case_id: CASE-03-OMNIBANK
case: Case_03_OmniBank_Financial
complexity: Maximum (5 regulations, 38 sub-domains, 62 use cases, 72 FRs)
---

# Functional Requirements

**Case:** Case 03 — OmniBank Financial Systems (Maximum Complexity)
**Phase:** 3 — Decomposition & Risk Integration
**Step:** 8 — Functional Requirements Derivation

---

## 1. DOCUMENT PURPOSE

This document defines the Functional Requirements (FRs) derived from the Functional Tree (Doc 17) and the Use Cases Catalog (Doc 13). FRs are technology-agnostic statements of what the system must do, organized by the six FR domains: IAM, DP, SEC, DEV, GOV, TRN.

Each FR follows the derivation formula: **Actor → Behavior → Constraint → Verification**, ensuring full traceability from regulatory requirement to implementation.

---

## 2. FR DEFINITION STRUCTURE

| Field | Type | Description |
|-------|------|-------------|
| **FR ID** | string | Unique identifier: `FR-{Number}` |
| **FR Description** | text | Actor + verb + object + constraint |
| **Source UC** | string | UC that derives this FR |
| **Source Node** | string | Tree node that implements this FR |
| **Source Rule** | string | Compliance rule this FR satisfies |
| **Domain** | enum | IAM, DP, SEC, DEV, GOV, TRN |
| **Verification Method** | enum | TEST, INSPECT, DEMONSTRATE, ANALYZE |
| **Priority** | enum | CRITICAL, HIGH, MEDIUM, LOW |

---

## 3. FR SUMMARY

| Metric | Value |
|--------|-------|
| **Total FRs** | 72 |
| **IAM Domain** | 12 FRs |
| **DP Domain** | 14 FRs |
| **SEC Domain** | 18 FRs |
| **DEV Domain** | 10 FRs |
| **GOV Domain** | 12 FRs |
| **TRN Domain** | 6 FRs |
| **Verification Methods** | TEST: 24, INSPECT: 28, DEMONSTRATE: 14, ANALYZE: 6 |
| **Priority Distribution** | CRITICAL: 28, HIGH: 26, MEDIUM: 14, LOW: 4 |

---

## 4. FUNCTIONAL REQUIREMENTS BY DOMAIN

### 4.1 FR-IAM: Identity & Access Management (12 FRs)

#### FR-01: Unified Identity Provisioning

| Field | Value |
|-------|-------|
| **FR ID** | FR-01 |
| **FR Description** | System SHALL support unified identity provisioning across all internal systems, cloud services, and AI platforms with automated HR-driven lifecycle management |
| **Source UC** | PROC-10 |
| **Source Node** | D-03.1.1 |
| **Source Rule** | CR-D-03.1-001 |
| **Domain** | IAM |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-02: MFA for Privileged Access

| Field | Value |
|-------|-------|
| **FR ID** | FR-02 |
| **FR Description** | System SHALL enforce MFA for all privileged access, remote access, and AI system access with step-up authentication for high-risk financial transactions |
| **Source UC** | UC-17 |
| **Source Node** | D-03.2.1 |
| **Source Rule** | CR-D-03.2-001 |
| **Domain** | IAM |
| **Verification** | TEST |
| **Priority** | CRITICAL |

---

#### FR-03: FIDO2/WebAuthn Support

| Field | Value |
|-------|-------|
| **FR ID** | FR-03 |
| **FR Description** | System SHALL support FIDO2/WebAuthn for phishing-resistant MFA across all user-facing applications |
| **Source UC** | UC-22 |
| **Source Node** | D-03.2.2 |
| **Source Rule** | BPR-D-03.2-001 |
| **Domain** | IAM |
| **Verification** | TEST |
| **Priority** | HIGH |

---

#### FR-04: Quarterly Access Review

| Field | Value |
|-------|-------|
| **FR ID** | FR-04 |
| **FR Description** | System SHALL enforce least privilege with quarterly access reviews for all systems including AI model access and training data access |
| **Source UC** | PROC-11 |
| **Source Node** | D-03.3.1 |
| **Source Rule** | CR-D-03.3-001 |
| **Domain** | IAM |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-05: Automated Deprovisioning

| Field | Value |
|-------|-------|
| **FR ID** | FR-05 |
| **FR Description** | System SHALL support automated deprovisioning of user access within 24 hours of HR notification |
| **Source UC** | PROC-13 |
| **Source Node** | D-03.1.2 |
| **Source Rule** | CR-D-03.1-001 |
| **Domain** | IAM |
| **Verification** | TEST |
| **Priority** | HIGH |

---

#### FR-06: AI Platform Access Control

| Field | Value |
|-------|-------|
| **FR ID** | FR-06 |
| **FR Description** | System SHALL manage access to AI model training data, inference endpoints, and parameter changes with MFA and least privilege |
| **Source UC** | UC-21 |
| **Source Node** | D-03.2.1 |
| **Source Rule** | CR-D-03.1-001, CR-D-03.2-001 |
| **Domain** | IAM |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-07: Dual Approval for AI Parameters

| Field | Value |
|-------|-------|
| **FR ID** | FR-07 |
| **FR Description** | System SHALL require dual approval for high-risk AI model parameter changes with independent oversight |
| **Source UC** | UC-21.1 |
| **Source Node** | D-03.3.1 |
| **Source Rule** | CR-D-03.3-001 |
| **Domain** | IAM |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-08: RBAC Implementation

| Field | Value |
|-------|-------|
| **FR ID** | FR-08 |
| **FR Description** | System SHALL implement Role-Based Access Control (RBAC) with defined roles, permissions, and separation of duties |
| **Source UC** | PROC-10 |
| **Source Node** | D-03.1.1 |
| **Source Rule** | BPR-D-03.1-001 |
| **Domain** | IAM |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-09: PAM with Just-in-Time Access

| Field | Value |
|-------|-------|
| **FR ID** | FR-09 |
| **FR Description** | System SHALL implement Privileged Access Management (PAM) with just-in-time access, session recording, and credential vaulting |
| **Source UC** | PROC-11 |
| **Source Node** | D-03.3.1 |
| **Source Rule** | BPR-D-03.3-001 |
| **Domain** | IAM |
| **Verification** | DEMONSTRATE |
| **Priority** | MEDIUM |

---

#### FR-10: SSO Integration

| Field | Value |
|-------|-------|
| **FR ID** | FR-10 |
| **FR Description** | System SHALL integrate with enterprise SSO for unified authentication across all platforms |
| **Source UC** | PROC-10 |
| **Source Node** | D-03.1.1 |
| **Source Rule** | CR-D-03.1-001 |
| **Domain** | IAM |
| **Verification** | TEST |
| **Priority** | HIGH |

---

#### FR-11: Hardware Security Key Support

| Field | Value |
|-------|-------|
| **FR ID** | FR-11 |
| **FR Description** | System SHALL support hardware security keys for privileged accounts with phishing-resistant authentication |
| **Source UC** | UC-22 |
| **Source Node** | D-03.2.2 |
| **Source Rule** | BPR-D-03.2-001 |
| **Domain** | IAM |
| **Verification** | TEST |
| **Priority** | MEDIUM |

---

#### FR-12: Access Review Automation

| Field | Value |
|-------|-------|
| **FR ID** | FR-12 |
| **FR Description** | System SHALL automate access review workflow with remediation tracking and escalation for non-compliance |
| **Source UC** | PROC-11.1 |
| **Source Node** | D-03.3.1 |
| **Source Rule** | CR-D-03.3-001 |
| **Domain** | IAM |
| **Verification** | DEMONSTRATE |
| **Priority** | HIGH |

---

### 4.2 FR-DP: Data Protection (14 FRs)

#### FR-13: AES-256 Encryption at Rest

| Field | Value |
|-------|-------|
| **FR ID** | FR-13 |
| **FR Description** | System SHALL encrypt all personal, financial, and AI training data at rest using AES-256 or stronger |
| **Source UC** | UC-02, UC-06 |
| **Source Node** | D-01.1.1, D-01.1.2 |
| **Source Rule** | CR-D-01.1-001 |
| **Domain** | DP |
| **Verification** | TEST |
| **Priority** | CRITICAL |

---

#### FR-14: Field-Level PII Encryption

| Field | Value |
|-------|-------|
| **FR ID** | FR-14 |
| **FR Description** | System SHALL implement field-level encryption for PII fields and AI training datasets |
| **Source UC** | UC-06 |
| **Source Node** | D-01.1.2 |
| **Source Rule** | CR-D-01.1-001 |
| **Domain** | DP |
| **Verification** | TEST |
| **Priority** | CRITICAL |

---

#### FR-15: TLS 1.3 for Data in Transit

| Field | Value |
|-------|-------|
| **FR ID** | FR-15 |
| **FR Description** | System SHALL encrypt all data in transit using TLS 1.3 with HSTS and certificate pinning |
| **Source UC** | UC-03 |
| **Source Node** | D-01.2.1, D-01.2.2, D-01.2.3 |
| **Source Rule** | CR-D-01.2-001 |
| **Domain** | DP |
| **Verification** | TEST |
| **Priority** | CRITICAL |

---

#### FR-16: HSM Key Lifecycle Management

| Field | Value |
|-------|-------|
| **FR ID** | FR-16 |
| **FR Description** | System SHALL manage cryptographic keys with HSM-backed lifecycle controls including generation, rotation, revocation, and destruction |
| **Source UC** | PROC-02, PROC-04 |
| **Source Node** | D-01.3.1 |
| **Source Rule** | CR-D-01.3-001 |
| **Domain** | DP |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-17: AI Model Integrity Validation

| Field | Value |
|-------|-------|
| **FR ID** | FR-17 |
| **FR Description** | System SHALL validate AI model integrity using cryptographic checksums and version control on every model load |
| **Source UC** | PROC-03, UC-08 |
| **Source Node** | D-01.4.1, D-01.4.2 |
| **Source Rule** | CR-D-01.4-001 |
| **Domain** | DP |
| **Verification** | TEST |
| **Priority** | HIGH |

---

#### FR-18: Data Minimization Enforcement

| Field | Value |
|-------|-------|
| **FR ID** | FR-18 |
| **FR Description** | System SHALL enforce data minimization by validating AI training data relevance, representativeness, and bias proxy freedom |
| **Source UC** | PROC-20, PROC-22 |
| **Source Node** | D-05.1.1, D-05.1.2 |
| **Source Rule** | CR-D-05.1-001 |
| **Domain** | DP |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-19: Tiered Retention Enforcement

| Field | Value |
|-------|-------|
| **FR ID** | FR-19 |
| **FR Description** | System SHALL enforce tiered retention: 10-year financial records (MiFID II), 5-year operational records, 6-month AI inference logs |
| **Source UC** | PROC-21 |
| **Source Node** | D-05.2.1, D-05.2.2 |
| **Source Rule** | CR-D-05.2-001 |
| **Domain** | DP |
| **Verification** | ANALYZE |
| **Priority** | CRITICAL |

---

#### FR-20: Cryptographic Sharding Erasure

| Field | Value |
|-------|-------|
| **FR ID** | FR-20 |
| **FR Description** | System SHALL execute cryptographic sharding-based erasure within 30 days of request, destroying PII keys while preserving audit log structure |
| **Source UC** | UC-33, UC-33.1 |
| **Source Node** | D-05.3.1 |
| **Source Rule** | CR-D-05.3-001 |
| **Domain** | DP |
| **Verification** | TEST |
| **Priority** | CRITICAL |

---

#### FR-21: Machine-Readable Data Export

| Field | Value |
|-------|-------|
| **FR ID** | FR-21 |
| **FR Description** | System SHALL export data in machine-readable formats (JSON, CSV) including AI model decisions and credit scoring factors within 30 days |
| **Source UC** | UC-34, UC-34.1 |
| **Source Node** | D-05.4.1 |
| **Source Rule** | CR-D-05.4-001 |
| **Domain** | DP |
| **Verification** | TEST |
| **Priority** | HIGH |

---

#### FR-22: AI Training Data Lineage

| Field | Value |
|-------|-------|
| **FR ID** | FR-22 |
| **FR Description** | System SHALL document AI training data lineage on every training run including collection, preprocessing, and validation |
| **Source UC** | PROC-22 |
| **Source Node** | D-05.1.1 |
| **Source Rule** | CR-D-05.1-001 |
| **Domain** | DP |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-23: Third-Party Erasure Notification

| Field | Value |
|-------|-------|
| **FR ID** | FR-23 |
| **FR Description** | System SHALL notify third-party data processors of erasure requests and verify compliance within 72 hours |
| **Source UC** | UC-33 |
| **Source Node** | D-05.3.1 |
| **Source Rule** | CR-D-05.3-001 |
| **Domain** | DP |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-24: Data Classification Schema

| Field | Value |
|-------|-------|
| **FR ID** | FR-24 |
| **FR Description** | System SHALL implement data classification schema with automated discovery and classification-based handling rules |
| **Source UC** | PROC-20 |
| **Source Node** | D-05.1.1 |
| **Source Rule** | BPR-D-05.1-001 |
| **Domain** | DP |
| **Verification** | INSPECT |
| **Priority** | MEDIUM |

---

#### FR-25: Automated Deletion on Expiry

| Field | Value |
|-------|-------|
| **FR ID** | FR-25 |
| **FR Description** | System SHALL automatically delete data upon retention expiry with audit trail of deletion |
| **Source UC** | PROC-21 |
| **Source Node** | D-05.2.1 |
| **Source Rule** | CR-D-05.2-001 |
| **Domain** | DP |
| **Verification** | ANALYZE |
| **Priority** | HIGH |

---

#### FR-26: Key Classification & Segregation

| Field | Value |
|-------|-------|
| **FR ID** | FR-26 |
| **FR Description** | System SHALL segregate cryptographic keys by data classification and regulatory domain |
| **Source UC** | PROC-02 |
| **Source Node** | D-01.3.2 |
| **Source Rule** | CR-D-01.3-001 |
| **Domain** | DP |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

### 4.3 FR-SEC: Security Operations (18 FRs)

#### FR-27: 24/7 SOC Monitoring

| Field | Value |
|-------|-------|
| **FR ID** | FR-27 |
| **FR Description** | System SHALL operate 24/7 SOC with automated incident detection and triage including AI anomaly detection |
| **Source UC** | CAP-02, PROC-17 |
| **Source Node** | D-04.1.1, D-04.1.2 |
| **Source Rule** | CR-D-04.1-001 |
| **Domain** | SEC |
| **Verification** | DEMONSTRATE |
| **Priority** | CRITICAL |

---

#### FR-28: Business Continuity with 99.99% Uptime

| Field | Value |
|-------|-------|
| **FR ID** | FR-28 |
| **FR Description** | System SHALL maintain 99.99% uptime SLA with disaster recovery RTO <= 4h and RPO <= 1h |
| **Source UC** | PROC-14, PROC-16 |
| **Source Node** | D-04.2.1, D-04.2.2 |
| **Source Rule** | CR-D-04.2-001 |
| **Domain** | SEC |
| **Verification** | DEMONSTRATE |
| **Priority** | CRITICAL |

---

#### FR-29: Universal Incident Notification

| Field | Value |
|-------|-------|
| **FR ID** | FR-29 |
| **FR Description** | System SHALL execute 24-hour universal incident notification workflow across GDPR (72h), CRA (24h), NIS 2 (24h), DORA (4h initial + 72h follow-up), AI Act (15d) |
| **Source UC** | PROC-15, PROC-15.1, PROC-15.2, UC-25-NIS2, UC-25-CRA, UC-25-AI |
| **Source Node** | D-04.3.1, D-04.3.2, D-04.3.3, D-04.3.4, D-04.3.5 |
| **Source Rule** | CR-D-04.3-001 |
| **Domain** | SEC |
| **Verification** | TEST |
| **Priority** | CRITICAL |

---

#### FR-30: Immutable Backup with Failover

| Field | Value |
|-------|-------|
| **FR ID** | FR-30 |
| **FR Description** | System SHALL maintain redundant backup systems with automated failover across EU data centers with sovereignty controls |
| **Source UC** | UC-26 |
| **Source Node** | D-04.4.1 |
| **Source Rule** | CR-D-04.4-001 |
| **Domain** | SEC |
| **Verification** | DEMONSTRATE |
| **Priority** | CRITICAL |

---

#### FR-31: Vulnerability Scanning

| Field | Value |
|-------|-------|
| **FR ID** | FR-31 |
| **FR Description** | System SHALL execute continuous automated vulnerability scanning with Critical findings remediated within 72 hours |
| **Source UC** | PROC-05, CAP-01 |
| **Source Node** | D-02.1.1 |
| **Source Rule** | CR-D-02.1-001 |
| **Domain** | SEC |
| **Verification** | DEMONSTRATE |
| **Priority** | CRITICAL |

---

#### FR-32: AI Vulnerability Assessment

| Field | Value |
|-------|-------|
| **FR ID** | FR-32 |
| **FR Description** | System SHALL assess AI model vulnerabilities including data poisoning, model evasion, and adversarial attacks per MITRE ATLAS |
| **Source UC** | PROC-09 |
| **Source Node** | D-02.1.2 |
| **Source Rule** | CR-D-02.1-001, BPR-D-12.4-001 |
| **Domain** | SEC |
| **Verification** | DEMONSTRATE |
| **Priority** | HIGH |

---

#### FR-33: Automated Patch Deployment

| Field | Value |
|-------|-------|
| **FR ID** | FR-33 |
| **FR Description** | System SHALL deploy automated patch management with 72-hour SLA for critical vulnerabilities |
| **Source UC** | PROC-06 |
| **Source Node** | D-02.2.1 |
| **Source Rule** | CR-D-02.2-001 |
| **Domain** | SEC |
| **Verification** | TEST |
| **Priority** | CRITICAL |

---

#### FR-34: ENISA/CSIRT Vulnerability Disclosure

| Field | Value |
|-------|-------|
| **FR ID** | FR-34 |
| **FR Description** | System SHALL report critical incidents to ENISA/CSIRT within 24 hours per coordinated vulnerability disclosure policy |
| **Source UC** | PROC-07 |
| **Source Node** | D-02.3.1 |
| **Source Rule** | CR-D-02.3-001 |
| **Domain** | SEC |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-35: TLPT Execution

| Field | Value |
|-------|-------|
| **FR ID** | FR-35 |
| **FR Description** | System SHALL execute annual Threat-Led Penetration Testing (TLPT) per DORA RTS including AI bias testing and adversarial robustness |
| **Source UC** | PROC-08, PROC-08.1, PROC-08.2 |
| **Source Node** | D-02.4.1, D-02.4.2 |
| **Source Rule** | CR-D-02.4-001 |
| **Domain** | SEC |
| **Verification** | DEMONSTRATE |
| **Priority** | CRITICAL |

---

#### FR-36: AI Model Drift Detection

| Field | Value |
|-------|-------|
| **FR ID** | FR-36 |
| **FR Description** | System SHALL detect AI model drift hourly with automated retraining triggered within 4 hours of threshold breach |
| **Source UC** | UC-61, UC-61.1 |
| **Source Node** | D-10.1.2 |
| **Source Rule** | BPR-D-12.2-001 |
| **Domain** | SEC |
| **Verification** | ANALYZE |
| **Priority** | HIGH |

---

#### FR-37: Immutable Audit Logging

| Field | Value |
|-------|-------|
| **FR ID** | FR-37 |
| **FR Description** | System SHALL maintain immutable audit logs with PII separation and AI system traceability using cryptographic sharding |
| **Source UC** | UC-58 |
| **Source Node** | D-10.2.1, D-10.2.2 |
| **Source Rule** | CR-D-10.2-001 |
| **Domain** | SEC |
| **Verification** | ANALYZE |
| **Priority** | CRITICAL |

---

#### FR-38: AI-Powered Threat Detection

| Field | Value |
|-------|-------|
| **FR ID** | FR-38 |
| **FR Description** | System SHALL deploy 24/7 continuous security monitoring with AI-powered threat detection across all systems and AI pipelines |
| **Source UC** | UC-57, UC-57.1 |
| **Source Node** | D-10.1.1 |
| **Source Rule** | CR-D-10.1-001 |
| **Domain** | SEC |
| **Verification** | TEST |
| **Priority** | CRITICAL |

---

#### FR-39: Red Team Operations

| Field | Value |
|-------|-------|
| **FR ID** | FR-39 |
| **FR Description** | System SHALL conduct red team operations for AI systems including adversarial robustness testing per MITRE ATLAS |
| **Source UC** | PROC-36, PROC-37, PROC-37.1 |
| **Source Node** | D-10.3.1 |
| **Source Rule** | BPR-D-12.4-001 |
| **Domain** | SEC |
| **Verification** | DEMONSTRATE |
| **Priority** | HIGH |

---

#### FR-40: Incident Response Playbooks

| Field | Value |
|-------|-------|
| **FR ID** | FR-40 |
| **FR Description** | System SHALL maintain incident response playbooks covering all incident types including AI model compromise and supply chain attacks |
| **Source UC** | CAP-02 |
| **Source Node** | D-04.1.1 |
| **Source Rule** | BPR-D-04.1-001 |
| **Domain** | SEC |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-41: AI Anomaly Investigation

| Field | Value |
|-------|-------|
| **FR ID** | FR-41 |
| **FR Description** | System SHALL investigate AI model anomalies including model drift, adversarial manipulation, and data quality with root cause within 4 hours |
| **Source UC** | PROC-17, PROC-17.1 |
| **Source Node** | D-04.1.2 |
| **Source Rule** | CR-D-04.1-001, CR-D-10.1-001 |
| **Domain** | SEC |
| **Verification** | DEMONSTRATE |
| **Priority** | HIGH |

---

#### FR-42: Quarterly Tabletop Exercises

| Field | Value |
|-------|-------|
| **FR ID** | FR-42 |
| **FR Description** | System SHALL conduct quarterly tabletop exercises with cross-functional participants and documented lessons learned |
| **Source UC** | PROC-18 |
| **Source Node** | D-04.1.1 |
| **Source Rule** | BPR-D-04.3-001 |
| **Domain** | SEC |
| **Verification** | DEMONSTRATE |
| **Priority** | MEDIUM |

---

#### FR-43: Backup Verification

| Field | Value |
|-------|-------|
| **FR ID** | FR-43 |
| **FR Description** | System SHALL verify backup integrity quarterly with full restore drills and immutable backups isolated from production |
| **Source UC** | UC-26 |
| **Source Node** | D-04.4.1 |
| **Source Rule** | BPR-D-04.4-001 |
| **Domain** | SEC |
| **Verification** | DEMONSTRATE |
| **Priority** | MEDIUM |

---

#### FR-44: AI System Recovery

| Field | Value |
|-------|-------|
| **FR ID** | FR-44 |
| **FR Description** | System SHALL recover AI systems within 2 hours including model restoration from immutable backup and inference service resumption |
| **Source UC** | PROC-16 |
| **Source Node** | D-04.2.2 |
| **Source Rule** | CR-D-04.2-001 |
| **Domain** | SEC |
| **Verification** | DEMONSTRATE |
| **Priority** | HIGH |

---

### 4.4 FR-DEV: Secure Development (10 FRs)

#### FR-45: Secure-by-Design Implementation

| Field | Value |
|-------|-------|
| **FR ID** | FR-45 |
| **FR Description** | System SHALL implement privacy and security by design per CRA secure-by-default standard with threat modeling and AI ethical design reviews |
| **Source UC** | PROC-28, UC-46 |
| **Source Node** | D-07.1.1, D-07.1.2 |
| **Source Rule** | CR-D-07.1-001 |
| **Domain** | DEV |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-46: SAST/DAST Integration

| Field | Value |
|-------|-------|
| **FR ID** | FR-46 |
| **FR Description** | System SHALL integrate SAST/DAST per OWASP ASVS Level 2 in all CI/CD pipelines including AI code repositories |
| **Source UC** | PROC-29, PROC-29.1 |
| **Source Node** | D-07.2.1 |
| **Source Rule** | CR-D-07.2-001 |
| **Domain** | DEV |
| **Verification** | DEMONSTRATE |
| **Priority** | CRITICAL |

---

#### FR-47: Security Gates Automation

| Field | Value |
|-------|-------|
| **FR ID** | FR-47 |
| **FR Description** | System SHALL enforce automated security gates (SAST, DAST, SCA, secrets detection, IaC scanning) blocking deployment on critical findings |
| **Source UC** | UC-44, UC-44.1 |
| **Source Node** | D-07.3.1, D-07.3.2 |
| **Source Rule** | CR-D-07.3-001 |
| **Domain** | DEV |
| **Verification** | TEST |
| **Priority** | CRITICAL |

---

#### FR-48: AI Deployment Gate

| Field | Value |
|-------|-------|
| **FR ID** | FR-48 |
| **FR Description** | System SHALL enforce AI-specific deployment gates including model signing, bias testing, and adversarial robustness validation before production |
| **Source UC** | UC-44.1, UC-46 |
| **Source Node** | D-07.3.2 |
| **Source Rule** | CR-D-07.3-001, CR-D-07.1-001 |
| **Domain** | DEV |
| **Verification** | DEMONSTRATE |
| **Priority** | CRITICAL |

---

#### FR-49: Dual Control Change Management

| Field | Value |
|-------|-------|
| **FR ID** | FR-49 |
| **FR Description** | System SHALL implement formal change management with dual control approval and independent oversight for all production changes |
| **Source UC** | PROC-30 |
| **Source Node** | D-07.4.1 |
| **Source Rule** | CR-D-07.4-001 |
| **Domain** | DEV |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-50: IaC Scanning

| Field | Value |
|-------|-------|
| **FR ID** | FR-50 |
| **FR Description** | System SHALL scan infrastructure-as-code (IaC) for vulnerabilities before deployment using Checkov or equivalent |
| **Source UC** | UC-47 |
| **Source Node** | D-07.3.1 |
| **Source Rule** | BPR-D-07.3-001 |
| **Domain** | DEV |
| **Verification** | TEST |
| **Priority** | MEDIUM |

---

#### FR-51: SBOM Generation

| Field | Value |
|-------|-------|
| **FR ID** | FR-51 |
| **FR Description** | System SHALL generate Software Bill of Materials (SBOM) in SPDX and CycloneDX formats on every release with AI model dependencies |
| **Source UC** | CAP-03 |
| **Source Node** | D-06.2.1 |
| **Source Rule** | CR-D-06.2-001 |
| **Domain** | DEV |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-52: NIST SSDF Implementation

| Field | Value |
|-------|-------|
| **FR ID** | FR-52 |
| **FR Description** | System SHALL implement NIST Secure Software Development Framework (SSDF) practices across all development teams |
| **Source UC** | PROC-28 |
| **Source Node** | D-07.1.1 |
| **Source Rule** | BPR-D-07.1-001 |
| **Domain** | DEV |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-53: Secrets Detection

| Field | Value |
|-------|-------|
| **FR ID** | FR-53 |
| **FR Description** | System SHALL detect secrets and credentials in code repositories and pipeline configurations before deployment |
| **Source UC** | UC-44 |
| **Source Node** | D-07.3.1 |
| **Source Rule** | CR-D-07.3-001 |
| **Domain** | DEV |
| **Verification** | TEST |
| **Priority** | HIGH |

---

#### FR-54: AI Training Pipeline Security

| Field | Value |
|-------|-------|
| **FR ID** | FR-54 |
| **FR Description** | System SHALL secure AI training pipeline including data validation, model signing, artifact verification, and deployment approval |
| **Source UC** | UC-46 |
| **Source Node** | D-07.3.2 |
| **Source Rule** | CR-D-07.1-001, CR-D-07.3-001 |
| **Domain** | DEV |
| **Verification** | DEMONSTRATE |
| **Priority** | HIGH |

---

### 4.5 FR-GOV: Governance (12 FRs)

#### FR-55: Unified ISMS

| Field | Value |
|-------|-------|
| **FR ID** | FR-55 |
| **FR Description** | System SHALL maintain unified Information Security Management System (ISMS) covering all 5 regulatory frameworks with 10+ year documentation retention |
| **Source UC** | CAP-05, UC-52-DORA |
| **Source Node** | D-09.1.1 |
| **Source Rule** | CR-D-09.1-001 |
| **Domain** | GOV |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-56: IPSARA Unified Assessment

| Field | Value |
|-------|-------|
| **FR ID** | FR-56 |
| **FR Description** | System SHALL execute IPSARA unified risk assessments combining DPIA, FRIA, cybersecurity risk, and ICT risk per AI Act requirements |
| **Source UC** | PROC-34, PROC-34.1, PROC-34.2 |
| **Source Node** | D-09.2.1 |
| **Source Rule** | CR-D-09.2-001 |
| **Domain** | GOV |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-57: Asset Inventory Automation

| Field | Value |
|-------|-------|
| **FR ID** | FR-57 |
| **FR Description** | System SHALL maintain comprehensive asset and ICT inventory with automated discovery including AI models and training data |
| **Source UC** | CAP-06 |
| **Source Node** | D-09.3.1 |
| **Source Rule** | CR-D-09.3-001 |
| **Domain** | GOV |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-58: AI Model Card Maintenance

| Field | Value |
|-------|-------|
| **FR ID** | FR-58 |
| **FR Description** | System SHALL maintain AI model cards updated on every release including performance metrics, bias test results, and intended use |
| **Source UC** | CAP-07, CAP-07.1 |
| **Source Node** | D-09.4.1 |
| **Source Rule** | CR-D-09.4-001 |
| **Domain** | GOV |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-59: AI Decision Logging

| Field | Value |
|-------|-------|
| **FR ID** | FR-59 |
| **FR Description** | System SHALL log AI decisions with full traceability including inputs, outputs, model version, and decision factors for regulatory examination |
| **Source UC** | UC-58, PROC-38 |
| **Source Node** | D-09.4.2, D-10.2.1 |
| **Source Rule** | CR-D-09.4-001, CR-D-02.1-001, CR-D-02.1-001 |
| **Domain** | GOV |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-60: ICT Third-Party Risk Management

| Field | Value |
|-------|-------|
| **FR ID** | FR-60 |
| **FR Description** | System SHALL assess all ICT third-party providers pre-engagement and annually including AI model providers using SIG or CAIQ |
| **Source UC** | PROC-24, PROC-24.1, UC-37-DORA |
| **Source Node** | D-06.1.1 |
| **Source Rule** | CR-D-06.1-001 |
| **Domain** | GOV |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-61: Vendor Exit Strategy

| Field | Value |
|-------|-------|
| **FR ID** | FR-61 |
| **FR Description** | System SHALL manage third-party concentration risk with documented exit strategies for critical vendors including data migration |
| **Source UC** | PROC-26 |
| **Source Node** | D-06.4.1 |
| **Source Rule** | CR-D-06.4-001 |
| **Domain** | GOV |
| **Verification** | ANALYZE |
| **Priority** | HIGH |

---

#### FR-62: Regulatory Compliance Reporting

| Field | Value |
|-------|-------|
| **FR ID** | FR-62 |
| **FR Description** | System SHALL generate regulatory compliance reports for ECB/BaFin, ENISA, and other authorities including AI governance indicators |
| **Source UC** | PROC-35 |
| **Source Node** | D-09.1.1 |
| **Source Rule** | CR-D-09.1-001, CR-D-09.1-001 |
| **Domain** | GOV |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-63: DPIA Documentation

| Field | Value |
|-------|-------|
| **FR ID** | FR-63 |
| **FR Description** | System SHALL document GDPR Data Protection Impact Assessments for processing likely to result in high risk |
| **Source UC** | PROC-34.1 (DPIA) |
| **Source Node** | D-09.2.1 |
| **Source Rule** | CR-D-09.2-001 |
| **Domain** | GOV |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-64: FRIA Documentation

| Field | Value |
|-------|-------|
| **FR ID** | FR-64 |
| **FR Description** | System SHALL document AI Act Fundamental Rights Impact Assessments for high-risk AI systems |
| **Source UC** | PROC-34.2 (FRIA) |
| **Source Node** | D-09.2.1 |
| **Source Rule** | CR-D-06.1-001 |
| **Domain** | GOV |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-65: Contractual Security Clauses

| Field | Value |
|-------|-------|
| **FR ID** | FR-65 |
| **FR Description** | System SHALL enforce minimum security requirements in all vendor contracts including audit rights and breach notification SLAs |
| **Source UC** | PROC-25, UC-39-DORA |
| **Source Node** | D-06.3.1 |
| **Source Rule** | CR-D-06.3-001 |
| **Domain** | GOV |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-66: Board ICT Risk Reporting

| Field | Value |
|-------|-------|
| **FR ID** | FR-66 |
| **FR Description** | System SHALL provide board-level ICT risk dashboards with regulatory compliance status, risk metrics, and incident trends |
| **Source UC** | PROC-32 |
| **Source Node** | D-08.3.1 |
| **Source Rule** | CR-D-08.3-001 |
| **Domain** | GOV |
| **Verification** | DEMONSTRATE |
| **Priority** | MEDIUM |

---

### 4.6 FR-TRN: Training & Awareness (6 FRs)

#### FR-67: Annual Security Awareness Training

| Field | Value |
|-------|-------|
| **FR ID** | FR-67 |
| **FR Description** | System SHALL deliver annual security awareness training to all 5000+ employees with role-specific modules for developers, operations, and management |
| **Source UC** | PROC-31, UC-48-Online, UC-48-Classroom |
| **Source Node** | D-08.1.1 |
| **Source Rule** | CR-D-08.1-001 |
| **Domain** | TRN |
| **Verification** | INSPECT |
| **Priority** | CRITICAL |

---

#### FR-68: AI Ethics Training

| Field | Value |
|-------|-------|
| **FR ID** | FR-68 |
| **FR Description** | System SHALL include AI ethics training for data science and ML teams covering bias detection, fairness metrics, and human oversight |
| **Source UC** | PROC-31 (AI ethics component) |
| **Source Node** | D-08.1.1 |
| **Source Rule** | CR-D-08.2-001 |
| **Domain** | TRN |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-69: Phishing Simulations

| Field | Value |
|-------|-------|
| **FR ID** | FR-69 |
| **FR Description** | System SHALL conduct quarterly phishing simulations with click rate < 5% and remedial training for failures |
| **Source UC** | PROC-33 |
| **Source Node** | D-08.1.2 |
| **Source Rule** | BPR-D-08.1-001 |
| **Domain** | TRN |
| **Verification** | DEMONSTRATE |
| **Priority** | MEDIUM |

---

#### FR-70: Role Certification Tracking

| Field | Value |
|-------|-------|
| **FR ID** | FR-70 |
| **FR Description** | System SHALL track mandatory security certifications for privileged roles with annual competence assessment |
| **Source UC** | CAP-04, UC-49-AI |
| **Source Node** | D-08.2.1 |
| **Source Rule** | CR-D-08.2-001 |
| **Domain** | TRN |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-71: AI Human Oversight Training

| Field | Value |
|-------|-------|
| **FR ID** | FR-71 |
| **FR Description** | System SHALL ensure AI human oversight personnel complete training on interpreting AI decisions and override procedures |
| **Source UC** | UC-49-AI |
| **Source Node** | D-08.2.2 |
| **Source Rule** | BPR-D-12.3-001 |
| **Domain** | TRN |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

#### FR-72: Board Security Training

| Field | Value |
|-------|-------|
| **FR ID** | FR-72 |
| **FR Description** | System SHALL provide management board DORA/NIS 2 training within 60 days of appointment with quarterly ICT risk oversight |
| **Source UC** | PROC-32 |
| **Source Node** | D-08.3.1 |
| **Source Rule** | CR-D-08.3-001 |
| **Domain** | TRN |
| **Verification** | INSPECT |
| **Priority** | HIGH |

---

## 5. TRACEABILITY SUMMARY

| Source | FRs Generated |
|--------|----------------|
| UC-02, UC-06 | FR-72, FR-02 |
| UC-03 | FR-72 |
| PROC-02, PROC-04 | FR-72, FR-14 |
| PROC-03, UC-08 | FR-72 |
| PROC-05, CAP-01 | FR-72 |
| PROC-06 | FR-72 |
| PROC-07 | FR-72 |
| PROC-08, PROC-08.1, PROC-08.2 | FR-72 |
| PROC-09 | FR-72 |
| PROC-10, PROC-13 | FR-72, FR-05, FR-08, FR-10 |
| UC-17, UC-22 | FR-72, FR-03, FR-11 |
| PROC-11, PROC-11.1 | FR-72, FR-09, FR-12 |
| UC-21, UC-21.1 | FR-72, FR-07 |
| CAP-02, PROC-17 | FR-72, FR-14, FR-15 |
| PROC-14, PROC-16 | FR-72, FR-18 |
| PROC-15 (all specializations) | FR-72 |
| UC-26 | FR-72, FR-17 |
| PROC-18 | FR-72 |
| PROC-20, PROC-22 | FR-72, FR-10, FR-12 |
| PROC-21 | FR-72, FR-13 |
| UC-33, UC-33.1 | FR-72, FR-11 |
| UC-34, UC-34.1 | FR-72 |
| PROC-24, PROC-24.1, UC-37-DORA | FR-72 |
| CAP-03 | FR-72 |
| PROC-25, UC-39-DORA | FR-72 |
| PROC-26 | FR-72 |
| PROC-28, UC-46 | FR-72, FR-08, FR-10 |
| PROC-29, PROC-29.1 | FR-72 |
| UC-44, UC-44.1 | FR-72, FR-04, FR-09 |
| PROC-30 | FR-72 |
| UC-47 | FR-72 |
| PROC-31, UC-48-Online, UC-48-Classroom | FR-72, FR-02 |
| CAP-04, UC-49-AI | FR-72, FR-05 |
| PROC-32 | FR-72, FR-12 |
| PROC-33 | FR-72 |
| CAP-05, UC-52-DORA | FR-72, FR-08 |
| PROC-34, PROC-34.1, PROC-34.2 | FR-72, FR-09, FR-10 |
| CAP-06 | FR-72 |
| CAP-07, CAP-07.1 | FR-72 |
| PROC-35 | FR-72 |
| UC-57, UC-57.1 | FR-72 |
| UC-58 | FR-72 |
| PROC-36, PROC-37, PROC-37.1 | FR-72 |
| UC-61, UC-61.1 | FR-72 |
| PROC-38 | FR-72 |

---

## 6. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-28 | Security Architect | Initial creation — 72 FRs across 6 domains |

---

**Next Step:** Proceed to 24_Non_Functional_Requirements.md for NFR derivation.