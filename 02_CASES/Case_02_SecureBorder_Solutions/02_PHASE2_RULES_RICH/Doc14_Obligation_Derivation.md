---
document_id: AEGIS-P2-08
title: Obligation Derivation Report
phase: 2
version: 5.1
created: 2026-04-03
updated: 2026-08-13
author: Compliance Lead
status: MIGRATED
inputs: [07_Structured_Compliance_Matrix.md, 06_Clause_Mapping_Matrix.xlsx]
outputs: [09_Strategic_Tensions_Report.md, 10_Privacy_Security_Goals.md]
traceability: AEGIS Class Model → RegulatoryObligation, AbstractNFR classes
related_documents: 00_Taxonomy_Reference.md, 03_Design_Decisions_Log.md
---

# Obligation Derivation Report

## 1. DOCUMENT PURPOSE

This document consolidates the obligation derivation process (Step B1+B2+B3), transforming regulatory clauses into abstract non-functional requirements (RegulatoryObligations) with traceability and Normative Intensity propagation.

**Alignment with Class Model:**
- `RegulatoryObligation` (formerly AbstractNFR) - Derived obligations from clauses
- `RegulatoryClause` - Source clauses for each obligation
- `DomainCoverageEntry` - Sub-domain mapping for obligations

**Phase 2 Step:** B (Obligation Derivation)

**Gate Criteria:** All applicable clauses mapped to obligations with NI propagation

---

## 2. OBLIGATION DERIVATION METADATA

| Attribute | Value |
|-----------|-------|
| derivationId | DERIV-SECUREBORDER-2026-001 |
| derivationDate | 2026-04-03 |
| basedOnComplianceMatrix | SCM-SECUREBORDER-2026-001 |
| derivedBy | Compliance Lead |
| phase2Step | B1+B2+B3 |
| companyContextId | CC-SECUREBORDER-2026-001 |
| applicableRegulations | GDPR, CRA, NIS 2, AI_Act |
| totalSourceClauses | 111 (GDPR 28 + CRA 26 + NIS 2 29 + AI_Act 28) |
| totalObligations | 38 (one per covered sub-domain) |

---

## 3. DERIVATION METHODOLOGY

### 3.1 Derivation Rules

| Rule ID | Rule Description | Application |
|---------|------------------|-------------|
| DR-001 | One-to-Many: One clause may derive multiple obligations | When clause spans multiple sub-domains |
| DR-002 | NI Propagation: Max NI from source clauses | obligationNI = MAX(clauseNI) |
| DR-003 | Traceability: Each obligation links to source clause(s) | Mandatory bidirectional link |
| DR-004 | Sub-Domain Assignment: Each obligation targets one sub-domain | Primary domain classification |
| DR-005 | Actor Separation: Do not merge clauses with different obligatedParty | GDPR (CONTROLLER) vs CRA (MANUFACTURER) vs NIS 2 (ESSENTIAL_ENTITY) vs AI_Act (PROVIDER) kept separate where actors differ |
| DR-006 | Sole Authority Flag: Mark obligations from sub-domains with single-regulation coverage | OBL-D-05.4-001 (GDPR sole), OBL-D-06.2-001 (CRA sole), OBL-D-06.4-001 (NIS 2 sole), OBL-D-07.3-001 (NIS 2 sole), OBL-D-07.4-001 (NIS 2 sole), OBL-D-08.3-001 (NIS 2 sole), OBL-D-09.3-001 (NIS 2 sole) |
| DR-007 | Activation Condition Flag: Mark obligations that derive from clauses with different trigger conditions | Obligations combining clauses with distinct triggers (e.g., GDPR personal data breach + CRA exploited vuln + NIS 2 significant incident + AI_Act serious incident) are flagged as CONTEXTUAL |
| DR-008 | Activation Nature: Classify obligation as structural or contextual | If all source clauses share the same trigger context → STRUCTURAL (always active). If source clauses have distinct triggers that may or may not overlap → CONTEXTUAL (activated by compound event) |

### 3.2 Obligation ID Structure

```
OBL-[Sub-Domain ID]-[Sequence Number]
Example: OBL-D-01.1-001
```

### 3.3 Multi-Regulation Obligation Strategy

For SecureBorder Solutions, 4 regulations apply with different obligated parties:

| Obligated Party | Regulations | Strategy |
|-----------------|-------------|----------|
| CONTROLLER | GDPR | Native obligations for data processing |
| MANUFACTURER | CRA | Native obligations for product security |
| ESSENTIAL_ENTITY_SUPPLIER | NIS 2 | Native obligations for operational security |
| PROVIDER | AI_Act | Native obligations for AI system governance |

**Merging Rule:** Clauses from different regulations targeting the same sub-domain are merged into a single obligation when the obligated parties are compatible (all apply to SecureBorder as the same organization). The obligation inherits the highest NI and all source clauses.

---

## 4. REGULATORY OBLIGATIONS CATALOG

### D-01: Data Protection & Encryption Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----- | ---------------- | ---------------- | --- | --- | --- | --- | --- | --- |
| OBL-D-01.1-001 | Encrypt all personal, biometric, and sensitive data at rest using strong cryptographic protocols (strong symmetric encryption or equivalent) with strong cryptographic modules cryptographic modules | GDPR-C04, GDPR-C14, CRA-C07, NIS2-C18, AI-C17 | D-01.1 | 3.000 | CONTINUOUS | CONTROLLER + MANUFACTURER + ESSENTIAL_ENTITY + PROVIDER | CT.DM-P1, PR.DS-P1 | MANAGE-2.1, MAP-2.1 | CT.DM-P1, PR.DS-P1 | MANAGE-2.1, MAP-2.1 | CT.DM-P1, PR.DS-P1 | MANAGE-2.1, MAP-2.1 |
| OBL-D-01.2-001 | All personal and product data crossing network boundaries must be protected by confidentiality mechanisms appropriate to channel classification for biometric data, passport data, and audit logs | GDPR-C15, CRA-C08, NIS2-C18 | D-01.2 | 3.000 | CONTINUOUS | CONTROLLER + MANUFACTURER + ESSENTIAL_ENTITY | CT.DM-P1 | MAP-2.1 | CT.DM-P1 | MAP-2.1 | CT.DM-P1 | MAP-2.1 |
| OBL-D-01.3-001 | Implement secure cryptographic key management with integrity verification for biometric template encryption and update signing | CRA-C15, NIS2-C18, AI-C17 | D-01.3 | 3.000 | CONTINUOUS | MANUFACTURER + ESSENTIAL_ENTITY + PROVIDER | PR.DS-P3 | — | PR.DS-P3 | — | PR.DS-P3 | — |
| OBL-D-01.4-001 | Protect data against unauthorised manipulation and accidental loss using cryptographic checksums and integrity verification | GDPR-C05, CRA-C09, AI-C18 | D-01.4 | 3.000 | CONTINUOUS | CONTROLLER + MANUFACTURER + PROVIDER | CT.DM-P3 | MEASURE-2.5 | CT.DM-P3 | MEASURE-2.5 | CT.DM-P3 | MEASURE-2.5 |

**D-01 Summary:** 4 obligations | Avg NI: 3.000 | All CONTINUOUS | All 4 regulations

---

### D-02: Vulnerability Management Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----- | ---------------- | ---------------- | --- | --- | --- | --- | --- | --- |
| OBL-D-02.1-001 | Identify, track, and remediate vulnerabilities through continuous scanning, SBOM analysis, and pre-release assessment ensuring no known exploitable vulnerabilities at delivery | CRA-C01, CRA-C17, NIS2-C12, AI-C03, AI-C16 | D-02.1 | 3.000 | CONTINUOUS | MANUFACTURER + ESSENTIAL_ENTITY + PROVIDER | — | — | — | — | — | — |
| OBL-D-02.2-001 | Implement prompt patch management and security update capability including automatic and signed OTA updates without delay | CRA-C04, CRA-C19, NIS2-C12 | D-02.2 | 3.000 | CONTINUOUS + TRIGGERED | MANUFACTURER + ESSENTIAL_ENTITY | — | — | — | — | — | — |
| OBL-D-02.3-001 | Publish and maintain coordinated vulnerability disclosure policy (security.txt) with structured reporting to ENISA and national CSIRTs | CRA-C21, CRA-C26, NIS2-C12 | D-02.3 | 3.000 | CONTINUOUS + TRIGGERED | MANUFACTURER + ESSENTIAL_ENTITY | — | — | — | — | — | — |
| OBL-D-02.4-001 | Conduct threat-led penetration testing and bias/error testing for AI training data and accuracy performance | NIS2-C13, AI-C04 | D-02.4 | 3.000 | PERIODIC | ESSENTIAL_ENTITY + PROVIDER | — | — | — | — | — | — |

**D-02 Summary:** 4 obligations | Avg NI: 3.000 | CONTINUOUS + TRIGGERED + PERIODIC

---

### D-03: Access Control Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----- | ---------------- | ---------------- | --- | --- | --- | --- | --- | --- |
| OBL-D-03.1-001 | Implement identity lifecycle management with authentication, access control policies, and competent human oversight for AI systems | CRA-C05, NIS2-C16, NIS2-C19, AI-C15 | D-03.1 | 3.000 | CONTINUOUS | MANUFACTURER + ESSENTIAL_ENTITY + PROVIDER | — | MAP-2.1 | — | MAP-2.1 | — | MAP-2.1 |
| OBL-D-03.2-001 | Implement multi-factor authentication for all system access points including border control operator interfaces | CRA-C06, NIS2-C17 | D-03.2 | 3.000 | CONTINUOUS | MANUFACTURER + ESSENTIAL_ENTITY | — | MEASURE-2.5 | — | MEASURE-2.5 | — | MEASURE-2.5 |
| OBL-D-03.3-001 | Enforce authorization controls and least privilege access for data processing, system administration, and AI oversight functions | GDPR-C10, GDPR-C17, NIS2-C20 | D-03.3 | 3.000 | CONTINUOUS | CONTROLLER + ESSENTIAL_ENTITY | — | — | — | — | — | — |
| OBL-D-03.4-001 | Deliver product with secure default configuration: disable unused ports, no default passwords, most secure default state | CRA-C03 | D-03.4 | 3.000 | ONE_TIME | MANUFACTURER | — | — | — | — | — | — |

