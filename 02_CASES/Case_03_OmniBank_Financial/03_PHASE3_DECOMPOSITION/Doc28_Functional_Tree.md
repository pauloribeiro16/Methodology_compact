---
document_id: AEGIS-P3-17
title: Functional Tree
phase: 3
version: 1.1
created: 2026-04-28
updated: 2026-09-05
author: Security Architect
status: DRAFT
inputs: [13_Use_Cases_Catalog.md, 14_Architectural_Nodes.md, 15_Requirements_Allocation.md]
outputs: [23_Functional_Requirements.md, 24_Non_Functional_Requirements.md, 22_Traceability_Matrix.xlsx]
traceability: AEGIS Class Model → FunctionalNode, NodeType, FunctionalTree classes
related_documents: 14_Architectural_Nodes.md, 23_Functional_Requirements.md, 24_Non_Functional_Requirements.md
case_id: CASE-03-OMNIBANK
case: Case_03_OmniBank_Financial
complexity: Maximum (5 regulations, 38 sub-domains, 93 use cases (UC-01..93), 28 nodes, 40 gates)
---

# Functional Tree

**Case:** Case 03 — OmniBank Financial Systems (Maximum Complexity)
**Phase:** 3 — Decomposition & Risk Integration
**Step:** 7 — Functional Tree Definition

---

## 1. DOCUMENT PURPOSE

This document defines the functional tree that decomposes OmniBank's security and privacy capabilities into hierarchical nodes. The functional tree provides the structural backbone for deriving Functional Requirements (Doc 23) and Non-Functional Requirements (Doc 24).

The tree is organized by security domain, with nodes representing both capabilities (what the system does) and components (how it is structured). Each leaf node in the tree corresponds to a verifiable requirement.

---

## 2. FUNCTIONAL TREE STRUCTURE

