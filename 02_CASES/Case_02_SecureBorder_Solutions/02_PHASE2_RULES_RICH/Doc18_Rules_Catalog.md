> **Sprint 10 note (corr-008 migration):** This document has been migrated from corr-007 (PG/SG) to corr-008 (PO/SO). All PG/SG references have been replaced with PO/SO IDs. BPR-AI-NN rules have been migrated to BPR-D-XX.Y-NNN format with AI_Act framework flag. Multi-PSO per CR rule is now supported via the multi-PSO relationship in the catalog.
>
> **Note (2026-08-13, R9 of remediation contract):** This is the canonical Rich Mode version of the Phase 2 rules catalog for Case_02. Earlier text referenced a sibling `../02_PHASE2_RULES/Doc18_Rules_Catalog.md` (a path that no longer exists in this case); that reference has been removed and replaced with this self-referential canonical statement.

---
document_id: AEGIS-P2-11
title: AEGIS Control Set — Rich Mode (Case_02)
phase: 2
version: 6.0
created: 2026-04-03
updated: 2026-08-28
author: Compliance Lead
status: CONTROL_SET_V1
inputs: [Doc14_Obligation_Derivation.md, Doc15_Strategic_Tensions_Report.md, Doc16_Privacy_Security_Goals.md]
outputs: [13_Use_Cases_Catalog.md, 14_Architectural_Nodes.md]
traceability: AEGIS Class Model → RulesCatalog, AbstractRule, ComplianceRule, BestPracticeRule classes
related_documents: 12_Rules_Catalog.xlsx, 00_Taxonomy_Reference.md
normative_intensity_rule: AVG_with_AI_MUST_override
dr_002_resolution: >
  DR-002 definido como AVG (não MAX). MAX mata diferenciação (AP-P2-09).
  AVG preserva SHOULD. Adicionalmente, qualquer CR com AI-C* nas source
  clauses é forçado MUST (NI=3) — alinhamento com a baseline AI_Act
  (todas as 28 cláusulas AI_Act em scope são NI=3 → MUST; AI-C19 Art. 26
  excluded per D1 — SecureBorder is PROVIDER only). Aplicado
  retroactivamente a todos os 79 cartões.
frameworks_mapped: [NIST_CSF_2.0, NIST_Privacy_FW_1.0, NIST_AI_RMF_1.0]
expected_fields_per_card: 20   # Control Set v1 (port Fase 5): 11 base + 1 NI recomputed + 6 Block D anchors + 3 posture statuses (F21/F22) + 2 F23/F24; legacy 18-col and 18-cell (Case_02-specific) rows normalised — corrected numbering, no missing/duplicated fields
fields_per_card: 20   # CR tables 19 cols (17+2), Case_02-specific tables 20 cols; BPR tables 16 cols (14+2) — see §1 mapping
# Case_02 Doc 11 is table-only; fields_per_card counts visible columns. Block D added 6 anchor columns; port Fase 5 replaced the 3 maturity-score columns with Implementation Status (backfill per posture model §4) and added Traceability (F23) + Framework Anchors (F24) columns; an extra Case_02-specific column exists in the D-04/D-05/D-10 tables (declared in the header).
maturity_dual: false   # legacy key (per D11 Case_02, superseded by posture statuses — port Fase 5)
maturity_dual_mode: triple   # legacy key (CSF + Privacy + AI RMF, superseded by posture statuses)
---

# Rules Catalog

## 1. DOCUMENT PURPOSE

> **CONTROL SET v1 (port Fase 5, 2026-08-28).** This catalog implements the
> AEGIS Control Set schema (canonical 24 fields, corrected numbering — the
> Case_01 defects of a missing Field 13 / duplicated Field 14 are NOT
> replicated). Field mapping for this table-format catalog:
> F1 Rule ID · F2 Description · F3 Source (Legal) · F4 Scope (Sub-Domain) ·
> F5 NI · F6 Priority · F7 Verification Criteria · F8 Verification Method ·
> F9 Related Goals (PSO) · F10 Dependencies (Tension) · F11 Type line
> (MUST/SHOULD via NI recomputed) · F12-14 Framework anchors CSF/PF/AIRMF
> (Field 24 part 1) · F21 Implementation Status (CSF) · F22 Implementation
> Status (Privacy) / (AI RMF for BPR) · F23 Traceability (Legal → AG-D →
> OBL-D → PSO) · F24 Framework Anchors cross-reference to §10.1 (ISO 27001,
> NIST 800-53, OWASP ASVS). Fields 15-20 of the canonical schema (owner,
> status history, stakeholders, reporting) are carried by the per-domain
> guidance in §8 and the §10 mapping table.
> Posture statuses are the deterministic legacy backfill per
> IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md §4.

> **CONTROL SET v1 (port Fase 5, 2026-08-28).** This catalog implements the
> AEGIS Control Set schema (canonical 24 fields, corrected numbering — the
> Case_01 defects of a missing Field 13 / duplicated Field 14 are NOT
> replicated). Field mapping for this table-format catalog:
> F1 Rule ID · F2 Description · F3 Source (Legal) · F4 Scope (Sub-Domain) ·
> F5 NI · F6 Priority · F7 Verification Criteria · F8 Verification Method ·
> F9 Related Goals (PSO) · F10 Dependencies (Tension) · F11 Type line
> (MUST/SHOULD via NI recomputed) · F12-14 Framework anchors CSF/PF/AIRMF
> (Field 24 part 1) · F21 Implementation Status (CSF) · F22 Implementation
> Status (Privacy) / (AI RMF for BPR) · F23 Traceability (Legal → AG-D →
> OBL-D → PSO) · F24 Framework Anchors cross-reference to §10.1 (ISO 27001,
> NIST 800-53, OWASP ASVS). Fields 15-20 of the canonical schema (owner,
> status history, stakeholders, reporting) are carried by the per-domain
> guidance in §8 and the §10 mapping table.
> Posture statuses are the deterministic legacy backfill per
> IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md §4.

> **CONTROL SET v1 (port Fase 5, 2026-08-28).** This catalog implements the
> AEGIS Control Set schema (canonical 24 fields, corrected numbering — the
> Case_01 defects of a missing Field 13 / duplicated Field 14 are NOT
> replicated). Field mapping for this table-format catalog:
> F1 Rule ID · F2 Description · F3 Source (Legal) · F4 Scope (Sub-Domain) ·
> F5 NI · F6 Priority · F7 Verification Criteria · F8 Verification Method ·
> F9 Related Goals (PSO) · F10 Dependencies (Tension) · F11 Type line
> (MUST/SHOULD via NI recomputed) · F12-14 Framework anchors CSF/PF/AIRMF
> (Field 24 part 1) · F21 Implementation Status (CSF) · F22 Implementation
> Status (Privacy) / (AI RMF for BPR) · F23 Traceability (Legal → AG-D →
> OBL-D → PSO) · F24 Framework Anchors cross-reference to §10.1 (ISO 27001,
> NIST 800-53, OWASP ASVS). Fields 15-20 of the canonical schema (owner,
> status history, stakeholders, reporting) are carried by the per-domain
> guidance in §8 and the §10 mapping table.
> Posture statuses are the deterministic legacy backfill per
> IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md §4.

This document presents the complete Rules Catalog (Step E1+E2+E3+E4), consolidating compliance rules and best practices with domain mapping. This is the primary output of Phase 2.

**Alignment with Class Model:**
- `RulesCatalog` - Complete collection of rules
- `AbstractRule` - Base class for all rules
- `ComplianceRule` - Rules derived from regulatory obligations
- `BestPracticeRule` - Rules derived from frameworks and best practices

**Phase 2 Step:** E (Rules Catalog Creation)

**Phase 2 Gate:** ✅ COMPLETE when this document and 12_Rules_Catalog.xlsx are approved

---

## 2. RULES CATALOG METADATA

| Attribute | Value |
|-----------|-------|
| rulesCatalogId | RULES-SECUREBORDER-2026-001 |
| completionDate | 2026-04-03 |
| basedOnGoalsCatalog | GOALS-SECUREBORDER-2026-001 |
| completedBy | Compliance Lead |
| phase2Status | COMPLETE |
| ruleFormat | Markdown (human-readable) + Excel (machine-readable) |
| companyContextId | CC-SECUREBORDER-2026-001 |

---

## 3. RULE DEFINITION STRUCTURE

Each rule follows this structure:

| Field | Description | Example |
|-------|-------------|---------|
| Rule ID | Unique identifier | CR-D-01.1-001 |
| Rule Type | COMPLIANCE or BEST_PRACTICE | COMPLIANCE |
| Rule Description | Clear statement of the rule | Data at rest shall be encrypted |
| Source | Origin of the rule | GDPR-C14, CRA-C07, NIS2-C18, AI-C17 |
| Sub-Domain | Target sub-domain | D-01.1 |
| Priority | P1 (NI≥2.8), P2 (NI 2.5-2.799), P3 (NI<2.5) | P1 |
| Verification Method | TEST, INSPECT, DEMONSTRATE, ANALYZE | TEST |
| Related Goals | Linked privacy/security goals | PO-D-01.1-001 |
| Normative Intensity | Derived from source clauses | 3.000 |
| Implementation Mode | NATIVE or INHERITED | NATIVE |
| Tension Reference | Resolved tension affecting rule | T-001, T-002 |

---

## 4. COMPLIANCE RULES CATALOG (38 Rules)

### D-01: Data Protection & Encryption

