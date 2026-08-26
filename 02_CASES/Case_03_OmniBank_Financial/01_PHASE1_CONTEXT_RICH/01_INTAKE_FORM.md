---
document_id: AEGIS-P3-RICH-01-INTAKE
title: AEGIS Intake Form — Company Context Assessment (Rich Mode)
phase: 1
version: 2.1
created: 2026-04-01
updated: 2026-08-06
author: Compliance Lead (Sprint 1 reconciliation copy)
status: RECONCILED
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
inactive_documented: []
traceability: AEGIS Class Model → CompanyContext class
inputs: []
outputs: [04_Company_Context_Assessment.md, 05_Regulatory_Applicability.md]
related_documents: [00_Taxonomy_Reference.md, 02_Regulatory_Mapping_Master.xlsx]
supersedes: 01_Company_Context_LEGACY.md
sibling_of: ../../00_COMMON/01_Company_Context.md
reconciliation_notes:
  - "Sprint 1 (2026-08-06): Copied from 00_COMMON/01_Company_Context.md → Rich folder as 01_INTAKE_FORM.md; frontmatter migrated to AEGIS-P3-RICH-* prefix; status DRAFT → RECONCILED; active_subdomains confirmed = 38 (Case_03 MAX). Body unchanged — layered intake format (Layer 0/1/2/3) preserved verbatim."
---

<!-- RECONCILED (Sprint 1, 2026-08-06): Document copied from legacy 00_COMMON/01_Company_Context.md to Rich folder, renamed 01_INTAKE_FORM.md (canonical filename pattern for Phase 1).
Changes: (a) document_id migrated to AEGIS-P3-RICH-01-INTAKE (P3 = Case_03 prefix); (b) status DRAFT → RECONCILED;
(c) active_subdomains: 38 confirmed for Case_03 MAX; (d) Layer 0/1/2/3 intake format preserved (38 questions, 8 conditional blocks, 4 interaction scans).
Body content unchanged — intake form is canonical and frozen at v2.0.
-->

---

# AEGIS Intake Form — Company Context Assessment

## CHANGELOG

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2026-04-23 | Converted to layered intake format — Layer 0 (Company Profile), Layer 1 (Decision Tree), Layer 2 (Conditional Blocks) |
| 1.0 | 2026-04-01 | Initial release - OmniBank Financial Systems case |

---

## 1. PURPOSE

This document is the **structured intake form** for AEGIS Phase 1. It captures company facts through a layered approach: Layer 0 (static profile), Layer 1 (regulatory decision tree), Layer 2 (conditional questions based on applicability).

**Gate Criteria:**
- [x] Layer 0 (Company Profile) complete
- [x] Layer 1 (Regulatory Decision Tree) completed for all 5 regulations
- [x] Layer 2 (Conditional Blocks) answered based on trigger conditions
- [x] Layer 3 (Regulatory Interaction Scans) completed
- [x] complexityTier derived and recorded

---

## 2. LAYER 0 — COMPANY PROFILE

**Purpose:** Capture foundational company facts that determine regulatory applicability.

### 2.1 Basic Information

| Field | Value | Notes |
|-------|-------|-------|
| Company Legal Name | OmniBank Financial Systems S.A. | |
| Registration Country | Germany (EU) | |
| HQ Location | Frankfurt, Germany | |
| Legal Structure | Société Anonyme (S.A.) | German/French corporate structure |
| Website / Contact | info@omnibank.eu | Consumer credit and risk management |

### 2.2 Size Classification

| Field | Value | Threshold Check |
|-------|-------|----------------|
| Number of Employees | 5,000+ | >250 = Large, >50 = Medium, ≤50 = Small |
| Annual Revenue (EUR) | >€1.5B | >€50M = Large, >€10M = Medium, ≤€10M = Small |
| EU Size Classification | Large | Per EU recommendation 2003/361 |

### 2.3 Business Sector

| Field | Value | Regulatory Relevance |
|-------|-------|---------------------|
| Primary Industry Sector | Banking and Financial Services | NIS 2 Annex I — Essential sector; DORA Art. 2 — Financial entity |
| Secondary Sectors (if any) | None | |
| Service Criticality | **Essential** | Financial infrastructure; systemic importance |

---

## 3. LAYER 1 — REGULATORY DECISION TREE

**Purpose:** Determine which regulations apply through branching logic.

### 3.1 GDPR Applicability

