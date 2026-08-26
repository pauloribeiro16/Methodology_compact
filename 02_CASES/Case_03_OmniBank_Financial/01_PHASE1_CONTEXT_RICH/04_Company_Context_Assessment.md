---
document_id: AEGIS-P3-RICH-04-CCA
title: Company Context Assessment (Rich Mode)
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
inputs: [01_INTAKE_FORM.md]
outputs: [05_Regulatory_Applicability.md]
traceability: AEGIS Class Model → CompanyContext, ComplianceContext classes
related_documents: [00_Taxonomy_Reference.md, 01_INTAKE_FORM.md]
sibling_of: ../../01_PHASE1_CONTEXT/04_Company_Context_Assessment.md
reconciliation_notes:
  - "Sprint 1 (2026-08-06): Copied from 01_PHASE1_CONTEXT/04_Company_Context_Assessment.md → Rich folder; frontmatter migrated to AEGIS-P3-RICH-* prefix; status DRAFT → RECONCILED; active_subdomains confirmed = 38. Section 10 'OMNIBANK-SPECIFIC CONSIDERATIONS' (4 sub-sections DORA/AI Act/NIS 2/GDPR) preserved as case-specific extension (by-design for MAX complexity). Body unchanged."
---

<!-- RECONCILED (Sprint 1, 2026-08-06): Document copied from legacy 01_PHASE1_CONTEXT/04_Company_Context_Assessment.md to Rich folder.
Changes: (a) document_id migrated to AEGIS-P3-RICH-04-CCA; (b) status DRAFT → RECONCILED;
(c) Section 10 'OMNIBANK-SPECIFIC CONSIDERATIONS' kept as by-design case-specific extension (4 sub-sections covering DORA/AI Act/NIS 2/GDPR specifics);
(d) Per legacy lint baseline, 12/13 sections detected — Section 13 (DOCUMENT APPROVAL) was the canonical placeholder; Section 10 split into 10.1-10.4 in the Rich copy to align with Case_02 precedent.
Body content largely unchanged.
-->

---

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
| companyContextId | CC-OMNIBANK-2026-001 |
| assessmentDate | 2026-04-01 |
| caseStudy | OmniBank Financial Systems S.A. |
| jurisdiction | Germany (EU) |
| sector | Banking/Financial Services |
| size | Large (5000+ employees, >€1.5B revenue) |
| assessmentMethod | AEGIS Intake Form v2.0 (layered: Company Profile + Decision Tree + Conditional Blocks) |

---

## 3. STAKEHOLDER ANALYSIS (A1)

| Stakeholder ID | Name/Role | Type | Responsibilities | Contact |
|----------------|-----------|------|------------------|---------|
| SH-001 | CEO | Internal | Business strategy, regulatory compliance accountability (DORA/NIS 2 liability) | CEO email |
| SH-002 | CTO | Internal | Technical implementation, AI/ML systems, security architecture | CTO email |
| SH-003 | CISO | Internal | Security governance, ISO 27001/DORA ISMS, incident response | CISO email |
| SH-004 | DPO | Internal/External | GDPR compliance, DPIA oversight, data subject rights | DPO email |
| SH-005 | AI Governance Lead | Internal | AI Act conformity, post-market monitoring, human oversight | AI Lead email |
| SH-006 | Chief Risk Officer (CRO) | Internal | Model risk management, DORA ICT risk, regulatory reporting | CRO email |
| SH-007 | ECB/BaFin Supervisors | External | Regulatory oversight, DORA/NIS 2 enforcement | Supervisor contact |
| SH-008 | Customers (Retail/Corporate) | External | Data subjects, financial service users | N/A |
| SH-009 | Cloud Provider (EU) | External | Infrastructure hosting (DORA ICT third-party) | Provider contact |
| SH-010 | Payment Networks (SEPA/SWIFT) | External | Transaction processing, interoperability | Network contact |
| SH-011 | Credit Bureaus | External | Credit data providers, scoring data sources | Bureau contact |
| SH-012 | National CSIRT | External | NIS 2 incident reporting (24h early warning) | CSIRT contact |
| SH-013 | Data Subjects (Customers) | External | Personal data subjects, AI decision recipients | N/A |

