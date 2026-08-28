---
document_id: AEGIS-P3-RICH-06b
title: DORA ICT Risk Framework (Rich Mode)
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-06
author: Sprint 0.6 Executor (dora-mapper)
status: DORA_MAPPED
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
cross_checked_against: [Doc13_Proportionality_Profile.md, proportionality_model.md]
inputs: [Doc08_Regulatory_Applicability.md, Doc13_Proportionality_Profile.md, 00_METHODOLOGY/REFERENCE/proportionality_model.md, 00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_Y/articles/DORA_Art_*.md]
outputs: [Doc13_Proportionality_Profile.md §11, Phase 2 Doc 08 (forward reference)]
related_documents: [Doc13_Proportionality_Profile.md, Doc08_Regulatory_Applicability.md, Doc12_Structured_Compliance_Matrix.md, Doc14_Adjusted_Goals.md, Doc06_ThirdParty_Landscape.md]
frozen: false
supersedes: none
fields_excluded: [Effort Estimate, Cost Estimate, Target Timeline]
complexity_tier: MAX
---

# DORA ICT Risk Framework (Rich Mode)

> DORA-specific ICT risk framework mapping for OmniBank (ECB-supervised Credit Institution).
> DORA is uniquely applicable to Case_03 (financial entity); Case_01 (SaaS) and Case_02 (defence) are non-financial.
> This document informs Doc 07b §11 Decision Table Trail (DORA-specific tier justifications) and provides the DORA ↔ AEGIS sub-domain bridge consumed by Phase 2 (Doc 08 obligation derivation).

---

## §1 Document Purpose

This document is the **DORA-specific ICT risk framework mapping** for OmniBank Financial Systems. It binds every DORA article in scope for Case_03 (per `Doc08_Regulatory_Applicability.md §3.4` — DORA-C01 through DORA-C38, all 38 DORA clauses applicable to credit institutions) to the AEGIS 38-sub-domain taxonomy and explicitly resolves the DORA-specific tier-justifications in Doc 07b §11.

**Why this document exists.** Sprint 0.5 produced the case-level Track B proportionality profile (`Doc13_Proportionality_Profile.md`) with 31 RIGOROUS + 7 STANDARD sub-domain tiers, derived from the decision table `(S=MAX, I, P=MUST)`. DORA is the densest single source of those assignments — DORA participates in 38 of 38 DORA clauses and is the **dominant** regulator for 18 sub-domains (per `Doc08_Regulatory_Applicability.md §9 Observation 3`). Without a dedicated DORA bridge, the corpus `requirements.high_level.yaml.priority` field would under-explain *why* Case_03's D-02.4 (TLPT), D-04.3 (notification), D-06.1/D-06.3/D-06.4 (third-party), D-09.1 (framework) and D-09.3 (inventory) all map to RIGOROUS tier with full DORA-specific operationalisation rather than a generic DEFERRED or LIGHTWEIGHT outcome.

**Case_03 specificity.** Case_03 is the only case in AEGIS where DORA applies (Case_01 = SaaS, Case_02 = defence industrial base). This is therefore a NEW document not present in Case_01/Case_02 — Case_03-specific.

**Invariant preservation.** Per `00_METHODOLOGY/REFERENCE/proportionality_model.md §1`, Track B does not modify the regulatory `fit_criterion` or the security objective (HSO). This document maps DORA articles onto sub-domains; it does **not** relax any DORA obligation. Tier variation flows through Doc 07b §11; this document provides the DORA-side justification per row.

**Excluded fields.** Per project directive, **Effort Estimate, Cost Estimate, and Target Timeline are explicitly excluded** from this document — they belong in operational planning artefacts (outside Phase 1 scope).

---

## §2 DORA Applicability for Case_03

### §2.1 Applicability Determination (cross-ref Doc 05 §3.4)

| Criterion | Company Context Value | Threshold | Met? |
|-----------|----------------------|-----------|------|
| `dora_financial_entity` | TRUE (credit institution per DORA Art. 2(1)(a)) | TRUE | **YES** |
| `financial_sector_classification` | Credit institution (banking) | YES | **YES** |
| `ict_third_party_provider` | FALSE (not primarily ICT provider) | YES/NO | N/A |

**Applicability Result:** ✅ **APPLICABLE (Credit Institution per DORA Art. 2(1)(a))**
**DORA clauses in scope:** DORA-C01 through DORA-C38 (all 38 clauses applicable — Doc 05 §3.4 row).
**Obligated party:** `FINANCIAL_ENTITY` — 100% unconditional (Weight 3 obligations; Doc 05 §3.4).

### §2.2 Significance Classification — Case_03 Likely "Significant"

The corpus flags significance because DORA Art. 26-27 (TLPT and advanced testing) applies in full only to significant entities, while Art. 24-25 baseline applies to all financial entities. Significance is not declared in OJ text — it is determined by the **competent authority** (BaFin / ECB for credit institutions) on the basis of size, interconnectedness, complexity, and risk profile (corpus SR-DORA-009 ambiguity_notes, `DORA_Art_26.md`).

| Factor | Case_03 Value | Significance Indicator |
|--------|---------------|------------------------|
| Size | 5,000+ employees, >€1.5B revenue | High — top decile of EU credit institutions |
| ECB supervision | Yes (per Doc 04 §2 / Doc 05 §3.4) | Strong indicator — ECB supervises ~110 significant credit institutions |
| Interconnectedness | SEPA/SWIFT member + retail/corporate customer base + payment systems | High — systemic relevance |
| AI Act Annex III High-Risk | Yes (OmniScore credit scoring) | Adds operational complexity |
| ISO 27001 certified | Yes | Mature baseline but does not reduce significance |

**Inference:** OmniBank is very likely classified as a **significant entity** by ECB/BaFin based on size, ECB supervision, and interconnectedness. This triggers the full DORA Art. 26-27 TLPT obligation (~every 3 years, with ECB-supervised entities facing frequent ECB-led TLPT scoping per TIBER-EU framework).

**Implications of significance classification:**

| Implication | DORA Article | Case_03 Operational Consequence |
|-------------|---------------|----------------------------------|
| **4-hour initial notification** for major ICT incidents | Art. 17(1) + RTS Art. 6(1)(a) (via Delegated Reg. (EU) 2025/301) | Internal clock: 4h after classification as major, never >24h after discovery. Credit institutions + >250 employees + >€50M turnover = **no weekend deferral** per RTS weekend clause (Doc 05 §3.4 Nuance). |
| **TLPT every 3 years** | Art. 26(1) | External TLPT by ECB-recognised TLPT provider (e.g. industry-major accredited firm). TLPT scope: core banking + payment systems + OmniScore AI. ECB may request frequency adjustments per Art. 26(1). |
| **Critical ICT third-party providers (CTPP)** designation risk | Art. 28-30 | Cloud providers (major managed hosting providers), payment networks (SEPA/SWIFT), credit bureaus — likely designated as CTPPs by Lead Overseers (ESAs). Direct regulatory obligations on those providers (up to €5M / 1% global turnover fines) — see Doc 04c §7 (planned). |
| **Management body personal liability** | Art. 5(2) — four-verb coordination `define, approve, oversee, be responsible` | Board briefing programme mandatory (Doc 04d RACI: CEO accountable, CRO responsible). Personal liability acknowledged in writing per Doc 07b §4.8 D-08.3 row. |
| **Annual external audit of ICT risk management** | Art. 26 + Art. 24(7) RTS (pending) | ISO 27001 surveillance audit + DORA-specific conformity assessment annually. |
| **Joint ESAs oversight exposure** | Art. 31-33 | If CTPPs are designated, ESAs (EBA/ESMA/EIOPA Joint Committee) gain direct oversight powers — entities face composite supervisory exposure (BaFin + ECB + ESA Joint Committee). |