```
START: Does the company process personal data of EU residents?
├── YES ──────────────────┐
│  Customer PII, financial data, credit scores │
│                        │
│  Is the processing      │
│  purely local/household│
│  activity?             │
│  ├── YES → GDPR: NOT  │
│  │     APPLICABLE     │
│  └── NO ──────────────→ GDPR: APPLICABLE
│                        │
└── NO → GDPR: NOT APPLICABLE
```

| Decision Point | Answer | GDPR Applicable? |
|----------------|--------|-----------------|
| Processes EU resident personal data? | YES | Customer PII, financial transactions, credit scores |
| Any exemption (household/individual)? | NO | Commercial financial services operations |

**GDPR Roles:**
- **CONTROLLER** (for customer data, credit decisions)
- **PROCESSOR** (for regulatory reporting to BaFin/ECB)

### 3.2 CRA Applicability

```
START: Does the company place products on the EU market?
├── YES ──────────────────┐
│  Mobile app + web platform │
│                        │
│  Does the product      │
│  have digital         │
│  elements?            │
│  ├── NO → CRA: NOT   │
│  │     APPLICABLE    │
│  └── YES ───────────→ CRA: APPLICABLE
│                        │
│  Product Class?        │
│  ├── Default          │ ← SELECTED
│  ├── Important Class I│
│  ├── Important Class II│
│  └── Critical         │
│
└── NO → CRA: NOT APPLICABLE
```

| Decision Point | Answer | CRA Applicable? |
|----------------|--------|-----------------|
| Places products on EU market? | YES | Mobile app + web platform deployed in EU |
| Product has digital elements? | YES | Digital financial services |
| Product Class | Default | Not critical infrastructure |

**CRA Roles:**
- **MANUFACTURER** (develops mobile app and web platform)

### 3.3 NIS 2 Applicability

```
START: Is the company in a NIS 2 sector?
├── YES ──────────────────┐
│  Banking and Financial  │
│  Services (Annex I)     │
│                        │
│  SIZE THRESHOLDS:      │
│  ├── ≥50 employees →│ YES (5000+)  │
│  └── ANY → NIS 2:    │
│       APPLICABLE      │
│
└── NO → NIS 2: NOT APPLICABLE
```

| Decision Point | Answer | NIS 2 Applicable? |
|----------------|--------|-------------------|
| NIS 2 Sector (Annex I or II)? | YES | Banking and Financial Services |
| Employees ≥50? | YES | 5,000+ employees |
| Entity Type | **ESSENTIAL ENTITY** | Per NIS 2 Art. 2 |

**Result: NIS 2 — APPLICABLE**

### 3.4 DORA Applicability

```
START: Is the company a financial entity?
├── YES ──────────────────┐
│  Credit scoring, fraud  │
│  detection, payments     │
│                        │
│  Art. 2(1) entity?     │
│  (bank, investment,     │
│   insurance, payment,    │
│   crypto, UCITS, AIFM) │
│  ├── YES → DORA:     │
│  │    APPLICABLE      │
│  └── NO → ...         │
│
└── NO → DORA: NOT APPLICABLE
```

| Decision Point | Answer | DORA Applicable? |
|----------------|--------|-----------------|
| Financial entity per Art. 2? | **YES** | Credit institution; payment service provider |
| ICT provider to financial entities? | N/A | Already Art. 2 entity |

**Result: DORA — APPLICABLE**

### 3.5 AI Act Applicability

```
START: Does the company develop/deploy/use AI systems?
├── YES ──────────────────┐
│  Credit scoring AI,     │
│  fraud detection AI     │
│                        │
│  Annex II product?     │
│  ├── YES → High-risk  │
│  │    PROVIDER        │
│  └── NO → Annex III  │
│       use case?        │
│       ├── YES → High  │
│       │    -risk      │
│       │    DEPLOYER   │
│       └── NO → ...    │
│
└── NO → AI Act: NOT APPLICABLE
```

| Decision Point | Answer | AI Act Applicable? |
|----------------|--------|---------------------|
| AI system present? | YES | Credit scoring AI, fraud detection AI |
| Annex II product? | NO | Not an AI-enabled product |
| Annex III use case? | YES | Credit scoring = Annex III (financial access) |

**AI Act Roles:**
- **DEPLOYER** (operates credit scoring AI)
- **PROVIDER** (develops AI models in-house)

### 3.6 APPLICABILITY SUMMARY

