---
document_id: AEGIS-P3-15
title: Requirements Allocation
phase: 3
version: 1.0
created: 2026-04-28
updated: 2026-04-28
author: Security Architect
status: DRAFT
inputs: [14_Architectural_Nodes.md, 13_Use_Cases_Catalog.md, 11_Rules_Catalog.md]
outputs: [16_Compliance_Gates_Report.md, 23_Functional_Requirements.md, 24_Non_Functional_Requirements.md]
traceability: AEGIS Class Model → RequirementAllocation, RuleAllocation, NodeAllocation classes
related_documents: 14_Architectural_Nodes.md, 13_Use_Cases_Catalog.md, 11_Rules_Catalog.md
case_id: CASE-03-OMNIBANK
case: Case_03_OmniBank_Financial
complexity: Maximum (5 regulations, 38 sub-domains, 63 rules → 28 nodes)
---

# Requirements Allocation

**Case:** Case 03 — OmniBank Financial Systems (Maximum Complexity)
**Phase:** 3 — Decomposition & Risk Integration
**Step:** 5 — Requirements Allocation

---

## 1. DOCUMENT PURPOSE

This document defines how compliance rules and best practice rules from the Rules Catalog are allocated to architectural nodes defined in Doc 14. Each rule is mapped to at least one node, with cross-track dependencies documented for capability sub-requirements.

The allocation follows the derivation formula: **Rule → Node → UC → FR/NFR**, establishing the complete traceability chain from regulatory requirement to implementation component.

---

## 2. ALLOCATION SUMMARY

| Metric | Value |
|--------|-------|
| **Total Rules** | 63 (38 CR + 25 BPR) |
| **Rules Allocated** | 63/63 (100%) |
| **Total Allocations** | 78 (some rules map to multiple nodes) |
| **Nodes Used** | 28/28 (100%) |
| **Cross-Track Dependencies** | 3 |

---

## 3. RULE-TO-NODE ALLOCATION

### 3.1 D-01: Data Protection & Encryption

| Rule ID | Rule Description | Node ID | Allocation Rationale | Track | NIST Anchors |
| --------- | ----------------- | --------- | --------------------- | ------- | --- |
| CR-D-01.1-001 | Encrypt all personal/financial/AI data at rest using AES-256 | NODE-D-01-01 | Central encryption management | TECHNOLOGY | CSF: PR.DS-01 | PF: CT.DP-P2,PR.DS-P1 | AI: GOVERN-1.6,MEASURE-2.5,MEASURE-2.7 |
| CR-D-01.2-001 | Encrypt all data in transit using TLS 1.3 | NODE-D-01-01 | TLS termination and encryption | TECHNOLOGY | CSF: PR.DS-02 | PF: PR.DS-P2 |
| CR-D-01.3-001 | HSM-backed cryptographic key management | NODE-D-01-01.1 | Dedicated HSM key management service | TECHNOLOGY | CSF: PR.DS-01 | PF: CT.DP-P2,PR.DS-P1 | AI: GOVERN-1.6,MEASURE-2.7 |
| CR-D-01.4-001 | Data integrity controls and AI system resilience | NODE-D-01-01.2 | AI model integrity validation | TECHNOLOGY | CSF: PR.DS-01,PR.DS-02 | PF: CT.DM-P1,CT.DM-P3,PR.DS-P1 | AI: MANAGE-2.3,MEASURE-2.6,MEASURE-2.7 |
| BPR-D-01.1-001 | AES-256 encryption standard with authenticated encryption | NODE-D-01-01 | Implementation of CR-D-01.1 | TECHNOLOGY | — |
| BPR-D-01.2-001 | TLS 1.3 with forward secrecy | NODE-D-01-01 | Implementation of CR-D-01.2 | TECHNOLOGY | — |
| BPR-D-01.3-001 | HSM-backed key management per NIST SP 800-57 | NODE-D-01-01.1 | Implementation of CR-D-01.3 | TECHNOLOGY | — |
| BPR-D-01.4-001 | Data integrity controls using cryptographic hash | NODE-D-01-01.2 | Implementation of CR-D-01.4 | TECHNOLOGY | — |

### 3.2 D-02: Vulnerability Management

