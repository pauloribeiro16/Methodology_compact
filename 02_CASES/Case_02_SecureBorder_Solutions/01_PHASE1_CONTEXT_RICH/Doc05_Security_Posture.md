---
document_id: AEGIS-P2-RICH-04b-POSTURE
title: Security Posture Assessment (Rich Mode, superseded)
phase: 1
version: 1.3
created: 2026-07-11
updated: 2026-08-27
author: Executor (Sprint 2 Corpus Enrichment, 2026-08-06; Phase 2 Bloco E posture-model migration; v2.3 maturity redesign note)
status: DEPRECATED_FOR_MATURITY
status_history:
  - { date: '2026-08-07', from: CORPUS_ENRICHED, to: DEPRECATED_FOR_POSTURE,
      reason: 'Posture ownership moved to Doc19 (legacy 13_Framework_Mapping_Matrix) — resolves PHASE1_STRATEGY §7 contradiction' }
  - { date: '2026-08-27', from: DEPRECATED_FOR_POSTURE, to: DEPRECATED_FOR_MATURITY,
      reason: 'Maturity redesigned per MATURITY_MODEL_CSF_STRICT.md (CSF 2.0 strict, two scales, evidence-based); see Case_02_P1_Maturity.html Folio VIII' }
maturity_owner: 00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md
posture_owner: Doc19_Framework_Mapping_Matrix.md
note: >
  Este documento mantém-se como INPUT qualitativo (postura observada).
  v2.3 — A avaliação de escala A/B (CSF Tiers + Coverage) foi movida para
  00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §3-§6 (referencial único
  CSF 2.0 §3.4, Tiers T1-T4 ao nível Organisation/Function, EvidenceItem
  nodes no grafo P1, sem maturity_cur/maturity_tgt scalars no sub-domínio).
  Ver Case_02_P1_Maturity.html Folio VIII para visualização. AI-RMF anchors
  aplicáveis (SecureBorder é AI Act provider) aparecem na tabela Scale A.
  A avaliação de postura (Implementation Posture) continua em
  02_PHASE2_RULES_RICH/Doc19_Framework_Mapping_Matrix.md §4-5.
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
active_subdomains: 34
inactive_documented: [D-06.4, D-07.4, D-08.3, D-09.3 NOT_ADDRESSED]
inputs:
  - Doc03_Company_Context_Assessment.md
  - Doc04_Architecture_DataInventory.md
  - Doc08_Regulatory_Applicability.md
outputs:
  - Doc06_ThirdParty_Landscape.md
  - Doc07_Org_Roles_RACI.md
  - Doc11_Structured_Compliance_Matrix.md
related_documents:
  - Doc04_Architecture_DataInventory.md
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/index.md
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/
reconciliation:
  role: reconciliation
  base_doc: ../01_PHASE1_CONTEXT/Doc05_Security_Posture.md (legacy, frozen)
  notes: |
    Sprint 1 reconciliation (Case_02, 2026-08-06):
    - Frontmatter updated to AEGIS-P2-RICH-* convention (P2 = Case_02).
    - status: DRAFT → RECONCILED.
    - active_subdomains aligned to 35 (legacy declared 38, canonical for Case_02 is 35).
    - applicable_regs aligned to [GDPR, CRA, NIS 2, AI_Act] (excludes DORA per Case_02).
    - Body preserved verbatim (Sprint 1 is content-neutral; Sprint 2 adds corpus linkages).
    - Sprint 2 Corpus Enrichment:
      - §2 Per-Domain Assessment: each macro-domain gains 2 corpus fields (Target fit_criterion + Verification Method).
      - §6 Corpus Provenance: new section with per-macro-domain corpus linkage table.
---

> ⚠️ **DEPRECATED FOR POSTURE (2026-08-07).** A avaliação e o modelo de postura e
> postura vivem agora em
> `02_PHASE2_RULES_RICH/Doc19_Framework_Mapping_Matrix.md` §4-5. Este documento
> mantém-se como input qualitativo (postura observada). Ver `status_history`
> no frontmatter.

<!-- CORPUS ENRICHMENT BANNER (Sprint 2, 2026-08-06):
     This is the Rich Mode copy of AEGIS-P1-04b.
     Source: ../01_PHASE1_CONTEXT/Doc05_Security_Posture.md.
     Sprint 2 added: §2 per-macro-domain (D-01..D-10) Corpus fit_criterion + Verification Method;
                     new §6 Corpus Provenance.
     See SPRINT2_ENRICHMENT_REPORT_EXISTING.md for the per-doc change list.
-->

# Security Posture Assessment (superseded by Implementation Posture Model v2.0)

## 1. Assessment Methodology

SecureBorder is a **HIGH-complexity** company with 450 employees, ISO 27001 + ISO 27701 certified, in-house 24/7 SOC, hardware cryptographic module cluster, on-device product (GuardianGate) classified as CRA Critical Class + AI_Act Annex III. Current posture reflects what exists today; the target profile reflects what the active GDPR + CRA + NIS 2 + AI_Act SubDomains fit_criteria require. Where ISO 27001 controls are inherited but regulation-specific overlays exist (D-02.4 pen testing per CRA; D-04.3 multi-regulation notification deadlines; D-07.2 secure-coding under AI_Act risk management), the higher target applies.

