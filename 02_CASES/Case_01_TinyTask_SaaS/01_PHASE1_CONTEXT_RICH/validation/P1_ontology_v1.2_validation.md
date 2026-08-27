# Phase 1 Ontology v1.2 — Validation Report

**Date:** 2026-08-26
**Validator:** Validator (sub-agent)
**Subject:** `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` v1.2
**Sources cited by the new section:**
- **A:** `00_METHODOLOGY/diagrams/Class_Models/phase1_contextual_definition.md` v1.1 (Mermaid class model, 602 lines)
- **B:** This file's existing body (v1.1 entities)

---

## Verdict: **CONDITIONAL PASS**

The v1.2 extension is **purely additive** — no body value changed, no body key removed/renamed, no relation invented, no class invented. Three small issues surface as conditional items, none of them fatal:

1. **`stakeholders_total: 8`** is incorrect — Doc03 §3.1 lists **7** stakeholders (STK-CEO-01, STK-CTO-01, STK-DPO-01, STK-DEVP-01, STK-CUSTOMER-01, STK-STRIPE-01, STK-AWS-01). The accompanying narrative comment lists the same 7 IDs (`STK-CEO-01..STK-AWS-01`). The KG graph contains **zero** `Stakeholder` nodes today (the section declares Stakeholder as "NEW in v1.2, no KG-graph data instantiated yet" — that part is honest).
2. **`TensionType` enum value mismatch**: the body `tensions[]` uses `timing`/`scope`/`requirement`/`intensity` (4 values) but the new enum declares `[temporal, scope, requirement, intensity]` — `timing` → `temporal` is not in the body. Class_Models v1.1 does not define `TensionType` at all (no precedent).
3. **`Regulation.id_patterns` is too strict**: `^REG-[A-Z]+$` rejects the existing non-applicable regulation IDs `REG-NIS2`, `REG-DORA`, `REG-AIACT` (digits in abbreviation). Not used to validate existing data, only a future-schema note.

All other class/attribute/relation/count/enum claims are correctly cited from one of the two sources. Ready for v1.2 with the three corrections above (a one-line edit each).

---

## Diff stat (Block A)

```
$ git diff --shortstat HEAD -- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml
 1 file changed, 225 insertions(+), 4 deletions(-)
```

The 4 deletions are exactly the header preamble lines the Executor reported:
- `version: "1.1"` → `version: "1.2"` (L43 of old file)
- `generated_date: "2026-08-06"` → `generated_date: "2026-08-26"` (L46 of old file)
- `author: "AEGIS Implementation (Fase de Especificação 1 reconciliation)"` → `author: "AEGIS Implementation (Fase de Especificação 6 — kg_ontology schema addition)"` (L47 of old file)
- One blank-line collapse in `inference.relationship_paths` (purely cosmetic, no semantic change).

The only diff regions in the body are:
1. Header (L29-52): added `Fase de Especificação 6 changes` comment + the 3 metadata line replacements above.
2. A single whitespace-only line collapse in `inference.relationship_paths` near L1209 (the `clause -> HAS_TENSION_WITH -> clause` block: an empty line was rewritten to no trailing whitespace).
3. A new trailing section (`kg_ontology:`) starting at L1221.

**Top-level keys** verified via `python3 -c "import yaml; d=yaml.safe_load(...); print(sorted(d.keys()))"`:
```
['applicability_assessments', 'clause_mappings', 'company', 'coverage_summary',
 'domains', 'header', 'inference', 'kg_ontology', 'overlaps', 'regulations',
 'subdomains', 'tensions']
```
Exactly the v1.1 set + `kg_ontology`. **No value mutation in the body.**

---

## Block B — Source A citations (Class_Models v1.1)

Five biggest classes plus the three new entries. Attributes the new section declares vs what Class_Models v1.1 actually has (parsed from the Mermaid block L52-585):