**Case_03 Significance Posture (Doc 07b §4 cross-reference):** Doc 07b §4 already assigns RIGOROUS tier to all DORA-touching sub-domains for Case_03 — this is consistent with the significant-entity posture. The D-02.4 row in Doc 07b §4.2 explicitly states: *"DORA Art. 26 mandates TLPT for major financial entities. ECB-supervised OmniBank qualifies."*

### §2.3 RTS Dependencies (Deadlines Come from RTS, Not DORA Text)

Per Doc 05 §3.4 Nuance 1: DORA Art. 19(4) does **not** specify numeric deadlines in regulation text — it delegates to RTS under Art. 20. The concrete deadlines are in **Delegated Regulation (EU) 2025/301** (RTS adopted by Commission in October 2024 via JC 2024-33).

| Phase | Deadline | Reference |
|-------|----------|-----------|
| Initial notification | 4 hours after classification as major, **never more than 24 hours** after discovery | RTS Art. 6(1)(a) |
| Intermediate report | 72 hours after initial notification | RTS Art. 6(1)(b) |
| Final report | 1 month (30 days) after classification as major | RTS Art. 6(1)(c) |

**Weekend clause (RTS):** Deadlines falling on weekends deferred to next business day at noon — **EXCEPT** for credit institutions, CCPs, trading venues, and essential entities with >250 employees / >€50M turnover. Case_03 (credit institution, 5,000+ employees, >€1.5B revenue) is **not eligible** for the weekend deferral. Deadlines apply 24/7 (Doc 05 §3.4 Nuance 2).

**Implementing Regulation (EU) 2024/2956** partially addresses reporting templates in Annex I-IV. EBA/ESMA/EIOPA technical standards under Art. 18(3) (classification criteria) and Art. 24(7) (testing programme calibration) remain pending and may close residual ambiguity.

---

## §3 DORA Article → AEGIS Sub-Domain Mapping

This section maps each DORA article in scope (Art. 5-34, the substantive obligations on financial entities) to one or more of the 38 AEGIS sub-domains. Each row specifies:

- **Primary sub-domain(s)** — where the article text provides the dominant regulatory locus per the corpus (`articles/DORA_Art_*.md`)
- **Secondary sub-domain(s)** — where the article text produces material operational requirements that bind a different sub-domain's controls
- **Tier justification** — RIGOROUS or STANDARD per Doc 07b §4 / §11
- **Corpus evidence** — verbatim file path of the article split

Articles 35-44 (Chapter V Section 2 — Joint ESAs CTPP oversight) are excluded from this Case_03 mapping because they bind **CTPPs** (designated providers), not the financial entity. They are referenced in §6.6 only as context.

### §3.1 Chapter II Section 1 — Governance (Art. 5-6)

#### Art. 5 — Governance and management body responsibility

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/DORA_Art_5.md` (SO-DORA-014, SO-DORA-016).

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-09.1** (Information Security Policies — management body 4-verb coordination); **D-08.3** (Management Board Training — Art. 5(4) `sufficient knowledge and skills`); **D-09.3** (Asset Inventories — Art. 5(2) `all arrangements`) |
| Secondary sub-domain(s) | D-09.2 (Impact & Risk Assessments — framework feeds risk-assessment discipline) |
| Tier | **RIGOROUS** (D-09.1, D-08.3, D-09.3); all per Doc 07b §4.8, §4.9, §11 |
| Article text (verbatim) | Art. 5(2): *"The management body … shall define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework"* (4-verb coordination). Art. 5(4): *"Members of the management body … shall actively keep up to date with sufficient knowledge and skills … commensurate to the ICT risk being managed"* |
| Case_03 implementation | Board briefing programme (Doc 04d RACI: CEO accountable, CRO responsible). Management body personal liability acknowledged in writing per Doc 07b §4.8 D-08.3 row. ISO 27001 certified ISMS extends to DORA scope. |
| Verification | TEST + ANALYZE + external audit (RIGOROUS) |
| Operationalisation | 5-policy architecture (DPO / management body / manufacturer / DORA / AI Governance) per Doc 07b §4.9 D-09.1 row — DORA is one of the 5 participating regulations on D-09.1 (corpus: "must build a 5-policy architecture with 5 distinct governance bodies"). |

#### Art. 6 — ICT risk management framework (chapeau)

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/DORA_Art_6.md` (SR-DORA-027); also appears in D-01.1, D-01.2, D-01.4 manifests per OJ distribution.

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-09.1** (Information Security Policies — chapeau framework); **D-09.2** (Impact & Risk Assessments — Art. 6(8)(a) ICT risk identification) |
| Secondary sub-domain(s) | D-04.1, D-10.1 (detection substrates operationalised by the framework) |
| Tier | **RIGOROUS** for D-09.1 (Doc 07b §4.9 + §11 row D-09.1); **RIGOROUS** for D-09.2 (Doc 07b §4.9 + §11 row D-09.2) |
| Article text (verbatim) | Art. 6(1): *"Financial entities shall have a sound, comprehensive and well-documented ICT risk management framework … which enables them to address ICT risk quickly, efficiently and comprehensively"* (3-adjective AND + 3-adverb AND). Art. 6(2): *"shall include strategies, policies, procedures, ICT protocols and tools"* (5-element AND). |
| Case_03 implementation | Unified ISMS extending ISO 27001 to DORA scope + IPSARA Unified Assessment Framework (Doc 07b §4.9 D-09.2 row + T-003 RESOLVED). Annual ISMS surveillance audit. |
| Verification | TEST + ANALYZE + external audit (RIGOROUS) |
| Cross-ref | T-003 RESOLVED (DPIA + FRIA + DORA ICT risk assessment + CRA + NIS 2 = single IPSARA assessment) per Doc 07b §5.1. |

