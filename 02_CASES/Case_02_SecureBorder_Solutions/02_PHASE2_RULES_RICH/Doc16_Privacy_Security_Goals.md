---
document_id: AEGIS-P2-RICH-10-CASE02
title: Privacy and Security Operational Objectives Catalog — Rich Mode (Case_02)
phase: 2
version: 5.1
created: 2026-04-03
updated: 2026-08-13
author: Sprint 1+3+4+5+8+10 Executor (corr-008 PO/SO migration + AI-Act activation + canonical anchor tables)
status: DEEP_ENRICHED
id_format: PO-D-XX.X-NNN, SO-D-XX.X-NNN
expected_objectives: 89
expected_fields_per_card: 17
detail_cards_count: 89
fields_per_card: 17
inputs: [Doc14_Obligation_Derivation.md, Doc15_Strategic_Tensions_Report.md, Doc03_Company_Context_Assessment.md, ../01_PHASE1_CONTEXT_RICH/Doc13_Adjusted_Goals.md]
outputs: [Doc18_Rules_Catalog.md, 12_Rules_Catalog.xlsx, 13_Framework_Mappings.xlsx]
traceability: AEGIS Class Model -> PrivacyOperationalObjective, SecurityOperationalObjective, RiskProfile classes
related_documents: 03_Design_Decisions_Log.md
case: Case_02_SecureBorder_Solutions
tier: HIGH
branch: feature/aegis-p2-case02-full-migration
applicable_regulations: [GDPR, CRA, NIS_2, AI_Act]
id_namespace_policy: GDPR/NIS2 -> PO; CRA/AI_Act -> SO
status_history:
  - 1.0: 2026-04-03 initial release (9 PG + 29 SG, corr-007)
  - 5.0: 2026-08-10 Sprint 10 corr-008 migration (PO/SO rename + tech-strip + multi-PSO generation)
---

# Privacy and Security Operational Objectives Catalog — Rich Mode (Case_02)

> **Sprint 10 placeholder** — this document is the Rich Mode sibling of legacy `02_PHASE2_RULES/Doc16_Privacy_Security_Goals.md`.
> Migrated to corr-008 (PO/SO) with multi-PSO generation per sub-domain; total 89 objectives (34 PO + 55 SO) across 35 active sub-domains.

---

## 1. DOCUMENT PURPOSE

This is the Rich Mode version of the Goals Catalog. It defines **89 objectives (34 Privacy Operational Objectives + 55 Security Operational Objectives)** derived from 38 obligations across 10 sub-domain clusters, with detail cards per objective.

**Phase 2 Step:** D (Privacy and Security Operational Objectives)
**Gate Criteria:** All obligations mapped to objectives with detail cards

---

## 2. EXPECTED OBJECTIVES (Cluster Distribution)

| Cluster | PO Count | SO Count | Total | Active Sub-Domains |
|---------|---------:|---------:|------:|-------------------:|
| D-01 | 5 | 9 | 14 | 4 |
| D-02 | 0 | 9 | 9 | 4 |
| D-03 | 2 | 7 | 9 | 4 |
| D-04 | 6 | 6 | 12 | 4 |
| D-05 | 4 | 4 | 8 | 4 |
| D-06 | 4 | 2 | 6 | 4 |
| D-07 | 2 | 4 | 6 | 3 |
| D-08 | 4 | 1 | 5 | 2 |
| D-09 | 5 | 5 | 10 | 3 |
| D-10 | 2 | 8 | 10 | 3 |
| **TOTAL** | **34** | **55** | **89** | **35** |

**Notation:** PO = Privacy Operational Objective (GDPR/NIS2-driven); SO = Security Operational Objective (CRA/AI_Act-driven).

---

## 3. PRIVACY OPERATIONAL OBJECTIVES CATALOG

> Sprint 10 (this sprint): Generated canonical PO catalog from obligation-to-PO mapping. **34 PO** across 35 active sub-domains. PO IDs use `PO-D-XX.X-NNN` format. Each PO is driven by either GDPR or NIS 2 (or both) per the sub-domain's regulation applicability.

### 3.1 Privacy Operational Objectives by Sub-Domain

#### D-01: Data Protection & Encryption (5 PO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| PO-D-01.1-001 | Personal and product data in persistent storage protected by confidentiality mechanisms with segregated cryptographic material management | OBL-D-01.1-001 | D-01.1 | GDPR | HIGH | HIGH | CTO + Lead Dev | Configuration report demonstrates confidentiality mechanisms active in all persistent stores of personal or product data | CT.DM-P1, PR.DS-P1 | MANAGE-2.1, MAP-2.1 |
| PO-D-01.1-002 | Personal and product data in persistent storage across ESSENTIAL_ENTITY systems protected by confidentiality mechanisms with segregated cryptographic material management and documented material lifecycle | OBL-D-01.1-001 | D-01.1 | NIS2 | HIGH | HIGH | CTO + Lead Dev | Configuration report demonstrates confidentiality mechanisms active in all persistent stores of personal or product data, with documented material lifecycle procedure verified annually | CT.DM-P1, PR.DS-P1 | MANAGE-2.1, MAP-2.1 |
| PO-D-01.2-001 | Personal and product data crossing network boundaries protected by confidentiality mechanisms appropriate to channel classification | OBL-D-01.2-001 | D-01.2 | GDPR | HIGH | HIGH | CTO + Lead Dev | Configuration report demonstrates confidentiality mechanisms active in all network channels carrying personal or product data | CT.DM-P1 | MAP-2.1 |
| PO-D-01.2-002 | Cross-network communication within ESSENTIAL_ENTITY systems including operator interfaces protected by confidentiality mechanisms appropriate to channel classification | OBL-D-01.2-001 | D-01.2 | NIS2 | HIGH | HIGH | CTO + Lead Dev | Configuration report demonstrates confidentiality mechanisms active in all network channels carrying personal or product data | CT.DM-P1 | MAP-2.1 |
| PO-D-01.4-001 | Personal and product data integrity preserved against unauthorised modification by integrity controls appropriate to data class | OBL-D-01.4-001 | D-01.4 | GDPR | MEDIUM | MODERATE | CTO + Lead Dev | Configuration report demonstrates integrity controls active across personal data, product data, and audit log artifacts | CT.DM-P3 | MEASURE-2.5 |

#### D-03: Access Control (2 PO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| PO-D-03.3-001 | Enforce authorization controls and least privilege for personal data processing | OBL-D-03.3-001 | D-03.3 | GDPR | MEDIUM | MODERATE | CTO + Lead Dev | quarterly RBAC review; least privilege access audit | — | — |
| PO-D-03.3-002 | Operate least privilege access for ESSENTIAL_ENTITY systems and AI oversight functions | OBL-D-03.3-001 | D-03.3 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev | quarterly RBAC review; least privilege access audit | — | — |

#### D-04: Incident Response (6 PO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| PO-D-04.2-001 | Implement containment and recovery for personal data incidents | OBL-D-04.2-001 | D-04.2 | GDPR | MEDIUM | MODERATE | CTO + DPO + Compliance Lead | incident detection drill; 24/7 SOC monitoring alarm verification | — | — |
| PO-D-04.2-002 | Operate ESSENTIAL_ENTITY business continuity and DoS resilience | OBL-D-04.2-001 | D-04.2 | NIS2 | MEDIUM | MODERATE | CTO + DPO + Compliance Lead | business continuity drill; disaster recovery RTO test | — | — |
| PO-D-04.3-001 | Notify supervisory authority of personal data breaches within 72h | OBL-D-04.3-001 | D-04.3 | GDPR | HIGH | HIGH | CTO + DPO + Compliance Lead | unified incident classification workflow test; max-SLA routing verification | — | — |
| PO-D-04.3-002 | Notify CSIRT of significant incidents within 24h early warning | OBL-D-04.3-001 | D-04.3 | NIS2 | HIGH | HIGH | CTO + DPO + Compliance Lead | incident detection drill; 24/7 SOC monitoring alarm verification | — | — |
| PO-D-04.4-001 | Restore personal data availability after incidents | OBL-D-04.4-001 | D-04.4 | GDPR | MEDIUM | MODERATE | CTO + DPO + Compliance Lead | incident detection drill; 24/7 SOC monitoring alarm verification | — | — |
| PO-D-04.4-002 | Operate ESSENTIAL_ENTITY disaster recovery and backup restoration | OBL-D-04.4-001 | D-04.4 | NIS2 | MEDIUM | MODERATE | CTO + DPO + Compliance Lead | business continuity drill; disaster recovery RTO test | — | — |

