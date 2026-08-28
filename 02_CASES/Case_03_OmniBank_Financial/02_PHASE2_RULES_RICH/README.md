---
document_id: AEGIS-P2-RICH-README-CASE03
title: README — Phase 2 Rich Mode (Case_03)
phase: 2
version: 1.0
created: 2026-08-07
updated: 2026-08-08
author: Rich-Symmetry Executor (Case_03 replication)
status: ACTIVE
case: Case_03_OmniBank_Financial
tier: MAX
sibling_of: ../02_PHASE2_RULES_RICH/
branch: feature/aegis-p2-case03-csf-pf-airmf
verdict: PASS_WITH_FINDINGS
---

# Phase 2 Rich Mode — Case_03 (OmniBank Financial Systems)

> Phase 2 Rich Mode — corpus-enriched sibling of legacy `02_PHASE2_RULES/`.
> Case_03 contract: AEGIS Phase 2 — Case_03 OmniBank Financial — CSF + Privacy FW + AI RMF (MAX complexity).
>
> **Status:** All 7 blocos (A→G) merged into `main` on `feature/aegis-p2-case03-csf-pf-airmf`. This Rich folder
> now mirrors the structural skeleton of Case_01 Rich Mode (12 files + `validation/` subfolder).
> All 9 validation reports present, including the Tier-1+2 Validator verdict (PASS_WITH_FINDINGS, 8 findings tracked).

---

## §1 Status Dashboard

| Bloco | Date | Theme | Status |
|-------|------|-------|:------:|
| **Validator** | 2026-08-07 | Tier 1+2 PASS_WITH_FINDINGS (independent verdict on 5 frameworks × 78 cards) | ✅ PASS_WITH_FINDINGS |
| **Bloco G fix** | 2026-08-07 | FN-01 Crosswalk ACTIVE + FN-02 frozen IDs + FN-03 ni_avg_rule_note + FN-05 §6.5 inventory | ✅ DONE |
| **Bloco F** | 2026-08-07 | 4 visualizações + Excel 10 sheets (3 frameworks, MAX complexity) | ✅ DONE |
| **Bloco E** | 2026-08-07 | 04b deprecated (maturity moved to Doc 13) | ✅ DONE |
| **Bloco D** | 2026-08-07 | Doc 11 estendido campos 19-24 (tri-maturidade CSF+PF+AI RMF) | ✅ DONE |
| **Bloco C** | 2026-08-07 | Doc 13 unified matrix (3 frameworks CSF+PF+AI RMF) | ✅ DONE |
| **Bloco B** | 2026-08-07 | NI formal (AVG+AI MUST), 78 cartões, DR-002 resolvido | ✅ DONE |
| **Bloco A** | 2026-08-07 | (Reused from Case_02 — Crosswalk already ACTIVE) | ⚠ REUSED |

**Aggregate:** ✅ All 7 blocos complete (B + C + D + E + F + G + Validator); Bloco A reused from Case_02 contract.

**Final status:** Phase 2 Rich Mode is `DEEP_ENRICHED`. Doc 13 unified matrix covers **3 NIST frameworks** (CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0) + DORA via CSF coverage, over **38 unique CR + 40 unique BPR = 78 cards**. Validator verdict: PASS_WITH_FINDINGS (FN-01, FN-02, FN-03, FN-05 addressed by Bloco G fix).

---

## §2 Deliverables Map