| Rule ID | Rule Description | Source | Sub-Domain | NI | Priority | Verification | Implementation | Related Goals | Tension Ref | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | AI RMF Note | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|--------|------------|-----|----------|--------------|----------------|---------------|-------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| CR-D-01.1-001 | All personal and product data in persistent storage must be protected by confidentiality mechanisms with segregated cryptographic material management | GDPR-C04, GDPR-C14, CRA-C07, NIS2-C18, AI-C17 | D-01.1 | 3.000 | P1 | TEST | NATIVE | PO-D-01.1-001 | — | 3 (MUST AVG=3.000; AI-C present forces MUST) | PR.DS-01 | PR.DS-P1;CT.DP-P2 | GOVERN-1.6;MEASURE-2.7;MEASURE-2.5 | PARTIAL | PARTIAL | PARTIAL | GDPR-C04, GDPR-C14, CRA-C07, NIS2-C18, AI-C17 → AG-D-01.1-001/-002 → OBL-D-01.1-001 → PO-D-01.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-01.2-001 | All personal and product data crossing network boundaries must be protected by confidentiality mechanisms appropriate to channel classification | GDPR-C15, CRA-C08, NIS2-C18 | D-01.2 | 3.000 | P1 | TEST | NATIVE | PO-D-01.2-001 | — | 3 (MUST AVG=3.000) | PR.DS-02 | PR.DS-P2 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | GDPR-C15, CRA-C08, NIS2-C18 → AG-D-01.2-001/-002 → OBL-D-01.2-001 → PO-D-01.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-01.3-001 | Cryptographic material used by protection mechanisms must be managed with segregation between material access and data access, and with documented lifecycle and integrity verification | CRA-C15, NIS2-C18, AI-C17 | D-01.3 | 3.000 | P1 | INSPECT | NATIVE | SO-D-01.3-001 | — | 3 (MUST AVG=3.000; AI-C present forces MUST) | PR.DS-01 | PR.DS-P1;CT.DP-P2 | MEASURE-2.7;GOVERN-1.6 | PARTIAL | PARTIAL | PARTIAL | CRA-C15, NIS2-C18, AI-C17 → AG-D-01.3-001/-002 → OBL-D-01.3-001 → SO-D-01.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-01.4-001 | All personal and product data must be protected against unauthorised modification through integrity controls appropriate to data class | GDPR-C05, CRA-C09, AI-C18 | D-01.4 | 3.000 | P1 | TEST | NATIVE | PO-D-01.4-001 | — | 3 (MUST AVG=3.000; AI-C present forces MUST) | PR.DS-01;PR.DS-02 | PR.DS-P1;CT.DM-P1;CT.DM-P3 | MEASURE-2.6;MEASURE-2.7;MANAGE-2.3 | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | GDPR-C05, CRA-C09, AI-C18 → AG-D-01.4-001/-002 → OBL-D-01.4-001 → PO-D-01.4-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

**D-01 Summary:** 4 rules | Avg NI: 3.000 | All P1 | All NATIVE | All rules STRUCTURAL (always active) | All CR MUST (4 AI-MUST overrides)

---

### D-02: Vulnerability Management

| Rule ID | Rule Description | Source | Sub-Domain | NI | Priority | Verification | Implementation | Related Goals | Tension Ref | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | AI RMF Note | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|--------|------------|-----|----------|--------------|----------------|---------------|-------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| CR-D-02.1-001 | Identify, track, and remediate vulnerabilities through continuous scanning, SBOM analysis, and pre-release assessment ensuring no known exploitable vulnerabilities at delivery | CRA-C01, CRA-C17, NIS2-C12, AI-C03, AI-C16 | D-02.1 | 3.000 | P1 | TEST + INSPECT | NATIVE | SO-D-02.1-001 | — | 3 (MUST AVG=3.000; AI-C present forces MUST) | ID.RA-01; ID.RA-08 | ID.RA-P3;ID.RA-P5 | MEASURE-1.1;MEASURE-2.1;MEASURE-2.3;MAP-3.3;MEASURE-2.7;MANAGE-1.3;MAP-3.2 | PARTIAL | IMPLEMENTED | IMPLEMENTED | CRA-C01, CRA-C17, NIS2-C12, AI-C03, AI-C16 → AG-D-02.1-001/-002 → OBL-D-02.1-001 → SO-D-02.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-02.2-001 | Implement prompt patch management and security update capability including automatic and signed OTA updates without delay | CRA-C04, CRA-C19, NIS2-C12 | D-02.2 | 3.000 | P1 | TEST | NATIVE | SO-D-02.2-001 | — | 3 (MUST AVG=3.000) | PR.PS-02 | UNMAPPED_PF (no PF 1.0 analogue for product patch/OTA update management) | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | CRA-C04, CRA-C19, NIS2-C12 → AG-D-02.2-001/-002 → OBL-D-02.2-001 → SO-D-02.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-02.3-001 | Publish and maintain coordinated vulnerability disclosure policy (security.txt) with structured reporting to ENISA and national CSIRTs | CRA-C21, CRA-C26, NIS2-C12 | D-02.3 | 3.000 | P1 | INSPECT | NATIVE | SO-D-02.3-001 | — | 3 (MUST AVG=2.667) | ID.RA-08 | ID.IM-P7;GV.PO-P5 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | CRA-C21, CRA-C26, NIS2-C12 → AG-D-02.3-001/-002 → OBL-D-02.3-001 → SO-D-02.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-02.4-001 | Conduct threat-led penetration testing and bias/error testing for AI training data and accuracy performance | NIS2-C13, AI-C04 | D-02.4 | 3.000 | P1 | TEST | NATIVE | SO-D-02.4-001 | — | 3 (MUST AVG=3.000; AI-C present forces MUST) | ID.IM-02;ID.RA-03 | ID.RA-P3;ID.RA-P4;ID.RA-P5 | MEASURE-2.7;MEASURE-2.11 | PARTIAL | IMPLEMENTED | IMPLEMENTED | NIS2-C13, AI-C04 → AG-D-02.4-001/-002 → OBL-D-02.4-001 → SO-D-02.4-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

**D-02 Summary:** 4 rules | Avg NI: 3.000 | All P1 | All NATIVE | All rules STRUCTURAL (always active) | All CR MUST (2 AI-MUST overrides; note: NIS2-C12→NI=3 baseline)

---

### D-03: Access Control

| Rule ID | Rule Description | Source | Sub-Domain | NI | Priority | Verification | Implementation | Related Goals | Tension Ref | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | AI RMF Note | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|--------|------------|-----|----------|--------------|----------------|---------------|-------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| CR-D-03.1-001 | Implement identity lifecycle management with authentication, access control policies, and competent human oversight for AI systems | CRA-C05, NIS2-C16, NIS2-C19, AI-C15 | D-03.1 | 3.000 | P1 | INSPECT | NATIVE | SO-D-03.1-001 | — | 3 (MUST AVG=2.750; AI-C present forces MUST) | PR.AA-01;PR.AA-03;PR.AA-05 | CT.PO-P1 | MAP-3.5;GOVERN-2.1;GOVERN-3.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED | CRA-C05, NIS2-C16, NIS2-C19, AI-C15 → AG-D-03.1-001/-002 → OBL-D-03.1-001 → SO-D-03.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-03.2-001 | Implement multi-factor authentication for all system access points including border control operator interfaces | CRA-C06, NIS2-C17 | D-03.2 | 3.000 | P1 | TEST | NATIVE | SO-D-03.2-001 | — | 3 (MUST AVG=3.000) | PR.AA-03 | UNMAPPED_PF (no PF 1.0 MFA subcategory) | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | CRA-C06, NIS2-C17 → AG-D-03.2-001/-002 → OBL-D-03.2-001 → SO-D-03.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-03.3-001 | Enforce authorization controls and least privilege access for data processing, system administration, and AI oversight functions | GDPR-C10, GDPR-C17, NIS2-C20 | D-03.3 | 3.000 | P1 | INSPECT | NATIVE | PO-D-03.3-001 | — | 3 (MUST AVG=3.000) | PR.AA-05;PR.AA-01 | CT.PO-P1 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | GDPR-C10, GDPR-C17, NIS2-C20 → AG-D-03.3-001/-002 → OBL-D-03.3-001 → PO-D-03.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-03.4-001 | Deliver product with secure default configuration: disable unused ports, no default passwords, most secure default state | CRA-C03 | D-03.4 | 3.000 | P1 | INSPECT | NATIVE | SO-D-03.4-001 | — | 3 (MUST AVG=3.000) | PR.PS-01 | CT.DP-P4;CT.PO-P4 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | CRA-C03 → AG-D-03.4-001/-002 → OBL-D-03.4-001 → SO-D-03.4-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

**D-03 Summary:** 4 rules | Avg NI: 3.000 | All P1 | All NATIVE | D-03.4 is CRA Sole Authority | All rules STRUCTURAL (always active) | All CR MUST (1 AI-MUST override; D-03.1 has NIS2-C19→NI=2)

---

### D-04: Incident Response