| Level | Label | Description |
|---|---|---|
| 0 | None | No controls in place |
| 1 | Ad-hoc | Informal, inconsistent, no documentation |
| 2 | Defined | Documented or consistently repeatable, but not fully measured |
| 3 | Managed | Implemented, monitored, measured, and regularly reviewed |
| 4 | Optimized | Continuously improved and substantially automated |

Evidence is drawn from `Doc04_Architecture_DataInventory.md`, `Doc03_Company_Context_Assessment.md`, and `Doc08_Regulatory_Applicability.md`. Active scope: 38 of 38 SubDomains (4 regulations applicable; no INACTIVE sub-domain for SecureBorder).

## 2. Per-Domain Assessment

### D-01 Data Protection — Implementation Status: IMPLEMENTED (backfilled from legacy level 3, target met)

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Encryption at rest | industry-standard symmetric encryption KMS-managed with hardware cryptographic module-bound CMK across all production stores (STORE-01 to STORE-07) | SYS-01 KMS + SYS-07 hardware cryptographic module in `04a §1.1` + STORE-01..07 in `04a §2.1` | Watchlist cache (STORE-03) and biometric transient cache (STORE-05) use hardware cryptographic module-bound CMK; deletion-by-design for biometrics |
| Encryption in transit | mutual transport authentication over QUIC for kiosk-to-cloud; modern transport security internal; mutual transport authentication to government via SYS-02/SYS-03 | FLOW-01..12 in `04a §2.2`; SYS-04 firmware in `04a §1.1` | cryptographic module certified to applicable assurance level Level 3 hardware cryptographic module session keys; client cert in TPM 2.0 for SYS-04 |
| Key management | cryptographic module certified to applicable assurance level Level 3 hardware cryptographic module cluster (SYS-07); quarterly key ceremonies; dual control | SYS-07 in `04a §1.1`; SYS-07 dual-control note in `04a §1.4` | Some legacy keys still on managed cryptographic key custody without hardware cryptographic module bind — tracked as low-priority migration |
| Data integrity | approved hash function hash-chained audit entries (hardware cryptographic module-signed per row) in STORE-04; cryptographic signing-signed OTA packages in STORE-02 | SYS-09 + SYS-11 in `04a §1.1`; STORE-04 + STORE-02 integrity in `04a §2.1` | Tamper-evident immutable WORM with cryptographic hash chain |

**Target profile note:** some sub-targets at legacy level 4 — see Regulatory Baseline fit criteria for D-01.4)
**Gap**: 0 (with isolated low-priority migration item)
**Notes**: Current evidence supports D-01.1 through D-01.4 at level 3; the only minor item is migrating remaining managed cryptographic key custody keys to hardware cryptographic module-bound CMK (low-priority, ~30-day project tracked separately). The cryptographic integrity layer for audit (D-01.4) achieves level 4 by being cryptographically signed and hash-chained. Relevant Regulatory Baseline files: [D-01.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.1.md), [D-01.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.2.md), [D-01.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.3.md), [D-01.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.4.md).


**Corpus Target fit_criterion** (from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.manifest.json` + first applicable sub-domain JSON sidecar):

> industry-standard symmetric encryption (or stronger) symmetric encryption is applied to all data-at-rest storage volumes holding the in-scope data class (personal data, NIS data, CRA product data, or DORA ICT-supported data, as triggered); key custody is logically or physically separated from data access via role-based access control on key-material vs operational-environment credentials; cipher strength meets or exceeds the st...

**Verification Method** (aggregated from `requirements.sub_requirements[].verification_method` across applicable sub-domains):

> TEST

### D-02 Vulnerability Management — Implementation Status: IMPLEMENTED (backfilled from legacy level 3, target met)

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Vulnerability scanning | Weekly enterprise vulnerability scanner on SYS-01 + enterprise vulnerability scanner for firmware; dependency security scanner per-build on SYS-11; EDR-detected runtime vulns via endpoint detection and response platform | SYS-11, SYS-12 in `04a §1.1`; FLOW-09 in `04a §2.2` | Critical-class (CRA) + AI-system (AI_Act) overlay targets sub-7-day remediation for known CVEs |
| Patch management | Critical CVEs patched within 7 calendar days; firmware OTA distributed via SYS-11; quarterly maintenance window for non-critical | SYS-04 firmware dev; SYS-11 in `04a §1.1` | CRA Art. 13(8) 5-year support period floor; secure dispatch via signed artefacts |
| Pen testing | Annual external (certified penetration testing body-accredited) pen test + 6-monthly internal red team exercises; AI-system adversarial testing | STORE-04 in `04a §2.1`; FLOW-01 in `04a §2.2` | Threat-led per CRA Annex I Part II (2); AI_Act Art. 9 + 15 adversarial-robustness |
| CVD policy | Published at `/.well-known/security.txt` per CRA Art. 14; ENISA CVD hub registration; ISAC participation (Border Security ISAC) | (paper artefact; policy reference) | Coordinated flow established; CSIRT (NL) + ENISA copy flow per CRA Art. 14(1) |

**Target profile note:** D-02.4 pen testing per CRA + AI_Act is a level-3 target profile
**Gap**: 0
**Notes**: Threat-led pen testing (D-02.4) achieves CRA Critical Class + AI_Act Annex III expectations. The CVD policy (D-02.3) is published and includes a 24h early-warning notification channel to CSIRT per CRA Art. 14(1). Relevant Regulatory Baseline files: [D-02.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.1.md), [D-02.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.2.md), [D-02.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.3.md), [D-02.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.4.md).


**Corpus Target fit_criterion** (from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.manifest.json` + first applicable sub-domain JSON sidecar):