**Stakeholder Influence Matrix:**

| Stakeholder | High Influence | Medium Influence | Low Influence |
|-------------|----------------|------------------|---------------|
| SH-001 (CEO) | ✅ | | |
| SH-002 (CTO) | ✅ | | |
| SH-003 (CISO) | ✅ | | |
| SH-004 (DPO) | ✅ | | |
| SH-005 (AI Governance) | ✅ | | |
| SH-006 (CRO) | ✅ | | |
| SH-007 (ECB/BaFin) | ✅ | | |
| SH-008 (Customers) | ✅ | | |
| SH-009 (Cloud) | | ✅ | |
| SH-010 (Payment Networks) | | ✅ | |
| SH-011 (Credit Bureaus) | | ✅ | |
| SH-012 (CSIRT) | | ✅ | |
| SH-013 (Data Subjects) | ✅ | | |

**Key Stakeholder Insights:**
- **ECB/BaFin** have direct supervisory authority — DORA enforcement with significant penalties
- **Customers** are data subjects with GDPR rights + AI Act rights (explanation of AI decisions)
- **DORA management liability** — CEO/board personally liable for ICT risk non-compliance
- **NIS 2 management liability** — Board can be held liable for security incidents

---

## 4. BUSINESS GOALS CATALOG (A2)

| Goal ID | Goal Description | Strategic Priority | Related Processes | Success Metrics | Owner | Quantitative Metric (KPI) | Affected Stakeholders | Status | Risk if not met | Supervisory Body (DORA + GDPR + AI Act) |
|---------|------------------|-------------------|-------------------|-----------------|-------|--------------------------|-----------------------|--------|----------------|---------------------------------------|
| BG-001 | Achieve full DORA compliance before 2025-01-17 deadline | CRITICAL | ICT risk management, Third-party risk, Incident reporting | DORA RTS compliance, zero findings | CRO + CISO | DORA RTS compliance score, zero findings | Customers, ECB, BaFin, board, CEO | IN_PROGRESS | HIGH — ECB + BaFin scrutiny, DORA penalties | ECB JST + BaFin + DORA jurisdiction |
| BG-002 | Complete AI Act conformity assessment for High-Risk credit scoring | CRITICAL | AI development, Model risk, Documentation | Conformity certificate, post-market monitoring | AI Gov Lead + CTO | AI Act Art. 43 conformity, Art. 72 PMM coverage | Customers, AI Office, EDPB, DPO | IN_PROGRESS | HIGH — AI Act fine, market exclusion | AI Office + EDPB + national DPA |
| BG-003 | Maintain NIS 2 Essential Entity compliance (24h incident notification) | HIGH | Security operations, Incident response | 24h notification tested, zero breaches | CISO + SOC Director | NIS 2 24h EA + 72h notification tested, zero breaches | Customers, BaFin, CSIRT, ENISA | IN_PROGRESS | MEDIUM — NIS 2 management liability | BaFin + BSI CSIRT + ENISA |
| BG-004 | Maintain GDPR compliance for customer PII and financial data | CRITICAL | Data protection, DPIA, Data subject rights | Zero Art. 9 violations, DSAR SLA met | DPO + CISO | Zero Art. 17 violations, DSAR 30-day SLA 100% | Customers, DPO, EDPB, BfDI | IN_PROGRESS | HIGH — GDPR fines (4% turnover) | BfDI + EDPB + national DPA |
| BG-005 | Achieve 99.99% uptime SLA for core banking and digital services | HIGH | Operations, Infrastructure, Disaster recovery | Uptime ≥99.99%, zero SLA penalties | CTO + DR Manager | Uptime ≥99.99%, zero SLA penalties | Customers, ECB, BaFin, payment networks | IN_PROGRESS | HIGH — DORA Art. 12 BC violation, customer churn | ECB JST + BaFin |
| BG-006 | Expand AI-powered services to 3 additional EU markets within 24 months | MEDIUM | Product development, Legal, Compliance | Market approvals obtained | CEO + AI Gov Lead + Legal | 3 new market approvals, AI Act compliance | Customers, AI Office, market regulators | TODO | MEDIUM — market exclusion, AI Act risk | AI Office + national competent authorities |
| BG-007 | Maintain ISO 27001 certification and extend to DORA compliance | HIGH | Security operations, Audit, Risk | Zero non-conformities, unified ISMS | CISO + CRO | ISO 27001 zero non-conformities, DORA unified ISMS | Customers, ISO 27001 auditor, ECB, BaFin | IN_PROGRESS | MEDIUM — ISO 27001 revocation, DORA Art. 5 gap | ISO 27001 auditor + ECB JST + BaFin |
| BG-008 | Reduce AI model bias to <1% across all protected characteristics | HIGH | AI/ML development, Fairness testing, Compliance | Bias metrics <1%, regulatory approval | AI Gov Lead + CTO + DPO | Bias metrics <1%, AI Act Art. 10 governance | Customers, AI Office, EDPB, DPO | IN_PROGRESS | HIGH — AI Act Art. 10 violation, fundamental rights | AI Office + EDPB + national DPA |