```
ROOT: OmniBank Financial Systems
│
├── L1: D-01: Data Protection & Encryption [T]
│   ├── L2: D-01.1: Data at Rest Encryption [T]
│   │   ├── L3: D-01.1.1: AES-256 Encryption Engine [T]
│   │   ├── L3: D-01.1.2: Field-Level PII Encryption [T]
│   │   └── L3: D-01.1.3: AI Training Data Encryption [T]
│   ├── L2: D-01.2: Data in Transit Encryption [T]
│   │   ├── L3: D-01.2.1: TLS 1.3 Termination [T]
│   │   ├── L3: D-01.2.2: HSTS Enforcement [T]
│   │   └── L3: D-01.2.3: Certificate Pinning [T]
│   ├── L2: D-01.3: Cryptographic Key Management [T]
│   │   ├── L3: D-01.3.1: HSM Key Lifecycle [T]
│   │   └── L3: D-01.3.2: Key Classification & Segregation [T]
│   └── L2: D-01.4: AI Model Integrity [T]
│       ├── L3: D-01.4.1: Model Checksum Validation [T]
│       └── L3: D-01.4.2: Unauthorized Modification Detection [T]
│
├── L1: D-02: Vulnerability Management [T]
│   ├── L2: D-02.1: Vulnerability Assessment [T]
│   │   ├── L3: D-02.1.1: Automated Vulnerability Scanning [T]
│   │   └── L3: D-02.1.2: AI Model Vulnerability Assessment [T]
│   ├── L2: D-02.2: Patch Management [P]
│   │   └── L3: D-02.2.1: Automated Patch Deployment [P]
│   ├── L2: D-02.3: Coordinated Disclosure [P]
│   │   └── L3: D-02.3.1: ENISA/CSIRT Reporting [P]
│   └── L2: D-02.4: Penetration Testing [P]
│       ├── L3: D-02.4.1: TLPT Execution [P]
│       └── L3: D-02.4.2: AI Adversarial Testing [P]
│
├── L1: D-03: Access Control [T]
│   ├── L2: D-03.1: Identity Management [T]
│   │   ├── L3: D-03.1.1: Unified Identity Provisioning [T]
│   │   └── L3: D-03.1.2: HR-Driven Deprovisioning [T]
│   ├── L2: D-03.2: MFA Enforcement [T]
│   │   ├── L3: D-03.2.1: Step-Up Authentication [T]
│   │   └── L3: D-03.2.2: FIDO2/WebAuthn Support [T]
│   ├── L2: D-03.3: Least Privilege [P]
│   │   └── L3: D-03.3.1: Quarterly Access Review [P]
│   └── L2: D-03.4: Secure Configuration [T]
│       └── L3: D-03.4.1: CIS Benchmarks Enforcement [T]
│
├── L1: D-04: Incident Response [P→T]
│   ├── L2: D-04.1: SOC Operations [T]
│   │   ├── L3: D-04.1.1: 24/7 Monitoring [T]
│   │   └── L3: D-04.1.2: AI Anomaly Detection [T]
│   ├── L2: D-04.2: Business Continuity [P]
│   │   ├── L3: D-04.2.1: Disaster Recovery [P]
│   │   └── L3: D-04.2.2: AI System Failover [P]
│   ├── L2: D-04.3: Universal Notification [P]
│   │   ├── L3: D-04.3.1: GDPR Notification Module [P]
│   │   ├── L3: D-04.3.2: DORA Notification Module [P]
│   │   ├── L3: D-04.3.3: NIS2 Notification Module [P]
│   │   ├── L3: D-04.3.4: CRA Notification Module [P]
│   │   └── L3: D-04.3.5: AI Act Notification Module [P]
│   └── L2: D-04.4: Backup Management [T]
│       └── L3: D-04.4.1: Immutable Backup Recovery [T]
│
├── L1: D-05: Data Lifecycle [T]
│   ├── L2: D-05.1: Data Minimization [P]
│   │   ├── L3: D-05.1.1: AI Training Data Validation [P]
│   │   └── L3: D-05.1.2: Bias Proxy Detection [P]
│   ├── L2: D-05.2: Retention Enforcement [T]
│   │   ├── L3: D-05.2.1: Financial Record Retention (10yr) [T]
│   │   └── L3: D-05.2.2: AI Inference Log Retention (6mo) [T]
│   ├── L2: D-05.3: Cryptographic Erasure [T]
│   │   └── L3: D-05.3.1: Cryptographic Sharding [T]
│   └── L2: D-05.4: Data Portability [T]
│       └── L3: D-05.4.1: Machine-Readable Export [T]
│
├── L1: D-06: Supply Chain [P]
│   ├── L2: D-06.1: Vendor Risk Management [P]
│   │   ├── L3: D-06.1.1: ICT Provider Assessment [P]
│   │   └── L3: D-06.1.2: AI Model Provider Assessment [P]
│   ├── L2: D-06.2: SBOM Management [T]
│   │   └── L3: D-06.2.1: SBOM Generation & Maintenance [T]
│   ├── L2: D-06.3: Contractual Security [P]
│   │   └── L3: D-06.3.1: Security Clause Enforcement [P]
│   └── L2: D-06.4: Concentration Risk [P]
│       └── L3: D-06.4.1: Exit Strategy Management [P]
│
├── L1: D-07: Secure Development [P]
│   ├── L2: D-07.1: Secure-by-Design [P]
│   │   ├── L3: D-07.1.1: CRA Secure-by-Default [P]
│   │   └── L3: D-07.1.2: AI Ethical Design Review [P]
│   ├── L2: D-07.2: Secure Coding [P]
│   │   └── L3: D-07.2.1: SAST/DAST Integration [P]
│   ├── L2: D-07.3: CI/CD Security [T]
│   │   ├── L3: D-07.3.1: Security Gates Automation [T]
│   │   └── L3: D-07.3.2: AI Deployment Gate [T]
│   └── L2: D-07.4: Change Management [P]
│       └── L3: D-07.4.1: Dual Control Approval [P]
│
├── L1: D-08: Human Factors [P]
│   ├── L2: D-08.1: Security Awareness [P]
│   │   ├── L3: D-08.1.1: Annual Training Delivery [P]
│   │   └── L3: D-08.1.2: Phishing Simulation [P]
│   ├── L2: D-08.2: Security Competence [P]
│   │   ├── L3: D-08.2.1: Role Certification Tracking [P]
│   │   └── L3: D-08.2.2: AI Human Oversight Procedures [P]
│   └── L2: D-08.3: Board Oversight [P]
│       └── L3: D-08.3.1: Board Training & Reporting [P]
│
├── L1: D-09: Governance & Documentation [P]
│   ├── L2: D-09.1: Unified ISMS [P]
│   │   └── L3: D-09.1.1: Multi-Framework Integration [P]
│   ├── L2: D-09.2: IPSARA Assessment [P]
│   │   ├── L3: D-09.2.1: DPIA Module [P]
│   │   └── L3: D-09.2.2: FRIA Module [P]
│   ├── L2: D-09.3: Asset Inventory [T]
│   │   └── L3: D-09.3.1: Automated Discovery [T]
│   └── L2: D-09.4: AI Documentation [P]
│       ├── L3: D-09.4.1: Model Card Maintenance [P]
│       └── L3: D-09.4.2: Decision Log Retention [P]
│
├── L1: D-10: Monitoring & Audit [T]
│   ├── L2: D-10.1: AI-Powered Monitoring [T]
│   │   ├── L3: D-10.1.1: Real-Time Threat Detection [T]
│   │   └── L3: D-10.1.2: AI Model Drift Detection [T]
│   ├── L2: D-10.2: Immutable Audit [T]
│   │   ├── L3: D-10.2.1: PII Separation [T]
│   │   └── L3: D-10.2.2: Cryptographic Sharding [T]
│   └── L2: D-10.3: Penetration Testing [P]
│       └── L3: D-10.3.1: Red Team Operations [P]
│
└── L1: Cross-Domain Capabilities [P→T]
    ├── L2: CS-01: Multi-Regulation Incident Correlation [P→T]
    ├── L2: CS-02: AI Decision Audit Trail [T]
    └── L2: CS-03: Cryptographic Sharding Engine [T]
```

