---
document_id: AEGIS-P2-10
title: Privacy and Security Operational Objectives Catalog
phase: 2
version: 1.0
created: 2026-04-03
updated: 2026-04-03
author: Compliance Lead
status: DRAFT
inputs: [08_Obligation_Derivation.md, 09_Strategic_Tensions_Report.md, 04_Company_Context_Assessment.md]
outputs: [11_Rules_Catalog.md, 12_Rules_Catalog.xlsx]
traceability: AEGIS Class Model → PrivacyGoal, SecurityGoal, RiskProfile classes
related_documents: 03_Design_Decisions_Log.md
---

# Privacy and Security Operational Objectives Catalog

**Case:** Case 03 — OmniBank Financial Systems (High Complexity)  
**Phase:** 2 — Elaboration & Secure Design  
**Step:** D — Privacy & Security Objectives Derivation

---

## 1. DOCUMENT PURPOSE

This document defines the Privacy and Security Objectives derived from the 38 regulatory obligations identified in the Obligation Derivation (08_Obligation_Derivation.md) and informed by the Strategic Tensions Report (09_Strategic_Tensions_Report.md) and Company Context Assessment (04_Company_Context_Assessment.md).

The objectives serve as the bridge between abstract regulatory obligations and concrete, implementable rules in the Rules Catalog. Each objective is traceable to its source obligations, assigned a risk profile, and prioritized for implementation sequencing.

**Scope:** 33 total objectives (11 Privacy Objectives, 22 Security Objectives) derived from 38 obligations across 5 regulations (GDPR, CRA, NIS 2, DORA, AI Act).

---

## 2. OBJECTIVES CATALOG METADATA

| Field | Value |
|-------|-------|
| Document ID | AEGIS-P2-10 |
| Version | 1.0 |
| Phase | 2 — Elaboration & Secure Design |
| Status | DRAFT |
| Created | 2026-04-03 |
| Updated | 2026-04-03 |
| Author | Compliance Lead |
| Inputs | 08_Obligation_Derivation.md, 09_Strategic_Tensions_Report.md, 04_Company_Context_Assessment.md |
| Outputs | 11_Rules_Catalog.md, 12_Rules_Catalog.xlsx |
| Traceability | AEGIS Class Model → PrivacyGoal, SecurityGoal, RiskProfile classes |
| Related Documents | 03_Design_Decisions_Log.md |

---

## 3. PRIVACY OBJECTIVES CATALOG

Privacy objectives are derived from obligations related to data protection, data lifecycle, secure development (privacy aspects), and governance/documentation requirements.

### 3.1 D-01: Data Protection & Encryption

| Objective ID | Objective Description | Source Obligations | Risk Profile | Priority | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------- | -------------- | ---------- | --- | --- | --- |
| AG-D-01.1-001 | Personal, financial, and AI model data in persistent storage protected by confidentiality mechanisms with segregated cryptographic material management across all storage systems | OBL-D-01.1-001 | MEDIUM | CRITICAL | PR.DS-01, PR.DS-02, PR.DS-10, PR.IR-01 | PR.DS-P1 | MANAGE-2.1, MAP-2.1 |
| AG-D-01.2-001 | Data crossing network boundaries protected by confidentiality mechanisms appropriate to channel classification | OBL-D-01.2-001 | MEDIUM | HIGH | — | PR.DS-P2 | MAP-2.1 |
| AG-D-01.3-001 | Cryptographic material custody with documented lifecycle controls | OBL-D-01.3-001 | MEDIUM | HIGH | — | PR.DS-P3 | — |
| AG-D-01.4-001 | Ensure data integrity and resilience of AI systems against manipulation | OBL-D-01.4-001 | MEDIUM | HIGH | — | PR.DS-P3 | MEASURE-2.5 |

### 3.2 D-05: Data Lifecycle

| Objective ID | Objective Description | Source Obligations | Risk Profile | Priority | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------- | -------------- | ---------- | --- | --- | --- |
| AG-D-05.1-001 | Minimize data collection to essential fields; ensure AI training data relevance and representativeness | OBL-D-05.1-001 | MEDIUM | HIGH | — | CT.PO-P1, ID.IM-P1 | MAP-1.5, MAP-3.1 |
| AG-D-05.2-001 | Enforce retention policies per regulatory requirements (5-10 years financial, 6 months AI logs) | OBL-D-05.2-001 | HIGH | CRITICAL | — | CT.DM-P2, GV.RM-P1 | MANAGE-2.4 |
| AG-D-05.3-001 | Enable complete data erasure via cryptographic sharding within 30 days of request | OBL-D-05.3-001 | HIGH | CRITICAL | PR.DS-01, PR.PS-01 | CT.DM-P3 | — |
| AG-D-05.4-001 | Provide data export in machine-readable formats within regulatory SLAs | OBL-D-05.4-001 | LOW | MODERATE | — | CT.PO-P2 | MAP-1.6 |

