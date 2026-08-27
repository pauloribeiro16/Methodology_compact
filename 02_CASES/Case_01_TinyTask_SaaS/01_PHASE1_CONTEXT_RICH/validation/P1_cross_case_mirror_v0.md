# P1 Cross-Case Mirror v0 — Case_01 vs Case_02 vs Case_03

**Scope:** Comparative mirror of Phase 1 corpus across all 3 AEGIS cases. Goal: isolate (a) Case_01-specific drift, (b) transversal practice shared by all 3 cases, (c) universal drift (i.e. drift that is endemic to the methodology and present in every implementation).

**Method:** Read-only inventory + grep. Counts: `grep -cE`, `wc -l`. Verbatim `grep -rn "fluxdiagram" 02_CASES/<case>`. All paths absolute.

**Date:** 2026-08-27.

---

## 0. Anchoring (from cross-case governance docs)

From `02_CASES/GLOBAL_PROJECT_STATE.md` v6.3 (2026-08-24):

- All 3 cases: **Phase 1 Complete** (per §3.1 — 8/8 documents, lints passed for Case_01 only; Case_02/03 lints not run).
- Phase 2: Case_01 "Pending" (note: this contradicts `progress.json` which marks Case_01 `phase_2` complete — see triage §6 below), Case_02/03 complete.
- Phase 3: Case_01 complete 78.6% (v2.0) + Phase 3 RICH PASS_WITH_FINDINGS; Case_02 85.2%; Case_03 99.2%.
- Case_01 only: has a `03_PHASE3_DECOMPOSITION_RICH/` worktree validated in Sprint 5/6.

The `README.md` is structurally stale: it still lists `Case_02_Medium_Complexity` as the directory name (the directory was renamed to `Case_02_SecureBorder_Solutions` per `CHANGE_LOG_CENTRAL.md` 2026-04-03). Drift source: directory rename did not propagate to `02_CASES/README.md`.

---

## 1. Deliverable inventory per case (condensed)

Columns: classification, PURPOSE section present? (Y/N based on `^##\s+\d+\.\s+(DOCUMENT\s+)?PURPOSE`), goal linkage count (AG-D-/PG-D-/SG-D-/AO-D-), orphan / dangling refs.

Legend for classification:
- **FLOW-NATIVE** — present in methodology `fluxdiagram/phase1/` slot or naturally part of Phase 1 named flow.
- **JUSTIFIED-EXTENSION** — not in canonical 8-doc flow but defensible extension (e.g. Doc06 ThirdParty, Doc07 RACI, Doc09 Ambiguity).
- **ORPHAN** — neither part of named phase 1 flow nor justified extension (e.g. INTAKE_FORM, Corpus_Field_Map).
- **META-INFRA** — orchestration/validation artefacts (README, ontology, xlsx, validators).

### 1.1 Case_01_TinyTask_SaaS

