---
document_id: AEGIS-P1-07
title: Structured Compliance Matrix
phase: 1
version: 1.1
created: 2026-04-01
updated: 2026-08-06
author: Compliance Lead (Sprint 1 reconciliation)
status: RECONCILED
sprint: 1
sprint_role: reconciled_from_legacy
inputs: [Doc03_Company_Context_Assessment.md, Doc08_Regulatory_Applicability.md, Doc10_Clause_Mapping_Matrix.md]
outputs: [08_Obligation_Derivation.md]
traceability: AEGIS Class Model → ComplianceContext, DomainCoverageEntry classes
related_documents: 00_Taxonomy_Reference.md
---

> **Sprint 1 Reconciliation Note (2026-08-06)**
> Rich Mode copy of legacy `01_PHASE1_CONTEXT/07_Structured_Compliance_Matrix.md` (v1.0). Sprint 1 changes:
> - **I-10 (status DRAFT → RECONCILED):** Sprint 1 milestone.
> - **input pointer:** Changed `06_Clause_Mapping_Matrix.xlsx` → `06_Clause_Mapping_Matrix.md` (Rich Mode uses the markdown shim table from the new §8 Cross-Reference as primary; the xlsx remains authoritative for the underlying numeric matrix in `Case_01_Phase1.xlsx → GDPR_MAPPING` / `CRA_MAPPING` sheets but is now an additional reference, not the primary).
> - **I-13 (02_Regulatory_Mapping_Master.md deprecation):** Not referenced. N/A.
> - Body content unchanged from legacy. Sprint 2 will reconcile the D-07 coverage matrix (41 entries vs 38 expected — see LINT_REPORT_BEFORE.md issue 1) and the 4 missing sole-authority gap rows.

# Structured Compliance Matrix

## 1. DOCUMENT PURPOSE

This document presents the final Phase 1 output (Step C1+C2+C3), consolidating the compliance matrix with complementarity analysis and strategic implications. This is the primary output of Phase 1 and input to Phase 2.

**Alignment with Class Model:**
- `ComplianceContext` - Final applicable regulations with coverage scores
- `DomainCoverageEntry` - Complete 38 sub-domain coverage matrix
- `RegulatoryClause` - Filtered and mapped clauses

**Phase 1 Step:** C (Structured Compliance Matrix)

**Phase 1 Gate:** ✅ COMPLETE when this document is approved

---

## 2. COMPLIANCE MATRIX METADATA

| Attribute | Value |
|-----------|-------|
| complianceMatrixId | CM-TINYTASK-2026-001 |
| completionDate | 2026-04-01 |
| basedOnCompanyContext | CC-TINYTASK-2026-001 |
| basedOnApplicability | COMPLIANCE-TINYTASK-2026-001 |
| basedOnClauseMapping | AEGIS-P1-06 |
| phase1Status | COMPLETE |

---

## 3. SUB-DOMAIN COVERAGE MATRIX (38 Entries)

### D-01: Data Protection & Encryption

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Total | Coverage | NI |
|------------|------|-----|-------|------|--------|-------|----------|-----|
| D-01.1 Data at Rest Encryption | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-01.2 Data in Transit Encryption | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-01.3 Cryptographic Key Management | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-01.4 Data Integrity Mechanisms | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |

### D-02: Vulnerability Management

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Total | Coverage | NI |
|------------|------|-----|-------|------|--------|-------|----------|-----|
| D-02.1 Vulnerability Identification | — | ✅ | — | — | — | 1 | PARTIAL | 3.0 |
| D-02.2 Patch Management & Updates | — | ✅ | — | — | — | 1 | PARTIAL | 3.0 |
| D-02.3 Coordinated Vuln. Disclosure | — | ✅ | — | — | — | 1 | PARTIAL | 3.0 |
| D-02.4 Threat-Led Penetration Testing | — | — | — | — | — | 0 | NOT_ADDRESSED | — |

