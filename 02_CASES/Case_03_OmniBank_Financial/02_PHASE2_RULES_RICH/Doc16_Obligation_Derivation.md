---
document_id: AEGIS-P2-08
title: Obligation Derivation Report
phase: 2
version: 1.0
created: 2026-04-03
updated: 2026-08-28
author: Compliance Lead
status: ACTIVE
inputs: [Doc12_Structured_Compliance_Matrix.md, ../01_PHASE1_CONTEXT_RICH/Case_03_Phase1_RICH.xlsx]
outputs: [Doc17_Strategic_Tensions_Report.md, Doc18_Privacy_Security_Objectives.md]
traceability: AEGIS Class Model → RegulatoryObligation, RegulatoryClause classes
related_documents: 00_Taxonomy_Reference.md, 03_Design_Decisions_Log.md
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI_Act]
---

# Obligation Derivation Report

## 1. DOCUMENT PURPOSE

This document consolidates the obligation derivation process (Step B1+B2+B3), transforming 150 regulatory clauses from 5 regulations (GDPR, CRA, NIS 2, DORA, AI Act) into abstract regulatory obligations (RegulatoryObligations) with traceability and Normative Intensity propagation. This is the maximum complexity case in the AEGIS methodology.

**Alignment with Class Model:**
- `RegulatoryObligation` - Derived obligations from clauses
- `RegulatoryClause` - Source clauses for each obligation (150 total)
- `DomainCoverageEntry` - Sub-domain mapping for obligations

**Phase 2 Step:** B (Obligation Derivation)

**Gate Criteria:** All 150 applicable clauses mapped to obligations with NI propagation

---

## 2. OBLIGATION DERIVATION METADATA

| Attribute | Value |
|-----------|-------|
| derivationId | DERIV-OMNIBANK-2026-001 |
| derivationDate | 2026-04-03 |
| basedOnComplianceMatrix | SCM-OMNIBANK-2026-001 |
| derivedBy | Compliance Lead |
| phase2Step | B1+B2+B3 |
| caseComplexity | MAXIMUM (5/5 regulations, 38/38 sub-domains) |

---

## 3. DERIVATION METHODOLOGY

### 3.1 Derivation Rules

| Rule ID | Rule Description | Application |
|---------|------------------|-------------|
| DR-001 | One-to-Many: One clause may derive multiple obligations | When clause spans multiple sub-domains |
| DR-002 | NI Propagation: AVG of source clause NIs | obligationNI = AVG(clauseNI) |
| DR-003 | Traceability: Each obligation links to source clause(s) | Mandatory bidirectional link |
| DR-004 | Sub-Domain Assignment: Each obligation targets one sub-domain | Primary domain classification |
| DR-005 | Actor Separation: Do not merge clauses with different obligatedParty | GDPR (CONTROLLER) vs CRA (MANUFACTURER) vs NIS 2 (ESSENTIAL_ENTITY) vs DORA (FINANCIAL_ENTITY) vs AI Act (PROVIDER) |
| DR-006 | Sole Authority Flag: Mark obligations from sub-domains with single-regulation coverage | e.g., D-03.4 (CRA sole in Case 3 context) |
| DR-007 | Activation Condition Flag: Mark obligations that derive from clauses with different trigger conditions | Obligations combining clauses with distinct triggers (e.g., GDPR personal data breach + CRA exploited vuln + NIS 2 significant incident + DORA ICT incident + AI Act serious AI incident) are flagged as CONTEXTUAL |
| DR-008 | Activation Nature: Classify obligation as structural or contextual | If all source clauses share the same trigger context → STRUCTURAL (always active). If source clauses have distinct triggers that may or may not overlap → CONTEXTUAL (activated by compound event) |

### 3.2 Obligation ID Structure

```
OBL-[Sub-Domain ID]-[Sequence Number]
Example: OBL-D-01.1-001
```

### 3.3 Complexity Profile

| Metric | Case 1 (TinyTask) | Case 3 (OmniBank) | Delta |
|--------|-------------------|-------------------|-------|
| Regulations | 2 (GDPR, CRA) | 5 (ALL) | +3 |
| Total Clauses | 54 | 150 | +96 (+178%) |
| Sub-Domains Covered | 20/38 (52.6%) | 38/38 (100%) | +18 |
| Obligation Types | 4 | 4 | Same |
| Mean NI | 2.821 | 2.858 | +0.037 |

---

## 4. REGULATORY OBLIGATIONS CATALOG

### D-01: Data Protection & Encryption Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty(ies) |
|---------------|------------------------|----------------|------------|-----|----------------|---------------------|
| OBL-D-01.1-001 | Personal, financial, and AI data in persistent storage protected by confidentiality mechanisms with segregated cryptographic material management | GDPR-C04, GDPR-C14, CRA-C07, NIS2-C18, DORA-C09, AI-C17 | D-01.1 | 2.667 | CONTINUOUS | CONTROLLER, PROCESSOR, MANUFACTURER, ESSENTIAL_ENTITY, FINANCIAL_ENTITY, PROVIDER |
| OBL-D-01.2-001 | Data crossing network boundaries protected by confidentiality mechanisms appropriate to channel classification | GDPR-C15, CRA-C08, DORA-C10 | D-01.2 | 2.667 | CONTINUOUS | CONTROLLER, PROCESSOR, MANUFACTURER, FINANCIAL_ENTITY |
| OBL-D-01.3-001 | Implement secure cryptographic key management with authentication, integrity verification, and key lifecycle controls | CRA-C15, DORA-C17 | D-01.3 | 3.000 | CONTINUOUS | MANUFACTURER, FINANCIAL_ENTITY |
| OBL-D-01.4-001 | Protect data against unauthorised manipulation, accidental loss, and ensure resilience of AI systems | GDPR-C05, CRA-C09, AI-C18 | D-01.4 | 2.667 | CONTINUOUS | CONTROLLER, MANUFACTURER, PROVIDER |