| # | File | Classif. | Purpose? | AG- | AO- | PG- | SG- | Orphan refs |
|---|------|----------|----------|-----|-----|-----|-----|-------------|
| 01 | Doc01_Taxonomy_Reference.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | none |
| 02 | Doc02_INTAKE_FORM.md | ORPHAN (Sprint 1 stub-only) | Y | 0 | 0 | 0 | 0 | none |
| 03 | Doc03_Company_Context_Assessment.md | FLOW-NATIVE | Y | 5 | 0 | 1 | 1 | refs `Doc 07c_Adjusted_Goals` (legacy alias; replaced by Doc13) |
| 04 | Doc04_Architecture_DataInventory.md | FLOW-NATIVE | **N** | 0 | 0 | 0 | 0 | none |
| 05 | Doc05_Security_Posture.md | JUSTIFIED-EXTENSION (maturity lens) | **N** | 0 | 0 | 0 | 0 | none |
| 06 | Doc06_ThirdParty_Landscape.md | JUSTIFIED-EXTENSION | **N** | 0 | 0 | 0 | 0 | none |
| 07 | Doc07_Org_Roles_RACI.md | JUSTIFIED-EXTENSION (RACI lens) | **N** | 0 | 0 | 0 | 0 | none |
| 08 | Doc08_Regulatory_Applicability.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | refs `Doc 07c` §A.1.1 (legacy alias) |
| 09 | Doc09_Ambiguity_Register.md | JUSTIFIED-EXTENSION (ambiguity lens) | **N** | 0 | 0 | 0 | 0 | none |
| 10 | Doc10_Clause_Mapping_Matrix.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | none |
| 11 | Doc11_Structured_Compliance_Matrix.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | none |
| 12 | Doc12_Proportionality_Profile.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | none |
| 13 | Doc13_Adjusted_Goals.md | FLOW-NATIVE | **N** (§0 Document Purpose present but does not match strict regex) | **124** | 0 | 12 | 13 | refs Doc07c legacy alias throughout |
| — | README.md | META-INFRA | Y (own §1 Purpose) | 0 | 0 | 0 | 0 | n/a |
| — | PROJECT_STATE.md | META-INFRA | Y | 0 | 0 | 0 | 0 | n/a |
| — | phase1_ontology.yaml | META-INFRA | n/a | 3 | 0 | 0 | 0 | n/a |
| — | Citation_Index.md | META-INFRA | n/a | 0 | 0 | 0 | 0 | n/a |
| — | Corpus_Field_Map.md | META-INFRA | n/a | 0 | 0 | 0 | 0 | n/a |
| — | Case_01_Phase1_RICH.xlsx | META-INFRA | n/a | n/a | n/a | n/a | n/a | n/a |

Goal linkage totals (Doc01..Doc13 only): **AG=129, AO=0, PG=13, SG=14** — exclusively AG- prefix.

### 1.2 Case_02_SecureBorder_Solutions

| # | File | Classif. | Purpose? | AG- | AO- | PG- | SG- | Orphan refs |
|---|------|----------|----------|-----|-----|-----|-----|-------------|
| 01 | Doc01_Taxonomy_Reference.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | none |
| 02 | Doc02_INTAKE_FORM.md | ORPHAN | Y | 0 | 0 | 0 | 0 | none |
| 03 | Doc03_Company_Context_Assessment.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | none |
| 04 | Doc04_Architecture_DataInventory.md | FLOW-NATIVE | **N** | 0 | 0 | 0 | 0 | none |
| 05 | Doc05_Security_Posture.md | JUSTIFIED-EXTENSION | **N** | 0 | 0 | 0 | 0 | none |
| 06 | Doc06_ThirdParty_Landscape.md | JUSTIFIED-EXTENSION | **N** | 0 | 0 | 0 | 0 | none |
| 07 | Doc07_Org_Roles_RACI.md | JUSTIFIED-EXTENSION | **N** | 0 | 0 | 0 | 0 | none |
| 08 | Doc08_Regulatory_Applicability.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | none |
| 09 | Doc09_Ambiguity_Register.md | JUSTIFIED-EXTENSION | **N** | 0 | 0 | 0 | 0 | none |
| 10 | Doc10_Clause_Mapping_Matrix.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | none |
| 11 | Doc11_Structured_Compliance_Matrix.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | refs to PG/SG (3 + 3) — these are inside the doc body, not separate count above |
| 12 | Doc12_Proportionality_Profile.md | FLOW-NATIVE | **N** | 0 | 0 | 0 | 0 | none |
| 13 | Doc13_Adjusted_Objectives.md | FLOW-NATIVE (RENAME: Adjusted_Goals → Adjusted_Objectives) | **N** | 0 | 0 | **70** | **71** | none |
| — | README.md | META-INFRA | Y (own `## Purpose`) | 0 | 0 | 0 | 0 | n/a |
| — | PROJECT_STATE.md | META-INFRA | Y | 0 | 0 | 0 | 0 | n/a |
| — | phase1_ontology.yaml | META-INFRA | n/a | 3 | 0 | 0 | 0 | n/a |
| — | Citation_Index.md | META-INFRA | n/a | 0 | 0 | 0 | 0 | n/a |
| — | Corpus_Field_Map.md | META-INFRA | n/a | 0 | 0 | 0 | 0 | n/a |
| — | RICH_VS_LEGACY.md | META-INFRA | Y | 0 | 0 | 0 | 0 | n/a |
| — | Case_02_Phase1_RICH.xlsx | META-INFRA | n/a | n/a | n/a | n/a | n/a | n/a |

