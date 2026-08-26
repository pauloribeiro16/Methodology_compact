---
document_id: AEGIS-P2-RICH-10b
title: Privacy & Security Operational Objectives — NIST Implications (Case_01)
phase: 2
version: 2.0
created: 2026-08-07
updated: 2026-08-10
author: Orchestrator (Case_01 implications)
status: ACTIVE
sprint: 9
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs:
  - 10_Privacy_Security_Objectives.md
  - 11_Rules_Catalog.md
  - ../../../00_METHODOLOGY/PREPROCESSING/Regulation/GDPR/01b_SecurityObjectives_NIST_Implications.md
  - ../../../00_METHODOLOGY/PREPROCESSING/Regulation/GDPR/02b_SecurityRules_NISTPF.md
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md
  - ../../../00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md
outputs: [11_Rules_Catalog.md (forward-link), Phase 3 inputs]
traceability: PO/SO -> sub_domain -> NIST mapping (CSF for SO, CSF+PF for PO)
related_documents: 10_Privacy_Security_Objectives.md, 11_Rules_Catalog.md
forward_looking_note: >
  NI (AVG) and dual-maturity implications reference SPEC_NIST_MATRIX_UNIFIED.md
  decisions. Case_01 is MICRO tier, GDPR+RA apply; AI RMF N/A (no AI systems).
coverage:
  objectives: 31  # 11 PO + 20 SO
  po_with_pf_mapping: 11/11
  so_with_csf_mapping: 16/20
  so_with_pf_overlap: 13/20
  ai_rmf_applicable: false   # Case_01 has no AI
---

# Privacy & Security Operational Objectives — NIST Implications (Case_01)

> **Purpose.** For each of the 31 Privacy/Security Operational Objectives of Case_01 (TinyTask SaaS,
> MICRO tier), this file documents the **operational implications** for implementation
> in the TinyTask context, derived from the NIST mappings (Privacy FW for PO, CSF for
> SO). Sibling to `10_Privacy_Security_Objectives.md` (declarative objectives) — this file
> adds 4 implication dimensions, reusing the PO-D-* / SO-D-* namespace.

> **Case_01 context.** TinyTask is a B2B SaaS (small team, GDPR+RA). All 31 objectives are
> GDPR-derived. Privacy Operational Objectives (PO) map to Privacy FW; Security Operational Objectives (SO) map to CSF
> 2.0. **AI RMF is not applicable** — Case_01 has no AI systems (AI Act NOT APPLICABLE).

> **Four implication dimensions (per goal):**
> 1. **Technical (controls):** specific TinyTask-relevant controls implied by the
>    NIST subcategories (e.g. managed object-storage encryption for PR.DS-P1, consent UI for CT.PO-P3).
> 2. **Maturity [PENDENTE SPEC]:** dual-maturity target (current→target) for the goal,
>    consistent with MICRO proportionality.
> 3. **Priority/NI [PENDENTE SPEC]:** AVG(NI) over the goal's source clauses,
>    bucketed to P1/P2/P3 (MUST/SHOULD/COULD).
> 4. **Dependencies:** goals sharing NIST subcats → consolidation candidates.

---

## Privacy Operational Objectives (PO) — Privacy FW implications

Privacy Operational Objectives anchor primarily to the **Privacy FW 1.0** axis (privacy-specific
subcategories: CT.*-P data decisions, GV.*-P governance, CM.*-P communication).

### PO Implications Catalog

| Goal ID | Sub-domain | PF Subcats | Key implication (TinyTask) |
|---|---|---|---|
| PO-D-01.1-001 | D-01.1 | PR.DS-P1 | Data-at-rest protected (confidentiality) |
| PO-D-01.2-001 | D-01.2 | PR.DS-P2 | Data-in-transit protected (confidentiality) |
| PO-D-01.4-001 | D-01.4 | CT.DM-P1, CT.DM-P3 | Data reviewable + alterable (integrity) |
| PO-D-05.1-001 | D-05.1 | CT.DP-P4, CT.PO-P4, ID.RA-P3 | Selective collection + lifecycle + risk |
| PO-D-05.2-001 | D-05.2 | CT.DM-P5, CT.PO-P4 | Destruction per policy + lifecycle |
| PO-D-05.3-001 | D-05.3 | CT.DM-P4, CT.DM-P5 | Deletion + destruction per policy |
| PO-D-05.4-001 | D-05.4 | CT.DM-P1, CT.DM-P6 | Reviewable + standardised export |
| PO-D-07.1-001 | D-07.1 | CT.DP-P2, CT.DP-P4, CT.DP-P5, CT.PO-P4, GV.PO-P2 | De-identification + selective + privacy-by-design |
| PO-D-09.1-001 | D-09.1 | CM.PO-P1, GV.PO-P1, GV.PO-P5 | Transparency + values + legal compliance |
| PO-D-09.2-001 | D-09.2 | ID.RA-P3, ID.RA-P4, ID.RA-P5 | Risk identification + prioritisation + response |
| PO-D-09.4-001 | D-09.4 | ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8 | Inventory + data actions + elements + mapping |

### PO Detail Implications

#### PO-D-01.1-001 — Encrypt all personal and sensitive data at rest using strong symmetric encryption

- **Source obligation:** OBL-D-01.1-001
- **Sub-domain:** D-01.1
- **PF subcategories:** `PR.DS-P1` (data-at-rest protection)
- **CSF subcategories:** `PR.DS-01`, `PR.DS-02`, `PR.DS-10`, `PR.DS-10`

