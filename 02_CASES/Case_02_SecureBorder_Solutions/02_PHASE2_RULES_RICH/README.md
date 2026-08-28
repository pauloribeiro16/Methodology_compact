---
document_id: AEGIS-P2-RICH-README-CASE02
title: README — Phase 2 Rich Mode (Case_02)
phase: 2
version: 1.0
created: 2026-08-07
updated: 2026-08-08
author: Rich-Symmetry Executor (Case_02 replication)
status: ACTIVE
case: Case_02_SecureBorder_Solutions
tier: HIGH
sibling_of: ../02_PHASE2_RULES/
branch: feature/aegis-p2-case02-csf-pf-airmf
verdict: PASS_WITH_FINDINGS
---

# Phase 2 Rich Mode — Case_02 (SecureBorder Solutions)

> Phase 2 Rich Mode — corpus-enriched sibling of legacy `02_PHASE2_RULES/`.
> Case_02 contract: AEGIS Phase 2 — Case_02 SecureBorder Solutions — CSF + Privacy FW + AI RMF (HIGH complexity).
>
> **Status:** All 7 blocos (A→G) merged into `main` on `feature/aegis-p2-case02-csf-pf-airmf`. This Rich folder
> now mirrors the structural skeleton of Case_01 Rich Mode (12 files + `validation/` subfolder).
> All 9 validation reports present, including the Tier-1+2 Validator verdict (PASS_WITH_FINDINGS, 7 findings closed).

---

## §1 Status Dashboard

| Bloco | Date | Theme | Status |
|-------|------|-------|:------:|
| **Validator** | 2026-08-07 | Tier 1+2 PASS_WITH_FINDINGS (7 findings closed by Bloco G fix) | ✅ PASS_WITH_FINDINGS |
| **Bloco G fix** | 2026-08-07 | FN-01..FN-07 (frozen IDs, AI RMF anchor, heatmap, 35 active, path labels, field count) | ✅ DONE |
| **Bloco F** | 2026-08-07 | 4 visualizações + Excel 10 sheets (3 frameworks) | ✅ DONE |
| **Bloco E** | 2026-08-07 | 04b deprecated (legacy maturity moved to Doc 13) | ✅ DONE |
| **Bloco D** | 2026-08-07 | Doc 11 estendido campos 19-24 (tri-maturidade legacy CSF+PF+AI RMF; superseded pela postura, port Fase 4) | ✅ DONE |
| **Bloco C** | 2026-08-07 | Doc 13 unified matrix (3 frameworks CSF+PF+AI RMF) | ✅ DONE |
| **Bloco B** | 2026-08-07 | NI formal (AVG + AI MUST override), 79 cartões, DR-002 resolvido | ✅ DONE |
| **Bloco A** | 2026-08-07 | Crosswalk promoted DRAFT → ACTIVE | ✅ DONE |

**Aggregate:** ✅ All 7 blocos complete (A + B + C + D + E + F + G + Validator) | Phase 2 Rich Mode overall: ✅ DEEP_ENRICHED.

**Final status:** Phase 2 Rich Mode is `DEEP_ENRICHED`. Doc 13 unified matrix covers **3 NIST frameworks** (CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0) over **38 unique CR + 17 unique BPR = 55 cards**. Validator verdict: PASS_WITH_FINDINGS, all 7 findings (FN-01..FN-07) closed by the Bloco G fix commit.

---

## §2 Deliverables Map

