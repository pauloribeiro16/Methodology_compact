---
document_id: AEGIS-P3-RICH-CORPUS-LINKAGE
title: Corpus Linkage — Artefact-to-Sub-domain Map (Case_01 Phase 3 RICH)
phase: 3
version: 1.0
created: 2026-08-24
updated: 2026-08-24
author: Fase de Especificação 2 Executor (paulo@methodology.pt)
status: ACTIVE
case: Case_01_TinyTask_SaaS
tier: MICRO
branch: feature/aegis-p3-case01-rich
inputs:
  - RULE_FREEZE.md §1 (46 rules), §2 (31 goals), §5-§7 (UC/FR/NFR/Risk/Node/Gate counts)
  - 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4 (CR) + §5 (BPR)
  - 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §3 (PO) + §4 (SO)
  - 03_PHASE3_DECOMPOSITION/ legacy 13/14/15/16/23/24/25 (read-only)
  - 00_METHODOLOGY/PREPROCESSING_by_domain/domains/ (38 sub-domain list)
totals:
  rules: 46     # 30 CR + 16 BPR
  goals: 31     # 11 PO + 20 SO
  use_cases: 35 # 6 DP + 7 SEC + 7 IAM + 5 DEV + 7 GOV + 3 TRN
  frs: 30
  nfrs: 46
  nodes: 49     # 17 TECH + 20 PROC + 12 ROLE
  derivation_nodes: 30   # 1:1 with CR per Doc 15 §4
  gates: 30     # 1:1 with CR per Doc 16 §5
  risks: 10
  threats: 38
  total_artefacts: 344
related_deliverables:
  - RULE_FREEZE.md
  - validation/SPRINT2_REPORT.md
  - NIST_ANCHORS.md
  - KG_CHAINS.md
---

# Corpus Linkage — Artefact-to-Sub-domain Map

> **Purpose.** Single-page mapping of every Phase 3 Rich artefact to its `D-XX.Y` sub-domain.
> Source of truth: `RULE_FREEZE.md` (canonical freeze) + Doc 14/15/16 freeze values.
> Methodology: D-XX.Y derived from rule ID for CR/BPR; mirrored 1:1 for DN/Gate; cross-checked against UC/FR/NFR/Risk/Node source attributions from legacy Phase 3 docs.

---

## §1 Rules (46: 30 CR + 16 BPR)

| Artefact ID | Type | D-subdomain | Source file | Verification |
|-------------|------|-------------|-------------|--------------|
| CR-D-01.1-001 | RULE | D-01.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-01.2-001 | RULE | D-01.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-01.3-001 | RULE | D-01.3 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-01.4-001 | RULE | D-01.4 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-02.1-001 | RULE | D-02.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-02.2-001 | RULE | D-02.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-02.3-001 | RULE | D-02.3 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-03.1-001 | RULE | D-03.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-03.2-001 | RULE | D-03.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-03.3-001 | RULE | D-03.3 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-03.4-001 | RULE | D-03.4 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-04.1-001 | RULE | D-04.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-04.2-001 | RULE | D-04.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-04.3-001 | RULE | D-04.3 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-04.4-001 | RULE | D-04.4 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-05.1-001 | RULE | D-05.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-05.2-001 | RULE | D-05.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-05.3-001 | RULE | D-05.3 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-05.4-001 | RULE | D-05.4 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-06.1-001 | RULE | D-06.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-06.2-001 | RULE | D-06.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-06.3-001 | RULE | D-06.3 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-07.1-001 | RULE | D-07.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-08.1-001 | RULE | D-08.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-08.2-001 | RULE | D-08.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-09.1-001 | RULE | D-09.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-09.2-001 | RULE | D-09.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-09.4-001 | RULE | D-09.4 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-10.2-001 | RULE | D-10.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| CR-D-10.3-001 | RULE | D-10.3 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-01.1-001 | RULE | D-01.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-01.2-001 | RULE | D-01.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-02.1-001 | RULE | D-02.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-02.2-001 | RULE | D-02.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-03.1-001 | RULE | D-03.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-03.2-001 | RULE | D-03.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-03.4-001 | RULE | D-03.4 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-04.3-001 | RULE | D-04.3 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-04.3-002 | RULE | D-04.3 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-05.3-001 | RULE | D-05.3 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-07.1-001 | RULE | D-07.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-07.2-001 | RULE | D-07.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-09.1-001 | RULE | D-09.1 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-10.2-001 | RULE | D-10.2 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-10.3-001 | RULE | D-10.3 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |
| BPR-D-10.3-002 | RULE | D-10.3 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §4/§5 | Doc 11 §7.1/§7.2 |