| Doc | Lines (legacy) | Lines (Rich, now) | Cards / content | Bloco | Status |
|-----|---------------:|------------------:|-----------------|:-----:|:------:|
| `Doc16_Obligation_Derivation.md` | 472 | 472 | 38 obligations, NI re-derived under AVG+AI MUST+DORA | legacy copy | ✅ COPIED |
| `Doc17_Strategic_Tensions_Report.md` | 687 | 687 | 5 tensions resolved (T-001..T-005; legacy row — port Fase 0) | legacy copy | ✅ COPIED |
| `Doc18_Privacy_Security_Objectives.md` | 461 | 461 | 76 goal rows (24 PG + 52 SG) | legacy copy | ✅ COPIED |
| `Doc20_Rules_Catalog.md` | 651 | 651+ | 78 cards (38 CR + 40 BPR, 17 fields + banner) | legacy copy + banner | ✅ COPIED |
| `12_Rules_Catalog.xlsx` | 24KB | 24KB | Excel catalog (canonical) | legacy copy | ✅ COPIED |
| `Doc21_Framework_Mapping_Matrix.md` | — | **unified matrix** | 3 frameworks (CSF + PF + AI RMF), triple maturity, DORA via CSF | C → D → F | ✅ DEEP_ENRICHED |
| `README.md` | — | this file | orientation + dashboard + schema | rich-symmetry | ✅ NEW |
| `PROJECT_STATE.md` | — | sibling | project state snapshot | rich-symmetry | ✅ NEW |
| `RICH_VS_LEGACY.md` | — | sibling | Rich vs legacy diff summary | rich-symmetry | ✅ NEW |
| `SPEC_NIST_MATRIX_UNIFIED.md` | — | sibling | 17-decision spec, 8 blocos | rich-symmetry | ✅ NEW |
| `10b_Privacy_Security_Goals_NIST_Implications.md` | — | sibling | 76 PG/SG × 3 frameworks implications | rich-symmetry | ✅ NEW |
| `validation/` (9 reports) | — | sibling | LINT_BEFORE + 5 Bloco reports + VALIDATOR_BLOCOG + VALIDATOR_SPRINT5 | rich-symmetry | ✅ NEW |

**Totals:** 5 Phase 2 legacy docs replicated + 7 orchestration/rich docs = **12 files + `validation/`**. Validator verdict: **PASS_WITH_FINDINGS**.

---

## §3 18-Field Schema (canonical, Case_03)

**12 base fields** (common to all tiers) + **3 triple-maturity fields** (CSF / Privacy FW / AI RMF) + **3 Case_03-specific fields** (MAX tier).

| # | Field | Type | Description |
|---|-------|------|-------------|
| 1 | Sub-Domain Name | header | e.g., `OBL-D-01.1-001 — Data Encryption at Rest` |
| 2 | Description | multi-paragraph | What + why + scope/out-of-scope context |
| 3 | Scope | paragraph | What's included (from Doc 07b §4) |
| 4 | Out of Scope | paragraph | What's excluded (edge cases) |
| 5 | Source Article | list | GDPR/CRA/NIS 2/DORA/AI Act article refs |
| 6 | NIST CSF Anchors | list | PR.DS-01, PR.AC-01, etc. |
| 7 | Privacy FW Anchors | list | PR.DS-P1, GV.PO-P1, etc. |
| 8 | AI RMF Anchors | list | GOVERN-1.1, MAP-1.1, etc. |
| 9 | Verification Criteria | 3+ bullets | Operational checks |
| 10 | Verification Method | enum | DEMONSTRATE / INSPECT / TEST / ANALYZE |
| 11 | Owner | role | CTO / DPO / CISO / AI Lead / DORA Compliance Officer |
| 12 | Status | enum | TODO / IN_PROGRESS / DONE |
| 13 | Dependencies | list | Related OBL/PG/SG IDs |
| 14 | Risk if not met | H/M/L + 1-line | Qualitative risk |
| 15 | Affected Stakeholders | list | Internal + external parties |
| 16 | Maturity (CSF) | Cur X/4 → Tgt Y/4 | 0-4 scale |
| 17 | Maturity (Privacy) | Cur X/4 → Tgt Y/4 | 0-4 scale |
| 18 | Maturity (AI RMF) | Cur X/4 → Tgt Y/4 | 0-4 scale |

**3 Case_03-specific fields:**

