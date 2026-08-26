---
document_id: AEGIS-P3-RICH-07-MATRIX
title: Structured Compliance Matrix (Rich Mode)
phase: 1
version: 1.1
created: 2026-04-01
updated: 2026-08-06
author: Compliance Lead (Sprint 1 reconciliation copy)
status: RECONCILED
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
inactive_documented: []
inputs: [04_Company_Context_Assessment.md, 05_Regulatory_Applicability.md, 06_Clause_Mapping_Matrix.md]
outputs: [08_Obligation_Derivation.md]
traceability: AEGIS Class Model → StructuredComplianceMatrix, DomainCoverageEntry classes
related_documents: [00_Taxonomy_Reference.md, 06b_DORA_ICT_Risk_Framework.md, 07b_Proportionality_Profile.md]
sibling_of: ../01_PHASE1_CONTEXT/07_Structured_Compliance_Matrix.md
reconciliation_notes:
  - "Sprint 1 (2026-08-06): Copied from 01_PHASE1_CONTEXT/07_Structured_Compliance_Matrix.md → Rich folder; frontmatter migrated to AEGIS-P3-RICH-* prefix; status DRAFT → RECONCILED; inputs updated to reference 06_Clause_Mapping_Matrix.md (not .xlsx). 5 strategic tensions preserved: T-001..T-004 (pre-existing) + T-005 (NEW for DORA TLPT cycle from Sprint 0.6 Doc 06b §4.5) — added to Section 5.5. 9 case-specific sections (5.1-5.5 + 6.1-6.3 + 8) marked as by-design MAX extensions. Body largely unchanged — section 5.5 enriched to register T-005."
---

<!-- RECONCILED (Sprint 1, 2026-08-06): Document copied from legacy 01_PHASE1_CONTEXT/07_Structured_Compliance_Matrix.md to Rich folder.
Changes: (a) document_id migrated to AEGIS-P3-RICH-07-MATRIX; (b) status DRAFT → RECONCILED;
(c) inputs updated: 06_Clause_Mapping_Matrix.xlsx → 06_Clause_Mapping_Matrix.md (Sprint 1 I-C03-01 RESOLVED);
(d) Tension T-005 ADDED to §5.5 (DORA TLPT Triennial Cycle vs ISO 27001 Annual Testing Cycle, from Sprint 0.6 Doc 06b §4.5);
(e) Tensions T-001..T-004 marked as case-specific (NOT in ground-truth ontology per legacy lint baseline I-C03-02 — Sprint 2+ candidate to register in ontology).
Body content largely unchanged — Compliance Matrix (38 sub-domains × 5 regulations × 150 clauses) preserved verbatim; 5.5 enriched with T-005.
-->

---

# Structured Compliance Matrix

## 1. DOCUMENT PURPOSE

This document presents the final Phase 1 output (Step C1+C2+C3), consolidating the compliance matrix with complementarity analysis and strategic implications. This is the primary output of Phase 1 and input to Phase 2.

**Alignment with Class Model:**
- `StructuredComplianceMatrix` - Complete 38 sub-domain coverage matrix
- `DomainCoverageEntry` - Individual sub-domain entries
- `ComplementarityAnalysis` - Cross-regulation overlap analysis

**Phase 1 Step:** C (Structured Compliance Matrix)

**Phase 1 Gate:** ✅ COMPLETE when this document and 06_Clause_Mapping_Matrix.xlsx are approved

---

## 2. COMPLIANCE MATRIX METADATA

| Attribute | Value |
|-----------|-------|
| matrixId | SCM-OMNIBANK-2026-001 |
| analysisDate | 2026-04-01 |
| version | 1.0 |
| companyContextId | CC-OMNIBANK-2026-001 |
| complianceContextId | COMPLIANCE-OMNIBANK-2026-001 |
| applicableRegulations | GDPR, CRA, NIS 2, DORA, AI Act (ALL 5) |
| excludedRegulations | NONE |
| totalSubDomains | 38 |
| coveredSubDomains | 38 (100%) |
| uncoveredSubDomains | 0 (0%) |
| totalClauses | 150 (GDPR 28 + CRA 26 + NIS 2 29 + DORA 38 + AI Act 29) |
| nativeCompliance | TBD (Phase 2) |
| inheritedCompliance | TBD (Phase 2) |
| hybridCompliance | TBD (Phase 2) |