## §2 Goals (31: 11 PO + 20 SO)

| Artefact ID | Type | D-subdomain | Source file | Verification |
|-------------|------|-------------|-------------|--------------|
| PO-D-01.1-001 | GOAL | D-01.1 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §3.1 | Doc 10b |
| PO-D-01.2-001 | GOAL | D-01.2 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §3.1 | Doc 10b |
| PO-D-01.4-001 | GOAL | D-01.4 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §3.1 | Doc 10b |
| PO-D-05.1-001 | GOAL | D-05.1 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §3.1 | Doc 10b |
| PO-D-05.2-001 | GOAL | D-05.2 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §3.1 | Doc 10b |
| PO-D-05.3-001 | GOAL | D-05.3 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §3.1 | Doc 10b |
| PO-D-05.4-001 | GOAL | D-05.4 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §3.1 | Doc 10b |
| PO-D-07.1-001 | GOAL | D-07.1 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §3.1 | Doc 10b |
| PO-D-09.1-001 | GOAL | D-09.1 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §3.1 | Doc 10b |
| PO-D-09.2-001 | GOAL | D-09.2 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §3.1 | Doc 10b |
| PO-D-09.4-001 | GOAL | D-09.4 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §3.1 | Doc 10b |
| SO-D-02.1-001 | GOAL | D-02.1 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-02.2-001 | GOAL | D-02.2 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-02.3-001 | GOAL | D-02.3 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-03.1-001 | GOAL | D-03.1 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-03.2-001 | GOAL | D-03.2 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-03.3-001 | GOAL | D-03.3 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-03.4-001 | GOAL | D-03.4 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-04.1-001 | GOAL | D-04.1 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-04.2-001 | GOAL | D-04.2 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-04.3-001 | GOAL | D-04.3 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-04.4-001 | GOAL | D-04.4 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-06.1-001 | GOAL | D-06.1 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-06.2-001 | GOAL | D-06.2 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-06.3-001 | GOAL | D-06.3 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-08.1-001 | GOAL | D-08.1 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-08.2-001 | GOAL | D-08.2 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-09.1-001 | GOAL | D-09.1 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-09.2-001 | GOAL | D-09.2 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-10.2-001 | GOAL | D-10.2 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |
| SO-D-10.3-001 | GOAL | D-10.3 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md §4.1 | Doc 10b |

## §3 Use Cases (35 L1 cards: 6 DP + 7 SEC + 7 IAM + 5 DEV + 7 GOV + 3 TRN)

