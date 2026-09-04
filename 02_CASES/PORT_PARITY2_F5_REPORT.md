# PORT-PARITY-2 · Block F5 Report — Case_01 Phase 3 RICH layer → Case_02 + Case_03

**Executor:** AEGIS Executor (campaign PORT-PARITY-2, block F5)
**Date:** 2026-09-04
**Base:** Case_01 `03_PHASE3_DECOMPOSITION_RICH/` (scripts + narrative-doc layer) + F4's P2 ports (control_set.yaml, P1/P2 graph JSONs)
**Git:** tree left dirty by design — NO commits made (orchestrator verifies and commits)

---

## 1. What was ported, per case

Into each case's `03_PHASE3_DECOMPOSITION/scripts/` (4 scripts; the 3 mandated ports + 1 generator so the narrative docs are reproducible):

| Script | Port notes |
|---|---|
| `verify_rich.py` | Case_01's xlsx stub upgraded (per its own docstring promise) into a real structural checker: 8 checks — frontmatter 8-field completeness, FR/NFR/UC/rule id censuses vs each doc's own claimed counts, dangling rule refs vs control_set, corr-008 cross-refs, rule-traceability coverage. Parsers adapted per case (C2: table-style Doc29; C3: card-style Doc30/Doc31, GATE-D-XX-NN gate cards). |
| `build_traceability_matrix_rich.py` | Unlike Case_01's hard-coded freeze tables, this port PARSES live artefacts (control_set.yaml, FR/NFR docs, UC catalog rule lines, allocation tables, gate cards, P2 graph JSON). Emits `22_Traceability_Matrix_rich_v0.xlsx` (9 sheets) **alongside** — legacy `22_Traceability_Matrix.xlsx` untouched in both cases. |
| `gen_drawio.py` | Mermaid→drawio port. C2: Doc27 mermaid → `18_Functional_Tree.drawio` (29 nodes/28 edges). C3: Doc28 mermaid → `18_Functional_Tree.drawio` (53 nodes/52 edges, nested `[T]` track tags re-closed). Neither case had the file before (both doc frontmatters listed it as pending). XML parse-back validated. |
| `gen_narrative_docs_v0.py` | Emits RULE_FREEZE / KG_CHAINS / NIST_ANCHORS / CORPUS_LINKAGE v0 mechanically from control_set.yaml + P1/P2 graph JSONs + live P3 doc censuses. 8-field frontmatter + `GENERATED v0 (PORT-PARITY-2)` banner on every doc. |

Case_02 additionally got `scripts/audit_traceability_v0.py` → emits `02_PHASE2_RULES_RICH/TRACEABILITY_AUDIT.md` (deliverable 5; structure follows Case_03's P2 audit, scoped to the P3 layer C3's audit does not cover).

## 2. Files created (all NEW — git status shows only untracked files; zero modifications to existing deliverables)

**Case_02** (`03_PHASE3_DECOMPOSITION/` unless noted): `RULE_FREEZE.md`, `KG_CHAINS.md`, `NIST_ANCHORS.md`, `CORPUS_LINKAGE.md`, `22_Traceability_Matrix_rich_v0.xlsx`, `18_Functional_Tree.drawio`, `scripts/{verify_rich,build_traceability_matrix_rich,gen_drawio,gen_narrative_docs_v0,audit_traceability_v0}.py`, `validation/RICH_LINT_BASELINE.md`; plus `../02_PHASE2_RULES_RICH/TRACEABILITY_AUDIT.md` (new file only).

**Case_03** (same layout, no audit — already existed): the 4 narrative docs, `22_Traceability_Matrix_rich_v0.xlsx`, `18_Functional_Tree.drawio`, the 4 scripts, `validation/RICH_LINT_BASELINE.md`.

## 3. Script run results (exit codes, counts)