---

## 3. SUB-DOMAIN COVERAGE MATRIX (38 Entries)

### D-01: Data Protection & Encryption

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Coverage Level | Native/Inherited | Clause Count | Primary Owner |
|------------|------|-----|-------|------|--------|----------------|------------------|--------------|---------------|
| **D-01.1** Data at Rest Encryption | S (2) | P (1) | P (1) | P (1) | P (1) | **SUBSTANTIVE** | Hybrid (Cloud) | 6 | CISO |
| **D-01.2** Data in Transit Encryption | P (1) | P (1) | P (1) | P (1) | P (1) | **SUBSTANTIVE** | Hybrid (Cloud) | 5 | CISO |
| **D-01.3** Cryptographic Key Management | — | P (1) | P (1) | P (1) | P (1) | **SUBSTANTIVE** | Native | 4 | CISO |
| **D-01.4** Data Integrity Mechanisms | P (1) | P (1) | — | P (1) | P (1) | **SUBSTANTIVE** | Native | 4 | CTO |

**D-01 Summary:** 4/4 sub-domains covered (100%) | 19 total clauses | Hybrid + Native

---

### D-02: Vulnerability Management

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Coverage Level | Native/Inherited | Clause Count | Primary Owner |
|------------|------|-----|-------|------|--------|----------------|------------------|--------------|---------------|
| **D-02.1** Vulnerability Identification | — | S (2) | P (1) | P (1) | P (1) | **SUBSTANTIVE** | Native | 5 | CTO |
| **D-02.2** Patch Management & Updates | — | S (2) | P (1) | P (1) | — | **SUBSTANTIVE** | Native | 4 | DevOps |
| **D-02.3** Coordinated Vuln. Disclosure | — | S (2) | P (1) | — | — | **SUBSTANTIVE** | Native | 3 | CISO |
| **D-02.4** Threat-Led Penetration Testing | — | — | P (1) | P (1) | P (1) | **SUBSTANTIVE** | Native | 3 | CISO |

**D-02 Summary:** 4/4 sub-domains covered (100%) | 15 total clauses | All Native

---

### D-03: Access Control

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Coverage Level | Native/Inherited | Clause Count | Primary Owner |
|------------|------|-----|-------|------|--------|----------------|------------------|--------------|---------------|
| **D-03.1** Identity Lifecycle Management | — | P (1) | P (1) | P (1) | P (1) | **SUBSTANTIVE** | Hybrid (IdP) | 4 | CTO |
| **D-03.2** Multi-Factor Authentication | — | P (1) | P (1) | P (1) | P (1) | **SUBSTANTIVE** | Hybrid (IdP) | 4 | CTO |
| **D-03.3** Authorization & Least Privilege | S (2) | — | P (1) | P (1) | — | **SUBSTANTIVE** | Native | 3 | CTO |
| **D-03.4** Secure System Defaults | — | P (1) | — | — | — | **PARTIAL** | Native | 1 | CTO |

**D-03 Summary:** 4/4 sub-domains covered (100%) | 12 total clauses | Hybrid + Native

---

### D-04: Incident Response

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Coverage Level | Native/Inherited | Clause Count | Primary Owner |
|------------|------|-----|-------|------|--------|----------------|------------------|--------------|---------------|
| **D-04.1** Incident Detection & Triage | — | P (1) | P (1) | P (1) | P (1) | **SUBSTANTIVE** | Native (SOC) | 4 | CISO |
| **D-04.2** Containment & Mitigation | P (1) | P (1) | P (1) | P (1) | — | **SUBSTANTIVE** | Native | 4 | CISO |
| **D-04.3** Regulatory Notification | S (2) | P (1) | S (3) | P (1) | P (1) | **SUBSTANTIVE** | Native | 8 | CEO |
| **D-04.4** Data Restoration & Recovery | P (1) | — | P (1) | P (1) | — | **SUBSTANTIVE** | Native | 3 | DevOps |

**D-04 Summary:** 4/4 sub-domains covered (100%) | 19 total clauses | All Native | **TENSION:** D-04.3 (24h vs 72h)

---

