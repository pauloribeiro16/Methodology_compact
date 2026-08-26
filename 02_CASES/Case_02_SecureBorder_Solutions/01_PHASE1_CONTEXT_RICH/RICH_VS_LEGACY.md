---
document_id: AEGIS-P2-RICH-DIFF
title: Rich vs Legacy — Diff Summary (Case_02)
phase: 1
version: 1.1
created: 2026-08-06
author: Sprint 3 Executor
status: FINAL
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
active_subdomains: 35
related_documents:
  - README.md
  - PROJECT_STATE.md
  - 07b_Proportionality_Profile.md
  - validation/VALIDATOR_SPRINT3.md
  - ../01_PHASE1_CONTEXT/
frozen: false
---

# Rich vs Legacy — Diff Summary (Case_02)

> Side-by-side comparison of `01_PHASE1_CONTEXT_RICH/` (corpus-enriched, Sprints 0–3) against `01_PHASE1_CONTEXT/` (legacy, frozen).
> **Legacy is read-only.** Nothing in this document implies a change to it.

> **Sprint 9 update (corr-Case02, 2026-08-10):** Full migration to corr-008 model. 6 commits on `feature/aegis-p2-case02-full-migration`. Diff below appended in §8.

---

## §1 Files Inventory

Line counts are actual (`wc -l`) as of Sprint 3 close.

| Doc | Legacy | Lines | Rich | Lines | Δ | Change |
|-----|--------|------:|------|------:|---:|--------|
| 00 Taxonomy Reference | `00_COMMON/00_Taxonomy_Reference.md` | 256 | `00_Taxonomy_Reference.md` | 256 | 0 | Relocated into the phase folder; content verbatim |
| 01 Intake | `00_COMMON/01_Company_Context.md` | 611 | `01_INTAKE_FORM.md` | 611 | 0 | **Renamed**; content verbatim (layered intake v2.0) |
| 04 Company Context | `04_Company_Context_Assessment.md` | 305 | same | 337 | +32 | Frontmatter reconciled; by-design section markers |
| 04a Architecture / Data Inventory | `04a_Architecture_DataInventory.md` | 219 | same | 316 | **+97** | **Enriched** — §3 gains `Corpus Manifest Path` + `NIST CSF Anchors` (38 rows); new §4 Corpus Provenance |
| 04b Security Posture | `04b_Security_Posture.md` | 243 | same | 379 | **+136** | **Enriched** — corpus requirement IDs per control area |
| 04c Third-Party Landscape | `04c_ThirdParty_Landscape.md` | 232 | same | 303 | **+71** | **Enriched** — verbatim GDPR Art. 28 / NIS 2 / AI_Act obligation text (18 Art. 28 references) |
| 04d Org Roles / RACI | `04d_Org_Roles_RACI.md` | 396 | same | 414 | +18 | **Enriched** — `Corpus Reg Req` column on §3 (10 tables) + §5; `active_subdomains` 38 → 35 |
| 05 Regulatory Applicability | `05_Regulatory_Applicability.md` | 394 | same | 443 | +49 | Frontmatter reconciled; by-design markers |
| **05b Ambiguity Register** | — | — | `05b_Ambiguity_Register.md` | 632 | **NEW** | **NEW IN RICH** — 1,071 filtered Berry cards; per-sub-domain breakdown (38 rows); 20 documented cards |
| 06 Clause Mapping Matrix | `06_Clause_Mapping_Matrix.md` | 214 | same | 301 | +87 | Frontmatter reconciled; corpus anchors |
| 07 Structured Compliance Matrix | `07_Structured_Compliance_Matrix.md` | 379 | same | 444 | +65 | Frontmatter reconciled; §3 regulation-name marker table (Sprint 1 I-03) |
| **07b Proportionality Profile** | — | — | `07b_Proportionality_Profile.md` | 308 | **NEW** | **NEW IN RICH** — Track B instance, 35 rows + §11 Sprint 3 corpus cross-check |
| **07c Adjusted Objectives** | — | — | `07c_Adjusted_Objectives.md` | 53 | **NEW** | ⚠️ **PLACEHOLDER ONLY** — `status: DRAFT (placeholder)`; Sprint 4 deliverable |
| **Citation Index** | — | — | `Citation_Index.md` | 127 | **NEW** | **NEW IN RICH** — corpus citation index |
| Corpus field map | — | — | `corpus_field_map.md` | 211 | **NEW** | Sprint 0 mapping aid; still `DRAFT` |
| Ontology | `00_COMMON/phase1_ontology.yaml` | 1766 | `phase1_ontology.yaml` | 1766 | 0 | v1.0 → **v1.1** — adds T-006/T-007/T-008; see §4 caveat |
| Excel companion | `Case_02_Phase1.xlsx` | 2 sheets | `Case_02_Phase1_RICH.xlsx` | **15 sheets** | +13 | 13 new sheets incl. `CORPUS_SUMMARY`, `SUBDOMAINS`, `REG_CHAIN`, `Corpus Cross-Reference` |
| Clause mapping Excel | `06_Clause_Mapping_Matrix.xlsx` | — | *(not carried)* | — | — | Superseded by the consolidated `_RICH.xlsx` |
| Design decisions log | `00_COMMON/03_Design_Decisions_Log.md` | — | *(not carried)* | — | — | Case-wide artefact; stays in `00_COMMON/` |
| Regulatory Mapping Master | `00_COMMON/02_Regulatory_Mapping_Master.md` | — | *(not carried)* | — | — | DEPRECATED artefact; deliberately excluded (see §4) |