| Rule ID | Rule Description | Source | Sub-Domain | NI | Priority | Verification | Implementation | Related Goals | Tension Ref | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | AI RMF Note | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|--------|------------|-----|----------|--------------|----------------|---------------|-------------|---------------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| CR-D-04.1-001 | Implement incident detection and triage systems with impact reduction design, fail-safe mechanisms, and 24/7 SOC monitoring | CRA-C13, NIS2-C28, AI-C25 | D-04.1 | 3.000 | P1 | TEST | NATIVE | SO-D-04.1-001 | — | STRUCTURAL — always active | 3 (MUST AVG=3.000; AI-C present forces MUST) | DE.AE-02;DE.CM-01;DE.CM-09 | CM.AW-P7 | MEASURE-2.4;MEASURE-3.1;MANAGE-2.3;MANAGE-4.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED | CRA-C13, NIS2-C28, AI-C25 → AG-D-04.1-001/-002 → OBL-D-04.1-001 → SO-D-04.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-04.2-001 | Implement containment, mitigation, and business continuity measures including DoS resilience, backup systems, and disaster recovery | GDPR-C18, CRA-C11, NIS2-C05 | D-04.2 | 3.000 | P1 | TEST + DEMONSTRATE | NATIVE | PO-D-04.2-001 | — | STRUCTURAL — always active | 3 (MUST AVG=3.000) | RS.MI-01;RS.MI-02 | PR.PO-P7;CT.DM-P10 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | GDPR-C18, CRA-C11, NIS2-C05 → AG-D-04.2-001/-002 → OBL-D-04.2-001 → PO-D-04.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-04.3-001 | Notify regulatory authorities of significant incidents: 24h early warning to CSIRT (NIS 2/CRA Art.14(1-2)), 72h breach notification to SA (GDPR), market surveillance cooperation (AI_Act 15d/2d), with final report within 1 month (CRA Art.14(3-5): 14d post-fix for vulns, 1 month for incidents) — using unified incident classification workflow | GDPR-C21, GDPR-C23, CRA-C25, NIS2-C25, NIS2-C26, NIS2-C27, AI-C26, AI-C29 | D-04.3 | 3.000 | P1 | TEST + DEMONSTRATE | NATIVE | PO-D-04.3-001 | T-001 | **CONTEXTUAL** — multi-path notification activated when compound event satisfies triggers from 2+ regulations. Max-SLA routing selects notification path based on incident classification. See T-001. | 3 (MUST AVG=3.000; AI-C present forces MUST) | RS.CO-02;RS.CO-03 | CM.AW-P7;CM.PO-P2;CM.PO-P1;GV.PO-P5 | MANAGE-2.3;MANAGE-4.3;GOVERN-1.1 | PARTIAL | PARTIAL | PARTIAL | GDPR-C21, GDPR-C23, CRA-C25, NIS2-C25, NIS2-C26, NIS2-C27, AI-C26, AI-C29 → AG-D-04.3-001/-002 → OBL-D-04.3-001 → PO-D-04.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-04.4-001 | Restore data availability and recover systems after incidents with disaster recovery plans and backup restoration | GDPR-C16, NIS2-C06 | D-04.4 | 3.000 | P1 | DEMONSTRATE | NATIVE | PO-D-04.4-001 | — | STRUCTURAL — always active | 3 (MUST AVG=3.000) | UNMAPPED_PF (no PF 1.0 backup/DR recovery subcategory; CSF IDs corrected to CSF column per Doc19 §1) | UNMAPPED_PF | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | GDPR-C16, NIS2-C06 → AG-D-04.4-001/-002 → OBL-D-04.4-001 → PO-D-04.4-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

**D-04 Summary:** 4 rules | Avg NI: 3.000 | All P1 | All NATIVE | T-001 resolved: unified workflow | All CR MUST (2 AI-MUST overrides)

---

### D-05: Data Lifecycle

| Rule ID | Rule Description | Source | Sub-Domain | NI | Priority | Verification | Implementation | Related Goals | Tension Ref | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | AI RMF Note | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|--------|------------|-----|----------|--------------|----------------|---------------|-------------|---------------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| CR-D-05.1-001 | Minimize data collection to adequate, relevant, and necessary fields only; ensure AI training data relevance and representativeness | GDPR-C01, CRA-C10, AI-C05, AI-C06 | D-05.1 | 3.000 | P1 | INSPECT + ANALYZE | NATIVE | PO-D-05.1-001 | — | STRUCTURAL — always active | 3 (MUST AVG=3.000; AI-C present forces MUST) | PR.DS-10;ID.AM-03 | CT.PO-P4;CT.DP-P4;ID.RA-P3 | GOVERN-1.4;MAP-2.1;MEASURE-2.11;MAP-2.2 | PARTIAL | IMPLEMENTED | IMPLEMENTED | GDPR-C01, CRA-C10, AI-C05, AI-C06 → AG-D-05.1-001/-002 → OBL-D-05.1-001 → PO-D-05.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-05.2-001 | Retain personal data only for defined purpose duration; maintain training data retention for AI lifecycle; comply with government-mandated retention periods | GDPR-C02, GDPR-C03, AI-C07 | D-05.2 | 3.000 | P1 | INSPECT | NATIVE | PO-D-05.2-001 | — | STRUCTURAL — always active | 3 (MUST AVG=3.000; AI-C present forces MUST) | PR.DS-01;PR.PS-06 | CT.PO-P4;CT.DM-P5 | MEASURE-2.4;MEASURE-4.2;GOVERN-1.4 | PARTIAL | IMPLEMENTED | IMPLEMENTED | GDPR-C02, GDPR-C03, AI-C07 → AG-D-05.2-001/-002 → OBL-D-05.2-001 → PO-D-05.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-05.3-001 | Enable right to erasure and secure data removal on user request using cryptographic sharding: destroy identity mappings while retaining anonymized AI activity logs | GDPR-C06, CRA-C16 | D-05.3 | 3.000 | P1 | TEST | NATIVE | PO-D-05.3-001 | T-002 | CONTEXTUAL — activated by erasure request when personal data exists in AI logs. Cryptographic sharding resolves T-002. | 3 (MUST AVG=3.000) | PR.DS-10 | CT.DM-P4;CT.DM-P5 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | GDPR-C06, CRA-C16 → AG-D-05.3-001/-002 → OBL-D-05.3-001 → PO-D-05.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-05.4-001 | Provide data portability in machine-readable format on request within defined timeframe | GDPR-C07 | D-05.4 | 3.000 | P1 | TEST | NATIVE | PO-D-05.4-001 | — | STRUCTURAL — always active | 3 (MUST AVG=3.000) | — | CT.DM-P1;CT.DM-P6 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | GDPR-C07 → AG-D-05.4-001/-002 → OBL-D-05.4-001 → PO-D-05.4-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

**D-05 Summary:** 4 rules | Avg NI: 3.000 | All P1 | All NATIVE | T-002 resolved: cryptographic sharding | All CR MUST (2 AI-MUST overrides)

---

### D-06: Supply Chain

| Rule ID | Rule Description | Source | Sub-Domain | NI | Priority | Verification | Implementation | Related Goals | Tension Ref | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | AI RMF Note | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|--------|------------|-----|----------|--------------|----------------|---------------|-------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| CR-D-06.1-001 | Assess and manage vendor security risks through continuous monitoring, supplier questionnaires, and vendor risk management programs | GDPR-C11, NIS2-C08, NIS2-C23 | D-06.1 | 3.000 | P1 | INSPECT | NATIVE | PO-D-06.1-001 | T-006 | 3 (MUST AVG=3.000) | GV.SC-04; GV.SC-07; ID.RA-10 | ID.IM-P2 | — | PARTIAL | PARTIAL | N/A (non-AI scope) | GDPR-C11, NIS2-C08, NIS2-C23 → AG-D-06.1-001/-002 → OBL-D-06.1-001 → PO-D-06.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-06.2-001 | Generate, maintain, and update Software Bill of Materials (SBOM) documenting all components, dependencies, and known vulnerabilities | CRA-C18 | D-06.2 | 3.000 | P1 | INSPECT | NATIVE | SO-D-06.2-001 | — | 3 (MUST AVG=3.000) | GV.SC-09 | ID.IM-P7 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | CRA-C18 → AG-D-06.2-001/-002 → OBL-D-06.2-001 → SO-D-06.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-06.3-001 | Include mandatory security clauses in all supplier and processor contracts (DPA, security requirements, incident notification) | GDPR-C12, NIS2-C09 | D-06.3 | 3.000 | P1 | INSPECT | NATIVE | PO-D-06.3-001 | — | 3 (MUST AVG=3.000) | GV.SC-05;GV.SC-06 | GV.PO-P5 | — | PARTIAL | PARTIAL | N/A (non-AI scope) | GDPR-C12, NIS2-C09 → AG-D-06.3-001/-002 → OBL-D-06.3-001 → PO-D-06.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-06.4-001 | Define and enforce third-party boundary management with physical isolation per airport/country instance | NIS2-C24 | D-06.4 | 3.000 | P1 | INSPECT | NATIVE | SO-D-06.4-001 | — | 3 (MUST AVG=3.000) | DE.CM-06;PR.IR-01 | UNMAPPED_PF (no PF 1.0 analogue for physical third-party boundary isolation) | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | NIS2-C24 → AG-D-06.4-001/-002 → OBL-D-06.4-001 → SO-D-06.4-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

**D-06 Summary:** 4 rules | Avg NI: 3.000 | All P1 | All NATIVE | D-06.2 is CRA Sole Authority, D-06.4 is NIS 2 Sole Authority | All rules STRUCTURAL (always active) | All CR MUST (0 AI-MUST overrides)

**Nuance — AI_Act Downstream Provider (Art. 25):** If a government authority or third party substantially modifies GuardianGate's AI system, that entity may become the "provider" with full AI_Act Art. 16 obligations. SecureBorder should include written agreements specifying information, capabilities, and technical access needed for downstream compliance. This is an extension of supply chain obligations beyond standard vendor risk management.

---

### D-07: Secure Development

