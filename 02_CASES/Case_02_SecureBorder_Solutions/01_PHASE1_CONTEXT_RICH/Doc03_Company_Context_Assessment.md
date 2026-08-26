---
document_id: AEGIS-P2-RICH-04-CONTEXT
title: Company Context Assessment (Rich Mode)
phase: 1
version: 2.1
created: 2026-04-01
updated: 2026-08-06
author: Compliance Lead (Rich copy: Sprint 1 Executor, 2026-08-06)
status: RECONCILED
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
active_subdomains: 35
inactive_documented: [D-08.3 INACTIVE, 3 NOT_ADDRESSED]
inputs: [01_INTAKE_FORM.md]
outputs: [05_Regulatory_Applicability.md]
traceability: AEGIS Class Model → CompanyContext, ComplianceContext classes
related_documents: [00_Taxonomy_Reference.md, 01_INTAKE_FORM.md]
reconciliation:
  sprint: 1
  role: reconciliation
  base_doc: ../01_PHASE1_CONTEXT/04_Company_Context_Assessment.md (legacy, frozen)
  notes: |
    Sprint 1 reconciliation (Case_02, 2026-08-06):
    - Frontmatter updated to AEGIS-P2-RICH-* convention (P2 = Case_02).
    - status: DRAFT → RECONCILED.
    - Section 10 (SECUREBORDER-SPECIFIC CONSIDERATIONS) preserved verbatim — flagged by lint
      as "extra section not in template" but is a Case_02 first-class extension (10.x sub-sections
      cover CRA Critical Class, AI_Act High-Risk, NIS 2 Essential Entity, GDPR Art. 9). Marked
      with `<!-- BY-DESIGN: case-specific extension -->` markers below.
    - Body preserved verbatim (Sprint 1 is content-neutral; Sprint 2 adds corpus linkages).
---

<!-- RECONCILIATION BANNER (Sprint 1, 2026-08-06):
     This is the Rich Mode copy of AEGIS-P1-04.
     Source: ../01_PHASE1_CONTEXT/04_Company_Context_Assessment.md.
     Body unchanged from legacy. Sprint 2 will add corpus linkages (L1 sub-domain .md refs).
     See SPRINT1_REPORT.md for the full fix list.
-->

<!-- BY-DESIGN: Section 10 (SECUREBORDER-SPECIFIC CONSIDERATIONS) and 10.1–10.4 sub-sections
     are intentional Case_02-specific extensions. The lint flags them as "extra sections not in
     template" but they support the case's 4 applicable regulations × 4 special categories.
     See LINT_REPORT_BEFORE.md §6 (Issue 5) for the by-design classification.
-->

# Company Context Assessment

## 1. DOCUMENT PURPOSE

This document consolidates the company context assessment (Step A1+A2+A3) including stakeholder analysis, business goals, and intake form responses. This is the primary input for regulatory applicability assessment.

**Alignment with Class Model:**
- `CompanyContext` - Instantiated from AEGIS Intake Form v2.0 (layered format)
- `ComplianceContext` - Derived regulatory applicability flags
- `Stakeholder` - Organizational roles and responsibilities
- `BusinessGoal` - Strategic objectives

**Phase 1 Step:** A (Company Context Assessment)

**Gate Criteria:** Intake form complete; regulatory applicability determined

---

## 2. ASSESSMENT SUMMARY

| Attribute | Value |
|-----------|-------|
| companyContextId | CC-SECUREBORDER-2026-001 |
| assessmentDate | 2026-04-01 |
| caseStudy | SecureBorder Solutions B.V. |
| jurisdiction | Netherlands (EU) |
| sector | Defense/Security/Critical Infrastructure |
| size | Medium-Large (450 employees, €120M revenue) |
| assessmentMethod | AEGIS Intake Form v2.0 (layered: Company Profile + Decision Tree + Conditional Blocks) |

---

## 3. STAKEHOLDER ANALYSIS (A1)

This section registers all stakeholders (internal and external) involved in or affected by regulatory compliance at SecureBorder, and assesses their influence on compliance decisions. The stakeholder set spans operational roles (CEO, CTO, CISO, DPO, AI Governance Lead), external parties (government controllers, notified body, CSIRT, cloud and hardware suppliers), and data subjects (Schengen travelers).

### 3.1 Stakeholder Register

