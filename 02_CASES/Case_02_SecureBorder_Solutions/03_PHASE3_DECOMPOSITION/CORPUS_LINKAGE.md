---
document_id: AEGIS-C02-P3-CORPUS-LINKAGE
title: Corpus Linkage v0 (Case_02 Phase 3)
phase: 3
version: 0.0
created: 2026-09-04
updated: 2026-09-04
author: PORT-PARITY-2 Executor (generated)
status: GENERATED
case: Case_02_SecureBorder_Solutions
---

> **GENERATED v0 (PORT-PARITY-2) — pending human review.** Mechanically derived from D-XX.Y census across Doc21–Doc30 + requirements/*.md of this P3 folder, ../02_PHASE2_RULES_RICH/control_set.yaml@sub_domain, 00_METHODOLOGY/PREPROCESSING_by_domain/domains/index.md; verify before relying on it.

# Corpus Linkage v0 — Case_02 SecureBorder Solutions

Mechanical census of `D-XX.Y` sub-domain references across the 15 Markdown files of this P3 folder, cross-read against the 63 controls of `../02_PHASE2_RULES_RICH/control_set.yaml` (per-`sub_domain`). Methodology corpus index: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/index.md` (38 sub-domains D-01.1 … D-10.4; per `00_METHODOLOGY/AGENTS.md` the domain corpus is read-only here).

## §1 Controls per sub-domain (control_set.yaml@sub_domain)

| Sub-domain | Controls | Sub-domain | Controls |
|---|---:|---|---:|
| D-01.1 | 2 | D-05.4 | 1 |
| D-01.2 | 1 | D-06.1 | 2 |
| D-01.3 | 2 | D-06.2 | 1 |
| D-01.4 | 1 | D-06.3 | 1 |
| D-02.1 | 3 | D-06.4 | 1 |
| D-02.2 | 1 | D-07.1 | 2 |
| D-02.3 | 1 | D-07.2 | 1 |
| D-02.4 | 3 | D-07.3 | 3 |
| D-03.1 | 4 | D-07.4 | 1 |
| D-03.2 | 1 | D-08.1 | 2 |
| D-03.3 | 1 | D-08.2 | 1 |
| D-03.4 | 1 | D-08.3 | 1 |
| D-04.1 | 3 | D-09.1 | 3 |
| D-04.2 | 2 | D-09.2 | 1 |
| D-04.3 | 1 | D-09.3 | 1 |
| D-04.4 | 1 | D-09.4 | 1 |
| D-05.1 | 3 | D-10.1 | 4 |
| D-05.2 | 1 | D-10.2 | 2 |
| D-05.3 | 1 | D-10.3 | 1 |

## §2 D-XX.Y references per P3 doc

| Doc | distinct D-XX.Y | total mentions |
|---|---:|---:|
| Doc21_Use_Cases_Catalog.md | 48 | 301 |
| Doc22_Use_Case_Relationships.md | 0 | 0 |
| Doc23_Use_Case_Variability.md | 0 | 0 |
| Doc24_Architectural_Nodes.md | 43 | 162 |
| Doc25_Requirements_Allocation.md | 48 | 290 |
| Doc26_Compliance_Gates_Report.md | 39 | 180 |
| Doc27_Functional_Tree.md | 38 | 176 |
| Doc28_Risk_Analysis.md | 1 | 2 |
| A_Use_Case_Diagrams.md | 0 | 0 |
| B_Sequence_Diagrams.md | 0 | 0 |
| C_Class_Diagrams.md | 0 | 0 |
| D_KG_Inference_Examples.md | 0 | 0 |
| PHASE3_PLAN.md | 3 | 3 |
| Doc29_Functional_Requirements.md | 10 | 59 |
| Doc30_Non_Functional_Requirements.md | 26 | 116 |

**Total D-XX.Y mentions across P3 docs: 1289; distinct sub-domains referenced: 48.**

## §3 Top sub-domains by mention volume (P3 docs)

| Sub-domain | Mentions |
|---|---:|
| D-03.1 | 71 |
| D-05.1 | 66 |
| D-09.1 | 62 |
| D-02.1 | 59 |
| D-02.4 | 58 |
| D-10.2 | 57 |
| D-01.1 | 56 |
| D-10.1 | 56 |
| D-07.1 | 55 |
| D-04.2 | 46 |

## §4 Pointers

- Domain corpus: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/index.md` → per-sub-domain `D-XX.Y.md` (read-only)
- Impact tool: `scripts/kg.sh impact <ID>` (repo root; RP-1) before any change to rule/requirement IDs
- Sibling linkage docs: Case_01 `03_PHASE3_DECOMPOSITION_RICH/CORPUS_LINKAGE.md` (structure template)