### 3.3 D-07: Secure Development

| Objective ID | Objective Description | Source Obligations | Risk Profile | Priority | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------- | -------------- | ---------- | --- | --- | --- |
| AG-D-07.1-001 | Integrate privacy and security into SDLC design from outset per CRA secure-by-default standard | OBL-D-07.1-001 | MEDIUM | HIGH | — | — | GOVERN-2.2, GOVERN-3.1 |

### 3.4 D-09: Governance & Documentation

| Objective ID | Objective Description | Source Obligations | Risk Profile | Priority | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------- | -------------- | ---------- | --- | --- | --- |
| AG-D-09.1-001 | Maintain unified ISMS covering GDPR, DORA, and AI Act documentation requirements | OBL-D-09.1-001 | HIGH | CRITICAL | GV.RM-01, ID.RA-01, ID.RA-04 | ID.RA-P1 | GOVERN-4.1, GOVERN-5.2, MAP-3.1 |
| AG-D-09.2-001 | Conduct IPSARA unified risk assessments prior to all new systems and annually for existing | OBL-D-09.2-001 | HIGH | CRITICAL | — | — | — |
| AG-D-09.4-001 | Maintain comprehensive records of processing, AI traceability, and regulatory documentation | OBL-D-09.4-001 | MEDIUM | HIGH | — | GV.RM-P1, ID.RA-P3 | GOVERN-5.1, MAP-3.1 |

### 3.5 Privacy Objectives Summary

| Metric | Value |
|--------|-------|
| Total Privacy Objectives | 11 |
| By Priority — CRITICAL | 4 (36.4%) |
| By Priority — HIGH | 6 (54.5%) |
| By Priority — MODERATE | 1 (9.1%) |
| By Risk Profile — MEDIUM | 6 |
| By Risk Profile — HIGH | 4 |
| By Risk Profile — LOW | 1 |

---

## 4. SECURITY OBJECTIVES CATALOG

Security objectives are derived from obligations related to vulnerability management, access control, incident response, supply chain security, secure development (security aspects), human factors, governance, and monitoring/audit.

### 4.1 D-02: Vulnerability Management

| Objective ID | Objective Description | Source Obligations | Risk Profile | Priority | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------- | -------------- | ---------- | --- | --- | --- |
| AG-D-02.1-002 | Maintain zero known exploitable vulnerabilities across all systems; ensure AI data governance | OBL-D-02.1-001 | HIGH | CRITICAL | — | — | — |
| AG-D-02.2-002 | Enable automated patch management with 72h critical remediation SLA | OBL-D-02.2-001 | HIGH | CRITICAL | — | — | — |
| AG-D-02.3-002 | Publish coordinated vulnerability disclosure policy with 24h incident reporting | OBL-D-02.3-001 | MEDIUM | HIGH | — | — | — |
| AG-D-02.4-002 | Conduct annual TLPT (Threat-Led Penetration Testing) per DORA RTS; perform AI bias testing | OBL-D-02.4-001 | HIGH | CRITICAL | — | — | — |

### 4.2 D-03: Access Control

| Objective ID | Objective Description | Source Obligations | Risk Profile | Priority | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------- | -------------- | ---------- | --- | --- | --- |
| AG-D-03.1-002 | Implement unified identity management with MFA for all access points | OBL-D-03.1-001 | MEDIUM | HIGH | — | — | MAP-2.1 |
| AG-D-03.2-002 | Enforce MFA for all privileged, remote, and AI system access | OBL-D-03.2-001 | MEDIUM | HIGH | — | — | MEASURE-2.5 |
| AG-D-03.3-002 | Enforce least privilege across all systems with quarterly access reviews | OBL-D-03.3-001 | MEDIUM | HIGH | — | — | — |
| AG-D-03.4-002 | Harden all systems per hardened-default baseline; secure default configuration per CRA | OBL-D-03.4-001 | LOW | MODERATE | — | — | — |

### 4.3 D-04: Incident Response