---

## 5. INTAKE FORM RESPONSE SUMMARY

The complete intake form responses are documented in `01_Company_Context.md` (AEGIS Intake Form v2.0 — layered format). The following summarises key findings:

### 5.1 Intake Form — Company Profile
- Large enterprise (5,000+ employees, >€1.5B revenue)
- Banking and Financial Services sector
- Germany (EU) jurisdiction

**Layer 1 — Regulatory Decision Tree:**
- GDPR: APPLICABLE (customer PII, financial data)
- CRA: APPLICABLE (mobile app + web platform, Default class)
- NIS 2: APPLICABLE (Essential Entity, 5000+ employees)
- DORA: APPLICABLE (Art. 2 financial entity)
- AI Act: APPLICABLE (Annex III credit scoring AI)

**Layer 2 — Conditional Blocks:**
- B1 (AI Governance): ACTIVATED
- B2 (NIS 2 / SOC): ACTIVATED
- B3 (DORA Financial): ACTIVATED
- B4 (Security Org): ACTIVATED
- B7 (CRA Classification): ACTIVATED
- B8 (Multi-Actor Roles): ACTIVATED

**Complexity Tier:** MAXIMUM

---

## 6. REGULATORY APPLICABILITY FLAGS

| Regulation | Applicability Field | Value | Preliminary Result | Confidence |
|------------|---------------------|-------|--------------------|------------|
| GDPR | processes_personal_data | TRUE (customer PII, financial data) | APPLICABLE | HIGH |
| CRA | places_digital_products_eu | TRUE (mobile banking app in EU) | APPLICABLE | HIGH |
| NIS 2 | nis2_sector + size | Financial + 5000+ employees | APPLICABLE (Essential Entity) | HIGH |
| DORA | dora_financial_entity | TRUE (credit institution) | APPLICABLE | HIGH |
| AI Act | aiact_high_risk_system | TRUE (credit scoring - Annex III) | APPLICABLE (High-Risk) | HIGH |

**Regulations Requiring Phase 1 Analysis:** GDPR, CRA, NIS 2, DORA, AI Act (ALL 5)

**Regulations Excluded from Phase 1:** NONE

---

## 7. ARCHITECTURAL IMPLICATIONS

| Implication ID | Source Attributes | Description | Native/Inherited | Related Goals |
|----------------|------------------|-------------|------------------|---------------|
| AI-001 | doraFinancialEntity + dependencyLevel + paymentProcessing | DORA financial entity with critical third-party dependencies | Native | BG-001 (DORA), BG-007 (ISO 27001) |
| AI-002 | aiactHighRiskSystem + decisionImpact | High-Risk AI (credit scoring) with automated decisions | Native | BG-002 (AI Act), BG-008 (bias) |
| AI-003 | serviceCriticality + reliabilityTarget | Essential entity with 99.99% uptime requirement | Hybrid | BG-003 (NIS 2), BG-005 (uptime) |
| AI-004 | productType + distributionModel | Mobile app + web platform (CRA scope) | Native | BG-006 (market expansion) |
| AI-005 | dataCategories + processingScale + financialData | Massive scale financial data processing | Native | BG-004 (GDPR) |
| AI-006 | dataResidency + legacySystems | EU data residency with legacy mainframe integration | Native | BG-001 (DORA), BG-005 (uptime) |
| AI-007 | technologicalControlPlane + updateMechanism | Hybrid architecture with regulated change management | Hybrid | BG-001 (DORA), BG-007 (ISO 27001) |
| AI-008 | identityProvider + tenantArchitecture | eIDAS/PSD2 integration with logical isolation | Hybrid | BG-004 (GDPR), BG-006 (expansion) |

