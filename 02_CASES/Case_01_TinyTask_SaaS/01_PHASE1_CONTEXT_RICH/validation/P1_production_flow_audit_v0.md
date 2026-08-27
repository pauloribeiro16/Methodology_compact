# P1 Production-Flow Audit v0 — Case_01 Phase 1 (RICH)

**Scope:** `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/` (13 numbered deliverables + 6 meta artefacts) plus `00_COMMON/` references.
**Decisions already made by the user (input to this audit):**
- The artefact for this case is `PRODUCTION_FLOW.md` (meta, NOT numbered).
- The methodology extension is an **additive** sibling diagram `phase1_rich_extension.md` plus a master pointer.
- Dashboard expansion Fases B–E is **PAUSED**.

This audit classifies each item as FLOW-NATIVE / JUSTIFIED-EXTENSION / ORPHAN / META-INFRA and surfaces the lacunae the user must close if KEEP-IN-FLOW.

---

## Audit Matrix

Legend: §PURP = PURPOSE section present. §OBJ = objective-link count `AG-/AO-/PG-/SG-` (cleaned to letters-only matches inside the body; frontmatter is excluded). §KG = source provenance in `data/phase1_graph.json` node+link `source[]` lists. §DANGLING = unresolved sibling / methodology paths.

### Deliverables (13 numbered)