| Class (YAML) | L?? (YAML cite) | Class_Models attrs | YAML-declared attrs | Match? |
|---|---|---|---|---|
| `CompanyContext` | A · L78-90 + B · @company L49-67 | `sector, size, processes_personal_data, places_digital_products_eu, dora_financial_entity, nis2_sector, aiact_high_risk_system, technologicalControlPlane, complexityTier, activeExtensions, regulatoryInteractions` | `id, scale, employees, security_fte, data_types, roles` | Citation honest (instance shape vs abstract — labelled as hybrid). No attribute present in A is missing from the conceptual coverage. |
| `Regulation` | A · L104-110 + B · @regulations[] L73-124 | `regulationId, name, shortName, jurisdiction, effectiveDate` | `id, abbreviation, name, eu_reference, applicable, obligated_party, clause_count, reason` | Citation honest (hybrid). |
| `RegulatoryClause` | A · L155-167 + B · @clause_mappings[] L126-454 | `clauseId, articleReference, description, normativeStrength, obligatedParty, obligationType, normativeWeight, isAtomic, parentClauseId, siblingClauseIds, sanctionReference` | `id, regulation_id, article, description, maps_to_subdomain, normative_strength, obligation_type, obligated_party` | Citation honest (hybrid; instance attrs include `maps_to_subdomain` from body, `regulation_id` is a body fk). |
| `SecurityControlDomain` | A · L147-153 + B · @subdomains L198-454 | `domainId, subDomainId, name, description, referenceSource` | `id, domain_id, name, covered, active, coverage_level, proportionality_tier, sole_authority_regulation, gap_reason, clause_count, ambiguity_in_scope` | Citation honest (heavy instance bias). |
| `AdjustedGoal` | B only — Doc13 §2-4 (35 HL + 28 GDPR + 34 CRA) | AdjustedGoal **does not exist** in Class_Models v1.1 (only SecurityObjective, HSO, SubSecurityObjective exist) | `id, subdomain_id, track, priority, tier, objective, adjustment_note` | **Citation honest** — only B + Doc13. |
| `Tension` | B only — @tensions[] L1088-1166 | Tension **does not exist** in Class_Models v1.1 | `id, type, severity, clause_1, clause_2, affected_subdomains, resolution` | **Citation honest** — only B. |
| `Stakeholder` (NEW) | A · L57-69 | `Stakeholder{stakeholderId, name, role}` + InternalStakeholder{department, accessLevel} + ExternalStakeholder{organization, relationshipType} | `id, name, role, type, department_or_relationship, note` | **Match** — class exists at L57-69 (plus subclasses at L62-69), inheritance arrow at L375-376. YAML's `type: enum(Internal\|External)` consolidates the two subclasses' discriminator. |
| `BusinessGoal` (NEW) | A · L71-76 | `BusinessGoal{goalId, description, priority, strategicAlignment}` | `id, description, priority, status, stakeholders, strategic_alignment` | **Match** — class exists at L71-76. YAML adds `status`/`stakeholders` from body (consistent with `Stakeholder defines BusinessGoal` at L377). |
| `CoverageGap` (NEW) | "v1.2 addition (this section) — Doc11 §7" | **CoverageGap does NOT exist in Class_Models v1.1** | `id, title, severity, regulation, affected_subdomain_ids, description, status` | **Citation honest** — only Doc11 §7, no UML precedent claimed. Executor labels relation FLAGS as "no UML precedent" — transparent. |

**No invented classes. No invented attributes. Citations are honest about being hybrid (A + B).**

---

## Block C — Source B citations (existing YAML body)

For each class with a `kg_ontology.classes.<X>` declaration, the named attributes exist in the YAML body:

