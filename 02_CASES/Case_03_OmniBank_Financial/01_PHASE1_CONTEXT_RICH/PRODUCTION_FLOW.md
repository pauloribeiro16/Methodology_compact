---
document_id: AEGIS-CASE03-P1-PROD-FLOW
title: "PRODUCTION_FLOW — Case_03 Phase 1 (Layers 0/1/2)"
phase: 1
version: 1.0
created: 2026-08-28
updated: 2026-08-28
author: Orchestrator (port campaign Fase 7)
status: ACTIVE
case: Case_03_OmniBank_Financial
note: META document — not a numbered deliverable. Mirrors the Case_01/Case_02
  instances; Case_03 slot map differs (Doc11_DORA inserted; P2 = Doc15–Doc20).
---

# PRODUCTION_FLOW — Case_03 Phase 1

## Layer 0 — Phase 0 frozen baseline (read-only)

Consumes `00_METHODOLOGY/PREPROCESSING_by_domain/` (guard-protected), citing
never modifying. Case_03 consumes the widest slice of the corpus: 5/5
regulations, 150 clauses, 38/38 sub-domains. DORA articles are anchored via
the corpus `DORA_Art_*` files and the case-local `Doc11_DORA_ICT_Risk_Framework.md`.

## Layer 1 — Document flow (14 deliverables — corr-010 slot map)

```
Doc01_Taxonomy_Reference → Doc02_INTAKE_FORM → Doc03_Company_Context_Assessment
                              ├→ Doc04_Architecture_DataInventory (lens)
                              ├→ Doc06_ThirdParty_Landscape (lens, DORA CTPP register)
                              └→ Doc07_Org_Roles_RACI (lens)
Doc02 → Doc05_Security_Posture (DEPRECATED_FOR_POSTURE; ownership → Doc20)
Doc03/04 → Doc08_Regulatory_Applicability → Doc10_Clause_Mapping_Matrix
Doc10 → Doc11_DORA_ICT_Risk_Framework (DORA-specific: 38 clauses, T-005, TLPT)
Doc08/10/11 → Doc12_Structured_Compliance_Matrix → Doc13_Proportionality_Profile
Doc12/13 → Doc14_Adjusted_Goals  (SOLE goal producer: 76 AG-D-XX.Y-001/-002)
Doc09_Ambiguity_Register (sidecar, 1,490 cards)
```

P1 → P2 hand-off (Case_03 slot map): Doc14 goals → Doc15 obligations
(OBL-D-XX.Y-NNN) → Doc17 objectives (AG-D-, corr-012 PO/SO split deferred) →
Doc19 Control Set (CR/BPR-D-XX.Y-NNN, 78 controls) → Doc20 aggregate matrix.
P3 = Doc22–Doc31 (complete). NOTE: C2's Doc20_NIST_Framework_Inputs has no
Case_03 counterpart (port rule: map by content, not number).

## Layer 2 — Infrastructure

- `phase1_ontology.yaml` v2.0-port — canonical kg_ontology instance with the
  **DORA branch** (`RegulatoryClause: ^(GDPR|CRA|NIS2|DORA|AI)-C\d{2}$`),
  posture block, invariants (150 clauses, AI-C19 KEPT — PROVIDER+DEPLOYER,
  `dora_coverage: via_CSF`, 5 tensions).
- Graph build + dashboard DEFERRED (mirrors the Case_02 locked decision).
- KG E3 contains no Case_03 nodes (verified: `kg.sh impact` no-match) — first
  ingest will use this instance; no F-S1-09-style contamination.

## §3 Goal-linkage matrix

Doc14 is the sole AdjustedGoal producer: **76 goals** = 38 sub-domains ×
privacy `-001` + security `-002` (38/38 active — no NOT_ADDRESSED sub-domains
in Case_03). Lens declarations:

| Document | serves_goals |
|---|---|
| Doc04_Architecture_DataInventory | all AG-D-XX.Y-001/-002 (architecture lens) |
| Doc06_ThirdParty_Landscape | AG-D-06.x sets + DORA Art. 28-30 CTPP-related goals |
| Doc07_Org_Roles_RACI | AG-D-08.x/09.1 sets (people/roles lens) |
| Doc14_Adjusted_Goals | producer (76 AG nodes) |

## §5 Exit criteria (P1 → P2)

All deliverables present with clean frontmatter; §3 matrix authoritative;
inputs/outputs resolve; ontology YAML parses; both gates
(`02_PHASE2_RULES_RICH/validation/check_unmapped.py`,
repo-root `validation/check_implementation_posture_case03.py`) exit 0;
progress.json + CHANGE_LOG_CENTRAL carry the campaign records.

## §6 Open items

1. Layer 2 graph build + dashboard (deferred, as Case_02).
2. corr-012: PO/SO split in P2 objectives (registered pending item; P7
   decision 2026-08-28 — AG- retained).
3. `_deprecated/Doc15_Appendix_A_OLD.md` carries malformed legacy alias IDs
   (`AG-D-D-*`); historical file — fix or delete is a P7 call.
4. Doc08 §8D-style local decompositions and 00_METHODOLOGY/REFERENCE|SCHEMA
   references point to upstream-corpus artefacts absent from the compact repo.
5. CSF frozen-list membership check is WARN-only (list not mirrored in the
   compact repo) — shared limitation with Case_02.