**D-01 Summary:** 4 obligations | Avg NI: 2.750 | All CONTINUOUS | 5-regulation coverage for D-01.1

---

### D-02: Vulnerability Management Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty(ies) |
|---------------|------------------------|----------------|------------|-----|----------------|---------------------|
| OBL-D-02.1-001 | Deliver systems with no known exploitable vulnerabilities; maintain vulnerability tracking; ensure AI data governance and accuracy | CRA-C01, CRA-C17, NIS2-C12, DORA-C08, AI-C03, AI-C16 | D-02.1 | 3.000 | ONE_TIME, CONTINUOUS | MANUFACTURER, ESSENTIAL_ENTITY, FINANCIAL_ENTITY, PROVIDER |
| OBL-D-02.2-001 | Enable automatic security updates; remediate vulnerabilities promptly; maintain patch management processes | CRA-C04, CRA-C19, NIS2-C12, DORA-C13 | D-02.2 | 3.000 | ONE_TIME, TRIGGERED, CONTINUOUS | MANUFACTURER, ESSENTIAL_ENTITY, FINANCIAL_ENTITY |
| OBL-D-02.3-001 | Publish coordinated vulnerability disclosure policy; report severe incidents to ENISA/CSIRT within regulatory timelines | CRA-C21, CRA-C26 | D-02.3 | 3.000 | CONTINUOUS, TRIGGERED | MANUFACTURER |
| OBL-D-02.4-001 | Conduct threat-led penetration testing (TLPT); test AI data for biases and errors; perform vulnerability scanning | DORA-C27, DORA-C29, AI-C04 | D-02.4 | 3.000 | PERIODIC | FINANCIAL_ENTITY, PROVIDER |

**D-02 Summary:** 4 obligations | Avg NI: 3.000 | All mandatory | DORA + AI Act add unique obligations

---

### D-03: Access Control Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty(ies) |
|---------------|------------------------|----------------|------------|-----|----------------|---------------------|
| OBL-D-03.1-001 | Implement authentication, identity lifecycle, and access control measures for all users with appropriate oversight competence | CRA-C05, NIS2-C16, NIS2-C19, DORA-C11, DORA-C15, AI-C15 | D-03.1 | 3.000 | CONTINUOUS, ONE_TIME | MANUFACTURER, ESSENTIAL_ENTITY, FINANCIAL_ENTITY, PROVIDER |
| OBL-D-03.2-001 | Enable multi-factor authentication for all privileged and remote access | CRA-C06, NIS2-C17, DORA-C16 | D-03.2 | 3.000 | CONTINUOUS, ONE_TIME | MANUFACTURER, ESSENTIAL_ENTITY, FINANCIAL_ENTITY |
| OBL-D-03.3-001 | Restrict access to authorised personnel only; enforce least privilege principle | GDPR-C10, GDPR-C17, NIS2-C20, DORA-C14 | D-03.3 | 3.000 | ONE_TIME, CONTINUOUS | CONTROLLER, PROCESSOR, ESSENTIAL_ENTITY, FINANCIAL_ENTITY |
| OBL-D-03.4-001 | Disable unused ports/services; no default passwords; secure default configuration | CRA-C03 | D-03.4 | 3.000 | ONE_TIME | MANUFACTURER (Sole Authority) |

**D-03 Summary:** 4 obligations | Avg NI: 3.000 | All mandatory | D-03.4 = CRA sole authority

---

### D-04: Incident Response Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty(ies) | Activation Nature |
|---------------|------------------------|----------------|------------|-----|----------------|---------------------|-------------------|
| OBL-D-04.1-001 | Design systems to limit severity of exploits; implement fail-safe mechanisms, incident detection, and triage capabilities | CRA-C13, NIS2-C28, DORA-C18, DORA-C21 | D-04.1 | 3.000 | ONE_TIME, CONTINUOUS, TRIGGERED | MANUFACTURER, ESSENTIAL_ENTITY, FINANCIAL_ENTITY | STRUCTURAL (always active) |
| OBL-D-04.2-001 | Restore availability after incidents; build resilience against DoS attacks; implement business continuity, containment, and disaster recovery | GDPR-C18, CRA-C11, NIS2-C05, DORA-C19, DORA-C22, DORA-C24 | D-04.2 | 3.000 | TRIGGERED, CONTINUOUS | CONTROLLER, PROCESSOR, MANUFACTURER, ESSENTIAL_ENTITY, FINANCIAL_ENTITY | STRUCTURAL (always active) |
| OBL-D-04.3-001 | Notify supervisory authorities within regulatory-specific timelines: 72h (GDPR), 24h early warning (NIS 2), 24h initial (DORA), 24h (CRA); comply with market surveillance and database registration (AI Act) | GDPR-C21, GDPR-C23, CRA-C25, NIS2-C25, NIS2-C26, NIS2-C27, DORA-C35, DORA-C36, DORA-C37, AI-C26, AI-C29 | D-04.3 | 3.000 | TRIGGERED | CONTROLLER, PROCESSOR, MANUFACTURER, ESSENTIAL_ENTITY, FINANCIAL_ENTITY, PROVIDER | **CONTEXTUAL** — GDPR triggers on personal data breach; CRA triggers on exploited vulnerability; NIS 2 triggers on significant incident; DORA triggers on ICT-related incident; AI Act triggers on serious AI incident. All activate simultaneously only in compound event (EVT-001). See TENSION-H-001. |
| OBL-D-04.4-001 | Ensure ongoing availability and ability to restore data after incident; implement recovery procedures and backup systems | GDPR-C16, NIS2-C06, DORA-C23, DORA-C25 | D-04.4 | 3.000 | CONTINUOUS, TRIGGERED | CONTROLLER, PROCESSOR, ESSENTIAL_ENTITY, FINANCIAL_ENTITY | STRUCTURAL (always active) |