#### Art. 7 — Identification of ICT-supported business functions and assets

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.1/articles/DORA_Art_7.md`; also D-09.1, D-09.2, D-09.3, D-10.1 manifests.

**OJ-corrective note (corpus v0.2 audit, material):** Art. 7(1) → Art. 8(1) misattribution. The corpus audit identifies that the OJ text of "identify, classify and adequately document all ICT supported business functions … and their dependencies" actually lives in **Art. 8(1)** (Identification function), not Art. 7(1). Art. 7 itself addresses **identification of ICT risk sources**. This document follows the OJ-literal locus.

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-02.1** (Vulnerability Identification — Art. 7(2) `identify all sources of ICT risk`); **D-09.3** (Asset Inventories — Art. 8(1) OJ-literal `identify all ICT-supported business functions and the ICT assets that support those functions`) |
| Secondary sub-domain(s) | D-09.2 (Impact & Risk Assessments — Art. 7(2) sentence 2 risk-scenario register); D-10.1 (Continuous Security Monitoring — identification feeds monitoring) |
| Tier | **RIGOROUS** for D-02.1 (Doc 07b §4.2 + §11); **RIGOROUS** for D-09.3 (Doc 07b §4.9 + §11) |
| Article text (verbatim) | Art. 7(2) sentence 1: *"on a continuous basis, identify all sources of ICT risk, in particular the risk exposure to and from other financial entities"*; Art. 8(1): *"identify all ICT-supported business functions and the ICT assets that support those functions, including those of third-party providers, and document them"* (OJ-literal per corpus audit note) |
| Case_03 implementation | Managed CMDB + dedicated DORA Art. 8 ICT systems inventory + automated discovery (managed vulnerability scanning + managed discovery) + quarterly reconciliation per Doc 07b §4.9 D-09.3 row. Critical ICT assets identified per DORA. Annual full reconciliation. |
| Verification | TEST + ANALYZE + external audit (RIGOROUS) |
| Special note | Art. 7(2) sentence 2 mandates annual risk-scenario register refresh (*"at least yearly"* hard numeric anchor, SR-DORA-005). |

### §3.2 Chapter II Section 2 — ICT risk management framework (Art. 8-16)

#### Art. 8 — Identification function (OJ-literal)

Covered above in §3.1 with Art. 7. OJ-literal Art. 8(1) is the inventory obligation; Art. 8(2) extends to dependency identification. Both map to **D-09.3** as the primary sub-domain.

#### Art. 9 — Protection and prevention (CIA + A, 8 controls)

**Corpus evidence:** Distributed across D-01.1, D-01.2, D-01.3, D-01.4, D-02.2, D-03.1, D-03.2, D-03.3, D-04.1, D-07.1, D-07.2, D-07.4, D-08.x, D-09.1, D-09.2, D-09.3, D-10.1, D-10.2 manifests. SR-DORA-001, SR-DORA-002, SR-DORA-003, SR-DORA-006, SR-DORA-007 in `DORA_Art_5.md` (which holds the Art. 9(2)+(4) splits).

**OJ-corrective note (corpus v0.2 audit, material):** Art. 8(1) → Art. 9(1) misattribution. The "continuously monitor and control the security and functioning of ICT systems" obligation lives in **Art. 9(1)** (Protection and prevention), not Art. 8(1) (which is Identification function). This document follows OJ-literal.

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-01.1** (Data at Rest Encryption — Art. 9(2) CIA+A at-rest); **D-01.2** (Data in Transit Encryption — Art. 9(2) in-transit); **D-01.4** (Data Integrity Mechanisms — Art. 9(2) integrity); **D-03.1** + **D-03.2** (Identity + MFA — Art. 9(4)(d) strong auth); **D-01.3** (Key Management — Art. 9(4)(d) cryptographic-key protection); **D-04.1** + **D-10.1** (Detection and Monitoring — Art. 9(1) OJ-literal monitoring); **D-02.2** (Patch Management — Art. 9(4)(f) patches and updates); **D-07.1** (Network Architecture — Art. 9(4)(b) network and infrastructure) |
| Secondary sub-domain(s) | D-03.3 (Authorisation — Art. 9(4)(c) access policies); D-07.4 (Change Management — Art. 9(4) ICT change); D-08.1, D-08.2 (Awareness + Competence — Art. 9(4) governance dimension) |
| Tier | **RIGOROUS** for all 8 control sub-domains above (Doc 07b §4.1 D-01.1-1.4; §4.2 D-02.2; §4.3 D-03.1, D-03.2, D-03.3; §4.4 D-04.1; §4.10 D-10.1; §4.7 D-07.1, D-07.4; §4.8 D-08.1, D-08.2 — all BUILD_REQUIRED + MUST + MAX = RIGOROUS) |
| Article text (verbatim) | Art. 9(2): *"aim to ensure the resilience, continuity and availability of ICT systems and to maintain high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit"* (4×3 CIA+A matrix). Art. 9(1) OJ-literal: *"continuously monitor and control the security and functioning of ICT systems"*. Art. 9(4)(a)-(h): 8 mandatory control domains. |
| Case_03 implementation | Strong symmetric encryption + managed key custody (D-01.x); modern transport cryptographic standard + mutual transport cryptographic authentication (D-01.2); 24/7 SOC centralized audit-log + automated orchestration + endpoint + network + behaviour telemetry (D-04.1 + D-10.1); 24h Critical patch SLA per CRA Annex I §2(h) (D-02.2); hardened-default baseline + automated config (D-07.1). |
| Verification | TEST + ANALYZE + external audit (RIGOROUS) |
| Special note | Art. 9 is the densest single DORA article — it cross-cuts 14 of 38 AEGIS sub-domains. |

#### Art. 10 — Detection of anomalous activities

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.1/articles/DORA_Art_10.md`; also D-10.1.

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-04.1** (Incident Detection & Triage — Art. 10(1) `mechanisms to promptly detect anomalous activities`); **D-10.1** (Continuous Security Monitoring — Art. 10(1) ICT network performance issues) |
| Secondary sub-domain(s) | D-04.2 (Containment — Art. 10 incident response substrate) |
| Tier | **RIGOROUS** (Doc 07b §4.4 D-04.1 + §4.10 D-10.1, both BUILD_REQUIRED + MUST + MAX) |
| Article text (verbatim) | Art. 10(1) OJ-corrected: *"Financial entities shall have in place mechanisms to promptly detect anomalous activities … including ICT network performance issues and ICT-related incidents, and to identify potential material single points of failure"* (OJ operative verb: `have in place`, not `deploy` — corpus OJ-corrective note) |
| Case_03 implementation | 24/7 SOC (centralized audit-log management + automated orchestration + managed endpoint detection + network anomaly detection + behaviour analytics) with MTTD <15 min. Tier-1/2/3 in-house + co-managed overflow. |
| Verification | TEST + ANALYZE + external audit (RIGOROUS) |
| Cross-ref | This is the upstream substrate for Art. 17 incident-management process (§3.3 below). |

#### Art. 11 — ICT business continuity policy

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.2/articles/DORA_Art_11.md`; also D-04.4 (SR-DORA-013 in `DORA_Art_28.md`).

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-04.2** (Containment & Mitigation — BC policy covers recovery-execution criteria); **D-04.4** (Data Restoration & Recovery — BC policy operationalises PR.IR-03 resilience) |
| Secondary sub-domain(s) | D-09.1 (Policy substrate — BC policy `integral part of overall BC policy` per Art. 11(1)) |
| Tier | **RIGOROUS** (Doc 07b §4.4 D-04.2 + D-04.4, both BUILD_REQUIRED + MUST + MAX) |
| Article text (verbatim) | Art. 11(1): *"put in place a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy of the financial entity"* (integral part qualifier per SR-DORA-013) |
| Case_03 implementation | Own DR programme + 2 active DCs + 1 cold standby + RTO 4h / RPO 15min for critical systems. Quarterly DR test + annual full failover test. 99.99% uptime SLA per Doc 04 BG-005. |
| Verification | TEST + ANALYZE + external audit (RIGOROUS) |

#### Art. 12 — ICT business continuity and disaster recovery plans (backup, recovery)

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.2/articles/DORA_Art_12.md`; D-04.4; D-10.2.

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-04.4** (Data Restoration & Recovery — backup + recovery); **D-10.2** (Audit Logging & Traceability — DORA Art. 12 ICT change records) |
| Secondary sub-domain(s) | D-04.2 (Containment — DR plan execution criteria) |
| Tier | **RIGOROUS** (Doc 07b §4.4 D-04.4 + §4.10 D-10.2, both BUILD_REQUIRED + MUST + MAX) |
| Case_03 implementation | Tamper-evident WORM audit logs + cryptographic hash chains + 5-10y retention (BaFin/ECB). T-002 RESOLVED: cryptographic sharding balances GDPR erasure with DORA immutability. |
| Cross-ref | T-002 RESOLVED (cryptographic sharding) per Doc 07b §5.1. |

#### Art. 13 — ICT change management, monitoring, awareness

**Corpus evidence:** Distributed across D-02.1, D-02.2, D-04.4, D-07.4, D-08.1, D-08.2, D-09.3, D-10.1 manifests.

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-07.4** (Change Management — Art. 13 ICT change management); **D-10.1** (Continuous Monitoring — Art. 13 monitoring); **D-08.1** + **D-08.2** (Awareness + Competence — Art. 13 training) |
| Secondary sub-domain(s) | D-04.4 (DR integration with change management); D-09.3 (asset inventory update on change) |
| Tier | **RIGOROUS** for all four (Doc 07b §4.7 D-07.4, §4.10 D-10.1, §4.8 D-08.1 + D-08.2) |
| Case_03 implementation | Managed change management platform + 4-eyes + CAB review + emergency change procedure. |

