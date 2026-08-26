---
document_id: AEGIS-P2-RICH-STATE
title: Project State — Phase 1 Rich Mode (Case_02)
phase: 1
version: 1.0
created: 2026-08-06
author: Sprint 3 Executor
status: FINAL
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
active_subdomains: 35
track: B
tier: MEDIUM (disputed — see §7 F-01)
related_documents:
  - README.md
  - RICH_VS_LEGACY.md
  - 07b_Proportionality_Profile.md
  - validation/VALIDATOR_SPRINT3.md
  - ../PROJECT_STATE.md
frozen: false
---

# Project State — Phase 1 Rich Mode (Case 02)

> Case_02_SecureBorder_Solutions B.V. — Phase 1 Rich Mode (corpus-enriched sibling of legacy `01_PHASE1_CONTEXT/`).
>
> **Scope note:** this file is *localised* to the Rich folder. The case-wide state of record remains `../PROJECT_STATE.md`, which is unmodified by Sprints 0–3.

---

## §1 Status

| Track | Status | Notes |
|-------|--------|-------|
| **Phase 1 Rich** | ⚠️ **CONDITIONAL_PASS** (Sprints 0–5 executed) | Not "COMPLETE" — 2 blocking items open (§7); `07c` is DEEP_ENRICHED. See `validation/VALIDATOR_SPRINT3.md`. |
| Phase 1 (legacy) | ✅ COMPLETE | Frozen, read-only; still the folder consumed by Phase 2/3 |
| Phase 2 (legacy) | ✅ COMPLETE | Gate decision PASS; Docs 08–12 |
| Phase 3 (legacy) | ✅ COMPLETE (84.1%) | 53/63 rules satisfied; Docs 13–24 |

**Substitution has NOT occurred.** The Rich folder does not yet supersede the legacy folder as the Phase 2/3 input. Promotion requires O-01 and O-02 (§7) to be closed and `07c` to be delivered.

---

## §2 Deliverables

### Phase 1 documents (16 `.md`, 5,349 lines)

| Doc | Path | Status |
|-----|------|--------|
| 00 | `00_Taxonomy_Reference.md` | ✅ RECONCILED |
| 01 | `01_INTAKE_FORM.md` | ✅ RECONCILED |
| 04 | `04_Company_Context_Assessment.md` | ✅ RECONCILED |
| 04a | `04a_Architecture_DataInventory.md` | ✅ ENRICHED (Sprint 2) |
| 04b | `04b_Security_Posture.md` | ✅ ENRICHED (Sprint 2) |
| 04c | `04c_ThirdParty_Landscape.md` | ✅ ENRICHED (Sprint 2) |
| 04d | `04d_Org_Roles_RACI.md` | ✅ ENRICHED (Sprint 2) |
| 05 | `05_Regulatory_Applicability.md` | ✅ RECONCILED |
| **05b** | `05b_Ambiguity_Register.md` | ⚠️ COMPLETE with defect — §3 top-20 covers only 3 distinct clauses (O-04) |
| 06 | `06_Clause_Mapping_Matrix.md` | ✅ RECONCILED |
| 07 | `07_Structured_Compliance_Matrix.md` | ✅ RECONCILED |
| **07b** | `07b_Proportionality_Profile.md` | ⚠️ ACTIVE + cross-checked — 1 MAJOR finding open (F-01) |
| **07c** | `07c_Adjusted_Objectives.md` | ✅ **DEEP_ENRICHED** (2,169 lines, Sprint 5) |
| — | `Citation_Index.md` | ✅ COMPLETE (Sprint 2) |
| — | `corpus_field_map.md` | ⚠️ still `DRAFT` (Sprint 0) |
| — | `README.md` | ✅ ACTIVE (Sprint 3) |

### Supporting artefacts

| Path | Status |
|------|--------|
| `phase1_ontology.yaml` | ✅ v1.1 (T-006/007/008 added) — ⚠️ not read by lints (O-05) |
| `Case_02_Phase1_RICH.xlsx` | ✅ 15 sheets |
| `RICH_VS_LEGACY.md` | ✅ FINAL (Sprint 3) |
| `PROJECT_STATE.md` | ✅ FINAL (Sprint 3) — this file |
| `scripts/generate_corpus_links.py` | ⚠️ stub (36 lines) |
| `scripts/filter_ambiguity_cards.py` | ⚠️ stub (40 lines) |
| `scripts/regenerate_ontology.py` | ⚠️ stub (43 lines) |
| `validation/` | ✅ 7 reports |

---

## §3 Sprint History

| Sprint | Date | Output |
|--------|------|--------|
| **Sprint 0** | 2026-08-06 | Skeleton (14 placeholders), 3 script stubs, lint baseline (6/6 PASS, 30 warnings), `corpus_field_map.md` |
| **Sprint 0.5** | 2026-08-06 | `07b` Track B instance — 35 active sub-domains, 8 RIGOROUS + 27 STANDARD, 3 NOT_ADDRESSED documented |
| **Sprint 1** | 2026-08-06 | Reconciliation — 10 docs + ontology v1.1 into Rich; `active_subdomains` 38 → 35; T-006/007/008 added; by-design section markers |
| **Sprint 3** | 2026-08-06 | `07b` §11 corpus cross-check (15 rows, 6 findings); README dashboard + navigation; `RICH_VS_LEGACY.md`; this file; Validator verdict |
| **Sprint 4** | 2026-08-06 | Adjusted objectives — `07c_Adjusted_Objectives.md` delivered with 70 objective cards | 
| **Sprint 5** | 2026-08-06 | DEEP enrichment — `07c` status promoted to DEEP_ENRICHED; 70 detail cards and 3 tensions expanded |

