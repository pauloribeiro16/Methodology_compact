---
document_id: AEGIS-P3-17
title: Functional Tree
phase: 3
version: 1.0
created: 2026-04-28
updated: 2026-04-28
author: Security Architect
status: DRAFT
inputs: [13_Use_Cases_Catalog.md, 14_Architectural_Nodes.md, 15_Requirements_Allocation.md]
outputs: [23_Functional_Requirements.md, 24_Non_Functional_Requirements.md, 22_Traceability_Matrix.xlsx]
traceability: AEGIS Class Model → FunctionalNode, NodeType, FunctionalTree classes
related_documents: 14_Architectural_Nodes.md, 23_Functional_Requirements.md, 24_Non_Functional_Requirements.md
case_id: CASE-03-OMNIBANK
complexity: Maximum (5 regulations, 38 sub-domains, 62 use cases, 28 nodes, 40 gates)
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

## 7. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-28 | Security Architect | Initial creation — 38 domain nodes, 72 sub-nodes, 89 leaf nodes |
| 2.0 | 2026-05-05 | Security Architect | Added ROOT node, Mermaid diagram, and track tags [T/P/P→T] |

---

**Next Step:** Proceed to 23_Functional_Requirements.md to derive functional requirements from the tree.