**Totals:** legacy Phase 1 body = 8 docs / 2,382 lines (+ 3 `00_COMMON/` docs). Rich = **16 `.md` / 5,349 lines** (excluding this diff doc) + ontology + 15-sheet Excel + 3 script stubs + 7 validation reports.

**Net new documents in Rich: 5** — `05b`, `07b`, `07c` (placeholder), `Citation_Index.md`, `corpus_field_map.md`.

---

## §2 Corpus Linkage Summary

Layers per `00_METHODOLOGY/PREPROCESSING/` and `PREPROCESSING_by_domain/`.

| Layer | Source | Consumed by | Evidence in Rich |
|-------|--------|-------------|------------------|
| **L1 — SubDomains** | `PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.Y/D-XX.Y.{md,json}` | 04a, 04b, 04d, 05b, 07b, Citation_Index | 04a §3 `Corpus Manifest Path` (38 rows); 04d `Corpus Reg Req` (10 tables); 07b §11 cross-check (15 rows) |
| **L2 — Regulation / Articles** | `PREPROCESSING/Regulation/<REG>/02_SecurityRules_NIST.md`, `Articles/Art_N.md` | 04c, 05, 06, 07, Citation_Index | 04c verbatim Art. 28 / NIS 2 Art. 21 / AI_Act obligation text; 06 clause anchors |
| **L2 — Ambiguity** | `PREPROCESSING/Regulation/<REG>/Ambiguity/clause_cards.md` + JSON sidecars | 05b | 05b §2 per-sub-domain counts (38 rows, 1,071 cards); §3 20 documented cards |
| **L3 — CrossRegulation** | `PREPROCESSING/CrossRegulation/{DomainAnalysis,DeepAnalysis}/` | 04a, 05b, 07b, 07c | 07b §11 quotes CRDA pair verdicts (SAME / COMPLEMENTARY / CORRECTED) per sub-domain |
| **L4 — HSO / CSF** | `PREPROCESSING/00_Hierarchical_SecurityObjectives.md`, `NIST_CSF_2.0_subcategories.md` | 01, 05, 06, 07, 07b, 07c | 04a §3 `NIST CSF Anchors` column; Excel `REG_CHAIN` (105 rows) |

**Corpus facts newly verified in Sprint 3** (all 38 sub-domains, `requirements.high_level.yaml`):

