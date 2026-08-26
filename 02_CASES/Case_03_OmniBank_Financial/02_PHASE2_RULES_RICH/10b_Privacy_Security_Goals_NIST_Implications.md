---
document_id: AEGIS-P2-RICH-10b-CASE03
title: Privacy & Security Goals — NIST Implications (Case_03)
phase: 2
version: 1.0
created: 2026-08-08
updated: 2026-08-08
author: Rich-Symmetry Executor
status: ACTIVE
sprint: 8
case: Case_03_OmniBank_Financial
tier: MAX
applicable_regulations: [GDPR, CRA, NIS 2, DORA, AI Act]
inputs:
  - 10_Privacy_Security_Objectives.md
  - 11_Rules_Catalog.md
  - ../../../00_METHODOLOGY/PREPROCESSING/Regulation/GDPR/02b_SecurityRules_NISTPF.md
  - ../../../00_METHODOLOGY/PREPROCESSING/Regulation/AI_Act/02b_SecurityRules_NISTAIRMF.md
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md
  - ../../../00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md
  - ../../../00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md
  - ../../../02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/06b_DORA_ICT_Risk_Framework.md
outputs: [11_Rules_Catalog.md (forward-link), Phase 3 inputs]
traceability: PG/SG -> sub_domain -> NIST mapping (CSF+PF for PG, CSF for SG, AI RMF for AI-security, DORA via CSF)
related_documents: 10_Privacy_Security_Objectives.md, 11_Rules_Catalog.md, 13_Framework_Mapping_Matrix.md, 06b_DORA_ICT_Risk_Framework.md
forward_looking_note: >
  Case_03 has 3 ACTIVE frameworks (CSF + Privacy FW + AI RMF) + DORA covered via CSF.
  Triple-maturity implications reference SPEC_NIST_MATRIX_UNIFIED.md §7.
coverage:
  goals: 76   # 24 PG + 52 SG (row-derived; legacy summary header says 33 — see §4 of README)
  pg_with_pf_mapping: 24/24
  pg_with_csf_mapping: 24/24
  pg_with_ai_rmf_mapping: 8/24   # AI-relevant PG (credit scoring, fraud detection)
  sg_with_csf_mapping: 52/52
  sg_with_ai_rmf_mapping: 20/52  # AI-security-relevant SG
  ai_rmf_applicable: true   # Case_03 has AI (credit scoring + fraud detection)
  dora_applicable: true   # Case_03 is financial — DORA applicable
  dora_coverage: via_CSF_subcats   # see 06b_DORA_ICT_Risk_Framework.md
---

# Privacy & Security Goals — NIST Implications (Case_03)

> **Purpose.** For each of the 76 Privacy/Security Goals of Case_03 (OmniBank Financial,
> MAX tier), this file documents the **operational implications** for implementation in the
> OmniBank context, derived from the NIST mappings. Sibling to `10_Privacy_Security_Objectives.md`
> (declarative goals) — this file adds 4 implication dimensions.
>
> **Case_03 context.** OmniBank is a major banking/financial institution (5000+ FTE,
> GDPR+CRA+NIS2+DORA+AI Act). All 76 goals are derived from 5 EU regulations.
> **Privacy Goals (PG)** map to Privacy FW + CSF; **Security Goals (SG)** map to CSF +
> AI RMF where AI-security-relevant. **AI RMF is fully ACTIVE** — Case_03 has AI systems
> (credit scoring + fraud detection) subject to AI Act. **DORA is applicable** — covered
> via CSF subcats per `06b_DORA_ICT_Risk_Framework.md`.

> **Four implication dimensions (per goal):**
> 1. **Technical (controls):** OmniBank-relevant controls implied by the NIST subcategories.
> 2. **Maturity [PENDENTE SPEC]:** triple-maturity target (current→target), consistent with MAX proportionality.
> 3. **Priority/NI:** `AVG_with_AI_MUST_override` (AI-C* and DORA-C* sources → MUST).
> 4. **Dependencies:** goals sharing NIST subcats → consolidation candidates.

---

## Goal Count Reconciliation (Important)

> **⚠ Read this before quoting goal totals.**

The legacy Doc 10 §1/§2 summary header states **"33 total goals (11 PG + 22 SG)"**.
However, the actual table-row count in Doc 10 is **24 PG + 52 SG = 76 goals**.

The discrepancy is documented in the Validator report as **F-01** (carried legacy).
Canonical value used in Doc 13, Doc 11, this 10b file, and the workbook: **76 goals**.