| Regulation | Applicable | Confidence | Role(s) | Notes |
|------------|------------|------------|---------|-------|
| GDPR | **YES** | HIGH | CONTROLLER + PROCESSOR | Large-scale processing of PII and financial data |
| CRA | **YES** | HIGH | MANUFACTURER | Default class; mobile app + web platform |
| NIS 2 | **YES** | HIGH | ESSENTIAL ENTITY | Banking sector; 5000+ employees |
| DORA | **YES** | HIGH | FINANCIAL ENTITY | Credit institution per Art. 2 |
| AI Act | **YES** | HIGH | DEPLOYER + PROVIDER | Annex III credit scoring AI |

**Complexity Tier:** MAXIMUM (5/5 regulations applicable)

---

## 4. LAYER 2 — CONDITIONAL QUESTIONS

**Purpose:** Capture additional context based on applicable regulations.

### 4.1 Block Activation Matrix

| Block ID | Trigger Condition | Status | Questions |
|----------|------------------|--------|-----------|
| **B1: AI Governance** | AI Act applicable | **ACTIVATED** | Q39-Q46 |
| **B2: NIS 2 / SOC** | NIS 2 applicable | **ACTIVATED** | Q47-Q52 |
| **B3: DORA Financial** | DORA applicable | **ACTIVATED** | Q53-Q56 |
| **B4: Security Org** | size ≥50 OR maturity ≥Managed | **ACTIVATED** | Q57-Q61 |
| B5: Special Category Data | GDPR + special category data | NOT APPLICABLE | Q62-Q65 |
| B6: Supply Chain | supplyChainVisibility = Low OR hardware | NOT APPLICABLE | Q66-Q68 |
| **B7: CRA Classification** | CRA applicable | **ACTIVATED** | Q69-Q72 |
| **B8: Multi-Actor Roles** | 2+ regulations OR mixed roles | **ACTIVATED** | Q73-Q75 |

**Block Activation Statement:**
> Block B1: **ACTIVATED** — AI Act applicable (Annex III credit scoring AI)
> Block B2: **ACTIVATED** — NIS 2 applicable (Essential Entity, 5000+ employees)
> Block B3: **ACTIVATED** — DORA applicable (Art. 2 financial entity)
> Block B4: **ACTIVATED** — 5000+ employees, securityMaturity = VERY HIGH
> Block B5: NOT APPLICABLE — Financial data not special category under GDPR Art. 9
> Block B6: NOT APPLICABLE — Supply chain visibility = HIGH
> Block B7: **ACTIVATED** — CRA applicable (Default class)
> Block B8: **ACTIVATED** — 5 regulations applicable + mixed controller/processor roles

---

#### BLOCK B1: AI Governance Extension
**Trigger:** AI Act applicable
**Activated:** YES

| Question | Response | Notes |
|----------|----------|-------|
| Q39: AI System Classification | Annex III use case (credit scoring) | AI Act Annex III: credit scoring systems |
| Q40: Verification vs Identification | 1:many identification | Profiling and scoring; not 1:1 verification |
| Q41: Conformity Assessment Procedure | Notified body | High-risk AI requires notified body assessment |
| Q42: Human Oversight Mechanisms | Human review for high-value decisions; automated for standard | Credit decisions above threshold reviewed manually |
| Q43: Post-Market Monitoring Plan | Defined (AI model performance monitoring) | Continuous model drift and fairness monitoring |
| Q44: Prohibited Practices Check (Art. 5) | Confirmed not applicable | Credit scoring not a prohibited AI practice |
| Q45: Downstream Provider Risk | No modifications expected | Mobile app customers; no substantial modifications |
| Q46: AI Risk Management System | Defined | DORA-aligned AI risk management framework |

---

#### BLOCK B2: NIS 2 / SOC Extension
**Trigger:** NIS 2 applicable
**Activated:** YES

| Question | Response | Notes |
|----------|----------|-------|
| Q47: Entity Classification | Essential entity | Financial sector essential entity under NIS 2 |
| Q48: Incident Response Capability | Dedicated team (24/7 SOC + CSIRT) | In-house SOC + dedicated incident response team |
| Q49: Business Continuity Plan | Documented and tested | Tested BCP; BaFin required |
| Q50: Supply Chain Security Management | Formal program | DORA-aligned ICT third-party risk management |
| Q51: Crisis Communication Procedures | Defined | BaFin/ECB notification procedures |
| Q52: Security Operations Center | In-house SOC | 24/7 dedicated security operations center |

---

