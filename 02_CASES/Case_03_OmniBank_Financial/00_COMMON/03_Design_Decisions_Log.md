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
| Decision Statement | NIS 2 APPLICABLE — OmniBank is Essential Entity (financial sector + 5000+ employees) |
| Alternatives Considered | 1. Exclude NIS 2: Argue below threshold<br>2. Apply NIS 2 (Selected): Essential entity per Art. 21 |
| Rationale | 1. T8.4 ComplianceContext: nis2_sector = "Financial" + size = 5000+ employees (> 50)<br>2. Legal accuracy: NIS 2 Art. 21 applies to essential entities in financial sector<br>3. Regulatory requirement: Financial entities are automatically essential<br>4. AEGIS principle: Analyze all applicable regulations |
| Class Model Reference | ComplianceContext.applicable_regulations |
| Impact Assessment | - Positive: Regulatory compliance; avoids penalties<br>- Negative: Additional 29 clauses; 24h notification requirement<br>- Mitigation: Leverage existing incident response from financial regulations |
| Review Date | Annual (or if entity classification changes) |
| Status | ✅ APPROVED |

---

| Decision ID | D-003 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team + CTO |
| Decision Statement | AI Act APPLICABLE — OmniScore AI is High-Risk AI (Annex III: credit scoring) |
| Alternatives Considered | 1. Exclude AI Act: Argue AI is ancillary<br>2. Apply AI Act (Selected): Annex III explicitly covers credit scoring |
| Rationale | 1. T8.4: aiact_high_risk_system = TRUE (Annex III: credit scoring)<br>2. AI Act Art. 6: Credit scoring is high-risk per se<br>3. Market access: Conformity assessment required before EU market placement<br>4. AEGIS principle: Analyze CURRENT state (AI is deployed) |
| Class Model Reference | CompanyContext.aiact_high_risk_system + StrategicImplication |
| Impact Assessment | - Positive: Legal compliance; market access<br>- Negative: 29 additional clauses; conformity assessment required<br>- Mitigation: Integrate AI Act requirements into existing risk management |
| Review Date | Before any AI model changes |
| Status | ✅ APPROVED |

---

| Decision ID | D-004 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | DORA APPLICABLE — OmniBank is financial entity per Art. 2 |
| Alternatives Considered | 1. Exclude DORA: Argue not in scope<br>2. Apply DORA (Selected): Financial institution per Art. 2 |
| Rationale | 1. T8.4: dora_financial_entity = TRUE (banking institution)<br>2. DORA Art. 2: Credit institutions are in scope<br>3. ECB/BaFin supervision confirms DORA applicability<br>4. AEGIS principle: Analyze all applicable regulations |
| Class Model Reference | ComplianceContext.applicable_regulations |
| Impact Assessment | - Positive: Regulatory compliance; avoids ECB penalties<br>- Negative: 38 additional clauses; 100% Weight 3 (unconditional)<br>- Mitigation: Leverage existing BSI/ISO 27001 foundation |
| Review Date | Annual (or if regulatory status changes) |
| Status | ✅ APPROVED |

---

| Decision ID | D-005 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | Include ALL Nuances (1-3) in RegulatoryClause class |
| Alternatives Considered | 1. Nuance 1 only<br>2. Nuance 2 only<br>3. Nuance 3 only<br>4. All Nuances (Selected) |
| Rationale | 1. Class Model annotation: "Incluir todas as Nuances"<br>2. T1-T5: All required for complete characterization<br>3. Phase 2: Critical for Strategic Tension Analysis (5 regulations = more tensions)<br>4. Traceability: Supports decomposition + conflict detection |
| Class Model Reference | RegulatoryClause class + Decision Note |
| Impact Assessment | - Positive: Complete clause characterization; supports 5-regulation analysis<br>- Negative: Increased complexity (150 clauses × 3 nuances)<br>- Mitigation: Use structured tables; automate where possible |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-006 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | Normative Weight assigned at clause level — NOT sub-domain level |
| Alternatives Considered | 1. Sub-Domain Level<br>2. Clause Level (Selected)<br>3. Regulation Level |
| Rationale | 1. T9: Explicitly at clause level<br>2. Precision: Different clauses may differ across 5 regulations<br>3. Weighted Score accuracy: Required for multi-regulation overlay<br>4. AEGIS principle: Enables precise Strategic Tension detection |
| Class Model Reference | RegulatoryClause.normativeWeight |
| Impact Assessment | - Positive: Precise NI calculation across 5 regulations<br>- Negative: Increased effort (150 clause weight assignments)<br>- Mitigation: Use T9.1 tables as reference |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-007 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | ComplementarityAnalysis is PERSISTENT entity — NOT derived query |
| Alternatives Considered | 1. Derived Query: Calculate on-demand<br>2. Persistent (Selected): Versioned artifact |
| Rationale | 1. Class Model: "Entidade persistente — Versionamento + auditoria"<br>2. Traceability: Auditable for thesis + regulatory audits<br>3. Reproducibility: Re-run Phase 1 verification<br>4. T7 Metrics: Required for 5-regulation overlap analysis |
| Class Model Reference | ComplementarityAnalysis class + Decision Note |
| Impact Assessment | - Positive: Audit trail; reproducible; supports 5-regulation complexity<br>- Negative: Storage overhead<br>- Mitigation: Store as document with version control |
| Review Date | Thesis Defense + Regulatory Audits |
| Status | ✅ APPROVED |

