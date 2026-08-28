---
document_id: AEGIS-P2-RICH-05b-AMBIG
title: Ambiguity Register (Rich Mode)
phase: 1
version: 1.1
created: 2026-08-06
updated: 2026-08-06
author: Sprint 2 Executor (corpus enrichment); Sprint 4 Executor (top-20 distinctness fix + active-set reconciliation)
status: CORPUS_ENRICHED
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
active_subdomains: 35
inactive_subdomains: [D-07.4, D-08.3, D-09.3]
new_in_rich: true
inputs:
  - 00_METHODOLOGY/PREPROCESSING_by_domain/domains/
  - Doc08_Regulatory_Applicability.md
  - Doc12_Proportionality_Profile.md
outputs:
  - Doc13_Adjusted_Goals.md
  - Doc11_Structured_Compliance_Matrix.md
---

# Ambiguity Register

## 1. Summary

This register catalogues every Berry-flagged ambiguity card present in the per-sub-domain JSON sidecars under `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`, filtered to the four applicable regulations for Case_02: **GDPR + CRA + NIS 2 + AI_Act**. DORA is excluded (does not apply to SecureBorder).

**Berry lens** (per `00_METHODOLOGY/PREPROCESSING/AMBIGUITY_ANALYSIS/01_Framework.md`):

| Category | Code | Meaning |
|---|---|---|
| VAG | Vagueness | Words like "appropriate", "state of the art" without objective anchor |
| POLY | Polysemy | Single term with multiple operational senses (e.g., "delete") |
| SCOPE | Scope ambiguity | Universal quantifier without clear boundary (e.g., "all data") |
| COORD | Coordination | Ambiguous logical connector (AND/OR) |

**Severity** S1 (low) → S2 (medium) → S3 (high).

**Aggregate counts (Case_02 applicable regs only):**

| Metric | Value |
|---|---:|
| Sub-domains scanned | 38 |
| Active sub-domains (Case_02) | 35 |
| NOT_ADDRESSED sub-domains | 3 (D-07.4, D-08.3, D-09.3) |
| Total ambiguity cards (filtered) | 1071 |
| Top-20 documented below | 20 |

## 2. Per-Sub-Domain Ambiguity-Card Breakdown

Sorted by card count descending; the top sub-domains drive the top-20 cards in §3 below.

| Sub-domain | Sub-domain name | Status | Applicable regs | Card count |
|---|---|---|---|---:|
| D-09.1 | Information Security Policies | ACTIVE | CRA, GDPR, NIS2 | 88 |
| D-09.4 | Records of Processing | ACTIVE | CRA, GDPR, NIS2 | 64 |
| D-06.3 | Contractual Security Obligations | ACTIVE | CRA, GDPR, NIS2 | 61 |
| D-04.3 | Incident Notification & Reporting | ACTIVE | CRA, GDPR, NIS2 | 57 |
| D-09.2 | Impact & Risk Assessments | ACTIVE | CRA, GDPR, NIS2 | 54 |
| D-07.1 | Secure-by-Design Principles | ACTIVE | CRA, GDPR, NIS2 | 47 |
| D-03.1 | Identity Lifecycle Management | ACTIVE | CRA, GDPR, NIS2 | 45 |
| D-02.1 | Vulnerability Identification | ACTIVE | CRA, GDPR, NIS2 | 41 |
| D-01.1 | Data at Rest Encryption | ACTIVE | CRA, GDPR, NIS2 | 39 |
| D-04.2 | Incident Containment & Response | ACTIVE | CRA, GDPR, NIS2 | 37 |
| D-04.4 | Incident Recovery & Lessons Learned | ACTIVE | CRA, GDPR, NIS2 | 37 |
| D-10.1 | Continuous Security Monitoring | ACTIVE | CRA, GDPR, NIS2 | 36 |
| D-10.3 | Compliance Testing | ACTIVE | CRA, GDPR, NIS2 | 35 |
| D-08.1 | General Security Awareness | ACTIVE | GDPR, NIS2 | 33 |
| D-09.3 | Asset Inventories | NOT_ADDRESSED | CRA, NIS2 | 33 |
| D-01.2 | Data in Transit Encryption | ACTIVE | CRA, GDPR, NIS2 | 31 |
| D-04.1 | Incident Detection & Triage | ACTIVE | CRA, GDPR, NIS2 | 31 |
| D-02.3 | Coordinated Vulnerability Disclosure | ACTIVE | CRA, NIS2 | 30 |
| D-03.3 | Authorisation & Least Privilege | ACTIVE | CRA, GDPR, NIS2 | 30 |
| D-05.1 | Data Minimisation | ACTIVE | CRA, GDPR | 30 |
| D-08.2 | Role-Specific Competence | ACTIVE | GDPR, NIS2 | 30 |
| D-06.1 | Vendor Risk Assessment | ACTIVE | CRA, GDPR, NIS2 | 29 |
| D-03.2 | Multi-Factor Authentication | ACTIVE | GDPR, NIS2 | 26 |
| D-06.4 | Third-Party Boundary Management | ACTIVE | CRA, GDPR, NIS2 | 17 |
| D-05.3 | Right to Erasure | ACTIVE | GDPR | 14 |
| D-01.4 | Data Integrity Mechanisms | ACTIVE | GDPR | 13 |
| D-10.2 | Audit Logging & Traceability | ACTIVE | CRA, GDPR | 11 |
| D-05.2 | Retention & Archiving | ACTIVE | CRA, GDPR | 10 |
| D-01.3 | Cryptographic Key Management | ACTIVE | CRA, GDPR, NIS2 | 9 |
| D-03.4 | Secure System Defaults | ACTIVE | CRA, GDPR | 9 |
| D-07.4 | Change Management | NOT_ADDRESSED | CRA | 9 |
| D-02.2 | Patch Management & Updates | ACTIVE | CRA | 8 |
| D-08.3 | Management Board Training | NOT_ADDRESSED | NIS2 | 6 |
| D-05.4 | Data Portability | ACTIVE | GDPR | 5 |
| D-02.4 | Threat-Led Penetration Testing | ACTIVE |  | 4 |
| D-06.2 | Software Bill of Materials (SBOM) | ACTIVE |  | 4 |
| D-07.2 | Secure Coding Practices | ACTIVE |  | 4 |
| D-07.3 | CI/CD Pipeline Security | ACTIVE |  | 4 |

## 3. Top-20 Ambiguity Cards (highest severity × Case-02 impact)

**Selection logic (Sprint 4 — distinctness fix).** Each card below is a **distinct clause** keyed on `(regulation, clause_id)` (or `(regulation, article_ref, title)` where clause_id is null). Cards are deduplicated across all 35 active sub-domains before ranking. The 20 selected cards are the highest-severity × highest-Case-02-impact clauses:

1. **Severity filter** — keep only cards whose highest instance is `S3` (Berry §5.1 highest severity).
2. **Case-02 impact tier** — prefer cards anchored in RIGOROUS sub-domains (8: D-01.1, D-01.3, D-04.3, D-06.1, D-06.3, D-07.1, D-07.3, D-10.1) over STANDARD sub-domains (27).
3. **Regulatory balance** — round-robin across the four applicable regulations (GDPR + CRA + NIS 2 + AI_Act) to ensure each lens is represented. Distribution in the top-20: GDPR 10, NIS 2 5, CRA 5, AI_Act 0.
4. **AI_Act gap (corpus-side)** — note that the corpus (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/*/D-*.json`) carries 35 `AI_Act — No applicable ambiguity` placeholder cards (one per active sub-domain) and **0 substantive AI_Act ambiguity cards**. AI_Act obligations on SecureBorder are addressed in Doc 07 (`Doc11_Structured_Compliance_Matrix.md`) Annex III §1 (biometric) + §7 (border control) compliance assessment, but the Berry-lens ambiguity register has no AI_Act entries to surface for this case. This is a corpus-coverage gap, not a Case-02 omission — see `00_METHODOLOGY/PREPROCESSING/AMBIGUITY_ANALYSIS/01_Framework.md` for Berry-lens methodology.

Each card shows: regulation + clause_id + article_ref + sub-domain + title + Berry type + severity + verbatim phrase + analysis + variant readings (R1/R2/R3 where present in corpus).


### 3.01 [GDPR] GDPR-CL23 — Art. 9(2)(g)

- **Sub-domain:** D-01.1 (Data at Rest Encryption)
- **Title:** Substantial public interest
- **Type:** lawfulness base (special category)
- **Obligation type:** PER-MEMBER-STATE-LAW
- **Obligated party:** CONTROLLER

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "substantial public interest"

> **Analysis:** `substantial public interest` inherits the Art. 6(1)(e) `public interest` ambiguity plus the `substantial` qualifier. The clause cross-references Charter Art. 52(1) via `essence of the right`.

S3 — same family of ambiguity as Art. 6(1)(e), but more severe because `substantial` is undefined.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R2 — strict reading (substantial public interest = government-contracted border control qualifies per Charter Art. 52(1) `essence of the right` test).
- **Stakeholder Impact:** Travelers (data subjects), DPO, government authorities (controller), DPA.
- **Risk:** HIGH — Wrong reading risks Art. 9 unlawful processing = Art. 83(5) fine (€20M / 4% turnover). Resolution: document per-processing-scope in DPIA; re-evaluate on government contract change.
---

### 3.02 [GDPR] GDPR-CP02 — Art. 25(1)

- **Sub-domain:** D-01.1 (Data at Rest Encryption)
- **Title:** Privacy by design
- **Type:** design obligation
- **Obligation type:** CONTINUOUS
- **Obligated party:** CONTROLLER

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "state of the art"

> **Analysis:** `state of the art` is the canonical Berry-flagged vague term (Berry §5.1). Time-dependent (2024 vs 2026 vs 2028), jurisdiction-dependent, sector-dependent. No objective anchor in the OJ text.

**Variant readings:**

- **R1:** `State of the art` = ISO 27001 + sector-specific best practices at design time.
  - *Source:* Industry reading.
- **R2:** `State of the art` = ENISA / EDPB-published state-of-the-art guidance.
  - *Source:* Strict reading.
- **R3:** `State of the art` = any reasonable technical measure documented at design time.
  - *Source:* Loose reading.

**Instance 2: POLY (S2)**

> **Verbatim phrase:** "effective manner"

> **Analysis:** `effective` is inquiry-resistant but inherits Art. 32(1)(d) testing obligation. S2 because the compliance practice (test + document) is the same.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R2 — ENISA / EDPB-published state-of-the-art guidance as the strictest ceiling; ISO 27001 + sector best practices as a minimum.
- **Stakeholder Impact:** All internal: CTO, DPO, CISO; regulators on audit.
- **Risk:** MEDIUM — Insufficient state-of-the-art Art. 25(1) application. Resolution: ISO 27001 certified ISMS + ENISA state-of-the-art guidance at design time.
---

### 3.03 [GDPR] GDPR-CP15 — Art. 32(1)

- **Sub-domain:** D-01.1 (Data at Rest Encryption)
- **Title:** Security measures (open list)
- **Type:** security
- **Obligation type:** CONTINUOUS
- **Obligated party:** CONTROLLER, PROCESSOR

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "state of the art"

> **Analysis:** Cross-clause propagation — same as Art. 25(1). S3 because security-engineering scope is material to compliance.

**Instance 2: COORD (S3)**

> **Verbatim phrase:** "(a) AND (b) AND (c) AND (d)"

> **Analysis:** The 4-element list `(a) pseudonymisation/encryption, (b) CIA+R, (c) restore-in-timely-manner, (d) regular-testing` is closed (and). All 4 required.

Instance 3 — POLY+VAG / S3 / `in a timely manner` (Art. 32(1)(c))

`Timely manner` is the textbook Berry-flagged temporal vague phrase. Recital 49 (non-binding) attempts to fix: "restore the availability and access as soon as possible". The cross-reference is non-binding and the operational meaning drifts.

**Variant readings:**

- **R1:** `Timely` = RTO defined per processing activity (objective measure).
  - *Source:* Industry standard (BCP/DRP best practice).
- **R2:** `Timely` = as-soon-as-practicable for the specific incident.
  - *Source:* EDPB Guidelines 7/2019 (generic).


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Timely = RTO defined per processing activity (objective measure). Aligns with ISO 27001 BCP/DRP best practice.
- **Stakeholder Impact:** CISO, SOC, internal IT, external auditors.
- **Risk:** HIGH — Art. 32(1)(c) failure on biometric data = Art. 83(5) fine. Resolution: CASE-02 RTO 24h, RPO 1h documented per processing activity.
---

### 3.04 [GDPR] GDPR-RT16 — Art. 21(1)

- **Sub-domain:** D-01.1 (Data at Rest Encryption)
- **Title:** Objection grounds and overriding
- **Type:** data subject right (object)
- **Obligation type:** PER-OBJECTION
- **Obligated party:** CONTROLLER

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "compelling legitimate grounds"

> **Analysis:** `compelling` is stronger than Art. 6(1)(f) `legitimate interests`. The `overriding` test for compelling grounds is undefined.

**Variant readings:**

- **R1:** `Compelling` = strictly necessary (lex specialis to legitimate interests).
  - *Source:* EDPB Guidelines on legitimate interests.
- **R2:** `Compelling` = materially more weighty than legitimate interests.
  - *Source:* Loose reading.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Compelling legitimate grounds = documented per-objection risk assessment with DPO sign-off.
- **Stakeholder Impact:** Travelers (data subjects), DPO, government authorities.
- **Risk:** MEDIUM — Art. 21 objection handling failure. Resolution: objection endpoint + manual review per request.
---

### 3.05 [GDPR] GDPR-CP19 — Art. 34(1)

- **Sub-domain:** D-01.3 (Cryptographic Key Management)
- **Title:** High-risk threshold
- **Type:** breach communication
- **Obligation type:** TRIGGERED (per high-risk breach)
- **Obligated party:** CONTROLLER

**Instance 1: POLY+VAG (S3)**

> **Verbatim phrase:** "likely to result in a high risk"

> **Analysis:** Three undefined qualifiers. The cross-clause threshold distinction (`risk` Art. 33 vs `high risk` Arts. 34, 35) is the central notification-litigation question.

**Variant readings:**

- **R1:** `High risk` = objectively elevated above ordinary processing risk.
  - *Source:* EDPB Guidelines 9/2022.
- **R2:** `High risk` = severe impact on data subject's rights.
  - *Source:* CNIL guidance.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Art. 34(1) communication to data subject within Art. 12(3) one-month clock; high-risk + Art. 9 fingerprint triggers immediate communication.
- **Stakeholder Impact:** Travelers, DPO, government authorities, DPA.
- **Risk:** HIGH — Art. 34(1) failure on biometric = Art. 83(5) fine. Resolution: communication template per Art. 34(3); DPO oversight on biometric-data breach communication.
---

### 3.06 [GDPR] GDPR-CP20 — Art. 34(3)

- **Sub-domain:** D-01.3 (Cryptographic Key Management)
- **Title:** Exceptions to data-subject communication
- **Type:** breach communication exception
- **Obligation type:** PER-BREACH
- **Obligated party:** CONTROLLER

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "render the personal data unintelligible"

> **Analysis:** `Unintelligible` (typically achieved via encryption) inherits the encryption-key-management question. If keys are lost, data is unintelligible in one sense but inaccessible to legitimate users too.

**Instance 2: VAG (S3)**

> **Verbatim phrase:** "disproportionate effort"

> **Analysis:** Same Berry-flagged phrase as Art. 14(5)(b). S3 because the exception triggers instead-of notification duty, materially distinct compliance outcome.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Art. 34(3) exceptions (encrypted, disproportionate effort, individual not identifiable) interpreted strictly; biometric Art. 9 data fails the encryption carve-out only if AES-256 + HSM-backed key + cryptographic sharding + AI_Act log re-identification prevented.
- **Stakeholder Impact:** DPO, CISO, travelers.
- **Risk:** MEDIUM — Art. 34(3) carve-out mis-application. Resolution: HSM-backed cryptographic sharding + anonymised AI_Act log per T-002.
---

### Article 35 — Data protection impact assessment

#### Verbatim (with highlighting)

> Article 35
> Data protection impact assessment
>
> 1. Where a type of processing in particular using new technologies, and taking into account the nature, scope, context and purposes of the processing, is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall, prior to the processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data. A single assessment may address a set of similar processing operations that present similar high risks.

> 2. The controller shall seek the advice of the data protection officer, where designated, when carrying out a data protection impact assessment.

> 3. A data protection impact assessment referred to in paragraph 1 shall in particular be required in the case of:

> (a) a systematic and extensive evaluation of personal aspects relating to natural persons which is based on automated processing, including profiling, and on which decisions are based that produce legal effects concerning the natural person or similarly significantly affect the natural person;

> (b) processing on a large scale of special categories of data referred to in Article 9(1), or of personal data relating to criminal convictions and offences referred to in Article 10; or

> (c) a systematic monitoring of a publicly accessible area on a large scale.

> 4. The supervisory authority shall establish and make public a list of the kind of processing operations which are subject to the requirement for a data protection impact assessment pursuant to paragraph 1. The supervisory authority shall communicate those lists to the Board referred to in Article 68.

> 5. The supervisory authority may also establish and make public a list of the kind of processing operations for which no data protection impact assessment is required.

> 6. Prior to the adoption of the lists referred to in paragraphs 4 and 5, the competent supervisory authority shall apply the consistency mechanism referred to in Article 63 where such lists involve processing activities which are related to the offering of goods or services to data subjects or to the monitoring of their behaviour in several Member States, or may substantially affect the free movement of personal data within the Union.

> 7. The assessment shall contain at least:

> (a) a systematic description of the envisaged processing operations and the purposes of the processing, including, where applicable, the legitimate interest pursued by the controller;

> (b) an assessment of the necessity and proportionality of the processing operations in relation to the purposes;

> (c) an assessment of the risks to the rights and freedoms of data subjects referred to in paragraph 1;

> (d) the measures envisaged to address the risks, including safeguards, security measures and mechanisms to ensure the protection of personal data and to demonstrate compliance with this Regulation taking into account the rights and legitimate interests of data subjects and other persons concerned.

> 8. Compliance with approved codes of conduct referred to in Article 40 by the relevant controllers or processors shall be taken into due account in assessing the impact of the processing operations performed by such controllers or processors, in particular for the purposes of a data protection impact assessment.

> 9. Where appropriate, the controller shall seek the views of data subjects or their representatives on the intended processing, without prejudice to the protection of commercial or public interests or the security of processing operations.

> 10. Where processing pursuant to point (c) or (e) of Article 6(1) has a legal basis in Union law or in the law of the Member State to which the controller is subject, that law regulates the specific processing operation or set of operations in question, and a data protection impact assessment has already been carried out as part of a general impact assessment in the context of the adoption of that legal basis, paragraphs 1 to 7 shall not apply unless Member States deem it to be necessary to carry out such an assessment prior to processing activities.

> 11. Where necessary, the controller shall carry out a review to assess if processing is performed in accordance with the data protection impact assessment at least when there is a change of the risk represented by processing operations.

#### Clause breakdown

---

### 3.07 [GDPR] GDPR-RT08 — Art. 14(5)(b)

- **Sub-domain:** D-04.3 (Incident Notification & Reporting)
- **Title:** Disproportionate effort exception
- **Type:** information duty (exception)
- **Obligation type:** PER-CASE
- **Obligated party:** CONTROLLER

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "proves impossible or would involve a disproportionate effort"

> **Analysis:** `disproportionate effort` is the recurring vague phrase. Recital 62 attempts to fix as cost-vs-risk assessment. S3 because the exception is widely used to skip Article 14 notification in practice (e.g. large-scale behavioural advertising).

**Variant readings:**

- **R1:** Exception applies narrowly to research/archiving; controllers must demonstrate efforts.
  - *Source:* Recital 62 (non-binding).
- **R2:** Exception applies broadly; controllers judge what is disproportionate.
  - *Source:* Industry reading.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Art. 14(5)(b) disclosure limited to extent strictly necessary; indirect-source notice at first communication.
- **Stakeholder Impact:** DPO, travelers via privacy notice, government authorities.
- **Risk:** MEDIUM — Art. 14(5)(b) over-disclosure. Resolution: privacy notice at data collection point + indirect-source notice at first communication.
---

### 3.08 [GDPR] GDPR-RT11 — Art. 15(4)

- **Sub-domain:** D-04.3 (Incident Notification & Reporting)
- **Title:** Third-party rights
- **Type:** data subject right (scope limitation)
- **Obligation type:** PER-REQUEST
- **Obligated party:** CONTROLLER

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "shall not adversely affect the rights and freedoms of others"

> **Analysis:** Whose `rights and freedoms`? Other data subjects (whose data appears in shared records), the controller, third parties (employees, partners)? The clause does not differentiate.

**Variant readings:**

- **R1:** Redact only data identifying other natural persons.
  - *Source:* EDPB reading.
- **R2:** Redact any data that could affect other parties (incl. commercial confidentiality).
  - *Source:* Broad reading.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Art. 15(4) right to obtain copy = machine-readable format (JSON), one-month clock.
- **Stakeholder Impact:** DPO, travelers, government authorities.
- **Risk:** MEDIUM — Art. 15(4) format failure. Resolution: JSON export endpoint + DPO oversight.
---

### 3.09 [GDPR] GDPR-RT20 — Art. 23(1)

- **Sub-domain:** D-04.3 (Incident Notification & Reporting)
- **Title:** Permissible restriction grounds
- **Type:** principle (restrictions scope)
- **Obligation type:** PER-RESTRICTION
- **Obligated party:** MEMBER STATE

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "essence of the fundamental rights and freedoms"

> **Analysis:** `Essence` is Charter Art. 52(1) terminology. CJEU case law (Schrems I/II, Digital Rights Ireland) uses `essence` as a hard-test threshold but does not specify the operational test. S3 because Member State restrictions on Charter rights depend on the essence-test being met.

**Variant readings:**

- **R1:** `Essence` = the absolute core of the right (cannot be touched).
  - *Source:* CJEU Charter interpretation.
- **R2:** `Essence` = the proportionality balance of the right.
  - *Source:* Loose reading.

**Instance 2: COORD (S2)**

> **Verbatim phrase:** "(a) OR (b) OR (c) OR ... (j)"

> **Analysis:** 10 disjunctive grounds (Berry §5.4.7 menu-card pattern). S2 because all 10 grounds converge on the same scrutiny mechanism.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Art. 23(1) restrictions limited to Member State law scope; document per-restriction-scope in DPIA.
- **Stakeholder Impact:** DPO, government authorities, DPA.
- **Risk:** LOW — Art. 23(1) is a controller-side restriction; minimal impact on SecureBorder as processor. Resolution: document per-restriction-scope in DPIA.
---

### Chapter III synthesis

#### Counts

| Category | Instances | Clauses affected |
|---|---|---|
| VAG | 27 | 20 / 20 |
| POLY | 11 | 11 / 20 |
| COORD | 12 | 12 / 20 |
| SCOPE-Q | 3 | 3 / 20 |
| Total | 53 | 20 / 20 |

| Severity | Instances |
|---|---|
| S1 — Low | 0 |
| S2 — Medium | 34 |
| S3 — High | 19 |

#### Recurring patterns

- `Reasonable` (Berry-flagged) appears in 8 of 20 clauses — dominant vague term of Chapter III.
- 1-month + 2-month temporal pair (Art. 12(3)) is the only hard numeric anchor in the chapter; all other timelines are vague.
- ADM (Art. 22) overlaps with AI_Act Art. 13 — Chapter III Art. 22(3) `meaningful information about the logic` is the foundational obligation that the AI_Act operationalises for high-risk AI.

#### Cross-clause structural observations

1. Art. 12 is the procedural backbone. All other rights (Art. 13–22) depend on Art. 12's response-time, identity-verification, and refusal grounds.
2. Art. 13/14 split — collection-source vs third-party-source information duties are structurally parallel but with different timing rules (immediate vs 1-month). The third-party-source timing is the more lenient and more often waived.
3. Art. 15–22 cascade. Each right (access, rectification, erasure, restriction, portability, object, ADM) inherits Art. 12's procedural rules and Art. 5(1)(d) accuracy / Art. 5(1)(c) minimisation anchors. Cross-clause implementations can reuse components.
4. Art. 22 ADM — the most software-impact-relevant right in GDPR, with direct overlap to AI_Act's high-risk transparency requirements. Cross-regulatory coordination required.
5. Art. 23 restrictions — the Member State's escape valve from Chapter III. The `essence` test (Charter Art. 52(1)) is the constitutional backstop but its operationalisation is CJEU-driven.

#### Anti-pattern notes for downstream files

- Chapter IV inherits Chapter III rights via Art. 24(1) "implement appropriate technical and organisational measures" + Art. 25 by-design. `Appropriate measures` for rights-exercise includes consent-collection UIs, SAR portals, rectification workflows.
- Chapter V transfer mechanisms do not create new Chapter III rights but the Art. 15(2) right to be informed of transfer safeguards cross-references Chapter V.

---

### 3.10 [GDPR] GDPR-CP04 — Art. 26(1)

- **Sub-domain:** D-06.3 (Contractual Security Obligations)
- **Title:** Joint-controller determination
- **Type:** multi-controller
- **Obligation type:** CONTINUOUS
- **Obligated party:** CONTROLLER (joint)

**Instance 1: POLY (S3)**

> **Verbatim phrase:** "jointly determine"

> **Analysis:** Inherits Art. 4(7) `alone or jointly with others` ambiguity. The CJEU IAB Europe case (C-604/22, 2024) held that joint controllership can exist even when one party lacks direct influence on processing purposes — extending the scope of `jointly determine` beyond the original EDPB reading.

**Variant readings:**

- **R1:** `Jointly determine` = shared decision-making authority on purposes.
  - *Source:* EDPB Guidelines 07/2020 (original).
- **R2:** `Jointly determine` = either party having determinative influence on purposes.
  - *Source:* CJEU IAB Europe (C-604/22).


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Joint controllers arrangement with government (out of SecureBorder's control scope); transparent allocation of GDPR obligations.
- **Stakeholder Impact:** DPO, government authorities, Legal Counsel.
- **Risk:** MEDIUM — Art. 26 transparency arrangement. Resolution: documented joint-controller arrangement with government; SecureBorder's role is processor.
---

### 3.11 [NIS 2] NIS2-CL07 — Art. 21(1) sentence 1

- **Sub-domain:** D-01.1 (Data at Rest Encryption)
- **Title:** Risk-management core obligation
- **Type:** (n/a)
- **Obligation type:** (n/a)
- **Obligated party:** (n/a)

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "appropriate and proportionate"

> **Analysis:** The opening qualifier. Three materially distinct readings:

- R1: `appropriate` and `proportionate` are independent (entity must satisfy both tests, separately).
- R2: `appropriate` modifies `proportionate` (entity must satisfy proportionality, with `appropriate` as a placeholder synonym).
- R3: `appropriate and proportionate` is a single compound qualifier (a fixed phrase).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Independent | None in OJ |
| R2 | Hierarchical | None in OJ |
| R3 | Compound | In-Directive: Art. 21(1) sentence 2 operationalises proportionality by specific factors (exposure, size, likelihood, severity) |

R1 and R3 produce materially distinct compliance obligations (R1 admits two separate failure modes; R3 admits one composite test). S3.

This is the dominant VAG trigger of NIS 2. It propagates to all 10 sub-points of Art. 21(2)(a)–(j) and to Art. 21(3) and Art. 21(4). Every measure listed in Art. 21(2) inherits the `appropriate and proportionate` qualifier by reference to "The measures referred to in paragraph 1".

**Instance 2: POLY (S2)**

> **Verbatim phrase:** "technical, operational and organisational measures"

> **Analysis:** Three-term coordination. Three readings:

- R1: Three distinct categories of measures (entity must implement at least one of each).
- R2: Cumulative description (a measure is "technical, operational and organisational" if it has all three characteristics).
- R3: Open list (entity may add more categories).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Distinct categories | In-Directive: literal `technical, operational and organisational` |
| R2 | Cumulative single measure | None in OJ |
| R3 | Open list | In-Directive: recital 56 (proportionality) |

R1 is the literal reading. R3 is the dominant reading (recital 56 implies entity-discretion on additional categories). S2.

**Instance 4: POLY (S2)**

> **Verbatim phrase:** "impact"

> **Analysis:** `impact` — on recipients of services (downstream effect) or on other services (cascading effect)?

- R1: Impact on direct recipients.
- R2: Impact on other services (cascade).
- R3: Both.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Recipients | In-Directive: literal `recipients of their services` |
| R2 | Other services | In-Directive: literal `on other services` |
| R3 | Both | In-Directive: literal `recipients … and … other services` |

R3 is the literal reading (coordinated by `and`). The fact that the two objects are coordinated by AND rather than OR means the entity must consider impact on both. S2 because the surface ambiguity is between "focus on direct recipients" and "consider cascading effects".


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Art. 21(1) sentence 1 chapeau risk-management measures = 10 OJ-explicit factors; risk assessment output is a single document that also discharges GDPR Art. 35 (DPIA) and AI_Act Art. 9 (AI risk-management system) on the same artefact (T-003).
- **Stakeholder Impact:** CISO, DPO, AI Governance Lead, external auditors.
- **Risk:** HIGH — Art. 21(1) failure on supply chain = NIS 2 management liability. Resolution: unified risk-assessment document per T-003 (DPIA+FRIA).
---

### 3.12 [NIS 2] NIS2-CL08 — Art. 21(1) sentence 2

- **Sub-domain:** D-01.1 (Data at Rest Encryption)
- **Title:** Risk-management factors
- **Type:** (n/a)
- **Obligation type:** (n/a)
- **Obligated party:** (n/a)

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "state-of-the-art"

> **Analysis:** Same Berry-classic vague term as GDPR Art. 25(1) and Art. 32(1). Three materially distinct readings:

- R1: `state-of-the-art` = current best practice (qualitative).
- R2: `state-of-the-art` = published standards (e.g. ISO/IEC 27001:2022, NIST CSF 2.0).
- R3: `state-of-the-art` = cutting-edge research (academic / frontier).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Best practice | In-Directive: `state-of-the-art and … standards` (R1 contrasts with R2) |
| R2 | Standards | In-Directive: same as R1 |
| R3 | Frontier | None in OJ |

R1 and R2 produce materially distinct obligations (R1 admits "industry-typical" measures; R2 mandates standards-based measures). R3 is rejected by recital 56 (cost-of-implementation consideration implies off-the-shelf). S3.

**Instance 2: VAG (S2)**

> **Verbatim phrase:** "cost of implementation"

> **Analysis:** `cost` — to whom? The entity's cost? The national-economy cost? The supply-chain cost?

- R1: Entity's cost.
- R2: National-economy cost (recital 56).
- R3: Supply-chain cost (R3 imports the Art. 21(2)(d) supply-chain frame).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Entity's cost | In-Directive: literal `cost of implementation` (the implementation is the entity's) |
| R2 | National-economy cost | In-Directive: recital 56 |
| R3 | Supply-chain cost | None in OJ |

R1 is the literal reading. R2 is a non-operational reading (national-economy cost is not assessable by the entity). R3 is T3-imposed (no support in the OJ text). S2.

**Instance 3: VAG (S2)**

> **Verbatim phrase:** "appropriate to the risks posed"

> **Analysis:** `appropriate to the risks posed` — what is the proportionality function?

- R1: Linear (proportional to exposure × likelihood × impact).
- R2: Tiered (mapped to entity's classification under Art. 3).
- R3: Risk-tiered (mapped to specific risk-assessment output).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Linear | None in OJ |
| R2 | Tiered | None in OJ; Art. 3 essential/important classification |
| R3 | Risk-tiered | In-Directive: Art. 21(1) sentence 2 lists risk factors |

R3 is the dominant reading. S2.

**Instance 4: VAG (S2)**

> **Verbatim phrase:** "the degree of the entity's exposure to risks"

> **Analysis:** `exposure` — exposure to threat? Exposure to impact? Exposure to incident likelihood?

- R1: Threat exposure.
- R2: Impact exposure (downstream).
- R3: Combined.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Threat | None in OJ |
| R2 | Impact | None in OJ |
| R3 | Combined | None in OJ; Art. 6(9) `risk` (loss or disruption) |

**Instance 5: VAG (S2)**

> **Verbatim phrase:** "the entity's size"

> **Analysis:** `size` — by employee count, by turnover, by balance sheet total, by user count? The Recommendation 2003/361/EC definition is the standard EU benchmark, but the Directive does not reference it.

- R1: Employee count.
- R2: Turnover.
- R3: Balance sheet total.
- R4: User count (a non-traditional measure for digital service providers).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Employees | In-Directive: Art. 3 cross-refs to Rec. 2003/361/EC (employee + turnover) |
| R2 | Turnover | In-Directive: same as R1 |
| R3 | Balance sheet | In-Directive: same as R1 |
| R4 | User count | None in OJ |

R1–R3 are the standard EU micro/small/medium/large measures. R4 is T3-imposable. S2.

**Instance 6: VAG (S2)**

> **Verbatim phrase:** "likelihood of occurrence of incidents and their severity"

> **Analysis:** `likelihood` + `severity` (AND). The two-factor risk-treatment.

- `likelihood` — same POLY as in Art. 6(9) (frequentist / Bayesian / qualitative).
- `severity` — same VAG as `severe` in Art. 23(3) (defines `significant incident`).

| # | Reading (likelihood) | Disambiguation source |
|---|---|---|
| R1 | Frequentist | None in OJ |
| R2 | Bayesian | None in OJ |
| R3 | Qualitative | None in OJ |

| # | Reading (severity) | Disambiguation source |
|---|---|---|
| R1 | Operational impact only | In-Directive: Art. 23(3)(a) `severe operational disruption` |
| R2 | Financial only | In-Directive: Art. 23(3)(a) `financial loss` |
| R3 | Societal + economic | In-Directive: literal `societal and economic impact` |
| R4 | Any | None in OJ; recital 56 |

R3 and R4 are operative. S2.

**Instance 7: VAG (S2)**

> **Verbatim phrase:** "societal and economic impact"

> **Analysis:** `societal` — collective harm to public welfare; `economic` — financial harm to markets or to the entity.

- R1: `societal` and `economic` are independent impact dimensions (entity must consider both).
- R2: `societal and economic` is a compound describing the type of impact.
- R3: `societal` = public-impact, `economic` = private-impact, and the AND binds them.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Independent dimensions | In-Directive: literal `societal and economic` |
| R2 | Compound description | None in OJ |
| R3 | Public + private | None in OJ; recital 56 |

R1 is the literal reading. S2.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Art. 21(1) sentence 2 risk-management factors = 10 OJ-explicit factors mandatory; single document discharges GDPR + AI_Act (T-003).
- **Stakeholder Impact:** CISO, DPO, AI Governance Lead.
- **Risk:** HIGH — Same as 3.11. Resolution: same as 3.11 (unified risk-assessment).
---

### 3.13 [NIS 2] NIS2-CL17 — Art. 21(2)(h)

- **Sub-domain:** D-01.1 (Data at Rest Encryption)
- **Title:** Cryptography and, where appropriate, encryption
- **Type:** (n/a)
- **Obligation type:** (n/a)
- **Obligated party:** (n/a)

**Instance 2: VAG (S2)**

> **Verbatim phrase:** "where appropriate"

> **Analysis:** Soft hedge on the encryption sub-obligation. Reading:

- R1: `appropriate` is determined by risk assessment.
- R2: `appropriate` is determined by state-of-the-art.
- R3: `appropriate` is determined by the entity's classification.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Risk-based | In-Directive: Art. 21(1) factors |
| R2 | State-of-the-art-based | In-Directive: Art. 21(1) sentence 2 |
| R3 | Classification-based | None in OJ |

R1 and R2 are operative. S2.

**Instance 3: COORD (S3)**

> **Verbatim phrase:** "cryptography AND, where appropriate, encryption"

> **Analysis:** AND of two terms where one is hedged. Three readings:

- R1: Cryptography always required; encryption required when appropriate.
- R2: Cryptography = encryption (the `where appropriate` applies to both).
- R3: Cryptography and encryption are alternatives (OR, not AND).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Hierarchical AND (cryptography always, encryption sometimes) | In-Directive: literal `cryptography and, where appropriate, encryption` |
| R2 | Equal AND with hedge on both | None in OJ |
| R3 | OR | None in OJ |

R1 is the literal reading. S3 because the surface ambiguity drives whether the entity can satisfy Art. 21(2)(h) by adopting only cryptography (R1: yes, with the hedge; R2: no; R3: no).


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — `Where appropriate` hedge on encryption admits narrower scope than GDPR's `appropriate`; AES-256 satisfies CRA state-of-the-art baseline.
- **Stakeholder Impact:** CISO, CTO, DPO.
- **Risk:** HIGH — Art. 21(2)(h) failure on biometric data. Resolution: AES-256-GCM + HSM-backed KMS + cryptography policy documented.
---

### 3.14 [NIS 2] NIS2-CL26 — Art. 23(1) ¶1

- **Sub-domain:** D-04.3 (Incident Notification & Reporting)
- **Title:** Notification to CSIRT (the core)
- **Type:** (n/a)
- **Obligation type:** (n/a)
- **Obligated party:** (n/a)

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "without undue delay"

> **Analysis:** The recurring Berry-classic vague term (GDPR Art. 33, CRA Art. 14, NIS 2 Art. 21(4)). Three materially distinct readings:

- R1: `without undue delay` = 24 hours (matches Art. 23(4)(a) early-warning hard anchor).
- R2: `without undue delay` = reasonable time considering the nature of the incident.
- R3: `without undue delay` = as soon as technically feasible.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | 24 h | In-Directive: Art. 23(4)(a) hard anchor |
| R2 | Reasonable | In-Directive: recital 60; standard EU drafting |
| R3 | Technically feasible | None in OJ |

R2 is the dominant reading. R1 is the practical baseline. S3.

**Instance 2: VAG (S3)**

> **Verbatim phrase:** "significant impact"

> **Analysis:** `significant impact` — the threshold term. Defined in Art. 23(3) (CL33 + CL34) but `significant impact` itself is shorthand for the test result. The reading:

- R1: `significant impact` = severe operational disruption (Art. 23(3)(a) test A).
- R2: `significant impact` = considerable damage to other persons (Art. 23(3)(b) test B).
- R3: Either test satisfied.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Test A only | In-Directive: Art. 23(3)(a) |
| R2 | Test B only | In-Directive: Art. 23(3)(b) |
| R3 | Either | In-Directive: literal `or` (Art. 23(3) chapeau) |

R3 is the literal reading (OR). S3 because R1/R2/R3 admit materially different compliance populations.

**Instance 3: POLY (S2)**

> **Verbatim phrase:** "incident"

> **Analysis:** Inherits Art. 6(6) `incident` definition: `an event compromising the availability, authenticity, integrity or confidentiality of stored, transmitted or processed data or of the services offered by, or accessible via, network and information systems`. Same POLY as Art. 6(6) and Art. 2 NIS 2 D02:

- R1: Security incident (intentional, malicious).
- R2: Operational incident (any disruption).
- R3: All-hazards (per Art. 21(2) chapeau).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Security | None in OJ; recital 32 |
| R2 | Operational | None in OJ |
| R3 | All-hazards | In-Directive: Art. 21(2) all-hazards approach |

R3 is the dominant reading. S2.

**Instance 4: POLY (S2)**

> **Verbatim phrase:** "CSIRT or competent authority"

> **Analysis:** Two alternative routing paths. Three readings:

- R1: CSIRT only (default).
- R2: Competent authority only (where no CSIRT).
- R3: Either (entity's choice).
- R4: Member State determines.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | CSIRT default | In-Directive: literal `CSIRT or, where applicable, its competent authority` |
| R2 | CA fallback | In-Directive: `where applicable` |
| R3 | Entity choice | None in OJ |
| R4 | MS-determined | In-Directive: literal `where applicable` is MS-determined |

R4 is the dominant reading. S2.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Confirmed and materialised incident (not probabilistic detection alone) starts the 24h clock; max-SLA 24h routing across NIS 2 + CRA + GDPR + AI_Act (T-001).
- **Stakeholder Impact:** CISO, DPO, Legal Counsel, CEO, AI Governance Lead, CSIRT, ENISA, DPA, Notified Body.
- **Risk:** CRITICAL — Late notification triggers 4 fines (GDPR + CRA + NIS 2 + AI_Act). Resolution: max-SLA 24h routing pipeline per T-001.
---

### 3.15 [NIS 2] NIS2-CL33 — Art. 23(3)(a)

- **Sub-domain:** D-04.3 (Incident Notification & Reporting)
- **Title:** Significant-incident test A
- **Type:** (n/a)
- **Obligation type:** (n/a)
- **Obligated party:** (n/a)

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "severe operational disruption"

> **Analysis:** `severe` — undefined; `operational disruption` — undefined. Three materially distinct readings:

- R1: `severe` = >X% of service capacity disrupted (e.g. >50% downtime).
- R2: `severe` = >X hours of downtime.
- R3: `severe` = qualitative judgment by management.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Capacity-based | None in OJ |
| R2 | Time-based | None in OJ |
| R3 | Qualitative | None in OJ; recital 56 |

R1 and R2 produce materially distinct compliance obligations (R1 requires capacity monitoring; R2 requires downtime tracking). R3 is rejected by Art. 23(11) implementing-acts. S3.

**Instance 2: VAG (S2)**

> **Verbatim phrase:** "operational disruption"

> **Analysis:** `operational` — what counts? Service outage? Performance degradation? Internal-process disruption?

- R1: Service outage.
- R2: Performance degradation.
- R3: Internal-process disruption.
- R4: All of the above.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Outage | In-Directive: literal `disruption` |
| R2 | Degradation | None in OJ |
| R3 | Internal | None in OJ |
| R4 | All | In-Directive: recital 56 |

R4 is the dominant reading. S2.

**Instance 3: COORD (S2)**

> **Verbatim phrase:** "caused OR is capable of causing"

> **Analysis:** The OR between actual and potential.

- R1: Past tense only — incidents that already caused disruption.
- R2: Future-tense only — incidents with the *capability* to cause disruption (preventive reporting).
- R3: Either.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Past | None in OJ |
| R2 | Future-capable | None in OJ |
| R3 | Either | In-Directive: literal `caused or is capable of causing` |

R3 is the literal reading. S2.

**Instance 4: COORD (S2)**

> **Verbatim phrase:** "severe operational disruption OR financial loss"

> **Analysis:** The OR between operational and financial impact.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Operational only | In-Directive: literal `operational disruption` |
| R2 | Financial only | In-Directive: literal `financial loss` |
| R3 | Either | In-Directive: literal `or` |

R3 is the literal reading. S2.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Early warning 24h limb + notification 72h limb are sequential; same max-SLA 24h routing pipeline (T-001).
- **Stakeholder Impact:** CISO, CSIRT, DPO, Legal Counsel.
- **Risk:** CRITICAL — Same as 3.14. Resolution: same as 3.14 (max-SLA 24h routing).
---

### 3.16 [CRA] CRA-CL02 — Art. 6(a) proviso

- **Sub-domain:** D-01.1 (Data at Rest Encryption)
- **Title:** Installation/use conditions
- **Type:** (n/a)
- **Obligation type:** (n/a)
- **Obligated party:** (n/a)

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "properly installed, maintained"

> **Analysis:** `properly` — what constitutes proper?

- R1: Per manufacturer instructions (Annex II §8).
- R2: Per industry standards.
- R3: Per a reasonable user's understanding.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Per instructions | In-Directive: Annex II §8 `necessary measures during initial commissioning` |
| R2 | Per industry | None in OJ |
| R3 | Per reasonable user | None in OJ |

R1 is the literal reading. R2/R3 admit materially different compliance populations. S3.

**Instance 2: VAG (S3)**

> **Verbatim phrase:** "intended purpose or under conditions which can reasonably be foreseen"

> **Analysis:** `intended purpose` (Art. 3(23)) OR `reasonably foreseeable` (Art. 3(24)) — alternative conditions.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Intended purpose OR foreseeable | In-Directive: literal `or` |
| R2 | Intended purpose ONLY | None in OJ |
| R3 | Foreseeable ONLY | None in OJ |

R1 is the literal reading. S3.

**Instance 3: VAG (S2)**

> **Verbatim phrase:** "where applicable, the necessary security updates have been installed"

> **Analysis:** `necessary security updates` — which updates are necessary?

- R1: Critical security updates only.
- R2: All security updates.
- R3: Updates required by Annex I Part II §3 (effective and regular tests).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Critical | None in OJ |
| R2 | All | In-Directive: Annex I Part II §3 |
| R3 | Per Annex I | In-Directive: Annex I Part II §3 |

R2 is the literal reading. S2.

**Instance 4: POLY (S2)**

> **Verbatim phrase:** "installed"

> **Analysis:** `installed` — software-only? Hardware? Firmware?

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Software | None in OJ |
| R2 | Hardware | None in OJ |
| R3 | Any | In-Directive: literal `installed` |

R3 is the literal reading. S2.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Per Annex II §8 (R1 literal reading); R3 fallback for kiosk deployments outside documented use conditions.
- **Stakeholder Impact:** CTO, CISO, Notified Body, government customers.
- **Risk:** HIGH — Art. 6(a) compliance failure. Resolution: R1 with R3 fallback for non-airport venues.
---

### 3.17 [CRA] CRA-CL51 — Art. 14(1) sentence 1

- **Sub-domain:** D-04.3 (Incident Notification & Reporting)
- **Title:** AEV notification duty
- **Type:** (n/a)
- **Obligation type:** (n/a)
- **Obligated party:** (n/a)

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "becomes aware of"

> **Analysis:** Same awareness-trigger pattern as NIS 2 Art. 23(4)(a)(b) and GDPR Art. 33(1).

- R1: Actual knowledge.
- R2: Constructive knowledge.
- R3: Either.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Actual | In-Directive: literal |
| R2 | Constructive | CJEU case law |
| R3 | Either | None in OJ |

R1 is the literal reading; R2 is the dominant judicial reading. S3.

**Instance 2: POLY (S2)**

> **Verbatim phrase:** "actively exploited vulnerability"

> **Analysis:** Inherits Art. 3(42) `actively exploited vulnerability` definition. Same POLY (D42) — `reliable evidence` + `without permission`. Propagates.

**Instance 3: VAG (S3)**

> **Verbatim phrase:** "simultaneously"

> **Analysis:** `simultaneously` — to both CSIRT and ENISA at the same time.

- R1: Same notification, same timestamp.
- R2: Same notification, same day.
- R3: Same notification, within a short window (hours).

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Same timestamp | In-Directive: literal |
| R2 | Same day | None in OJ |
| R3 | Short window | None in OJ |

R1 is the literal reading. R2/R3 are operational concessions. S3.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — "Actively exploited" requires observed exploitation in the wild affecting SecureBorder products or substantively similar products (per ENISA guidance); 24h clock starts at confirmed exploitation, not CVE publication.
- **Stakeholder Impact:** CISO, ENISA, CSIRT, Notified Body, government customers.
- **Risk:** CRITICAL — AEV reporting failure = CRA Art. 56 fine. Resolution: max-SLA 24h routing per T-001 + ENISA-aligned AEV definition.
---

### 3.18 [CRA] CRA-CL56 — Art. 14(3) sentence 1

- **Sub-domain:** D-04.3 (Incident Notification & Reporting)
- **Title:** Severe-incident notification duty
- **Type:** (n/a)
- **Obligation type:** (n/a)
- **Obligated party:** (n/a)

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "severe incident"

> **Analysis:** Inherits Art. 14(5) definition (CL61/CL62). Same definitional regress as NIS 2 Art. 23(3) `significant incident`.

- R1: Severity = operational disruption.
- R2: Severity = data compromise.
- R3: Severity = malicious code execution.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Operational | In-Directive: Art. 14(5)(a) |
| R2 | Data | In-Directive: Art. 14(5)(a) |
| R3 | Malicious code | In-Directive: Art. 14(5)(b) |

R1 vs R2 vs R3 produce materially distinct compliance populations. S3.

**Instance 2: VAG (S3)**

> **Verbatim phrase:** "becomes aware of"

> **Analysis:** Same awareness trigger as CL51. S3.

**Instance 3: VAG (S3)**

> **Verbatim phrase:** "simultaneously"

> **Analysis:** Same as CL51. S3.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Severe incident = confirmed and materialised product-security incident; 24h clock + 72h notification + 1 month final report.
- **Stakeholder Impact:** CISO, ENISA, CSIRT, Notified Body.
- **Risk:** CRITICAL — Severe incident reporting failure = CRA Art. 56 fine. Resolution: max-SLA 24h routing per T-001 + severity classification per CRA.
---

### 3.19 [CRA] CRA-CL61 — Art. 14(5)(a)

- **Sub-domain:** D-04.3 (Incident Notification & Reporting)
- **Title:** Severe-incident test A
- **Type:** (n/a)
- **Obligation type:** (n/a)
- **Obligated party:** (n/a)

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "negatively affects or is capable of negatively affecting"

> **Analysis:** Same pattern as NIS 2 Art. 23(3) `caused or is capable of causing`. Actual vs potential.

- R1: Past only (already affected).
- R2: Potential only (capable of affecting).
- R3: Either.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Past | In-Directive: literal |
| R2 | Potential | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |

R3 is the literal reading. S3.

**Instance 2: POLY (S2)**

> **Verbatim phrase:** "sensitive or important data or functions"

> **Analysis:** `data or functions` (same as Art. 3(44)) + `sensitive or important` (undefined qualifier).

- R1: `sensitive` = personal data.
- R2: `sensitive` = critical business data.
- R3: `sensitive` = any data whose loss has consequences.
- R4: `important` = essential to product function.
- R5: `important` = significant to user operations.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Personal data | None in OJ |
| R2 | Critical business | None in OJ |
| R3 | Consequential | None in OJ |
| R4 | Essential to product | None in OJ |
| R5 | Significant to user | None in OJ |

R5 is the broadest reading. S2.

**Instance 4: POLY (S2)**

> **Verbatim phrase:** "availability, authenticity, integrity or confidentiality"

> **Analysis:** Same four dimensions as NIS 2 Art. 6(2) D02. Inherits same POLY (authenticity undefined).


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Final report 1 month after incident handling; ongoing incident provision (Art. 14(5)(a)) allows progress report + final report on incident handling.
- **Stakeholder Impact:** CISO, ENISA, CSIRT, DPO.
- **Risk:** MEDIUM — Final report failure. Resolution: max-SLA 24h routing + ongoing incident provision per Art. 14(5)(a).
---

### 3.20 [CRA] CRA-CL62 — Art. 14(5)(b)

- **Sub-domain:** D-04.3 (Incident Notification & Reporting)
- **Title:** Severe-incident test B
- **Type:** (n/a)
- **Obligation type:** (n/a)
- **Obligated party:** (n/a)

**Instance 1: VAG (S3)**

> **Verbatim phrase:** "led or is capable of leading"

> **Analysis:** Same actual-vs-potential pattern as CL61. S3.

**Instance 2: POLY (S2)**

> **Verbatim phrase:** "malicious code"

> **Analysis:** `malicious code` — what counts?

- R1: Malware (traditional).
- R2: Exploit code.
- R3: Backdoor.
- R4: Any code with malicious intent.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Malware | None in OJ |
| R2 | Exploit | None in OJ |
| R3 | Backdoor | None in OJ |
| R4 | Any | In-Directive: literal `malicious code` |

R4 is the literal reading. S2.

**Instance 3: POLY (S2)**

> **Verbatim phrase:** "introduction or execution"

> **Analysis:** Two modes (OR).

- R1: Introduction only (presence).
- R2: Execution only (activity).
- R3: Either.

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | Presence | In-Directive: literal |
| R2 | Activity | In-Directive: literal |
| R3 | Either | In-Directive: literal `or` |

R3 is the literal reading. S2.


**Resolution (Sprint 5 enrichment):**

- **Recommended Variant:** R1 — Final report 1 month after incident handling; same as 3.19 but applied to significant incidents impacting product security.
- **Stakeholder Impact:** CISO, ENISA, CSIRT, DPO.
- **Risk:** MEDIUM — Same as 3.19. Resolution: same as 3.19 (max-SLA 24h routing + ongoing incident provision).
---

## 4. Recommended Disambiguation (Case-02 reading per top-20 card)

The Case-02 reading adopted in this register follows the **AEGIS Berry-lens conventions** preserved in the corpus per-card `considerations` blocks. Each top-20 card above has at least one variant reading (R1/R2/R3) documented verbatim from the corpus; the recommended reading is the **strict-but-defensible** interpretation that satisfies both regulatory accountability (GDPR Art. 5(2), CRA conformity assessment, NIS 2 Art. 21, AI_Act Art. 9) and operational reality at SecureBorder's HIGH complexity tier.

**General Case-02 disambiguation conventions:**

1. **`state of the art` (GDPR Art. 32, CRA Annex I)** → ISO 27001 + sector-specific best practices + ENISA state-of-the-art guidance at the time of design. Strictest floor applies (CRA discharges GDPR/NIS 2/DORA on a single artefact).
2. **`appropriate technical measures` (GDPR Art. 32)** → anchored to the five Art. 32(1) preamble factors documented in the DPIA.
3. **`deletes` (GDPR Art. 17, Art. 28(3)(g))** → cryptographic erasure (key destruction) where data is replicated; physical destruction only for single-copy storage media.
4. **`sufficient guarantees` (GDPR Art. 28(1))** → documented due-diligence (questionnaire + certifications + audit + sub-processor inventory) + Art. 28(3) contract clauses.
5. **`incident` (NIS 2 Art. 23, AI_Act Art. 73)** → confirmed and materialised incident (not probabilistic detection alone) for 24h clock; AI_Act 3-tier (15d / 2d / 10d) depends on incident category.
6. **`substantial public interest` (GDPR Art. 9(2)(g))** → government-contracted border control qualifies; documented per processing scope in the DPIA.
7. **`high-risk AI system` (AI_Act Annex III)** → Annex III §1 (biometric) + §7 (border control) both apply to GuardianGate; conformity assessment per Art. 43.
8. **`essential cybersecurity requirements` (CRA Art. 6 + Annex I)** → all Part I (1) requirements are mandatory (literal `only where` reading per Art. 6 chapeau); Part I (2) requirements are conditional on the risk assessment (Art. 13(3) carve-out — `shall indicate whether and, if so in what manner`); the `essential` modifier is mandatory floor, not minimum.
9. **`properly installed, maintained, used for intended purpose or under conditions reasonably foreseeable` (CRA Art. 6(a) proviso)** → per-manufacturer-instructions reading (Annex II §8 — R1 literal); industry-standard reading (R2 — admits materially different compliance populations); reasonable-user reading (R3 — strict but operationally fragile). Case-02 adopts **R1** with R3 fallback for kiosk deployments outside documented use conditions (e.g. non-airport venues).
10. **`risk-management factors` (NIS 2 Art. 21(1) sentence 2)** → the 10 OJ-explicit factors are mandatory for the Art. 21(1) all-hazards risk assessment; the risk-assessment output is a single document that also discharges GDPR Art. 35 (DPIA) and AI_Act Art. 9 (AI risk-management system) on the same artefact (resolves T-003 via unified DPIA+FRIA per Doc 07b §4 D-09.2).
11. **`CSIRT notification` (NIS 2 Art. 23(1) ¶1)** → confirmed and materialised incident (not probabilistic detection alone) starts the 24h clock; the `early warning` 24h limb and the `notification` 72h limb are sequential, not parallel — Case-02 adopts max-SLA 24h routing across NIS 2 + CRA + GDPR + AI_Act (resolves T-001 per Doc 07b §4 D-04.3).
12. **`AEV (actively-exploited vulnerability) notification` (CRA Art. 14(1) sentence 1)** → "actively exploited" requires observed exploitation in the wild affecting SecureBorder products or substantively similar products (per ENISA guidance); the 24h clock starts at confirmed exploitation, not at CVE publication.

**Distribution note.** The §3 top-20 selection (Sprint 4 fix) intentionally spans the three regulations with substantive corpus entries (GDPR 10 + NIS 2 5 + CRA 5); AI_Act entries are not surfaced because the corpus has 0 substantive AI_Act ambiguity cards (see §3 selection logic). The disambiguation conventions above cover all four applicable regulations regardless of §3 representation.

**Resolution status:** All 20 cards above are flagged `OPEN` in this register; resolution is deferred to Phase 2 / Phase 3, where the chosen reading is formalised in the per-clause specifications of `Doc11_Structured_Compliance_Matrix.md` and the strategic-tensions resolution document.

---

## N. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-08-06 | Sprint 2 Executor | Sprint 2 fill: collected 1071 ambiguity cards from corpus JSON sidecars, filtered to Case_02 applicable regs; documented top-20 cards verbatim with R1/R2/R3 readings; added per-sub-domain breakdown table; added recommended disambiguation conventions. |
| 1.1 | 2026-08-06 | Sprint 4 Executor | **V-02 fix:** §1 Summary and §2 breakdown table reconciled to canonical 35 active sub-domains per Doc 07b §4 — D-07.2 marked ACTIVE, D-08.3 marked NOT_ADDRESSED. NOT_ADDRESSED set is now `[D-07.4, D-08.3, D-09.3]`. **V-04 fix:** §3 Top-20 cards regenerated as 20 **distinct** clauses (was 3 distinct + 17 duplicates). New distribution: GDPR 10 + NIS 2 5 + CRA 5 + AI_Act 0 (corpus-gap noted). Selection logic: S3-first, RIGOROUS-preferred, regulatory round-robin, `(regulation, clause_id)` dedup. §4 disambiguation conventions extended with CRA Annex I, CRA Art. 6(a) proviso, NIS 2 Art. 21(1) risk-management factors, NIS 2 Art. 23 CSIRT notification, CRA Art. 14(1) AEV — covering the regulations now represented in §3. **No tier was changed** — this is a content-completeness fix, not a Track B modification. |

## N. See also

- **Corpus source:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` (per-sub-domain `<SD_ID>.json` sidecar — `ambiguity_cards[]` field)
- **Berry framework:** `00_METHODOLOGY/PREPROCESSING/AMBIGUITY_ANALYSIS/01_Framework.md`
- **Strategic tensions:** `Doc08_Regulatory_Applicability.md §6` (T-001 Temporal, T-002 Cryptographic, T-003 TRIGGER_MISMATCH)