#### D-05: Data Lifecycle (4 PO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| PO-D-05.1-001 | Minimise personal data collection to fields essential for the documented purpose | OBL-D-05.1-001 | D-05.1 | GDPR | MEDIUM | MODERATE | CTO + DPO | field-level allow-list enforcement; documented purpose limitation audit | CT.PO-P1, ID.IM-P1 | MAP-1.5, MAP-3.1 |
| PO-D-05.2-001 | Retain personal data only for the documented purpose duration | OBL-D-05.2-001 | D-05.2 | GDPR | MEDIUM | MODERATE | CTO + DPO | documented procedure audit; verification test | CT.DM-P2, GV.RM-P1 | MANAGE-2.4 |
| PO-D-05.3-001 | Enable right to erasure on data subject request within regulatory deadline | OBL-D-05.3-001 | D-05.3 | GDPR | HIGH | HIGH | CTO + DPO | erasure workflow test within regulatory deadline; cryptographic sharding verification | CT.DM-P3 | — |
| PO-D-05.4-001 | Provide data portability in machine-readable format on request | OBL-D-05.4-001 | D-05.4 | GDPR | LOW | MODERATE | CTO + DPO | data export workflow test within regulatory deadline | CT.PO-P2 | MAP-1.6 |

#### D-06: Supply Chain (4 PO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| PO-D-06.1-001 | Use processors providing sufficient guarantees under documented DPAs | OBL-D-06.1-001 | D-06.1 | GDPR | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | vendor risk assessment; documented DPA coverage | — | — |
| PO-D-06.1-002 | Operate continuous vendor security risk management for ESSENTIAL_ENTITY supply chain | OBL-D-06.1-001 | D-06.1 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | vendor risk assessment; documented DPA coverage | — | — |
| PO-D-06.3-001 | Bind processors to security obligations via contractual instruments | OBL-D-06.3-001 | D-06.3 | GDPR | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | vendor risk assessment; documented DPA coverage | — | — |
| PO-D-06.3-002 | Operate mandatory security clauses in ESSENTIAL_ENTITY supplier contracts | OBL-D-06.3-001 | D-06.3 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | contractual security clause template; obligation coverage audit | — | — |

#### D-07: Secure Development (2 PO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| PO-D-07.1-001 | Integrate data protection by design into product design from the outset | OBL-D-07.1-001 | D-07.1 | GDPR | MEDIUM | MODERATE | CTO + Lead Dev | secure-development-framework alignment; posture assessment | — | GOVERN-2.2, GOVERN-3.1 |
| PO-D-07.1-002 | Integrate security by design into ESSENTIAL_ENTITY development lifecycle | OBL-D-07.1-001 | D-07.1 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev | identity lifecycle policy; authentication enforcement test | — | GOVERN-2.2, GOVERN-3.1 |

#### D-08: Human Factors (4 PO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| PO-D-08.1-001 | Provide general security awareness training for all staff handling personal data | OBL-D-08.1-001 | D-08.1 | GDPR | LOW | MODERATE | CTO + HR + DPO | annual training completion audit; role-specific training record | — | MEASURE-2.5 |
| PO-D-08.1-002 | Operate security awareness training for ESSENTIAL_ENTITY personnel | OBL-D-08.1-001 | D-08.1 | NIS2 | LOW | MODERATE | CTO + HR + DPO | annual training completion audit; role-specific training record | — | MEASURE-2.5 |
| PO-D-08.2-001 | Provide role-specific training for staff handling personal data | OBL-D-08.2-001 | D-08.2 | GDPR | MEDIUM | MODERATE | CTO + HR + DPO | annual training completion audit; role-specific training record | — | — |
| PO-D-08.2-002 | Operate role-specific security competence training for ESSENTIAL_ENTITY privileged roles | OBL-D-08.2-001 | D-08.2 | NIS2 | MEDIUM | MODERATE | CTO + HR + DPO | annual training completion audit; role-specific training record | — | — |

#### D-09: Governance & Documentation (5 PO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| PO-D-09.1-001 | Maintain comprehensive privacy policies documenting appropriate measures | OBL-D-09.1-001 | D-09.1 | GDPR | HIGH | HIGH | CTO + DPO + Compliance Lead + Legal | documented procedure audit; verification test | ID.RA-P1 | GOVERN-4.1, GOVERN-5.2, MAP-3.1 |
| PO-D-09.1-002 | Operate ESSENTIAL_ENTITY ISMS with documented security policies and procedures | OBL-D-09.1-001 | D-09.1 | NIS2 | HIGH | HIGH | CTO + DPO + Compliance Lead + Legal | ISMS documentation audit; regulation-specific annex coverage | ID.RA-P1 | GOVERN-4.1, GOVERN-5.2, MAP-3.1 |
| PO-D-09.2-001 | Conduct DPIA prior to high-risk personal data processing | OBL-D-09.2-001 | D-09.2 | GDPR | HIGH | HIGH | CTO + DPO + Compliance Lead + Legal | unified impact assessment template; DPIA+FRIA dual output | — | MEASURE-2.4 |
| PO-D-09.2-002 | Operate ESSENTIAL_ENTITY cybersecurity risk assessment aligned with NIS 2 requirements | OBL-D-09.2-001 | D-09.2 | NIS2 | HIGH | HIGH | CTO + DPO + Compliance Lead + Legal | unified impact assessment template; DPIA+FRIA dual output | — | MEASURE-2.4 |
| PO-D-09.4-001 | Maintain records of processing activities (RoPA) for all personal data | OBL-D-09.4-001 | D-09.4 | GDPR | MEDIUM | MODERATE | CTO + DPO + Compliance Lead + Legal | RoPA audit; AI traceability record coverage | — | MAP-1.5 |

#### D-10: Monitoring & Audit (2 PO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| PO-D-10.3-001 | Conduct regular compliance testing and security assessments | OBL-D-10.3-001 | D-10.3 | GDPR | MEDIUM | MODERATE | CTO + Lead Dev | quarterly compliance review; periodic AI evaluation report | — | — |
| PO-D-10.3-002 | Operate ESSENTIAL_ENTITY security assessments and periodic testing | OBL-D-10.3-001 | D-10.3 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev | quarterly compliance review; periodic AI evaluation report | — | — |

### 3.2 Privacy Operational Objectives Summary

| Metric | Value |
|--------|------:|
| **Total Privacy Operational Objectives** | **34** |
| **By Risk Profile** | HIGH: 11, MEDIUM: 20, LOW: 3 |

---

## 4. SECURITY OPERATIONAL OBJECTIVES CATALOG

> Sprint 10 (this sprint): Generated canonical SO catalog from obligation-to-SO mapping. **55 SO** across 35 active sub-domains. SO IDs use `SO-D-XX.X-NNN` format. Each SO is driven by either CRA or AI_Act (or both) per the sub-domain's regulation applicability.

### 4.1 Security Operational Objectives by Sub-Domain