| Rule ID | Rule Description | Source | Sub-Domain | NI | Priority | Verification | Implementation | Related Goals | Tension Ref | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | AI RMF Note | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|--------|------------|-----|----------|--------------|----------------|---------------|-------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| CR-D-07.1-001 | Integrate privacy-by-design, secure-by-default, and manufacturer obligation principles into product design, development, and production per CRA Annex I requirements | GDPR-C09, CRA-C02, CRA-C22 | D-07.1 | 3.000 | P1 | INSPECT | NATIVE | PO-D-07.1-001 | T-007 | 3 (MUST AVG=2.667) | PR.PS-06;ID.RA-01 | GV.PO-P2;CT.PO-P4;CT.DP-P2;CT.DP-P5 | GOVERN-4.1;GOVERN-4.3;MEASURE-2.5;MEASURE-2.6;MEASURE-2.7;GOVERN-1.2 | PARTIAL | PARTIAL | PARTIAL | GDPR-C09, CRA-C02, CRA-C22 → AG-D-07.1-001/-002 → OBL-D-07.1-001 → PO-D-07.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-07.2-001 | Implement secure coding practices including code review, static analysis, and secure development lifecycle | CRA-C02, NIS2-C11 | D-07.2 | 3.000 | P1 | INSPECT | NATIVE | SO-D-07.2-001 | — | 3 (MUST AVG=3.000) | PR.PS-06 | UNMAPPED_PF (no PF 1.0 secure-SDLC subcategory) | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | CRA-C02, NIS2-C11 → AG-D-07.2-001/-002 → OBL-D-07.2-001 → SO-D-07.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-07.3-001 | Secure CI/CD pipeline with protected development and deployment pipelines, signed builds, and integrity verification | NIS2-C11 | D-07.3 | 3.000 | P1 | INSPECT | NATIVE | SO-D-07.3-001 | — | 3 (MUST AVG=3.000) | PR.PS-06;PR.PS-02 | PR.PO-P4 | — | PARTIAL | PARTIAL | N/A (non-AI scope) | NIS2-C11 → AG-D-07.3-001/-002 → OBL-D-07.3-001 → SO-D-07.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-07.4-001 | Implement formal change management procedures for all system modifications with documented approval and rollback capability | NIS2-C10 | D-07.4 | 3.000 | P1 | INSPECT | NATIVE | NOT_ADDRESSED | — | 2 (SHOULD AVG=2.000; NIS2-C10 NI=2) | ID.RA-07 | ID.RA-P3 | — | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | N/A (non-AI scope) | NIS2-C10 → AG-D-07.4-001/-002 → OBL-D-07.4-001 → NOT_ADDRESSED | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

**D-07 Summary:** 4 rules | Avg NI: 3.000 | All P1 | All NATIVE | D-07.3 and D-07.4 are NIS 2 Sole Authority | All rules STRUCTURAL (always active) | 3 CR MUST + 1 CR SHOULD (D-07.4 only; **discrepancy with legacy NI=3.000 — recomputed NI=2 SHOULD**)

---

### D-08: Human Factors

| Rule ID | Rule Description | Source | Sub-Domain | NI | Priority | Verification | Implementation | Related Goals | Tension Ref | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | AI RMF Note | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|--------|------------|-----|----------|--------------|----------------|---------------|-------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| CR-D-08.1-001 | Provide general security awareness training to all staff involved in processing and system operations | GDPR-C27, NIS2-C14 | D-08.1 | 3.000 | P1 | INSPECT | NATIVE | PO-D-08.1-001 | T-008 | 3 (MUST AVG=3.000) | PR.AT-01 | GV.AT-P1;GV.AT-P2 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | GDPR-C27, NIS2-C14 → AG-D-08.1-001/-002 → OBL-D-08.1-001 → PO-D-08.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-08.2-001 | Provide role-specific security competence training for developers, operators, and AI human oversight personnel ensuring appropriate competence levels | GDPR-C28, NIS2-C15, AI-C14, AI-C24 | D-08.2 | 3.000 | P1 | INSPECT | NATIVE | PO-D-08.2-001 | — | 3 (MUST AVG=3.000; AI-C present forces MUST) | PR.AT-02 | GV.AT-P1;GV.AT-P2 | MAP-3.5;GOVERN-2.1;GOVERN-2.2;GOVERN-3.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED | GDPR-C28, NIS2-C15, AI-C14, AI-C24 → AG-D-08.2-001/-002 → OBL-D-08.2-001 → PO-D-08.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-08.3-001 | Ensure management board receives cybersecurity-specific training with awareness of NIS 2 management liability obligations | NIS2-C02 | D-08.3 | 3.000 | P1 | INSPECT | NATIVE | NOT_ADDRESSED | — | 3 (MUST AVG=3.000) | GV.RR-01;PR.AT-02 | UNMAPPED_PF (no PF 1.0 board-training subcategory) | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | NIS2-C02 → AG-D-08.3-001/-002 → OBL-D-08.3-001 → NOT_ADDRESSED | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

**D-08 Summary:** 3 rules | Avg NI: 3.000 | All P1 | All NATIVE | D-08.3 is NIS 2 Sole Authority | All rules STRUCTURAL (always active) | All CR MUST (1 AI-MUST override)

---

### D-09: Governance & Documentation

| Rule ID | Rule Description | Source | Sub-Domain | NI | Priority | Verification | Implementation | Related Goals | Tension Ref | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | AI RMF Note | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|--------|------------|-----|----------|--------------|----------------|---------------|-------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| CR-D-09.1-001 | Establish, document, and maintain comprehensive ISMS with regulation-specific annexes (GDPR, CRA, NIS 2, AI_Act) covering security policies, technical documentation, transparency information, conformity assessment records, and quality management system | GDPR-C08, GDPR-C25, GDPR-C26, CRA-C24, NIS2-C01, AI-C08, AI-C12, AI-C13, AI-C20, AI-C23 | D-09.1 | 3.000 | P1 | INSPECT | NATIVE | PO-D-09.1-001 | T-004 | 3 (MUST AVG=3.000; AI-C present forces MUST) | GV.PO-01;GV.PO-02 | GV.PO-P1;GV.PO-P5;CM.PO-P1 | GOVERN-1.1;GOVERN-1.3;GOVERN-1.4;GOVERN-1.6;MAP-1.1;MEASURE-2.8;MEASURE-2.9;MAP-3.4 | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | GDPR-C08, GDPR-C25, GDPR-C26, CRA-C24, NIS2-C01, AI-C08, AI-C12, AI-C13, AI-C20, AI-C23 → AG-D-09.1-001/-002 → OBL-D-09.1-001 → PO-D-09.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-09.2-001 | Conduct unified impact and risk assessments (DPIA + FRIA) with dual outputs including cybersecurity risk assessment, AI-specific risk assessments, and incident reporting | GDPR-C20, GDPR-C24, CRA-C23, NIS2-C04, AI-C01, AI-C02, AI-C22 | D-09.2 | 3.000 | P1 | ANALYZE | NATIVE | PO-D-09.2-001 | T-003 | 3 (MUST AVG=2.857; AI-C present forces MUST) | ID.RA-04;ID.RA-05;GV.RM-06 | ID.RA-P3;ID.RA-P4;ID.RA-P5 | GOVERN-1.1;GOVERN-1.3;GOVERN-1.5;MAP-5.1;MAP-3.1;MAP-3.2;MANAGE-1.2 | PARTIAL | IMPLEMENTED | IMPLEMENTED | GDPR-C20, GDPR-C24, CRA-C23, NIS2-C04, AI-C01, AI-C02, AI-C22 → AG-D-09.2-001/-002 → OBL-D-09.2-001 → PO-D-09.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-09.3-001 | Maintain comprehensive asset inventories covering all hardware, software, data assets, and AI system components | NIS2-C07 | D-09.3 | 3.000 | P1 | INSPECT | NATIVE | NOT_ADDRESSED | — | 3 (MUST AVG=3.000) | ID.AM-01;ID.AM-02;ID.AM-07 | ID.IM-P1;ID.IM-P4;ID.IM-P6;ID.IM-P8 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | NIS2-C07 → AG-D-09.3-001/-002 → OBL-D-09.3-001 → NOT_ADDRESSED | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-09.4-001 | Maintain records of processing activities (RoPA), AI traceability records, and breach documentation for all personal data and AI system processing | GDPR-C13, GDPR-C22, AI-C11 | D-09.4 | 3.000 | P1 | INSPECT | NATIVE | PO-D-09.4-001 | — | 3 (MUST AVG=2.667; AI-C present forces MUST) | ID.AM-07;GV.OC-03 | ID.IM-P1;ID.IM-P4;ID.IM-P6;ID.IM-P8;CM.PO-P1 | MEASURE-2.4;MEASURE-3.1;GOVERN-1.6;GOVERN-2.1;MEASURE-4.2 | PARTIAL | IMPLEMENTED | IMPLEMENTED | GDPR-C13, GDPR-C22, AI-C11 → AG-D-09.4-001/-002 → OBL-D-09.4-001 → PO-D-09.4-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

**D-09 Summary:** 4 rules | Avg NI: 3.000 | All P1 | All NATIVE | D-09.3 is NIS 2 Sole Authority | All rules STRUCTURAL (always active) | All CR MUST (3 AI-MUST overrides; D-09.2 CRA-C23→NI=2, D-09.4 GDPR-C13→NI=2)

---

### D-10: Monitoring & Audit