#### BLOCK B3: DORA Financial Extension
**Trigger:** DORA applicable
**Activated:** YES

| Question | Response | Notes |
|----------|----------|-------|
| Q53: ICT Risk Management Framework | Documented | DORA-aligned ICT risk management framework |
| Q54: Third-Party ICT Provider Register | Maintained | Critical ICT third-party providers documented |
| Q55: Digital Operational Resilience Testing | TLPT conducted | Threat-led penetration testing required |
| Q56: Information Sharing Arrangements | Member of ISAC | Financial sector threat intelligence sharing |

---

#### BLOCK B4: Security Organization Maturity Extension
**Trigger:** size ≥50 employees OR securityMaturity ≥ Managed
**Activated:** YES

| Question | Response | Notes |
|----------|----------|-------|
| Q57: CISO Appointment | Appointed | Dedicated CISO with security organization of 100+ |
| Q58: DPO Appointment | Mandatory appointment | DPO required for large-scale financial data processing |
| Q59: ISO 27001 Scope | Certified | ISO 27001 + PCI-DSS certified |
| Q60: Security Training Program | Formal program | Annual security + regulatory compliance training |
| Q61: Internal Audit Function | Dedicated team | Internal audit team + external auditors |

---

#### BLOCK B7: CRA Classification Extension
**Trigger:** CRA applicable
**Activated:** YES

| Question | Response | Notes |
|----------|----------|-------|
| Q69: CRA Product Class | Default | Mobile app and web platform; not Critical |
| Q70: Conformity Assessment Regime | Self-assessment | Standard digital products; self-assessment applicable |
| Q71: Art. 24 Exclusion Check | Confirmed not excluded | Mobile app with connectivity; not in exclusions |
| Q72: EU Certification Scheme Availability | No scheme | No EU cybersecurity certification scheme for this category |

---

#### BLOCK B8: Multi-Actor Role Resolution Extension
**Trigger:** 2+ regulations applicable AND dataRole = Mixed
**Activated:** YES

| Question | Response | Notes |
|----------|----------|-------|
| Q73: Per-Data-Element Role Assignment | Controller for customer PII; Processor for regulatory reporting | Clear separation per data category |
| Q74: Cross-Regulation Role Implications | CRA=manufacturer; GDPR=controller/processor; DORA=financial entity; AI Act=deployer | Multiple roles across all 5 applicable regulations |
| Q75: Processor Native Compliance | Yes | Processor has direct Art. 32 obligations |

---

## 5. LAYER 3 — REGULATORY INTERACTION SCANS

**Purpose:** Identify conflicts and tensions when 2+ regulations apply.
**Required when:** 5 regulations applicable — **ACTIVE (GDPR + CRA + NIS 2 + DORA + AI Act)**

### 5.1 Scan 1: Temporal Conflict Scan

| Conflict ID | Regulation A | Deadline A | Regulation B | Deadline B | Conflict Type | Resolution Principle |
|-------------|-------------|------------|-------------|------------|---------------|---------------------|
| TC-001 | AI Act Art. 73 | 15 days (standard) | NIS 2 Art. 23 | 24h (incident) | Different triggers | Separate workflows; 24h takes priority |
| TC-002 | AI Act Art. 73 | 2 days (widespread) | DORA Art. 56 | 4h (major incident) | Different severity levels | Severity-based escalation |
| TC-003 | CRA Art. 14 | 24h (vulnerability) | GDPR Art. 33 | 72h (breach) | Same event, different deadlines | Max-SLA: use 24h workflow |

### 5.2 Scan 2: Requirement Conflict Scan

| Conflict ID | Regulation A | Requirement A | Regulation B | Requirement B | Conflict Type | Resolution |
|-------------|-------------|--------------|-------------|--------------|---------------|------------|
| RC-001 | GDPR Art. 17 | Right to erasure | DORA Art. 17 | Immutable logs | Constraint conflict | Financial records exemption; retention requirements override |

### 5.3 Scan 3: Trigger Mismatch Scan

| Conflict ID | Assessment Type | Trigger A | Trigger B | Mismatch | Resolution |
|-------------|----------------|-----------|-----------|----------|------------|
| TM-001 | DPIA / FRIA | GDPR: large-scale | AI Act: high-risk AI | Different scope | Unified DPIA/FRIA approach |
| TM-002 | Risk Assessment | DORA: ICT risk | NIS 2: security risk | Different methodologies | Map DORA framework to NIS 2 |