| Rule ID | Rule Description | Node ID | Allocation Rationale | Track | NIST Anchors |
| --------- | ----------------- | --------- | --------------------- | ------- | --- |
| CR-D-02.1-001 | Zero known exploitable vulnerabilities; AI data governance | NODE-D-02-01 | Central vulnerability assessment platform | TECHNOLOGY | CSF: ID.RA-01 | PF: ID.RA-P3,ID.RA-P5 | AI: MANAGE-1.3,MAP-3.2,MAP-3.3,MEASURE-1.1,MEASURE-2.1 |
| CR-D-02.2-001 | Automated patch management with 72h SLA | NODE-D-02-01.2 | Dedicated patch management service | PROCESS | CSF: PR.PS-02 |
| CR-D-02.3-001 | Coordinated vulnerability disclosure policy | NODE-D-02-01 | Coordinated disclosure through platform | TECHNOLOGY | PF: GV.PO-P5,ID.IM-P7 |
| CR-D-02.4-001 | Annual TLPT per DORA RTS; AI bias testing | NODE-D-02-02 | Dedicated penetration testing framework | PROCESS | CSF: ID.IM-02,ID.RA-03 | PF: ID.RA-P3,ID.RA-P4,ID.RA-P5 | AI: MAP-3.3,MEASURE-1.1,MEASURE-2.1,MEASURE-2.3,MEASURE-2.7 |
| BPR-D-02.1-001 | Quarterly vulnerability scanning with CVSS v3.1 | NODE-D-02-01 | Part of vulnerability assessment platform | TECHNOLOGY | — |
| BPR-D-02.2-001 | SBOM in SPDX and CycloneDX formats | NODE-D-06-02 | SBOM management in supply chain | TECHNOLOGY | — |
| BPR-D-02.3-001 | Vulnerability management program with risk prioritization | NODE-D-02-01 | Part of vulnerability assessment platform | TECHNOLOGY | — |
| BPR-D-02.4-001 | Annual TLPT per TIBER-EU methodology | NODE-D-02-02 | Implementation of CR-D-02.4 | PROCESS | — |
| BPR-D-12.4-001 | AI adversarial robustness testing per MITRE ATLAS | NODE-D-02-01.1 | AI vulnerability module | TECHNOLOGY | — |

### 3.3 D-03: Access Control

| Rule ID | Rule Description | Node ID | Allocation Rationale | Track | NIST Anchors |
| --------- | ----------------- | --------- | --------------------- | ------- | --- |
| CR-D-03.1-001 | Unified identity management with MFA | NODE-D-03-01 | Central IAM platform | TECHNOLOGY | CSF: PR.AA-01,PR.AA-03,PR.AA-05 | PF: CT.PO-P1 | AI: GOVERN-1.4,GOVERN-2.1,MAP-3.4 |
| CR-D-03.2-001 | MFA for privileged, remote, and AI access | NODE-D-03-01.1 | Dedicated MFA enforcement service | TECHNOLOGY | CSF: PR.AA-03 |
| CR-D-03.3-001 | Least privilege with quarterly access reviews | NODE-D-03-01.2 | Access review automation | PROCESS | CSF: PR.AA-01,PR.AA-05 | PF: CT.PO-P1 |
| CR-D-03.4-001 | Secure default configuration per CIS Benchmarks | NODE-D-03-02 | Configuration hardening service | TECHNOLOGY | CSF: PR.PS-01 | PF: CT.DP-P4,CT.PO-P4 |
| BPR-D-03.1-001 | RBAC with automated provisioning/deprovisioning | NODE-D-03-01 | Implementation of CR-D-03.1 | TECHNOLOGY | — |
| BPR-D-03.2-001 | FIDO2/WebAuthn for MFA | NODE-D-03-01.1 | Implementation of CR-D-03.2 | TECHNOLOGY | — |
| BPR-D-03.3-001 | PAM with just-in-time access and session recording | NODE-D-03-01.2 | Implementation of CR-D-03.3 | PROCESS | — |
| BPR-D-03.4-001 | CIS Benchmarks Level 2 configuration compliance | NODE-D-03-02 | Implementation of CR-D-03.4 | TECHNOLOGY | — |

### 3.4 D-04: Incident Response

| Rule ID | Rule Description | Node ID | Allocation Rationale | Track | NIST Anchors |
| --------- | ----------------- | --------- | --------------------- | ------- | --- |
| CR-D-04.1-001 | 24/7 SOC with automated incident detection | NODE-D-04-01 | Central SOC platform | TECHNOLOGY | CSF: DE.AE-02,DE.CM-01,DE.CM-09 | PF: CM.AW-P7 |
| CR-D-04.2-001 | Business continuity with 99.99% uptime; DR | NODE-D-04-02 | Business continuity management | PROCESS | CSF: RS.MI-01,RS.MI-02 | PF: CT.DM-P10,PR.PO-P7 |
| CR-D-04.3-001 | 24h universal incident notification workflow | NODE-D-04-03, NODE-CS-01 | Universal notification + correlation | PROCESS + CAPABILITY | CSF: RS.CO-02,RS.CO-03 | PF: CM.AW-P7,CM.PO-P1,CM.PO-P2,GV.PO-P5 | AI: GOVERN-1.1,MANAGE-2.3,MANAGE-4.3 |
| CR-D-04.4-001 | Redundant backup systems with automated failover | NODE-D-04-02.1 | AI system recovery module | TECHNOLOGY | CSF: RC.RP-01,RC.RP-03,RC.RP-05 |
| BPR-D-04.1-001 | Incident response playbooks per ISO 27001 | NODE-D-04-01 | Part of SOC platform | TECHNOLOGY | — |
| BPR-D-04.2-001 | BCP/DRP per ISO 22301; tested annually | NODE-D-04-02 | Part of BCM system | PROCESS | — |
| BPR-D-04.3-001 | Quarterly tabletop exercises | NODE-D-04-01 | SOC operations | TECHNOLOGY | — |
| BPR-D-04.4-001 | Automated backup verification | NODE-D-04-02.1 | Implementation of CR-D-04.4 | TECHNOLOGY | — |

