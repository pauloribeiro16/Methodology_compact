# PORT-PARITY-2 — Independent Verification Report

> **Validator:** Independent (report-only; nothing fixed, no git mutations).
> **Date:** 2026-09-04. **Scope:** 16 commits `49aa5e4..7403269`.
> **Method:** every claim re-derived from disk reality, not from reports.

**Verdict: CLEAN-WITH-FINDINGS** — 0 BLOCKER · 4 MAJOR · 6 MINOR · 4 NIT.
Campaign parity claims hold (corr-013, graphs, dashboards, gates, bookkeeping).
Findings concentrate in the GENERATED v0 P3 docs and pre-existing graph data
carried through campaign rebuilds.

---

## A. corr-013 completeness — PASS

| Check | Result | Evidence |
|---|---|---|
| A1 old basenames in live C3 files | PASS — 0 hits (text files, any type) | `grep -rE "Doc16_Obligation_Derivation|…|Doc21_Framework_Mapping_Matrix"` over C3 = zero hits incl. historical reports |
| A1 phantom count | PASS — exactly 2 | `Doc20_NIST_Framework_Inputs`: `validation/PORT_census_v0.md:75` (historical) + `01_PHASE1_CONTEXT_RICH/PRODUCTION_FLOW.md:42` (cross-case note re C2 — legitimate) |
| A2 XLSX blind spot | PASS — 0 old names inside any xlsx | zipfile scan of `Case_03_Phase1_RICH.xlsx`, `12_Rules_Catalog.xlsx`, `22_Traceability_Matrix.xlsx`, `22_Traceability_Matrix_rich_v0.xlsx` (sharedStrings/inlineStr). Only new-numbering refs found (`Doc22_Use_Cases_Catalog.md`, `Doc26_Requirements_Allocation.md §3` — both exist). `18_Functional_Tree.drawio` (plain XML) has zero Doc tokens. No `.json` outside `data/` in C3. Note: C3 has no `13_Framework_Mappings.xlsx` (C2-only file) |
| A3 bare-number coherence | PASS w/ findings MINOR-1/2 | All DocNN refs in live files resolve to existing files; §-anchors verified (Doc20 §1/§4/§5/§5.1, Doc19 §4, Doc16 §4, Doc17 §3 all exist) |
| A4 C2 corr-013 non-applicability | PASS | C2 P2 = `Doc14_Obligation_Derivation … Doc19_Framework_Mapping_Matrix + Doc20_NIST_Framework_Inputs` (all present); zero C3-style names referenced anywhere in C2 (incl. historical) |
| A5 Doc21 gap | PASS — 0 live pointers | 15 `\bDoc21\b` hits total, all historical/log (`PORT_census_v0.md`, `VALIDATOR_UNMAPPED_AUDIT_v0.md`, `progress.json:160` change-log prose). Zero in live docs/scripts |

**MINOR-1** — stale legacy dir `02_PHASE2_RULES/` (no `_RICH`) still referenced in live C3 P1 files: `Doc11:600-603` (4 refs), `Doc14:466-468` (3 refs). Dir does not exist in any case. Pre-existing; corr-013 fixed the basenames inside these lines but left the dir (mixed signal). 
**MINOR-2** — `Doc13_Proportionality_Profile.md:~` prose uses legacy relative numbers "Doc 08 / Doc 11 / Doc 14 / Doc 15" with corrected basenames in parentheses (campaign rewrote same lines). Human-trip hazard in prose only.

## B. Graph JSON integrity — PASS for campaign-built graphs; pre-existing dangles carried

Verified on all 6 graphs (`C1/C2/C3 × P1/P2`), using `from`/`to` as endpoints (`source` = provenance, correctly ignored):

| Graph | nodes/links/audits/EV | dangling | invariants vs disk | forbidden scalars | audit node_ids | EV sources |
|---|---|---|---|---|---|---|
| C1_P1 | 456/1412/31/57 | **20** (pre-existing) | OK | 0 | 0 bad | 0 empty; 1 literal `Doc11 T-001` (acceptable) |
| C1_P2 | 216/433/1/0 | **24** (MAJOR-3) | OK | n/a | 0 bad | n/a |
| C2_P1 | 521/1205/8/59 | **26** (pre-existing content, carried through 49aa5e4 rebuild) | OK | 0 | 0 bad | 0 empty |
| C2_P2 | 278/356/4/0 | 0 | OK | n/a | 0 bad | n/a |
| C3_P1 | 749/2054/9/119 | 0 | OK | 0 | 0 bad | 0 empty; all resolve/literal |
| C3_P2 | 242/340/6/0 | 0 | OK | n/a | 0 bad | n/a |