**D-03 Summary:** 4 obligations | Avg NI: 3.000 | CONTINUOUS + ONE_TIME | D-03.4 is CRA Sole Authority

---

### D-04: Incident Response Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | Activation Nature | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----- | ---------------- | ---------------- | ------------------- | --- | --- | --- | --- | --- | --- |
| OBL-D-04.1-001 | Implement incident detection and triage systems with impact reduction design, fail-safe mechanisms, and 24/7 SOC monitoring | CRA-C13, NIS2-C28, AI-C25 | D-04.1 | 3.000 | CONTINUOUS | MANUFACTURER + ESSENTIAL_ENTITY + PROVIDER | STRUCTURAL (always active) | — | — | — | — | — | — |
| OBL-D-04.2-001 | Implement containment, mitigation, and business continuity measures including DoS resilience, backup systems, and disaster recovery | GDPR-C18, CRA-C11, NIS2-C05 | D-04.2 | 3.000 | CONTINUOUS + TRIGGERED | CONTROLLER + MANUFACTURER + ESSENTIAL_ENTITY | STRUCTURAL (always active) | — | — | — | — | — | — |
| OBL-D-04.3-001 | Notify regulatory authorities of significant incidents and vulnerabilities: 24h early warning to CSIRT (NIS 2/CRA), 72h breach notification to SA (GDPR), market surveillance cooperation (AI_Act), with final report within 1 month | GDPR-C21, GDPR-C23, CRA-C25, NIS2-C25, NIS2-C26, NIS2-C27, AI-C26, AI-C29 | D-04.3 | 3.000 | TRIGGERED | CONTROLLER + MANUFACTURER + ESSENTIAL_ENTITY + PROVIDER | **CONTEXTUAL** — GDPR triggers on personal data breach; CRA triggers on exploited vulnerability; NIS 2 triggers on significant incident; AI_Act triggers on serious AI incident. All activate simultaneously only in compound event (EVT-001/EVT-002). See T-001. | — | — | — | — | — | — |
| OBL-D-04.4-001 | Restore data availability and recover systems after incidents with disaster recovery plans and backup restoration | GDPR-C16, NIS2-C06 | D-04.4 | 3.000 | TRIGGERED | CONTROLLER + ESSENTIAL_ENTITY | STRUCTURAL (always active) | — | — | — | — | — | — |

**D-04 Summary:** 4 obligations | Avg NI: 3.000 | **1 contextual (OBL-D-04.3-001)** | **Tension T-001:** timing conflict (72h vs 24h vs 15d) — only active when compound event occurs

**Nuance — Processor Breach Notification (GDPR Art. 33(2)):** As a processor for government biometric data, SecureBorder must notify the government authority (controller) of personal data breaches "without undue delay" — a distinct obligation from the controller's 72h notification to the supervisory authority (Art. 33(1)). The processor→controller clock has no fixed numeric deadline. This should be contractually defined with the government authority (e.g., within 4-8 hours). The existing OBL-D-04.3-001 captures the 72h/24h/1-month regulatory notifications but does not explicitly capture the processor→controller "without undue delay" obligation — a separate internal SLA should be established for this.

---

### D-05: Data Lifecycle Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | Activation Nature | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----- | ---------------- | ---------------- | ------------------- | --- | --- | --- | --- | --- | --- |
| OBL-D-05.1-001 | Minimize data collection to adequate, relevant, and necessary fields only; ensure training data relevance and representativeness for AI systems | GDPR-C01, CRA-C10, AI-C05, AI-C06 | D-05.1 | 3.000 | CONTINUOUS + ONE_TIME | CONTROLLER + MANUFACTURER + PROVIDER | STRUCTURAL (always active) | CT.PO-P1, ID.IM-P1 | MAP-1.5, MAP-3.1 | CT.PO-P1, ID.IM-P1 | MAP-1.5, MAP-3.1 | CT.PO-P1, ID.IM-P1 | MAP-1.5, MAP-3.1 |
| OBL-D-05.2-001 | Retain personal data only for defined purpose duration; maintain training data retention for AI lifecycle; comply with government-mandated retention periods | GDPR-C02, GDPR-C03, AI-C07 | D-05.2 | 3.000 | CONTINUOUS | CONTROLLER + PROVIDER | STRUCTURAL (always active) | CT.DM-P2, GV.RM-P1 | MANAGE-2.4 | CT.DM-P2, GV.RM-P1 | MANAGE-2.4 | CT.DM-P2, GV.RM-P1 | MANAGE-2.4 |
| OBL-D-05.3-001 | Enable right to erasure and secure data removal on user request with complete deletion capability | GDPR-C06, CRA-C16 | D-05.3 | 3.000 | TRIGGERED | CONTROLLER + MANUFACTURER | **CONTEXTUAL** — GDPR erasure trigger (data subject request) vs AI_Act log retention obligation. Conflict when erasure request meets AI logging requirement. See T-002. | CT.DM-P3 | — | CT.DM-P3 | — | CT.DM-P3 | — |
| OBL-D-05.4-001 | Provide data portability in machine-readable format on request within defined timeframe | GDPR-C07 | D-05.4 | 3.000 | TRIGGERED | CONTROLLER | STRUCTURAL (always active) | CT.PO-P2 | MAP-1.6 | CT.PO-P2 | MAP-1.6 | CT.PO-P2 | MAP-1.6 |

**D-05 Summary:** 4 obligations | Avg NI: 3.000 | **1 contextual (OBL-D-05.3-001)** | D-05.4 is GDPR Sole Authority

---

### D-06: Supply Chain Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----- | ---------------- | ---------------- | --- | --- | --- | --- | --- | --- |
| OBL-D-06.1-001 | Assess and manage vendor security risks through continuous monitoring, supplier questionnaires, and vendor risk management programs | GDPR-C11, NIS2-C08, NIS2-C23 | D-06.1 | 3.000 | CONTINUOUS | CONTROLLER + ESSENTIAL_ENTITY | — | — | — | — | — | — |
| OBL-D-06.2-001 | Generate, maintain, and update Software Bill of Materials (SBOM) documenting all components, dependencies, and known vulnerabilities | CRA-C18 | D-06.2 | 3.000 | CONTINUOUS | MANUFACTURER | — | — | — | — | — | — |
| OBL-D-06.3-001 | Include mandatory security clauses in all supplier and processor contracts (DPA, security requirements, incident notification) | GDPR-C12, NIS2-C09 | D-06.3 | 3.000 | ONE_TIME + CONTINUOUS | CONTROLLER + ESSENTIAL_ENTITY | — | — | — | — | — | — |
| OBL-D-06.4-001 | Define and enforce third-party boundary management with physical isolation per airport/country instance | NIS2-C24 | D-06.4 | 3.000 | CONTINUOUS | ESSENTIAL_ENTITY | — | — | — | — | — | — |

**D-06 Summary:** 4 obligations | Avg NI: 3.000 | CONTINUOUS + ONE_TIME | D-06.2 is CRA Sole Authority, D-06.4 is NIS 2 Sole Authority

**Nuance — AI_Act Downstream Provider (Art. 25):** If a government authority or third party substantially modifies GuardianGate's AI system (e.g., repurposing it for a different border control function, adding new biometric modalities, or rebranding it), that entity may become the "provider" with full Art. 16 obligations. SecureBorder should include written agreements (Art. 25(4)) specifying information, capabilities, and technical access needed for compliance with any downstream entities. This creates a downstream obligation beyond the standard vendor risk management in OBL-D-06.1-001 and OBL-D-06.3-001 — specifically for AI system value chain responsibilities.

---

### D-07: Secure Development Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----- | ---------------- | ---------------- | --- | --- | --- | --- | --- | --- |
| OBL-D-07.1-001 | Integrate privacy-by-design, secure-by-default, and manufacturer obligation principles into product design, development, and production per Annex I requirements | GDPR-C09, CRA-C02, CRA-C22 | D-07.1 | 3.000 | ONE_TIME + CONTINUOUS | CONTROLLER + MANUFACTURER | — | GOVERN-2.2, GOVERN-3.1 | — | GOVERN-2.2, GOVERN-3.1 | — | GOVERN-2.2, GOVERN-3.1 |
| OBL-D-07.2-001 | Implement secure coding practices including code review, static analysis, and secure development lifecycle | CRA-C02, NIS2-C11 | D-07.2 | 3.000 | CONTINUOUS | MANUFACTURER + ESSENTIAL_ENTITY | — | MEASURE-2.5 | — | MEASURE-2.5 | — | MEASURE-2.5 |
| OBL-D-07.3-001 | Secure CI/CD pipeline with protected development and deployment pipelines, signed builds, and integrity verification | NIS2-C11 | D-07.3 | 3.000 | CONTINUOUS | ESSENTIAL_ENTITY | — | — | — | — | — | — |
| OBL-D-07.4-001 | Implement formal change management procedures for all system modifications with documented approval and rollback capability | NIS2-C10 | D-07.4 | 3.000 | CONTINUOUS | ESSENTIAL_ENTITY | — | — | — | — | — | — |

**D-07 Summary:** 4 obligations | Avg NI: 3.000 | ONE_TIME + CONTINUOUS | D-07.3 and D-07.4 are NIS 2 Sole Authority

**Nuance — CRA Support Period (Art. 13(8)):** The CRA requires a minimum **5-year support period** from product placement for GuardianGate eGate kiosks. Given the critical infrastructure nature (15-20 year deployment lifespans), this translates to a continuous obligation to provide security patches and vulnerability fixes for at least 5 years per deployed unit. This is captured under existing CRA clauses (CRA-C04, CRA-C19) but the 5-year quantitative threshold is a concrete compliance milestone.