| # | File (basename) | Classificação | §2 Inputs decl. vs realized | §3 Outputs decl. vs realized | §4 Secção Propósito | §5 Ligação objetivos | §6 Proveniência KG | §7 Refs penduradas | §8 Recomendação | §9 Lacuna para fechar se KEEP |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | Doc01_Taxonomy_Reference.md | FLOW-NATIVE (root) | decl `[ ]` → realized: cited as input by Doc02, Doc03, Doc08, Doc10, Doc11. **OK** — declared empty but consumed downstream (root). | decl `[01_INTAKE_FORM.md]` → realized: Doc02 does NOT cite `Taxonomy_Reference` in inputs/outputs (it's referenced in body). **MINOR** — only Doc02 cites it in `related_documents`. | YES (## 1. DOCUMENT PURPOSE) | 0 / 0 / 0 / 0 — taxonomy reference, OK 0 expected | 0 node/link refs (no `Doc01` token in graph) — OK as a corpus root | 1: `outputs: [01_INTAKE_FORM.md]` cites legacy basename | KEEP-IN-FLOW | rewrite `outputs:` to `Doc02_INTAKE_FORM.md`; nothing else needed. |
| 02 | Doc02_INTAKE_FORM.md | FLOW-NATIVE | decl `[00_Taxonomy_Reference.md]` → realized: Doc03 cites `01_INTAKE_FORM` (legacy). Consumers OK. | decl `[04_Company_Context_Assessment.md]` → realized: Doc03 is named `Doc03_…` but legacy token in consumer grep is a hit — the **flow is intact**, only the **naming is broken**. | YES (## 1. PURPOSE) | 0 | 1 node ref (Doc02 §2/§3) — `nodes=1, links=0` | 5: `inputs: [00_Taxonomy_Reference.md]`, `outputs: [04_Company_Context_Assessment.md]`, `related_documents: [00_Taxonomy_Reference.md]`, in-body: `02_Regulatory_Mapping_Master.md` (DEPRECATED, kept as note), `02_CASES/Case_01_TinyTask_SaaS/00_COMMON/01_Company_Context.md` | KEEP-IN-FLOW | rewrite 3 frontmatter entries to `Doc01_Taxonomy_Reference.md` / `Doc03_Company_Context_Assessment.md` / `Doc01_Taxonomy_Reference.md`. Confirm deprecation note stays (intentional). |
| 03 | Doc03_Company_Context_Assessment.md | FLOW-NATIVE (convergence) | decl `[01_INTAKE_FORM.md]` → realized: Doc04, Doc05, Doc06, Doc07, Doc08, Doc10, Doc11, Doc12, Doc13 all cite Doc03 in their inputs/related. **MATCH.** | decl `[05_Regulatory_Applicability.md]` → realized: Doc08 (legacy) consumes. **MATCH.** | YES (## 1. DOCUMENT PURPOSE) | 5×AG- / 0×AO- / 1×PG- / 1×SG- — **AG-prefix inside body, contradicts methodology AO-canonical** (see Section A) | 28 node/link refs (nodes=13, links=15) — STRONG | 6+: all inputs/outputs in legacy basenames; in-body refs to `00_Taxonomy_Reference.md`, `01_INTAKE_FORM.md`, `02_Regulatory_Mapping_Master.md`, `01_PHASE1_CONTEXT/04_…`, `00_COMMON/01_Company_Context.md`, `05_Regulatory_Applicability.md` | KEEP-IN-FLOW (essential hub) | (1) frontmatter rename 4 entries to DocNN form; (2) cross-decode the 5 `AG-D-XX.X-NNN` body IDs to `AO-D-XX.X-NNN`; (3) replace `01_PHASE1_CONTEXT/04_…` and `02_Regulatory_Mapping_Master.md` references with current DocNN / ontology paths. |
| 04 | Doc04_Architecture_DataInventory.md | FLOW-NATIVE | decl `[04_Company_Context_Assessment.md, 01_INTAKE_FORM.md, 05_Regulatory_Applicability.md]` → realized: Doc05, Doc06, Doc07, Doc09 all cite Doc04 in inputs/outputs. **MATCH (with rename debt).** | decl `[04b_Security_Posture.md, 07_Structured_Compliance_Matrix.md]` → realized: Doc05/Doc06/Doc07 forward to those. **MATCH.** | NO top-level "Purpose" heading — first heading is "1. Technical Architecture". This is **§1 PURPOSE absent** (sub-sections exist, no purpose preamble). | 0 | 298 node/link refs (nodes=20, links=278) — HEAVIEST | 51+: legacy `Doc03`, `Doc02`, `Doc08` names in frontmatter; `../../../00_METHODOLOGY/PREPROCESSING/SubDomains/*` (path does not exist — PREPROCESSING/ is gone); `D-XX.Y.manifest.json` (does not exist); `01_PHASE1_CONTEXT/04a_…`; `02_Regulatory_Mapping_Master.md` | KEEP-IN-FLOW | (1) insert §1 PURPOSE; (2) frontmatter rewrite to DocNN; (3) rewrite 37 link refs from `PREPROCESSING/SubDomains/D-XX_Y/D-XX.Y.md` to `PREPROCESSING_by_domain/domains/D-XX_Y/…`; (4) drop `D-XX.Y.manifest.json` refs (no manifests exist). |
| 05 | Doc05_Security_Posture.md | ORPHAN-HYBRID (DEPRECATED_FOR_MATURITY) | decl `[04_Company_Context_Assessment.md, 04a_Architecture_DataInventory.md, 05_Regulatory_Applicability.md]` → realized: Doc06, Doc07 cite Doc05. | decl `[07_Structured_Compliance_Matrix.md]` → no consumer cites Doc05 as input. Frontmatter declares ownership moved to Phase 2 Doc 13. | YES (## 1. Assessment Methodology) — but it's a methodology preamble, not a purpose preamble. | 0 | 0 node/link refs (graph does not know Doc05). Plus frontmatter `status: DEPRECATED_FOR_MATURITY` and `note:` redirects ownership to `02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md`. | 41+: legacy names + `01_PHASE1_CONTEXT/04b_…` + the 37 PREPROCESSING/SubDomains links + `02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md` | ORPHAN (in-flow signal lost) | choose: (a) PROMOTE to meta-input (keep posture only) and remove from FLOW-NATIVE chain, OR (b) DELETE and re-reconcile Doc05 ownership in Doc07/Doc11. **Recommendation: option (a)** — mark as INPUT-only artefact consumed before Doc07 synthesis. |
| 06 | Doc06_ThirdParty_Landscape.md | FLOW-NATIVE | decl `[04_Company_Context_Assessment.md, 04a_Architecture_DataInventory.md, 01_INTAKE_FORM.md]` → realized: Doc07 cites Doc06. **MATCH.** | decl `[04b_Security_Posture.md, 06_Clause_Mapping_Matrix.md, 07_Structured_Compliance_Matrix.md]` → Doc07 cited; Doc10 cited via legacy name. **MATCH.** | YES (## 1. Purpose & Scope) | 0 | 0 node/link refs (graph omits Doc06). | 17+: legacy names; `../../../00_METHODOLOGY/TEMPLATES/04c_ThirdParty_Landscape.md` (TEMPLATES/ gone); `../../../00_METHODOLOGY/CONTEXT/CONTEXT_PHASE1.md` (CONTEXT/ gone); `00_METHODOLOGY/PREPROCESSING_by_domain/_by_regulation/...` (wrong subpath); `01_PHASE1_CONTEXT/04c_…` | KEEP-IN-FLOW | (1) frontmatter rewrite to DocNN; (2) replace TEMPLATES/ and CONTEXT/ refs with corpus equivalents (or drop); (3) fix `_by_regulation/` path; (4) add graph source provenance for Doc06 in next kg emission. |
| 07 | Doc07_Org_Roles_RACI.md | FLOW-NATIVE | decl `[04_Company_Context_Assessment.md, 04a_Architecture_DataInventory.md, 04c_ThirdParty_Landscape.md, ../00_COMMON/01_Company_Context]` → no other Doc declares Doc07 as input/related in their frontmatter. **Downstream is silent** — Doc07 is a feeder, not a consumer. OK. | decl `[04b_Security_Posture.md, 05_Regulatory_Applicability.md, 06_Clause_Mapping_Matrix.md, 07_Structured_Compliance_Matrix.md]` → Doc08, Doc10, Doc11 cite Doc07 — matches with legacy naming. **MATCH.** | YES (## 1. Purpose & Scope) | 0 | 0 node/link refs (graph does not represent RACI in v1.3; v1.4 / Folio VI dashboard holds it separately). | 19+: legacy names; `../../../00_METHODOLOGY/CONTEXT/CONTEXT_PHASE1.md`; `../../../00_METHODOLOGY/TEMPLATES/04d_Org_Roles_RACI.md`; `01_PHASE1_CONTEXT/04d_…`; `../00_COMMON/01_Company_Context.md` (path OK: `01_Company_Context.md` exists in 00_COMMON). | KEEP-IN-FLOW | (1) frontmatter rewrite; (2) drop TEMPLATES/ and CONTEXT/ refs; (3) fix `_legacy_superseded` related; (4) the `00_COMMON/01_Company_Context.md` ref is correct (note: doc01/doc02 also `Doc03` references it — cross-check naming consistency). |
| 08 | Doc08_Regulatory_Applicability.md | FLOW-NATIVE | decl `[04_Company_Context_Assessment.md]` → realized: Doc10, Doc11 cite Doc08; Doc12 cites it; Doc13 cites it. **MATCH.** | decl `[06_Clause_Mapping_Matrix.md]` → realized: Doc10 cites. **MATCH.** | YES (## 1. DOCUMENT PURPOSE) | 0 | 0 node/link refs — graph uses `phase1_ontology.yaml@applicability_assessments` and `Doc08 §4` token, **not** the literal `Doc08` token in source strings. (Disambiguation: Doc05 maps to legacy Doc05 too — the graph references Doc05 §4+§9 implicitly via the ontology, so §6 here is conservative. Confirm by adding `Doc08` token in next emission.) | 10+: legacy names + `../../../00_METHODOLOGY/PHASE1_STRATEGY.md` (does not exist) + `01_PHASE1_CONTEXT_RICH/07c_Adjusted_Goals.md` (Doc13's pre-rename name, now Doc13) + `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` (OK path) + in-body `02_Regulatory_Mapping_Master.md` (DEPRECATED) | KEEP-IN-FLOW | (1) frontmatter rewrite 5 entries; (2) drop PHASE1_STRATEGY.md ref or re-home; (3) replace `07c_Adjusted_Goals.md` → `Doc13_Adjusted_Goals.md`; (4) drop DEPRECATED master ref (or keep with note like Doc02). |
| 09 | Doc09_Ambiguity_Register.md | JUSTIFIED-EXTENSION | decl `[ ]` → declared inputs empty. Realized: no Doc declares Doc09 in inputs/outputs. OK — it's a synthesis sidecar. | decl `[ ]` → no declared outputs. Realized: no Doc declares Doc09 as downstream. OK as sidecar. | NO (first heading is `§1 Summary Statistics`). §0 Purpose absent in body, but document is structured as enumerative synthesis so preamble is implicit. | 0 | **0** node/link refs in graph — the register has 417 cards yet none surface in `data/phase1_graph.json` `source[]` lists. **GAP**: graph v1.4 does not cover Doc09. | none observed in frontmatter (one of the cleanest). The body has 417 cards referencing `D-XX.Y/articles/<REG>_Art_<N>.md`, paths valid in `PREPROCESSING_by_domain/domains/`. | KEEP-IN-FLOW (justify as extension) | (1) add §0 Purpose for symmetry with Doc01/02/03/08/10/11/12; (2) ensure next graph emission (≥v1.5) adds Doc09 in `meta.canonical_sources` (currently absent) and indexes ambiguity cards as nodes. |
| 10 | Doc10_Clause_Mapping_Matrix.md | FLOW-NATIVE | decl `[04_Company_Context_Assessment.md, 05_Regulatory_Applicability.md]` → realized: Doc11 cites both via legacy names. **MATCH.** | decl `[07_Structured_Compliance_Matrix.md]` → realized: Doc11 cites. **MATCH.** | YES (## 1. DOCUMENT PURPOSE) | 0 | 12 node/link refs (nodes=6, links=6). | 4+: legacy `04_…`, `05_…`, `07_…` (should be Doc03/Doc08/Doc11). | KEEP-IN-FLOW | (1) frontmatter rewrite 3 entries; (2) graph: bump source token to `Doc10` for clarity. |
| 11 | Doc11_Structured_Compliance_Matrix.md | FLOW-NATIVE (convergence) | decl `[04_Company_Context_Assessment.md, 05_Regulatory_Applicability.md, 06_Clause_Mapping_Matrix.md]` → realized: Doc12 cites all three; Doc13 cites all three. **MATCH.** | decl `[08_Obligation_Derivation.md]` → realized: Doc13 + Doc12 list Doc11 in their inputs. **MATCH (with cross-phase path debt).** | YES (## 1. DOCUMENT PURPOSE) | 0 | 398 node/link refs (nodes=103, links=295) — SECOND HEAVIEST. Graph-rich. | 5+: legacy names + `08_Obligation_Derivation.md` (Phase 2 doc, not in Phase 1 dir — cross-phase, OK semantically). | KEEP-IN-FLOW | (1) frontmatter rewrite 4 entries to DocNN; (2) no other lacuna. |
| 12 | Doc12_Proportionality_Profile.md | FLOW-NATIVE | decl `[04_Company_Context_Assessment.md, 05_Regulatory_Applicability.md, 07_Structured_Compliance_Matrix.md, ../../../../../00_METHODOLOGY/REFERENCE/proportionality_model.md, ../../../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/]` → realized: Doc13 cites Doc12 in inputs + related. **MATCH.** The methodology refs are dangling (see §7). | decl `[08_Obligation_Derivation.md, 11_Rules_Catalog.md, 14_Architectural_Nodes.md, 07c_Adjusted_Goals.md]` → realized: Doc13 cites Doc12 in inputs + related. Cross-phase outputs are intra-Phase-2/3 paths, OK semantically. | YES (## 1. DOCUMENT PURPOSE) | 0 | 0 node/link refs — graph does NOT cover Doc12 (`source` token absent). **GAP.** | 17+: legacy names; `00_METHODOLOGY/REFERENCE/proportionality_model.md` (REFERENCE/ gone); `00_METHODOLOGY/REFERENCE/fr_nfr_numbering.md` (gone); `00_METHODOLOGY/REGULATORY_BASELINE.md` (gone); `01_PHASE1_CONTEXT/07b_…`; `02_Regulatory_Mapping_Master.md`; `../03_PHASE3_DECOMPOSITION/annexes/Critical_Analysis_Micro_Enterprise.md` (path needs verification). | KEEP-IN-FLOW | (1) frontmatter rewrite 8 entries to DocNN; (2) drop or relocate REFERENCES and REGULATORY_BASELINE.md refs (they are obsolete methodology paths); (3) recalibrate `eval_proportionality.py` mention in §9 line 55 — the script is in `02_PHASE1_CONTEXT_RICH/scripts/` not in `01_IMPLEMENTATION_TOOLS/`; (4) graph: add Doc12 to `meta.canonical_sources` in next emission. |
| 13 | Doc13_Adjusted_Goals.md | JUSTIFIED-EXTENSION (canonical Phase 1 AO table; supersedes Phase 2 10_Privacy_Security_Goals §3-§4) | decl `[04_Company_Context_Assessment.md, 05_Regulatory_Applicability.md, 07_Structured_Compliance_Matrix.md, 07b_Proportionality_Profile.md, 10_Privacy_Security_Objectives.md, 09_Strategic_Tensions_Report.md, phase1_ontology.yaml, ../../../../../00_METHODOLOGY/REFERENCE/proportionality_model.md]` → realized: 0 consumers cite Doc13 in inputs/related at frontmatter level (Doc03, Doc08, Doc12 cite Doc13 in **body** only, not frontmatter). **MATCH (with body-only consumers).** | decl `[phase 2 rules catalog (11_Rules_Catalog.md) consumes adjusted objectives]` (prose-only) → no Doc declares Doc13 as input/output. Cross-phase handoff is implicit. | YES (## §0 Document Purpose) | **124×AG-D-, 0×AO-D-, 12×PG-D-, 13×SG-D-** — see Section A. AG-canonical inside the doc, AO-canonical in methodology. **CONTRADICTION.** | 0 node/link refs in graph for Doc13 token — but Doc13 is heavily used as §ref in node `source` (e.g., `Doc13 §2 (HL) + §3 (GDPR-driven)`); the **token** `Doc13` is in graph `source[]` strings **18 times** across 150 node-occurrences (per earlier count `Doc13: 150`). Conservative: §6 marks 0, but the **section-level** provenance is present. | 10+: legacy `04_…`, `05_…`, `07_…`, `07b_…`, `09_…`, `10_…`, `11_…`; `02_PHASE2_RULES/09_Strategic_Tensions_Report.md` and `02_PHASE2_RULES/10_Privacy_Security_Goals.md` (now Phase-2-rich dir `02_PHASE2_RULES_RICH/`); `../../../../../00_METHODOLOGY/REFERENCE/proportionality_model.md`; in-body mention of `07c_Adjusted_Goals.md` (self-reference, now Doc13) | KEEP-IN-FLOW (justify as extension; corr-008 supersedes corr-007) | (1) frontmatter rewrite 8 entries to DocNN; (2) re-id 124×AG- to AO- in body (mechanical); (3) update `id_format:` field to `AO-D-XX.X-NNN (canonical Phase 1)`; (4) relocate or drop `02_PHASE2_RULES/09_…` and `02_PHASE2_RULES/10_…` paths to `02_PHASE2_RULES_RICH/`; (5) drop proportionality_model.md reference (path gone); (6) graph: bump token to `Doc13 §2/§3/§4/App A.0` (already there as prose — confirm). |

### Meta (6 items)

| # | File | Classificação | §2 Inputs decl. | §3 Outputs decl. | §4 Propósito | §5 Objetivos | §6 Proveniência KG | §7 Refs penduradas | §8 Recomendação | §9 Lacuna se KEEP |
|---|---|---|---|---|---|---|---|---|---|---|
| M1 | README.md | META-INFRA | none | none | n/a (orientation doc) | 0 | n/a — README does not appear in `source[]` | 4 lines stale: `01_PHASE1_CONTEXT/` (sibling dir, never existed); `RICH_VS_LEGACY.md` (no such file); `01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py` (never existed); lint report path; `eval_proportionality` lineage. | KEEP-IN-FLOW (orientation) | (1) drop sibling-of `01_PHASE1_CONTEXT/` claim; (2) remove RICH_VS_LEGACY.md refs (file never created); (3) remove `01_IMPLEMENTATION_TOOLS/` lint command (linter lives in scripts/ in-dir); (4) add explicit pointer to `PRODUCTION_FLOW.md` once written. |
| M2 | PROJECT_STATE.md | META-INFRA | none | none | n/a (status doc) | 0 | n/a | 14+ lines stale: `01_PHASE1_CONTEXT/`, `RICH_VS_LEGACY.md`, `corpus_field_map.md` (now `Corpus_Field_Map.md`), `01_PHASE1_CONTEXT_RICH/05b_…`/`07b_…` (rename), `01_IMPLEMENTATION_TOOLS/lints/…`, `01_PHASE1_CONTEXT_RICH/data/phase1_graph.json` "181/248/12" (now stale after v1.4). | KEEP-IN-FLOW | (1) rewrite all stale legacy paths; (2) re-stamp graph node/link counts (181→388 per v1.4); (3) drop the `01_IMPLEMENTATION_TOOLS/` lint command. |
| M3 | Citation_Index.md | META-INFRA (extracted) | n/a — it's a derivation | n/a | n/a | 0 | n/a (not a node source) | body cites legacy basenames (e.g. `04c_ThirdParty_Landscape.md`, `04d_Org_Roles_RACI.md`, `05_Regulatory_Applicability.md`, `07b_Proportionality_Profile.md`) — need rename. | KEEP-IN-FLOW | regenerate against current DocNN names — likely an automated rebuild via `scripts/generate_corpus_links.py`. |
| M4 | Corpus_Field_Map.md | META-INFRA (Sprint 0 DRAFT, never updated) | n/a | n/a | n/a (DRAFT status) | 0 | n/a | 21+: `../../01_PHASE1_CONTEXT/_legacy_superseded/*.md` (sibling dir never existed); `STRUCTURE_REFERENCE.md` (never created); `../../../00_METHODOLOGY/PHASE1_STRATEGY.md` (gone); `scripts/preprocess/parse_domain.py` (never created); legacy DocNN names (`01_INTAKE_FORM`, `04_Company_Context_Assessment`, `04a`, `04b`, `04c`, `04d`, `05_…`, `06_…`, `07_…`, `07b_…`). | PARK-META (DRAFT, status never advanced; values consumed by Sprint 2 already) | either DELETE or FIX — at minimum drop the `_legacy_superseded` references and add a deprecation banner pointing to the post-Sprint-2 in-doc DocNN naming. |
| M5 | phase1_ontology.yaml | META-INFRA (machine-readable spine) | n/a — YAML key: `inputs:` not used; manual derivation | n/a | n/a | 0 (ontology encodes D-XX.Y / AO-D-XX.X-NNN via separate `coverage_summary`/`objectives` blocks — verified indirectly) | This file **IS** the KG spine: every node links back to `phase1_ontology.yaml@<section>`. Verified in graph meta: `"phase1_ontology.yaml@01_PHASE1_CONTEXT_RICH v1.3"`. | none observed at file level | KEEP-IN-FLOW (essential) | bump `v1.3 → v1.5` in `meta.canonical_sources` once Doc09 and Doc12/Doc13 token coverage lands. |
| M6 | data/phase1_graph.json | META-INFRA (machine-readable artifact) | n/a | n/a | n/a | encodes 150 Doc13 §refs + 318 Doc07 etc. as strings | n/a — this IS the KG | none at file level (it's the artifact) | KEEP-IN-FLOW (essential) | regenerate via `scripts/build_p1_graph.py` after fixes land. |

---

## A) Contradição AG- vs AO-

**Exact counts (verbatim from the commands in the brief):**

| Command | Count |
|---|---|
| `grep -nE "AG-D-\|AO-D-" /home/.../Doc13_Adjusted_Goals.md \| wc -l` | **124** (all `AG-D-`; `AO-D-` count is 0) |
| `grep -rnE "\bAG-D-" /home/.../00_METHODOLOGY/ \| wc -l` | **0** in `*.md` + `*.yaml` (4 hits were in HTML dashboard scripts, not documentation) |
| `grep -rnE "\bAO-D-" /home/.../00_METHODOLOGY/ \| wc -l` | **7** in `*.md` + `*.yaml` (`00_METHODOLOGY/dependency_graph.yaml` ×6 lines, `00_METHODOLOGY/AGENTS.md` ×1) |
| `bash scripts/kg.sh impact AEGIS-P1-RICH-07c` | **`No unique node match for AEGIS-P1-RICH-07c`** (kg.sh E3 graph uses bare DocNN tokens, not the `AEGIS-P1-RICH-07c` document_id) |

**The AG→AO migration story (commit log):**

- The `dependency_graph.yaml` declares the canonical Phase 1 goal prefix as `AO-D-XX.X-NNN` (6 occurrences, lines 64/85/121/154/256/257) and maps `PG/SG-D-XX.X-NNN → AO-D-XX.X-NNN (Phase 1)` explicitly (lines 256–257).
- The `00_METHODOLOGY/AGENTS.md` table (line 53) names Phase 1 IDs as `AO-D-XX.X-NNN — Adjusted Objectives — Doc 07c`.
- **No commit message in the git log mentions corr-009 or corr-015 by name** — these contracts are recorded **inside Doc13's frontmatter** (`corr-009 ao-id-alias-update`, `corr-015-ao-canonical-ids`, `2026-08-10`) and Doc03's frontmatter (`corr-009 ao-id-alias-update`, `corr-015 ao-canonical-ids cross-refs`). The two sprints that did the work are recorded in PROJECT_STATE adjacent dates as Sprints 8 and 9 but no standalone commit carries the corr-XXX tag.
- Sprint 8 updated Doc03 BG-03/BG-04 (`ao_id_alias_update_bg03_bg04`) and Doc08 (`ao_id_cross_ref_note`) — the "alias" form. Sprint 9 was the "cross-refs" pass. The migration renamed **internal cross-references** but **did not re-id the 124 body occurrences in Doc13** nor update the `id_format:` frontmatter field.
- Sprint 11 (2026-08-14) added the NIST controls layer (`corr-016-nist-controls-layer`); no further migration of the AG→AO tokens was made.
- The net result: **the methodology says AO, the deliverable says AG**. Doc13 still declares `id_format: AG-D-XX.X-NNN (canonical Phase 1)` (frontmatter line 16), uses `AG-D-` 124 times in body, and lists 8 `appendix_a_migrated_d01_cards` whose values are `AG-D-XX.X-NNN` (frontmatter lines 47–54).
- Doc13's frontmatter records `ao_id_migration_sprint: 8` and `corr_015_crossref_update_sprint: 9`, but the frontmatter `id_format:` line is **inconsistent** with the AO canonical it claims to have migrated to.

---

## B) Frontmatter damage from rename `c94b840`

The commit message states: *"Rename: case-file convention DocNN_Nome.md (95 renames, 0 content diff)"* — the `git mv` step. It also states: *"14 broken markdown links fixed (Case_02 only); prose mentions of old filenames intentionally untouched per user direction."*

That last clause is the source of the frontmatter damage. Counts of legacy basenames in frontmatter (each entry counted once even if cited multiple times in the same frontmatter):

| Doc | legacy basename hits in frontmatter | DocNN hits in frontmatter |
|---|---|---|
| Doc01 | 1 | 0 |
| Doc02 | 4 | 0 |
| Doc03 | 4 | 0 |
| Doc04 | 5 | 0 |
| Doc05 | 5 | 0 |
| Doc06 | 7 | 0 |
| Doc07 | 8 | 0 |
| Doc08 | 5 | 0 |
| Doc10 | 4 | 0 |
| Doc11 | 4 | 0 |
| Doc12 | 8 | 0 |
| Doc13 | 8 | 0 |
| **TOTAL** | **63 legacy basename citations across 12 of 13 frontmatter blocks (Doc09 has none)** | **0** |

The most-affected frontmatter is **Doc07 (8)**, **Doc06 (7)**, **Doc12 (8)**, **Doc13 (8)** — Doc12 and Doc13 are the deepest Phase 1 outputs, so the frontmatter damage is concentrated where downstream consumers look first.

The damage is **cosmetic-only** at the frontmatter level: the on-disk files were renamed, so any tool that resolves the path *via* the actual file location still works. But any tool that uses the frontmatter `inputs:`/`outputs:` to drive a topology graph (e.g., the next graph emission, the linter, the `phase1_rich_extension.md` master pointer) will read the **legacy names** and emit broken links.

---

## C) Stale refs in case-level docs

### README.md
- Line 11 `sibling_of: 01_PHASE1_CONTEXT/` — **never existed** (Case_01 only has `01_PHASE1_CONTEXT_RICH/`).
- Line 24 "legacy `01_PHASE1_CONTEXT/` remains the as-shipped artefact" — **false**.
- Line 42 "RICH_VS_LEGACY, PROJECT_STATE, VALIDATOR_SPRINT3" — **RICH_VS_LEGACY.md never created**.
- Line 74 `| RICH_VS_LEGACY.md | NEW |` — **never created**.
- Line 108 "Diff vs legacy: `RICH_VS_LEGACY.md`" — **never created**.
- Line 129 `python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_01_TinyTask_SaaS" --quiet` — **path never existed**.
- Line 132 `Latest report: 01_IMPLEMENTATION_TOOLS/lints/reports/lint_report_phase1_20260806_120303.md` — **never existed**.

### PROJECT_STATE.md
- Line 15 `> Phase 1 Rich Mode — corpus-enriched sibling of legacy 01_PHASE1_CONTEXT/.` — **never existed**.
- Line 16 `> ... legacy 02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md.` — **never existed** (only `02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md` does exist, but not in the legacy `01_PHASE1_CONTEXT/` form claimed here).
- Line 23 `Phase 1 Legacy | INTACT | ... 01_PHASE1_CONTEXT/ not modified` — **never existed**.
- Line 34 `Corpus field map (515 lines) | 01_PHASE1_CONTEXT_RICH/corpus_field_map.md` — file is **now** `Corpus_Field_Map.md` (c94b840).
- Line 37 `Diff summary (Sprint 3) | 01_PHASE1_CONTEXT_RICH/RICH_VS_LEGACY.md` — **never created**.
- Line 39 `Sprint 3 corpus cross-check | 01_PHASE1_CONTEXT_RICH/07b_Proportionality_Profile.md` — now `Doc12_…`.
- Line 51 `| 3 | 2026-08-06 | ... (RICH_VS_LEGACY, PROJECT_STATE)` — references the never-created file.
- Line 62 + 64 `01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py` and the report path — **never existed**.
- Line 74 "Canonical graph (181 nodes / 248 links / 12 audits)" — stale (v1.4 is 246/505/21; v1.5+ drifted further).
- Line 137 `01_PHASE1_CONTEXT_RICH/RICH_VS_LEGACY.md` — **never created**.
- Line 143 `02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md` (the legacy case-level state) — **exists** at case root, OK.

### Corpus_Field_Map.md
- 10 entries in `related_documents` reference `../../01_PHASE1_CONTEXT/_legacy_superseded/*.md` — **the `01_PHASE1_CONTEXT/` directory never existed at all** (no legacy sibling of the RICH folder).
- `../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/STRUCTURE_REFERENCE.md` — **never created**.
- `../../../00_METHODOLOGY/PHASE1_STRATEGY.md` — **never created**.
- `scripts/preprocess/parse_domain.py` — **never created**.
- Body refers to `STRUCTURE_REFERENCE.md §3, §9` and `STRUCTURE_REFERENCE.md §8` — **never created**.
- Doc-by-Doc body sections are titled `### Doc 04 — Company Context Assessment (04_Company_Context_Assessment.md)`, `### Doc 04a — Architecture & Data Inventory (04a_Architecture_DataInventory.md)`, etc. — all 10 in-doc references use **legacy basenames** rather than DocNN.
- File is `status: DRAFT` per frontmatter and was never advanced past Sprint 0.

### Citation_Index.md
- Lines 39–55 cite legacy basenames inside the "cited in" column (`04c_ThirdParty_Landscape.md`, `07b_Proportionality_Profile.md`, `04d_Org_Roles_RACI.md`, `01_INTAKE_FORM.md`, `04_Company_Context_Assessment.md`, `04b_Security_Posture.md`, `05_Regulatory_Applicability.md`, `04d_Org_Roles_RACI.md`).
- Line 19 corpus path `01_PHASE1_CONTEXT_RICH/` is OK (dir exists); the rest of the body and the embedded "↳ cited in" column is the legacy-naming issue, not a missing file.
- No dangling methodology file references in Citation_Index itself.

### Cross-cutting
- `RICH_VS_LEGACY.md` (cited 5× across README + PROJECT_STATE): **never created**.
- `eval_proportionality.py` (cited in Doc12 lines 55, 180, 185, 283): implementation lives in `02_PHASE1_CONTEXT_RICH/scripts/` (or Phase 2); the references imply `01_IMPLEMENTATION_TOOLS/evals/` which never existed.
- `run_phase1_lints.py` (cited README line 129, PROJECT_STATE line 62): no such path.
- `01_IMPLEMENTATION_TOOLS/`: never existed at repo root.
- `RICH_VS_LEGACY.md`, `eval_proportionality.py`, `run_phase1_lints.py`, `01_IMPLEMENTATION_TOOLS/`, `evaluation/`, `QUALITY/`, `GUIDES/`: **none exist**.

---

## D) Suggested integration point for `phase1_rich_extension.md`

Read location: `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/00_METHODOLOGY/diagrams/fluxdiagram/phase1/phase1_contextual_definition.md`

**Recommended insertion site: between the existing "Document Flow Summary" (lines 176–189) and the "What This Diagram Does NOT Show" section (line 195).**

Verbatim quote of the seam (lines 176–195):

```
176: ## Document Flow Summary
177:
178: ```
179: Company Facts ──→ Doc 04 ──→ Doc 05 ──→ Doc 06 (Excel) ──→ Doc 07
180:                      │           │                              ↑
181:                      │           │                              │
182:                      └───────────┴──→ Doc 07 (direct feed) ────┘
183:                                                         ↑
184: Taxonomy (00) ─────────────────────────────────────────→ │
185: Design Decisions (03) ─────────────────────────────────→ │
186:                                                          │
187:                                                          │     ↓
188:                                                   Doc 07b ←┘ (Proportionality Profile)
189: ```
190:
191: Doc 07 is the **convergence point**. It pulls from multiple sources and generates 4 new analyses that don't exist in any upstream document. It is not just an aggregation — it is a synthesis engine.
192:
193: ---
194:
195: ## What This Diagram Does NOT Show
```

**Suggested new section (insert immediately after line 191, before the `---` at line 193):**

```
## Rich-Mode Extension (Case-Level Add-On)

The base diagram above models the methodology's canonical Phase 1 flow.
Case_01 Phase 1 (RICH) extends it with **five additional artefacts** that
the methodology intentionally keeps out of the canonical flow because
they are case-specific or research-specific:

1. **Doc 09 — Ambiguity Register** (Rich-Mode only): per-clause
   ambiguity cards (417 in Case_01) extracted from the corpus.
2. **Doc 13 — Adjusted Objectives per Sub-Domain** (Rich-Mode only):
   substitutes the canonical AG-D-XX.X-NNN / AO-D-XX.X-NNN objective
   table for the Phase 2 PG/SG table.
3. **Citation Index** (extracted sidecar): per-article cross-reference
   matrix derived from Doc04/Doc05/Doc07/Doc13.
4. **Phase 1 Story Folio** (Folio V of the Case_01 dashboard):
   end-to-end 264-link narrative view of the KG.
5. **PRODUCTION_FLOW.md** (case artefact): orientation narrative
   that links the case-specific 13 docs into the canonical flow.

The full Rich-Mode flow diagram (mermaid + Document Flow Summary +
additive per-doc cards) is in the sibling file
[`phase1_rich_extension.md`](phase1_rich_extension.md).
For the Case_01 implementation, see
[`02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/PRODUCTION_FLOW.md`](../../../02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/PRODUCTION_FLOW.md).
```

**Why this site:**
- Lines 178–189 (the `Document Flow Summary` ASCII box) stop at Doc 07b.
  The five Rich-Mode artefacts are downstream of Doc 07b / Doc 13 and
  upstream of Phase 2 — exactly the seam between the canonical flow
  (Doc 01 → Doc 13) and the cross-phase handoff.
- Line 191 already names Doc 07 as "the convergence point"; the
  extension lives in the convergence neighbourhood.
- Line 195 "What This Diagram Does NOT Show" is the natural place to
  *stop* showing things, so adding the extension pointer just before
  the `---` separator (line 193) creates a clean two-section structure
  (canonical → extension → non-shown).
- The link target `phase1_rich_extension.md` is a sibling in the same
  `phase1/` directory, so the relative path is stable across method
  rebuilds.
- The Case_01 `PRODUCTION_FLOW.md` pointer uses a 3-up
  `../../../02_CASES/...` jump; this matches the relative-path
  convention already used in `related_documents` in Doc04–Doc07.

**Master-pointer approach:** the user already decided that the
methodology artefact is additive and pointed-to from this file, not
inlined; the section above does only the pointer, and the new
`phase1_rich_extension.md` holds the diagram itself.

---

## Headline numbers

- Deliverables: 13 numbered docs. Of those, 9 are FLOW-NATIVE (Doc01-04, Doc06, Doc07, Doc08, Doc10, Doc11, Doc12 = 11 if counted loosely; the precise count below), 1 is ORPHAN-HYBRID (Doc05 DEPRECATED_FOR_MATURITY), 2 are JUSTIFIED-EXTENSION (Doc09, Doc13).
  - **FLOW-NATIVE (10):** Doc01, Doc02, Doc03, Doc04, Doc06, Doc07, Doc08, Doc10, Doc11, Doc12.
  - **JUSTIFIED-EXTENSION (2):** Doc09, Doc13.
  - **ORPHAN-HYBRID (1):** Doc05.
  - **META-INFRA (6):** README, PROJECT_STATE, Citation_Index, Corpus_Field_Map, phase1_ontology.yaml, data/phase1_graph.json.
- §A: Doc13 has 124 AG-D- vs 0 AO-D-; methodology has 0 AG-D- and 7 AO-D-; kg.sh impact returns `No unique node match`.
- §B: 63 legacy-basename citations across 12 of 13 frontmatter blocks; 0 DocNN-style citations.
- §C: 5 case-level stale-ref categories — `01_PHASE1_CONTEXT/` (never existed, 5+ refs), `RICH_VS_LEGACY.md` (never created, 5 refs), `01_IMPLEMENTATION_TOOLS/` (never existed, 3 refs), `corpus_field_map.md` (now `Corpus_Field_Map.md`, 1 ref), DocNN legacy basenames throughout all four meta docs.
- §D: insertion site is `phase1_contextual_definition.md` line 192 (immediately before the `---` at line 193), pointing to a sibling `phase1_rich_extension.md` plus `02_CASES/.../PRODUCTION_FLOW.md`.