---

| Decision ID | D-008 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | ImplementationMapping INCLUDED in Phase 1 — NOT deferred to Phase 3 |
| Alternatives Considered | 1. Phase 3 Only<br>2. Phase 1 Inclusion (Selected) |
| Rationale | 1. Class Model: "Manter na Fase 1 — Rastreabilidade"<br>2. Traceability: Prevents Phase 3 refactoring<br>3. Framework selection: Critical for 5-regulation overlay (ISO 27001, NIST AI RMF, DORA RTS, etc.)<br>4. AEGIS principle: regulation → sub-domain → framework → control |
| Class Model Reference | ImplementationMapping class + Decision Note |
| Impact Assessment | - Positive: Prevents refactoring; enables multi-framework mapping<br>- Negative: Increased Phase 1 effort (framework mapping for 38 covered sub-domains)<br>- Mitigation: Use WP1 Taxonomy Crosswalk |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-009 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | Taxonomy: 10 Domains × 38 Sub-Domains — FIXED for Phase 1 |
| Alternatives Considered | 1. Dynamic Taxonomy<br>2. Fixed (Selected)<br>3. Regulation-Specific |
| Rationale | 1. Class Model: "Vocabulário comum"<br>2. Common vocabulary: Enables cross-regulation comparison (5 regulations)<br>3. Traceability: Consistent references across all documents<br>4. AEGIS principle: "Common language" between regulations |
| Class Model Reference | SecurityControlDomain class + Decision Note |
| Impact Assessment | - Positive: Consistent references; enables T6/T7 analysis for 5 regulations<br>- Negative: Requires update if new sub-domains discovered<br>- Mitigation: Document gaps; propose extensions for Phase 2 |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-010 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team |
| Decision Statement | RelationType distinguishes overlap types — Nuance 5 |
| Alternatives Considered | 1. Binary Overlap<br>2. RelationType (Selected): 4 types |
| Rationale | 1. Class Model: "relationType distingue Overlap vs Reinforcement vs Conflict vs Gap"<br>2. T7.5: Different types trigger different resolutions<br>3. Strategic Tension: Critical for 5-regulation complexity<br>4. AEGIS principle: Not all overlaps equal |
| Class Model Reference | DomainCoverageEntry.relationType + RelationType enumeration |
| Impact Assessment | - Positive: Precise tension detection for 5 regulations<br>- Negative: Increased complexity (38 covered sub-domains × 4 relation types)<br>- Mitigation: Use T7.5 table as reference |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-011 |
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

| Decision ID | D-012 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team + CISO |
| Decision Statement | **OmniBank-Specific:** DORA ICT risk management framework extends existing BSI |
| Alternatives Considered | 1. Create new framework from scratch<br>2. Extend existing BSI (Selected) |
| Rationale | 1. Existing BSI already covers 70% of DORA requirements<br>2. Efficiency: Extend rather than duplicate<br>3. Regulatory alignment: DORA builds on existing financial regulations<br>4. AEGIS principle: Leverage existing controls where possible |
| Class Model Reference | CompanyContext.technologicalControlPlane + ImplementationMapping |
| Impact Assessment | - Positive: Reduced implementation effort; faster compliance<br>- Negative: Gap analysis required to identify missing 30%<br>- Mitigation: DORA gap assessment scheduled |
| Review Date | DORA compliance deadline (2025-01-17) |
| Status | ✅ APPROVED |

---