| Rule ID | Rule Description | Source | Sub-Domain | NI | Priority | Verification | Implementation | Related Goals | Tension Ref | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | AI RMF Note | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|--------|------------|-----|----------|--------------|----------------|---------------|-------------|---------------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| CR-D-10.1-001 | Implement continuous security monitoring with integrated AI post-market monitoring in unified SOC platform covering attack surface minimization, AI monitoring, and fallback plans | CRA-C12, NIS2-C21, NIS2-C29, AI-C25 | D-10.1 | 3.000 | P1 | TEST | NATIVE | SO-D-10.1-001 | T-005 | STRUCTURAL — always active | 3 (MUST AVG=2.800; AI-C present forces MUST) | DE.CM-01;DE.CM-09;DE.AE-02 | CM.AW-P7 | MANAGE-4.1;MEASURE-3.1;MEASURE-4.1;GOVERN-1.5;MEASURE-2.4 | PARTIAL | PARTIAL | PARTIAL | CRA-C12, NIS2-C21, NIS2-C29, AI-C25 → AG-D-10.1-001/-002 → OBL-D-10.1-001 → SO-D-10.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-10.2-001 | Implement comprehensive audit logging and traceability for all security-relevant events, AI activities, and system operations with minimum 6-month retention using cryptographic sharding for personal data | CRA-C14, NIS2-C22, AI-C09, AI-C10 | D-10.2 | 3.000 | P1 | TEST + INSPECT | NATIVE | SO-D-10.2-001 | T-002 | STRUCTURAL — always active. Retention obligation runs concurrently with potential erasure requests (T-002). | 3 (MUST AVG=3.000; AI-C present forces MUST) | PR.PS-04;DE.AE-03;RS.AN-06 | CT.DM-P9 | MEASURE-2.4;MEASURE-3.1;GOVERN-1.6;MEASURE-4.2;GOVERN-1.4;GOVERN-2.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED | CRA-C14, NIS2-C22, AI-C09, AI-C10 → AG-D-10.2-001/-002 → OBL-D-10.2-001 → SO-D-10.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| CR-D-10.3-001 | Conduct regular compliance testing, security assessments, post-market monitoring, and periodic AI system evaluations | GDPR-C19, CRA-C20, NIS2-C13, AI-C21, AI-C27 | D-10.3 | 3.000 | P1 | TEST + ANALYZE | NATIVE | PO-D-10.3-001 | — | STRUCTURAL — always active | 3 (MUST AVG=2.800; AI-C present forces MUST) | UNMAPPED_PF (no PF 1.0 compliance-testing subcategory; CSF IDs corrected to CSF column per Doc19 §1) | UNMAPPED_PF | MEASURE-2.7;MEASURE-2.11;MANAGE-1.2;MEASURE-3.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED | GDPR-C19, CRA-C20, NIS2-C13, AI-C21, AI-C27 → AG-D-10.3-001/-002 → OBL-D-10.3-001 → PO-D-10.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

**D-10 Summary:** 3 rules | Avg NI: 3.000 | All P1 | All NATIVE | All CR MUST (3 AI-MUST overrides; D-10.1 NIS2-C29→NI=2, D-10.3 CRA-C20→NI=2)

---

## 5. BEST PRACTICE RULES CATALOG (25 Rules)

Best practice rules supplement compliance rules with industry-standard practices that exceed regulatory minimums.

### 5.1 Security Best Practices

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|---------------------|------------|----------|--------------|-------------------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| BPR-D-01.1-001 | Implement dedicated cryptographic material storage segregated from data storage with formal material lifecycle procedures | ISO 27001 A.5.33, NIST SP 800-57 | D-01.1 | P2 | INSPECT | CR-D-01.1-001, CR-D-01.3-001 | 2 (SHOULD BP framework only) | PR.DS-01;PR.DS-10 | PR.DS-P1;CT.DP-P2 | — | PARTIAL | PARTIAL | N/A (non-AI scope) | Implement dedicated cryptographic material storage segregate… best-practice → AG-D-01.1-001/-002 → related CRs: CR-D-01.1-001, CR-D-01.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-02.1-001 | Implement automated vulnerability scanning with 24-hour detection-to-remediation SLA for critical vulnerabilities | industry secure-development standards (PR.PS-01), industry security testing standards (V1) | D-02.1 | P1 | TEST | CR-D-02.1-001, CR-D-02.2-001 | 2 (SHOULD BP framework only) | ID.RA-01;DE.CM-01 | ID.RA-P3;ID.RA-P5 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | Implement automated vulnerability scanning with 24-hour dete… best-practice → AG-D-02.1-001/-002 → related CRs: CR-D-02.1-001, CR-D-02.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-03.1-001 | Implement zero-trust architecture with continuous verification for all access requests | NIST SP 800-207, ISO 27001 A.5.15 | D-03.1 | P2 | TEST | CR-D-03.1-001, CR-D-03.3-001 | 2 (SHOULD BP framework only) | PR.AA-01;PR.AA-05 | CT.PO-P1 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | Implement zero-trust architecture with continuous verificati… best-practice → AG-D-03.1-001/-002 → related CRs: CR-D-03.1-001, CR-D-03.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-04.1-001 | Implement automated incident response playbooks with 15-minute detection-to-triage SLA | NIST SP 800-61, ISO 27001 A.5.24 | D-04.1 | P1 | TEST | CR-D-04.1-001, CR-D-04.3-001 | 2 (SHOULD BP framework only) | DE.AE-02;DE.CM-01 | CM.AW-P7 | MANAGE-2.3;MANAGE-4.3 | PARTIAL | IMPLEMENTED | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | Implement automated incident response playbooks with 15-minu… best-practice → AG-D-04.1-001/-002 → related CRs: CR-D-04.1-001, CR-D-04.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-07.1-001 | Implement automated security testing in CI/CD pipeline with blocking gates for critical findings | industry secure-development standards (PR.IR-04), industry security testing standards | D-07.3 | P2 | TEST | CR-D-07.3-001 | 2 (SHOULD BP framework only) | PR.PS-06 | GV.PO-P2;CT.PO-P4 | GOVERN-4.1;GOVERN-4.3;MEASURE-2.7 | PARTIAL | PARTIAL | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | Implement automated security testing in CI/CD pipeline with … best-practice → AG-D-07.3-001/-002 → related CRs: CR-D-07.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-09.1-001 | Implement automated compliance monitoring dashboard with real-time regulatory compliance status | ISO 27001 A.5.35, NIST CSF DE.CM | D-09.1 | P2 | DEMONSTRATE | CR-D-09.1-001 | 2 (SHOULD BP framework only) | GV.PO-01;GV.PO-02 | GV.PO-P1;GV.PO-P5 | GOVERN-1.1;GOVERN-1.4;GOVERN-1.5 | IMPLEMENTED | IMPLEMENTED | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | Implement automated compliance monitoring dashboard with rea… best-practice → AG-D-09.1-001/-002 → related CRs: CR-D-09.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-10.1-001 | Implement SIEM with AI-powered anomaly detection and automated alerting for border control AI systems | NIST SP 800-53 SI-4, ISO 27001 A.8.16 | D-10.1 | P1 | TEST | CR-D-10.1-001 | 2 (SHOULD BP framework only) | DE.CM-01;DE.CM-09 | CM.AW-P7 | MANAGE-4.1;MEASURE-3.1;MEASURE-2.4 | PARTIAL | PARTIAL | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | Implement SIEM with AI-powered anomaly detection and automat… best-practice → AG-D-10.1-001/-002 → related CRs: CR-D-10.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