```yaml
- goal_id: PO-D-01.1-001
  goal_type: PO
  sub_domain: D-01.1
  pf_subcategories: ['PR.DS-P1']
  csf_subcategories: ['PR.DS-01', 'PR.DS-02', 'PR.DS-10', 'PR.DS-10', 'PR.IR-01', 'PR.PS-06']
  implications:
    technical_rationale: |
      `PR.DS-P1`: Data-at-rest are protected (privacy-specific confidentiality control).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo para MICRO: CSF 2/4 → 3/4;
      PF 1/4 → 2/4. Consistente com LIGHTWEIGHT Track B.
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. Tipicamente MUST (P1) para
      PO GDPR-derivadas (cláusulas Art. 5/32/25 quase todas NI=3).
    dependencies: |
      Controlo partilhado via CSF PR.DS-* + PF PR.DS-P1.
```

#### PO-D-01.2-001 — Encrypt all personal data in transit using modern transport cryptographic protection

- **Source obligation:** OBL-D-01.2-001
- **Sub-domain:** D-01.2
- **PF subcategories:** `PR.DS-P2` (data-in-transit protection)
- **CSF subcategories:** `PR.DS-02`, `PR.IR-01`

```yaml
- goal_id: PO-D-01.2-001
  goal_type: PO
  sub_domain: D-01.2
  pf_subcategories: ['PR.DS-P2']
  csf_subcategories: ['PR.DS-02', 'PR.IR-01']
  implications:
    technical_rationale: |
      `PR.DS-P2`: Data-in-transit are protected (privacy-specific transit confidentiality).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo para MICRO: CSF 2/4 → 3/4;
      PF 1/4 → 2/4. Consistente com LIGHTWEIGHT Track B.
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. Tipicamente MUST (P1) para
      PO GDPR-derivadas (cláusulas Art. 5/32/25 quase todas NI=3).
    dependencies: |
      Controlo partilhado via CSF PR.DS-* + PF PR.DS-P2.
```

#### PO-D-01.4-001 — Protect personal data against unauthorised manipulation and accid

- **Source obligation:** OBL-D-01.4-001
- **Sub-domain:** D-01.4
- **PF subcategories:** `CT.DM-P1`, `CT.DM-P3` (review + alteration access)
- **CSF subcategories:** `PR.DS-01`, `PR.DS-10`, `PR.DS-10`

```yaml
- goal_id: PO-D-01.4-001
  goal_type: PO
  sub_domain: D-01.4
  pf_subcategories: ['CT.DM-P1', 'CT.DM-P3']
  csf_subcategories: ['PR.DS-01', 'PR.DS-10', 'PR.DS-10']
  implications:
    technical_rationale: |
      `CT.DM-P1`: Data elements can be accessed for review (privacy integrity review).
      `CT.DM-P3`: Data elements can be accessed for alteration (privacy integrity edit).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo para MICRO: CSF 2/4 → 3/4;
      PF 1/4 → 2/4. Consistente com LIGHTWEIGHT Track B.
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. Tipicamente MUST (P1) para
      PO GDPR-derivadas (cláusulas Art. 5/32/25 quase todas NI=3).
    dependencies: |
      Controlo partilhado via CSF PR.DS-* + PF CT.DM-P1/P3.
```

#### PO-D-05.1-001 — Minimize personal data collection to essential task management fi

- **Source obligation:** OBL-D-05.1-001
- **Sub-domain:** D-05.1
- **PF subcategories:** `CT.DP-P4`, `CT.PO-P4`, `ID.RA-P3` (selective collection + lifecycle + risk identification)
- **CSF subcategories:** `GV.OC-03`, `GV.PO-01`, `GV.PO-02`, `ID.AM-03`

```yaml
- goal_id: PO-D-05.1-001
  goal_type: PO
  sub_domain: D-05.1
  pf_subcategories: ['CT.DP-P4', 'CT.PO-P4', 'ID.RA-P3']
  csf_subcategories: ['GV.OC-03', 'GV.PO-01', 'GV.PO-02', 'ID.AM-03', 'PR.AA-02', 'PR.DS-10']
  implications:
    technical_rationale: |
      `CT.DP-P4`: Selective collection/disclosure configurations (data minimisation).
      `CT.PO-P4`: Data lifecycle aligned with SDLC (privacy lifecycle integration).
      `ID.RA-P3`: Potential problematic data actions identified (risk identification).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo para MICRO: CSF 2/4 → 3/4;
      PF 1/4 → 2/4. Consistente com LIGHTWEIGHT Track B.
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. Tipicamente MUST (P1) para
      PO GDPR-derivadas (cláusulas Art. 5/32/25 quase todas NI=3).
    dependencies: |
      Controlo partilhado via CSF GV/ID/PR.* + PF CT.DP-P4/CT.PO-P4/ID.RA-P3.
```

#### PO-D-05.2-001 — Retain personal data only for duration of active task + 30 days p

- **Source obligation:** OBL-D-05.2-001
- **Sub-domain:** D-05.2
- **PF subcategories:** `CT.DM-P5`, `CT.PO-P4` (destruction + lifecycle)
- **CSF subcategories:** `ID.AM-03`, `PR.DS-10`

```yaml
- goal_id: PO-D-05.2-001
  goal_type: PO
  sub_domain: D-05.2
  pf_subcategories: ['CT.DM-P5', 'CT.PO-P4']
  csf_subcategories: ['ID.AM-03', 'PR.DS-10']
  implications:
    technical_rationale: |
      `CT.DM-P5`: Data are destroyed according to policy (privacy retention enforcement).
      `CT.PO-P4`: Data lifecycle aligned with SDLC (privacy lifecycle integration).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo para MICRO: CSF 2/4 → 3/4;
      PF 1/4 → 2/4. Consistente com LIGHTWEIGHT Track B.
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. Tipicamente MUST (P1) para
      PO GDPR-derivadas (cláusulas Art. 5/32/25 quase todas NI=3).
    dependencies: |
      Controlo partilhado via CSF ID/PR.* + PF CT.DM-P5/CT.PO-P4.
```

#### PO-D-05.3-001 — Enable complete data erasure on user request within 7 days

