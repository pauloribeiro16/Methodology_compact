---
document_id: AEGIS-P2-RICH-13-CASE02
title: Framework Mapping Matrix — Unified NIST (CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0)
phase: 2
version: 5.2
created: 2026-08-07
updated: 2026-08-13
author: Executor (Bloco C)
status: ACTIVE
sprint: 10
case: Case_02_SecureBorder_Solutions
tier: HIGH
applicable_regulations: [GDPR, CRA, NIS_2, AI_Act]
frameworks_in_scope: [NIST_CSF_2.0, NIST_Privacy_FW_1.0, NIST_AI_RMF_1.0]   # all 3 active for Case_02
frameworks_placeholder: []   # no placeholder in this case
normative_intensity_rule: AVG_with_AI_MUST_override
dr_002_resolution: >
  DR-002 definido como AVG (não MAX). MAX mata diferenciação (AP-P2-09).
  AVG preserva SHOULD. Adicionalmente, qualquer CR com AI-C* nas source
  clauses é forçado MUST (NI=3) — alinhamento com a baseline AI_Act
  (todas as 28 cláusulas AI_Act em scope são NI=3 → MUST; AI-C19 Art. 26
  deployer obligations excluded per D1 — SecureBorder is PROVIDER only).
  Aplicado retroactivamente a todos os 79 cartões.
ni_avg_rule_note: |
  AVG(NI) per regulation source clauses. AI-C* presence forces MUST (NI=3)
  to preserve AI_Act signal (baseline). NIS2-C10/C19/C29 with NI=2 do
  not override the AI MUST signal.
inputs: [Doc18_Rules_Catalog.md,           # in 02_PHASE2_RULES_RICH/ (Rich copy)
         Doc14_Obligation_Derivation.md,   # in 02_PHASE2_RULES_RICH/ (Rich copy)
         Doc15_Strategic_Tensions_Report.md,
         Doc16_Privacy_Security_Goals.md,
         12_Rules_Catalog.xlsx,
         README.md,
         PROJECT_STATE.md,
         Framework_Crosswalk_ARM.md, NIST_PF_1.0_subcategories.md,
         NIST_AI_RMF_1.0_subcategories.md, NIST_CSF_2.0_subcategories.md,
         GDPR/02b_SecurityRules_NISTPF.md, AI_Act/02b_SecurityRules_NISTAIRMF.md,
         Doc12_Proportionality_Profile.md, Doc05_Security_Posture.md]
outputs: [Phase 3 inputs, 12_Rules_Catalog.xlsx]
traceability: AEGIS Framework Mapping Layer (CSF + PF + AI RMF)
related_documents: Doc18_Rules_Catalog.md, 12_Rules_Catalog.xlsx, Doc05_Security_Posture.md,
                   Doc15_Strategic_Tensions_Report.md
note_inputs: >
  (2026-08-13, R9) Earlier this note referenced a `../02_PHASE2_RULES/`
  sibling folder that no longer exists. The current Doc18_Rules_Catalog.md
  in this RICH folder is now self-canonical for Case_02; cross-case
  references should treat `02_PHASE2_RULES_RICH/Doc18_Rules_Catalog.md`
  as the live operational document. The earlier pointer has been
  removed as it pointed to a non-existent path.
---

# Framework Mapping Matrix — Unified NIST (CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0)

> **Case_02 — SecureBorder Solutions B.V.** (HIGH complexity; 4 applicable regulations: GDPR + CRA + NIS 2 + AI_Act).
> This document unifies the three NIST frameworks against the 38 unique Compliance Rules (CR) and 17 Best Practice Rules (BPR-D-*) — 55 cards total — derived from Phase 2.
> All three frameworks are ACTIVE for Case_02 (AI_Act applicable). The matrix follows the AEGIS invariant: **frameworks are mapping targets, never derivation sources.** CR and BPR are derived from regulatory obligations (`Doc18_Rules_Catalog.md`); this matrix anchors each rule to the corresponding subcategory(ies) in the three frameworks.

---

## §1 — Matriz Unificada (CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0)

> 38 unique CR rows. Columns: rule_id, sub_domain, regulations, NI (recomputed by AVG + AI-C MUST override), CSF 2.0 subcategories, Privacy FW 1.0 subcategories, AI RMF 1.0 subcategories, ISO 27001 mapping, secure-development standards mapping, csf_norm, priv_norm, airmf_norm.
> `csf_norm = min(|CSF subcats|) if |CSF subcats|>0 else '—'`; `priv_norm` and `airmf_norm` same convention.
> Marker vocabulary per SPEC §4.6 (canonical, port Fase 3): `UNMAPPED_CSF` / `UNMAPPED_PF` with justification where no natural anchor exists; `N/A (non-AI scope)` where the rule has no AI dimension; `UNMAPPED_PRIVACY` is a RETIRED token (zero tolerance).
> Privacy FW mapping sourced from `Regulation/GDPR/02b_SecurityRules_NISTPF.md` (68 SR, 59/104 active subcats; 100% coverage for GDPR-touched sub-domains).
> AI RMF mapping sourced from `Regulation/AI_Act/02b_SecurityRules_NISTAIRMF.md` (24 SR, 41/72 active subcats). For CR with AI-C* source clauses, AI RMF mapping is anchored via SR-AIACT-XXX. For CR without AI-C* (21 CR), `UNMAPPED_AIRMF` with justification.
> ISO 27001 mapping / secure-development standards mapping from `Framework_Crosswalk_ARM.md` (ACTIVE v1.0; CSF 38/38, ISO 38/38, secure-development standards 23/38; 800-53 out of scope per `note_800_53`).

| rule_id | sub_domain | regulations | NI | CSF 2.0 | Privacy FW 1.0 | AI RMF 1.0 | ISO 27001 | SSDF | csf_norm | priv_norm | airmf_norm |
|---------|-----------|-------------|----|---------|----------------|-----------|-----------|------|----------|-----------|-----------|

| CR-D-01.1-001 | D-01.1 | GDPR,CRA,NIS2,AI_Act | 3.00 (MUST) | PR.DS-01 | PR.DS-P1,CT.DP-P2 | GOVERN-1.6,MEASURE-2.7,MEASURE-2.5 | A.8.24, A.8.13 | PO.5 | 1 | 2 | 3 |
| CR-D-01.2-001 | D-01.2 | GDPR,CRA,NIS2 | 3.00 (MUST) | PR.DS-02 | PR.DS-P2 | N/A (non-AI scope) | A.8.24, A.8.20 | — | 1 | 2 | 0 |
| CR-D-01.3-001 | D-01.3 | CRA,NIS2,AI_Act | 3.00 (MUST) | PR.DS-01 | PR.DS-P1,CT.DP-P2 | MEASURE-2.7,GOVERN-1.6 | A.8.24 | — | 1 | 2 | 2 |
| CR-D-01.4-001 | D-01.4 | GDPR,CRA,AI_Act | 3.00 (MUST) | PR.DS-01,PR.DS-02 | PR.DS-P1,CT.DM-P1,CT.DM-P3 | MEASURE-2.6,MEASURE-2.7,MANAGE-2.3 | A.8.24, A.5.14 | — | 2 | 3 | 3 |
| CR-D-02.1-001 | D-02.1 | CRA,NIS2,AI_Act | 3.00 (MUST) | ID.RA-01; ID.RA-08 | ID.RA-P3,ID.RA-P5 | MEASURE-1.1,MEASURE-2.1,MEASURE-2.3,MAP-3.3,MEASURE-2.7,MANAGE-1.3,MAP-3.2 | A.8.8, A.5.7 | RV.1, RV.3 | 2 | 2 | 7 |
| CR-D-02.2-001 | D-02.2 | CRA,NIS2 | 3.00 (MUST) | PR.PS-02 | UNMAPPED_PF (no PF 1.0 analogue for product patch/OTA update management) | N/A (non-AI scope) | A.8.8, A.8.19 | RV.2 | 1 | 1 | 0 |
| CR-D-02.3-001 | D-02.3 | CRA,NIS2 | 3.00 (MUST) | ID.RA-08 | ID.IM-P7,GV.PO-P5 | N/A (non-AI scope) | A.5.5, A.5.6 | RV.1 | 1 | 2 | 0 |
| CR-D-02.4-001 | D-02.4 | NIS2,AI_Act | 3.00 (MUST) | ID.IM-02,ID.RA-03 | ID.RA-P3,ID.RA-P4,ID.RA-P5 | MEASURE-2.7,MEASURE-2.11 | A.5.35, A.5.36 | PW.8 | 2 | 3 | 2 |
| CR-D-03.1-001 | D-03.1 | CRA,NIS2,AI_Act | 3.00 (MUST) | PR.AA-01,PR.AA-03,PR.AA-05 | CT.PO-P1 | MAP-3.5,GOVERN-2.1,GOVERN-3.1 | A.5.16, A.5.18 | — | 3 | 5 | 3 |
| CR-D-03.2-001 | D-03.2 | CRA,NIS2 | 3.00 (MUST) | PR.AA-03 | UNMAPPED_PF (no PF 1.0 MFA subcategory) | N/A (non-AI scope) | A.8.5, A.8.2 | — | 1 | 1 | 0 |
| CR-D-03.3-001 | D-03.3 | GDPR,NIS2 | 3.00 (MUST) | PR.AA-05,PR.AA-01 | CT.PO-P1 | N/A (non-AI scope) | A.5.15, A.5.18, A.8.3 | — | 2 | 3 | 0 |
| CR-D-03.4-001 | D-03.4 | CRA | 3.00 (MUST) | PR.PS-01 | CT.DP-P4,CT.PO-P4 | N/A (non-AI scope) | A.8.9 | PW.9 | 1 | 2 | 0 |
| CR-D-04.1-001 | D-04.1 | CRA,NIS2,AI_Act | 3.00 (MUST) | DE.AE-02,DE.CM-01,DE.CM-09 | CM.AW-P7 | MEASURE-2.4,MEASURE-3.1,MANAGE-2.3,MANAGE-4.1 | A.5.25, A.8.16 | RV.1 | 3 | 2 | 4 |
| CR-D-04.2-001 | D-04.2 | GDPR,CRA,NIS2 | 3.00 (MUST) | RS.MI-01,RS.MI-02 | PR.PO-P7,CT.DM-P10 | N/A (non-AI scope) | A.5.26, A.5.29 | — | 2 | 4 | 0 |
| CR-D-04.3-001 | D-04.3 | GDPR,CRA,NIS2,AI_Act | 3.00 (MUST) | RS.CO-02,RS.CO-03 | CM.AW-P7,CM.PO-P2,CM.PO-P1,GV.PO-P5 | MANAGE-2.3,MANAGE-4.3,GOVERN-1.1 | A.5.24, A.5.5 | — | 2 | 4 | 3 |
| CR-D-04.4-001 | D-04.4 | GDPR,NIS2 | 3.00 (MUST) | RC.RP-01,RC.RP-03,RC.RP-05 | UNMAPPED_PF (no PF 1.0 backup/DR recovery subcategory) | N/A (non-AI scope) | A.8.13, A.8.14, A.5.30 | — | 3 | 3 | 0 |
| CR-D-05.1-001 | D-05.1 | GDPR,CRA,AI_Act | 3.00 (MUST) | PR.DS-10,ID.AM-03 | CT.PO-P4,CT.DP-P4,ID.RA-P3 | GOVERN-1.4,MAP-2.1,MEASURE-2.11,MAP-2.2 | A.8.10 | — | 2 | 3 | 4 |
| CR-D-05.2-001 | D-05.2 | GDPR,AI_Act | 3.00 (MUST) | PR.DS-01,PR.PS-06 | CT.PO-P4,CT.DM-P5 | MEASURE-2.4,MEASURE-4.2,GOVERN-1.4 | A.5.33, A.5.31 | PS.3 | 2 | 2 | 3 |
| CR-D-05.3-001 | D-05.3 | GDPR,CRA | 3.00 (MUST) | PR.DS-10 | CT.DM-P4,CT.DM-P5 | N/A (non-AI scope) | A.8.10, A.7.14, A.5.34 | — | 1 | 2 | 0 |
| CR-D-05.4-001 | D-05.4 | GDPR | 3.00 (MUST) | UNMAPPED_CSF | CT.DM-P1,CT.DM-P6 | N/A (non-AI scope) | A.5.14, A.5.34 | — | 0 | 2 | 0 |
| CR-D-06.1-001 | D-06.1 | GDPR,NIS2 | 3.00 (MUST) | GV.SC-04; GV.SC-07; ID.RA-10 | ID.IM-P2 | N/A (non-AI scope) | A.5.19, A.5.20, A.5.22 | PW.4 | 3 | 2 | 0 |
| CR-D-06.2-001 | D-06.2 | CRA | 3.00 (MUST) | GV.SC-09 | ID.IM-P7 | N/A (non-AI scope) | A.5.21, A.5.9 | PS.3 | 1 | 1 | 0 |
| CR-D-06.3-001 | D-06.3 | GDPR,NIS2 | 3.00 (MUST) | GV.SC-05; GV.SC-06 | GV.PO-P5 | N/A (non-AI scope) | A.5.20, A.5.31 | — | 2 | 3 | 0 |
| CR-D-06.4-001 | D-06.4 | NIS2 | 3.00 (MUST) | DE.CM-06,PR.IR-01 | UNMAPPED_PF (no PF 1.0 analogue for physical third-party boundary isolation) | N/A (non-AI scope) | A.8.22, A.8.21 | — | 2 | 1 | 0 |
| CR-D-07.1-001 | D-07.1 | GDPR,CRA,AI_Act | 3.00 (MUST) | PR.PS-06,ID.RA-01 | GV.PO-P2,CT.PO-P4,CT.DP-P2,CT.DP-P5 | MEASURE-2.7 | A.8.25, A.8.27, A.5.8 | PO.1, PW.1 | 2 | 4 | 0 |
| CR-D-07.2-001 | D-07.2 | CRA,NIS2 | 3.00 (MUST) | PR.PS-06 | UNMAPPED_PF (no PF 1.0 secure-SDLC subcategory) | N/A (non-AI scope) | A.8.28, A.8.26 | PW.5 | 1 | 1 | 0 |
| CR-D-07.3-001 | D-07.3 | NIS2 | 3.00 (MUST) | PR.PS-06,PR.PS-02 | PR.PO-P4 | N/A (non-AI scope) | A.8.4, A.8.31, A.8.29 | PO.3, PW.6 | 2 | 1 | 0 |
| CR-D-07.4-001 | D-07.4 | NIS2 | 2.00 (SHOULD) | ID.RA-07 | ID.RA-P3 | N/A (non-AI scope) | A.8.32, A.8.19 | RV.3 | 1 | 1 | 0 |
| CR-D-08.1-001 | D-08.1 | GDPR,NIS2 | 3.00 (MUST) | PR.AT-01 | GV.AT-P1,GV.AT-P2 | N/A (non-AI scope) | A.6.3 | PO.2 | 1 | 2 | 0 |
| CR-D-08.2-001 | D-08.2 | GDPR,NIS2,AI_Act | 3.00 (MUST) | PR.AT-02 | GV.AT-P1,GV.AT-P2 | MAP-3.5,GOVERN-2.1,GOVERN-2.2,GOVERN-3.1 | A.6.3, A.6.1 | PO.2 | 1 | 2 | 4 |
| CR-D-08.3-001 | D-08.3 | NIS2 | 3.00 (MUST) | GV.RR-01,PR.AT-02 | UNMAPPED_PF (no PF 1.0 board-training subcategory) | N/A (non-AI scope) | A.5.4, A.5.35 | PO.2 | 2 | 1 | 0 |
| CR-D-09.1-001 | D-09.1 | GDPR,CRA,NIS2,AI_Act | 3.00 (MUST) | GV.PO-01,GV.PO-02 | GV.PO-P1,GV.PO-P5,CM.PO-P1 | GOVERN-1.1,GOVERN-1.3,GOVERN-1.4,GOVERN-1.6,MAP-1.1,MEASURE-2.8,MEASURE-2.9,MAP-3.4 | A.5.1, A.5.36, A.5.37 | PO.4 | 2 | 5 | 8 |
| CR-D-09.2-001 | D-09.2 | GDPR,CRA,NIS2,AI_Act | 3.00 (MUST) | ID.RA-04,ID.RA-05,GV.RM-06 | ID.RA-P3,ID.RA-P4,ID.RA-P5 | GOVERN-1.1,GOVERN-1.3,GOVERN-1.5,MAP-5.1,MAP-3.1,MAP-3.2,MANAGE-1.2 | A.5.7, A.5.9, A.5.12 | PW.1 | 3 | 4 | 7 |
| CR-D-09.3-001 | D-09.3 | NIS2 | 3.00 (MUST) | ID.AM-01,ID.AM-02,ID.AM-07 | ID.IM-P1,ID.IM-P4,ID.IM-P6,ID.IM-P8 | N/A (non-AI scope) | A.5.9, A.7.10 | — | 3 | 4 | 0 |
| CR-D-09.4-001 | D-09.4 | GDPR,AI_Act | 3.00 (MUST) | ID.AM-07,GV.OC-03 | ID.IM-P1,ID.IM-P4,ID.IM-P6,ID.IM-P8,CM.PO-P1 | MEASURE-2.4,MEASURE-3.1,GOVERN-1.6,GOVERN-2.1,MEASURE-4.2 | A.5.33, A.5.34, A.5.31 | PO.3 | 2 | 5 | 5 |
| CR-D-10.1-001 | D-10.1 | CRA,NIS2,AI_Act | 3.00 (MUST) | DE.CM-01,DE.CM-09,DE.AE-02 | CM.AW-P7 | MANAGE-4.1,MEASURE-3.1,MEASURE-4.1,GOVERN-1.5,MEASURE-2.4 | A.8.16, A.7.4, A.5.22 | RV.1 | 3 | 2 | 5 |
| CR-D-10.2-001 | D-10.2 | CRA,NIS2,AI_Act | 3.00 (MUST) | PR.PS-04,DE.AE-03,RS.AN-06 | CT.DM-P9 | MEASURE-2.4,MEASURE-3.1,GOVERN-1.6,MEASURE-4.2,GOVERN-1.4,GOVERN-2.1 | A.8.15, A.5.28, A.8.17 | PO.3 | 3 | 1 | 6 |
| CR-D-10.3-001 | D-10.3 | GDPR,CRA,NIS2,AI_Act | 3.00 (MUST) | ID.IM-01,ID.IM-02,ID.IM-03 | UNMAPPED_PF (no PF 1.0 compliance-testing subcategory) | MEASURE-2.7,MEASURE-2.11,MANAGE-1.2,MEASURE-3.1 | A.5.35, A.5.36, A.8.29 | PW.7, PW.8 | 3 | 1 | 4 |