### 5.2 AI-Specific Best Practices

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|---------------------|------------|----------|--------------|-------------------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| BPR-D-07.1-002 | Implement AI model versioning with rollback capability for all production AI models | NIST AI RMF GOV 3.2, ISO/IEC 42001 | D-07.1 | P1 | INSPECT | CR-D-07.1-001 | 2 (SHOULD BP framework only) | — | — | MANAGE-4.1 | PARTIAL | PARTIAL | PARTIAL | Implement AI model versioning with rollback capability for a… best-practice → AG-D-07.1-001/-002 → related CRs: CR-D-07.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-10.5-001 | Implement continuous AI accuracy monitoring with automated drift detection and alerting at >1% accuracy degradation | NIST AI RMF MAP 3.1, ISO/IEC 42001 A.8 | D-10.1 | P1 | TEST | CR-D-10.1-001 | 2 (SHOULD BP framework only) | DE.CM-01 | — | MEASURE-2.6; MEASURE-2.7; MANAGE-4.2 | PARTIAL | PARTIAL | PARTIAL | Implement continuous AI accuracy monitoring with automated d… best-practice → AG-D-10.1-001/-002 → related CRs: CR-D-10.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-02.4-001 | Implement AI bias testing suite with quarterly assessment across demographic groups | NIST AI RMF MAP 3.2, EU AI_Act Recital 71 | D-02.4 | P1 | TEST | CR-D-02.4-001 | 2 (SHOULD BP framework only) | ID.RA-03 | ID.RA-P3 | MEASURE-2.6; MEASURE-2.5; MEASURE-2.11 | PARTIAL | PARTIAL | PARTIAL | Implement AI bias testing suite with quarterly assessment ac… best-practice → AG-D-02.4-001/-002 → related CRs: CR-D-02.4-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-03.1-002 | Implement human-in-the-loop override for all border control AI decisions with documented override procedures | EU AI_Act Art. 14, NIST AI RMF GOV 1.3 | D-03.1 | P1 | DEMONSTRATE | CR-D-03.1-001 | 2 (SHOULD BP framework only) | — <!-- human oversight is governance, not technical control; no valid CSF 2.0 anchor --> | — | GOVERN-4.2; GOVERN-5.2; MANAGE-2.3 | PARTIAL | PARTIAL | PARTIAL | Implement human-in-the-loop override for all border control … best-practice → AG-D-03.1-001/-002 → related CRs: CR-D-03.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-10.2-001 | Implement AI explainability reports for each border control decision with confidence scores and contributing factors | EU AI_Act Art. 13, ISO/IEC 42001 A.7 | D-10.2 | P1 | INSPECT | CR-D-10.2-001 | 2 (SHOULD BP framework only) | — <!-- explainability reporting; no CSF 2.0 anchor --> | — | GOVERN-4.1; MEASURE-2.9 | PARTIAL | PARTIAL | PARTIAL | Implement AI explainability reports for each border control … best-practice → AG-D-10.2-001/-002 → related CRs: CR-D-10.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-02.4-002 | Implement adversarial testing for AI models with quarterly red-team exercises targeting biometric spoofing | NIST AI RMF TE 2.3, industry AI security testing standards | D-02.4 | P1 | TEST | CR-D-02.4-001 | 2 (SHOULD BP framework only) | ID.RA-03 | ID.RA-P4 | MEASURE-3.1 | PARTIAL | PARTIAL | PARTIAL | Implement adversarial testing for AI models with quarterly r… best-practice → AG-D-02.4-001/-002 → related CRs: CR-D-02.4-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-04.2-001 | Implement AI incident response playbook specific to AI failures (false accept, false reject, model drift) | NIST AI RMF MM 3.1, ISO/IEC 42001 A.9 | D-04.2 | P1 | DEMONSTRATE | CR-D-04.2-001 | 2 (SHOULD BP framework only) | RS.MA-01 | CM.AW-P* | MANAGE-4.3; MEASURE-3.1 <!-- AI RMF 1.0 has only GOVERN/MAP/MEASURE/MANAGE functions; prior non-canonical RSPF function label removed; MEASURE-3.1 (AI system resilience testing) substituted per AI Act Art. 9(6) + Art. 15 resilience-testing anchor --> | PARTIAL | PARTIAL | PARTIAL | Implement AI incident response playbook specific to AI failu… best-practice → AG-D-04.2-001/-002 → related CRs: CR-D-04.2-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-05.1-001 | Implement AI training data versioning with lineage tracking for all model training datasets | NIST AI RMF MAP 2.2, ISO/IEC 42001 A.6 | D-05.1 | P2 | INSPECT | CR-D-05.1-001 | 2 (SHOULD BP framework only) | ID.AM-03 | CT.PO-P4 | MANAGE-2.3; MAP-1.3 | PARTIAL | PARTIAL | PARTIAL | Implement AI training data versioning with lineage tracking … best-practice → AG-D-05.1-001/-002 → related CRs: CR-D-05.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

---

## 6. RULES SUMMARY DASHBOARD

### 6.1 Compliance Rules by Domain

| Domain | Rules | Avg NI | P1 | P2 | P3 | NATIVE | INHERITED |
|--------|-------|--------|----|----|----|--------|-----------|
| D-01 | 4 | 3.000 | 4 | 0 | 0 | 4 | 0 |
| D-02 | 4 | 3.000 | 4 | 0 | 0 | 4 | 0 |
| D-03 | 4 | 3.000 | 4 | 0 | 0 | 4 | 0 |
| D-04 | 4 | 3.000 | 4 | 0 | 0 | 4 | 0 |
| D-05 | 4 | 3.000 | 4 | 0 | 0 | 4 | 0 |
| D-06 | 4 | 3.000 | 4 | 0 | 0 | 4 | 0 |
| D-07 | 4 | 3.000 | 4 | 0 | 0 | 4 | 0 |
| D-08 | 3 | 3.000 | 3 | 0 | 0 | 3 | 0 |
| D-09 | 4 | 3.000 | 4 | 0 | 0 | 4 | 0 |
| D-10 | 3 | 3.000 | 3 | 0 | 0 | 3 | 0 |
| **TOTAL** | **38** | **3.000** | **38** | **0** | **0** | **38** | **0** |

### 6.2 Best Practice Rules by Category

| Category | Rules | Priority |
|----------|-------|----------|
| Security Best Practices | 7 | 3 P1, 4 P2 |
| AI-Specific Best Practices | 8 | 7 P1, 1 P2 |
| **TOTAL** | **15** | **10 P1, 5 P2** |

### 6.3 Combined Rules Summary

| Metric | Value |
|--------|-------|
| **Total Rules** | **53** (38 Compliance + 15 Best Practice) |
| **P1 (Critical)** | 48 (38 CR + 10 BP) |
| **P2 (Important)** | 5 (all BP) |
| **P3 (Recommended)** | 0 |
| **Verification Methods** | TEST: 18, INSPECT: 18, DEMONSTRATE: 5, ANALYZE: 3 |
| **Rules with Tension Reference** | 8 (CR-D-04.3, CR-D-05.3, CR-D-06.1, CR-D-07.1, CR-D-08.1, CR-D-09.1, CR-D-09.2, CR-D-10.1, CR-D-10.2) |

### 6.4 Sole Authority Rules

| Rule ID | Sub-Domain | Sole Authority Regulation | Must Implement? |
|---------|------------|---------------------------|-----------------|
| CR-D-03.4-001 | D-03.4 | CRA | ✅ Yes (CRA applicable) |
| CR-D-05.4-001 | D-05.4 | GDPR | ✅ Yes (GDPR applicable) |
| CR-D-06.2-001 | D-06.2 | CRA | ✅ Yes (CRA applicable) |
| CR-D-06.4-001 | D-06.4 | NIS 2 | ✅ Yes (NIS 2 applicable) |
| CR-D-07.3-001 | D-07.3 | NIS 2 | ✅ Yes (NIS 2 applicable) |
| CR-D-07.4-001 | D-07.4 | NIS 2 | ✅ Yes (NIS 2 applicable) |
| CR-D-08.3-001 | D-08.3 | NIS 2 | ✅ Yes (NIS 2 applicable) |
| CR-D-09.3-001 | D-09.3 | NIS 2 | ✅ Yes (NIS 2 applicable) |

**All 8 sole authority rules must be implemented** — all 4 regulations are applicable to SecureBorder.

---

## 7. VERIFICATION METHOD DISTRIBUTION

| Method | Count | Description | Example Rules |
|--------|-------|-------------|---------------|
| **TEST** | 18 | Technical testing of controls | CR-D-01.1 (encryption test), CR-D-02.1 (vuln scan) |
| **INSPECT** | 18 | Review of documentation, configuration | CR-D-03.1 (access policy review), CR-D-09.1 (ISMS audit) |
| **DEMONSTRATE** | 5 | Operational demonstration | CR-D-04.2 (DR drill), CR-D-04.3 (notification drill) |
| **ANALYZE** | 3 | Analysis of data, risk assessments | CR-D-05.1 (data minimization analysis), CR-D-09.2 (risk analysis) |

---

## 8. PHASE 2 GATE E CRITERIA

| Criterion | Status | Evidence |
|-----------|--------|----------|
| All 38 obligations mapped to compliance rules | ✅ PASS | Section 4 (38 CR rules) |
| Best practice rules defined | ✅ PASS | Section 5 (25 BP rules) |
| Verification methods assigned | ✅ PASS | Section 7 (TEST/INSPECT/DEMONSTRATE/ANALYZE) |
| Priority classification complete | ✅ PASS | Section 6.3 (48 P1, 5 P2) |
| Tension references inherited | ✅ PASS | Section 6.3 (8 rules with tension refs) |
| Sole authority rules flagged | ✅ PASS | Section 6.4 (8 flagged) |
| Excel catalog generated | ⏳ PENDING | 12_Rules_Catalog.xlsx (next step) |

**Gate E Status:** ✅ **PASS** (pending Excel generation) — Phase 2 essentially complete

---

## 8b. PER-RULE IMPLEMENTATION GUIDANCE (Critical Rules)

### 8.1 CR-D-04.3-001: Regulatory Notification (Unified 24h/72h Workflow)

| Field | Value |
|-------|-------|
| **Rule ID** | CR-D-04.3-001 |
| **Priority** | P1 (CRITICAL) |
| **Source** | GDPR-C21/C23, CRA-C25, NIS2-C25/C26/C27, AI-C26/C29 |
| **Tension Reference** | T-001 (24h vs 72h timing conflict) |

**Implementation Steps:**
1. **Event Detection (0h):** SOC detects security event → auto-create incident ticket
2. **Triage (≤4h):** Classify event type:
   - Type A: Actively exploited vulnerability → CRA 24h ENISA notification
   - Type B: Significant incident → NIS 2 24h CSIRT early warning
   - Type C: Personal data breach → GDPR 72h SA notification
   - Type D: AI incident → AI_Act market surveillance cooperation
   - Type E: Multiple types → Apply shortest deadline (24h)
3. **Early Warning (≤24h):** Send initial notification to CSIRT/ENISA for Types A, B, E
4. **Detailed Notification (≤72h):** Send full breach notification to SA for Types C, E
5. **Final Report (≤1 month):** Submit comprehensive report per NIS 2 Art. 23(3)

**Technical Controls Required:**
- Automated incident classification engine
- Pre-built notification templates for each regulation
- Escalation workflow with 4h/24h/72h/1mo milestones
- Audit trail for all notification timestamps

**Verification:** DEMONSTRATE — Run tabletop exercise simulating personal data breach that is also an actively exploited vulnerability; verify 24h and 72h notifications both sent.

---

