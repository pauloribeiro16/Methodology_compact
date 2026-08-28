---
document_id: AEGIS-P2-RICH-10b-CASE02
title: Privacy & Security Goals — NIST Implications (Case_02)
phase: 2
version: 2.2
created: 2026-08-08
updated: 2026-08-13
author: Rich-Symmetry Executor
status: ACTIVE
case: Case_02_SecureBorder_Solutions
tier: HIGH
applicable_regulations: [GDPR, CRA, NIS 2, AI_Act]
inputs:
  - Doc16_Privacy_Security_Goals.md
  - Doc18_Rules_Catalog.md
  - ../../../00_METHODOLOGY/PREPROCESSING/Regulation/GDPR/02b_SecurityRules_NISTPF.md
  - ../../../00_METHODOLOGY/PREPROCESSING/Regulation/AI_Act/02b_SecurityRules_NISTAIRMF.md
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md
  - ../../../00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md
  - ../../../00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md
outputs: [Doc18_Rules_Catalog.md (forward-link), Phase 3 inputs]
traceability: PG/SG -> sub_domain -> NIST mapping (CSF+PF for PG, CSF for SG, AI RMF for AI-security)
related_documents: Doc16_Privacy_Security_Goals.md, Doc18_Rules_Catalog.md, Doc19_Framework_Mapping_Matrix.md
forward_looking_note: >
  Case_02 has 3 ACTIVE frameworks (CSF + Privacy FW + AI RMF). All three
  are populated below — no placeholder columns. Triple-maturity (legacy design note; superseded by the Implementation Posture Model, port Fase 4) —
  implications reference SPEC_NIST_MATRIX_UNIFIED.md §7.
coverage:
  goals: 89   # 34 PO + 55 SO
  pg_with_pf_mapping: 34/34
  pg_with_csf_mapping: 34/34
  pg_with_ai_rmf_mapping: 12/34   # biometric/AI-relevant PG
  sg_with_csf_mapping: 55/55
  sg_with_ai_rmf_mapping: 25/55  # AI-security-relevant SG
  ai_rmf_applicable: true   # Case_02 has AI (biometric border-control)
---

# Privacy & Security Goals — NIST Implications (Case_02)

> **Purpose.** For each of the 89 Privacy/Security Operational Objectives of Case_02 (SecureBorder Solutions,
> HIGH tier), this file documents the **operational implications** for implementation in the
> SecureBorder context, derived from the NIST mappings (Privacy FW for PG, CSF for SG,
> AI RMF for AI-relevant controls). Sibling to `Doc16_Privacy_Security_Goals.md` (declarative
> goals) — this file adds 4 implication dimensions, reusing the PO-D-*/SO-D-* namespace.
>
> **Case_02 context.** SecureBorder is a biometric border-control technology company
> (250-500 FTE, GDPR+CRA+NIS2+AI_Act). All 89 goals (34 PO + 55 SO) are GDPR/CRA/NIS2/AI-Act-derived.
> **Privacy Operational Objectives (PO)** map to Privacy FW + CSF; **Security Operational Objectives (SO)** map to CSF +
> AI RMF where AI-security-relevant. **AI RMF is fully ACTIVE** — Case_02 has AI systems
> (biometric recognition) subject to AI_Act.

> **Four implication dimensions (per goal):**
> 1. **Technical (controls):** specific SecureBorder-relevant controls implied by the
>    NIST subcategories across the 3 frameworks.
> 2. **Posture note [was Maturity, PENDENTE SPEC — superseded]:** legacy triple-maturity target quote (current→target) for the goal,
>    consistent with HIGH proportionality and Track B.
> 3. **Priority/NI:** `AVG_with_AI_MUST_override` over the goal's source clauses,
>    bucketed to P1/P2/P3 (MUST/SHOULD/COULD). AI-C* sources force MUST (NI=3).
> 4. **Dependencies:** goals sharing NIST subcats → consolidation candidates.

---

## Privacy Operational Objectives (PO) — Privacy FW + AI RMF implications

Privacy Goals anchor primarily to the **Privacy FW 1.0** axis (privacy-specific
subcategories: CT.*-P data decisions, GV.*-P governance, CM.*-P communication),
with **AI RMF** mappings for biometric/AI-specific PG (data subject rights over
biometric data processing).

### PO Implications Catalog