> An ID.RA-01 vulnerabilities-identified-validated-recorded register is maintained at the DORA-cadenced `continuous + at-least-yearly` floor (when DORA in scope) or the CRA-R2 `constructive knowledge` baseline (when CRA-only) or the NIS-2 silent baseline (when NIS-2-only); the register records scope-determiner tag (personal data / NIS / product with digital elements / ICT-supported business function...

**Verification Method** (aggregated from `requirements.sub_requirements[].verification_method` across applicable sub-domains):

> TEST

### D-03 Access Control — Implementation Status: IMPLEMENTED (backfilled from legacy level 3, target met)

| Control | Current | Evidence | Notes |
|---|---|---|---|
| IAM system | dedicated identity provider for SaaS with federation bridge for legacy systems; SAML federation protocol 2.0 / open identity protocol across all corporate apps | SYS-08 in `04a §1.1`; STORE-06 in `04a §2.1` | Hybrid model: dedicated identity provider for SaaS, federation bridge for on-prem legacy; managed via single dedicated identity provider dashboard |
| multi-factor authentication | Mandatory for ALL accounts: hardware-backed second-factor authenticator hardware keys for privileged (40 staff); time-based one-time password fallback for non-privileged | SYS-08 + SYS-07 in `04a §1.4` | Customer multi-factor authentication not applicable (kiosks are unmanned; end-user authenticates via passport) |
| role-based access control | Tiered: 6 user roles + 8 privileged roles (mapped to leak matrix); HR-driven joiner-mover-leaver workflow | SYS-08 + SYS-12 SOC roles in `04a §1.4` | Quarterly access reviews owned by DPO + CISO; evidence in STORE-04 |
| Privileged access management | Just-in-time elevated access via dedicated identity provider + step-up multi-factor authentication for high-risk actions; hardware cryptographic module key access requires dual control | SYS-07 dual-control note + SYS-08 in `04a §1.4` | PAM-tier achieved; PAM-tool (CyberArk) under evaluation for high-risk system accounts |
| Default secure configs | CIS benchmarks + ISO 27001 A.13 baseline; SOC2 monitoring against drift; CRA Annex I Part I (1) secure-by-default design for SYS-04 firmware | SYS-04 firmware in `04a §1.1` | Kiosk firmware ships in secure-default state (no debug ports enabled) |

**What's missing (PARTIAL):** uplift for D-03.3 due to NIS 2 + AI_Act privileged access requirements (legacy target level 4)
**Gap**: 1 (PAM tool procurement — minor)
**Notes**: Privileged access is well-controlled at level 3; the PAM-tool procurement would lift D-03.3 to level 4. Quarterly access reviews are documented with evidence; hardware cryptographic module dual control is in place. The "customer multi-factor authentication" issue from TinyTask does not apply (kiosks are unmanned; authentication is via document). Relevant Regulatory Baseline files: [D-03.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.1.md), [D-03.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.2.md), [D-03.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.3.md), [D-03.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.4.md).


**Corpus Target fit_criterion** (from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.manifest.json` + first applicable sub-domain JSON sidecar):

> A multi-boundary identity architecture is operated with one identity register per boundary (data-subject verification register, workforce JML register, product-side user/service/component register, financial-entity staff/service-identity assertion register) and explicit hand-off protocols at the four identity-type surfaces; each register records identity subject, trigger, threshold anchor, lifecyc...

**Verification Method** (aggregated from `requirements.sub_requirements[].verification_method` across applicable sub-domains):

> TEST

### D-04 Incident Response — Implementation Status: IMPLEMENTED (backfilled from legacy level 3, target met)

| Control | Current | Evidence | Notes |
|---|---|---|---|
| IR plan | Documented incident response plan v4.7 (April 2026); quarterly incident response exercises; 2 annual full-scale exercises with airport authority | SOC v4.7 procedure docs; evidence in STORE-04 | Plan covers all 4 regulations' notification timelines (24h CRA / 24h NIS 2 / 72h GDPR / 15d AI_Act) |
| Detection capability | centralised log aggregation platform Enterprise Security Security Information and Event Management (USPs 13 SOC analysts 24/7; 4 across 3 shifts + 1 on-call) + endpoint detection and response platform endpoint detection and response platform + managed vulnerability intelligence feed + custom ML anomaly detection | SYS-12 in `04a §1.1`; STORE-04 in `04a §2.1` | One of the few EU SOCs with native AIR (Adversarial Input Recognition) for AI-system anomaly detection |
| Notification process | CISO-owned 24h CSIRT routing (NIS 2 Art. 23(4)(a)); 72h DPA routing (GDPR Art. 33) via DPO; AI_Act 3-tier routing (Art. 73) per AI Governance Lead | FLOW-10 in `04a §2.2` | Tested quarterly; tabletop timings recorded in STORE-04 audit |
| Recovery procedures | BCP tested annually; RTO 4h, RPO 15min; immutable backup via SYS-01 + STORE-02 + cross-region replication | STORE-01 + STORE-02 backups in `04a §2.1` | Critical Class CRA + 99.99% SLA for airport ops requires tested sub-4h recovery |

**Target:** met (legacy level 3)
**Gap**: 0
**Notes**: All 4 regulations' notification timelines are met, but the AI_Act 3-tier reporting (15d / 2d / 10d) requires more rigour than the prior ISO-only process. The integrated playbooks for compound events (e.g., AI-Act-triggered product vulnerability that is also a GDPR personal-data breach) are tracked in Phase 2 strategic-tensions resolution. Relevant Regulatory Baseline files: [D-04.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.1.md), [D-04.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.2.md), [D-04.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.3.md), [D-04.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.4.md).


**Corpus Target fit_criterion** (from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.manifest.json` + first applicable sub-domain JSON sidecar):

> A multi-layer detection architecture is operated with one detection pipeline per layer (data-flow / entity / product-internal / financial-entity ICT) and explicit layer hand-offs at the detection-type surfaces; each pipeline records detection object, trigger anchor, threshold qualifier, awareness/triage moment, recipient (downstream), and evidence template per asset; the DORA `multi-layer + alert-...

**Verification Method** (aggregated from `requirements.sub_requirements[].verification_method` across applicable sub-domains):

> TEST

### D-05 Data Lifecycle — Implementation Status: IMPLEMENTED (backfilled from legacy level 3, target met)

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Data minimisation | biometric reference data deleted within seconds (Art. 5(1)(c) by design); watchlist data lives at controller; SYS-04 + SYS-06 hardware-locked TTL on caches | STORE-05 in `04a §2.1`; DPO policy | Traveller data minimisation is a key GDPR Art. 9 + AI_Act Art. 10 data-governance design principle |
| Retention policies | Tamper-evident 10-year audit retention (STORE-04); SAP-driven 7-year employment records; dedicated identity provider 90-day post-termination credential retention | STORE-04, STORE-06, STORE-07 in `04a §2.1` | Lifetime retention for AI-system training data lineage (Art. 10 AI_Act) |
| Erasure procedures | Automated for biometric and watchlist cache; controller-driven for traveller data; HR-driven for employee records with DPO oversight; DSAR via dedicated portal | SYS-10 + DPO workflow in `04a §2.4` | Tested via annual DSAR tabletop |
| Data portability | Controller-side (not within SecureBorder scope) — government authority owns traveller-data export; SecureBorder provides audit-log export to controller | (n/a for traveller data; controller owns) | EU staff records exportable via SAP standard HR process |

**Target:** met (legacy level 3)
**Gap**: 0
**Notes**: Data minimisation at the kiosk edge (D-05.1) is exemplary (level 4) — biometric reference data lives for seconds, not hours. The retention policies balance 10-year audit (NIS 2 + GDPR Art. 5(1)(e)) with AI_Act training-data lineage. Right to erasure (D-05.3) has both automated and HR-DPO workflows. Portability (D-05.4) is partial — SecureBorder is a processor for traveller data so the right is in the controller; SecureBorder's audit-log export to controller supports it. Relevant Regulatory Baseline files: [D-05.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.1.md), [D-05.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.2.md), [D-05.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.3.md), [D-05.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.4.md).


**Corpus Target fit_criterion** (from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.manifest.json` + first applicable sub-domain JSON sidecar):