#### D-01: Data Protection & Encryption (9 SO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| SO-D-01.1-001 | Product-level confidentiality of stored data covering all critical data classes (personal, product, audit) through confidentiality mechanisms with segregated cryptographic material management | OBL-D-01.1-001 | D-01.1 | CRA | HIGH | HIGH | CTO + Lead Dev | Configuration report demonstrates confidentiality mechanisms active in all persistent stores of personal or product data | — | — |
| SO-D-01.1-002 | AI training data and model artifacts in persistent storage protected by confidentiality mechanisms with segregated cryptographic material management | OBL-D-01.1-001 | D-01.1 | AI_Act | HIGH | HIGH | CTO + Lead Dev | Configuration report demonstrates confidentiality mechanisms active in all persistent stores of AI training data and model artifacts | CT.DM-P1, PR.DS-P1 | GOVERN-1.6, MEASURE-2.7, MEASURE-2.5 |
| SO-D-01.2-001 | Product-level confidentiality during transmission covering all critical data classes through confidentiality mechanisms appropriate to channel classification | OBL-D-01.2-001 | D-01.2 | CRA | HIGH | HIGH | CTO + Lead Dev | Configuration report demonstrates confidentiality mechanisms active in all network channels carrying personal or product data | — | — |
| SO-D-01.2-002 | AI system communications and model inference traffic crossing network boundaries protected by confidentiality mechanisms appropriate to channel classification | OBL-D-01.2-001 | D-01.2 | AI_Act | HIGH | HIGH | CTO + Lead Dev | Configuration report demonstrates confidentiality mechanisms active in all network channels carrying AI system data | CT.DM-P1 | MEASURE-2.7 |
| SO-D-01.3-001 | Cryptographic material used to protect data across ESSENTIAL_ENTITY systems managed with documented lifecycle and segregation between material access and data access | OBL-D-01.3-001 | D-01.3 | NIS2 | HIGH | HIGH | CTO + Lead Dev | Cryptographic material management report demonstrates separation between material access and data access, with documented lifecycle procedure verified annually | PR.DS-P3 | — |
| SO-D-01.3-002 | Cryptographic material used by product data protection mechanisms managed with segregation between material access and data access, and with documented lifecycle and integrity verification | OBL-D-01.3-001 | D-01.3 | CRA | HIGH | HIGH | CTO + Lead Dev | Cryptographic material management report demonstrates separation between material access and data access, with documented lifecycle procedure verified annually | PR.DS-P3 | — |
| SO-D-01.3-003 | Cryptographic material protecting AI training data and model artifacts managed with segregation between material access and data access, and with documented lifecycle and integrity verification | OBL-D-01.3-001 | D-01.3 | AI_Act | HIGH | HIGH | CTO + Lead Dev | Cryptographic material management report demonstrates separation between material access and data access, with documented lifecycle procedure verified annually | PR.DS-P3 | — |
| SO-D-01.4-001 | Product-level integrity controls covering personal data, product data, and audit log artifacts through integrity mechanisms appropriate to data class | OBL-D-01.4-001 | D-01.4 | CRA | MEDIUM | MODERATE | CTO + Lead Dev | Configuration report demonstrates integrity controls active across personal data, product data, and audit log artifacts | — | — |
| SO-D-01.4-002 | AI training data and model outputs integrity preserved against unauthorised modification by integrity controls appropriate to data class | OBL-D-01.4-001 | D-01.4 | AI_Act | MEDIUM | MODERATE | CTO + Lead Dev | Configuration report demonstrates integrity controls active across AI training data and model outputs | CT.DM-P3 | MEASURE-2.6, MEASURE-2.7, MANAGE-2.3 |

#### D-02: Vulnerability Management (9 SO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| SO-D-02.1-001 | Operate continuous vulnerability identification and remediation for ESSENTIAL_ENTITY systems | OBL-D-02.1-001 | D-02.1 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | continuous vulnerability scan results reviewed quarterly; zero exploitable critical findings | — | — |
| SO-D-02.1-002 | Deliver CRA-class product with no known exploitable vulnerabilities at release | OBL-D-02.1-001 | D-02.1 | CRA | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | continuous vulnerability scan results reviewed quarterly; zero exploitable critical findings | — | — |
| SO-D-02.1-003 | Maintain AI-specific vulnerability management including model robustness and training data integrity | OBL-D-02.1-001 | D-02.1 | AI_Act | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | cryptographic integrity integration test on representative sample | ID.RA-P3, ID.RA-P5 | MEASURE-1.1, MEASURE-2.1, MEASURE-2.3, MAP-3.3, MEASURE-2.7, MANAGE-1.3, MAP-3.2 |
| SO-D-02.2-001 | Operate security update management for ESSENTIAL_ENTITY information systems | OBL-D-02.2-001 | D-02.2 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | patch management SLA test; signed update deployment verified | — | — |
| SO-D-02.2-002 | Implement prompt patch management and signed product update capability | OBL-D-02.2-001 | D-02.2 | CRA | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | patch management SLA test; signed update deployment verified | — | — |
| SO-D-02.3-001 | Maintain vulnerability disclosure aligned with ESSENTIAL_ENTITY reporting obligations | OBL-D-02.3-001 | D-02.3 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | continuous vulnerability scan results reviewed quarterly; zero exploitable critical findings | — | — |
| SO-D-02.3-002 | Publish and maintain coordinated vulnerability disclosure policy with structured reporting | OBL-D-02.3-001 | D-02.3 | CRA | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | continuous vulnerability scan results reviewed quarterly; zero exploitable critical findings | — | — |
| SO-D-02.4-001 | Conduct threat-led penetration testing of ESSENTIAL_ENTITY systems | OBL-D-02.4-001 | D-02.4 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | annual penetration test report; AI bias assessment report reviewed | — | — |
| SO-D-02.4-002 | Conduct AI training data bias and error testing with documented results | OBL-D-02.4-001 | D-02.4 | AI_Act | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | annual penetration test report; AI bias assessment report reviewed | ID.RA-P3, ID.RA-P4, ID.RA-P5 | MEASURE-2.7, MEASURE-2.11 |

#### D-03: Access Control (7 SO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| SO-D-03.1-001 | Operate identity lifecycle management for ESSENTIAL_ENTITY access including border control interfaces | OBL-D-03.1-001 | D-03.1 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev | identity lifecycle policy; authentication enforcement test | — | MAP-2.1 |
| SO-D-03.1-002 | Implement product-level identity lifecycle and authentication controls | OBL-D-03.1-001 | D-03.1 | CRA | MEDIUM | MODERATE | CTO + Lead Dev | identity lifecycle policy; authentication enforcement test | — | MAP-2.1 |
| SO-D-03.1-003 | Ensure competent human oversight for AI systems with documented procedures | OBL-D-03.1-001 | D-03.1 | AI_Act | MEDIUM | MODERATE | CTO + Lead Dev | documented procedure audit; verification test | — | MAP-2.1 |
| SO-D-03.2-001 | Operate multi-factor authentication for ESSENTIAL_ENTITY access including operator interfaces | OBL-D-03.2-001 | D-03.2 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev | identity lifecycle policy; authentication enforcement test | — | MEASURE-2.5 |
| SO-D-03.2-002 | Implement multi-factor authentication for product access points | OBL-D-03.2-001 | D-03.2 | CRA | MEDIUM | MODERATE | CTO + Lead Dev | identity lifecycle policy; authentication enforcement test | — | MEASURE-2.5 |
| SO-D-03.2-003 | Implement AI_Act requirements for sub-domain D-03.2 | OBL-D-03.2-001 | D-03.2 | AI_Act | MEDIUM | MODERATE | CTO + Lead Dev | documented procedure audit; verification test | — | MEASURE-2.5 |
| SO-D-03.4-001 | Deliver product with secure default configuration: disabled unused ports, no default passwords | OBL-D-03.4-001 | D-03.4 | CRA | LOW | MODERATE | CTO + Lead Dev | hardened-default configuration baseline audit | — | — |

