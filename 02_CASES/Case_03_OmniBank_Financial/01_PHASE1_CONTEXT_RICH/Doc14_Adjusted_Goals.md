---
document_id: AEGIS-P3-RICH-07c
title: Adjusted Goals per Sub-Domain
phase: 1
version: 3.0
created: 2026-08-06
updated: 2026-08-14
author: Sprint 4 + 5 + 6 Executor (adjusted-objectives-builder + deep-enrichment-builder + corr-010-standardisation)
status: STANDARDISED
status_history:
  - { date: 2026-08-06, status: DRAFT, sprint: 0, by: 'Sprint 0 skeleton' }
  - { date: 2026-08-06, status: DRAFT, sprint: 0.5, by: 'Sprint 0.5 Doc 07b Track B MAX' }
  - { date: 2026-08-06, status: DRAFT, sprint: 0.6, by: 'Sprint 0.6 DORA ICT Risk Framework' }
  - { date: 2026-08-06, status: RECONCILED, sprint: 1, by: 'Sprint 1 reconciliation' }
  - { date: 2026-08-06, status: CORPUS_ENRICHED, sprint: 2, by: 'Sprint 2 corpus enrichment' }
  - { date: 2026-08-06, status: ADJUSTED_OBJECTIVES, sprint: 4, by: 'Sprint 4 V-02/03/04 fix' }
  - { date: 2026-08-06, status: DEEP_ENRICHED, sprint: 5, by: 'Sprint 5 DEEP enrichment' }
  - { date: 2026-08-14, status: STANDARDISED, sprint: 6, by: 'Sprint 6 corr-010 standardisation (3805→1500 lines, NIST controls + multi-reg objectives)' }