**D-04 Summary:** 4 obligations | Avg NI: 3.000 | All mandatory | **1 contextual (OBL-D-04.3-001)** | **CRITICAL TENSION T-001 / TENSION-H-001:** D-04.3 has 5 different notification timelines — only active when compound event occurs

**Nuance — Processor Breach Notification (GDPR Art. 33(2)):** OmniBank's cloud providers and payment processors (acting as processors) must notify OmniBank (controller) of personal data breaches "without undue delay" — a distinct obligation from OmniBank's 72h notification to the supervisory authority. The processor→controller clock has no fixed numeric deadline. This should be contractually defined in DPAs (e.g., within 4-8 hours). OBL-D-04.3-001 captures the controller's regulatory notifications but not the downstream processor→controller notification.

---

### D-05: Data Lifecycle Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty(ies) | Activation Nature |
|---------------|------------------------|----------------|------------|-----|----------------|---------------------|-------------------|
| OBL-D-05.1-001 | Process only data adequate, relevant and limited to what is necessary; ensure AI training data relevance and representativeness | GDPR-C01, CRA-C10, AI-C05, AI-C06 | D-05.1 | 3.000 | CONTINUOUS, ONE_TIME | CONTROLLER, MANUFACTURER, PROVIDER | STRUCTURAL (always active) |
| OBL-D-05.2-001 | Do not keep personal data longer than necessary; manage AI data retention per regulatory requirements | GDPR-C02, GDPR-C03, AI-C07 | D-05.2 | 3.000 | CONTINUOUS | CONTROLLER, PROVIDER | STRUCTURAL (always active) |
| OBL-D-05.3-001 | Enable complete and secure data deletion on user request; ensure secure permanent data removal from products | GDPR-C06, CRA-C16 | D-05.3 | 3.000 | TRIGGERED, ONE_TIME | CONTROLLER, PROCESSOR, MANUFACTURER | **CONTEXTUAL** — GDPR Art.17 erasure trigger vs DORA Art.11/19 immutable log retention. Both obligations run concurrently; tension activates when customer requests erasure of data in DORA-mandated audit logs. See TENSION-H-002. |
| OBL-D-05.4-001 | Provide data export in structured, machine-readable format on request | GDPR-C07 | D-05.4 | 3.000 | TRIGGERED | CONTROLLER (Sole Authority) | STRUCTURAL (always active) |

**D-05 Summary:** 4 obligations | Avg NI: 3.000 | All mandatory | **1 contextual (OBL-D-05.3-001)** | **CRITICAL TENSION T-002 / TENSION-H-002:** GDPR erasure vs DORA immutable log retention

---

### D-06: Supply Chain Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty(ies) |
|---------------|------------------------|----------------|------------|-----|----------------|---------------------|
| OBL-D-06.1-001 | Use only processors/providers providing sufficient guarantees; conduct vendor risk assessments, due diligence, and manage third-party ICT risk | GDPR-C11, NIS2-C08, NIS2-C23, DORA-C30, DORA-C32 | D-06.1 | 3.000 | ONE_TIME, CONTINUOUS | CONTROLLER, PROCESSOR, ESSENTIAL_ENTITY, FINANCIAL_ENTITY |
| OBL-D-06.2-001 | Document all third-party components in machine-readable format (SBOM) | CRA-C18 | D-06.2 | 3.000 | CONTINUOUS | MANUFACTURER (Sole Authority) |
| OBL-D-06.3-001 | Bind processors and suppliers to security obligations via contractual safeguards and Data Processing Agreements | GDPR-C12, NIS2-C09, DORA-C31 | D-06.3 | 3.000 | ONE_TIME, CONTINUOUS | CONTROLLER, PROCESSOR, ESSENTIAL_ENTITY, FINANCIAL_ENTITY |
| OBL-D-06.4-001 | Manage third-party boundaries with exit strategies and concentration risk monitoring | NIS2-C24, DORA-C33, DORA-C34 | D-06.4 | 3.000 | ONE_TIME, CONTINUOUS | ESSENTIAL_ENTITY, FINANCIAL_ENTITY |