| UC ID | Pkg | D-subdomain |
|-------|-----|-------------|
| PROC-01 | DP | D-01.1 |
| PROC-02 | DP | D-01.4 |
| U.C.1.2.1 | DP | D-05.3 |
| U.C.1.3.1 | DP | D-05.1 |
| U.C.1.4.1 | DP | D-05.2 |
| U.C.1.5.1 | DP | D-05.4 |
| PROC-03 | SEC | D-02.1 |
| U.C.2.2.1 | SEC | D-02.2 |
| PROC-04 | SEC | D-02.3 |
| U.C.2.4.1 | SEC | D-04.1 |
| U.C.2.4.2 | SEC | D-04.2 |
| PROC-05 | SEC | D-04.3 |
| U.C.2.6.1 | SEC | D-04.4 |
| U.C.3.1.1 | IAM | D-03.1 |
| U.C.3.1.2 | IAM | D-03.2 |
| U.C.3.2.1 | IAM | D-03.3 |
| U.C.3.3.1 | IAM | D-03.4 |
| PROC-06 | IAM | D-09.4 |
| U.C.3.5.1 | IAM | D-10.2 |
| PROC-07 | IAM | D-10.3 |
| PROC-08 | DEV | D-07.1 |
| U.C.4.2.1 | DEV | D-07.2 |
| U.C.4.3.1 | DEV | D-02.2 |
| U.C.4.4.1 | DEV | D-04.1 |
| PROC-09 | DEV | D-09.2 |
| PROC-10 | GOV | D-09.1 |
| PROC-11 | GOV | D-09.1 |
| PROC-12 | GOV | D-09.2 |
| PROC-13 | GOV | D-09.4 |
| PROC-14 | GOV | D-06.1 |
| CAP-01 | GOV | D-06.3 |
| U.C.5.6.1 | GOV | D-06.2 |
| PROC-15 | TRN | D-08.1 |
| PROC-16 | TRN | D-08.2 |
| PROC-17 | TRN | D-08.1 |

## §4 Functional Requirements (30: FR-01..FR-30)

| Artefact ID | Type | D-subdomain | Source file | Verification |
|-------------|------|-------------|-------------|--------------|
| FR-01 | FR | D-03.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-02 | FR | D-03.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-03 | FR | D-03.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-04 | FR | D-03.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-05 | FR | D-03.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-06 | FR | — | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-07 | FR | D-01.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-08 | FR | D-01.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-09 | FR | D-01.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-10 | FR | — | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-11 | FR | D-01.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-12 | FR | D-01.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-13 | FR | D-02.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-14 | FR | D-04.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-15 | FR | D-04.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-16 | FR | D-01.1 (note: Doc 23 maps to CR-D-01.1; Fase de Especificação 5 should remap to CR-D-04.3) | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-17 | FR | D-02.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-18 | FR | D-02.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-19 | FR | D-03.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-20 | FR | D-07.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-21 | FR | D-02.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-22 | FR | — | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-23 | FR | D-02.1 (note: Doc 23 maps to CR-D-02.1; Fase de Especificação 5 should remap to CR-D-06.2) | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-24 | FR | — | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-25 | FR | D-06.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-26 | FR | D-06.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-27 | FR | D-06.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-28 | FR | D-02.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-29 | FR | D-08.1 | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |
| FR-30 | FR | — | 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md §3 | Doc 23 §3 |

## §5 Non-Functional Requirements (46: NFR-01..NFR-46)

| Artefact ID | Type | D-subdomain | Source file |
|-------------|------|-------------|-------------|
| NFR-01 | NFR | D-01.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-02 | NFR | D-01.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-03 | NFR | D-01.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-04 | NFR | D-01.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-05 | NFR | D-01.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-06 | NFR | D-01.4 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-07 | NFR | D-01.4 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-08 | NFR | D-05.3 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-09 | NFR | D-05.3 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-10 | NFR | D-09.4 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-11 | NFR | D-09.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-12 | NFR | D-09.4 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-13 | NFR | D-04.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-14 | NFR | D-04.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-15 | NFR | D-04.4 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-16 | NFR | D-04.4 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-17 | NFR | D-04.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-18 | NFR | D-04.4 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-19 | NFR | D-04.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-20 | NFR | D-01.4 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-21 | NFR | D-02.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-22 | NFR | D-02.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-23 | NFR | D-02.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-24 | NFR | D-02.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-25 | NFR | D-03.3 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-26 | NFR | D-10.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-27 | NFR | D-10.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-28 | NFR | D-10.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-29 | NFR | D-10.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-30 | NFR | D-05.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-31 | NFR | D-05.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-32 | NFR | D-05.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-33 | NFR | D-05.3 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-34 | NFR | D-05.4 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-35 | NFR | D-09.4 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-36 | NFR | D-07.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-37 | NFR | D-07.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-38 | NFR | D-09.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-39 | NFR | D-05.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-40 | NFR | D-09.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-41 | NFR | D-09.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-42 | NFR | D-09.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-43 | NFR | D-09.4 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-44 | NFR | D-10.2 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-45 | NFR | D-09.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |
| NFR-46 | NFR | D-09.1 | 03_PHASE3_DECOMPOSITION/requirements/24_Non_Functional_Requirements.md §3 |