| Field | Corpus value | Confirms |
|-------|--------------|----------|
| `priority` | `MUST` — 38/38 | 07b §2/§3: no SHOULD/COULD rows ⇒ §5.2 tier-drop and DEFERRED both inapplicable |
| `verification_method` | `TEST` — 37/38; `INSPECT` — 1/38 (D-07.4) | The TEST floor in both STANDARD and RIGOROUS tier definitions |
| `applicable_if.scope_overlap` | `N` — **0/38** | 07b §3: LIGHTWEIGHT = 0 and MINIMAL = 0 is corpus-grounded, not assumed |

**Known corpus-side defect (F-06):** regulation-name casing is inconsistent upstream — `AI_Act` at D-01.4/D-02.1/D-04.3/D-07.x vs `AI_Act` at D-05.1/D-05.2. This is the likely cause of the four empty "Applicable regs" cells (D-02.4, D-06.2, D-07.2, D-07.3) in `05b` §2.

---

## §3 Track B Distribution

Per `07b_Proportionality_Profile.md` §3, under the **as-written** `S = MEDIUM` assumption:

- **RIGOROUS: 8** — D-01.1 / D-01.3 (biometric Art. 9, HSM-backed key custody), D-04.3 (4-reg max-SLA 24h notification), D-06.1 / D-06.3 (NIS 2 supply chain + GDPR Art. 28 chain), D-07.1 / D-07.3 (AI_Act Art. 9 risk mgmt + CRA secure-by-default; NIS 2 SDLC / SLSA L3), D-10.1 (24/7 SOC + AI_Act Art. 72 post-market)
- **STANDARD: 27**
- **LIGHTWEIGHT / MINIMAL / DEFERRED: 0** — corpus-confirmed (no `scope_overlap: N` anywhere ⇒ nothing is INHERITABLE; MEDIUM + FTE > 1.0 rules out DEFERRED)
- **Total: 35** active of 38

⚠️ **This distribution is provisional.** Sprint 3 finding **F-01** (`07b` §11.3) shows the `S` input contradicts `proportionality_model.md` §2:

| Input | 07b as written | Model §2 table | 450 emp / €120M |
|-------|----------------|----------------|-----------------|
| MEDIUM band | claimed | ≤250 emp, <€50M | exceeds by 1.8× / 2.4× |
| LARGE band | rejected as "not yet LARGE" | >250 emp, ≥€50M | **satisfies both** |

Under `S = LARGE`, §5.1 gives `LARGE + BUILD_REQUIRED + MUST = RIGOROUS`, so the distribution becomes **RIGOROUS: 35, STANDARD: 0**. The regulatory floor is unaffected either way (Track B §1 invariant), but evidence depth and ownership shift on 27 rows. Awaiting orchestrator adjudication.

---

## §4 Lint Status

**Authoritative, reproducible result:**

```bash
python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_02_SecureBorder_Solutions"
# 6/6 passed, 0 errors, 33 warnings
```

| Milestone | Lints | Errors | Warnings | Scope |
|-----------|-------|-------:|---------:|-------|
| Sprint 0 (BEFORE) | 6/6 PASS | 0 | **30** | Whole case, legacy only |
| Sprint 1 (claimed) | 6/6 PASS | 0 | *6* | **Synthetic mirror** — not reproducible |
| Sprint 3 (actual) | 6/6 PASS | 0 | **33** | Whole case, legacy + Rich |

⚠️ **Correction to the Sprint 1 figure.** `SPRINT1_REPORT.md` and `LINT_REPORT_AFTER_RECONCILE.md` report "30 → 6 warnings (−80%)". That figure does **not** reproduce, for two structural reasons:

1. **`run_phase1_lints.py` is case-scoped, not folder-scoped.** It accepts only `--case <name>` and scans the entire case directory (53 documents: legacy + Rich + `00_COMMON/`). It cannot emit a Rich-only count. The 6-warning run used a hand-built wrapper over a mirror at `/tmp/opencode/case02_rich_lint_target/`, with Rich content copied into a stand-in `01_PHASE1_CONTEXT/`.
2. **Several "fixes" were file omissions, not repairs.** 5 of the 24 eliminated warnings (4 obligated-party + 1 domain-coverage) came from `02_Regulatory_Mapping_Master.md` simply not being copied into the mirror. The file still exists in the real case and still warns.