**Regulations column legend.** `GDPR,CRA,NIS2,AI_Act` (4) — all 4 apply. `GDPR,CRA,NIS2` (3) — 3 apply. `CRA,NIS2,AI_Act` (3) — 3 apply. `GDPR,AI_Act` (2), `GDPR,CRA` (2), `CRA,NIS2` (2), `GDPR,NIS2` (2), `NIS2,AI_Act` (2), `CRA` (1), `GDPR` (1), `NIS2` (1) — fewer apply (Sole-Authority rules per `Doc18_Rules_Catalog.md` §6.4).

**`UNMAPPED_*` rationale (Case_02 specifics):**
- `UNMAPPED_CSF` (1 row — `CR-D-05.4-001` data portability): CSF 2.0 has no subcategory addressing data subject portability rights (confirmed in `Framework_Crosswalk_ARM.md` §3.D-05.4 — NONE for CSF). Privacy FW 1.0 covers it natively via `CT.DM-P1/P6`.
- `UNMAPPED_PRIVACY` (0 rows in §1 matrix; token RETIRED — the 2 former `UNMAPPED_PRIVACY` cells for CR-D-07.3-001/BPR-D-07.5-001 are now `PR.PO-P4`): all 38 CR touch at least one GDPR-touched sub-domain, and the 68 SR in `02b_SecurityRules_NISTPF.md` provide 100% PF coverage for the GDPR axis. No `UNMAPPED_PRIVACY` tokens needed.
- `N/A (non-AI scope)` (21 rows, adjudicated from retired `UNMAPPED_AIRMF` per SPEC §4.6 in port Fase 3): 21 CR have no AI-C* in source clauses (no AI dimension). The remaining 17 CR (those with AI-C*) carry AI RMF anchors via the 24 SR-AIACT-XXX mappings. The 31/72 unused AI RMF subcategories are the `MEASURE-2.*` (environmental / human subjects) and `MANAGE-2.*` clusters that have no AI_Act T5 counterpart (documented in `02b_SecurityRules_NISTAIRMF.md` §"Unused AI RMF Subcategories").

**Distribution snapshot:**

| Frameworks with natural anchor | CR count | BPR count | Notes |
|--------------------------------|---------:|----------:|-------|
| CSF + PF + AI RMF (all 3) | 17 | 0 | AI-C* source — full triple coverage |
| CSF + PF only (no AI RMF) | 21 | 17 | BPR-D-* + CR without AI-C*; AI RMF not anchored |
| CSF + AI RMF only (no PF) | 0 | 0 | AI-C* source always also touches a GDPR sub-domain |
| PF + AI RMF only (no CSF) | 0 | 0 | Privacy/AI always co-anchored with security in this case |
| CSF only | 0 | 0 | every CR touches a privacy sub-domain in this case |
| PF only | 0 | 0 | every CR with PF anchor also has CSF anchor |
| AI RMF only | 0 | 0 | every CR with AI RMF anchor also has CSF+PF |
| **Total cards with CSF anchor** | **38** | **17** |
| **Total cards with PF anchor** | **38** | **17** | 100% via GDPR SR coverage |
| **Total cards with AI RMF anchor** | **17** | **0** | AI-C* presence only in 17 CR (none of the 17 BPR have AI-C*) |

---

## §2 — Vista Govern Consolidada 3-way (CSF GV + Privacy FW GV-P + AI RMF GOVERN)

> Mirrors Case_01 SPEC §4.4 but extended to 3 active frameworks. For each of 6 governance concepts, a sub-section with rows for the 3 framework Govern anchors + Case_02 CR anchor column.
> AI RMF column is ACTIVE in this case (Case_02 has AI_Act applicable), unlike Case_01 where it was a placeholder.

### §2.1 — Missão e objectivos organizacionais (mission)

| Framework | Subcategoria | Statement (resumo) | Cobertura Case_02 |
|-----------|--------------|--------------------|-------------------|
| CSF 2.0 | `GV.OC-01` | Missão organizacional compreendida e informa a gestão de risco | ✅ CR-D-09.1-001 (ISMS) |
| Privacy FW | `ID.BE-P1` (≈ `ID.IM-P1`) | Inventário de sistemas/processos que processam dados | ✅ CR-D-09.1-001, CR-D-09.4-001 |
| AI RMF | `GOVERN-1.1` | Requisitos legais e regulatórios (incluindo missões de IA) | ✅ CR-D-09.1-001, CR-D-09.2-001 |

### §2.2 — Requisitos legais e regulatórios (legal)

| Framework | Subcategoria | Statement (resumo) | Cobertura Case_02 |
|-----------|--------------|--------------------|-------------------|
| CSF 2.0 | `GV.OC-03`, `GV.LR-*` (CSF 2.0 GV-LR foi consolidado em GV.OC-03) | Requisitos legais, regulatórios, contratuais compreendidos e geridos — inclui privacidade e liberdades civis | ✅ CR-D-09.1-001, CR-D-09.4-001 |
| Privacy FW | `GV.PO-P5` | Requisitos legais, regulatórios, contratuais relativos a privacidade compreendidos e geridos | ✅ CR-D-09.1-001, CR-D-06.3-001, CR-D-09.4-001 |
| AI RMF | `GOVERN-1.1` | Requisitos legais e regulatórios (AI_Act) | ✅ CR-D-09.1-001, CR-D-09.2-001, CR-D-04.3-001 (AI_Act market surveillance) |

**4-regulation convergence.** All 4 regulations (GDPR, CRA, NIS 2, AI_Act) anchor in this section — SecureBorder's ISMS (CR-D-09.1-001) explicitly carries "regulation-specific annexes" per the implementation guidance in `Doc18_Rules_Catalog.md` §8.3.

### §2.3 — Política de segurança / privacidade / IA (policy)

| Framework | Subcategoria | Statement (resumo) | Cobertura Case_02 |
|-----------|--------------|--------------------|-------------------|
| CSF 2.0 | `GV.PO-01`, `GV.PO-02` | Política de cibersegurança estabelecida, comunicada, mantida; revista e actualizada periodicamente | ✅ CR-D-09.1-001 (ISO 27001 ISMS base) |
| Privacy FW | `GV.PO-P1` | Valores e políticas de privacidade organizacional | ✅ CR-D-09.1-001 (GDPR Annex), CR-D-09.4-001 |
| AI RMF | `GOVERN-1.4` | Políticas, procedimentos e controlos transparentes para gestão de risco de IA | ✅ CR-D-09.1-001 (AI_Act Annex), CR-D-05.1-001 (data governance) |

### §2.4 — Papéis e responsabilidades (roles)

| Framework | Subcategoria | Statement (resumo) | Cobertura Case_02 |
|-----------|--------------|--------------------|-------------------|
| CSF 2.0 | `GV.RR-01`, `GV.RR-02`, `GV.RR-04` | Liderança accountable; roles, responsabilidades, autoridades comunicadas; recursos adequados alocados | ✅ CR-D-09.1-001, CR-D-08.3-001 (NIS 2 board liability) |
| Privacy FW | `GV.PO-P1` (PF 1.0 frozen mirror has no dedicated roles subcategory; governance-policy subcategory covers accountability — element gap recorded in §6.2) | Liderança responsável; papéis workforce; recursos adequados (DPO per Art. 37) | ✅ CR-D-09.1-001, CR-D-09.4-001 (DPO designation) |
| AI RMF | `GOVERN-2.1`, `GOVERN-2.2`, `GOVERN-3.1` | Papéis, responsabilidades documentados; treino; decisão informada por equipa diversa | ✅ CR-D-03.1-001, CR-D-08.2-001, CR-D-09.1-001 (AI Governance Lead) |

### §2.5 — Gestão de risco (risk) — **special section: T-001..T-004 cross-reference**

| Framework | Subcategoria | Statement (resumo) | Cobertura Case_02 |
|-----------|--------------|--------------------|-------------------|
| CSF 2.0 | `GV.RM-01..07` (estratégia + processo), `ID.RA-01..10` (análise) | Estratégia de risco; identificação, análise, priorização; respostas; monitorização | ✅ CR-D-09.2-001 (unified risk assessment) |
| Privacy FW | `ID.RA-P1..P5`, `GV.RM-P1..P4` | Ações de dados problemáticos identificadas; respostas; estratégia revista | ✅ CR-D-09.2-001, CR-D-09.4-001 |
| AI RMF | `GOVERN-5.*`, `MAP-5.*` (impactos), `MANAGE-1.*` (tratamento) | Feedback externo; impactos; tratamento priorizado | ✅ CR-D-09.2-001, CR-D-10.1-001 |

**Strategic tensions cross-reference** (per `Doc15_Strategic_Tensions_Report.md`):

| Tension | Sub-Domain | Risk-framework convergence point | Resolution pattern (in Doc 11 / Phase 2) |
|---------|-----------|----------------------------------|------------------------------------------|
| **T-001** | D-04.3 (Regulatory Notification) | All 4 risk/notification frameworks converge on incident classification + max-SLA routing (24h early warning) | `CR-D-04.3-001` — unified incident classification workflow + 24h ENISA/CSIRT + 72h SA + 15d MSA + 2d widespread AI_Act |
| **T-002** | D-05.3 (Erasure) ↔ D-10.2 (Logging) | GDPR right-to-erasure (`GV.PO-P1` + `CT.DM-P4/5`) vs AI_Act log retention (`MEASURE-2.4` + `MEASURE-4.2`) | `CR-D-05.3-001` (cryptographic sharding) + `CR-D-10.2-001` (tokenised log) — privacy + AI RMF converge on anonymisation |
| **T-003** | D-09.2 (Impact & Risk Assessment) | GDPR DPIA (`ID.RA-P3/4/5`) vs AI_Act FRIA (`GOVERN-1.1/1.3/1.5` + `MAP-5.1`) — both are risk-management processes | `CR-D-09.2-001` — unified DPIA + FRIA single process, dual output; per-reg templates preserved verbatim (F-02 caution) |
| **T-004** | D-09.1 (Documentation) | 4 regulations × documentation obligations | `CR-D-09.1-001` — ISO 27001 ISMS base + 4 regulation-specific annexes (GDPR / CRA / NIS 2 / AI_Act) |

> **Convergence point at D-09.2.** The 4 regulations' risk frameworks converge at `CR-D-09.2-001` (unified DPIA + FRIA + NIS 2 risk assessment + CRA risk-management process). The CSF axis anchors via `ID.RA-04/05`; the Privacy FW axis via `ID.RA-P3/4/5`; the AI RMF axis via `GOVERN-1.1/1.3/1.5` + `MAP-5.1`. See §3 mapping entry for `CR-D-09.2-001`.

### §2.6 — Estratégia e melhoria contínua (strategy)

| Framework | Subcategoria | Statement (resumo) | Cobertura Case_02 |
|-----------|--------------|--------------------|-------------------|
| CSF 2.0 | `GV.STR-*`, `GV.OV-01..03` | Estratégia, políticas, procedimentos, processo, integração; revisão | ✅ CR-D-09.1-001, CR-D-10.3-001 (compliance testing + lessons learned) |
| Privacy FW | `GV.MT-P6` (melhoria), `GV.MT-P1` (revisão) | Estratégia revista; melhoria; performance medida | ✅ CR-D-10.3-001, CR-D-09.4-001 |
| AI RMF | `GOVERN-1.5`, `GOVERN-6.1` (third-party), `MANAGE-4.*` (incident feedback) | Monitorização contínua; políticas de third-party; lições aprendidas | ✅ CR-D-09.1-001, CR-D-10.1-001, CR-D-10.3-001 |