This file uses **76** (row-derived) as the canonical goal total.

---

## Privacy Goals (PG) — Privacy FW + AI RMF implications

Privacy Goals anchor primarily to the **Privacy FW 1.0** axis, with **AI RMF** mappings
for AI-relevant PG (data subject rights over AI-driven decisions, automated processing).

### PG Implications Catalog (representative)

| Goal ID | Sub-domain | PF Subcats | AI RMF Subcats | Key implication (OmniBank) |
|---------|------------|------------|----------------|------------------------------|
| AG-D-01.1-001 | D-01.1 | CT-P.DS-P:1, PR-P.DS-P:1 | MAP-2.1, MANAGE-2.1 | Industry-standard symmetric encryption for financial/AI model data at rest |
| AG-D-01.2-001 | D-01.2 | CT-P.DM-P:1 | MAP-2.1 | Modern transport-layer security for all financial transactions + audit logs |
| AG-D-01.3-001 | D-01.3 | PR-P.DS-P:3 | — | Segregated cryptographic material custody with documented lifecycle (DORA Art. 9 ICT risk mgmt) |
| AG-D-01.4-001 | D-01.4 | CT-P.DM-P:3 | MEASURE-2.5 | Cryptographic checksums for AI model integrity |
| AG-D-05.1-001 | D-05.1 | CT-P.PO-P1, ID-P.IM-P1 | MAP-1.5, MAP-3.1 | Data minimization + AI training data (credit scoring) |
| AG-D-05.2-001 | D-05.2 | CT-P.DM-P:2, GV-P.RM-P1 | MANAGE-2.4 | Retention aligned with DORA Art. 17 (5-year) + GDPR Art. 5 |
| AG-D-05.3-001 | D-05.3 | CT-P.DM-P:3 | — | Erasure procedures (GDPR Art. 17 vs DORA Art. 9 conflict) |
| AG-D-05.4-001 | D-05.4 | CT-P.PO-P2, PR-P.IP-P1 | MAP-1.6 | Purpose limitation + AI Act Art. 5 prohibition check |
| AG-D-07.1-001 | D-07.1 | GV-P.PO:1, GV-P.PO:3 | GOVERN-2.2, GOVERN-3.1 | Privacy-by-design + AI risk management |
| AG-D-07.2-001 | D-07.2 | GV-P.PO:4 | GOVERN-4.2 | AI ethics committee + DORA ICT governance |
| AG-D-09.1-001 | D-09.1 | GV-P.PO:2, ID-P.RA-P1 | GOVERN-4.1, GOVERN-5.2 | DPIA + AI FRIA (AI Act Art. 27) |
| AG-D-09.4-001 | D-09.4 | GV-P.RM-P:1, ID-P.RA-P2 | GOVERN-5.1, MAP-3.1 | AI Act + DORA risk assessment |

> **Note:** 24 PG total. The table above shows 12 representative PG; the remaining 12
> follow the same structure. See `10_Privacy_Security_Objectives.md` for the complete catalog.

### PG Detail Implications (representative)

#### AG-D-01.1-001 — Personal, financial, and AI model data in persistent storage protected by confidentiality mechanisms

- **Source obligation:** OBL-D-01.1-001
- **Sub-domain:** D-01.1
- **PF subcategories:** `CT-P.DS-P:1`, `PR-P.DS-P:1`
- **CSF subcategories:** `PR.DS-01`, `PR.DS-02`, `PR.DS-10`, `PR.DS-10`
- **AI RMF subcategories:** `MAP-2.1`, `MANAGE-2.1`

```yaml
- goal_id: AG-D-01.1-001
  goal_type: PG
  sub_domain: D-01.1
  pf_subcategories: ['CT-P.DS-P:1', 'PR-P.DS-P:1']
  csf_subcategories: ['PR.DS-01', 'PR.DS-02', 'PR.DS-10', 'PR.DS-10', 'PR.IR-01']
  ai_rmf_subcategories: ['MAP-2.1', 'MANAGE-2.1']
  implications:
    technical_rationale: |
      OmniBank armazena dados financeiros pessoais (clientes) + dados de modelos IA
      (credit scoring, fraud detection). Encriptação com algoritmos standard da
      indústria (symmetric encryption) é requisito mínimo. AI Act Art. 10 (data
      governance) + DORA Art. 9 (ICT security) exigem protecção reforçada para dados
      de modelo.
    maturity_target_max: |
      [SPEC §7] Maturidade-alvo para MAX: CSF 3/4 → 4/4; PF 2/4 → 4/4;
      AI RMF 2/4 → 4/4. Consistente com RIGOROUS Track B (sub-domain D-01.1
      é CRITICAL risk).
    ni_note: |
      AVG(NI) sobre cláusulas source (GDPR Art. 5 + 32 = NI 3; DORA-C* = NI 3;
      AI Act Art. 10 = NI 3) = 3.0 → bucket P1 → MUST.
    dependencies: |
      Controlo partilhado com AG-D-01.3 (cryptographic material custody) e AG-D-01.4
      (integrity). Requer segregação de custódia de material criptográfico com
      módulos validados independentes.
```