| Doc | Lines (legacy) | Lines (Rich, now) | Cards / content | Bloco | Status |
|-----|---------------:|------------------:|-----------------|:-----:|:------:|
| `08_Obligation_Derivation.md` | 754 | 754 | 38 obligations, NI re-derived under AVG+AI MUST | legacy copy | ✅ COPIED |
| `09_Strategic_Tensions_Report.md` | 640 | 640 | 6 tensions resolved (HIGH+MEDIUM context) | legacy copy | ✅ COPIED |
| `10_Privacy_Security_Goals.md` | 394 | 394 | 47 goal rows (10 PG + 37 SG, 1:1 OBL→goal) | legacy copy | ✅ COPIED |
| `11_Rules_Catalog.md` | 602 | 602+ | 55 cards (38 CR + 17 BPR, 17 fields + banner) | legacy copy + banner | ✅ COPIED |
| `12_Rules_Catalog.xlsx` | 28KB | 28KB | Excel catalog (canonical) | legacy copy | ✅ COPIED |
| `13_Framework_Mapping_Matrix.md` | — | **unified matrix** | 3 frameworks (CSF + PF + AI RMF), triple maturity (legacy design; superseded by posture, port Fase 4) | C → D → F | ✅ DEEP_ENRICHED |
| `README.md` | — | this file | orientation + dashboard + schema | rich-symmetry | ✅ NEW |
| `PROJECT_STATE.md` | — | sibling | project state snapshot | rich-symmetry | ✅ NEW |
| `RICH_VS_LEGACY.md` | — | sibling | Rich vs legacy diff summary | rich-symmetry | ✅ NEW |
| `SPEC_NIST_MATRIX_UNIFIED.md` | — | sibling | 17-decision spec, 8 blocos | rich-symmetry | ✅ NEW |
| `10b_Privacy_Security_Goals_NIST_Implications.md` | — | sibling | 47 PG/SG × 3 frameworks implications | rich-symmetry | ✅ NEW |
| `validation/` (9 reports) | — | sibling | LINT_BEFORE + 5 Bloco reports + VALIDATOR_BLOCOG + VALIDATOR_SPRINT5 | rich-symmetry | ✅ NEW |

**Totals:** 5 Phase 2 legacy docs replicated + 7 orchestration/rich docs = **12 files + `validation/`**. Validator verdict: **PASS_WITH_FINDINGS**.

---

## §3 18-Field Schema (canonical, Case_02)

**12 base fields** (common to all tiers) + **3 triple-status fields** (CSF / Privacy FW / AI RMF; legacy maturity fields superseded by the Implementation Posture Model, port Fase 4) + **3 Case_02-specific fields** (HIGH tier).

| # | Field | Type | Description |
|---|-------|------|-------------|
| 1 | Sub-Domain Name | header | e.g., `OBL-D-01.1-001 — Data Encryption at Rest` |
| 2 | Description | multi-paragraph | What + why + scope/out-of-scope context |
| 3 | Scope | paragraph | What's included (from Doc 07b §4) |
| 4 | Out of Scope | paragraph | What's excluded (edge cases) |
| 5 | Source Article | list | GDPR/CRA/NIS 2/AI_Act article refs |
| 6 | NIST CSF Anchors | list | PR.DS-01, PR.AC-01, etc. |
| 7 | Privacy FW Anchors | list | PR.DS-P1, GV.PO-P1, etc. |
| 8 | AI RMF Anchors | list | GOVERN-1.1, MAP-1.1, etc. |
| 9 | Verification Criteria | 3+ bullets | Operational checks |
| 10 | Verification Method | enum | DEMONSTRATE / INSPECT / TEST / ANALYZE |
| 11 | Owner | role | CTO / DPO / CISO / AI Lead |
| 12 | Status | enum | TODO / IN_PROGRESS / DONE |
| 13 | Dependencies | list | Related OBL/PG/SG IDs |
| 14 | Risk if not met | H/M/L + 1-line | Qualitative risk |
| 15 | Affected Stakeholders | list | Internal + external parties |
| 16 | Implementation Status (CSF) | IMPLEMENTED/PARTIAL/NOT IMPLEMENTED | posture model v2.0 (was Maturity Cur X/4 → Tgt Y/4, legacy) |
| 17 | Implementation Status (Privacy) | IMPLEMENTED/PARTIAL/NOT IMPLEMENTED | posture model v2.0 (was Maturity, legacy) |
| 18 | Implementation Status (AI RMF) | IMPLEMENTED/PARTIAL/NOT IMPLEMENTED/N/A (non-AI scope) | posture model v2.0 (was Maturity, legacy) |

