---
document_id: AEGIS-P3-RICH-04b-SEC
title: Security Posture Assessment — Maturity Model (Rich Mode)
phase: 1
version: 1.2
created: 2026-07-11
updated: 2026-08-07
author: Executor (Sprint 1 reconciliation copy; Phase 2 Bloco E maturity deprecation)
status: DEPRECATED_FOR_MATURITY
status_history:
  - { date: '2026-08-07', from: CORPUS_ENRICHED, to: DEPRECATED_FOR_MATURITY,
      reason: 'Maturity model moved to Phase 2 Doc 13 — resolves PHASE1_STRATEGY §7 contradiction' }
maturity_owner: 02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md
note: >
  Este documento mantém-se como INPUT qualitativo (postura observada).
  A avaliação e o modelo de maturidade foram movidos para
  02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md §4-5.
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
inactive_documented: []
inputs:
  - 04_Company_Context_Assessment.md
  - 04a_Architecture_DataInventory.md
  - 05_Regulatory_Applicability.md
outputs:
  - 04c_ThirdParty_Landscape.md
  - 04d_Org_Roles_RACI.md
  - 07_Structured_Compliance_Matrix.md
related_documents:
  - 04a_Architecture_DataInventory.md
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/
sibling_of: ../01_PHASE1_CONTEXT/04b_Security_Posture.md
reconciliation_notes:
  - "Sprint 1 (2026-08-06): Copied from 01_PHASE1_CONTEXT/04b_Security_Posture.md → Rich folder; frontmatter migrated to AEGIS-P3-RICH-* prefix; status DRAFT → RECONCILED; applicable_regs normalized to [GDPR, CRA, NIS 2, DORA, AI Act]; active_subdomains confirmed = 38. Tension T-002 (GDPR erasure vs AI Act immutability) preserved as case-specific (declared in legacy). Body unchanged."
---

> ⚠️ **DEPRECATED FOR MATURITY (2026-08-07).** A avaliação e o modelo de
> maturidade vivem agora em
> `02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md` §4-5. Este documento
> mantém-se como input qualitativo (postura observada). Ver `status_history`
> no frontmatter.

<!-- CORPUS_ENRICHED (Sprint 2, 2026-08-06): Enrichment with corpus fit_criteria + verification methods.
Replaces RECONCILED comment. Document copied from legacy 01_PHASE1_CONTEXT/04b_Security_Posture.md to Rich folder.
Changes: (a) document_id migrated to AEGIS-P3-RICH-04b-SEC; (b) status DRAFT → RECONCILED;
(c) applicable_regs normalized from [GDPR, NIS2, CRA, DORA, AI_Act] to [GDPR, CRA, NIS 2, DORA, AI Act] (canonical order);
(d) Tension T-002 preserved as legacy case-specific (NOT registered in ground-truth ontology per legacy lint baseline I-C03-02 — Sprint 2+ candidate to register in ontology per Phase 2 derivation pattern).
Sprint 2 (2026-08-06): New §2.1 Corpus-Derived Target fit_criteria section added with per-macro-domain + per-sub-domain fit_criteria + verification methods from corpus JSON sidecars; status RECONCILED → CORPUS_ENRICHED. Body content of maturity assessment preserved verbatim.
-->

---
---

# Security Posture Assessment (Maturity Model)

## 1. Assessment Methodology

OmniBank is a **MAXIMUM-complexity** credit institution with 5,000+ employees, ISO 27001 + documented third-party security attestation certified, in-house 24/7 SOC + CSIRT, 100-person security organisation, dedicated CISO/DPO/CRO/AI Governance Lead, and DORA financial entity + NIS 2 Essential Entity + CRA mobile-app Manufacturer + AI Act Annex III Provider+Deployer obligations. Current maturity reflects what exists today; target maturity reflects what the active 5-regulation SubDomains fit_criteria require (including DORA Art. 6 ICT risk management and AI Act Art. 9 risk-management). Financial-sector baseline is high (BaFin/ECB supervised, ISO 27001 + documented third-party security attestation certified), but DORA + AI Act overlays add specific maturity requirements (TLPT every 3 years, AI post-market monitoring, multi-deadline notification routing, cryptographic sharding for AI Act log-retention vs. GDPR Art. 17 erasure).

| Level | Label | Description |
|---|---|---|
| 0 | None | No controls in place |
| 1 | Ad-hoc | Informal, inconsistent, no documentation |
| 2 | Defined | Documented or consistently repeatable, but not fully measured |
| 3 | Managed | Implemented, monitored, measured, and regularly reviewed |
| 4 | Optimized | Continuously improved and substantially automated |

Evidence is drawn from `04a_Architecture_DataInventory.md`, `04_Company_Context_Assessment.md`, and `05_Regulatory_Applicability.md`. Active scope: 38 of 38 SubDomains (5 regulations applicable; no INACTIVE sub-domain for OmniBank).

## 2. Per-Domain Assessment

### D-01 Data Protection — Maturity: 4

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Encryption at rest | Strong symmetric encryption with HSM-bound CMK across all 12 production stores; CBS mainframe uses legacy database built-in encryption + SYS-22 HSM | SYS-22 HSM + STORE-01..12 in `04a §2.1`; SYS-01 CBS mainframe + STORE-01 in `04a §1.1`/`§2.1` | Card vault (STORE-06) tokenised per card-scheme security standard; CDS (STORE-04) field-level encryption for sensitive PII |
| Encryption in transit | Mutual transport cryptographic authentication over modern transport cryptographic standard across all 25 flows; IPSec for mainframe-to-cloud; SWIFT PKI for correspondent banking | FLOW-01..25 in `04a §2.2` | BaFin/ECB mandate EU-only TLS endpoints; SWIFT CSP 2024 compliance verified |
| Key management | FIPS 140-2 Level 3 HSM cluster (SYS-22: payment HSMs + general HSMs); dual-control key ceremonies; payment HSMs for PIN translation | SYS-22 in `04a §1.1` | Quarterly key ceremonies; HSM firmware SBOM per CRA Art. 13(13) |
| Data integrity | HSM-signed hash chain for audit (STORE-05); co-signature-signed model artefacts (STORE-10); standardised regulatory-reporting integrity for regulatory submissions (STORE-09) | SYS-23 + SYS-12 + SYS-03 in `04a §1.1`; STORE-05 + STORE-09 + STORE-10 in `04a §2.1` | Tamper-evident immutable WORM with cryptographic hash chain; AI Act Art. 15 cybersecurity for models |

**Target maturity**: 4
**Gap**: 0
**Notes**: D-01 achieves level 4 by combining HSM-backed keys, cryptographic integrity, and dual-control ceremonies. The CBS mainframe (SYS-01) uses mainframe cryptographic services integrated with SYS-22 HSM cluster. Relevant Regulatory Baseline files: [D-01.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.1.md), [D-01.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.2.md), [D-01.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.3.md), [D-01.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.4.md).

### D-02 Vulnerability Management — Maturity: 4

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Vulnerability scanning | Weekly managed vulnerability scanning on infrastructure; automated dependency scanner per-build on SYS-02 mobile app + SYS-03 OmniScore; static analysis; dedicated mainframe vulnerability scanning | SYS-25 in `04a §1.1`; FLOW-15 in `04a §2.2` | Critical CVEs patched within 7 days for production; 14 days for non-critical |
| Patch management | Critical CVEs patched within 7 calendar days (CRA + NIS 2 commitment); mainframe maintenance windows; firmware OTA where applicable | SYS-25 + SYS-01 in `04a §1.1` | DORA Art. 8 ICT change management; CRA Art. 13(8) 5-year support floor |
| Pen testing | Annual external (industry-accredited) + 6-monthly internal red team; DORA Art. 24 TLPT every 3 years on CBS mainframe + OmniScore AI | STORE-05 in `04a §2.1`; FLOW-04 in `04a §2.2` | TLPT includes threat-led adversarial testing per EBA Guidelines; AI-system adversarial testing per AI Act Art. 15 |
| CVD policy | Published at `/.well-known/security.txt` per CRA Art. 14; BSI/ENISA CVD hub registration; industry threat-sharing consortium member (German Banking consortium) | (paper artefact) | 24h early-warning notification channel to BSI per CRA Art. 14(1) |

**Target maturity**: 4
**Gap**: 0
**Notes**: D-02.4 TLPT per DORA Art. 24 every 3 years is a hard obligation for a credit institution; first TLPT scheduled 2026-Q4. Threat-led adversarial testing for AI Act Annex III AI systems is integrated with TLPT scope. Relevant Regulatory Baseline files: [D-02.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.1.md), [D-02.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.2.md), [D-02.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.3.md), [D-02.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.4.md).

### D-03 Access Control — Maturity: 4

| Control | Current | Evidence | Notes |
|---|---|---|---|
| IAM system | Managed identity service (EU tenant) + on-prem identity federation + mainframe access control (legacy OS); tiered RBAC across corporate + mainframe + cloud | SYS-24 + SYS-01 in `04a §1.1`; STORE-11 in `04a §2.1` | Hybrid IAM spanning mainframe, cloud, mobile — fully integrated via managed identity service federation |
| MFA | Mandatory for ALL accounts: strong cryptographic hardware keys for ~250 privileged staff; time-based one-time password fallback; PSD2 SCA for customer-facing (strong cryptographic key + biometrics + transaction signing) | SYS-24 + SYS-02 + SYS-22 in `04a §1.4` | PSD2 SCA via eIDAS-compliant certificate-based strong customer authentication |
| RBAC | Tiered: 8 user roles + 12 privileged roles + mainframe resource-class access control; HR-driven joiner-mover-leaver workflow | SYS-24 + SYS-01 mainframe access control + SYS-25 SOC roles in `04a §1.4` | Quarterly access reviews owned by DPO + CISO + CRO; mainframe review automated via mainframe access-control reports |
| Privileged access management | Managed PAM for ~250 privileged accounts; just-in-time elevated access; HSM key access dual-control | SYS-22 dual-control + SYS-24 in `04a §1.4` | Managed PAM deployment — achieves D-03.3 level 4; mainframe Enhanced Session Management |
| Default secure configs | Hardened-default baseline + ISO 27001 A.13 baseline + mainframe secure defaults (access-control defaults); CRA Annex I Part I (1) secure-by-default for SYS-02 mobile app | SYS-01 + SYS-02 + SYS-22 in `04a §1.1` | Mobile app ships in secure-default state (no debug ports, code obfuscation, certificate pinning) |