| Decision ID | D-013 |
|-------------|-------|
| Decision Date | 2026-04-01 |
| Decision Maker | AEGIS Research Team + AI Governance Lead |
| Decision Statement | **OmniBank-Specific:** AI Act conformity integrated with existing model risk management |
| Alternatives Considered | 1. Create separate AI compliance function<br>2. Integrate with existing model risk (Selected) |
| Rationale | 1. Existing model risk management covers similar ground<br>2. Efficiency: Single governance structure<br>3. Regulatory alignment: AI Act complements existing model oversight<br>4. AEGIS principle: Integrate rather than duplicate |
| Class Model Reference | CompanyContext.aiact_high_risk_system + ImplementationMapping |
| Impact Assessment | - Positive: Unified AI governance; reduced overhead<br>- Negative: Model risk framework requires updates for AI Act specifics<br>- Mitigation: AI Act gap assessment scheduled |
| Review Date | AI Act applicability date |
| Status | ✅ APPROVED |

---

### 3.2 PHASE 2 DECISIONS (Elaboration & Secure Design)

| Decision ID | D-014 |
|-------------|-------|
| Decision Date | 2026-04-03 |
| Decision Maker | Compliance Lead + CISO |
| Decision Statement | NI Propagation uses AVG (not MAX) for multi-regulation obligation derivation |
| Alternatives Considered | 1. MAX(clauseNI) — used in Case 1 (TinyTask, 2 regs)<br>2. AVG(clauseNI) — selected<br>3. Weighted AVG by regulatory priority |
| Rationale | 1. With 5 regulations and up to 13 source clauses per obligation (OBL-D-09.1-001), MAX would over-inflate NI — every clause is Weight 3 from NIS 2/DORA/AI Act<br>2. AVG better reflects the blended regulatory pressure across all 5 regulations<br>3. Case 1 uses MAX because with only 2 regulations, the difference is minimal<br>4. AEGIS principle: propagation method should reflect case complexity |
| Class Model Reference | RegulatoryObligation.normativeIntensity |
| Impact Assessment | - Positive: More nuanced NI distribution; avoids artificial inflation<br>- Negative: Slightly more complex to calculate<br>- Mitigation: Document AVG formula in derivation methodology; Excel auto-calculates |
| Review Date | Phase 2 Gate Review |
| Status | ✅ APPROVED |

---

| Decision ID | D-015 |
|-------------|-------|
| Decision Date | 2026-04-03 |
| Decision Maker | CISO + Compliance Lead |
| Decision Statement | T-001 resolved via Max-SLA Routing — 24h universal incident notification workflow |
| Alternatives Considered | 1. Parallel workflows per regulation<br>2. Max-SLA Routing (selected) — 24h satisfies all<br>3. Risk-based prioritization per incident type |
| Rationale | 1. 24h is the most stringent requirement across all 5 regulations<br>2. Meeting 24h automatically satisfies 72h GDPR and NIS 2/DORA detailed notifications<br>3. Single workflow reduces operational complexity vs. parallel tracks<br>4. OmniBank's 24/7 SOC capability supports 24h SLA |
| Class Model Reference | StrategicTension.resolutionStrategy |
| Impact Assessment | - Positive: Single incident management process; regulatory compliance across all 5<br>- Negative: Requires 24/7 SOC capability and pre-approved notification templates<br>- Mitigation: Leverage existing SOC; automate notification routing |
| Review Date | Annual or after regulatory timeline changes |
| Status | ✅ APPROVED |

---

| Decision ID | D-016 |
|-------------|-------|
| Decision Date | 2026-04-03 |
| Decision Maker | DPO + CISO |
| Decision Statement | T-002 resolved via Cryptographic Sharding — PII separation at log ingestion |
| Alternatives Considered | 1. Dual retention (impossible — direct contradiction)<br>2. Cryptographic Sharding (selected) — PII separated, keys destroyed on erasure<br>3. Consent-based override of erasure right |
| Rationale | 1. GDPR erasure and AI Act/DORA immutable logging are fundamentally incompatible without architectural intervention<br>2. Cryptographic sharding preserves audit integrity while enabling erasure via key destruction<br>3. Proportionate to OmniBank's high security maturity and available resources<br>4. Aligns with ECB guidance on data protection in financial logging | *(legacy design text — superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0, port Fase 4)*
| Class Model Reference | StrategicTension.resolutionStrategy + ConflictResolution |
| Impact Assessment | - Positive: Resolves fundamental architectural contradiction<br>- Negative: Requires log pipeline redesign; key management infrastructure<br>- Mitigation: Phase in via logging architecture upgrade project |
| Review Date | After logging architecture implementation |
| Status | ✅ APPROVED |