- B1 stale pinned numbers: C2/C3 dashboard-builder `EXPECTED` dicts match graph invariants exactly (28 + 46 keys). **MINOR-3**: C1 `build_p2_graph.py:77` pins `obligations_total: 30` (stale; unused — line 510 computes 34; graph correct).
- B6 campaign-report counts vs disk: C3 P1 749/2054/9+119 EV ✓; C2 P2 278/356/4 ✓; C3 P2 242/340/6 ✓; C1 P2 216/433/1 ✓.

**MAJOR-3** — C1_P2 `data/phase2_graph.json` (built by campaign commit 7be0b3b) has 24 dangling `from/to` links: 20 × `MITIGATES`→`SO--D-XX.Y-NNN` (double-dash typo inherited from `control_set.yaml` trace.objectives, 16 occurrences at e.g. `:1278`) + 3 × →`SO-D-01.x-001`/`PO-D-01.3-001` (no such nodes) + 4 × `YIELDS` to same. Validator (`build_p2_dashboard.py --check`, 7 checks) has **no dangling check** — hence "7 checks PASS" is technically true but does not cover this. Pre-campaign provenance for the control_set typos (file last touched 7be7682); the graph artefact is campaign-built. Related: C2_P1 26 dangling (25 `CITES_OUTCOME`→bare `PR.DS-01`-style ids vs `NIST-`-prefixed nodes + 1 `HAS_TENSION_WITH` `CRA-AnnexI-2l`→`GDPR-C32_2`) — identical 26 pre-campaign (505-link era), carried into the campaign's 1205-link rebuild; C1_P1 20 dangling (untouched pre-campaign). Validator gap (no dangling check) applies to all case P1/P2 validators.

## C. Dashboards + smoke + identity — PASS

- C1: `python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py` → **16/16 PASS**, exit 0, identity purge OK.
- C2 identity leaks: C3 dashboards (P1, P1_Maturity, P2) — **0 hits** for TinyTask/SecureBorder/Case 01 variants. C2_P2_Dashboard — 9 `SecureBorder`/`SECUREBORDER` hits = Case_02's own identity (legitimate); 0 TinyTask.
- C3 number coherence (C3_P1_Dashboard): strap `749 nodes · 2054 links · Audits: 9` ✓; 5 × `YES` applicability markers (GDPR/CRA/NIS2/DORA/AI Act), 0 `NO` ✓; RACI 65×15 = graph `raci_activities: 65 / raci_roles: 15` ✓ (rendered data-driven, not a literal); tiers `[31,7]` present, matches `subdomains_rigorous: 31 / standard: 7` ✓.
- C4: `Case_02_P1_Maturity.html:777-781` contains the 0×0-canvas resize fix (same code as C3 standalone); smoke ✓.
- C5: suite discovers via `rglob` (16 unique paths, no duplicates) + 4 pinned `REQUIRED_DASHBOARDS` entries, all exist.

## D. Gates + state chain + git — PASS (claimed gates), 1 pre-existing red gate outside the set