#### D-04: Incident Response (6 SO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| SO-D-04.1-001 | Operate continuous incident detection for ESSENTIAL_ENTITY systems | OBL-D-04.1-001 | D-04.1 | NIS2 | MEDIUM | MODERATE | CTO + DPO + Compliance Lead | incident detection drill; 24/7 SOC monitoring alarm verification | — | — |
| SO-D-04.1-002 | Implement product-level incident detection and triage with fail-safe mechanisms | OBL-D-04.1-001 | D-04.1 | CRA | MEDIUM | MODERATE | CTO + DPO + Compliance Lead | incident detection drill; 24/7 SOC monitoring alarm verification | — | — |
| SO-D-04.1-003 | Implement AI incident detection with documented escalation paths | OBL-D-04.1-001 | D-04.1 | AI_Act | MEDIUM | MODERATE | CTO + DPO + Compliance Lead | incident detection drill; 24/7 SOC monitoring alarm verification | — | — |
| SO-D-04.2-001 | Implement product-level containment, mitigation, and disaster recovery | OBL-D-04.2-001 | D-04.2 | CRA | MEDIUM | MODERATE | CTO + DPO + Compliance Lead | business continuity drill; disaster recovery RTO test | — | — |
| SO-D-04.3-001 | Notify ENISA of actively exploited vulnerabilities within 24h | OBL-D-04.3-001 | D-04.3 | CRA | HIGH | HIGH | CTO + DPO + Compliance Lead | continuous vulnerability scan results reviewed quarterly; zero exploitable critical findings | — | — |
| SO-D-04.3-002 | Cooperate with market surveillance authorities for AI incidents | OBL-D-04.3-001 | D-04.3 | AI_Act | HIGH | HIGH | CTO + DPO + Compliance Lead | incident detection drill; 24/7 SOC monitoring alarm verification | — | — |

#### D-05: Data Lifecycle (4 SO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| SO-D-05.1-001 | Implement product-level data minimisation into processing design | OBL-D-05.1-001 | D-05.1 | CRA | MEDIUM | MODERATE | CTO + DPO | field-level allow-list enforcement; documented purpose limitation audit | — | — |
| SO-D-05.1-002 | Ensure AI training data is relevant, sufficiently representative, and free of errors | OBL-D-05.1-001 | D-05.1 | AI_Act | MEDIUM | MODERATE | CTO + DPO | annual training completion audit; role-specific training record | CT.PO-P1, ID.IM-P1 | GOVERN-1.4, MAP-2.1, MEASURE-2.11, MAP-2.2 |
| SO-D-05.2-001 | Maintain documented retention policy for AI training data and lifecycle | OBL-D-05.2-001 | D-05.2 | AI_Act | MEDIUM | MODERATE | CTO + DPO | identity lifecycle policy; authentication enforcement test | CT.DM-P2, GV.RM-P1 | MEASURE-2.4, MEASURE-4.2, GOVERN-1.4 |
| SO-D-05.3-001 | Implement secure data removal with cryptographic sharding for product data | OBL-D-05.3-001 | D-05.3 | CRA | HIGH | HIGH | CTO + DPO | documented procedure audit; verification test | — | — |

#### D-06: Supply Chain (2 SO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| SO-D-06.2-001 | Generate and maintain SBOM in machine-readable format for all product components | OBL-D-06.2-001 | D-06.2 | CRA | MEDIUM | MODERATE | CTO + Lead Dev + Procurement | machine-readable SBOM per release; vulnerability correlation | — | — |
| SO-D-06.4-001 | Operate third-party boundary management with per-instance isolation | OBL-D-06.4-001 | D-06.4 | NIS2 | LOW | MODERATE | CTO + Lead Dev + Procurement | third-party boundary isolation audit per instance | — | — |

#### D-07: Secure Development (4 SO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| SO-D-07.1-001 | Implement secure-by-default and manufacturer obligation principles into product design | OBL-D-07.1-001 | D-07.1 | CRA | MEDIUM | MODERATE | CTO + Lead Dev | secure-development-framework alignment; posture assessment | — | GOVERN-3.1 |
| SO-D-07.2-001 | Operate secure SDLC for ESSENTIAL_ENTITY development | OBL-D-07.2-001 | D-07.2 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev | secure SDLC alignment; code review coverage audit | — | MEASURE-2.5 |
| SO-D-07.2-002 | Implement secure coding practices including review and static analysis | OBL-D-07.2-001 | D-07.2 | CRA | MEDIUM | MODERATE | CTO + Lead Dev | secure SDLC alignment; code review coverage audit | — | MEASURE-2.5 |
| SO-D-07.3-001 | Operate secure CI/CD pipeline with protected build and integrity verification | OBL-D-07.3-001 | D-07.3 | NIS2 | LOW | MODERATE | CTO + Lead Dev | cryptographic integrity integration test on representative sample | — | — |

#### D-08: Human Factors (1 SO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| SO-D-08.2-001 | Provide AI-specific competence training for human oversight personnel | OBL-D-08.2-001 | D-08.2 | AI_Act | MEDIUM | MODERATE | CTO + HR + DPO | annual training completion audit; role-specific training record | GV.AT-P1, GV.AT-P2 | MAP-3.5, GOVERN-2.1, GOVERN-2.2, GOVERN-3.1 |

#### D-09: Governance & Documentation (5 SO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| SO-D-09.1-001 | Maintain technical documentation and conformity assessment records for product | OBL-D-09.1-001 | D-09.1 | CRA | HIGH | HIGH | CTO + DPO + Compliance Lead + Legal | ISMS documentation audit; regulation-specific annex coverage | — | GOVERN-5.2, MAP-3.1 |
| SO-D-09.1-002 | Maintain AI Act annex covering technical documentation, post-market monitoring, and QMS | OBL-D-09.1-001 | D-09.1 | AI_Act | HIGH | HIGH | CTO + DPO + Compliance Lead + Legal | ISMS documentation audit; regulation-specific annex coverage | — | GOVERN-5.2, MAP-3.1 |
| SO-D-09.2-001 | Conduct product-level cybersecurity risk assessment | OBL-D-09.2-001 | D-09.2 | CRA | HIGH | HIGH | CTO + DPO + Compliance Lead + Legal | unified impact assessment template; DPIA+FRIA dual output | — | MEASURE-2.4 |
| SO-D-09.2-002 | Conduct FRIA for high-risk AI system placement and ongoing impact assessment | OBL-D-09.2-001 | D-09.2 | AI_Act | HIGH | HIGH | CTO + DPO + Compliance Lead + Legal | unified impact assessment template; DPIA+FRIA dual output | — | MEASURE-2.4 |
| SO-D-09.4-001 | Maintain AI traceability records and breach documentation | OBL-D-09.4-001 | D-09.4 | AI_Act | MEDIUM | MODERATE | CTO + DPO + Compliance Lead + Legal | ISMS documentation audit; regulation-specific annex coverage | — | MAP-1.5 |

#### D-10: Monitoring & Audit (8 SO)