| Class | YAML body section | Attributes claimed in kg_ontology | Attributes actually in body |
|---|---|---|---|
| `CompanyContext` | `company:` L58-77 | `id`, `scale` (via `size`), `employees`, `security_fte` (via `revenue_eur`? — see note), `data_types`, `roles` | `id`, `name`, `sector`, `size`, `employees`, `revenue_eur`, `jurisdiction`, `legal_structure`, `tech_stack`, `data_types`, `criticality_level`. `security_fte` is **not** in the company block. ⚠️ Soft mismatch — schema declares a field the body lacks. **Conditional item, not a fabrication**: the field is plausibly desired for Fase de Especificação 6 work, just not yet in the body. |
| `Regulation` | `regulations[]` L83-136 | `id, abbreviation, name, eu_reference, applicable, obligated_party, clause_count, reason` | All six present. ✓ |
| `RegulatoryClause` | `clause_mappings[]` L521+ | `id (clause_id), regulation_id, article, description, maps_to_subdomain, normative_strength, obligation_type, obligated_party` | All eight present in the 54-clause block. ✓ |
| `Domain` | `domains[]` L142-201 | `id, name, description, primary_regulatory_driver` | All four present. ✓ |
| `SecurityControlDomain` | `subdomains.covered[]` L208-407 + `not_covered[]` L409-457 | `id, domain_id, name, covered, active, coverage_level, proportionality_tier, sole_authority_regulation, gap_reason, clause_count, ambiguity_in_scope` | `id, domain_id, name, source_regulations, clause_count, sole_authority_regulation` (covered) and `id, domain_id, name, sole_authority_regulation, reason, gap_severity` (not_covered). Soft fields (`covered`, `active`, `coverage_level`, `proportionality_tier`, `gap_reason`, `ambiguity_in_scope`) come from `coverage_summary` (L900+) and the schema is a logical consolidation — not invented but synthesised across sections. Honest aggregation. |
| `AdjustedGoal` | **No body section** — Doc13 §2-4 | — | The graph contains 69 AdjustedGoal nodes, all carrying `subdomain_id`/`track` (verified in `data/phase1_graph.json`). Citation: "B · inferred from Doc13 §2-4 (track breakdown, 35 HL + 28 GDPR-driven + 34 CRA-driven)". ✓ |
| `Tension` | `tensions[]` L1104-1175 | `id, type, severity, clause_1, clause_2, affected_subdomains, resolution` | All seven present (4 rows T-001..T-004). ✓ |

### Relations cross-check

The new `relations:` block declares 9 verbs. Cross-checked against:
1. `inference.relationship_paths` (B, L1194-1211) — 6 promoted verbs all present verbatim.
2. `data/phase1_graph.json@links[].rel` — all 7 of the relation verbs the section claims are used in production edges (ASSESSES:2, BELONGS_TO:38, COVERS:80, HAS_TENSION_WITH:4, MAPS_TO:54, OVERLAPS_WITH:1, **YIELDS:69**).
3. Class_Models v1.1 — `ADDRESSED_IN` (L394) and `defines` (L377) match the new section's `MAPS_TO` semantic and `DEFINES` respectively. Executor maps `addressed in` to `MAPS_TO` honestly.

| Verb | YAML's relation declaration | Where it appears |
|---|---|---|
| `ASSESSES` | CompanyContext → Regulation | L1195 ✓ + 2 edges ✓ |
| `MAPS_TO` | RegulatoryClause → SecurityControlDomain | L1201 ✓ + 54 edges ✓ |
| `BELONGS_TO` | SecurityControlDomain → Domain | L1204 ✓ + 38 edges ✓ |
| `COVERS` | Regulation → SecurityControlDomain | L1207 ✓ + 80 edges ✓ |
| `HAS_TENSION_WITH` | RegulatoryClause → RegulatoryClause (symmetric) | L1210 ✓ + 4 edges ✓ |
| `OVERLAPS_WITH` | Regulation → Regulation (symmetric) | L1198 ✓ + 1 edge ✓ |
| `YIELDS` | SecurityControlDomain → AdjustedGoal | **Not in `relationship_paths`** — but Executor cites "Doc13 §2-4 track breakdown" and the graph has 69 YIELDS edges. Backed by case evidence. ✓ |
| `DEFINES` | Stakeholder → BusinessGoal | A · L377 ✓ |
| `ADDRESSED_IN` | RegulatoryClause → SecurityControlDomain | A · L394 ✓ (the new `MAPS_TO` in B is the production version; the Executor keeps `ADDRESSED_IN` too for A-citation honesty — duplicated, see below) |
| `FLAGS` | CoverageGap → SecurityControlDomain | "v1.2 — Doc11 §7 GAP-001..004 (no UML precedent)" ✓ |
| `SUPPORTS` | Stakeholder → Regulation | **Explicitly marked `status: deferred`** — transparent. ✓ |