Additionally, the **T-006/007/008 ontology warnings persist** in the real repo: the lints load the ontology from `case_path/00_COMMON/phase1_ontology.yaml` (`lint_regulatory_ground_truth.py:184`, `lint_cross_document_consistency.py:127`), so the Rich `phase1_ontology.yaml` v1.1 that added those tension IDs is never read by the lint. The Sprint 1 fix is real but **unreachable** at the legacy ontology path.

**Warning breakdown at Sprint 3 (33 total, 0 errors):**

| Lint | Warnings | Nature |
|------|---------:|--------|
| `lint_company_context` | 0 | — |
| `lint_regulatory_mapping` | 1 | `02_Regulatory_Mapping_Master.md` — only 1 security domain mentioned |
| `lint_regulatory_references` | 0 | **958/958 references valid** (anti-hallucination clean, up from 453) |
| `lint_regulatory_ground_truth` | 7 | 3 × T-006/007/008 not in ontology (path issue above) + 4 obligated-party false positives in the DEPRECATED master |
| `lint_cross_document_consistency` | 1 | Regs mapped in Doc 06 not mentioned in Doc 07 coverage (`AIAct` name-normalisation artefact) |
| `lint_template_compliance` | 24 | "Extra section not in template" — by-design case extensions + 5 canonical templates absent from the repo |

The +3 net versus the Sprint 0 baseline of 30 is attributable to Rich documents adding template-extra and consistency warnings of the same by-design kinds already present in the baseline. **No warning is an error, and no lint fails.**

---

## §5 Outstanding Items

| # | Item | Severity | Owner |
|---|------|----------|-------|
| **O-01** | **F-01 — `S = MEDIUM` contradicts `proportionality_model.md` §2** (450 emp / €120M is LARGE on both axes). Blocks the §3 distribution and `07b` §6 GATE-P check (c). Resolve by re-tiering to LARGE **or** recording an explicit justified deviation. | **BLOCKING** | Orchestrator |
| **O-02** | **Active sub-domain set disagreement.** `05b` §2 marks NOT_ADDRESSED = {D-07.2, D-07.4, D-09.3} with D-08.3 ACTIVE; `07b` §4 excludes {D-07.4, D-08.3, D-09.3} with D-07.2 ACTIVE. Both total 35, so no count lint fires, but the sets differ on 2 sub-domains. | **BLOCKING** | Executor |
| **O-03** | **`07c_Adjusted_Objectives.md` is a 53-line placeholder** (`status: DRAFT (placeholder)`). One of the 3 headline "new in Rich" docs is not delivered. | HIGH | Sprint 4 |
| **O-04** | **`05b` §3 "Top-20" cards are not 20 distinct ambiguities.** They cover only 3 distinct GDPR clauses (GDPR-CL23 Art. 9(2)(g) ×7, GDPR-CP15 Art. 32(1) ×11, GDPR-CP10 Art. 28(3)(g) ×2); cards 3.01/3.02 are verbatim identical but for the sub-domain label. Despite §2 showing CRA/NIS 2 cards dominating the 1,071 total, §3 contains **zero** CRA / NIS 2 / AI_Act cards. | HIGH | Executor |
| **O-05** | Rich ontology v1.1 is not read by the lints (loaded from `00_COMMON/`). Either point the lints at the Rich copy or accept the 3 warnings as structural. | MEDIUM | Tooling |
| **O-06** | F-02 — D-04.3 unified-workflow claim needs the corpus's recipient-segregation qualifier on policy/evidence layers. | MEDIUM | Executor |
| **O-07** | F-03 — D-10.1 CRDA genuine tension (CRA Annex I (2)(l) opt-out vs mandatory monitoring) unrecorded; add as T-004 or justify non-application. | MEDIUM | Executor |
| **O-08** | F-04 — T-002 cites AI_Act Art. 12 for log retention; the retention floor is Art. 19(1), and D-05.3 has no AI_Act participant (GDPR + CRA only). | LOW | Executor |
| **O-09** | F-05 — D-02.4 note cites NIS 2; corpus participants are [CRA, DORA, AI_Act]. | LOW | Executor |
| **O-10** | F-06 — upstream corpus `AI_Act` / `AI_Act` casing inconsistency; likely cause of 4 empty reg cells in `05b` §2. | LOW | Corpus maintainer |
| **O-11** | `corpus_field_map.md` still `status: DRAFT` from Sprint 0. | LOW | Executor |
| **O-12** | 5 canonical templates absent from `00_METHODOLOGY/TEMPLATES/`, generating unavoidable template-compliance warnings. | LOW | Tooling |