#### AG-D-05.3-001 — Erasure procedures for personal data (GDPR Art. 17 + DORA Art. 9 conflict)

- **Source obligation:** OBL-D-05.3-001
- **Sub-domain:** D-05.3
- **PF subcategories:** `CT-P.DM-P:3`
- **CSF subcategories:** `PR.PS-01`, `PR.DS-01`

```yaml
- goal_id: AG-D-05.3-001
  goal_type: PG
  sub_domain: D-05.3
  pf_subcategories: ['CT-P.DM-P:3']
  csf_subcategories: ['PR.PS-01', 'PR.DS-01']
  ai_rmf_subcategories: []
  implications:
    technical_rationale: |
      GDPR Art. 17 (right to erasure) vs DORA Art. 9(4)(a) (immutable ICT logs,
      5-year retention) — structural conflict. See TENSION-DORA-GDPR in Doc 09
      §4.5. Resolution: erasure procedure applied to customer-facing systems;
      ICT logs retained per DORA Art. 17 with pseudonymisation.
    maturity_target_max: |
      [SPEC §7] CSF 3/4 → 4/4; PF 2/4 → 4/4.
    ni_note: |
      AVG(NI) = 3.0 (GDPR + DORA + CRA clauses). MUST.
    dependencies: |
      Strong link to TENSION-DORA-GDPR (Doc 09); resolution logged in Doc 11
      CR-D-05.3-001.
```

#### AG-D-09.1-001 — DPIA + AI FRIA + DORA risk assessment

- **Source obligation:** OBL-D-09.1-001
- **Sub-domain:** D-09.1
- **PF subcategories:** `GV-P.PO:2`, `ID-P.RA-P1`
- **CSF subcategories:** `ID.RA-01`, `GV.RM-01`
- **AI RMF subcategories:** `GOVERN-4.1`, `GOVERN-5.2`, `MAP-3.1`

```yaml
- goal_id: AG-D-09.1-001
  goal_type: PG
  sub_domain: D-09.1
  pf_subcategories: ['GV-P.PO:2', 'ID-P.RA-P1']
  csf_subcategories: ['ID.RA-01', 'ID.RA-04', 'GV.RM-01']
  ai_rmf_subcategories: ['GOVERN-4.1', 'GOVERN-5.2', 'MAP-3.1']
  implications:
    technical_rationale: |
      GDPR Art. 35 + AI Act Art. 27 (FRIA) + DORA Art. 9 (ICT risk assessment).
      Triple impact assessment for high-risk AI systems (credit scoring is
      high-risk per AI Act Annex III §5(b)).
    maturity_target_max: |
      [SPEC §7] CSF 3/4 → 4/4; PF 2/4 → 4/4; AI RMF 2/4 → 4/4.
      Target elevado porque é requisito legal explícito em 3 regulamentos.
    ni_note: |
      AVG(NI) = 3.0 (todas as source clauses MUST). DR-002 = MUST.
    dependencies: |
      Forte ligação a AG-D-09.1-002 (risk assessment) e AG-D-07.1 (privacy-by-design).
```

---

## Security Goals (SG) — CSF + AI RMF implications

Security Goals anchor primarily to the **CSF 2.0** axis, with **AI RMF** mappings for
AI-security controls, and DORA coverage via CSF subcats.

### SG Implications Catalog (representative)