### 8.2 CR-D-05.3-001: Right to Erasure (Cryptographic Sharding)

| Field | Value |
|-------|-------|
| **Rule ID** | CR-D-05.3-001 |
| **Priority** | P1 (CRITICAL) |
| **Source** | GDPR-C06, CRA-C16 |
| **Tension Reference** | T-002 (Erasure vs AI_Act Art. 19(1) 6-month logging; Art. 12 = transparency, NOT a D-05.3 participant) |

**Implementation Steps:**
1. **Tokenization at Ingestion:** When traveler data enters AI system, generate irreversible token (SHA-256 with per-traveler salt). Store token→identity mapping in separate encrypted database.
2. **Log Entry Structure:** AI logs contain only tokens (T-XXXX), never raw identity. Match confidence scores and decision outcomes are logged with token reference.
3. **Erasure Request Processing:**
   - Receive erasure request from data subject
   - Locate token→identity mapping in encrypted store
   - Cryptographically destroy mapping (overwrite with random data 7x)
   - Log erasure action with timestamp
   - Retain anonymized AI logs (token-only entries)
4. **Verification:** Attempt to reconstruct identity from token — must fail.

**Technical Controls Required:**
- Tokenization service with cryptographic salt
- Encrypted identity mapping store with separate access controls
- Automated erasure workflow with audit trail
- Token-only log format for AI activity logs

**Verification:** TEST + INSPECT — Submit erasure request; verify identity mapping is unrecoverable; verify AI logs remain intact with tokens only.

---

### 8.3 CR-D-09.1-001: Unified ISMS with Regulation-Specific Annexes

| Field | Value |
|-------|-------|
| **Rule ID** | CR-D-09.1-001 |
| **Priority** | P1 (CRITICAL) |
| **Source** | GDPR-C08/C25/C26, CRA-C24, NIS2-C01, AI-C08/C12/C13/C20/C23 |
| **Tension Reference** | T-004 (Documentation overlap) |

**ISMS Structure:**
```
SecureBorder ISMS (ISO 27001:2022 Foundation)
├── Core ISMS (shared across all regulations)
│   ├── Information Security Policy
│   ├── Risk Management Framework
│   ├── Asset Management
│   ├── Access Control Policy
│   ├── Incident Management
│   └── Business Continuity
├── GDPR Annex
│   ├── Privacy Policy
│   ├── Records of Processing Activities (RoPA)
│   ├── DPIA Templates & Results
│   ├── DPO Designation & Responsibilities
│   └── Data Subject Rights Procedures
├── CRA Annex
│   ├── Technical Documentation (10-year retention)
│   ├── Conformity Assessment Records
│   ├── SBOM (Software Bill of Materials)
│   ├── Vulnerability Disclosure Policy
│   └── Critical Class Certification Records
├── NIS 2 Annex
│   ├── Security Policies (Art. 21)
│   ├── Risk Analysis & Security Concepts
│   ├── Incident Handling Procedures
│   ├── Supply Chain Security Policies
│   └── Management Training Records
└── AI_Act Annex
    ├── AI Technical Documentation
    ├── Conformity Assessment Records
    ├── Post-Market Monitoring Plan
    ├── Quality Management System
    ├── Transparency Information
    └── Fundamental Rights Impact Assessments
```

**Cross-Reference Matrix:** Each regulatory requirement maps to specific ISMS section. Example: GDPR Art. 32 → Core ISMS §5.3 + GDPR Annex §3.2.

**Verification:** INSPECT — Audit ISMS documentation; verify all 4 annexes present, cross-referenced, and up-to-date.

---

### 8.4 CR-D-09.2-001: Unified Impact Assessment (DPIA + FRIA)

| Field | Value |
|-------|-------|
| **Rule ID** | CR-D-09.2-001 |
| **Priority** | P1 (CRITICAL) |
| **Source** | GDPR-C20/C24, CRA-C23, NIS2-C04, AI-C01/C02/C22 |
| **Tension Reference** | T-003 (DPIA vs FRIA trigger mismatch) |

**Unified Assessment Structure:**
```
Unified Impact Assessment (UIA)
├── Section A: System Description (shared)
│   ├── System architecture and data flows
│   ├── Processing purposes and categories
│   └── Stakeholder identification
├── Section B: Data Processing Description (shared)
│   ├── Data categories and sources
│   ├── Processing operations and logic
│   └── Data retention and deletion procedures
├── Section C: Necessity & Proportionality (shared)
│   ├── Legal basis assessment
│   ├── Data minimization analysis
│   └── Purpose limitation verification
├── Section D: Risk Identification (shared)
│   ├── Threat modeling
│   ├── Vulnerability assessment
│   └── Impact analysis
├── Section E: Mitigation Measures (shared)
│   ├── Technical controls
│   ├── Organizational controls
│   └── Residual risk assessment
├── Section F: DPIA (GDPR Art. 35(7))
│   ├── Systematic description of processing operations
│   ├── Necessity and proportionality assessment
│   ├── Risk assessment for data subjects' rights
│   └── Safeguards, security measures, and mechanisms
└── Section G: FRIA (AI_Act Fundamental Rights)
    ├── Affected fundamental rights identification
    ├── Risk to rights holders (travelers, operators)
    ├── Vulnerable persons impact assessment
    └── Post-market fundamental rights monitoring plan
```

**Trigger Alignment:** Initiate UIA when EITHER trigger fires:
- GDPR trigger: High-risk personal data processing (Art. 35)
- AI_Act trigger: High-risk AI system placement (Art. 9)
- Whichever comes first; complete both sections F and G

**Verification:** ANALYZE — Review completed UIA; verify both DPIA and FRIA sections meet respective regulatory requirements.

---

## 9. EXPANDED BEST PRACTICE RULES (25 Total)

### 9.1 Additional Security Best Practices (10 new)

| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |
|---------|------------------|---------------------|------------|----------|--------------|------------|-------------------------------||--------|--------|--------|--------|--------|--------|
| BPR-D-01.2-001 | Implement automated cryptographic material rotation with documented rotation cycle intervals | NIST SP 800-57, ISO 27001 A.5.33 | D-01.3 | P1 | INSPECT | CR-D-01.3-001 | 2 (SHOULD BP framework only) | PR.DS-01 | PR.DS-P1;CT.DP-P2 | — | PARTIAL | PARTIAL | N/A (non-AI scope) | Implement automated cryptographic material rotation with doc… best-practice → AG-D-01.3-001/-002 → related CRs: CR-D-01.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-02.5-001 | Implement automated vulnerability scanning with 24h detection-to-remediation SLA for critical findings | industry secure-development standards (PR.PS-01), industry security testing standards (V1) | D-02.1 | P1 | TEST | CR-D-02.1-001 | 2 (SHOULD BP framework only) | ID.RA-01;DE.CM-01 | ID.RA-P3;ID.RA-P5 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | Implement automated vulnerability scanning with 24h detectio… best-practice → AG-D-02.1-001/-002 → related CRs: CR-D-02.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-03.5-001 | Implement zero-trust architecture with continuous verification for all access requests | NIST SP 800-207, ISO 27001 A.5.15 | D-03.1 | P2 | TEST | CR-D-03.1-001 | 2 (SHOULD BP framework only) | PR.AA-01;PR.AA-05 | CT.PO-P1 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | Implement zero-trust architecture with continuous verificati… best-practice → AG-D-03.1-001/-002 → related CRs: CR-D-03.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-04.5-001 | Implement automated incident response playbooks with 15-min detection-to-triage SLA | NIST SP 800-61, ISO 27001 A.5.24 | D-04.1 | P1 | TEST | CR-D-04.1-001 | 2 (SHOULD BP framework only) | DE.AE-02;DE.CM-01 | CM.AW-P7 | MANAGE-2.3;MANAGE-4.3 | PARTIAL | IMPLEMENTED | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | Implement automated incident response playbooks with 15-min … best-practice → AG-D-04.1-001/-002 → related CRs: CR-D-04.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-05.5-001 | Implement automated data classification and labeling for all personal and biometric data | ISO 27001 A.5.12, NIST SP 800-53 MP-3 | D-05.1 | P2 | INSPECT | CR-D-05.1-001 | 2 (SHOULD BP framework only) | PR.DS-10;ID.AM-03 | CT.PO-P4;CT.DP-P4 | MAP-2.1;MAP-2.2;MEASURE-2.11 | PARTIAL | IMPLEMENTED | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | Implement automated data classification and labeling for all… best-practice → AG-D-05.1-001/-002 → related CRs: CR-D-05.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-06.5-001 | Implement continuous supplier security scoring with automated alerting for score degradation | ENISA Supplier Security Guidelines | D-06.1 | P2 | DEMONSTRATE | CR-D-06.1-001 | 2 (SHOULD BP framework only) | GV.SC-04; GV.SC-07 | ID.IM-P2 | — | PARTIAL | PARTIAL | N/A (non-AI scope) | Implement continuous supplier security scoring with automate… best-practice → AG-D-06.1-001/-002 → related CRs: CR-D-06.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-07.5-001 | Implement automated security gates in CI/CD pipeline blocking deployment on critical findings | industry secure-development standards (PR.IR-04), industry security testing standards | D-07.3 | P1 | TEST | CR-D-07.3-001 | 2 (SHOULD BP framework only) | PR.PS-06;PR.PS-02 | PR.PO-P4 | — | PARTIAL | PARTIAL | N/A (non-AI scope) | Implement automated security gates in CI/CD pipeline blockin… best-practice → AG-D-07.3-001/-002 → related CRs: CR-D-07.3-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-08.4-001 | Implement phishing simulation testing quarterly for all employees with targeted remediation | NIST SP 800-50, ENISA Guidelines | D-08.1 | P2 | TEST | CR-D-08.1-001 | 2 (SHOULD BP framework only) | PR.AT-01 | GV.AT-P1;GV.AT-P2 | — | PARTIAL | IMPLEMENTED | N/A (non-AI scope) | Implement phishing simulation testing quarterly for all empl… best-practice → AG-D-08.1-001/-002 → related CRs: CR-D-08.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-09.5-001 | Implement automated compliance monitoring dashboard with real-time regulatory status tracking | ISO 27001 A.5.35, NIST CSF DE.CM | D-09.1 | P2 | DEMONSTRATE | CR-D-09.1-001 | 2 (SHOULD BP framework only) | GV.PO-01;GV.PO-02 | GV.PO-P1;GV.PO-P5 | GOVERN-1.1;GOVERN-1.4;GOVERN-1.5 | IMPLEMENTED | IMPLEMENTED | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | Implement automated compliance monitoring dashboard with rea… best-practice → AG-D-09.1-001/-002 → related CRs: CR-D-09.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |
| BPR-D-10.4-001 | Implement SIEM with AI-powered anomaly detection and automated alerting for border control AI systems | NIST SP 800-53 SI-4, ISO 27001 A.8.16 | D-10.1 | P1 | TEST | CR-D-10.1-001 | 2 (SHOULD BP framework only) | DE.CM-01;DE.CM-09 | CM.AW-P7 | MANAGE-4.1;MEASURE-3.1;MEASURE-2.4 | PARTIAL | PARTIAL | N/A — EXCLUDED (NI=2 SHOULD; not in posture scope (legacy maturity wording)) | Implement SIEM with AI-powered anomaly detection and automat… best-practice → AG-D-10.1-001/-002 → related CRs: CR-D-10.1-001 | CSF/PF/AIRMF inline; ISO 27001 + NIST 800-53 + OWASP ASVS → §10.1 row |