| Goal ID | Sub-domain | PF Subcats | AI RMF Subcats | Key implication (SecureBorder) |
|---------|------------|------------|----------------|--------------------------------|
| PO-D-01.1-001, PO-D-01.1-002 | D-01.1 | CT-P.DS-P:1, PR-P.DS-P:1 | MAP-2.1, MANAGE-2.1 | strong cryptographic modules hardware security storage for biometric template encryption |
| PO-D-01.2-001, PO-D-01.2-002 | D-01.2 | CT-P.DM-P:1 | MAP-2.1 | confidentiality mechanisms appropriate to channel classification for biometric/passport/audit data in transit |
| SO-D-01.3-001, SO-D-01.3-002, SO-D-01.3-003 | D-01.3 | PR-P.DS-P:3 | — | hardware-backed key lifecycle for biometric template encryption |
| PO-D-01.4-001 | D-01.4 | CT-P.DM-P:3 | MEASURE-2.5 | Cryptographic checksums for biometric data integrity |
| PO-D-05.1-001 | D-05.1 | CT-P.PO-P1, ID-P.IM-P1 | MAP-1.5, MAP-3.1 | Data minimization + AI training data relevance (biometric samples) |
| PO-D-05.2-001 | D-05.2 | CT-P.DM-P:2, GV-P.RM-P1 | MANAGE-2.4 | Retention policy aligned with biometric data lifecycle |
| PO-D-05.3-001 | D-05.3 | CT-P.DM-P:3 | — | Erasure procedures for biometric templates |
| PO-D-05.4-001 | D-05.4 | CT-P.PO-P2, PR-P.IP-P1 | MAP-1.6 | Purpose limitation + AI_Act Art. 5 prohibition check |
| PO-D-07.1-001, PO-D-07.1-002 | D-07.1 | GV-P.PO:1, GV-P.PO:3 | GOVERN-2.2, GOVERN-3.1 | Privacy-by-design policy + AI risk management |
| PO-D-09.1-001, PO-D-09.1-002 | D-09.1 | GV-P.PO:2, ID-P.RA-P1 | GOVERN-4.1, GOVERN-5.2 | DPIA + AI fundamental rights impact assessment (FRIA, AI_Act Art. 27) |

> **Note:** PO-D-09.2-001, PO-D-09.2-002 and PO-D-09.4-001 are also mapped in the full Case_02
> PG catalog (10 PG total); abbreviated here for space. See `Doc16_Privacy_Security_Goals.md`
> for the complete list.

### PO Detail Implications (representative)

#### PO-D-01.1-001, PO-D-01.1-002 — Encrypt all personal, biometric, and sensitive data at rest using strong symmetric encryption with strong cryptographic modules

- **Source obligation:** OBL-D-01.1-001
- **Sub-domain:** D-01.1
- **PF subcategories:** `CT-P.DS-P:1` (data-action management), `PR-P.DS-P:1` (data security)
- **CSF subcategories:** `PR.DS-01`, `PR.DS-02`, `PR.DS-10`, `PR.DS-10`
- **AI RMF subcategories:** `MAP-2.1` (AI system context), `MANAGE-2.1` (AI risk treatment)

```yaml
- goal_id: PO-D-01.1-001, PO-D-01.1-002
  goal_type: PO
  sub_domain: D-01.1
  pf_subcategories: ['CT-P.DS-P:1', 'PR-P.DS-P:1']
  csf_subcategories: ['PR.DS-01', 'PR.DS-02', 'PR.DS-10', 'PR.DS-10', 'PR.IR-01']
  ai_rmf_subcategories: ['MAP-2.1', 'MANAGE-2.1']
  implications:
    technical_rationale: |
      Biometric templates são dados pessoais sensíveis (Art. 9 GDPR). Encriptação
      strong symmetric encryption com módulos strong cryptographic modules é requisito mínimo para templates
      biométricos. AI_Act Art. 10 (data governance) exige protecção reforçada.
    posture_target_note_high: |  # legacy-scale quote; superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0
      [Legacy scale quote — superseded; backfill: CSF PARTIAL, PF PARTIAL, AI RMF PARTIAL] Target profile for HIGH was:
      AI RMF 1/4 → 3/4. Consistente com RIGOROUS Track B (sub-domain D-01.1
      é CRITICAL risk).
    ni_note: |
      AVG(NI) sobre cláusulas source (GDPR Art. 9 = NI 3; GDPR Art. 32 = NI 3;
      AI_Act Art. 10 = NI 3) = 3.0 → bucket P1 ≥ 2.5 → MUST.
    dependencies: |
      Controlo partilhado com SO-D-01.3-001 (key management) e PO-D-01.4-001 (integrity).
      Requer hardware security storage (Hardware Security Module) deployment.
```