Goal linkage totals: **AG=3 (all in phase1_ontology.yaml), AO=0, PG=73 (3 in Doc11 + 70 in Doc13), SG=74**. **No AG-D-** prefix is used as a goal ID anywhere in Case_02.

### 1.3 Case_03_OmniBank_Financial

| # | File | Classif. | Purpose? | AG- | AO- | PG- | SG- | Orphan refs |
|---|------|----------|----------|-----|-----|-----|-----|-------------|
| 01 | Doc01_Taxonomy_Reference.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | none |
| 02 | Doc02_INTAKE_FORM.md | ORPHAN | Y | 0 | 0 | 0 | 0 | none |
| 03 | Doc03_Company_Context_Assessment.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | none |
| 04 | Doc04_Architecture_DataInventory.md | FLOW-NATIVE | **N** | 0 | 0 | 0 | 0 | none |
| 05 | Doc05_Security_Posture.md | JUSTIFIED-EXTENSION | **N** | 0 | 0 | 0 | 0 | none |
| 06 | Doc06_ThirdParty_Landscape.md | JUSTIFIED-EXTENSION | **N** | 0 | 0 | 0 | 0 | none |
| 07 | Doc07_Org_Roles_RACI.md | JUSTIFIED-EXTENSION | **N** | 0 | 0 | 0 | 0 | none |
| 08 | Doc08_Regulatory_Applicability.md | FLOW-NATIVE | Y | 0 | 0 | 0 | 0 | none |
| 09 | Doc09_Ambiguity_Register.md | JUSTIFIED-EXTENSION | **N** | 0 | 0 | 0 | 0 | none |
| 10 | Doc10_Clause_Mapping_Matrix.md | FLOW-NATIVE | **N** | 0 | 0 | 0 | 0 | none |
| 11 | Doc11_DORA_ICT_Risk_Framework.md | **JUSTIFIED-EXTENSION** (DORA-specific annex; this is the +1 vs Case_01/02) | **N** | 0 | 0 | 0 | 0 | none |
| 12 | Doc12_Structured_Compliance_Matrix.md | FLOW-NATIVE (slot-shifted +1) | Y | 6 | 0 | 0 | 0 | none |
| 13 | Doc13_Proportionality_Profile.md | FLOW-NATIVE (slot-shifted +1) | **N** | 0 | 0 | 0 | 0 | none |
| 14 | Doc14_Adjusted_Goals.md | FLOW-NATIVE (slot-shifted +1) | **N** (uses `## §0 Document Purpose` header — non-canonical format) | **42** | 0 | 0 | 0 | legacy appendix `_deprecated/Doc15_Appendix_A_OLD.md` (242 hits) |
| — | README.md | META-INFRA | Y (own `## 1. Purpose`) | 0 | 0 | 0 | 0 | n/a |
| — | PROJECT_STATE.md | META-INFRA | Y | 0 | 0 | 0 | 0 | n/a |
| — | phase1_ontology.yaml | META-INFRA | n/a | 0 | 0 | 0 | 0 | n/a |
| — | Citation_Index.md | META-INFRA | n/a | 0 | 0 | 0 | 0 | n/a |
| — | Corpus_Field_Map.md | META-INFRA | n/a | 0 | 0 | 0 | 0 | n/a |
| — | RICH_VS_LEGACY.md | META-INFRA | Y | 0 | 0 | 0 | 0 | n/a |
| — | Case_03_Phase1_RICH.xlsx | META-INFRA | n/a | n/a | n/a | n/a | n/a | n/a |

Goal linkage totals: **AG=48 (6 in Doc12 + 42 in Doc14), AO=0, PG=0, SG=0** — uses **AG-D-** prefix exclusively (matches Case_01, not Case_02).

Note: the brief asks "AG-D- or AO-D- as goal prefix". The honest finding is **AO-D- is unused everywhere**. The split is between Case_01+03 (AG- unified) vs Case_02 (PG/SG split).