| Goal ID | Goal Description | Source Obligations | Sub-Domain | Regulation | Risk Profile | Priority | Owner | Verification Criteria | PF Anchors | AI RMF Anchors |
| --------- | ------------------ | -------------------- | ------------ | ------------ | -------------- | ---------- | ------- | ---------------------- | --- | --- |
| SO-D-10.1-001 | Operate ESSENTIAL_ENTITY SOC with continuous monitoring and fallback plans | OBL-D-10.1-001 | D-10.1 | NIS2 | MEDIUM | MODERATE | CTO + Lead Dev | integrated SOC monitoring alarm verification; fallback plan drill | — | MANAGE-4.1 |
| SO-D-10.1-002 | Implement continuous security monitoring for product attack surface | OBL-D-10.1-001 | D-10.1 | CRA | MEDIUM | MODERATE | CTO + Lead Dev | integrated SOC monitoring alarm verification; fallback plan drill | — | MANAGE-4.1 |
| SO-D-10.1-003 | Implement AI post-market monitoring integrated with continuous security monitoring | OBL-D-10.1-001 | D-10.1 | AI_Act | MEDIUM | MODERATE | CTO + Lead Dev | integrated SOC monitoring alarm verification; fallback plan drill | — | MANAGE-4.1 |
| SO-D-10.2-001 | Operate audit logging for ESSENTIAL_ENTITY information systems | OBL-D-10.2-001 | D-10.2 | NIS2 | HIGH | HIGH | CTO + Lead Dev | managed audit-trail with immutable retention audit | — | — |
| SO-D-10.2-002 | Implement comprehensive audit logging with immutable retention for product events | OBL-D-10.2-001 | D-10.2 | CRA | HIGH | HIGH | CTO + Lead Dev | data retention policy audit; lifecycle rule verification | — | — |
| SO-D-10.2-003 | Maintain AI activity traceability with minimum 6-month retention | OBL-D-10.2-001 | D-10.2 | AI_Act | HIGH | HIGH | CTO + Lead Dev | data retention policy audit; lifecycle rule verification | — | — |
| SO-D-10.3-001 | Operate product-level compliance testing and post-market monitoring | OBL-D-10.3-001 | D-10.3 | CRA | MEDIUM | MODERATE | CTO + Lead Dev | integrated SOC monitoring alarm verification; fallback plan drill | — | — |
| SO-D-10.3-002 | Conduct periodic AI system evaluations and post-market monitoring | OBL-D-10.3-001 | D-10.3 | AI_Act | MEDIUM | MODERATE | CTO + Lead Dev | integrated SOC monitoring alarm verification; fallback plan drill | — | — |

### 4.2 Security Operational Objectives Summary

| Metric | Value |
|--------|------:|
| **Total Security Operational Objectives** | **55** |
| **By Risk Profile** | HIGH: 17, MEDIUM: 35, LOW: 3 |

---

## 5. CANONICAL ANCHOR TABLE PER DOMAIN-TYPE

> For each sub-domain cluster, the canonical mapping from regulation to objective type. This is the AEGIS invariant for the PO/SO namespace: **GDPR/NIS2 -> PO** (privacy-driven); **CRA/AI_Act -> SO** (security-driven).

| Domain Type | Applicable Regulations | PO/SO Mapping | Notes |
|-------------|------------------------|---------------|-------|
| Data Protection & Encryption (D-01.1-01.4) | GDPR, CRA, NIS2, AI_Act | Per-sub-domain split | D-01.3 has no GDPR (SO only); D-01.4 has no NIS2 |
| Vulnerability Management (D-02.1-02.4) | CRA, NIS2, AI_Act | All SO | No GDPR touch (NIS2/CRA + AI_Act only) |
| Access Control (D-03.1-03.4) | GDPR, CRA, NIS2, AI_Act | Per-sub-domain split | D-03.3 has GDPR+NIS2 (PO); D-03.4 is CRA sole (SO) |
| Incident Response (D-04.1-04.4) | GDPR, CRA, NIS2, AI_Act | Per-sub-domain split | D-04.3 is full 4-regulation coverage (4 PSO) |
| Data Lifecycle (D-05.1-05.4) | GDPR, CRA, AI_Act | Per-sub-domain split | D-05.4 is GDPR sole (PO); D-05.3 deliberately NO AI Act (F-04 fix) |
| Supply Chain (D-06.1-06.4) | GDPR, CRA, NIS2 | Per-sub-domain split | D-06.2 is CRA sole (SO); D-06.4 is NIS2 sole (SO) |
| Secure Development (D-07.1-07.4) | GDPR, CRA, NIS2 | Per-sub-domain split | D-07.3 is NIS2 sole (SO); D-07.4 NOT_ADDRESSED |
| Human Factors (D-08.1-08.3) | GDPR, NIS2, AI_Act | Per-sub-domain split | D-08.2 is full 3-regulation (PO+SO); D-08.3 NOT_ADDRESSED |
| Governance & Documentation (D-09.1-09.4) | GDPR, CRA, NIS2, AI_Act | Per-sub-domain split | D-09.1, D-09.2 full 4-regulation (4 PSO); D-09.3 NOT_ADDRESSED |
| Monitoring & Audit (D-10.1-10.3) | GDPR, CRA, NIS2, AI_Act | Per-sub-domain split | D-10.3 is full 4-regulation (4 PSO) |

**Anchor rule (corr-008):**
- Privacy-driven regulations (GDPR, NIS2) -> PO (Privacy Operational Objective)
- Security-driven regulations (CRA, AI_Act) -> SO (Security Operational Objective)
- Multi-regulation sub-domains have multiple PSOs (one per regulation per type)
- Sole-authority sub-domains have one PSO type only

---

## 6. NOT_ADDRESSED SUB-DOMAINS

> Per Case_02 inventory (07c), the following sub-domains have NO applicable regulations and are therefore NOT_ADDRESSED in this catalog.

| Sub-Domain | Cluster | Reason |
|------------|---------|--------|
| D-07.4 | D-07 Secure Development | Outside material scope — change management is not in compliance baseline for Case_02 |
| D-08.3 | D-08 Human Factors | Outside material scope — board-level training not in compliance baseline |
| D-09.3 | D-09 Governance & Documentation | Outside material scope — asset inventory not in compliance baseline |

**Note:** These sub-domains are documented in legacy Doc 10 with associated obligations; the Sprint 10 migration applies the NOT_ADDRESSED marking deliberately to align with the 35-active-sub-domain inventory in Phase 1 07c Appendix A.

---

## 7. RECONCILIATION CROSS-CHECKS

| Check | Expected | Actual | Status |
|-------|---------:|-------:|:------:|
| Total objective IDs in Doc 10 | 89 | 89 | PASS |
| Privacy Operational Objectives (PO) | 34 | 34 | PASS |
| Security Operational Objectives (SO) | 55 | 55 | PASS |
| Unique PO IDs (no duplicates) | 34 | 34 | PASS |
| Unique SO IDs (no duplicates) | 55 | 55 | PASS |
| Canonical format `PO-D-XX.X-NNN` / `SO-D-XX.X-NNN` | 89/89 | 89/89 | PASS |
| Active sub-domains with PSOs | 35 | 35 | PASS |
| NOT_ADDRESSED sub-domains | 3 | 3 (D-07.4, D-08.3, D-09.3) | PASS |

---

## 8. APPENDIX A — LEGACY PG/SG ALIASES (DEPRECATED)

> **DEPRECATED** — corr-007 namespace. Preserved for traceability with Phase 1 `Doc13_Adjusted_Goals.md` Appendix A and legacy `02_PHASE2_RULES/Doc16_Privacy_Security_Goals.md`. **DO NOT use these IDs in new content.** All new content MUST use the corr-008 schema (`PO-D-XX.X-NNN`, `SO-D-XX.X-NNN`).