**Nuance — CRA Security Update Retention (Art. 13(9)):** Security updates must remain available for a minimum of **10 years** or the support period, whichever is longer. For critical infrastructure with multi-decade deployments, this means old GuardianGate software versions' patches must be archived and accessible for at least a decade.

**Nuance — CRA Certification Scheme Absence (Art. 8(1)):** Although GuardianGate is classified as Critical Class, no European cybersecurity certification scheme exists yet for critical products. Until the Commission adopts the relevant delegated acts, Critical Class products default to **Art. 32(3)** conformity assessment (full quality assurance + EU-type examination by a notified body), not certification. OBL-D-07.1-001's conformity assessment obligation should be planned as Art. 32(3) assessment, with a potential transition to certification when the scheme becomes available.

**Nuance — CRA Exclusions Analysis (Art. 24):** GuardianGate eGate kiosks are commercial civilian border control systems, not military/defence products. They do not fall under any excluded sectoral regulation (medical devices, motor vehicles, marine equipment, aviation). No CRA exclusions apply. This confirms that all CRA obligations in this derivation are valid.

---

### D-08: Human Factors Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----- | ---------------- | ---------------- | --- | --- | --- | --- | --- | --- |
| OBL-D-08.1-001 | Provide general security awareness training to all staff involved in processing and system operations | GDPR-C27, NIS2-C14 | D-08.1 | 3.000 | PERIODIC | CONTROLLER + ESSENTIAL_ENTITY | — | MEASURE-2.5 | — | MEASURE-2.5 | — | MEASURE-2.5 |
| OBL-D-08.2-001 | Provide role-specific security competence training for developers, operators, and AI human oversight personnel ensuring appropriate competence levels | GDPR-C28, NIS2-C15, AI-C14, AI-C24 | D-08.2 | 3.000 | PERIODIC + CONTINUOUS | CONTROLLER + ESSENTIAL_ENTITY + PROVIDER | — | — | — | — | — | — |
| OBL-D-08.3-001 | Ensure management board receives cybersecurity-specific training with awareness of NIS 2 management liability obligations | NIS2-C02 | D-08.3 | 3.000 | PERIODIC | ESSENTIAL_ENTITY | — | — | — | — | — | — |

**D-08 Summary:** 3 obligations | Avg NI: 3.000 | PERIODIC + CONTINUOUS | D-08.3 is NIS 2 Sole Authority

---

### D-09: Governance & Documentation Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----- | ---------------- | ---------------- | --- | --- | --- | --- | --- | --- |
| OBL-D-09.1-001 | Establish, document, and maintain comprehensive information security policies, technical documentation, transparency information, conformity assessment records, and quality management system | GDPR-C08, GDPR-C25, GDPR-C26, CRA-C24, NIS2-C01, AI-C08, AI-C12, AI-C13, AI-C20, AI-C23 | D-09.1 | 3.000 | CONTINUOUS + ONE_TIME | CONTROLLER + MANUFACTURER + ESSENTIAL_ENTITY + PROVIDER | ID.RA-P1 | GOVERN-4.1, GOVERN-5.2, MAP-3.1 | ID.RA-P1 | GOVERN-4.1, GOVERN-5.2, MAP-3.1 | ID.RA-P1 | GOVERN-4.1, GOVERN-5.2, MAP-3.1 |
| OBL-D-09.2-001 | Conduct comprehensive impact and risk assessments including DPIA, FRIA, cybersecurity risk assessment, AI-specific risk assessments, and incident reporting | GDPR-C20, GDPR-C24, CRA-C23, NIS2-C04, AI-C01, AI-C02, AI-C22 | D-09.2 | 3.000 | ONE_TIME + PERIODIC + CONTINUOUS | CONTROLLER + MANUFACTURER + ESSENTIAL_ENTITY + PROVIDER | — | MEASURE-2.4 | — | MEASURE-2.4 | — | MEASURE-2.4 |
| OBL-D-09.3-001 | Maintain comprehensive asset inventories covering all hardware, software, data assets, and AI system components | NIS2-C07 | D-09.3 | 3.000 | CONTINUOUS | ESSENTIAL_ENTITY | — | — | — | — | — | — |
| OBL-D-09.4-001 | Maintain records of processing activities (RoPA), AI traceability records, and breach documentation for all personal data and AI system processing | GDPR-C13, GDPR-C22, AI-C11 | D-09.4 | 3.000 | CONTINUOUS + TRIGGERED | CONTROLLER + PROVIDER | — | MAP-1.5 | — | MAP-1.5 | — | MAP-1.5 |

**D-09 Summary:** 4 obligations | Avg NI: 3.000 | CONTINUOUS + ONE_TIME + PERIODIC + TRIGGERED | D-09.3 is NIS 2 Sole Authority

**Nuance — DPO Mandatory (GDPR Art. 37(1)(c)):** SecureBorder processes biometric facial templates (Art. 9 special category data) on behalf of government authorities at large scale. Art. 37(1)(c) requires **both the controller AND the processor** to designate a DPO when core activities consist of large-scale processing of Art. 9 data. SecureBorder as processor has a **direct statutory DPO obligation** — not merely a contractual one via the government DPA. The OBL-D-09.1-001 references GDPR-C26 (DPO designation) but should explicitly note that this is a mandatory Art. 37(1)(c) obligation for the processor role, not discretionary.

**Nuance — DPIA Always Required (GDPR Art. 35(3)(b)):** Large-scale processing of Art. 9 biometric data is an **automatic DPIA trigger** — no discretionary risk assessment is needed to determine whether a DPIA is required. The DPIA is mandatory by statute. OBL-D-09.2-001 references GDPR-C24 (DPIA mandatory) but should explicitly cite Art. 35(3)(b) as the automatic trigger, not a risk-based determination.

**Nuance — AI_Act Prohibited Practices (Art. 5):** OBL-D-09.1-001 references AI-C08 (transparency information) but the obligation derivation should explicitly confirm that GuardianGate's AI system does not fall under any of the 8 prohibited AI practices in Art. 5 (subliminal manipulation, exploitation of vulnerabilities, social scoring, predictive policing, untargeted facial scraping, emotion inference in workplace/education, biometric categorization inferring sensitive attributes, real-time remote biometric ID). GuardianGate performs one-to-one verification at a controlled kiosk — this is high-risk classification (Annex III), not a prohibited practice. This is a negative confirmation that should be documented in the derivation.

---

### D-10: Monitoring & Audit Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | Activation Nature | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors | PF Anchors | AI RMF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----- | ---------------- | ---------------- | ------------------- | --- | --- | --- | --- | --- | --- |
| OBL-D-10.1-001 | Implement continuous security monitoring systems with attack surface minimization, AI monitoring, and fallback plans | CRA-C12, NIS2-C21, NIS2-C29, AI-C25 | D-10.1 | 3.000 | CONTINUOUS | MANUFACTURER + ESSENTIAL_ENTITY + PROVIDER | STRUCTURAL (always active) | — | MANAGE-4.1 | — | MANAGE-4.1 | — | MANAGE-4.1 |
| OBL-D-10.2-001 | Implement comprehensive audit logging and traceability for all security-relevant events, AI activities, and system operations with minimum 6-month retention | CRA-C14, NIS2-C22, AI-C09, AI-C10 | D-10.2 | 3.000 | CONTINUOUS | MANUFACTURER + ESSENTIAL_ENTITY + PROVIDER | **CONTEXTUAL** — AI_Act requires minimum 6-month log retention (AI-C09, AI-C10); GDPR erasure (GDPR-C06) may require earlier deletion of personal data in logs. See T-002. | — | — | — | — | — | — |
| OBL-D-10.3-001 | Conduct regular compliance testing, security assessments, post-market monitoring, and periodic AI system evaluations | GDPR-C19, CRA-C20, NIS2-C13, AI-C21, AI-C27 | D-10.3 | 3.000 | PERIODIC + CONTINUOUS | CONTROLLER + MANUFACTURER + ESSENTIAL_ENTITY + PROVIDER | STRUCTURAL (always active) | — | — | — | — | — | — |

**D-10 Summary:** 3 obligations | Avg NI: 3.000 | **1 contextual (OBL-D-10.2-001)** | **Tension T-002:** AI_Act 6-month retention vs GDPR erasure

---

## 5. OBLIGATION SUMMARY DASHBOARD

### 5.1 By Domain

| Domain ID | Domain Name | Obligations | Avg NI | Types | Sole Authority |
|-----------|-------------|-------------|--------|-------|----------------|
| D-01 | Data Protection & Encryption | 4 | 3.000 | CONTINUOUS | No |
| D-02 | Vulnerability Management | 4 | 3.000 | CONTINUOUS + TRIGGERED + PERIODIC | No |
| D-03 | Access Control | 4 | 3.000 | CONTINUOUS + ONE_TIME | D-03.4 (CRA) |
| D-04 | Incident Response | 4 | 3.000 | CONTINUOUS + TRIGGERED | No |
| D-05 | Data Lifecycle | 4 | 3.000 | CONTINUOUS + TRIGGERED | D-05.4 (GDPR) |
| D-06 | Supply Chain | 4 | 3.000 | CONTINUOUS + ONE_TIME | D-06.2 (CRA), D-06.4 (NIS 2) |
| D-07 | Secure Development | 4 | 3.000 | ONE_TIME + CONTINUOUS | D-07.3 (NIS 2), D-07.4 (NIS 2) |
| D-08 | Human Factors | 3 | 3.000 | PERIODIC + CONTINUOUS | D-08.3 (NIS 2) |
| D-09 | Governance & Documentation | 4 | 3.000 | CONTINUOUS + ONE_TIME + PERIODIC + TRIGGERED | D-09.3 (NIS 2) |
| D-10 | Monitoring & Audit | 3 | 3.000 | CONTINUOUS + PERIODIC | No |
| **TOTAL** | **All Domains** | **38** | **3.000** | **Mixed** | **8 sub-domains** |