**D-06 Summary:** 4 obligations | Avg NI: 3.000 | All mandatory | D-06.2 = CRA sole authority

---

### D-07: Secure Development Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty(ies) | Activation Nature |
|---------------|------------------------|----------------|------------|-----|----------------|---------------------|-------------------|
| OBL-D-07.1-001 | Integrate data protection and security into design from outset; secure by default; implement manufacturer and provider obligations | GDPR-C09, CRA-C02, CRA-C22 | D-07.1 | 2.667 | ONE_TIME | CONTROLLER, MANUFACTURER | STRUCTURAL (always active) |
| OBL-D-07.2-001 | Implement secure coding practices per organizational standards | NIS2-C11, DORA-C20 | D-07.2 | 3.000 | CONTINUOUS | ESSENTIAL_ENTITY, FINANCIAL_ENTITY | STRUCTURAL (always active) |
| OBL-D-07.3-001 | Secure CI/CD pipeline with automated security testing and controls | NIS2-C11, DORA-C20 | D-07.3 | 3.000 | CONTINUOUS | ESSENTIAL_ENTITY, FINANCIAL_ENTITY | STRUCTURAL (always active) |
| OBL-D-07.4-001 | Implement formal change management processes with regulatory oversight | NIS2-C10, DORA-C06 | D-07.4 | 3.000 | CONTINUOUS | ESSENTIAL_ENTITY, FINANCIAL_ENTITY | STRUCTURAL (always active) |

**D-07 Summary:** 4 obligations | Avg NI: 2.917 | All mandatory | All structural | **Tension T-004:** D-07.1 intensity gap (GDPR NI=2 vs CRA NI=3)

**Nuance — CRA Support Period (Art. 13(8)):** The CRA requires a minimum **5-year support period** for OmniBank's mobile banking app. Each app version has its own 5-year support clock for security patches and vulnerability fixes. Captured under existing CRA clauses but the 5-year threshold is a concrete milestone.

**Nuance — CRA Security Update Retention (Art. 13(9)):** Security updates must remain available for **10 years** or the support period, whichever is longer. Old app versions' patches must be accessible for a decade.

---

### D-08: Human Factors Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty(ies) |
|---------------|------------------------|----------------|------------|-----|----------------|---------------------|
| OBL-D-08.1-001 | Train staff involved in processing operations on security awareness annually | GDPR-C27, NIS2-C14 | D-08.1 | 3.000 | PERIODIC | CONTROLLER, PROCESSOR, ESSENTIAL_ENTITY |
| OBL-D-08.2-001 | Provide role-specific security competence training; ensure AI human oversight competence; maintain staff competence | GDPR-C28, NIS2-C15, AI-C14, AI-C24 | D-08.2 | 3.000 | PERIODIC, CONTINUOUS, ONE_TIME | CONTROLLER, PROCESSOR, ESSENTIAL_ENTITY, PROVIDER |
| OBL-D-08.3-001 | Ensure management board receives security training and oversees ICT risk management | NIS2-C02, DORA-C02 | D-08.3 | 3.000 | PERIODIC, CONTINUOUS | ESSENTIAL_ENTITY, FINANCIAL_ENTITY |

**D-08 Summary:** 3 obligations | Avg NI: 3.000 | All mandatory | NIS 2 + DORA board obligations

---