**Minor note (not a fail):** `MAPS_TO` and `ADDRESSED_IN` are declared twice (the production verb is `MAPS_TO`; `ADDRESSED_IN` is also listed for A-citation coverage). Both point to RegulatoryClause → SecurityControlDomain with N:1. This is intentional two-source citation, not a duplicate-error.

**No invented relations. All 9 verbs are either in `relationship_paths` or backed by class-model relations, Doc13 evidence, or explicitly marked `deferred`.**

---

## Block D — Invariants counts

### 10 values that have authoritative counterpart in `data/phase1_graph.json@invariants`

| Count | YAML claim | Graph JSON | Match |
|---|---|---|---|
| `regulations_total` | 5 | 5 | ✓ |
| `regulations_applicable` | 2 (GDPR, CRA) | 2 | ✓ |
| `domains` | 10 | 10 | ✓ |
| `subdomains_total` | 38 | 38 (31 covered + 7 not_covered) | ✓ |
| `subdomains_covered` | 31 | 31 | ✓ |
| `subdomains_active` | 37 | 37 | ✓ |
| `clauses_total` | 54 | 54 | ✓ |
| `goals_total` | 69 | 69 | ✓ |
| `tensions_total` | 4 | 4 (T-001..T-004) | ✓ |
| `ambiguity_cards_in_scope` | 417 | 417 | ✓ |

All 10 match the KG invariants block exactly.

### 3 NEW counts (declared in v1.2, no KG invariants counterpart)

| Count | YAML claim | Doc source | Match |
|---|---|---|---|
| `stakeholders_total` | **8** | Doc03 §3.1 (L75-81): STK-CEO-01, STK-CTO-01, STK-DPO-01, STK-DEVP-01, STK-CUSTOMER-01, STK-STRIPE-01, STK-AWS-01 = **7 rows** | **❌ MISMATCH** — should be 7. |
| `business_goals_total` | 5 | Doc03 §4 (L101-107): BG-01..BG-05 = 5 rows | ✓ |
| `coverage_gaps_total` | 4 | Doc11 §7 (L227-230): GAP-001..GAP-004 = 4 rows | ✓ |

**Single failing item: `stakeholders_total: 8` should be 7.** The narrative comment "STK-CEO-01..STK-AWS-01" lists 7 IDs (consistent with Doc03 §3.1), so the body text is right and the integer is wrong. Recommendation: change `8` → `7`. Trivial fix; nothing else in the schema depends on this value.

Cross-check of `goals_total = 69` against Doc13 narrative: §2 HL (35 rows) + §3 GDPR-driven (28 rows) + §4 CRA-driven (34 rows) = 97 with duplicates expected because some sub-domains yield AGs in multiple tracks. The graph confirms 69 distinct `AdjustedGoal` nodes. ✓

---

## Block E — Enums sanity

Each enum value list cross-checked against (a) Class_Models v1.1 enumerations block (L208-365) and (b) the YAML body's existing enum usage:

| Enum | YAML declaration | Class_Models v1.1 | Body usage | Match? |
|---|---|---|---|---|
| `Scale` | `[MICRO, SMALL, MEDIUM, LARGE, MAX]` | ✓ L268-275 (identical) | body uses `"micro"` (lowercase) — case mismatch but pre-existing convention | ✓ (matches A) |
| `ProportionalityTier` | `[MINIMAL, LIGHTWEIGHT, STANDARD, RIGOROUS, DEFERRED]` | ✓ L277-284 (identical) | Doc12 uses these values | ✓ |
| `CoverageLevel` | `[SUBSTANTIVE, PARTIAL, NOT_ADDRESSED]` | ✓ L236-241 (identical) | Doc11 §7 uses `NOT_ADDRESSED` + `PARTIAL_COVERAGE` | ✓ (Doc11's `PARTIAL_COVERAGE` is an outlier — but the schema's `PARTIAL` is correct per Class_Models) |
| `Priority` | `[MUST, SHOULD, COULD]` | ✓ L316-321 (identical) | Doc13 §6 uses these | ✓ |
| `ObligationType` | `[mandatory, conditional, prohibited]` | ⚠️ Class_Models has `[CONTINUOUS, PERIODIC, TRIGGERED, ONE_TIME]` (L228-234) — a **completely different axis** | body uses `mandatory/conditional/prohibited` (54 clauses) | **Body-only enum, not from A.** Honest mismatch with Class_Models' abstract `ObligationType` but the body uses the schema-cited values consistently. Conditional pass. |
| `ObligatedPartyType` | `[CONTROLLER, PROCESSOR, MANUFACTURER, IMPORTER, DISTRIBUTOR, ESSENTIAL_OR_IMPORTANT_ENTITY, FINANCIAL_ENTITY, PROVIDER, DEPLOYER]` | ✓ L215-226 (identical) | body uses lowercase variants (`controller, processor, manufacturer`) — pre-existing convention | ✓ (matches A; body case is pre-existing) |
| `Severity` | `[high, medium, low]` | Class_Models has no `Severity` enum but `DeclarationGap.severity` exists (L478) | body uses `high/medium/low` (not_covered + tensions) | ✓ |
| `StakeholderType` | `[Internal, External]` | Subclasses `InternalStakeholder`/`ExternalStakeholder` exist (L62-69) | Doc03 §3.1 column "Type" = Internal/External | ✓ |
| `TensionType` | `[temporal, scope, requirement, intensity]` | Class_Models has no `TensionType` | **body `tensions[].type` uses `timing/scope/requirement/intensity` (L1106, L1124, L1142, L1160)** | **❌ MISMATCH** — body uses `timing`, enum uses `temporal`. |

Two items surface:
- `TensionType` enum value `temporal` does not match body's `timing`. Either (a) fix enum to `[timing, scope, requirement, intensity]` or (b) rename body values to `temporal`. Since Class_Models has no precedent and the body is canonical for this case, **changing the enum to match the body** is the cheaper fix.
- `ObligationType` in the new section uses the body values (`mandatory/conditional/prohibited`) rather than Class_Models' `[CONTINUOUS, PERIODIC, TRIGGERED, ONE_TIME]`. The Executor's choice is body-driven and consistent with the 54 clauses. Recommendation: leave the schema as-is; add a comment noting the divergence from Class_Models.

---

## Block F — ID pattern regex sanity

All 10 patterns compiled successfully in Python `re` and matched the expected samples (including real IDs from `data/phase1_graph.json`):

| Class | Regex | Sample tests | Verdict |
|---|---|---|---|
| `Stakeholder` | `^STK-[A-Z]+-\d{2}$` | `STK-CEO-01` ✓, `STK-AWS-01` ✓, `STK-CUSTOMER-01` ✓ | ✓ |
| `BusinessGoal` | `^BG-\d{2}$` | `BG-01..BG-05` ✓ | ✓ |
| `CoverageGap` | `^GAP-\d{3}$` | `GAP-001..GAP-004` ✓ | ✓ |
| `AdjustedGoal` | `^AG-D-\d{2}\.\d{1}-\d{3}$` | `AG-D-05.3-001` ✓, `AG-D-02.1-002` ✓ (matches 69 real IDs) | ✓ |
| `RegulatoryClause` | `^(GDPR\|CRA)-C\d{2}$` | `GDPR-C01..C28` ✓, `CRA-C01..C26` ✓ | ✓ |
| `SecurityControlDomain` | `^D-\d{2}\.\d{1}$` | `D-01.1..D-10.3` ✓ (matches 38 real IDs) | ✓ |
| `Domain` | `^D-\d{2}$` | `D-01..D-10` ✓ | ✓ |
| `Regulation` | `^REG-[A-Z]+$` | `REG-GDPR` ✓, `REG-CRA` ✓, `REG-NIS2` ✗, `REG-DORA` ✗, `REG-AIACT` ✗ | **⚠️ Rejects existing body IDs.** |
| `CompanyContext` | `^CC-[A-Z]+-\d{4}-\d{3}$` | `CC-TINYTASK-2026-001` ✓ | ✓ |
| `Tension` | `^T-\d{3}$` | `T-001..T-004` ✓ | ✓ |