### D-03: Access Control

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Total | Coverage | NI |
|------------|------|-----|-------|------|--------|-------|----------|-----|
| D-03.1 Identity Lifecycle Management | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-03.2 Multi-Factor Authentication | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-03.3 Authorization & Least Privilege | ✅ | — | — | — | — | 1 | PARTIAL | 3.0 |
| D-03.4 Secure System Defaults | — | ✅ | — | — | — | 1 | PARTIAL | 3.0 |

### D-04: Incident Response

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Total | Coverage | NI |
|------------|------|-----|-------|------|--------|-------|----------|-----|
| D-04.1 Incident Detection & Triage | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-04.2 Containment & Mitigation | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-04.3 Regulatory Notification | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-04.4 Data Restoration & Recovery | ✅ | — | — | — | — | 1 | PARTIAL | 3.0 |

### D-05: Data Lifecycle

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Total | Coverage | NI |
|------------|------|-----|-------|------|--------|-------|----------|-----|
| D-05.1 Data Minimization | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-05.2 Retention & Archiving | ✅ | — | — | — | — | 1 | PARTIAL | 3.0 |
| D-05.3 Right to Erasure | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-05.4 Data Portability | ✅ | — | — | — | — | 1 | PARTIAL | 3.0 |

### D-06: Supply Chain

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Total | Coverage | NI |
|------------|------|-----|-------|------|--------|-------|----------|-----|
| D-06.1 Vendor Risk Assessment | ✅ | — | — | — | — | 1 | PARTIAL | 3.0 |
| D-06.2 Software Bill of Materials (SBOM) | — | ✅ | — | — | — | 1 | PARTIAL | 3.0 |
| D-06.3 Contractual Security Obligations | ✅ | — | — | — | — | 1 | PARTIAL | 3.0 |
| D-06.4 Third-Party Boundary Management | — | — | — | — | — | 0 | NOT_ADDRESSED | — |

### D-07: Secure Development

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Total | Coverage | NI |
|------------|------|-----|-------|------|--------|-------|----------|-----|
| D-07.1 Secure-by-Design Principles | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-07.2 Secure Coding Practices | — | ✅ | — | — | — | 1 | PARTIAL | 3.0 |
| D-07.3 CI/CD Pipeline Security | — | ✅ | — | — | — | 1 | PARTIAL | 3.0 |
| D-07.4 Change Management | — | ✅ | — | — | — | 1 | PARTIAL | 3.0 |

### D-08: Human Factors

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Total | Coverage | NI |
|------------|------|-----|-------|------|--------|-------|----------|-----|
| D-08.1 General Security Awareness | ✅ | — | — | — | — | 1 | PARTIAL | 3.0 |
| D-08.2 Role-Specific Competence | ✅ | — | — | — | — | 1 | PARTIAL | 3.0 |
| D-08.3 Management Board Training | — | — | — | — | — | 0 | NOT_ADDRESSED | — |

### D-09: Governance & Documentation

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Total | Coverage | NI |
|------------|------|-----|-------|------|--------|-------|----------|-----|
| D-09.1 Information Security Policies | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-09.2 Impact & Risk Assessments | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-09.3 Asset Inventories | — | ✅ | — | — | — | 1 | PARTIAL | 3.0 |
| D-09.4 Records of Processing | ✅ | — | — | — | — | 1 | PARTIAL | 3.0 |

### D-10: Monitoring & Audit

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Total | Coverage | NI |
|------------|------|-----|-------|------|--------|-------|----------|-----|
| D-10.1 Continuous Security Monitoring | — | ✅ | — | — | — | 1 | PARTIAL | 3.0 |
| D-10.2 Audit Logging & Traceability | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |
| D-10.3 Compliance Testing | ✅ | ✅ | — | — | — | 2 | SUBSTANTIVE | 3.0 |

---

## 4. COVERAGE SUMMARY DASHBOARD

| Metric | Value | Formula |
|--------|-------|---------|
| Total Sub-Domains | 38 | Fixed |
| Substantive Coverage (≥2 regs) | 16 | COUNTIF(Coverage, "SUBSTANTIVE") |
| Partial Coverage (1 reg) | 19 | COUNTIF(Coverage, "PARTIAL") |
| Not Addressed (0 regs) | 3 | COUNTIF(Coverage, "NOT_ADDRESSED") |
| Coverage Percentage | 92.1% | (Substantive + Partial) / 38 |
| Total Applicable Clauses | 54 | GDPR (28) + CRA (26) |
| Average Normative Intensity | 2.947 | AVERAGE(NI column) |
| Sole Authority Gaps | 3 | D-02.4, D-06.4, D-08.3 |

