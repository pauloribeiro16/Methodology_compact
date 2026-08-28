---
document_id: AEGIS-COMMON-03
title: Design Decisions Log
version: 1.0
created: 2026-04-01
updated: 2026-04-01
author: AEGIS Research Team
status: DRAFT
traceability: AEGIS Class Model decision notes (drawio.xml)
inputs: [All Phase 1-3 documents]
outputs: [Design decision records]
related_documents: All Phase 1-3 documents
---

# Design Decisions Log

## 1. DOCUMENT PURPOSE

This document captures all design decisions made throughout all AEGIS phases. Each decision is recorded with its rationale, alternatives considered, and traceability to AEGIS class model attributes.

**Alignment with Class Model:** This document supports decision notes annotated in the AEGIS Class Model diagrams (Phase 1, 2, and 3).

**Phase Usage:**
- Phase 1: CompanyContext, RegulatoryClause, ComplianceContext decisions
- Phase 2: RegulatoryObligation, StrategicTension, RulesCatalog decisions
- Phase 3: ArchitecturalNode, FunctionalNode, ComplianceGate decisions

---

## 2. DECISION LOG STRUCTURE

Each decision is recorded using the following template:

| Field | Description |
|-------|-------------|
| Decision ID | Unique identifier (D-XXX) |
| Decision Date | Date decision was made |
| Decision Maker | Role/person who made the decision |
| Decision Statement | Clear statement of what was decided |
| Alternatives Considered | Other options that were evaluated |
| Rationale | Why this decision was made |
| Class Model Reference | Link to class model element |
| Impact Assessment | Downstream effects of this decision |
| Review Date | When decision should be re-evaluated |
| Status | ✅ APPROVED / ⚠️ CONDITIONAL / ❌ REJECTED |

---

## 3. DECISION REGISTER

### 3.1 PHASE 1 DECISIONS (Company Context & Regulatory Inference)

| Decision ID | D-001 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team + CTO |
| Decision Statement | Keep CompanyContext as monolithic entity — do NOT decompose into RegulatoryApplicability + OperationalProfile |
| Alternatives Considered | 1. Decomposed: Split into RegulatoryApplicability + OperationalProfile<br>2. Monolithic (Selected): Single entity with all attributes |
| Rationale | 1. Simplicity over premature optimization<br>2. Class Model annotation: "Manter monolítico"<br>3. Phase 1 scope: CompanyContext is input artifact<br>4. Traceability: All attributes map to T8.4 |
| Class Model Reference | CompanyContext class + Decision Note |
| Impact Assessment | - Positive: Simpler structure; easier to populate<br>- Negative: May need refactoring if Phase 2 requires separation<br>- Mitigation: Document attribute groupings for future extraction |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-002 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team + CEO |
| Decision Statement | NIS 2 APPLICABLE — SecureBorder is supplier to essential entities (450 employees > 50 threshold) |
| Alternatives Considered | 1. Exclude NIS 2: Argue below threshold<br>2. Apply NIS 2 (Selected): Essential entity supplier per Art. 21 |
| Rationale | 1. T8.4 ComplianceContext: nis2_sector = "Security" + size = 450 employees (> 50)<br>2. Legal accuracy: NIS 2 Art. 21 applies to suppliers of essential entities<br>3. Contractual requirement: Government contracts mandate NIS 2 compliance<br>4. AEGIS principle: Analyze all applicable regulations |
| Class Model Reference | ComplianceContext.applicable_regulations |
| Impact Assessment | - Positive: Contractual compliance; market access<br>- Negative: Additional 29 clauses to implement<br>- Mitigation: Leverage ISO 27001 certification as foundation |
| Review Date | Annual (or if employee count drops below 50) |
| Status | ✅ APPROVED |

---

| Decision ID | D-003 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team + CTO |
| Decision Statement | AI Act APPLICABLE — GuardianGate is High-Risk AI (Annex III: border control) |
| Alternatives Considered | 1. Exclude AI Act: Argue AI is ancillary<br>2. Apply AI Act (Selected): Annex III explicitly covers border control AI |
| Rationale | 1. T8.4: aiact_high_risk_system = TRUE (Annex III: migration, asylum, border control)<br>2. AI Act Art. 6: Border control AI is high-risk per se<br>3. Market access: Conformity assessment required before EU market placement<br>4. AEGIS principle: Analyze CURRENT state (AI is deployed) |
| Class Model Reference | CompanyContext.aiact_high_risk_system + StrategicImplication |
| Impact Assessment | - Positive: Legal compliance; market access<br>- Negative: 29 additional clauses; conformity assessment required<br>- Mitigation: Integrate AI Act requirements into existing ISO 27001 ISMS |
| Review Date | Before any AI model changes |
| Status | ✅ APPROVED |