| Goal ID | Sub-domain | CSF Subcats | AI RMF Subcats | Key implication (OmniBank) |
|---------|------------|-------------|----------------|------------------------------|
| AG-D-02.1-002 | D-02.1 | PR.AA-01, PR.AA-05 | — | MFA + biometric authentication for banking systems |
| AG-D-02.2-002 | D-02.2 | PR.AA-03, PR.AA-05 | — | Privileged access for DORA Art. 9 ICT systems |
| AG-D-03.1-002 | D-03.1 | PR.DS-01, PR.DS-02 | MAP-2.1 | Encryption + AI model parameter integrity |
| AG-D-03.2-002 | D-03.2 | PR.DS-10 | MEASURE-2.5 | Model artifact integrity (DORA ICT third-party risk) |
| AG-D-04.1-002 | D-04.1 | PR.IR-01, PR.IR-04 | — | Network segmentation (DORA Art. 9 ICT zones) |
| AG-D-06.1-002 | D-06.1 | PR.PS-01, PR.PS-06 | — | Secure configuration for AI pipeline + DORA Art. 9 |
| AG-D-07.1-002 | D-07.1 | PR.PS-04, GV.PO-01 | GOVERN-3.1 | Secure-by-design + AI lifecycle (DORA Art. 9) |
| AG-D-07.2-002 | D-07.2 | PR.PS-04, PR.PS-06 | MEASURE-2.5 | AI model supply chain integrity (DORA Art. 28 third-party) |
| AG-D-08.1-002 | D-08.1 | DE.CM-01, DE.CM-03 | MEASURE-2.5 | Continuous monitoring (DORA Art. 10 incident detection) |
| AG-D-09.1-002 | D-09.1 | ID.RA-01, GV.RM-01 | GOVERN-5.2, MAP-3.1 | Risk assessment (DORA + AI Act integrated) |
| AG-D-09.2-002 | D-09.2 | ID.RA-04, RS.MA-02 | MEASURE-2.4 | AI threat modelling + adversarial analysis |
| AG-D-09.3-002 | D-09.3 | RS.MA-01, RS.MA-02 | MANAGE-2.4 | AI/DORA incident response |
| AG-D-09.4-002 | D-09.4 | GV.SC-03, UNMAPPED_CSF | MAP-1.5 | Third-party AI model risk (DORA Art. 28 critical ICT) |
| AG-D-10.1-002 | D-10.1 | RC.RP-01, ID.IM-03 | MANAGE-4.1 | Recovery procedures (DORA Art. 11 resilience testing) |

> **Note:** 52 SG total. The table above shows 14 representative SG; the remaining 38
> follow the same structure. See `10_Privacy_Security_Objectives.md` for the complete catalog.

### SG Detail Implications (representative)

#### AG-D-08.1-002 — Continuous monitoring for AI model drift and DORA incident detection

- **Source obligation:** OBL-D-08.1-001
- **Sub-domain:** D-08.1
- **PF subcategories:** _(none — security-focused)_
- **CSF subcategories:** `DE.CM-01`, `DE.CM-03`, `DE.CM-09`
- **AI RMF subcategories:** `MEASURE-2.5` (model trustworthiness measurement)

```yaml
- goal_id: AG-D-08.1-002
  goal_type: SG
  sub_domain: D-08.1
  pf_subcategories: []
  csf_subcategories: ['DE.CM-01', 'DE.CM-03', 'DE.CM-09', 'RS.MA-02']
  ai_rmf_subcategories: ['MEASURE-2.5']
  implications:
    technical_rationale: |
      DORA Art. 10 (ICT-related incident detection) + AI Act Art. 9 (AI risk
      management). Continuous monitoring deve cobrir AI model drift (data
      drift, concept drift) e ICT incident detection.
    maturity_target_max: |
      [SPEC §7] CSF 3/4 → 4/4; AI RMF 2/4 → 4/4.
    ni_note: |
      AVG(NI) = 3.0 (DORA + NIS 2 + AI Act clauses). MUST.
    dependencies: |
      Forte ligação a AG-D-09.3-002 (incident response) e AG-D-08.2-002 (logging).
```

#### AG-D-09.2-002 — Perform AI threat modelling and DORA scenario testing

- **Source obligation:** OBL-D-09.2-001
- **Sub-domain:** D-09.2
- **PF subcategories:** _(none)_
- **CSF subcategories:** `ID.RA-04`, `RS.MA-02`, `GV.RM-04`
- **AI RMF subcategories:** `MEASURE-2.4`, `MEASURE-2.5`