### 5.2 By Obligation Type

| Type | Count | Percentage |
|------|-------|------------|
| CONTINUOUS | 28 | 73.7% |
| TRIGGERED | 6 | 15.8% |
| ONE_TIME | 6 | 15.8% |
| PERIODIC | 6 | 15.8% |

*Note: Some obligations have multiple types*

### 5.3 By Obligated Party

| Party | Obligations | Regulations |
|-------|-------------|-------------|
| CONTROLLER | 15 | GDPR |
| MANUFACTURER | 16 | CRA |
| ESSENTIAL_ENTITY | 22 | NIS 2 |
| PROVIDER | 14 | AI_Act |

*Note: Most obligations have multiple obligated parties*

### 5.4 Sole Authority Obligations

| Obligation ID | Sub-Domain | Sole Authority Regulation | Risk if Regulation Excluded |
|---------------|------------|---------------------------|----------------------------|
| OBL-D-03.4-001 | D-03.4 Secure System Defaults | CRA | Zero mandate |
| OBL-D-05.4-001 | D-05.4 Data Portability | GDPR | Zero mandate |
| OBL-D-06.2-001 | D-06.2 SBOM | CRA | Zero mandate |
| OBL-D-06.4-001 | D-06.4 Third-Party Boundary | NIS 2 | Zero mandate |
| OBL-D-07.3-001 | D-07.3 CI/CD Pipeline Security | NIS 2 | Zero mandate |
| OBL-D-07.4-001 | D-07.4 Change Management | NIS 2 | Zero mandate |
| OBL-D-08.3-001 | D-08.3 Management Board Training | NIS 2 | Zero mandate |
| OBL-D-09.3-001 | D-09.3 Asset Inventories | NIS 2 | Zero mandate |

**All 8 sole authority obligations are covered** because all 4 regulations (GDPR, CRA, NIS 2, AI_Act) are applicable to SecureBorder Solutions.

---

## 6. NORMATIVE INTENSITY ANALYSIS

### 6.1 NI Distribution

| NI Value | Obligations | Percentage |
|----------|-------------|------------|
| 3.000 | 38 | 100.0% |
| 2.000-2.999 | 0 | 0.0% |
| < 2.000 | 0 | 0.0% |

**Mean NI:** 3.000 (all obligations are mandatory)

**Insight:** SecureBorder has the highest possible NI profile because all 4 applicable regulations have predominantly Weight 3 clauses (88%+ mandatory). This means all obligations are unconditional "shall" requirements.

### 6.2 NI by Regulation Contribution

| Regulation | Clauses Contributed | Obligations Impacted | Mean Clause NI |
|------------|--------------------|---------------------|----------------|
| GDPR | 28 | 15 | 2.643 |
| CRA | 26 | 16 | 2.923 |
| NIS 2 | 29 | 22 | 3.000 |
| AI_Act | 28 | 14 | 3.000 |

---

## 7. TRACEABILITY MATRIX

### 7.1 Clause → Obligation Mapping

| Source Clause | Target Obligation | Sub-Domain | NI Preserved? |
|---------------|-------------------|------------|---------------|
| GDPR-C01, CRA-C10, AI-C05, AI-C06 | OBL-D-05.1-001 | D-05.1 | ✅ MAX(3,3,3,3) = 3.000 |
| GDPR-C02, GDPR-C03, AI-C07 | OBL-D-05.2-001 | D-05.2 | ✅ MAX(3,3,3) = 3.000 |
| GDPR-C04, GDPR-C14, CRA-C07, NIS2-C18, AI-C17 | OBL-D-01.1-001 | D-01.1 | ✅ MAX(2,2,3,3,3) = 3.000 |
| GDPR-C05, CRA-C09, AI-C18 | OBL-D-01.4-001 | D-01.4 | ✅ MAX(2,3,3) = 3.000 |
| GDPR-C06, CRA-C16 | OBL-D-05.3-001 | D-05.3 | ✅ MAX(3,3) = 3.000 |
| GDPR-C07 | OBL-D-05.4-001 | D-05.4 | ✅ 3.000 |
| GDPR-C08, GDPR-C25, GDPR-C26, CRA-C24, NIS2-C01, AI-C08, AI-C12, AI-C13, AI-C20, AI-C23 | OBL-D-09.1-001 | D-09.1 | ✅ MAX(2,3,2,3,3,3,3,3,3,3) = 3.000 |
| GDPR-C09, CRA-C02, CRA-C22 | OBL-D-07.1-001 | D-07.1 | ✅ MAX(2,3,3) = 3.000 |
| GDPR-C10, GDPR-C17, NIS2-C20 | OBL-D-03.3-001 | D-03.3 | ✅ MAX(3,3,3) = 3.000 |
| GDPR-C11, NIS2-C08, NIS2-C23 | OBL-D-06.1-001 | D-06.1 | ✅ MAX(3,3,3) = 3.000 |
| GDPR-C12, NIS2-C09 | OBL-D-06.3-001 | D-06.3 | ✅ MAX(3,3) = 3.000 |
| GDPR-C13, GDPR-C22, AI-C11 | OBL-D-09.4-001 | D-09.4 | ✅ MAX(3,3,3) = 3.000 |
| GDPR-C15, CRA-C08, NIS2-C18 | OBL-D-01.2-001 | D-01.2 | ✅ MAX(2,3,3) = 3.000 |
| GDPR-C16, NIS2-C06 | OBL-D-04.4-001 | D-04.4 | ✅ MAX(2,3) = 3.000 |
| GDPR-C18, CRA-C11, NIS2-C05 | OBL-D-04.2-001 | D-04.2 | ✅ MAX(2,3,3) = 3.000 |
| GDPR-C19, CRA-C20, NIS2-C13, AI-C21, AI-C27 | OBL-D-10.3-001 | D-10.3 | ✅ MAX(3,2,3,3,3) = 3.000 |
| GDPR-C20, GDPR-C24, CRA-C23, NIS2-C04, AI-C01, AI-C02, AI-C22 | OBL-D-09.2-001 | D-09.2 | ✅ MAX(2,3,3,3,3,3,3) = 3.000 |
| GDPR-C21, GDPR-C23, CRA-C25, NIS2-C25, NIS2-C26, NIS2-C27, AI-C26, AI-C29 | OBL-D-04.3-001 | D-04.3 | ✅ MAX(3,3,3,3,3,3,3,3) = 3.000 |
| GDPR-C27, NIS2-C14 | OBL-D-08.1-001 | D-08.1 | ✅ MAX(3,3) = 3.000 |
| GDPR-C28, NIS2-C15, AI-C14, AI-C24 | OBL-D-08.2-001 | D-08.2 | ✅ MAX(3,3,3,3) = 3.000 |
| CRA-C01, CRA-C17, NIS2-C12, AI-C03, AI-C16 | OBL-D-02.1-001 | D-02.1 | ✅ MAX(3,3,3,3,3) = 3.000 |
| CRA-C03 | OBL-D-03.4-001 | D-03.4 | ✅ 3.000 |
| CRA-C04, CRA-C19, NIS2-C12 | OBL-D-02.2-001 | D-02.2 | ✅ MAX(3,3,3) = 3.000 |
| CRA-C05, NIS2-C16, NIS2-C19, AI-C15 | OBL-D-03.1-001 | D-03.1 | ✅ MAX(3,3,3,3) = 3.000 |
| CRA-C06, NIS2-C17 | OBL-D-03.2-001 | D-03.2 | ✅ MAX(2,3) = 3.000 |
| CRA-C12, NIS2-C21, NIS2-C29, AI-C25 | OBL-D-10.1-001 | D-10.1 | ✅ MAX(3,3,3,3) = 3.000 |
| CRA-C13, NIS2-C28, AI-C25 | OBL-D-04.1-001 | D-04.1 | ✅ MAX(3,3,3) = 3.000 |
| CRA-C14, NIS2-C22, AI-C09, AI-C10 | OBL-D-10.2-001 | D-10.2 | ✅ MAX(3,3,3,3) = 3.000 |
| CRA-C15, NIS2-C18, AI-C17 | OBL-D-01.3-001 | D-01.3 | ✅ MAX(3,3,3) = 3.000 |
| CRA-C18 | OBL-D-06.2-001 | D-06.2 | ✅ 3.000 |
| CRA-C21, CRA-C26, NIS2-C12 | OBL-D-02.3-001 | D-02.3 | ✅ MAX(3,3,3) = 3.000 |
| CRA-C02, NIS2-C11 | OBL-D-07.2-001 | D-07.2 | ✅ MAX(3,3) = 3.000 |
| NIS2-C02 | OBL-D-08.3-001 | D-08.3 | ✅ 3.000 |
| NIS2-C07 | OBL-D-09.3-001 | D-09.3 | ✅ 3.000 |
| NIS2-C10 | OBL-D-07.4-001 | D-07.4 | ✅ 3.000 |
| NIS2-C11 | OBL-D-07.3-001 | D-07.3 | ✅ 3.000 |
| NIS2-C24 | OBL-D-06.4-001 | D-06.4 | ✅ 3.000 |
| NIS2-C13, AI-C04 | OBL-D-02.4-001 | D-02.4 | ✅ MAX(3,3) = 3.000 |

**Total Mappings:** 111 clauses → 38 obligations
**NI Preservation:** 100% (all obligations use MAX NI from source clauses)

---

## 8. PHASE 2 GATE B CRITERIA

| Criterion | Status | Evidence |
|-----------|--------|----------|
| All 111 clauses mapped to obligations | ✅ PASS | Section 4 (38 obligations) |
| NI propagation complete | ✅ PASS | Section 6 (all 3.000) |
| Traceability matrix complete | ✅ PASS | Section 7 (111 → 38 mappings) |
| Sole authority obligations flagged | ✅ PASS | Section 5.4 (8 flagged) |
| Obligation types assigned | ✅ PASS | Section 5.2 |
| Obligated parties assigned | ✅ PASS | Section 5.3 |