| Stakeholder ID | Name/Role | Type | Responsibilities | Contact |
|----------------|-----------|------|------------------|---------|
| SH-001 | CEO | Internal | Business strategy, regulatory compliance accountability | CEO email |
| SH-002 | CTO | Internal | Technical implementation, AI/ML systems, security architecture | CTO email |
| SH-003 | CISO | Internal | Security governance, ISO 27001 ISMS, incident response | CISO email |
| SH-004 | DPO | Internal/External | GDPR compliance, DPIA oversight, Art. 9 legal basis | DPO email |
| SH-005 | AI Governance Lead | Internal | AI_Act conformity, post-market monitoring, human oversight | AI Lead email |
| SH-006 | Government Contract Managers | External | Contract compliance, security requirements enforcement | Contract email |
| SH-007 | Border Control Authorities | External | Data controller (government), watchlist data providers | Government contact |
| SH-008 | Airport Operators | External | System deployment, operational requirements, SLA enforcement | Airport security |
| SH-009 | Cloud Provider (EU) | External | Infrastructure hosting, model update delivery | Provider contact |
| SH-010 | Hardware Suppliers | External | Component security, SBOM provision, firmware signing | Supplier contact |
| SH-011 | Notified Body (CRA) | External | Critical Class conformity assessment, certification | Notified Body contact |
| SH-012 | National CSIRT | External | NIS 2 incident reporting (24h early warning) | CSIRT contact |
| SH-013 | Data Subjects (Travelers) | External | Biometric data subjects, fundamental rights holders | N/A |

### 3.2 Stakeholder Influence Matrix

| Stakeholder | High Influence | Medium Influence | Low Influence |
|-------------|----------------|------------------|---------------|
| SH-001 (CEO) | ✅ | | |
| SH-002 (CTO) | ✅ | | |
| SH-003 (CISO) | ✅ | | |
| SH-004 (DPO) | ✅ | | |
| SH-005 (AI Governance) | ✅ | | |
| SH-006 (Govt Contract) | ✅ | | |
| SH-007 (Border Authorities) | ✅ | | |
| SH-008 (Airports) | ✅ | | |
| SH-009 (Cloud) | | ✅ | |
| SH-010 (Suppliers) | | ✅ | |
| SH-011 (Notified Body) | ✅ | | |
| SH-012 (CSIRT) | | ✅ | |
| SH-013 (Travelers) | ✅ | | |

**Key Stakeholder Insights:**
- **Government authorities** are data controllers — SecureBorder is processor (GDPR Art. 28)
- **Notified Body** has veto power over market access (CRA Critical Class)
- **Travelers** are data subjects with fundamental rights (free movement, privacy)
- **NIS 2 management liability** — CEO/board personally liable for non-compliance

---

## 4. BUSINESS GOALS CATALOG (A2)

