---
document_id: AEGIS-P3-RICH-24-REV
title: NFR Review Report (ported from legacy, reconciled to P2-RICH)
phase: 3
version: 0.3
created: 2026-08-24
updated: 2026-08-24
author: Sprint 4 Executor (paulo@methodology.pt)
status: ADJUSTED_FIELDS
sprint: 4
sprint_role: schema_adjustment
case: Case_01_TinyTask_SaaS
tier: MICRO
sibling_of: ../03_PHASE3_DECOMPOSITION/requirements/24_NFR_Review_Report.md
branch: feature/aegis-p3-case01-rich
inputs: [requirements/24_Non_Functional_Requirements.md, RULE_FREEZE.md, ../02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md]
outputs: [requirements/24_Non_Functional_Requirements.md, validation/SPRINT1_REPORT.md]
related_documents: [requirements/23_FR_Review_Report.md]
expected_documents: 24
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Maturity, Priority, Stakeholders, Reporting]
reconciliation_note: "Ported from legacy 24_NFR_Review_Report.md (2026-04-02). F-00b NFR RESOLVED — 46 NFRs (NFR-01..NFR-46) confirmed by §3 row re-count, NOT stale 45 figure; F-S1-09 KG contamination (concept_ai_model_security / nfr_avail_category) recorded."
sprint4_note: "Sprint 4: review-report status bumped RECONCILED → ADJUSTED_FIELDS. Review tables remain as legacy-port (no markdown restructuring) — Sprint 5 will harmonise with Doc 24 §2 schema."
---

> **PORTED FROM LEGACY on 2026-08-24 for Sprint 1; reconciled to P2-RICH upstream.**
>
> This document is a verbatim port of the legacy `03_PHASE3_DECOMPOSITION/requirements/24_NFR_Review_Report.md`
> (286 lines, dated 2026-04-02, reviewer: Security Architect).
> It is preserved for traceability — Sprint 5 will produce an amendment §10 listing the corrected
> NFR count (46, not 45) and re-confirming the §3.4 verdict. The legacy review's verdict
> (APPROVED WITH MINOR REVISIONS) is preserved as-is; it speaks to the v1.0 NFR catalog,
> not the post-Sprint 1 freeze.

# NFR Catalog Review & Validation Report

**Document ID:** AEGIS-P3-24-REVIEW  
**Date:** 2026-04-02  
**Reviewer:** Security Architect  
**Document Reviewed:** 24_Non_Functional_Requirements.md (v1.0)  
**Status:** ✅ APPROVED WITH MINOR REVISIONS  

---

## 1. EXECUTIVE SUMMARY

| Category | Status | Issues Found | Severity |
|----------|--------|--------------|----------|
| **Completeness** | ✅ Complete | 0 gaps | — |
| **Consistency** | ✅ Consistent | 2 minor inconsistencies | LOW |
| **Measurability** | ✅ Complete | 0 issues | — |
| **Regulatory Coverage** | ✅ Complete | 0 gaps | — |
| **Use Case Traceability** | ✅ Complete | 0 gaps | — |
| **Feasibility (TinyTask)** | ✅ Feasible | 3 stretch goals | MEDIUM |
| **PhD Alignment** | ✅ Aligned | 0 issues | — |

**Overall Status:** ✅ **APPROVED WITH MINOR REVISIONS**

---

## 2. VALIDATION CRITERIA

### 2.1 PhD Requirements (NFR→FR Transformation)

| Criterion | Status | Evidence |
|-----------|--------|----------|
| NFRs derived from regulations | ✅ | Section 6 (NFR→Regulation Traceability) |
| NFRs mapped to Use Cases | ✅ | Section 5 (NFR→Use Case Traceability) |
| All NFRs measurable | ✅ | Section 4.1 (100% measurability) |
| NFRs feasible for context | ✅ | Section 7 (Feasibility Assessment) |
| NFRs prioritized | ✅ | Section 8 (MoSCoW Prioritization) |
| NFRs ready for FR derivation | ✅ | Section 9 (Preliminary NFR→FR Mapping) |

**PhD Alignment:** ✅ All requirements satisfied

