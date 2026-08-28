---
document_id: AEGIS-CASE02-PORT-ONT-VAL
title: "P1 ontology port validation (v2.1 D1 propagation + v2.2 kg_ontology alignment)"
phase: 1
version: 1.0
created: 2026-08-28
updated: 2026-08-28
author: Validator (port Fase 2)
status: ACTIVE
case: Case_02_SecureBorder_Solutions
---

# P1 ontology port validation — Case_02 phase1_ontology.yaml

## Scope

Port Fase 0 + Fase 2 changes to `01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml`,
checked against the canonical sources (Case_01 ontology v1.6 lineage,
`IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md` v2.0, `00_COMMON` frozen copy).

## Checks

| # | Check | Result |
|---|-------|--------|
| 1 | YAML parses (`yaml.safe_load`) | PASS |
| 2 | v2.1: AI-C19 commented out; active AI clauses = 28; total = 111 (verified programmatically) | PASS |
| 3 | v2.1: REG-AIAct `clause_count: 28`, `key_clauses_in_scope` notes D1 exclusion, Art. 26 dropped from `key_articles` | PASS |
| 4 | v2.2: `kg_ontology` section added as INSTANCE of the canonical schema (schema pointer to Case_01 `kg_ontology`; no schema redefinition — ontology-first rule) | PASS |
| 5 | v2.2: `AdjustedGoal` pattern matches the migrated ID space (`AG-D-XX.Y-001/-002`, 70 goals) | PASS |
| 6 | v2.2: `RegulatoryClause` pattern covers the 4-regulation namespaces (GDPR/CRA/NIS2/AI) | PASS |
| 7 | v2.2: `forbidden_subdomain_attrs` = posture-model ban list (tier, maturity_*, capability_score) | PASS |
| 8 | v2.2: posture section cites Model v2.0, 3 states + 2 special categories + evidence rules | PASS |
| 9 | v2.2: `case_invariants` reflect post-D1 reality (111/28, 35 active, 3 NOT_ADDRESSED, 70 goals, 9 tensions) | PASS |
| 10 | Version history entry added; version bumped 2.1 → 2.2 | PASS |

## Known divergences (documented, not blockers)

1. **Doc08 §8D** uses a Sprint 5 local AI_Act article decomposition (29 rows,
   own `(Cnn)` coding, no Art. 26 row). Not reconciled to the canonical
   28-clause set in this port; counts in Doc08 now state the divergence
   explicitly instead of claiming canonical numbers.
2. **ThirdParty id_pattern** left generic; the vendor enumeration lives in
   Doc06 (single source). Case_01 hardcodes its 6 vendors in the pattern.
3. KG rebuild (E4) out of scope: `kg.sh impact PG-D-01.1` still resolves to
   E3 graph nodes labelled with legacy PG labels — stale until the next
   graphify re-ingest in the main repo (F-S1-09 pending, human approval).

## Verdict

PASS — ontology is D1-consistent and schema-aligned; graph build deferred by
locked port decision 2.