> A multi-class data-minimisation architecture is operated with explicit class-segregated hand-offs at the personal-data / product-data / training-data surfaces; each data class has a documented necessity assessment (purpose + lawful basis + data-class scope + necessity test + retention time-limit + safeguard posture) per ID.AM-03 data-inventory substrate + PR.DS-12 risk-strategy-bound retention; th...

**Verification Method** (aggregated from `requirements.sub_requirements[].verification_method` across applicable sub-domains):

> INSPECT, TEST

### D-06 Supply Chain — Implementation Status: IMPLEMENTED (backfilled from legacy level 3, target met)

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Vendor assessment | Tiered criticality; annual formal assessment for Critical + Important vendors; ISO 27001 + third-party assurance attestation + ISO 27701 evidence required for all data processors | `Doc06_ThirdParty_Landscape.md §5` (separate document) | NIS 2 supply-chain security obligations (Art. 21(2)(d)) |
| software bill of materials | machine-readable software bill of materials format 1.5 emission per release; published per OTA; verified against ENISA software bill of materials guidance | SYS-11 + STORE-02 in `04a §1.1`; FLOW-04 in `04a §2.2` | Required for CRA Critical Class (Art. 13(13)); integrated with vulnerability management |
| Contract clauses | Article 28 GDPR DPA template; CRA Annex I Part I (2)(h) (component security) clauses; NIS 2 supply-chain addendum; AI_Act provider-deployer interface clauses (Art. 25) | (paper artefact; DPA template library) | Multi-regulation clause bank maintained by DPO + Legal |
| Boundary management | Vendor egress reviewed; sub-processor chains tracked; pseudonymisation before any logging egress; formal sub-processor change notifications | SYS-09 + DPAs in `04a §1.3` | Per GDPR Art. 28(2) sub-processor notification flow |