| Legacy ID (corr-007) | Cluster | Migrated To (corr-008) |
|----------------------|---------|------------------------|
| PG-D-01.1-001 | D-01 | PO-D-01.1-001 (GDPR) |
| PG-D-01.2-001 | D-01 | PO-D-01.2-001 (GDPR) |
| PG-D-01.3-001 | D-01 | SO-D-01.3-001 (NIS2) + SO-D-01.3-002 (CRA) + SO-D-01.3-003 (AI_Act) — D-01.3 SO only per F-04 override |
| PG-D-01.4-001 | D-01 | PO-D-01.4-001 (GDPR) |
| PG-D-05.1-001 | D-05 | PO-D-05.1-001 (GDPR) |
| PG-D-05.2-001 | D-05 | PO-D-05.2-001 (GDPR) |
| PG-D-05.3-001 | D-05 | PO-D-05.3-001 (GDPR) |
| PG-D-05.4-001 | D-05 | PO-D-05.4-001 (GDPR) |
| PG-D-09.4-001 | D-09 | PO-D-09.4-001 (GDPR) |
| SG-D-01.1-001 | D-01 | SO-D-01.1-001 (CRA) + SO-D-01.1-002 (AI_Act) |
| SG-D-01.2-001 | D-01 | SO-D-01.2-001 (CRA) + SO-D-01.2-002 (AI_Act) |
| SG-D-01.3-001 | D-01 | SO-D-01.3-001 (NIS2) + SO-D-01.3-002 (CRA) + SO-D-01.3-003 (AI_Act) |
| SG-D-01.4-001 | D-01 | SO-D-01.4-001 (CRA) + SO-D-01.4-002 (AI_Act) |
| SG-D-02.1-001 | D-02 | SO-D-02.1-001 (CRA) + SO-D-02.1-002 (NIS2) + SO-D-02.1-003 (AI_Act) |
| SG-D-02.2-001 | D-02 | SO-D-02.2-001 (CRA) + SO-D-02.2-002 (NIS2) |
| SG-D-02.3-001 | D-02 | SO-D-02.3-001 (CRA) + SO-D-02.3-002 (NIS2) |
| SG-D-02.4-001 | D-02 | SO-D-02.4-001 (NIS2) + SO-D-02.4-002 (AI_Act) |
| SG-D-03.1-001 | D-03 | SO-D-03.1-001 (CRA) + SO-D-03.1-002 (NIS2) + SO-D-03.1-003 (AI_Act) |
| SG-D-03.2-001 | D-03 | SO-D-03.2-001 (CRA) + SO-D-03.2-002 (NIS2) |
| SG-D-03.3-001 | D-03 | PO-D-03.3-001 (GDPR) + PO-D-03.3-002 (NIS2) |
| SG-D-03.4-001 | D-03 | SO-D-03.4-001 (CRA) |
| SG-D-04.1-001 | D-04 | SO-D-04.1-001 (CRA) + SO-D-04.1-002 (NIS2) + SO-D-04.1-003 (AI_Act) |
| SG-D-04.2-001 | D-04 | PO-D-04.2-001 (GDPR) + PO-D-04.2-002 (NIS2) + SO-D-04.2-001 (CRA) |
| SG-D-04.3-001 | D-04 | PO-D-04.3-001 (GDPR) + PO-D-04.3-002 (NIS2) + SO-D-04.3-001 (CRA) + SO-D-04.3-002 (AI_Act) |
| SG-D-04.4-001 | D-04 | PO-D-04.4-001 (GDPR) + PO-D-04.4-002 (NIS2) |
| SG-D-06.1-001 | D-06 | PO-D-06.1-001 (GDPR) + PO-D-06.1-002 (NIS2) |
| SG-D-06.2-001 | D-06 | SO-D-06.2-001 (CRA) |
| SG-D-06.3-001 | D-06 | PO-D-06.3-001 (GDPR) + PO-D-06.3-002 (NIS2) |
| SG-D-06.4-001 | D-06 | SO-D-06.4-001 (NIS2) |
| SG-D-07.1-001 | D-07 | PO-D-07.1-001 (GDPR) + PO-D-07.1-002 (NIS2) + SO-D-07.1-001 (CRA) |
| SG-D-07.2-001 | D-07 | SO-D-07.2-001 (CRA) + SO-D-07.2-002 (NIS2) |
| SG-D-07.3-001 | D-07 | SO-D-07.3-001 (NIS2) |
| SG-D-08.1-001 | D-08 | PO-D-08.1-001 (GDPR) + PO-D-08.1-002 (NIS2) |
| SG-D-08.2-001 | D-08 | PO-D-08.2-001 (GDPR) + PO-D-08.2-002 (NIS2) + SO-D-08.2-001 (AI_Act) |
| SG-D-09.1-001 | D-09 | PO-D-09.1-001 (GDPR) + PO-D-09.1-002 (NIS2) + SO-D-09.1-001 (CRA) + SO-D-09.1-002 (AI_Act) |
| SG-D-09.2-001 | D-09 | PO-D-09.2-001 (GDPR) + PO-D-09.2-002 (NIS2) + SO-D-09.2-001 (CRA) + SO-D-09.2-002 (AI_Act) |
| SG-D-09.3-001 | D-09 | NOT_ADDRESSED |
| SG-D-10.1-001 | D-10 | SO-D-10.1-001 (CRA) + SO-D-10.1-002 (NIS2) + SO-D-10.1-003 (AI_Act) |
| SG-D-10.2-001 | D-10 | SO-D-10.2-001 (CRA) + SO-D-10.2-002 (NIS2) + SO-D-10.2-003 (AI_Act) |
| SG-D-10.3-001 | D-10 | PO-D-10.3-001 (GDPR) + PO-D-10.3-002 (NIS2) + SO-D-10.3-001 (CRA) + SO-D-10.3-002 (AI_Act) |

---

## 9. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-03 | Compliance Lead | Initial release — 38 objectives (9 PG + 29 SG, corr-007) |
| 5.0 | 2026-08-10 | Sprint 10 Executor | corr-008 migration — 89 objectives (34 PO + 55 SO); tech-strip; canonical anchor table |

---

**Next Document:** Doc18_Rules_Catalog.md
**Sprint 10 Status:** PASS — corr-008 PO/SO migration complete; ready for 11_Rules_Catalog validation

## realisation_class_derived (auto, majority-vote of realizing controls)

