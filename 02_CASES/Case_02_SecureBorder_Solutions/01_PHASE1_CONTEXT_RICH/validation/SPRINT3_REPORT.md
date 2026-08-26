---
document_id: AEGIS-P2-RICH-SPRINT3
title: Sprint 3 Report — Final Validation + Documentation (Case_02 Rich Mode)
phase: 1
version: 1.0
created: 2026-08-06
author: Sprint 3 Executor
status: FINAL
case: Case_02_SecureBorder_Solutions
sprint: 3
verdict: CONDITIONAL_PASS
frozen: false
---

# Sprint 3 Report — Final Validation + Documentation (Case_02 Rich Mode)

---

## §1 Summary

Sprint 3 closed Phase 1 Rich Mode with documentation, navigation, a corpus cross-check of the Track B profile, and an independent Validator review.

| Metric | Result |
|--------|--------|
| Tasks completed | **7 / 7** |
| Files created | 4 (`RICH_VS_LEGACY.md`, `PROJECT_STATE.md`, `VALIDATOR_SPRINT3.md`, `SPRINT3_REPORT.md`) |
| Files updated | 2 (`07b_Proportionality_Profile.md`, `README.md`) |
| Legacy / Phase 2-3 / corpus files touched | **0** |
| Git commits created | **0** (per constraint) |
| **Lint status** | ✅ **6/6 PASS, 0 errors, 33 warnings** |
| **Validator verdict** | ⚠️ **CONDITIONAL_PASS** — 2 blocking items |
| **Phase 1 Rich final status** | ⚠️ **NOT_READY** for promotion over legacy |

### 1.1 Headline outcome

The folder is **structurally complete and lint-clean**: 16/16 Phase 1 documents present, 15-sheet Excel, ontology v1.1, 3 script stubs, 7 validation reports, and 958/958 regulatory references valid. Corpus linkage is genuine and deep, not decorative.

The corpus cross-check (Task 1) did what it was meant to do — it **found something**. Two blocking defects surfaced:

1. **The Track B scale input is wrong (F-01 / V-01).** `07b` assigns `S = MEDIUM`. `proportionality_model.md` §2 defines `MEDIUM = ≤250 employees, <€50M` and `LARGE = >250 employees, ≥€50M`. SecureBorder is **450 employees / €120M** — exceeding both MEDIUM ceilings (1.8× / 2.4×) and satisfying both LARGE criteria. Doc 04 §2 itself records "Medium-Large". Under `S = LARGE`, §5.1 gives `LARGE + BUILD_REQUIRED + MUST = RIGOROUS` for **all 35 rows**, not 8 RIGOROUS + 27 STANDARD.
2. **`05b` and `07b` disagree on which sub-domains are active (V-02).** Both total 35, so no lint fires, but they name different exclusion sets.

**A third correction concerns this sprint's own brief.** The brief asked me to document "6 warnings, −80%". That figure is not reproducible: the documented command yields **33 warnings**. `run_phase1_lints.py` accepts only `--case` and scans the whole case (53 documents, legacy + Rich + `00_COMMON/`); the Sprint 1 "6" came from a synthetic mirror under `/tmp/opencode/` in which several warning-generating files were absent. I recorded 33 as authoritative rather than repeating the brief's figure. Detail in `RICH_VS_LEGACY.md` §4.

**What is not in doubt:** 0 errors, 6/6 lints pass, the Track B §1 invariant is intact (no `fit_criterion` or HSO altered anywhere), and no constraint was violated.

---

## §2 Per-Doc Change List

### 2.1 `07b_Proportionality_Profile.md` — UPDATED (239 → 308 lines, +69)

| Change | Detail |
|--------|--------|
| Frontmatter | `+ cross_checked_against_corpus: true`, `+ cross_check_sprint: 3`, `+ cross_check_scope: 15 of 35 rows spot-checked` |
| §8 Version History | `+` v1.1 row recording the cross-check and the 6 findings |
| **§11 NEW** | Sprint 3 Corpus Cross-Check — §11.1 method, §11.2 cross-check table, §11.3 findings, §11.4 verdict |

§11.2 cross-checks **15 rows** (43% of 35) covering all 10 macro-domains, both tiers, all 8 RIGOROUS overrides, plus D-07.4 as a negative control. Corpus source: `PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.Y/D-XX.Y.json` → `requirements.high_level.yaml`.

**Result: 14/14 in-scope rows match** on `verification_method` and tier definition. On `considerations`: 9 clean, 5 with caveat, 1 mismatch (D-10.1).

**No tier was changed.** Three `07b` claims moved from *inferred* to *corpus-confirmed*:

| Claim | Corpus evidence |
|-------|-----------------|
| All rows `MUST`; §5.2 tier-drop and DEFERRED inapplicable | `priority = MUST` in 38/38 |
| LIGHTWEIGHT = 0, MINIMAL = 0 (nothing INHERITABLE) | `scope_overlap = N` in **0/38** |
| Tier `verification_method` respects the corpus floor | `verification_method = TEST` in 37/38 (`INSPECT` only at excluded D-07.4) |