---

| Decision ID | D-004 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | Include ALL Nuances (1-3) in RegulatoryClause class |
| Alternatives Considered | 1. Nuance 1 only<br>2. Nuance 2 only<br>3. Nuance 3 only<br>4. All Nuances (Selected) |
| Rationale | 1. Class Model annotation: "Incluir todas as Nuances"<br>2. T1-T5: All required for complete characterization<br>3. Phase 2: Critical for Strategic Tension Analysis (4 regulations = more tensions)<br>4. Traceability: Supports decomposition + conflict detection |
| Class Model Reference | RegulatoryClause class + Decision Note |
| Impact Assessment | - Positive: Complete clause characterization; supports multi-regulation analysis<br>- Negative: Increased complexity (112 clauses × 3 nuances)<br>- Mitigation: Use structured tables; automate where possible |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-005 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | Normative Weight assigned at clause level — NOT sub-domain level |
| Alternatives Considered | 1. Sub-Domain Level<br>2. Clause Level (Selected)<br>3. Regulation Level |
| Rationale | 1. T9: Explicitly at clause level<br>2. Precision: Different clauses may differ (GDPR vs AI Act)<br>3. Weighted Score accuracy: Required for multi-regulation overlay<br>4. AEGIS principle: Enables precise Strategic Tension detection |
| Class Model Reference | RegulatoryClause.normativeWeight |
| Impact Assessment | - Positive: Precise NI calculation across 4 regulations<br>- Negative: Increased effort (112 clause weight assignments)<br>- Mitigation: Use T9.1 tables as reference |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-006 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | ComplementarityAnalysis is PERSISTENT entity — NOT derived query |
| Alternatives Considered | 1. Derived Query: Calculate on-demand<br>2. Persistent (Selected): Versioned artifact |
| Rationale | 1. Class Model: "Entidade persistente — Versionamento + auditoria"<br>2. Traceability: Auditable for thesis + regulatory audits<br>3. Reproducibility: Re-run Phase 1 verification<br>4. T7 Metrics: Required for 4-regulation overlap analysis |
| Class Model Reference | ComplementarityAnalysis class + Decision Note |
| Impact Assessment | - Positive: Audit trail; reproducible; supports 4-regulation complexity<br>- Negative: Storage overhead<br>- Mitigation: Store as document with version control |
| Review Date | Thesis Defense + Regulatory Audits |
| Status | ✅ APPROVED |

---