---

## 5. COMPLEMENTARITY ANALYSIS (C2)

### 5.1 Cross-Regulation Overlap

| Regulation Pair | Shared Sub-Domains | Overlap % | Synergy Opportunities |
|-----------------|-------------------|-----------|----------------------|
| GDPR + CRA | D-01, D-03, D-04, D-05, D-07, D-09, D-10 | 70% | Single encryption standard satisfies both |

### 5.2 Complementarity Opportunities

| Opportunity ID | Sub-Domain | Regulations Involved | Description | Implementation Benefit |
|----------------|------------|---------------------|-------------|------------------------|
| CO-001 | D-01 (Encryption) | GDPR + CRA | Unified encryption standard | Single implementation satisfies both |
| CO-002 | D-04 (Incident Response) | GDPR + CRA | Coordinated incident process | One process, dual compliance |
| CO-003 | D-09 (Governance) | GDPR + CRA | Integrated policy framework | Reduced documentation overhead |

### 5.3 Conflict Classification (Structural vs Contextual)

Overlaps between regulations create three types of relationships:

| Relationship Type | Definition | Sub-Domains | Example |
|-------------------|-----------|-------------|---------|
| **Synergistic** (Complementarity) | Two regulations reinforce each other with compatible requirements | D-01.1, D-01.2, D-01.4, D-03.1, D-05.1 | GDPR+CRA both require encryption → single AES-256 standard satisfies both |
| **Structural Tension** | Two regulations apply permanently with differing requirements; resolved once at design level | D-07.1, D-09.2 | GDPR "appropriate measures" (NI=2) vs CRA "secure by default" (NI=3) |
| **Contextual Tension** | Two regulations may conflict only when the same factual event triggers both; resolved per-event | D-04.3 | GDPR 72h (personal data breach) vs CRA 24h (exploited vulnerability) — only when same incident involves both |

### 5.4 Compound Event Scenarios

This section identifies **factual events** that can simultaneously trigger obligations from multiple regulations. A compound event exists when a single incident satisfies the trigger conditions of two or more regulatory clauses in the same sub-domain.

**Why this matters:** Compound events are the source of contextual tensions. They are NOT inherent to the regulations — they emerge from the interaction between the company's operational profile and the regulatory triggers that apply to it.

| Event ID | Compound Event Description | Regulations Triggered | Sub-Domain | Tension Created | Resolution Required |
|----------|--------------------------|----------------------|------------|-----------------|-------------------|
| EVT-001 | Attacker exploits product vulnerability AND exfiltrates personal data | GDPR (personal data breach) + CRA (actively exploited vuln) | D-04.3 | T-H-001 (TEMPORAL_CONFLICT: 72h vs 24h) | Max-SLA Routing — 24h workflow satisfies both |
| EVT-002 | Product launch involves high-risk personal data processing | GDPR (DPIA trigger) + CRA (risk assessment trigger) | D-09.2 | T-M-001 (FREQUENCY_MISMATCH) | Unified assessment — single document, dual outputs |
| EVT-003 | New feature designed that processes personal data | GDPR (data protection by design) + CRA (secure by default) | D-07.1 | T-M-002 (INTENSITY_GAP: NI=2 vs NI=3) | Follow CRA higher bar — satisfies both |

**Events that do NOT create compound scenarios (parallel obligations only):**

| Scenario | Triggers GDPR? | Triggers CRA? | Tension? | Why Not |
|----------|---------------|---------------|----------|---------|
| Employee accidentally emails customer list to wrong recipient | ✅ Yes (personal data breach) | ❌ No | No | No exploited product vulnerability |
| XSS vulnerability in task rendering engine (no data access) | ❌ No | ✅ Yes (exploited vuln) | No | No personal data involved |
| User requests data erasure | ✅ Yes (GDPR-C06) | ✅ Yes (CRA-C16) | No | Same right, same timeline — no conflict |