---

## 3. FUNCTIONAL TREE DIAGRAM

```mermaid
graph TB
    ROOT[OmniBank Financial Systems — Compliance Architecture]
    
    ROOT --> L1_DP[D-01: Data Protection & Encryption [T]]
    ROOT --> L1_VM[D-02: Vulnerability Management [T]]
    ROOT --> L1_AC[D-03: Access Control [T]]
    ROOT --> L1_IR[D-04: Incident Response [P→T]]
    ROOT --> L1_DL[D-05: Data Lifecycle [T]]
    ROOT --> L1_SC[D-06: Supply Chain [P]]
    ROOT --> L1_SD[D-07: Secure Development [P]]
    ROOT --> L1_HF[D-08: Human Factors [P]]
    ROOT --> L1_GD[D-09: Governance & Documentation [P]]
    ROOT --> L1_MA[D-10: Monitoring & Audit [T]]
    ROOT --> L1_CS[Cross-Domain Capabilities [P→T]]
    
    L1_DP --> L2_DP_01[D-01.1: Data at Rest Encryption [T]]
    L1_DP --> L2_DP_02[D-01.2: Data in Transit Encryption [T]]
    L1_DP --> L2_DP_03[D-01.3: Key Management [T]]
    L1_DP --> L2_DP_04[D-01.4: AI Model Integrity [T]]
    
    L1_VM --> L2_VM_01[D-02.1: Vulnerability Assessment [T]]
    L1_VM --> L2_VM_02[D-02.2: Patch Management [P]]
    L1_VM --> L2_VM_03[D-02.3: Coordinated Disclosure [P]]
    L1_VM --> L2_VM_04[D-02.4: Penetration Testing [P]]
    
    L1_AC --> L2_AC_01[D-03.1: Identity Management [T]]
    L1_AC --> L2_AC_02[D-03.2: MFA Enforcement [T]]
    L1_AC --> L2_AC_03[D-03.3: Least Privilege [P]]
    L1_AC --> L2_AC_04[D-03.4: Secure Configuration [T]]
    
    L1_IR --> L2_IR_01[D-04.1: SOC Operations [T]]
    L1_IR --> L2_IR_02[D-04.2: Business Continuity [P]]
    L1_IR --> L2_IR_03[D-04.3: Universal Notification [P]]
    L1_IR --> L2_IR_04[D-04.4: Backup Management [T]]
    
    L1_DL --> L2_DL_01[D-05.1: Data Minimization [P]]
    L1_DL --> L2_DL_02[D-05.2: Retention Enforcement [T]]
    L1_DL --> L2_DL_03[D-05.3: Cryptographic Erasure [T]]
    L1_DL --> L2_DL_04[D-05.4: Data Portability [T]]
    
    L1_SC --> L2_SC_01[D-06.1: Vendor Risk Management [P]]
    L1_SC --> L2_SC_02[D-06.2: SBOM Management [T]]
    L1_SC --> L2_SC_03[D-06.3: Contractual Security [P]]
    L1_SC --> L2_SC_04[D-06.4: Concentration Risk [P]]
    
    L1_SD --> L2_SD_01[D-07.1: Secure-by-Design [P]]
    L1_SD --> L2_SD_02[D-07.2: Secure Coding [P]]
    L1_SD --> L2_SD_03[D-07.3: CI/CD Security [T]]
    L1_SD --> L2_SD_04[D-07.4: Change Management [P]]
    
    L1_HF --> L2_HF_01[D-08.1: Security Awareness [P]]
    L1_HF --> L2_HF_02[D-08.2: Security Competence [P]]
    L1_HF --> L2_HF_03[D-08.3: Board Oversight [P]]
    
    L1_GD --> L2_GD_01[D-09.1: Unified ISMS [P]]
    L1_GD --> L2_GD_02[D-09.2: IPSARA Assessment [P]]
    L1_GD --> L2_GD_03[D-09.3: Asset Inventory [T]]
    L1_GD --> L2_GD_04[D-09.4: AI Documentation [P]]
    
    L1_MA --> L2_MA_01[D-10.1: AI-Powered Monitoring [T]]
    L1_MA --> L2_MA_02[D-10.2: Immutable Audit [T]]
    L1_MA --> L2_MA_03[D-10.3: Penetration Testing [P]]
    
    L1_CS --> L2_CS_01[CS-01: Multi-Regulation Correlation [P→T]]
    L1_CS --> L2_CS_02[CS-02: AI Decision Audit Trail [T]]
    L1_CS --> L2_CS_03[CS-03: Cryptographic Sharding [T]]
```