| Objective ID | Objective Description | Source Obligations | Risk Profile | Priority | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------- | -------------- | ---------- | --- | --- | --- |
| AG-D-04.1-002 | Implement 24/7 SOC with automated incident detection and triage | OBL-D-04.1-001 | HIGH | CRITICAL | — | — | — |
| AG-D-04.2-002 | Maintain business continuity with 99.99% uptime SLA; tested disaster recovery | OBL-D-04.2-001 | HIGH | CRITICAL | — | — | — |
| AG-D-04.3-002 | Execute 24h universal incident notification workflow satisfying all 5 regulations | OBL-D-04.3-001 | CRITICAL | CRITICAL | — | — | — |
| AG-D-04.4-002 | Maintain redundant backup systems with automated failover capabilities | OBL-D-04.4-001 | HIGH | CRITICAL | — | — | — |

### 4.4 D-06: Supply Chain

| Objective ID | Objective Description | Source Obligations | Risk Profile | Priority | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------- | -------------- | ---------- | --- | --- | --- |
| AG-D-06.1-002 | Maintain vendor risk management program covering all DORA/NIS 2/GDPR requirements | OBL-D-06.1-001 | HIGH | CRITICAL | — | — | — |
| AG-D-06.2-002 | Maintain comprehensive SBOM for all software products and dependencies | OBL-D-06.2-001 | MEDIUM | HIGH | — | — | — |
| AG-D-06.3-002 | Enforce contractual security obligations across all third-party relationships | OBL-D-06.3-001 | HIGH | HIGH | — | — | — |
| AG-D-06.4-002 | Manage third-party concentration risk with documented exit strategies | OBL-D-06.4-001 | HIGH | HIGH | — | — | — |

### 4.5 D-07: Secure Development (Security)

| Objective ID | Objective Description | Source Obligations | Risk Profile | Priority | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------- | -------------- | ---------- | --- | --- | --- |
| AG-D-07.2-002 | Implement secure coding standards with automated static and dynamic analysis mechanisms | OBL-D-07.2-001 | MEDIUM | HIGH | — | — | MEASURE-2.5 |
| AG-D-07.3-002 | Secure CI/CD pipeline with automated security gates and approval workflows | OBL-D-07.3-001 | MEDIUM | HIGH | — | — | — |
| AG-D-07.4-002 | Implement formal change management with dual control and regulatory oversight | OBL-D-07.4-001 | MEDIUM | HIGH | — | — | — |

### 4.6 D-08: Human Factors (Security)

| Objective ID | Objective Description | Source Obligations | Risk Profile | Priority | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------- | -------------- | ---------- | --- | --- | --- |
| AG-D-08.1-002 | Conduct annual security awareness training for all 5000+ employees | OBL-D-08.1-001 | LOW | MODERATE | DE.CM-01, DE.CM-03, DE.CM-09, RS.MA-02 | — | MEASURE-2.5 |
| AG-D-08.2-002 | Maintain role-specific security competence programs; ensure AI human oversight | OBL-D-08.2-001 | MEDIUM | HIGH | — | — | — |
| AG-D-08.3-002 | Ensure management board receives DORA/NIS 2 security training and exercises ICT risk oversight | OBL-D-08.3-001 | MEDIUM | HIGH | — | — | — |

### 4.7 D-09: Governance (Security)

| Objective ID | Objective Description | Source Obligations | Risk Profile | Priority | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------- | -------------- | ---------- | --- | --- | --- |
| AG-D-09.3-002 | Maintain comprehensive asset and ICT asset inventory with automated discovery | OBL-D-09.3-001 | MEDIUM | HIGH | — | — | MANAGE-2.4 |

### 4.8 D-10: Monitoring & Audit

| Objective ID | Objective Description | Source Obligations | Risk Profile | Priority | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------- | -------------- | ---------- | --- | --- | --- |
| AG-D-10.1-002 | Implement 24/7 continuous security monitoring with AI threat detection | OBL-D-10.1-001 | HIGH | CRITICAL | — | — | MANAGE-4.1 |
| AG-D-10.2-002 | Maintain immutable, tamper-evident audit logs with PII separation and AI traceability | OBL-D-10.2-001 | HIGH | CRITICAL | — | — | — |
| AG-D-10.3-002 | Conduct annual penetration testing, resilience testing, and periodic AI evaluation | OBL-D-10.3-001 | HIGH | CRITICAL | — | — | — |

### 4.9 Security Objectives Summary

| Metric | Value |
|--------|-------|
| Total Security Objectives | 22 |
| By Priority — CRITICAL | 8 (36.4%) |
| By Priority — HIGH | 11 (50.0%) |
| By Priority — MODERATE | 3 (13.6%) |
| By Risk Profile — HIGH | 10 |
| By Risk Profile — MEDIUM | 10 |
| By Risk Profile — CRITICAL | 1 |
| By Risk Profile — LOW | 2 |