| Script | Case_02 | Case_03 |
|---|---|---|
| `verify_rich.py` | **exit 1 — honest FAIL** (2 FAIL / 6 PASS) | **exit 1 — honest FAIL** (3 FAIL / 5 PASS) |
| `build_traceability_matrix_rich.py` | exit 0 — 63 rules, 84 FRs (59 mapped/25 `—`), 56 NFRs, 38 gates, 61 allocations, 278n/356l | exit 0 — 78 rules, 72 FRs (62 mapped), 12 NFR cards, 62 UCs w/ rules, 115 alloc rows, 40 gates, 242n/340l |
| `gen_drawio.py` | exit 0 — 29 nodes/28 edges, XML parse-back OK | exit 0 — 53 nodes/52 edges, parse-back OK, 0 malformed labels |
| `gen_narrative_docs_v0.py` | exit 0 — 4 docs (18.2k/6.5k/9.0k/3.0k chars) | exit 0 — 4 docs (22.5k/7.6k/11.8k/3.1k chars) |
| `audit_traceability_v0.py` | exit 0 — 7.3k chars, 63-rule × 4-layer coverage matrix | n/a |

KG_CHAINS content: real derivation chains per regulation (C2: 4 chains GDPR/CRA/NIS2/AIAct citing `GDPR-C04`, `CRA-C07`, `NIS2-C18`, `AI-C17`; C3: 5 chains + DORA citing `DORA-C09`), with verbatim P1/P2 node ids; graph-edge hops labelled with their relation, id-convention hops labelled `ID-join` (honest: P1↔P2 graphs have no cross-graph edges).

## 4. Lint findings needing human attention (P7)

**Case_02** (RICH_LINT_BASELINE §4): F5-C2-01 HIGH — FR-level rule traceability sparse (25/84 Doc29 FRs have Source Rule `—`; only 10 distinct rules cited at FR level; catalog-level coverage is 63/63 via Doc25/Doc26). F5-C2-02 MEDIUM — stale "53 rules (38 CR + 15 BP)" claims in Doc25 pre-dating the 63-control renumbering. F5-C2-03 LOW — Doc29 duplicated FR-71/FR-72 rows. F5-C2-04 LOW — Doc21–Doc28 frontmatter missing `case:` (7/8 fields). All content edits — outside F5 touch-scope.

**Case_03** (RICH_LINT_BASELINE §4): F5-C3-02 HIGH — Doc31 claims "Total NFRs 56" (summary rows 12+10+12+10+6+6) but defines only 12 NFR cards; suspected body truncation. F5-C3-06 MEDIUM — 5 FR cards cite raw articles (AI-C09, AI-C10, DORA-C38, "GDPR Art. 35", "AI Act Art. 28") instead of catalog rule ids. F5-C3-01 MEDIUM — Doc26 still says "63 rules (38 CR + 25 BPR)" vs frozen 78. F5-C3-03 LOW — BPR-D-12.1-001 not allocated in Doc26 §3. F5-C3-04 LOW — Doc23 references nonexistent UC-99. F5-C3-05 LOW — frontmatter `case:` missing on Doc22–Doc29. F5-C3-07 INFO — CR-D-05.4-001's "N/A — não mapeado a CSF 2.0" is the single deliberate CSF gap (documented, not a defect).

`verify_rich` FAILs are **not faked to PASS** — they reflect the real findings above; exit code 1 is the honest baseline verdict.

## 5. Gates re-run after changes

| Gate | Result |
|---|---|
| check_unmapped C1 / C2 / C3 | **3× exit 0 GATE PASS** (new .md files are inside the scans' scope — C2/C3 re-verified after every doc emission) |
| repo-root posture case02 / case03 | **2× exit 0 GATE PASS** |
| `test_dashboards.py` full smoke | **16/16 PASS** (no dashboards added; no regression) |
| Frontmatter check on all 11 new .md | 8/8 fields + banner present on every file |
| PF/AI-RMF tokens in new docs vs frozen vocabularies | 0 violations (all anchors copied verbatim from control_set.yaml, which is gate-clean) |

## 6. Scope notes

* Touched only: both cases' `03_PHASE3_DECOMPOSITION/**` (new files) + the single new `Case_02/02_PHASE2_RULES_RICH/TRACEABILITY_AUDIT.md`. No DocNN content modified; no `kg/**`, no methodology files, no snapshots needed (no browser work).
* No `git add`/`git commit` performed.
* Banner vocabulary kept gate-safe: the one verbatim status string containing a legacy-scoped token quotes the control_set wording containing the waiver word, so posture/unmapped gates stay PASS without weakening them.