---

## 2. Per-case answers to the specific checks

### 2.1 PRODUCTION_FLOW.md or equivalent? + mermaid blocks

`find` for `*PRODUCTION_FLOW*` and `*flow*` in `01_PHASE1_CONTEXT_RICH/`: **0 hits in all 3 cases**. The Case_01 phase 1 README documents "Phase 1 Documents (14 files)" but there is no separate PRODUCTION_FLOW artefact.

`grep -cE "^\`\`\`mermaid"` per case dir:
- Case_01: **0**
- Case_02: **0**
- Case_03: **0**

All Phase 1 RICH docs are pure prose. Visualisation of the Phase 1 flow exists **only** under `00_METHODOLOGY/diagrams/fluxdiagram/phase1/` (7 `.md` files) — these are methodology-level, not case-level.

### 2.2 References to `00_METHODOLOGY/diagrams/fluxdiagram/phase1/`

`grep -rn "fluxdiagram" 02_CASES/<case>` — verbatim counts:
- Case_01: **0**
- Case_02: **0**
- Case_03: **0**

The only `fluxdiagram` occurrences in `02_CASES/` are in `GLOBAL_PROJECT_STATE.md` (methodology-level summary line) and in `Case_01/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` (3 hits in the ontology header). None of the Phase 1 doc bodies in any case cite the fluxdiagram path. **Universal drift.**

### 2.3 progress.json — `phase_1_rich` / `phase_1` entries

All 3 progress.json files use the key `phase_1` (not `phase_1_rich`). Case_01 additionally has a `phase_3_rich` entry (not phase 1). Statuses:

| Case | phase_1.status | gate | completed_at | notes |
|------|----------------|------|--------------|-------|
| Case_01 | `complete` | `P1_PASS` | 2026-04-01 | Lists 4 docs (04,05,06,07) — note: Doc06 with `lint_06_clause_mapping.py` here, conflicts with Case_02/03 `_notes` saying "no lint script for .xlsx". |
| Case_02 | `complete` | `P1_PASS` | 2026-04-01 | Lists 3 docs (04,05,07). `_notes`: "06_Clause_Mapping_Matrix.xlsx present but no lint script available for .xlsx" |
| Case_03 | `complete` | `P1_PASS` | 2026-04-01 | Lists 3 docs (04,05,07). Same `_notes` as Case_02. |

**Inconsistency (transversal drift):** Case_01 progress.json claims `06_Clause_Mapping_Matrix` was linted; Case_02 and Case_03 explicitly disclaim this. Either Case_01 has a hidden lint script or its progress.json is incorrect.

### 2.4 AG- or AO- as goal prefix

Goal IDs of the form `\bAG-D-` and `\bAO-D-` (word-bounded) per case (Doc01..Doc14 only):

| Case | AG-D- count | AO-D- count | Other prefixes used |
|------|-------------|-------------|---------------------|
| Case_01 | **129** | **0** | PG- (13), SG- (14) |
| Case_02 | **0** | **0** | PG- (73), SG- (74) |
| Case_03 | **48** | **0** | (none — AG-unified) |

**AO-D- is zero everywhere.** Methodology intent (per AGENTS.md / corr-010 standardisation note in Case_03) appears to have settled on **AG-D-** (Adjusted Goals) as the unified prefix, but Case_02 was never migrated to AG-. **Transversal drift** (Case_02 lagged).

### 2.5 RACI / inventário / maturidade / third-party / ambiguidade presence

File-level counts (`grep -liE` per case, Doc*.md only):

| Theme | Case_01 | Case_02 | Case_03 |
|-------|---------|---------|---------|
| RACI | 4 files | 4 files | 8 files |
| Maturidade/maturity | 9 files | 8 files | 10 files |
| Third-party | 11 files | 11 files | 14 files |
| Ambiguidade/ambiguity | 3 files | 3 files | 7 files |

**All themes are present in all 3 cases.** RACI, third-party and ambiguity are each anchored in a single dedicated Doc (Doc07, Doc06, Doc09 respectively) but are cross-referenced from other docs (Doc08 cites maturity in Case_01; Doc12 in Case_03 cites maturity multiple times).