- D1: 3 × `check_unmapped.py` (C1/C2/C3) **PASS**; `validation/check_implementation_posture_case02.py` + `_case03.py` **PASS**. All 5 claimed gates green.
- **MAJOR-4** — the 6th gate `validation/check_implementation_posture.py` (C1 root) **FAILs, exit 1, 8 `/maturi/` violations** (`Case_01 P2 PROJECT_STATE.md:32`, `C1 P1 PROJECT_STATE.md:8`, `Doc05:8/14/15/20/22`, `Doc12:8`). Verified identical failure at pre-campaign tree (`49aa5e4^`, archive run in /tmp) → pre-existing and outside the claimed 5-gate set; but bf811e2's "Doc05/Doc12 author+note rewords" did not make it green, and a human running the repo's C1 posture gate sees FAIL today. Recommend same treatment as F6 (waiver tokens or reword).
- D2 waiver diff-sanity: **PASS**. Gained tokens exactly as claimed — C1 (case-sensitive): `MODEL_CSF_STRICT`, `maturity_cur`, `maturity_tgt`, `maturity redesign`, `P1_Maturity.html`; C2 (lowercase): `model_csf_strict`, `maturity_cur`, `maturity_tgt`, `evidence model`, `maturity redesign`, `p1_maturity.html`; C3: first five, no `p1_maturity.html`. Nothing else added. Eyeballed every line waived solely by the new tokens (C2: 9 — all frontmatter provenance/file references; C3: 0). No scalar assignments masked.
- D3: `progress.json` ×2 valid JSON; `port_parity2_campaign_complete` 2026-09-04 entry present in both.
- D4: CHANGE_LOG_CENTRAL v6.8 + §0.4 2026-09-04 ✓; GLOBAL 6.8 + C2/C3 §1.1 rows + timeline row ✓; C2/C3 case PROJECT_STATEs updated 2026-09-04 with campaign sections ✓ (C1 case root untouched — correct, C1 was source-only). Stale-number grep: no live file claims 521/505 as current (all `505` hits are historical validation reports or the "505→1205 corrected" prose).
- **MINOR-4** — phase-level PROJECT_STATEs not refreshed: C3 P1 `updated: 2026-08-06`, C3 P2 / C2 P2 `updated: 2026-08-08` despite campaign content edits (corr-013 table rewrites); 0 `2026-09-04` mentions. Phase files appear to be legacy-era artefacts; case roots carry the campaign state.
- D5: `git status --porcelain` → 0 lines ✓; `git log` shows exactly the 16 campaign commits ✓; sampled 75bd626 / 468c500 / 637ccc5 — all paths inside claimed scope ✓.

## E. Generated P3 docs — 1 PASS, 2 findings (1 is a mis-reported "honesty" finding)