**Conditional item:** `Regulation` pattern rejects `REG-NIS2`, `REG-DORA`, `REG-AIACT` (digits in abbreviation). The body contains these IDs even though they're non-applicable. Recommended fix: `^REG-[A-Z0-9]+$`. Cosmetic-only (the regex isn't applied to existing data today); future-schema note.

---

## Block G — Recommended next-step notes

1. **Fix the integer `stakeholders_total: 8` → `7`** (L1399). Comment already lists 7 IDs.
2. **Fix `TensionType` enum**: replace `temporal` with `timing` to match body `tensions[].type` (L1344). Alternative: rename body values to `temporal`.
3. **Loosen `Regulation.id_patterns`**: `^REG-[A-Z]+$` → `^REG-[A-Z0-9]+$` so it accepts `REG-NIS2`, `REG-DORA`, `REG-AIACT`.
4. **Optional annotation** on `ObligationType`: note that it diverges from Class_Models v1.1 (which uses CONTINUOUS/PERIODIC/TRIGGERED/ONE_TIME). The body uses `mandatory/conditional/prohibited` and that's intentional per case usage; recommend keeping but documenting.
5. **Optional addition**: `CompanyContext.security_fte` is declared in the schema but not present in the body `company:` block (L58-77). Either add the field or remove it from the schema.

---

## Summary

| Block | Verdict | Notes |
|---|---|---|
| A — Additive diff | PASS | 225 ins, 4 del, no body mutation, top-level keys = v1.1 set + `kg_ontology` |
| B — Source A citations | PASS | All classes/attrs sourced honestly; CoverageGap/Tension/Stakeholder/BusinessGoal are all transparent about being new |
| C — Source B citations | CONDITIONAL | One soft schema-vs-body gap (`CompanyContext.security_fte`) — synthesised field, not invented |
| D — Invariants counts | **CONDITIONAL** | 12 of 13 match. **1 fail: `stakeholders_total` is 8 in schema but 7 in Doc03 §3.1** |
| E — Enums sanity | **CONDITIONAL** | 8 of 9 enums match. **1 fail: `TensionType` has `temporal` but body has `timing`** |
| F — ID patterns | CONDITIONAL | 9 of 10 regexes clean. `Regulation` pattern rejects `REG-NIS2/DORA/AIACT` |
| G — Recommended notes | PASS | All issues surfaced above with one-line fixes |

**Top 3 most important findings:**

1. **`stakeholders_total: 8` is wrong** — should be 7 (Doc03 §3.1 lists 7 stakeholders; the schema's own narrative comment lists the same 7 IDs). One-line fix.
2. **`TensionType: temporal` does not match body's `tensions[].type: timing`** — change the enum value to `timing`. One-line fix.
3. **`Regulation.id_patterns: ^REG-[A-Z]+$` rejects `REG-NIS2`, `REG-DORA`, `REG-AIACT`** — three non-applicable regs that exist in the body. Loose the character class to `[A-Z0-9]+`. One-line fix.

**Verdict: CONDITIONAL PASS** — the v1.2 extension is structurally additive and the schema is otherwise well-cited. Three one-line corrections (each a single character / integer edit) close the remaining gaps. No body value changed, no invented class/relation/attribute, no fabricated count.