---

## §3 — Mapeamento n:m CR/BPR ↔ Subcategorias (38 CR + 17 BPR = 55 cards)

> For each of the 55 cards, a YAML block with `rule_id, subdomain, regulations, normative_intensity, priority_label, csf_subcategories, privacy_subcategories, airmf_subcategories, mapping_rationale`. The 3 subcat lists are drawn from the frozen lists (`NIST_CSF_2.0_subcategories.md`, `NIST_PF_1.0_subcategories.md`, `NIST_AI_RMF_1.0_subcategories.md`); BPR may have `[]` where the framework source has no natural anchor (D16: coerência BPR, not 100%).

### §3.1 — Compliance Rules (38 CR)

```yaml
- rule_id: CR-D-01.1-001
  subdomain: D-01.1
  regulations: [GDPR,CRA,NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.DS-01]
  privacy_subcategories: [PR.DS-P1,CT.DP-P2]
  airmf_subcategories: [GOVERN-1.6,MEASURE-2.7,MEASURE-2.5]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-01.2-001
  subdomain: D-01.2
  regulations: [GDPR,CRA,NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.DS-02]
  privacy_subcategories: [PR.DS-P2]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-01.3-001
  subdomain: D-01.3
  regulations: [CRA,NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.DS-01]
  privacy_subcategories: [PR.DS-P1,CT.DP-P2]
  airmf_subcategories: [MEASURE-2.7,GOVERN-1.6]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-01.4-001
  subdomain: D-01.4
  regulations: [GDPR,CRA,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.DS-01,PR.DS-02]
  privacy_subcategories: [PR.DS-P1,CT.DM-P1,CT.DM-P3]
  airmf_subcategories: [MEASURE-2.6,MEASURE-2.7,MANAGE-2.3]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-02.1-001
  subdomain: D-02.1
  regulations: [CRA,NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [ID.RA-01,ID.RA-08]
  privacy_subcategories: [ID.RA-P3,ID.RA-P5]
  airmf_subcategories: [MEASURE-1.1,MEASURE-2.1,MEASURE-2.3,MAP-3.3,MEASURE-2.7,MANAGE-1.3,MAP-3.2]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-02.2-001
  subdomain: D-02.2
  regulations: [CRA,NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.PS-02]
  privacy_subcategories: [UNMAPPED_PF]
  unmapped_pf_justification: "no PF 1.0 analogue for this rule's privacy dimension (element-level gap, per SPEC §4.6)"
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-02.3-001
  subdomain: D-02.3
  regulations: [CRA,NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [ID.RA-08]
  privacy_subcategories: [ID.IM-P7,GV.PO-P5]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-02.4-001
  subdomain: D-02.4
  regulations: [NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [ID.IM-02,ID.RA-03]
  privacy_subcategories: [ID.RA-P3,ID.RA-P4,ID.RA-P5]
  airmf_subcategories: [MEASURE-2.7,MEASURE-2.11]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-03.1-001
  subdomain: D-03.1
  regulations: [CRA,NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.AA-01,PR.AA-03,PR.AA-05]
  privacy_subcategories: [CT.PO-P1]
  airmf_subcategories: [MAP-3.5,GOVERN-2.1,GOVERN-3.1]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-03.2-001
  subdomain: D-03.2
  regulations: [CRA,NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.AA-03]
  privacy_subcategories: [UNMAPPED_PF]
  unmapped_pf_justification: "no PF 1.0 analogue for this rule's privacy dimension (element-level gap, per SPEC §4.6)"
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-03.3-001
  subdomain: D-03.3
  regulations: [GDPR,NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.AA-05,PR.AA-01]
  privacy_subcategories: [CT.PO-P1]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-03.4-001
  subdomain: D-03.4
  regulations: [CRA]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.PS-01]
  privacy_subcategories: [CT.DP-P4,CT.PO-P4]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-04.1-001
  subdomain: D-04.1
  regulations: [CRA,NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [DE.AE-02,DE.CM-01,DE.CM-09]
  privacy_subcategories: [CM.AW-P7]
  airmf_subcategories: [MEASURE-2.4,MEASURE-3.1,MANAGE-2.3,MANAGE-4.1]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-04.2-001
  subdomain: D-04.2
  regulations: [GDPR,CRA,NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [RS.MI-01,RS.MI-02]
  privacy_subcategories: [PR.PO-P7,CT.DM-P10]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-04.3-001
  subdomain: D-04.3
  regulations: [GDPR,CRA,NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [RS.CO-02,RS.CO-03]
  privacy_subcategories: [CM.AW-P7,CM.PO-P2,CM.PO-P1,GV.PO-P5]
  airmf_subcategories: [MANAGE-2.3,MANAGE-4.3,GOVERN-1.1]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-04.4-001
  subdomain: D-04.4
  regulations: [GDPR,NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [RC.RP-01,RC.RP-03,RC.RP-05]
  privacy_subcategories: [UNMAPPED_PF]
  unmapped_pf_justification: "no PF 1.0 analogue for this rule's privacy dimension (element-level gap, per SPEC §4.6)"
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-05.1-001
  subdomain: D-05.1
  regulations: [GDPR,CRA,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.DS-10,ID.AM-03]
  privacy_subcategories: [CT.PO-P4,CT.DP-P4,ID.RA-P3]
  airmf_subcategories: [GOVERN-1.4,MAP-2.1,MEASURE-2.11,MAP-2.2]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-05.2-001
  subdomain: D-05.2
  regulations: [GDPR,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.DS-01,PR.PS-06]
  privacy_subcategories: [CT.PO-P4,CT.DM-P5]
  airmf_subcategories: [MEASURE-2.4,MEASURE-4.2,GOVERN-1.4]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-05.3-001
  subdomain: D-05.3
  regulations: [GDPR,CRA]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.DS-10]
  privacy_subcategories: [CT.DM-P4,CT.DM-P5]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-05.4-001
  subdomain: D-05.4
  regulations: [GDPR]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [UNMAPPED_CSF]
  privacy_subcategories: [CT.DM-P1,CT.DM-P6]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: CSF 2.0 has no direct subcategory for this control; no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-06.1-001
  subdomain: D-06.1
  regulations: [GDPR,NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [GV.SC-04,GV.SC-07,ID.RA-10]
  privacy_subcategories: [ID.IM-P2]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-06.2-001
  subdomain: D-06.2
  regulations: [CRA]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [GV.SC-09]
  privacy_subcategories: [ID.IM-P7]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-06.3-001
  subdomain: D-06.3
  regulations: [GDPR,NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [GV.SC-05,GV.SC-06]
  privacy_subcategories: [GV.PO-P5]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-06.4-001
  subdomain: D-06.4
  regulations: [NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [DE.CM-06,PR.IR-01]
  privacy_subcategories: [UNMAPPED_PF]
  unmapped_pf_justification: "no PF 1.0 analogue for this rule's privacy dimension (element-level gap, per SPEC §4.6)"
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-07.1-001
  subdomain: D-07.1
  regulations: [GDPR,CRA,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.PS-06,ID.RA-01]
  privacy_subcategories: [GV.PO-P2,CT.PO-P4,CT.DP-P2,CT.DP-P5]
  airmf_subcategories: [MEASURE-2.7]
  mapping_rationale: MEASURE-2.7 (canonical AI RMF, frozen list) — AI-system security and resilience evaluation; rule has AI_Act in its regulation set (product-design security for an AI system) though no AI-C* literal in Doc 11 source; adjudicated in port Fase 3; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-07.2-001
  subdomain: D-07.2
  regulations: [CRA,NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.PS-06]
  privacy_subcategories: [UNMAPPED_PF]
  unmapped_pf_justification: "no PF 1.0 analogue for this rule's privacy dimension (element-level gap, per SPEC §4.6)"
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-07.3-001
  subdomain: D-07.3
  regulations: [NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.PS-06,PR.PS-02]
  privacy_subcategories: [PR.PO-P4]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: PR.PO-P4 (canonical PF 1.0, frozen list) — governance policy for the CI/CD security rule; no AI-C* in source clauses; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-07.4-001
  subdomain: D-07.4
  regulations: [NIS2]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [ID.RA-07]
  privacy_subcategories: [ID.RA-P3]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: ID.RA-07 — Changes and exceptions are managed, assessed for risk impact, recorded, and tracked (frozen CSF 2.0 ID); frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-08.1-001
  subdomain: D-08.1
  regulations: [GDPR,NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.AT-01]
  privacy_subcategories: [GV.AT-P1,GV.AT-P2]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-08.2-001
  subdomain: D-08.2
  regulations: [GDPR,NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.AT-02]
  privacy_subcategories: [GV.AT-P1,GV.AT-P2]
  airmf_subcategories: [MAP-3.5,GOVERN-2.1,GOVERN-2.2,GOVERN-3.1]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-08.3-001
  subdomain: D-08.3
  regulations: [NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [GV.RR-01,PR.AT-02]
  privacy_subcategories: [UNMAPPED_PF]
  unmapped_pf_justification: "no PF 1.0 analogue for this rule's privacy dimension (element-level gap, per SPEC §4.6)"
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-09.1-001
  subdomain: D-09.1
  regulations: [GDPR,CRA,NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [GV.PO-01,GV.PO-02]
  privacy_subcategories: [GV.PO-P1,GV.PO-P5,CM.PO-P1]
  airmf_subcategories: [GOVERN-1.1,GOVERN-1.3,GOVERN-1.4,GOVERN-1.6,MAP-1.1,MEASURE-2.8,MEASURE-2.9,MAP-3.4]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-09.2-001
  subdomain: D-09.2
  regulations: [GDPR,CRA,NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [ID.RA-04,ID.RA-05,GV.RM-06]
  privacy_subcategories: [ID.RA-P3,ID.RA-P4,ID.RA-P5]
  airmf_subcategories: [GOVERN-1.1,GOVERN-1.3,GOVERN-1.5,MAP-5.1,MAP-3.1,MAP-3.2,MANAGE-1.2]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-09.3-001
  subdomain: D-09.3
  regulations: [NIS2]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [ID.AM-01,ID.AM-02,ID.AM-07]
  privacy_subcategories: [ID.IM-P1,ID.IM-P4,ID.IM-P6,ID.IM-P8]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-09.4-001
  subdomain: D-09.4
  regulations: [GDPR,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [ID.AM-07,GV.OC-03]
  privacy_subcategories: [ID.IM-P1,ID.IM-P4,ID.IM-P6,ID.IM-P8,CM.PO-P1]
  airmf_subcategories: [MEASURE-2.4,MEASURE-3.1,GOVERN-1.6,GOVERN-2.1,MEASURE-4.2]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-10.1-001
  subdomain: D-10.1
  regulations: [CRA,NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [DE.CM-01,DE.CM-09,DE.AE-02]
  privacy_subcategories: [CM.AW-P7]
  airmf_subcategories: [MANAGE-4.1,MEASURE-3.1,MEASURE-4.1,GOVERN-1.5,MEASURE-2.4]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-10.2-001
  subdomain: D-10.2
  regulations: [CRA,NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [PR.PS-04,DE.AE-03,RS.AN-06]
  privacy_subcategories: [CT.DM-P9]
  airmf_subcategories: [MEASURE-2.4,MEASURE-3.1,GOVERN-1.6,MEASURE-4.2,GOVERN-1.4,GOVERN-2.1]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: CR-D-10.3-001
  subdomain: D-10.3
  regulations: [GDPR,CRA,NIS2,AI_Act]
  normative_intensity: 3.0
  priority_label: MUST
  csf_subcategories: [ID.IM-01,ID.IM-02,ID.IM-03]
  privacy_subcategories: [UNMAPPED_PF]
  unmapped_pf_justification: "no PF 1.0 analogue for this rule's privacy dimension (element-level gap, per SPEC §4.6)"
  airmf_subcategories: [MEASURE-2.7,MEASURE-2.11,MANAGE-1.2,MEASURE-3.1]
  mapping_rationale: natural multi-framework anchor; AI-C* present — AI RMF anchor via SR-AIACT-XXX; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```


### §3.2 — Best Practice Rules (17 BPR-D-*)

```yaml
- rule_id: BPR-D-01.1-001
  subdomain: D-01.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [PR.DS-01,PR.DS-10]
  privacy_subcategories: [PR.DS-P1,CT.DP-P2]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-01.2-001
  subdomain: D-01.3
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [PR.DS-01]
  privacy_subcategories: [PR.DS-P1,CT.DP-P2]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-02.1-001
  subdomain: D-02.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [ID.RA-01,DE.CM-01]
  privacy_subcategories: [ID.RA-P3,ID.RA-P5]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-02.5-001
  subdomain: D-02.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [ID.RA-01,DE.CM-01]
  privacy_subcategories: [ID.RA-P3,ID.RA-P5]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-03.1-001
  subdomain: D-03.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [PR.AA-01,PR.AA-05]
  privacy_subcategories: [CT.PO-P1]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-03.5-001
  subdomain: D-03.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [PR.AA-01,PR.AA-05]
  privacy_subcategories: [CT.PO-P1]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-04.1-001
  subdomain: D-04.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [DE.AE-02,DE.CM-01]
  privacy_subcategories: [CM.AW-P7]
  airmf_subcategories: [MANAGE-2.3,MANAGE-4.3]
  mapping_rationale: natural multi-framework anchor; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-04.5-001
  subdomain: D-04.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [DE.AE-02,DE.CM-01]
  privacy_subcategories: [CM.AW-P7]
  airmf_subcategories: [MANAGE-2.3,MANAGE-4.3]
  mapping_rationale: natural multi-framework anchor; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-05.5-001
  subdomain: D-05.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [PR.DS-10,ID.AM-03]
  privacy_subcategories: [CT.PO-P4,CT.DP-P4]
  airmf_subcategories: [MAP-2.1,MAP-2.2,MEASURE-2.11]
  mapping_rationale: natural multi-framework anchor; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-06.5-001
  subdomain: D-06.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [GV.SC-04,GV.SC-07]
  privacy_subcategories: [ID.IM-P2]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-07.1-001
  subdomain: D-07.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [PR.PS-06]
  privacy_subcategories: [GV.PO-P2,CT.PO-P4]
  airmf_subcategories: [GOVERN-4.1,GOVERN-4.3,MEASURE-2.7]
  mapping_rationale: natural multi-framework anchor; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-07.5-001
  subdomain: D-07.3
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [PR.PS-06,PR.PS-02]
  privacy_subcategories: [PR.PO-P4]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: PR.PO-P4 (canonical PF 1.0, frozen list) — governance policy for the CI/CD security rule; no AI-C* in source clauses; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-08.4-001
  subdomain: D-08.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [PR.AT-01]
  privacy_subcategories: [GV.AT-P1,GV.AT-P2]
  airmf_subcategories: [N/A (non-AI scope)]
  mapping_rationale: no AI-C* in source clauses — no AI_Act duty; AI RMF anchor not applicable; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-09.1-001
  subdomain: D-09.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [GV.PO-01,GV.PO-02]
  privacy_subcategories: [GV.PO-P1,GV.PO-P5]
  airmf_subcategories: [GOVERN-1.1,GOVERN-1.4,GOVERN-1.5]
  mapping_rationale: natural multi-framework anchor; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-09.5-001
  subdomain: D-09.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [GV.PO-01,GV.PO-02]
  privacy_subcategories: [GV.PO-P1,GV.PO-P5]
  airmf_subcategories: [GOVERN-1.1,GOVERN-1.4,GOVERN-1.5]
  mapping_rationale: natural multi-framework anchor; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-10.1-001
  subdomain: D-10.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [DE.CM-01,DE.CM-09]
  privacy_subcategories: [CM.AW-P7]
  airmf_subcategories: [MANAGE-4.1,MEASURE-3.1,MEASURE-2.4]
  mapping_rationale: natural multi-framework anchor; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```