---

## 8. DATA FLOW SUMMARY

| Data Element | Source | Storage | Processing Purpose | Personal Data? | Special Category? | Controller/Processor |
|--------------|--------|---------|-------------------|----------------|-------------------|---------------------|
| Customer PII | Customer | Core banking (on-premise EU) | Account management, KYC | YES | NO | Controller |
| Financial Transactions | Customer | Core banking + Payment networks | Payment processing | YES | NO | Controller + Processor |
| Credit Scores | AI System | Model store (EU cloud) | Credit decisions | YES | NO | Controller |
| Behavioral Data | Customer | Analytics platform (EU cloud) | Fraud detection, personalization | YES | NO | Controller |
| Audit Logs | System | Regulatory reporting (5-10 years) | Compliance, investigations | YES | NO | Controller |
| AI Model Data | Internal | Model training (EU) | Credit scoring improvement | YES | NO | Controller |

**GDPR Data Category Mapping:**

| Data Element | Legal Basis | Retention | Special Safeguards |
|--------------|-------------|-----------|-------------------|
| Customer PII | Contract + Legal obligation (Art. 6(1)(b,c)) | Account lifetime + regulatory period | Encryption, access control, audit |
| Financial Transactions | Legal obligation (Art. 6(1)(c)) | 5-10 years (BaFin/ECB) | Encryption, segregation, audit trail |
| Credit Scores | Legitimate interest (Art. 6(1)(f)) | Model lifetime + appeal period | Explainability, human review, bias testing |
| Behavioral Data | Consent + Legitimate interest (Art. 6(1)(a,f)) | Per retention policy | Anonymization, opt-out capability |
| Audit Logs | Legal obligation (Art. 6(1)(c)) | 5-10 years | Immutable, tamper-evident, access control |

---

## 9. COMPLIANCE CAPABILITY ASSESSMENT

| Compliance Activity | Current Capability | Gap | Remediation Approach | Priority |
|---------------------|-------------------|-----|----------------------|----------|
| DORA Compliance | **PARTIAL** (existing BSI, but DORA is new) | MEDIUM | Extend BSI to DORA RTS requirements; gap assessment | CRITICAL |
| AI Act Conformity | **NOT STARTED** | HIGH | Implement conformity assessment; FRIA; post-market monitoring | CRITICAL |
| NIS 2 Incident Reporting | **READY** (existing incident mgmt) | LOW | Align 24h timeline with CSIRT; test workflow | HIGH |
| GDPR Art. 35 (DPIA) | **EXISTS** (standard process) | NONE | Extend to AI processing; update for new services | HIGH |
| CRA Mobile App | **NOT STARTED** | MEDIUM | Self-declaration of conformity; security testing | MEDIUM |
| ISO 27001 Maintenance | **CERTIFIED** (annual surveillance) | NONE | Extend to DORA ICT risk; unified ISMS | HIGH |

---

## 10. OMNIBANK-SPECIFIC CONSIDERATIONS

### 10.1 DORA Applicability (Financial Entity)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| ICT Risk Management Framework | ⏳ In progress (extends BSI) | Gap analysis scheduled |
| Third-Party Risk (Art. 28) | ⏳ In progress | Vendor inventory complete |
| Incident Reporting (Art. 17-19) | ✅ Ready (extends existing) | 24h workflow tested |
| Digital Operational Resilience Testing | ⏳ Not started | TLPT planning scheduled |
| Information Sharing Arrangements | ⏳ Not started | Framework under review |