**Gate B Status:** ✅ **PASS** — Ready for Gate C (Strategic Tensions Analysis)

---

## 9. REGULATORY COMPLEMENTARITY ANALYSIS (4-Regulation Overlay)

### 9.1 Pairwise Regulation Overlap (Jaccard Index)

With 4 applicable regulations (GDPR, CRA, NIS 2, AI_Act), there are 6 pairwise combinations to analyze.

| Regulation Pair | Intersection (Shared Sub-Domains) | Union (Total Sub-Domains) | Jaccard Index | Interpretation |
|-----------------|-----------------------------------|--------------------------|---------------|----------------|
| **GDPR ↔ CRA** | 11 | 31 | 0.355 | Moderate overlap — data protection + product security |
| **GDPR ↔ NIS 2** | 14 | 29 | 0.483 | High overlap — operational security + data protection |
| **GDPR ↔ AI_Act** | 10 | 27 | 0.370 | Moderate overlap — data protection + AI governance |
| **CRA ↔ NIS 2** | 16 | 30 | 0.533 | **Highest overlap** — product security + operational security |
| **CRA ↔ AI_Act** | 9 | 32 | 0.281 | Lower overlap — product security vs AI governance |
| **NIS 2 ↔ AI_Act** | 11 | 34 | 0.324 | Moderate overlap — operational security + AI governance |

**Key Insight:** CRA ↔ NIS 2 has the highest overlap (0.533) because both focus on technical security controls (vulnerability management, access control, incident response, monitoring). GDPR ↔ AI_Act has moderate overlap (0.370) centered on data governance and transparency.

### 9.2 Triple Regulation Overlap

| Sub-Domain | Regulations Covering It | Count | Relation Type |
|------------|------------------------|-------|---------------|
| D-01.1 Data at Rest Encryption | GDPR + CRA + NIS 2 + AI_Act | 4 | CUMULATIVE_REINFORCEMENT |
| D-01.2 Data in Transit Encryption | GDPR + CRA + NIS 2 | 3 | CUMULATIVE_REINFORCEMENT |
| D-01.4 Data Integrity Mechanisms | GDPR + CRA + AI_Act | 3 | CUMULATIVE_REINFORCEMENT |
| D-02.1 Vulnerability Identification | CRA + NIS 2 + AI_Act | 3 | CUMULATIVE_REINFORCEMENT |
| D-03.1 Identity Lifecycle Management | CRA + NIS 2 + AI_Act | 3 | CUMULATIVE_REINFORCEMENT |
| D-03.2 Multi-Factor Authentication | CRA + NIS 2 + AI_Act | 3 | CUMULATIVE_REINFORCEMENT |
| D-04.1 Incident Detection & Triage | CRA + NIS 2 + AI_Act | 3 | CUMULATIVE_REINFORCEMENT |
| D-04.2 Containment & Mitigation | GDPR + CRA + NIS 2 | 3 | CUMULATIVE_REINFORCEMENT |
| D-04.3 Regulatory Notification | GDPR + CRA + NIS 2 + AI_Act | 4 | **CONFLICT (Timing)** |
| D-05.1 Data Minimization | GDPR + CRA + AI_Act | 3 | CUMULATIVE_REINFORCEMENT |
| D-07.1 Secure-by-Design Principles | GDPR + CRA + NIS 2 | 3 | CUMULATIVE_REINFORCEMENT |
| D-08.2 Role-Specific Competence | GDPR + NIS 2 + AI_Act | 3 | CUMULATIVE_REINFORCEMENT |
| D-09.1 Information Security Policies | GDPR + CRA + NIS 2 + AI_Act | 4 | CUMULATIVE_REINFORCEMENT |
| D-09.2 Impact & Risk Assessments | GDPR + CRA + NIS 2 + AI_Act | 4 | **CONFLICT (Trigger)** |
| D-10.1 Continuous Security Monitoring | CRA + NIS 2 + AI_Act | 3 | CUMULATIVE_REINFORCEMENT |
| D-10.2 Audit Logging & Traceability | CRA + NIS 2 + AI_Act | 3 | CUMULATIVE_REINFORCEMENT |
| D-10.3 Compliance Testing | GDPR + CRA + NIS 2 + AI_Act | 4 | CUMULATIVE_REINFORCEMENT |

**Triple+ Overlap Summary:** 17 sub-domains covered by 3+ regulations (44.7% of taxonomy)

### 9.3 Quadruple Regulation Overlap (All 4 Regulations)

| Sub-Domain | Regulations | Combined NI | Relation Type | Implementation Implication |
|------------|-------------|-------------|---------------|---------------------------|
| D-01.1 Data at Rest Encryption | GDPR + CRA + NIS 2 + AI_Act | 3.000 | CUMULATIVE_REINFORCEMENT | Single encryption standard satisfies all |
| D-04.3 Regulatory Notification | GDPR + CRA + NIS 2 + AI_Act | 3.000 | **CONFLICT (Timing)** | Max-SLA routing required (24h workflow) |
| D-09.1 Information Security Policies | GDPR + CRA + NIS 2 + AI_Act | 3.000 | CUMULATIVE_REINFORCEMENT | Unified ISMS (ISO 27001) satisfies all |
| D-09.2 Impact & Risk Assessments | GDPR + CRA + NIS 2 + AI_Act | 3.000 | **CONFLICT (Trigger)** | Unified assessment (DPIA + FRIA) |
| D-10.3 Compliance Testing | GDPR + CRA + NIS 2 + AI_Act | 3.000 | CUMULATIVE_REINFORCEMENT | Unified testing program |

**Quadruple Overlap Summary:** 5 sub-domains covered by all 4 regulations (13.2% of taxonomy). Of these, 2 have conflicts requiring resolution (D-04.3, D-09.2).

### 9.4 Complementarity Opportunities

| Sub-Domain | Regulations | Complementarity Type | Implementation Approach | Efficiency Gain |
|------------|-------------|---------------------|------------------------|-----------------|
| D-01.1 | 4 regulations | Cumulative Reinforcement | Single strong symmetric encryption encryption standard | 75% reduction vs. 4 separate |
| D-04.3 | 4 regulations | Conflict (Timing) | Unified 24h/72h workflow | Single process satisfies all |
| D-09.1 | 4 regulations | Cumulative Reinforcement | Unified ISMS with annexes | 60% reduction vs. 4 separate |
| D-09.2 | 4 regulations | Conflict (Trigger) | Unified DPIA+FRIA assessment | 40% reduction vs. 4 separate |
| D-10.3 | 4 regulations | Cumulative Reinforcement | Unified testing program | 65% reduction vs. 4 separate |

---

## 10. MULTI-PARTY OBLIGATION ANALYSIS

### 10.1 Obligated Party Distribution

SecureBorder Solutions operates under 4 different obligated party roles simultaneously:

| Obligated Party | Regulations | Obligations Affected | Key Responsibilities |
|-----------------|-------------|---------------------|----------------------|
| **CONTROLLER** | GDPR | 15/38 (39.5%) | Data protection, DPIA, breach notification, RoPA, DPO |
| **MANUFACTURER** | CRA | 16/38 (42.1%) | Product security, vulnerability management, SBOM, conformity assessment |
| **ESSENTIAL_ENTITY_SUPPLIER** | NIS 2 | 22/38 (57.9%) | Operational security, 24h incident notification, supply chain, board training |
| **PROVIDER** | AI_Act | 14/38 (36.8%) | AI conformity, post-market monitoring, human oversight, fundamental rights |

### 10.2 Multi-Party Obligations (All 4 Roles)

These obligations require SecureBorder to act in ALL 4 roles simultaneously:

| Obligation ID | Sub-Domain | CONTROLLER Role | MANUFACTURER Role | ESSENTIAL_ENTITY Role | PROVIDER Role |
|---------------|------------|-----------------|-------------------|----------------------|---------------|
| OBL-D-01.1-001 | D-01.1 | Encrypt personal data | Encrypt product data | Encrypt operational data | Encrypt AI data |
| OBL-D-04.3-001 | D-04.3 | 72h breach notification | 24h vuln notification | 24h incident notification | Market surveillance cooperation |
| OBL-D-09.1-001 | D-09.1 | Privacy policies | Technical documentation | Security policies | AI technical documentation |
| OBL-D-09.2-001 | D-09.2 | DPIA | Cybersecurity risk assessment | Incident handling procedures | FRIA + AI risk assessment |
| OBL-D-10.3-001 | D-10.3 | Security testing | Regular testing | Security testing | Periodic AI evaluation |

### 10.3 Role-Specific Obligations (Single Party)

| Obligation ID | Sub-Domain | Sole Obligated Party | Reason |
|---------------|------------|---------------------|--------|
| OBL-D-03.4-001 | D-03.4 Secure System Defaults | MANUFACTURER (CRA) | Product design requirement |
| OBL-D-05.4-001 | D-05.4 Data Portability | CONTROLLER (GDPR) | Data subject right |
| OBL-D-06.2-001 | D-06.2 SBOM | MANUFACTURER (CRA) | Product documentation |
| OBL-D-06.4-001 | D-06.4 Third-Party Boundary | ESSENTIAL_ENTITY (NIS 2) | Operational boundary |
| OBL-D-07.3-001 | D-07.3 CI/CD Pipeline Security | ESSENTIAL_ENTITY (NIS 2) | Operational security |
| OBL-D-07.4-001 | D-07.4 Change Management | ESSENTIAL_ENTITY (NIS 2) | Operational process |
| OBL-D-08.3-001 | D-08.3 Management Board Training | ESSENTIAL_ENTITY (NIS 2) | Management liability |
| OBL-D-09.3-001 | D-09.3 Asset Inventories | ESSENTIAL_ENTITY (NIS 2) | Operational asset management |

---

## 11. PER-REGULATION OBLIGATION BREAKDOWN

### 11.1 GDPR-Specific Obligations (28 clauses → 15 obligations)