**Target:** met (legacy level 3)
**Gap**: 0
**Notes**: D-06 covers both legal (DPA template library, sub-processor flow) and technical (software bill of materials pipeline). The cross-border aspects (different DPAs per country deployment) are tracked separately in `Doc06_ThirdParty_Landscape.md`. Relevant Regulatory Baseline files: [D-06.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.1.md), [D-06.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.2.md), [D-06.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.3.md), [D-06.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.4.md).


**Corpus Target fit_criterion** (from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.manifest.json` + first applicable sub-domain JSON sidecar):

> A 4-tier vendor-risk-assessment architecture is operated with explicit tier separation (processor-tier GDPR / supplier-tier NIS 2 / component-tier CRA / ICT-provider-tier DORA) and documented tier hand-offs at the assessment-type surfaces; each tier records assessment object (processor-as-legal-entity / supplier-as-relationship / component-as-technical-artefact / ICT-provider-as-counterparty), pro...

**Verification Method** (aggregated from `requirements.sub_requirements[].verification_method` across applicable sub-domains):

> TEST

### D-07 Secure Development — Implementation Status: IMPLEMENTED (backfilled from legacy level 3, target met)

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Secure-by-design | Threat model per feature; ISO 27001 A.14 baseline; CRA Annex I Part I (1) secure-by-design; AI_Act Art. 9 risk-management system integrated | SYS-04 firmware dev + SYS-05 ML pipeline in `04a §1.1` | EU AI_Act Art. 9 risk-management is a level-3 control for high-risk AI |
| Secure coding | OWASP Top 10 + IEC 62443 embedded-system baseline; static analysis (dependency security scanner + custom); peer review on all PRs | SYS-11 in `04a §1.1` | Secure-by-default coding for SYS-04 firmware (CRA Part I (1)) |
| CI/CD security | static application security testing + SCA + cryptographic signing signing + artefact registry + dynamic application security testing on staging; machine-readable software bill of materials format software bill of materials emission per build | SYS-11 + STORE-02 in `04a §1.1` | software bill of materials + signed artefacts per CRA Critical Class |
| Change management | PR review + CAB + dual approval for production; AI model changes follow AI_Act Art. 9 + 16 change-control procedure | SYS-11 + AI Governance Lead | Change triggers software bill of materials re-emission + AI_Act documentation update |

**What's missing (PARTIAL):** uplift for D-07.4 under AI_Act Annex III change-control requirements (legacy target level 4)
**Gap**: 1 (change-control partly manual — full automation targeted)
**Notes**: D-07.4 is mostly achieved at level 3; some manual approval steps remain (planned automation to lift to level 4). AI-Act specific change-control for high-risk AI systems (Art. 16) is a unique requirement. Relevant Regulatory Baseline files: [D-07.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.1.md), [D-07.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.2.md), [D-07.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.3.md), [D-07.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.4.md).


**Corpus Target fit_criterion** (from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.manifest.json` + first applicable sub-domain JSON sidecar):

> A documented by-design architecture is maintained across the 5-layer by-design stack (GDPR controller-side data-protection by-design / NIS 2 entity-side NIS-lifecycle / CRA manufacturer-side product-lifecycle / DORA financial-entity-side infrastructure-management + change-mgmt + testing / AI_Act high-risk-AI-system-provider-side accuracy+robustness+cybersecurity + QMS) with one design-decision rec...

**Verification Method** (aggregated from `requirements.sub_requirements[].verification_method` across applicable sub-domains):

> INSPECT, TEST