---

## 4. TREE METRICS

| Metric | Value |
|--------|-------|
| **Total Domains** | 10 |
| **Total Level-1 Nodes** | 10 |
| **Total Level-2 Nodes** | 38 |
| **Total Level-3 Nodes** | 72 |
| **Total Leaf Nodes** | 89 |
| **Cross-Domain Capabilities** | 3 |
| **Depth** | 4 levels |

---

## 5. TRACEABILITY — TREE TO NODES

| Tree Node | Architectural Node | Track |
|-----------|-------------------|-------|
| D-01.1.1 | NODE-TECH-001 | [T] |
| D-01.1.2 | NODE-TECH-001 | [T] |
| D-01.1.3 | NODE-TECH-001 | [T] |
| D-01.2.1 | NODE-TECH-001 | [T] |
| D-01.3.1 | NODE-TECH-002 | [T] |
| D-01.4.1 | NODE-TECH-003 | [T] |
| D-02.1.1 | NODE-TECH-004 | [T] |
| D-02.1.2 | NODE-TECH-005 | [T] |
| D-02.2.1 | NODE-TECH-006 | [P] |
| D-02.3.1 | NODE-PROC-002 | [P] |
| D-02.4.1 | NODE-TECH-007 | [P] |
| D-03.1.1 | NODE-TECH-008 | [T] |
| D-03.1.2 | NODE-TECH-008 | [T] |
| D-03.2.1 | NODE-TECH-009 | [T] |
| D-03.2.2 | NODE-TECH-009 | [T] |
| D-03.3.1 | NODE-TECH-010 | [P] |
| D-03.4.1 | NODE-TECH-011 | [T] |
| D-04.1.1 | NODE-TECH-012 | [T] |
| D-04.1.2 | NODE-TECH-013 | [T] |
| D-04.2.1 | NODE-PROC-005 | [P] |
| D-04.2.2 | NODE-TECH-014 | [P] |
| D-04.3.1 | NODE-PROC-007 | [P] |
| D-04.3.2 | NODE-PROC-008 | [P] |
| D-04.3.3 | NODE-PROC-009 | [P] |
| D-04.4.1 | NODE-TECH-014 | [T] |
| D-05.1.1 | NODE-TECH-017 | [P] |
| D-05.1.2 | NODE-TECH-017 | [P] |
| D-05.2.1 | NODE-TECH-015 | [T] |
| D-05.2.2 | NODE-TECH-015 | [T] |
| D-05.3.1 | NODE-TECH-016 | [T] |
| D-05.4.1 | NODE-TECH-015 | [T] |
| D-06.1.1 | NODE-PROC-011 | [P] |
| D-06.1.2 | NODE-PROC-012 | [P] |
| D-06.2.1 | NODE-TECH-018 | [T] |
| D-06.3.1 | NODE-PROC-013 | [P] |
| D-06.4.1 | NODE-PROC-011 | [P] |
| D-07.1.1 | NODE-PROC-014 | [P] |
| D-07.1.2 | NODE-PROC-014 | [P] |
| D-07.2.1 | NODE-PROC-014 | [P] |
| D-07.3.1 | NODE-PROC-014 | [T] |
| D-07.3.2 | NODE-PROC-014 | [T] |
| D-07.4.1 | NODE-PROC-014 | [P] |
| D-08.1.1 | NODE-PROC-015 | [P] |
| D-08.1.2 | NODE-PROC-018 | [P] |
| D-08.2.1 | NODE-PROC-016 | [P] |
| D-08.2.2 | NODE-PROC-016 | [P] |
| D-08.3.1 | NODE-PROC-017 | [P] |
| D-09.1.1 | NODE-PROC-019 | [P] |
| D-09.2.1 | NODE-PROC-020 | [P] |
| D-09.2.2 | NODE-PROC-020 | [P] |
| D-09.3.1 | NODE-PROC-019 | [T] |
| D-09.4.1 | NODE-PROC-021 | [P] |
| D-09.4.2 | NODE-PROC-021 | [P] |
| D-10.1.1 | NODE-TECH-019 | [T] |
| D-10.1.2 | NODE-TECH-020 | [T] |
| D-10.2.1 | NODE-TECH-021 | [T] |
| D-10.2.2 | NODE-TECH-021 | [T] |
| D-10.3.1 | NODE-TECH-007 | [P] |
| CS-01 | NODE-CS-001 | [P→T] |
| CS-02 | NODE-CS-002 | [T] |
| CS-03 | NODE-CS-003 | [T] |