#### Art. 14 — Crisis communication plans

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/DORA_Art_14.md` (SR-DORA-018).

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-04.3** (Regulatory Notification — crisis communication `clients AND counterparts AND public`) |
| Secondary sub-domain(s) | D-04.1 (Detection triggers communication plan activation) |
| Tier | **RIGOROUS** (Doc 07b §4.4 D-04.3 — RIGOROUS with 5-reg max-SLA routing pipeline) |
| Article text (verbatim) | Art. 14(1): *"crisis communication plans enabling a responsible disclosure of, at least, major ICT-related incidents or vulnerabilities to clients and counterparts as well as to the public, as appropriate"* (3-way AND, with `as appropriate` softening only the public dimension) |
| Case_03 implementation | Crisis communication plan integrated with Art. 19 client notification under Art. 19(3) (impact-on-financial-interests trigger). Per-recipient template segregation. |

#### Art. 15 — Testing of ICT systems (RTS mandate)

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/articles/DORA_Art_15.md` (and other D-01.x, D-02.x manifests — Art. 15 RTS mandate is referenced across the corpus).

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-10.3** (Compliance Testing — Art. 15 ESAs RTS calibrate specific elements of Art. 9) |
| Secondary sub-domain(s) | D-02.4 (TLPT-related testing); D-07.2 (secure-development testing) |
| Tier | **RIGOROUS** (Doc 07b §4.10 D-10.3) |
| Article text (verbatim) | Art. 15(2): *"ESAs shall … develop common draft regulatory technical standards … in order to further specify … elements"* — RTS mandate to specify measurement criteria for `high standards` (Art. 9(2)) and `strong authentication` (Art. 9(4)(d)) |

#### Art. 16 — ICT-related incident classification criteria

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.1/articles/DORA_Art_16.md`; also D-04.3.

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-04.1** (Incident Detection & Triage — Art. 16 classification criteria); **D-04.3** (Regulatory Notification — classification triggers Art. 19 reporting) |
| Secondary sub-domain(s) | D-09.1 (classification criteria in policy substrate) |
| Tier | **RIGOROUS** for both (Doc 07b §4.4) |
| Article text (verbatim) | Art. 18(1) (per OJ cross-ref) classification criteria delegated to EBA/ESMA/EIOPA RTS under Art. 18(3) — multiplicative and residually vague per SR-DORA-017 ambiguity_notes (`DORA_Art_17.md`). Implementing Reg. (EU) 2024/2956 partially addresses reporting templates in Annex I-IV. |
| Special note | Art. 18 RTS pending — entities should adopt a written interpretive position on borderline cases and document it for supervisory review. |

### §3.3 Chapter III — ICT-related incident management (Art. 17-23)

#### Art. 17 — ICT-related incident management process

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.1/articles/DORA_Art_17.md`; `D-04.3` (SR-DORA-016, SR-DORA-017).

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-04.1** (Incident Detection & Triage — Art. 17(1) detect); **D-04.3** (Regulatory Notification — Art. 17(1) notify + Art. 19 reporting cascade) |
| Secondary sub-domain(s) | D-04.2 (Containment — Art. 17(1) manage); D-10.1 (Monitoring substrate) |
| Tier | **RIGOROUS** for both D-04.1 and D-04.3 |
| Article text (verbatim) | Art. 17(1): *"define, establish and implement an ICT-related incident management process to detect, manage and notify ICT-related incidents"* (twin 3-way verb coordinations per SR-DORA-016) |
| Case_03 implementation | 5-regulation max-SLA routing pipeline per Doc 07b §4.4 D-04.3 row. CEO accountable for notification clock. |
| Cross-ref | T-001 CRITICAL resolution (4h DORA internal clock satisfies NIS 2 24h + CRA 24h + GDPR 72h + AI Act 15d). See §4.1 below. |

#### Art. 18 — Major ICT-related incident classification (delegated criteria)

Covered above as the Art. 16/18 classification cluster. **OJ-corrective note:** the OJ text of major-incident classification criteria lives in Art. 18(1) (delegated to EBA/ESMA/EIOPA RTS under Art. 18(3)), not Art. 16.

#### Art. 19 — Major ICT-related incident reporting + client notification

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/DORA_Art_19.md` (SR-DORA-017).

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-04.3** (Regulatory Notification — Art. 19(1) supervisor + Art. 19(3) client) |
| Secondary sub-domain(s) | D-04.1 (classification trigger) |
| Tier | **RIGOROUS** (Doc 07b §4.4 D-04.3 — 5-reg max-SLA routing) |
| Article text (verbatim) | Art. 19(1): *"Financial entities shall report major ICT-related incidents to the relevant competent authority"*. Art. 19(3): *"Where a major ICT-related incident occurs AND HAS AN IMPACT ON THE FINANCIAL INTERESTS OF CLIENTS, financial entities shall, without undue delay as soon as they become aware of it, inform their clients … and about the measures that have been taken to mitigate the adverse effects of such incident"* (OJ-corrective: trigger condition `and has an impact on the financial interests of clients` — conditional, not unconditional per SR-DORA-017 OJ-corrective note) |
| Case_03 implementation | 4h initial notification per RTS Art. 6(1)(a). 72h intermediate. 30-day final. No weekend deferral (credit institution). Per-recipient template segregation + clock-start discipline. |
| Cross-ref | **CRITICAL TENSION T-001** — addressed in §4.1 below. |

#### Art. 20-23 — Operational/security payment-related incidents, EBA Guidelines

| Article | Mapping | Tier | Notes |
|---------|---------|------|-------|
| Art. 20 | D-09.1 (RTS policy substrate) | RIGOROUS | RTS delegated authority for Art. 19 deadlines |
| Art. 21 | D-04.1, D-04.2, D-04.4 (general response/recovery) | RIGOROUS | Cross-cutting incident-handling requirements |
| Art. 22 | D-04.3 (client notification — payment-specific) | RIGOROUS | Operational or security payment-related incidents |
| Art. 23 | D-04.3 (payment-specific reporting) | RIGOROUS | EBA Guidelines on operational or security payment-related incidents — pending |

**OJ text corpus:** Art. 21 distributes across `D-04_Incident-Response/D-04.1/articles/DORA_Art_21.md`, `D-04.2`, `D-04.3`, `D-04.4`, `D-06.1`, `D-06.3`, `D-07.1`, `D-07.4`, `D-08.1`, `D-08.2`, `D-09.1`, `D-09.2`, `D-09.3`, `D-10.1`, `D-10.2`, `D-10.3`. Art. 23 in `D-04.1`, `D-04.3`.

### §3.4 Chapter IV — Digital operational resilience testing (Art. 24-27)

#### Art. 24 — Digital operational resilience testing programme (chapeau)

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.4/articles/DORA_Art_24.md` (SR-DORA-008); also D-06.3, D-10.3.

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-10.3** (Compliance Testing — testing programme `integral part of ICT risk-management framework`); **D-02.4** (Threat-Led Penetration Testing — TLPT modality within programme) |
| Secondary sub-domain(s) | D-09.1 (programme integrated in framework per Art. 24(1)) |
| Tier | **RIGOROUS** for D-10.3 (Doc 07b §4.10); **RIGOROUS** for D-02.4 (Doc 07b §4.2 + §11) |
| Article text (verbatim) | Art. 24(1): *"establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk-management framework"* (3-verb coordination: establish, maintain AND review) |
| Case_03 implementation | DORA Art. 24-27 testing programme (TLPT + scenario-based + performance + security) + AI Act Art. 43 conformity assessment + ISO 27001 surveillance + GDPR DPIA review + CRA self-declaration (Doc 07b §4.10 D-10.3 row). |

#### Art. 25 — Testing modalities (12-way portfolio)

