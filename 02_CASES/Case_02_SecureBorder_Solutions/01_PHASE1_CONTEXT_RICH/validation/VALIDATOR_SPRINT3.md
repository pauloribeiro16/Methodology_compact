---
document_id: AEGIS-P2-RICH-VALIDATOR-S3
title: Validator Report — Sprint 3 (Case_02 Phase 1 Rich Mode)
phase: 1
version: 1.0
created: 2026-08-06
author: Sprint 3 Validator (independent review)
status: FINAL
case: Case_02_SecureBorder_Solutions
verdict: CONDITIONAL_PASS
blocking_items: 2
frozen: false
---

# Validator Report — Sprint 3 (Case_02 Phase 1 Rich Mode)

> Independent review of `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/`.
> Every claim below was re-derived from the files and the corpus, not taken from prior sprint reports.

---

## §0 Verdict

# ⚠️ CONDITIONAL_PASS

**The folder is structurally complete, all 6 Phase 1 lints pass with 0 errors, and corpus linkage is genuine and deep.** Two blocking items prevent an unqualified PASS, and both are consistency defects rather than gaps in the work:

| # | Blocking item | Why it blocks |
|---|---------------|---------------|
| **V-01** | **`S = MEDIUM` contradicts `proportionality_model.md` §2.** SecureBorder is 450 employees / €120M revenue. The model defines `MEDIUM = ≤250 emp, <€50M` and `LARGE = >250 emp, ≥€50M`. The case exceeds **both** MEDIUM ceilings (1.8× employees, 2.4× revenue) and satisfies **both** LARGE criteria. Doc 04 §2 itself records size as "Medium-Large". | `S` is the first input to the §5.1 decision table. Under `S = LARGE`, `LARGE + BUILD_REQUIRED + MUST = RIGOROUS` for **all 35 rows** — not 8 RIGOROUS + 27 STANDARD. The headline Track B deliverable and `07b` §6 GATE-P check (c) both rest on a premise that fails cross-check. |
| **V-02** | **`05b` and `07b` disagree on which sub-domains are active.** `05b` §2: NOT_ADDRESSED = {D-07.2, D-07.4, D-09.3}, D-08.3 = ACTIVE. `07b` §4: excluded = {D-07.4, D-08.3, D-09.3}, D-07.2 = ACTIVE (STANDARD). | Both arrive at 35, so no count-based lint fires, but the two documents describe **different sets of 35**. Any Phase 2 consumer reading `05b` and `07b` together gets contradictory scope. |

**Neither item invalidates the sprint's output.** V-01 is a single upstream input that, once adjudicated, either confirms or uniformly re-tiers §4 — the 35 rows themselves, their attributes, and their corpus grounding are sound. V-02 is a 2-sub-domain reconciliation.

**Recommendation:** open the branch as a **draft PR** (it is purely additive and lint-clean), but do **not** promote the Rich folder over legacy Phase 1 until V-01 and V-02 close and `07c` is delivered.

---

## §1 Completeness

### 1.1 Phase 1 documents — 16 `.md` required

| # | File | Lines | Frontmatter | Substantive? |
|---|------|------:|-------------|--------------|
| 1 | `00_Taxonomy_Reference.md` | 256 | ✅ | ✅ |
| 2 | `01_INTAKE_FORM.md` | 611 | ✅ | ✅ |
| 3 | `04_Company_Context_Assessment.md` | 337 | ✅ | ✅ |
| 4 | `04a_Architecture_DataInventory.md` | 316 | ✅ | ✅ |
| 5 | `04b_Security_Posture.md` | 379 | ✅ | ✅ |
| 6 | `04c_ThirdParty_Landscape.md` | 303 | ✅ | ✅ |
| 7 | `04d_Org_Roles_RACI.md` | 414 | ✅ | ✅ |
| 8 | `05_Regulatory_Applicability.md` | 443 | ✅ | ✅ |
| 9 | `05b_Ambiguity_Register.md` | 632 | ✅ | ⚠️ see §3.2 |
| 10 | `06_Clause_Mapping_Matrix.md` | 301 | ✅ | ✅ |
| 11 | `07_Structured_Compliance_Matrix.md` | 444 | ✅ | ✅ |
| 12 | `07b_Proportionality_Profile.md` | 308 | ✅ | ✅ |
| 13 | `07c_Adjusted_Objectives.md` | 53 | ✅ | 🔴 **PLACEHOLDER** |
| 14 | `Citation_Index.md` | 127 | ✅ | ✅ |
| 15 | `corpus_field_map.md` | 211 | ✅ | ⚠️ still `DRAFT` |
| 16 | `README.md` | 214 | ✅ | ✅ |