| # | Field | Case_03 Value |
|---|-------|---------------|
| (×) | Regulatory Reporting | EDPB 72h GDPR + ENISA 24h CRA + NIS 2 incident + DORA major ICT + AI Act serious incident |
| (×) | External Auditor | ISO 27001 + SOC 2 Type II + PCI-DSS + DORA ICT audit + AI Act conformity |
| (×) | Supervisory Body | EDPB + ENISA + national NIS 2 CSIRT + national DORA CA + national AI Act authority |

**Excluded by directive:** Effort, Cost, Timeline — absent from every card and every workbook sheet.

---

## §4 Case_03 Phase 2 Rich — Domain Profile

**Case:** OmniBank Financial Systems (banking / financial services)
**Tier:** MAX (5000+ FTE; multi-billion ARR)
**Applicable regulations:** 5/5 (GDPR + CRA + NIS 2 + **DORA** + AI Act) — **all 5 applicable**
**Sub-domains:** 38 obligation-bearing, all active (per `Doc13_Proportionality_Profile.md`)

| Metric | Value | Source |
|--------|------:|--------|
| Obligations (Doc 08) | 38 | `02_PHASE2_RULES/Doc16_Obligation_Derivation.md` §4 |
| Privacy Goals (PG) | 24 | `02_PHASE2_RULES/10_Privacy_Security_Goals.md` §4 (rows) |
| Security Goals (SG) | 52 | `02_PHASE2_RULES/10_Privacy_Security_Goals.md` §5 (rows) |
| Total goal rows | 76 | (24 PG + 52 SG; legacy summary header says "33" but row count is 76) |
| Tensions (Doc 09) | 7 (HIGH + MEDIUM + INACTIVE) | Rich `Doc17_Strategic_Tensions_Report.md` §4 |
| Compliance Rules (CR) | 38 unique | `02_PHASE2_RULES/Doc20_Rules_Catalog.md` §4 |
| Best Practice Rules (BPR) | 40 unique | `02_PHASE2_RULES/Doc20_Rules_Catalog.md` §5 |
| Total Rules | 78 | Doc 11 §6 |
| Track B distribution | 31 RIGOROUS + 7 STANDARD + 0 DEFERRED | `Doc13_Proportionality_Profile.md` §3 |
| Active sub-domains | 38/38 (all active, no DEFERRED) | `Doc13_Proportionality_Profile.md` §3 |
| Source clauses | GDPR (28) + CRA (26) + NIS 2 (29) + DORA (38) + AI Act (29) = 150 | Doc 08 §5 + Phase 1 ontology |
| Frameworks in scope | NIST CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0 (all 3 ACTIVE; DORA via CSF coverage) | Doc 13 frontmatter |

> **⚠ Goal count — read this before quoting.** Legacy Doc 10 §1/§2 summary states 33 total goals (11 PG + 22 SG). The actual table-row count is **24 PG + 52 SG = 76**. Doc 13 + Doc 11 use **76** as the canonical goal total. (Discrepancy surfaced as F-01 by Bloco G fix.)

---

## §5 Bloco Plan

### Bloco A — Crosswalk promotion ✅ REUSED
- `Framework_Crosswalk_ARM.md` was promoted to ACTIVE in the Case_02 contract (commit `c972048`)
- Case_03 reuses the promotion — no separate commit needed
- Note raised in Validator report (FN-01): missing Bloco A commit on Case_03 branch

### Bloco B — NI formalization ✅ COMPLETE
- DR-002 = AVG with AI MUST override (AI Act signal preserved); DORA clauses uniformly NI=3
- 78 cart rows with field 18 (NI) populated
- All GDPR/CRA/NIS 2 clauses re-evaluated; AI-C* and DORA-C* sources → NI=3 (MUST)
- Commit: `290cd67 [EXECUTOR] Bloco B — NI formal (AVG+AI MUST) em 78 cartões, DR-002 resolvido`