- **Source obligation:** OBL-D-05.3-001
- **Sub-domain:** D-05.3
- **PF subcategories:** `CT.DM-P4`, `CT.DM-P5` (deletion + destruction)
- **CSF subcategories:** `GV.SC-04`, `PR.DS-10`, `PR.DS-10`, `RS.CO-02`

```yaml
- goal_id: PO-D-05.3-001
  goal_type: PO
  sub_domain: D-05.3
  pf_subcategories: ['CT.DM-P4', 'CT.DM-P5']
  csf_subcategories: ['GV.SC-04', 'PR.DS-10', 'PR.DS-10', 'RS.CO-02']
  implications:
    technical_rationale: |
      `CT.DM-P4`: Data elements can be accessed for deletion (right-to-erasure).
      `CT.DM-P5`: Data are destroyed according to policy (destruction enforcement).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo para MICRO: CSF 2/4 → 3/4;
      PF 1/4 → 2/4. Consistente com LIGHTWEIGHT Track B.
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. Tipicamente MUST (P1) para
      PO GDPR-derivadas (cláusulas Art. 5/32/25 quase todas NI=3).
    dependencies: |
      Controlo partilhado via CSF GV/PR/RS.* + PF CT.DM-P4/P5.
```

#### PO-D-05.4-001 — Provide data export in machine-readable format (JSON) on request

- **Source obligation:** OBL-D-05.4-001
- **Sub-domain:** D-05.4
- **PF subcategories:** `CT.DM-P1`, `CT.DM-P6` (reviewable + standardised formats)
- **CSF subcategories:** `PR.DS-10`, `PR.DS-10`

```yaml
- goal_id: PO-D-05.4-001
  goal_type: PO
  sub_domain: D-05.4
  pf_subcategories: ['CT.DM-P1', 'CT.DM-P6']
  csf_subcategories: ['PR.DS-10', 'PR.DS-10']
  implications:
    technical_rationale: |
      `CT.DM-P1`: Data elements can be accessed for review (data portability access).
      `CT.DM-P6`: Data are transmitted using standardised formats (machine-readable export).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo para MICRO: CSF 2/4 → 3/4;
      PF 1/4 → 2/4. Consistente com LIGHTWEIGHT Track B.
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. Tipicamente MUST (P1) para
      PO GDPR-derivadas (cláusulas Art. 5/32/25 quase todas NI=3).
    dependencies: |
      Controlo partilhado via CSF PR.DS-* + PF CT.DM-P1/P6.
```

#### PO-D-07.1-001 — Integrate data protection measures into processing design from ou

- **Source obligation:** OBL-D-07.1-001
- **Sub-domain:** D-07.1
- **PF subcategories:** `CT.DP-P2`, `CT.DP-P4`, `CT.DP-P5`, `CT.PO-P4`, `GV.PO-P2` (privacy-by-design stack)
- **CSF subcategories:** `PR.DS-01`, `PR.DS-10`, `PR.PS-01`, `PR.PS-06`

```yaml
- goal_id: PO-D-07.1-001
  goal_type: PO
  sub_domain: D-07.1
  pf_subcategories: ['CT.DP-P2', 'CT.DP-P4', 'CT.DP-P5', 'CT.PO-P4', 'GV.PO-P2']
  csf_subcategories: ['PR.DS-01', 'PR.DS-10', 'PR.PS-01', 'PR.PS-06']
  implications:
    technical_rationale: |
      `CT.DP-P2`: Limit identification (de-identification / tokenisation).
      `CT.DP-P4`: Selective collection/disclosure (privacy-by-design configuration).
      `CT.DP-P5`: Attribute references substituted for attribute values (privacy-by-design).
      `CT.PO-P4`: Data lifecycle aligned with SDLC (privacy lifecycle integration).
      `GV.PO-P2`: Privacy values instilled in development/operations (privacy-by-design governance).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo para MICRO: CSF 2/4 → 3/4;
      PF 1/4 → 3/4 (privacy-by-design é high-leverage para D-07.1). Consistente com LIGHTWEIGHT Track B.
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. Tipicamente MUST (P1) para
      PO GDPR-derivadas (cláusulas Art. 5/32/25 quase todas NI=3).
    dependencies: |
      Controlo partilhado via CSF PR.* + PF CT.DP-P2/P4/P5/CT.PO-P4/GV.PO-P2 (privacy-by-design stack).
```

#### PO-D-09.1-001 — Maintain comprehensive privacy policies documenting appropriate m

- **Source obligation:** OBL-D-09.1-001
- **Sub-domain:** D-09.1
- **PF subcategories:** `CM.PO-P1`, `GV.PO-P1`, `GV.PO-P5` (transparency + values + legal)
- **CSF subcategories:** `GV.OC-02`, `GV.OC-03`, `GV.OV-03`, `GV.PO-01`

```yaml
- goal_id: PO-D-09.1-001
  goal_type: PO
  sub_domain: D-09.1
  pf_subcategories: ['CM.PO-P1', 'GV.PO-P1', 'GV.PO-P5']
  csf_subcategories: ['GV.OC-02', 'GV.OC-03', 'GV.OV-03', 'GV.PO-01', 'GV.PO-02', 'GV.RM-04']
  implications:
    technical_rationale: |
      `CM.PO-P1`: Transparency policies for data processing purposes/practices established.
      `GV.PO-P1`: Organizational privacy values and policies established and communicated.
      `GV.PO-P5`: Legal, regulatory, and contractual privacy requirements understood and managed.
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo para MICRO: CSF 2/4 → 3/4;
      PF 1/4 → 2/4. Consistente com LIGHTWEIGHT Track B.
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. Tipicamente MUST (P1) para
      PO GDPR-derivadas (cláusulas Art. 5/32/25 quase todas NI=3).
    dependencies: |
      Controlo partilhado via CSF GV.* + PF CM.PO-P1/GV.PO-P1/GV.PO-P5.
```