**Goal-references from these "lens" docs:**
- Case_01: Doc03 (Company Context) cites **AG-/PG-/SG-** directly in BG-01..BG-05. Doc05/Doc06/Doc07/Doc09 themselves contain zero goal-ID refs — they are content sources, not goal consumers. **Universal drift: only Doc03 (and Doc13) anchor goals; the lens docs are isolated.**
- Case_02: **No goal-ID refs anywhere in Doc03, Doc05, Doc06, Doc07, Doc09.** The lens docs are completely decoupled from Doc13 goal IDs. **Transversal drift.**
- Case_03: Doc12_Structured_Compliance_Matrix has 6 AG-D- refs. Doc14 has 42 AG-D- refs. Lens docs (Doc05-09) carry zero goal refs. **Same pattern as Case_01: lens docs isolated.**

---

## 3. Cross-case comparison table (13 doc slots)

Canonical 13 slots from Case_01 (Doc01..Doc13). For Case_03 the table maps by *content role*, not slot number (Case_03 inserts Doc11_DORA_ICT_Risk_Framework and shifts Doc12/Doc13 down by one slot).

Cell notation: `✓ file | goal-link | dangling-refs`.

| Slot | Role | Case_01 | Case_02 | Case_03 (slot-shift) |
|------|------|---------|---------|----------------------|
| 01 | Taxonomy Reference | Doc01 ✓ \| 0 \| none | Doc01 ✓ \| 0 \| none | Doc01 ✓ \| 0 \| none |
| 02 | Intake Form (orphan) | Doc02 ✓ \| 0 \| none | Doc02 ✓ \| 0 \| none | Doc02 ✓ \| 0 \| none |
| 03 | Company Context Assessment | Doc03 ✓ \| **AG=5, PG=1, SG=1** \| legacy Doc07c alias | Doc03 ✓ \| 0 \| none | Doc03 ✓ \| 0 \| none |
| 04 | Architecture / Data Inventory | Doc04 (no purpose) \| 0 \| none | Doc04 (no purpose) \| 0 \| none | Doc04 (no purpose) \| 0 \| none |
| 05 | Security Posture (maturity) | Doc05 (no purpose) \| 0 \| none | Doc05 (no purpose) \| 0 \| none | Doc05 (no purpose) \| 0 \| none |
| 06 | Third-Party Landscape | Doc06 (no purpose) \| 0 \| none | Doc06 (no purpose) \| 0 \| none | Doc06 (no purpose) \| 0 \| none |
| 07 | Org Roles / RACI | Doc07 (no purpose) \| 0 \| none | Doc07 (no purpose) \| 0 \| none | Doc07 (no purpose) \| 0 \| none |
| 08 | Regulatory Applicability | Doc08 ✓ \| 0 \| legacy Doc07c alias | Doc08 ✓ \| 0 \| none | Doc08 ✓ \| 0 \| none |
| 09 | Ambiguity Register | Doc09 (no purpose) \| 0 \| none | Doc09 (no purpose) \| 0 \| none | Doc09 (no purpose) \| 0 \| none |
| 10 | Clause Mapping Matrix | Doc10 ✓ \| 0 \| none | Doc10 ✓ \| 0 \| none | Doc10 **(no purpose)** \| 0 \| none |
| 11 | Structured Compliance Matrix | Doc11 ✓ \| 0 \| none | Doc11 ✓ \| **PG=3, SG=3** \| none | Doc11_DORA_ICT_Risk_Framework **(no purpose)** \| 0 \| none |
| 12 | Proportionality Profile | Doc12 ✓ \| 0 \| none | Doc12 **(no purpose)** \| 0 \| none | Doc12_Structured_Compliance_Matrix ✓ \| **AG=6** \| none |
| 13 | Adjusted Goals / Objectives | Doc13_Adjusted_Goals (§0 Doc Purpose non-canonical) \| **AG=124, PG=12, SG=13** \| legacy Doc07c alias throughout | Doc13_Adjusted_Objectives **(no purpose)** \| **PG=70, SG=71** \| none | Doc13_Proportionality_Profile (§1 Doc Purpose non-canonical) \| 0 \| none |
| 14 | (Case_03 only) Adjusted Goals | n/a | n/a | Doc14_Adjusted_Goals (§0 Doc Purpose) \| **AG=42** \| legacy Doc15 alias in `_deprecated/` |

