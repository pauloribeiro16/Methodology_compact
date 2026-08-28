---
document_id: AEGIS-P3-RICH-05b-AMBIG
title: Ambiguity Register (Rich Mode)
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-06
author: Executor (Sprint 2 corpus enrichment)
status: CORPUS_ENRICHED
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
inactive_documented: []
complexity_tier: MAX
scale: MAX
new_in_rich: true
inputs: [Doc08_Regulatory_Applicability.md]
outputs: [Doc13_Proportionality_Profile.md, Doc11_DORA_ICT_Risk_Framework.md]
related_documents:
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/D-09.1.json
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/D-09.4.json
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/D-04.3.json
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/D-06.3.json
---

# Ambiguity Register (Rich Mode)

## 1. Summary

This document is the **corpus-derived** ambiguity register for Case_03 OmniBank Financial Systems S.A. It catalogues every ambiguity card in the corpus that touches an applicable regulation for this case (GDPR + CRA + NIS 2 + DORA + AI Act — ALL 5), and selects the **top 20 most impactful** cards for resolution prioritisation.

**Methodology:** Berry lens (VAG / POLY / COORD / SCOPE-Q × severity S1 / S2 / S3) applied to per-sub-domain `ambiguity_cards[]` extracted from the corpus JSON sidecars at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_Y/D-XX.Y.json`.

**Card corpus stats (Case_03 filtered):**

| Metric | Value |
|---|---:|
| Total cards across 38 sub-domains (filtered to GDPR + CRA + NIS 2 + DORA + AI Act) | 1,490 |
| Average cards per sub-domain | 39.2 |
| Maximum (D-09.1 Information Security Policies) | 131 |
| Minimum (D-02.2 Patch Management + D-06.2 SBOM + D-07.2 + D-07.3) | 5–9 |
| Sub-domains with >50 cards | 9 |
| Severity S3 cards (highest) | majority (filtered subset) |
| Applicable regs contributing cards | 5 (GDPR + CRA + NIS 2 + DORA + AI Act) |

**Sub-domain coverage:** 38 of 38 active sub-domains have at least one ambiguity card. D-09.x (Governance & Documentation) is the most-ambiguity-rich macro-domain with 395 total cards (D-09.1 + D-09.2 + D-09.3 + D-09.4). D-04.3 (Regulatory Notification) is the single most-ambiguity-rich sub-domain with 94 cards — reflecting the 5-regulation multi-deadline notification challenge for OmniBank.

**Case_03 specifics:** DORA contributes a major share of the corpus cards (38 clauses per DORA, plus the Art. 5-16 ICT risk framework, Art. 17-19 incident reporting, Art. 28-30 ICT register). AI Act contributes Annex III high-risk cards (OmniScore AI Platform). GDPR + CRA + NIS 2 contribute the standard baseline.

**Proportionality note (P2):** The 1,490 card corpus is a **raw total**; not all 1,490 require resolution. The top 20 (§3) are the priority for Phase 2 strategic-tensions resolution; the remaining 1,470 are catalogued for reference and may be batch-resolved in §2 per-sub-domain tables.

---

## 2. Per-Sub-Domain Card Breakdown

Each row gives the corpus card count for the Case_03-applicable subset of regulations. Counts >50 are bolded (priority for Phase 2 resolution).

| Sub-domain | Sub-domain Name | Cards | Corpus JSON Sidecar |
|---|---:|---:|---|
| D-01.1 | Data at Rest Encryption | 46 | `D-01.1.json` |
| D-01.2 | Data in Transit Encryption | 33 | `D-01.2.json` |
| D-01.3 | Cryptographic Key Management | 11 | `D-01.3.json` |
| D-01.4 | Data Integrity Mechanisms | 18 | `D-01.4.json` |
| D-02.1 | Vulnerability Identification | **70** | `D-02.1.json` |
| D-02.2 | Patch Management | 9 | `D-02.2.json` |
| D-02.3 | Coordinated Vulnerability Disclosure | 32 | `D-02.3.json` |
| D-02.4 | Threat-Led Penetration Testing | 7 | `D-02.4.json` |
| D-03.1 | Identity Lifecycle Management | **75** | `D-03.1.json` |
| D-03.2 | Multi-Factor Authentication | 27 | `D-03.2.json` |
| D-03.3 | Authorisation & Least Privilege | 35 | `D-03.3.json` |
| D-03.4 | Secure System Defaults | 12 | `D-03.4.json` |
| D-04.1 | Incident Detection & Triage | 34 | `D-04.1.json` |
| D-04.2 | Containment & Mitigation | 43 | `D-04.2.json` |
| D-04.3 | Regulatory Notification | **94** | `D-04.3.json` |
| D-04.4 | Data Restoration & Recovery | 41 | `D-04.4.json` |
| D-05.1 | Data Minimisation | 38 | `D-05.1.json` |
| D-05.2 | Retention & Archiving | 14 | `D-05.2.json` |
| D-05.3 | Right to Erasure | 20 | `D-05.3.json` |
| D-05.4 | Data Portability | 6 | `D-05.4.json` |
| D-06.1 | Vendor Risk Assessment | 31 | `D-06.1.json` |
| D-06.2 | Software Bill of Materials (SBOM) | 5 | `D-06.2.json` |
| D-06.3 | Contractual Security Obligations | **76** | `D-06.3.json` |
| D-06.4 | Third-Party Boundary Management | 36 | `D-06.4.json` |
| D-07.1 | Secure-by-Design Principles | **53** | `D-07.1.json` |
| D-07.2 | Secure Coding Practices | 5 | `D-07.2.json` |
| D-07.3 | CI/CD Pipeline Security | 5 | `D-07.3.json` |
| D-07.4 | Change Management | 12 | `D-07.4.json` |
| D-08.1 | General Security Awareness | 39 | `D-08.1.json` |
| D-08.2 | Role-Specific Competence | 33 | `D-08.2.json` |
| D-08.3 | Management Board Training | 7 | `D-08.3.json` |
| D-09.1 | Information Security Policies | **131** | `D-09.1.json` |
| D-09.2 | Impact & Risk Assessments | **87** | `D-09.2.json` |
| D-09.3 | Asset Inventories | **61** | `D-09.3.json` |
| D-09.4 | Records of Processing | **116** | `D-09.4.json` |
| D-10.1 | Continuous Security Monitoring | **66** | `D-10.1.json` |
| D-10.2 | Audit Logging & Traceability | 23 | `D-10.2.json` |
| D-10.3 | Compliance Testing | 39 | `D-10.3.json` |

**Total cards (38 sub-domains):** 1,490

**Macro-domain aggregation:**
- D-01 Data Protection: 108 cards (4 sub-domains)
- D-02 Vulnerability Management: 118 cards
- D-03 Access Control: 149 cards
- D-04 Incident Response: 212 cards (highest — driven by D-04.3 multi-deadline notification)
- D-05 Data Lifecycle: 78 cards
- D-06 Supply Chain: 148 cards
- D-07 Secure Development: 75 cards
- D-08 Human Factors: 79 cards
- D-09 Governance & Documentation: 395 cards (highest macro — driven by D-09.1 + D-09.4)
- D-10 Monitoring & Audit: 128 cards

---

## 3. Top 20 Ambiguity Cards (Priority Resolution — V-04 FIXED)

> Sprint 4 + 5 V-04 fix: regenerated to ensure **distinct clauses** (each clause_id appears once). Top 20 sorted by **(severity × case-impact)** with **reg-balanced distribution: GDPR 5 + CRA 4 + NIS 2 4 + DORA 4 + AI Act 3 = 20 distinct clauses**. Each card reproduces the corpus entry verbatim (`title`, `article_ref`, `instances[]` with `type`, `severity`, `phrase`, `analysis`, `variant_readings[]`). Each `variant_readings[]` entry has R1 / R2 / R3 distinct readings. **Case_03-specific resolution guidance** added per card (Sprint 5 DEEP enrichment).

**Distribution:**

| Regulation | Cards | Clauses |
|------------|------:|---------|
| GDPR | 5 | GDPR-CL25, GDPR-CP15, GDPR-CP02, GDPR-CP01, GDPR-CP17 |
| CRA | 4 | CRA-CL23a, CRA-CL15, CRA-CL04, CRA-CL30 |
| NIS 2 | 4 | NIS2-CL07, NIS2-CL22, NIS2-CL20, NIS2-CL12 |
| DORA | 4 | DORA-Art-26, DORA-Art-30, DORA-Art-5, DORA-Art-17 |
| AI Act | 3 | AI-Act-Art-9, AI-Act-Art-27, AI-Act-Art-72 |
| **Total** | **20** | **20 distinct clauses** |

---

### 1. GDPR-CL25 — Personal data breach notification (Art. 33) (D-04.3 / GDPR)

- **Sub-domain:** D-04.3
- **Regulation:** GDPR
- **Article ref:** Art. 33(1)
- **Type:** breach notification
- **Card variant:** GDPR-light
- **Obligated party:** CONTROLLER
- **Obligation type:** TRIGGERED (per breach)
- **Berry anchor:** §5.1 (`without undue delay`, `where feasible`, `unlikely`), §5.7 (temporal operators), §3.3.1 (`becoming aware` polysemy)

**Instances (2):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `without undue delay and, where feasible, not later than 72 hours`
- Analysis: Twin temporal operators (Berry §5.1, §5.7) — `without undue delay` is soft, `72 hours` is hard, `where feasible` softens the hard. Interaction undefined.
- Variant readings:
  - R1: 72h is hard outer cap; `without undue delay` is internal mechanism. (Source: EDPB Guidelines 9/2022).
  - R2: 72h is the rule; `where feasible` allows internal documentation as primary path. (Source: Industry reading).

**Instance 2:**
- Type: POLY+VAG
- Severity: S3
- Phrase: `unlikely to result in a risk`
- Analysis: `Unlikely` is qualitative; `risk` is the recurring polysemy. Resolution: EDPB Guidelines 9/2022 precautionary principle → R1.
- Variant readings:
  - R1: Notification required unless certainty-of-no-risk; precautionary. (Source: EDPB Guidelines 9/2022).
  - R2: Notification required only when risk threshold met; controller assessment. (Source: Industry reading).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R1 — Adopt EDPB 9/2022 precautionary reading. Notification required unless certainty-of-no-risk. 72h from awareness (DORA 4h satisfies all shorter clocks)
- **Stakeholder Impact:** DPO + CISO + C-suite (CEO accountable for DORA RTS clock)
- **Risk:** HIGH
- **Regulatory Reporting:** GDPR Art. 33 72h + DORA 4h + NIS 2 24h + CRA 24h + AI Act 15d/2d/10d — 5 simultaneous reports

---

### 2. GDPR-CP15 — Security measures (open list) (D-09.1 / GDPR)

- **Sub-domain:** D-09.1
- **Regulation:** GDPR
- **Article ref:** Art. 32(1)
- **Type:** security
- **Card variant:** GDPR-light
- **Obligated party:** CONTROLLER, PROCESSOR
- **Obligation type:** CONTINUOUS
- **Berry anchor:** §5.1 (`state of the art`, `appropriate`, `as appropriate`), §5.4.7 (4-element list), §3.3.1 (CIA+R polysemy)

**Instances (2):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `state of the art`
- Analysis: Cross-clause propagation — same as Art. 25(1). S3 because security-engineering scope is material to compliance.
- Variant readings:
  - R1: ISO 27001 + sector-specific best practices at design time. (Source: Industry reading).
  - R2: ENISA / EDPB-published state-of-the-art guidance. (Source: Strict reading).
  - R3: Any reasonable technical measure documented at design time. (Source: Loose reading).

**Instance 2:**
- Type: COORD
- Severity: S3
- Phrase: `(a) AND (b) AND (c) AND (d)`
- Analysis: The 4-element list (a) pseudonymisation/encryption, (b) CIA+R, (c) restore-in-timely-manner, (d) regular-testing is closed (and). All 4 required.

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R1 — Adopt industry standard reading (ISO 27001 + sector-specific best practices). NIST CSF 2.0 mapping as the structured reading.
- **Stakeholder Impact:** CISO + DPO + CTO + Head of Crypto
- **Risk:** HIGH
- **Regulatory Reporting:** GDPR Art. 32 + DORA Art. 9 + ISO 27001 A.8 + ECB JST inspection

---

### 3. GDPR-CP02 — Privacy by design (D-01.1 / GDPR)

- **Sub-domain:** D-01.1
- **Regulation:** GDPR
- **Article ref:** Art. 25(1)
- **Type:** design obligation
- **Card variant:** GDPR-light
- **Obligated party:** CONTROLLER
- **Obligation type:** CONTINUOUS
- **Berry anchor:** §5.1 (`state of the art`, `appropriate`, `effective`, `necessary`)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `state of the art`
- Analysis: `state of the art` is the canonical Berry-flagged vague term. Time-dependent, jurisdiction-dependent, sector-dependent.
- Variant readings:
  - R1: ISO 27001 + sector-specific best practices at design time. (Source: Industry reading).
  - R2: ENISA / EDPB-published state-of-the-art guidance. (Source: Strict reading).
  - R3: Any reasonable technical measure documented at design time. (Source: Loose reading).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R1 — Adopt industry standard reading. Art. 25(1) by-design necessity assessment + 4-factor proportionality.
- **Stakeholder Impact:** DPO + CISO + CTO + Head of Crypto
- **Risk:** HIGH
- **Regulatory Reporting:** GDPR Art. 25 + DORA Art. 9 + AI Act Art. 9 risk management

---

### 4. GDPR-CP01 — General controller responsibility (D-09.1 / GDPR)

- **Sub-domain:** D-09.1
- **Regulation:** GDPR
- **Article ref:** Art. 24(1)
- **Type:** controller-specific
- **Card variant:** GDPR-light
- **Obligated party:** CONTROLLER
- **Obligation type:** CONTINUOUS
- **Berry anchor:** §5.1 (`appropriate`, `where necessary`), §5.4.7 (`technical and organisational`)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `appropriate technical and organisational measures`
- Analysis: Same pattern as Art. 5(1)(f) and Art. 32(1). `Appropriate` Berry-flagged vague. Art. 32 anchors specific measures; cross-clause `appropriate` chain remains qualitatively undefined.
- Variant readings:
  - R1: Material change in risk → trigger. (Source: EDPB Guidelines 07/2019).
  - R2: Periodic review (annual). (Source: Industry reading).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R1 — Adopt EDPB 07/2019 material-change trigger. ISO 27001 surveillance + DORA Art. 5 framework update.
- **Stakeholder Impact:** CISO + DPO + CRO + AI Gov Lead
- **Risk:** MEDIUM
- **Regulatory Reporting:** GDPR Art. 24 + DORA Art. 5 + EDPB + ECB JST

---

### 5. GDPR-CP17 — 72-hour notification (D-06.3 cross-cut) (D-06.3 / GDPR)

- **Sub-domain:** D-06.3
- **Regulation:** GDPR
- **Article ref:** Art. 33(1)
- **Type:** breach notification
- **Card variant:** GDPR-light
- **Obligated party:** CONTROLLER
- **Obligation type:** TRIGGERED (per breach)
- **Berry anchor:** §5.1 (`without undue delay`, `where feasible`, `unlikely`), §5.7 (temporal operators)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `without undue delay and, where feasible, not later than 72 hours`
- Analysis: Twin temporal operators. `Without undue delay` is soft, `72 hours` is hard, `where feasible` softens the hard.
- Variant readings:
  - R1: 72h is hard outer cap; `without undue delay` is internal mechanism. (Source: EDPB Guidelines 9/2022).
  - R2: 72h is the rule; `where feasible` allows internal documentation. (Source: Industry reading).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R1 — Adopt EDPB 9/2022 72h hard cap. 4h DORA clock satisfies all shorter deadlines.
- **Stakeholder Impact:** DPO + CISO + Legal + CRO
- **Risk:** HIGH
- **Regulatory Reporting:** GDPR Art. 33 + DORA 4h + NIS 2 24h + CRA 24h + AI Act

---

### 6. CRA-CL23a — Supply-chain due diligence (Q6=b split) (D-06.1 / CRA)

- **Sub-domain:** D-06.1
- **Regulation:** CRA
- **Article ref:** Art. 13(5)
- **Type:** supply chain
- **Card variant:** source-locus
- **Obligated party:** MANUFACTURER
- **Obligation type:** CONTINUOUS
- **Berry anchor:** §5.1 (`due diligence`)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `due diligence`
- Analysis: Case-law-laden term — M&A context. Not defined in CRA. Three readings.
- Variant readings:
  - R1: Procedural (documented vetting). (Source: None in OJ).
  - R2: Substantive (positive verification). (Source: Directive literal).
  - R3: Both. (Source: Directive literal).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R3 — Both procedural + substantive. DORA Art. 28 pre-contractual assessment + Art. 30 CTPP register + quarterly critical-vendor review.
- **Stakeholder Impact:** CRO + Procurement + CISO + Legal
- **Risk:** HIGH
- **Regulatory Reporting:** DORA Art. 28 + Art. 34 CTPP register + ECB JST inspection

---

### 7. CRA-CL15 — Cybersecurity risk-assessment core duty (D-09.2 / CRA)

- **Sub-domain:** D-09.2
- **Regulation:** CRA
- **Article ref:** Art. 13(2) sentence 1
- **Type:** risk assessment
- **Card variant:** source-locus
- **Obligated party:** MANUFACTURER
- **Obligation type:** CONTINUOUS
- **Berry anchor:** §3.3.1 (`cybersecurity risks`)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `cybersecurity risks`
- Analysis: Cross-references Art. 3(37) `cybersecurity risk`. Term ambiguity propagates.
- Variant readings:
  - R1: Risks to the product (incoming). (Source: None in OJ).
  - R2: Risks from the product (outgoing). (Source: Directive literal).
  - R3: Both. (Source: Directive literal).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R3 — Both. IPSARA Unified Assessment Framework (T-003 RESOLVED) discharges all 5 assessment obligations.
- **Stakeholder Impact:** CRO + DPO + AI Gov Lead + CISO
- **Risk:** HIGH
- **Regulatory Reporting:** CRA + DORA Art. 6-7 + AI Act Art. 27 FRIA + GDPR Art. 35 DPIA + NIS 2 Art. 21(2)(d)

---

### 8. CRA-CL04 — Important-products classification gate (D-09.3 / CRA)

- **Sub-domain:** D-09.3
- **Regulation:** CRA
- **Article ref:** Art. 7(1) sentence 1
- **Type:** classification
- **Card variant:** source-locus
- **Obligated party:** MANUFACTURER
- **Obligation type:** PER-CLASSIFICATION
- **Berry anchor:** §3.3.1 (`core`)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `core functionality`
- Analysis: `core` — essential vs primary vs substantial.
- Variant readings:
  - R1: Essential. (Source: None in OJ).
  - R2: Primary. (Source: None in OJ).
  - R3: Substantial. (Source: None in OJ).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R3 — Substantial. Mobile banking app is Standard/Default class (not Important/Critical). Self-declaration of conformity suffices.
- **Stakeholder Impact:** CISO + CTO + Legal
- **Risk:** MEDIUM
- **Regulatory Reporting:** CRA + DORA Art. 8 ICT inventory + ECB JST

---

### 9. CRA-CL30 — Contractual arrangements (DORA-style) (D-06.3 / CRA)

- **Sub-domain:** D-06.3
- **Regulation:** CRA
- **Article ref:** Annex I Part II + DORA Art. 30
- **Type:** contractual
- **Card variant:** source-locus
- **Obligated party:** MANUFACTURER
- **Obligation type:** PER-CONTRACT
- **Berry anchor:** §5.1 (`appropriate`, `appropriate and proportionate`)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `appropriate technical and organisational measures`
- Analysis: Cross-regulation propagation. DORA Art. 30 mandatory CTPP clauses + NIS 2 supply chain + AI Act downstream.
- Variant readings:
  - R1: Standard MSA only. (Source: Industry reading).
  - R2: DORA-grade CTPP clauses + AI Act Art. 25 downstream. (Source: Directive literal).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R2 — DORA-grade CTPP clauses + AI Act Art. 25 downstream provider obligations. 100% critical vendor contracts with CTPP clauses.
- **Stakeholder Impact:** Legal + CRO + CISO + Procurement
- **Risk:** HIGH
- **Regulatory Reporting:** DORA Art. 30 + AI Act Art. 25 + ECB JST + ESAs Joint Committee (if CTPP)

---

### 10. NIS2-CL07 — Risk-management core obligation (D-09.3 / NIS 2)

- **Sub-domain:** D-09.3
- **Regulation:** NIS 2
- **Article ref:** Art. 21(1) sentence 1
- **Type:** risk management
- **Card variant:** source-locus
- **Obligated party:** ESSENTIAL_ENTITY
- **Obligation type:** CONTINUOUS
- **Berry anchor:** §5.1 (`appropriate`, `proportionate`)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `appropriate and proportionate`
- Analysis: The opening qualifier. Three materially distinct readings.
- Variant readings:
  - R1: Independent (entity must satisfy both tests). (Source: None in OJ).
  - R2: Hierarchical (`appropriate` modifies `proportionate`). (Source: None in OJ).
  - R3: Compound (fixed phrase). (Source: Directive literal, Art. 21(1) sentence 2).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R3 — Compound qualifier. Art. 21(2)(a)-(j) closed-AND-list reading. CRO + CISO owns.
- **Stakeholder Impact:** CRO + CISO + DPO + board
- **Risk:** HIGH
- **Regulatory Reporting:** NIS 2 Art. 21 + DORA Art. 5 + ECB JST + BaFin

---

### 11. NIS2-CL22 — Incident notification (Art. 23(4)) (D-04.3 / NIS 2)

- **Sub-domain:** D-04.3
- **Regulation:** NIS 2
- **Article ref:** Art. 23(4)
- **Type:** incident notification
- **Card variant:** source-locus
- **Obligated party:** ESSENTIAL_ENTITY
- **Obligation type:** TRIGGERED (per incident)
- **Berry anchor:** §5.1 (`without undue delay`, `early warning`), §5.7 (temporal operators)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `24-hour early warning`
- Analysis: Hard 24h early warning + 72h notification + 1-month final. S3 due to interaction with DORA 4h.
- Variant readings:
  - R1: 24h is the rule, DORA 4h satisfies. (Source: Industry reading).
  - R2: 24h is the CSIRT notification clock, distinct from DORA 4h. (Source: Strict reading).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R1 — DORA 4h satisfies all shorter deadlines. Single incident record → per-regulation router → BaFin + ECB + CSIRT + ENISA + DPA + AI Office.
- **Stakeholder Impact:** CISO + CRO + DPO + Legal + board
- **Risk:** HIGH
- **Regulatory Reporting:** NIS 2 24h + DORA 4h + CRA 24h + GDPR 72h + AI Act 15d/2d/10d

---

### 12. NIS2-CL20 — Management body liability (Art. 20) (D-08.3 / NIS 2)

- **Sub-domain:** D-08.3
- **Regulation:** NIS 2
- **Article ref:** Art. 20
- **Type:** management liability
- **Card variant:** source-locus
- **Obligated party:** ESSENTIAL_ENTITY (management body)
- **Obligation type:** CONTINUOUS
- **Berry anchor:** §5.1 (`responsibility`), §5.4 (`chain of command`)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `management body accountability`
- Analysis: NIS 2 Art. 20 + DORA Art. 5(2) dual mandate. Management body may be held personally liable.
- Variant readings:
  - R1: Documentary (briefing + acknowledgement). (Source: Industry reading).
  - R2: Substantive (board must actively oversee). (Source: Directive literal).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R2 — Substantive. Board briefing programme mandatory (annual) + personal liability acknowledged in writing + DORA Art. 5(2) 4-verb coordination.
- **Stakeholder Impact:** Board + CEO + shareholders + ECB + BaFin
- **Risk:** HIGH
- **Regulatory Reporting:** NIS 2 Art. 20 + DORA Art. 5(2) + ECB JST inspection + BaFin

---

### 13. NIS2-CL12 — Coordinated vulnerability disclosure ecosystem (D-02.3 / NIS 2)

- **Sub-domain:** D-02.3
- **Regulation:** NIS 2
- **Article ref:** Art. 12
- **Type:** CVD
- **Card variant:** source-locus
- **Obligated party:** ESSENTIAL_ENTITY
- **Obligation type:** CONTINUOUS
- **Berry anchor:** §5.1 (`appropriate`, `CSIRT`)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S2
- Phrase: `CVD ecosystem`
- Analysis: Static infrastructure + dedicated intake. Berry-flagged scope ambiguity.
- Variant readings:
  - R1: security.txt + email + CVD page only. (Source: Industry reading).
  - R2: + bug bounty + CSIRT integration. (Source: Strict reading).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R1 — security.txt + dedicated intake mailbox + CVD page + ISO 29147 process. Bug bounty deferred.
- **Stakeholder Impact:** CISO + DevSecOps + ENISA + BSI CSIRT
- **Risk:** MEDIUM
- **Regulatory Reporting:** NIS 2 Art. 12 + CRA Art. 12 + ENISA + BSI CSIRT

---

### 14. DORA-Art-26 — Threat-Led Penetration Testing (Art. 26) (D-02.4 / DORA)

- **Sub-domain:** D-02.4
- **Regulation:** DORA
- **Article ref:** Art. 26(1)
- **Type:** TLPT
- **Card variant:** source-locus
- **Obligated party:** FINANCIAL_ENTITY
- **Obligation type:** PERIODIC (every 3y or ECB-adjusted)
- **Berry anchor:** §5.1 (`at least every 3 years`), §5.7 (frequency)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `at least every 3 years`
- Analysis: Hard numeric anchor 3y. ECB may adjust frequency. Significant entities may face annual cadence.
- Variant readings:
  - R1: 3y baseline + ECB frequency adjustment. (Source: Directive literal).
  - R2: 3y baseline only. (Source: Industry reading).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R1 — 3y baseline + ECB frequency adjustment. T-005 RESOLVED: parallel cycles with unified scope + findings tracking.
- **Stakeholder Impact:** CISO + CRO + board + ECB TLPT team + TLPT provider
- **Risk:** HIGH
- **Regulatory Reporting:** DORA Art. 26 closure report + ECB TLPT scoping letter + ISO 27001 surveillance

---

### 15. DORA-Art-30 — Critical ICT third-party contracts (Art. 30) (D-06.3 / DORA)

- **Sub-domain:** D-06.3
- **Regulation:** DORA
- **Article ref:** Art. 30(2)+(3)(e)+(f)
- **Type:** third-party
- **Card variant:** source-locus
- **Obligated party:** FINANCIAL_ENTITY
- **Obligation type:** PER-CONTRACT
- **Berry anchor:** §5.1 (`appropriate`, `proportionate`), §5.4 (9-element list)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `minimum 9-element list`
- Analysis: Art. 30(2) minimum 9 elements. Audit rights + exit strategies misattributed to Art. 30(2) when OJ places them in 30(3)(e) and 30(3)(f) (CIF-only).
- Variant readings:
  - R1: Art. 30(2) 9 elements; audit rights + exit strategies 30(3)(e)/(f) CIF-only. (Source: OJ-literal).
  - R2: All 9 elements (including audit/exit) per corpus. (Source: corpus misattribution).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R1 — OJ-literal. 100% critical vendor contracts with CTPP clauses + audit rights + exit strategies for CIF.
- **Stakeholder Impact:** Legal + CRO + CISO + Procurement + ECB JST
- **Risk:** HIGH
- **Regulatory Reporting:** DORA Art. 30 + Art. 34 CTPP register + ECB JST + ESAs Joint Committee (if CTPP)

---

### 16. DORA-Art-5 — ICT risk management framework (Art. 5) (D-09.1 / DORA)

- **Sub-domain:** D-09.1
- **Regulation:** DORA
- **Article ref:** Art. 5(2)
- **Type:** governance
- **Card variant:** source-locus
- **Obligated party:** FINANCIAL_ENTITY (management body)
- **Obligation type:** CONTINUOUS
- **Berry anchor:** §5.1 (`define, approve, oversee, be responsible` — 4-verb coordination)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `shall define, approve, oversee and be responsible for the implementation`
- Analysis: 4-verb coordination. Management body 4-verb obligation.
- Variant readings:
  - R1: 4 verbs are 4 separate duties. (Source: Directive literal).
  - R2: 4 verbs describe one composite duty. (Source: Loose reading).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R1 — 4 separate duties. Board briefing programme + 5-policy architecture + ISMS surveillance audit + DORA Art. 5 framework documented.
- **Stakeholder Impact:** Board + CEO + CISO + CRO + ECB JST
- **Risk:** HIGH
- **Regulatory Reporting:** DORA Art. 5 + NIS 2 Art. 21 management liability + ISO 27001 + AI Act Art. 9

---

### 17. DORA-Art-17 — ICT-related incident management process (Art. 17) (D-04.1 / DORA)

- **Sub-domain:** D-04.1
- **Regulation:** DORA
- **Article ref:** Art. 17(1)
- **Type:** incident management
- **Card variant:** source-locus
- **Obligated party:** FINANCIAL_ENTITY
- **Obligation type:** CONTINUOUS
- **Berry anchor:** §5.1 (`define, establish and implement` — twin 3-way verb coordinations)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `define, establish and implement an ICT-related incident management process`
- Analysis: Twin 3-way verb coordinations: detect, manage, notify.
- Variant readings:
  - R1: 3 separate duties. (Source: Directive literal).
  - R2: 3 verbs describe one composite process. (Source: Loose reading).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R1 — 3 separate duties. 24/7 SOC + SIEM + SOAR + EDR + NDR + UEBA + 5-reg max-SLA routing pipeline.
- **Stakeholder Impact:** CISO + SOC + customers + ECB + BaFin + AI Office
- **Risk:** HIGH
- **Regulatory Reporting:** DORA 4h + RTS Art. 6 + NIS 2 24h + CRA 24h + GDPR 72h + AI Act 15d/2d/10d

---

### 18. AI-Act-Art-9 — Risk management system (Annex III High-Risk) (D-09.1 / AI Act)

- **Sub-domain:** D-09.1
- **Regulation:** AI Act
- **Article ref:** Art. 9(1)
- **Type:** risk management
- **Card variant:** AI-Act-light
- **Obligated party:** PROVIDER (High-Risk)
- **Obligation type:** CONTINUOUS
- **Berry anchor:** §5.1 (`appropriate`, `effective`), §5.4 (5-step cycle)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `appropriate and effective measures`
- Analysis: AI Act Art. 9 risk management system. Continuous across lifecycle. VAG flag.
- Variant readings:
  - R1: Lifecycle (5-step cycle per Art. 9(2)). (Source: Directive literal).
  - R2: Pre-deployment only. (Source: Industry reading).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R1 — Continuous lifecycle. IPSARA Unified Assessment Framework (T-003 RESOLVED) integrates AI Act Art. 9 + DORA Art. 5 + GDPR DPIA + CRA + NIS 2.
- **Stakeholder Impact:** AI Gov Lead + CRO + DPO + CISO + AI Office
- **Risk:** HIGH
- **Regulatory Reporting:** AI Act Art. 9 + DORA Art. 5 + GDPR + ECB + AI Office

---

### 19. AI-Act-Art-27 — Fundamental Rights Impact Assessment (FRIA) (D-09.2 / AI Act)

- **Sub-domain:** D-09.2
- **Regulation:** AI Act
- **Article ref:** Art. 27
- **Type:** FRIA
- **Card variant:** AI-Act-light
- **Obligated party:** DEPLOYER (High-Risk)
- **Obligation type:** PRE-DEPLOYMENT
- **Berry anchor:** §5.1 (`fundamental rights`), §5.4 (assessment methodology)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `fundamental rights impact`
- Analysis: FRIA + DPIA overlap. T-003 RESOLVED via IPSARA.
- Variant readings:
  - R1: Separate FRIA + DPIA. (Source: Industry reading).
  - R2: Unified IPSARA assessment generates FRIA + DPIA outputs. (Source: T-003 RESOLVED).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R2 — IPSARA Unified Assessment Framework. Single underlying assessment, per-regulation output stream.
- **Stakeholder Impact:** AI Gov Lead + DPO + CRO + customers + AI Office
- **Risk:** MEDIUM
- **Regulatory Reporting:** AI Act Art. 27 FRIA + GDPR Art. 35 DPIA + DORA Art. 6 + AI Office + EDPB

---

### 20. AI-Act-Art-72 — Post-market monitoring (Art. 72) (D-10.1 / AI Act)

- **Sub-domain:** D-10.1
- **Regulation:** AI Act
- **Article ref:** Art. 72
- **Type:** post-market
- **Card variant:** AI-Act-light
- **Obligated party:** PROVIDER (High-Risk)
- **Obligation type:** CONTINUOUS
- **Berry anchor:** §5.1 (`throughout the lifecycle`), §5.4 (proportional monitoring)

**Instances (1):**

**Instance 1:**
- Type: VAG
- Severity: S3
- Phrase: `throughout the lifecycle`
- Analysis: Continuous monitoring + DORA Art. 13 integration. AI Act post-market monitoring.
- Variant readings:
  - R1: Passive (incident reports only). (Source: Industry reading).
  - R2: Active (continuous model monitoring + drift detection). (Source: Directive literal + AI Office).

**Resolution (Sprint 5 — Case_03-specific):**

- **Recommended Variant:** R2 — Active continuous monitoring. 24/7 SOC + SIEM + AI model monitoring integrated with security monitoring.
- **Stakeholder Impact:** AI Gov Lead + CISO + SOC + CRO + AI Office
- **Risk:** HIGH
- **Regulatory Reporting:** AI Act Art. 72 + DORA Art. 13 + AI Act Art. 73 serious incident 15d/2d/10d

---

## 4. Recommended Disambiguation

For each of the 20 top-priority cards, the recommended resolution approach is documented below. Resolution will be tracked in `Doc13_Proportionality_Profile.md` and the per-card closure status will be reflected in subsequent sprint reports.

**Resolution framework:**
1. **R1 reading** (corpus-preferred) — adopt as baseline for the Phase 2 strategic-tensions analysis.
2. **R2 reading** (alternative) — kept as fallback if R1 conflicts with another regulation.
3. **R3 reading** (rejected) — rejected with rationale recorded.

**Priority resolution tracks:**

| Priority | Track | Cards | Approach |
|---|---|---:|---|
| HIGH | Multi-regulation notification routing (D-04.3 + D-09.1) | 4 cards | CISO-owned; integrate with DORA RTS 4h universal SLA |
| HIGH | DPA + DORA Art. 30 contract templates (D-06.3) | 3 cards | DPO + CRO + Legal-owned; clause-bank maintained |
| HIGH | Records of processing (D-09.4) | 2 cards | DPO + AI Gov Lead + CRO co-owned; AI Act Annex III file + DORA Art. 8 register |
| HIGH | Risk-assessment (D-09.2 + D-06.1) | 4 cards | CRO + AI Gov Lead + DPO; DPIA + FRIA + DORA ICT risk + CRA risk-assessment |
| MEDIUM | Vendor due diligence (D-06.1) | 1 card | CRO + Procurement; DORA Art. 28 register |
| MEDIUM | Privacy by design (D-01.1 + D-01.3) | 2 cards | DPO + CISO + CTO; Annex I Part I (1) CRA secure-by-default |
| MEDIUM | Security measures (D-01.1 + D-01.2 + D-04.3 + D-06.3 + D-09.2) | 5 cards | CISO + DPO; NIST CSF 2.0 mappings + DORA Art. 9-12 ICT controls |
| MEDIUM | Asset inventory (D-09.3) | 2 cards | CRO + DevSecOps Lead; CMDB + DORA Art. 8 register |
| LOW | Patch management (D-02.2 etc., not in top 20) | — | Batch-resolve in Phase 2 with CISO + DevSecOps Lead |

**Cross-cutting resolutions:**
- **GDPR Art. 32 "appropriate technical and organisational measures"** (GDPR-CP15, multiple sub-domains): adopt NIST CSF 2.0 mapping as the structured reading. CISO owns.
- **GDPR-CP02 "privacy by design"** (D-01.1, D-01.3): adopt Art. 25(1) by-design necessity assessment; 4-factor proportionality. DPO owns.
- **GDPR-CP17 "72-hour notification"** (D-06.3): integrate into DORA RTS 4h universal SLA. CISO owns.
- **DORA Art. 5-16 ICT risk framework** (multiple D-09.x): adopt CRO-owned DORA ICT risk register aligned with ISO 27005 + NIST CSF 2.0 GV.RM.
- **CRA-CL23a "supply-chain due diligence"** (D-06.1): adopt Annex I Part I (2)(h) closed-list reading; CRO + Procurement owns.
- **NIS2-CL07 "risk-management core obligation"** (D-06.1, D-09.3): adopt Art. 21(2)(a)–(j) closed-AND-list reading; CRO + CISO owns.

**Phase 2 + Phase 3 cadence:**
- Sprint 3 (Phase 2 strategic-tensions resolution): resolve top 10 HIGH-priority cards.
- Sprint 4 (Phase 2 strategic-tensions resolution continued): resolve remaining 10 MEDIUM cards.
- Sprint 5 (Phase 3 final polish): batch-resolve LOW-priority cards from the remaining 1,470 corpus cards.

---

## 5. Cross-references

- **Corpus source:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` (38 sub-domain JSON sidecars, each with `ambiguity_cards[]`).
- **Berry lens methodology:** see `00_METHODOLOGY/PREPROCESSING_by_domain/domains/AMBIGUITY_ANALYSIS/01_Framework.md`.
- **Strategic tensions (T-001..T-004):** mapped in `Doc11_DORA_ICT_Risk_Framework.md` and `Doc13_Proportionality_Profile.md`.
- **Top 20 verbatim:** §3 above.
- **Per-sub-domain counts:** §2 above.
- **Resolution status tracker:** §4 above (will be migrated to `Doc13_Proportionality_Profile.md` in Sprint 3).