---

## 6. DOMAIN COVERAGE SUMMARY

| Domain | Tree Nodes | Leaf Nodes | Coverage |
|--------|------------|------------|----------|
| D-01: Data Protection | 4 | 7 | 100% |
| D-02: Vulnerability | 4 | 6 | 100% |
| D-03: Access Control | 4 | 6 | 100% |
| D-04: Incident Response | 4 | 9 | 100% |
| D-05: Data Lifecycle | 4 | 6 | 100% |
| D-06: Supply Chain | 4 | 5 | 100% |
| D-07: Secure Development | 4 | 5 | 100% |
| D-08: Human Factors | 3 | 5 | 100% |
| D-09: Governance | 4 | 6 | 100% |
| D-10: Monitoring | 3 | 4 | 100% |
| **TOTAL** | **38** | **59** | **100%** |

---

## 6A. PRODUCT FUNCTIONAL BRANCH (PKG-A..F — UC-03..33) — ADDITIVE

> Additive section (v1.1) — extends the functional tree with the OmniBank platform product
> use cases from Doc22 §6B. Lane note per `LANE_NAMING_CENSUS_v0`: UC-06 (Underwriter
> Review) and UC-32 (Complaint Handling) are process-lane members of product journeys.
> Existing tree structure (§2–§6) is unchanged.