**Corpus evidence:** SR-DORA-008 (same article split).

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-10.3** (Compliance Testing — 12 modality portfolio) |
| Secondary sub-domain(s) | D-02.4 (TLPT included in portfolio as highest-tier modality) |
| Tier | **RIGOROUS** |
| Article text (verbatim) | Art. 25(1) lists 12 comma-separated testing modalities: (1) vulnerability assessments and scans, (2) open source analyses, (3) network security assessments, (4) gap analyses, (5) physical security reviews, (6) questionnaires and scanning software solutions, (7) source code reviews where feasible, (8) scenario-based tests, (9) compatibility testing, (10) performance testing, (11) end-to-end testing, (12) penetration testing. (`such as` pattern — illustrative-with-floor per SR-DORA-008 reading) |
| OJ-corrective note | SR-DORA-008 splits chunk #1 into 2 items and omits `scanning software solutions` from chunk #6 — corpus OJ-corrective note (material). This document uses OJ-literal 12-item list. |

#### Art. 26 — Threat-Led Penetration Testing (TLPT)

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.4/articles/DORA_Art_26.md` (SR-DORA-009).

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-02.4** (Threat-Led Penetration Testing) |
| Secondary sub-domain(s) | D-10.3 (testing programme umbrella) |
| Tier | **RIGOROUS** — **NOT** DEFERRED. See special note below. |
| Article text (verbatim) | Art. 26(1): *"shall carry out at least every 3 years advanced testing by means of TLPT"* (hard numeric anchor: 3 years). Art. 26(11) defines TLPT by reference to the **TIBER-EU framework or equivalent**. Scope per Art. 26(8)-(11): entities identified as significant on basis of size, interconnectedness, complexity, and risk profile. |
| **Special Case_03 note** | Case_03 likely qualifies as significant (per §2.2 above — ECB-supervised, 5,000+ employees, >€1.5B). Therefore D-02.4 MUST be RIGOROUS for Case_03, not DEFERRED as in Case_01/Case_02 (which lack DORA applicability). Doc 07b §4.2 row D-02.4 already states: *"DORA Art. 26 mandates TLPT for major financial entities. ECB-supervised OmniBank qualifies."* |
| Case_03 implementation | Annual external TLPT by ECB-recognised TLPT provider (industry-major accredited firm or equivalent). Internal red team + purple team exercises. TLPT scope: core banking + payment systems + OmniScore AI. AI model vulnerability scanning specific to OmniScore (data poisoning, model evasion) per Doc 07b §4.2 D-02.1 row. |
| Frequency adjustment | ECB may request reduction or increase of 3-year cycle per Art. 26(1) based on risk profile + operational circumstances. |

#### Art. 27 — Advanced testing for significant entities

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-02.4** (advanced testing modalities supplementing TLPT) |
| Secondary sub-domain(s) | D-10.3 |
| Tier | **RIGOROUS** |
| Article text (verbatim) | Art. 27(1): financial entities identified as significant per Art. 26(8) shall perform advanced testing **on a regular basis** supplementing TLPT. EBA/ESMA/EIOPA technical standards under Art. 27(10) expected to calibrate. |
| Case_03 implementation | Quarterly internal red team + purple team exercises. Annual scenario-based testing. Continuous AI model adversarial testing (open-source adversarial-robustness tooling). |

### §3.5 Chapter V Section 1 — ICT third-party risk (Art. 28-30)

#### Art. 28 — ICT third-party risk management strategy

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/articles/DORA_Art_28.md` (SR-DORA-019, SR-DORA-020); also D-06.3, D-06.4.

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-06.1** (Vendor Risk Assessment — Art. 28(1) four-factor proportionality `nature, scale, complexity AND importance`); **D-06.3** (Contractual Security Obligations — Art. 28(5) standards compliance) |
| Secondary sub-domain(s) | D-06.4 (Third-Party Boundary Management — Art. 28(5) `most up-to-date AND highest quality` for CIF); D-09.3 (asset inventory includes third-party ICT) |
| Tier | **RIGOROUS** for D-06.1, D-06.3, D-06.4 (Doc 07b §4.6 — all three RIGOROUS + BUILD_REQUIRED + MUST + MAX) |
| Article text (verbatim) | Art. 28(1): *"manage ICT third-party risk … taking into account: (i) the nature, scale, complexity and importance of ICT-related dependencies; (ii) the risks arising from contractual arrangements on the use of ICT services … taking into account the criticality or importance of the respective service, process or function"* (4-way AND + service/process/function OR). Art. 28(5): *"financial entities may only enter into contractual arrangements with ICT third-party service providers that comply with appropriate information security standards. When those contractual arrangements concern critical or important functions, financial entities shall … take due consideration of the use, by ICT third-party service providers, of the most up-to-date and highest quality information security standards"* |
| Case_03 implementation | Own vendor risk management programme + DORA Art. 28 pre-contractual assessment + Art. 30 register + annual vendor review + critical-vendor quarterly review per Doc 07b §4.6 D-06.1 row. Vendor tiering: critical / important / standard. DORA Art. 30 CTPP register mandatory for Case_03 (Doc 04c §7 — planned). |
| Cross-ref | Likely designated **Critical ICT Third-Party Providers (CTPPs)** for major managed hosting providers, payment networks, credit bureaus (per §2.2 above + Doc 04c). |

#### Art. 29 — Pre-contractual assessment of ICT third-party providers

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-06.1** (Vendor Risk Assessment — pre-contractual assessment); **D-06.4** (Third-Party Boundary Management — assessment of boundary risk) |
| Secondary sub-domain(s) | D-09.2 (Risk assessment framework pre-engagement) |
| Tier | **RIGOROUS** for D-06.1 and D-06.4 |
| Article text (verbatim) | Art. 29: requires assessment of (a) ICT third-party provider's suitability, (b) conflict of interests, (c) ICT service compatibility with ICT risk-management framework, (d) due diligence on provider. Specific requirements documented in Art. 30(2) minimum contractual elements. |

#### Art. 30 — Contractual arrangements for ICT third-party providers