### D-05: Data Lifecycle

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Coverage Level | Native/Inherited | Clause Count | Primary Owner |
|------------|------|-----|-------|------|--------|----------------|------------------|--------------|---------------|
| **D-05.1** Data Minimization | P (1) | P (1) | — | — | P (1) | **SUBSTANTIVE** | Native | 3 | DPO |
| **D-05.2** Retention & Archiving | S (2) | — | — | — | P (1) | **PARTIAL** | Native | 3 | DPO |
| **D-05.3** Right to Erasure | P (1) | P (1) | — | — | — | **PARTIAL** | Native | 2 | DPO |
| **D-05.4** Data Portability | P (1) | — | — | — | — | **PARTIAL** | Native | 1 | DPO |

**D-05 Summary:** 4/4 sub-domains covered (100%) | 9 total clauses | All Native | GDPR-dominant

---

### D-06: Supply Chain

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Coverage Level | Native/Inherited | Clause Count | Primary Owner |
|------------|------|-----|-------|------|--------|----------------|------------------|--------------|---------------|
| **D-06.1** Vendor Risk Assessment | P (1) | — | P (1) | P (1) | — | **SUBSTANTIVE** | Hybrid | 3 | CISO |
| **D-06.2** SBOM | — | P (1) | — | — | — | **PARTIAL** | Native | 1 | CTO |
| **D-06.3** Contractual Security Obligations | P (1) | — | P (1) | P (1) | — | **SUBSTANTIVE** | Hybrid | 3 | Legal |
| **D-06.4** Third-Party Boundary Management | — | — | P (1) | P (1) | — | **PARTIAL** | Native | 2 | CISO |

**D-06 Summary:** 4/4 sub-domains covered (100%) | 9 total clauses | Hybrid + Native

---

### D-07: Secure Development

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Coverage Level | Native/Inherited | Clause Count | Primary Owner |
|------------|------|-----|-------|------|--------|----------------|------------------|--------------|---------------|
| **D-07.1** Secure-by-Design Principles | P (1) | S (2) | P (1) | P (1) | — | **SUBSTANTIVE** | Native | 5 | CTO |
| **D-07.2** Secure Coding Practices | — | P (1) | P (1) | P (1) | — | **SUBSTANTIVE** | Native | 3 | CTO |
| **D-07.3** CI/CD Pipeline Security | — | — | P (1) | P (1) | — | **PARTIAL** | Native | 2 | DevOps |
| **D-07.4** Change Management | — | — | P (1) | P (1) | — | **PARTIAL** | Native | 2 | DevOps |

**D-07 Summary:** 4/4 sub-domains covered (100%) | 12 total clauses | All Native

---

### D-08: Human Factors

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Coverage Level | Native/Inherited | Clause Count | Primary Owner |
|------------|------|-----|-------|------|--------|----------------|------------------|--------------|---------------|
| **D-08.1** General Security Awareness | P (1) | — | P (1) | P (1) | — | **SUBSTANTIVE** | Native | 3 | HR |
| **D-08.2** Role-Specific Competence | P (1) | — | P (1) | P (1) | P (1) | **SUBSTANTIVE** | Native | 4 | HR |
| **D-08.3** Management Board Training | — | — | P (1) | P (1) | — | **PARTIAL** | Native | 2 | CEO |

**D-08 Summary:** 3/3 sub-domains covered (100%) | 9 total clauses | All Native | NIS 2 + DORA board training

---

### D-09: Governance & Documentation

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Coverage Level | Native/Inherited | Clause Count | Primary Owner |
|------------|------|-----|-------|------|--------|----------------|------------------|--------------|---------------|
| **D-09.1** Information Security Policies | S (3) | P (1) | P (1) | P (1) | S (2) | **SUBSTANTIVE** | Native | 8 | CISO |
| **D-09.2** Impact & Risk Assessments | S (2) | P (1) | P (1) | P (1) | S (2) | **SUBSTANTIVE** | Native | 7 | CISO |
| **D-09.3** Asset Inventories | — | — | P (1) | P (1) | — | **PARTIAL** | Native | 2 | CISO |
| **D-09.4** Records of Processing | S (2) | — | — | — | P (1) | **PARTIAL** | Native | 3 | DPO |

**D-09 Summary:** 4/4 sub-domains covered (100%) | 20 total clauses | All Native

---

### D-10: Monitoring & Audit