| Goal ID | Goal Description | Strategic Priority | Related Processes | Success Metrics | Owner | Quantitative KPI | Affected Stakeholders | Status | Risk if not met |
|---------|------------------|-------------------|-------------------|-----------------|-------|------------------|----------------------|--------|-----------------|
| BG-001 | Achieve CRA Critical Class certification before product launch | CRITICAL | Product development, Quality assurance, Legal | Certification obtained, CE marking approved | CTO + Notified Body project lead | Time to certification (months); conformity assessment pass-rate | CTO, CEO, Notified Body, ENISA, government customers | IN_PROGRESS | HIGH — Market access blocked; CRA Art. 56 fines (up to €15M / 2.5% turnover) |
| BG-002 | Complete AI_Act conformity assessment for High-Risk AI system | CRITICAL | AI development, Documentation, Testing | Conformity certificate, post-market monitoring system | AI Governance Lead + CTO | Time to conformity certificate; post-market monitoring uptime | AI Governance Lead, CTO, DPO, Notified Body, AI Supervisory Authority | IN_PROGRESS | HIGH — Market access blocked; AI_Act Art. 99 fines (up to €15M / 3% turnover) |
| BG-003 | Maintain NIS 2 compliance (24h incident notification capability) | HIGH | Security operations, Incident response | 24h notification tested, zero breaches | CISO + SOC | MTTD (mean time to detect); MTTR (mean time to respond); 24h routing pipeline test pass-rate | CISO, SOC, DPO, CSIRT, CEO | DONE | HIGH — NIS 2 Art. 20 management liability; CEO/board personally liable |
| BG-004 | Maintain GDPR Art. 9 compliance for biometric processing | CRITICAL | Data protection, DPIA, Legal basis | DPIA updated, zero Art. 9 violations | DPO + Legal Counsel | DPO oversight hours; DPIA refresh cadence; Art. 9 violation count | DPO, travelers (data subjects), DPA, CEO | DONE | HIGH — GDPR Art. 83(5) fine (up to €20M / 4% turnover) |
| BG-005 | Achieve 99.99% uptime SLA for airport operations | HIGH | Operations, Infrastructure, Support | Uptime ≥99.99%, zero SLA penalties | CTO + Operations Lead | Uptime %; SLA breach count; MTTR for service incidents | CTO, airport operators, airport security, government customers | IN_PROGRESS | HIGH — SLA penalties; airport contract loss; customer trust erosion |
| BG-006 | Expand to 5 additional Schengen countries within 18 months | MEDIUM | Sales, Legal, Compliance | Country certifications obtained | CEO + Sales Lead | Country certifications obtained; revenue from new countries | CEO, Sales, Legal, country authorities | IN_PROGRESS | MEDIUM — Missed market opportunity; competitive disadvantage |
| BG-007 | Maintain ISO 27001 certification (annual surveillance) | HIGH | Security operations, Audit | Zero non-conformities, continuous certification | CISO + ISMS Manager | Surveillance audit pass-rate; non-conformity count | CISO, ISMS team, surveillance auditor, customers | DONE | LOW — Recertification requires additional effort; customer trust impact |

**Note:** BG-008 (AI false match rate <0.1%) moved to Phase 3 — this is a technical requirement for Functional Node allocation, not a Phase 1 business goal.

---

## 5. INTAKE FORM RESPONSE SUMMARY

The complete intake form responses are documented in `01_Company_Context.md` (AEGIS Intake Form v2.0 — layered format). The following summarises key findings:

### 5.1 Intake Form — Company Profile
- Medium-Large enterprise (450 employees, ~€120M revenue)
- Defense/Security/Critical Infrastructure sector
- Netherlands (EU) jurisdiction

### 5.2 Layer 1 — Regulatory Decision Tree Results
- GDPR: APPLICABLE (processes biometric data, Art. 9)
- CRA: APPLICABLE (hardware+software, Critical Class)
- NIS 2: APPLICABLE (essential entity supplier, 450 employees)
- DORA: NOT APPLICABLE (not financial entity)
- AI_Act: APPLICABLE (Annex III border control AI)

### 5.3 Layer 2 — Conditional Block Activation
- B1 (AI Governance): ACTIVATED
- B2 (NIS 2 / SOC): ACTIVATED
- B4 (Security Org): ACTIVATED
- B5 (Special Category Data): ACTIVATED
- B6 (Supply Chain): ACTIVATED
- B7 (CRA Classification): ACTIVATED
- B8 (Multi-Actor Roles): ACTIVATED

**Complexity Tier:** HIGH

---

## 6. REGULATORY APPLICABILITY — DETAILED ANALYSIS

The detailed clause-by-clause applicability rationale and obligated-party allocation for each regulation is documented in `05_Regulatory_Applicability.md` (Sections 3.1–3.5). This section provides the assessment summary table and per-regulation pointers for navigation.

| Regulation | Applicability Field | Value | Preliminary Result | Confidence |
|------------|---------------------|-------|--------------------|------------|
| GDPR | processes_personal_data + specialCategoryData | TRUE (biometric data, Art. 9) | APPLICABLE | HIGH |
| CRA | places_digital_products_eu + criticalClass | TRUE (hardware+software, Critical Class) | APPLICABLE | HIGH |
| NIS 2 | nis2_sector + size | Security sector + 450 employees | APPLICABLE | HIGH |
| DORA | dora_financial_entity | FALSE | NOT APPLICABLE | HIGH |
| AI_Act | aiact_high_risk_system | TRUE (Annex III - border control) | APPLICABLE | HIGH |

**Regulations Requiring Phase 1 Analysis:** GDPR, CRA, NIS 2, AI_Act

**Regulations Excluded from Phase 1:** DORA

### 6.1 GDPR

