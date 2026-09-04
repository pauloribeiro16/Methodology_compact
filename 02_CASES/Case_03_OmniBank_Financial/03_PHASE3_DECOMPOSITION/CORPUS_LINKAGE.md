---
document_id: AEGIS-C03-P3-CORPUS-LINKAGE
title: Corpus Linkage v0 (Case_03 Phase 3)
phase: 3
version: 0.0
created: 2026-09-04
updated: 2026-09-04
author: PORT-PARITY-2 Executor (generated)
status: GENERATED
case: Case_03_OmniBank_Financial
---

> **GENERATED v0 (PORT-PARITY-2) — pending human review.** Mechanically derived from D-XX.Y census across Doc22–Doc31 + requirements/*.md of this P3 folder, ../02_PHASE2_RULES_RICH/control_set.yaml@sub_domain, 00_METHODOLOGY/PREPROCESSING_by_domain/domains/index.md; verify before relying on it.

# Corpus Linkage v0 — Case_03 OmniBank Financial

Mechanical census of `D-XX.Y` sub-domain references across the 14 Markdown files of this P3 folder, cross-read against the 78 controls of `../02_PHASE2_RULES_RICH/control_set.yaml` (per-`sub_domain`). Methodology corpus index: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/index.md` (38 sub-domains D-01.1 … D-10.4; per `00_METHODOLOGY/AGENTS.md` the domain corpus is read-only here). Case_03 adds 4 AI-specific D-12.x rules (BPR block) beyond the 38-sub-domain corpus grid.

## §1 Controls per sub-domain (control_set.yaml@sub_domain)

| Sub-domain | Controls | Sub-domain | Controls |
|---|---:|---|---:|
| D-01.1 | 2 | D-05.4 | 2 |
| D-01.2 | 2 | D-06.1 | 2 |
| D-01.3 | 2 | D-06.2 | 2 |
| D-01.4 | 2 | D-06.3 | 2 |
| D-02.1 | 3 | D-06.4 | 2 |
| D-02.2 | 2 | D-07.1 | 2 |
| D-02.3 | 1 | D-07.2 | 2 |
| D-02.4 | 3 | D-07.3 | 2 |
| D-03.1 | 2 | D-07.4 | 2 |
| D-03.2 | 2 | D-08.1 | 2 |
| D-03.3 | 2 | D-08.2 | 3 |
| D-03.4 | 2 | D-08.3 | 2 |
| D-04.1 | 2 | D-09.1 | 3 |
| D-04.2 | 2 | D-09.2 | 3 |
| D-04.3 | 2 | D-09.3 | 1 |
| D-04.4 | 2 | D-09.4 | 1 |
| D-05.1 | 2 | D-10.1 | 3 |
| D-05.2 | 1 | D-10.2 | 2 |
| D-05.3 | 2 | D-10.3 | 2 |

## §2 D-XX.Y references per P3 doc

| Doc | distinct D-XX.Y | total mentions |
|---|---:|---:|
| Doc22_Use_Cases_Catalog.md | 42 | 324 |
| Doc23_Use_Case_Relationships.md | 0 | 0 |
| Doc24_Use_Case_Variability.md | 0 | 0 |
| Doc25_Architectural_Nodes.md | 39 | 98 |
| Doc26_Requirements_Allocation.md | 41 | 225 |
| Doc27_Compliance_Gates_Report.md | 42 | 82 |
| Doc28_Functional_Tree.md | 38 | 199 |
| Doc29_Risk_Analysis.md | 0 | 0 |
| Doc30_Functional_Requirements.md | 40 | 163 |
| Doc31_Non_Functional_Requirements.md | 30 | 56 |
| A_Use_Case_Diagrams.md | 0 | 0 |
| B_Sequence_Diagrams.md | 0 | 0 |
| C_Class_Diagrams.md | 0 | 0 |
| D_KG_Inference_Examples.md | 0 | 0 |

**Total D-XX.Y mentions across P3 docs: 1147; distinct sub-domains referenced: 42.**

## §3 Top sub-domains by mention volume (P3 docs)

| Sub-domain | Mentions |
|---|---:|
| D-04.3 | 42 |
| D-01.1 | 38 |
| D-03.1 | 38 |
| D-10.1 | 37 |
| D-03.2 | 37 |
| D-04.1 | 37 |
| D-07.3 | 37 |
| D-10.2 | 37 |
| D-04.2 | 36 |
| D-05.1 | 36 |

## §4 Pointers

- Domain corpus: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/index.md` → per-sub-domain `D-XX.Y.md` (read-only)
- Impact tool: `scripts/kg.sh impact <ID>` (repo root; RP-1) before any change to rule/requirement IDs
- Sibling linkage docs: Case_01 `03_PHASE3_DECOMPOSITION_RICH/CORPUS_LINKAGE.md` (structure template)