### 2.2 AEGIS Methodology Requirements

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Based on Phase 1 Compliance Matrix | ✅ | Based on 07_Structured_Compliance_Matrix.md |
| Based on Phase 2 Security Goals | ✅ | Based on 10_Privacy_Security_Objectives.md |
| NFR categories (CIA + Privacy) | ✅ | 6 categories: CONF, INT, AVAIL, PRIV, ACC, COMP |
| Traceability to regulations | ✅ | GDPR, CRA, NIS2 mapped |
| Ready for Phase 3 FR specification | ✅ | Section 9 provides preliminary mapping |

**AEGIS Alignment:** ✅ All requirements satisfied

---

## 3. DETAILED REVIEW

### 3.1 NFR Catalog Completeness

| Category | NFR Count | Expected | Status |
|----------|-----------|----------|--------|
| Confidentiality | 7 | ≥5 | ✅ Complete |
| Integrity | 7 | ≥5 | ✅ Complete |
| Availability | 7 | ≥5 | ✅ Complete |
| Privacy (GDPR) | 10 | ≥8 | ✅ Complete |
| Accountability | 7 | ≥5 | ✅ Complete |
| Compliance | 8 | ≥5 | ✅ Complete |
| **TOTAL** | **46** | ≥33 | ✅ Complete |

> **Sprint 1 reconciliation note (F-00b NFR RESOLVED):** Re-counted the NFR table rows in legacy Doc 24 §3:
> CONF (7) + INT (7) + AVAIL (7) + PRIV (10) + ACC (7) + COMP (8) = **46 NFRs** (NFR-01..NFR-46).
> The legacy §5.1 cross-doc table says "45/46 NFRs satisfied (98%)" referring to a phantom
> `NFR-PRIV-04` process-control NFR that doesn't exist in §3 — this is a legacy summary
> drift, not a real gap. Sprint 5 will populate **46 detail cards × 17 fields = 782 cells**
> per RULE_FREEZE.md §7.

**Assessment:** All categories have sufficient coverage

### 3.2 Measurability Assessment

**Sample Check (10 NFRs reviewed in detail):**

| NFR ID | Requirement | Measurement Criteria | Measurable? | Testable? |
|--------|-------------|---------------------|-------------|-----------|
| NFR-CONF-01 | Protect from unauthorized access | MFA mandatory for admin accounts; privileged access reviewed quarterly | ✅ | ✅ |
| NFR-PRIV-01 | DSAR access | 7 days (target), 30 days (max) | ✅ | ✅ |
| NFR-PRIV-02 | Erasure | 7 days (target), 30 days (max) | ✅ | ✅ |
| NFR-AVAIL-01 | 99.5% uptime | 99.5% measured via CloudWatch; downtime alerted within 15 min | ✅ | ✅ |
| NFR-AVAIL-02 | Recovery | RTO < 24h (manual), RPO < 4h (automated backups); DR tested annually | ✅ | ✅ |
| NFR-INT-01 | Data accuracy | All external user inputs validated; validation errors reviewed monthly | ✅ | ✅ |
| NFR-ACC-01 | Log security events | Authentication, authorization, data modification events logged; monthly review | ✅ | ✅ |
| NFR-COMP-03 | NIS2 incident reporting | Incident reports within 24h (actively exploited) / 72h (authorities) | ✅ | ✅ |
| NFR-CONF-06 | Session timeout | 30 minutes inactivity | ✅ | ✅ |
| NFR-PRIV-10 | DPIA | DPIA completed before high-risk processing | ✅ | ✅ |

**Measurability:** ✅ 100% of sampled NFRs are measurable and testable

### 3.3 Regulatory Coverage

| Regulation | Articles/Requirements | NFRs Mapped | Coverage |
|------------|----------------------|-------------|----------|
| **GDPR** | 16 articles | 28 NFRs | ✅ 100% |
| **CRA** | 6 requirements | 15 NFRs | ✅ 100% |
| **NIS2** | 2 articles | 3 NFRs | ✅ 100% |

**Note:** NIS2 not applicable to TinyTask (below 50 employees), but mapped for completeness

**Regulatory Coverage:** ✅ Complete

### 3.4 Use Case Traceability

| Metric | Value | Expected | Status |
|--------|-------|----------|--------|
| Total Use Cases | 24 | — | — |
| Use Cases with NFRs | 24 | 24 | ✅ 100% |
| NFRs with Use Cases | 46 | 46 | ✅ 100% |

