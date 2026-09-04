---
document_id: AEGIS-C02-P3-RICH-LINT-BASELINE
title: RICH Lint Baseline v0 (Case_02 Phase 3, PORT-PARITY-2)
phase: 3
version: 0.0
created: 2026-09-04
updated: 2026-09-04
author: PORT-PARITY-2 Executor (generated)
status: GENERATED
case: Case_02_SecureBorder_Solutions
sibling_doc: ../ (Case_01: 03_PHASE3_DECOMPOSITION_RICH/validation/RICH_LINT_BASELINE.md)
---

# RICH Lint Baseline v0 — Case_02 Phase 3

> **GENERATED v0 (PORT-PARITY-2) — pending human review.** Mechanically derived from
> `scripts/verify_rich.py` runs over Doc21–Doc30 + requirements/Doc29–Doc30 +
> `../02_PHASE2_RULES_RICH/control_set.yaml`, plus the ad-hoc greps listed in §3;
> verify before relying on it.

---

## §1 Snapshot metadata

| Field | Value |
|-------|-------|
| Date captured | 2026-09-04 |
| Runner | `python3 scripts/verify_rich.py` (ported from Case_01's RICH folder, adapted to Case_02 id spaces) |
| Target folder | `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/` |
| Rule universe | `../02_PHASE2_RULES_RICH/control_set.yaml` v6.0 — 63 controls (38 CR + 25 BPR) |
| verify_rich exit code | **1** (2 FAIL / 6 PASS — honest result, findings listed below) |

---

## §2 verify_rich results (verbatim verdicts)

| Check | Verdict | Detail |
|---|---|---|
| CHK-0 sources | PASS | control_set.yaml v6.0: 63 controls (38 CR + 25 BPR) |
| CHK-1 frontmatter (8 corr-008 fields) | **FAIL** | all 8 DocNN docs (Doc21–Doc28) miss the `case:` field (7/8 present) |
| CHK-2 FR census | **FAIL** | 84 unique FR ids match `totalFRs=84`, but FR-71 and FR-72 rows are duplicated in Doc29 tables |
| CHK-3 NFR census | PASS | 56 unique NFR ids (NFR-001…NFR-056) match `totalNFRs=56` |
| CHK-4 rule refs / dangling | PASS | 63 distinct rule refs across P3 docs; 0 dangling (all resolve against control_set 63) |
| CHK-5 UC census | PASS (info) | 47 detailed `U.C.*` ids + 7 packages (DP/SEC/IAM/DEV/GOV/AI/TRN); catalog version history claims 44 UCs — mixed id space, no dangling refs |
| CHK-6 corr-008 cross-refs | PASS | every Doc29 `Source Rule` token well-formed and resolvable; Doc26 gate→rule and gate→FR refs resolvable |
| CHK-7 rule traceability coverage | PASS (with caveat) | 63/63 rules referenced by ≥1 P3 doc; **but** FR-level Source Rule covers only 10 rules (see F5-C2-01) |

---

## §3 Ad-hoc greps (complementary census)

| Grep | Result | Verdict |
|---|---|---|
| `U.C.*` refs in Doc25/Doc26/Doc27 resolving to Doc21 catalog | 0 dangling | PASS |
| Doc30 `AG-D-XX.X-NNN` refs (26 distinct) resolving against P1 graph AdjustedGoal nodes | 0 dangling | PASS |
| Doc29 FR table row count vs unique FR ids | 86 rows / 84 unique → FR-71, FR-72 duplicated | **FAIL** (F5-C2-03) |
| frontmatter `case:` field across Doc21–Doc28 | 0/8 carry it | **FAIL** (F5-C2-04) |
| stale rule-count claims (Doc25 “53 rules (38 CR + 15 BP)”, “all 53 compliance rules”) | found (see RULE_FREEZE.md §3) | FINDING (F5-C2-02) |

---

## §4 Findings requiring human attention (P7)

| # | Severity | Finding | Disposition |
|---|---|---|---|
| F5-C2-01 | HIGH | **FR-level rule traceability sparse**: 25/84 Doc29 FRs carry Source Rule `—`; only 10 distinct rules cited at FR level (FR→rule gap; Doc25 allocation and Doc26 gates close the gap at catalog level, 63/63 covered somewhere in P3). | Fixing requires editing Doc29 content — outside F5 touch-scope. Recorded in `../02_PHASE2_RULES_RICH/TRACEABILITY_AUDIT.md` §5. |
| F5-C2-02 | MEDIUM | Stale count claims pre-dating the P2 renumbering to 63 controls (Doc25 “53 rules (38 CR + 15 BP)” + “all 53 compliance rules”; catalog claims “44 UCs” vs 47 detailed U.C.* ids). | Requires DocNN content edits — outside F5 touch-scope. Census in RULE_FREEZE.md §3. |
| F5-C2-03 | LOW | Doc29 duplicated FR rows (FR-71, FR-72 appear twice in the domain tables). | Content edit — outside F5 touch-scope. |
| F5-C2-04 | LOW | Doc21–Doc28 frontmatter missing the `case:` field (corr-008 8-field completeness: 7/8 present). | Content edit — outside F5 touch-scope. |
| F5-C2-05 | INFO | Mixed UC id spaces in Doc21 (U.C.X.Y.Z detailed cards, UC-SECUREBORDER-2026-001 catalog id, UC-XX package labels). Contextually resolvable; 0 dangling refs. | No action required; noted for future UC renumbering (corr-0xx). |

**No PASS was faked**: CHK-1 and CHK-2 FAIL on real, verifiable issues; exit code 1 is the honest verifier verdict for this baseline.

---

## §5 Generated artefacts introduced by F5 (all inside this folder unless noted)

| Artefact | Generator | Note |
|---|---|---|
| `RULE_FREEZE.md`, `KG_CHAINS.md`, `NIST_ANCHORS.md`, `CORPUS_LINKAGE.md` | `scripts/gen_narrative_docs_v0.py` | v0, banner-marked, mechanically derived |
| `22_Traceability_Matrix_rich_v0.xlsx` (9 sheets) | `scripts/build_traceability_matrix_rich.py` | emitted alongside; legacy `22_Traceability_Matrix.xlsx` untouched |
| `18_Functional_Tree.drawio` (29 nodes / 28 edges) | `scripts/gen_drawio.py` | new file (Doc27 frontmatter listed it as pending output) |
| `../02_PHASE2_RULES_RICH/TRACEABILITY_AUDIT.md` | `scripts/audit_traceability_v0.py` | new file only (deliverable 5) |

---

## §6 Gate status at capture time

| Gate | Result |
|---|---|
| `02_PHASE2_RULES_RICH/validation/check_unmapped.py` (Case_02) | GATE PASS (re-run with the new .md files in scan scope) |
| repo-root `validation/check_implementation_posture_case02.py` | GATE PASS |