**Cross-case implication:** The number of compound event scenarios grows with the number of applicable regulations. Case 1 (2 regs) has 3 compound scenarios. Case 3 (5 regs) could have 10+.

---

## 6. STRATEGIC IMPLICATIONS (C3)

| Implication ID | Sub-Domain | Source Regulation(s) | Description | Architectural Impact | Priority |
|----------------|------------|---------------------|-------------|---------------------|----------|
| SI-001 | D-01 | GDPR, CRA | Dual encryption requirements | Single standard (AES-256) satisfies both | HIGH |
| SI-002 | D-06.2 | CRA | SBOM requirement new | Need dependency scanning in CI/CD | HIGH |
| SI-003 | D-05 | GDPR | Data subject rights | User-facing export/delete functionality | MEDIUM |
| SI-004 | D-02.3 | CRA | Vulnerability disclosure | security.txt + contact email | MEDIUM |

---

## 7. IDENTIFIED GAPS SUMMARY

| Gap ID | Sub-Domain | Regulation | Clause | Gap Type | Risk Level | Recommended Action |
|--------|------------|------------|--------|----------|------------|-------------------|
| GAP-001 | D-09.4 | GDPR | Art.30 | NOT_ADDRESSED | HIGH | Create RoPA template |
| GAP-002 | D-01 | GDPR | Art.32 | PARTIAL_COVERAGE | MEDIUM | Document security controls |
| GAP-003 | D-06.2 | CRA | Art.18 | NOT_ADDRESSED | HIGH | Implement SBOM tooling |
| GAP-004 | D-02.3 | CRA | Art.21 | NOT_ADDRESSED | MEDIUM | Create security.txt |

**Gap Summary:**
- HIGH Risk Gaps: 2 (D-09.4, D-06.2)
- MEDIUM Risk Gaps: 2 (D-01, D-02.3)
- LOW Risk Gaps: 0

---

## 8. PHASE 1 GATE CRITERIA CHECKLIST

| Criterion | Status | Evidence |
|-----------|--------|----------|
| All 38 questions answered (04) | ✅ COMPLETE | Section 5 of 04_Company_Context_Assessment.md |
| All 5 regulations assessed (05) | ✅ COMPLETE | Section 3 of 05_Regulatory_Applicability.md |
| Clause mapping complete (06) | ✅ COMPLETE | 06_Clause_Mapping_Matrix.xlsx |
| Sub-domain coverage complete | ✅ COMPLETE | Section 3 of this document |
| Gaps identified and prioritized | ✅ COMPLETE | Section 7 of this document |
| Strategic implications documented | ✅ COMPLETE | Section 6 of this document |
| Design decisions logged (03) | ⏳ PENDING | To be completed in 03_Design_Decisions_Log.md |

**Phase 1 Gate Decision:** ✅ PASS (pending design decisions log)

**Gate Review Date:** TBD

**Gate Reviewers:**
- Compliance Lead: _________________
- Technical Review (CTO): _________________
- AEGIS Methodology Review: _________________

---

## 9. INPUT TO PHASE 2

The following artifacts are passed to Phase 2:

| Artifact | Document Reference | Purpose in Phase 2 |
|----------|-------------------|-------------------|
| Applicable Regulations | Section 3 | Filter for obligation derivation (GDPR, CRA) |
| Sub-Domain Coverage Matrix | Section 3 | Rules Catalog organization |
| Clause Mapping | 06_Clause_Mapping_Matrix.xlsx | Source for AbstractNFR derivation |
| Strategic Implications | Section 6 | Input for Strategic Tension detection |
| Identified Gaps | Section 7 | Priority input for Rules Catalog |

---

## 10. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | Compliance Lead | Initial release - TinyTask SaaS case |

---

## 11. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-01 |
| Technical Review (CTO) | | | |
| Business Review (CEO) | | | |
| AEGIS Methodology Review | | | |

---

**Phase 1 Status:** ✅ COMPLETE
**Next Phase:** 02_PHASE2_RULES → 08_Obligation_Derivation.md