> **Sprint 1 reconciliation note:** UC count = 35 L1 cards (per Doc 16 §5B SC2 + Synthesis §3.3);
> the §3.4 "24 Use Cases" figure refers to a subset of Use Cases that appear in the NFR table
> §5.2 (UCs with at least one NFR mapping), not the full UC catalog. Both figures are
> internally consistent at the freeze.

**Sample Check:**

| Use Case | Related NFRs | Coverage |
|----------|--------------|----------|
| U.C.1.1.1 (DSAR) | NFR-PRIV-01, NFR-AVAIL-07 | ✅ Complete |
| U.C.1.2.1 (Erasure) | NFR-PRIV-02 | ✅ Complete |
| U.C.3.1.1 (Authentication) | 7 NFRs (CONF, INT, AVAIL, ACC) | ✅ Complete |
| U.C.2.7.1 (BC/DR) | 6 NFRs (AVAIL, INT) | ✅ Complete |
| U.C.5.7.1 (Regulatory Notification) | 3 NFRs (PRIV, COMP) | ✅ Complete |

**Use Case Traceability:** ✅ Complete

---

## 4. FEASIBILITY ASSESSMENT (TinyTask Context)

### 4.1 Resource Requirements

| Issue | NFR | Current SLA | Recommended | Impact |
|-------|-----|-------------|-------------|--------|
| **FEAS-001** | NFR-PRIV-01 (DSAR) | 7 days target | Keep 7 days target, 30 days max | ⚠️ Stretch goal (manual process) |
| **FEAS-002** | NFR-PRIV-02 (Erasure) | 7 days target | Keep 7 days target, 30 days max | ⚠️ Stretch goal (manual process) |
| **FEAS-003** | NFR-AVAIL-01 (99% uptime) | 99% business hours | ✅ Feasible with AWS | — |

**Assessment:** 
- 2 stretch goals (DSAR/Erasure 7-day target) — acceptable since 30-day max is compliant
- Overall feasible for 8-person team with MSSP

### 4.2 Tool Gaps

| NFR Category | Tool Gap | Priority | Recommendation |
|--------------|----------|----------|----------------|
| Privacy | DSAR automation | MEDIUM | Implement DSAR tool (e.g., OneTrust, DataGrail) |
| Compliance | GRC platform | MEDIUM | Implement lightweight GRC (e.g., Vanta, Drata) |
| Availability | MSSP for 24/7 monitoring | HIGH | Contract MSSP for incident detection |

**Recommendation:** Prioritize MSSP contract before Phase 3 FR implementation

---

## 5. CONSISTENCY CHECK

### 5.1 Internal Consistency

| Issue | Location | Description | Recommendation |
|-------|----------|-------------|----------------|
| **CONSIST-001** | Section 3.1 | NFR-CONF-07 mentions "DEV-03" but should also reference "IAM-02" | Add U.C.3.1.1 to Source UC |
| **CONSIST-002** | Section 8.1 | MoSCoW counts don't sum to 46 (13+23+10=46) | ✅ Actually correct — no action needed |

**Assessment:** 1 minor inconsistency — trivial fix

### 5.2 Cross-Document Consistency

| Document | Consistency Check | Status |
|----------|-------------------|--------|
| 13_Use_Cases_Catalog.md (v2.1) | All 35 UCs mapped | ✅ Consistent |
| 10_Privacy_Security_Goals.md | All goals reflected in NFRs | ✅ Consistent |
| 07_Structured_Compliance_Matrix.md | All obligations covered | ✅ Consistent |

**Assessment:** ✅ Consistent with source documents

---

## 6. PHD ALIGNMENT CHECK

### 6.1 NFR→FR Transformation Readiness

| Criterion | Status | Evidence |
|-----------|--------|----------|
| NFRs are atomic | ✅ | Each NFR addresses single quality attribute |
| NFRs are unambiguous | ✅ | Clear, precise language |
| NFRs have measurable criteria | ✅ | All 46 NFRs have quantifiable metrics |
| NFRs are traceable to source | ✅ | Regulations, Use Cases mapped |
| NFRs are feasible | ✅ | Feasibility assessment complete |
| NFRs ready for FR derivation | ✅ | Section 9 provides preliminary mapping |

**PhD Readiness:** ✅ Ready for FR derivation

### 6.2 Knowledge Graph Integration Points