| Sub-Domain | GDPR | CRA | NIS 2 | DORA | AI Act | Coverage Level | Native/Inherited | Clause Count | Primary Owner |
|------------|------|-----|-------|------|--------|----------------|------------------|--------------|---------------|
| **D-10.1** Continuous Security Monitoring | — | P (1) | P (1) | P (1) | P (1) | **SUBSTANTIVE** | Hybrid (SOC) | 4 | CISO |
| **D-10.2** Audit Logging & Traceability | — | P (1) | P (1) | P (1) | P (1) | **SUBSTANTIVE** | Hybrid (Cloud) | 4 | CISO |
| **D-10.3** Compliance Testing | P (1) | P (1) | P (1) | P (1) | P (1) | **SUBSTANTIVE** | Native | 5 | CISO |

**D-10 Summary:** 3/3 sub-domains covered (100%) | 13 total clauses | Hybrid + Native

---

## 4. COVERAGE SUMMARY BY DOMAIN

| Domain ID | Domain Name | Sub-Domains | Covered | Coverage % | Total Clauses | Native % | Inherited % |
|-----------|-------------|-------------|---------|------------|---------------|----------|-------------|
| D-01 | Data Protection & Encryption | 4 | 4 | 100.0% | 19 | 50.0% | 50.0% |
| D-02 | Vulnerability Management | 4 | 4 | 100.0% | 15 | 100.0% | 0.0% |
| D-03 | Access Control | 4 | 4 | 100.0% | 12 | 60.0% | 40.0% |
| D-04 | Incident Response | 4 | 4 | 100.0% | 19 | 100.0% | 0.0% |
| D-05 | Data Lifecycle | 4 | 4 | 100.0% | 9 | 100.0% | 0.0% |
| D-06 | Supply Chain | 4 | 4 | 100.0% | 9 | 50.0% | 50.0% |
| D-07 | Secure Development | 4 | 4 | 100.0% | 12 | 100.0% | 0.0% |
| D-08 | Human Factors | 3 | 3 | 100.0% | 9 | 100.0% | 0.0% |
| D-09 | Governance & Documentation | 4 | 4 | 100.0% | 20 | 100.0% | 0.0% |
| D-10 | Monitoring & Audit | 3 | 3 | 100.0% | 13 | 60.0% | 40.0% |
| **TOTAL** | **All Domains** | **38** | **38** | **100.0%** | **150** | **~85%** | **~15%** |

---

## 5. COMPLEMENTARITY ANALYSIS (C2)

<!-- BY-DESIGN: case-specific extension — Regulatory Overlap Summary is MAX-only (5-reg overlap analysis). Per legacy lint baseline §A.3.6, this is one of 17 by-design extra sections in Case_03 (MAX tier complexity). -->

### 5.1 Regulatory Overlap Summary

| Overlap Type | Sub-Domain Count | Percentage | Example Sub-Domains |
|--------------|------------------|------------|---------------------|
| **All 5 Regulations** | 7 | 18.4% | D-01.1, D-01.2, D-04.3, D-09.1, D-09.2, D-10.3 |
| **4 Regulations** | 15 | 39.5% | D-01.3, D-02.1, D-03.1, D-10.1, D-10.2 |
| **3 Regulations** | 10 | 26.3% | D-02.2, D-03.3, D-05.1, D-06.1 |
| **2 Regulations** | 4 | 10.5% | D-02.3, D-05.2, D-05.3, D-09.4 |
| **1 Regulation** | 2 | 5.3% | D-03.4 (CRA), D-05.4 (GDPR) |
| **0 Regulations** | 0 | 0.0% | — |

**Average Regulatory Overlap:** 3.7 regulations per sub-domain

<!-- BY-DESIGN: case-specific extension — Complementarity Opportunities is MAX-only. Per legacy lint baseline §A.3.6, this is one of 17 by-design extra sections in Case_03 (MAX tier complexity). -->

### 5.2 Complementarity Opportunities

| Sub-Domain | Regulations | Complementarity Type | Implementation Approach |
|------------|-------------|---------------------|------------------------|
| D-01.1 | GDPR + CRA + NIS 2 + DORA + AI Act | **Cumulative Reinforcement** | Single encryption standard satisfies all |
| D-04.3 | GDPR + CRA + NIS 2 + DORA + AI Act | **Conflict (Timing)** | Max-SLA Routing (24h workflow) |
| D-09.1 | GDPR + CRA + NIS 2 + DORA + AI Act | **Cumulative Reinforcement** | Unified ISMS (ISO 27001 + DORA) |
| D-09.2 | GDPR + CRA + NIS 2 + DORA + AI Act | **Trigger Mismatch** | Unified assessment (DPIA + FRIA) |

