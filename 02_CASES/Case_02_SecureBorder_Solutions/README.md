# Case_02 — SecureBorder Solutions B.V.

## Company profile
- **Legal name:** SecureBorder Solutions B.V. (Netherlands, EU)
- **Sector:** Defense / Security / Critical Infrastructure (border-control eGate kiosks "GuardianGate")
- **Size:** 450 employees, ~€120M revenue (F-01 settled: scale = MEDIUM, P7 human arbiter 2026-08-10)
- **Complexity tier:** HIGH (4 regulations applicable)
- **Applicable regulations:** GDPR ✅, CRA ✅ (Critical Class), NIS 2 ✅ (Essential Entity Supplier), AI Act ✅ (Annex III High-Risk), DORA ❌

## Architecture map

### Phase 1 — Context (Rich Mode)
- `01_PHASE1_CONTEXT_RICH/`
  - `01_INTAKE_FORM.md` (Q1-Q72 intake)
  - `04_Company_Context_Assessment.md` (BG-01..BG-05 business goals)
  - `04a_Architecture_DataInventory.md` (system inventory + data flows)
  - `04b_Security_Posture.md` (current controls + maturity)
  - `04c_ThirdParty_Landscape.md` (subprocessors + DPAs)
  - `04d_Org_Roles_RACI.md` (RACI matrix)
  - `05_Regulatory_Applicability.md` (per-article applicability)
  - `05b_Ambiguity_Register.md` (Berry ambiguity cards)
  - `06_Clause_Mapping_Matrix.md` (clauses → corpus)
  - `07_Structured_Compliance_Matrix.md` (sub-domain coverage matrix)
  - `07b_Proportionality_Profile.md` (Track B decisions; F-01 SETTLED)
  - **`Doc13_Adjusted_Goals.md`** (Phase 1 AO layer, 35 ACTIVE subdomains × 1-4 AOs each; tech-free)
  - `phase1_ontology.yaml` (canonical ontology; F-01..F-06 status)
  - `Citation_Index.md`, `corpus_field_map.md`, `RICH_VS_LEGACY.md`, `PROJECT_STATE.md`

### Phase 2 — Rules (Rich Mode)
- `02_PHASE2_RULES_RICH/`
  - `08_Obligation_Derivation.md` (30 OBLs from 4 regs)
  - `09_Strategic_Tensions_Report.md` (T-001..T-009; F-03 added T-009)
  - **`10_Privacy_Security_Goals.md`** (Phase 2 PSO layer: 34 PO + 55 SO = 89 PSOs)
  - `10b_Privacy_Security_Goals_NIST_Implications.md` (PO/SO × NIST CSF/PRIV/AI RMF)
  - **`11_Rules_Catalog.md`** (38 CR + 25 BPR = 63 rules, 23 fields per entry)
  - `12_Rules_Catalog.xlsx` (xlsx generator output)
  - `13_Framework_Mapping_Matrix.md` (legacy, PO/SO migration + tech-strip)
  - **`13_Framework_Mappings.xlsx`** (3-sheet: NIST CSF + Privacy + AI RMF, 12 cols each)

### Phase 3 — Decomposition (Rich Mode)
- `03_PHASE3_DECOMPOSITION/`
  - `13_Use_Cases_Catalog.md` (UC + FR + NFR; PSO-linked)
  - `14_Architectural_Nodes.md` (PROC + SYS nodes)
  - `15_Requirements_Allocation.md` (DN → rule linkage)
  - `16_Compliance_Gates_Report.md` (GATE + SC1/SC2)
  - `17_Functional_Tree.md` (FT-X.Y → Phase 1 AO linkage)
  - `25_Risk_Analysis.md` (R + T; T-001..T-009)

### Legacy (read-only, deprecated)
- `00_COMMON/` (legacy Phase 0)
- `01_PHASE1_CONTEXT/` (legacy Phase 1; superseded by 01_PHASE1_CONTEXT_RICH/)
- `02_PHASE2_RULES/` (legacy Phase 2; superseded by 02_PHASE2_RULES_RICH/)