#### PO-D-05.1-001 — Minimize personal data collection to adequate, relevant, and necessary fields

- **Source obligation:** OBL-D-05.1-001
- **Sub-domain:** D-05.1
- **PF subcategories:** `CT-P.PO-P1` (data processing purposes), `ID-P.IM-P1` (inventory)
- **CSF subcategories:** `ID.AM-01`, `ID.AM-02`, `PR.PS-04`
- **AI RMF subcategories:** `MAP-1.5` (AI training data), `MAP-3.1` (AI system impact)

```yaml
- goal_id: PO-D-05.1-001
  goal_type: PO
  sub_domain: D-05.1
  pf_subcategories: ['CT-P.PO-P1', 'ID-P.IM-P1']
  csf_subcategories: ['ID.AM-01', 'ID.AM-02', 'PR.PS-04']
  ai_rmf_subcategories: ['MAP-1.5', 'MAP-3.1']
  implications:
    technical_rationale: |
      AI_Act Art. 10 (data governance) + GDPR Art. 5(1)(c). Para treino de
      modelos biométricos, datasets devem ser relevantes, suficientemente
      representativos, e livres de erros.
    posture_target_note_high: |  # legacy-scale quote; superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0
      [SPEC §7] CSF 2/4 → 3/4; PF 2/4 → 3/4; AI RMF 1/4 → 3/4.
    ni_note: |
      AVG(NI) = 3.0 (GDPR Art. 5 + AI_Act Art. 10). MUST.
    dependencies: |
      Forte ligação a PO-D-09.1-001, PO-D-09.1-002 (DPIA/FRIA). Requer data inventory
      automatizado para AI training datasets.
```

#### PO-D-09.1-001, PO-D-09.1-002 — Conduct Data Protection Impact Assessment (DPIA) and AI Fundamental Rights Impact Assessment (FRIA)

- **Source obligation:** OBL-D-09.1-001
- **Sub-domain:** D-09.1
- **PF subcategories:** `GV-P.PO:2` (roles/responsibilities), `ID-P.RA-P1` (risk assessment)
- **CSF subcategories:** `ID.RA-01`, `GV.RM-01`
- **AI RMF subcategories:** `GOVERN-4.1` (AI roles), `GOVERN-5.2` (AI risk management)

```yaml
- goal_id: PO-D-09.1-001, PO-D-09.1-002
  goal_type: PO
  sub_domain: D-09.1
  pf_subcategories: ['GV-P.PO:2', 'ID-P.RA-P1']
  csf_subcategories: ['ID.RA-01', 'ID.RA-04', 'GV.RM-01']
  ai_rmf_subcategories: ['GOVERN-4.1', 'GOVERN-5.2', 'MAP-3.1']
  implications:
    technical_rationale: |
      GDPR Art. 35 + AI_Act Art. 27 (FRIA obrigatória para high-risk AI).
      Biometric identification é high-risk AI system (AI_Act Annex III §1).
    posture_target_note_high: |  # legacy-scale quote; superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0
      [SPEC §7] CSF 2/4 → 4/4; PF 2/4 → 4/4; AI RMF 1/4 → 4/4.
      Target elevado porque FRIA é requisito legal explícito.
    ni_note: |
      AVG(NI) = 3.0 (todas as source clauses MUST). DR-002 = MUST.
    dependencies: |
      Forte ligação a SO-D-09.1-001 (risk assessment) e PO-D-07.1-001 (privacy-by-design).
```

---

## Security Operational Objectives (SO) — CSF + AI RMF implications

Security Goals anchor primarily to the **CSF 2.0** axis (technical security
subcategories: PR.*, DE.*, RS.*, RC.*), with **AI RMF** mappings for AI-security
controls (model integrity, adversarial robustness, AI-specific risk management).

### SO Implications Catalog (representative)