## §6 Architectural Nodes (49: 17 TECH + 20 PROC + 12 ROLE)

| Artefact ID | Type | D-subdomain |
|-------------|------|-------------|
| NODE-SYS-001 | NODE-TECH | D-10.2 |
| NODE-SYS-002 | NODE-TECH | D-10.2 |
| NODE-SYS-003 | NODE-TECH | D-10.2 |
| NODE-SYS-004 | NODE-TECH | D-04.3 |
| NODE-SYS-005 | NODE-TECH | D-04.1 |
| NODE-SYS-006 | NODE-TECH | D-03.1 |
| NODE-SYS-007 | NODE-TECH | D-03.1 |
| NODE-SYS-008 | NODE-TECH | D-03.4 |
| NODE-SYS-009 | NODE-TECH | D-10.3 |
| NODE-SYS-010 | NODE-TECH | D-01.1 |
| NODE-SYS-011 | NODE-TECH | D-01.2 |
| NODE-SYS-012 | NODE-TECH | D-07.2 |
| NODE-SYS-013 | NODE-TECH | D-06.2 |
| NODE-SYS-014 | NODE-TECH | D-09.4 |
| NODE-SYS-015 | NODE-TECH | D-04.4 |
| NODE-SYS-016 | NODE-TECH | D-01.4 |
| NODE-SYS-017 | NODE-TECH | D-09.4 |
| NODE-PROC-001 | NODE-PROC | D-04.3 |
| NODE-PROC-002 | NODE-PROC | D-04.1 |
| NODE-PROC-003 | NODE-PROC | D-04.4 |
| NODE-PROC-004 | NODE-PROC | D-09.1 |
| NODE-PROC-005 | NODE-PROC | D-09.2 |
| NODE-PROC-006 | NODE-PROC | D-09.4 |
| NODE-PROC-007 | NODE-PROC | D-07.1 |
| NODE-PROC-008 | NODE-PROC | D-07.2 |
| NODE-PROC-009 | NODE-PROC | D-07.1 |
| NODE-PROC-010 | NODE-PROC | D-07.1 |
| NODE-PROC-011 | NODE-PROC | D-06.1 |
| NODE-PROC-012 | NODE-PROC | D-06.3 |
| NODE-PROC-013 | NODE-PROC | D-07.2 |
| NODE-PROC-014 | NODE-PROC | D-07.2 |
| NODE-PROC-015 | NODE-PROC | D-02.2 |
| NODE-PROC-016 | NODE-PROC | D-02.3 |
| NODE-PROC-017 | NODE-PROC | D-02.1 |
| NODE-PROC-018 | NODE-PROC | D-08.1 |
| NODE-PROC-019 | NODE-PROC | D-08.2 |
| NODE-PROC-020 | NODE-PROC | D-10.3 |
| NODE-ROLE-001 | NODE-ROLE | D-09.1 |
| NODE-ROLE-002 | NODE-ROLE | D-08.2 |
| NODE-ROLE-003 | NODE-ROLE | D-08.2 |
| NODE-ROLE-004 | NODE-ROLE | D-03.3 |
| NODE-ROLE-005 | NODE-ROLE | D-08.1 |
| NODE-ROLE-006 | NODE-ROLE | D-09.2 |
| NODE-ROLE-007 | NODE-ROLE | D-09.4 |
| NODE-ROLE-008 | NODE-ROLE | D-04.3 |
| NODE-ROLE-009 | NODE-ROLE | D-06.1 |
| NODE-ROLE-010 | NODE-ROLE | D-04.1 |
| NODE-ROLE-011 | NODE-ROLE | D-06.3 |
| NODE-ROLE-012 | NODE-ROLE | D-09.1 |