<!-- BY-DESIGN: case-specific extension — Conflict Classification is MAX-only (structural vs contextual taxonomy). Per legacy lint baseline §A.3.6, this is one of 17 by-design extra sections in Case_03 (MAX tier complexity). -->

### 5.3 Conflict Classification (Structural vs Contextual)

Overlaps between regulations create three types of relationships:

| Relationship Type | Definition | Sub-Domains | Example |
|-------------------|-----------|-------------|---------|
| **Synergistic** (Complementarity) | 2+ regulations reinforce with compatible requirements | D-01.1, D-01.2, D-01.4, D-03.1, D-05.1, D-10.3 | GDPR+CRA+NIS2+DORA all require encryption → single strong symmetric encryption standard satisfies all |
| **Structural Tension** | 2+ regulations apply permanently with differing requirements | D-05.3 vs D-10.2, D-07.1, D-09.1, D-09.2 | DORA immutable logs vs GDPR right to erasure — permanently coexist |
| **Contextual Tension** | 2+ regulations conflict only when same factual event triggers both | D-04.3 | GDPR 72h + CRA 24h + NIS2 24h + DORA 4h + AI Act 15d — only when same incident triggers multiple |

<!-- BY-DESIGN: case-specific extension — Compound Event Scenarios is MAX-only (10 scenarios). Per legacy lint baseline §A.3.6, this is one of 17 by-design extra sections in Case_03 (MAX tier complexity). -->

### 5.4 Compound Event Scenarios

This section identifies **factual events** that can simultaneously trigger obligations from multiple regulations. A compound event exists when a single incident satisfies the trigger conditions of two or more regulatory clauses in the same sub-domain.

**Why this matters:** Compound events are the source of contextual tensions. They are NOT inherent to the regulations — they emerge from the interaction between the company's operational profile and the regulatory triggers that apply to it. With ALL 5 regulations applicable, OmniBank faces the maximum possible surface for compound events.

| Event ID | Compound Event Description | Regulations Triggered | Sub-Domain | Tension Created | Resolution Required |
|----------|--------------------------|----------------------|------------|-----------------|-------------------|
| EVT-001 | Cyberattack exploits product vulnerability AND exfiltrates personal data AND disrupts banking services AND involves AI trading model | GDPR + CRA + NIS 2 + DORA + AI Act | D-04.3 | TENSION-H-001 (TEMPORAL_CONFLICT: 72h vs 24h vs 24h vs 4h vs 15d) | Max-SLA Routing — DORA 4h initial report satisfies all shorter deadlines |
| EVT-002 | Cyberattack exploits vulnerability AND exfiltrates personal data AND disrupts payment systems | GDPR + CRA + NIS 2 + DORA | D-04.3 | TENSION-H-001 (4-reg) | Max-SLA Routing — 4h DORA |
| EVT-003 | AI trading model malfunction causes unauthorized transactions (personal data involved) | GDPR + DORA + AI Act | D-04.3 | TENSION-H-001 (3-reg) | DORA 4h + GDPR 72h + AI Act 15d |
| EVT-004 | Customer requests erasure of personal data that exists in DORA immutable audit logs | GDPR (Art. 17) + DORA (Art. 11/19) | D-05.3 vs D-10.2 | TENSION-H-002 (REQUIREMENT_CONFLICT) | Cryptographic sharding — destroy identity, retain anonymized log |
| EVT-005 | New AI credit scoring model launch with personal data processing | GDPR (DPIA) + CRA (risk assessment) + NIS 2 (risk analysis) + DORA (ICT risk) + AI Act (FRIA) | D-09.2 | TENSION-M-001 (structural) | IPSARA Framework — unified assessment |
| EVT-006 | Product design phase for new mobile banking feature | GDPR + CRA + AI Act | D-07.1 | TENSION-L-001 (structural) | Follow CRA higher bar |
| EVT-007 | Ransomware attack encrypts core banking systems + customer data | GDPR + NIS 2 + DORA | D-04.2 | No tension (complementary recovery) | Unified BCP/DRP |
| EVT-008 | Supply chain vendor breach affecting bank's customer data | GDPR + NIS 2 + DORA | D-06.1 | Structural — always active | Unified vendor assessment |
| EVT-009 | Annual compliance documentation update | GDPR + CRA + NIS 2 + DORA + AI Act | D-09.1 | Structural — always active | Unified GRC platform |
| EVT-010 | AI model drift detected in fraud detection system | AI Act + DORA | D-10.1 | Structural — always active | Integrated monitoring |