#### PO-D-09.2-001 — Conduct privacy impact assessments (DPIA) prior to high-risk proc

- **Source obligation:** OBL-D-09.2-001
- **Sub-domain:** D-09.2
- **PF subcategories:** `ID.RA-P3`, `ID.RA-P4`, `ID.RA-P5` (DPIA identification + scoring + treatment)
- **CSF subcategories:** `GV.OC-03`, `GV.OV-03`, `GV.PO-01`, `GV.RR-02`

```yaml
- goal_id: PO-D-09.2-001
  goal_type: PO
  sub_domain: D-09.2
  pf_subcategories: ['ID.RA-P3', 'ID.RA-P4', 'ID.RA-P5']
  csf_subcategories: ['GV.OC-03', 'GV.OV-03', 'GV.PO-01', 'GV.RR-02', 'GV.SC-02', 'GV.SC-03']
  implications:
    technical_rationale: |
      `ID.RA-P3`: Potential problematic data actions identified (DPIA identification phase).
      `ID.RA-P4`: Problematic data actions, likelihoods, impacts determine/prioritise risk (DPIA scoring).
      `ID.RA-P5`: Risk responses identified, prioritised, implemented (DPIA treatment).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo para MICRO: CSF 2/4 → 3/4;
      PF 1/4 → 3/4 (DPIA é core privacy control). Consistente com LIGHTWEIGHT Track B.
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. Tipicamente MUST (P1) para
      PO GDPR-derivadas (cláusulas Art. 5/32/25 quase todas NI=3).
    dependencies: |
      Controlo partilhado via CSF GV.* + PF ID.RA-P3/P4/P5 (DPIA workflow stack).
```

#### PO-D-09.4-001 — Maintain records of all personal data processing activities

- **Source obligation:** OBL-D-09.4-001
- **Sub-domain:** D-09.4
- **PF subcategories:** `ID.IM-P1`, `ID.IM-P4`, `ID.IM-P6`, `ID.IM-P8` (RoPA inventory + mapping)
- **CSF subcategories:** `DE.AE-03`, `GV.PO-02`, `ID.AM-03`, `PR.AA-02`

```yaml
- goal_id: PO-D-09.4-001
  goal_type: PO
  sub_domain: D-09.4
  pf_subcategories: ['ID.IM-P1', 'ID.IM-P4', 'ID.IM-P6', 'ID.IM-P8']
  csf_subcategories: ['DE.AE-03', 'GV.PO-02', 'ID.AM-03', 'PR.AA-02', 'PR.DS-10', 'PR.PS-04']
  implications:
    technical_rationale: |
      `ID.IM-P1`: Systems/products/services that process data are inventoried (RoPA inventory).
      `ID.IM-P4`: Data actions of the systems/products/services are inventoried (RoPA actions).
      `ID.IM-P6`: Data elements within data actions are inventoried (RoPA elements).
      `ID.IM-P8`: Data processing is mapped (RoPA data flow mapping).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo para MICRO: CSF 2/4 → 3/4;
      PF 1/4 → 3/4 (RoPA é core GDPR Art. 30 control). Consistente com LIGHTWEIGHT Track B.
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. Tipicamente MUST (P1) para
      PO GDPR-derivadas (cláusulas Art. 5/32/25 quase todas NI=3).
    dependencies: |
      Controlo partilhado via CSF DE/GV/ID/PR.* + PF ID.IM-P1/P4/P6/P8 (RoPA stack).
```

---

## Security Operational Objectives (SO) — CSF implications

Security Operational Objectives anchor primarily to the **NIST CSF 2.0** axis. Privacy FW subcategories
apply where the security control also has a privacy dimension (e.g. access control).

### SO Implications Catalog

| Goal ID | Sub-domain | CSF Subcats | PF overlap | Key implication (TinyTask) |
|---|---|---|---|---|
| SO-D-02.1-001 | D-02.1 | ID.IM-02, ID.RA-01, ID.RA-05 | ID.RA-P3, ID.RA-P5 | Improvement processes for cybersecurity risk  |
| SO-D-02.2-001 | D-02.2 | — | — | — |
| SO-D-02.3-001 | D-02.3 | — | — | — |
| SO-D-03.1-001 | D-03.1 | GV.OC-03, GV.PO-02, PR.AA-02 | — | Legal, regulatory, and contractual requiremen |
| SO-D-03.2-001 | D-03.2 | — | — | — |
| SO-D-03.3-001 | D-03.3 | PR.AA-05, PR.AA-06, PR.AT-02 | CT.PO-P1 | Access permissions, entitlements, and authori |
| SO-D-03.4-001 | D-03.4 | PR.DS-10, PR.PS-01, PR.PS-06 | CT.DP-P4, CT.PO-P4 | Data is managed consistent with the organizat |
| SO-D-04.1-001 | D-04.1 | DE.AE-02, DE.CM-01, DE.CM-03 | CM.AW-P7 | Detected events are analyzed to understand at |
| SO-D-04.2-001 | D-04.2 | PR.DS-01, RS.MI-01, RS.MI-02 | CT.DM-P10, PR.PO-P7 | The confidentiality, integrity, and availabil |
| SO-D-04.3-001 | D-04.3 | GV.OC-03, ID.RA-06, PR.DS-01 | CM.AW-P7, CM.AW-P8, CM.PO-P1, CM.PO-P2 | Legal, regulatory, and contractual requiremen |
| SO-D-04.4-001 | D-04.4 | PR.DS-01, PR.IR-04, RC.RP-04 | — | Backups of data are created, protected, maint |
| SO-D-06.1-001 | D-06.1 | GV.SC-02, GV.SC-03 | ID.IM-P2 | Suppliers and other third parties are known,  |
| SO-D-06.2-001 | D-06.2 | — | — | — |
| SO-D-06.3-001 | D-06.3 | DE.CM-06, GV.OC-03, GV.RR-02 | — | External service provider activities and serv |
| SO-D-08.1-001 | D-08.1 | GV.OV-03, ID.IM-02, PR.AA-05 | GV.AT-P1, GV.AT-P2 | Organizational cybersecurity performance is e |
| SO-D-08.2-001 | D-08.2 | PR.AT-01, PR.AT-02 | GV.AT-P1, GV.AT-P2 | All users are informed and trained on cyberse |
| SO-D-09.1-001 | D-09.1 | GV.OC-02, GV.OC-03, GV.OV-03 | CM.PO-P1, GV.PO-P1, GV.PO-P5 | Internal and external stakeholders are unders |
| SO-D-09.2-001 | D-09.2 | GV.OC-03, GV.OV-03, GV.PO-01 | ID.RA-P3, ID.RA-P4, ID.RA-P5 | Legal, regulatory, and contractual requiremen |
| SO-D-10.2-001 | D-10.2 | DE.AE-03, GV.OV-03, GV.PO-02 | CT.DM-P4, CT.DM-P9 | Event data are collected and correlated from  |
| SO-D-10.3-001 | D-10.3 | ID.IM-02, ID.IM-04, ID.RA-01 | ID.RA-P3, ID.RA-P5 | Improvement processes for cybersecurity risk  |