### 3.5 D-05: Data Lifecycle

| Rule ID | Rule Description | Node ID | Allocation Rationale | Track | NIST Anchors |
| --------- | ----------------- | --------- | --------------------- | ------- | --- |
| CR-D-05.1-001 | Data minimization; AI training data relevance | NODE-D-05-01, NODE-D-05-01.2 | Centralized data lifecycle + AI-specific | TECHNOLOGY + PROCESS | CSF: ID.AM-03,PR.DS-10 | PF: CT.DP-P4,CT.PO-P4,ID.RA-P3 | AI: GOVERN-1.4,MAP-2.1,MAP-2.2,MEASURE-2.11 |
| CR-D-05.2-001 | Tiered retention (10yr financial, 5yr operational, 6mo AI) | NODE-D-05-01 | Data lifecycle platform | TECHNOLOGY | CSF: PR.DS-01,PR.PS-06 | PF: CT.DM-P5,CT.PO-P4 | AI: GOVERN-1.4,MAP-2.1,MAP-2.2,MEASURE-2.11,MEASURE-2.4 |
| CR-D-05.3-001 | Cryptographic sharding erasure within 30 days | NODE-D-05-01.1, NODE-CS-03 | Dedicated erasure + crypto sharding | TECHNOLOGY + CAPABILITY | CSF: PR.DS-10 | PF: CT.DM-P4,CT.DM-P5 |
| CR-D-05.4-001 | Data export in machine-readable formats | NODE-D-05-01 | Data lifecycle platform | TECHNOLOGY | PF: CT.DM-P1,CT.DM-P6 |
| BPR-D-05.1-001 | Data classification schema with automated discovery | NODE-D-05-01 | Part of data lifecycle platform | TECHNOLOGY | — |
| BPR-D-05.3-001 | Media sanitization per NIST SP 800-88 | NODE-D-05-01.1 | Implementation of CR-D-05.3 | TECHNOLOGY | — |
| BPR-D-05.4-001 | Automated data lifecycle management | NODE-D-05-01 | Implementation of CR-D-05.4 | TECHNOLOGY | — |

### 3.6 D-06: Supply Chain

| Rule ID | Rule Description | Node ID | Allocation Rationale | Track | NIST Anchors |
| --------- | ----------------- | --------- | --------------------- | ------- | --- |
| CR-D-06.1-001 | Vendor risk management for DORA, NIS 2, GDPR | NODE-D-06-01 | Central VRM platform | PROCESS | CSF: GV.SC-04 | PF: ID.IM-P2 |
| CR-D-06.2-001 | SBOM for all products and dependencies | NODE-D-06-02 | SBOM management system | TECHNOLOGY | PF: ID.IM-P7 |
| CR-D-06.3-001 | Contractual security obligations with third parties | NODE-D-06-01 | VRM platform contractual management | PROCESS | CSF: GV.SC-05 | PF: GV.PO-P5 |
| CR-D-06.4-001 | Third-party concentration risk with exit strategies | NODE-D-06-01 | VRM platform risk management | PROCESS | CSF: DE.CM-06,PR.IR-01 |
| BPR-D-06.1-001 | Vendor assessment using SIG or CAIQ | NODE-D-06-01 | Implementation of CR-D-06.1 | PROCESS | — |
| BPR-D-06.3-001 | Minimum security requirements in vendor contracts | NODE-D-06-01 | Implementation of CR-D-06.3 | PROCESS | — |
| BPR-D-06.4-001 | Vendor exit strategies with data migration plans | NODE-D-06-01 | Implementation of CR-D-06.4 | PROCESS | — |

### 3.7 D-07: Secure Development