**Universal findings (all 3 cases):**
- Same 13 doc roles in all cases (Case_03 adds +1: Doc11_DORA_ICT_Risk_Framework, inserted before Structured Compliance Matrix).
- Doc04, Doc05, Doc06, Doc07, Doc09 **never** carry a `^## \d+\. PURPOSE` heading in any case.
- Doc13/14 (Adjusted Goals) is the only doc that anchors goal IDs in quantity.
- Doc03 has goal refs only in Case_01 (not in Case_02/03).

---

## 4. Triage — Case_01-specific vs transversal vs universal

### 4.1 Case_01-specific drift

1. **Sprint artifacts (sprint5_report / SPRINT1..5_REPORT, VALIDATOR_*, P1_*_validation.md, CORPUS_AUGMENTATION_REPORT, FIX_TIER1_REPORT, LINT_REPORT_*, data/phase1_graph.json, scripts/build_p1_graph.py).** No equivalent in Case_02/03 `validation/` dirs (Case_02/03 `validation/` dirs do exist but contain a different minimal set: VALIDATOR_TIER1/2, VALIDATOR_SPRINT5). Only Case_01 has the full P1 dashboard + graph + ontology validation lineage.
2. **Legacy Doc07c alias.** `Doc03` and `Doc08` of Case_01 cite `Doc 07c_Adjusted_Goals` (legacy alias) — Case_02/03 do not have this alias pattern. Drift: Case_01 doc body was not fully migrated to Doc13 naming after the 13-doc re-numbering.
3. **`phase_3_rich` block in progress.json.** Unique to Case_01 (Sprint 6 PASS_WITH_FINDINGS).
4. **Doc03 has goal cross-refs.** Only Case_01's Doc03 carries AG-/PG-/SG- anchors; Case_02/03 Doc03 are pure prose.

### 4.2 Transversal drift (methodology-level gap)