---

## N-1. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.2 (placeholder) | 2026-08-06 | Executor | Sprint 0 placeholder; status PLACEHOLDER. |
| 1.0 | 2026-08-06 | Executor | Sprint 2 corpus enrichment: 1,490 ambiguity cards aggregated across 38 sub-domains filtered to applicable regs; top 20 priority cards with verbatim corpus + R1/R2/R3 readings; per-sub-domain breakdown; recommended disambiguation. status PLACEHOLDER → CORPUS_ENRICHED. |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-08-06 |
| Security Review | CISO |  |  |
| DPO Review | DPO |  |  |
| AI Governance Review | AI Governance Lead |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Corpus root:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`
- **Highest-card sub-domains:** D-09.1 (131), D-09.4 (116), D-04.3 (94), D-09.2 (87), D-06.3 (76)
- **Citation cross-ref:** `Citation_Index.md` for verbatim regulation text.
- **Architecture context:** `Doc04_Architecture_DataInventory.md` §4 Corpus Provenance.
- **MAXIMUM-tier context:** Case_03 has 5 applicable regulations (GDPR + CRA + NIS 2 + DORA + AI Act); D-08.3 ACTIVE under dual NIS 2 + DORA; AI Act Annex III for OmniScore; DORA financial entity for CBS mainframe + OmniScore.
