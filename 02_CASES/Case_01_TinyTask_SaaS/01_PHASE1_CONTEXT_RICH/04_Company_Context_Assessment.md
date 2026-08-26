---
document_id: AEGIS-P1-04
title: Company Context Assessment
phase: 1
version: 2.4
created: 2026-04-17
updated: 2026-08-10
author: Sprint 5 Executor (deep-enrichment-builder)
sprint_1_author: Compliance Lead (Sprint 1 reconciliation)
sprint_8_author: Sprint 8 Executor (corr-009 ao-id-alias-update)
sprint_9_author: Sprint 9 Executor (corr-015 ao-canonical-ids cross-refs)
status: DEEP_ENRICHED
deep_enrichment_date: 2026-08-06
deep_enrichment_sprint: 5
ao_id_alias_update_date: 2026-08-10
ao_id_alias_update_sprint: 8
corr_015_crossref_update_date: 2026-08-10
corr_015_crossref_update_sprint: 9
bg_table_cols_added: 6
sprint: 8
sprint_role: ao_id_alias_update_bg03_bg04
inputs: [01_INTAKE_FORM.md]
outputs: [05_Regulatory_Applicability.md]
traceability: AEGIS Class Model -> CompanyContext, ComplianceContext classes
related_documents: [00_Taxonomy_Reference.md, 01_INTAKE_FORM.md]
---

> **Sprint 1 Reconciliation Note (2026-08-06)**
> Rich Mode copy of legacy `01_PHASE1_CONTEXT/04_Company_Context_Assessment.md` (v2.0). Sprint 1 changes:
> - **I-10 (status DRAFT → RECONCILED):** Sprint 1 milestone.
> - **I-05/I-06 (FR/NFR IDs):** No FR/NFR IDs present in this doc (Phase 1 — no functional/architectural decomposition). N/A.
> - **I-07/I-08 (rule/UC counts):** No rule or UC counts referenced. N/A.
> - **I-13 (02_Regulatory_Mapping_Master.md deprecation):** Not referenced in this doc. N/A.
> - Body content unchanged from legacy. Sprint 2 will add L2 manifest paths per stakeholder/goal/AI/capability field.

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

| Field | Value |
|-------|-------|
| Assessment ID | A417FB3B |
| Assessment Date | 2026-04-17 |
| Assessor | Compliance Lead |
| Company Name | TinyTask Lda. |
| Jurisdiction | EU |
| Sector | Technology |
| Size Category | Micro — 8 employees, <€2M revenue |
| Assessment Method | AEGIS Intake Form v2.0 (layered: Company Profile + Decision Tree + Conditional Blocks) |

---

## 3. STAKEHOLDER ANALYSIS (A1)

### 3.1 Stakeholder Register

| ID | Name | Role | Organization | Contact | Responsibilities |
|----|------|------|-------------|---------|-----------------|
| STK-CEO-01 | CEO (implicit) | Internal | TinyTask Lda. | — | Business strategy, compliance accountability |
| STK-CTO-01 | CTO (implicit) | Internal | TinyTask Lda. | — | Technical leadership, security architecture |
| STK-DPO-01 | DPO (implicit) | Internal | TinyTask Lda. | — | Data protection oversight, GDPR compliance |
| STK-DEVP-01 | Development Team | Internal | TinyTask Lda. | — | Secure development, implementation |
| STK-CUSTOMER-01 | B2B Customers | External | Client organizations | — | Data controllers; recipient of breach notifications |
| STK-STRIPE-01 | Stripe | External | Stripe Technologies | compliance@stripe.com | Payment processing; PCI-DSS compliance |
| STK-AWS-01 | AWS | External | Amazon Web Services | — | Cloud infrastructure; inherited security controls |

**ID Pattern:** `STK-{Role}-{NN}` where `{Role}` is abbreviated role name (CEO, CTO, DPO, etc.) and `{NN}` is a 2-digit sequential number.

### 3.2 Stakeholder Influence Matrix

| Stakeholder ID | Influence Level | Interest Level | Engagement Strategy |
|----------------|----------------|----------------|-------------------|
| STK-CEO-01 | HIGH | HIGH | Weekly briefings; direct involvement in compliance decisions |
| STK-CTO-01 | HIGH | HIGH | Technical reviews; architecture decisions |
| STK-DPO-01 | MEDIUM | HIGH | Quarterly reviews; incident coordination |
| STK-DEVP-01 | MEDIUM | MEDIUM | Sprint reviews; implementation feedback |
| STK-CUSTOMER-01 | LOW | HIGH | Annual review; contract updates |
| STK-STRIPE-01 | LOW | LOW | Ad-hoc coordination; compliance documentation |
| STK-AWS-01 | LOW | LOW | Ad-hoc; annual security review |