**Target maturity**: 4
**Gap**: 0
**Notes**: D-03 achieves level 4 with managed PAM deployment; mainframe access-control integration is a financial-sector differentiator. PSD2 SCA for customer-facing access control is regulator-mandated. Relevant Regulatory Baseline files: [D-03.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.1.md), [D-03.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.2.md), [D-03.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.3.md), [D-03.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.4.md).

### D-04 Incident Response — Maturity: 3

| Control | Current | Evidence | Notes |
|---|---|---|---|
| IR plan | Documented incident response plan v6.2 (April 2026); quarterly tabletop exercises; 2 annual full-scale exercises with ECB/BaFin observers | SOC v6.2 procedure docs; evidence in STORE-05 | Plan covers all 5 regulations' notification timelines (4h DORA RTS / 24h NIS 2 / 24h CRA / 72h GDPR / 15d AI Act) |
| Detection capability | Centralized audit-log management SIEM (EU region) + managed endpoint detection + managed vulnerability feed + custom ML anomaly detection + dedicated fraud telemetry; 24 SOC analysts in 4 shifts + 1 on-call | SYS-25 in `04a §1.1`; STORE-05 in `04a §2.1` | ECB-supervised; multiple regulatory notification deadlines drive runbook complexity |
| Notification process | CISO-owned 4h DORA RTS routing (per RTS Art. 6(1)(a)); 24h CSIRT routing (NIS 2 Art. 23(4)(a) + CRA Art. 14(1)); 72h DPA routing (GDPR Art. 33) via DPO; 15d AI Act routing (Art. 73(2)) via AI Governance Lead | FLOW-17 + FLOW-23 in `04a §2.2` | Tested quarterly; tabletop timings recorded in STORE-05 audit |
| Recovery procedures | BCP tested annually + semi-annual DR tests (EU sites); RTO 4h, RPO 15min for critical CBS mainframe; 99.99% uptime SLA | STORE-01 + STORE-02 + STORE-05 backups in `04a §2.1`; FLOW-22 in `04a §2.2` | BaFin-required DR testing; ECB stress tests included |

**Target maturity**: 4 (for D-04.3 multi-deadline routing + D-04.4 DR automation)
**Gap**: 1 (D-04.3 multi-deadline routing workflow integration; D-04.4 DR automation partial)
**Notes**: D-04.3 has the most complex routing logic (5 different deadlines for compound events). The integrated playbooks for compound events (e.g., AI-Act serious-incident that is also a GDPR personal-data breach + DORA major incident + CRA active-exploitation + NIS 2 significant incident) are tracked in Phase 2 strategic-tensions resolution. D-04.4 DR is at level 3 with mainframe automated (managed disaster replication) but cloud-region DR needs further automation. Relevant Regulatory Baseline files: [D-04.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.1.md), [D-04.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.2.md), [D-04.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.3.md), [D-04.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.4.md).

### D-05 Data Lifecycle — Maturity: 3

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Data minimisation | Mobile app collects minimum necessary for PSD2 SCA; managed behavioural biometric collected only with explicit consent (Art. 9); CDW uses pseudonymised data for analytics | STORE-02, STORE-04, STORE-07 in `04a §2.1`; DPO policy | BaFin retention exemption applies for AML records; CDW anonymisation pipeline for analytics |
| Retention policies | 10-year BaFin/GoBD retention for financial records; 7-year for HR/tax; AML 10-year; explicit retention matrix per data category | STORE-01, STORE-04, STORE-05, STORE-08 in `04a §2.1` | Lifetime retention for AI Act technical documentation (10 years); Crypto-shredding for credentials |
| Erasure procedures | DPO workflow with BaFin retention exemption logic; CDW anonymisation pipeline; Art. 17 GDPR handled with retention override; DSAR via dedicated portal | SYS-13 + DPO workflow in `04a §2.4` | Tested annually via DSAR tabletop; crypto-shredding for HSM-managed keys |
| Data portability | Customer data export via DSAR portal (Art. 20 GDPR); machine-readable format (JSON); 30-day SLA | SYS-02 export in `04a §2.4` | Open Banking / PSD2 also provides portability for account information |

**Target maturity**: 4 (for D-05.3 erasure-vs-retention conflict resolution)
**Gap**: 1 (D-05.3 cryptographic sharding for AI Act log retention vs. GDPR Art. 17 erasure — Phase 2 strategic-tensions resolution)
**Notes**: D-05.3 has a known conflict between GDPR Art. 17 erasure and AI Act Art. 12 technical-documentation retention. The cryptographic-sharding solution (anonymise erasure target before applying erasure) is tracked in Phase 2. D-05.4 is mature due to PSD2/Open Banking portability infrastructure. Relevant Regulatory Baseline files: [D-05.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.1.md), [D-05.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.2.md), [D-05.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.3.md), [D-05.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.4.md).

### D-06 Supply Chain — Maturity: 4

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Vendor assessment | Tiered criticality; annual formal assessment for Critical + Important vendors; DORA Art. 28 ICT third-party register; ISO 27001 + documented third-party security attestation evidence required for all data processors | `04c_ThirdParty_Landscape.md §5` (separate document) | DORA Art. 30 ICT contracts register; BaFin-supervised vendor programme |
| SBOM | Machine-readable SBOM format emission per release for SYS-02 mobile app + SYS-03 OmniScore; published per release; verified against ENISA SBOM guidance | SYS-11 build pipeline + STORE-02 in `04a §1.1`/`§2.1` | Required for CRA mobile app (CRA Art. 13(13) 10-year retention); AI Act Art. 11 technical documentation |
| Contract clauses | GDPR Art. 28 DPA template; DORA Art. 30 ICT contract template (pre-contract + exit + audit + sub-outsourcing + termination); CRA Annex I Part I (2)(h); AI Act Art. 25 provider-deployer | (paper artefact; DPA + DORA contract template library) | Multi-regulation clause bank maintained by DPO + Legal + CRO |
| Boundary management | Vendor egress reviewed; sub-processor chains tracked; pseudonymisation before logging egress; formal sub-processor change notifications | SYS-23 + DPAs in `04a §1.3` | GDPR Art. 28(2) sub-processor notification flow; DORA Art. 28 sub-outsourcing register |

**Target maturity**: 4
**Gap**: 0
**Notes**: D-06 covers both legal (DPA template library + DORA Art. 30 ICT contract template + sub-processor flow) and technical (SBOM pipeline). The DORA Art. 30 ICT contract register is maintained by CRO with annual re-assessment; critical CTPPs tracked separately. Relevant Regulatory Baseline files: [D-06.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.1.md), [D-06.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.2.md), [D-06.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.3.md), [D-06.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.4.md).

### D-07 Secure Development — Maturity: 4

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Secure-by-design | Threat model per feature; ISO 27001 A.14 baseline; CRA Annex I Part I (1) secure-by-design for SYS-02 mobile; AI Act Art. 9 risk-management system integrated for SYS-03 OmniScore | SYS-02 mobile dev + SYS-03 ML pipeline in `04a §1.1` | EU AI Act Art. 9 risk-management is a level-4 control for high-risk AI |
| Secure coding | Industry secure-coding guidelines (web + mobile); industry industrial-cybersecurity standard for industrial components; static analysis + peer review on all PRs | SYS-02 + SYS-03 + SYS-14 in `04a §1.1` | Secure-by-default coding for SYS-02 mobile app + SYS-03 OmniScore (CRA Part I (1)) |
| CI/CD pipeline security | Static + dependency + dynamic analysis + co-signature signing + managed artefact repository + machine-readable SBOM format emission per build; AI model signing per AI Act Art. 15 | SYS-11 build pipeline + STORE-02 + STORE-10 in `04a §1.1`/`§2.1` | SBOM + signed artefacts per CRA + AI Act Art. 15 cybersecurity |
| Change management | PR review + CAB + dual approval for production; mainframe change-control; AI model changes follow AI Act Art. 9 + 16 change-control procedure | SYS-11 + AI Governance Lead + Mainframe Operations | Change triggers SBOM re-emission + AI Act documentation update; AI model version control per Art. 16 |

**Target maturity**: 4
**Gap**: 0
**Notes**: D-07 achieves level 4 with full pipeline automation including AI model signing. AI Act Art. 16 change-control for high-risk AI systems (OmniScore) is a unique requirement tracked separately. Mainframe change-control is a financial-sector baseline. Relevant Regulatory Baseline files: [D-07.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.1.md), [D-07.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.2.md), [D-07.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.3.md), [D-07.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.4.md).