### 5.4 Scan 4: Negative Analysis Checklist

| Item | Regulation | Provision | Non-Applicability Confirmed? | Rationale |
|------|-----------|-----------|------------------------------|-----------|
| NA-001 | AI Act | Art. 5 (Prohibited) | YES | Credit scoring not a prohibited purpose |
| NA-002 | CRA | Art. 24 (Exclusions) | YES | Mobile app not in exclusion list |
| NA-003 | GDPR | Art. 37 (DPO) | YES | Large-scale financial data processing |
| NA-004 | NIS 2 | Art. 3 (Entity) | YES | Essential entity in banking sector |

### 5.5 Interaction Summary

| Metric | Value |
|--------|-------|
| Applicable Regulations | 5/5 |
| Active Extension Blocks | B1, B2, B3, B4, B7, B8 |
| Temporal Conflicts Identified | 3 |
| Requirement Conflicts Identified | 1 |
| Trigger Mismatches Identified | 2 |
| Negative Analyses Completed | 4/4 |
| **Complexity Tier (Final)** | MAXIMUM |

---

## 6. IMPLEMENTATION READINESS PREVIEW

### 6.1 Client Declaration vs System Verification

| Regulation | Client Declaration | System Check | Final Applicable | Confidence |
|------------|-------------------|--------------|------------------|------------|
| GDPR | YES | processes_personal_data = TRUE | YES | HIGH |
| CRA | YES | Digital product + EU market = TRUE | YES | HIGH |
| NIS 2 | YES | Essential sector + 5000+ employees = TRUE | YES | HIGH |
| DORA | YES | Financial entity per Art. 2 = TRUE | YES | HIGH |
| AI Act | YES | Annex III AI system = TRUE | YES | HIGH |

### 6.2 Implementation Readiness Areas

| Area | Question | Response | Evidence / Notes |
|------|----------|----------|------------------|
| IR-01: Governance | Named security responsible? | YES | Dedicated CISO; security org 100+ |
| IR-02: DPO | DPO appointed/required? | YES | Mandatory for large-scale financial processing |
| IR-03: Incident Response | Incident response capability? | YES | Dedicated team (24/7 SOC + CSIRT) |
| IR-04: Business Continuity | BCP documented? | YES | Documented and tested; BaFin required |
| IR-05: Data Processing Register | Art. 30 register? | YES | Comprehensive register maintained |
| IR-06: Supplier Register | Critical suppliers tracked? | YES | DORA-aligned ICT third-party risk management |
| IR-07: Security Policies | Documented security policies? | YES | ISO 27001 + PCI-DSS; comprehensive |
| IR-08: Training | Security training program? | YES | Annual security + regulatory compliance training |
| IR-09: Access Control | Formal access control policy? | YES | Strict RBAC; logical isolation |
| IR-10: Data Classification | Data classification scheme? | YES | Financial data classification defined |
| IR-11: Asset Inventory | IT asset inventory? | YES | Comprehensive CMDB maintained |
| IR-12: Risk Management | Risk management process? | YES | DORA-aligned ICT risk framework |

### 6.3 Implementation Readiness Summary

| Metric | Count |
|--------|-------|
| Total Areas Assessed | 12 |
| Fully Implemented (YES) | 11 |
| Partially Implemented | 1 |
| Not Implemented (NO) | 0 |
| **Readiness Score** | 11/12 — HIGH |

---

## 7. ROLE MATRIX

| Regulation | Role(s) | Native Obligations | Inherited Obligations | Notes |
|------------|---------|-------------------|----------------------|-------|
| GDPR | CONTROLLER + PROCESSOR | Art. 32 security, Art. 33 breach notification | Via DPA from processors | Large-scale processing of PII |
| CRA | MANUFACTURER | Annex I essential requirements, Art. 13-14 reporting | Via contracts from suppliers | Default class; self-assessment |
| NIS 2 | ESSENTIAL ENTITY | Art. 21 risk management, Art. 23 incident notification | Via DPA from processors | 24h early warning; BaFin/ENISA reporting |
| DORA | FINANCIAL ENTITY | Art. 5-16 ICT risk framework, Art. 17-19 incident reporting | Via contracts from CTPPs | TLPT required; ISAC member |
| AI Act | DEPLOYER + PROVIDER | Art. 9-15 high-risk requirements, Art. 72 post-market | Via Art. 25 agreements | Annex III credit scoring AI |

---