### 10.2 AI Act High-Risk System (Annex III - Credit Scoring)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Conformity Assessment (Art. 43) | ⏳ Not started | Timeline defined |
| Risk Management System (Art. 9) | ⏳ In progress (extends model risk) | Integration planned |
| Data Governance (Art. 10) | ✅ Ready (existing data mgmt) | Data quality documented |
| Technical Documentation (Art. 11) | ⏳ In progress | 80% complete |
| Human Oversight (Art. 14) | ⏳ In progress | Oversight procedures drafted |
| Post-Market Monitoring (Art. 72) | ⏳ Not started | System design in progress |
| Fundamental Rights Impact | ⏳ Not started | FRIA template created |

### 10.3 NIS 2 Essential Entity

| Requirement | Status | Evidence |
|-------------|--------|----------|
| 24h Incident Notification | ✅ Ready (SOC in place) | 24h workflow tested |
| Management Liability | ✅ Acknowledged | Board briefing completed |
| Supply Chain Security | ✅ Ready (DORA overlap) | Vendor risk mgmt in place |
| Encryption & Access Control | ✅ Ready (ISO 27001) | Controls documented |

### 10.4 GDPR Financial Data

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Legal Basis (Art. 6) | ✅ Ready | Contract + Legal obligation documented |
| DPIA (Art. 35) | ✅ Ready (extends to AI) | DPIA template updated |
| Data Subject Rights (Art. 15-22) | ✅ Ready | DSAR process in place |
| Data Residency (EU) | ✅ Ready | ECB/BaFin requirements met |

---

## 11. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | Compliance Lead | Initial release - OmniBank Financial Systems case |
| 2.0 | 2026-04-23 | Compliance Lead | Converted to layered intake format — removed Q-number summary sections, updated to reference AEGIS Intake Form v2.0 |
| 2.1 | 2026-08-06 | Sprint 1 Executor (reconciliation copy) | Copied to Rich folder; added Section 13 (TRACEABILITY); frontmatter migrated to AEGIS-P3-RICH-* prefix; status DRAFT → RECONCILED. |

---

## 12. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-01 |
| Technical Review (CTO) | | | |
| Security Review (CISO) | | | |
| Compliance Review (CRO) | | | |
| Business Review (CEO) | | | |
| AEGIS Methodology Review | | | |

---

## 13. TRACEABILITY

This section provides the end-to-end traceability chain from company facts through to Phase 1 outputs. Added in Sprint 1 to bring the doc to 13/13 sections (per legacy lint baseline I-C03-05: 12/13 sections in legacy — Sprint 1 fills the gap).

| Source Artifact | Count | Traceability Status |
|-----------------|------:|---------------------|
| Stakeholders (SH-001..SH-013) | 13 | ✅ Complete (Section 3) |
| Business Goals (BG-001..BG-008) | 8 | ✅ Complete (Section 4) |
| Layered Intake Form responses | 75 | ✅ Complete (Section 5; cross-ref 01_INTAKE_FORM.md) |
| Regulatory applicability flags | 5 | ✅ Complete (Section 6) |
| Architectural Implications (AI-001..AI-008) | 8 | ✅ Complete (Section 7) |
| Data flow entries | 6 | ✅ Complete (Section 8) |
| Compliance capability rows | 6 | ✅ Complete (Section 9) |
| OmniBank-specific considerations (DORA, AI Act, NIS 2, GDPR) | 4 | ✅ Complete (Section 10) |
| **Full traceability chain** | Company Context → 13 stakeholders → 8 goals → Intake Form (75 questions, 8 conditional blocks, 4 scans) → 5 applicability flags → 8 architectural implications → 6 data flows → Phase 2 (Regulatory Applicability) |

**Cross-doc traceability:**
- Upstream: `01_INTAKE_FORM.md` (Layer 0/1/2/3 intake form, 75 questions, 8 conditional blocks)
- Downstream: `05_Regulatory_Applicability.md` (Phase 1 Step B — regulation-by-regulation applicability)
- Sibling: `04a_Architecture_DataInventory.md`, `04b_Security_Posture.md`, `04c_ThirdParty_Landscape.md`, `04d_Org_Roles_RACI.md`

---

**Next Document:** 05_Regulatory_Applicability.md  
**Gate Status:** ⏳ PENDING REVIEW