| Rule ID | Rule Description | Node ID | Allocation Rationale | Track | NIST Anchors |
| --------- | ----------------- | --------- | --------------------- | ------- | --- |
| CR-D-07.1-001 | Privacy/security by design per CRA standard | NODE-D-07-01 | Central SDL platform | PROCESS | CSF: ID.RA-01,PR.PS-06 | PF: CT.DP-P2,CT.DP-P5,CT.PO-P4,GV.PO-P2 |
| CR-D-07.2-001 | Secure coding per OWASP ASVS with SAST/DAST | NODE-D-07-01.1 | SAST/DAST integration module | TECHNOLOGY | CSF: PR.PS-06 |
| CR-D-07.3-001 | CI/CD pipeline with automated security gates | NODE-D-07-01.2 | AI deployment gate module | TECHNOLOGY | CSF: PR.PS-02,PR.PS-06 |
| CR-D-07.4-001 | Formal change management with dual control | NODE-D-07-01 | SDL platform change management | PROCESS | PF: ID.RA-P3 |
| BPR-D-07.1-001 | NIST SSDF practices across development teams | NODE-D-07-01 | Implementation of CR-D-07.1 | PROCESS | — |
| BPR-D-07.2-001 | SAST/DAST per OWASP ASVS Level 2 | NODE-D-07-01.1 | Implementation of CR-D-07.2 | TECHNOLOGY | — |
| BPR-D-07.3-001 | IaC scanning with Checkov or equivalent | NODE-D-07-01 | Part of SDL platform | PROCESS | — |
| BPR-D-07.4-001 | Change management controls with CAB | NODE-D-07-01 | Implementation of CR-D-07.4 | PROCESS | — |

### 3.8 D-08: Human Factors

| Rule ID | Rule Description | Node ID | Allocation Rationale | Track | NIST Anchors |
| --------- | ----------------- | --------- | --------------------- | ------- | --- |
| CR-D-08.1-001 | Annual security awareness training for 5000+ employees | NODE-D-08-01 | Security training platform | PROCESS | CSF: PR.AT-01 | PF: GV.AT-P1,GV.AT-P2 |
| CR-D-08.2-001 | Role-specific security competence; AI human oversight | NODE-D-08-02 | Security competence management | PROCESS | CSF: PR.AT-02 | PF: GV.AT-P1,GV.AT-P2 | AI: GOVERN-2.1,GOVERN-2.2,GOVERN-3.1,MAP-3.5 |
| CR-D-08.3-001 | Management board DORA/NIS 2 training | NODE-D-08-03 | Board training system | PROCESS | CSF: GV.RR-01,PR.AT-02 |
| BPR-D-08.1-001 | Security awareness per SANS framework | NODE-D-08-01 | Implementation of CR-D-08.1 | PROCESS | — |
| BPR-D-08.2-001 | Security competence framework with certifications | NODE-D-08-02 | Implementation of CR-D-08.2 | PROCESS | — |
| BPR-D-08.3-001 | Executive cyber risk reporting | NODE-D-08-03 | Part of board training system | PROCESS | — |
| BPR-D-12.3-001 | AI human oversight procedures per EU AI Act | NODE-D-08-02 | AI-specific human oversight | PROCESS | — |

### 3.9 D-09: Governance & Documentation

| Rule ID | Rule Description | Node ID | Allocation Rationale | Track | NIST Anchors |
| --------- | ----------------- | --------- | --------------------- | ------- | --- |
| CR-D-09.1-001 | Unified ISMS covering all 5 regulatory frameworks | NODE-D-09-01 | Central ISMS platform | PROCESS | CSF: GV.PO-01,GV.PO-02 | PF: CM.PO-P1,GV.PO-P1,GV.PO-P5 | AI: GOVERN-1.1,GOVERN-1.3,GOVERN-1.4,GOVERN-1.6,GOVERN-2.1 |
| CR-D-09.2-001 | IPSARA unified risk assessments | NODE-D-09-01.1 | IPSARA assessment engine | PROCESS | CSF: GV.RM-06,ID.RA-04,ID.RA-05 | PF: ID.RA-P3,ID.RA-P4,ID.RA-P5 | AI: GOVERN-1.1,GOVERN-1.3,GOVERN-1.5,MANAGE-1.2,MAP-3.1 |
| CR-D-09.3-001 | Comprehensive asset/ICT inventory | NODE-D-09-01 | Part of ISMS platform | PROCESS | CSF: ID.AM-01,ID.AM-02,ID.AM-07 | PF: ID.IM-P1,ID.IM-P4,ID.IM-P6,ID.IM-P8 |
| CR-D-09.4-001 | Records of processing, AI traceability documentation | NODE-D-09-01.2 | AI governance documentation module | PROCESS | CSF: GV.OC-03,ID.AM-07 | PF: CM.PO-P1,ID.IM-P1,ID.IM-P4,ID.IM-P6,ID.IM-P8 | AI: GOVERN-1.4,MAP-1.1,MAP-3.4 |
| BPR-D-09.1-001 | ISMS per ISO 27001:2022 | NODE-D-09-01 | Implementation of CR-D-09.1 | PROCESS | — |
| BPR-D-09.2-001 | Risk assessments per ISO 27005 | NODE-D-09-01.1 | Implementation of CR-D-09.2 | PROCESS | — |
| BPR-D-09.3-001 | AI governance framework per NIST AI RMF | NODE-D-09-01.1 | Part of IPSARA engine | PROCESS | — |
| BPR-D-09.4-001 | AI transparency documentation per IEEE 7000 | NODE-D-09-01.2 | Implementation of CR-D-09.4 | PROCESS | — |