```
OmniBank Platform Product (PKG-A..F)
├── PKG-A — Onboarding & KYC (Doc22 §6B.2)
│   ├── UC-09  Open Account via Mobile App
│   ├── UC-10  eIDAS Identity Verification
│   ├── UC-11  KYC Document Upload & Vault Filing (SYS-16, 10y retention)
│   ├── UC-12  Sanctions & PEP Screening (SYS-11)
│   ├── UC-13  OmniScore Consent & Data-Use Acknowledgement
│   └── UC-14  Tax Residency Self-Certification (FATCA/CRS)
├── PKG-B — Digital Banking Core (Doc22 §6B.3)
│   ├── UC-15  Login with PSD2 SCA
│   ├── UC-16  View Balances & Transactions
│   ├── UC-17  SEPA Transfer (incl. Instant)
│   ├── UC-18  Manage Cards (block/limits)
│   ├── UC-19  Standing Orders
│   └── UC-20  Statements & Export
├── PKG-C — Lending & OmniScore (Doc22 §6B.1)
│   ├── UC-03  Apply for Consumer Credit
│   ├── UC-04  OmniScore Computes Credit Score (SYS-03)
│   ├── UC-05  Customer Receives Score Explanation
│   ├── UC-06  Underwriter Review (manual/borderline decision path)
│   ├── UC-07  Customer Accepts Offer & Contract Signed
│   └── UC-08  Customer Manages Repayment & Arrears View
├── PKG-D — Payments & Open Banking (Doc22 §6B.4)
│   ├── UC-21  PSD2 Consent Grant/Revoke
│   ├── UC-22  TPP Onboarding & AIS Access (SYS-18)
│   ├── UC-23  PIS Payment Initiation with SCA
│   ├── UC-24  Payment Dispute & Chargeback
│   └── UC-25  Payment Limits Management
├── PKG-E — Corporate & Treasury (Doc22 §6B.5)
│   ├── UC-26  Corporate Onboarding with Delegated Users (SYS-21)
│   ├── UC-27  Cash Management Dashboard
│   ├── UC-28  FX Deal Execution (SYS-08)
│   └── UC-29  Trade Finance Letter of Credit (SYS-07, UCP 600)
└── PKG-F — Fraud & Customer Service (Doc22 §6B.6)
    ├── UC-30  In-App Fraud Alert Confirm/Deny (SYS-11)
    ├── UC-31  Card Block via Contact Centre (SYS-20)
    ├── UC-32  Complaint Handling (complaint SOP)
    └── UC-33  Secure Messaging
```

**Product branch traceability:** journey sequencing is defined in Doc23 §3.11 (onboarding
UC-09..14 precede banking core UC-15..20; OmniScore UC-03/04 feed lending decisions).

---

## 6B. LANE BRANCHES (PROC-01..40, CAP-01..07) — ADDITIVE