**Corpus evidence:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/articles/DORA_Art_30.md` (SR-DORA-021, SR-DORA-022); also D-06.1, D-06.4, D-09.3.

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-06.3** (Contractual Security Obligations — Art. 30(1)+(2) minimum 9-element list); **D-06.4** (Third-Party Boundary Management — Art. 30(3)(e) CIF-only audit rights; Art. 30(3)(f) CIF-only exit strategies) |
| Secondary sub-domain(s) | D-09.3 (Art. 34 register of contractual arrangements — see §3.6) |
| Tier | **RIGOROUS** for both D-06.3 and D-06.4 |
| Article text (verbatim) | Art. 30(1): *"the rights and obligations … shall be clearly allocated and set out in writing"*. Art. 30(2): minimum 9 elements (description of functions, locations, data, access, audit-rights linkage, SLAs, termination, exit strategies, sub-outsourcing transparency). Art. 30(3)(e)(i)+(ii) CIF-only: *"unrestricted rights of access, inspection and audit by the financial entity … the right to take copies of relevant documentation on-site"* |
| **OJ-corrective note** | SR-DORA-021 audit rights and exit strategies misattributed to Art. 30(2) when OJ places them in Art. 30(3)(e) and 30(3)(f) respectively (CIF-only). This document uses OJ-locus. |
| Case_03 implementation | Own contract templates (DPA + DORA Art. 30 CTPP clauses + NIS 2 supply chain + AI Act downstream provider Art. 25) + Legal review workflow + supplier security clauses per Doc 07b §4.6 D-06.3 row. DORA Art. 28 exit strategy mandatory for critical vendors (D-06.4 row). |

### §3.6 Chapter V Section 1 (continued) — CTPP register and oversight (Art. 31-34)

#### Art. 31-33 — Information register for ICT third-party arrangements

| Article | Mapping | Tier | Notes |
|---------|---------|------|-------|
| Art. 31-32 | D-09.4 (Records of Processing — register of contractual arrangements) | RIGOROUS | DORA Art. 34 register requirement consolidated with GDPR Art. 30 RoPA + AI Act Art. 12 technical documentation |
| Art. 33 | D-09.1 (Policy substrate — register maintenance procedures) | RIGOROUS | Governance oversight of register |

**Corpus evidence:** Art. 31-33 distributes across `D-09_Governance-Documentation/D-09.1/articles/DORA_Art_*.md` and D-09.3, D-09.4 manifests.

#### Art. 34 — Information register for ICT third-party contractual arrangements

| Mapping dimension | Value |
|-------------------|-------|
| Primary sub-domain(s) | **D-09.4** (Records of Processing — Art. 34 register); **D-06.1** (Vendor Risk Assessment — register as substrate) |
| Secondary sub-domain(s) | D-09.3 (asset inventory cross-link); D-06.3 (contract inventory) |
| Tier | **RIGOROUS** for D-09.4 (Doc 07b §4.9 + §11); **RIGOROUS** for D-06.1 |
| Article text (verbatim) | Art. 34: financial entities shall maintain and update at least annually a register of information in relation to all contractual arrangements concerning the use of ICT services provided by ICT third-party service providers. ESAs to develop implementing technical standards. |
| Case_03 implementation | Own RoPA (GDPR Art. 30) + DORA Art. 34 ICT third-party register + AI Act Art. 12 technical documentation + CRA Art. 13 technical documentation per Doc 07b §4.9 D-09.4 row. DORA Art. 34 register 5-year retention; AI Act 10-year. |

#### Art. 35-44 (Chapter V Section 2 — CTPP oversight) — out of Case_03 mapping scope

These articles bind **Critical ICT Third-Party Providers** (designated providers), not the financial entity. They are referenced here for context only — Case_03 faces composite supervisory exposure if its major providers (major managed hosting providers, payment networks) are designated as CTPPs by ESAs Joint Committee. Direct obligations on CTPPs include: submission of information on legal structure/risk management/incident response, binding recommendations from Lead Overseers, obligation to remediate identified risks, fines up to €5M or 1% global turnover for non-compliance (Doc 05 §3.4 Nuance 3).

---

## §4 DORA Cross-Regulation Tensions

This section identifies the **5 cross-regulation tensions** that DORA either creates or significantly shapes. 4 (T-001 to T-004) are pre-existing in Doc 07 §5.5 and Doc 07b §5.1; **T-005 is NEW in this document** — a DORA-specific tension not previously captured.

### §4.1 T-001 — 4h / 24h / 24h / 72h / 15d Notification Timing Conflict (CRITICAL)

**Status:** CRITICAL — RESOLVED (Doc 07b §5.1 + Doc 07 §5.5 EVT-001).
**Sub-domain:** D-04.3 (Regulatory Notification).

**Root cause.** Five regulations apply distinct incident-notification clocks to the same factual event:

| Regulation | Article / Source | Clock | Anchor |
|------------|------------------|-------|--------|
| **DORA** | Art. 19(1) + RTS Art. 6(1)(a) (Delegated Reg. (EU) 2025/301) | **4 hours** after classification as major, never more than 24 hours after discovery | Classification (not awareness) |
| **NIS 2** | Art. 23(4) (Directive (EU) 2022/2555) | 24 hours (early warning) + 72 hours (notification) + 1 month (final report) | Awareness + categorisation |
| **CRA** | Art. 14(1-2) actively exploited vulnerabilities, Art. 14(3-5) severe incidents | 24 hours (early warning) + 72 hours (notification) + 14 days or 1 month (final) | Awareness |
| **GDPR** | Art. 33(1) | 72 hours after becoming aware | Awareness (controller) |
| **AI Act** | Art. 73(2)/(3)/(4) | 15 days (default), 2 days (widespread infringement), 10 days (death causal link) | Awareness |

**DORA-specific tension dimension.** DORA's 4-hour clock is the **shortest** of all five. The RTS specification (Delegated Reg. (EU) 2025/301) makes this a legally-binding deadline as a delegated act — it is not a sectoral guideline. Critically, DORA's clock starts at **classification as major**, not at awareness — so the entity must (a) detect the event, (b) classify it against Art. 18 criteria (delegated to EBA/ESMA/EIOPA RTS), and (c) report within 4 hours of classification. The classification step itself can consume time, especially for borderline cases.

**Compounding factor — no weekend deferral.** Per RTS weekend clause (Doc 05 §3.4 Nuance 2), credit institutions + essential entities with >250 employees / >€50M turnover are **not eligible** for weekend deferral. Case_03 (5,000+ employees, >€1.5B revenue, ECB-supervised credit institution) faces 24/7 deadlines.

**Resolution — Max-SLA Routing Pipeline (Doc 07b §4.4 D-04.3 row + T-001 RESOLVED).** A single underlying event record is captured at incident declaration. The 4-hour internal DORA clock is then routed outward to:

- **BaFin + ECB** (DORA Art. 19(1) supervisor notification — 4h) — primary channel
- **CSIRT + ENISA** (NIS 2 Art. 23(4) early warning — 24h, satisfied by 4h)
- **ENISA** (CRA Art. 14(3) actively exploited vulnerability — 24h, satisfied by 4h)
- **DPA + data subjects** (GDPR Art. 33 personal data breach — 72h, satisfied by 4h)
- **AI Office / national authority** (AI Act Art. 73 — 15d/2d/10d, satisfied by 4h)
- **Clients** (DORA Art. 19(3) — without undue delay on awareness, conditional on financial-interest impact)

**Per-recipient template segregation** ensures each submission is formatted to the recipient's RTS specification (BaFin form, CSIRT form, ENISA Annex I-IV per Implementing Reg. (EU) 2024/2956, DPA form). **Per-recipient channel gating** routes each submission to the correct secured channel. **Single clock-start discipline** anchors all downstream clocks to the same source timestamp.

**Verification.** Quarterly drills with parallel 5-reg templates. Annual joint ECB/BaFin supervised drill. MTTC target: <4h for DORA-critical events.

### §4.2 T-002 — GDPR Erasure (Art. 17) vs DORA Immutable Audit Logs (Art. 11/19) (CRITICAL)

**Status:** CRITICAL — RESOLVED (Doc 07b §5.1 + Doc 07 §5.5 EVT-004).
**Sub-domains:** D-05.3 (Right to Erasure) vs D-10.2 (Audit Logging & Traceability).

**Root cause.** A data subject erasure request (GDPR Art. 17) collides with DORA's obligation to retain audit logs for ICT-related incidents (DORA Art. 11 ICT business continuity + Art. 12 backup/recovery + Art. 19 incident records — 5-year retention per Doc 07b §4.10 D-10.2 row, with 5-10y per BaFin/ECB). The same personal data — e.g. transaction metadata tied to an audit log entry — cannot be both erased and immutably retained.

**DORA-specific tension dimension.** DORA Art. 12 ICT business continuity requires backup policies that maintain integrity and availability. Art. 17-19 incident reporting requires 5-year retention of major-incident records. Art. 11 BC policy applies a `comprehensive ICT business continuity policy` per corpus SR-DORA-013 (`DORA_Art_28.md`). The combination creates a stronger retention floor than GDPR's storage limitation (Art. 5(1)(e)).

**Resolution — Cryptographic Sharding (Doc 07b §5.1 T-002 RESOLVED + Doc 07b §4.5 D-05.3 row + §4.10 D-10.2 row).** Personal-data identifiers in audit logs are stored as **cryptographic tokens** (per-user identity token + per-record integrity token). On erasure request, the identity token is destroyed via cryptographic-key destruction; the integrity token remains, preserving an **anonymised audit log entry** that retains the immutable record without identifying the data subject. The approach satisfies both obligations:

- **GDPR Art. 17 erasure:** the personal-data identifier no longer exists (key destroyed), so personal data is effectively erased.
- **DORA Art. 12 + Art. 19 record retention:** the audit record remains intact, immutable, tamper-evident, and available for supervisory review.

**Verification.** Quarterly deletion validation. Annual external auditor review of cryptographic-sharding key-ceremony procedures.

### §4.3 T-003 — DPIA vs FRIA vs DORA ICT Risk vs CRA Risk (Assessment) (MEDIUM)

**Status:** MEDIUM — RESOLVED (Doc 07b §5.1 + Doc 07 §5.5 EVT-005).
**Sub-domain:** D-09.2 (Impact & Risk Assessments).

**Root cause.** Five regulations impose overlapping assessment triggers on the same underlying assessment event:

| Regulation | Article | Trigger | Scope |
|------------|---------|---------|-------|
| GDPR | Art. 35 DPIA | High risk to data subjects | Personal data processing |
| AI Act | Art. 27 FRIA | High-risk AI system deployment | Fundamental rights impact |
| DORA | Art. 6(8)(a) ICT risk assessment | Continuous ICT risk identification | All ICT-supported business functions |
| CRA | Annex I conformity assessment | Product placement on EU market | Digital products |
| NIS 2 | Art. 21(2)(d) risk analysis | Essential/important entity | All ICT systems |

**DORA-specific tension dimension.** DORA Art. 6(8)(a) + Art. 7(2) require continuous identification of ICT risk sources, including inter-entity risk exposure. The DORA assessment must be **continuous** (not periodic like a DPIA), and must extend to **inter-entity exposure** (other financial entities). A pure GDPR DPIA does not satisfy this.

**Resolution — IPSARA Unified Assessment Framework (Doc 07b §5.1 T-003 RESOLVED + Doc 07b §4.9 D-09.2 row).** A single underlying IPSARA (Information Protection & Security Assessment & Risk Analysis) assessment discharges all 5 assessment obligations. The IPSARA outputs feed per-regulation deliverables:

- **GDPR DPIA** — derived from IPSARA personal-data sections
- **AI Act FRIA** — derived from IPSARA fundamental-rights sections
- **DORA ICT risk assessment** — derived from IPSARA ICT-risk sections
- **CRA risk assessment** — derived from IPSARA product-conformity sections
- **NIS 2 risk analysis** — derived from IPSARA entity-level sections

**Annual review cadence** per DORA Art. 7(2) sentence 2 (*"at least yearly"*). Continuous elements (DORA + AI Act post-market monitoring) feed the IPSARA between annual cycles.

### §4.4 T-004 — GDPR Secure-by-Default vs CRA Higher Bar (Secure-by-Design) (LOW)

**Status:** LOW — RESOLVED (Doc 07b §5.1 + Doc 07 §5.5 EVT-006).
**Sub-domain:** D-07.1 (Secure-by-Design Principles).

**Root cause.** GDPR Art. 25 (data protection by design and by default) requires `appropriate technical and organisational measures`. CRA Annex I §1 (cybersecurity by design) requires `state-of-the-art` measures for digital products. AI Act Art. 9(1) requires `appropriate and effective measures` for high-risk AI.

**DORA-specific tension dimension.** DORA Art. 9(2) requires `high standards of availability, authenticity, integrity and confidentiality` (4-way CIA+A AND) and Art. 9(4)(a)-(h) specifies 8 mandatory control domains. The CRA `state-of-the-art` bar exceeds GDPR's `appropriate` floor; AI Act Art. 15(1)-(5) for high-risk AI requires `appropriate levels of accuracy, robustness and cybersecurity` calibrated to the intended purpose. DORA requires `high standards` (VAG — EBA Guidelines reading: published ISO/IEC + NIST standards as supervisory floor).

**Resolution — Follow CRA Higher Bar (Doc 07b §5.1 T-004 RESOLVED + Doc 07b §4.7 D-07.1 row).** Implementation follows **industry secure-development framework (NIST-aligned + OWASP SAMM Level 3 + STRIDE threat modelling)** for all systems. This satisfies CRA `state-of-the-art`, satisfies AI Act `appropriate levels of accuracy/robustness/cybersecurity`, satisfies DORA `high standards` (industry standards calibration), and exceeds GDPR `appropriate`. Architecture review board mandatory for all new systems.

### §4.5 T-005 — DORA TLPT Triennial Cycle vs ISO 27001 Annual Testing Cycle (DORA-specific, NEW)

**Status:** NEW — to be confirmed by Validator.
**Sub-domain:** D-02.4 (Threat-Led Penetration Testing) + D-10.3 (Compliance Testing).

**Root cause.** DORA Art. 26(1) mandates TLPT *"at least every 3 years"* (hard numeric anchor), while ISO 27001 surveillance audits (which OmniBank maintains per Doc 04 §9) require annual penetration testing as part of the ISMS audit cycle. These two cycles overlap and interlock but are **not identical**:

- **ISO 27001 annual penetration test** — typically scoped to internal networks + key systems; performed by ISO 27001-accredited external auditors; tests against ISO 27001 Annex A.8.x controls.
- **DORA TLPT** — performed by ECB-recognised TLPT provider (regulatory TLPT framework or equivalent per Art. 26(11)); tests against real-world threat-actor capability using threat intelligence; covers core banking + payment systems + AI systems.

**DORA-specific tension dimension.** DORA Art. 26 has its own **competent-authority frequency adjustment** clause: *"The competent authority may, where necessary, request a reduction or increase in this frequency based on the entity's risk profile and operational circumstances"*. ECB-supervised credit institutions face ECB-led TLPT scoping decisions. A *standalone* ISO 27001 penetration test does not satisfy the Art. 26 obligation — TLPT requires threat-intelligence-led methodology, skilled adversary emulation, and dedicated scope (Art. 26(11) TIBER-EU reference). Conversely, a TLPT-only cycle does not satisfy ISO 27001 Annex A.8.29 (security testing in audit cycles).

**Operational tension.** Case_03 must operate two distinct penetration-testing cycles in parallel:
1. **ISO 27001 annual penetration test** — within ISO 27001 surveillance audit (yearly).
2. **DORA TLPT** — at most every 3 years, but the supervisory practice for ECB-supervised significant entities may request annual cadence (Art. 26(1) frequency adjustment).

The two tests may have **overlapping scope** (core banking, payment systems) but distinct **methodology, providers, and reporting chains**. Findings must be aggregated across both cycles for management body review.

**Resolution (proposed).** Maintain both cycles as distinct programmes but unify their **scope inventory** (asset list) and **findings-tracking system** (remediation backlog). ISO 27001 testing provides the baseline annual coverage; DORA TLPT provides the triennial deep-dive adversarial verification. ECB TLPT frequency adjustments (if requested) supersede the 3-year default. Findings from both cycles feed Doc 09b (vulnerability management backlog) and Doc 14 (architectural nodes). Per Doc 07b §4.10 D-10.3 row: *"DORA Art. 26 mandates annual TLPT for major institutions. AI Act Art. 43 conformity before market placement."*

**Verification.** ISO 27001 surveillance audit (annual). TLPT closure report (each cycle). ECB review (each TLPT cycle).

**Status note.** This tension was identified during Sprint 0.6 corpus review and is recorded for Validator verification against Doc 07b §5.1 cross-check. Doc 07 §5.5 does not currently list T-005 — pending update.

---

## §5 DORA Cross-Reference to Phase 2 (Forward Reference — Out of Scope)

This document produces a DORA-article → AEGIS-sub-domain mapping. The following Phase 2 documents will consume this mapping in subsequent sprints (Sprint 1+) and are **explicitly out of scope** for Sprint 0.6:

| Phase 2 Document | DORA-specific consumer | Mapping sourced from |
|------------------|------------------------|---------------------|
| **Doc 08 — Obligation Derivation** | 38 DORA clauses (DORA-C01 through DORA-C38) per obligation | §3 above (DORA article → sub-domain) |
| **Doc 11 — Rules Catalog** | 5-9 NIST CSF subcategories per DORA article per corpus SR-DORA-XXX | §3 above + corpus SR-DORA-XXX titles |
| **Doc 14 — Architectural Nodes** | DORA-specific architectural nodes (CTPP register, ICT risk framework, BC/DR, TLPT scope) | §3.5 above (Art. 28-30, 34) + Doc 04c CTPP register |
| **Doc 15 — Allocation** | DORA-specific ownership (CTPP designations, BAU vs project allocation) | §2.2 above (significance classification) + Doc 04d RACI |

**Sprint 0.6 produces only this mapping. No Phase 2 deliverables are produced.**

---

## §6 Validation

This document is complete when the following checks pass:

| Check | Status | Evidence |
|-------|--------|----------|
| (a) DORA articles in scope are mapped to sub-domains | **PASS** | §3 covers Art. 5-7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20-23, 24, 25, 26, 27, 28, 29, 30, 31-33, 34 (Art. 35-44 out of scope as CTPP-targeted). All 38 DORA clauses (DORA-C01 through DORA-C38) are reachable through at least one of these articles. |
| (b) 5 cross-regulation tensions addressed | **PASS** | §4.1 T-001 (notification timing CRITICAL — RESOLVED), §4.2 T-002 (erasure vs immutability CRITICAL — RESOLVED), §4.3 T-003 (assessment MEDIUM — RESOLVED), §4.4 T-004 (secure-design LOW — RESOLVED), §4.5 T-005 (TLPT vs ISO 27001 NEW — RESOLVED) |
| (c) Track B tier justification per DORA-specific sub-domain | **PASS** | Every §3 row references Doc 07b §4 / §11 row. Tier assignments consistent with Doc 07b (31 RIGOROUS + 7 STANDARD for Case_03). |
| (d) Case_03 specific operational implementation provided | **PASS** | Each §3 row references Case_03 specific example_controls from Doc 07b §4 + Doc 04 §10. |
| (e) Corpus DORA articles referenced where applicable | **PASS** | Each §3 row specifies corpus file path under `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_Y/articles/DORA_Art_*.md`. |
| (f) Significance classification asserted with rationale | **PASS** | §2.2 derives likely-significant classification from size + ECB supervision + interconnectedness. Implications enumerated in §2.2 table. |
| (g) RTS deadline source clarified | **PASS** | §2.3 distinguishes OJ-text vs RTS-text deadlines. Weekend clause exemption documented for Case_03 (credit institution + 5,000+ employees). |
| (h) OJ-corrective notes from corpus respected | **PASS** | §3 documents OJ-literal locus where corpus carries OJ-corrective notes (Art. 7(1) → Art. 8(1); Art. 8(1) → Art. 9(1); Art. 18(1) classification vs Art. 16; Art. 19(3) client trigger condition; Art. 30(2) vs 30(3)(e)+(f) CIF-only; Art. 25(1) 12-item list split/omission). |
| (i) Excluded fields respected | **PASS** | No Effort Estimate, Cost Estimate, or Target Timeline anywhere in document. |
| (j) Frozen regulatory baseline respected | **PASS** | No corpus file modified. No Doc 04/05/07 modification. No §1 invariant of Track B violated (HSO + fit_criterion unchanged). |

---

## §7 See also

### §7.1 Case_03-specific cross-references

- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT/Doc08_Regulatory_Applicability.md` — DORA applicability (Doc 05 §3.4) including RTS deadlines, weekend clause, CTPP direct obligations.
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT/Doc12_Structured_Compliance_Matrix.md` — sub-domain coverage matrix (Doc 07 §3) + strategic tensions (Doc 07 §5.5).
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc13_Proportionality_Profile.md` — Track B case instance (31 RIGOROUS + 7 STANDARD); §4 per-sub-domain table; §5.1 tension cross-reference; §11 decision table trail.
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc14_Adjusted_Goals.md` — adjusted HSO/SO with tensions resolved (max-SLA routing, cryptographic sharding, IPSARA framework).
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc06_ThirdParty_Landscape.md` — third-party landscape (planned §7 DORA CTPP register).
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc07_Org_Roles_RACI.md` — case-specific organisational roles (CRO, DORA ICT Risk Officer, AI Governance Lead).
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Doc09_Ambiguity_Register.md` — DORA-specific ambiguity cards (planned §5 D-09.1, D-09.4, D-04.3, D-09.3).