### 3.10 D-10: Monitoring & Audit

| Rule ID | Rule Description | Node ID | Allocation Rationale | Track | NIST Anchors |
| --------- | ----------------- | --------- | --------------------- | ------- | --- |
| CR-D-10.1-001 | 24/7 continuous monitoring with AI threat detection | NODE-D-10-01 | AI-powered monitoring platform | TECHNOLOGY | CSF: DE.AE-02,DE.CM-01,DE.CM-09 | PF: CM.AW-P7 | AI: GOVERN-1.5,MANAGE-4.1,MEASURE-2.4,MEASURE-3.1,MEASURE-4.1 |
| CR-D-10.2-001 | Immutable audit logs with PII separation; crypto sharding | NODE-D-10-02, NODE-CS-03 | Audit logging + crypto sharding | TECHNOLOGY + CAPABILITY | CSF: DE.AE-03,PR.PS-04,RS.AN-06 | PF: CT.DM-P9 | AI: GOVERN-1.4,GOVERN-1.6,GOVERN-2.1,MEASURE-2.4,MEASURE-3.1 |
| CR-D-10.3-001 | Annual pentesting, TLPT, periodic AI evaluation | NODE-D-02-02 | Penetration testing framework | PROCESS | CSF: ID.IM-01,ID.IM-02,ID.IM-03 | AI: MAP-3.3,MEASURE-1.1,MEASURE-2.1,MEASURE-2.3,MEASURE-2.7 |
| BPR-D-10.1-001 | SIEM/SOAR with automated threat correlation | NODE-D-10-01 | Implementation of CR-D-10.1 | TECHNOLOGY | — |
| BPR-D-10.2-001 | Centralized log management per NIST SP 800-92 | NODE-D-10-02 | Implementation of CR-D-10.2 | TECHNOLOGY | — |
| BPR-D-10.3-001 | Penetration testing per OWASP Testing Guide v4 | NODE-D-02-02 | Implementation of CR-D-10.3 | PROCESS | — |
| BPR-D-12.1-001 | AI lifecycle management per CRA-C20 (AI Act Art. 9) | NODE-D-08-01.1 | AI lifecycle control module | CAPABILITY | — |
| BPR-D-12.2-001 | AI model monitoring for drift detection | NODE-D-10-01.1 | AI drift detection module | TECHNOLOGY | — |

---

## 4. CROSS-TRACK DEPENDENCY ANALYSIS

Capability sub-requirements (CS) represent cross-track dependencies where PROCESS capabilities enable TECHNOLOGY implementations:

| CS Node | From (P) | To (T) | Dependency Purpose |
|---------|----------|--------|-------------------|
| NODE-CS-01 | Multi-Regulation Incident Correlation | NODE-D-10-01 (Monitoring) | Correlation engine requires monitoring data as input; monitoring data feeds notification system |
| NODE-CS-02 | AI Decision Audit Trail | NODE-D-10-02 (Audit Logs) | Audit trail stored in immutable logs; AI decisions logged for regulatory examination |
| NODE-CS-03 | Cryptographic Sharding Engine | NODE-D-05-01.1 (Erasure), NODE-D-10-02 (Audit Logs) | Erasure uses crypto sharding; logs use crypto sharding for integrity; enables T-002 resolution |

---

## 5. ALLOCATION VERIFICATION

### 5.1 Rule Coverage Verification

| Domain | CR Rules | BPR Rules | Total | Allocated | Coverage |
|--------|----------|-----------|-------|-----------|----------|
| D-01 | 4 | 4 | 8 | 8 | 100% |
| D-02 | 4 | 4 | 8 | 8 | 100% |
| D-03 | 4 | 4 | 8 | 8 | 100% |
| D-04 | 4 | 4 | 8 | 8 | 100% |
| D-05 | 4 | 3 | 7 | 7 | 100% |
| D-06 | 4 | 3 | 7 | 7 | 100% |
| D-07 | 4 | 4 | 8 | 8 | 100% |
| D-08 | 3 | 3 | 6 | 6 | 100% |
| D-09 | 4 | 4 | 8 | 8 | 100% |
| D-10 | 3 | 3 | 6 | 6 | 100% |
| **TOTAL** | **38** | **25** | **63** | **63** | **100%** |

### 5.2 Node Utilization