| Obligation ID | Sub-Domain | Source GDPR Clauses | NI | obligationType |
|---------------|------------|--------------------|-----|----------------|
| OBL-D-01.1-001 | D-01.1 | GDPR-C04, GDPR-C14 | 2.000 | CONTINUOUS |
| OBL-D-01.2-001 | D-01.2 | GDPR-C15 | 2.000 | CONTINUOUS |
| OBL-D-01.4-001 | D-01.4 | GDPR-C05 | 2.000 | CONTINUOUS |
| OBL-D-03.3-001 | D-03.3 | GDPR-C10, GDPR-C17 | 3.000 | CONTINUOUS |
| OBL-D-04.2-001 | D-04.2 | GDPR-C18 | 2.000 | TRIGGERED |
| OBL-D-04.3-001 | D-04.3 | GDPR-C21, GDPR-C23 | 3.000 | TRIGGERED |
| OBL-D-04.4-001 | D-04.4 | GDPR-C16 | 2.000 | TRIGGERED |
| OBL-D-05.1-001 | D-05.1 | GDPR-C01 | 3.000 | CONTINUOUS |
| OBL-D-05.2-001 | D-05.2 | GDPR-C02, GDPR-C03 | 3.000 | CONTINUOUS |
| OBL-D-05.3-001 | D-05.3 | GDPR-C06 | 3.000 | TRIGGERED |
| OBL-D-05.4-001 | D-05.4 | GDPR-C07 | 3.000 | TRIGGERED |
| OBL-D-06.1-001 | D-06.1 | GDPR-C11 | 3.000 | ONE_TIME |
| OBL-D-06.3-001 | D-06.3 | GDPR-C12 | 3.000 | ONE_TIME |
| OBL-D-07.1-001 | D-07.1 | GDPR-C09 | 2.000 | ONE_TIME |
| OBL-D-08.1-001 | D-08.1 | GDPR-C27 | 3.000 | PERIODIC |
| OBL-D-08.2-001 | D-08.2 | GDPR-C28 | 3.000 | PERIODIC |
| OBL-D-09.1-001 | D-09.1 | GDPR-C08, GDPR-C25, GDPR-C26 | 2.333 | CONTINUOUS |
| OBL-D-09.2-001 | D-09.2 | GDPR-C20, GDPR-C24 | 2.500 | ONE_TIME |
| OBL-D-09.4-001 | D-09.4 | GDPR-C13, GDPR-C22 | 3.000 | CONTINUOUS |
| OBL-D-10.3-001 | D-10.3 | GDPR-C19 | 3.000 | PERIODIC |

**GDPR Mean NI:** 2.643 | **Obligations:** 20 | **Dominant Types:** CONTINUOUS (10), TRIGGERED (5)

### 11.2 CRA-Specific Obligations (26 clauses → 16 obligations)

| Obligation ID | Sub-Domain | Source CRA Clauses | NI | obligationType |
|---------------|------------|--------------------|-----|----------------|
| OBL-D-01.1-001 | D-01.1 | CRA-C07 | 3.000 | CONTINUOUS |
| OBL-D-01.2-001 | D-01.2 | CRA-C08 | 3.000 | CONTINUOUS |
| OBL-D-01.3-001 | D-01.3 | CRA-C15 | 3.000 | CONTINUOUS |
| OBL-D-01.4-001 | D-01.4 | CRA-C09 | 3.000 | CONTINUOUS |
| OBL-D-02.1-001 | D-02.1 | CRA-C01, CRA-C17 | 3.000 | CONTINUOUS |
| OBL-D-02.2-001 | D-02.2 | CRA-C04, CRA-C19 | 3.000 | CONTINUOUS |
| OBL-D-02.3-001 | D-02.3 | CRA-C21, CRA-C26 | 3.000 | CONTINUOUS |
| OBL-D-03.1-001 | D-03.1 | CRA-C05 | 3.000 | ONE_TIME |
| OBL-D-03.2-001 | D-03.2 | CRA-C06 | 2.000 | ONE_TIME |
| OBL-D-03.4-001 | D-03.4 | CRA-C03 | 3.000 | ONE_TIME |
| OBL-D-04.1-001 | D-04.1 | CRA-C13 | 3.000 | ONE_TIME |
| OBL-D-04.2-001 | D-04.2 | CRA-C11 | 3.000 | ONE_TIME |
| OBL-D-04.3-001 | D-04.3 | CRA-C25 | 3.000 | TRIGGERED |
| OBL-D-05.1-001 | D-05.1 | CRA-C10 | 3.000 | ONE_TIME |
| OBL-D-05.3-001 | D-05.3 | CRA-C16 | 3.000 | ONE_TIME |
| OBL-D-06.2-001 | D-06.2 | CRA-C18 | 3.000 | CONTINUOUS |
| OBL-D-07.1-001 | D-07.1 | CRA-C02, CRA-C22 | 3.000 | ONE_TIME |
| OBL-D-07.2-001 | D-07.2 | CRA-C02 | 3.000 | CONTINUOUS |
| OBL-D-09.1-001 | D-09.1 | CRA-C24 | 3.000 | CONTINUOUS |
| OBL-D-09.2-001 | D-09.2 | CRA-C23 | 3.000 | ONE_TIME |
| OBL-D-10.1-001 | D-10.1 | CRA-C12 | 3.000 | CONTINUOUS |
| OBL-D-10.2-001 | D-10.2 | CRA-C14 | 3.000 | CONTINUOUS |
| OBL-D-10.3-001 | D-10.3 | CRA-C20 | 2.000 | PERIODIC |

**CRA Mean NI:** 2.923 | **Obligations:** 23 | **Dominant Types:** CONTINUOUS (11), ONE_TIME (9)

### 11.3 NIS 2-Specific Obligations (29 clauses → 22 obligations)

| Obligation ID | Sub-Domain | Source NIS 2 Clauses | NI | obligationType |
|---------------|------------|---------------------|-----|----------------|
| OBL-D-01.1-001 | D-01.1 | NIS2-C18 | 3.000 | CONTINUOUS |
| OBL-D-01.2-001 | D-01.2 | NIS2-C18 | 3.000 | CONTINUOUS |
| OBL-D-01.3-001 | D-01.3 | NIS2-C18 | 3.000 | CONTINUOUS |
| OBL-D-02.1-001 | D-02.1 | NIS2-C12 | 3.000 | CONTINUOUS |
| OBL-D-02.2-001 | D-02.2 | NIS2-C12 | 3.000 | CONTINUOUS |
| OBL-D-02.3-001 | D-02.3 | NIS2-C12 | 3.000 | CONTINUOUS |
| OBL-D-02.4-001 | D-02.4 | NIS2-C13 | 3.000 | PERIODIC |
| OBL-D-03.1-001 | D-03.1 | NIS2-C16, NIS2-C19 | 3.000 | CONTINUOUS |
| OBL-D-03.2-001 | D-03.2 | NIS2-C17 | 3.000 | CONTINUOUS |
| OBL-D-03.3-001 | D-03.3 | NIS2-C20 | 3.000 | CONTINUOUS |
| OBL-D-04.1-001 | D-04.1 | NIS2-C28 | 3.000 | CONTINUOUS |
| OBL-D-04.2-001 | D-04.2 | NIS2-C05 | 3.000 | CONTINUOUS |
| OBL-D-04.3-001 | D-04.3 | NIS2-C25, NIS2-C26, NIS2-C27 | 3.000 | TRIGGERED |
| OBL-D-04.4-001 | D-04.4 | NIS2-C06 | 3.000 | TRIGGERED |
| OBL-D-06.1-001 | D-06.1 | NIS2-C08, NIS2-C23 | 3.000 | CONTINUOUS |
| OBL-D-06.3-001 | D-06.3 | NIS2-C09 | 3.000 | ONE_TIME |
| OBL-D-06.4-001 | D-06.4 | NIS2-C24 | 3.000 | CONTINUOUS |
| OBL-D-07.2-001 | D-07.2 | NIS2-C11 | 3.000 | CONTINUOUS |
| OBL-D-07.3-001 | D-07.3 | NIS2-C11 | 3.000 | CONTINUOUS |
| OBL-D-07.4-001 | D-07.4 | NIS2-C10 | 3.000 | CONTINUOUS |
| OBL-D-08.1-001 | D-08.1 | NIS2-C14 | 3.000 | PERIODIC |
| OBL-D-08.2-001 | D-08.2 | NIS2-C15 | 3.000 | PERIODIC |
| OBL-D-08.3-001 | D-08.3 | NIS2-C02 | 3.000 | PERIODIC |
| OBL-D-09.1-001 | D-09.1 | NIS2-C01 | 3.000 | CONTINUOUS |
| OBL-D-09.2-001 | D-09.2 | NIS2-C04 | 3.000 | CONTINUOUS |
| OBL-D-09.3-001 | D-09.3 | NIS2-C07 | 3.000 | CONTINUOUS |
| OBL-D-10.1-001 | D-10.1 | NIS2-C21, NIS2-C29 | 3.000 | CONTINUOUS |
| OBL-D-10.2-001 | D-10.2 | NIS2-C22 | 3.000 | CONTINUOUS |
| OBL-D-10.3-001 | D-10.3 | NIS2-C13 | 3.000 | PERIODIC |

**NIS 2 Mean NI:** 3.000 | **Obligations:** 29 | **Dominant Types:** CONTINUOUS (21), PERIODIC (4), TRIGGERED (3), ONE_TIME (1)

### 11.4 AI_Act-Specific Obligations (28 clauses → 14 obligations)