### Bloco C — Doc 13 unified matrix ✅ COMPLETE
- All 3 frameworks ACTIVE (CSF + PF + AI RMF); NO placeholder columns; DORA via CSF coverage
- 6 sub-sections + 2 visualisation sections
- 38 unique CR + 40 unique BPR = 78 YAML blocks
- Commit: `a89fefe [EXECUTOR] Bloco C — Doc 13 unified matrix (3 frameworks) + triple maturity (MAX complexity)`

### Bloco D — Doc 11 extension ✅ COMPLETE
- Fields 19-24 added: csf_subcategories, privacy_subcategories, ai_rmf_subcategories, maturity_csf, maturity_privacy, maturity_ai_rmf
- 18 fields per card (15→17 from Bloco B + 6 columns from Bloco D)
- Commit: `23e062c [EXECUTOR] Bloco D — Doc 11 estendido (campos 19-24, tri-maturidade CSF+PF+AI RMF)`

### Bloco E — 04b deprecated ✅ COMPLETE
- `Doc05_Security_Posture.md` status: DEPRECATED_FOR_MATURITY
- Maturity model ownership moved to Doc 13
- Commit: `7f57c76 [EXECUTOR] Bloco E — 04b deprecated for maturity (moved to Doc 13)`

### Bloco F — 4 visualizations + Excel ✅ COMPLETE
- V1 matriz cobertura, V2 mapa por Function, V3 Mermaid traceability graph, V4 heatmap
- 6 new Excel sheets added (Unified_Matrix, Govern_Consolidated, Mapping_nm, Maturity_Dual, Cov_Function, Heatmap_Maturity)
- Commit: `96364ed [EXECUTOR] Bloco F — 4 visualizações + 6 folhas Excel (3 frameworks, MAX complexity)`

### Bloco G fix — FN-01..FN-05 ✅ COMPLETE
- FN-01 Crosswalk ACTIVE (no commit on Case_03, but Crosswalk ACTIVE from Case_02)
- FN-02 frozen IDs enforced
- FN-03 ni_avg_rule_note frontmatter added
- FN-05 §6.5 inventory added
- Commit: `520c910 [EXECUTOR] Bloco G fix — FN-01 Crosswalk ACTIVE + FN-02 frozen IDs + FN-03 ni_avg_rule_note + FN-05 §6.5 inventory`

### Validator — Tier 1+2 ✅ PASS_WITH_FINDINGS
- Independent sub-agent verdict
- All Tier 1 checks PASS after Bloco G fix
- Tier 2 alignment check: PASS_WITH_FINDINGS (F-01 goal count discrepancy from legacy Doc 10 summary)
- Commit: `2a05dc7 [VALIDATOR] Tier 1+2 evaluation — Case_03 unified matrix (3 frameworks, Block G)`

---

## §6 Invariants Preserved