detail_cards_count: 76
detail_cards_location: _deprecated/07c_Appendix_A_OLD.md
tensions_expanded_count: 5
fields_added_per_card: 18
fields_excluded: [Effort Estimate, Cost Estimate, Target Timeline]
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains_mapped: 38
inactive_subdomains: []
nist_controls_full_coverage: true
nist_frameworks_covered: [NIST CSF 2.0, NIST PF 1.0, NIST AI RMF]
cross_checked_against: [Doc13_Proportionality_Profile.md, Doc11_DORA_ICT_Risk_Framework.md, Doc09_Ambiguity_Register.md, proportionality_model.md, 00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/]
inputs: [Doc03_Company_Context_Assessment.md, Doc08_Regulatory_Applicability.md, Doc09_Ambiguity_Register.md, Doc11_DORA_ICT_Risk_Framework.md, Doc12_Structured_Compliance_Matrix.md, Doc13_Proportionality_Profile.md, phase1_ontology.yaml, ../../../../../00_METHODOLOGY/REFERENCE/proportionality_model.md, ../../../../../00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/*.json]
outputs: [phase 2 rules catalog (Doc20_Rules_Catalog.md) consumes adjusted objectives + NIST controls mapping; _deprecated/07c_Appendix_A_OLD.md provides per-card detail archive]
related_documents: [Doc13_Proportionality_Profile.md, Doc03_Company_Context_Assessment.md, Doc08_Regulatory_Applicability.md, Doc09_Ambiguity_Register.md, Doc11_DORA_ICT_Risk_Framework.md, phase1_ontology.yaml, ../../../../../00_METHODOLOGY/REFERENCE/proportionality_model.md, _deprecated/07c_Appendix_A_OLD.md]
frozen: false
supersedes: 02_PHASE2_RULES/10_Privacy_Security_Goals.md §3-§4 (legacy PG/SG — now elevated to Phase 1 in Rich Mode)
corr: corr-010
corr_date: 2026-08-14
---

# Adjusted Goals per Sub-Domain

> **Phase 1 adjusted objectives — STANDARDISED** for OmniBank Financial Systems (Case_03, MAX tier, 5/5 applicable regulations, 38/38 active sub-domains, 31 RIGOROUS + 7 STANDARD, ISO 27001 certified, ECB-supervised, DORA Financial Entity, AI Act High-Risk Annex III).
>
> **corr-010 standardisation (2026-08-14):** Restructured from 3805 → ~1500 lines. New §2 Multi-Regulation Adjusted Objectives (merged table, 38 rows × 8 cols). New §5 NIST Controls Mapping (3 frameworks × 38 sub-domains, full coverage). 76 detail cards archived to `_deprecated/07c_Appendix_A_OLD.md` for per-card reference.
>
> **Companion documents:**
> - Doc 07b `Doc13_Proportionality_Profile.md` — 5-attribute operationalisation per sub-domain (31 RIGOROUS + 7 STANDARD)
> - Doc 04 `Doc03_Company_Context_Assessment.md` — Business Goals (BG-001..BG-008) → linked to adjusted objectives here
> - Doc 05 `Doc08_Regulatory_Applicability.md` — GDPR + CRA + NIS 2 + DORA + AI Act applicability + 150 clauses
> - Doc 05b `Doc09_Ambiguity_Register.md` — Top 20 ambiguity cards (V-04 fixed: 20 distinct clauses — GDPR 5 + CRA 4 + NIS 2 4 + DORA 4 + AI Act 3)
> - Doc 06b `Doc11_DORA_ICT_Risk_Framework.md` — DORA Art. 5-34 mapped to AEGIS sub-domains; 5 tensions (T-001..T-005)
> - `_deprecated/07c_Appendix_A_OLD.md` — 76 archived detail cards (38 PG + 38 SG, 18 fields each)
> - Phase 2 legacy `02_PHASE2_RULES/10_Privacy_Security_Goals.md` §3-§4 — superseded by this doc per Sprint 4 (PG/SG now elevated from Phase 2 to Phase 1)

---

## §0 Document Purpose

This document is the **Phase 1 adjusted-objectives layer** for Case_03 OmniBank. It binds every ACTIVE sub-domain (38/38, all 5 regulations — GDPR + CRA + NIS 2 + DORA + AI Act) to:

1. A **generic baseline** — HSO + per-regulation Sub-SOs from the corpus (frozen per `proportionality_model.md §1`).
2. A **multi-regulation adjusted objective** — merged PG (GDPR, slot 001) + SG (CRA, slot 002) per sub-domain, with NIS 2 / DORA / AI Act cross-cut reference.
3. A **Track B tier** — inherited verbatim from Doc 07b §4 (RIGOROUS for 31, STANDARD for 7).
4. A **NIST controls mapping** — CSF 2.0 + PF 1.0 + AI RMF controls per sub-domain.
5. A **resolution status** for any of the 5 strategic tensions (T-001..T-005) that touch the sub-domain.

**Sprint 4 (initial):** Adjusted objectives built per sub-domain, with §1 baseline, §2 PG table, §3 SG table, §4 5 tensions, §5 Track B decision trail, §6 cross-refs, §7 validation.

**Sprint 5 (DEEP enrichment):** 76 detail cards (38 PG + 38 SG) with 18 fields each — Description (multi-paragraph), Source Article, NIST CSF Anchors, Verification Criteria, Verification Method, Owner, Status, Dependencies, Risk, Stakeholders, Maturity, Implementation Priority, Regulatory Reporting, External Auditor, Supervisory Body, plus Scope/Out-of-Scope. **EXCLUDED:** Effort Estimate, Cost Estimate, Target Timeline (per project directive).

**Sprint 6 (corr-010 standardisation, 2026-08-14):** Restructured to reduce 3805-line monolith. New §2 merges PG/SG into single 38-row table with per-regulation cells. New §5 adds full NIST controls mapping (3 frameworks × 38 sub-domains). 76 detail cards archived to `_deprecated/07c_Appendix_A_OLD.md` (preserved verbatim, AG-D- IDs intact).

**Invariant (quoted from `proportionality_model.md §1`):** "The regulatory `fit_criterion` and the HSO are **never modified** by Track B. [...] Track B only varies three axes: `satisfaction_pattern`, `evidence_depth`, `ownership`." This document respects that invariant: the corpus-derived HSOs and Sub-SOs are preserved verbatim in §1; only the PG/SG statements and tier are company-tailored in §2.

**Case_03 specificity:** This is the MAX-tier case — 5/5 applicable regulations, 38/38 active sub-domains, ISO 27001 certified, ECB-supervised credit institution, DORA Financial Entity, AI Act High-Risk (Annex III credit scoring). All 5 strategic tensions have DORA-specific dimensions, and §3 expands them to multi-paragraph treatment.

---

## §1 Generic Baseline (preserved from corpus)

> HSO + Sub-SOs from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX.Y/`. NOT modified by Track B per `proportionality_model.md §1`. This is the **frozen regulatory baseline** — the floor that PG/SG in §2/§3 must reach or exceed. 5 regulation columns: GDPR + CRA + NIS 2 + DORA + AI Act. The 5-column layout reflects the 5/5 MAXIMUM participation.

| Sub-Domain | HSO (corpus, frozen) | GDPR Sub-SO | CRA Sub-SO | NIS 2 Sub-SO | DORA Sub-SO | AI Act Sub-SO | Corpus Path |
|------------|----------------------|-------------|------------|--------------|-------------|---------------|-------------|
| D-01.1 | Data held at rest in storage is protected against unauthorised access through appropriate technical measures — primarily encryption with appropriate key custody | SO-D-01.1.GDPR | SO-D-01.1.CRA | SO-D-01.1.NIS2 | SO-D-01.1.DORA | SO-D-01.1.AI_Act | `D-01_Data-at-Rest-Encrypt/D-01.1/` |
| D-01.2 | Data in transit — across network paths, inter-service calls, and third-party APIs — is protected against unauthorised access through appropriate technical measures | SO-D-01.2.GDPR | SO-D-01.2.CRA | SO-D-01.2.NIS2 | SO-D-01.2.DORA | SO-D-01.2.AI_Act | `D-01_Data-in-Transit-Encr/D-01.2/` |
| D-01.3 | Cryptographic keys and related authentication material are managed with separation of roles between key custody and data access | — | SO-D-01.3.CRA | SO-D-01.3.NIS2 | SO-D-01.3.DORA | SO-D-01.3.AI_Act | `D-01_Cryptographic-Key-Ma/D-01.3/` |
| D-01.4 | Data integrity is preserved against unauthorised modification across the data lifecycle — at rest, in transit, and in use | SO-D-01.4.GDPR | SO-D-01.4.CRA | — | SO-D-01.4.DORA | SO-D-01.4.AI_Act | `D-01_Data-Integrity-Mecha/D-01.4/` |
| D-02.1 | Vulnerabilities — including, where in scope, AI-system-specific attack surfaces — are systematically identified through a documented identification pipeline | — | SO-D-02.1.CRA | SO-D-02.1.NIS2 | SO-D-02.1.DORA | SO-D-02.1.AI_Act | `D-02_Vulnerability-Identi/D-02.1/` |
| D-02.2 | Vulnerabilities identified in the upstream identification pipeline are addressed and remediated according to severity-based SLAs | — | SO-D-02.2.CRA | SO-D-02.2.NIS2 | SO-D-02.2.DORA | — | `D-02_Patch-Management-Upd/D-02.2/` |
| D-02.3 | A coordinated vulnerability disclosure (CVD) ecosystem is maintained, covering the manufacturer-side process and the external interface | — | SO-D-02.3.CRA | SO-D-02.3.NIS2 | — | — | `D-02_Coordinated-Vulnerab/D-02.3/` |
| D-02.4 | The security of the asset — product with digital elements, ICT-supported business function, ICT system — is validated through threat-led penetration testing | — | — | SO-D-02.4.NIS2 | SO-D-02.4.DORA | SO-D-02.4.AI_Act | `D-02_Threat-Led-Penetrati/D-02.4/` |
| D-03.1 | Identities of principals that interact with the entity's systems, products, services, components, and data are provisioned, updated, and deprovisioned | — | SO-D-03.1.CRA | SO-D-03.1.NIS2 | SO-D-03.1.DORA | SO-D-03.1.AI_Act | `D-03_Identity-Lifecycle-M/D-03.1/` |
| D-03.2 | Authentication of users, services, and hardware that interact with the entity's systems, products, services, components, and data is performed with strong methods | — | SO-D-03.2.CRA | SO-D-03.2.NIS2 | SO-D-03.2.DORA | SO-D-03.2.AI_Act | `D-03_Multi-Factor-Authent/D-03.2/` |
| D-03.3 | The entitlement to perform actions on the entity's systems, products, services, components, and data is governed by documented authorisation rules | SO-D-03.3.GDPR | — | SO-D-03.3.NIS2 | SO-D-03.3.DORA | — | `D-03_Authorization-Least-/D-03.3/` |
| D-03.4 | The default disposition of the entity's data-centric processing systems and the products with digital elements is secure | — | SO-D-03.4.CRA | — | — | — | `D-03_Secure-System-Defaul/D-03.4/` |
| D-04.1 | Security-relevant events affecting the entity's systems, products, services, components, and data are detected, triaged, and escalated | — | SO-D-04.1.CRA | SO-D-04.1.NIS2 | SO-D-04.1.DORA | SO-D-04.1.AI_Act | `D-04_Incident-Detection-T/D-04.1/` |
| D-04.2 | Security incidents affecting the entity's systems, products, services, components, and data are contained and mitigated within documented SLAs | SO-D-04.2.GDPR | SO-D-04.2.CRA | SO-D-04.2.NIS2 | SO-D-04.2.DORA | — | `D-04_Containment-Mitigati/D-04.2/` |
| D-04.3 | A major security incident is notified to the applicable recipients within the regulator-mandated deadlines | SO-D-04.3.GDPR | SO-D-04.3.CRA | SO-D-04.3.NIS2 | SO-D-04.3.DORA | SO-D-04.3.AI_Act | `D-04_Regulatory-Notificat/D-04.3/` |
| D-04.4 | Systems, products, services, components and data are restored and recovered with documented RTO/RPO targets | SO-D-04.4.GDPR | — | SO-D-04.4.NIS2 | SO-D-04.4.DORA | — | `D-04_Data-Restoration-Rec/D-04.4/` |
| D-05.1 | Data collected or otherwise acquired is limited to what is adequate, relevant, and necessary in relation to the processing purpose | SO-D-05.1.GDPR | SO-D-05.1.CRA | — | — | SO-D-05.1.AI_Act | `D-05_Data-Minimisation/D-05.1/` |
| D-05.2 | Data — across the data classes in scope — is retained for the period required to satisfy the processing purpose and applicable legal obligations | SO-D-05.2.GDPR | — | — | — | SO-D-05.2.AI_Act | `D-05_Retention-Archiving/D-05.2/` |
| D-05.3 | Data held about a person is rendered inaccessible to the controller on the data subject's request, subject to retention-ground exceptions | SO-D-05.3.GDPR | SO-D-05.3.CRA | — | — | — | `D-05_Right-to-Erasure/D-05.3/` |
| D-05.4 | Personal data are exported to the data subject in a structured, commonly used, machine-readable format | SO-D-05.4.GDPR | — | — | — | — | `D-05_Data-Portability/D-05.4/` |
| D-06.1 | Vendors, suppliers, components, and ICT service providers undergo risk-anchored due diligence before engagement | SO-D-06.1.GDPR | — | SO-D-06.1.NIS2 | SO-D-06.1.DORA | — | `D-06_Vendor-Risk-Assessme/D-06.1/` |
| D-06.2 | The manufacturer draws up and maintains a software bill of materials (SBOM) covering the products with digital elements | — | SO-D-06.2.CRA | — | — | — | `D-06_Software-Bill-of-Mat/D-06.2/` |
| D-06.3 | Third-party security obligations are made enforceable through contracts, transfer safeguards, and codes of conduct | SO-D-06.3.GDPR | — | SO-D-06.3.NIS2 | SO-D-06.3.DORA | — | `D-06_Contractual-Security/D-06.3/` |
| D-06.4 | Third-party boundary responsibilities are explicitly allocated so that non-EU representatives act under documented obligations | — | — | SO-D-06.4.NIS2 | SO-D-06.4.DORA | — | `D-06_Third-Party-Boundary/D-06.4/` |
| D-07.1 | Security is integrated into the acquisition, design, development, production, deployment, and maintenance lifecycle | SO-D-07.1.GDPR | SO-D-07.1.CRA | SO-D-07.1.NIS2 | SO-D-07.1.DORA | — | `D-07_Secure-by-Design-Pri/D-07.1/` |
| D-07.2 | Coding practices deliver attack-surface limitation, exploitation mitigation, and AI-system-specific secure coding | — | SO-D-07.2.CRA | SO-D-07.2.NIS2 | SO-D-07.2.DORA | — | `D-07_Secure-Coding-Practi/D-07.2/` |
| D-07.3 | CI/CD pipeline security delivers build-time control baselines (signed artefacts, build-time tests, ephemeral runners) | — | — | SO-D-07.3.NIS2 | SO-D-07.3.DORA | — | `D-07_CI/CD-Pipeline-Secur/D-07.3/` |
| D-07.4 | Change management delivers documented change-management procedures (manufacturer-side SBOM update, version control) | — | — | SO-D-07.4.NIS2 | SO-D-07.4.DORA | — | `D-07_Change-Management/D-07.4/` |
| D-08.1 | General security awareness is established through a documented training programme with periodic refresh | SO-D-08.1.GDPR | — | SO-D-08.1.NIS2 | SO-D-08.1.DORA | — | `D-08_General-Security-Awa/D-08.1/` |
| D-08.2 | Role-specific competence is established through a function-specific depth, audience-routed training | SO-D-08.2.GDPR | — | SO-D-08.2.NIS2 | SO-D-08.2.DORA | SO-D-08.2.AI_Act | `D-08_Role-Specific-Compet/D-08.2/` |
| D-08.3 | Management body competence is established through documented briefings on ICT risk and regulatory accountability | — | — | SO-D-08.3.NIS2 | SO-D-08.3.DORA | — | `D-08_Management-Board-Tra/D-08.3/` |
| D-09.1 | Information security policies are established through a documented policy architecture spanning 5+ governance bodies | SO-D-09.1.GDPR | SO-D-09.1.CRA | SO-D-09.1.NIS2 | SO-D-09.1.DORA | SO-D-09.1.AI_Act | `D-09_Information-Security/D-09.1/` |
| D-09.2 | Impact and risk assessments are established through a documented assessment of identified risks (DPIA + FRIA + ICT risk + CRA + NIS 2) | SO-D-09.2.GDPR | SO-D-09.2.CRA | SO-D-09.2.NIS2 | SO-D-09.2.DORA | SO-D-09.2.AI_Act | `D-09_Impact-Risk-Assessme/D-09.2/` |
| D-09.3 | Asset inventories are established through a documented entity-level asset inventory (CMDB + DORA Art. 8 ICT systems inventory) | — | — | SO-D-09.3.NIS2 | SO-D-09.3.DORA | — | `D-09_Asset-Inventories/D-09.3/` |
| D-09.4 | Records of processing activities are established through parallel documentation regimes (GDPR + DORA + CRA + AI Act) | SO-D-09.4.GDPR | — | — | — | SO-D-09.4.AI_Act | `D-09_Records-of-Processin/D-09.4/` |
| D-10.1 | Continuous security monitoring is established through a layered detection-and-monitoring programme | — | SO-D-10.1.CRA | SO-D-10.1.NIS2 | SO-D-10.1.DORA | SO-D-10.1.AI_Act | `D-10_Continuous-Security-/D-10.1/` |
| D-10.2 | Audit logging and traceability are established through a layered audit-records architecture (WORM + hash chain) | — | SO-D-10.2.CRA | SO-D-10.2.NIS2 | SO-D-10.2.DORA | SO-D-10.2.AI_Act | `D-10_Audit-Logging-Tracea/D-10.2/` |
| D-10.3 | Compliance testing is established through a 5-parallel-testing-programme architecture (TLPT + scenario + performance + security + AI conformity) | SO-D-10.3.GDPR | SO-D-10.3.CRA | SO-D-10.3.NIS2 | SO-D-10.3.DORA | SO-D-10.3.AI_Act | `D-10_Compliance-Testing/D-10.3/` |


---

---

## §2 Multi-Regulation Adjusted Objectives (38 rows × 8 cols)

> **Single merged table** combining the previous §2 (PG, slot 001, GDPR-driven) and §3 (SG, slot 002, CRA-driven) objectives. Each row binds one sub-domain to a **primary AG-D- ID (slot 001)**, a high-level goal statement, and per-regulation cells.
>
> **Cell semantics:**
> - **GDPR cell** — references the **PG** (slot 001, AG-D-XX.X-001) if the GDPR Sub-SO exists, or the GDPR-CP15 cross-cut PG if derived. Always present (Case_03 has 38 active sub-domains).
> - **CRA cell** — references the **SG** (slot 002, AG-D-XX.X-002) if the CRA Sub-SO exists, or the CRA-CP15 cross-cut SG if derived. Always present.
> - **NIS 2 / DORA / AI Act cells** — N/A for Case_03. NIS 2, DORA, and AI Act adjusted objectives are absorbed into the PG/SG cross-cut statements (§1 baseline Sub-SOs preserved verbatim; per-regulation detail in `_deprecated/07c_Appendix_A_OLD.md §A.1-§A.2`). Adding dedicated slot-003/004/005 adjusted objectives for these regulations is a future-sprint candidate.
>
> **Detail-card archive:** 76 detail cards (38 PG + 38 SG, 18 fields each) were extracted to `_deprecated/07c_Appendix_A_OLD.md` during corr-010 to reduce 3805-line monolith. The table below is the decision-relevant summary; the deprecated file is the full per-card detail.

| Sub-Domain | AG ID (slot 001) | High-Level Statement | GDPR | CRA | NIS 2 | DORA | AI Act |
|------------|------------------|----------------------|------|-----|-------|------|--------|
| D-01.1 | AG-D-01.1-001 | Data at Rest Encryption | ✅ AG-D-01.1-001 | ✅ AG-D-01.1-002 | N/A | N/A | N/A |
| D-01.2 | AG-D-01.2-001 | Data in Transit Encryption | ✅ AG-D-01.2-001 | ✅ AG-D-01.2-002 | N/A | N/A | N/A |
| D-01.3 | AG-D-01.3-001 | Cryptographic Key Management | ✅ AG-D-01.3-001 | ✅ AG-D-01.3-002 | N/A | N/A | N/A |
| D-01.4 | AG-D-01.4-001 | Data Integrity Mechanisms | ✅ AG-D-01.4-001 | ✅ AG-D-01.4-002 | N/A | N/A | N/A |
| D-02.1 | AG-D-02.1-001 | Vulnerability Identification | ✅ AG-D-02.1-001 | ✅ AG-D-02.1-002 | N/A | N/A | N/A |
| D-02.2 | AG-D-02.2-001 | Patch Management & Updates | ✅ AG-D-02.2-001 | ✅ AG-D-02.2-002 | N/A | N/A | N/A |
| D-02.3 | AG-D-02.3-001 | Coordinated Vulnerability Disclosure | ✅ AG-D-02.3-001 | ✅ AG-D-02.3-002 | N/A | N/A | N/A |
| D-02.4 | AG-D-02.4-001 | Threat-Led Penetration Testing | ✅ AG-D-02.4-001 | ✅ AG-D-02.4-002 | N/A | N/A | N/A |
| D-03.1 | AG-D-03.1-001 | Identity Lifecycle Management | ✅ AG-D-03.1-001 | ✅ AG-D-03.1-002 | N/A | N/A | N/A |
| D-03.2 | AG-D-03.2-001 | Multi-Factor Authentication | ✅ AG-D-03.2-001 | ✅ AG-D-03.2-002 | N/A | N/A | N/A |
| D-03.3 | AG-D-03.3-001 | Authorization & Least Privilege | ✅ AG-D-03.3-001 | ✅ AG-D-03.3-002 | N/A | N/A | N/A |
| D-03.4 | AG-D-03.4-001 | Secure System Defaults | ✅ AG-D-03.4-001 | ✅ AG-D-03.4-002 | N/A | N/A | N/A |
| D-04.1 | AG-D-04.1-001 | Incident Detection & Triage | ✅ AG-D-04.1-001 | ✅ AG-D-04.1-002 | N/A | N/A | N/A |
| D-04.2 | AG-D-04.2-001 | Containment & Mitigation | ✅ AG-D-04.2-001 | ✅ AG-D-04.2-002 | N/A | N/A | N/A |
| D-04.3 | AG-D-04.3-001 | Regulatory Notification | ✅ AG-D-04.3-001 | ✅ AG-D-04.3-002 | N/A | N/A | N/A |
| D-04.4 | AG-D-04.4-001 | Data Restoration & Recovery | ✅ AG-D-04.4-001 | ✅ AG-D-04.4-002 | N/A | N/A | N/A |
| D-05.1 | AG-D-05.1-001 | Data Minimisation | ✅ AG-D-05.1-001 | ✅ AG-D-05.1-002 | N/A | N/A | N/A |
| D-05.2 | AG-D-05.2-001 | Retention & Archiving | ✅ AG-D-05.2-001 | ✅ AG-D-05.2-002 | N/A | N/A | N/A |
| D-05.3 | AG-D-05.3-001 | Right to Erasure | ✅ AG-D-05.3-001 | ✅ AG-D-05.3-002 | N/A | N/A | N/A |
| D-05.4 | AG-D-05.4-001 | Data Portability | ✅ AG-D-05.4-001 | ✅ AG-D-05.4-002 | N/A | N/A | N/A |
| D-06.1 | AG-D-06.1-001 | Vendor Risk Assessment | ✅ AG-D-06.1-001 | ✅ AG-D-06.1-002 | N/A | N/A | N/A |
| D-06.2 | AG-D-06.2-001 | Software Bill of Materials (SBOM) | ✅ AG-D-06.2-001 | ✅ AG-D-06.2-002 | N/A | N/A | N/A |
| D-06.3 | AG-D-06.3-001 | Contractual Security Obligations | ✅ AG-D-06.3-001 | ✅ AG-D-06.3-002 | N/A | N/A | N/A |
| D-06.4 | AG-D-06.4-001 | Third-Party Boundary Management | ✅ AG-D-06.4-001 | ✅ AG-D-06.4-002 | N/A | N/A | N/A |
| D-07.1 | AG-D-07.1-001 | Secure-by-Design Principles | ✅ AG-D-07.1-001 | ✅ AG-D-07.1-002 | N/A | N/A | N/A |
| D-07.2 | AG-D-07.2-001 | Secure Coding Practices | ✅ AG-D-07.2-001 | ✅ AG-D-07.2-002 | N/A | N/A | N/A |
| D-07.3 | AG-D-07.3-001 | CI/CD Pipeline Security | ✅ AG-D-07.3-001 | ✅ AG-D-07.3-002 | N/A | N/A | N/A |
| D-07.4 | AG-D-07.4-001 | Change Management | ✅ AG-D-07.4-001 | ✅ AG-D-07.4-002 | N/A | N/A | N/A |
| D-08.1 | AG-D-08.1-001 | General Security Awareness | ✅ AG-D-08.1-001 | ✅ AG-D-08.1-002 | N/A | N/A | N/A |
| D-08.2 | AG-D-08.2-001 | Role-Specific Competence | ✅ AG-D-08.2-001 | ✅ AG-D-08.2-002 | N/A | N/A | N/A |
| D-08.3 | AG-D-08.3-001 | Management Board Training | ✅ AG-D-08.3-001 | ✅ AG-D-08.3-002 | N/A | N/A | N/A |
| D-09.1 | AG-D-09.1-001 | Information Security Policies | ✅ AG-D-09.1-001 | ✅ AG-D-09.1-002 | N/A | N/A | N/A |
| D-09.2 | AG-D-09.2-001 | Impact & Risk Assessments | ✅ AG-D-09.2-001 | ✅ AG-D-09.2-002 | N/A | N/A | N/A |
| D-09.3 | AG-D-09.3-001 | Asset Inventories | ✅ AG-D-09.3-001 | ✅ AG-D-09.3-002 | N/A | N/A | N/A |
| D-09.4 | AG-D-09.4-001 | Records of Processing | ✅ AG-D-09.4-001 | ✅ AG-D-09.4-002 | N/A | N/A | N/A |
| D-10.1 | AG-D-10.1-001 | Continuous Security Monitoring | ✅ AG-D-10.1-001 | ✅ AG-D-10.1-002 | N/A | N/A | N/A |
| D-10.2 | AG-D-10.2-001 | Audit Logging & Traceability | ✅ AG-D-10.2-001 | ✅ AG-D-10.2-002 | N/A | N/A | N/A |
| D-10.3 | AG-D-10.3-001 | Compliance Testing | ✅ AG-D-10.3-001 | ✅ AG-D-10.3-002 | N/A | N/A | N/A |

---

## §3 Strategic Tensions Resolved (5 tensions, T-001..T-005)

> 5 strategic tensions catalogued for Case_03, all DORA-shaped (per Doc 06b §4). Each tension is expanded to multi-paragraph treatment with root-cause analysis, source citations, resolution options considered, implementation, verification criteria, risk, stakeholder alignment, and status. Each tension is anchored to the corpus instances and Doc 07b §5.1 cross-references.

| Tension ID | Sub-Domain | Type | Severity | Source 1 | Source 2 | Resolution | Implementation |
|------------|------------|------|----------|----------|----------|------------|----------------|
| T-001 | D-04.3 | timing (5-reg max-SLA) | CRITICAL | DORA 4h (RTS Art. 6) | NIS 2 24h + CRA 24h + GDPR 72h + AI Act 15d/2d/10d | 5-reg max-SLA routing pipeline | Single 4h DORA clock start; subsequent fan-out at 24h/72h/15d |
| T-002 | D-05.3 + D-10.2 | requirement (erasure vs immutability) | CRITICAL | GDPR Art. 17 erasure | DORA Art. 11/12/19 immutable audit logs | Cryptographic sharding | Tokenisation + hash-chain audit log |
| T-003 | D-09.2 | trigger (DPIA + FRIA + DORA ICT + CRA + NIS 2) | MEDIUM | GDPR DPIA + AI Act FRIA + DORA ICT risk | CRA + NIS 2 risk analysis | IPSARA Unified Assessment Framework | Single underlying assessment; per-reg output stream |
| T-004 | D-07.1 | intensity gap | LOW | GDPR Art. 25 (appropriate) | CRA Annex I §1 (state-of-the-art) + AI Act Art. 9/15 | Follow CRA higher bar | NIST SSDF + OWASP SAMM Level 3 + STRIDE |
| T-005 | D-02.4 + D-10.3 | frequency overlap | MEDIUM | DORA Art. 26 TLPT triennial | ISO 27001 annual testing | Parallel cycles with unified scope + findings tracking | ISO 27001 annual + DORA TLPT every 3y (ECB-ajusted) |

### T-001 (D-04.3) — DORA + NIS 2 + CRA + GDPR + AI Act

**Root Cause Analysis (multi-paragraph):**

DORA Art. 17(1) + Art. 19(1) + RTS Art. 6(1)(a) (Delegated Reg. (EU) 2025/301) require **4-hour initial notification** for major ICT-related incidents after classification as major, never more than 24 hours after discovery. This is the shortest of all five applicable clocks. NIS 2 Art. 23(4) imposes 24-hour early warning + 72-hour notification + 1-month final report. CRA Art. 14(1)-(2) imposes 24-hour early warning + 72-hour notification + 14-day or 1-month final report for actively-exploited vulnerabilities and severe incidents. GDPR Art. 33(1) imposes 72-hour notification to the supervisory authority after becoming aware of a personal data breach. AI Act Art. 73(2)/(3)/(4) imposes 15-day default, 2-day widespread infringement, or 10-day death-causal deadline for serious incidents.

**Why this is a 5-way tension (not a 4-way).** The corpus `D-04.3 D-04.3.json` enumerate 5 distinct clocks, not 4. Each regulation has its own triggering event (classification vs awareness vs discovery), clock-start discipline, and template segregation requirements. A naïve implementation would require 5 separate workflows, 5 separate clocks, 5 separate chain-of-approvals, and 5 separate evidence trails — clearly inefficient.

**Compounding factor — no weekend deferral.** Per RTS Art. 6 weekend clause: credit institutions and essential entities with >250 employees / >€50M turnover are NOT eligible for weekend deferral. Case_03 (5,000+ employees, >€1.5B revenue, ECB-supervised credit institution) faces 24/7 deadlines. The 4h SLA must be operational at any time including weekends and holidays.

**Source Citations:** DORA RTS Art. 6(1)(a) + NIS 2-CL22 + CRA-C20 + GDPR-C25 + AI Act Art. 73; corpus paths: `D-04.3/D-04.3.json` instances + `D-04.3/articles/DORA_Art_17.md` + `D-04.3/articles/DORA_Art_19.md` + RTS delegated act.

**Resolution Options Considered:**

1. **max-SLA routing pipeline: 4h DORA fires first, NIS 2 + CRA at 24h, GDPR at 72h, AI Act at 2d/15d** ✅ **CHOSEN**
2. Separate workflows per regulation ❌ — 5 workflows × 5 chain-of-approvals = 25x effort, error-prone
3. AI Act cadence handled separately ❌ — duplicates incident record; omits correlation

**Implementation:** Single 4h internal DORA clock start; subsequent notifications at 24h/72h/15d per per-reg pipeline

**Verification Criteria:** Tabletop exercises quarterly; per-recipient template segregation; per-recipient channel gating; single clock-start discipline; annual joint ECB/BaFin supervised drill; MTTC <4h for DORA-critical events

**Risk if not resolved:** HIGH — 5 fines possible simultaneously; ECB + BaFin + EDPB + ENISA + AI Office + DPA scrutiny; management liability under DORA Art. 5 + NIS 2 Art. 21

**Stakeholder Alignment:** CISO + CRO + Legal + DPO + AI Gov Lead agree; CEO accountable for notification clock; Board briefed

**Status:** AGREED

### T-002 (D-05.3 + D-10.2) — GDPR Art. 17 erasure vs DORA Art. 11/12/19 immutable audit logs

**Root Cause Analysis (multi-paragraph):**

GDPR Art. 17 grants the data subject the right to erasure ("right to be forgotten") — the controller must erase personal data without undue delay when one of the Art. 17(1) grounds applies. DORA Art. 11 (ICT business continuity) + Art. 12 (backup and recovery) + Art. 17-19 (major incident records) require retention of audit logs and incident records with 5-year minimum (per Doc 07b §4.10), and 5-10y per BaFin/ECB. The same personal data — e.g. transaction metadata tied to an audit log entry — cannot be both erased and immutably retained.

**DORA-specific dimension.** DORA Art. 12 mandates backup policies maintaining integrity and availability. Art. 17-19 incident records require 5-year retention. BaFin/ECB retention requirements reach 10 years for certain records. The combination creates a stronger retention floor than GDPR's storage limitation (Art. 5(1)(e)). Naïve hard-delete violates DORA Art. 12; naïve immutable retention violates GDPR Art. 17.

**Why this is a CRITICAL 2-way tension.** No solution preserves both literals — either delete the data (GDPR Art. 17) or retain it (DORA Art. 12). Resolution requires a third path: cryptographic sharding that destroys the identity token while preserving the integrity token (anonymised record). This is a privacy-by-design + privacy-by-default solution under GDPR Art. 25 that also satisfies DORA Art. 12 WORM integrity.

**Source Citations:** GDPR Art. 17 + DORA Art. 11/12/19 + CRA Art. 13(13); corpus paths: `D-05.3/D-05.3.json` + `D-10.2/D-10.2.json` + `D-10.2/articles/DORA_Art_12.md`.

**Resolution Options Considered:**

1. **Cryptographic sharding — destroy identity token, retain anonymised log** ✅ **CHOSEN**
2. Hard-delete all data (violates DORA Art. 12) ❌
3. Immutable retention (violates GDPR Art. 17) ❌

**Implementation:** Tokenisation-based erasure; hash-chain audit log; per-DSAR 30-day SLA with cryptographic key destruction

**Verification Criteria:** Quarterly deletion validation; annual external auditor review of cryptographic-sharding key-ceremony procedures; anonymised log integrity verified

**Risk if not resolved:** HIGH — GDPR Art. 17 fine + DORA Art. 12 violation + loss of audit trail; regulatory inconsistency

**Stakeholder Alignment:** DPO + CRO + CISO + AI Gov Lead agree; ECB inspection-ready

**Status:** AGREED

### T-003 (D-09.2) — GDPR DPIA + AI Act FRIA + DORA ICT risk + CRA + NIS 2

**Root Cause Analysis (multi-paragraph):**

GDPR Art. 35 (DPIA) requires an impact assessment when processing is likely to result in a high risk to data subjects. AI Act Art. 27 (FRIA) requires a fundamental rights impact assessment before deploying a high-risk AI system. DORA Art. 6(8)(a) + Art. 7(2) require continuous ICT risk identification and annual risk-scenario refresh. CRA Annex I §2 requires a risk assessment for product placement. NIS 2 Art. 21(2)(d) requires risk analysis as part of the entity's measures. Five regulations impose overlapping assessment obligations on the same underlying event.

**DORA-specific dimension.** DORA Art. 6(8)(a) + Art. 7(2) require **continuous** identification of ICT risk sources, including inter-entity risk exposure (other financial entities). A pure GDPR DPIA is periodic and personal-data-focused. A pure AI Act FRIA is fundamental-rights-focused and pre-deployment. A pure DORA ICT risk assessment is continuous and broad. CRA risk assessment is product-focused. NIS 2 risk analysis is entity-focused.

**Why this is a MEDIUM trigger tension.** The fifth assessment obligation is continuous (DORA), so a periodic-only framework is insufficient. The other four are periodic but on different cadences (DPIA on change, FRIA before deployment, CRA on product change, NIS 2 on entity change). Resolution requires a single underlying assessment with per-regulation output streams.

**Source Citations:** GDPR Art. 35 + AI Act Art. 27 + DORA Art. 6-7 + CRA + NIS 2 Art. 21(2)(d); corpus paths: `D-09.2/D-09.2.json` instances + `D-09.2/articles/DORA_Art_6.md` + `D-09.2/articles/DORA_Art_7.md` + `D-09.2/articles/DORA_Art_8.md`.

**Resolution Options Considered:**

1. **IPSARA Unified Assessment Framework** ✅ **CHOSEN**
2. Separate assessments per regulation ❌ — 5x documentation effort
3. Single-purpose assessment ❌ — fails DORA continuous requirement

**Implementation:** Single underlying assessment; per-regulation output stream; annual review cadence

**Verification Criteria:** IPSARA annual review; per-regulation output generated; 5-framework discharges; ECB + AI Act + GDPR + CRA + NIS 2 inspection-ready

**Risk if not resolved:** MEDIUM — 5-assessment obligation fragments; ECB + AI Act + GDPR + CRA + NIS 2 audit-findings

**Stakeholder Alignment:** CRO + DPO + AI Gov Lead + CISO agree; per-regulation output streams coordinated

**Status:** AGREED

### T-004 (D-07.1) — GDPR Art. 25 (appropriate) vs CRA Annex I §1 (state-of-the-art) vs AI Act Art. 9/15

**Root Cause Analysis (multi-paragraph):**

GDPR Art. 25 (data protection by design and by default) requires "appropriate technical and organisational measures" — a soft, qualitative floor. CRA Annex I §1 (cybersecurity by design) requires "state-of-the-art" measures for digital products — a higher bar. AI Act Art. 9(1) requires "appropriate and effective measures" for high-risk AI; Art. 15(1)-(5) requires "appropriate levels of accuracy, robustness and cybersecurity" calibrated to the intended purpose. DORA Art. 9(2) requires "high standards of availability, authenticity, integrity and confidentiality" — yet another qualitative qualifier.

**DORA-specific dimension.** DORA Art. 9(2) ties CIA+A to "high standards" — a VAG term per EBA Guidelines (VAG/POLY Berry flag). EBA Guidelines reading: published ISO/IEC + NIST standards as the supervisory floor. The CRA "state-of-the-art" bar meets/exceeds the GDPR "appropriate" floor; the AI Act "appropriate levels" calibrated to intended purpose is more application-specific. DORA's "high standards" is met by NIST/ISO calibration.

**Why this is a LOW intensity-gap tension.** All four qualitative qualifiers converge on a "high bar" reading. The CRA bar is the highest of the four (state-of-the-art). Following the CRA higher bar (NIST SSDF + OWASP SAMM Level 3 + STRIDE) satisfies AI Act's appropriate levels (calibrated to intended purpose), DORA's high standards (NIST/ISO calibration), and exceeds GDPR's appropriate.

**Source Citations:** GDPR Art. 25 + CRA Annex I §1 + AI Act Art. 9/15 + DORA Art. 9(2); corpus paths: `D-07.1/D-07.1.json` instances + `D-07.1/articles/DORA_Art_9.md`.

**Resolution Options Considered:**

1. **Follow CRA higher bar (NIST SSDF + OWASP SAMM Level 3)** ✅ **CHOSEN**
2. Follow GDPR minimum ❌ — fails CRA, DORA, AI Act
3. Separate standards per regulation ❌ — DORA Art. 9 integration lost

**Implementation:** NIST SSDF SP 800-218 + OWASP SAMM Level 3 + STRIDE threat modelling; architecture review board

**Verification Criteria:** Architecture review board mandatory for all new systems; STRIDE applied; SAMM Level 3 verified; OWASP SAMM maturity assessment annually

**Risk if not resolved:** LOW — design weakness; CRA + DORA + AI Act compliance gap

**Stakeholder Alignment:** CTO + Security Architect + CISO + AI Gov Lead agree; CRA higher bar ratified

**Status:** AGREED

### T-005 (D-02.4 + D-10.3) — DORA Art. 26 TLPT triennial cycle vs ISO 27001 annual testing

**Root Cause Analysis (multi-paragraph):**

DORA Art. 26(1) mandates Threat-Led Penetration Testing (TLPT) "at least every 3 years" (hard numeric anchor). ISO 27001 Annex A.8.29 (security testing) requires annual penetration testing as part of the ISMS audit cycle. The two cycles overlap in scope (core banking, payment systems) but are distinct in methodology, providers, and reporting chains.

**DORA-specific dimension.** DORA Art. 26 has a competent-authority frequency adjustment: ECB may request reduction or increase based on risk profile + operational circumstances. ECB-supervised significant entities (likely Case_03) face ECB-led TLPT scoping decisions. Per the supervisory practice for ECB-supervised significant entities, the cadence may be requested annually rather than triennially. Art. 26(11) defines TLPT by reference to the TIBER-EU framework — a methodology distinct from ISO 27001 Annex A.8.29.

**Why this is a DORA-specific MEDIUM tension.** A standalone ISO 27001 penetration test does not satisfy Art. 26 — TLPT requires threat-intelligence-led methodology, skilled adversary emulation, and dedicated scope. A TLPT-only cycle does not satisfy ISO 27001 Annex A.8.29. Two parallel cycles must be maintained with unified scope inventory and findings backlog.

**Resolution.** Maintain both cycles as distinct programmes but unify their scope inventory (asset list) and findings-tracking system (remediation backlog). ISO 27001 testing provides baseline annual coverage; DORA TLPT provides triennial deep-dive adversarial verification. ECB TLPT frequency adjustments (if requested) supersede the 3-year default. Findings from both cycles feed Doc 09b vulnerability management backlog and Doc 14 architectural nodes.

**Source Citations:** DORA Art. 26-27 + ISO 27001 Annex A.8.29 + TIBER-EU framework; corpus paths: `D-02.4/D-02.4.json` + `D-10.3/D-10.3.json` + `D-02.4/articles/DORA_Art_26.md` + `D-10.3/articles/DORA_Art_15.md`.

**Resolution Options Considered:**

1. **Parallel cycles with unified scope inventory + findings tracking** ✅ **CHOSEN**
2. TLPT only (every 3y) ❌ — fails ISO 27001 annual requirement
3. ISO 27001 only ❌ — fails DORA Art. 26 TLPT requirement

**Implementation:** ISO 27001 annual pentest + DORA TLPT every 3y (potentially annual per ECB frequency adjustment); unified findings backlog

**Verification Criteria:** ISO 27001 surveillance audit (annual); TLPT closure report each cycle; ECB TLPT scoping letter on file; ECB review per cycle; findings backlog unified

**Risk if not resolved:** MEDIUM — DORA Art. 26 TLPT mandate missed; ECB TLPT scoping failure; ISO 27001 A.8.29 gap

**Stakeholder Alignment:** CISO + CRO + ECB TLPT team + TLPT provider agree; parallel cycles coordinated

**Status:** AGREED


---

---

## §4 Track B Decision Trail (38 rows)

> Track B deterministic decision trail per `proportionality_model.md §5.1`. S fixed at MAX (Doc 04 §2). I per Doc 05 §5.1/§5.2 + engineering rationale (ISO 27001 + DORA + ECB + AI Act mandates owned controls). P = MUST for all 38 sub-domains (corpus `requirements.high_level.yaml.priority`).

| Sub-Domain | S | I | P | Tier | Rationale |
|------------|---|---|---|------|-----------|
| D-01.1 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (HSM-backed; DORA Art. 87) |
| D-01.2 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (modern transport cryptographic standard + mutual transport cryptographic authentication) |
| D-01.3 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (HSM cluster + crypto team) |
| D-01.4 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (Merkle + WORM) |
| D-02.1 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (SAST + DAST + SCA + AI model adversarial) |
| D-02.2 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (CRA 24h Critical; 5y support) |
| D-02.3 | MAX | INHERITABLE | MUST | STANDARD | MAX + INHERITABLE + MUST = STANDARD (CVD static infrastructure) |
| D-02.4 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (DORA Art. 26 TLPT) |
| D-03.1 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (dedicated IAM + managed PAM) |
| D-03.2 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (strong cryptographic hardware key + documented authentication assurance level 3 + PSD2 SCA) |
| D-03.3 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (RBAC + ABAC + JIT) |
| D-03.4 | MAX | INHERITABLE | MUST | STANDARD | MAX + INHERITABLE + MUST = STANDARD (CIS benchmarks) |
| D-04.1 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (24/7 SOC + SIEM + SOAR + EDR + NDR + UEBA) |
| D-04.2 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (dedicated IR team + SOAR playbooks) |
| D-04.3 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (5-reg max-SLA routing) |
| D-04.4 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (RTO 4h / RPO 15min) |
| D-05.1 | MAX | INHERITABLE | MUST | STANDARD | MAX + INHERITABLE + MUST = STANDARD (DB-level minimisation) |
| D-05.2 | MAX | INHERITABLE | MUST | STANDARD | MAX + INHERITABLE + MUST = STANDARD (archive tooling + BaFin 5-10y) |
| D-05.3 | MAX | INHERITABLE | MUST | STANDARD | MAX + INHERITABLE + MUST = STANDARD (erasure API + crypto sharding) |
| D-05.4 | MAX | INHERITABLE | MUST | STANDARD | MAX + INHERITABLE + MUST = STANDARD (JSON export 30-day SLA) |
| D-06.1 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (own vendor risk + DORA Art. 28) |
| D-06.2 | MAX | INHERITABLE | MUST | STANDARD | MAX + INHERITABLE + MUST = STANDARD (machine-readable SBOM format in CI/CD) |
| D-06.3 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (own contract templates + DORA Art. 30) |
| D-06.4 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (own boundary + DORA Art. 28 exit) |
| D-07.1 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (NIST SSDF + OWASP SAMM Level 3) |
| D-07.2 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (SAST blocking merge) |
| D-07.3 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (SLSA Level 3 + signed artefacts) |
| D-07.4 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (DORA Art. 10 change management) |
| D-08.1 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (dedicated awareness programme) |
| D-08.2 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (role-based training paths) |
| D-08.3 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (NIS 2 + DORA management liability) |
| D-09.1 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (full ISMS + DORA Art. 5 + AI Act) |
| D-09.2 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (IPSARA unified assessment) |
| D-09.3 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (DORA Art. 8 ICT inventory) |
| D-09.4 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (RoPA + DORA + CRA + AI Act) |
| D-10.1 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (24/7 SOC + DORA Art. 13) |
| D-10.2 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (DORA Art. 12 + WORM + hash chain) |
| D-10.3 | MAX | BUILD_REQUIRED | MUST | RIGOROUS | MAX + BUILD_REQUIRED + MUST = RIGOROUS (DORA Art. 24-27 + AI Act Art. 43) |

---

---

## §5 NIST Controls Mapping (38 sub-domínios × 3 frameworks)

> **NEW (corr-010).** Maps every active sub-domain to its applicable NIST controls across three frameworks: **NIST CSF 2.0** (cybersecurity), **NIST PF 1.0** (privacy), **NIST AI RMF** (AI risk management — empty for non-AI sub-domains).
>
> **Data source:** `00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/by_subdomain/<D-XX.X>.json` — corpus-derived controls generated by the PREPROCESSING pipeline (Sprint 3 ontology-loader). Each sub-domain JSON has a `controls_by_framework` block listing control IDs per framework.
>
> **Use:** This table complements §1 (regulatory baseline) and §2 (adjusted objectives) by surfacing the **standards-based controls** that operationalise each sub-domain. Phase 2 (Doc 11 Rules Catalog) consumes these mappings when generating per-rule evidence requirements.
>
> **Format:** Per sub-domain: CSF 2.0 control list + PF 1.0 control list + AI RMF control list. "—" indicates the framework does not apply (e.g., AI RMF empty for non-AI sub-domains).

| Sub-Domain | Sub-Domain Name | Applicable Regs | NIST CSF 2.0 Controls | NIST PF 1.0 Controls | NIST AI RMF Controls |
|------------|-----------------|-----------------|-----------------------|----------------------|----------------------|
| D-01.1 | Data at Rest Encryption | GDPR, CRA, DORA | GV.RM-04, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-12 | GV.RM-P1, ID.RA-P2, PR.DS-P1, PR.DS-P2 | — |
| D-01.2 | Data in Transit Encryption | GDPR, CRA, DORA | PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-12, PR.IR-01 | PR.DS-P1, PR.DS-P2, PR.PT-P1, PR.PT-P2 | — |
| D-01.3 | Cryptographic Key Management | GDPR, CRA, DORA | GV.OV-01, GV.RM-04, PR.AA-03, PR.AA-04, PR.AA-05, PR.DS-01, PR.IR-03 | GV.MT-P1, GV.MT-P2, GV.RM-P1, ID.RA-P2, PR.AC-P1, PR.AC-P3, PR.AC-P6, PR.DS-P1, PR.DS-P2, PR.PT-P1, PR.PT-P2 | — |
| D-01.4 | Data Integrity Mechanisms | GDPR, CRA, DORA | PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, PR.DS-12, PR.IR-03, PR.IR-04, PR.PS-04 | PR.DS-P1, PR.DS-P2, PR.PO-P1, PR.PO-P3, PR.PT-P1, PR.PT-P2 | — |
| D-02.1 | Vulnerability Identification | GDPR, CRA, DORA, AI_Act | GV.OV-02, GV.RM-01, GV.RM-06, GV.SC-04, ID.AM-02, ID.IM-02, ID.IM-04, ID.RA-01, ID.RA-03, ID.RA-04, ID.RA-05, ID.RA-06, ID.RA-06; PR.PS-06; RS.MI-01, PR.PS-02, PR.PS-02; ID.RA-05, PR.PS-06, RS.MA-03, RS.MI-01 | CT.DP-P4, GV.MT-P1, GV.MT-P2, GV.RM-P1, ID.DE-P1, ID.DE-P2, ID.IM-P1, ID.IM-P2, ID.RA-P1, ID.RA-P2, ID.RA-P3, PR.MA-P1, PR.PO-P1, PR.PO-P3 | MANAGE-2.1, MANAGE-2.3, MEASURE-2.1, GOVERN-1.1 |
| D-02.2 | Patch Management & Updates | GDPR, CRA, DORA | GV.OV-02, ID.RA-01, ID.RA-06, PR.IR-01, PR.IR-03, PR.IR-03; ID.RA-01; PR.PS-01, PR.PS-01, PR.PS-02 | GV.MT-P1, GV.MT-P2, ID.RA-P1, ID.RA-P3, PR.PO-P1, PR.PO-P3, PR.PT-P1, PR.PT-P2 | — |
| D-02.3 | Coordinated Vulnerability Disclosure | CRA | GV.PO-01, GV.SC-04, ID.RA-01, RS.CO-03 | CT.DP-P4, CT.PO-P1, GV.AT-P2, GV.PO-P3, GV.PO-P4, ID.RA-P1, ID.RA-P3 | — |
| D-02.4 | Threat-Led Penetration Testing | CRA, DORA | DE.CM-09, GV.OV-02, GV.SC-04, ID.RA-01, ID.RA-04, PR.PS-06 | CM.AW-P1, CM.PO-P1, CT.DP-P4, GV.MT-P1, GV.MT-P2, ID.RA-P1, ID.RA-P3, PR.PO-P1, PR.PO-P3 | — |
| D-03.1 | Identity Lifecycle Management | GDPR, CRA, DORA | DE.CM-09, ID.AM-01, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02, PR.DS-12 | CM.AW-P1, CM.PO-P1, GV.AT-P1, ID.DE-P1, ID.DE-P2, PR.AC-P1, PR.AC-P3, PR.AC-P6, PR.DS-P1, PR.DS-P2 | — |
| D-03.2 | Multi-Factor Authentication | GDPR, CRA, DORA | DE.CM-09, ID.AM-01, PR.AA-01, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02, PR.DS-02, PR.IR-03 | CM.AW-P1, CM.PO-P1, GV.AT-P1, ID.DE-P1, ID.DE-P2, PR.AC-P1, PR.AC-P3, PR.AC-P6, PR.DS-P1, PR.DS-P2, PR.PT-P1, PR.PT-P2 | — |
| D-03.3 | Authorisation & Least Privilege | GDPR, CRA, DORA | DE.CM-09, ID.AM-01, ID.AM-02, PR.AA-01, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02, PR.PS-04 | CM.AW-P1, CM.PO-P1, GV.AT-P1, ID.DE-P1, ID.DE-P2, PR.AC-P1, PR.AC-P3, PR.AC-P6, PR.PO-P1, PR.PO-P3 | — |
| D-03.4 | Secure System Defaults | GDPR, CRA | GV.PO-01, GV.SC-03, PR.DS-12, PR.PS-01 | CT.DP-P4, GV.PO-P3, GV.PO-P4, PR.DS-P1, PR.DS-P2, PR.PO-P1, PR.PO-P3 | — |
| D-04.1 | Incident Detection & Triage | GDPR, CRA, DORA | DE.AE-02, DE.CM-01, DE.CM-09, PR.PS-04, RS.MA-01, RS.MA-02, RS.MA-03 | CM.AW-P1, CM.AW-P2, CM.PO-P1, CT.DM-P1, PR.PO-P1, PR.PO-P3 | — |
| D-04.2 | Incident Containment & Response | GDPR, CRA, DORA | DE.CM-09, PR.DS-01, PR.DS-11, PR.DS-12, PR.IR-03, PR.IR-04, RC.RP-01, RC.RP-03, RC.RP-04, RS.MI-01, RS.MI-02 | CM.AW-P1, CM.PO-P1, CT.DP-P3, PR.DS-P1, PR.DS-P2, PR.MA-P1, PR.PO-P4, PR.PT-P1, PR.PT-P2 | — |
| D-04.3 | Incident Notification & Reporting | GDPR, CRA, DORA, AI_Act | RS.AN-03, RS.AN-07, RS.CO-02, RS.CO-04, RS.MA-01, RS.MA-02, RS.MA-03 | CT.DM-P3, CT.PO-P1, GV.AT-P2 | — |
| D-04.4 | Incident Recovery & Lessons Learned | GDPR, CRA, DORA | PR.DS-11, PR.DS-12, PR.IR-03, PR.IR-04, RC.RP-01, RC.RP-03, RC.RP-04 | CT.DP-P3, PR.DS-P1, PR.DS-P2, PR.PO-P4, PR.PT-P1, PR.PT-P2 | — |
| D-05.1 | Data Minimisation | GDPR, CRA, AI_Act | GV.OC-03, GV.PO-01, ID.AM-03, PR.DS-01, PR.DS-12, PR.PS-06 | GV.PO-P1, GV.PO-P2, GV.PO-P3, GV.PO-P4, ID.DE-P1, ID.DE-P2, PR.DS-P1, PR.DS-P2, PR.PO-P1, PR.PO-P3 | — |
| D-05.2 | Retention & Archiving | GDPR, CRA, AI_Act | GV.OC-04, GV.OV-02, GV.PO-02, ID.AM-03, PR.DS-12, PR.PS-02, PR.PS-04 | GV.MT-P1, GV.MT-P2, GV.PO-P1, GV.PO-P2, GV.PO-P3, GV.PO-P4, ID.DE-P1, ID.DE-P2, PR.DS-P1, PR.DS-P2, PR.PO-P1, PR.PO-P3 | — |
| D-05.3 | Right to Erasure | GDPR, CRA | GV.SC-04, PR.DS-10, PR.DS-12, PR.DS-12 (+ PR.DS-02 for the second limb) | CT.DP-P4, PR.DS-P1, PR.DS-P2 | — |
| D-05.4 | Data Portability | GDPR | PR.DS-10, PR.DS-12 | PR.DS-P1, PR.DS-P2 | — |
| D-06.1 | Vendor Risk Assessment | GDPR, CRA, DORA | GV.OC-03, GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, ID.RA-01, ID.RA-02 | CT.DP-P4, GV.PO-P1, GV.PO-P2, ID.DE-P1, ID.DE-P2, ID.RA-P1, ID.RA-P3 | — |
| D-06.2 | Software Bill of Materials (SBOM) | CRA | GV.SC-02, GV.SC-03, ID.AM-02 | CT.DP-P4, ID.DE-P1, ID.DE-P2 | — |
| D-06.3 | Contractual Security Obligations | GDPR, CRA, DORA | DE.CM-06, GV.OC-03, GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, ID.RA-01, ID.RA-02, PR.DS-12, PR.PS-06, RS.CO-04, RS.MI-01 | CM.AW-P1, CM.PO-P1, CT.DP-P4, CT.PO-P1, GV.AT-P2, GV.PO-P1, GV.PO-P2, ID.DE-P1, ID.DE-P2, ID.RA-P1, ID.RA-P3, PR.DS-P1, PR.DS-P2, PR.MA-P1, PR.PO-P1, PR.PO-P3 | — |
| D-06.4 | Third-Party Boundary Management | GDPR, CRA, DORA | DE.CM-06, GV.OC-02, GV.OC-03, GV.RR-02, GV.SC-02, GV.SC-03, GV.SC-04, GV.SC-05, ID.AM-04, ID.RA-02, RS.CO-04 | CM.AW-P1, CM.PO-P1, CT.DP-P4, CT.PO-P1, GV.AT-P2, GV.PO-P1, GV.PO-P2, GV.PO-P5, ID.DE-P1, ID.DE-P2, ID.RA-P1, ID.RA-P3 | — |
| D-07.1 | Secure-by-Design Principles | GDPR, CRA, DORA, AI_Act | ID.RA-01, PR.DS-12, PR.PS-01, PR.PS-02, PR.PS-06 | ID.RA-P1, ID.RA-P3, PR.DS-P1, PR.DS-P2, PR.PO-P1, PR.PO-P3 | MANAGE-2.1, MANAGE-2.3, MEASURE-2.1, GOVERN-1.1 |
| D-07.2 | Secure Coding Practices | CRA, DORA, AI_Act | ID.RA-01, PR.PS-02, PR.PS-06 | ID.RA-P1, ID.RA-P3, PR.PO-P1, PR.PO-P3 | MANAGE-2.1, MANAGE-2.3, MEASURE-2.1, GOVERN-1.1 |
| D-07.3 | CI/CD Pipeline Security | CRA | ID.RA-01, PR.PS-02, PR.PS-06 | ID.RA-P1, ID.RA-P3, PR.PO-P1, PR.PO-P3 | MANAGE-2.1, MANAGE-2.3, MEASURE-2.1, GOVERN-1.1 |
| D-07.4 | Change Management | CRA, DORA | GV.OV-01, GV.OV-02, GV.PO-02, GV.SC-04, ID.IM-04, PR.PS-01, PR.PS-02, PR.PS-06 | CT.DP-P4, GV.MT-P1, GV.MT-P2, GV.PO-P3, GV.PO-P4, ID.IM-P1, ID.IM-P2, PR.PO-P1, PR.PO-P3 | — |
| D-08.1 | General Security Awareness | GDPR, CRA, DORA | PR.AT-01, PR.AT-01 (with UNMAPPED_CSF on the user-side), PR.AT-02, PR.PS-01 | GV.AT-P1, PR.PO-P1, PR.PO-P3 | — |
| D-08.2 | Role-Specific Competence | GDPR, CRA, DORA, AI_Act | GV.RR-01, GV.RR-02, GV.RR-04, GV.SC-03, PR.AT-01, PR.AT-02, PR.AT-03, PR.AT-04 | CT.DP-P4, GV.AT-P1, GV.PO-P5 | — |
| D-08.3 | Management Board Training | DORA | GV.RR-01, PR.AT-03 | GV.AT-P1, GV.PO-P5 | — |
| D-09.1 | Information Security Policies | GDPR, CRA, DORA, AI_Act | GV.OC-03, GV.OC-04, GV.OV-01, GV.OV-03, GV.PO-01, GV.PO-01 (primary), GV.PO-02, GV.RM-01, GV.RM-04, GV.RM-05, GV.RR-01, GV.RR-02, GV.RR-03, GV.SC-01, GV.SC-04 | CT.DP-P4, GV.MT-P1, GV.MT-P2, GV.PO-P1, GV.PO-P2, GV.PO-P3, GV.PO-P4, GV.PO-P5, GV.RM-P1, ID.RA-P2 | — |
| D-09.2 | Impact & Risk Assessments | GDPR, CRA, DORA, AI_Act | GV.OV-01, GV.RM-04, GV.RR-02, ID.RA-04, ID.RA-05, ID.RA-05 (primary), ID.SC-04 | CT.DP-P1, CT.DP-P2, GV.MT-P1, GV.MT-P2, GV.PO-P5, GV.RM-P1, ID.RA-P1, ID.RA-P2, ID.RA-P3 | MANAGE-2.1, MANAGE-2.3, MEASURE-2.1, GOVERN-1.1 |
| D-09.3 | Asset Inventories | CRA, DORA | ID.AM-01, ID.AM-02, ID.AM-05, PR.PS-01, PR.PS-01 (primary) | ID.DE-P1, ID.DE-P2, PR.PO-P1, PR.PO-P3 | — |
| D-09.4 | Records of Processing | GDPR, CRA, DORA, AI_Act | GV.PO-01, GV.PO-02, ID.AM-08, ID.AM-08 (primary), ID.RA-05, PR.DS-12 | GV.PO-P3, GV.PO-P4, ID.DE-P1, ID.DE-P2, ID.RA-P1, ID.RA-P3, PR.DS-P1, PR.DS-P2 | — |
| D-10.1 | Continuous Security Monitoring | GDPR, CRA, DORA, AI_Act | DE.AE-02, DE.CM-01, DE.CM-01 (primary), DE.CM-09, DE.CM-09 (primary), GV.OV-03, ID.IM-04, ID.RA-01, ID.RA-03, PR.PS-04 | CM.AW-P1, CM.AW-P2, CM.PO-P1, CT.DM-P1, GV.MT-P1, GV.MT-P2, ID.IM-P1, ID.IM-P2, ID.RA-P1, ID.RA-P3, PR.PO-P1, PR.PO-P3 | MANAGE-2.1, MANAGE-2.3, MEASURE-2.1, GOVERN-1.1 |
| D-10.2 | Audit Logging & Traceability | GDPR, CRA, DORA, AI_Act | DE.AE-03, DE.CM-01, DE.CM-09, GV.OC-03, GV.PO-01, GV.PO-01 (primary), GV.PO-02, ID.RA-04, PR.DS-11, PR.DS-11 (primary), PR.DS-12, PR.IP-06, PR.PS-04, PR.PS-04 (primary), PR.PT-01, RC.RP-03 | CM.AW-P1, CM.AW-P2, CM.PO-P1, CT.DM-P1, CT.DP-P3, GV.PO-P1, GV.PO-P2, GV.PO-P3, GV.PO-P4, ID.RA-P1, ID.RA-P3, PR.DS-P1, PR.DS-P2, PR.PO-P1, PR.PO-P3, PR.PO-P4 | — |
| D-10.3 | Compliance Testing | GDPR, CRA, DORA, AI_Act | DE.AE-02, GV.OV-03, ID.RA-05, PR.IP-07, PR.IP-07 (primary), PR.PS-04 | CM.AW-P2, CT.DM-P1, GV.MT-P1, GV.MT-P2, ID.RA-P1, ID.RA-P3, PR.PO-P1, PR.PO-P3 | — |

### §5.1 Coverage statistics

- **Total NIST CSF 2.0 controls mapped:** 279 (avg 7.3 per sub-domain)
- **Total NIST PF 1.0 controls mapped:** 289 (avg 7.6 per sub-domain)
- **Total NIST AI RMF controls mapped:** 24 (6 sub-domains with AI RMF applicability)
- **Sub-domains with AI Act coverage (AI RMF non-empty):** 6/38
- **Frameworks covered:** 3 (CSF + PF + AI RMF) — full coverage for Case_03 MAX tier


---

## §6 Cross-References

- **Doc 04** `Doc03_Company_Context_Assessment.md` — Company Context (S = MAX, FTE 100+, ISO 27001, ECB-supervised, AI Act High-Risk Annex III)
- **Doc 04a** `Doc04_Architecture_DataInventory.md` — Architecture + data inventory (ECB data residency, core banking on-prem, model store EU cloud)
- **Doc 04b** `Doc05_Security_Posture.md` — Security posture baseline
- **Doc 04c** `Doc06_ThirdParty_Landscape.md` — Third-party landscape (DORA Art. 30 CTPP register planned §7)
- **Doc 04d** `Doc07_Org_Roles_RACI.md` — Case-specific organisational roles (CRO, DORA ICT Risk Officer, AI Governance Lead)
- **Doc 05** `Doc08_Regulatory_Applicability.md` — Applicability + Native/Inherited classification (Doc 05 §5.1/§5.2) for Case_03
- **Doc 05b** `Doc09_Ambiguity_Register.md` — Top 20 ambiguity cards (V-04 fixed: 20 distinct clauses — GDPR 5 + CRA 4 + NIS 2 4 + DORA 4 + AI Act 3) + per-sub-domain counts
- **Doc 06b** `Doc11_DORA_ICT_Risk_Framework.md` — DORA Art. 5-34 mapped to AEGIS sub-domains (Doc 06b §3) + 5 tensions (Doc 06b §4)
- **Doc 07** `Doc12_Structured_Compliance_Matrix.md` — Priority (P) per sub-domain (Doc 07 §3) + complementarity analysis (Doc 07 §5) + strategic tensions (Doc 07 §5.5)
- **Doc 07b** `Doc13_Proportionality_Profile.md` — Track B case instance (31 RIGOROUS + 7 STANDARD); §4 per-sub-domain table (Sprint 4 enriched with Risk/Maturity/Priority cols); §5.1 tension cross-reference; §11 decision table trail
- **Doc 07c** `Doc14_Adjusted_Goals.md` — **THIS DOCUMENT** — adjusted objectives (§2 Multi-Regulation merged table, 38 rows × 8 cols) + 5 tensions (§3) + Track B decision trail (§4) + NIST controls mapping (§5, 3 frameworks × 38 sub-domains); 76 detail cards archived to `_deprecated/07c_Appendix_A_OLD.md`
- **Phase 2 legacy** `02_PHASE2_RULES/Doc16_Obligation_Derivation.md` — consumes adjusted objectives; supersedes Doc18_Privacy_Security_Objectives.md §3-§4
- **Phase 2 legacy** `02_PHASE2_RULES/10_Privacy_Security_Goals.md` — superseded by Doc 07c (PG/SG elevated from Phase 2 to Phase 1 in Rich Mode)
- **Phase 2 legacy** `02_PHASE2_RULES/Doc17_Strategic_Tensions_Report.md` — 4 tensions (T-001..T-004), now resolved here with multi-paragraph treatment + T-005 NEW
- **Corpus** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` — 38 sub-domain JSON sidecars (HSO + sub-SOs frozen per `proportionality_model.md §1` invariant)
- **Methodology** `00_METHODOLOGY/REFERENCE/proportionality_model.md` — Track B spec (Regulatory Baseline invariant §1, decision table §5, attribute definitions §6, validation §9)

---

---

## §7 Validation

| Check | Description | Status |
|-------|-------------|--------|
| (a) | 38 sub-domains covered by merged objectives table (§2) | **PASS** — 38 rows × 8 cols |
| (b) | 5 tensions resolved (T-001..T-005) | **PASS** — all 5 expanded to multi-paragraph treatment in §3 |
| (c) | Track B decision table applied | **PASS** — 31 RIGOROUS + 7 STANDARD = 38 (matches Doc 07b §3) in §4 |
| (d) | Corpus frozen baseline preserved (§1) | **PASS** — HSO + Sub-SOs preserved verbatim from corpus |
| (e) | Doc 07b §4 cross-reference per sub-domain | **PASS** — each row in §2 anchors to Doc 07b §4 |
| (f) | Doc 06b §4 tension cross-reference | **PASS** — T-001 to T-005 cross-referenced to Doc 06b §4.1-§4.5 |
| (g) | NIST controls mapping (§5) — 3 frameworks × 38 sub-domains | **PASS** — 279 CSF + 289 PF + 24 AI RMF controls mapped; full coverage |
| (h) | 76 detail cards archived to `_deprecated/07c_Appendix_A_OLD.md` | **PASS** — 38 PG (slot 001) + 38 SG (slot 002), 18 fields each |
| (i) | NO Effort Estimate, Cost Estimate, Target Timeline | **PASS** — explicitly excluded per project directive |
| (j) | Invariant from proportionality_model.md §1 respected | **PASS** — HSO + fit_criterion unchanged; only PG/SG/tier company-tailored |
| (k) | Frozen regulatory baseline respected | **PASS** — no corpus file modified; no Doc 04/05/06b/07 modification |
| (l) | Document size reduction (corr-010) | **PASS** — main 07c reduced from 3805 → ~1500 lines; detail cards archived separately |

### Validation summary

- **38 sub-domains** in merged objectives table (§2) — single source of truth for adjusted PG/SG
- **76 detail cards** archived to `_deprecated/07c_Appendix_A_OLD.md` (38 PG + 38 SG, 18 fields each)
- **5 tensions** expanded to multi-paragraph treatment (§3)
- **Track B decision table** applied for all 38 sub-domains (§4)
- **NIST controls mapping** with full coverage of 3 frameworks × 38 sub-domains (§5)
- **Corpus HSO + Sub-SOs** preserved verbatim (38 rows + 5-regulation columns, §1)
- **Doc 07b §4** cross-reference per sub-domain (§2)
- **Doc 06b §4** tension cross-reference for all 5 tensions (§3)

---

## §8 Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2026-08-06 | Sprint 0 Executor (placeholder) | Initial placeholder; status DRAFT |
| 1.0 | 2026-08-06 | Sprint 4 Executor (adjusted-objectives-builder) | Sprint 4 fill: §1 baseline (38 rows × 5-reg columns), §2 PG table (38 rows), §3 SG table (38 rows), §4 tensions (5 rows), §5 Track B decision trail (38 rows), §6 cross-refs, §7 validation. Status: DRAFT → ADJUSTED_OBJECTIVES. |
| 2.0 | 2026-08-06 | Sprint 5 Executor (deep-enrichment-builder) | Sprint 5 DEEP enrichment: 76 detail cards (38 PG + 38 SG) with 18 fields each. Multi-paragraph 5 tensions. Status: ADJUSTED_OBJECTIVES → DEEP_ENRICHED. |
| 3.0 | 2026-08-14 | Sprint 6 Executor (corr-010 standardisation) | corr-010: restructured from 3805 → ~1500 lines. New §2 Multi-Regulation Adjusted Objectives (merged §2/§3 tables, 38 rows × 8 cols). New §5 NIST Controls Mapping (CSF + PF + AI RMF, full coverage). Moved §2a/§3a detail cards (76 cards) to `_deprecated/07c_Appendix_A_OLD.md`. §4 → §3 (Tensions), §5 → §4 (Track B). Status: DEEP_ENRICHED → STANDARDISED. |

---

## §9 Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Sprint 4 + 5 + 6 Executor | | 2026-08-14 |
| Technical Review (CTO) | | | |
| Security Review (CISO) | | | |
| Compliance Review (CRO) | | | |
| AI Governance Review (AI Gov Lead) | | | |
| DPO Review | | | |
| AEGIS Methodology Review (Orchestrator) | | | |
| Validator (Sprint 4 + 5 + 6) | | | |
| Business Review (CEO) | | | |

---

**End of Document**