---

## 4. BUSINESS GOALS CATALOG

| Goal ID | Goal | Description | Priority | Related Regulations | Success Metrics | Linked Adjusted Goals (Doc 07c_Adjusted_Goals) | Owner | Quantitative Metric | Affected Stakeholders | Status | Risk if not met |
|---------|------|-------------|----------|-------------------|-----------------|--------------------------------------|--------|-------------|--------------------|----------|-----------------|
| BG-01 | GDPR Compliance Baseline | Establish baseline GDPR compliance for all personal data processing activities | HIGH | GDPR | Zero audit findings; RoPA complete | → Doc 07c_Adjusted_Goals §1 (Generic Baseline, corpus-frozen) + §2 (HL, 35 rows: AG-D-XX.X-001) + §3 (GDPR-driven, 28 rows: AG-D-XX.X-001) + §5 (Tensions T-001..T-004) + §6 (Track B tier) + Appendix A.A.0 (legacy alias) | CTO + DPO | Zero audit findings in last 12 months; RoPA 100% complete | CEO, CTO, DPO, all B2B clients (data controllers) | IN_PROGRESS | HIGH — GDPR fines up to €10M or 2% turnover; contractual breach with B2B clients |
| BG-02 | CRA Conformity | Achieve CRA conformity for Team Organizer SaaS product | HIGH | CRA | SBOM published; security.txt active | → Doc 07c_Adjusted_Goals §4 (CRA-driven, 34 rows: AG-D-XX.X-002) + §2 (HL: AG-D-XX.X-001) — D-02.x (vuln + patch + CVD) + D-06.2 (SBOM) + D-07.x (secure dev) | Lead Dev | SBOM published per release (37 releases planned for first 12 months); security.txt active + reachable | CTO, Lead Dev, B2B clients (procurement), EU market-surveillance authorities | TODO | HIGH — CRA non-conformity prevents EU market access |
| BG-03 | Data Subject Rights | Enable data export and erasure for all users | MEDIUM | GDPR | User-facing export/delete features live | → Doc 07c_Adjusted_Goals §3 GDPR-driven D-05.3 (`AG-D-05.3-001` — formerly `PG-D-05.3-001` — erasure) + D-05.4 (`AG-D-05.4-001` — formerly `PG-D-05.4-001` — portability), both LIGHTWEIGHT; complement in Appendix A.A.0 alias | DPO + CTO | <30d DSAR turnaround; JSON export endpoint live within 90 days | Customers (data subjects), DPO, B2B client controllers | TODO | HIGH — Art. 17 erasure + Art. 20 portability are statutory deadlines |
| BG-04 | Security by Design | Integrate security into development lifecycle | MEDIUM | CRA, GDPR | SAST/DAST in CI/CD pipeline | → Doc 07c_Adjusted_Goals §4 CRA-driven D-02.1 (`AG-D-02.1-002` — formerly `SG-D-02.1-001` — vulnerability ID) + D-07.x (secure dev pipeline), all LIGHTWEIGHT; complement in §3 GDPR-driven (`AG-D-02.1-001`) | Lead Dev + CTO | SAST in CI by end of quarter; zero CRITICAL findings on main branch | CTO, Lead Dev, B2B clients (security review) | IN_PROGRESS | MEDIUM — CRA Art. 18 + GDPR Art. 25 design-time obligations |
| BG-05 | Supplier Due Diligence | Maintain SOC 2/ISO 27001 evidence from cloud providers | MEDIUM | GDPR, CRA | Annual review completed | → Doc 07c_Adjusted_Goals §3 GDPR-driven D-06.1 (`AG-D-06.1-001`) + §4 CRA-driven D-06.1 (`AG-D-06.1-002`) (MINIMAL INHERIT vendor attestation, dual-coverage) + §5 T-002 (unified vendor mgmt) + Appendix A.A.0 alias | CTO + Procurement | Annual review of AWS SOC 2, Stripe PCI-DSS, Firebase security docs | CTO, Procurement, B2B clients (procurement) | IN_PROGRESS | MEDIUM — GDPR Art. 28 + CRA Art. 7 supplier obligations |

**ID Pattern:** `BG-{NN}` where `{NN}` is a 2-digit sequential number.

---

## 5. INTAKE FORM RESPONSE SUMMARY

The complete intake form responses are documented in `01_Company_Context.md` (AEGIS Intake Form v2.0 — layered format). The following summarises key findings:

### 5.1 Intake Form — Company Profile
- Micro-enterprise (8 employees, <€2M revenue)
- Technology/Software sector
- Portugal (EU) jurisdiction