| Decision ID | D-007 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | ImplementationMapping INCLUDED in Phase 1 — NOT deferred to Phase 3 |
| Alternatives Considered | 1. Phase 3 Only<br>2. Phase 1 Inclusion (Selected) |
| Rationale | 1. Class Model: "Manter na Fase 1 — Rastreabilidade"<br>2. Traceability: Prevents Phase 3 refactoring<br>3. Framework selection: Critical for 4-regulation overlay (ISO 27001, NIST AI RMF, CRA guidelines)<br>4. AEGIS principle: regulation → sub-domain → framework → control |
| Class Model Reference | ImplementationMapping class + Decision Note |
| Impact Assessment | - Positive: Prevents refactoring; enables multi-framework mapping<br>- Negative: Increased Phase 1 effort (framework mapping for 35 covered sub-domains)<br>- Mitigation: Use WP1 Taxonomy Crosswalk |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-008 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | Taxonomy: 10 Domains × 38 Sub-Domains — FIXED for Phase 1 |
| Alternatives Considered | 1. Dynamic Taxonomy<br>2. Fixed (Selected)<br>3. Regulation-Specific |
| Rationale | 1. Class Model: "Vocabulário comum"<br>2. Common vocabulary: Enables cross-regulation comparison (4 regulations)<br>3. Traceability: Consistent references across all documents<br>4. AEGIS principle: "Common language" between regulations |
| Class Model Reference | SecurityControlDomain class + Decision Note |
| Impact Assessment | - Positive: Consistent references; enables T6/T7 analysis for 4 regulations<br>- Negative: Requires update if new sub-domains discovered<br>- Mitigation: Document gaps; propose extensions for Phase 2 |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-009 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | RelationType distinguishes overlap types — Nuance 5 |
| Alternatives Considered | 1. Binary Overlap<br>2. RelationType (Selected): 4 types |
| Rationale | 1. Class Model: "relationType distingue Overlap vs Reinforcement vs Conflict vs Gap"<br>2. T7.5: Different types trigger different resolutions<br>3. Strategic Tension: Critical for 4-regulation complexity<br>4. AEGIS principle: Not all overlaps equal |
| Class Model Reference | DomainCoverageEntry.relationType + RelationType enumeration |
| Impact Assessment | - Positive: Precise tension detection for 4 regulations<br>- Negative: Increased complexity (35 covered sub-domains × 4 relation types)<br>- Mitigation: Use T7.5 table as reference |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-010 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | RegulatoryObligation RENAMED from "AbstractNFR" |
| Alternatives Considered | 1. Keep AbstractNFR<br>2. Rename (Selected) |
| Rationale | 1. Class Model: "Semanticamente correto"<br>2. Semantic accuracy: ARE regulatory obligations<br>3. Phase boundary: Prevents Phase 1/3 confusion<br>4. Traceability: Clear derivation path |
| Class Model Reference | RegulatoryObligation class + Decision Note |
| Impact Assessment | - Positive: Clear semantic distinction<br>- Negative: Legacy reference updates<br>- Mitigation: Document rename; update all documents |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-011 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team + CTO |
| Decision Statement | **SecureBorder-Specific:** Biometric data processing requires explicit Art. 9 legal basis (government contract) |
| Alternatives Considered | 1. Consent (not feasible for border control)<br>2. Legal obligation (Selected): Government contract as legal basis |
| Rationale | 1. GDPR Art. 9: Biometric data requires explicit legal basis<br>2. Border control context: Consent not feasible (mandatory process)<br>3. Government contract provides legal obligation basis<br>4. DPIA mandatory (large-scale special category data) |
| Class Model Reference | CompanyContext.specialCategoryData + GDPR Art. 9 |
| Impact Assessment | - Positive: Legal compliance for biometric processing<br>- Negative: DPIA required; additional documentation<br>- Mitigation (legacy maturity wording, superseded): DPIA already completed per securityMaturity assessment |
| Review Date | Annual or upon contract renewal |
| Status | ✅ APPROVED |

---

| Decision ID | D-012 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team + CTO |
| Decision Statement | **SecureBorder-Specific:** CRA Critical Class requires third-party conformity assessment |
| Alternatives Considered | 1. Self-certification (not allowed for Critical Class)<br>2. Third-party assessment (Selected): Notified body required |
| Rationale | 1. CRA Art. 42: Critical Class products require notified body assessment<br>2. GuardianGate eGate is security function for border control<br>3. Market access: CE marking requires conformity certificate<br>4. Timeline: Assessment scheduled before product launch |
| Class Model Reference | CompanyContext.productType + CRA Critical Class |
| Impact Assessment | - Positive: Market access; legal compliance<br>- Negative: Cost and timeline for assessment<br>- Mitigation: ISO 27001 certification reduces assessment effort |
| Review Date | Before product launch |
| Status | ✅ APPROVED |

---

### 3.2 PHASE 2 DECISIONS (Elaboration & Secure Design)

*To be completed during Phase 2 implementation*

---

### 3.3 PHASE 3 DECISIONS (Decomposition & Risk)

*To be completed during Phase 3 implementation*

---

## 4. DECISION SUMMARY DASHBOARD

| Decision ID | Decision Statement | Phase | Status | Review Date |
|-------------|-------------------|-------|--------|-------------|
| D-001 | CompanyContext monolithic | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-002 | NIS 2 APPLICABLE (essential entity supplier) | Phase 1 | ✅ APPROVED | Annual |
| D-003 | AI Act APPLICABLE (High-Risk border control AI) | Phase 1 | ✅ APPROVED | Before AI changes |
| D-004 | Include ALL Nuances (1-3) | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-005 | Normative Weight at clause level | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-006 | ComplementarityAnalysis persistent | Phase 1 | ✅ APPROVED | Thesis Defense |
| D-007 | ImplementationMapping in Phase 1 | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-008 | Taxonomy fixed (10×38) | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-009 | RelationType distinguishes overlap types | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-010 | RegulatoryObligation renamed | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-011 | Biometric data: Art. 9 legal basis | Phase 1 | ✅ APPROVED | Annual |
| D-012 | CRA Critical Class: Third-party assessment | Phase 1 | ✅ APPROVED | Before launch |