### D-08 Human Factors — Maturity: 4

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Security awareness | Annual formal programme for all 5,000+ staff; quarterly phishing simulations; AI literacy (AI Act Art. 4) integrated; completion tracked in LMS | (LMS records) | ISO 27001 A.7 + NIS 2 Art. 21(2)(g) + CRA Annex I Part I (8)(f) + AI Act Art. 4 |
| Role-specific training | Developers: secure coding + mobile security; SOC analysts: industry security certifications + IR + fraud; DPO: industry privacy certifications + GDPR; CRO: DORA + Basel; AI Governance Lead: AI Act bootcamp + ISO 42001; Compliance team: BaFin/ECB regulator engagement training | (LMS curriculum; certifications tracked) | EU AI Act Art. 4 (AI literacy) for staff operating AI systems; PSD2 SCA training for customer-facing |
| Board training | **D-08.3 ACTIVE for OmniBank under NIS 2 + DORA Art. 5 management liability** — quarterly cybersecurity + AI risk briefings to Management Board + Non-Exec Directors; annual external cyber-board training | (governance records; board agenda minutes) | NIS 2 Art. 20 (Management bodies' training) + DORA Art. 5 management liability for ICT risk |

**Target maturity**: 4
**Gap**: 0
**Notes**: All 3 sub-domains (D-08.1, D-08.2, D-08.3) are ACTIVE for OmniBank (NIS 2 + DORA + AI Act all apply). D-08.3 is a NIS 2 Art. 20 + DORA Art. 5 dual obligation — board is personally liable for ICT risk under DORA. AI literacy (Art. 4 AI Act) is integrated into general awareness. Board training is a dual NIS 2 + DORA obligation; quarterly briefings are recorded in board minutes. Relevant Regulatory Baseline files: [D-08.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.1.md), [D-08.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.2.md), [D-08.3 ACTIVE](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.3.md) — note: ACTIVE for OmniBank (NIS 2 + DORA-applicable).

### D-09 Governance & Documentation — Maturity: 4

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Security policies | ISO 27001 v6.2 policy set with full Annex A coverage + documented third-party security attestation scope + DORA ISMS overlay + AI-specific addendum + BaFin MaRisk compliance; approved by Management Board | (paper artefact; policy index in intranet) | Integration of 5 regulatory requirements into single ISMS; MaRisk AT 9 compliance for financial sector |
| Risk assessment | Annual ISO 27001 risk assessment + per-feature DPIA + FRIA + NIS 2 risk assessment + DORA ICT risk (Art. 5-16) + AI Act risk management (Art. 9); unified risk register maintained | (paper artefact; risk register) | Multi-regulation unified assessment; tracked in Phase 2 strategic-tensions resolution |
| Asset inventories | CMDB with 100% asset coverage; DORA Art. 8 ICT asset register; auto-discovered monthly + manually reviewed quarterly; linked to ticket system for change control | (CMDB tool of record) | D-09.3 ACTIVE for OmniBank via NIS 2 + CRA + DORA + ISO 27001 |
| RoPA | GDPR RoPA maintained; AI Act training-data lineage register; NIS 2 risk-assessment register; DORA Art. 8 ICT register; CRA Annex VII documentation; DPO + AI Lead + CRO + CISO co-own | (paper artefact; tooling) | D-09.4 highly developed for credit institution |

**Target maturity**: 4
**Gap**: 0
**Notes**: D-09 is the strongest domain for OmniBank given ISO 27001 + documented third-party security attestation + DORA + NIS 2 + AI Act governance requirements. The asset inventory (D-09.3) is a derived strong point — DORA Art. 8 ICT register is mandatory for credit institutions. MaRisk AT 9 governance is a financial-sector baseline. Relevant Regulatory Baseline files: [D-09.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.1.md), [D-09.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.2.md), [D-09.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.3.md), [D-09.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.4.md).

### D-10 Monitoring & Audit — Maturity: 4

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Continuous monitoring | Centralized audit-log management SIEM (24/7, 24 SOC analysts) + managed endpoint detection + managed vulnerability feed + custom ML anomaly detection + AI Act post-market monitoring for OmniScore + mainframe security monitoring | SYS-25 in `04a §1.1`; STORE-05 in `04a §2.1` | Includes AI Act post-market monitoring (Art. 72) overlay; DORA Art. 13 monitoring; ECB-supervised |
| Audit logging | Tamper-evident WORM with HSM-signed hash chain; 10-year retention; immutable across legal hold; mainframe audit + access-control logging + centralized audit-log correlation | SYS-23 + SYS-01 + STORE-05 in `04a §1.1`/`§2.1` | HSM-signed audit entries; chain anchored via SYS-22; DORA Art. 17 logging |
| Compliance testing | Annual ISO 27001 surveillance audit + annual documented third-party security attestation ROC + annual MaRisk audit + AI Act conformity assessment (in progress) + DORA Art. 24 TLPT every 3 years | (paper + tool artefacts) | TLPT first scheduled 2026-Q4 per DORA Art. 24; AI Act conformity assessment 2026-Q3 |

**Target maturity**: 4
**Gap**: 0
**Notes**: D-10 achieves level 4 with cryptographically HSM-signed audit chain, AI-system post-market monitoring, mainframe SMF integration, and ECB/BaFin-supervised compliance testing programme. DORA Art. 24 TLPT every 3 years is a hard obligation tracked. Relevant Regulatory Baseline files: [D-10.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.1.md), [D-10.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.2.md), [D-10.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.3.md).

## 2.1 Corpus-Derived Target fit_criteria (Sprint 2)

This sub-section adds the Volere-style **Target fit_criterion** and **Verification Method** for each macro-domain, extracted from the corpus JSON sidecars at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_Y/*.json` (`requirements.sub_requirements[].yaml.fit_criterion` + `verification_method`). All fit_criteria are MUST priority unless otherwise noted.

| Macro-domain | Sub-Domains | Sub-Reqs | Verification Method(s) | Target fit_criterion (Volere — composite) |
|---|---:|---:|---|---|
| D-01 Data Protection | 4 | 14 | TEST | Strong symmetric encryption is applied to all personal-data storage volumes; key custody is logically or physically separated from data access; the controller/processor risk-assessment artefact cites the five Art. 32(1) preamble factors and selects cipher strength ... |
| D-02 Vulnerability Management | 4 | 12 | TEST | A periodic testing programme (vulnerability scans, control-effectiveness tests, penetration tests against critical systems) operates with documented cadence scaled to the five Art. 32(1) preamble factors; a DPIA register documents review on every material change (processing-purpo... |
| D-03 Access Control | 4 | 14 | TEST | A graduated verification standard operates at the rights-exercise endpoint (no verification for low-risk requests, document verification for high-risk, strong authentication for very-high-risk) with verification requests anchored to documented risk-classification criteria; an Art... |
| D-04 Incident Response | 4 | 17 | TEST | Continuous monitoring of the controller's data-flow boundary is operated covering the five Art. 4(12) breach types via DE.CM-01 networks-monitored leg (unauthorised disclosure / exfiltration vector) + DE.CM-09 host / runtime / data leg (alteration / access / loss vector) + PR.PS-... |
| D-05 Data Lifecycle | 4 | 9 | INSPECT, TEST | A controller-side personal-data-minimisation architecture is operated under ID.AM-03 inventories of data and corresponding metadata for designated data types (data-class inventory with declared purpose, lawful basis, and envisaged erasure time per data category) + PR.DS-12 data m... |
| D-06 Supply Chain | 4 | 13 | TEST | A processor-selection discipline is operated before engagement covering each prospective processor via GV.SC-02 documented-due-diligence practice (written due-diligence questionnaire, certifications review, security-measures audit, sub-processor inventory) anchored on the EDPB Gu... |
| D-07 Secure Development | 4 | 12 | INSPECT, TEST | A documented Art. 25(1) by-design necessity assessment is maintained for each processing activity, applying the 4-factor qualitative proportionality (state of the art + cost of implementation + nature/scope/context/purposes of processing + risks of varying likelihood and severity... |
| D-08 Human Factors | 3 | 11 | TEST | A DPO-catalysed data-protection awareness programme is operated covering all personnel authorised to process personal data via PR.AT-01 broad-coverage leg (phishing, social-engineering, password-discipline, removable-media, incident-reporting reflexes as they apply to data-protec... |
| D-09 Governance & Documentation | 4 | 18 | TEST | Appropriate data-protection policies are documented and enforced under Art. 24(1) `appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner` (SR-GDPR-043) with GV.PO-01 policy-instrum... |
| D-10 Monitoring & Audit | 3 | 14 | TEST | Entity-level monitoring of personal-data processing systems is operational per Art. 32(1)(b) + Art. 32(1)(d) + Art. 32(2) + Art. 33(1) (SR-GDPR-019 + SR-GDPR-020 + SR-GDPR-021) verified by DE.CM-01 primary (Networks and network services are monitored to find potentially adverse e... |

**Detailed per-sub-domain fit_criteria:**


### D-01 Data Protection — detailed fit_criteria

| Req ID | Sub-Domain | Priority | Verification | fit_criterion (truncated) |
|---|---|---|---|---|
| 1.1.1 | D-01.1 | MUST | TEST/INSPECT (per corpus) | Strong symmetric encryption is applied to all personal-data storage volumes; key custody is logically or physically separated from data access; the controller/processor risk-assessment artefact cites the five Art. 32(1) preamble factors and selects cipher strength accordingly; verifie... |
| 1.1.2 | D-01.1 | MUST | TEST/INSPECT (per corpus) | A documented cryptography policy exists and is maintained per Art. 21(2)(h); where the entity's risk assessment determines encryption is appropriate, strong symmetric encryption is applied to NIS-scope data at rest; key custody is separated from data access; policy review cadence is d... |
| 1.1.3 | D-01.1 | MUST | TEST/INSPECT (per corpus) | State-of-the-art symmetric encryption (or harmonised-standards-conformant equivalent under CRA Art. 27) is applied to all data at rest of the product with digital elements; the Annex I (2)(e) `render unintelligible` test is met for the relevant data; key custody is functionally sepa... |
| 1.1.4 | D-01.1 | MUST | TEST/INSPECT (per corpus) | High-standards symmetric encryption (or stronger, EBA/ESMA/EIOPA RTS-conformant under DORA Art. 15 where applicable) is applied to financial-entity ICT-supported data at rest; the DORA Art. 9(4)(d) classification-driven cipher-strength overlay (per SR-DORA-003 / GV.RM-04) is documented for I... |
| 1.2.1 | D-01.2 | MUST | TEST/INSPECT (per corpus) | Modern transport cryptographic standard (or stronger) is applied to all in-transit channels carrying personal data; the five-event Art. 32(2) risk enumeration is addressed by technical measures on each event class (encryption for confidentiality, integrity verification for alteration, network segmentation for destruction/loss/acce... |
| 1.2.2 | D-01.2 | MUST | TEST/INSPECT (per corpus) | State-of-the-art in-transit cryptography (or harmonised-standards-conformant equivalent under CRA Art. 27) is applied to data in transit of the product with digital elements; the Annex I (2)(e) `render unintelligible` test is met; the Annex I (2)(j) attack-surface-limitat... |
| 1.2.3 | D-01.2 | MUST | TEST/INSPECT (per corpus) | High-standards in-transit cryptography (modern transport cryptographic standard or stronger, with cipher suites conforming to EBA/ESMA/EIOPA RTS under DORA Art. 15 where applicable) is applied across all in-transit channels of the financial entity's ICT landscape; mutual-authentication (mutual transport cryptographic authentication) architecture + zone-trust + peer-peer ... |
| 1.3.1 | D-01.3 | MUST | TEST/INSPECT (per corpus) | The cryptographic key, mapping table, or tokenisation seed protecting personal data is stored physically or logically separated from the personal data it protects; separation is governed by RBAC-distinct roles with distinct credentials under documented control (key-material custodian role ≠ data-pla... |
| 1.3.2 | D-01.3 | MUST | TEST/INSPECT (per corpus) | The product with digital elements implements functional RBAC separation such that the key-material custodian and the operational-environment custodian are distinct roles with distinct credentials under least-privilege entitlements; the Annex I (2)(e) `render unintelligible` test is met by separation... |
| 1.3.3 | D-01.3 | MUST | TEST/INSPECT (per corpus) | Cryptographic keys protecting financial-entity ICT-supported data are stored in FIPS 140-3 / Common Criteria EAL4+ certified HSMs (or RTS-conformant equivalent under DORA Art. 15 where applicable); split-knowledge ceremonies with quorum-based recovery are documented and tested (per EBA Guidelines §1... |
| 1.4.1 | D-01.4 | MUST | TEST/INSPECT (per corpus) | Personal-data storage uses integrity-checked storage with cryptographic hashes / MACs that detect tampering on reads (PR.DS-01); data-quality monitoring is in place with documented periodic-refresh cadence governing accuracy review (PR.DS-12); the Art. 16 rectification workflow is documented with re... |
| 1.4.2 | D-01.4 | MUST | TEST/INSPECT (per corpus) | All stored, transmitted, or processed data — together with commands, programs, and configuration — are protected by cryptographic hashes / MACs / signed firmware (PR.DS-01 + PR.DS-10) such that any unauthorised manipulation invalidates the integrity check on the next read; corruption events are surf... |
| 1.4.3 | D-01.4 | MUST | TEST/INSPECT (per corpus) | ICT-system-level integrity controls cover at-rest integrity (PR.DS-01 — cryptographic hashes / MACs on stored data), in-transit integrity (PR.DS-02 — signed-protocol integrity on data in motion), in-use integrity (PR.DS-10 — runtime integrity controls such as signed firmware, control-flow integrity,... |
| 1.4.4 | D-01.4 | MUST | TEST/INSPECT (per corpus) | The high-risk AI system implements resilience mechanisms for errors, faults, and inconsistencies that occur within the system or its environment (PR.IR-03 — failover, redundant inference paths, graceful degradation); capacity is sized for the resilience target, not just steady-state workload (PR.IR-... |

### D-02 Vulnerability Management — detailed fit_criteria

| Req ID | Sub-Domain | Priority | Verification | fit_criterion (truncated) |
|---|---|---|---|---|
| 2.1.1 | D-02.1 | MUST | TEST/INSPECT (per corpus) | A periodic testing programme (vulnerability scans, control-effectiveness tests, penetration tests against critical systems) operates with documented cadence scaled to the five Art. 32(1) preamble factors; a DPIA register documents review on every material change (processing-purpose change under Art.... |
| 2.1.2 | D-02.1 | MUST | TEST/INSPECT (per corpus) | A documented CVD policy exists and is maintained under Art. 21(2)(e); vulnerability signals from internal scanning, vendor advisories, threat-intelligence feeds and coordinated-disclosure submissions are ingested, validated against the entity's asset population, and recorded with severity, scope and... |
| 2.1.3 | D-02.1 | MUST | TEST/INSPECT (per corpus) | The release-engineering pipeline closes out identified vulnerabilities before market placement under the R2 `constructive knowledge` baseline (vendor advisories + ISACs + CERT-EU alerts + peer-manufacturer channels joined by the manufacturer); a vulnerability register and a machine-readable SBOM cov... |
| 2.1.4 | D-02.1 | MUST | TEST/INSPECT (per corpus) | A continuous ICT-risk-identification programme operates with documented cadence (vulnerability scanning, CVE-feed ingestion, authenticated vulnerability validation, threat-intelligence feeds weighted by the OJ `in particular the risk exposure to and from other financial entities` qualifier under Art... |
| 2.1.5 | D-02.1 | MUST | TEST/INSPECT (per corpus) | A risk-management system document is established, implemented, documented, and maintained for each high-risk AI system across its lifecycle with stakeholder-agreed objectives (GV.RM-01) and a standardised risk-calculation method (GV.RM-06); the Art. 9(2) 4-step closed-list cycle operates continuousl... |
| 2.2.1 | D-02.2 | MUST | TEST/INSPECT (per corpus) | Remediation action commences immediately on the R2 `constructive knowledge` awareness baseline (vendor advisories + ISACs + CERT-EU alerts + peer-manufacturer channels joined) with a documented timeline from awareness to user-dissemination; technical-feasibility carve-out for non-separation of secur... |
| 2.2.2 | D-02.2 | MUST | TEST/INSPECT (per corpus) | A documented patch-and-update policy exists, is approved by management, and specifies scope (full asset estate), severity-classification taxonomy, SLA-bound deployment windows per severity tier, exception-handling procedures for compensating controls during deferred-patch windows, rollback runbooks ... |
| 2.3.1 | D-02.3 | MUST | TEST/INSPECT (per corpus) | A documented CVD policy is published on the manufacturer's external-facing surface and enforced operationally (intake-channel evidence + triage-log records + post-disclosure verification artefacts under SR-CRA-019 R3 reading); a publicly identifiable contact address is machine-discoverable via secur... |
| 2.3.2 | D-02.3 | MUST | TEST/INSPECT (per corpus) | A coordinated vulnerability handling and disclosure process is integrated into the system acquisition, development, and maintenance lifecycle under Art. 21(2)(e); vulnerability signals from internal scanning, vendor advisories, threat-intelligence feeds and coordinated-disclosure submissions are ing... |
| 2.4.1 | D-02.4 | MUST | TEST/INSPECT (per corpus) | An SDLC-integrated testing programme (static analysis + dynamic analysis + fuzzing + integration testing + penetration testing + threat-modelling reviews per SR-CRA-022 PR.PS-06) operates on a continuing basis across the support period under Art. 13(8); the testing programme produces documented test... |
| 2.4.2 | D-02.4 | MUST | TEST/INSPECT (per corpus) | A comprehensive testing programme covers all 12 OJ-named testing modalities per SR-DORA-008 OJ-literal enumeration (vulnerability assessments + scans + open source analyses + network security assessments + gap analyses + physical security reviews + questionnaires + scanning software solutions + sour... |
| 2.4.3 | D-02.4 | MUST | TEST/INSPECT (per corpus) | Art. 9(6) consistency-for-intended-purpose testing of the AI-system's risk-management-measure effectiveness operates throughout the lifecycle against the Art. 9(2) 4-step risk-identification cycle outputs (ID.RA-01 + ID.RA-04 substrate), with documented test records covering accuracy + robustness + ... |

### D-03 Access Control — detailed fit_criteria

| Req ID | Sub-Domain | Priority | Verification | fit_criterion (truncated) |
|---|---|---|---|---|
| 3.1.1 | D-03.1 | MUST | TEST/INSPECT (per corpus) | A graduated verification standard operates at the rights-exercise endpoint (no verification for low-risk requests, document verification for high-risk, strong authentication for very-high-risk) with verification requests anchored to documented risk-classification criteria; an Art. 5(1)(c) minimisati... |
| 3.1.2 | D-03.1 | MUST | TEST/INSPECT (per corpus) | A joiner-mover-leaver (JML) register operates for the workforce with documented induction-provisioning tickets, role-transition review tickets, and separation-revocation tickets, each linked to the underlying personnel-record event; access-control policy and asset-management artefacts reference the ... |
| 3.1.3 | D-03.1 | MUST | TEST/INSPECT (per corpus) | A product-side identity-management framework is maintained in verifiable manner throughout the operational lifetime, covering human users, service identities, and integrated-component identities; type/batch/serial unique-identification markings back the SBOM-correlated identity register (ID.AM-01 ha... |
| 3.1.4 | D-03.1 | MUST | TEST/INSPECT (per corpus) | An identity provider operates with assertion-conveyance integrity (signed federated-identity tokens, mutual transport authentication, PKI chain-of-trust) for staff and service-to-service identities at the financial-entity boundary; an authenticator-inventory register with AAL mappings (documented authentication assurance levels ... |
| 3.2.1 | D-03.2 | MUST | TEST/INSPECT (per corpus) | A chain-of-authority pattern operates (controller → processor → authorised persons, with documented instructions binding each link) and a verification pattern operates (data-subject → verification-on-reasonable-doubt → proportionate additional information); Art. 28(3)(b) processor-contract confident... |
| 3.2.2 | D-03.2 | MUST | TEST/INSPECT (per corpus) | An authentication-mechanism choice (MFA or continuous-authentication) is documented with risk-tier mapping anchored to Art. 21(1) factors (state of the art, costs of implementation, exposure, size, risk) and a documented `where appropriate` justification per authentication surface; ENISA 2022 baseli... |
| 3.2.3 | D-03.2 | MUST | TEST/INSPECT (per corpus) | A product-side authentication-mechanism choice operates, anchored to a documented risk assessment for the product with digital elements; the OJ Annex I Part I (2)(d) text does not specify the authentication mechanism, so the SR preserves the OJ-literal language without naming MFA; the mechanism sele... |
| 3.2.4 | D-03.2 | MUST | TEST/INSPECT (per corpus) | An authenticator-inventory register with AAL mappings aligned with documented authentication assurance levels (per the EBA Guidelines §145–§148 dominant supervisory expectation) is maintained for financial-entity staff, service identities, and machine identities; the strong-authentication architecture includes strong cryptographic hardware keys... |
| 3.3.1 | D-03.3 | MUST | TEST/INSPECT (per corpus) | A documented-instructions register records, for each processing operation, the controller-issued instruction, the processor-contract Art. 28(3)(a)/(b) clause that anchors it, and the operational instructions issued under it; an Art. 28(3)(b) confidentiality-undertaking register binds each authorised... |
| 3.3.2 | D-03.3 | MUST | TEST/INSPECT (per corpus) | A model-agnostic access-control policy (the OJ does not impose RBAC, ABAC, MAC or DAC — the policy can be implemented under any model that satisfies least-privilege; the T3-vs-text gap on `RBAC + need-to-know + least privilege` vocabulary not present in the OJ is preserved as model-agnostic) is esta... |
| 3.3.3 | D-03.3 | MUST | TEST/INSPECT (per corpus) | A product-side authenticated-and-authorised boundary operates with PR.AA-05 + PR.AA-06 least-privilege entitlement baseline + boundary-enforcement on physical and logical assets; a reporting-and-monitoring substrate under PR.PS-04 + DE.CM-09 captures attempted and successful unauthorised access and ... |
| 3.3.4 | D-03.3 | MUST | TEST/INSPECT (per corpus) | A financial-entity-side ICT-asset access policy operates with the literal `only` qualifier enforced on every access grant — no access may be granted that is not tied to a documented legitimate and approved function; an entitlement inventory + access-review records + separation-of-duties attestation ... |
| 3.4.1 | D-03.4 | MUST | TEST/INSPECT (per corpus) | A by-default configuration operates at the processing-system level with the four Art. 25(2) dimensions minimised independently and AND-coordinated — amount of personal data collected limited to what is necessary for the specific purpose (no over-collection); extent of processing limited to operation... |
| 3.4.2 | D-03.4 | MUST | TEST/INSPECT (per corpus) | A product-centric secure-by-default configuration operates with PR.PS-01 configuration-management baseline applied at first power-up to every unit leaving the manufacturing pipeline (R1 features-enabled-on-default — security features including authentication, access control, audit logging, network s... |

### D-04 Incident Response — detailed fit_criteria

| Req ID | Sub-Domain | Priority | Verification | fit_criterion (truncated) |
|---|---|---|---|---|
| 4.1.1 | D-04.1 | MUST | TEST/INSPECT (per corpus) | Continuous monitoring of the controller's data-flow boundary is operated covering the five Art. 4(12) breach types via DE.CM-01 networks-monitored leg (unauthorised disclosure / exfiltration vector) + DE.CM-09 host / runtime / data leg (alteration / access / loss vector) + PR.PS-04 log-records-gener... |
| 4.1.2 | D-04.1 | MUST | TEST/INSPECT (per corpus) | An entity-wide monitoring capability is operated covering cybersecurity + operational + physical-environment hazards via DE.CM-01 networks-monitored leg (entity-level network telemetry, flow analytics, north-south and east-west monitoring) + DE.CM-09 host / runtime / data leg (endpoint telemetry, pr... |
| 4.1.3 | D-04.1 | MUST | TEST/INSPECT (per corpus) | An intra-product recording capability is maintained on a continuing basis throughout the support period under Art. 13(8), capturing state changes relevant to security (access to or modification of data, services, or functions) via DE.CM-09 computing-hardware-monitored leg + PR.PS-04 software-logs-re... |
| 4.1.4 | D-04.1 | MUST | TEST/INSPECT (per corpus) | A multi-layer detection architecture is operated on the financial-entity ICT infrastructure with DE.CM-01 networks-monitored leg + DE.CM-09 computing-hardware-monitored leg (SPOF identification substrate) + DE.AE-02 adverse-event analysis leg for threshold-driven escalation; the architecture defines... |
| 4.2.1 | D-04.2 | MUST | TEST/INSPECT (per corpus) | A personal-data post-breach TOMs catalogue is maintained covering containment, mitigation and remediation measures, with the measures selected per the `where appropriate` Art. 33(3)(d) qualifier and depth scaled to data-category risk (Art. 9 special categories, financial data, health data trigger de... |
| 4.2.2 | D-04.2 | MUST | TEST/INSPECT (per corpus) | The entity-level response plan documents the `contain` action as one of the six Art. 6(8) incident-handling actions (prevent, detect, analyse, contain, respond, recover) with explicit isolation procedures, system-segregation runbooks, blast-radius limitation protocols, and stakeholder-coordination s... |
| 4.2.3 | D-04.2 | MUST | TEST/INSPECT (per corpus) | A product-design framework is maintained combining DoS resilience (Annex I Part I (2)(h)) + cross-product impact minimisation (Annex I Part I (2)(i)) + exploitation-mitigation mechanisms (Annex I Part I (2)(k)) via PR.IR-04 adequate-resource-capacity leg (DoS resilience) + PR.IR-03 network-resources... |
| 4.2.4 | D-04.2 | MUST | TEST/INSPECT (per corpus) | A comprehensive ICT business continuity policy is established and implemented as an integral part of the overall business continuity policy of the financial entity; the BC arrangements are operationalised through a 4-way AND of artefacts per Art. 11(2) — response and recovery plans (RC.RP-01 recover... |
| 4.3.1 | D-04.3 | MUST | TEST/INSPECT (per corpus) | A DPA-notification pipeline is operated with documented breach-classification discipline (controller designates whether breach is `unlikely to result in a risk`, `may result in a risk`, or `likely to result in a high risk` per EDPB Guidelines 9/2022 §3.5), 72h clock-start anchored at the 4.1 GDPR le... |
| 4.3.2 | D-04.3 | MUST | TEST/INSPECT (per corpus) | A CSIRT-notification pipeline is operated with 3-tier temporal discipline: 24h early warning clock-started from 4.1 NIS 2 leg's awareness event (Art. 23(4)(a) — `without undue delay and in any event within 24 hours`), 72h incident notification with severity/impact/IoC content (Art. 23(4)(b) — `in an... |
| 4.3.3 | D-04.3 | MUST | TEST/INSPECT (per corpus) | An AEV-notification pipeline is operated with dual-pathway discipline (AEV 24h/72h/14d per Art. 14(1); SI 24h/72h/1m per Art. 14(3)/(4)) — the manufacturer designates which Art. 14 leg applies per the AEV-vs-SI classification test; the 24h early-warning tier for AEV fires upon manufacturer awareness... |
| 4.3.4 | D-04.3 | MUST | TEST/INSPECT (per corpus) | A DORA CA-notification pipeline is operated with parallel CA + client tracks: the CA notification (Art. 19(1)) fires per the EBA/ESMA/EIOPA RTS under Art. 18(3) (Implementing Regulation (EU) 2024/2956 pending 4h preliminary-classification tier; substantive thresholds + content template per RTS when ... |
| 4.3.5 | D-04.3 | MUST | TEST/INSPECT (per corpus) | An MSA-notification pipeline is operated with 4-trigger × 4-timeline matrix discipline: the default 15d timeline fires upon provider awareness (per Art. 73(1)/(4) — `15 days after the date on which the provider becomes aware`); the 10d timeline fires when the serious incident results in death (per A... |
| 4.4.1 | D-04.4 | MUST | TEST/INSPECT (per corpus) | A tested-recovery-exercise capability is operated with documented per-processing-activity RTO/RPO targets under PR.IR-04 adequate-resource-capacity substrate (resource headroom to absorb incident and recover availability within the documented RTO) + PR.DS-11 backup-discipline substrate (backups crea... |
| 4.4.2 | D-04.4 | MUST | TEST/INSPECT (per corpus) | An entity-level BC framework is maintained with the four-pillar BC + backup + DR + CM triad as the operational vehicle; a tested BC plan is produced documenting scenarios (operational + physical-environment + cyber hazards per Recital 56 all-hazards); backup records demonstrate PR.DS-11 backup creat... |
| 4.4.3 | D-04.4 | MUST | TEST/INSPECT (per corpus) | An intra-product resilience architecture is engineered pre-incident so that essential and basic functions survive an attack (Annex I Part I (2)(h) `also after an incident`) — the resilience mechanism is in place before the incident, not bolted on after; an exploitation-mitigation mechanism operates ... |
| 4.4.4 | D-04.4 | MUST | TEST/INSPECT (per corpus) | A comprehensive ICT BC framework is operated at the financial-entity ICT-infrastructure layer with the DORA `dedicated, appropriate and documented` 3-way AND + `arrangements + plans + procedures + mechanisms` 4-way AND + Art. 11(3) independent internal audit on non-microenterprises as the audit-veri... |

### D-05 Data Lifecycle — detailed fit_criteria

| Req ID | Sub-Domain | Priority | Verification | fit_criterion (truncated) |
|---|---|---|---|---|
| 5.1.1 | D-05.1 | MUST | TEST/INSPECT (per corpus) | A controller-side personal-data-minimisation architecture is operated under ID.AM-03 inventories of data and corresponding metadata for designated data types (data-class inventory with declared purpose, lawful basis, and envisaged erasure time per data category) + PR.DS-12 data managed consistent wi... |
| 5.1.2 | D-05.1 | MUST | TEST/INSPECT (per corpus) | A manufacturer-side product-data minimisation architecture is operated under ID.AM-03 inventories of data and corresponding metadata for designated data types (data-class inventory per product variant with intended-purpose tag) + PR.DS-12 data managed consistent with the manufacturer's risk strategy... |
| 5.1.3 | D-05.1 | MUST | TEST/INSPECT (per corpus) | A provider-side training-pipeline data-governance architecture is operated under ID.AM-03 datasets and corresponding metadata inventory (data sources through preparation operations to deployed model, with bias-detection (f) and bias-detection/prevention/mitigation (g) records) + PR.DS-12 data manage... |
| 5.2.1 | D-05.2 | MUST | TEST/INSPECT (per corpus) | A controller-side personal-data-retention-ceiling architecture is operated under ID.AM-03 inventories of data and corresponding metadata for designated data types (every personal-data category appears in an inventory tagged with declared purpose, lawful basis, and envisaged erasure time so that peri... |
| 5.2.2 | D-05.2 | MUST | TEST/INSPECT (per corpus) | A manufacturer-side update-availability-tail architecture is operated under PR.PS-02 software maintained, replaced, and removed commensurate with risk (the artefact-availability leg — signed packages, version archives, integrity-protected catalogues, rather than the active-patching leg) + GV.OV-02 o... |
| 5.2.3 | D-05.2 | MUST | TEST/INSPECT (per corpus) | A provider-side high-risk AI log-retention architecture is operated under PR.PS-04 log-records-generated and retained (the log-generation substrate that the 6-month retention floor requires — without continuous log generation per Art. 12(1) `over the lifetime` VAG aligned with the product-lifecycle ... |
| 5.3.1 | D-05.3 | MUST | TEST/INSPECT (per corpus) | A controller-side erasure architecture is operated under PR.DS-10 in-use key-custody discipline (the runtime-protection prerequisite that erasure must extend through — active replicas, query caches, processing pipelines) + PR.DS-12 documented deletion procedure keyed to the Art. 17 trigger condition... |
| 5.3.2 | D-05.3 | MUST | TEST/INSPECT (per corpus) | A manufacturer-side user-facing removal affordance is exposed through the product UI (per SR-CRA-048 VAG+COORD-S2 R1 — both secure AND easy via a discoverable user-interface affordance; a deletion mechanism that is easy but not secure (plain-delete of pointers without overwriting storage) fails, one... |
| 5.4.1 | D-05.4 | MUST | TEST/INSPECT (per corpus) | A controller-side Art. 20 portability export endpoint is operated under PR.DS-10 runtime integrity posture (the export must reflect current processing truth under controlled exposure rather than stale snapshot drift — partial views derived from the same in-use data set are properly handled) + PR.DS-... |

### D-06 Supply Chain — detailed fit_criteria

| Req ID | Sub-Domain | Priority | Verification | fit_criterion (truncated) |
|---|---|---|---|---|
| 6.1.1 | D-06.1 | MUST | TEST/INSPECT (per corpus) | A processor-selection discipline is operated before engagement covering each prospective processor via GV.SC-02 documented-due-diligence practice (written due-diligence questionnaire, certifications review, security-measures audit, sub-processor inventory) anchored on the EDPB Guidelines 07/2020 4-f... |
| 6.1.2 | D-06.1 | MUST | TEST/INSPECT (per corpus) | A direct-supplier-risk-management discipline is operated covering each in-scope direct supplier via GV.SC-02 supplier register and prioritisation methodology (with R1 Tier-1 contractual as the minimum `direct` scope + R2 technical-integration + R3 operationally-dependent per Recital 56 risk-manageme... |
| 6.1.3 | D-06.1 | MUST | TEST/INSPECT (per corpus) | A manufacturer-side third-party-component due-diligence discipline is operated via GV.SC-01 documented programme-governance layer (cybersecurity supply chain risk management programme, strategy, objectives, policies, and processes established and agreed by organisational stakeholders, covering comme... |
| 6.1.4 | D-06.1 | MUST | TEST/INSPECT (per corpus) | A financial-entity ICT-third-party-risk-management discipline is operated via GV.SC-02 prioritisation and assessment engine stratified by the Art. 28(1)(i) four-factor AND proportionality (nature, scale, complexity, importance — all four factors informing risk assessment cumulatively per COORD-S2 R1... |
| 6.2.1 | D-06.2 | MUST | TEST/INSPECT (per corpus) | A manufacturer-side three-anchored SBOM architecture is operated via ID.AM-02 software-inventory substrate (the SBOM is the most specific operational expression of the software-inventory principle in the product-side cybersecurity domain, with the machine-readable format qualifier supplying the quer... |
| 6.3.1 | D-06.3 | MUST | TEST/INSPECT (per corpus) | A controller-processor DPA matrix is maintained covering each in-scope processor via Art. 28(3)(a)–(h) 8 closed-list clauses — (a) documented instructions + (b) confidentiality + (c) Art. 32 measures + (d) sub-processor conditions + (e) data-subject-rights assistance + (f) Art. 33/34 incident-assist... |
| 6.3.2 | D-06.3 | MUST | TEST/INSPECT (per corpus) | A direct-supplier contractual-security matrix is maintained covering each in-scope direct supplier via Art. 21(2)(d) `direct` scope-limiter with R1 Tier-1 contractual as minimum + R2 technically integrated + R3 operationally dependent per Recital 56 risk-management-precaution principle; security-rel... |
| 6.3.3 | D-06.3 | MUST | TEST/INSPECT (per corpus) | An economic-operator compliance matrix is maintained per importer/distributor/modifier with documented pre-market verification records (Art. 19(2) conformity-assessment verification + technical-documentation check + CE marking + manufacturer-identification verification) and due-care records (Art. 20... |
| 6.3.4 | D-06.3 | MUST | TEST/INSPECT (per corpus) | A financial-entity ICT-contract matrix is maintained for each ICT third-party service-provider relationship, with Art. 30(1) clear written allocation of rights and obligations and the Art. 30(2)(a)–(i) 9-element closed-list minimum clauses present in each contract: (a) clear description of functions... |
| 6.4.1 | D-06.4 | MUST | TEST/INSPECT (per corpus) | An Art. 27 written-Union-representative discipline is operated per non-EU controller/processor falling under Art. 3(2) with no Art. 27(2) exception; each designated representative maintains a written mandate, a Union address, an establishment-on-Union-territory-of-business record, a designated data-... |
| 6.4.2 | D-06.4 | MUST | TEST/INSPECT (per corpus) | A two-track NIS 2 boundary matrix is maintained with explicit separation of (Track-1) cross-MS routing and (Track-2) direct-supplier-scope register: Track-1 cross-MS routing covers each significant incident affecting 2+ Member States via SPOC designation per Art. 23(6)/(8), CSIRT-and-competent-autho... |
| 6.4.3 | D-06.4 | MUST | TEST/INSPECT (per corpus) | A CRA economic-operator boundary matrix is maintained per non-EU manufacturer / importer / distributor / substantial-modifier with explicit boundary-mechanism separation: Art. 18 authorised representative mandate is documented per non-EU manufacturer with written mandate text, AR establishment-on-Un... |
| 6.4.4 | D-06.4 | MUST | TEST/INSPECT (per corpus) | A CIF audit-rights framework is operated per CIF-supporting ICT third-party service-provider relationship covering (i) financial-entity access / inspection / audit right exercised directly or through an appointed third party, (ii) competent-authority access / inspection / audit right, (iii) on-site ... |

### D-07 Secure Development — detailed fit_criteria

| Req ID | Sub-Domain | Priority | Verification | fit_criterion (truncated) |
|---|---|---|---|---|
| 7.1.1 | D-07.1 | MUST | TEST/INSPECT (per corpus) | A documented Art. 25(1) by-design necessity assessment is maintained for each processing activity, applying the 4-factor qualitative proportionality (state of the art + cost of implementation + nature/scope/context/purposes of processing + risks of varying likelihood and severity); the by-design dec... |
| 7.1.2 | D-07.1 | MUST | TEST/INSPECT (per corpus) | A documented 3-phase NIS 2 lifecycle (acquisition / development / maintenance) is maintained with: (1) **acquisition phase** — supplier-SDLC assessment per Art. 21(3) sentence 1 supplier-secure-development-procedures three-prong (SR-NIS2-026), with supplier-by-design evidence records retained; (2) *... |
| 7.1.3 | D-07.1 | MUST | TEST/INSPECT (per corpus) | The product by-design discipline conforms to Annex I Part I essential cybersecurity requirements across the 11 sub-points (a)–(k) including attack-surface limitation (2)(j) + exploitation mitigation (2)(k) + automatic security updates (2)(c) + integrity protection (2)(f) + data-minimisation (2)(g) +... |
| 7.1.4 | D-07.1 | MUST | TEST/INSPECT (per corpus) | A documented Art. 9(4)(b) network-and-infrastructure-management structure is maintained using appropriate techniques, methods and protocols; documented Art. 9(4)(f) patch-and-update policies are maintained appropriate and comprehensive per the risk profile; the secure-by-design dimension is operatio... |
| 7.1.5 | D-07.1 | MUST | TEST/INSPECT (per corpus) | A documented Art. 15(1) accuracy+robustness+cybersecurity baseline is maintained with lifecycle consistency (`perform consistently in those respects throughout their lifecycle`); the baseline is calibrated to `appropriate level` per the intended purpose + conditions of use; an Art. 17(1) Quality Man... |
| 7.2.1 | D-07.2 | MUST | TEST/INSPECT (per corpus) | A documented attack-surface-limitation discipline is maintained per Annex I Part I (2)(j) — minimum-necessary external interfaces (default-closed port suppression, surface-area-baselining), minimum-necessary attack surfaces, minimum-necessary exploitable paths; configuration-management practices are... |
| 7.2.2 | D-07.2 | MUST | TEST/INSPECT (per corpus) | A documented Art. 9(4)(e) change-management policy is maintained covering all change targets (software / hardware / firmware components / systems / security parameters) with the 6-step process (recorded / tested / assessed / approved / implemented / verified in a controlled manner) based on a risk a... |
| 7.2.3 | D-07.2 | MUST | TEST/INSPECT (per corpus) | A documented Art. 15(4) attack-defence baseline is maintained for the 6 AI/ML-specific attack categories: (1) **data poisoning** — defence against manipulation of the training data set, including input-validation + data-provenance checks + training-data sanitisation + anomaly-detection on training-s... |
| 7.3.1 | D-07.3 | MUST | TEST/INSPECT (per corpus) | For 100% of in-scope maintenance releases, the pipeline record links the release identifier to a vulnerability register entry or scheduled maintenance item, risk assessment, approval actor, build or package identifier, deployment timestamp, post-deployment verification result, rollback decision, and... |
| 7.3.2 | D-07.3 | MUST | TEST/INSPECT (per corpus) | For 100% of security updates, the update-delivery record contains artefact identifier, signature or equivalent integrity proof, distribution-channel identifier, advisory-message reference, user-action metadata, publication timestamp, support-period applicability, and technical-documentation retentio... |
| 7.4.1 | D-07.4 | MUST | TEST/INSPECT (per corpus) | For 100% of product changes, the change record contains product/version identifier, change classification, substantial-modification decision, conformity-impact assessment, affected technical-documentation reference, responsible role, approval decision, corrective-action link where applicable, and re... |
| 7.4.2 | D-07.4 | MUST | TEST/INSPECT (per corpus) | For 100% of in-scope ICT changes, the change ticket contains requester, affected asset or parameter, risk assessment, test evidence, approver, implementation evidence, verification result, emergency-change flag if applicable, segregation-of-duty check, rollback decision, and immutable audit timestam... |

### D-08 Human Factors — detailed fit_criteria

| Req ID | Sub-Domain | Priority | Verification | fit_criterion (truncated) |
|---|---|---|---|---|
| 8.1.1 | D-08.1 | MUST | TEST/INSPECT (per corpus) | A DPO-catalysed data-protection awareness programme is operated covering all personnel authorised to process personal data via PR.AT-01 broad-coverage leg (phishing, social-engineering, password-discipline, removable-media, incident-reporting reflexes as they apply to data-protection obligations) on... |
| 8.1.2 | D-08.1 | MUST | TEST/INSPECT (per corpus) | An entity-wide basic-hygiene programme is operated covering all users of network and information systems with access to entity systems and services via the human-side hygiene substrate PR.AT-01 (phishing awareness, password discipline, social-engineering recognition, removable-media hygiene, discipl... |
| 8.1.3 | D-08.1 | MUST | TEST/INSPECT (per corpus) | The product with digital elements is accompanied by detailed secure-use instructions under Annex II §8(a) initial-commissioning + lifetime measures, §8(b) how changes to the product affect data security, §8(c) how security-relevant updates are installed, §8(d) secure decommissioning including user-d... |
| 8.1.4 | D-08.1 | MUST | TEST/INSPECT (per corpus) | A financial-entity compulsory-modules-led staff training scheme is operated covering PR.AT-01 baseline awareness (phishing recognition, social-engineering resistance, password hygiene, incident-reporting reflexes, removable-media hygiene, disciplined use of administrative privileges) + PR.AT-02 role... |
| 8.2.1 | D-08.2 | MUST | TEST/INSPECT (per corpus) | A DPO-catalysed role-specific training programme is operated for personnel with data-subject-facing, access-management, breach-response or DPO-deputy responsibilities via PR.AT-02 role-understanding dimension (Workforce understands role-specific responsibilities) on a quarterly cadence or event-trig... |
| 8.2.2 | D-08.2 | MUST | TEST/INSPECT (per corpus) | A Member-State-encouraged employee risk-identification training programme is operated when the entity adopts the encouragement, covering PR.AT-01 recurring training content (phishing, social engineering, password discipline, threat-recognition capability) + PR.AT-02 role-specific dimension supportin... |
| 8.2.3 | D-08.2 | MUST | TEST/INSPECT (per corpus) | Where the product with digital elements is `intended for integration` per the manufacturer's documented intended purpose (Article 3(23) D23 + Annex II §4 — not third-party speculation about possible integration patterns), the product is accompanied by information via PR.AT-04 integrator's understand... |
| 8.2.4 | D-08.2 | MUST | TEST/INSPECT (per corpus) | A financial-entity `commensurate to the remit` function-specific depth training programme is operated for staff in security-critical roles via PR.AT-02 role-specific depth (Workforce understands role-specific responsibilities) covering incident response (cross to D-04 layer — RS.MA-01 incident-manag... |
| 8.2.5 | D-08.2 | MUST | TEST/INSPECT (per corpus) | For an AI-Act-scope high-risk AI system, the provider-side Art. 14(4) 5-element closed-list AND-coordinated design obligation is operationalised in NIST CSF 2.0 through PR.AT-02 (Workforce understands role-specific responsibilities — covers sub-points (a) `properly understand` and (c) `correctly int... |
| 8.3.1 | D-08.3 | MUST | TEST/INSPECT (per corpus) | Each member of the management body individually (the OJ does not provide a designation carve-out — the literal `members of the management bodies` reads as every member individually, per SR-NIS2-031 ambiguity_notes) has documented evidence of cybersecurity training completion covering the OJ purpose-... |
| 8.3.2 | D-08.3 | MUST | TEST/INSPECT (per corpus) | Each member of the management body has documented evidence of `actively keep up to date` against the Art. 5(4) threshold — `sufficient knowledge and skills to enable them to understand and assess ICT risk and its impact on the operations of the financial entity, including by following specific train... |

### D-09 Governance & Documentation — detailed fit_criteria

| Req ID | Sub-Domain | Priority | Verification | fit_criterion (truncated) |
|---|---|---|---|---|
| 9.1.1 | D-09.1 | MUST | TEST/INSPECT (per corpus) | Appropriate data-protection policies are documented and enforced under Art. 24(1) `appropriate technical and organisational measures, such as policies … which are designed to implement data-protection principles … in an effective manner` (SR-GDPR-043) with GV.PO-01 policy-instrument discipline (ever... |
| 9.1.2 | D-09.1 | MUST | TEST/INSPECT (per corpus) | Documented policies are established and maintained under Art. 21(2)(a) `policies on risk analysis and information system security` (SR-NIS2-035) documenting the entity's approach to identifying, assessing, and treating cybersecurity risks to network and information systems, and under Art. 21(2)(f) `... |
| 9.1.3 | D-09.1 | MUST | TEST/INSPECT (per corpus) | Manufacturer policies/processes/procedures are documented under Art. 13(8) sentence 6 `appropriate policies including a CVD policy` + Annex I Part II §5 CVD policy + Art. 13(8) sentence 2 support-period factors + Art. 13(23) cessation-of-operations communication procedure (SR-CRA-075) with GV.PO-01 ... |
| 9.1.4 | D-09.1 | MUST | TEST/INSPECT (per corpus) | A sound, comprehensive, and well-documented ICT risk-management framework is established under Art. 6(1) `which enables them to address ICT risk quickly, efficiently and comprehensively` (SR-DORA-027) with GV.PO-01 + GV.PO-02 + GV.RM-04 (the framework documents the entity's approach to ICT risk, sup... |
| 9.1.5 | D-09.1 | MUST | TEST/INSPECT (per corpus) | A QMS is documented under Art. 17(1) (SR-AIACT-017) in a systematic and orderly manner in the form of written policies, procedures, and instructions (POLY on `quality management system` — R1 ISO 9001 / R2 ISO/IEC 23053 / R3 internal bespoke; chosen reading: R3 literal since the OJ does not name any ... |
| 9.2.1 | D-09.2 | MUST | TEST/INSPECT (per corpus) | A pre-launch DPIA is documented and maintained under Art. 35(1) `prior to processing … carry out an assessment of the impact of the envisaged processing operations on the protection of personal data` (SR-GDPR-045) covering the 4-item Art. 35(7) content list (SR-GDPR-046) with ID.RA-04 impact-and-lik... |
| 9.2.2 | D-09.2 | MUST | TEST/INSPECT (per corpus) | Documented policies on risk analysis and information system security are established and maintained on a continuous basis under Art. 21(2)(a) `policies on risk analysis and information system security` (SR-NIS2-035) with ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (the entity's ap... |
| 9.2.3 | D-09.2 | MUST | TEST/INSPECT (per corpus) | The cybersecurity risk assessment is documented under Art. 13(3) sentence 1 `documented and updated` (SR-CRA-064) with ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (Art. 13(2) `cybersecurity risk assessment … taking into account the intended purpose and reasonably foreseeable use, ... |
| 9.2.4 | D-09.2 | MUST | TEST/INSPECT (per corpus) | The financial entity's ICT risk identification register is maintained on a continuous basis under Art. 7(2) sentence 1 `continuously … identify all sources of ICT risk … including the risk exposure to and from other financial entities, and assess cyber threats and ICT vulnerabilities relevant to ICT... |
| 9.2.5 | D-09.2 | MUST | TEST/INSPECT (per corpus) | A continuous iterative risk-management system is established, implemented, documented, and maintained across the AI lifecycle under Art. 9(1) `established, implemented, documented and maintained` (SR-AIACT-001) with ID.RA-05 threats-vulnerabilities-likelihoods-impacts dimension (Art. 9(2)(a) `the id... |
| 9.3.1 | D-09.3 | MUST | TEST/INSPECT (per corpus) | The Art. 21(2)(i) sub-domain `human resources security, access control policies and asset management` (SR-NIS2-005) is established as one of three coordinated sub-domains of access control (HR security + access control + asset management) with PR.PS-01 configuration-management dimension (the entity ... |
| 9.3.2 | D-09.3 | MUST | TEST/INSPECT (per corpus) | The technical documentation is drawn up under Annex VII §1 `general description` (intended purpose + software versions affecting compliance + hardware external features where applicable + user information and instructions per Annex II) + Annex VII §2 `design, development, production and vulnerabilit... |
| 9.3.3 | D-09.3 | MUST | TEST/INSPECT (per corpus) | The financial entity maintains a dedicated entity-level asset inventory under Art. 7(1) `Financial entities shall identify, classify and adequately document all ICT supported business functions, the roles and responsibilities supporting those functions, the information assets and ICT assets supporti... |
| 9.4.1 | D-09.4 | MUST | TEST/INSPECT (per corpus) | A RoPA is maintained per Art. 30(1) `record of processing activities under its responsibility` with the 7-item content list (SR-GDPR-048) verified by ID.AM-08 lifecycle-management dimension (controller demonstrates ex post that systems, hardware, software, services, and data are managed throughout t... |
| 9.4.2 | D-09.4 | MUST | TEST/INSPECT (per corpus) | Certification-driven records are maintained per Art. 24(1) sentence 1 `Member States shall encourage the use of European or internationally accepted standards and specifications relevant to the security of network and information systems` (SR-NIS2-043) verified by ID.AM-08 lifecycle-management dimen... |
| 9.4.3 | D-09.4 | MUST | TEST/INSPECT (per corpus) | Technical documentation is drawn up before placing on market per Art. 13(12) sentence 1 `the manufacturer shall draw up the technical documentation referred to in Article 31` (SR-CRA-085) verified by ID.AM-08 lifecycle-management dimension (manufacturer demonstrates ex post that the Annex VII §1-§8 ... |
| 9.4.4 | D-09.4 | MUST | TEST/INSPECT (per corpus) | An information security policy is developed and documented per Art. 9(4)(a) `Financial entities shall … develop and document an information security policy defining rules to protect the availability, authenticity, integrity and confidentiality of data, information assets and ICT assets, including th... |
| 9.4.5 | D-09.4 | MUST | TEST/INSPECT (per corpus) | Technical documentation is drawn up and kept up-to-date per Art. 11(1) `Providers of high-risk AI systems shall draw up and keep up-to-date the technical documentation of the high-risk AI system in accordance with Annex IV before that system is placed on the market or put into service` (SR-AIACT-009... |

### D-10 Monitoring & Audit — detailed fit_criteria

| Req ID | Sub-Domain | Priority | Verification | fit_criterion (truncated) |
|---|---|---|---|---|
| 10.1.1 | D-10.1 | MUST | TEST/INSPECT (per corpus) | Entity-level monitoring of personal-data processing systems is operational per Art. 32(1)(b) + Art. 32(1)(d) + Art. 32(2) + Art. 33(1) (SR-GDPR-019 + SR-GDPR-020 + SR-GDPR-021) verified by DE.CM-01 primary (Networks and network services are monitored to find potentially adverse events — the controll... |
| 10.1.2 | D-10.1 | MUST | TEST/INSPECT (per corpus) | An incident-handling capability is established per Art. 21(2)(b) `incident handling` (SR-NIS2-009 + SR-NIS2-014) with the 6-action lifecycle (prevent, detect, analyse, contain, respond, recover — per SR-NIS2-008) verified by DE.CM-01 primary (Networks and network services are monitored to find poten... |
| 10.1.3 | D-10.1 | MUST | TEST/INSPECT (per corpus) | Product-level on-device internal-activity monitoring is operational per Annex I Part I (2)(l) + Annex I Part II (6) (SR-CRA-100 + SR-CRA-101) verified by DE.CM-01 primary (Networks and network services are monitored to find potentially adverse events — anchors the CRA Annex I Part I (2)(l) on-device... |
| 10.1.4 | D-10.1 | MUST | TEST/INSPECT (per corpus) | Continuous monitoring of ICT systems and tools is operational per Art. 8(1) per SR-DORA-030 OJ-literal locus Art. 9(1) `Financial entities shall continuously monitor and control the security and functioning of ICT systems and tools and shall minimise the impact of ICT risk on ICT systems through the... |
| 10.1.5 | D-10.1 | MUST | TEST/INSPECT (per corpus) | A post-market monitoring system is established and documented per Art. 72(1) + Art. 72(2) + Art. 74(1) (SR-AIACT-021 + SR-AIACT-022) verified by DE.CM-09 primary (Computing hardware and software, runtime environments, and their data are monitored — anchors the AI Act Art. 72(2) `actively and systema... |
| 10.2.1 | D-10.2 | MUST | TEST/INSPECT (per corpus) | Entity-level compliance records are maintained in writing or electronic form with integrity + traceability per Art. 30(3) + Art. 5(2) + Art. 31 (SR-GDPR-044 + SR-GDPR-048 + SR-GDPR-050) verified by PR.DS-11 primary (Data are destroyed according to policy — anchors the GDPR Art. 30(3) `in writing, in... |
| 10.2.2 | D-10.2 | MUST | TEST/INSPECT (per corpus) | Product-level documentation traceability is operational per Annex VII §5–§8 + Annex VII §3 + Annex I Part II (3) + Art. 13(4) sentence 1 + Art. 13(22) (SR-CRA-088 + SR-CRA-080 + SR-CRA-069 + SR-CRA-070 + SR-CRA-102) verified by PR.DS-11 primary (Data are destroyed according to policy — anchors the C... |
| 10.2.3 | D-10.2 | MUST | TEST/INSPECT (per corpus) | An information security policy is developed and documented per Art. 9(4)(a) (SR-DORA-031) verified by GV.PO-01 primary (Organizational information security policy is established and communicated — anchors the DORA Art. 9(4)(a) information security policy mapped to NIST CSF 2.0 GV.PO-01) + PR.DS-12 (... |
| 10.2.4 | D-10.2 | MUST | TEST/INSPECT (per corpus) | AI-system automatic event logging is operational per Art. 12(1) + Art. 12(2) + Art. 19(1) (SR-AIACT-007 + SR-AIACT-008 + SR-AIACT-009) verified by PR.PS-04 primary (Software installation, operation, and updates are performed consistent with the security policy — anchors the AI Act Art. 12(1) `techni... |
| 10.3.1 | D-10.3 | MUST | TEST/INSPECT (per corpus) | An effectiveness-evaluation process is established per Art. 32(1)(d) + Art. 35(11) (SR-GDPR-019 + SR-GDPR-021 + SR-GDPR-022) verified by PR.IP-07 primary (Configuration change control processes are in place — anchors the GDPR Art. 32(1)(d) `regularly testing, assessing and evaluating the effectivene... |
| 10.3.2 | D-10.3 | MUST | TEST/INSPECT (per corpus) | Effectiveness-assessment policies and procedures are established per Art. 21(2)(f) (SR-NIS2-037 + SR-NIS2-038) verified by PR.IP-07 primary (Configuration change control processes are in place — anchors the NIS 2 Art. 21(2)(f) `policies and procedures to assess the effectiveness of cybersecurity ris... |
| 10.3.3 | D-10.3 | MUST | TEST/INSPECT (per corpus) | Product-level conformity-assessment is operational per Annex I Part II (3) + Annex VII §6 + Annex VIII Part I (Module A) + Annex VIII Part II (Module B+C and H) (SR-CRA-101 + SR-CRA-103 + SR-CRA-104) verified by PR.IP-07 primary (Configuration change control processes are in place — anchors the CRA ... |
| 10.3.4 | D-10.3 | MUST | TEST/INSPECT (per corpus) | A digital operational resilience testing programme is established, maintained, and reviewed per Art. 24(1) + Art. 25(1) + Art. 26(1) (SR-DORA-008 + SR-DORA-009 + SR-DORA-010) verified by PR.IP-07 primary (Configuration change control processes are in place — anchors the DORA Art. 24(1) `sound and co... |
| 10.3.5 | D-10.3 | MUST | TEST/INSPECT (per corpus) | AI-system-level testing is operational per Art. 9(6) + Art. 9(7) + Art. 15(1) (SR-AIACT-003 + SR-AIACT-014) verified by PR.IP-07 primary (Configuration change control processes are in place — anchors the AI Act Art. 9(6) `tested for the purpose of identifying the most appropriate and targeted risk m... |

## 3. Summary Dashboard

| Macro-domain | Current | Target | Gap |
|---|---:|---:|---:|
| D-01 Data Protection | 4 | 4 | 0 |
| D-02 Vulnerability Management | 4 | 4 | 0 |
| D-03 Access Control | 4 | 4 | 0 |
| D-04 Incident Response | 3 | 4 | 1 |
| D-05 Data Lifecycle | 3 | 4 | 1 |
| D-06 Supply Chain | 4 | 4 | 0 |
| D-07 Secure Development | 4 | 4 | 0 |
| D-08 Human Factors | 4 | 4 | 0 |
| D-09 Governance & Documentation | 4 | 4 | 0 |
| D-10 Monitoring & Audit | 4 | 4 | 0 |
| **OVERALL** | **3.8** | **4.0** | **0.2** |

## 4. Top Gaps (feeds Doc 07)

| Rank | Macro-domain | Gap | Gap Summary | Priority Remediation |
|---:|---|---:|---|---|
| 1 | D-04 Incident Response | 1 | D-04.3 multi-deadline routing workflow for 5-regulation compound events (4h DORA / 24h NIS 2 / 24h CRA / 72h GDPR / 15d AI Act) needs full integration | Implement unified routing matrix with 4h DORA RTS as the universal SLA; compound-event playbook for AI-Act + DORA + CRA + NIS 2 + GDPR stack; tabletop Q3 2026 |
| 2 | D-05 Data Lifecycle | 1 | D-05.3 cryptographic sharding for AI Act log retention vs. GDPR Art. 17 erasure conflict (T-002 Phase 2 strategic-tensions) | Implement cryptographic sharding: anonymise erasure target before applying erasure to satisfy AI Act Art. 12 log retention + GDPR Art. 17 simultaneously; cryptographic sharding solution |
| 3 | D-04 Incident Response | 1 | D-04.4 cloud-region DR automation for EU cloud production; managed disaster replication is automated but EU cloud regions need further automation | Automate cross-region failover for STORE-02 + STORE-04 + STORE-07; quarterly DR test cadence |
| 4 | D-04 Incident Response (overlay gap) | — | AI Act 3-tier reporting (Art. 73: 15d / 2d / 10d death) requires dedicated SOC playbook updates | Add 3-tier reporting playbook; tabletop Q3 2026 |
| 5 | D-09 Governance (active gap) | — | DORA Art. 24 TLPT every 3 years — first TLPT scheduled 2026-Q4; AI Act conformity assessment 2026-Q3 | Schedule TLPT kickoff 2026-Q3; complete AI Act conformity assessment; CRO owns |

## 5. Consistency Check

| Consistency Item | Status | Evidence |
|---|---|---|
| Architecture evidence matches 04a | PASS | SYS-01..SYS-25, STORE-01..STORE-12, FLOW-01..FLOW-25 referenced consistently |
| Regulatory scope matches Doc 04 and Doc 05 | PASS | `applicable_regs = [GDPR, NIS2, CRA, DORA, AI_Act]`; 38 active SubDomains; D-08.3 ACTIVE (NIS 2 + DORA) |
| MAXIMUM-tier proportionality maintained | PASS | No over-engineering (HSM cluster + SIEM + EDR + managed PAM + mainframe access control are the minimum for a credit institution + 5-regulation overlap); no under-engineering (DORA Art. 24 TLPT + AI Act conformity assessment scheduled) |
| Maturity scale used consistently | PASS | Current values are integers 0-4; target and gap shown numerically |
| Evidence and gaps align | PASS | D-04, D-05 are top gaps (operationally); D-01, D-02, D-03, D-06, D-07, D-08, D-09, D-10 are strongest (mature) |
| D-08.3 ACTIVE flagged correctly | PASS | D-08.3 participation: [NIS2, DORA]; applicable_regs includes both → ACTIVE. Dual NIS 2 Art. 20 + DORA Art. 5 obligation |

## 6. Gate

| Gate Criterion | Status | Evidence |
|---|---|---|
| All 10 macro-domains assessed with maturity level and evidence | PASS | Section 2 |
| Target maturity defined per macro-domain | PASS | Sections 2 and 3 |
| Summary dashboard populated | PASS | Section 3 |
| Top 5 gaps identified | PASS | Section 4 |
| SubDomains references included | PASS | Each macro-domain section links to all 38 active Regulatory Baseline files |
| D-08.3 ACTIVE flagged (NIS 2 + DORA-applicable) | PASS | D-08.3 section §2 + consistency check §5 |

## N-1. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-07-11 | Executor | Created OmniBank populated security posture assessment from the 04b template; MAXIMUM-tier maturity averaging 3.8 (vs SecureBorder's 3.0 for HIGH tier; vs TinyTask's 1.3 for LOW tier), with D-08.3 ACTIVE under NIS 2 + DORA Art. 5 dual obligation. |
| 1.2 | 2026-08-06 | Executor | Sprint 2 corpus enrichment: new §2.1 added with per-macro-domain + per-sub-domain Volere fit_criteria + verification methods from corpus JSON sidecars (134 sub-requirements across 38 sub-domains aggregated to 10 macro-domains; MUST priority dominant); status RECONCILED → CORPUS_ENRICHED. |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-07-11 |
| Technical Review | CTO |  |  |
| Security Review | CISO |  |  |
| Compliance Review | CRO |  |  |
| DPO Review | DPO |  |  |
| AI Governance Review | AI Governance Lead |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Data backbone:** `Case_03_Phase1.xlsx` (13 sheets: COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, MATURITY, SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES)
- **Architecture context:** `04a_Architecture_DataInventory.md` §1.1 (25 systems), §2.1 (12 stores), §2.2 (25 flows).
- **People/RACI:** `04d_Org_Roles_RACI.md` (~40 named-RACI roles including CISO + DPO + CRO + AI Governance Lead + dedicated mainframe + AI + payments teams).
- **MAXIMUM-tier context:** `../../02_CASES/Case_03_OmniBank_Financial/00_COMMON/01_Company_Context.md` (5 applicable regulations; complexity tier MAXIMUM; 5,000+ employees; DORA financial entity + NIS 2 essential entity + AI Act Annex III + CRA mobile app).
- **Corpus fit_criteria source:** see §2.1 for per-macro-domain + per-sub-domain Volere fit_criteria + verification methods derived from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_Y/*.json` (Volere `requirements.sub_requirements[].yaml`). 134 sub-requirements total across 38 sub-domains; all MUST priority; verification methods TEST + INSPECT (D-05 + D-07).