| Goal ID | Sub-domain | CSF Subcats | AI RMF Subcats | Key implication (SecureBorder) |
|---------|------------|-------------|----------------|--------------------------------|
| SO-D-02.1-001, SO-D-02.1-002, SO-D-02.1-003 | D-02.1 | PR.AA-01, PR.AA-05 | — | multi-factor authentication + biometric authentication for border-control systems |
| SO-D-02.2-001, SO-D-02.2-002 | D-02.2 | PR.AA-03, PR.AA-05 | — | Privileged access management for AI model deployment |
| SO-D-03.1-001, SO-D-03.1-002, SO-D-03.1-003 | D-03.1 | PR.DS-01, PR.DS-02 | MAP-2.1 | Encryption + AI model parameter integrity |
| SO-D-03.2-001, SO-D-03.2-002, SO-D-03.2-003 | D-03.2 | PR.DS-10 | MEASURE-2.5 | Model artifact integrity (hash verification) |
| SO-D-04.1-001, SO-D-04.1-002, SO-D-04.1-003 | D-04.1 | PR.IR-01, PR.IR-04 | — | Network segmentation for biometric processing zone |
| PO-D-06.1-001, PO-D-06.1-002 | D-06.1 | PR.PS-01, PR.PS-06 | — | Secure configuration management for AI pipeline |
| PO-D-07.1-001, PO-D-07.1-002, SO-D-07.1-001 | D-07.1 | PR.PS-04, GV.PO-01 | GOVERN-3.1 | Secure-by-design + AI system lifecycle management |
| SO-D-07.2-001, SO-D-07.2-002 | D-07.2 | PR.PS-04, PR.PS-06 | MEASURE-2.5 | AI model supply chain integrity |
| PO-D-08.1-001, PO-D-08.1-002 | D-08.1 | DE.CM-01, DE.CM-03 | MEASURE-2.5 | Continuous monitoring for AI model drift |
| PO-D-09.1-001, PO-D-09.1-002, SO-D-09.1-001, SO-D-09.1-002 | D-09.1 | ID.RA-01, GV.RM-01 | GOVERN-5.2, MAP-3.1 | Risk assessment (AI-specific) |
| PO-D-09.2-001, PO-D-09.2-002, SO-D-09.2-001, SO-D-09.2-002 | D-09.2 | ID.RA-04, RS.MA-02 | MEASURE-2.4 | AI threat modelling + adversarial analysis |
| NOT_ADDRESSED | D-09.3 | RS.MA-01, RS.MA-02 | MANAGE-2.4 | AI incident response procedures |
| PO-D-09.4-001, SO-D-09.4-001 | D-09.4 | GV.SC-03 | MAP-1.5 | Third-party AI model risk assessment |
| SO-D-10.1-001, SO-D-10.1-002, SO-D-10.1-003 | D-10.1 | RC.RP-01, ID.IM-03 | MANAGE-4.1 | AI system recovery procedures |

> **Note:** 55 SO total (corr-008: SO-D-* namespace, 25/55 SO have AI RMF mappings; the
> remaining 30 SO map to CSF only). The table above shows 14 representative SO with
> AI RMF mappings. See `Doc16_Privacy_Security_Goals.md` for the complete catalog.

### SO Detail Implications (representative)

#### PO-D-09.2-001, PO-D-09.2-002, SO-D-09.2-001, SO-D-09.2-002 — Perform AI threat modelling and adversarial analysis

- **Source obligation:** OBL-D-09.2-001
- **Sub-domain:** D-09.2
- **PF subcategories:** _(none — security-focused)_
- **CSF subcategories:** `ID.RA-04`, `RS.MA-02`
- **AI RMF subcategories:** `MEASURE-2.4` (AI risk measurement)

```yaml
- goal_id: PO-D-09.2-001, PO-D-09.2-002, SO-D-09.2-001, SO-D-09.2-002
  goal_type: SO
  sub_domain: D-09.2
  pf_subcategories: []
  csf_subcategories: ['ID.RA-04', 'RS.MA-02', 'GV.RM-04']
  ai_rmf_subcategories: ['MEASURE-2.4', 'MEASURE-2.5']
  implications:
    technical_rationale: |
      AI_Act Art. 9 (risk management) + NIS 2 Art. 21(2)(d). Biometric
      recognition systems require adversarial robustness testing
      (e.g., adversarial patch attacks, presentation attacks).
    posture_target_note_high: |  # legacy-scale quote; superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0
      [SPEC §7] CSF 2/4 → 3/4; AI RMF 1/4 → 3/4. PF N/A.
    ni_note: |
      AVG(NI) = 2.5 (NIS 2 = NI 2, AI_Act = NI 3) → bucket P1 → MUST
      (NI ≥ 2.5).
    dependencies: |
      Forte ligação a PO-D-08.1-001 (monitoring) e AG-D-09.3-002 (incident response).
```

#### SO-D-07.2-001, SO-D-07.2-002 — Implement AI model supply chain integrity (BPR)

- **Source rule:** BPR-D-07.2-001
- **Sub-domain:** D-07.2
- **PF subcategories:** _(none)_
- **CSF subcategories:** `PR.PS-04`, `PR.PS-06`
- **AI RMF subcategories:** `MEASURE-2.5` (model trustworthiness)