**Total Decisions:** 12  
**Approved:** 12 (100%)  
**Conditional:** 0  
**Rejected:** 0

---

## 5. DECISION TRACEABILITY MATRIX

| Decision ID | Related Document | Related Class | Related T-Table | Phase 2 Impact |
|-------------|------------------|---------------|-----------------|----------------|
| D-001 | 01_Company_Context.md | CompanyContext | T8.4 | CompanyContext structure |
| D-002 | 05_Regulatory_Applicability.md | ComplianceContext | T8.4 | NIS 2 scope added |
| D-003 | 05_Regulatory_Applicability.md | ComplianceContext | T8.4 | AI Act scope added |
| D-004 | 06_Clause_Mapping_Matrix.xlsx | RegulatoryClause | T1-T5 | Clause characterization |
| D-005 | 06_Clause_Mapping_Matrix.xlsx | RegulatoryClause | T9 | NI calculation |
| D-006 | 08_Complementarity_Analysis.md | ComplementarityAnalysis | T7 | Audit trail |
| D-007 | 07_Structured_Compliance_Matrix.md | ImplementationMapping | T6 | Framework traceability |
| D-008 | All Phase 1 documents | SecurityControlDomain | Taxonomia.txt | Common vocabulary |
| D-009 | 08_Complementarity_Analysis.md | DomainCoverageEntry | T7.5 | Tension detection |
| D-010 | All Phase 1-3 documents | RegulatoryObligation | N/A | Semantic clarity |
| D-011 | 07_Structured_Compliance_Matrix.md | CompanyContext | GDPR Art. 9 | Special category handling |
| D-012 | 07_Structured_Compliance_Matrix.md | CompanyContext | CRA Art. 42 | Critical Class certification |

---

## 6. DECISION PATTERNS & LESSONS LEARNED

### 6.1 Recurring Decision Themes

| Theme | Frequency | Pattern | Recommendation |
|-------|-----------|---------|----------------|
| Monolithic vs. Decomposed | 2 (D-001, D-008) | Keep simple for Phase 1 | Defer optimization until Phase 3 |
| Phase Inclusion vs. Deferral | 2 (D-003, D-007) | Include traceability early | Prevents refactoring |
| Naming Conventions | 1 (D-010) | Semantic accuracy over legacy | Rename early |
| Persistence vs. Derived | 1 (D-006) | Persistent for audit trail | Thesis + regulatory requirement |
| Granularity Level | 1 (D-005) | Fine granularity | Enables precision for 4 regulations |
| Regulatory Classification | 2 (D-011, D-012) | Explicit classification | Market access requirement |

### 6.2 Lessons Learned

| Lesson | Phase | Impact | Future Application |
|--------|-------|--------|-------------------|
| Taxonomy as common vocabulary | Phase 1 | Enabled 4-regulation cross-comparison | Use in all future cases |
| Early traceability prevents rework | Phase 1 | ImplementationMapping saved Phase 3 refactoring | Standard practice |
| Critical Class has special requirements | Phase 1 | CRA third-party assessment required | Factor into timeline/cost |
| High-Risk AI requires conformity assessment | Phase 1 | AI Act adds 29 clauses + assessment | Integrate with ISO 27001 |
| Biometric data requires Art. 9 legal basis | Phase 1 | Government contract provides basis | Document in DPIA |
| NIS 2 applies to suppliers of essential entities | Phase 1 | 29 additional clauses | Leverage existing ISO 27001 |

---

## 7. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | AEGIS Research Team | Initial release - SecureBorder Solutions case (12 decisions) |

---

## 8. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | AEGIS Research Team | | 2026-04-01 |
| AEGIS Methodology Review | | | |
| Technical Review (CTO) | | | |
| Business Review (CEO) | | | |

---

**Next Document:** Phase-specific documents (01_PHASE1_CONTEXT)  
**Dependency:** None (foundational governance artifact)  
**Case Study:** SecureBorder Solutions (High Complexity)  
**Total Decisions Logged:** 12