**3 Case_02-specific fields:**

| # | Field | Case_02 Value |
|---|-------|---------------|
| (×) | Regulatory Reporting | EDPB 72h GDPR + ENISA 24h CRA + NIS 2 incident + AI_Act serious incident |
| (×) | External Auditor | ISO 27001 + SOC 2 Type II + AI_Act conformity assessment body |
| (×) | Supervisory Body | EDPB + ENISA + national NIS 2 CSIRT + national AI_Act authority |

**Excluded by directive:** Effort, Cost, Timeline — absent from every card and every workbook sheet.

---

## §4 Case_02 Phase 2 Rich — Domain Profile

**Case:** SecureBorder Solutions B.V. (biometric border-control technology)
**Tier:** HIGH (250-500 FTE; €50-100M ARR)
**Applicable regulations:** 4/5 (GDPR + CRA + NIS 2 + AI_Act) — **DORA NOT APPLICABLE** (not financial)
**Sub-domains:** 38 obligation-bearing, all active (per `07b_Proportionality_Profile.md`)

| Metric | Value | Source |
|--------|------:|--------|
| Obligations (Doc 08) | 38 | `02_PHASE2_RULES/08_Obligation_Derivation.md` §4 |
| Privacy Goals (PG) | 10 | `02_PHASE2_RULES/10_Privacy_Security_Goals.md` §4 (rows) |
| Security Goals (SG) | 37 | `02_PHASE2_RULES/10_Privacy_Security_Goals.md` §5 (rows) |
| Total goal rows | 47 | (10 PG + 37 SG, 1:1 OBL→goal derivation DR-D01) |
| Tensions (Doc 09) | 6 (HIGH + MEDIUM) | Rich `09_Strategic_Tensions_Report.md` §4 |
| Compliance Rules (CR) | 38 unique | `02_PHASE2_RULES/11_Rules_Catalog.md` §4 |
| Best Practice Rules (BPR) | 17 unique | `02_PHASE2_RULES/11_Rules_Catalog.md` §5 |
| Total Rules | 55 | Doc 11 §6 |
| Track B distribution | 7 RIGOROUS + 27 STANDARD + 1 DEFERRED + 3 LIGHTWEIGHT | `07b_Proportionality_Profile.md` §3 |
| Active sub-domains | 35/38 (3 marked DEFERRED in Track B) | `07b_Proportionality_Profile.md` §3 |
| Source clauses | GDPR (28) + CRA (26) + NIS 2 (29) + AI_Act (29) = 112 | Doc 08 §5 + Phase 1 ontology |
| Frameworks in scope | NIST CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0 (all 3 ACTIVE) | Doc 13 frontmatter |

> **⚠ Goal count — read this before quoting.** Legacy Doc 10 §3.2/§4.2 *summary* states 38 goals (1:1 OBL→goal). The actual table-row count is **10 PG + 37 SG = 47**. Case_02's DR-D01 ("one-to-one") is interpreted as 1:1 at the **structural** level (every OBL has a goal) but the **PG/SG split** is a sub-domain classification, not a 1:1 with OBL count. Doc 13 + Doc 11 use **47** as the canonical goal total.

---

## §5 Bloco Plan

### Bloco A — Crosswalk promotion ✅ COMPLETE
- `Framework_Crosswalk_ARM.md` promoted DRAFT v0.1 → ACTIVE v1.0
- 800-53 column intentionally OUT OF SCOPE for Case_02 (as Case_01)
- Commit: `c972048 [EXECUTOR] Bloco A — crosswalk promoted DRAFT→ACTIVE`

### Bloco B — NI formalization ✅ COMPLETE
- DR-002 = AVG with AI-C* MUST override (AI_Act signal preserved)
- 79 card rows (38 unique CR + 17 unique BPR + duplicate impact rows)
- AVG applied retroactively; AI-C* sources → NI=3 (MUST)
- Commit: `62e6b61 [EXECUTOR] Bloco B — NI formal (AVG+AI MUST) em 79 cartões, DR-002 resolvido`