```yaml
- rule_id: BPR-D-10.4-001
  subdomain: D-10.1
  regulations: [—]
  normative_intensity: 2.0
  priority_label: SHOULD
  csf_subcategories: [DE.CM-01,DE.CM-09]
  privacy_subcategories: [CM.AW-P7]
  airmf_subcategories: [MANAGE-4.1,MEASURE-3.1,MEASURE-2.4]
  mapping_rationale: natural multi-framework anchor; frameworks are mapping targets, never derivation sources (AEGIS invariant)
```


---

## §4 — Implementation Posture (adopted 2026-08-28, port Fase 4; supersedes the legacy triple-maturity model)

> Previously mirrored the Case_01 SPEC §7 double-maturity model extended to 3 frameworks. Superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0 — see §4.1. **Three independent scores** (csf / privacy / airmf) — no aggregation; D11 desynchrony preserved.

### §4.1 — Implementation Posture scale (ADOPTED, port Fase 4, 2026-08-28)

> **SUPERSEDED.** The legacy triple-maturity model (CSF Implementation Tiers
> T1–T4 at program/Function level; 0–4 per-subcategory scales on the CSF,
> Privacy FW and AI RMF axes) is superseded by
> `00_METHODOLOGY/IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md` v2.0:
>
> - States: **IMPLEMENTED** (evidence pointer mandatory) / **PARTIAL** /
>   **NOT IMPLEMENTED** ("what's missing" note mandatory), plus special
>   categories `N/A — product-security deliverable (SSDF <ID>)` and
>   `N/A — statutory obligation`.
> - Numerical maturity scores, 0–4 scales and Tier designations are
>   PROHIBITED at control and Function level (Model §9).
> - The §5.1 per-control table and the §4.5/§5.2 Function views use the
>   deterministic legacy backfill (Model §4); the historical scale
>   definitions remain in git history only.

### §4.5 — Function-level qualitative implementation context (15 rows: 6 CSF + 5 Privacy + 4 AI RMF)

> Qualitative Implementation Context per Posture Model §5: operational strengths,
> active remediation for PARTIAL controls, roadmap priorities. Derived from the legacy
> cur/tier numbers via the deterministic backfill (Model §4); legacy values quoted for
> traceability.

> Legacy note (pre-port): cur_tier derived from Doc 11 column 13 aggregated per Function; now backfilled — `tgt_tier` from Track B tier (`Doc12_Proportionality_Profile.md` §3) and posture assessment (`Doc05_Security_Posture.md` §3).

| # | Framework | Function | Implementation Context (qualitative) |
|---|-----------|----------|------------------------------------------|
| 1 | CSF 2.0 | **GV** Govern | **PARTIAL — active gap to target** (legacy scale 3→4): documented policy architecture provides the foundation; target 4 with continuous-improvement artefacts (Doc 04 §9; Doc 04b §D-09) |
| 2 | CSF 2.0 | **ID** Identify | **PARTIAL — active gap to target** (legacy scale 3→4): CMDB 100% coverage (D-09.3); risk register unified (D-09.2); target 4 with continuous asset discovery |
| 3 | CSF 2.0 | **PR** Protect | **PARTIAL — active gap to target** (legacy scale 3→4): confidentiality mechanisms with segregated material management (D-01.x), access boundaries (D-03.x), AI RMF MAP-3.5; target 4 with full PAM automation (Doc 04b §D-03 gap) |
| 4 | CSF 2.0 | **DE** Detect | **PARTIAL — active gap to target** (legacy scale 3→4): continuous monitoring mechanisms and anomaly detection (D-04.1, D-10.1); target 4 with AI post-market monitoring complete (Doc 04b §D-10.1 gap) |
| 5 | CSF 2.0 | **RS** Respond | **PARTIAL — active gap to target** (legacy scale 3→4): Max-SLA 24h routing (T-001, D-04.3 RIGOROUS); target 4 with automation and external audit (Doc 04b §D-04) |
| 6 | CSF 2.0 | **RC** Recover | **PARTIAL — active gap to target** (legacy scale 3→4): recovery mechanisms with documented RTO/RPO and tamper-evident backup retention (D-04.4, D-10.2); target 4 with hash-chained WORM |
| 7 | Privacy FW | **ID-P** Identify | **PARTIAL — active gap to target** (legacy scale 3→4): RoPA complete, DPIA unified with FRIA (D-09.2 RIGOROUS); target 4 with automated data discovery |
| 8 | Privacy FW | **GV-P** Govern | **PARTIAL — active gap to target** (legacy scale 3→4): ISMS with GDPR Annex + DPO designation; target 4 with privacy-by-design automatizado (D-07.1 RIGOROUS) |
| 9 | Privacy FW | **CT-P** Control | **PARTIAL — active gap to target** (legacy scale 3→4): Cryptographic sharding (D-05.3, T-002 RESOLVED); biometric ephemeral deletion (D-05.1); target 4 |
| 10 | Privacy FW | **CM-P** Communicate | **Target profile met** (legacy scale 3→3): Privacy notice + DSAR + breach notification; target 3 (CM-P fully met by 04b §D-09; higher tier not required for HIGH) |
| 11 | Privacy FW | **PR-P** Protect | **PARTIAL — active gap to target** (legacy scale 3→4): confidentiality mechanisms with segregated material management + access boundaries; target 4 with PAM automation (Doc 04b §D-03.3 gap) |
| 12 | AI RMF | **GOVERN** | **PARTIAL — active gap to target** (legacy scale 3→4): documented policy architecture + AI_Act Annex + AI Governance Lead; target 4 with continuous AI risk review |
| 13 | AI RMF | **MAP** | **PARTIAL — active gap to target** (legacy scale 3→4): Unified DPIA + FRIA (D-09.2); AI use cases mapped; target 4 with MAP-5.1/5.2 fully documented (currently MAP-5.2 unused per AI RMF frozen list §"Unused") |
| 14 | AI RMF | **MEASURE** | **PARTIAL — active gap to target** (legacy scale 2→4): AI_Act conformity assessment IN PROGRESS (Doc 04 §9); post-market monitoring partial (Doc 04b §D-10.1 gap); target 4 by Q4 2026 |
| 15 | AI RMF | **MANAGE** | **PARTIAL — active gap to target** (legacy scale 3→4): Incident response playbooks (BPR-AI-07 / D-04.2); target 4 with automated prioritization |

**Tally (4.5):** 6 CSF Functions at 3/4 → 4/4 (avg gap 1); 5 Privacy FW Functions at 3/3.8 → 4/4 (avg gap ~0.6); 4 AI RMF Functions at 2.75/4 → 4/4 (avg gap 1.25). **Top gap: AI RMF MEASURE** — explicit post-market monitoring implementation roadmap tracked in Phase 2 (Doc 04b §4).

### §4.6 — Status distribution (replaces the legacy numerical heatmap)

> The legacy heatmap formula (numerical cur/tgt gaps per axis, GREEN..RED bands)
> is retired with the maturity model — numerical maturity heatmaps are prohibited
> (Posture Model §9). The §5.1 per-control statuses distribute as follows
> (156 axis-cells over 52 in-scope controls): **IMPLEMENTED 54 · PARTIAL 67 ·
> N/A (non-AI scope / no privacy axis) 35 · NOT IMPLEMENTED 0**. Non-uniformity
> is intentional and gate-checked.
## §5 — Aplicação ao Case_02 (per-control + per-Function)

### §5.1 — Per-control table (52 cards: 38 CR + 17 BPR, excl. 3 OUT-OF-SCOPE per Track B)

> 52 rows × `[rule_id, sub_domain, cur_csf, tgt_csf, cur_priv, tgt_priv, cur_airmf, tgt_airmf, gap_csf, gap_priv, gap_airmf, gap_min, gap_worst]`.
> Legacy note (pre-port): cur_csf was Doc 11 column 13 (Maturity Score); §5.1 statuses below are the deterministic backfill — `tgt_csf` = Track B target per `Doc12_Proportionality_Profile.md` §3 (RIGOROUS → 4, STANDARD → 3, EXCLUDED → N/A).
> `cur/tgt_priv` and `cur/tgt_airmf` = Track B tier default: RIGOROUS → 3-4, STANDARD → 3, EXCLUDED → N/A. CR without AI-C* → airmf N/A; same for PF (none in Case_02).
> `gap_min` = MIN of applicable gaps per §4.6 N/A-exclusion rule (coverage indicator; preserved for backwards compatibility).
> `gap_worst` = MAX of applicable gaps per §4.6 N/A-exclusion rule (worst-axis heatmap value used by V4).
> **OUT-OF-SCOPE per Track B:** D-07.4, D-08.3, D-09.3 (excluded from `Doc12_Proportionality_Profile.md` §4 + §11.4 F-01/F-05); not in this per-control table.

| rule_id | sub_domain | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) |
|---------|-----------|------|---------|---------|
|---------|-----------|--------:|--------:|---------:|---------:|----------:|----------:|--------:|---------:|----------:|--------:|----------:|

| CR-D-01.1-001 | D-01.1 | PARTIAL | PARTIAL | PARTIAL |
| CR-D-01.2-001 | D-01.2 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-01.3-001 | D-01.3 | PARTIAL | PARTIAL | PARTIAL |
| CR-D-01.4-001 | D-01.4 | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED |
| CR-D-02.1-001 | D-02.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED |
| CR-D-02.2-001 | D-02.2 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-02.3-001 | D-02.3 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-02.4-001 | D-02.4 | PARTIAL | IMPLEMENTED | IMPLEMENTED |
| CR-D-03.1-001 | D-03.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED |
| CR-D-03.2-001 | D-03.2 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-03.3-001 | D-03.3 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-03.4-001 | D-03.4 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-04.1-001 | D-04.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED |
| CR-D-04.2-001 | D-04.2 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-04.3-001 | D-04.3 | PARTIAL | PARTIAL | PARTIAL |
| CR-D-04.4-001 | D-04.4 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-05.1-001 | D-05.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED |
| CR-D-05.2-001 | D-05.2 | PARTIAL | IMPLEMENTED | IMPLEMENTED |
| CR-D-05.3-001 | D-05.3 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-05.4-001 | D-05.4 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-06.1-001 | D-06.1 | PARTIAL | PARTIAL | N/A |
| CR-D-06.2-001 | D-06.2 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-06.3-001 | D-06.3 | PARTIAL | PARTIAL | N/A |
| CR-D-06.4-001 | D-06.4 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-07.1-001 | D-07.1 | PARTIAL | PARTIAL | N/A |
| CR-D-07.2-001 | D-07.2 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-07.3-001 | D-07.3 | PARTIAL | PARTIAL | N/A |
| CR-D-08.1-001 | D-08.1 | PARTIAL | IMPLEMENTED | N/A |
| CR-D-08.2-001 | D-08.2 | PARTIAL | IMPLEMENTED | IMPLEMENTED |
| CR-D-09.1-001 | D-09.1 | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED |
| CR-D-09.2-001 | D-09.2 | PARTIAL | IMPLEMENTED | IMPLEMENTED |
| CR-D-09.4-001 | D-09.4 | PARTIAL | IMPLEMENTED | IMPLEMENTED |
| CR-D-10.1-001 | D-10.1 | PARTIAL | PARTIAL | PARTIAL |
| CR-D-10.2-001 | D-10.2 | PARTIAL | IMPLEMENTED | IMPLEMENTED |
| CR-D-10.3-001 | D-10.3 | PARTIAL | IMPLEMENTED | IMPLEMENTED |
| BPR-D-01.1-001 | D-01.1 | PARTIAL | PARTIAL | N/A |
| BPR-D-01.2-001 | D-01.3 | PARTIAL | PARTIAL | N/A |
| BPR-D-02.1-001 | D-02.1 | PARTIAL | IMPLEMENTED | N/A |
| BPR-D-02.5-001 | D-02.1 | PARTIAL | IMPLEMENTED | N/A |
| BPR-D-03.1-001 | D-03.1 | PARTIAL | IMPLEMENTED | N/A |
| BPR-D-03.5-001 | D-03.1 | PARTIAL | IMPLEMENTED | N/A |
| BPR-D-04.1-001 | D-04.1 | PARTIAL | IMPLEMENTED | N/A |
| BPR-D-04.5-001 | D-04.1 | PARTIAL | IMPLEMENTED | N/A |
| BPR-D-05.5-001 | D-05.1 | PARTIAL | IMPLEMENTED | N/A |
| BPR-D-06.5-001 | D-06.1 | PARTIAL | PARTIAL | N/A |
| BPR-D-07.1-001 | D-07.1 | PARTIAL | PARTIAL | N/A |
| BPR-D-07.5-001 | D-07.3 | PARTIAL | PARTIAL | N/A |
| BPR-D-08.4-001 | D-08.1 | PARTIAL | IMPLEMENTED | N/A |
| BPR-D-09.1-001 | D-09.1 | IMPLEMENTED | IMPLEMENTED | N/A |
| BPR-D-09.5-001 | D-09.1 | IMPLEMENTED | IMPLEMENTED | N/A |
| BPR-D-10.1-001 | D-10.1 | PARTIAL | PARTIAL | N/A |
| BPR-D-10.4-001 | D-10.1 | PARTIAL | PARTIAL | N/A |

**Per-control summary stats:** 52 cards in scope (38 CR + 17 BPR = 55 minus 3 OUT-OF-SCOPE per Track B: D-07.4, D-08.3, D-09.3). FN-02 (updated, port Fase 3) — CR-D-07.1-001 airmf anchored to MEASURE-2.7 (previously N/A; no AI-C* in Doc 11 source). FN-03 — `gap_worst` distribution: 0 (D-01.4, D-09.1 + BPR-D-09.1 + BPR-D-09.5), 1 (most — gap_worst = 1 means at least one applicable axis has gap 1), 2 (D-04.3, D-05.3, D-07.1, D-07.3, D-10.1, BPR-D-07.1, BPR-D-07.5, BPR-D-10.1, BPR-D-10.4 — RIGOROUS tiers with explicit cur deficits from `04b §4` top-gaps list).