**Events that do NOT create compound scenarios (parallel obligations only):**

| Scenario | Triggers GDPR? | Triggers CRA? | Triggers NIS 2? | Triggers DORA? | Triggers AI Act? | Tension? | Why Not |
|----------|---------------|---------------|-----------------|----------------|-----------------|----------|---------|
| Customer changes address | ✅ Yes | ❌ No | ❌ No | ❌ No | ❌ No | No | GDPR only, no security incident |
| AI model accuracy drift | ❌ No | ❌ No | ❌ No | ❌ No | ✅ Yes | No | AI Act only, no personal data breach |
| Internal IT system outage | ❌ No | ❌ No | ❌ No | ✅ Yes | ❌ No | No | DORA only, no personal data involved |
| Vendor contract renewal | ❌ No | ❌ No | ✅ Yes | ❌ No | ❌ No | No | NIS 2 only, no data processing change |

**Cross-case implication:** The number of compound event scenarios scales with regulatory overlap. Case 1 (2 regs, TinyTask) has 3 compound scenarios. Case 2 (3 regs, SecureBorder) has 6. Case 3 (5 regs, OmniBank) has 10+ — reflecting the combinatorial explosion when all regulations apply simultaneously. This validates the AEGIS methodology's emphasis on structural vs contextual tension classification: most 5-regulation overlaps are synergistic or structural, and only D-04.3 produces contextual tension at scale.

### 5.5 Strategic Tensions Identified

| Tension ID | Sub-Domain | Regulations | Conflict Type | Severity | Resolution Required |
|------------|------------|-------------|---------------|----------|---------------------|
| **T-001** | D-04.3 | GDPR (72h) vs CRA (24h) vs NIS 2 (24h) vs DORA (24h) | Timing Mismatch | **CRITICAL** | Max-SLA Routing (24h) |
| **T-002** | D-05.3 vs D-10.2 | GDPR (erasure) vs AI Act (6-month logs) | Retention Conflict | **CRITICAL** | Cryptographic Sharding |
| **T-003** | D-09.2 | GDPR (DPIA) vs AI Act (FRIA) | Trigger Mismatch | MEDIUM | Unified Assessment |
| **T-004** | D-04.3 | NIS 2 (24h) vs DORA (24h) | Alignment Opportunity | LOW | Unified 24h workflow |
| **T-005** | D-02.4 vs D-10.3 | DORA Art. 26 (TLPT triennial) vs ISO 27001 (annual testing) | Frequency Mismatch | MEDIUM | Cycle orchestration (DORA TLPT every 3y + ISO 27001 annual + AI Act conformity in between) |

**T-005 — NEW in Sprint 1 (2026-08-06):** Added from Sprint 0.6 Doc 06b §4.5. DORA Art. 26 mandates Threat-Led Penetration Testing (TLPT) every 3 years for major financial entities (OmniBank qualifies per ECB-supervised significance). ISO 27001 surveillance cycle is annual. AI Act Art. 43 conformity assessment is per-market-placement. Resolved by **cycle orchestration**: DORA TLPT every 3y (most stringent), ISO 27001 annual in between (with TLPT-scope mini-tests in year 2), AI Act conformity at each major release. Cross-reference: `06b_DORA_ICT_Risk_Framework.md §4.5`.

---

## 6. STRATEGIC IMPLICATIONS (C3)

<!-- BY-DESIGN: case-specific extension — Business Goal Alignment is MAX-only. Per legacy lint baseline §A.3.6, this is one of 17 by-design extra sections in Case_03 (MAX tier complexity). -->

### 6.1 Business Goal Alignment