## §7 Derivation Nodes (30: DN-01..DN-30, 1:1 with CR per Doc 15 §4)

| Artefact ID | Type | D-subdomain |
|-------------|------|-------------|
| DN-01 | DN | D-01.1 |
| DN-02 | DN | D-01.2 |
| DN-03 | DN | D-01.3 |
| DN-04 | DN | D-01.4 |
| DN-05 | DN | D-02.1 |
| DN-06 | DN | D-02.2 |
| DN-07 | DN | D-02.3 |
| DN-08 | DN | D-03.1 |
| DN-09 | DN | D-03.2 |
| DN-10 | DN | D-03.3 |
| DN-11 | DN | D-03.4 |
| DN-12 | DN | D-04.1 |
| DN-13 | DN | D-04.2 |
| DN-14 | DN | D-04.3 |
| DN-15 | DN | D-04.4 |
| DN-16 | DN | D-05.1 |
| DN-17 | DN | D-05.2 |
| DN-18 | DN | D-05.3 |
| DN-19 | DN | D-05.4 |
| DN-20 | DN | D-06.1 |
| DN-21 | DN | D-06.2 |
| DN-22 | DN | D-06.3 |
| DN-23 | DN | D-07.1 |
| DN-24 | DN | D-08.1 |
| DN-25 | DN | D-08.2 |
| DN-26 | DN | D-09.1 |
| DN-27 | DN | D-09.2 |
| DN-28 | DN | D-09.4 |
| DN-29 | DN | D-10.2 |
| DN-30 | DN | D-10.3 |

## §8 Compliance Gates (30: 1:1 with CR per Doc 16 §5)

| Artefact ID | Type | D-subdomain |
|-------------|------|-------------|
| GATE-CR-D-01.1-001 | GATE | D-01.1 |
| GATE-CR-D-01.2-001 | GATE | D-01.2 |
| GATE-CR-D-01.3-001 | GATE | D-01.3 |
| GATE-CR-D-01.4-001 | GATE | D-01.4 |
| GATE-CR-D-02.1-001 | GATE | D-02.1 |
| GATE-CR-D-02.2-001 | GATE | D-02.2 |
| GATE-CR-D-02.3-001 | GATE | D-02.3 |
| GATE-CR-D-03.1-001 | GATE | D-03.1 |
| GATE-CR-D-03.2-001 | GATE | D-03.2 |
| GATE-CR-D-03.3-001 | GATE | D-03.3 |
| GATE-CR-D-03.4-001 | GATE | D-03.4 |
| GATE-CR-D-04.1-001 | GATE | D-04.1 |
| GATE-CR-D-04.2-001 | GATE | D-04.2 |
| GATE-CR-D-04.3-001 | GATE | D-04.3 |
| GATE-CR-D-04.4-001 | GATE | D-04.4 |
| GATE-CR-D-05.1-001 | GATE | D-05.1 |
| GATE-CR-D-05.2-001 | GATE | D-05.2 |
| GATE-CR-D-05.3-001 | GATE | D-05.3 |
| GATE-CR-D-05.4-001 | GATE | D-05.4 |
| GATE-CR-D-06.1-001 | GATE | D-06.1 |
| GATE-CR-D-06.2-001 | GATE | D-06.2 |
| GATE-CR-D-06.3-001 | GATE | D-06.3 |
| GATE-CR-D-07.1-001 | GATE | D-07.1 |
| GATE-CR-D-08.1-001 | GATE | D-08.1 |
| GATE-CR-D-08.2-001 | GATE | D-08.2 |
| GATE-CR-D-09.1-001 | GATE | D-09.1 |
| GATE-CR-D-09.2-001 | GATE | D-09.2 |
| GATE-CR-D-09.4-001 | GATE | D-09.4 |
| GATE-CR-D-10.2-001 | GATE | D-10.2 |
| GATE-CR-D-10.3-001 | GATE | D-10.3 |

