---
document_id: AEGIS-CASE03-PORT-ONT-VAL
title: "P1 ontology port validation (v2.0-port kg_ontology alignment)"
phase: 1
version: 1.0
created: 2026-08-28
updated: 2026-08-28
author: Validator (port Fase 2)
status: ACTIVE
case: Case_03_OmniBank_Financial
---

# P1 ontology port validation — Case_03 phase1_ontology.yaml

## Scope

Port Fase 2 changes to `01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml`
(header 1.1 → 2.0-port; additive `kg_ontology` section), checked against the
canonical schema (Case_01 kg_ontology) and the Case_02 port precedent.

## Checks

| # | Check | Result |
|---|-------|--------|
| 1 | YAML parses (`yaml.safe_load`) | PASS |
| 2 | `kg_ontology` section added as INSTANCE of the canonical schema (no redefinition — ontology-first rule) | PASS |
| 3 | `RegulatoryClause` pattern covers **5 regulation namespaces incl. DORA**: `^(GDPR\|CRA\|NIS2\|DORA\|AI)-C\d{2}$` | PASS |
| 4 | `AdjustedGoal` pattern matches the corr-010 ID space (76 goals = 38× -001 + 38× -002, verified in Fase 0 census) | PASS |
| 5 | `forbidden_subdomain_attrs` = posture-model ban list | PASS |
| 6 | `implementation_posture` block cites Model v2.0, 3 states + special categories + evidence rules | PASS |
| 7 | `case_invariants`: 150 clauses, 38/38 active, DORA 38, `dora_coverage: via_CSF`, 76 goals, 5 tensions | PASS |
| 8 | AI-C19 decision recorded: KEPT (PROVIDER + DEPLOYER) — inverse of Case_02 D1 | PASS |
| 9 | `inference.version` restored to 1.1 (port bump applies to header only) | PASS |
| 10 | 00_COMMON copy divergence resolved: P1 RICH copy declared canonical; 00_COMMON = frozen legacy | PASS |

## Known divergences (documented, not blockers)

1. `00_METHODOLOGY/SCHEMA/tensions.yaml` referenced in the ontology preamble
   does not exist in the compact repo — upstream-corpus reference, marked.
2. Doc11 §4 declares "5 cross-regulation tensions"; Doc17 carried 4 until
   port Fase 0 added T-005. Canonical set T-001..T-005 now consistent across
   Doc11 / Doc17 / ontology / state files.
3. KG E3 has no Case_03 nodes (kg.sh impact: no unique match) — no F-S1-09-style
   contamination; first ingest will use this v2.0-port instance.

## Verdict

PASS — DORA-aware, posture-aligned, schema-instantiated.