> **Note — AI-specific BPR subset (8 cards):** The 8 AI-specific BPR rows in `Doc18_Rules_Catalog.md` §5.2 (`BPR-D-07.1-002`, `BPR-D-10.5-001`, `BPR-D-02.4-001`, `BPR-D-02.4-002`, `BPR-D-03.1-002`, `BPR-D-10.2-001`, `BPR-D-04.2-001`, `BPR-D-05.1-001`) are intentionally excluded from the per-control table above because they sit outside the 38 CR + 17 BPR = 55 card count. Their CSF/PF/AI RMF mappings and maturity values are documented in `Doc18_Rules_Catalog.md` §5.2 (see Doc 11 for the authoritative mappings per NIST remediation B1, 2026-08).

### §5.2 — Per-Function aggregated implementation context (15 rows)

> Legacy aggregation note (pre-port): MAX(cur across cards) anchored each Function's cur; the qualitative contexts below quote the legacy scale for traceability. tgt = MAX(tgt across cards in that Function). gap = tgt - cur. This is the "worst-case per Function" aggregation.

| # | Framework | Function | Aggregated from cards | Implementation Context (qualitative) |
|---|-----------|----------|-----------------------|------------------------------------------|
|---|-----------|----------|---------:|---------:|----:|-----------------------|---------------|
| 1 | CSF 2.0 | GV | D-09.1, D-09.2, D-09.3, D-09.4 | **PARTIAL — active gap to target** (legacy scale 3→4): ISO 27001 ISMS at 4/4 already for D-09.1; D-09.2 cur 3 (DPIA+FRIA unified, not yet 4) |
| 2 | CSF 2.0 | ID | D-02.1, D-02.2, D-02.3, D-02.4 | **PARTIAL — active gap to target** (legacy scale 3→4): D-02.4 cur 2 (pen testing cadence); D-09.3 OUT-OF-SCOPE per Track B |
| 3 | CSF 2.0 | PR | D-01.x, D-03.x, D-05.x, D-07.x | **PARTIAL — active gap to target** (legacy scale 3→4): D-03.3 cur 3 (PAM pending) caps PR; D-07.1/D-07.3 cur 2 (RIGOROUS partial) |
| 4 | CSF 2.0 | DE | D-04.1, D-04.2, D-04.3, D-04.4 | **PARTIAL — active gap to target** (legacy scale 3→4): D-04.3 cur 2 (RIGOROUS, multi-reg notification in progress) |
| 5 | CSF 2.0 | RS | D-04.x | **PARTIAL — active gap to target** (legacy scale 3→4): Same as DE above; D-04.3 cur 2 anchors RS |
| 6 | CSF 2.0 | RC | D-04.4, D-10.2 | **PARTIAL — active gap to target** (legacy scale 3→4): D-10.2 cur 4 (hash-chained WORM); D-04.4 cur 3 |
| 7 | Privacy FW | ID-P | D-09.2, D-09.4 | **PARTIAL — active gap to target** (legacy scale 3→4): D-09.2 cur 3 (DPIA+FRIA in progress; not yet 4) |
| 8 | Privacy FW | GV-P | D-09.1, D-09.2, D-09.4 | **PARTIAL — active gap to target** (legacy scale 3→4): D-09.1 cur 4 (ISO 27001 + GDPR Annex); gap from D-09.2 |
| 9 | Privacy FW | CT-P | D-05.1, D-05.2, D-05.3, D-05.4 | **PARTIAL — active gap to target** (legacy scale 3→4): D-05.3 cur 2 (T-002 cryptographic sharding in deployment) |
| 10 | Privacy FW | CM-P | D-09.1, D-09.4 | **Target profile met** (legacy scale 3→3): Privacy notice + DSAR + breach notification; no gap (HIGH-tier ceiling at 3) |
| 11 | Privacy FW | PR-P | D-01.x, D-03.x, D-05.x | **PARTIAL — active gap to target** (legacy scale 3→4): D-03.3 cur 3 (PAM) caps PR-P |
| 12 | AI RMF | GOVERN | D-09.1, D-09.2, D-08.2, D-03.1, D-04.3 | **PARTIAL — active gap to target** (legacy scale 3→4): D-04.3 cur 2 anchors GOVERN (max-SLA routing AI_Act) |
| 13 | AI RMF | MAP | D-09.1, D-09.2, D-05.1, D-05.2 | **PARTIAL — active gap to target** (legacy scale 3→4): D-09.2 cur 3 (DPIA+FRIA, MAP-5 partial) |
| 14 | AI RMF | MEASURE | D-10.1, D-10.2, D-10.3, D-02.1, D-02.4, D-04.1, D-09.2, D-05.1, D-05.2 | **PARTIAL — active gap to target** (legacy scale 2→4): **Largest gap.** D-10.1 cur 2 (post-market monitoring INCOMPLETE per Doc 04b §4 #2) |
| 15 | AI RMF | MANAGE | D-04.2, D-04.3, D-09.2, D-10.1 | **PARTIAL — active gap to target** (legacy scale 3→4): D-04.3 cur 2 anchors MANAGE |

**Per-Function summary:** all 15 Functions have tgt 4 (4/4) except CM-P (tgt 3, ceiling for HIGH complexity). Average gap: 0.93. Largest gap: AI RMF MEASURE (2 — D-10.1 post-market monitoring + D-02.4 adversarial testing + D-04.1 AI incident detection).

---

## §6 — Gap Analysis

> Three axes: (a) framework subcategories not covered by any Case_02 CR/BPR; (b) sub-domains with low target maturity; (c) tension cross-reference.

### §6.1 — CSF 2.0 subcategories not covered by any Case_02 CR/BPR

> From the 106 subcategories in the frozen list, the mapping in §1 + §3 covers the CSF subcategories that appear in `Framework_Crosswalk_ARM.md` for the 35 active sub-domains. Subcategories not appearing in any crosswalk row are listed below.

| CSF subcategory | Status | Justification |
|-----------------|--------|---------------|
| `ID.IM-03` (Improvements from evaluations implemented) | gap-acceptable | Covered implicitly by D-10.3 compliance testing; no specific sub-domain row in Case_02 crosswalk |
| `GV.OC-02` (Stakeholder needs understood) | gap-acceptable | Stakeholder management lives in 09_Regulatory_Applicability + 04d_Org_Roles_RACI; CSF anchor used by D-09.1 |
| `GV.OC-04` (Critical objectives/services communicated) | gap-acceptable | Business-continuity context; anchored by D-04.4 + D-09.1 |
| `GV.OC-05` (Outcomes the org depends on) | gap-acceptable | Same as OC-04 |
| `GV.SC-08` (Supplier risk prioritized) | covered by D-06.1 (redundant with GV.SC-04/07) | — |
| `PR.PS-03` (Hardware maintained) | gap-acceptable | Hardware maintenance is operational; D-02.2 patch mgmt covers |
| `PR.PS-05` (Software installation techniques) | gap-acceptable | Operational; not security-control-relevant in Case_02 |
| `PR.IR-04` (Adequate resource capacity) | covered by D-04.4 (RC axis) | — |
| `DE.CM-01` (Malicious code detected) | gap-acceptable | EDR (EDR) is operational; not a CR anchor |
| `DE.CM-09` (Unauthorized mobile code detected) | gap-acceptable | Same as CM-04 |
| `DE.CM-06..08` (External/Personnel/Activity monitoring) | covered by D-10.1 | — |
| `ID.RA-06` (Newly identified vulnerabilities mitigated) | covered by D-02.2 | — |
| `RS.MA-02..05` (Investigation root cause, etc.) | gap-acceptable | Part of incident response process; not a separate CR anchor |
| `RC.CO-04..03` (Recovery communication) | covered by D-04.3 (RS.CO-02/03) | — |

**Verdict §6.1:** ~14 of 106 CSF subcategories are not anchored by a specific Case_02 CR. Most are operational/overlap (acceptable gap) or covered by adjacent CR via redundancy. **No critical gap.**

### §6.1.5 — Frozen-list integrity findings (FN-01)

> Earlier in this case's history, 11 CSF IDs (6 in §1/§3 core mappings + 5 descriptive IDs in §6.1 narrative) were converted to `UNMAPPED_CSF` based on an incorrect assumption that the frozen `NIST_CSF_2.0_subcategories.md` list defined only `GV.SC-01..-05` and `ID.RA-01..-06`. The corrected frozen list actually contains `GV.SC-01..-10` and `ID.RA-01..-10` (both families are complete). All §1/§3 core mappings have been restored to valid IDs; descriptive §6.1 narrative references to `GV.SC-06/-07/-09`, `ID.RA-07/-08/-10`, and `ID.RA-09` (originally gap-coverage markers) remain as-is for traceability but are no longer "absent" from the frozen list. Resolution of the frozen-list integrity check itself is deferred (DF1 — future dedicated contract).

| Frozen family | Family size in frozen list | Status |
|---------------|----------------------------|--------|
| `GV.SC` (supply chain) | `-01..-10` | All 10 IDs valid; §1/§3 mappings restored to valid IDs (CR-D-06.1-001 uses GV.SC-04/07/-10; CR-D-06.2-001 uses GV.SC-09; CR-D-06.3-001 uses GV.SC-05/-06; BPR-D-06.5-001 uses GV.SC-04/-07) |
| `ID.RA` (risk assessment) | `-01..-10` | All 10 IDs valid; §1/§3 mappings restored to valid IDs (CR-D-02.1-001 uses ID.RA-01/-08; CR-D-02.3-001 uses ID.RA-08; CR-D-06.1-001 uses ID.RA-10; CR-D-07.4-001 uses ID.RA-07) |

> §6 also references `DE.CM-01`, `DE.CM-09`, `ID.RA-06`, `RS.MA-02..05`, `RC.CO-04..03` — these appear in the §6.1 narrative as informational gap-acceptable coverage (not as active §1/§3 anchors), and remain unchanged here.

**Privacy FW normalisation.** §2 previously used legacy/non-canonical labels (`ID-P.*`, `GV-P.*`); these have been normalised to the frozen canonical forms (`ID.*-P*`, `GV.*-P*`). The v1.0 redirect `PR.PO-P4` (per frozen list §0) has been replaced with `UNMAPPED_PRIVACY` in §1 (CR-D-07.3-001), §3 (CR-D-07.3-001 + BPR-D-07.5-001), §8.1 (V1).

### §6.2 — Privacy FW 1.0 subcategories not covered

> The 68 SR in `02b_SecurityRules_NISTPF.md` cover 59/104 active PF subcategories (100% of GDPR-touched sub-domains). The 45 unused active PF subcategories (104-59) are:
> - Specialised de-identification (`UNMAPPED_PF (P9-class specialised de-identification has no PF 1.0 analogue)`) — no direct GDPR clause
> - Data provenance lineage (`CM.AW-P6`) — not required by GDPR
> - Business environment subcats (`ID.BE-P*`) — partially covered by `ID.IM-P*` (same intent)
> - Training/awareness variants beyond what the GDPR-SR file covers

**Verdict §6.2:** No critical gap. The 45 unused active PF subcategories are either specialised de-identification techniques or business-environment subcats without a direct GDPR clause. They could be addressed in a future contract that includes the Canadian/Nigerian data-protection frameworks.

### §6.3 — AI RMF 1.0 subcategories not covered

> 24 SR in `02b_SecurityRules_NISTAIRMF.md` cover 41/72 active AI RMF subcategories. **31/72 (43%) AI RMF subcategories are unused.** This is the **largest gap** in the matrix.

| AI RMF subcategory cluster | Count | Why unused |
|----------------------------|------:|------------|
| `GOVERN-1.7` (Decommissioning) | 1 | No AI_Act T5 counterpart |
| `GOVERN-2.3` (Executive leadership) | 1 | Internal practice, not AI_Act duty |
| `GOVERN-3.2` (Roles/responsibilities for human-AI configurations) | 1 | Covered by `GOVERN-2.1` for SecureBorder |
| `GOVERN-4.2` (Documented risks/impacts communication) | 1 | No AI_Act T5 counterpart |
| `GOVERN-5.2` (Mechanisms to incorporate feedback) | 1 | Internal AI RMF practice |
| `GOVERN-6.2` (Contingency processes for failures) | 1 | Partially via D-04.2 (incident containment) |
| `MAP-1.2..1.6` (Interdisciplinary actors, mission, business value, risk tolerance, system requirements) | 5 | No AI_Act T5 counterpart (organisational context, not AI_Act duty) |
| `MAP-2.3` (Scientific integrity + TEVV) | 1 | Internal TEVV practice |
| `MAP-4.1..4.2` (Tech/legislative landscape, internal risk controls) | 2 | No AI_Act T5 counterpart |
| `MAP-5.2` (Personnel for regulatory support) | 1 | Internal practice |
| `MEASURE-1.2` (Appropriateness of AI metrics) | 1 | Internal measurement practice |
| `MEASURE-1.3` (Independent internal experts) | 1 | Internal practice |
| `MEASURE-2.2` (Human subjects research evaluations) | 1 | No AI_Act T5 counterpart |
| `MEASURE-2.12` (Environmental impact) | 1 | Outside AI_Act cybersecurity scope |
| `MEASURE-2.13` (TEVV effectiveness) | 1 | Internal AI RMF practice |
| `MEASURE-3.2` (Difficult-to-detect risk tracking) | 1 | Internal practice |
| `MEASURE-3.3` (Feedback processes for end users) | 1 | No AI_Act T5 counterpart |
| `MEASURE-4.3` (Performance improvements from consultations) | 1 | Internal practice |
| `MANAGE-1.1` (Determination of AI risk level) | 1 | No AI_Act T5 counterpart |
| `MANAGE-1.4` (Residual risks to downstream acquirers) | 1 | Art. 26 partially; covered elsewhere |
| `MANAGE-2.1` (Resources for AI risk management) | 1 | Internal practice |
| `MANAGE-2.2` (Sustaining value of deployed AI) | 1 | Business outcome, not AI_Act duty |
| `MANAGE-2.4` (Mechanisms for AI risks) | 1 | Internal practice |
| `MANAGE-3.1..3.2` (Third-party/pre-trained model risk) | 2 | Partially via GOVERN-5/6 + SR-AIACT-023 |
| `MANAGE-4.2` (Decommissioning processes) | 1 | No AI_Act T5 counterpart |
| **Total unused** | **31** |

**Verdict §6.3:** 31 unused subcategories are **either** internal AI RMF practices (no AI_Act duty) **or** environmental / human subjects (outside T5 cybersecurity scope). For Case_02 — a HIGH-complexity border-control AI provider with all 4 regulations applicable — this is a **defensible gap**: the 31 unused subcategories would be relevant in a future contract extending AI_Act coverage to T6/T7 or to GPAI systemic-risk-specific obligations. **No flag in §6 of this contract; tracked for Case_03 / future contract.**

### §6.4 — Sub-domains at the STANDARD target profile (legacy tgt = 3)

> Per the §4.6 rule, every active sub-domain in Case_02 has tgt ≥ 3 (Track B floor: STANDARD → tgt 3, RIGOROUS → tgt 4). The 3 active sub-domains with `tgt = 3` (not 4) are tracked here for proportion justification. (D-07.4, D-08.3, D-09.3 are OUT-OF-SCOPE per Track B 07b §4 + §11.4 F-01/F-05 and are excluded from this list.)

| Sub-domain | tier | tgt | Justification (proportion) |
|-----------|------|----:|---------------------------|
| D-01.4 Data Integrity | STANDARD | 3 | NIS 2 + GDPR baseline; ISO 27001 A.5.14; high-level cryptographic hash-SHA256 sufficient for HIGH |
| D-02.3 Coordinated Vuln Disclosure | STANDARD | 3 | CRA Art. 14 + NIS 2 baseline; CVD policy + 24h ack SLA; tgt 4 not justified |
| D-05.4 Data Portability | STANDARD | 3 | GDPR Art. 20; JSON export endpoint; controller owns (not SecureBorder scope) |

**No active sub-domain falls below the STANDARD target profile** (legacy tgt 3; Track B floor enforced — posture equivalent: every active sub-domain has at least PARTIAL-with-defined-target controls). The 3 sub-domains at tgt 3 are justified by (a) Track B STANDARD tier, (b) post-floor rationale (target 4 requires continued investment beyond HIGH-tier proportionality), and (c) Doc 04b posture evidence.

> **FN-04 alignment note.** This section now reflects the 35 active sub-domains per Track B (`Doc12_Proportionality_Profile.md` §4 + §11.4 F-01/F-05). D-07.4, D-08.3, and D-09.3 are OUT-OF-SCOPE for Track B and are not counted in §5.1, §5.2 (except as excluded), or §8.4 (V4 heatmap). D-07.4 carries NI=2 SHOULD per Doc 11 §4.7; D-08.3 carries NIS 2 Art. 20 board-training; D-09.3 carries NIS 2 Art. 21 asset inventory — all deferred to a future contract if Track B scope expands.

### §6.5 — Tension cross-reference (T-001..T-004)

> Per `Doc15_Strategic_Tensions_Report.md` (Case_02: 8 tensions; this section cross-references the 4 most relevant for the Govern view §2.5 — T-001, T-002, T-003, T-004).

| Tension | Sub-Domain | Risk-framework convergence | Doc 13 anchor |
|---------|-----------|-----------------------------|---------------|
| T-001 (TEMPORAL_CONFLICT, CRITICAL, contextual) | D-04.3 | 4-reg notification timelines; max-SLA 24h routing | §2.5 risk view, §3 CR-D-04.3-001, §5.1 row, §5.2 row 4 (CSF DE) / row 5 (CSF RS) |
| T-002 (REQUIREMENT_CONFLICT, CRITICAL, contextual) | D-05.3 ↔ D-10.2 | GDPR erasure vs AI_Act log retention; cryptographic sharding | §2.5 risk view, §3 CR-D-05.3-001 + CR-D-10.2-001, §5.1 rows, §5.2 row 9 (PF CT-P) |
| T-003 (TRIGGER_MISMATCH, HIGH, structural) | D-09.2 | GDPR DPIA vs AI_Act FRIA; unified DPIA+FRIA single process | §2.5 risk view, §3 CR-D-09.2-001, §5.1 row, §5.2 row 1 (CSF GV) / row 7 (PF ID-P) / row 13 (AI RMF MAP) |
| T-004 (RESOURCE_CONFLICT, HIGH, structural) | D-09.1 | 4-reg documentation overlap; unified ISMS with 4 annexes | §2.5 risk view, §3 CR-D-09.1-001, §5.1 row, §5.2 row 1 (CSF GV) / row 8 (PF GV-P) / row 12 (AI RMF GOVERN) |

> **No resolution here** — resolutions live in `Doc15_Strategic_Tensions_Report.md` §4 and `Doc18_Rules_Catalog.md` §8. This section is a **pointer** for the framework mapping view.

### §6.6 — SO/FRIA + AI risk treatment convergence (additional)

> Beyond the 4 tensions, the framework mapping surfaces a methodological convergence worth noting: the 4 regulations' risk frameworks converge at `CR-D-09.2-001` (DPIA + FRIA + NIS 2 risk assessment + CRA risk-management process). The CSF axis anchors via `ID.RA-04/05`; the Privacy FW axis via `ID.RA-P3/4/5`; the AI RMF axis via `GOVERN-1.1/1.3/1.5` + `MAP-5.1`. The 24 SR-AIACT-XXX mappings plus the 68 SR-GDPR-XXX mappings converge here. **This is the methodological heart of Case_02's 4-reg compliance posture.**

---

## §7 — V3 Traceability Graph (Mermaid)

> `graph LR` covering 5 paths across the 4 regulations:
> (a) GDPR-only path; (b) CRA-only path; (c) NIS 2-only path; (d) AI_Act-only path; (e) Multi-regulation path.

```mermaid
graph LR
  %% (a) GDPR-only path — CR-D-05.4-001 (data portability)
  GDPR_Art20[GDPR Art. 20 Right to Portability] --> GDPR_C07[GDPR-C07]
  GDPR_C07 --> CR_05_4[CR-D-05.4-001 MUST NI=3]
  CR_05_4 --> SD_05_4[D-05.4 Data Portability]
  SD_05_4 --> PF_CT_DM_P1[PF CT.DM-P1 review access]
  SD_05_4 --> PF_CT_DM_P6[PF CT.DM-P6 standardized formats]
  SD_05_4 --> ISO_A5_14[ISO A.5.14 Information Transfer]
  SD_05_4 --> UNMAPPED_CSF[UNMAPPED_CSF — CSF has no portability subcategory]

  %% (b) CRA-origin path — CR-D-02.1-001 (vulnerability identification)
  CRA_AnnexI_2a[CRA Annex I §2(a) Vulnerability handling] --> CRA_C01[CRA-C01]
  CRA_C01 --> CR_02_1[CR-D-02.1-001 MUST NI=3]
  CR_02_1 --> SD_02_1[D-02.1 Vulnerability Identification]
  SD_02_1 --> CSF_ID_RA_01[CSF ID.RA-01]
  SD_02_1 --> CSF_ID_RA_08[CSF ID.RA-08]
  SD_02_1 --> SSDF_RV_1[SSDF RV.1]
  SD_02_1 --> ISO_A8_8[ISO A.8.8]

  %% (c) NIS 2-only path — CR-D-04.3-001 (notification — partial; primarily multi-reg; using as NIS 2 anchor)
  NIS2_Art23[NIS 2 Art. 23 Significant incident notification] --> NIS2_C25[NIS2-C25]
  NIS2_C25 --> CR_04_3[CR-D-04.3-001 MUST NI=3]
  CR_04_3 --> SD_04_3[D-04.3 Regulatory Notification]
  SD_04_3 --> CSF_RS_CO_02[CSF RS.CO-02]
  SD_04_3 --> PF_CM_AW_P7[PF CM.AW-P7 breach notification]
  SD_04_3 --> AI_MANAGE_4_3[AI RMF MANAGE-4.3 incident communication]
  SD_04_3 --> ISO_A5_24[ISO A.5.24]
  CR_04_3 -. T-001 resolution .-> T001[(T-001 max-SLA 24h routing)]

  %% (d) AI_Act-origin path — CR-D-05.1-001 (data governance, AI_Act anchor)
  AI_Art10[AI_Act Art. 10 Data governance] --> AI_C05[AI-C05]
  AI_C05 --> CR_05_1[CR-D-05.1-001 MUST NI=3]
  CR_05_1 --> SD_05_1[D-05.1 Data Minimisation]
  SD_05_1 --> CSF_PR_DS_10[CSF PR.DS-10]
  SD_05_1 --> PF_CT_PO_P4[PF CT.PO-P4 data lifecycle]
  SD_05_1 --> AI_GOVERN_1_4[AI RMF GOVERN-1.4 transparent policies]
  SD_05_1 --> AI_MAP_2_1[AI RMF MAP-2.1 task definition]
  SD_05_1 --> AI_MEASURE_2_11[AI RMF MEASURE-2.11 fairness/bias]

  %% (e) Multi-regulation path — CR-D-01.1-001 (4-reg, the only fully-4-reg CR with the most anchors)
  GDPR_C14_2[GDPR-C14] --> CR_01_1[CR-D-01.1-001 MUST NI=3]
  CRA_C07_2[CRA-C07] --> CR_01_1
  NIS2_C18_2[NIS2-C18] --> CR_01_1
  AI_C17_2[AI-C17] --> CR_01_1
  CR_01_1 --> SD_01_1[D-01.1 Data at Rest Encryption]
  SD_01_1 --> CSF_PR_DS_01[CSF PR.DS-01 data-at-rest]
  SD_01_1 --> PF_PR_DS_P1[PF PR.DS-P1]
  SD_01_1 --> PF_CT_DP_P2[PF CT.DP-P2 de-identification]
  SD_01_1 --> AI_MEASURE_2_7[AI RMF MEASURE-2.7 security/resilience]
  SD_01_1 --> AI_MEASURE_2_5[AI RMF MEASURE-2.5 valid/reliable]
  SD_01_1 --> ISO_A8_24[ISO A.8.24 cryptography]
  SD_01_1 --> SSDF_PO_5[SSDF PO.5 secure environments]
  CR_01_1 -. T-002 partial .-> T002[(T-002 cryptographic sharding context)]

  %% Multi-regulation governance convergence — D-09.2 (T-003 convergence)
  GDPR_C20[GDPR-C20] --> CR_09_2[CR-D-09.2-001 MUST NI=3]
  CRA_C23[CRA-C23] --> CR_09_2
  NIS2_C04[NIS2-C04] --> CR_09_2
  AI_C01[AI-C01] --> CR_09_2
  CR_09_2 --> SD_09_2[D-09.2 Impact & Risk Assessments]
  SD_09_2 --> CSF_ID_RA_04[CSF ID.RA-04]
  SD_09_2 --> CSF_ID_RA_05[CSF ID.RA-05]
  SD_09_2 --> PF_ID_RA_P3[PF ID.RA-P3]
  SD_09_2 --> PF_ID_RA_P5[PF ID.RA-P5]
  SD_09_2 --> AI_GOVERN_1_1[AI RMF GOVERN-1.1 legal reqs]
  SD_09_2 --> AI_MAP_5_1[AI RMF MAP-5.1 impacts]
  CR_09_2 -. T-003 resolution .-> T003[(T-003 unified DPIA+FRIA)]

  classDef crNode fill:#cce5ff,stroke:#003366,color:#000
  classDef sdNode fill:#d4edda,stroke:#155724,color:#000
  classDef csfNode fill:#fff3cd,stroke:#856404,color:#000
  classDef pfNode fill:#f8d7da,stroke:#721c24,color:#000
  classDef aiNode fill:#e2d5f1,stroke:#5b2c6f,color:#000
  classDef isoNode fill:#d6d8db,stroke:#1b4d3e,color:#000
  classDef tensionNode fill:#ffe5b4,stroke:#cc6600,color:#000
  classDef unmappedNode fill:#f5f5f5,stroke:#999,color:#000,stroke-dasharray: 5 5

  class CR_01_1,CR_02_1,CR_04_3,CR_05_1,CR_05_4,CR_09_2 crNode
  class SD_01_1,SD_02_1,SD_04_3,SD_05_1,SD_05_4,SD_09_2 sdNode
  class CSF_PR_DS_01,CSF_PR_DS_10,CSF_ID_RA_01,CSF_ID_RA_04,CSF_ID_RA_05,CSF_ID_RA_08,CSF_RS_CO_02 csfNode
  class PF_PR_DS_P1,PF_CT_DP_P2,PF_CT_PO_P4,PF_CT_DM_P1,PF_CT_DM_P6,PF_CM_AW_P7,PF_ID_RA_P3,PF_ID_RA_P5 pfNode
  class AI_MEASURE_2_5,AI_MEASURE_2_7,AI_MEASURE_2_11,AI_GOVERN_1_1,AI_GOVERN_1_4,AI_MAP_2_1,AI_MAP_5_1,AI_MANAGE_4_3 aiNode
  class ISO_A5_14,ISO_A5_24,ISO_A8_8,ISO_A8_24,SSDF_RV_1,SSDF_PO_5 isoNode
  class T001,T002,T003 tensionNode
  class UNMAPPED_CSF unmappedNode
```

**Reading the graph.** Each `CR-XXX` node is a `Compliance Rule` (must-implement, NI=3 unless noted). Each `SD-XXX` is an AEGIS sub-domain. Each framework node (CSF / PF / AI RMF / ISO / SSDF) is a single mapping target. The dotted edges to `T00X` show where a tension resolution is anchored. The `UNMAPPED_CSF` node shows where a CR has no natural CSF anchor (D-05.4 portability).

---

## §8 — Visualizations (Block F)

> **Block F rendering.** Four visualizations (V1-V4) below. V1/V2/V4 are markdown tables generated from §1, §3, §5; V3 is a Mermaid graph extending §7 with two additional sub-paths. **AI RMF is ACTIVE** for Case_02 (unlike Case_01 where it was a placeholder). The MIN-3-axis heatmap formula per §4.6 is applied: `gap_display = MIN(gap_csf, gap_priv, gap_airmf)` with N/A exclusion (N/A meaning the framework is not anchored for that control — excluded from MIN, not treated as gap 0).

### V1 — Matriz de Cobertura (CR/BPR × CSF + Privacy + AI RMF)

> 55-row table (38 CR + 17 BPR). Columns: `rule_id, type, NI, regulations, subdomain, csf_subcats, priv_subcats, airmf_subcats`. Source: §1 (CR) + §3 (BPR) + §5.1 (mat values). Semicolon-separated ID lists within cells. `UNMAPPED_*` tokens where the framework has no natural anchor.

| rule_id | type | NI | regulations | subdomain | csf_subcats | priv_subcats | airmf_subcats |
|---------|------|----|-------------|-----------|-------------|--------------|---------------|
| CR-D-01.1-001 | CR | 3.00 (MUST) | GDPR,CRA,NIS2,AI_Act | D-01.1 | PR.DS-01 | PR.DS-P1,CT.DP-P2 | GOVERN-1.6,MEASURE-2.7,MEASURE-2.5 |
| CR-D-01.2-001 | CR | 3.00 (MUST) | GDPR,CRA,NIS2 | D-01.2 | PR.DS-02 | PR.DS-P2 | N/A (non-AI scope) |
| CR-D-01.3-001 | CR | 3.00 (MUST) | CRA,NIS2,AI_Act | D-01.3 | PR.DS-01 | PR.DS-P1,CT.DP-P2 | MEASURE-2.7,GOVERN-1.6 |
| CR-D-01.4-001 | CR | 3.00 (MUST) | GDPR,CRA,AI_Act | D-01.4 | PR.DS-01,PR.DS-02 | PR.DS-P1,CT.DM-P1,CT.DM-P3 | MEASURE-2.6,MEASURE-2.7,MANAGE-2.3 |
| CR-D-02.1-001 | CR | 3.00 (MUST) | CRA,NIS2,AI_Act | D-02.1 | ID.RA-01, ID.RA-08 | ID.RA-P3,ID.RA-P5 | MEASURE-1.1,MEASURE-2.1,MEASURE-2.3,MAP-3.3,MEASURE-2.7,MANAGE-1.3,MAP-3.2 |
| CR-D-02.2-001 | CR | 3.00 (MUST) | CRA,NIS2 | D-02.2 | PR.PS-02 | UNMAPPED_PF (no PF 1.0 analogue for product patch/OTA update management) | N/A (non-AI scope) |
| CR-D-02.3-001 | CR | 3.00 (MUST) | CRA,NIS2 | D-02.3 | ID.RA-08 | ID.IM-P7,GV.PO-P5 | N/A (non-AI scope) |
| CR-D-02.4-001 | CR | 3.00 (MUST) | NIS2,AI_Act | D-02.4 | ID.IM-02,ID.RA-03 | ID.RA-P3,ID.RA-P4,ID.RA-P5 | MEASURE-2.7,MEASURE-2.11 |
| CR-D-03.1-001 | CR | 3.00 (MUST) | CRA,NIS2,AI_Act | D-03.1 | PR.AA-01,PR.AA-03,PR.AA-05 | CT.PO-P1 | MAP-3.5,GOVERN-2.1,GOVERN-3.1 |
| CR-D-03.2-001 | CR | 3.00 (MUST) | CRA,NIS2 | D-03.2 | PR.AA-03 | UNMAPPED_PF (no PF 1.0 MFA subcategory) | N/A (non-AI scope) |
| CR-D-03.3-001 | CR | 3.00 (MUST) | GDPR,NIS2 | D-03.3 | PR.AA-05,PR.AA-01 | CT.PO-P1 | N/A (non-AI scope) |
| CR-D-03.4-001 | CR | 3.00 (MUST) | CRA | D-03.4 | PR.PS-01 | CT.DP-P4,CT.PO-P4 | N/A (non-AI scope) |
| CR-D-04.1-001 | CR | 3.00 (MUST) | CRA,NIS2,AI_Act | D-04.1 | DE.AE-02,DE.CM-01,DE.CM-09 | CM.AW-P7 | MEASURE-2.4,MEASURE-3.1,MANAGE-2.3,MANAGE-4.1 |
| CR-D-04.2-001 | CR | 3.00 (MUST) | GDPR,CRA,NIS2 | D-04.2 | RS.MI-01,RS.MI-02 | PR.PO-P7,CT.DM-P10 | N/A (non-AI scope) |
| CR-D-04.3-001 | CR | 3.00 (MUST) | GDPR,CRA,NIS2,AI_Act | D-04.3 | RS.CO-02,RS.CO-03 | CM.AW-P7,CM.PO-P2,CM.PO-P1,GV.PO-P5 | MANAGE-2.3,MANAGE-4.3,GOVERN-1.1 |
| CR-D-04.4-001 | CR | 3.00 (MUST) | GDPR,NIS2 | D-04.4 | RC.RP-01,RC.RP-03,RC.RP-05 | UNMAPPED_PF (no PF 1.0 backup/DR recovery subcategory) | N/A (non-AI scope) |
| CR-D-05.1-001 | CR | 3.00 (MUST) | GDPR,CRA,AI_Act | D-05.1 | PR.DS-10,ID.AM-03 | CT.PO-P4,CT.DP-P4,ID.RA-P3 | GOVERN-1.4,MAP-2.1,MEASURE-2.11,MAP-2.2 |
| CR-D-05.2-001 | CR | 3.00 (MUST) | GDPR,AI_Act | D-05.2 | PR.DS-01,PR.PS-06 | CT.PO-P4,CT.DM-P5 | MEASURE-2.4,MEASURE-4.2,GOVERN-1.4 |
| CR-D-05.3-001 | CR | 3.00 (MUST) | GDPR,CRA | D-05.3 | PR.DS-10 | CT.DM-P4,CT.DM-P5 | N/A (non-AI scope) |
| CR-D-05.4-001 | CR | 3.00 (MUST) | GDPR | D-05.4 | UNMAPPED_CSF | CT.DM-P1,CT.DM-P6 | N/A (non-AI scope) |
| CR-D-06.1-001 | CR | 3.00 (MUST) | GDPR,NIS2 | D-06.1 | GV.SC-04; GV.SC-07; ID.RA-10 | ID.IM-P2 | N/A (non-AI scope) |
| CR-D-06.2-001 | CR | 3.00 (MUST) | CRA | D-06.2 | GV.SC-09 | ID.IM-P7 | N/A (non-AI scope) |
| CR-D-06.3-001 | CR | 3.00 (MUST) | GDPR,NIS2 | D-06.3 | GV.SC-05; GV.SC-06 | GV.PO-P5 | N/A (non-AI scope) |
| CR-D-06.4-001 | CR | 3.00 (MUST) | NIS2 | D-06.4 | DE.CM-06,PR.IR-01 | UNMAPPED_PF (no PF 1.0 analogue for physical third-party boundary isolation) | N/A (non-AI scope) |
| CR-D-07.1-001 | CR | 3.00 (MUST) | GDPR,CRA,AI_Act | D-07.1 | PR.PS-06,ID.RA-01 | GV.PO-P2,CT.PO-P4,CT.DP-P2,CT.DP-P5 | N/A (non-AI scope) |
| CR-D-07.2-001 | CR | 3.00 (MUST) | CRA,NIS2 | D-07.2 | PR.PS-06 | UNMAPPED_PF (no PF 1.0 secure-SDLC subcategory) | N/A (non-AI scope) |
| CR-D-07.3-001 | CR | 3.00 (MUST) | NIS2 | D-07.3 | PR.PS-06,PR.PS-02 | PR.PO-P4 | N/A (non-AI scope) |
| CR-D-08.1-001 | CR | 3.00 (MUST) | GDPR,NIS2 | D-08.1 | PR.AT-01 | GV.AT-P1,GV.AT-P2 | N/A (non-AI scope) |
| CR-D-08.2-001 | CR | 3.00 (MUST) | GDPR,NIS2,AI_Act | D-08.2 | PR.AT-02 | GV.AT-P1,GV.AT-P2 | MAP-3.5,GOVERN-2.1,GOVERN-2.2,GOVERN-3.1 |
| CR-D-09.1-001 | CR | 3.00 (MUST) | GDPR,CRA,NIS2,AI_Act | D-09.1 | GV.PO-01,GV.PO-02 | GV.PO-P1,GV.PO-P5,CM.PO-P1 | GOVERN-1.1,GOVERN-1.3,GOVERN-1.4,GOVERN-1.6,MAP-1.1,MEASURE-2.8,MEASURE-2.9,MAP-3.4 |
| CR-D-09.2-001 | CR | 3.00 (MUST) | GDPR,CRA,NIS2,AI_Act | D-09.2 | ID.RA-04,ID.RA-05,GV.RM-06 | ID.RA-P3,ID.RA-P4,ID.RA-P5 | GOVERN-1.1,GOVERN-1.3,GOVERN-1.5,MAP-5.1,MAP-3.1,MAP-3.2,MANAGE-1.2 |
| CR-D-09.4-001 | CR | 3.00 (MUST) | GDPR,AI_Act | D-09.4 | ID.AM-07,GV.OC-03 | ID.IM-P1,ID.IM-P4,ID.IM-P6,ID.IM-P8,CM.PO-P1 | MEASURE-2.4,MEASURE-3.1,GOVERN-1.6,GOVERN-2.1,MEASURE-4.2 |
| CR-D-10.1-001 | CR | 3.00 (MUST) | CRA,NIS2,AI_Act | D-10.1 | DE.CM-01,DE.CM-09,DE.AE-02 | CM.AW-P7 | MANAGE-4.1,MEASURE-3.1,MEASURE-4.1,GOVERN-1.5,MEASURE-2.4 |
| CR-D-10.2-001 | CR | 3.00 (MUST) | CRA,NIS2,AI_Act | D-10.2 | PR.PS-04,DE.AE-03,RS.AN-06 | CT.DM-P9 | MEASURE-2.4,MEASURE-3.1,GOVERN-1.6,MEASURE-4.2,GOVERN-1.4,GOVERN-2.1 |
| CR-D-10.3-001 | CR | 3.00 (MUST) | GDPR,CRA,NIS2,AI_Act | D-10.3 | ID.IM-01,ID.IM-02,ID.IM-03 | UNMAPPED_PF (no PF 1.0 compliance-testing subcategory) | MEASURE-2.7,MEASURE-2.11,MANAGE-1.2,MEASURE-3.1 |
| BPR-D-01.1-001 | BPR | 2.0 (SHOULD) | — | D-01.1 | PR.DS-01,PR.DS-10 | PR.DS-P1,CT.DP-P2 | N/A (non-AI scope) |
| BPR-D-01.2-001 | BPR | 2.0 (SHOULD) | — | D-01.3 | PR.DS-01 | PR.DS-P1,CT.DP-P2 | N/A (non-AI scope) |
| BPR-D-02.1-001 | BPR | 2.0 (SHOULD) | — | D-02.1 | ID.RA-01,DE.CM-01 | ID.RA-P3,ID.RA-P5 | N/A (non-AI scope) |
| BPR-D-02.5-001 | BPR | 2.0 (SHOULD) | — | D-02.1 | ID.RA-01,DE.CM-01 | ID.RA-P3,ID.RA-P5 | N/A (non-AI scope) |
| BPR-D-03.1-001 | BPR | 2.0 (SHOULD) | — | D-03.1 | PR.AA-01,PR.AA-05 | CT.PO-P1 | N/A (non-AI scope) |
| BPR-D-03.5-001 | BPR | 2.0 (SHOULD) | — | D-03.1 | PR.AA-01,PR.AA-05 | CT.PO-P1 | N/A (non-AI scope) |
| BPR-D-04.1-001 | BPR | 2.0 (SHOULD) | — | D-04.1 | DE.AE-02,DE.CM-01 | CM.AW-P7 | MANAGE-2.3,MANAGE-4.3 |
| BPR-D-04.5-001 | BPR | 2.0 (SHOULD) | — | D-04.1 | DE.AE-02,DE.CM-01 | CM.AW-P7 | MANAGE-2.3,MANAGE-4.3 |
| BPR-D-05.5-001 | BPR | 2.0 (SHOULD) | — | D-05.1 | PR.DS-10,ID.AM-03 | CT.PO-P4,CT.DP-P4 | MAP-2.1,MAP-2.2,MEASURE-2.11 |
| BPR-D-06.5-001 | BPR | 2.0 (SHOULD) | — | D-06.1 | GV.SC-04; GV.SC-07 | ID.IM-P2 | N/A (non-AI scope) |
| BPR-D-07.1-001 | BPR | 2.0 (SHOULD) | — | D-07.1 | PR.PS-06 | GV.PO-P2,CT.PO-P4 | GOVERN-4.1,GOVERN-4.3,MEASURE-2.7 |
| BPR-D-07.5-001 | BPR | 2.0 (SHOULD) | — | D-07.3 | PR.PS-06,PR.PS-02 | PR.PO-P4 | N/A (non-AI scope) |
| BPR-D-08.4-001 | BPR | 2.0 (SHOULD) | — | D-08.1 | PR.AT-01 | GV.AT-P1,GV.AT-P2 | N/A (non-AI scope) |
| BPR-D-09.1-001 | BPR | 2.0 (SHOULD) | — | D-09.1 | GV.PO-01,GV.PO-02 | GV.PO-P1,GV.PO-P5 | GOVERN-1.1,GOVERN-1.4,GOVERN-1.5 |
| BPR-D-09.5-001 | BPR | 2.0 (SHOULD) | — | D-09.1 | GV.PO-01,GV.PO-02 | GV.PO-P1,GV.PO-P5 | GOVERN-1.1,GOVERN-1.4,GOVERN-1.5 |
| BPR-D-10.1-001 | BPR | 2.0 (SHOULD) | — | D-10.1 | DE.CM-01,DE.CM-09 | CM.AW-P7 | MANAGE-4.1,MEASURE-3.1,MEASURE-2.4 |
| BPR-D-10.4-001 | BPR | 2.0 (SHOULD) | — | D-10.1 | DE.CM-01,DE.CM-09 | CM.AW-P7 | MANAGE-4.1,MEASURE-3.1,MEASURE-2.4 |

### V2 — Mapa de Cobertura por Function

> 15 rows (6 CSF + 5 Privacy + 4 AI RMF Functions). For each Function, count distinct subcategories covered by CR, BPR, and the gap (subcats in the frozen list not covered by any CR or BPR). Source: §1 + §3 + frozen function totals.

| # | Framework | Function | total_subcats | subcats_with_CR | subcats_with_BPR | subcats_gap |
|---|-----------|----------|---------------|-----------------|------------------|-------------|
| 1 | CSF | GV | 19 | 10 | 4 | 9 |
| 2 | CSF | ID | 13 | 14 | 2 | 0 |
| 3 | CSF | PR | 22 | 14 | 7 | 8 |
| 4 | CSF | DE | 10 | 5 | 3 | 5 |
| 5 | CSF | RS | 13 | 5 | 0 | 8 |
| 6 | CSF | RC | 6 | 3 | 0 | 3 |
| 7 | Privacy FW | GV-P | 37 | 7 | 4 | 28 |
| 8 | Privacy FW | ID-P | 25 | 8 | 1 | 17 |
| 9 | Privacy FW | CT-P | 20 | 6 | 1 | 13 |
| 10 | Privacy FW | CM-P | 10 | 2 | 1 | 8 |
| 11 | Privacy FW | PR-P | 46 | 11 | 3 | 34 |
| 12 | AI RMF | GOVERN | 19 | 11 | 5 | 8 |
| 13 | AI RMF | MAP | 18 | 9 | 2 | 9 |
| 14 | AI RMF | MEASURE | 22 | 13 | 4 | 9 |
| 15 | AI RMF | MANAGE | 13 | 5 | 3 | 8 |

### V3 — Grafo de Rastreabilidade

> `graph LR` extending §7 with 2 additional sub-paths: (f) NIS 2 incident path (CR-D-04.3-001) and (g) AI_Act FRIA path (CR-D-09.2-001). All 4 regulations are represented (GDPR, CRA, NIS 2, AI_Act); the 3 frameworks (CSF, Privacy FW, AI RMF) are the mapping targets. Class definitions preserved from §7.

```mermaid
graph LR
  %% V3 Traceability Graph — Case_02 (3 frameworks, 4 regulations)
  %% Sub-paths: (a) GDPR-only; (b) CRA-only; (c) NIS 2-only; (d) AI_Act-only; (e) Multi-reg; (f) NIS 2 incident; (g) AI_Act FRIA

  %% (a) GDPR-only path — CR-D-05.4-001 (data portability)
  GDPR_Art20[GDPR Art. 20 Right to Portability] --> GDPR_C07[GDPR-C07]
  GDPR_C07 --> CR_05_4[CR-D-05.4-001 MUST NI=3]
  CR_05_4 --> SD_05_4[D-05.4 Data Portability]
  SD_05_4 --> PF_CT_DM_P1[PF CT.DM-P1]
  SD_05_4 --> PF_CT_DM_P6[PF CT.DM-P6]
  SD_05_4 --> ISO_A5_14[ISO A.5.14]
  SD_05_4 --> UNMAPPED_CSF[UNMAPPED_CSF]

  %% (b) CRA-origin path — CR-D-02.1-001
  CRA_AnnexI_2a[CRA Annex I §2(a)] --> CRA_C01[CRA-C01]
  CRA_C01 --> CR_02_1[CR-D-02.1-001 MUST NI=3]
  CR_02_1 --> SD_02_1[D-02.1 Vulnerability Identification]
  SD_02_1 --> CSF_ID_RA_01[CSF ID.RA-01]
  SD_02_1 --> CSF_ID_RA_08[CSF ID.RA-08]
  SD_02_1 --> SSDF_RV_1[SSDF RV.1]
  SD_02_1 --> ISO_A8_8[ISO A.8.8]

  %% (c) NIS 2-only path — CR-D-09.3-001 (asset inventory, NIS 2 Sole Authority)
  NIS2_Art21[NIS 2 Art. 21(2)(d) Asset management] --> NIS2_C07[NIS2-C07]
  NIS2_C07 --> CR_09_3[CR-D-09.3-001 MUST NI=3]
  CR_09_3 --> SD_09_3[D-09.3 Asset Inventories]
  SD_09_3 --> CSF_ID_AM_01[CSF ID.AM-01]
  SD_09_3 --> CSF_ID_AM_02[CSF ID.AM-02]
  SD_09_3 --> CSF_ID_AM_07[CSF ID.AM-07]
  SD_09_3 --> PF_ID_IM_P1[PF ID.IM-P1]
  SD_09_3 --> NA_AIS_NIS[N/A (non-AI scope) — no AI-C* in NIS2-C07]
  SD_09_3 --> ISO_A5_9[ISO A.5.9]

  %% (d) AI_Act-origin path — CR-D-05.1-001 (data governance, AI_Act)
  AI_Art10[AI_Act Art. 10 Data governance] --> AI_C05[AI-C05]
  AI_C05 --> CR_05_1[CR-D-05.1-001 MUST NI=3]
  CR_05_1 --> SD_05_1[D-05.1 Data Minimisation]
  SD_05_1 --> CSF_PR_DS_10[CSF PR.DS-10]
  SD_05_1 --> PF_CT_PO_P4[PF CT.PO-P4]
  SD_05_1 --> AI_GOVERN_1_4[AI RMF GOVERN-1.4]
  SD_05_1 --> AI_MAP_2_1[AI RMF MAP-2.1]
  SD_05_1 --> AI_MEASURE_2_11[AI RMF MEASURE-2.11]

  %% (e) Multi-regulation path — CR-D-01.1-001 (4-reg)
  GDPR_C14_2[GDPR-C14] --> CR_01_1[CR-D-01.1-001 MUST NI=3]
  CRA_C07_2[CRA-C07] --> CR_01_1
  NIS2_C18_2[NIS2-C18] --> CR_01_1
  AI_C17_2[AI-C17] --> CR_01_1
  CR_01_1 --> SD_01_1[D-01.1 Data at Rest Encryption]
  SD_01_1 --> CSF_PR_DS_01[CSF PR.DS-01]
  SD_01_1 --> PF_PR_DS_P1[PF PR.DS-P1]
  SD_01_1 --> PF_CT_DP_P2[PF CT.DP-P2]
  SD_01_1 --> AI_MEASURE_2_7[AI RMF MEASURE-2.7]
  SD_01_1 --> AI_MEASURE_2_5[AI RMF MEASURE-2.5]
  SD_01_1 --> ISO_A8_24[ISO A.8.24]
  SD_01_1 --> SSDF_PO_5[SSDF PO.5]

  %% (f) NIS 2 incident path — CR-D-04.3-001 (NIS 2 anchor + multi-reg T-001)
  NIS2_Art23[NIS 2 Art. 23 Significant incident] --> CR_04_3[CR-D-04.3-001 MUST NI=3]
  CR_04_3 --> SD_04_3[D-04.3 Regulatory Notification]
  SD_04_3 --> CSF_RS_CO_02[CSF RS.CO-02]
  SD_04_3 --> PF_CM_AW_P7[PF CM.AW-P7]
  SD_04_3 --> AI_MANAGE_4_3[AI RMF MANAGE-4.3]
  SD_04_3 --> ISO_A5_24[ISO A.5.24]
  CR_04_3 -. T-001 .-> T001[(T-001 max-SLA 24h routing)]

  %% (g) AI_Act FRIA path — CR-D-09.2-001 (DPIA + FRIA convergence)
  AI_Art27[AI_Act Art. 27 FRIA] --> CR_09_2[CR-D-09.2-001 MUST NI=3]
  CR_09_2 --> SD_09_2[D-09.2 Risk Assessments]
  SD_09_2 --> CSF_ID_RA_04[CSF ID.RA-04]
  SD_09_2 --> CSF_ID_RA_05[CSF ID.RA-05]
  SD_09_2 --> PF_ID_RA_P3[PF ID.RA-P3]
  SD_09_2 --> PF_ID_RA_P5[PF ID.RA-P5]
  SD_09_2 --> AI_GOVERN_1_1[AI RMF GOVERN-1.1]
  SD_09_2 --> AI_MAP_5_1[AI RMF MAP-5.1]
  CR_09_2 -. T-003 .-> T003[(T-003 unified DPIA+FRIA)]

  %% Class definitions
  classDef crNode fill:#cce5ff,stroke:#003366,color:#000
  classDef sdNode fill:#d4edda,stroke:#155724,color:#000
  classDef csfNode fill:#fff3cd,stroke:#856404,color:#000
  classDef pfNode fill:#f8d7da,stroke:#721c24,color:#000
  classDef aiNode fill:#e2d5f1,stroke:#5b2c6f,color:#000
  classDef isoNode fill:#d6d8db,stroke:#1b4d3e,color:#000
  classDef tensionNode fill:#ffe5b4,stroke:#cc6600,color:#000
  classDef unmappedNode fill:#f5f5f5,stroke:#999,color:#000,stroke-dasharray: 5 5

  class CR_01_1,CR_02_1,CR_04_3,CR_05_1,CR_05_4,CR_09_2,CR_09_3 crNode
  class SD_01_1,SD_02_1,SD_04_3,SD_05_1,SD_05_4,SD_09_2,SD_09_3 sdNode
  class CSF_PR_DS_01,CSF_PR_DS_10,CSF_ID_RA_01,CSF_ID_RA_04,CSF_ID_RA_05,CSF_ID_RA_08,CSF_RS_CO_02,CSF_ID_AM_01,CSF_ID_AM_02,CSF_ID_AM_07 csfNode
  class PF_PR_DS_P1,PF_CT_DP_P2,PF_CT_PO_P4,PF_CT_DM_P1,PF_CT_DM_P6,PF_CM_AW_P7,PF_ID_RA_P3,PF_ID_RA_P5,PF_ID_IM_P1 pfNode
  class AI_MEASURE_2_5,AI_MEASURE_2_7,AI_MEASURE_2_11,AI_GOVERN_1_1,AI_GOVERN_1_4,AI_MAP_2_1,AI_MAP_5_1,AI_MANAGE_4_3 aiNode
  class ISO_A5_14,ISO_A5_24,ISO_A8_8,ISO_A8_24,SSDF_RV_1,SSDF_PO_5,ISO_A5_9 isoNode
  class T001,T003 tensionNode
  class UNMAPPED_CSF,NA_AIS_NIS unmappedNode
```

### V4 — Implementation Status overview per sub-domain (replaces the legacy numerical heatmap)

> 35-row table (one per active Case_02 sub-domain per Track B). D-07.4, D-08.3, D-09.3 are OUT-OF-SCOPE per `Doc12_Proportionality_Profile.md` §4 + §11.4 F-01/F-05 and excluded from this heatmap. Columns: `sub_domain, cur_csf, tgt_csf, cur_priv, tgt_priv, cur_airmf, tgt_airmf, gap_csf, gap_priv, gap_airmf, gap_min, gap_worst, color`. Heatmap color driven by `gap_worst` (MAX of applicable gaps per §4.6 N/A-exclusion rule); `gap_min` (MIN) is preserved as a coverage indicator. Color buckets: GREEN (gap_worst 0), YELLOW (gap_worst 1), ORANGE (gap_worst 2), RED (gap_worst 3-4), GREY (N/A). Sorted by `gap_worst` descending (worst at top).

| sub_domain | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Note |
|------------|------|---------|---------|------|
|------------|--------:|--------:|---------:|---------:|----------:|----------:|--------:|---------:|----------:|--------:|----------:|:------|
| D-04.3 | PARTIAL | PARTIAL | PARTIAL | backfilled from legacy 2→4 / 3→4 / 3→4 (was ORANGE) |
| D-05.3 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 2→4 / 3→3 / N/A→N/A (was ORANGE) |
| D-07.1 | PARTIAL | PARTIAL | N/A | backfilled from legacy 2→4 / 3→4 / N/A→N/A (was ORANGE) |
| D-07.3 | PARTIAL | PARTIAL | N/A | backfilled from legacy 2→4 / 3→4 / N/A→N/A (was ORANGE) |
| D-10.1 | PARTIAL | PARTIAL | PARTIAL | backfilled from legacy 2→4 / 3→4 / 2→4 (was ORANGE) |
| D-01.1 | PARTIAL | PARTIAL | PARTIAL | backfilled from legacy 3→4 / 3→4 / 3→4 (was YELLOW) |
| D-01.2 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-01.3 | PARTIAL | PARTIAL | PARTIAL | backfilled from legacy 3→4 / 3→4 / 3→4 (was YELLOW) |
| D-02.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 3→4 / 3→3 / 3→3 (was YELLOW) |
| D-02.2 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-02.3 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-02.4 | PARTIAL | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 2→3 / 3→3 / 3→3 (was YELLOW) |
| D-03.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 3→4 / 3→3 / 3→3 (was YELLOW) |
| D-03.2 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-03.3 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-03.4 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-04.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 3→4 / 3→3 / 3→3 (was YELLOW) |
| D-04.2 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-04.4 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-05.1 | PARTIAL | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 3→4 / 3→3 / 3→3 (was YELLOW) |
| D-05.2 | PARTIAL | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 3→4 / 3→3 / 3→3 (was YELLOW) |
| D-05.4 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-06.1 | PARTIAL | PARTIAL | N/A | backfilled from legacy 3→4 / 3→4 / N/A→N/A (was YELLOW) |
| D-06.2 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-06.3 | PARTIAL | PARTIAL | N/A | backfilled from legacy 3→4 / 3→4 / N/A→N/A (was YELLOW) |
| D-06.4 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-07.2 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-08.1 | PARTIAL | IMPLEMENTED | N/A | backfilled from legacy 3→4 / 3→3 / N/A→N/A (was YELLOW) |
| D-08.2 | PARTIAL | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 3→4 / 3→3 / 3→3 (was YELLOW) |
| D-09.2 | PARTIAL | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 3→4 / 3→3 / 3→3 (was YELLOW) |
| D-09.4 | PARTIAL | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 3→4 / 3→3 / 3→3 (was YELLOW) |
| D-10.2 | PARTIAL | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 3→4 / 3→3 / 3→3 (was YELLOW) |
| D-10.3 | PARTIAL | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 3→4 / 3→3 / 3→3 (was YELLOW) |
| D-01.4 | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 3→3 / 3→3 / 3→3 (was GREEN) |
| D-09.1 | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | backfilled from legacy 4→4 / 3→3 / 3→3 (was GREEN) |

**Status overview.** Per-axis status counts derive from §5.1 (IMPLEMENTED 54 · PARTIAL 67 · N/A 35 · NOT IMPLEMENTED 0 across 156 axis-cells). No sub-domain is NOT IMPLEMENTED; the ORANGE legacy band (D-04.3, D-05.3, D-07.1, D-07.3, D-10.1) corresponds to PARTIAL controls with active remediation documented in §4.5/§5.2.

---

## Validation Notes (informative)

> Pre-`validate_doc.py` notes; full validation in `12_Rules_Catalog.xlsx` (Block F).

- **§1 coverage:** 38 CR × 12 columns = 456 cells. UNMAPPED tokens: 1 CSF (D-05.4), 0 Privacy FW, 21 AI RMF (justified by no AI-C* in source).
- **§3 coverage:** 38 CR + 17 BPR = 55 YAML blocks. BPR-D-* count = 17 (matches `Doc18_Rules_Catalog.md` BPR list with `BPR-D-*` prefix). BPR-AI-* are documented in `Doc18_Rules_Catalog.md` §5.2 / §9.2 but treated as a separate AI-specific BPR subset (not part of the 17 BPR-D-* mapping in §3.2).
- **§4.5 / §5.2 Function coverage:** 15 Functions (6 CSF + 5 Privacy + 4 AI RMF). No UNMAPPED Functions.
- **§6 framework unused subcategories:** CSF ~14 acceptable, PF 45 acceptable, AI RMF 31 documented in `02b_SecurityRules_NISTAIRMF.md`.
- **§7 Mermaid:** 5 paths (a/b/c/d/e) + governance convergence sub-path. 6 tensions referenced (T-001, T-002, T-003 visible; T-004 via D-09.1).

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-07 | Executor (Bloco C) | Initial release — Case_02 unified matrix (3 frameworks CSF + Privacy FW + AI RMF) + triple maturity. 38 CR + 17 BPR = 55 cards. §1-§8 present. Tensions T-001..T-004 cross-referenced in §2.5 and §6.5. AI RMF column ACTIVE (not placeholder). |

---

## See also

- `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/Doc18_Rules_Catalog.md` — 38 CR + 25 BPR (canonical Rich Mode catalog for Case_02).
- `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/Doc15_Strategic_Tensions_Report.md` — 8 tensions (T-001..T-008); T-001..T-004 are the most relevant for the Govern view §2.5.
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/Doc12_Proportionality_Profile.md` — Track B tier per sub-domain (8 RIGOROUS + 27 STANDARD + 3 EXCLUDED).
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/Doc05_Security_Posture.md` — qualitative posture input per macro-domain (DEPRECATED_FOR_POSTURE; superseded as scoring source).
- `00_METHODOLOGY/PREPROCESSING/Regulation/GDPR/02b_SecurityRules_NISTPF.md` — 68 SR GDPR→PF (100% coverage; 59/104 active PF subcats used).
- `00_METHODOLOGY/PREPROCESSING/Regulation/AI_Act/02b_SecurityRules_NISTAIRMF.md` — 24 SR AI_Act→AI RMF (100% coverage; 41/72 active AI RMF subcats used).
- `00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md` — CSF 2.0 frozen list (106 subcats).
- `00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md` — Privacy FW 1.0 frozen list (138 subcats; 104 active + 34 v1.0 redirects).
- `00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md` — AI RMF 1.0 frozen list (72 subcats).
- `03_REFERENCE_MATERIAL/Framework_Mappings/Framework_Crosswalk_ARM.md` — Framework crosswalk ACTIVE v1.0 (38/38 CSF, 38/38 ISO, 23/38 SSDF).
- `02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/SPEC_NIST_MATRIX_UNIFIED.md` — Case_01 SPEC for methodology reference.
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` — clause IDs and NI baseline.
- Root `AGENTS.md` — branch workflow + methodology invariants.

