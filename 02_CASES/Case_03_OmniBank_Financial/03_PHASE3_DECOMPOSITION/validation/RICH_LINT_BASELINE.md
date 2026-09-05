---
document_id: AEGIS-C03-P3-RICH-LINT-BASELINE
title: RICH Lint Baseline v0 (Case_03 Phase 3, PORT-PARITY-2)
phase: 3
version: 0.0
created: 2026-09-04
updated: 2026-09-04
author: PORT-PARITY-2 Executor (generated)
status: GENERATED
case: Case_03_OmniBank_Financial
sibling_doc: ../ (Case_01: 03_PHASE3_DECOMPOSITION_RICH/validation/RICH_LINT_BASELINE.md)
---

# RICH Lint Baseline v0 — Case_03 Phase 3

> **GENERATED v0 (PORT-PARITY-2) — pending human review.** Mechanically derived from
> `scripts/verify_rich.py` runs over Doc22–Doc31 + requirements/Doc30–Doc31 +
> `../02_PHASE2_RULES_RICH/control_set.yaml`, plus the ad-hoc greps listed in §3;
> verify before relying on it.

---

## §1 Snapshot metadata

| Field | Value |
|-------|-------|
| Date captured | 2026-09-04 |
| Runner | `python3 scripts/verify_rich.py` (ported from Case_01's RICH folder, adapted to Case_03 doc numbering Doc22–Doc31 and its card-style FR/NFR/gate formats) |
| Target folder | `02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/` |
| Rule universe | `../02_PHASE2_RULES_RICH/control_set.yaml` v2.0 — 78 controls (38 CR + 40 BPR incl. 4 D-12.x AI-specific) |
| verify_rich exit code | **1** (3 FAIL / 5 PASS — honest result, findings listed below) |

---

## §2 verify_rich results (verbatim verdicts)

| Check | Verdict | Detail |
|---|---|---|
| CHK-0 sources | PASS | control_set.yaml v2.0: 78 controls (38 CR + 40 BPR incl. 4 D-12.x AI-specific) |
| CHK-1 frontmatter (8 corr-008 fields) | **FAIL** | all 8 DocNN docs (Doc22–Doc29) miss the `case:` field (7/8 present) |
| CHK-2 FR census | PASS | 72 FR cards match Doc30 summary "Total FRs = 72" |
| CHK-3 NFR census | **FAIL** | 12 NFR cards defined (NFR-01…NFR-12) vs Doc31 summary claiming **"Total NFRs 56"** — real internal inconsistency (F5-C3-02) |
| CHK-4 rule refs / dangling | PASS | 78 distinct rule refs across P3 docs; 0 dangling (all resolve against control_set 78) |
| CHK-5 UC census | PASS (info) | 62 `## UC-NN:` cards in Doc22 (PROC-01…PROC-38) |
| CHK-6 corr-008 cross-refs | **FAIL** | 5 FR cards cite raw article citations instead of catalog rule ids in `Source Rule` (FR-59 → AI-C09/AI-C10, FR-62 → DORA-C38, FR-63 → "GDPR Art. 35", FR-64 → "AI Act Art. 28"; also AI Act Art. 14). Gate cards all resolve. |
| CHK-7 rule traceability coverage | PASS | 78/78 rules referenced by ≥1 P3 doc; FR-level Source Rule covers 49 rules |

---

## §3 Ad-hoc greps (complementary census)

| Grep | Result | Verdict |
|---|---|---|
| UC-NN refs in Doc23–Doc31 + requirements resolving to Doc22 cards | **Doc23_Use_Case_Relationships.md references UC-99 — no such card exists (Doc22 ends at PROC-38)** | **FAIL** (F5-C3-04) |
| AG-D-XX.X-NNN refs across P3 docs vs P1 graph AdjustedGoal nodes (76 ids) | 0 dangling | PASS |
| Doc26 allocation rule rows | 77 of 78 rules allocated — **BPR-D-12.1-001 (AI adversarial robustness testing) absent** from §3 tables (it appears only in Doc27 gates) | FINDING (F5-C3-03) |
| Doc27 gate cards' Rules Verified vs control_set | 78/78 rules verified by ≥1 gate; 0 dangling | PASS |
| Doc31 "Total NFRs" summary vs defined NFR cards | 56 claimed vs 12 defined (summary per-category rows sum to 56: 12+10+12+10+6+6) | **FAIL** (F5-C3-02) |
| frontmatter `case:` field across Doc22–Doc29 | 0/8 carry it | **FAIL** (F5-C3-05) |
| stale "63 rules (38 CR + 25 BPR)" claim (Doc26, + frontmatter complexity lines "63 rules") | found (see RULE_FREEZE.md §3) | FINDING (F5-C3-01) |

---

## §4 Findings requiring human attention (P7)

| # | Severity | Finding | Disposition |
|---|---|---|---|
| F5-C3-01 | MEDIUM | Stale rule counts pre-dating the P2 renumbering (Doc26 "63 rules (38 CR + 25 BPR)"; complexity frontmatter lines across Doc22/Doc26 claim "63 rules" vs frozen 78; Rules Catalog renumbered Doc18→Doc19, Framework Mapping →Doc20). | Census in RULE_FREEZE.md §3; content edits outside F5 touch-scope. |
| F5-C3-02 | HIGH | Doc31 internal inconsistency: summary claims 56 NFRs (per-category rows 12+10+12+10+6+6) but the body defines only 12 NFR cards (NFR-01…NFR-12, all CONF-category headers present). Suspected truncation of the NFR body in an earlier edit. | Content edit — outside F5 touch-scope. Needs human decision: restore 44 missing cards or correct the summary. |
| F5-C3-03 | LOW | BPR-D-12.1-001 not allocated to any node in Doc26 §3 (present in Doc27 gates and control_set). | Content edit — outside F5 touch-scope. |
| F5-C3-04 | LOW | Doc23 references UC-99 (dangling — Doc22 defines PROC-01…PROC-38). | Content edit — outside F5 touch-scope. |
| F5-C3-05 | LOW | Doc22–Doc29 frontmatter missing the `case:` field (corr-008 8-field completeness: 7/8 present). | Content edit — outside F5 touch-scope. |
| F5-C3-06 | MEDIUM | 5 FR cards trace via raw article citations (AI-C09, AI-C10, DORA-C38, "GDPR Art. 35", "AI Act Art. 28", "AI Act Art. 14") instead of catalog rule ids — corr-008 requires REQ-layer trace to point at the rule layer. | Content edit — outside F5 touch-scope. |
| F5-C3-07 | INFO | CR-D-05.4-001 carries the single deliberate CSF gap ("N/A — não mapeado a CSF 2.0", verbatim from control_set); 34 controls carry the legal `N/A (non-AI scope)` AI-RMF placeholder; 6 controls have `status_csf: —`. | Documented in NIST_ANCHORS.md §4; no action. |

**No PASS was faked**: CHK-1, CHK-3 and CHK-6 FAIL on real, verifiable issues; exit code 1 is the honest verifier verdict for this baseline.

---

## §5 Generated artefacts introduced by F5 (all inside this folder unless noted)

| Artefact | Generator | Note |
|---|---|---|
| `RULE_FREEZE.md`, `KG_CHAINS.md`, `NIST_ANCHORS.md`, `CORPUS_LINKAGE.md` | `scripts/gen_narrative_docs_v0.py` | v0, banner-marked, mechanically derived |
| `22_Traceability_Matrix_rich_v0.xlsx` (9 sheets) | `scripts/build_traceability_matrix_rich.py` | emitted alongside; legacy `22_Traceability_Matrix.xlsx` untouched |
| `18_Functional_Tree.drawio` (53 nodes / 52 edges) | `scripts/gen_drawio.py` | new file (Doc28's mermaid tree; labels re-close the nested track tags) |

(Case_03 already had `../02_PHASE2_RULES_RICH/TRACEABILITY_AUDIT.md` — used as the structural template for Case_02's new audit; not modified.)

---

## §6 Gate status at capture time

| Gate | Result |
|---|---|
| `02_PHASE2_RULES_RICH/validation/check_unmapped.py` (Case_03) | GATE PASS (re-run with the new .md files in scan scope) |
| repo-root `validation/check_implementation_posture_case03.py` | GATE PASS |