**Commits on `feature/aegis-p1-case02-rich`:** `5687792` (corpus cherry-pick) → `fff7915` (Sprint 0) → `1c74f6b` (Sprint 0.5) → `8decee0` (Sprint 1) → `973cc1e` (Sprint 2) → Sprint 3 *(uncommitted at time of writing)*.

---

## §4 Lint Status

```bash
python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_02_SecureBorder_Solutions"
```

**6/6 PASS · 0 errors · 33 warnings** · 958/958 regulatory references valid · 53 documents scanned.

| Lint | Result | Warnings |
|------|--------|---------:|
| `lint_company_context` | ✅ PASS | 0 |
| `lint_regulatory_mapping` | ✅ PASS | 1 |
| `lint_regulatory_references` | ✅ PASS | 0 |
| `lint_regulatory_ground_truth` | ✅ PASS | 7 |
| `lint_cross_document_consistency` | ✅ PASS | 1 |
| `lint_template_compliance` | ✅ PASS | 24 |

⚠️ **The 33 figure supersedes the "6 warnings" reported in Sprint 1.** `run_phase1_lints.py` is case-scoped (`--case` only) and scans legacy + Rich + `00_COMMON/` together; it cannot produce a Rich-only count. The Sprint 1 figure came from a synthetic mirror under `/tmp/opencode/` in which several warning-generating files were simply absent. Full analysis in `RICH_VS_LEGACY.md` §4.

All 33 are warnings, not errors. None causes a lint to fail.

---

## §5 Branch

- **Branch:** `feature/aegis-p1-case02-rich`
- **Base:** `main`
- **Working tree:** Sprint 3 edits uncommitted (no commits created by the Sprint 3 executor, per constraint)
- **PR readiness:** ⚠️ **NOT READY as a Phase 1 replacement.** The branch is safe to open as a **draft/review PR** — it is purely additive, touches no legacy, Phase 2/3, or corpus file, and all lints pass. It should not be merged as the substitution for legacy Phase 1 until O-01, O-02 and `07c` are closed.

---

## §6 Constraints Honoured

| Constraint | Status |
|------------|--------|
| No modification to legacy `01_PHASE1_CONTEXT/` | ✅ |
| No modification to Phase 2/3 docs | ✅ |
| No modification to any corpus file | ✅ |
| No git commits created | ✅ |
| `document_id: AEGIS-P2-RICH-*` on new docs | ✅ |
| Project YAML frontmatter + markdown conventions | ✅ |

---

## §7 Blocking & Outstanding Items

Full ledger in `RICH_VS_LEGACY.md` §5. Blocking subset:

| # | Item | Severity |
|---|------|----------|
| **O-01** | **F-01 — scale input.** `07b` sets `S = MEDIUM`; `proportionality_model.md` §2 puts 450 emp / €120M in **LARGE** on both axes (>250 emp, ≥€50M). Under LARGE, §5.1 makes all 35 rows RIGOROUS instead of 8 + 27. Invalidates the §3 distribution and the wording of `07b` §6 GATE-P check (c). | **BLOCKING** |
| **O-02** | **Active-set disagreement.** `05b` §2: NOT_ADDRESSED = {D-07.2, D-07.4, D-09.3}, D-08.3 ACTIVE. `07b` §4: excluded = {D-07.4, D-08.3, D-09.3}, D-07.2 ACTIVE. Both total 35, so no count-based lint fires. | **BLOCKING** |
| **O-03** | `07c_Adjusted_Objectives.md` delivered and marked DEEP_ENRICHED (Sprint 5). | CLOSED |
| **O-04** | `05b` §3 top-20 cards cover only 3 distinct GDPR clauses; zero CRA / NIS 2 / AI_Act cards. | HIGH |

Items O-05 → O-12 (MEDIUM/LOW: ontology path, D-04.3 qualifier, D-10.1 tension, T-002 citation, D-02.4 attribution, corpus casing, `corpus_field_map` DRAFT, missing templates) are catalogued in `RICH_VS_LEGACY.md` §5.

---

## §8 Next Steps (post-Rich)

**Required before promotion:**

1. **Adjudicate O-01** (orchestrator) — reclassify `S` to LARGE and re-tier §4, or record an explicit justified deviation from `proportionality_model.md` §2. Everything else in `07b` is verified and stable.
2. **Resolve O-02** — pick one canonical active-set and align `05b`, `07b`, `README.md`, and `phase1_ontology.yaml`.
3. **Sprint 4 — Adjusted Objectives** — fill `07c` from `07b` §4 tiers + L1 sub-SOs. Blocked by O-01: the tier column is `07c`'s primary input.
4. **Rework `05b` §3** (O-04) — select 20 *distinct* cards with CRA / NIS 2 / AI_Act representation.

**Optional, post-promotion:**

5. **Sprint 5 — DEEP enrichment** — per-clause analysis for the 8 RIGOROUS sub-domains (or all 35 if O-01 resolves to LARGE).
6. **Sprint 6 — Phase 2 adjusted requirements** — propagate tier / `evidence_depth` / `ownership` into Docs 08/11/14/15 per `07b` §7.
7. **Tooling** — add folder scoping to `run_phase1_lints.py` (O-05, O-12) so a Rich-only warning count becomes measurable.

---

## §9 See also

- `README.md` — Rich folder index + sprint dashboard
- `RICH_VS_LEGACY.md` — Rich ↔ legacy diff + outstanding-items ledger
- `07b_Proportionality_Profile.md` §11 — Sprint 3 corpus cross-check
- `validation/VALIDATOR_SPRINT3.md` — independent Sprint 3 verdict
- `validation/SPRINT3_REPORT.md` — Sprint 3 change list
- `../PROJECT_STATE.md` — case-wide state of record (unmodified)