**Headline:** SecureBorder processes special category data (biometric facial templates) on behalf of government border control authorities. As processor, GDPR obligations apply via Art. 28 DPA. Also a controller for audit logs and compliance data. Large-scale processing of Art. 9 data triggers mandatory DPIA (Art. 35).

**Key clauses in scope:** GDPR-C01 through GDPR-C28 (all 28). See `05_Regulatory_Applicability.md` §3.1 for the clause-by-clause applicability analysis.

**Obligated party:** CONTROLLER (for audit logs) + PROCESSOR (for biometric facial templates).

### 6.2 CRA

**Headline:** GuardianGate eGate systems are digital products with critical security functions for border control. As manufacturer, SecureBorder must comply with CRA Essential Requirements (Annex I Parts I and II). Critical Class classification requires third-party conformity assessment by a notified body (Art. 32(3) until Art. 8 certification scheme exists).

**Key clauses in scope:** CRA-C01 through CRA-C26 (all 26). See `05_Regulatory_Applicability.md` §3.2 for the clause-by-clause applicability analysis.

**Obligated party:** MANUFACTURER (Critical Class — Art. 32(3) full quality assurance + EU-type examination).

### 6.3 NIS 2

**Headline:** SecureBorder qualifies as a medium-sized enterprise (450 employees, €120M revenue) operating in the defense/security sector. As a supplier of critical systems to government border control (essential entities), NIS 2 supply chain security obligations apply (Art. 21(2)(d)). Management liability applies for non-compliance.

**Key clauses in scope:** NIS2-C01 through NIS2-C29 (all 29). See `05_Regulatory_Applicability.md` §3.3 for the clause-by-clause applicability analysis.

**Obligated party:** ESSENTIAL_ENTITY_SUPPLIER (24h incident notification — Art. 23(4)(a)).

### 6.5 AI_Act

**Headline:** GuardianGate uses Edge AI for automated border control (face matching, liveness detection). This falls explicitly under AI_Act Annex III (migration, asylum and border control management) as a high-risk AI system. Conformity assessment required before EU market placement (Art. 43(4) — Annex III requires third-party assessment). Post-market monitoring system mandatory (Art. 72).

**Key clauses in scope:** AI-C01 through AI-C29 (all 29). See `05_Regulatory_Applicability.md` §3.5 for the clause-by-clause applicability analysis.

**Obligated party:** PROVIDER (High-Risk AI System per Annex III).

---

## 7. ARCHITECTURAL IMPLICATIONS

| Implication ID | Source Attributes | Description | Native/Inherited | Related Goals |
|----------------|------------------|-------------|------------------|---------------|
| AI-001 | specialCategoryData + processingScale | Biometric data processing at large scale | Native | BG-004 (GDPR Art. 9) |
| AI-002 | aiactHighRiskSystem + updateMechanism | High-Risk AI with signed OTA updates | Native | BG-002 (AI_Act) |
| AI-003 | serviceCriticality + dependencyLevel | Critical infrastructure with cloud dependency | Hybrid | BG-003 (NIS 2), BG-005 (99.99%) |
| AI-004 | productType + supplyChainVisibility | Hardware+software Critical Class (CRA) | Native | BG-001 (CRA certification) |
| AI-005 | dataResidency + tenantArchitecture | EU data residency with physical isolation | Native | BG-006 (Schengen expansion) |
| AI-006 | legacySystems + identityProvider | Legacy government system integration | Native | BG-005 (uptime SLA) |

---

## 8. DATA FLOW SUMMARY

| Data Element | Source | Storage | Processing Purpose | Personal Data? | Special Category? | Controller/Processor |
|--------------|--------|---------|-------------------|----------------|-------------------|---------------------|
| Facial Template | Traveler | Edge AI (kiosk) | 1:1 face matching | YES | **YES (Art. 9)** | Processor (for government) |
| Passport Data | Traveler | Edge AI + Government DB | Identity verification | YES | NO | Processor |
| Watchlist Data | Government | Encrypted, isolated | Match against traveler | YES | NO | Processor |
| Match Decision | AI System | Audit log | Border control decision | YES | NO | **Controller (for compliance)** |
| Audit Logs | System | Government authority (10 years) | Legal compliance, challenges | YES | NO | Controller |
| AI Model Updates | Cloud | Edge (signed) | Model improvement | NO | NO | N/A |