## ID hierarchy

```
Corpus (frozen):    SO-D-XX.Y.{HL,GDPR,CRA,NIS2,AI_Act}

Phase 1 (AOs):      AO-D-XX.X-NNN (1-4 per active subdomain × regulation)

Phase 2 (PSOs):     PO-D-XX.X-NNN (Privacy Operational Objective)
                    SO-D-XX.X-NNN (Security Operational Objective)
                    (89 total: 34 PO + 55 SO)

Phase 2 (Rules):    CR-D-XX.X-NNN (Compliance Rule, 38)
                    BPR-D-XX.X-NNN (Best Practice Rule, 25; framework flag: GDPR/CRA/NIS2/AI_Act/ISO/NIST)

Phase 3 (decomp):   UC-XX (use cases)
                    FR-XX / NFR-XX (requirements)
                    FT-X.Y (functional tree)
                    N-XX (nodes)
                    G-X.Y (compliance gates)
                    R-X / THR-REG-XX (risks)
                    T-XXX (tensions, 9 total: T-001..T-009)
```

## Sub-domain coverage (35 ACTIVE)

| Sub-D | GDPR | CRA | NIS2 | AI Act | Tier |
|-------|------|-----|-------|--------|------|
| D-01.1 | ✅ | ✅ | ✅ | ✅ | RIGOROUS |
| D-01.3 | — | ✅ | ✅ | ✅ | RIGOROUS |
| D-04.3 | ✅ | ✅ | ✅ | ✅ | RIGOROUS |
| D-06.1 | ✅ | — | ✅ | — | RIGOROUS |
| D-06.3 | ✅ | — | ✅ | — | RIGOROUS |
| D-07.1 | ✅ | ✅ | ✅ | — | RIGOROUS |
| D-07.3 | — | — | ✅ | — | RIGOROUS |
| D-10.1 | — | ✅ | ✅ | ✅ | RIGOROUS |
| ... (27 STANDARD) | | | | | STANDARD |
| **8 RIGOROUS + 27 STANDARD = 35** | | | | | |

NOT_ADDRESSED: D-07.4 (NIS 2-only, ISO 27001 overlap), D-08.3 (NIS 2-only, board briefing), D-09.3 (NIS 2-only, ISO 27001 overlap)

## Findings

- **F-01** SETTLED (Scale = MEDIUM, P7 human arbiter 2026-08-10)
- **F-03** RESOLVED (T-009 D-10.1 monitoring opt-out)
- **F-04** RESOLVED (T-002 AI Act Art. 12 → Art. 19(1))
- **F-06** RESOLVED (AI_Act casing normalization)
- F-02, F-05 — still OPEN, deferred to future sprints

## Validation gates

```bash
source .venv/bin/activate
python 01_IMPLEMENTATION_TOOLS/scripts/validate_aegis_ids.py --quiet
python 01_IMPLEMENTATION_TOOLS/lints/run_all_lints.py --case "Case_02_SecureBorder_Solutions"
```

Expected: 17/19 PASS (Document Structure + Strategic Tensions pre-existing failures unrelated to migration).

## Migration history

- Sprint 9 (corr-Case02 A→F, 2026-08-10): 6 commits on `feature/aegis-p2-case02-full-migration`
- A: F-01 SETTLED MEDIUM
- B: F-03 (T-009) + F-04 (T-002 cite) + F-06 (AI_Act casing)
- C: Tech-strip 07c + Phase 1 RICH (131 → 0 vendor refs)
- D: Phase 2 migration (89 PSOs + 63 rules + 13_Framework_Mappings.xlsx with AI RMF populated)
- E: Phase 3 harmonisation (UC/FR/NFR + AO/PSO linkage)
- F: This README + final cleanup