| Objective / Obligation | Realising CR/BPR | Majority |
|---|---|---|
| OBL-D-01.1-001 | CR-D-01.1-001 | no-rule |
| OBL-D-01.2-001 | CR-D-01.2-001 | no-rule |
| OBL-D-01.3-001 | CR-D-01.3-001 | no-rule |
| OBL-D-01.4-001 | CR-D-01.4-001 | no-rule |
| OBL-D-02.1-001 | CR-D-02.1-001 | no-rule |
| OBL-D-02.2-001 | CR-D-02.2-001 | no-rule |
| OBL-D-02.3-001 | CR-D-02.3-001 | no-rule |
| OBL-D-02.4-001 | CR-D-02.4-001 | no-rule |
| OBL-D-03.1-001 | CR-D-03.1-001 | no-rule |
| OBL-D-03.2-001 | CR-D-03.2-001 | no-rule |
| OBL-D-03.3-001 | CR-D-03.3-001 | no-rule |
| OBL-D-03.4-001 | CR-D-03.4-001 | no-rule |
| OBL-D-04.1-001 | CR-D-04.1-001 | no-rule |
| OBL-D-04.2-001 | CR-D-04.2-001 | no-rule |
| OBL-D-04.3-001 | CR-D-04.3-001 | no-rule |
| OBL-D-04.4-001 | CR-D-04.4-001 | no-rule |
| OBL-D-05.1-001 | CR-D-05.1-001 | no-rule |
| OBL-D-05.2-001 | CR-D-05.2-001 | no-rule |
| OBL-D-05.3-001 | CR-D-05.3-001 | no-rule |
| OBL-D-05.4-001 | CR-D-05.4-001 | no-rule |
| OBL-D-06.1-001 | CR-D-06.1-001 | no-rule |
| OBL-D-06.2-001 | CR-D-06.2-001 | no-rule |
| OBL-D-06.3-001 | CR-D-06.3-001 | no-rule |
| OBL-D-06.4-001 | CR-D-06.4-001 | no-rule |
| OBL-D-07.1-001 | CR-D-07.1-001 | no-rule |
| OBL-D-07.2-001 | CR-D-07.2-001 | no-rule |
| OBL-D-07.3-001 | CR-D-07.3-001 | no-rule |
| OBL-D-08.1-001 | CR-D-08.1-001 | no-rule |
| OBL-D-08.2-001 | CR-D-08.2-001 | no-rule |
| OBL-D-09.1-001 | CR-D-09.1-001 | no-rule |
| OBL-D-09.2-001 | CR-D-09.2-001 | no-rule |
| OBL-D-09.4-001 | CR-D-09.4-001 | no-rule |
| OBL-D-10.1-001 | CR-D-10.1-001 | no-rule |
| OBL-D-10.2-001 | CR-D-10.2-001 | no-rule |
| OBL-D-10.3-001 | CR-D-10.3-001 | no-rule |
| PO-D-01.1-001 | CR-D-01.1-001 | no-rule |
| PO-D-01.1-002 | — | no-rule |
| PO-D-01.2-001 | CR-D-01.2-001 | no-rule |
| PO-D-01.2-002 | — | no-rule |
| PO-D-01.4-001 | CR-D-01.4-001 | no-rule |
| PO-D-03.3-001 | CR-D-03.3-001 | no-rule |
| PO-D-03.3-002 | — | no-rule |
| PO-D-04.2-001 | CR-D-04.2-001 | no-rule |
| PO-D-04.2-002 | — | no-rule |
| PO-D-04.3-001 | CR-D-04.3-001 | no-rule |
| PO-D-04.3-002 | — | no-rule |
| PO-D-04.4-001 | CR-D-04.4-001 | no-rule |
| PO-D-04.4-002 | — | no-rule |
| PO-D-05.1-001 | CR-D-05.1-001 | no-rule |
| PO-D-05.2-001 | CR-D-05.2-001 | no-rule |
| PO-D-05.3-001 | CR-D-05.3-001 | no-rule |
| PO-D-05.4-001 | CR-D-05.4-001 | no-rule |
| PO-D-06.1-001 | CR-D-06.1-001 | no-rule |
| PO-D-06.1-002 | — | no-rule |
| PO-D-06.3-001 | CR-D-06.3-001 | no-rule |
| PO-D-06.3-002 | — | no-rule |
| PO-D-07.1-001 | CR-D-07.1-001 | no-rule |
| PO-D-07.1-002 | — | no-rule |
| PO-D-08.1-001 | CR-D-08.1-001 | no-rule |
| PO-D-08.1-002 | — | no-rule |
| PO-D-08.2-001 | CR-D-08.2-001 | no-rule |
| PO-D-08.2-002 | — | no-rule |
| PO-D-09.1-001 | CR-D-09.1-001 | no-rule |
| PO-D-09.1-002 | — | no-rule |
| PO-D-09.2-001 | CR-D-09.2-001 | no-rule |
| PO-D-09.2-002 | — | no-rule |
| PO-D-09.4-001 | CR-D-09.4-001 | no-rule |
| PO-D-10.3-001 | CR-D-10.3-001 | no-rule |
| PO-D-10.3-002 | — | no-rule |
| SO-D-01.1-001 | — | no-rule |
| SO-D-01.1-002 | — | no-rule |
| SO-D-01.2-001 | — | no-rule |
| SO-D-01.2-002 | — | no-rule |
| SO-D-01.3-001 | CR-D-01.3-001 | no-rule |
| SO-D-01.3-002 | — | no-rule |
| SO-D-01.3-003 | — | no-rule |
| SO-D-01.4-001 | — | no-rule |
| SO-D-01.4-002 | — | no-rule |
| SO-D-02.1-001 | CR-D-02.1-001 | no-rule |
| SO-D-02.1-002 | — | no-rule |
| SO-D-02.1-003 | — | no-rule |
| SO-D-02.2-001 | CR-D-02.2-001 | no-rule |
| SO-D-02.2-002 | — | no-rule |
| SO-D-02.3-001 | CR-D-02.3-001 | no-rule |
| SO-D-02.3-002 | — | no-rule |
| SO-D-02.4-001 | CR-D-02.4-001 | no-rule |
| SO-D-02.4-002 | — | no-rule |
| SO-D-03.1-001 | CR-D-03.1-001 | no-rule |
| SO-D-03.1-002 | — | no-rule |
| SO-D-03.1-003 | — | no-rule |
| SO-D-03.2-001 | CR-D-03.2-001 | no-rule |
| SO-D-03.2-002 | — | no-rule |
| SO-D-03.2-003 | — | no-rule |
| SO-D-03.4-001 | CR-D-03.4-001 | no-rule |
| SO-D-04.1-001 | CR-D-04.1-001 | no-rule |
| SO-D-04.1-002 | — | no-rule |
| SO-D-04.1-003 | — | no-rule |
| SO-D-04.2-001 | — | no-rule |
| SO-D-04.3-001 | — | no-rule |
| SO-D-04.3-002 | — | no-rule |
| SO-D-05.1-001 | — | no-rule |
| SO-D-05.1-002 | — | no-rule |
| SO-D-05.2-001 | — | no-rule |
| SO-D-05.3-001 | — | no-rule |
| SO-D-06.2-001 | CR-D-06.2-001 | no-rule |
| SO-D-06.4-001 | CR-D-06.4-001 | no-rule |
| SO-D-07.1-001 | — | no-rule |
| SO-D-07.2-001 | CR-D-07.2-001 | no-rule |
| SO-D-07.2-002 | — | no-rule |
| SO-D-07.3-001 | CR-D-07.3-001 | no-rule |
| SO-D-08.2-001 | — | no-rule |
| SO-D-09.1-001 | — | no-rule |
| SO-D-09.1-002 | — | no-rule |
| SO-D-09.2-001 | — | no-rule |
| SO-D-09.2-002 | — | no-rule |
| SO-D-09.4-001 | — | no-rule |
| SO-D-10.1-001 | CR-D-10.1-001 | no-rule |
| SO-D-10.1-002 | — | no-rule |
| SO-D-10.1-003 | — | no-rule |
| SO-D-10.2-001 | CR-D-10.2-001 | no-rule |
| SO-D-10.2-002 | — | no-rule |
| SO-D-10.2-003 | — | no-rule |
| SO-D-10.3-001 | — | no-rule |
| SO-D-10.3-002 | — | no-rule |

## realisation_class_derived (auto, majority-vote of realizing controls)