### 2.2 `README.md` — UPDATED (155 → 214 lines, +59)

| Change | Detail |
|--------|--------|
| Frontmatter | `version: 0.1 → 1.0`; `+ updated`; author credits Sprint 3 |
| **+ Sprint status dashboard** | All sprints 0 / 0.5 / 1 / 2 / 3 ✅ + Sprint 4 pending, with the 2 blocking items stated inline |
| Sprint plan | Stale 7-row plan demoted to "Original sprint plan (Sprint 0 intent)" with a note that themes were resequenced |
| **+ Navigation** | 4 tables — 16 Phase 1 docs (linked, real line counts, status), supporting artefacts, 7 validation reports, 15 Excel sheet names |
| **+ Lint status** | Reproducible command + `6/6 PASS, 0 errors, 33 warnings` + case-scope caveat correcting the −80% claim |
| Track B specifics | ⚠️ DISPUTED note on the MEDIUM rationale pointing at F-01 |
| Substitution rule | Amended — substitution has **not** occurred; Phase 2/3 still consume legacy |

### 2.3 `RICH_VS_LEGACY.md` — NEW (205 lines)

§1 Files Inventory (21-row legacy↔Rich diff with actual line counts and Δ) · §2 Corpus Linkage Summary (L1–L4 + newly verified corpus facts) · §3 Track B Distribution (with the F-01 provisional warning) · §4 Lint Status (33 authoritative + full analysis of the non-reproducible −80%) · §5 Outstanding Items (**O-01…O-12**) · §6 Reviewer Quick-Start (5-min and 30-min paths + copy-paste verification commands) · §7 See also.

### 2.4 `PROJECT_STATE.md` — NEW (180 lines)

§1 Status · §2 Deliverables · §3 Sprint History (+ commit chain) · §4 Lint Status · §5 Branch · §6 Constraints Honoured · §7 Blocking & Outstanding · §8 Next Steps · §9 See also. Localised to the Rich folder; case-wide `../PROJECT_STATE.md` left unmodified.

### 2.5 `validation/VALIDATOR_SPRINT3.md` — NEW (228 lines)

§0 Verdict (CONDITIONAL_PASS + 2 blocking) · §1 Completeness · §2 Lint Verification · §3 Corpus Linkage Spot-Check · §4 Track B Verification · §5 Consistency Verification · §6 **What I Verified vs Accepted** · §7 Findings Ledger (V-01…V-12) · §8 Constraint Audit · §9 See also.

### 2.6 `validation/SPRINT3_REPORT.md` — NEW (this file)

### 2.7 Files deliberately NOT modified

`01_PHASE1_CONTEXT/` (legacy, frozen) · `02_PHASE2_RULES/`, `03_PHASE3_DECOMPOSITION/` · `00_METHODOLOGY/PREPROCESSING*` (corpus, read-only) · `../PROJECT_STATE.md` (case-wide) · `00_COMMON/` · `07c_Adjusted_Objectives.md` (Sprint 4 scope — deliberately left as placeholder rather than stubbed with filler).

---

## §3 Track B Distribution

Per `07b` §3, under the **as-written** `S = MEDIUM`:

| Tier | Count | Corpus-verified? |
|------|------:|------------------|
| **RIGOROUS** | **8** | ✅ all 8 spot-checked in §11.2 |
| **STANDARD** | **27** | ✅ 6 of 27 spot-checked |
| LIGHTWEIGHT | 0 | ✅ confirmed — `scope_overlap = N` in 0/38 |
| MINIMAL | 0 | ✅ same |
| DEFERRED | 0 | ✅ confirmed — `priority = MUST` in 38/38 |
| **Total** | **35** | of 38 (3 excluded) |

**RIGOROUS (8):** D-01.1 + D-01.3 (biometric Art. 9, HSM-backed key custody) · D-04.3 (4-reg max-SLA 24h) · D-06.1 + D-06.3 (NIS 2 supply chain + GDPR Art. 28 chain) · D-07.1 + D-07.3 (AI_Act Art. 9 + CRA secure-by-default; NIS 2 SDLC / SLSA L3) · D-10.1 (24/7 SOC + AI_Act Art. 72).

⚠️ **Provisional.** If F-01 resolves to `S = LARGE`, the distribution becomes **RIGOROUS: 35, STANDARD: 0**. The regulatory floor is unaffected (Track B §1 invariant); evidence depth and ownership shift on 27 rows.

---

## §4 Lint Final State

```bash
python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_02_SecureBorder_Solutions"
# 📊 Summary: 6/6 passed
# ⚠️ 33 warning(s)
# ✅ All Phase 1 lints passed!
```

| Lint | Status | Errors | Warnings | Nature of warnings |
|------|--------|-------:|---------:|--------------------|
| Company Context | ✅ PASSED | 0 | 0 | — |
| Regulatory Mapping | ✅ PASSED | 0 | 1 | DEPRECATED `02_Regulatory_Mapping_Master.md` |
| Regulatory References | ✅ PASSED | 0 | 0 | **958/958 valid** |
| Regulatory Ground Truth | ✅ PASSED | 0 | 7 | 3 × T-006/007/008 (ontology path) + 4 obligated-party false positives |
| Cross-Document Consistency | ✅ PASSED | 0 | 1 | `AIAct` name-normalisation artefact |
| Template Compliance | ✅ PASSED | 0 | 24 | by-design case extensions + 5 templates absent from repo |