### SO Detail Implications

#### SO-D-02.1-001 — Deliver product with zero known exploitable vulnerabilities

- **Source obligation:** OBL-D-02.1-001
- **Sub-domain:** D-02.1
- **CSF subcategories:** `ID.IM-02`, `ID.RA-01`, `ID.RA-05`, `PR.PS-02`

```yaml
- goal_id: SO-D-02.1-001
  goal_type: SO
  sub_domain: D-02.1
  csf_subcategories: ['ID.IM-02', 'ID.RA-01', 'ID.RA-05', 'PR.PS-02']
  pf_overlap: ['ID.RA-P3', 'ID.RA-P5']
  implications:
    technical_rationale: |
      `ID.IM-02`: Improvement processes for cybersecurity risk management are implemented across organi
      `ID.RA-01`: Vulnerabilities in assets are identified, validated, and recorded
      `ID.RA-05`: Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent ri
      `PR.PS-02`: Software is maintained, replaced, and removed commensurate with risk
      PF overlap: `ID.RA-P3` (potential problematic data actions identified), `ID.RA-P5`
      (risk responses identified, prioritised, implemented). Privacy dimension applies because
      vulnerability handling may surface personal data (e.g., user IDs in crash dumps).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-02.2-001 — Enable automatic security updates for all deployed components

- **Source obligation:** OBL-D-02.2-001
- **Sub-domain:** D-02.2
- **CSF subcategories:** —

```yaml
- goal_id: SO-D-02.2-001
  goal_type: SO
  sub_domain: D-02.2
  csf_subcategories: []
  pf_overlap: []
  implications:
    technical_rationale: |
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-02.3-001 — Publish coordinated vulnerability disclosure policy (security.txt

- **Source obligation:** OBL-D-02.3-001
- **Sub-domain:** D-02.3
- **CSF subcategories:** —

```yaml
- goal_id: SO-D-02.3-001
  goal_type: SO
  sub_domain: D-02.3
  csf_subcategories: []
  pf_overlap: []
  implications:
    technical_rationale: |
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-03.1-001 — Implement authentication controls for all user-facing interfaces

- **Source obligation:** OBL-D-03.1-001
- **Sub-domain:** D-03.1
- **CSF subcategories:** `GV.OC-03`, `GV.PO-02`, `PR.AA-02`, `PR.AA-03`, `PR.DS-10`

```yaml
- goal_id: SO-D-03.1-001
  goal_type: SO
  sub_domain: D-03.1
  csf_subcategories: ['GV.OC-03', 'GV.PO-02', 'PR.AA-02', 'PR.AA-03', 'PR.DS-10']
  pf_overlap: []
  implications:
    technical_rationale: |
      `GV.OC-03`: Legal, regulatory, and contractual requirements regarding cybersecurity — including p
      `GV.PO-02`: Cybersecurity processes and procedures for implementing the cybersecurity policy are
      `PR.AA-02`: Identities are proofed and bound to credentials based on the context of interactions
      `PR.AA-03`: Users, services, and hardware are authenticated
      `PR.DS-10`: Data is managed consistent with the organization's risk strategy to protect the confi
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-03.2-001 — Enable multi-factor authentication where appropriate

- **Source obligation:** OBL-D-03.2-001
- **Sub-domain:** D-03.2
- **CSF subcategories:** —

```yaml
- goal_id: SO-D-03.2-001
  goal_type: SO
  sub_domain: D-03.2
  csf_subcategories: []
  pf_overlap: []
  implications:
    technical_rationale: |
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-03.3-001 — Restrict access to authorised personnel only; enforce least privi

- **Source obligation:** OBL-D-03.3-001
- **Sub-domain:** D-03.3
- **CSF subcategories:** `PR.AA-05`, `PR.AA-06`, `PR.AT-02`

```yaml
- goal_id: SO-D-03.3-001
  goal_type: SO
  sub_domain: D-03.3
  csf_subcategories: ['PR.AA-05', 'PR.AA-06', 'PR.AT-02']
  pf_overlap: ['CT.PO-P1']
  implications:
    technical_rationale: |
      `PR.AA-05`: Access permissions, entitlements, and authorizations are defined and managed in accor
      `PR.AA-06`: Access to physical and logical assets is limited to authorized users, services, and h
      `PR.AT-02`: All members of the organization's workforce understand their roles and responsibiliti
      PF overlap: `CT.PO-P1` (policies for authorizing data processing, including access-based
      authorization). Privacy dimension applies because least-privilege control directly governs
      who can process which personal data.
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-03.4-001 — Disable all unused ports, services, and interfaces by default

- **Source obligation:** OBL-D-03.4-001
- **Sub-domain:** D-03.4
- **CSF subcategories:** `PR.DS-10`, `PR.PS-01`, `PR.PS-06`

```yaml
- goal_id: SO-D-03.4-001
  goal_type: SO
  sub_domain: D-03.4
  csf_subcategories: ['PR.DS-10', 'PR.PS-01', 'PR.PS-06']
  pf_overlap: ['CT.DP-P4', 'CT.PO-P4']
  implications:
    technical_rationale: |
      `PR.DS-10`: Data is managed consistent with the organization's risk strategy to protect the confi
      `PR.PS-01`: Configuration management practices are established, documented, and applied to assets
      `PR.PS-06`: Secure software development practices are integrated, and their performance is monito
      PF overlap: `CT.DP-P4` (selective collection/disclosure configurations), `CT.PO-P4`
      (data lifecycle aligned with SDLC). Privacy dimension applies because hardening defaults
      (disable ports, services) reduces the personal-data attack surface.
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-04.1-001 — Design system to limit severity of exploits; implement fail-safe

- **Source obligation:** OBL-D-04.1-001
- **Sub-domain:** D-04.1
- **CSF subcategories:** `DE.AE-02`, `DE.CM-01`, `DE.CM-03`, `DE.CM-09`, `RS.MA-02`

```yaml
- goal_id: SO-D-04.1-001
  goal_type: SO
  sub_domain: D-04.1
  csf_subcategories: ['DE.AE-02', 'DE.CM-01', 'DE.CM-03', 'DE.CM-09', 'RS.MA-02']
  pf_overlap: ['CM.AW-P7']
  implications:
    technical_rationale: |
      `DE.AE-02`: Detected events are analyzed to understand attack targets and methods
      `DE.CM-01`: Networks and network services are monitored to find potentially adverse events
      `DE.CM-03`: Personnel activity and technology usage are monitored to find potentially adverse eve
      `DE.CM-09`: Computing hardware and software, runtime environments, and their data are monitored t
      `RS.MA-02`: Incident reports are triaged and validated
      PF overlap: `CM.AW-P7` (impacted individuals/organizations notified about privacy breach/event).
      Privacy dimension applies because monitoring may detect breaches involving personal data,
      triggering breach-notification obligations.
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-04.2-001 — Build resilience against denial-of-service attacks

- **Source obligation:** OBL-D-04.2-001
- **Sub-domain:** D-04.2
- **CSF subcategories:** `PR.DS-01`, `RS.MI-01`, `RS.MI-02`

```yaml
- goal_id: SO-D-04.2-001
  goal_type: SO
  sub_domain: D-04.2
  csf_subcategories: ['PR.DS-01', 'RS.MI-01', 'RS.MI-02']
  pf_overlap: ['CT.DM-P10', 'PR.PO-P7']
  implications:
    technical_rationale: |
      `PR.DS-01`: The confidentiality, integrity, and availability of data-at-rest are protected
      `RS.MI-01`: Incidents are contained
      `RS.MI-02`: Incidents are mitigated
      PF overlap: `CT.DM-P10` (stakeholder privacy preferences in algorithmic design), `PR.PO-P7`
      (response plans established). Privacy dimension applies because DoS attacks may degrade
      availability of personal-data services, triggering data-subject impact.
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-04.3-001 — Notify ENISA/CSIRT of actively exploited vulnerabilities within 2

- **Source obligation:** OBL-D-04.3-001
- **Sub-domain:** D-04.3
- **CSF subcategories:** `GV.OC-03`, `ID.RA-06`, `PR.DS-01`, `PR.DS-10`, `PR.DS-10`

```yaml
- goal_id: SO-D-04.3-001
  goal_type: SO
  sub_domain: D-04.3
  csf_subcategories: ['GV.OC-03', 'ID.RA-06', 'PR.DS-01', 'PR.DS-10', 'PR.DS-10', 'PR.IR-03']
  pf_overlap: ['CM.AW-P7', 'CM.AW-P8', 'CM.PO-P1', 'CM.PO-P2']
  implications:
    technical_rationale: |
      `GV.OC-03`: Legal, regulatory, and contractual requirements regarding cybersecurity — including p
      `ID.RA-06`: Risk responses are chosen, prioritized, planned, tracked, and communicated
      `PR.DS-01`: The confidentiality, integrity, and availability of data-at-rest are protected
      `PR.DS-10`: The confidentiality, integrity, and availability of data-in-use are protected
      `PR.DS-10`: Data is managed consistent with the organization's risk strategy to protect the confi
      PF overlap: `CM.AW-P7` (impacted individuals notified about privacy breach), `CM.AW-P8`
      (individuals provided with mitigation mechanisms), `CM.PO-P1`/`CM.PO-P2` (transparency
      policies/roles for breach communication). Privacy dimension is central: dual-notification
      (CNPD 72h + ENISA 24h) per CRA Art. 14 + GDPR Art. 33.
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-04.4-001 — Restore availability and access to data in timely manner after in

- **Source obligation:** OBL-D-04.4-001
- **Sub-domain:** D-04.4
- **CSF subcategories:** `PR.DS-01`, `PR.IR-04`, `RC.RP-04`

```yaml
- goal_id: SO-D-04.4-001
  goal_type: SO
  sub_domain: D-04.4
  csf_subcategories: ['PR.DS-01', 'PR.IR-04', 'RC.RP-04']
  pf_overlap: []
  implications:
    technical_rationale: |
      `PR.DS-01`: Backups of data are created, protected, maintained, and tested
      `PR.IR-04`: Adequate resource capacity to ensure availability is maintained
      `RC.RP-04`: Critical mission functions and services are restored through the implementation of th
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-06.1-001 — Use only third-party processors providing sufficient guarantees

- **Source obligation:** OBL-D-06.1-001
- **Sub-domain:** D-06.1
- **CSF subcategories:** `GV.SC-02`, `GV.SC-03`

```yaml
- goal_id: SO-D-06.1-001
  goal_type: SO
  sub_domain: D-06.1
  csf_subcategories: ['GV.SC-02', 'GV.SC-03']
  pf_overlap: ['ID.IM-P2']
  implications:
    technical_rationale: |
      `GV.SC-02`: Suppliers and other third parties are known, prioritized, and assessed using a cybers
      `GV.SC-03`: Contracts with suppliers and other third parties are used to implement appropriate me
      PF overlap: `ID.IM-P2` (owners/operators of systems and their roles inventoried). Privacy
      dimension applies because processors under DPA are owners/operators of personal data
      (GDPR Art. 28 obligations require documented roles).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-06.2-001 — Maintain Software Bill of Materials in machine-readable format

- **Source obligation:** OBL-D-06.2-001
- **Sub-domain:** D-06.2
- **CSF subcategories:** —

```yaml
- goal_id: SO-D-06.2-001
  goal_type: SO
  sub_domain: D-06.2
  csf_subcategories: []
  pf_overlap: []
  implications:
    technical_rationale: |
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-06.3-001 — Bind processors to security obligations via Data Processing Agree

- **Source obligation:** OBL-D-06.3-001
- **Sub-domain:** D-06.3
- **CSF subcategories:** `DE.CM-06`, `GV.OC-03`, `GV.RR-02`, `GV.SC-01`, `GV.SC-02`

```yaml
- goal_id: SO-D-06.3-001
  goal_type: SO
  sub_domain: D-06.3
  csf_subcategories: ['DE.CM-06', 'GV.OC-03', 'GV.RR-02', 'GV.SC-01', 'GV.SC-02', 'GV.SC-03']
  pf_overlap: []
  implications:
    technical_rationale: |
      `DE.CM-06`: External service provider activities and services are monitored to find potentially a
      `GV.OC-03`: Legal, regulatory, and contractual requirements regarding cybersecurity — including p
      `GV.RR-02`: Roles, responsibilities, authorities, and accountabilities related to cybersecurity r
      `GV.SC-01`: A cybersecurity supply chain risk management program, strategy, objectives, policies,
      `GV.SC-02`: Suppliers and other third parties are known, prioritized, and assessed using a cybers
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-08.1-001 — Conduct security awareness training annually for all staff

- **Source obligation:** OBL-D-08.1-001
- **Sub-domain:** D-08.1
- **CSF subcategories:** `GV.OV-03`, `ID.IM-02`, `PR.AA-05`, `PR.AT-01`, `PR.AT-02`

```yaml
- goal_id: SO-D-08.1-001
  goal_type: SO
  sub_domain: D-08.1
  csf_subcategories: ['GV.OV-03', 'ID.IM-02', 'PR.AA-05', 'PR.AT-01', 'PR.AT-02']
  pf_overlap: ['GV.AT-P1', 'GV.AT-P2']
  implications:
    technical_rationale: |
      `GV.OV-03`: Organizational cybersecurity performance is evaluated and reviewed for needed adjustm
      `ID.IM-02`: Improvement processes for cybersecurity risk management are implemented across organi
      `PR.AA-05`: Access permissions, entitlements, and authorizations are defined and managed in accor
      `PR.AT-01`: All users are informed and trained on cybersecurity topics (e.g., recognition of phis
      `PR.AT-02`: All members of the organization's workforce understand their roles and responsibiliti
      PF overlap: `GV.AT-P1` (workforce informed/trained on privacy roles), `GV.AT-P2`
      (senior executives understand privacy roles). Privacy dimension applies because
      security-awareness training must include privacy breach recognition and notification duties.
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-08.2-001 — Provide role-specific security training to staff with access to p

- **Source obligation:** OBL-D-08.2-001
- **Sub-domain:** D-08.2
- **CSF subcategories:** `PR.AT-01`, `PR.AT-02`

```yaml
- goal_id: SO-D-08.2-001
  goal_type: SO
  sub_domain: D-08.2
  csf_subcategories: ['PR.AT-01', 'PR.AT-02']
  pf_overlap: ['GV.AT-P1', 'GV.AT-P2']
  implications:
    technical_rationale: |
      `PR.AT-01`: All users are informed and trained on cybersecurity topics (e.g., recognition of phis
      `PR.AT-02`: All members of the organization's workforce understand their roles and responsibiliti
      PF overlap: `GV.AT-P1`/`GV.AT-P2` (privacy roles training for workforce + executives).
      Privacy dimension applies because role-specific training for personal-data handlers
      must cover data minimisation and purpose-limitation duties.
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-09.1-001 — Maintain technical documentation for 10 years post-market placeme

- **Source obligation:** OBL-D-09.1-001
- **Sub-domain:** D-09.1
- **CSF subcategories:** `GV.OC-02`, `GV.OC-03`, `GV.OV-03`, `GV.PO-01`, `GV.PO-02`

```yaml
- goal_id: SO-D-09.1-001
  goal_type: SO
  sub_domain: D-09.1
  csf_subcategories: ['GV.OC-02', 'GV.OC-03', 'GV.OV-03', 'GV.PO-01', 'GV.PO-02', 'GV.RM-04']
  pf_overlap: ['CM.PO-P1', 'GV.PO-P1', 'GV.PO-P5']
  implications:
    technical_rationale: |
      `GV.OC-02`: Internal and external stakeholders are understood, and their needs and expectations r
      `GV.OC-03`: Legal, regulatory, and contractual requirements regarding cybersecurity — including p
      `GV.OV-03`: Organizational cybersecurity performance is evaluated and reviewed for needed adjustm
      `GV.PO-01`: Organizational cybersecurity policy is established, communicated, and enforced
      `GV.PO-02`: Cybersecurity processes and procedures for implementing the cybersecurity policy are
      PF overlap: `CM.PO-P1` (transparency policies for data processing), `GV.PO-P1` (privacy
      values/policies established), `GV.PO-P5` (legal/regulatory privacy requirements managed).
      Privacy dimension applies because technical documentation must include privacy-related
      design decisions and DPIA outcomes.
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-09.2-001 — Conduct cybersecurity risk assessment before product launch

- **Source obligation:** OBL-D-09.2-001
- **Sub-domain:** D-09.2
- **CSF subcategories:** `GV.OC-03`, `GV.OV-03`, `GV.PO-01`, `GV.RR-02`, `GV.SC-02`

```yaml
- goal_id: SO-D-09.2-001
  goal_type: SO
  sub_domain: D-09.2
  csf_subcategories: ['GV.OC-03', 'GV.OV-03', 'GV.PO-01', 'GV.RR-02', 'GV.SC-02', 'GV.SC-03']
  pf_overlap: ['ID.RA-P3', 'ID.RA-P4', 'ID.RA-P5']
  implications:
    technical_rationale: |
      `GV.OC-03`: Legal, regulatory, and contractual requirements regarding cybersecurity — including p
      `GV.OV-03`: Organizational cybersecurity performance is evaluated and reviewed for needed adjustm
      `GV.PO-01`: Organizational cybersecurity policy is established, communicated, and enforced
      `GV.RR-02`: Roles, responsibilities, authorities, and accountabilities related to cybersecurity r
      `GV.SC-02`: Suppliers and other third parties are known, prioritized, and assessed using a cybers
      PF overlap: `ID.RA-P3`/`P4`/`P5` (privacy risk identification/prioritisation/response).
      Privacy dimension applies because the cybersecurity risk assessment must include
      privacy risk (DPIA-style) per GDPR Art. 35 + CRA Art. 13.
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-10.2-001 — Log all security-relevant events with immutable audit trail

- **Source obligation:** OBL-D-10.2-001
- **Sub-domain:** D-10.2
- **CSF subcategories:** `DE.AE-03`, `GV.OV-03`, `GV.PO-02`, `ID.AM-03`, `PR.DS-10`

```yaml
- goal_id: SO-D-10.2-001
  goal_type: SO
  sub_domain: D-10.2
  csf_subcategories: ['DE.AE-03', 'GV.OV-03', 'GV.PO-02', 'ID.AM-03', 'PR.DS-10', 'PR.PS-04']
  pf_overlap: ['CT.DM-P4', 'CT.DM-P9']
  implications:
    technical_rationale: |
      `DE.AE-03`: Event data are collected and correlated from multiple sources and sensors
      `GV.OV-03`: Organizational cybersecurity performance is evaluated and reviewed for needed adjustm
      `GV.PO-02`: Cybersecurity processes and procedures for implementing the cybersecurity policy are
      `ID.AM-03`: Inventories of data and corresponding metadata for designated data types are maintain
      `PR.DS-10`: Data is managed consistent with the organization's risk strategy to protect the confi
      PF overlap: `CT.DM-P4` (data elements accessible for deletion, i.e., log retention/deletion),
      `CT.DM-P9` (technical measures for data processing tested/assessed). Privacy dimension
      applies because audit logs may contain personal data and need retention/deletion controls
      (GDPR Art. 5(1)(e)).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

#### SO-D-10.3-001 — Conduct regular security testing and code reviews

- **Source obligation:** OBL-D-10.3-001
- **Sub-domain:** D-10.3
- **CSF subcategories:** `ID.IM-02`, `ID.IM-04`, `ID.RA-01`, `ID.RA-05`, `ID.RA-06`

```yaml
- goal_id: SO-D-10.3-001
  goal_type: SO
  sub_domain: D-10.3
  csf_subcategories: ['ID.IM-02', 'ID.IM-04', 'ID.RA-01', 'ID.RA-05', 'ID.RA-06', 'PR.PS-02']
  pf_overlap: ['ID.RA-P3', 'ID.RA-P5']
  implications:
    technical_rationale: |
      `ID.IM-02`: Improvement processes for cybersecurity risk management are implemented across organi
      `ID.IM-04`: Cybersecurity risk management improvements are informed by awareness of related devel
      `ID.RA-01`: Vulnerabilities in assets are identified, validated, and recorded
      `ID.RA-05`: Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent ri
      `ID.RA-06`: Risk responses are chosen, prioritized, planned, tracked, and communicated
      PF overlap: `ID.RA-P3` (problematic data actions identified), `ID.RA-P5` (risk responses
      identified/prioritised/implemented). Privacy dimension applies because security testing
      (e.g., code review, pen-tests) may surface privacy issues (e.g., data leakage).
    maturity_target_micro: |
      [PENDENTE SPEC §7] Maturidade-alvo MICRO: CSF 2/4 → 3/4 (LIGHTWEIGHT Track B).
    ni_note: |
      [PENDENTE SPEC §6] AVG(NI) sobre cláusulas source. SO derivadas de Art. 32
      (TOMs) tipicamente NI=3 MUST; SO de boas-práticas podem ser SHOULD.
    dependencies: |
      Ver baseline 01b para articulação com SOs via sub_domain.
```

---

## Notes

1. **AI RMF not applicable.** Case_01 has no AI systems. The AI Act → AI RMF
   implications (baseline 01b AI Act) are inherited as `pending` but do not apply.
2. **Dual-maturity [PENDENTE SPEC §7].** When the unified matrix (Doc 13) is built,
   each PO will have CSF + Privacy scores; each SO primarily CSF (PF overlap where
   applicable). This file pre-positions the goals for that integration.
3. **MICRO proportionality.** All target maturities assume LIGHTWEIGHT Track B
   (typical MICRO pattern). Higher targets require explicit justification.
4. **Same goal ID namespace.** No new goals created — implications only on the
   existing 31 PO/SO from 10_Privacy_Security_Objectives.md.