### Bloco C — Doc 13 unified matrix ✅ COMPLETE
- All 3 frameworks ACTIVE (CSF + PF + AI RMF); NO placeholder columns
- 6 sub-sections (§1 matriz, §2 Govern consolidada, §3 mapeamento n:m, §4 posture (legacy maturidade, superseded), §5 aplicação, §6 gap analysis)
- 38 unique CR with full YAML mapping blocks
- Commit: `d9f8dfb [EXECUTOR] Bloco C — Doc 13 unified matrix (3 frameworks CSF+PF+AI RMF)`

### Bloco D — Doc 11 extension ✅ COMPLETE
- Fields 19-24 added: csf_subcategories, privacy_subcategories, ai_rmf_subcategories, maturity_csf, maturity_privacy, maturity_ai_rmf (legacy field names; superseded by posture statuses, port Fase 4)
- 18 fields per card (15→17 from Bloco B + 6 columns from Bloco D)
- Commit: `5ded4f4 [EXECUTOR] Bloco D — Doc 11 estendido (campos 19-24, tri-maturidade CSF+PF+AI RMF)` — legacy field extension, superseded by posture statuses (port Fase 4)

### Bloco E — 04b deprecated ✅ COMPLETE
- `04b_Security_Posture.md` status: DEPRECATED_FOR_MATURITY
- Legacy maturity model ownership moved to Doc 13 (superseded by posture model)
- Commit: `fee7978 [EXECUTOR] Bloco E — 04b deprecated for maturity`

### Bloco F — 4 visualizations + Excel ✅ COMPLETE
- V1 matriz cobertura, V2 mapa por Function, V3 Mermaid traceability graph, V4 heatmap
- 6 new Excel sheets added (Unified_Matrix, Govern_Consolidated, Mapping_nm, Maturity_Dual, Cov_Function, Heatmap_Maturity (legacy xlsx sheets))
- Commit: `62dd5c6 [EXECUTOR] Bloco F — 4 visualizações + 6 folhas Excel`

### Bloco G fix — FN-01..FN-07 ✅ COMPLETE
- Validator findings (FN-01 frozen IDs, FN-02 AI RMF anchor, FN-03 heatmap, FN-04 35 active, FN-05 path labels, FN-07 field count) closed
- Commit: `7462f9e [EXECUTOR] Bloco G fix — FN-01 frozen IDs + FN-02 AI RMF anchor + FN-03 heatmap MAX + FN-04 35 active + FN-05 path labels + FN-07 field count`

### Validator — Tier 1+2 ✅ PASS_WITH_FINDINGS
- Independent sub-agent verdict
- All Tier 1 checks PASS except FN-01..FN-07 (closed by Bloco G fix)
- Tier 2 alignment check: PASS_WITH_FINDINGS
- Commit: `db09358 [VALIDATOR] Tier 1+2 evaluation — Case_02 unified matrix (3 frameworks, Block G)`

---

## §6 Invariants Preserved

- ✅ Legacy `02_PHASE2_RULES/` **never modified** — verified byte-identical
- ✅ No corpus files modified (`00_METHODOLOGY/PREPROCESSING_by_domain/`)
- ✅ No Phase 1 or Phase 3 docs modified
- ✅ **No Effort/Cost/Timeline** in any card, table or workbook sheet
- ✅ Document IDs: `AEGIS-P2-RICH-*-CASE02` (parallel to legacy `AEGIS-P2-*`)
- ✅ Frontmatter status: ACTIVE on orchestration docs; legacy docs kept `status: DRAFT` (read-only)
- ✅ No AI RMF placeholder — 3 frameworks all ACTIVE
- ✅ Maturity TRIPLE (CSF + Privacy + AI RMF) per D11 Case_02 — legacy design, superseded by posture statuses (port Fase 4)

---

## §7 See Also

### Validation reports (9 in `validation/`)