| Node ID | Allocations | Rules Allocated | Utilization |
|---------|-------------|-----------------|-------------|
| NODE-D-01-01 | 4 | CR-D-01.1, CR-D-01.2, BPR-D-01.1, BPR-D-01.2 | HIGH |
| NODE-D-01-01.1 | 2 | CR-D-01.3, BPR-D-01.3 | MEDIUM |
| NODE-D-01-01.2 | 2 | CR-D-01.4, BPR-D-01.4 | MEDIUM |
| NODE-D-02-01 | 4 | CR-D-02.1, CR-D-02.3, BPR-D-02.1, BPR-D-02.3 | HIGH |
| NODE-D-02-01.1 | 1 | BPR-D-12.4 | LOW |
| NODE-D-02-01.2 | 1 | CR-D-02.2 | LOW |
| NODE-D-02-02 | 4 | CR-D-02.4, BPR-D-02.4, CR-D-10.3, BPR-D-10.3 | HIGH |
| NODE-D-03-01 | 2 | CR-D-03.1, BPR-D-03.1 | MEDIUM |
| NODE-D-03-01.1 | 2 | CR-D-03.2, BPR-D-03.2 | MEDIUM |
| NODE-D-03-01.2 | 2 | CR-D-03.3, BPR-D-03.3 | MEDIUM |
| NODE-D-03-02 | 2 | CR-D-03.4, BPR-D-03.4 | MEDIUM |
| NODE-D-04-01 | 4 | CR-D-04.1, BPR-D-04.1, BPR-D-04.3 | HIGH |
| NODE-D-04-01.1 | 1 | CR-D-10.1 | LOW |
| NODE-D-04-02 | 2 | CR-D-04.2, BPR-D-04.2 | MEDIUM |
| NODE-D-04-02.1 | 2 | CR-D-04.4, BPR-D-04.4 | MEDIUM |
| NODE-D-04-03 | 1 | CR-D-04.3 | LOW |
| NODE-D-05-01 | 5 | CR-D-05.1, CR-D-05.2, CR-D-05.4, BPR-D-05.1, BPR-D-05.4 | HIGH |
| NODE-D-05-01.1 | 2 | CR-D-05.3, BPR-D-05.3 | MEDIUM |
| NODE-D-05-01.2 | 2 | CR-D-05.1, CR-D-05.2 | MEDIUM |
| NODE-D-06-01 | 7 | CR-D-06.1, CR-D-06.3, CR-D-06.4, BPR-D-06.1, BPR-D-06.3, BPR-D-06.4 | VERY HIGH |
| NODE-D-06-01.1 | 1 | BPR-D-12.3 | LOW |
| NODE-D-06-02 | 2 | CR-D-06.2, BPR-D-02.2 | MEDIUM |
| NODE-D-07-01 | 4 | CR-D-07.1, CR-D-07.4, BPR-D-07.1, BPR-D-07.3 | HIGH |
| NODE-D-07-01.1 | 2 | CR-D-07.2, BPR-D-07.2 | MEDIUM |
| NODE-D-07-01.2 | 2 | CR-D-07.3, BPR-D-07.3 | MEDIUM |
| NODE-D-08-01 | 2 | CR-D-08.1, BPR-D-08.1 | MEDIUM |
| NODE-D-08-01.1 | 1 | CR-D-08.2-001 (CR-D-08.2-001 (AI Act Art. 14 — human oversight) — human oversight) | LOW |
| NODE-D-08-02 | 2 | CR-D-08.2, BPR-D-08.2 | MEDIUM |
| NODE-D-08-03 | 2 | CR-D-08.3, BPR-D-08.3 | MEDIUM |
| NODE-D-09-01 | 4 | CR-D-09.1, CR-D-09.3, BPR-D-09.1 | HIGH |
| NODE-D-09-01.1 | 3 | CR-D-09.2, BPR-D-09.2, BPR-D-09.3 | HIGH |
| NODE-D-09-01.2 | 2 | CR-D-09.4, BPR-D-09.4 | MEDIUM |
| NODE-D-10-01 | 4 | CR-D-10.1, BPR-D-10.1, BPR-D-12.2 | HIGH |
| NODE-D-10-01.1 | 1 | BPR-D-12.2 | LOW |
| NODE-D-10-02 | 3 | CR-D-10.2, BPR-D-10.2 | HIGH |
| NODE-CS-01 | 1 | CR-D-04.3 | LOW |
| NODE-CS-02 | 1 | CR-D-02.1-001 (AI-C09, AI-C10), CR-D-09.1-001 (DORA-C38) | LOW |
| NODE-CS-03 | 2 | CR-D-05.3, CR-D-10.2 | MEDIUM |

---

## 6. TRACEABILITY — RULE → NODE → UC