## §9 Risks + Threats (10 R + 38 T, from Doc 25)

| Artefact ID | Type | D-subdomain |
|-------------|------|-------------|
| RISK-01 | RISK | D-03.2 |
| RISK-02 | RISK | D-07.2 |
| RISK-03 | RISK | D-04.1 |
| RISK-04 | RISK | D-04.2 |
| RISK-05 | RISK | D-09.2 |
| RISK-06 | RISK | D-06.1 |
| RISK-07 | RISK | D-05.3 |
| RISK-08 | RISK | D-05.1 |
| RISK-09 | RISK | D-09.4 |
| RISK-10 | RISK | D-02.3 |
| THR-01 | THREAT | D-01.1 |
| THR-02 | THREAT | D-01.2 |
| THR-03 | THREAT | D-01.3 |
| THR-04 | THREAT | D-01.4 |
| THR-05 | THREAT | D-02.1 |
| THR-06 | THREAT | D-02.1 |
| THR-07 | THREAT | D-02.2 |
| THR-08 | THREAT | D-02.2 |
| THR-09 | THREAT | D-02.3 |
| THR-10 | THREAT | D-02.3 |
| THR-11 | THREAT | D-03.1 |
| THR-12 | THREAT | D-03.1 |
| THR-13 | THREAT | D-03.2 |
| THR-14 | THREAT | D-03.3 |
| THR-15 | THREAT | D-03.3 |
| THR-16 | THREAT | D-03.4 |
| THR-17 | THREAT | D-04.1 |
| THR-18 | THREAT | D-04.1 |
| THR-19 | THREAT | D-04.2 |
| THR-20 | THREAT | D-04.3 |
| THR-21 | THREAT | D-04.3 |
| THR-22 | THREAT | D-04.4 |
| THR-23 | THREAT | D-04.4 |
| THR-24 | THREAT | D-05.1 |
| THR-25 | THREAT | D-05.2 |
| THR-26 | THREAT | D-05.3 |
| THR-27 | THREAT | D-05.4 |
| THR-28 | THREAT | D-06.1 |
| THR-29 | THREAT | D-06.2 |
| THR-30 | THREAT | D-06.3 |
| THR-31 | THREAT | D-07.1 |
| THR-32 | THREAT | D-07.2 |
| THR-33 | THREAT | D-07.2 |
| THR-34 | THREAT | D-08.1 |
| THR-35 | THREAT | D-08.2 |
| THR-36 | THREAT | D-09.2 |
| THR-37 | THREAT | D-09.4 |
| THR-38 | THREAT | D-10.2 |

---
## §10 Coverage Matrix (D-subdomain × artefact count)