---

| Decision ID | D-017 |
|-------------|-------|
| Decision Date | 2026-04-03 |
| Decision Maker | CISO + DPO + AI Governance Lead |
| Decision Statement | T-003 resolved via IPSARA Unified Assessment Framework |
| Alternatives Considered | 1. Separate assessments per regulation<br>2. IPSARA Unified Assessment (selected)<br>3. Risk-based assessment selection |
| Rationale | 1. 5 regulatory assessments with overlapping risk analysis foundation create massive duplication<br>2. Single IPSARA document with 4 modular sections satisfies all 5 regulations<br>3. Reduces assessment effort from 5 separate processes to 1 integrated process<br>4. Aligns with OmniBank's existing ISO 27001 risk management framework |
| Class Model Reference | StrategicTension.resolutionStrategy |
| Impact Assessment | - Positive: 80% reduction in assessment effort; single risk register<br>- Negative: Requires new IPSARA template and training<br>- Mitigation: Develop IPSARA template based on ISO 27005 |
| Review Date | After first IPSARA assessment cycle |
| Status | ✅ APPROVED |

---

| Decision ID | D-018 |
|-------------|-------|
| Decision Date | 2026-04-03 |
| Decision Maker | CTO + Compliance Lead |
| Decision Statement | T-004 resolved by following CRA secure-by-default standard (higher bar) |
| Alternatives Considered | 1. GDPR "appropriate measures" only (lower bar)<br>2. CRA "secure by default" (selected) — higher bar satisfies both<br>3. Hybrid approach per system criticality |
| Rationale | 1. CRA NI=3 (unconditional) supersedes GDPR NI=2 (conditional) per T9.6 Intensity Gap resolution<br>2. CRA secure-by-default is a pass/fail criterion — simpler to verify than GDPR's contextual "appropriate"<br>3. Satisfies both regulations simultaneously<br>4. Consistent with OmniBank's high security maturity | *(legacy design text — superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0, port Fase 4)*
| Class Model Reference | StrategicTension.resolutionStrategy |
| Impact Assessment | - Positive: Higher security posture; simpler verification<br>- Negative: May require additional secure design controls for GDPR-only systems<br>- Mitigation: Apply CRA standard universally |
| Review Date | Phase 3 Gate Review |
| Status | ✅ APPROVED |

---

---

### 3.3 PHASE 3 DECISIONS (Decomposition & Risk)

*To be completed during Phase 3 implementation*

---

## 4. DECISION SUMMARY DASHBOARD

| Decision ID | Decision Statement | Phase | Status | Review Date |
|-------------|-------------------|-------|--------|-------------|
| D-001 | CompanyContext monolithic | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-002 | NIS 2 APPLICABLE (Essential Entity) | Phase 1 | ✅ APPROVED | Annual |
| D-003 | AI Act APPLICABLE (High-Risk credit scoring) | Phase 1 | ✅ APPROVED | Before AI changes |
| D-004 | DORA APPLICABLE (financial entity) | Phase 1 | ✅ APPROVED | Annual |
| D-005 | Include ALL Nuances (1-3) | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-006 | Normative Weight at clause level | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-007 | ComplementarityAnalysis persistent | Phase 1 | ✅ APPROVED | Thesis Defense |
| D-008 | ImplementationMapping in Phase 1 | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-009 | Taxonomy fixed (10×38) | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-010 | RelationType distinguishes overlap types | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-011 | RegulatoryObligation renamed | Phase 1 | ✅ APPROVED | Phase 2 Gate |
| D-012 | DORA extends existing BSI | Phase 1 | ✅ APPROVED | DORA deadline |
| D-013 | AI Act integrates with model risk | Phase 1 | ✅ APPROVED | AI Act date |

| D-014 | NI Propagation uses AVG for multi-regulation | Phase 2 | ✅ APPROVED | Phase 2 Gate |
| D-015 | T-001: 24h universal incident workflow | Phase 2 | ✅ APPROVED | Annual |
| D-016 | T-002: Cryptographic sharding for erasure vs logs | Phase 2 | ✅ APPROVED | After logging upgrade |
| D-017 | T-003: IPSARA unified assessment framework | Phase 2 | ✅ APPROVED | After 1st IPSARA |
| D-018 | T-004: Follow CRA secure-by-default standard | Phase 2 | ✅ APPROVED | Phase 3 Gate |