## 8. COMPLEXITY TIER DERIVATION

| Criterion | Threshold | Result |
|-----------|-----------|--------|
| Number of applicable regulations | ≥4 | MAXIMUM (5 regulations) |
| | 2-3 | |
| Active conditional blocks | ≥4 | MAXIMUM (6 blocks: B1,B2,B3,B4,B7,B8) |
| | 2-3 | |
| Regulatory interactions | ≥3 | MAXIMUM (3 temporal + 1 requirement + 2 trigger mismatches) |
| | 1-2 | |

**Final Complexity Tier:** MAXIMUM

---

## 9. GATE CRITERIA

### MAXIMUM Complexity Tier
- [x] Layer 0 complete
- [x] All 5 regulations assessed
- [x] Section 6.1: Client declaration vs system check (all 5 regulations)
- [x] Section 6.2: Implementation Readiness (all 12 areas responded)
- [x] Section 6.3: Readiness Summary calculated
- [x] Layer 1 decision tree completed
- [x] Layer 2: All applicable blocks activated
- [x] Layer 3: All 4 scans required
- [x] Role Matrix with all applicable regulations
- [x] Complexity Tier derived and justified

---

## N. COMPANY CONTEXT CLASS INSTANTIATION

```
CompanyContext {
    companyContextId: "CC-OMNIBANK-2026-001"
    assessmentDate: "2026-04-01"
    version: "2.0"

    sector: "Banking and Financial Services"
    size: "Large (5000+ employees, >€1.5B revenue)"
    processes_personal_data: TRUE
    places_digital_products_eu: TRUE
    dora_financial_entity: TRUE
    nis2_sector: "Banking (ESSENTIAL ENTITY)"
    aiact_high_risk_system: TRUE (Annex III - credit scoring)
    technologicalControlPlane: "Hybrid (on-premise core + cloud)"

    complexityTier: "MAXIMUM"
    activeExtensions: ["B1", "B2", "B3", "B4", "B7", "B8"]

    // Block B1 attributes (AI Act)
    aiSystemClassification: "Annex III (credit scoring)"
    aiVerificationMode: "1:many identification"
    aiConformityProcedure: "Notified body"
    aiHumanOversight: "Human review for high-value decisions"
    aiPostMarketMonitoring: "Defined (model drift and fairness)"
    aiProhibitedPractices: "Confirmed not applicable"
    aiDownstreamProviderRisk: "No modifications expected"
    aiRiskManagementSystem: "Defined"

    // Block B2 attributes (NIS 2)
    nis2EntityClass: "Essential entity"
    incidentResponseCapability: "Dedicated team (24/7 SOC + CSIRT)"
    businessContinuityPlan: "Documented and tested"
    supplyChainSecurityProgram: "Formal program"
    crisisCommunication: "Defined"
    socCapability: "In-house SOC"

    // Block B3 attributes (DORA)
    ictRiskFramework: "Documented"
    ictProviderRegister: "Maintained"
    resilienceTesting: "TLPT conducted"
    infoSharingArrangements: "Member of ISAC"

    // Block B4 attributes (Security Org)
    cisoAppointment: "Appointed"
    dpoAppointment: "Mandatory appointment"
    iso27001Scope: "Certified (ISO 27001 + PCI-DSS)"
    securityTrainingProgram: "Formal program"
    internalAuditFunction: "Dedicated team"

    // Block B7 attributes (CRA)
    craProductClass: "Default"
    craConformityRegime: "Self-assessment"
    craExclusionCheck: "Confirmed not excluded"
    craCertificationScheme: "No scheme"

    // Block B8 attributes (Multi-Actor)
    dataElementRoles: "Controller (customer PII) / Processor (regulatory reporting)"
    crossRegulationRoles: "CRA=manufacturer; GDPR=controller/processor; DORA=financial entity; AI Act=deployer"
    processorNativeCompliance: TRUE

    // Implementation readiness
    readinessScore: "11/12 — HIGH"
}
```

---

## N+1. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 2.0 | 2026-04-23 | Compliance Lead | Converted to layered intake format |
| 1.0 | 2026-04-01 | Compliance Lead | Initial release - OmniBank Financial Systems case |

---

## N+2. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-01 |
| Technical Review (CTO) | | | |
| Business Review (CEO) | | | |
| AEGIS Methodology Review | | | |

---

**Next Document:** 04_Company_Context_Assessment.md
**Dependency:** None (foundational input for Phase 1)