- E1: 11 files exist (KG_CHAINS/NIST_ANCHORS/RULE_FREEZE/CORPUS_LINKAGE ×2, TRACEABILITY_AUDIT C2, RICH_LINT ×2). All have ≥8 frontmatter fields + `GENERATED v0` banner.
- E2 **PASS**: C2 control_set 63 (38 CR + 25 BPR) = RULE_FREEZE 63, exact set equality, = Doc18 catalog; C3 78 (38 CR + 40 BPR) = RULE_FREEZE 78, exact equality, = Doc19.
- E3 **PASS (highest-value check)**: every node id cited in KG_CHAINS resolves to a node in that case's P1/P2 graph (two passes incl. aggressive regex; only false positives were relation names/headers). Bonus: quoted P1 relation histograms (RACI 631… / RACI 804…) match disk **exactly**.
- E4: C2 §2 table = recomputation **exactly** (GV8/ID12/PR26/DE8/RS3/other6, sums 63) ✓.
  **MINOR-5** (graded here, not MAJOR, because rows shown are individually correct but the table doesn't reconcile): C3 §2 table rows match recomputation (GV13/ID17/PR23/DE3/RS2/RC1/other8) **but 11 BPR controls whose `csf` field holds PF ids (first token CT.* ×7, CM.* ×4) appear in no row — column sums to 67 of 78**. Root cause: control_set BPR `csf` field holds PF anchors (C1-inherited convention); "(none/other)" should be 19, doc says 8.
- E5 verify_rich FAIL findings vs disk:
  - C2 25/84 Doc29 FRs with Source Rule `—`: **REAL** (25 dash rows / 84 unique FRs; NIT: 24 unique FRs — one duplicated row, cf. F5-C2-03) ✓; "10 distinct rules" ✓ exact.
  - C2 stale "53 rules (38 CR + 15 BP)": **REAL** (`Doc25_Requirements_Allocation.md:20,365`) ✓.
  - **MAJOR-1** — C3 "Doc31 NFR 56-vs-12 suspected truncation" (F5-C3-02 HIGH) is a **false positive on disk**: Doc31 defines all 56 NFR cards, complete with bodies; per-category sections restart numbering (`NFR-01…NFR-06` ×6 categories etc. → only 12 unique header names), and `verify_rich.py::parse_cards` keys a dict by id, collapsing 56 cards to 12. Summary table is internally consistent (12+10+12+10+6+6 = 56). There is no truncation; the queued human-review finding is inaccurate (hedged as "suspected", but wrong).
  - C3 Doc26 "63 rules" stale: **REAL** (`Doc26:15` "63 rules → 28 nodes", `:322`) ✓.
  - C3 BPR-D-12.1-001 unallocated: **REAL** (0 hits in Doc26; cited in Doc22/27/31/RULE_FREEZE) ✓.
  - C3 UC-99 dangling: **REAL** (0 hits in Doc22 catalog; 5+ refs in Doc23 + drawio) ✓.

## F. Known/accepted items — CONFIRMED

1. C3 `phase1_ontology.compact.json` `schema_version: null` — confirmed (cosmetic, known).
2. C3 P2 ends Doc20 / P3 starts Doc22 (Doc21 gap) — confirmed.
3. Phantom `Doc20_NIST_Framework_Inputs` — exactly 2 hits — confirmed.
4. Historical reports keep old numbering (PORT_census, VALIDATOR_*, SPRINT*, LINT_REPORT*) — confirmed.

---

## Finding register

| # | Sev | Section | Finding |
|---|---|---|---|
| MAJOR-1 | MAJOR | E5 | C3 F5-C3-02 "Doc31 NFR truncation" is a false positive — 56 complete cards exist; `parse_cards` id-collision artifact. Mis-reported in F5 report + commit 637ccc5 message |
| MAJOR-2 | — | — | *(reserved numbering; no second E-side major)* |
| MAJOR-3 | MAJOR | B2 | 24 dangling links in campaign-built C1_P2 graph (20 × `SO--D-` double-dash from control_set trace; validator lacks dangling check); +70 pre-existing dangles carried in C2_P1 (26) / C1_P1 (20) |
| MAJOR-4 | MAJOR | D1 | 6th gate `validation/check_implementation_posture.py` (C1) FAILs (8 `/maturi/` hits) — pre-existing (identical at baseline), outside claimed 5-gate set; recommend F6-style waiver/reword |
| MINOR-1 | MINOR | A3 | Stale `02_PHASE2_RULES/` dir refs, C3 Doc11/Doc14 (pre-existing, basenames now correct) |
| MINOR-2 | MINOR | A3 | C3 Doc13 legacy prose numbers "Doc 08/11/14/15" (corr-013 rewrote same lines) |
| MINOR-3 | MINOR | B1 | C1 `build_p2_graph.py:77` stale pinned `obligations_total: 30` (unused; graph correct at 34) |
| MINOR-4 | MINOR | D4 | Phase PROJECT_STATE `updated:` dates stale (C3 P1 08-06; C3/C2 P2 08-08) despite campaign content edits |
| MINOR-5 | MINOR | E4 | C3 NIST_ANCHORS §2 omits 11 PF-anchored BPRs — table sums 67/78; "(none/other)"=8 should be 19 |
| MINOR-6 | MINOR | B | C2_P1 compact ontology invariants (covered 35/active 35) vs builder+graph (38/34) — deliberate per builder comment; layer mismatch worth documenting |
| NIT-1 | NIT | C3 | "5/5" and "RACI 65×15" not literals in C3 P1 dashboard — data-driven; content correct (5 YES markers, 65/15 in graph) |
| NIT-2 | NIT | E5 | "25/84" counts dash rows (24 unique FRs — one dup row, already logged as F5-C2-03) |
| NIT-3 | NIT | A2 | C3 has no `13_Framework_Mappings.xlsx` (C2-only artefact; naming asymmetry) |
| NIT-4 | NIT | B4 | EV source literal `Doc11 T-001` (C1_P1/C2_P1) — doc-prose reference, not a node id; acceptable |

**Totals: 0 BLOCKER · 3 MAJOR (MAJOR-2 unused) · 6 MINOR · 4 NIT.**

## Recommended fix wave (for the orchestrator — not applied)

1. Re-run/reword Doc31-based finding: correct F5-C3-02 to "per-category NFR id collision (cosmetic numbering), no truncation" or fix `parse_cards` to key by (section, id).
2. Add a dangling-link check to the P1/P2 validators; fix `SO--D-*` in C1 `control_set.yaml` + rebuild C1_P2 graph; decide policy for the 46 pre-existing P1 dangles (bare-vs-`NIST-` prefixed ids).
3. Waive/reword the 8 C1 root-gate `/maturi/` hits (F6 pattern).
4. Patch C3 NIST_ANCHORS §2 (add CM/CT or fold into none/other=19).
5. Cosmetic: C1 builder pin 30→34 or delete; phase PROJECT_STATE `updated:` dates; Doc11/Doc14 dir refs; Doc13 prose numbers.