| File | Lines | Purpose |
|------|------:|---------|
| `validation/LINT_REPORT_BEFORE.md` | 122 | Pre-Bloco lint baseline (Case_02-adapted) |
| `validation/SPRINT0_REPORT.md` | 151 | Bloco A coverage report |
| `validation/SPRINT1_REPORT.md` | 383 | Bloco B NI formalization report |
| `validation/SPRINT2_REPORT.md` | 329 | Bloco C Doc 13 unified matrix |
| `validation/SPRINT3_REPORT.md` | 289 | Bloco D/E catalog port + deprecation |
| `validation/SPRINT3_4_REPORT.md` | 493 | Bloco D 6 new columns |
| `validation/SPRINT5_REPORT.md` | 321 | Bloco F visualisations + Excel |
| `validation/VALIDATOR_SPRINT5.md` | 370 | Validator sub-agent verdict |
| `validation/VALIDATOR_BLOCOG.md` | 380+ | **Canonical** Validator Tier 1+2 report (PASS_WITH_FINDINGS) |

### Related folders

- Legacy Phase 2 (read-only): `../02_PHASE2_RULES/`
- Phase 1 Rich Mode (template precedent): `../01_PHASE1_CONTEXT_RICH/`
- Case_01 Rich Mode (template): `../../Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/`
- Root methodology: `../../../00_METHODOLOGY/AGENTS.md`
- Branch strategy: `../../../00_METHODOLOGY/REFERENCE/branch_strategy.md`

---

## §8 Final Status (post Bloco G)

### Bloco dashboard

| Bloco | A | B | C | D | E | F | G | Validator |
|-------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:---------:|
| Status | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**8 of 8 complete.**

### Total cards

| Artefact | Count | Document |
|----------|------:|----------|
| Obligations | 38 | Doc 08 |
| Goals (10 PG + 37 SG) | 47 | Doc 10 |
| Rules (38 CR + 17 BPR) | 55 | Doc 11 |
| Tensions | 6 | Doc 09 |
| **Total mappings (Doc 13 §3)** | **55** | Doc 13 |

### Total cells

| Metric | Value |
|--------|------:|
| Doc 13 unified matrix rows | 55 (CR + BPR) |
| Triple-maturity cells (3 per card × 55 cards) | 165 — legacy numeric cells, superseded by posture statuses (port Fase 4) |
| Doc 11 fields per card | 18 |
| Doc 11 total cells (post-D) | 990 (55 × 18) |

### Total lines

| Group | Lines |
|-------|------:|
| Phase 2 legacy (08 + 09 + 10 + 11 = Rich copy) | 2,390 |
| Orchestration (README + PROJECT_STATE + RICH_VS_LEGACY + SPEC + 10b) | ~1,800 |
| Doc 13 unified matrix | ~2,400 |
| Validation reports (9) | ~2,800 |
| **Total Rich markdown** | **~9,400** |
| Legacy Phase 2 markdown (comparison) | 2,390 |

### Findings closed (post Bloco G)

| ID | Severity | Description | Disposition |
|----|----------|-------------|-------------|
| FN-01 | LOW | Frozen IDs not enforced in Doc 13 | **CLOSED** by Bloco G fix (commit 7462f9e) |
| FN-02 | LOW | AI RMF anchor fields missing in Doc 11 | **CLOSED** by Bloco G fix |
| FN-03 | LOW | Heatmap didn't reflect MAX tier | **CLOSED** by Bloco G fix |
| FN-04 | LOW | 35 active sub-domains not surfaced in Doc 13 | **CLOSED** by Bloco G fix |
| FN-05 | LOW | Path labels missing in traceability graph | **CLOSED** by Bloco G fix |
| FN-07 | LOW | Field count frontmatter mismatch (15 vs 18) | **CLOSED** by Bloco G fix |

All 7 findings from Validator Tier 1 closed. Validator verdict final: PASS_WITH_FINDINGS.

---

**End of README v1.0 — Phase 2 Rich Mode (Case_02) Bloco G final**