---

## 5. OBJECTIVES DERIVATION PATH

The objectives are derived through a systematic two-step derivation from regulatory clauses:

```
RegulatoryClause (150 clauses across 5 regulations)
    ↓ (Derivation Rules DR-001 to DR-007)
RegulatoryObligation (38 obligations)
    ↓ (Objective Derivation)
    ├─→ Privacy Objectives (11 objectives)
    └─→ Security Objectives (22 objectives)
        ↓ (Feeds)
    Rules Catalog (~60+ rules estimated)
```

### 5.1 Derivation Rules Applied

| Derivation Rule ID | Rule Description | Applied To |
|--------------------|-----------------|------------|
| DR-001 | Encryption obligations → encryption objectives | OBL-D-01.1, OBL-D-01.2, OBL-D-01.3 |
| DR-002 | Data lifecycle obligations → lifecycle objectives | OBL-D-05.1 through OBL-D-05.4 |
| DR-003 | Vulnerability obligations → vulnerability objectives | OBL-D-02.1 through OBL-D-02.4 |
| DR-004 | Access control obligations → access objectives | OBL-D-03.1 through OBL-D-03.4 |
| DR-005 | Incident response obligations → IR objectives | OBL-D-04.1 through OBL-D-04.4 |
| DR-006 | Supply chain obligations → vendor objectives | OBL-D-06.1 through OBL-D-06.4 |
| DR-007 | Governance obligations → governance objectives | OBL-D-09.1, OBL-D-09.2, OBL-D-09.3, OBL-D-09.4 |

### 5.2 Obligation-to-Objective Mapping Statistics

| Metric | Value |
|--------|-------|
| Total Obligations | 38 |
| Total Objectives Derived | 33 |
| Average Objectives per Obligation | 0.87 |
| Obligations with Multiple Objectives | 5 |
| Obligations with Single Objective | 28 |
| Obligations Deferred to Phase 3 | 5 |

### 5.3 Objective-to-Obligation-to-Clause Derivation Path

Full derivation path for every objective, tracing from objective through obligation to source regulatory clauses with Normative Intensity:

| Objective ID | Objective Description | Derived From Obligation | Source Clauses | Clause Count | Derived NI | Risk Profile | CSF Anchors | PF Anchors | AI RMF Anchors |
| --------- | ----------------- | ------------------------ | ---------------- | -------------- | ------------ | -------------- | --- | --- | --- |
| AG-D-01.1-001 | Encrypt data at rest | OBL-D-01.1-001 | GDPR-C04,C14; CRA-C07; NIS2-C18; DORA-C09; AI-C17 | 6 | 2.667 | MEDIUM | PR.DS-01, PR.DS-02, PR.DS-10, PR.IR-01 | PR.DS-P1 | MANAGE-2.1, MAP-2.1 |
| AG-D-01.2-001 | Encrypt data in transit | OBL-D-01.2-001 | GDPR-C15; CRA-C08; DORA-C10 | 3 | 2.667 | MEDIUM | — | PR.DS-P2 | MAP-2.1 |
| AG-D-01.3-001 | Cryptographic material custody with documented lifecycle | OBL-D-01.3-001 | CRA-C15; DORA-C17 | 2 | 3.000 | MEDIUM | — | PR.DS-P3 | — |
| AG-D-01.4-001 | Data integrity/AI resilience | OBL-D-01.4-001 | GDPR-C05; CRA-C09; AI-C18 | 3 | 2.667 | MEDIUM | — | PR.DS-P3 | MEASURE-2.5 |
| AG-D-05.1-001 | Data minimization; AI relevance | OBL-D-05.1-001 | GDPR-C01; CRA-C10; AI-C05,C06 | 4 | 3.000 | MEDIUM | — | CT.PO-P1, ID.IM-P1 | MAP-1.5, MAP-3.1 |
| AG-D-05.2-001 | Tiered retention enforcement | OBL-D-05.2-001 | GDPR-C02,C03; AI-C07 | 3 | 3.000 | HIGH | — | CT.DM-P2, GV.RM-P1 | MANAGE-2.4 |
| AG-D-05.3-001 | Cryptographic sharding erasure | OBL-D-05.3-001 | GDPR-C06; CRA-C16 | 2 | 3.000 | HIGH | PR.DS-01, PR.PS-01 | CT.DM-P3 | — |
| AG-D-05.4-001 | Data export in machine-readable | OBL-D-05.4-001 | GDPR-C07 | 1 | 3.000 | LOW | — | CT.PO-P2 | MAP-1.6 |
| AG-D-07.1-001 | Privacy/security by design | OBL-D-07.1-001 | GDPR-C09; CRA-C02,C22 | 3 | 2.667 | MEDIUM | — | — | GOVERN-2.2, GOVERN-3.1 |
| AG-D-09.1-001 | Unified ISMS | OBL-D-09.1-001 | GDPR-C08,C25,C26; CRA-C24; NIS2-C01,C03; DORA-C01,C03; AI-C08,C12,C13,C20,C23 | 13 | 2.846 | HIGH | GV.RM-01, ID.RA-01, ID.RA-04 | ID.RA-P1 | GOVERN-4.1, GOVERN-5.2, MAP-3.1 |
| AG-D-09.2-001 | IPSARA unified assessments | OBL-D-09.2-001 | GDPR-C20,C24; CRA-C23; NIS2-C04; DORA-C04; AI-C01,C02,C22,C28 | 9 | 2.889 | HIGH | — | — | — |
| AG-D-09.4-001 | Records of processing/AI traceability | OBL-D-09.4-001 | GDPR-C13,C22; DORA-C38; AI-C11 | 4 | 3.000 | MEDIUM | — | GV.RM-P1, ID.RA-P3 | GOVERN-5.1, MAP-3.1 |
| AG-D-02.1-002 | Zero exploitable vulnerabilities | OBL-D-02.1-001 | CRA-C01,C17; NIS2-C12; DORA-C08; AI-C03,C16 | 6 | 3.000 | HIGH | — | — | — |
| AG-D-02.2-002 | Automated patch management | OBL-D-02.2-001 | CRA-C04,C19; NIS2-C12; DORA-C13 | 4 | 3.000 | HIGH | — | — | — |
| AG-D-02.3-002 | Vuln disclosure policy | OBL-D-02.3-001 | CRA-C21,C26 | 2 | 3.000 | MEDIUM | — | — | — |
| AG-D-02.4-002 | Annual TLPT; AI bias testing | OBL-D-02.4-001 | DORA-C27,C29; AI-C04 | 3 | 3.000 | HIGH | — | — | — |
| AG-D-03.1-002 | Unified identity management | OBL-D-03.1-001 | CRA-C05; NIS2-C16,C19; DORA-C11,C15; AI-C15 | 6 | 3.000 | MEDIUM | — | — | MAP-2.1 |
| AG-D-03.2-002 | MFA for privileged/AI access | OBL-D-03.2-001 | CRA-C06; NIS2-C17; DORA-C16 | 3 | 2.667 | MEDIUM | — | — | MEASURE-2.5 |
| AG-D-03.3-002 | Least privilege enforcement | OBL-D-03.3-001 | GDPR-C10,C17; NIS2-C20; DORA-C14 | 4 | 3.000 | MEDIUM | — | — | — |
| AG-D-03.4-002 | Secure defaults per CIS | OBL-D-03.4-001 | CRA-C03 | 1 | 3.000 | LOW | — | — | — |
| AG-D-04.1-002 | 24/7 SOC detection/triage | OBL-D-04.1-001 | CRA-C13; NIS2-C28; DORA-C18,C21 | 4 | 3.000 | HIGH | — | — | — |
| AG-D-04.2-002 | Business continuity 99.99% | OBL-D-04.2-001 | GDPR-C18; CRA-C11; NIS2-C05; DORA-C19,C22,C24 | 6 | 2.833 | HIGH | — | — | — |
| AG-D-04.3-002 | 24h universal notification | OBL-D-04.3-001 | GDPR-C21,C23; CRA-C25; NIS2-C25,C26,C27; DORA-C35,C36,C37; AI-C26,C29 | 11 | 3.000 | CRITICAL | — | — | — |
| AG-D-04.4-002 | Redundant backup/failover | OBL-D-04.4-001 | GDPR-C16; NIS2-C06; DORA-C23,C25 | 4 | 2.750 | HIGH | — | — | — |
| AG-D-06.1-002 | Vendor risk management | OBL-D-06.1-001 | GDPR-C11; NIS2-C08,C23; DORA-C30,C32 | 5 | 3.000 | HIGH | — | — | — |
| AG-D-06.2-002 | SBOM maintenance | OBL-D-06.2-001 | CRA-C18 | 1 | 3.000 | MEDIUM | — | — | — |
| AG-D-06.3-002 | Contractual security obligations | OBL-D-06.3-001 | GDPR-C12; NIS2-C09; DORA-C31 | 3 | 3.000 | HIGH | — | — | — |
| AG-D-06.4-002 | Concentration risk management | OBL-D-06.4-001 | NIS2-C24; DORA-C33,C34 | 3 | 3.000 | HIGH | — | — | — |
| AG-D-07.2-002 | Secure coding per industry standards | OBL-D-07.2-001 | NIS2-C11; DORA-C20 | 2 | 3.000 | MEDIUM | — | — | MEASURE-2.5 |
| AG-D-07.3-002 | CI/CD security gates | OBL-D-07.3-001 | NIS2-C11; DORA-C20 | 2 | 3.000 | MEDIUM | — | — | — |
| AG-D-07.4-002 | Formal change management | OBL-D-07.4-001 | NIS2-C10; DORA-C06 | 2 | 3.000 | MEDIUM | — | — | — |
| AG-D-08.1-002 | Annual awareness training | OBL-D-08.1-001 | GDPR-C27; NIS2-C14 | 2 | 3.000 | LOW | DE.CM-01, DE.CM-03, DE.CM-09, RS.MA-02 | — | MEASURE-2.5 |
| AG-D-08.2-002 | Role-specific competence | OBL-D-08.2-001 | GDPR-C28; NIS2-C15; AI-C14,C24 | 4 | 3.000 | MEDIUM | — | — | — |
| AG-D-08.3-002 | Board DORA/NIS 2 training | OBL-D-08.3-001 | NIS2-C02; DORA-C02 | 2 | 3.000 | MEDIUM | — | — | — |
| AG-D-09.3-002 | Asset/ICT inventory | OBL-D-09.3-001 | NIS2-C07; DORA-C05 | 2 | 3.000 | MEDIUM | — | — | MANAGE-2.4 |
| AG-D-10.1-002 | 24/7 monitoring AI detection | OBL-D-10.1-001 | CRA-C12; NIS2-C21,C29; DORA-C07; AI-C19,C25 | 6 | 3.000 | HIGH | — | — | MANAGE-4.1 |
| AG-D-10.2-002 | Immutable audit logs PII sep. | OBL-D-10.2-001 | CRA-C14; NIS2-C22; DORA-C12; AI-C09,C10 | 5 | 3.000 | HIGH | — | — | — |
| AG-D-10.3-002 | Annual pentest/TLPT/AI eval | OBL-D-10.3-001 | GDPR-C19; CRA-C20; NIS2-C13; DORA-C26,C28; AI-C21,C27 | 7 | 2.857 | HIGH | — | — | — |