**Total Decisions:** 18
**Approved:** 18 (100%)
**Conditional:** 0  
**Rejected:** 0

---

## 5. DECISION TRACEABILITY MATRIX

| Decision ID | Related Document | Related Class | Related T-Table | Phase 2 Impact |
|-------------|------------------|---------------|-----------------|----------------|
| D-001 | 01_Company_Context.md | CompanyContext | T8.4 | CompanyContext structure |
| D-002 | 05_Regulatory_Applicability.md | ComplianceContext | T8.4 | NIS 2 scope added |
| D-003 | 05_Regulatory_Applicability.md | ComplianceContext | T8.4 | AI Act scope added |
| D-004 | 05_Regulatory_Applicability.md | ComplianceContext | T8.4 | DORA scope added |
| D-005 | 06_Clause_Mapping_Matrix.xlsx | RegulatoryClause | T1-T5 | Clause characterization |
| D-006 | 06_Clause_Mapping_Matrix.xlsx | RegulatoryClause | T9 | NI calculation |
| D-007 | 08_Complementarity_Analysis.md | ComplementarityAnalysis | T7 | Audit trail |
| D-008 | 07_Structured_Compliance_Matrix.md | ImplementationMapping | T6 | Framework traceability |
| D-009 | All Phase 1 documents | SecurityControlDomain | Taxonomia.txt | Common vocabulary |
| D-010 | 08_Complementarity_Analysis.md | DomainCoverageEntry | T7.5 | Tension detection |
| D-011 | All Phase 1-3 documents | RegulatoryObligation | N/A | Semantic clarity |
| D-012 | 07_Structured_Compliance_Matrix.md | CompanyContext | DORA RTS | BSI extension |
| D-013 | 07_Structured_Compliance_Matrix.md | CompanyContext | AI Act | Model risk integration |

---

## 6. DECISION PATTERNS & LESSONS LEARNED

### 6.1 Recurring Decision Themes

| Theme | Frequency | Pattern | Recommendation |
|-------|-----------|---------|----------------|
| Monolithic vs. Decomposed | 2 (D-001, D-009) | Keep simple for Phase 1 | Defer optimization until Phase 3 |
| Phase Inclusion vs. Deferral | 2 (D-003, D-008) | Include traceability early | Prevents refactoring |
| Naming Conventions | 1 (D-011) | Semantic accuracy over legacy | Rename early |
| Persistence vs. Derived | 1 (D-007) | Persistent for audit trail | Thesis + regulatory requirement |
| Granularity Level | 1 (D-006) | Fine granularity | Enables precision for 5 regulations |
| Integration vs. New | 2 (D-012, D-013) | Extend existing frameworks | Reduces duplication |
| Regulatory Classification | 3 (D-002, D-003, D-004) | Explicit classification | Market access requirement |

### 6.2 Lessons Learned

| Lesson | Phase | Impact | Future Application |
|--------|-------|--------|-------------------|
| Taxonomy as common vocabulary | Phase 1 | Enabled 5-regulation cross-comparison | Use in all future cases |
| Early traceability prevents rework | Phase 1 | ImplementationMapping saved Phase 3 refactoring | Standard practice |
| All 5 regulations = maximum coverage | Phase 1 | 100% sub-domain coverage; 0 gaps | Target state for critical sectors |
| DORA + NIS 2 have significant overlap | Phase 1 | Can leverage common controls | Efficiency opportunity |
| AI Act High-Risk requires conformity assessment | Phase 1 | Credit scoring is explicitly Annex III | Plan early for AI systems |
| Financial sector has mature foundation | Phase 1 | BSI/ISO 27001 reduces implementation effort | Leverage existing maturity | *(legacy design text — superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0, port Fase 4)*
| Extend rather than duplicate | Phase 1 | DORA extends BSI; AI Act extends model risk | Integration pattern |

---

## 7. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-01 | AEGIS Research Team | Initial release - OmniBank Financial Systems case (13 decisions) |

---

## 8. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | AEGIS Research Team | | 2026-04-01 |
| AEGIS Methodology Review | | | |
| Technical Review (CTO) | | | |
| Security Review (CISO) | | | |
| Business Review (CEO) | | | |

---

**Next Document:** Phase-specific documents (01_PHASE1_CONTEXT)  
**Dependency:** None (foundational governance artifact)  
**Case Study:** OmniBank Financial Systems (Maximum Complexity)  
**Total Decisions Logged:** 13