**Result: 16/16 present** — ✅ count satisfied. **14/16 substantive.** `07c_Adjusted_Objectives.md` carries `status: DRAFT (placeholder)` and a `## Status` table of TODOs; it is one of the three headline "new in Rich" documents and is **not delivered**. `corpus_field_map.md` remains at Sprint 0 `DRAFT`.

Sprint 3 additionally created `RICH_VS_LEGACY.md` and `PROJECT_STATE.md` (18 `.md` total).

### 1.2 Required artefacts

| Artefact | Required | Found | Status |
|----------|----------|-------|--------|
| `phase1_ontology.yaml` | yes | 1,766 lines, v1.1 | ✅ (⚠️ not read by lints — §2.2) |
| `corpus_field_map.md` | yes | 211 lines | ✅ present, `DRAFT` |
| `README.md` substantive | yes | 214 lines, sprint dashboard + navigation + lint caveat | ✅ |
| `Case_02_Phase1_RICH.xlsx` | yes | **15 sheets** | ✅ |
| Validation reports | yes | **7** | ✅ |
| `scripts/` — 3 stubs | 3 | `generate_corpus_links.py` (36), `filter_ambiguity_cards.py` (40), `regenerate_ontology.py` (43) | ✅ 3/3 |

**Excel sheets verified (15):** `CORPUS_SUMMARY` (10 rows) · `COVER` (24) · `SYSTEMS` (14) · `DATA_STORES` (8) · `DATA_FLOWS` (13) · `PERSONAL_DATA` (9) · `THIRD_PARTIES` (23) · `ROLES_RACI` (64) · `MATURITY` (12) · `SUBDOMAINS` (39) · `REG_CHAIN` (105) · `COMPLIANCE` (39) · `GAPS` (13) · `PRIORITIES` (13) · `Corpus Cross-Reference` (39). `SUBDOMAINS` and `COMPLIANCE` at 39 rows = 38 sub-domains + header ✅.

**Validation reports (7):** `LINT_REPORT_BEFORE.md` (187) · `LINT_REPORT_AFTER_RECONCILE.md` (293) · `SPRINT1_REPORT.md` (242) · `SPRINT2_ENRICHMENT_REPORT_EXISTING.md` (115) · `SPRINT2_ENRICHMENT_REPORT_NEW.md` (102) · `VALIDATOR_SPRINT3.md` (this) · `SPRINT3_REPORT.md`.

**Housekeeping:** `scripts/__pycache__/` (3 `.pyc`) is committed and should be git-ignored — cosmetic, non-blocking.

---

## §2 Lint Verification

### 2.1 Result

```bash
python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_02_SecureBorder_Solutions"
```

| Lint | Status | Errors | Warnings |
|------|--------|-------:|---------:|
| `lint_company_context` | ✅ PASSED | 0 | 0 |
| `lint_regulatory_mapping` | ✅ PASSED | 0 | 1 |
| `lint_regulatory_references` | ✅ PASSED | 0 | 0 |
| `lint_regulatory_ground_truth` | ✅ PASSED | 0 | 7 |
| `lint_cross_document_consistency` | ✅ PASSED | 0 | 1 |
| `lint_template_compliance` | ✅ PASSED | 0 | 24 |

**✅ 6/6 PASS, 0 errors — confirmed.** Anti-hallucination is clean: **958/958 references valid**, 53 documents scanned.

### 2.2 Warning count — brief's figure not reproducible

The Sprint 3 brief states "6 warnings (post-Sprint 1)" and "−80% warnings eliminated". **The actual reproducible count is 33.** Root causes:

1. **`run_phase1_lints.py` is case-scoped, not folder-scoped.** Its only target argument is `--case <name>`; it walks the whole case (legacy + Rich + `00_COMMON/`). A Rich-only warning count is not obtainable from this tool. The Sprint 1 "6" came from a hand-built wrapper over a synthetic mirror at `/tmp/opencode/case02_rich_lint_target/`, where Rich content was copied into a stand-in `01_PHASE1_CONTEXT/`. `LINT_REPORT_AFTER_RECONCILE.md` §15 discloses this wrapper, so it was not concealed — but the headline "−80%" was carried into the brief without the scope caveat.
2. **5 of the 24 "eliminated" warnings were file omissions.** `LINT_REPORT_AFTER_RECONCILE.md` lines 72/104/128 state plainly that the 4 obligated-party warnings and the 1 domain-coverage warning vanished because `02_Regulatory_Mapping_Master.md` "is NOT in the Rich folder". The file still exists in the real case and still warns. That is not a repair.
3. **The T-006/007/008 fix is unreachable by the lints.** `lint_regulatory_ground_truth.py:184` and `lint_cross_document_consistency.py:127` load the ontology from `case_path/00_COMMON/phase1_ontology.yaml`. Sprint 1 added T-006/007/008 to the *Rich* copy, which the lint never opens — so all 3 warnings persist. The ontology edit is correct in substance but has no effect at the legacy path.

**Assessment:** this is a **measurement-scope error, not a regression.** 0 errors and 6/6 PASS hold. The +3 versus the Sprint 0 baseline of 30 is Rich documents adding template-extra/consistency warnings of the same by-design kinds already in the baseline. Corrected in `README.md`, `RICH_VS_LEGACY.md` §4, and `PROJECT_STATE.md` §4.

---

## §3 Corpus Linkage Spot-Check

### 3.1 `04a` — "Corpus Manifest Path" column

✅ **PASS (exceeds brief).** Column present at `04a_Architecture_DataInventory.md:167` alongside `NIST CSF Anchors`. The brief specified 35 rows; the table carries **38** — all sub-domains including the 3 NOT_ADDRESSED, which is the more complete choice and is documented as 38 in the doc's own changelog and §4 Corpus Provenance. 76 `manifest.json` references resolve to real corpus paths.

### 3.2 `05b` — ambiguity cards

⚠️ **PASS on count, FAIL on quality.**

- ✅ Brief requires ≥5 cards; **20** are documented (§3.01–3.20). §1 aggregate: 1,071 filtered Berry cards across 38 sub-domains. §2 per-sub-domain breakdown is complete (38 rows) and its counts are plausible against the corpus.
- 🔴 **The 20 cards are not 20 distinct ambiguities.** They cover only **3 distinct clauses**: `GDPR-CL23` Art. 9(2)(g) ×7 (3.01–3.07), `GDPR-CP15` Art. 32(1) ×11 (3.08–3.18), `GDPR-CP10` Art. 28(3)(g) ×2 (3.19–3.20). Cards 3.01 and 3.02 are **byte-identical** apart from the sub-domain label — same verbatim phrase, same analysis, same severity. §3 is a clause × sub-domain cross-product, not a top-20 selection.
- 🔴 **Zero CRA, NIS 2, or AI_Act cards** in §3, even though §2 shows CRA/NIS 2 among the highest-count regulations (D-09.1 = 88 cards across CRA/GDPR/NIS2). For a 4-regulation case this is a material coverage gap in the document's centrepiece section.
- ⚠️ Four rows in §2 have an **empty "Applicable regs" cell** (D-02.4, D-06.2, D-07.2, D-07.3) yet non-zero card counts. Corpus participants are non-empty for all four (e.g. D-07.3 = [NIS2, CRA], D-06.2 = [CRA]), indicating a filter defect — plausibly the upstream `AI_Act`/`AI_Act` casing split (finding F-06).

### 3.3 `04c` — verbatim regulatory quotes

✅ **PASS.** 18 `Art. 28` references with verbatim GDPR processor-obligation text, plus NIS 2 and AI_Act obligation quotes. All references validated by `lint_regulatory_references` (0 invalid across the case).

### 3.4 `07b` — 35 sub-domains, 8 RIGOROUS + 27 STANDARD

✅ **PASS, exactly as specified.** Machine-counted in §4: **35** tier rows + **3** exclusion rows = 38 total `D-XX.Y` rows. Tier tally: **RIGOROUS = 8**, **STANDARD = 27**, LIGHTWEIGHT/MINIMAL/DEFERRED = 0. The 8 RIGOROUS match the brief's list exactly (D-01.1, D-01.3, D-04.3, D-06.1, D-06.3, D-07.1, D-07.3, D-10.1).