**Traceability verification:** 33 objectives × 150 clauses — every objective traces to at least one obligation, and every obligation traces to at least one regulatory clause. Mean clause count per objective: 4.1.

---

## 6. RISK PROFILE ASSESSMENT

Risk profiles are assigned based on the potential impact of objective failure on regulatory compliance, customer trust, financial stability, and operational continuity.

### 6.1 Overall Risk Profile Distribution

| Risk Profile | Privacy Objectives | Security Objectives | Total | Percentage |
|--------------|---------------|----------------|-------|------------|
| CRITICAL | 0 | 1 (AG-D-04.3-002) | 1 | 3.0% |
| HIGH | 4 | 10 | 14 | 42.4% |
| MEDIUM | 6 | 10 | 16 | 48.5% |
| LOW | 1 | 2 | 3 | 9.1% |
| **TOTAL** | **11** | **22** | **33** | **100%** |

### 6.2 Risk Profile Criteria

| Risk Profile | Definition | Examples |
|--------------|------------|----------|
| CRITICAL | Failure results in immediate regulatory breach, systemic risk, or material financial impact across multiple regulations | AG-D-04.3-002 (24h universal incident notification) |
| HIGH | Failure results in significant regulatory exposure, reputational damage, or operational degradation | AG-D-05.2-001 (retention), AG-D-06.1-002 (vendor risk) |
| MEDIUM | Failure results in moderate compliance gaps, correctable within standard remediation cycles | AG-D-01.1-001 (encryption at rest), AG-D-03.1-002 (identity management) |
| LOW | Failure results in minor compliance observations; low regulatory priority | AG-D-05.4-001 (data export), AG-D-08.1-002 (awareness training) |

### 6.3 Risk by Regulatory Driver