### D-09: Governance & Documentation Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty(ies) | Activation Nature |
|---------------|------------------------|----------------|------------|-----|----------------|---------------------|-------------------|
| OBL-D-09.1-001 | Implement comprehensive information security policies, ICT risk management framework, technical documentation, transparency information, quality management systems, and maintain documentation for regulatory periods | GDPR-C08, GDPR-C25, GDPR-C26, CRA-C24, NIS2-C01, NIS2-C03, DORA-C01, DORA-C03, AI-C08, AI-C12, AI-C13, AI-C20, AI-C23 | D-09.1 | 2.917 | CONTINUOUS, ONE_TIME | ALL 5 parties | STRUCTURAL (always active) |
| OBL-D-09.2-001 | Conduct unified risk assessments: DPIA (GDPR), cybersecurity risk assessment (CRA), incident handling (NIS 2), ICT risk assessment (DORA), AI risk management system and fundamental rights impact assessment (AI Act) | GDPR-C20, GDPR-C24, CRA-C23, NIS2-C04, DORA-C04, AI-C01, AI-C02, AI-C22, AI-C28 | D-09.2 | 3.000 | PERIODIC, ONE_TIME, CONTINUOUS, TRIGGERED | ALL 5 parties | STRUCTURAL (always active — all 5 assessment triggers permanently satisfied by bank's business model) |
| OBL-D-09.3-001 | Maintain asset and ICT asset inventories | NIS2-C07, DORA-C05 | D-09.3 | 3.000 | CONTINUOUS | ESSENTIAL_ENTITY, FINANCIAL_ENTITY | STRUCTURAL (always active) |
| OBL-D-09.4-001 | Maintain records of processing activities, breach documentation, AI traceability records, and regulatory record keeping | GDPR-C13, GDPR-C22, DORA-C38, AI-C11 | D-09.4 | 3.000 | CONTINUOUS, TRIGGERED | CONTROLLER, PROCESSOR, FINANCIAL_ENTITY, PROVIDER | STRUCTURAL (always active) |

**D-09 Summary:** 4 obligations | Avg NI: 2.979 | All mandatory | All structural | Highest clause density domain (40 clauses)

**Nuance — DPO Rationale (GDPR Art. 37):** OmniBank does NOT process special category data (Art. 9) — financial data is not a special category. The DPO obligation is triggered under **Art. 37(1)(b)** for large-scale systematic monitoring of customer financial behaviour (transaction monitoring, credit scoring, fraud detection), not under Art. 37(1)(c) for Art. 9 processing. OBL-D-09.1-001 references GDPR-C26 (DPO designation) — the legal basis should be clarified as Art. 37(1)(b).

**Nuance — AI Act Downstream Provider (Art. 25):** If a partner bank white-labels OmniScore AI and deploys it under their own brand, or substantially modifies the model for a different risk assessment purpose, that entity becomes the "provider" with full Art. 16 obligations. OmniBank should include written agreements (Art. 25(4)) with downstream entities specifying information, capabilities, and technical access needed for compliance. This creates AI value chain responsibilities beyond standard supply chain obligations in D-06.

---

### D-10: Monitoring & Audit Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty(ies) | Activation Nature |
|---------------|------------------------|----------------|------------|-----|----------------|---------------------|-------------------|
| OBL-D-10.1-001 | Implement continuous security monitoring, attack surface minimization, AI monitoring systems, and fallback plans | CRA-C12, NIS2-C21, NIS2-C29, DORA-C07, AI-C19, AI-C25 | D-10.1 | 3.000 | CONTINUOUS, ONE_TIME | MANUFACTURER, ESSENTIAL_ENTITY, FINANCIAL_ENTITY, PROVIDER | STRUCTURAL (always active) |
| OBL-D-10.2-001 | Log security-relevant events; maintain immutable audit trails; implement AI automatic logging with retention requirements | CRA-C14, NIS2-C22, DORA-C12, AI-C09, AI-C10 | D-10.2 | 3.000 | CONTINUOUS | MANUFACTURER, ESSENTIAL_ENTITY, FINANCIAL_ENTITY, PROVIDER | **CONTEXTUAL** — GDPR Art.17 erasure trigger vs DORA Art.11/19 immutable log retention. Both obligations run concurrently; tension activates when customer requests erasure of data in DORA-mandated audit logs. See TENSION-H-002. |
| OBL-D-10.3-001 | Regularly test effectiveness of technical and organisational measures; conduct security testing, resilience testing, penetration testing, post-market monitoring, and periodic AI evaluation | GDPR-C19, CRA-C20, NIS2-C13, DORA-C26, DORA-C28, AI-C21, AI-C27 | D-10.3 | 3.000 | PERIODIC, CONTINUOUS | CONTROLLER, PROCESSOR, MANUFACTURER, ESSENTIAL_ENTITY, FINANCIAL_ENTITY, PROVIDER | STRUCTURAL (always active) |

**D-10 Summary:** 3 obligations | Avg NI: 3.000 | All mandatory | **1 contextual (OBL-D-10.2-001)** | **CRITICAL TENSION T-002 / TENSION-H-002:** DORA logging vs GDPR erasure | 5-regulation coverage

---

## 5. TRACEABILITY MATRIX

### 5.1 Full Clause-to-Obligation Mapping

| Obligation ID | Source Regulation | Source Clause ID(s) | Clause NI Count | Derived NI |
|---------------|-------------------|---------------------|-----------------|------------|
| OBL-D-01.1-001 | GDPR | GDPR-C04, GDPR-C14 | 2, 2 | 2.667 |
| | CRA | CRA-C07 | 3 | |
| | NIS 2 | NIS2-C18 | 3 | |
| | DORA | DORA-C09 | 3 | |
| | AI Act | AI-C17 | 3 | |
| OBL-D-01.2-001 | GDPR | GDPR-C15 | 2 | 2.667 |
| | CRA | CRA-C08 | 3 | |
| | DORA | DORA-C10 | 3 | |
| OBL-D-01.3-001 | CRA | CRA-C15 | 3 | 3.000 |
| | DORA | DORA-C17 | 3 | |
| OBL-D-01.4-001 | GDPR | GDPR-C05 | 2 | 2.667 |
| | CRA | CRA-C09 | 3 | |
| | AI Act | AI-C18 | 3 | |
| OBL-D-02.1-001 | CRA | CRA-C01, CRA-C17 | 3, 3 | 3.000 |
| | NIS 2 | NIS2-C12 | 3 | |
| | DORA | DORA-C08 | 3 | |
| | AI Act | AI-C03, AI-C16 | 3, 3 | |
| OBL-D-02.2-001 | CRA | CRA-C04, CRA-C19 | 3, 3 | 3.000 |
| | NIS 2 | NIS2-C12 | 3 | |
| | DORA | DORA-C13 | 3 | |
| OBL-D-02.3-001 | CRA | CRA-C21, CRA-C26 | 3, 3 | 3.000 |
| OBL-D-02.4-001 | DORA | DORA-C27, DORA-C29 | 3, 3 | 3.000 |
| | AI Act | AI-C04 | 3 | |
| OBL-D-03.1-001 | CRA | CRA-C05 | 3 | 3.000 |
| | NIS 2 | NIS2-C16, NIS2-C19 | 3, 3 | |
| | DORA | DORA-C11, DORA-C15 | 3, 3 | |
| | AI Act | AI-C15 | 3 | |
| OBL-D-03.2-001 | CRA | CRA-C06 | 2 | 3.000 |
| | NIS 2 | NIS2-C17 | 3 | |
| | DORA | DORA-C16 | 3 | |
| OBL-D-03.3-001 | GDPR | GDPR-C10, GDPR-C17 | 3, 3 | 3.000 |
| | NIS 2 | NIS2-C20 | 3 | |
| | DORA | DORA-C14 | 3 | |
| OBL-D-03.4-001 | CRA | CRA-C03 | 3 | 3.000 |
| OBL-D-04.1-001 | CRA | CRA-C13 | 3 | 3.000 |
| | NIS 2 | NIS2-C28 | 3 | |
| | DORA | DORA-C18, DORA-C21 | 3, 3 | |
| OBL-D-04.2-001 | GDPR | GDPR-C18 | 2 | 3.000 |
| | CRA | CRA-C11 | 3 | |
| | NIS 2 | NIS2-C05 | 3 | |
| | DORA | DORA-C19, DORA-C22, DORA-C24 | 3, 3, 3 | |
| OBL-D-04.3-001 | GDPR | GDPR-C21, GDPR-C23 | 3, 3 | 3.000 |
| | CRA | CRA-C25 | 3 | |
| | NIS 2 | NIS2-C25, NIS2-C26, NIS2-C27 | 3, 3, 3 | |
| | DORA | DORA-C35, DORA-C36, DORA-C37 | 3, 3, 3 | |
| | AI Act | AI-C26, AI-C29 | 3, 3 | |
| OBL-D-04.4-001 | GDPR | GDPR-C16 | 2 | 3.000 |
| | NIS 2 | NIS2-C06 | 3 | |
| | DORA | DORA-C23, DORA-C25 | 3, 3 | |
| OBL-D-05.1-001 | GDPR | GDPR-C01 | 3 | 3.000 |
| | CRA | CRA-C10 | 3 | |
| | AI Act | AI-C05, AI-C06 | 3, 3 | |
| OBL-D-05.2-001 | GDPR | GDPR-C02, GDPR-C03 | 3, 3 | 3.000 |
| | AI Act | AI-C07 | 3 | |
| OBL-D-05.3-001 | GDPR | GDPR-C06 | 3 | 3.000 |
| | CRA | CRA-C16 | 3 | |
| OBL-D-05.4-001 | GDPR | GDPR-C07 | 3 | 3.000 |
| OBL-D-06.1-001 | GDPR | GDPR-C11 | 3 | 3.000 |
| | NIS 2 | NIS2-C08, NIS2-C23 | 3, 3 | |
| | DORA | DORA-C30, DORA-C32 | 3, 3 | |
| OBL-D-06.2-001 | CRA | CRA-C18 | 3 | 3.000 |
| OBL-D-06.3-001 | GDPR | GDPR-C12 | 3 | 3.000 |
| | NIS 2 | NIS2-C09 | 3 | |
| | DORA | DORA-C31 | 3 | |
| OBL-D-06.4-001 | NIS 2 | NIS2-C24 | 3 | 3.000 |
| | DORA | DORA-C33, DORA-C34 | 3, 3 | |
| OBL-D-07.1-001 | GDPR | GDPR-C09 | 2 | 2.667 |
| | CRA | CRA-C02, CRA-C22 | 3, 3 | |
| OBL-D-07.2-001 | NIS 2 | NIS2-C11 | 3 | 3.000 |
| | DORA | DORA-C20 | 3 | |
| OBL-D-07.3-001 | NIS 2 | NIS2-C11 | 3 | 3.000 |
| | DORA | DORA-C20 | 3 | |
| OBL-D-07.4-001 | NIS 2 | NIS2-C10 | 3 | 3.000 |
| | DORA | DORA-C06 | 3 | |
| OBL-D-08.1-001 | GDPR | GDPR-C27 | 3 | 3.000 |
| | NIS 2 | NIS2-C14 | 3 | |
| OBL-D-08.2-001 | GDPR | GDPR-C28 | 3 | 3.000 |
| | NIS 2 | NIS2-C15 | 3 | |
| | AI Act | AI-C14, AI-C24 | 3, 3 | |
| OBL-D-08.3-001 | NIS 2 | NIS2-C02 | 3 | 3.000 |
| | DORA | DORA-C02 | 3 | |
| OBL-D-09.1-001 | GDPR | GDPR-C08, GDPR-C25, GDPR-C26 | 2, 3, 2 | 2.917 |
| | CRA | CRA-C24 | 3 | |
| | NIS 2 | NIS2-C01, NIS2-C03 | 3, 3 | |
| | DORA | DORA-C01, DORA-C03 | 3, 3 | |
| | AI Act | AI-C08, AI-C12, AI-C13, AI-C20, AI-C23 | 3, 3, 3, 3, 3 | |
| OBL-D-09.2-001 | GDPR | GDPR-C20, GDPR-C24 | 2, 3 | 3.000 |
| | CRA | CRA-C23 | 3 | |
| | NIS 2 | NIS2-C04 | 3 | |
| | DORA | DORA-C04 | 3 | |
| | AI Act | AI-C01, AI-C02, AI-C22, AI-C28 | 3, 3, 3, 3 | |
| OBL-D-09.3-001 | NIS 2 | NIS2-C07 | 3 | 3.000 |
| | DORA | DORA-C05 | 3 | |
| OBL-D-09.4-001 | GDPR | GDPR-C13, GDPR-C22 | 3, 3 | 3.000 |
| | DORA | DORA-C38 | 3 | |
| | AI Act | AI-C11 | 3 | |
| OBL-D-10.1-001 | CRA | CRA-C12 | 3 | 3.000 |
| | NIS 2 | NIS2-C21, NIS2-C29 | 3, 3 | |
| | DORA | DORA-C07 | 3 | |
| | AI Act | AI-C19, AI-C25 | 3, 3 | |
| OBL-D-10.2-001 | CRA | CRA-C14 | 3 | 3.000 |
| | NIS 2 | NIS2-C22 | 3 | |
| | DORA | DORA-C12 | 3 | |
| | AI Act | AI-C09, AI-C10 | 3, 3 | |
| OBL-D-10.3-001 | GDPR | GDPR-C19 | 3 | 3.000 |
| | CRA | CRA-C20 | 2 | |
| | NIS 2 | NIS2-C13 | 3 | |
| | DORA | DORA-C26, DORA-C28 | 3, 3 | |
| | AI Act | AI-C21, AI-C27 | 3, 3 | |

---

## 6. NORMATIVE INTENSITY PROPAGATION

| Obligation ID | Source Clause NIs | Clause Count | Derived NI | Propagation Rule |
|---------------|-------------------|--------------|------------|------------------|
| OBL-D-01.1-001 | 2, 2, 3, 3, 3, 3 | 6 | 2.667 | AVG |
| OBL-D-01.2-001 | 2, 3, 3 | 3 | 2.667 | AVG |
| OBL-D-01.3-001 | 3, 3 | 2 | 3.000 | AVG |
| OBL-D-01.4-001 | 2, 3, 3 | 3 | 2.667 | AVG |
| OBL-D-02.1-001 | 3, 3, 3, 3, 3, 3 | 6 | 3.000 | AVG |
| OBL-D-02.2-001 | 3, 3, 3, 3 | 4 | 3.000 | AVG |
| OBL-D-02.3-001 | 3, 3 | 2 | 3.000 | AVG |
| OBL-D-02.4-001 | 3, 3, 3 | 3 | 3.000 | AVG |
| OBL-D-03.1-001 | 3, 3, 3, 3, 3, 3 | 6 | 3.000 | AVG |
| OBL-D-03.2-001 | 2, 3, 3 | 3 | 2.667 | AVG |
| OBL-D-03.3-001 | 3, 3, 3, 3 | 4 | 3.000 | AVG |
| OBL-D-03.4-001 | 3 | 1 | 3.000 | Single source |
| OBL-D-04.1-001 | 3, 3, 3, 3 | 4 | 3.000 | AVG |
| OBL-D-04.2-001 | 2, 3, 3, 3, 3, 3 | 6 | 2.833 | AVG |
| OBL-D-04.3-001 | 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 | 11 | 3.000 | AVG |
| OBL-D-04.4-001 | 2, 3, 3, 3 | 4 | 2.750 | AVG |
| OBL-D-05.1-001 | 3, 3, 3, 3 | 4 | 3.000 | AVG |
| OBL-D-05.2-001 | 3, 3, 3 | 3 | 3.000 | AVG |
| OBL-D-05.3-001 | 3, 3 | 2 | 3.000 | AVG |
| OBL-D-05.4-001 | 3 | 1 | 3.000 | Single source |
| OBL-D-06.1-001 | 3, 3, 3, 3, 3 | 5 | 3.000 | AVG |
| OBL-D-06.2-001 | 3 | 1 | 3.000 | Single source |
| OBL-D-06.3-001 | 3, 3, 3 | 3 | 3.000 | AVG |
| OBL-D-06.4-001 | 3, 3, 3 | 3 | 3.000 | AVG |
| OBL-D-07.1-001 | 2, 3, 3 | 3 | 2.667 | AVG |
| OBL-D-07.2-001 | 3, 3 | 2 | 3.000 | AVG |
| OBL-D-07.3-001 | 3, 3 | 2 | 3.000 | AVG |
| OBL-D-07.4-001 | 3, 3 | 2 | 3.000 | AVG |
| OBL-D-08.1-001 | 3, 3 | 2 | 3.000 | AVG |
| OBL-D-08.2-001 | 3, 3, 3, 3 | 4 | 3.000 | AVG |
| OBL-D-08.3-001 | 3, 3 | 2 | 3.000 | AVG |
| OBL-D-09.1-001 | 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 | 13 | 2.846 | AVG |
| OBL-D-09.2-001 | 2, 3, 3, 3, 3, 3, 3, 3, 3 | 9 | 2.889 | AVG |
| OBL-D-09.3-001 | 3, 3 | 2 | 3.000 | AVG |
| OBL-D-09.4-001 | 3, 3, 3, 3 | 4 | 3.000 | AVG |
| OBL-D-10.1-001 | 3, 3, 3, 3, 3, 3 | 6 | 3.000 | AVG |
| OBL-D-10.2-001 | 3, 3, 3, 3, 3 | 5 | 3.000 | AVG |
| OBL-D-10.3-001 | 3, 2, 3, 3, 3, 3, 3 | 7 | 2.857 | AVG |

**NI Distribution:**
- Weight 3.000 Obligations: 29 (76.3%)
- Weight 2.667-2.889 Obligations: 8 (21.1%)
- Weight <2.667 Obligations: 1 (2.6%)
- **Mean NI across all 38 obligations:** 2.934

---

## 7. OBLIGATION TYPE DISTRIBUTION

| obligationType | Count | Percentage | Example Obligations |
|----------------|-------|------------|---------------------|
| CONTINUOUS | 22 | 57.9% | OBL-D-01.1-001, OBL-D-02.1-001, OBL-D-10.1-001 |
| TRIGGERED | 10 | 26.3% | OBL-D-04.3-001, OBL-D-05.3-001, OBL-D-05.4-001 |
| ONE_TIME | 11 | 28.9% | OBL-D-03.4-001, OBL-D-07.1-001 |
| PERIODIC | 5 | 13.2% | OBL-D-02.4-001, OBL-D-08.1-001, OBL-D-10.3-001 |

**Note:** Obligations have mixed types (e.g., OBL-D-02.1-001 has ONE_TIME + CONTINUOUS). Total > 38 due to multi-type obligations.

---

## 8. REGULATORY CONTRIBUTION ANALYSIS

| Regulation | Clauses Contributed | Obligations Involved | % of Total Obligations | Dominant Sub-Domains |
|------------|---------------------|---------------------|----------------------|---------------------|
| **GDPR** | 28 | 12 | 31.6% | D-05, D-09, D-03 |
| **CRA** | 26 | 18 | 47.4% | D-02, D-03, D-07 |
| **NIS 2** | 29 | 24 | 63.2% | D-04, D-07, D-08 |
| **DORA** | 38 | 29 | 76.3% | D-06, D-09, D-10 |
| **AI Act** | 29 | 13 | 34.2% | D-09, D-02, D-10 |

**DORA dominates** with 38 clauses (25.3% of total) covering 29/38 obligations (76.3%).

---

## 9. DERIVATION GAPS

| Gap ID | Source | Gap Description | Impact | Recommended Action |
|--------|--------|-----------------|--------|-------------------|
| DERIV-GAP-001 | None | ALL 38 sub-domains covered — zero gaps | None | No action required |
| DERIV-GAP-002 | D-03.4, D-05.4, D-06.2 | Sole authority sub-domains (single regulation) | Regulatory risk if that regulation excluded | Document as critical dependency; monitor regulatory changes |

---

## 10. KEY OBSERVATIONS

1. **Maximum Derivation Density:** 150 clauses consolidated into 38 obligations (3.95:1 ratio) — higher consolidation than TinyTask (2.35:1) due to multi-regulation overlap in all sub-domains.

2. **100% Sub-Domain Coverage:** All 38 sub-domains have at least one obligation — this is the maximum possible coverage in the AEGIS methodology.

3. **DORA Dominance:** DORA contributes the most clauses (38, 25.3%) and covers the most obligations (29/38, 76.3%). All DORA clauses are Weight 3 (unconditional mandatory).

4. **No Derivation Gaps:** Unlike lower-complexity cases, OmniBank has zero uncovered sub-domains. This eliminates the need for best-practice supplementation at the obligation level.

5. **Four Strategic Tensions Identified:**
   - **T-001 (CRITICAL):** D-04.3 — 5 different notification timelines (GDPR 72h, CRA 24h, NIS 2 24h/72h, DORA 24h/72h, AI Act continuous)
   - **T-002 (CRITICAL):** D-05.3 vs D-10.2 — GDPR erasure vs AI Act/DORA immutable log retention
   - **T-003 (MEDIUM):** D-09.2 — DPIA vs FRIA trigger mismatch
   - **T-004 (LOW):** D-07.1 — GDPR NI=2 vs CRA NI=3 intensity gap

6. **Sole Authority Obligations:** 3 sub-domains have single-regulation coverage:
   - D-03.4 (CRA only) — secure default configuration
   - D-05.4 (GDPR only) — data portability
   - D-06.2 (CRA only) — SBOM

7. **Highest Clause Density:** D-09.1 (13 clauses from all 5 regulations), D-04.3 (11 clauses from all 5 regulations), D-09.2 (9 clauses from all 5 regulations).

---

## 11. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-03 | Compliance Lead | Initial release - OmniBank Financial Systems case (38 obligations derived from 150 clauses) |
| 1.1 | 2026-04-11 | Compliance Lead | CR-02: Corrected GDPR Art. 37 DPO rationale to Art. 37(1)(b) systematic monitoring (not Art. 9) (D-09); MD-01: Added GDPR Art. 33(2) "without undue delay" processor→controller nuance (D-04); MD-03: Added CRA Art. 13(8) 5-year support + Art. 13(9) 10-year update retention (D-07); MD-06: Added AI Act Art. 25 downstream provider obligations (D-09) |

---

## 12. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-03 |
| Technical Review (CTO) | | | |
| Security Review (CISO) | | | |
| Compliance Review (CRO) | | | |
| AEGIS Methodology Review | | | |

---

**Next Document:** Doc17_Strategic_Tensions_Report.md
**Phase 2 Step:** B ✅ COMPLETE