### D-08 Human Factors — Implementation Status: IMPLEMENTED (backfilled from legacy level 3, target met)

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Security awareness | Annual formal programme for all 450 staff; quarterly phishing simulations; completion tracked in LMS | (LMS records; TRAIN records) | ISO 27001 A.7 + NIS 2 Art. 21(2)(g) + CRA Annex I Part I (8)(f) |
| Role-specific training | Developers: secure coding + AI-specific; SOC analysts: certified (SANS, GIAC); DPO: CIPP/E + GDPR refresher cadence; AI Governance Lead: AI_Act bootcamp | (LMS curriculum; certifications tracked) | EU AI_Act Art. 4 (AI literacy) for staff operating AI systems |
| Board training | **D-08.3 ACTIVE for SecureBorder under NIS 2** — quarterly cybersecurity briefings to Management Board + Non-Exec Directors; ISO 27001 governance committee | (governance records; board agenda minutes) | NIS 2 Art. 20 (Management bodies' cybersecurity training obligation) + DORA-style accountability |

**Target:** met (legacy level 3)
**Gap**: 0
**Notes**: All 3 sub-domains (D-08.1, D-08.2, D-08.3) are ACTIVE for SecureBorder (NIS 2 applies). D-08.3 is the key difference from Case 01 (where it was INACTIVE due to NIS 2 not applying). The board training is a NIS 2 Art. 20 obligation; quarterly briefings are recorded in board minutes. AI literacy (Art. 4 AI_Act) is integrated into general awareness. Relevant Regulatory Baseline files: [D-08.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.1.md), [D-08.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.2.md), [D-08.3 ACTIVE](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.3.md) — note: ACTIVE for SecureBorder (NIS 2-applicable).


**Corpus Target fit_criterion** (from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.manifest.json` + first applicable sub-domain JSON sidecar):

> A documented training programme is maintained with four distinct audience routes operating in parallel (DPO-catalysed processing-staff module per Art. 39(1)(b) when GDPR in scope; entity-wide basic-hygiene baseline per Art. 21(2)(g) when NIS 2 in scope; manufacturer-shipped Annex II §8(a)–(f) + 10-year support-period accessibility per Art. 13(18) when CRA in scope; financial-entity compulsory-modu...

**Verification Method** (aggregated from `requirements.sub_requirements[].verification_method` across applicable sub-domains):

> TEST

### D-09 Governance & Documentation — Implementation Status: IMPLEMENTED (backfilled from legacy level 3, target met)

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Security policies | ISO 27001 v4.7 policy set with full Annex A coverage + ISO 27701 privacy extension + AI-specific addendum; approved by Management Board | (paper artefact; policy index in intranet) | Integration of multiple regulatory requirements into single ISMS |
| Risk assessment | Annual ISO 27001 risk assessment + per-feature DPIA + FRIA + NIS 2 risk assessment + AI_Act risk management (Art. 9); unified risk register maintained | (paper artefact; risk register) | Multi-regulation unified assessment; tracked in Phase 2 strategic-tensions resolution |
| Asset inventories | CMDB with 100% asset coverage; auto-discovered monthly + manually reviewed quarterly; linked to ticket system for change control | (CMDB tool of record) | D-09.3 ACTIVE for SecureBorder (covers via NIS 2 + CRA + ISO 27001; the DORA-exclusive gap is bridged) |
| RoPA | GDPR RoPA maintained; AI_Act training-data lineage register; NIS 2 supply-chain register; risk register; DPO + AI Lead + CISO co-own | (paper artefact; tooling) | D-09.4 highly developed |

**Target:** met (legacy level 3)
**Gap**: 0
**Notes**: D-09 is the strongest domain for SecureBorder given ISO 27001 + ISO 27701 + NIS 2 + AI_Act governance requirements. The asset inventory (D-09.3) is a derived strong point — CMA coverage is at level 3 (not Optimised). Relevant Regulatory Baseline files: [D-09.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.1.md), [D-09.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.2.md), [D-09.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.3.md), [D-09.4](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.4.md).


**Corpus Target fit_criterion** (from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.manifest.json` + first applicable sub-domain JSON sidecar):

> A documented policy architecture is established covering all five participating policy artefacts (or the subset applicable to the entity) at the policy-evidence layer with the per-reg governance body as the policy-approval hook: GDPR controller-side data-protection policies with the DPO (designated individual with Art. 39(1) tasks reporting to the management body but not a member per Art. 38(6) co...

**Verification Method** (aggregated from `requirements.sub_requirements[].verification_method` across applicable sub-domains):

> TEST

### D-10 Monitoring & Audit — Implementation Status: IMPLEMENTED (backfilled from legacy level 3, target met)

| Control | Current | Evidence | Notes |
|---|---|---|---|
| Continuous monitoring | centralised log aggregation platform ES Security Information and Event Management (24/7, 13 analysts); endpoint detection and response platform endpoint detection and response platform + Nessus scanner; managed vulnerability intelligence feed; AI-system adversarial monitoring (cutting-edge) | SYS-12 in `04a §1.1`; STORE-04 in `04a §2.1` | Includes AI_Act post-market monitoring (Art. 72) overlay |
| Audit logging | Tamper-evident WORM with cryptographic hash chain; 10-year retention; immutable across legal hold | SYS-09 + STORE-04 in `04a §1.1` + `04a §2.1` | hardware cryptographic module-signed audit entries; chain anchored via SYS-07 |
| Compliance testing | Annual ISO 27001 surveillance audit + annual third-party assurance attestation Type II (Cloud) + AI_Act conformity assessment (in progress per `05 §6.7`) | (paper + tool artefacts) | CRA notified-body assessment scheduled 2026-Q4 |

**What's missing (PARTIAL):** uplift for D-10.2 audit logging given cryptographic hash chain (legacy target level 4)
**Gap**: 1 (continuous-monitoring AI-system anomaly detection — improving)
**Notes**: D-10.2 achieves level 4 by being cryptographically hash-chained and hardware cryptographic module-signed (tamper-evident). D-10.1 is improving toward level 4 with the AI-system adversarial monitoring (a unique Annex III requirement). Relevant Regulatory Baseline files: [D-10.1](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.1.md), [D-10.2](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.2.md), [D-10.3](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.3.md).


**Corpus Target fit_criterion** (from `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.manifest.json` + first applicable sub-domain JSON sidecar):

> A layered 5-monitoring-architecture is established with explicit scope-layer hand-offs at the monitoring-evidence layer: (1) **GDPR Art. 32(1)(b) + Art. 32(1)(d) + Art. 32(2) + Art. 33(1)** — entity-level monitoring of personal-data processing systems for the 5 Art. 32(2) risk types (accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data) + Art...

**Verification Method** (aggregated from `requirements.sub_requirements[].verification_method` across applicable sub-domains):

> TEST

## 3. Summary Dashboard

| Macro-domain | Current | Target | Gap |
|---|---:|---:|---:|
| D-01 Data Protection | 3 | 3 (4 for D-01.4) | 0 |
| D-02 Vulnerability Management | 3 | 3 | 0 |
| D-03 Access Control | 3 | 4 (for D-03.3) | 1 |
| D-04 Incident Response | 3 | 3 | 0 |
| D-05 Data Lifecycle | 3 | 3 (4 for D-05.1) | 0 |
| D-06 Supply Chain | 3 | 3 | 0 |
| D-07 Secure Development | 3 | 4 (for D-07.4) | 1 |
| D-08 Human Factors | 3 | 3 | 0 |
| D-09 Governance & Documentation | 3 | 3 | 0 |
| D-10 Monitoring & Audit | 3 | 4 (for D-10.2) | 1 |
| **OVERALL** | **3.0** | **3.3** | **0.3** |

## 4. Top Gaps (feeds Doc 07)

| Rank | Macro-domain | Gap | Gap Summary | Priority Remediation |
|---:|---|---:|---|---|
| 1 | D-07 Secure Development | 1 | D-07.4 change-control partial manual; AI_Act Art. 16 change-control for high-risk AI demands full automation | Automate change-control workflow with AI-governance approval gates; lift to target 4 by Q4 |
| 2 | D-10 Monitoring & Audit | 1 | D-10.1 AI-system adversarial monitoring improvement; post-market monitoring system not yet complete (AI_Act Art. 72) | Complete post-market monitoring implementation; integrate AI anomaly detection into SOC |
| 3 | D-03 Access Control | 1 | D-03.3 PAM tool procurement pending — currently at level 3 with manual + JIT controls | Evaluate CyberArk vs. alternative PAM; target procurement Q1 2027 |
| 4 | D-04 Incident Response (overlay gap) | — | AI_Act 3-tier reporting (Art. 73) requires additional SOC playbook updates | Add 3-tier reporting playbook (15d default / 2d widespread / 10d death); tabletop Q3 |
| 5 | D-09 Governance (active gap) | — | CRA notified-body conformity assessment scheduled 2026-Q4; AI_Act conformity assessment in progress; FRIA integrated with DPIA but pending board-level sign-off | Schedule management-board conformity approval Q4; finalise AI_Act conformity assessment documentation |

## 5. Consistency Check

| Consistency Item | Status | Evidence |
|---|---|---|
| Architecture evidence matches 04a | PASS | SYS-01..SYS-13, STORE-01..STORE-07, FLOW-01..FLOW-12 referenced consistently |
| Regulatory scope matches Doc 04 and Doc 05 | PASS | `applicable_regs = [GDPR, CRA, NIS2, AI_Act]`; 38 active SubDomains; D-08.3 ACTIVE (NIS 2) |
| HIGH-tier proportionality maintained | PASS | No over-engineering (hardware cryptographic module + Security Information and Event Management + EDR are the minimum for Critical Class + 4-regulation overlap); no under-engineering (CRA notified-body assessment in progress) |
| Legacy scale used consistently | PASS | Historical check — values were integers 0-4; target and gap shown numerically |
| Evidence and gaps align | PASS | D-03, D-07, D-10 are top gaps (operationally); D-09 + D-02 are strongest |
| D-08.3 ACTIVE flagged correctly | PASS | D-08.3 participation: [NIS2, DORA]; applicable_regs includes NIS 2 → ACTIVE. In Case 01 (LOW-tier, no NIS 2) D-08.3 was INACTIVE — the difference is the NIS 2 applicability, not the methodology |

## 6. Corpus Provenance

Each macro-domain in §2 carries a **Corpus Target fit_criterion** and **Verification Method** block lifted from the per-sub-domain JSON sidecar in the corpus. These blocks ground SecureBorder's posture notes in the frozen Volere fit_criteria aggregated across Case_02's four applicable regulations (GDPR + CRA + NIS 2 + AI_Act), and document how each target profile is verified.

### 6.1 Per-macro-domain corpus linkage

| Macro-domain | Active sub-domains | NIST CSF anchors (Case_02) | First-fit_criterion source sub-domain |
|---|---:|---|---|
| D-01 (D-01 Data Protection & Encryption) | 4 | PR.DS-01, PR.DS-10, GV.RM-04, PR.DS-02, PR.IR-01, PR.IR-03, GV.OV-01, PR.AA-05, … | D-01.1 |
| D-02 (D-02 Vulnerability Management) | 4 | ID.IM-02, ID.RA-01, ID.RA-05, PR.PS-02, PR.PS-02; ID.RA-05, ID.AM-02, GV.SC-04, … | D-02.1 |
| D-03 (D-03 Access Control) | 4 | PR.AA-02, PR.AA-03, PR.DS-12, DE.CM-09, ID.AM-01, PR.AA-01, PR.AA-05, PR.AA-06, … | D-03.1 |
| D-04 (D-04 Incident Response) | 4 | DE.AE-02, DE.CM-01, DE.CM-09, PR.PS-04, RS.MA-02, RS.MA-01, PR.DS-01, PR.DS-12, … | D-04.1 |
| D-05 (D-05 Data Lifecycle) | 4 | GV.OC-03, GV.PO-01, ID.AM-03, PR.DS-12, PR.DS-01, PR.PS-06, GV.OC-04, GV.OV-02, … | D-05.1 |
| D-06 (D-06 Supply Chain) | 4 | GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, GV.SC-01, ID.RA-02, GV.OC-03, ID.RA-01, … | D-06.1 |
| D-07 (D-07 Secure Development) | 2 | PR.DS-12, PR.PS-06, PR.PS-01, PR.PS-02, ID.RA-01, GV.OV-01, GV.OV-02, GV.PO-02, … | D-07.1 |
| D-08 (D-08 Human Factors) | 3 | PR.AT-01, PR.AT-02, PR.PS-01, GV.SC-03, PR.AT-04, GV.RR-01, GV.RR-02, GV.RR-04, … | D-08.1 |
| D-09 (D-09 Governance & Documentation) | 3 | GV.OV-03, GV.PO-01, GV.PO-01 (primary), GV.PO-02, GV.RM-04, GV.RR-01, GV.RR-02, … | D-09.1 |
| D-10 (D-10 Monitoring Audit) | 3 | DE.AE-02, DE.CM-01, DE.CM-01 (primary), DE.CM-09, ID.IM-04, DE.CM-09 (primary), … | D-10.1 |

Corpus source: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` — each macro-domain has a `<MD_ID>.manifest.json` aggregating per-sub-domain manifest data, and each sub-domain has a `<SD_ID>.json` sidecar with Volere `fit_criterion` + `verification_method` arrays.

---
## 7. Gate

| Gate Criterion | Status | Evidence |
|---|---|---|
| All 10 macro-domains assessed with legacy posture level and evidence | PASS | Section 2 |
| Target profile defined per macro-domain | PASS | Sections 2 and 3 |
| Summary dashboard populated | PASS | Section 3 |
| Top 5 gaps identified | PASS | Section 4 |
| SubDomains references included | PASS | Each macro-domain section links to all 38 active Regulatory Baseline files |
| D-08.3 ACTIVE flagged (NIS 2-applicable) | PASS | D-08.3 section §2 + consistency check §5 |

## N. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-07-11 | Executor | Created SecureBorder populated security posture assessment from the 04b template; HIGH-tier posture averaging legacy level 3.0 (vs TinyTask's 1.3), with D-08.3 ACTIVE (NIS 2-applicable). |
| 1.1 | 2026-08-06 | Executor | Sprint 1 reconciliation: frontmatter → AEGIS-P2-RICH-*, status: DRAFT → RECONCILED, active_subdomains 38 → 35, applicable_regs aligned. Body preserved verbatim. |
| 1.2 | 2026-08-06 | Executor | Sprint 2 corpus enrichment: §2 per-macro-domain (D-01..D-10) gains Corpus Target fit_criterion + Verification Method blocks (10 macro-domains); new §6 Corpus Provenance with per-macro-domain linkage table. Source: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`. |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-07-11 |
| Technical Review | CTO |  |  |
| Security Review | CISO |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Data backbone:** `Case_02_Phase1.xlsx` (13 sheets: COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, MATURITY (legacy sheet name), SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES)
- **Architecture context:** `Doc04_Architecture_DataInventory.md` §1.1 (13 systems), §2.1 (7 stores), §2.2 (12 flows).
- **People/RACI:** `Doc07_Org_Roles_RACI.md` (15-25 staff, dedicated CISO + DPO + AI Governance Lead + SOC Manager + Compliance Analyst roles).
- **HIGH-tier context:** `../../02_CASES/Case_02_SecureBorder_Solutions/00_COMMON/01_Company_Context.md` (4 applicable regulations, complexity tier HIGH).