| Regulation | CRITICAL Objectives | HIGH Objectives | MEDIUM Objectives | LOW Objectives | Total |
|------------|---------------|------------|--------------|-----------|-------|
| GDPR | 0 | 3 | 4 | 1 | 8 |
| CRA | 0 | 2 | 3 | 0 | 5 |
| NIS 2 | 0 | 3 | 3 | 1 | 7 |
| DORA | 1 | 5 | 3 | 1 | 10 |
| AI Act | 0 | 1 | 3 | 0 | 4 |
| **Multi-Regulatory** | 0 | 3 | 0 | 1 | 4 |

---

## 7. ASSURANCE LEVEL DEFINITION

Assurance levels define the depth of verification required for each objective. Higher assurance levels require more rigorous evidence, independent verification, and formal documentation.

### 7.1 Assurance Level Distribution

| Assurance Level | Privacy Objectives | Security Objectives | Total | Percentage |
|-----------------|---------------|----------------|-------|------------|
| HIGH | 8 | 14 | 22 | 66.7% |
| MODERATE | 3 | 8 | 11 | 33.3% |
| BASIC | 0 | 0 | 0 | 0.0% |

### 7.2 Assurance Level Criteria

| Assurance Level | Verification Method | Evidence Requirements | Review Frequency |
|-----------------|---------------------|----------------------|------------------|
| HIGH | Independent audit + automated verification + regulatory examination | Formal evidence package, test results, auditor attestation | Quarterly |
| MODERATE | Internal audit + automated monitoring + management review | Documented procedures, monitoring dashboards, management sign-off | Semi-annual |
| BASIC | Self-assessment + periodic review | Checklist completion, management attestation | Annual |

### 7.3 Objectives by Assurance Level

| Assurance Level | Objective IDs |
|-----------------|----------|
| HIGH | AG-D-01.1-001, AG-D-05.2-001, AG-D-05.3-001, AG-D-09.1-001, AG-D-09.2-001, AG-D-02.1-002, AG-D-02.2-002, AG-D-02.4-002, AG-D-04.1-002, AG-D-04.2-002, AG-D-04.3-002, AG-D-04.4-002, AG-D-06.1-002, AG-D-06.3-002, AG-D-06.4-002, AG-D-10.1-002, AG-D-10.2-002, AG-D-10.3-002 |
| MODERATE | AG-D-01.2-001, AG-D-01.3-001, AG-D-01.4-001, AG-D-05.1-001, AG-D-05.4-001, AG-D-07.1-001, AG-D-09.4-001, AG-D-02.3-002, AG-D-03.1-002, AG-D-03.2-002, AG-D-03.3-002 |
| BASIC | AG-D-03.4-002, AG-D-07.2-002, AG-D-07.3-002, AG-D-07.4-002, AG-D-08.1-002, AG-D-08.2-002, AG-D-08.3-002, AG-D-09.3-002 |

---

## 8. PRIVACY/SECURITY CONFLICT RESOLUTION

Conflicts between privacy and security objectives are identified through analysis of the Strategic Tensions Report (09_Strategic_Tensions_Report.md). Each conflict is resolved through documented resolution patterns.

### 8.1 Identified Conflicts

| Conflict ID | Privacy Objective | Security Objective | Conflict Type | Resolution |
|-------------|-------------|---------------|---------------|------------|
| CONF-001 | AG-D-05.3 (Erasure) | AG-D-10.2-002 (Immutable Logs) | Retention vs Deletion | Cryptographic sharding (see T-002) |
| CONF-002 | AG-D-05.2 (Retention) | AG-D-10.2-002 (AI Log Retention) | Competing retention periods | Tiered retention: 5-10yr financial, 6mo AI, per-subject override |
| CONF-003 | AG-D-05.1 (Minimization) | AG-D-10.1-002 (AI Monitoring) | Data collection vs monitoring | Anonymized behavioral analytics; minimize PII |

### 8.2 Conflict Resolution Detail

#### CONF-001: Erasure vs. Immutable Logs

| Field | Value |
|-------|-------|
| Conflict ID | CONF-001 |
| Privacy Objective | AG-D-05.3-001 — Enable complete data erasure via cryptographic sharding within 30 days |
| Security Objective | AG-D-10.2-002 — Maintain immutable, tamper-evident audit logs with PII separation |
| Conflict Type | Retention vs Deletion |
| Root Cause | GDPR Art.17 right to erasure conflicts with audit log integrity requirements (NIS 2 Art.21, DORA Art.16) |
| Resolution | Cryptographic sharding: encrypt PII with per-subject keys; destroy keys on erasure request while retaining encrypted log structure |
| Traceability | Tension T-002 in Strategic Tensions Report |
| Status | Resolved |