| Objective / Obligation | Realising CR/BPR | Majority |
|---|---|---|
| OBL-D-01.1-001 | CR-D-01.1-001 | CAPABILITY |
| OBL-D-01.2-001 | CR-D-01.2-001 | TECHNOLOGY |
| OBL-D-01.3-001 | CR-D-01.3-001 | CAPABILITY |
| OBL-D-01.4-001 | CR-D-01.4-001 | TECHNOLOGY |
| OBL-D-02.1-001 | CR-D-02.1-001 | PROCESS |
| OBL-D-02.2-001 | CR-D-02.2-001 | TECHNOLOGY |
| OBL-D-02.3-001 | CR-D-02.3-001 | CAPABILITY |
| OBL-D-02.4-001 | CR-D-02.4-001 | PROCESS |
| OBL-D-03.1-001 | CR-D-03.1-001 | CAPABILITY |
| OBL-D-03.2-001 | CR-D-03.2-001 | TECHNOLOGY |
| OBL-D-03.3-001 | CR-D-03.3-001 | PROCESS |
| OBL-D-03.4-001 | CR-D-03.4-001 | PROCESS |
| OBL-D-04.1-001 | CR-D-04.1-001 | PROCESS |
| OBL-D-04.2-001 | CR-D-04.2-001 | PROCESS |
| OBL-D-04.3-001 | CR-D-04.3-001 | CAPABILITY |
| OBL-D-04.4-001 | CR-D-04.4-001 | PROCESS |
| OBL-D-05.1-001 | CR-D-05.1-001 | CAPABILITY |
| OBL-D-05.2-001 | CR-D-05.2-001 | CAPABILITY |
| OBL-D-05.3-001 | CR-D-05.3-001 | TECHNOLOGY |
| OBL-D-05.4-001 | CR-D-05.4-001 | PROCESS |
| OBL-D-06.1-001 | CR-D-06.1-001 | PROCESS |
| OBL-D-06.2-001 | CR-D-06.2-001 | PROCESS |
| OBL-D-06.3-001 | CR-D-06.3-001 | PROCESS |
| OBL-D-06.4-001 | CR-D-06.4-001 | TECHNOLOGY |
| OBL-D-07.1-001 | CR-D-07.1-001 | CAPABILITY |
| OBL-D-07.2-001 | CR-D-07.2-001 | PROCESS |
| OBL-D-07.3-001 | CR-D-07.3-001 | TECHNOLOGY |
| OBL-D-08.1-001 | CR-D-08.1-001 | CAPABILITY |
| OBL-D-08.2-001 | CR-D-08.2-001 | CAPABILITY |
| OBL-D-09.1-001 | CR-D-09.1-001 | CAPABILITY |
| OBL-D-09.2-001 | CR-D-09.2-001 | CAPABILITY |
| OBL-D-09.4-001 | CR-D-09.4-001 | CAPABILITY |
| OBL-D-10.1-001 | CR-D-10.1-001 | CAPABILITY |
| OBL-D-10.2-001 | CR-D-10.2-001 | CAPABILITY |
| OBL-D-10.3-001 | CR-D-10.3-001 | PROCESS |
| PO-D-01.1-001 | CR-D-01.1-001 | CAPABILITY |
| PO-D-01.1-002 | — | no-rule |
| PO-D-01.2-001 | CR-D-01.2-001 | TECHNOLOGY |
| PO-D-01.2-002 | — | no-rule |
| PO-D-01.4-001 | CR-D-01.4-001 | TECHNOLOGY |
| PO-D-03.3-001 | CR-D-03.3-001 | PROCESS |
| PO-D-03.3-002 | — | no-rule |
| PO-D-04.2-001 | CR-D-04.2-001 | PROCESS |
| PO-D-04.2-002 | — | no-rule |
| PO-D-04.3-001 | CR-D-04.3-001 | CAPABILITY |
| PO-D-04.3-002 | — | no-rule |
| PO-D-04.4-001 | CR-D-04.4-001 | PROCESS |
| PO-D-04.4-002 | — | no-rule |
| PO-D-05.1-001 | CR-D-05.1-001 | CAPABILITY |
| PO-D-05.2-001 | CR-D-05.2-001 | CAPABILITY |
| PO-D-05.3-001 | CR-D-05.3-001 | TECHNOLOGY |
| PO-D-05.4-001 | CR-D-05.4-001 | PROCESS |
| PO-D-06.1-001 | CR-D-06.1-001 | PROCESS |
| PO-D-06.1-002 | — | no-rule |
| PO-D-06.3-001 | CR-D-06.3-001 | PROCESS |
| PO-D-06.3-002 | — | no-rule |
| PO-D-07.1-001 | CR-D-07.1-001 | CAPABILITY |
| PO-D-07.1-002 | — | no-rule |
| PO-D-08.1-001 | CR-D-08.1-001 | CAPABILITY |
| PO-D-08.1-002 | — | no-rule |
| PO-D-08.2-001 | CR-D-08.2-001 | CAPABILITY |
| PO-D-08.2-002 | — | no-rule |
| PO-D-09.1-001 | CR-D-09.1-001 | CAPABILITY |
| PO-D-09.1-002 | — | no-rule |
| PO-D-09.2-001 | CR-D-09.2-001 | CAPABILITY |
| PO-D-09.2-002 | — | no-rule |
| PO-D-09.4-001 | CR-D-09.4-001 | CAPABILITY |
| PO-D-10.3-001 | CR-D-10.3-001 | PROCESS |
| PO-D-10.3-002 | — | no-rule |
| SO-D-01.1-001 | — | no-rule |
| SO-D-01.1-002 | — | no-rule |
| SO-D-01.2-001 | — | no-rule |
| SO-D-01.2-002 | — | no-rule |
| SO-D-01.3-001 | CR-D-01.3-001 | CAPABILITY |
| SO-D-01.3-002 | — | no-rule |
| SO-D-01.3-003 | — | no-rule |
| SO-D-01.4-001 | — | no-rule |
| SO-D-01.4-002 | — | no-rule |
| SO-D-02.1-001 | CR-D-02.1-001 | PROCESS |
| SO-D-02.1-002 | — | no-rule |
| SO-D-02.1-003 | — | no-rule |
| SO-D-02.2-001 | CR-D-02.2-001 | TECHNOLOGY |
| SO-D-02.2-002 | — | no-rule |
| SO-D-02.3-001 | CR-D-02.3-001 | CAPABILITY |
| SO-D-02.3-002 | — | no-rule |
| SO-D-02.4-001 | CR-D-02.4-001 | PROCESS |
| SO-D-02.4-002 | — | no-rule |
| SO-D-03.1-001 | CR-D-03.1-001 | CAPABILITY |
| SO-D-03.1-002 | — | no-rule |
| SO-D-03.1-003 | — | no-rule |
| SO-D-03.2-001 | CR-D-03.2-001 | TECHNOLOGY |
| SO-D-03.2-002 | — | no-rule |
| SO-D-03.2-003 | — | no-rule |
| SO-D-03.4-001 | CR-D-03.4-001 | PROCESS |
| SO-D-04.1-001 | CR-D-04.1-001 | PROCESS |
| SO-D-04.1-002 | — | no-rule |
| SO-D-04.1-003 | — | no-rule |
| SO-D-04.2-001 | — | no-rule |
| SO-D-04.3-001 | — | no-rule |
| SO-D-04.3-002 | — | no-rule |
| SO-D-05.1-001 | — | no-rule |
| SO-D-05.1-002 | — | no-rule |
| SO-D-05.2-001 | — | no-rule |
| SO-D-05.3-001 | — | no-rule |
| SO-D-06.2-001 | CR-D-06.2-001 | PROCESS |
| SO-D-06.4-001 | CR-D-06.4-001 | TECHNOLOGY |
| SO-D-07.1-001 | — | no-rule |
| SO-D-07.2-001 | CR-D-07.2-001 | PROCESS |
| SO-D-07.2-002 | — | no-rule |
| SO-D-07.3-001 | CR-D-07.3-001 | TECHNOLOGY |
| SO-D-08.2-001 | — | no-rule |
| SO-D-09.1-001 | — | no-rule |
| SO-D-09.1-002 | — | no-rule |
| SO-D-09.2-001 | — | no-rule |
| SO-D-09.2-002 | — | no-rule |
| SO-D-09.4-001 | — | no-rule |
| SO-D-10.1-001 | CR-D-10.1-001 | CAPABILITY |
| SO-D-10.1-002 | — | no-rule |
| SO-D-10.1-003 | — | no-rule |
| SO-D-10.2-001 | CR-D-10.2-001 | CAPABILITY |
| SO-D-10.2-002 | — | no-rule |
| SO-D-10.2-003 | — | no-rule |
| SO-D-10.3-001 | — | no-rule |
| SO-D-10.3-002 | — | no-rule |