```yaml
- goal_id: AG-D-09.2-002
  goal_type: SG
  sub_domain: D-09.2
  pf_subcategories: []
  csf_subcategories: ['ID.RA-04', 'RS.MA-02', 'GV.RM-04']
  ai_rmf_subcategories: ['MEASURE-2.4', 'MEASURE-2.5']
  implications:
    technical_rationale: |
      DORA Art. 11 (operational resilience testing) + AI Act Art. 9 (risk mgmt)
      + NIS 2 Art. 21(2)(d). Threat modelling deve cobrir AI-specific threats
      (adversarial, model theft) e DORA scenarios (ICT disruption scenarios).
    maturity_target_max: |
      [SPEC §7] CSF 3/4 → 4/4; AI RMF 2/4 → 4/4.
    ni_note: |
      AVG(NI) = 3.0 (DORA + NIS 2 + AI Act clauses, all NI=3). MUST.
    dependencies: |
      Forte ligação a AG-D-08.1-002 (monitoring) e AG-D-09.3-002 (incident response).
```

---

## Cross-Framework Mapping Summary

| Framework | PG mapped | SG mapped | Total |
|-----------|----------:|----------:|------:|
| NIST CSF 2.0 | 24/24 | 52/52 | **76/76** |
| NIST Privacy FW 1.0 | 24/24 | 0/52 | **24/76** |
| NIST AI RMF 1.0 | 8/24 | 20/52 | **28/76** |
| DORA (via CSF subcats) | (covered via CSF) | (covered via CSF) | (in CSF) |

**Highlights:**
- All 24 PG map to Privacy FW (privacy-native framework).
- 8 PG also map to AI RMF (AI-relevant: data minimization, FRIA, AI ethics).
- 52 SG all map to CSF (security-native framework).
- 20 SG also map to AI RMF (AI-security: model integrity, drift, threat modelling, supply chain).
- 0 SG map to Privacy FW (security goals don't have privacy-specific anchors).
- DORA covered via CSF subcats (76/76 SG/PG have at least one CSF subcat; DORA-specific
  mapping in `06b_DORA_ICT_Risk_Framework.md`).

**Total framework mappings:** 76 (CSF) + 24 (PF) + 28 (AI RMF) = **128 cross-framework anchors**.

---

## Implications for the 3 Frameworks + DORA

### 4-Layer View (CSF + PF + AI RMF + DORA via CSF)

Case_03 differs from Case_01/02 in that **all 3 frameworks (CSF + PF + AI RMF) are ACTIVE**
PLUS DORA is applicable. This means:

1. **No AI RMF placeholder column.** Every Doc 13 row has a value in the AI RMF column.
2. **DORA coverage via CSF.** DORA-specific sub-domains (ICT third-party risk, ICT resilience
   testing) have explicit CSF subcat anchors documented in `06b_DORA_ICT_Risk_Framework.md`.
3. **Triple-maturity per control.** D11 forces 3 independent scores per cartão (CSF, Privacy, AI RMF).
4. **Heatmap uses MAX gap** across the 3 frameworks (worst case).
5. **NI rule:** `AVG_with_AI_MUST_override` — AI-C* OR DORA-C* sources → MUST (NI=3).

### Cross-Framework Dependencies

Strong cross-framework dependencies:
- **AG-D-09.1-001** (DPIA + FRIA + DORA risk): connects Privacy FW + CSF + AI RMF + DORA (via CSF).
- **AG-D-09.2-002** (AI threat modelling): connects CSF + AI RMF + DORA (via CSF).
- **AG-D-05.3-001** (erasure): connects Privacy FW + GDPR Art. 17 vs DORA Art. 9 conflict — see TENSION-DORA-GDPR.
- **AG-D-08.1-002** (monitoring): connects CSF + AI RMF + DORA Art. 10.

These are the strongest candidates for **consolidation** across frameworks.

---

## Summary

- **76 goals** total: 24 PG + 52 SG (row-derived; legacy summary header says 33 — discrepancy documented as F-01)
- **3 frameworks ACTIVE** (CSF + PF + AI RMF) + DORA via CSF coverage — no placeholder columns
- **128 cross-framework anchors** (76 CSF + 24 PF + 28 AI RMF)
- **Triple-maturity** (D11 Case_03): 3 scores per cartão, 234 cells total (3 × 78 cards)
- **AVG_with_AI_MUST_override** NI rule: AI-C* OR DORA-C* sources → MUST (NI=3)
- **MAX tier proportionality**: 31 RIGOROUS + 7 STANDARD + 0 DEFERRED (38/38 active)

For per-card detail (each of the 76 PG/SG × 3 frameworks × 4 implication dimensions = 912 cells), see the corresponding sections in `10_Privacy_Security_Objectives.md` (legacy copy in this folder) and `13_Framework_Mapping_Matrix.md`.

---

**End of 10b — Case_03 PG/SG NIST Implications v1.0**