1. **No `00_METHODOLOGY/diagrams/fluxdiagram/phase1/` references inside any case.** The fluxdiagram is methodology-level but no Phase 1 doc cites it. None of the 3 cases embed a mermaid block. The "production flow" narrative is not traceable from case docs to methodology docs. **This is a methodology gap, not a case gap.**
2. **No `AO-D-` prefix anywhere.** Methodology intent (or at least the brief's mental model) mentions AO (Adjusted Objectives) — but no case uses it. Case_02 uses PG/SG, Case_01/03 use AG. **AO is documented nowhere in any case.**
3. **Doc13 slot + naming inconsistency.** Case_01/03 call the slot 13 (or 14) "Adjusted_Goals"; Case_02 calls it "Adjusted_Objectives". All three should align on `Adjusted_Goals` per corr-010 standardisation (per Case_03 README §6 note) but Case_02 was never renamed.
4. **Lens docs (Doc05/06/07/09) never cite goal IDs.** Across all 3 cases, the maturity / third-party / RACI / ambiguity lenses do not anchor to AG-/PG-/SG- IDs. Methodology gap: no rule forces these "input lens" docs to produce goal-bindable artefacts.
5. **Doc10 Clause_Mapping_Matrix — purpose-section drift.** Case_01/02 have it; Case_03 lacks it (Case_03 Doc10 is the same role but no PURPOSE heading).
6. **progress.json schema mismatch.** All 3 cases use `phase_1` key, but Case_01 has an extra `phase_3_rich`. There is no `phase_1_rich` even though Phase 1 has a RICH corpus (the README distinguishes "14 files" — i.e. RICH).
7. **Case_01 progress.json falsely claims Doc06 linted** while Case_02/03 explicitly disclaim this — one of the three is wrong.

### 4.3 Universal drift (endemic across all 3 cases)

1. **Purpose-section absence on Doc04, Doc05, Doc06, Doc07, Doc09.** Same 5 doc slots lack the canonical `^## \d+\. (DOCUMENT )?PURPOSE` heading in all 3 cases. (Doc13/14 uses `## §0 Document Purpose` / `## §1 Document Purpose` — non-canonical format that doesn't match the numeric regex, but the prose does exist.)
2. **Doc02 INTAKE_FORM classification as orphan.** All 3 cases include this doc, but it is not in the canonical Phase 1 named flow (`phase1_contextual_definition.md` slot a/b/c). It is a methodology-level questionnaire that has no clear home in the case-level phase 1 flow.
3. **No mermaid / no PRODUCTION_FLOW in any case.** The "Phase 1 production flow" is documented only at the methodology level; no case localises it.
4. **Lens docs (Doc05 maturity / Doc06 third-party / Doc07 RACI / Doc09 ambiguity) have no `goal_ref` slot in any case.** The methodology defines these lenses but doesn't bind them to the goal taxonomy.
5. **Citation_Index.md and Corpus_Field_Map.md exist in all 3 cases but never cross-link to goal IDs.** They are bookkeeping, not goal-aware.
6. **`02_CASES/README.md` is structurally stale** (lists `Case_02_Medium_Complexity` which was renamed 2026-04-03).

---

## 5. Concrete recommendations

1. **Universal: enforce purpose-section template** (e.g. via doc-conventions skill lint) on Doc04, Doc05, Doc06, Doc07, Doc09 — all 3 cases. This is the single highest-leverage, lowest-cost fix.
2. **Transversal: decide AG vs PG/SG once and migrate.** Either rename Case_02 Doc13 to `Adjusted_Goals.md` and add AG- IDs (matching corr-010), or re-introduce PG/SG in Case_01/03. The brief asks about `AO-` but AO is unused everywhere — either drop the AO intent from the prompt layer or instantiate it.
3. **Transversal: add a single Phase 1 mermaid / fluxdiagram embed** in each case's `README.md` (point to `00_METHODOLOGY/diagrams/fluxdiagram/phase1/phase1_contextual_definition.md`). Closes the "no fluxdiagram ref" gap.
4. **Case_01-specific: replace Doc07c legacy alias** in Doc03 (5 occurrences) and Doc08 (Sprint 5 banner) with Doc13. Tiny edit, high signal.
5. **Case_01-specific: reconcile progress.json phase_1** Doc06 entry vs Case_02/03 `_notes` (which say "no lint script for .xlsx"). Either document the missing lint script for all 3 cases or remove Case_01's false-positive lint_passed.
6. **Universal: link Doc05/06/07/09 lens outputs to goal IDs** — either by adding a `related_goals:` block to each doc's frontmatter or by emitting a small table in each doc. Currently the lens docs are detached from the goal taxonomy.
7. **Universal: add a Phase 1 PRODUCTION_FLOW.md** in each case (or a single one in `00_METHODOLOGY/` that all cases point to) that localises `fluxdiagram/phase1/phase1_contextual_definition.md` with case-specific doc IDs.

---

## 6. Appendix — raw counts

Doc count per case in `01_PHASE1_CONTEXT_RICH/` (`.md` only):
- Case_01: 17 (13 Doc*.md + README, PROJECT_STATE, Citation_Index, Corpus_Field_Map)
- Case_02: 18 (13 Doc*.md + README, PROJECT_STATE, Citation_Index, Corpus_Field_Map, RICH_VS_LEGACY)
- Case_03: 19 (14 Doc*.md + README, PROJECT_STATE, Citation_Index, Corpus_Field_Map, RICH_VS_LEGACY)

plus 3 orchestration files in each (xlsx, phase1_ontology.yaml, +Case_01 also has data/, scripts/, gui-test-screenshots/, validation/).

`phase_1_rich` key in any progress.json: **0** (all use `phase_1`).
`AO-D-` prefix occurrences across all 3 cases combined: **0**.

---

**End of mirror v0.** Next pass: triage by Doc08 ↔ Doc13 goal-binding edge density (this pass reports counts only; the edge inventory lives in `phase1_ontology.yaml` which was not deeply parsed here).