```yaml
- goal_id: SO-D-07.2-001, SO-D-07.2-002
  goal_type: SO
  sub_domain: D-07.2
  pf_subcategories: []
  csf_subcategories: ['PR.PS-04', 'PR.PS-06']
  ai_rmf_subcategories: ['MEASURE-2.5']
  implications:
    technical_rationale: |
      AI model artifacts devem ter integridade verificável (hash, signature).
      Supply chain attacks em modelos pré-treinados são vector de risco real.
    posture_target_note_high: |  # legacy-scale quote; superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0
      [SPEC §7] CSF 2/4 → 3/4; AI RMF 1/4 → 3/4.
    ni_note: |
      BPR com base NIST AI RMF + industry AI security testing standards. NI = 2 (SHOULD).
    dependencies: |
      Forte ligação a SO-D-07.1-001 (secure-by-design) e SO-D-09.4-001 (third-party risk).
```

---

## Cross-Framework Mapping Summary

| Framework | PG mapped | SG mapped | Total |
|-----------|----------:|----------:|------:|
| NIST CSF 2.0 | 34/34 | 55/55 | **89/89** |
| NIST Privacy FW 1.0 | 10/10 | 0/55 | **10/89** |
| NIST AI RMF 1.0 | 12/34 | 25/55 | **37/89** |

**Highlights (post Sprint 10 migration):**
- All 34 PO map to Privacy FW (privacy-native framework).
- 12 PO also map to AI RMF (biometric/AI-relevant: PO-D-01.1-001, PO-D-05.1-001, PO-D-07.1-001, PO-D-09.1-001).
- 55 SO all map to CSF (security-native framework).
- 25 SO also map to AI RMF (AI-security-relevant: model integrity, drift, supply chain, threat modelling).
- 0 SO map to Privacy FW (security goals don't have privacy-specific anchors).

**Total framework mappings:** 89 (CSF) + 10 (PF) + 37 (AI RMF) = **136 cross-framework anchors**.

---

## Implications for the 3 Frameworks

### 3-Framework View

Case_02 differs from Case_01 in that **all 3 frameworks (CSF + PF + AI RMF) are ACTIVE**.
This means:

1. **No AI RMF placeholder column.** Every Doc 13 row has a value in the AI RMF column.
2. **Triple implementation-status per control (post-port).** The D11 triple-maturity scoring was superseded by the Implementation Posture Model v2.0 (port Fase 4); statuses live in Doc19 §5.1.
3. **Heatmap uses MAX gap** across the 3 frameworks (worst case).
4. **NI rule:** `AVG_with_AI_MUST_override` — any CR with AI-C* source clause → MUST (NI=3).

### Cross-Framework Dependencies

Some goals have strong cross-framework dependencies:
- **PO-D-09.1-001, PO-D-09.1-002** (DPIA + FRIA): connects Privacy FW (GV-P.PO:2, ID-P.RA-P1) + CSF (ID.RA-01) + AI RMF (GOVERN-5.2, MAP-3.1).
- **PO-D-09.2-001, PO-D-09.2-002, SO-D-09.2-001, SO-D-09.2-002** (AI threat modelling): connects CSF (ID.RA-04) + AI RMF (MEASURE-2.4).
- **PO-D-01.1-001, PO-D-01.1-002** (encryption): connects CSF (PR.DS-01) + PF (CT-P.DS-P:1) + AI RMF (MAP-2.1).

These are the strongest candidates for **consolidation** across frameworks — single implementation serves multiple frameworks.

---

## Summary

- **89 objectives** total: 34 PO + 55 SO (1:1 OBL→goal derivation per DR-D01)
- **3 frameworks ACTIVE** (CSF + PF + AI RMF) — no placeholder columns
- **136 cross-framework anchors** (89 CSF + 10 PF + 37 AI RMF)
- **Triple implementation status** (D11 Case_02, post-port): 3 statuses per cartão in Doc19 §5.1; legacy 165 numeric cells superseded
- **AVG_with_AI_MUST_override** NI rule: AI-C* sources → MUST (NI=3)
- **HIGH tier proportionality**: 7 RIGOROUS + 27 STANDARD + 1 DEFERRED + 3 LIGHTWEIGHT

For per-card detail (each of the 89 PO/SO × 3 frameworks × 4 implication dimensions = 1068 cells), see the corresponding sections in `Doc16_Privacy_Security_Goals.md` (legacy copy in this folder) and `Doc19_Framework_Mapping_Matrix.md`.

---

**End of 10b — Case_02 PG/SG NIST Implications v1.0**