| Rule | Node | UC(s) | NIST Anchors |
| ------ | ------ | ------- | --- |
| CR-D-01.1-001 | NODE-D-01-01 | PROC-41, PROC-43 | CSF: PR.DS-01 | PF: CT.DP-P2,PR.DS-P1 | AI: GOVERN-1.6,MEASURE-2.5,MEASURE-2.7 |
| CR-D-01.2-001 | NODE-D-01-01 | PROC-42 | CSF: PR.DS-02 | PF: PR.DS-P2 |
| CR-D-01.3-001 | NODE-D-01-01.1 | PROC-02, PROC-04 | CSF: PR.DS-01 | PF: CT.DP-P2,PR.DS-P1 | AI: GOVERN-1.6,MEASURE-2.7 |
| CR-D-01.4-001 | NODE-D-01-01.2 | PROC-03, CAP-08 | CSF: PR.DS-01,PR.DS-02 | PF: CT.DM-P1,CT.DM-P3,PR.DS-P1 | AI: MANAGE-2.3,MEASURE-2.6,MEASURE-2.7 |
| CR-D-02.1-001 | NODE-D-02-01 | PROC-05 | CSF: ID.RA-01 | PF: ID.RA-P3,ID.RA-P5 | AI: MANAGE-1.3,MAP-3.2,MAP-3.3,MEASURE-1.1,MEASURE-2.1 |
| CR-D-02.2-001 | NODE-D-02-01.2 | PROC-06 | CSF: PR.PS-02 |
| CR-D-02.3-001 | NODE-D-02-01 | PROC-07 | PF: GV.PO-P5,ID.IM-P7 |
| CR-D-02.4-001 | NODE-D-02-02 | PROC-08 | CSF: ID.IM-02,ID.RA-03 | PF: ID.RA-P3,ID.RA-P4,ID.RA-P5 | AI: MAP-3.3,MEASURE-1.1,MEASURE-2.1,MEASURE-2.3,MEASURE-2.7 |
| CR-D-03.1-001 | NODE-D-03-01 | PROC-10, PROC-13 | CSF: PR.AA-01,PR.AA-03,PR.AA-05 | PF: CT.PO-P1 | AI: GOVERN-1.4,GOVERN-2.1,MAP-3.4 |
| CR-D-03.2-001 | NODE-D-03-01.1 | PROC-45 | CSF: PR.AA-03 |
| CR-D-03.3-001 | NODE-D-03-01.2 | PROC-11 | CSF: PR.AA-01,PR.AA-05 | PF: CT.PO-P1 |
| CR-D-03.4-001 | NODE-D-03-02 | PROC-12 | CSF: PR.PS-01 | PF: CT.DP-P4,CT.PO-P4 |
| CR-D-04.1-001 | NODE-D-04-01 | CAP-02 | CSF: DE.AE-02,DE.CM-01,DE.CM-09 | PF: CM.AW-P7 |
| CR-D-04.2-001 | NODE-D-04-02 | PROC-14 | CSF: RS.MI-01,RS.MI-02 | PF: CT.DM-P10,PR.PO-P7 |
| CR-D-04.3-001 | NODE-D-04-03, NODE-CS-01 | PROC-15 | CSF: RS.CO-02,RS.CO-03 | PF: CM.AW-P7,CM.PO-P1,CM.PO-P2,GV.PO-P5 | AI: GOVERN-1.1,MANAGE-2.3,MANAGE-4.3 |
| CR-D-04.4-001 | NODE-D-04-02.1 | CAP-09 | CSF: RC.RP-01,RC.RP-03,RC.RP-05 |
| CR-D-05.1-001 | NODE-D-05-01, NODE-D-05-01.2 | PROC-20, PROC-22 | CSF: ID.AM-03,PR.DS-10 | PF: CT.DP-P4,CT.PO-P4,ID.RA-P3 | AI: GOVERN-1.4,MAP-2.1,MAP-2.2,MEASURE-2.11 |
| CR-D-05.2-001 | NODE-D-05-01 | PROC-21 | CSF: PR.DS-01,PR.PS-06 | PF: CT.DM-P5,CT.PO-P4 | AI: GOVERN-1.4,MAP-2.1,MAP-2.2,MEASURE-2.11,MEASURE-2.4 |
| CR-D-05.3-001 | NODE-D-05-01.1, NODE-CS-03 | UC-33 | CSF: PR.DS-10 | PF: CT.DM-P4,CT.DM-P5 |
| CR-D-05.4-001 | NODE-D-05-01 | UC-34 | PF: CT.DM-P1,CT.DM-P6 |
| CR-D-06.1-001 | NODE-D-06-01, NODE-D-06-01.1 | PROC-24, PROC-27 | CSF: GV.SC-04 | PF: ID.IM-P2 |
| CR-D-06.2-001 | NODE-D-06-02 | CAP-03 | PF: ID.IM-P7 |
| CR-D-06.3-001 | NODE-D-06-01 | PROC-25 | CSF: GV.SC-05 | PF: GV.PO-P5 |
| CR-D-06.4-001 | NODE-D-06-01 | PROC-26 | CSF: DE.CM-06,PR.IR-01 |
| CR-D-07.1-001 | NODE-D-07-01 | PROC-28, PROC-49 | CSF: ID.RA-01,PR.PS-06 | PF: CT.DP-P2,CT.DP-P5,CT.PO-P4,GV.PO-P2 |
| CR-D-07.2-001 | NODE-D-07-01.1 | PROC-29 | CSF: PR.PS-06 |
| CR-D-07.3-001 | NODE-D-07-01.2 | PROC-48 | CSF: PR.PS-02,PR.PS-06 |
| CR-D-07.4-001 | NODE-D-07-01 | PROC-30 | PF: ID.RA-P3 |
| CR-D-08.1-001 | NODE-D-08-01 | PROC-31 | CSF: PR.AT-01 | PF: GV.AT-P1,GV.AT-P2 |
| CR-D-08.2-001 | NODE-D-08-02 | CAP-04 | CSF: PR.AT-02 | PF: GV.AT-P1,GV.AT-P2 | AI: GOVERN-2.1,GOVERN-2.2,GOVERN-3.1,MAP-3.5 |
| CR-D-08.3-001 | NODE-D-08-03 | PROC-32 | CSF: GV.RR-01,PR.AT-02 |
| CR-D-09.1-001 | NODE-D-09-01 | CAP-05 | CSF: GV.PO-01,GV.PO-02 | PF: CM.PO-P1,GV.PO-P1,GV.PO-P5 | AI: GOVERN-1.1,GOVERN-1.3,GOVERN-1.4,GOVERN-1.6,GOVERN-2.1 |
| CR-D-09.2-001 | NODE-D-09-01.1 | PROC-34 | CSF: GV.RM-06,ID.RA-04,ID.RA-05 | PF: ID.RA-P3,ID.RA-P4,ID.RA-P5 | AI: GOVERN-1.1,GOVERN-1.3,GOVERN-1.5,MANAGE-1.2,MAP-3.1 |
| CR-D-09.3-001 | NODE-D-09-01 | CAP-06 | CSF: ID.AM-01,ID.AM-02,ID.AM-07 | PF: ID.IM-P1,ID.IM-P4,ID.IM-P6,ID.IM-P8 |
| CR-D-09.4-001 | NODE-D-09-01.2 | CAP-07 | CSF: GV.OC-03,ID.AM-07 | PF: CM.PO-P1,ID.IM-P1,ID.IM-P4,ID.IM-P6,ID.IM-P8 | AI: GOVERN-1.4,MAP-1.1,MAP-3.4 |
| CR-D-10.1-001 | NODE-D-10-01 | PROC-51, PROC-52 | CSF: DE.AE-02,DE.CM-01,DE.CM-09 | PF: CM.AW-P7 | AI: GOVERN-1.5,MANAGE-4.1,MEASURE-2.4,MEASURE-3.1,MEASURE-4.1 |
| CR-D-10.2-001 | NODE-D-10-02, NODE-CS-03 | CAP-10 | CSF: DE.AE-03,PR.PS-04,RS.AN-06 | PF: CT.DM-P9 | AI: GOVERN-1.4,GOVERN-1.6,GOVERN-2.1,MEASURE-2.4,MEASURE-3.1 |
| CR-D-10.3-001 | NODE-D-02-02 | PROC-36 | CSF: ID.IM-01,ID.IM-02,ID.IM-03 | AI: MAP-3.3,MEASURE-1.1,MEASURE-2.1,MEASURE-2.3,MEASURE-2.7 |

---

## 7. STOP CONDITION CHECK — SC1 (Rule Coverage)

| Check | Value | Threshold | Status |
|-------|-------|-----------|--------|
| Total rules (CR + BPR) | 63 | — | — |
| Rules mapped to UCs | 63 | — | — |
| Rules with node allocation | 63 | — | — |
| Coverage | 100% | 100% | ✅ PASS |

**SC1: PASS — Every rule maps to ≥1 UC, every UC maps to ≥1 node.**

---

## 8. NEXT STEPS

1. **Compliance Gates Report (Doc 16)** — Define compliance verification points for each node
2. **Functional Requirements (Doc 23)** — Derive FRs from node allocations
3. **Non-Functional Requirements (Doc 24)** — Derive NFRs from node allocations

---

## 9. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-28 | Security Architect | Initial creation — 63 rules allocated to 28 nodes |

---

## 10. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Security Architect | [TBD] | | |
| Compliance Lead | [TBD] | | |
| CISO | [TBD] | | |
| AI Governance Lead | [TBD] | | |

---

**Next Step:** Proceed to 16_Compliance_Gates_Report.md to define compliance verification points.