| Business Goal | Related Sub-Domains | Regulatory Driver | Implementation Priority |
|---------------|---------------------|-------------------|------------------------|
| BG-001: DORA compliance (2025-01-17) | D-05, D-07, D-09, D-10 | DORA | **CRITICAL** |
| BG-002: AI Act conformity | D-07.1, D-09.1, D-09.2, D-10.3 | AI Act | **CRITICAL** |
| BG-003: NIS 2 compliance (24h) | D-04.1, D-04.3, D-10.1 | NIS 2 | **HIGH** |
| BG-004: GDPR compliance | D-05, D-09.4, D-10.2 | GDPR | **CRITICAL** |
| BG-005: 99.99% uptime SLA for core banking | D-04.4, D-09.1, D-10.1 | Operations / Infrastructure / DORA Art. 12 | **HIGH** |
| BG-006: Expand AI-powered services to 3 additional EU markets (24 months) | D-09.1, D-04.3, D-07.1 | Multi-jurisdiction (GDPR + DORA + AI Act + NIS 2 + CRA) | **MEDIUM** |
| BG-007: Maintain ISO 27001 + extend to DORA compliance | D-09.1, D-09.2, D-09.4, D-10.3 | ISO 27001 + DORA Art. 5 | **HIGH** |
| BG-008: Reduce AI model bias to <1% across all protected characteristics | D-07.1, D-09.2 | AI Act Art. 10 + Art. 13 + Art. 14 | **HIGH** |

### BG-005 → Doc 07 §6.1 mapping (added 2026-08-06)
- Affected sub-domains: D-04.4 (Data Restoration & Recovery), D-09.1 (Policies for BCP), D-10.1 (Continuous Security Monitoring)
- PG/SG references: AG-D-04.4-001 (RTO 4h / RPO 15min for critical systems), AG-D-04.4-002 (RTO 4h / RPO 15min), AG-D-10.1-001 (24/7 SOC + centralized monitoring)
- Verification criteria reinforce BG-005: managed backup with documented retention, multi-region DR, quarterly DR test — combined capacity supports 99.99% uptime target (per Doc 07c AG-D-04.4-002 "99.99% SLA per BG-005")

### BG-006 → Doc 07 §6.1 mapping (added 2026-08-06)
- Affected sub-domains: D-09.1 (Policies per jurisdiction), D-04.3 (Incident notification per country), D-07.1 (AI Act conformity assessment per market)
- PG/SG references: AG-D-09.1-001 (5-policy architecture extending per market), AG-D-04.3-002 (multi-reg 5-reg max-SLA routing), AG-D-07.1-001 (AI Act high-risk conformity)
- Verification criteria reinforce BG-006: Multi-reg incident notification pipeline (GDPR SA + NIS 2 CSIRT + CRA ENISA + DORA ECB JST + AI Act supervisory authority) supports multi-jurisdiction compliance for 3 new EU markets

### BG-007 → Doc 07 §6.1 mapping (added 2026-08-06)
- Affected sub-domains: D-09.1 (InfoSec Policies), D-09.2 (Risk Assessments), D-09.4 (Records), D-10.3 (Compliance Testing)
- PG/SG references: AG-D-09.1-001 (5-policy architecture with DORA overlay), AG-D-09.2-001 (Unified DPIA + CRA-RA + DORA ICT risk + AI Act FRIA), AG-D-09.4-001 (RoPA + DORA records), AG-D-10.3-002 (Quarterly compliance review + ISO 27001 surveillance)
- Verification criteria reinforce BG-007: ISO 27001 surveillance audit + DORA Art. 5 ICT risk framework + annual external auditor (per Doc 07c AG-D-09.1-002 + AG-D-10.3-002)

### BG-008 → Doc 07 §6.1 mapping (added 2026-08-06)
- Affected sub-domains: D-07.1 (Secure-by-Design for AI Act), D-09.2 (Risk Assessments for AI Act FRIA), D-10.1 (AI Act post-market monitoring)
- PG/SG references: AG-D-07.1-001 (AI Act high-risk conformity + secure-by-design), AG-D-09.2-001 (FRIA for fundamental rights impact), AG-D-10.1-001 (AI Act Art. 72 PMM with bias monitoring)
- Verification criteria reinforce BG-008: Bias metrics <1% via AI Act Art. 10 data quality governance + Art. 13 transparency obligations + Art. 14 human oversight

<!-- BY-DESIGN: case-specific extension — Resource Implications is MAX-only. Per legacy lint baseline §A.3.6, this is one of 17 by-design extra sections in Case_03 (MAX tier complexity). -->