| Obligation ID | Sub-Domain | Source AI_Act Clauses | NI | obligationType |
|---------------|------------|----------------------|-----|----------------|
| OBL-D-01.1-001 | D-01.1 | AI-C17 | 3.000 | CONTINUOUS |
| OBL-D-01.4-001 | D-01.4 | AI-C18 | 3.000 | CONTINUOUS |
| OBL-D-02.1-001 | D-02.1 | AI-C03, AI-C16 | 3.000 | CONTINUOUS |
| OBL-D-02.4-001 | D-02.4 | AI-C04 | 3.000 | PERIODIC |
| OBL-D-03.1-001 | D-03.1 | AI-C15 | 3.000 | CONTINUOUS |
| OBL-D-04.1-001 | D-04.1 | AI-C25 | 3.000 | CONTINUOUS |
| OBL-D-04.3-001 | D-04.3 | AI-C26, AI-C29 | 3.000 | CONTINUOUS |
| OBL-D-05.1-001 | D-05.1 | AI-C05, AI-C06 | 3.000 | ONE_TIME |
| OBL-D-05.2-001 | D-05.2 | AI-C07 | 3.000 | CONTINUOUS |
| OBL-D-08.2-001 | D-08.2 | AI-C14, AI-C24 | 3.000 | CONTINUOUS |
| OBL-D-09.1-001 | D-09.1 | AI-C08, AI-C12, AI-C13, AI-C20, AI-C23 | 3.000 | CONTINUOUS |
| OBL-D-09.2-001 | D-09.2 | AI-C01, AI-C02, AI-C22 | 3.000 | ONE_TIME |
| OBL-D-09.4-001 | D-09.4 | AI-C11 | 3.000 | CONTINUOUS |
| OBL-D-10.1-001 | D-10.1 | AI-C25 | 3.000 | CONTINUOUS |
| OBL-D-10.2-001 | D-10.2 | AI-C09, AI-C10 | 3.000 | CONTINUOUS |
| OBL-D-10.3-001 | D-10.3 | AI-C21, AI-C27 | 3.000 | PERIODIC |

**AI_Act Mean NI:** 3.000 | **Obligations:** 16 | **Dominant Types:** CONTINUOUS (12), PERIODIC (2), ONE_TIME (2)

---

## 12. FULL TRACEABILITY MATRIX (112 Clauses → 38 Obligations)

### 12.1 Complete Clause-to-Obligation Mapping