#### CONF-002: Competing Retention Periods

| Field | Value |
|-------|-------|
| Conflict ID | CONF-002 |
| Privacy Objective | AG-D-05.2-001 — Enforce retention policies per regulatory requirements |
| Security Objective | AG-D-10.2-002 — Maintain immutable audit logs with AI traceability |
| Conflict Type | Competing retention periods |
| Root Cause | Financial regulations require 5-10 year retention; AI Act requires 6-month AI system logs; GDPR storage limitation principle |
| Resolution | Tiered retention policy: financial records 5-10 years, AI system logs 6 months, personal data per-subject override via erasure request |
| Traceability | Tension T-005 in Strategic Tensions Report |
| Status | Resolved |

#### CONF-003: Minimization vs. Monitoring

| Field | Value |
|-------|-------|
| Conflict ID | CONF-003 |
| Privacy Objective | AG-D-05.1-001 — Minimize data collection to essential fields |
| Security Objective | AG-D-10.1-002 — Implement 24/7 continuous security monitoring with AI threat detection |
| Conflict Type | Data collection vs monitoring |
| Root Cause | AI threat detection requires behavioral data; GDPR data minimization limits collection scope |
| Resolution | Anonymized behavioral analytics; aggregate monitoring patterns without storing identifiable user data; minimize PII in monitoring pipeline |
| Traceability | Tension T-003 in Strategic Tensions Report |
| Status | Resolved |

---

## 9. KEY OBSERVATIONS

### 9.1 Objectives Density by Domain

| Security Domain | Privacy Objectives | Security Objectives | Total | Coverage |
|-----------------|---------------|----------------|-------|----------|
| D-01 Data Protection & Encryption | 4 | 0 | 4 | 100% |
| D-02 Vulnerability Management | 0 | 4 | 4 | 100% |
| D-03 Access Control | 0 | 4 | 4 | 100% |
| D-04 Incident Response | 0 | 4 | 4 | 100% |
| D-05 Data Lifecycle | 4 | 0 | 4 | 100% |
| D-06 Supply Chain | 0 | 4 | 4 | 100% |
| D-07 Secure Development | 1 | 3 | 4 | 100% |
| D-08 Human Factors | 0 | 3 | 3 | 100% |
| D-09 Governance & Documentation | 3 | 1 | 4 | 100% |
| D-10 Monitoring & Audit | 0 | 3 | 3 | 100% |

### 9.2 Complexity Indicators

| Indicator | Value | Assessment |
|-----------|-------|------------|
| Objectives per Obligation | 0.87 | HIGH (many-to-many mapping) |
| Multi-Regulatory Objectives | 4 | MAXIMUM (5-regulation overlap) |
| CRITICAL Priority Objectives | 12 (36.4%) | HIGH (requires immediate attention) |
| Conflicts Identified | 3 | MODERATE (all resolved) |
| HIGH Assurance Objectives | 22 (66.7%) | HIGH (substantial audit burden) |

### 9.3 Implementation Sequencing

| Phase | Objectives | Rationale |
|-------|-------|-----------|
| Wave 1 (Immediate) | CRITICAL priority objectives (12) | Regulatory deadlines, financial penalties |
| Wave 2 (Near-term) | HIGH priority objectives (17) | Substantial compliance exposure |
| Wave 3 (Medium-term) | MODERATE priority objectives (4) | Standard remediation cycle |

### 9.4 OmniBank-Specific Considerations

| Consideration | Impact |
|---------------|--------|
| 5000+ employee scale | Objectives AG-D-08.1-002, AG-D-06.1-002 require enterprise-grade rollout |
| Financial sector regulation | DORA objectives carry additional ECB/PRA supervisory expectations |
| AI model deployment | AI Act obligations (AG-D-01.4, AG-D-02.4-002) require specialized AI governance |
| Critical infrastructure classification | NIS 2 objectives subject to national competent authority oversight |
| Multi-jurisdictional operations | GDPR objectives must satisfy EU + third-country adequacy requirements |

---

## 10. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-03 | Compliance Lead | Initial creation — 33 objectives (11 Privacy, 22 Security) derived from 38 obligations |

---

## 11. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Compliance Lead | [TBD] | | |
| CISO | [TBD] | | |
| Data Protection Officer | [TBD] | | |
| Chief Risk Officer | [TBD] | | |

---

**Next Step:** Use these objectives to derive the Rules Catalog (11_Rules_Catalog.md / 12_Rules_Catalog.xlsx) via Phase 2, Step E — Rules Elaboration.