- ✅ Legacy `02_PHASE2_RULES/` **never modified** — verified byte-identical
- ✅ No corpus files modified (`00_METHODOLOGY/PREPROCESSING_by_domain/`)
- ✅ No Phase 1 or Phase 3 docs modified
- ✅ **No Effort/Cost/Timeline** in any card, table or workbook sheet
- ✅ Document IDs: `AEGIS-P2-RICH-*-CASE03` (parallel to legacy `AEGIS-P2-*`)
- ✅ Frontmatter status: ACTIVE on orchestration docs; legacy docs kept `status: DRAFT` (read-only)
- ✅ No AI RMF placeholder — 3 frameworks all ACTIVE
- ✅ Maturity TRIPLE (CSF + Privacy + AI RMF) per D11 Case_03
- ✅ DORA coverage via CSF subcats (per Case_03 SPEC §4.4, since DORA doesn't have a 1:1 NIST framework)

---

## §7 See Also

### Validation reports (9 in `validation/`)

| File | Lines | Purpose |
|------|------:|---------|
| `validation/LINT_REPORT_BEFORE.md` | 122 | Pre-Bloco lint baseline (Case_03-adapted) |
| `validation/SPRINT0_REPORT.md` | 151 | Bloco A coverage report |
| `validation/SPRINT1_REPORT.md` | 383 | Bloco B NI formalization report |
| `validation/SPRINT2_REPORT.md` | 329 | Bloco C Doc 13 unified matrix |
| `validation/SPRINT3_REPORT.md` | 289 | Bloco D/E catalog port + deprecation |
| `validation/SPRINT3_4_REPORT.md` | 493 | Bloco D 6 new columns |
| `validation/SPRINT5_REPORT.md` | 321 | Bloco F visualisations + Excel |
| `validation/VALIDATOR_SPRINT5.md` | 370 | Validator sub-agent verdict |
| `validation/VALIDATOR_BLOCOG.md` | 580+ | **Canonical** Validator Tier 1+2 report (PASS_WITH_FINDINGS) |

### Related folders

- Legacy Phase 2 (read-only): `../02_PHASE2_RULES_RICH/`
- Phase 1 Rich Mode (template precedent): `../01_PHASE1_CONTEXT_RICH/`
- Case_01 Rich Mode (template): `../../Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/`
- Case_02 Rich Mode (sibling): `../../Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/`
- Root methodology: `../../../00_METHODOLOGY/AGENTS.md`
- Branch strategy: `../../../00_METHODOLOGY/REFERENCE/branch_strategy.md`

---

## §8 Final Status (post Bloco G)

### Bloco dashboard

| Bloco | A | B | C | D | E | F | G | Validator |
|-------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:---------:|
| Status | ⚠ reused | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**8 of 8 complete** (Bloco A reused from Case_02).

### Total cards

| Artefact | Count | Document |
|----------|------:|----------|
| Obligations | 38 | Doc 08 |
| Goals (24 PG + 52 SG) | 76 | Doc 10 |
| Rules (38 CR + 40 BPR) | 78 | Doc 11 |
| Tensions | 7 | Doc 09 |
| **Total mappings (Doc 13 §3)** | **78** | Doc 13 |

### Total cells

| Metric | Value |
|--------|------:|
| Doc 13 unified matrix rows | 78 (CR + BPR) |
| Triple-maturity cells (3 per card × 78 cards) | 234 |
| Doc 11 fields per card | 18 |
| Doc 11 total cells (post-D) | 1,404 (78 × 18) |

### Total lines

| Group | Lines |
|-------|------:|
| Phase 2 legacy (08 + 09 + 10 + 11 = Rich copy) | 2,271 |
| Orchestration (README + PROJECT_STATE + RICH_VS_LEGACY + SPEC + 10b) | ~1,800 |
| Doc 13 unified matrix | ~2,800 |
| Validation reports (9) | ~2,900 |
| **Total Rich markdown** | **~9,800** |
| Legacy Phase 2 markdown (comparison) | 2,271 |

### Findings addressed (post Bloco G)

| ID | Severity | Description | Disposition |
|----|----------|-------------|-------------|
| FN-01 | LOW | Missing Bloco A commit on Case_03 branch | **ADDRESSED** by reference to Case_02 commit `c972048` (Crosswalk already ACTIVE) |
| FN-02 | LOW | Frozen IDs not enforced in Doc 13 | **ADDRESSED** by Bloco G fix |
| FN-03 | LOW | `ni_avg_rule_note` missing in frontmatter | **ADDRESSED** by Bloco G fix |
| FN-05 | LOW | §6.5 inventory missing | **ADDRESSED** by Bloco G fix |
| F-01 (legacy) | LOW | Doc 10 summary header "33 goals" contradicts table-row count (76) | **DOCUMENTED** in §4 (canonical = 76) |

All 5 Validator findings tracked and addressed/documented.

---

**End of README v1.0 — Phase 2 Rich Mode (Case_03) Bloco G final**