| Source Clause | → Target Obligation | Sub-Domain | NI Preserved? | Obligated Party |
|---------------|---------------------|------------|---------------|-----------------|
| GDPR-C01 | → OBL-D-05.1-001 | D-05.1 | ✅ 3.000 | CONTROLLER |
| GDPR-C02 | → OBL-D-05.2-001 | D-05.2 | ✅ 3.000 | CONTROLLER |
| GDPR-C03 | → OBL-D-05.2-001 | D-05.2 | ✅ 3.000 | CONTROLLER |
| GDPR-C04 | → OBL-D-01.1-001 | D-01.1 | ✅ MAX(2,2,3,3,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C05 | → OBL-D-01.4-001 | D-01.4 | ✅ MAX(2,3,3)=3.000 | CONTROLLER |
| GDPR-C06 | → OBL-D-05.3-001 | D-05.3 | ✅ 3.000 | CONTROLLER, PROCESSOR |
| GDPR-C07 | → OBL-D-05.4-001 | D-05.4 | ✅ 3.000 | CONTROLLER |
| GDPR-C08 | → OBL-D-09.1-001 | D-09.1 | ✅ MAX(2,3,2,3,3,3,3,3,3,3)=3.000 | CONTROLLER |
| GDPR-C09 | → OBL-D-07.1-001 | D-07.1 | ✅ MAX(2,3,3)=3.000 | CONTROLLER |
| GDPR-C10 | → OBL-D-03.3-001 | D-03.3 | ✅ MAX(3,3,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C11 | → OBL-D-06.1-001 | D-06.1 | ✅ MAX(3,3,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C12 | → OBL-D-06.3-001 | D-06.3 | ✅ MAX(3,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C13 | → OBL-D-09.4-001 | D-09.4 | ✅ MAX(3,3,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C14 | → OBL-D-01.1-001 | D-01.1 | ✅ MAX(2,2,3,3,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C15 | → OBL-D-01.2-001 | D-01.2 | ✅ MAX(2,3,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C16 | → OBL-D-04.4-001 | D-04.4 | ✅ MAX(2,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C17 | → OBL-D-03.3-001 | D-03.3 | ✅ MAX(3,3,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C18 | → OBL-D-04.2-001 | D-04.2 | ✅ MAX(2,3,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C19 | → OBL-D-10.3-001 | D-10.3 | ✅ MAX(3,2,3,3,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C20 | → OBL-D-09.2-001 | D-09.2 | ✅ MAX(2,3,3,3,3,3,3)=3.000 | CONTROLLER |
| GDPR-C21 | → OBL-D-04.3-001 | D-04.3 | ✅ MAX(3,3,3,3,3,3,3,3)=3.000 | CONTROLLER |
| GDPR-C22 | → OBL-D-09.4-001 | D-09.4 | ✅ MAX(3,3,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C23 | → OBL-D-04.3-001 | D-04.3 | ✅ MAX(3,3,3,3,3,3,3,3)=3.000 | CONTROLLER |
| GDPR-C24 | → OBL-D-09.2-001 | D-09.2 | ✅ MAX(2,3,3,3,3,3,3)=3.000 | CONTROLLER |
| GDPR-C25 | → OBL-D-09.1-001 | D-09.1 | ✅ MAX(2,3,2,3,3,3,3,3,3,3)=3.000 | CONTROLLER |
| GDPR-C26 | → OBL-D-09.1-001 | D-09.1 | ✅ MAX(2,3,2,3,3,3,3,3,3,3)=3.000 | CONTROLLER |
| GDPR-C27 | → OBL-D-08.1-001 | D-08.1 | ✅ MAX(3,3)=3.000 | CONTROLLER, PROCESSOR |
| GDPR-C28 | → OBL-D-08.2-001 | D-08.2 | ✅ MAX(3,3,3,3)=3.000 | CONTROLLER, PROCESSOR |
| CRA-C01 | → OBL-D-02.1-001 | D-02.1 | ✅ MAX(3,3,3,3,3)=3.000 | MANUFACTURER |
| CRA-C02 | → OBL-D-07.1-001, OBL-D-07.2-001 | D-07.1, D-07.2 | ✅ 3.000 | MANUFACTURER |
| CRA-C03 | → OBL-D-03.4-001 | D-03.4 | ✅ 3.000 | MANUFACTURER |
| CRA-C04 | → OBL-D-02.2-001 | D-02.2 | ✅ MAX(3,3,3)=3.000 | MANUFACTURER |
| CRA-C05 | → OBL-D-03.1-001 | D-03.1 | ✅ MAX(3,3,3,3)=3.000 | MANUFACTURER |
| CRA-C06 | → OBL-D-03.2-001 | D-03.2 | ✅ MAX(2,3)=3.000 | MANUFACTURER |
| CRA-C07 | → OBL-D-01.1-001 | D-01.1 | ✅ MAX(2,2,3,3,3)=3.000 | MANUFACTURER |
| CRA-C08 | → OBL-D-01.2-001 | D-01.2 | ✅ MAX(2,3,3)=3.000 | MANUFACTURER |
| CRA-C09 | → OBL-D-01.4-001 | D-01.4 | ✅ MAX(2,3,3)=3.000 | MANUFACTURER |
| CRA-C10 | → OBL-D-05.1-001 | D-05.1 | ✅ MAX(3,3,3,3)=3.000 | MANUFACTURER |
| CRA-C11 | → OBL-D-04.2-001 | D-04.2 | ✅ MAX(2,3,3)=3.000 | MANUFACTURER |
| CRA-C12 | → OBL-D-10.1-001 | D-10.1 | ✅ MAX(3,3,3,3,3)=3.000 | MANUFACTURER |
| CRA-C13 | → OBL-D-04.1-001 | D-04.1 | ✅ MAX(3,3,3)=3.000 | MANUFACTURER |
| CRA-C14 | → OBL-D-10.2-001 | D-10.2 | ✅ MAX(3,3,3,3)=3.000 | MANUFACTURER |
| CRA-C15 | → OBL-D-01.3-001 | D-01.3 | ✅ MAX(3,3,3)=3.000 | MANUFACTURER |
| CRA-C16 | → OBL-D-05.3-001 | D-05.3 | ✅ MAX(3,3)=3.000 | MANUFACTURER |
| CRA-C17 | → OBL-D-02.1-001 | D-02.1 | ✅ MAX(3,3,3,3,3)=3.000 | MANUFACTURER |
| CRA-C18 | → OBL-D-06.2-001 | D-06.2 | ✅ 3.000 | MANUFACTURER |
| CRA-C19 | → OBL-D-02.2-001 | D-02.2 | ✅ MAX(3,3,3)=3.000 | MANUFACTURER |
| CRA-C20 | → OBL-D-10.3-001 | D-10.3 | ✅ MAX(3,2,3,3,3)=3.000 | MANUFACTURER |
| CRA-C21 | → OBL-D-02.3-001 | D-02.3 | ✅ MAX(3,3,3)=3.000 | MANUFACTURER |
| CRA-C22 | → OBL-D-07.1-001 | D-07.1 | ✅ MAX(2,3,3)=3.000 | MANUFACTURER |
| CRA-C23 | → OBL-D-09.2-001 | D-09.2 | ✅ MAX(2,3,3,3,3,3,3)=3.000 | MANUFACTURER |
| CRA-C24 | → OBL-D-09.1-001 | D-09.1 | ✅ MAX(2,3,2,3,3,3,3,3,3,3)=3.000 | MANUFACTURER |
| CRA-C25 | → OBL-D-04.3-001 | D-04.3 | ✅ MAX(3,3,3,3,3,3,3,3)=3.000 | MANUFACTURER |
| CRA-C26 | → OBL-D-02.3-001 | D-02.3 | ✅ MAX(3,3,3)=3.000 | MANUFACTURER |
| NIS2-C01 | → OBL-D-09.1-001 | D-09.1 | ✅ MAX(2,3,2,3,3,3,3,3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C02 | → OBL-D-08.3-001 | D-08.3 | ✅ 3.000 | ESSENTIAL_ENTITY |
| NIS2-C03 | → OBL-D-09.1-001 | D-09.1 | ✅ MAX(2,3,2,3,3,3,3,3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C04 | → OBL-D-09.2-001 | D-09.2 | ✅ MAX(2,3,3,3,3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C05 | → OBL-D-04.2-001 | D-04.2 | ✅ MAX(2,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C06 | → OBL-D-04.4-001 | D-04.4 | ✅ MAX(2,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C07 | → OBL-D-09.3-001 | D-09.3 | ✅ 3.000 | ESSENTIAL_ENTITY |
| NIS2-C08 | → OBL-D-06.1-001 | D-06.1 | ✅ MAX(3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C09 | → OBL-D-06.3-001 | D-06.3 | ✅ MAX(3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C10 | → OBL-D-07.4-001 | D-07.4 | ✅ 3.000 | ESSENTIAL_ENTITY |
| NIS2-C11 | → OBL-D-07.2-001, OBL-D-07.3-001 | D-07.2, D-07.3 | ✅ 3.000 | ESSENTIAL_ENTITY |
| NIS2-C12 | → OBL-D-02.1-001, OBL-D-02.2-001, OBL-D-02.3-001 | D-02.1, D-02.2, D-02.3 | ✅ 3.000 | ESSENTIAL_ENTITY |
| NIS2-C13 | → OBL-D-02.4-001, OBL-D-10.3-001 | D-02.4, D-10.3 | ✅ MAX(3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C14 | → OBL-D-08.1-001 | D-08.1 | ✅ MAX(3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C15 | → OBL-D-08.2-001 | D-08.2 | ✅ MAX(3,3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C16 | → OBL-D-03.1-001 | D-03.1 | ✅ MAX(3,3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C17 | → OBL-D-03.2-001 | D-03.2 | ✅ MAX(2,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C18 | → OBL-D-01.1-001, OBL-D-01.2-001, OBL-D-01.3-001 | D-01.1, D-01.2, D-01.3 | ✅ 3.000 | ESSENTIAL_ENTITY |
| NIS2-C19 | → OBL-D-03.1-001 | D-03.1 | ✅ MAX(3,3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C20 | → OBL-D-03.3-001 | D-03.3 | ✅ MAX(3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C21 | → OBL-D-10.1-001 | D-10.1 | ✅ MAX(3,3,3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C22 | → OBL-D-10.2-001 | D-10.2 | ✅ MAX(3,3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C23 | → OBL-D-06.1-001 | D-06.1 | ✅ MAX(3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C24 | → OBL-D-06.4-001 | D-06.4 | ✅ 3.000 | ESSENTIAL_ENTITY |
| NIS2-C25 | → OBL-D-04.3-001 | D-04.3 | ✅ MAX(3,3,3,3,3,3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C26 | → OBL-D-04.3-001 | D-04.3 | ✅ MAX(3,3,3,3,3,3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C27 | → OBL-D-04.3-001 | D-04.3 | ✅ MAX(3,3,3,3,3,3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C28 | → OBL-D-04.1-001 | D-04.1 | ✅ MAX(3,3,3)=3.000 | ESSENTIAL_ENTITY |
| NIS2-C29 | → OBL-D-10.1-001 | D-10.1 | ✅ MAX(3,3,3,3,3)=3.000 | ESSENTIAL_ENTITY |
| AI-C01 | → OBL-D-09.2-001 | D-09.2 | ✅ MAX(2,3,3,3,3,3,3)=3.000 | PROVIDER |
| AI-C02 | → OBL-D-09.2-001 | D-09.2 | ✅ MAX(2,3,3,3,3,3,3)=3.000 | PROVIDER |
| AI-C03 | → OBL-D-02.1-001 | D-02.1 | ✅ MAX(3,3,3,3,3)=3.000 | PROVIDER |
| AI-C04 | → OBL-D-02.4-001 | D-02.4 | ✅ MAX(3,3)=3.000 | PROVIDER |
| AI-C05 | → OBL-D-05.1-001 | D-05.1 | ✅ MAX(3,3,3,3)=3.000 | PROVIDER |
| AI-C06 | → OBL-D-05.1-001 | D-05.1 | ✅ MAX(3,3,3,3)=3.000 | PROVIDER |
| AI-C07 | → OBL-D-05.2-001 | D-05.2 | ✅ MAX(3,3,3)=3.000 | PROVIDER |
| AI-C08 | → OBL-D-09.1-001 | D-09.1 | ✅ MAX(2,3,2,3,3,3,3,3,3,3)=3.000 | PROVIDER |
| AI-C09 | → OBL-D-10.2-001 | D-10.2 | ✅ MAX(3,3,3,3)=3.000 | PROVIDER |
| AI-C10 | → OBL-D-10.2-001 | D-10.2 | ✅ MAX(3,3,3,3)=3.000 | PROVIDER |
| AI-C11 | → OBL-D-09.4-001 | D-09.4 | ✅ MAX(3,3,3)=3.000 | PROVIDER |
| AI-C12 | → OBL-D-09.1-001 | D-09.1 | ✅ MAX(2,3,2,3,3,3,3,3,3,3)=3.000 | PROVIDER |
| AI-C13 | → OBL-D-09.1-001 | D-09.1 | ✅ MAX(2,3,2,3,3,3,3,3,3,3)=3.000 | PROVIDER |
| AI-C14 | → OBL-D-08.2-001 | D-08.2 | ✅ MAX(3,3,3,3)=3.000 | PROVIDER |
| AI-C15 | → OBL-D-03.1-001 | D-03.1 | ✅ MAX(3,3,3,3)=3.000 | PROVIDER |
| AI-C16 | → OBL-D-02.1-001 | D-02.1 | ✅ MAX(3,3,3,3,3)=3.000 | PROVIDER |
| AI-C17 | → OBL-D-01.1-001, OBL-D-01.3-001 | D-01.1, D-01.3 | ✅ 3.000 | PROVIDER |
| AI-C18 | → OBL-D-01.4-001 | D-01.4 | ✅ MAX(2,3,3)=3.000 | PROVIDER |
| AI-C20 | → OBL-D-09.1-001 | D-09.1 | ✅ MAX(2,3,2,3,3,3,3,3,3,3)=3.000 | PROVIDER |
| AI-C21 | → OBL-D-10.3-001 | D-10.3 | ✅ MAX(3,2,3,3,3)=3.000 | PROVIDER |
| AI-C22 | → OBL-D-09.2-001 | D-09.2 | ✅ MAX(2,3,3,3,3,3,3)=3.000 | PROVIDER |
| AI-C23 | → OBL-D-09.1-001 | D-09.1 | ✅ MAX(2,3,2,3,3,3,3,3,3,3)=3.000 | PROVIDER |
| AI-C24 | → OBL-D-08.2-001 | D-08.2 | ✅ MAX(3,3,3,3)=3.000 | PROVIDER |
| AI-C25 | → OBL-D-04.1-001, OBL-D-10.1-001 | D-04.1, D-10.1 | ✅ 3.000 | PROVIDER |
| AI-C26 | → OBL-D-04.3-001 | D-04.3 | ✅ MAX(3,3,3,3,3,3,3,3)=3.000 | PROVIDER |
| AI-C27 | → OBL-D-10.3-001 | D-10.3 | ✅ MAX(3,2,3,3,3)=3.000 | PROVIDER |
| AI-C28 | → OBL-D-09.2-001 | D-09.2 | ✅ MAX(2,3,3,3,3,3,3)=3.000 | PROVIDER |
| AI-C29 | → OBL-D-04.3-001 | D-04.3 | ✅ MAX(3,3,3,3,3,3,3,3)=3.000 | PROVIDER |

**Total Mappings:** 111 clauses → 38 obligations (100% coverage)
**NI Preservation:** 100% (all obligations use MAX NI from source clauses)
**Multi-Target Clauses:** 5 clauses map to multiple obligations (CRA-C02, NIS2-C11, NIS2-C12, NIS2-C13, NIS2-C18, AI-C17, AI-C25)

---

## 13. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-03 | Compliance Lead | Initial release - SecureBorder Solutions case (38 obligations from 112 clauses) |
| 1.1 | 2026-04-03 | Compliance Lead | Expanded: complementarity analysis (6 pairwise + triple + quadruple), multi-party analysis, per-regulation breakdown, full 112→38 traceability matrix |
| 1.2 | 2026-04-11 | Compliance Lead | CR-02: Added GDPR Art. 37(1)(c) mandatory DPO for processor handling Art. 9 data (D-09); MD-01: Added GDPR Art. 33(2) "without undue delay" processor→controller (D-04); MD-02: Added CRA Art. 8 certification scheme caveat (D-07); MD-03: Added CRA Art. 13(8) 5-year support + Art. 13(9) 10-year retention (D-07); MD-04: Added DPIA Art. 35(3)(b) automatic mandatory trigger (D-09); MD-05: Added AI_Act Art. 5 prohibited practices negative confirmation (D-09); MD-06: Added AI_Act Art. 25 downstream provider (D-06); MD-07: Added CRA Art. 24 exclusions analysis (D-07) |
| 5.1 | 2026-08-13 | Executor (R7 of remediation contract) | AI-C19 (AI Act Art. 26(1) deployer obligations) removed from AI Act clause list and from OBL-D-10.1-001 source clauses. D1 decision: SecureBorder is PROVIDER only; deployer duty falls on border-control authority. Total clauses 112 → 111 (29 → 28 AI Act). NI preserved at 3.000 via MAX(3,3,3,3) for the affected obligation. No new clause added. |

---

## 10. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-03 |
| Technical Review (CTO) | | | |
| Security Review (CISO) | | | |
| AEGIS Methodology Review | | | |

---

**Next Document:** 09_Strategic_Tensions_Report.md
**Gate Status:** ✅ PASS — Ready for Strategic Tensions Analysis
**Companion File:** 06_Clause_Mapping_Matrix.xlsx (source data)