---

## §6 Reviewer Quick-Start

**If you have 5 minutes** — read in this order:

1. `validation/VALIDATOR_SPRINT3.md` §Verdict — the CONDITIONAL_PASS and its 2 blocking items.
2. `07b_Proportionality_Profile.md` §11.3 — finding **F-01**, the one issue that changes numbers downstream.
3. §5 of this document — the full outstanding-items ledger.

**If you have 30 minutes** — add:

4. `07b_Proportionality_Profile.md` §3 + §4 — the tier distribution and all 35 rows.
5. `07b_Proportionality_Profile.md` §11.2 — the 15-row corpus cross-check table.
6. `05b_Ambiguity_Register.md` §1–§2 — the 1,071-card aggregate and per-sub-domain breakdown (then §3 to see O-04 for yourself: compare cards 3.01 and 3.02).
7. `04a_Architecture_DataInventory.md` §3–§4 — the densest corpus linkage in the folder.

**Verify the state yourself:**

```bash
# Lint: expect 6/6 passed, 0 errors, 33 warnings
python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_02_SecureBorder_Solutions"

# F-01: compare the scale table against the case facts
sed -n '42,52p' 00_METHODOLOGY/REFERENCE/proportionality_model.md
grep -n "450 employees" 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/04_Company_Context_Assessment.md

# O-02: the two conflicting active-set claims
grep -n "NOT_ADDRESSED" 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/05b_Ambiguity_Register.md | head
sed -n '141,146p'  02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/07b_Proportionality_Profile.md

# O-04: cards 3.01 and 3.02 differ only by sub-domain label
sed -n '100,137p' 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/05b_Ambiguity_Register.md
```

**What NOT to review here:** legacy `../01_PHASE1_CONTEXT/` (frozen), `../02_PHASE2_RULES/` and `../03_PHASE3_DECOMPOSITION/` (unchanged by Sprints 0–3), and any `00_METHODOLOGY/PREPROCESSING*` corpus file (read-only baseline).

---

## §7 See also

- `README.md` — Rich folder index + sprint dashboard
- `PROJECT_STATE.md` — localised Phase 1 Rich state
- `validation/VALIDATOR_SPRINT3.md` — Sprint 3 independent verdict
- `validation/SPRINT3_REPORT.md` — Sprint 3 change list
- `00_METHODOLOGY/REFERENCE/proportionality_model.md` — Track B spec (§2 scale table, §5 decision table, §6 tier attributes)
- `00_METHODOLOGY/REGULATORY_BASELINE.md` — frozen corpus contract

---

## §8 Sprint 9 Diff (corr-Case02, 2026-08-10)

Full migration to **corr-008** model. 6 commits on `feature/aegis-p2-case02-full-migration` (A → F).

| Doc | Old (corr-007) | New (corr-008) | Status |
|-----|-----------------|----------------|--------|
| 07c | 131 vendor refs | 0 (tech-free) | ✅ |
| 10 | 11 PG + 20 SG | 34 PO + 55 SO | ✅ |
| 11 | 30 CR + 15 BPR + 8 BPR-AI | 38 CR + 25 BPR (AI merged with framework flag) | ✅ |
| 12.xlsx | legacy IDs | PO/SO/CR/BPR | ✅ regenerated |
| 13.xlsx | did not exist | 3 sheets, 12 cols each | ✅ NEW |
| Phase 3 | UC/FR/NFR + AO/PSO linkage | refreshed | ✅ |

**Findings:** F-01 SETTLED, F-03/04/06 RESOLVED. F-02/F-05 still OPEN.