| NFR Category | KG Integration Potential | Status |
|--------------|-------------------------|--------|
| Confidentiality | D3FEND: D3-DE (Data Encryption) | ✅ Mappable |
| Integrity | D3FEND: D3-CO (Code Signing) | ✅ Mappable |
| Availability | D3FEND: D3-RR (Resource Reservation) | ✅ Mappable |
| Privacy | GDPR ontology mapping | ✅ Mappable |
| Accountability | D3FEND: D3-AL (Alerting) | ✅ Mappable |
| Compliance | Regulatory ontology mapping | ✅ Mappable |

**KG Readiness:** ✅ Ready for KG-based inference (Phase 3 Risk Analysis)

---

## 7. ISSUES SUMMARY

### 7.1 Issues by Severity

| Severity | Count | Issues |
|----------|-------|--------|
| **CRITICAL** | 0 | — |
| **HIGH** | 0 | — |
| **MEDIUM** | 3 | FEAS-001, FEAS-002, FEAS-003 (stretch goals) |
| **LOW** | 2 | CONSIST-001, CONSIST-002 |
| **TOTAL** | **5** | — |

### 7.2 Required Actions

| Priority | Action | Issue | Owner | Due |
|----------|--------|-------|-------|-----|
| **MEDIUM** | Document DSAR/Erasure feasibility (7 days vs 30 days) | FEAS-001, FEAS-002 | Security Architect | Before FR spec |
| **MEDIUM** | Prioritize MSSP contract | FEAS-003 | CTO | Before FR spec |
| **LOW** | Fix NFR-CONF-07 Source UC | CONSIST-001 | Security Architect | Next revision |

---

## 8. RECOMMENDATIONS

### 8.1 Must Do (Before FR Specification)

1. ✅ **Document DSAR/Erasure process:**
   - Current: Manual process
   - Target: 7 days (stretch), 30 days (compliant)
   - Action: Document manual process, plan for automation

2. ✅ **Prioritize MSSP contract:**
   - Required for: 24/7 monitoring (NFR-AVAIL-03, NFR-COMP-03)
   - Timeline: Before FR implementation
   - Action: Initiate MSSP vendor selection

### 8.2 Should Do (Recommended)

3. **Implement DSAR automation tool:**
   - Current: Manual (feasible but slow)
   - Target: Automated DSAR response
   - Timeline: Phase 2 implementation

4. **Implement GRC platform:**
   - Current: Manual documentation
   - Target: Automated compliance tracking
   - Timeline: Phase 2 implementation

### 8.3 Nice to Do (Optional)

5. **Add NFR-COMP-09 (Vendor Management):**
   - GDPR Art. 28 (processor agreements)
   - Currently covered by U.C.5.5.1
   - Optional enhancement

---

## 9. APPROVAL STATUS

| Role | Name | Status | Date | Comments |
|------|------|--------|------|----------|
| Document Author | Security Architect | ✅ Complete | 2026-04-02 | — |
| Technical Review (CTO) | | ⏳ Pending | | — |
| Business Review (CEO) | | ⏳ Pending | | — |
| Compliance Review (DPO) | | ⏳ Pending | | — |
| Security Review | Security Architect | ✅ Approved | 2026-04-02 | Minor revisions required |
| AEGIS Methodology Review | | ⏳ Pending | | — |
| PhD Supervisor Review | | ⏳ Pending | | — |

**Overall Status:** ✅ **APPROVED WITH MINOR REVISIONS**

**Next Steps:**
1. Address MEDIUM priority actions (DSAR/Erasure documentation, MSSP contract)
2. Fix LOW priority inconsistency (NFR-CONF-07)
3. Proceed to FR specification (23_Functional_Requirements.md)
4. Obtain CTO/DPO approval

---

**Review Completed:** 2026-04-02  
**Review Duration:** 1.5 hours  
**Issues Found:** 5 (0 Critical, 0 High, 3 Medium, 2 Low)  
**Recommendation:** ✅ PROCEED TO FR SPECIFICATION

---

> **Sprint 1 reconciliation footer (2026-08-24):** Ported as-is from legacy for traceability.
> F-00b NFR CLOSED (46 NFRs confirmed), F-S1-09 KG contamination (`concept_ai_model_security`, `nfr_avail_category`)
> recorded in RULE_FREEZE.md §4 (KG artefacts, NOT in markdown source).
> Sprint 5 will produce a §10 amendment listing the corrected NFR count and KG cleanup actions.