### 6.2 Resource Implications

| Resource Type | Requirement | Current Capability | Gap | Remediation |
|---------------|-------------|-------------------|-----|-------------|
| **Personnel** | AI Governance Lead | Not hired | **HIGH** | Hire before AI Act deadline |
| **Personnel** | DORA ICT Risk Lead | Partial (existing BSI) | **MEDIUM** | Extend BSI role |
| **Process** | 24h incident notification | SOC exists | **LOW** | Align timelines |
| **Process** | DORA conformity | Not started | **HIGH** | Gap assessment |
| **Process** | AI Act conformity | Not started | **HIGH** | Conformity assessment |
| **Tooling** | AI monitoring system | Partial | **MEDIUM** | Extend existing logging |
| **Tooling** | DORA testing (TLPT) | Not started | **HIGH** | Schedule TLPT |

<!-- BY-DESIGN: case-specific extension — Risk Profile Assessment is MAX-only. Per legacy lint baseline §A.3.6, this is one of 17 by-design extra sections in Case_03 (MAX tier complexity). -->

### 6.3 Risk Profile Assessment

| Risk Category | Risk Level | Justification |
|---------------|------------|---------------|
| **Regulatory Non-Compliance** | **CRITICAL** | 5 regulations with overlapping requirements |
| **Market Access** | **CRITICAL** | No DORA/AI Act certification = no EU market |
| **Management Liability** | **CRITICAL** | DORA + NIS 2 board liability |
| **Fundamental Rights** | **CRITICAL** | AI-driven credit decisions affect financial access |
| **Operational** | **MEDIUM** | ISO 27001/BSI foundation reduces risk |

---

## 7. PHASE 1 GATE CRITERIA CHECKLIST

| Criterion | Status | Evidence |
|-----------|--------|----------|
| **Company Context complete (38/38 questions)** | ✅ PASS | 04_Company_Context_Assessment.md |
| **Regulatory Applicability assessed (5/5 regulations)** | ✅ PASS | 05_Regulatory_Applicability.md |
| **Clause Mapping complete (150 clauses)** | ✅ PASS | 06_Clause_Mapping_Matrix.xlsx |
| **Sub-Domain coverage complete (38 sub-domains)** | ✅ PASS | Section 3 of this document |
| **Complementarity Analysis complete** | ✅ PASS | Section 5 of this document |
| **Strategic Implications documented** | ✅ PASS | Section 6 of this document |
| **Design decisions logged** | ✅ PASS | 03_Design_Decisions_Log.md (13 decisions) |
| **Traceability complete** | ✅ PASS | All clauses → sub-domains → regulations |

**Phase 1 Gate Decision:** ✅ **PASS**

**Gate Review Date:** 2026-04-01

**Phase 1 Status:** ✅ **COMPLETE** — Ready for Phase 2 (Obligation Derivation)

---

<!-- BY-DESIGN: case-specific extension — Traceability Summary is MAX-only. Per legacy lint baseline §A.3.6, this is one of 17 by-design extra sections in Case_03 (MAX tier complexity). -->

## 8. TRACEABILITY SUMMARY

| Source Artifact | Count | Traceability Status |
|-----------------|-------|---------------------|
| Regulatory Clauses (Phase 1) | 150 | ✅ Complete |
| Sub-Domains (Taxonomy) | 38 | ✅ Complete |
| Covered Sub-Domains | 38 | ✅ Complete (100%) |
| Compliance Matrix Entries | 38 | ✅ Complete |
| Complementarity Analyses | 38 | ✅ Complete |
| Strategic Implications | 8 | ✅ Complete |
| Design Decisions | 13 | ✅ Complete |

**Full Traceability Chain:** Company Context → Applicability → Clauses → Sub-Domains → Compliance Matrix → Complementarity → Strategic Implications

---

## 9. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | Compliance Lead | Initial release - OmniBank Financial Systems case |

---

## 10. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | | 2026-04-01 |
| Business Review (CEO) | | | |
| Technical Review (CTO) | | | |
| Security Review (CISO) | | | |
| Compliance Review (CRO) | | | |

---

**Phase 1 Status:** ✅ **COMPLETE**  
**Next Phase:** 02_PHASE2_RULES → 08_Obligation_Derivation.md  
**Companion File:** 06_Clause_Mapping_Matrix.xlsx