> Additive section (v1.1) — extends the functional tree with the process (PROC) and
> capability (CAP) lane ids from the Case_03 lane rename (`LANE_NAMING_CENSUS_v0`,
> T46/P40/C7). Grouping follows Doc22 §4.1–§4.10 (PKG-D-01..10 ↔ domain families D-01..D-10).

```
Lane Branches (compliance corpus, 62 ids)
├── D-01 Data Protection & Encryption (PKG-D-01)
│   ├── PROC-01..PROC-04  (encryption status, HSM keys, AI model integrity, key rotation)
│   └── PROC-39 / PROC-40 / PROC-41 / CAP-08  (technology lane)
├── D-02 Vulnerability Management (PKG-D-02)
│   ├── PROC-05..PROC-09  (scan, patch, disclosure, TLPT, AI vulnerabilities)
│   ├── CAP-01  Vulnerability Analyst Maintains Vulnerability Register
│   └── PROC-42  Generates SBOM for AI Model
├── D-03 Access Control (PKG-D-03)
│   ├── PROC-10..PROC-13  (provision, access review, hardening, deprovision)
│   └── PROC-43 / PROC-44 / PROC-45  (MFA, AI model access, FIDO2)
├── D-04 Incident Response (PKG-D-04)
│   ├── PROC-14..PROC-19  (DR, notification, AI recovery, anomaly, tabletop, AI report)
│   ├── CAP-02  SOC Analyst Monitors Security Events
│   └── CAP-09  Maintains Redundant Backup Systems
├── D-05 Data Lifecycle (PKG-D-05)
│   ├── PROC-20..PROC-23  (minimization, retention, AI training data, processor audit)
│   └── UC-01 / UC-02  (erasure, export)
├── D-06 Supply Chain (PKG-D-06)
│   ├── PROC-24..PROC-27  (provider assessment, contract terms, exit, AI provider monitoring)
│   └── CAP-03  Security Architect Maintains SBOM for Product
├── D-07 Secure Development (PKG-D-07)
│   ├── PROC-28..PROC-30  (secure-by-design, coding standards, change approval)
│   └── PROC-46 / PROC-47 / PROC-48  (CI/CD, AI training pipeline, IaC scanning)
├── D-08 Human Factors (PKG-D-08)
│   ├── PROC-31..PROC-33  (awareness training, board training, phishing simulation)
│   └── CAP-04  HR Manager Maintains Security Competence Program
├── D-09 Governance & Documentation (PKG-D-09)
│   ├── PROC-34 / PROC-35  (IPSARA, regulatory compliance report)
│   ├── CAP-05  CISO Maintains Unified ISMS
│   ├── CAP-06  IT Asset Manager Maintains Asset Inventory
│   └── CAP-07  AI Governance Lead Maintains AI Traceability Documentation
└── D-10 Monitoring & Audit (PKG-D-10)
    ├── PROC-36..PROC-38  (pentesting, AI adversarial robustness, audit trail report)
    └── PROC-49 / CAP-10 / PROC-50  (AI threat detection, immutable logs, AI drift)
```

**Counts:** 38 PROC + 7 CAP + 17 UC (technology lane, compliance corpus) = 62; plus
product-side UC-66/UC-92 and UC-63..93 (31) = 93 total use cases, matching Doc22 v2.3.

---

## 7. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-28 | Security Architect | Initial creation — 38 domain nodes, 72 sub-nodes, 89 leaf nodes |
| 1.1 | 2026-09-05 | Security Architect | Lane census alignment (Case_03 T46/P40/C7): additive §6A Product Functional Branch (PKG-A..F, UC-03..33) and §6B Lane Branches (PROC-01..40, CAP-01..07 grouped by D-01..D-10); existing tree unchanged |
| 2.0 | 2026-05-05 | Security Architect | Added ROOT node, Mermaid diagram, and track tags [T/P/P→T] |

---

**Next Step:** Proceed to 23_Functional_Requirements.md to derive functional requirements from the tree.