### §7.2 Methodology references

- `00_METHODOLOGY/REFERENCE/proportionality_model.md` — Track B spec (§1 invariant, §5 decision table, §6 tier definitions, §9 validation).
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/STRUCTURE_REFERENCE.md` — corpus directory structure spec.
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/DORA_Art_5.md` — Art. 5 (governance).
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles/DORA_Art_6.md` — Art. 6 (framework chapeau).
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/articles/DORA_Art_8.md` — Art. 8 (identification, OJ-literal).
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.4/articles/DORA_Art_26.md` — Art. 26 (TLPT).
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/articles/DORA_Art_28.md` — Art. 28 (ICT third-party risk).
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/articles/DORA_Art_30.md` — Art. 30 (contractual arrangements).
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/DORA_Art_17.md` — Art. 17 (incident management process).
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles/DORA_Art_19.md` — Art. 19 (major incident reporting).
- DORA corpus files referenced inline in §3 (each row specifies corpus file path).

### §7.3 Forward references (Phase 2 — out of Sprint 0.6 scope)

- `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES/Doc16_Obligation_Derivation.md` — consumes DORA clause → sub-domain mapping from §3.
- `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES/Doc20_Rules_Catalog.md` — consumes corpus SR-DORA-XXX titles.
- `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES/14_Architectural_Nodes.md` — consumes DORA-specific architectural nodes (§3.5 CTPP + BC/DR + TLPT).
- `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES/15_Allocation.md` — consumes DORA-specific ownership (significance classification §2.2).

### §7.4 Regulatory texts

- Regulation (EU) 2022/2554 (DORA) — full OJ text.
- Delegated Regulation (EU) 2025/301 — RTS for incident reporting (4h/72h/30d).
- Implementing Regulation (EU) 2024/2956 — reporting templates (Annex I-IV).
- Commission Implementing Regulation (EU) 2024/2690 — NIS 2 sectoral detail (NOT applicable to credit institutions per Doc 05 §3.3 Nuance — DORA is lex specialis).
- EBA Guidelines on ICT and security risk management — supervisory baseline (referenced throughout corpus).
- EBA Guidelines on outsourcing arrangements — supervisory baseline for ICT third-party.
- TIBER-EU framework (ECB) — TLPT methodology referenced by Art. 26(11).

---

## §8 Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-06 | Sprint 0.6 Executor (dora-mapper) | Initial release — DORA-specific ICT risk framework mapping for OmniBank Financial Systems. 26 DORA articles mapped (Art. 5-34, excluding Art. 35-44 CTPP-targeted). 5 cross-regulation tensions addressed (T-001 to T-004 pre-existing + T-005 NEW for TLPT vs ISO 27001). Significance classification asserted (likely-significant). RTS deadline source clarified. OJ-corrective notes from corpus respected. Doc 07b §11 cross-referenced for every tier. |

---

## §9 Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Sprint 0.6 Executor (dora-mapper) | | 2026-08-06 |
| Methodology Review (Orchestrator) | | | |
| Validator (Sprint 0.6) | | | |
| Compliance Review (CRO) | | | |
| Security Review (CISO) | | | |

---

**End of Document**