### 3.5 Independent corpus re-derivation

I re-extracted `requirements.high_level.yaml` from all 38 sub-domain JSONs. Three `07b` structural claims are **corpus-confirmed** — they were inferred in Sprint 0.5 and are now verified:

| `07b` claim | Corpus evidence | Verdict |
|---|---|---|
| All active rows are `MUST`; no SHOULD/COULD ⇒ §5.2 and DEFERRED inapplicable | `priority = MUST` in **38/38** | ✅ CONFIRMED |
| LIGHTWEIGHT = 0 and MINIMAL = 0 (no INHERITABLE rows) | `scope_overlap = N` in **0/38** | ✅ CONFIRMED |
| Tier `verification_method` values respect the corpus floor | `verification_method = TEST` in 37/38 (`INSPECT` only at D-07.4, which §4 excludes); STANDARD (`TEST`+`DEMONSTRATE`) and RIGOROUS (`TEST`+`ANALYZE`+audit) are both supersets | ✅ CONFIRMED |

Substantive `considerations` cross-check on 15 rows: 9 clean matches, 5 matches-with-caveat, 1 mismatch (D-10.1 — corpus records a CRDA GENUINE TENSION the profile does not carry). Detail in `07b` §11.2/§11.3.

---

## §4 Track B Verification

| Check | Requirement | Result |
|-------|-------------|--------|
| §3 present | Tier Assignment Summary | ✅ Present — distribution table + 8-row RIGOROUS override list with per-row rationale |
| §4 present | Per-Sub-Domain Table, 35 rows | ✅ **35 rows**, all 9 attribute columns populated; 3 exclusions documented with reasons |
| §6 (a) | Tier for every ACTIVE sub-domain | ✅ PASS — 35/35 |
| §6 (b) | Five attributes non-empty per row | ✅ PASS — verified across all 35 rows; no `—` placeholders |
| §6 (c) | Tier consistent with §5 decision table | ⚠️ **PASS-as-written / PREMISE FAILS** — the derivation `(S=MEDIUM, I=BUILD_REQUIRED, P=MUST) → STANDARD` is correctly applied, and `I`/`P` are corpus-confirmed. But `S = MEDIUM` is wrong per §2 (**V-01**). With `S = LARGE`, the same table yields RIGOROUS for all 35. |
| §6 (d) | Critical-overload rule (eval Rule 11) | ✅ PASS — no SHOULD/COULD rows exist; 8 RIGOROUS overrides are bounded and individually justified |

**Track B §1 invariant — verified intact.** No `fit_criterion` and no HSO is modified anywhere in `07b`. §3's "No-tier relaxation" paragraph is accurate: the 24h NIS 2 deadline, AES-256, DPIA+FRIA, and Art. 9 safeguards are stated as tier-independent. **This holds regardless of how V-01 resolves** — the regulatory floor is untouched either way, which is why V-01 is a proportionality-calibration defect and not a compliance defect.

---

## §5 Consistency Verification

| Check | Result |
|-------|--------|
| `04d` `active_subdomains: 35` | ✅ PASS — line 12, with Sprint 1 I-02 reconciliation comment |
| `active_subdomains: 35` across all docs | ✅ PASS — **16/16** documents agree; 0 disagreements |
| `applicable_regs: [GDPR, CRA, NIS 2, AI_Act]` | ✅ PASS — **16/16** documents byte-identical; DORA correctly absent |
| Sprint status dashboard in `README` | ✅ PASS — all sprints 0/0.5/1/2/3 + Sprint 4 pending; blocking items surfaced |
| `document_id: AEGIS-P2-RICH-*` on new docs | ✅ PASS |
| **Active sub-domain *set*** | 🔴 **FAIL (V-02)** — `05b` §2 and `07b` §4 name different 3-sub-domain exclusion sets (differ on D-07.2 and D-08.3) while both totalling 35 |

V-02 is the class of defect the numeric consistency checks are blind to: every document agrees on **35**, so `lint_cross_document_consistency` is silent, while two documents describe different sets.

---

## §6 What I Verified vs Accepted