**GDPR Data Category Mapping:**

| Data Element | Legal Basis | Retention | Special Safeguards |
|--------------|-------------|-----------|-------------------|
| Facial Template | Government contract (Art. 9(2)(g)) | Delete after match (seconds) | Encryption, access control, audit |
| Passport Data | Legal obligation (Art. 6(1)(c)) | Per government policy | Encryption, isolation |
| Watchlist Data | Legal obligation (Art. 6(1)(c)) | Per government policy | Highest encryption, need-to-know |
| Audit Logs | Legal obligation (Art. 6(1)(c)) | 10 years | Immutable, tamper-evident |

---

## 9. COMPLIANCE CAPABILITY ASSESSMENT

| Compliance Activity | Current Capability | Gap | Remediation Approach | Priority |
|---------------------|-------------------|-----|----------------------|----------|
| GDPR Art. 9 (Biometric) | **EXISTS** (DPIA completed) | LOW | Maintain and update annually | CRITICAL |
| GDPR Art. 35 (DPIA) | **EXISTS** | NONE | Annual review | CRITICAL |
| CRA Critical Class | **PENDING** (assessment scheduled) | HIGH | Complete notified body assessment | CRITICAL |
| AI_Act Conformity | **PARTIAL** (documentation in progress) | MEDIUM | Complete before market placement | CRITICAL |
| NIS 2 Incident Reporting | **READY** (SOC in place) | LOW | Align 24h timeline with CSIRT | HIGH |
| ISO 27001 Maintenance | **CERTIFIED** (annual surveillance) | NONE | Continuous compliance | HIGH |
| AI Post-Market Monitoring | **NOT STARTED** | HIGH | Implement monitoring system | HIGH |
| AI Human Oversight (Art. 14) | **PARTIAL** | MEDIUM | Define oversight procedures | HIGH |

---

<!-- BY-DESIGN: case-specific extension (Case_02 first-class, supports 4 applicable regs × 4 special categories) -->

## 10. SECUREBORDER-SPECIFIC CONSIDERATIONS

### 10.1 Critical Class Products (CRA)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Third-party conformity assessment | ⏳ Scheduled | Notified Body contract signed |
| Technical documentation (10 years) | ⏳ In progress | Documentation framework created |
| Vulnerability disclosure (24h) | ✅ Ready | Incident response team in place |
| SBOM maintenance | ✅ Ready | Supply chain visibility system |

### 10.2 High-Risk AI System (AI_Act Annex III)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Conformity assessment | ⏳ In progress | Technical documentation 80% complete |
| Risk management system | ✅ Ready | ISO 27001 ISMS extended to AI |
| Data governance (Art. 10) | ✅ Ready | Training data documented |
| Human oversight (Art. 14) | ⏳ In progress | Oversight procedures drafted |
| Post-market monitoring | ⏳ Not started | System design in progress |
| Fundamental rights impact | ⏳ In progress | FRIA integrated with DPIA |

### 10.3 NIS 2 Essential Entity Supplier

| Requirement | Status | Evidence |
|-------------|--------|----------|
| 24h incident notification | ✅ Ready | SOC with 24/7 monitoring |
| Management liability | ✅ Acknowledged | Board briefing completed |
| Supply chain security | ✅ Ready | Supplier security requirements |
| Encryption & access control | ✅ Ready | ISO 27001 controls |

### 10.4 GDPR Art. 9 (Special Category Data)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Explicit legal basis | ✅ Ready | Government contract (Art. 9(2)(g)) |
| DPIA (large-scale biometric) | ✅ Ready | DPIA completed |
| Data minimization | ✅ Ready | Facial template deleted after match |
| Data residency (EU/Schengen) | ✅ Ready | EU-only cloud contracts |

---

## 11. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | Compliance Lead | Initial release - SecureBorder Solutions case |
| 2.0 | 2026-04-23 | Compliance Lead | Converted to layered intake format — removed Q-number summary sections, updated to reference AEGIS Intake Form v2.0 |

---

## 12. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-01 |
| Technical Review (CTO) | | | |
| Security Review (CISO) | | | |
| Business Review (CEO) | | | |
| AEGIS Methodology Review | | | |

---

**Next Document:** 05_Regulatory_Applicability.md  
**Gate Status:** ⏳ PENDING REVIEW