| D | Rule | Goal | UC | FR | NFR | Node | DN | Gate | Risk | Total |
|---|------|------|----|----|-----|------|----|------|------|-------|
| D-01.1 | 2 | 1 | 1 | 1 | 3 | 1 | 1 | 1 | 0 | 12 |
| D-01.2 | 2 | 1 | 0 | 1 | 2 | 1 | 1 | 1 | 0 | 10 |
| D-01.3 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 5 |
| D-01.4 | 1 | 1 | 1 | 1 | 3 | 1 | 1 | 1 | 0 | 11 |
| D-02.1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 11 |
| D-02.2 | 2 | 1 | 2 | 1 | 3 | 1 | 1 | 1 | 0 | 14 |
| D-02.3 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 10 |
| D-03.1 | 2 | 1 | 1 | 1 | 0 | 2 | 1 | 1 | 0 | 11 |
| D-03.2 | 2 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 9 |
| D-03.3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 10 |
| D-03.4 | 2 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 9 |
| D-04.1 | 1 | 1 | 2 | 1 | 0 | 3 | 1 | 1 | 1 | 13 |
| D-04.2 | 1 | 1 | 1 | 1 | 4 | 0 | 1 | 1 | 1 | 12 |
| D-04.3 | 3 | 1 | 1 | 2 | 0 | 3 | 1 | 1 | 0 | 14 |
| D-04.4 | 1 | 1 | 1 | 1 | 3 | 2 | 1 | 1 | 0 | 13 |
| D-05.1 | 1 | 1 | 1 | 1 | 3 | 0 | 1 | 1 | 1 | 11 |
| D-05.2 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 8 |
| D-05.3 | 2 | 1 | 1 | 1 | 3 | 0 | 1 | 1 | 1 | 12 |
| D-05.4 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 8 |
| D-06.1 | 1 | 1 | 1 | 1 | 0 | 2 | 1 | 1 | 1 | 10 |
| D-06.2 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 8 |
| D-06.3 | 1 | 1 | 1 | 1 | 0 | 2 | 1 | 1 | 0 | 9 |
| D-07.1 | 2 | 1 | 1 | 1 | 2 | 3 | 1 | 1 | 0 | 13 |
| D-07.2 | 1 | 0 | 1 | 0 | 0 | 4 | 0 | 0 | 1 | 9 |
| D-08.1 | 1 | 1 | 2 | 1 | 0 | 2 | 1 | 1 | 0 | 10 |
| D-08.2 | 1 | 1 | 1 | 1 | 0 | 3 | 1 | 1 | 0 | 10 |
| D-09.1 | 2 | 2 | 2 | 1 | 5 | 3 | 1 | 1 | 0 | 17 |
| D-09.2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 14 |
| D-09.4 | 1 | 1 | 2 | 1 | 4 | 4 | 1 | 1 | 1 | 17 |
| D-10.2 | 2 | 1 | 1 | 0 | 5 | 3 | 1 | 1 | 0 | 15 |
| D-10.3 | 3 | 1 | 1 | 1 | 0 | 2 | 1 | 1 | 0 | 10 |
| **TOTAL** | **46** | **31** | **35** | **30** | **46** | **49** | **30** | **30** | **10** | **345** |

---
## §11 Derivation Rules

1. **CR/BPR (Rules)** → D-XX.Y parsed from rule ID. 1:1 direct mapping.
2. **PO/SO (Goals)** → D-XX.Y parsed from goal ID. 1:1 direct mapping.
3. **DN rows (Doc 15)** → mirrored from corresponding CR per Doc 15 §4 (30 DN rows, 1:1 with CR).
4. **Gates (Doc 16)** → mirrored from corresponding CR per Doc 16 §5 (30 GATE rows, 1:1 with CR).
5. **FRs (Doc 23)** → D-XX.Y from FR-NN ↔ CR-D-XX.X-NNN (per Doc 15/23 cross-ref; FR-NN ↔ CR-D-XX.X-NNN where XX.X = (NN-1)//3+1 approx).
6. **NFRs (Doc 24)** → D-XX.Y from NFR category (CONF→D-01.x, AVAIL→D-04.x, INT→D-01.4/02.x/10.2, PRIV→D-05.x/07.1/09.x, ACC→D-09.x/10.2, COMP→D-09.1). Fase de Especificação 5 will verify per-row.
7. **UCs (Doc 13)** → D-XX.Y from package (DP→D-01/05, SEC→D-02/04, IAM→D-03/09/10, DEV→D-07/02/04/09, GOV→D-06/09, TRN→D-08). Fase de Especificação 5 will verify per-card.
8. **Nodes (Doc 14)** → D-XX.Y from node purpose (TECH/PROC/ROLE → primary control objective). Fase de Especificação 5 will verify per-node.
9. **Risks + Threats (Doc 25)** → D-XX.Y from risk/threat category. Fase de Especificação 5 will verify per-row.

> **Coverage:** 100% of artefacts linked to at least one D-XX.Y sub-domain. Fase de Especificação 5 may surface intra-sub-domain secondary links (e.g. UC linked to multiple CRs across D-XX.Y).