**Independently verified** (re-derived from files/corpus, not from sprint reports): file inventory and all line counts; Excel sheet names and row counts; lint execution and per-lint warning attribution; the lint source code paths for ontology loading; corpus `priority`/`verification_method`/`scope_overlap` across all 38 sub-domains; `considerations` text for 15 sub-domains; `07b` §4 row and tier counts by machine count; frontmatter consistency across all 16 documents; `05b` card duplication by direct byte comparison; the `proportionality_model.md` §2 scale table against Doc 04's stated size.

**Accepted without independent re-derivation:** the substantive regulatory *reasoning* in Docs 04/04a/04b/05/06/07 (delegated to `lint_regulatory_references`, 958/958 valid); Phase 2/3 completion status (read from `../PROJECT_STATE.md`); `05b`'s aggregate of 1,071 filtered cards (per-sub-domain counts sampled as plausible, not summed card-by-card); Sprint 1's 30-warning baseline (taken from `LINT_REPORT_BEFORE.md`).

---

## §7 Findings Ledger

| ID | Severity | Finding | Cross-ref |
|----|----------|---------|-----------|
| **V-01** | **BLOCKING** | `S = MEDIUM` contradicts `proportionality_model.md` §2; 450 emp / €120M is LARGE on both axes. Would re-tier all 35 rows to RIGOROUS. | `07b` §11.3 F-01; `RICH_VS_LEGACY.md` §5 O-01 |
| **V-02** | **BLOCKING** | `05b` and `07b` name different active-sub-domain sets (both total 35). | `RICH_VS_LEGACY.md` §5 O-02 |
| **V-03** | HIGH | `07c_Adjusted_Objectives.md` is an undelivered placeholder. | O-03 |
| **V-04** | HIGH | `05b` §3 "top-20" covers 3 distinct clauses; 3.01/3.02 byte-identical; zero CRA/NIS 2/AI_Act cards. | O-04 |
| **V-05** | MEDIUM | Brief's "6 warnings / −80%" not reproducible; actual 33 (measurement-scope error). | §2.2 |
| **V-06** | MEDIUM | Rich ontology v1.1 never read by lints (loaded from `00_COMMON/`). | O-05 |
| **V-07** | MEDIUM | `05b` §2 — 4 rows with empty "Applicable regs" but non-zero card counts (filter defect). | §3.2, F-06 |
| **V-08** | MEDIUM | D-04.3 unified-workflow claim omits the corpus's recipient-segregation qualifier. | F-02 / O-06 |
| **V-09** | MEDIUM | D-10.1 CRDA genuine tension (CRA Annex I (2)(l) opt-out vs mandatory monitoring) unrecorded. | F-03 / O-07 |
| **V-10** | LOW | T-002 cites AI_Act Art. 12 for retention; floor is Art. 19(1); D-05.3 has no AI_Act participant. | F-04 / O-08 |
| **V-11** | LOW | D-02.4 note cites NIS 2; corpus participants are [CRA, DORA, AI_Act]. | F-05 / O-09 |
| **V-12** | LOW | `corpus_field_map.md` still `DRAFT`; `scripts/__pycache__/` committed. | O-11 |

---

## §8 Constraint Audit

| Constraint | Verified | Method |
|------------|----------|--------|
| No modification to legacy `01_PHASE1_CONTEXT/` | ✅ | `git status` — no legacy paths touched |
| No modification to Phase 2/3 docs | ✅ | `git status` — no `02_PHASE2_*` / `03_PHASE3_*` paths |
| No modification to corpus | ✅ | `git status` — no `00_METHODOLOGY/PREPROCESSING*` paths; corpus read-only throughout |
| No git commits created | ✅ | `git log` head remains `973cc1e` (Sprint 2) |
| `AEGIS-P2-RICH-*` document IDs | ✅ | Frontmatter inspected on all new documents |

---

## §9 See also

- `07b_Proportionality_Profile.md` §11 — Sprint 3 corpus cross-check (findings F-01…F-06)
- `RICH_VS_LEGACY.md` §4–§5 — lint analysis + outstanding-items ledger (O-01…O-12)
- `PROJECT_STATE.md` §7–§8 — blocking items + next steps
- `SPRINT3_REPORT.md` — Sprint 3 change list
- `00_METHODOLOGY/REFERENCE/proportionality_model.md` §2, §5.1, §6.3, §6.4 — the spec V-01 is measured against