**✅ 6/6 PASS, 0 errors.** All 33 are warnings; none fails a lint. The +3 vs the Sprint 0 baseline of 30 is Rich documents adding template-extra/consistency warnings of kinds already present in the baseline.

---

## §5 Outstanding Items

| # | Item | Severity | Owner |
|---|------|----------|-------|
| **O-01** | **F-01 / V-01 — `S = MEDIUM` contradicts `proportionality_model.md` §2.** Re-tier to LARGE, or record an explicit justified deviation. | **BLOCKING** | Orchestrator |
| **O-02** | **V-02 — active-set disagreement** between `05b` §2 {D-07.2, D-07.4, D-09.3} and `07b` §4 {D-07.4, D-08.3, D-09.3}. | **BLOCKING** | Executor |
| **O-03** | `07c_Adjusted_Objectives.md` placeholder (53 lines). | HIGH | Sprint 4 |
| **O-04** | `05b` §3 top-20 = 3 distinct clauses; 3.01/3.02 byte-identical; zero CRA/NIS 2/AI_Act cards. | HIGH | Executor |
| **O-05** | Rich ontology v1.1 not read by lints (loaded from `00_COMMON/`). | MEDIUM | Tooling |
| **O-06** | F-02 — D-04.3 needs the recipient-segregation qualifier on policy/evidence layers. | MEDIUM | Executor |
| **O-07** | F-03 — D-10.1 CRDA genuine tension unrecorded (add T-004 or justify). | MEDIUM | Executor |
| **O-08** | F-04 — T-002 cites AI_Act Art. 12; retention floor is Art. 19(1); D-05.3 has no AI_Act participant. | LOW | Executor |
| **O-09** | F-05 — D-02.4 cites NIS 2; corpus participants [CRA, DORA, AI_Act]. | LOW | Executor |
| **O-10** | F-06 — upstream corpus `AI_Act`/`AI_Act` casing split; likely cause of 4 empty reg cells in `05b` §2. | LOW | Corpus maintainer |
| **O-11** | `corpus_field_map.md` still `DRAFT`; `scripts/__pycache__/` committed. | LOW | Executor |
| **O-12** | 5 canonical templates absent from `00_METHODOLOGY/TEMPLATES/`. | LOW | Tooling |

---

## §6 Sprint 4 Readiness

**Status: ⚠️ BLOCKED on O-01.**

Sprint 4's deliverable is `07c_Adjusted_Objectives.md`, whose primary input is the per-sub-domain **tier** column from `07b` §4. If O-01 resolves to `S = LARGE`, all 27 STANDARD rows become RIGOROUS and every adjusted objective derived from them changes. Writing `07c` before O-01 is adjudicated would guarantee rework.

**Recommended order:**

| Step | Action | Owner | Gate |
|------|--------|-------|------|
| 1 | Adjudicate O-01 — LARGE re-tier, or documented deviation | Orchestrator | — |
| 2 | Resolve O-02 — one canonical active set across `05b` / `07b` / `README` / ontology | Executor | — |
| 3 | Re-run `07b` §11 cross-check if tiers changed | Executor | 07b §6 GATE-P |
| 4 | **Sprint 4** — write `07c` from settled tiers | Executor | GATE-P |
| 5 | Rework `05b` §3 (O-04) — 20 distinct cards with CRA/NIS 2/AI_Act coverage | Executor | — |
| 6 | Promote Rich over legacy | Orchestrator | Validator re-review |

**Ready now, independent of O-01:** O-04 (`05b` §3 rework), O-06…O-09 (documentation-precision fixes), O-11 (housekeeping).

**Phase 1 Rich final status: NOT_READY** for promotion. The branch is safe to open as a **draft PR** — purely additive, no legacy/Phase 2-3/corpus file touched, 6/6 lints pass with 0 errors.

---

## §7 Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-06 | Sprint 3 Executor | Sprint 3 completion report. 7/7 tasks. 4 files created, 2 updated. Lint 6/6 PASS / 0 errors / 33 warnings (corrects the brief's non-reproducible "6 / −80%"). Validator verdict CONDITIONAL_PASS with 2 blocking items (V-01 scale input, V-02 active-set disagreement). |

---

## §8 See also

- `VALIDATOR_SPRINT3.md` — independent Sprint 3 verdict (V-01…V-12)
- `../07b_Proportionality_Profile.md` §11 — corpus cross-check (F-01…F-06)
- `../RICH_VS_LEGACY.md` — legacy diff + outstanding ledger (O-01…O-12)
- `../PROJECT_STATE.md` — localised Phase 1 Rich state
- `../README.md` — sprint dashboard + navigation
- `SPRINT1_REPORT.md`, `SPRINT2_ENRICHMENT_REPORT_*.md` — prior sprint reports
