---
document_id: AEGIS-CASE02-P1-PROD-FLOW
title: "PRODUCTION_FLOW — Case_02 Phase 1 (Layers 0/1/2)"
phase: 1
version: 1.0
created: 2026-08-28
updated: 2026-08-28
author: Orchestrator (port campaign Fase 7)
status: ACTIVE
case: Case_02_SecureBorder_Solutions
note: META document — not a numbered deliverable. Mirrors the Case_01
  instance (Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/PRODUCTION_FLOW.md)
  per the cross-case recommendation in P1_cross_case_mirror_v0.md.
---

# PRODUCTION_FLOW — Case_02 Phase 1

## Layer 0 — Phase 0 frozen baseline (read-only)

Consumes `00_METHODOLOGY/PREPROCESSING_by_domain/` (guard-protected):
38 D-XX.Y files, manifests, 623 articles, NIST control JSONs, overlays.
Case docs CITE the baseline; they never modify it. See
`00_METHODOLOGY/PREPROCESSING_by_domain/PRODUCTION_FLOW.md` v2.0 (stages
C1 verbatim anchoring → C2 hierarchical objectives → C3 Volere cards →
C4 cross-regulation analysis → C5 ambiguity registration → C6 freeze).
Known baseline gaps (D-10.1/10.2/10.3 Part 2+3 stubs) are worked around,
never backported into case content.

## Layer 1 — Document flow (13 deliverables, corr-008/corr-010 naming)

```
Doc01_Taxonomy_Reference (root vocabulary, 00_COMMON mirror)
Doc02_INTAKE_FORM → Doc03_Company_Context_Assessment
                     ├→ Doc04_Architecture_DataInventory (lens)
                     ├→ Doc06_ThirdParty_Landscape (lens)
                     └→ Doc07_Org_Roles_RACI (lens)
Doc02 → Doc05_Security_Posture (DEPRECATED_FOR_POSTURE; posture ownership → Doc19)
Doc03/04 → Doc08_Regulatory_Applicability → Doc10_Clause_Mapping_Matrix
Doc08/10 → Doc11_Structured_Compliance_Matrix → Doc12_Proportionality_Profile
Doc10/12 → Doc13_Adjusted_Goals  (SOLE goal producer: 70 AG-D-XX.Y-NNN)
Doc09_Ambiguity_Register (sidecar, feeds Doc08/Doc12)
```

P1 outputs consumed by P2: Doc13 goals (AG-D-XX.Y-001/-002) → Doc14
obligations (OBL-D-XX.Y-NNN) → Doc16 objectives (PO/SO-D-XX.Y-NNN) →
Doc18 Control Set (CR/BPR-D-XX.Y-NNN) → Doc19 aggregate matrix.
Case_02 numbering continues into P3 (Doc21–Doc30); the P2-local Doc20
(NIST_Framework_Inputs, generated) is a JUSTIFIED-EXTENSION.

## Layer 2 — Infrastructure (ontology → graph → dashboard)

- `phase1_ontology.yaml` v2.2 — D1-consistent (111 clauses) and schema-aligned:
  instantiates the canonical `kg_ontology` schema of the Case_01 ontology
  (ontology-first rule: schema defined once, case instantiates).
- Graph build (`build_p1_graph.py` → `data/phase1_graph.json`) and dashboard
  are **DEFERRED by locked port decision 2** (2026-08-28): documents + ontology
  alignment only. When built, the KG/dash validation from the Case_01
  ontology-lineage reports applies unchanged.
- KG E3 caveat: `kg.sh impact PG-D-01.1` still resolves to E3 nodes labelled
  with legacy PG labels (F-S1-09 contamination nodes); stale until the next
  graphify re-ingest in the main repo.

## §3 Goal-linkage matrix (AdjustedGoal coverage)

Doc13 is the sole AdjustedGoal producer: **70 goals** = 35 sub-domains ×
privacy set (`AG-D-XX.Y-001`) + security set (`AG-D-XX.Y-002`); 3 NOT_ADDRESSED
sub-domains (D-07.4, D-08.3, D-09.3) produce none. Lens-doc declarations:

| Document | serves_goals |
|---|---|
| Doc04_Architecture_DataInventory | all AG-D-XX.Y-001/-002 (architecture lens, 35 sub-domains) |
| Doc06_ThirdParty_Landscape | AG-D-06.1-001/-002 … AG-D-06.4-001/-002 (supply-chain lens) |
| Doc07_Org_Roles_RACI | AG-D-08.1/08.2/09.1 sets (people/roles lens) |
| Doc13_Adjusted_Goals | producer (70 AG nodes) |

## §5 Exit criteria (P1 → P2)

All 13 deliverables present and frontmatter-clean; §3 matrix authoritative;
every `inputs:`/`outputs:` basename resolves (post port Fase 1 repair);
ontology YAML parses and is D1-consistent; both gates
(`02_PHASE2_RULES_RICH/validation/check_unmapped.py`,
repo-root `validation/check_implementation_posture_case02.py`) exit 0;
progress.json carries the campaign events; CHANGE_LOG_CENTRAL records them.

## §6 Open items

1. Layer 2 graph build + dashboard (deferred — decision 2, port 2026-08-28).
2. KG E3 stale PG/SG labels (F-S1-09, human approval required for re-run).
3. Doc08 §8D Sprint-5 local AI_Act decomposition (29 rows, own C-coding) —
   documented divergence, reconciliation candidate for a dedicated session.
4. Doc05 ORPHAN-HYBRID posture redirect (posture_owner → Doc19) mirrors the
   Case_01 pattern; final deletion decision is P7.
5. Cross-case transversal: Doc20 generated cross-ref is Case_02-specific;
   Cases 02/03 doc-slot alignment (corr-010) completed here for slot 13 only.