**Layer 1 — Regulatory Decision Tree:**
- GDPR: APPLICABLE (processes personal data)
- CRA: APPLICABLE (SaaS placed on EU market, Default class)
- NIS 2: NOT APPLICABLE (below all thresholds)
- DORA: NOT APPLICABLE (not financial entity)
- AI Act: NOT APPLICABLE (no AI/ML systems)

**Layer 2 — Conditional Blocks:**
- B6 (Supply Chain): ACTIVATED
- B7 (CRA Classification): ACTIVATED
- B8 (Multi-Actor Roles): ACTIVATED

**Complexity Tier:** MEDIUM

---

## 6. REGULATORY APPLICABILITY FLAGS

| Regulation | Applicable? | Rationale | Applicability Threshold | Threshold Met? |
|------------|-------------|-----------|------------------------|----------------|
| GDPR | YES | Processes personal data (emails, names) of EU residents | Processes personal data of EU residents | YES |
| CRA | YES | SaaS product placed on EU market; manufacturer status | Places digital products with digital elements on EU market | YES |
| NIS 2 | NO | Below employee (8 < 50) and revenue (<€2M < €10M) thresholds | Essential/Important entity AND (>=50 employees OR >=EUR 10M revenue) | NO |
| DORA | NO | Not a financial entity; payments via Stripe | Financial entity per Art. 2 definition | NO |
| AI Act | NO | No AI/ML systems; deterministic logic only | AI system provider/deployer; High-risk per Annex II/III | NO |

---

## 7. ARCHITECTURAL IMPLICATIONS

| Implication ID | Description | Source Regulation | Impact Area | Severity | Mitigation Approach |
|----------------|-------------|-------------------|-------------|----------|-------------------|
| AI-01 | High cloud dependency on third-party infrastructure requires inherited security controls | GDPR, CRA | Infrastructure | HIGH | Obtain SOC 2 / ISO 27001 evidence from cloud provider; include security clauses in contracts |

**ID Pattern:** `AI-{NN}` where `{NN}` is a 2-digit sequential number.

---

## 8. DATA FLOW SUMMARY

| Data ID | Data Type | Source | Destination | Transfer Method | Encryption | Regulatory Constraint |
|---------|-----------|--------|-------------|-----------------|------------|----------------------|
| `DF-{NN}` | [Type of data] | [Origin system/entity] | [Target system/entity] | [API, File, Stream, etc.] | [Encryption standard / In transit / At rest] | [Applicable regulatory constraint] |
| DF-01 | Customer PII (name, email) | User registration | Database (EU region) | HTTPS / REST API | TLS 1.3 in transit; AES-256 at rest | GDPR Art. 5, 32 — lawfulness, security |

**ID Pattern:** `DF-{NN}` where `{NN}` is a 2-digit sequential number.

---

## 9. COMPLIANCE CAPABILITY ASSESSMENT

| Capability ID | Capability | Current State | Target State | Gap | Priority |
|---------------|------------|---------------|--------------|-----|----------|
| `CAP-{NN}` | [Compliance capability name] | [Current maturity: NONE / AD-HOC / PARTIAL / MATURE] | [Desired maturity level] | [HIGH / MEDIUM / LOW / NONE] | MEDIUM |
| CAP-01 | Records of Processing Activities (RoPA) | NONE | MATURE | HIGH | HIGH — Implement automated logging and template; required by GDPR Art. 30 |

**ID Pattern:** `CAP-{NN}` where `{NN}` is a 2-digit sequential number.

---

## N-1. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-17 | Compliance Lead | Initial template release |
| 1.1 | 2026-04-22 | Compliance Lead | Fixed regulatory applicability (NIS 2/DORA/AI Act: YES→NO), corrected size (10→8 employees, EUR 1M→<€2M), filled 38-question summary (all 38 answered), populated stakeholder register and influence matrix, added business goals catalog |
| 2.2 | 2026-08-06 | Sprint 5 Executor | Deep enrichment — §4 BG table extended from 7 to 13 cols (added Owner, Quantitative Metric, Affected Stakeholders, Status, Risk if not met). NO Effort/Cost/Timeline fields added per Sprint 5 scope. BG-01..BG-05 enriched with operational data. Frontmatter updated: status → DEEP_ENRICHED, sprint → 5.
| 2.0 | 2026-04-23 | Compliance Lead | Converted to layered intake format — removed Q-number summary tables, updated to reference AEGIS Intake Form v2.0 |

## N. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-17 |
| Technical Review | | | |
| Business Review | | | |
| AEGIS Methodology Review | | | |

---

**Next Document:** 05_Regulatory_Applicability.md
**Gate Status:** [PENDING / PASS / FAIL]