|----------|-------|----|----|
| Security Best Practices | 17 | 8 | 9 |
| AI-Specific Best Practices | 8 | 7 | 1 |
| **Total BP Rules** | **25** | **15** | **10** |

---

## 10. FRAMEWORK MAPPING TABLE

### 10.1 Rules → Framework Mapping

| Rule ID | ISO 27001:2022 | NIST CSF 2.0 | NIST 800-53 | OWASP ASVS | NIST AI RMF |
|---------|----------------|-------------|-------------|------------|-------------|
| CR-D-01.1-001 | A.5.33, A.8.24 | PR.DS-01 | SC-28, SC-13 | V2.1 | — |
| CR-D-01.2-001 | A.5.33, A.8.24 | PR.DS-02 | SC-8, SC-13 | V2.2 | — |
| CR-D-02.1-001 | A.5.36, A.8.8 | DE.CM-01 | RA-5, SI-2 | V1.4 | GOV 2.2 |
| CR-D-02.2-001 | A.5.36, A.8.19 | PR.PS-01 | SI-2 | V1.5 | — |
| CR-D-03.1-001 | A.5.15, A.5.16 | PR.AA-01 | AC-2, IA-2 | V3.1 | GOV 1.3 |
| CR-D-04.1-001 | A.5.24, A.8.16 | ID.AM-03 | IR-4, SI-4 | V7.1 | MM 2.1 |
| CR-D-04.3-001 | A.5.24, A.5.26 | RS.MA-01 | IR-6, IR-7 | V7.3 | MM 3.1 |
| CR-D-05.1-001 | A.5.34, A.8.3 | PR.DS-01 | SC-28, MP-3 | V4.1 | MAP 2.2 |
| CR-D-06.1-001 | A.5.19, A.5.20 | GV.SC-03 | SR-2, SR-3 | — | — |
| CR-D-07.1-001 | A.5.8, A.8.25 | PR.PS-01 | SA-3, SA-4 | V1.1 | GOV 3.2 |
| CR-D-08.1-001 | A.6.3, A.6.4 | PR.AT-01 | AT-2, AT-3 | — | — |
| CR-D-09.1-001 | A.5.1, A.5.35 | GV.PO-01 | PM-1, PM-9 | — | GOV 1.1 |
| CR-D-09.2-001 | A.5.11, A.5.12 | ID.RA-01 | RA-3, RA-9 | — | MAP 1.1 |
| CR-D-10.1-001 | A.8.15, A.8.16 | DE.CM-01 | SI-4, AU-6 | V7.2 | MM 2.1 |
| CR-D-10.2-001 | A.8.15, A.8.25 | DE.CM-02 | AU-2, AU-12 | V7.4 | MAP 3.1 |
| CR-D-10.3-001 | A.5.35, A.8.35 | DE.CM-06 | CA-2, CA-7 | V1.6 | MM 3.2 |

### 10.2 Framework Coverage Summary

| Framework | Controls Mapped | Coverage % | Primary Domains |
|-----------|----------------|------------|-----------------|
| ISO 27001:2022 | 32/38 | 84.2% | All domains |
| NIST CSF 2.0 | 28/38 | 73.7% | Identify, Protect, Detect |
| NIST 800-53 | 25/38 | 65.8% | SC, SI, IR, AC, RA |
| OWASP ASVS | 12/38 | 31.6% | V1, V2, V3, V7 |
| NIST AI RMF | 10/38 | 26.3% | GOV, MAP, MM, TE |

---


## Annex A — CSF 2.0 Function Index (generated, port Fase 5)

| Function | Controls anchoring at least one subcategory of the function |
|---|---|
| GV (GOVERN) | 8 controls: BPR-D-06.5-001, BPR-D-09.1-001, BPR-D-09.5-001, CR-D-06.1-001, CR-D-06.2-001, CR-D-06.3-001, CR-D-08.3-001, CR-D-09.1-001 |
| ID (IDENTIFY) | 12 controls: BPR-D-02.1-001, BPR-D-02.4-001, BPR-D-02.4-002, BPR-D-02.5-001, BPR-D-05.1-001, CR-D-02.1-001, CR-D-02.3-001, CR-D-02.4-001… |
| PR (PROTECT) | 30 controls: BPR-D-01.1-001, BPR-D-01.2-001, BPR-D-02.1-001, BPR-D-02.5-001, BPR-D-03.1-001, BPR-D-03.5-001, BPR-D-05.5-001, BPR-D-07.1-001… |
| DE (DETECT) | 8 controls: BPR-D-04.1-001, BPR-D-04.5-001, BPR-D-10.1-001, BPR-D-10.4-001, BPR-D-10.5-001, CR-D-04.1-001, CR-D-06.4-001, CR-D-10.1-001 |
| RS (RESPOND) | 3 controls: BPR-D-04.2-001, CR-D-04.2-001, CR-D-04.3-001 |
| RC (RECOVER) | 0 controls:  |

## Annex B — ISO 27001:2022 Annex A Index (from §10.1)

| Rule | ISO 27001:2022 controls |
|---|---|
| CR-D-01.1-001 | A.5.33, A.8.24 |
| CR-D-01.2-001 | A.5.33, A.8.24 |
| CR-D-02.1-001 | A.5.36, A.8.8 |
| CR-D-02.2-001 | A.5.36, A.8.19 |
| CR-D-03.1-001 | A.5.15, A.5.16 |
| CR-D-04.1-001 | A.5.24, A.8.16 |
| CR-D-04.3-001 | A.5.24, A.5.26 |
| CR-D-05.1-001 | A.5.34, A.8.3 |
| CR-D-06.1-001 | A.5.19, A.5.20 |
| CR-D-07.1-001 | A.5.8, A.8.25 |
| CR-D-08.1-001 | A.6.3, A.6.4 |
| CR-D-09.1-001 | A.5.1, A.5.35 |
| CR-D-09.2-001 | A.5.11, A.5.12 |
| CR-D-10.1-001 | A.8.15, A.8.16 |
| CR-D-10.2-001 | A.8.15, A.8.25 |
| CR-D-10.3-001 | A.5.35, A.8.35 |

## Annex C — Statutory Source Index

Per-regulation touch count across the 63 controls (a control may cite several):

- **GDPR:** 20 controls
- **CRA:** 23 controls
- **NIS 2:** 29 controls
- **AI Act:** 19 controls

## 11. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 6.0 | 2026-08-28 | Executor (port Fase 5) | **Control Set v1.** Catalog tables carry the corrected 24-field schema mapping: maturity-score columns → Implementation Status (F21/F22, deterministic backfill per posture model §4), Traceability (F23: Legal → AG-D → OBL-D → PSO) and Framework Anchors (F24, cross-ref §10.1) added; corrupt duplicate separator rows removed; Annexes A–C appended; control_set.yaml now generated by `validation/build_control_set.py` (63 controls; Case_01 `'**'` status-parsing bug fixed). |

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-03 | Compliance Lead | Initial release - SecureBorder Solutions case (38 CR + 25 BP = 63 rules) |
| 1.1 | 2026-04-03 | Compliance Lead | Expanded: per-rule implementation guidance (4 critical rules), 10 additional BP rules (25 total), framework mapping table (5 frameworks) |

---

## 10b. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Compliance Lead | 2026-04-03 |
| Technical Review (CTO) |
| Security Review (CISO) |
| AEGIS Methodology Review |

---

**Next Document:** 12_Rules_Catalog.xlsx (Excel generation)
**Phase 2 Status:** ✅ COMPLETE (pending Excel) — Ready for Phase 3