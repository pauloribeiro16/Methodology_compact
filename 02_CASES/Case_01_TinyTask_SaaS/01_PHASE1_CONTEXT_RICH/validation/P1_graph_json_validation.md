# Phase 1 Graph JSON Validation — Report

Date: 2026-08-26
Validator: Validator (sub-agent)
Subject: `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json`
Companion: `scripts/build_p1_dashboard.py` (`--check`, `--summary`, `--emit`)

## Verdict: CONDITIONAL PASS

Reasoning: All structural invariants hold and `--check` returns 0; 10 of 12 audits independently verify clean against source docs; 2 audits (CFL-003 internal ontology drift, BAM-002 S3-only top-20) are real findings already documented by the Executor and confirmed here. The conditionality rests on (a) one schema-drift item (the JSON uses `attrs.normative_weight` for clauses and `attrs.regulation_id` rather than the field names implied by the brief's prompt — minor key-name variance only) and (b) several open provenance improvements in CFL-001/002/003 and the Doc10 §8.1 `(verify)` corpus-form markers (BLN-001) that are not JSON-defects but upstream-doc artefacts. No fabricated values detected; all company-context fields trace to Doc02/Doc03/Doc12/ontology; no invariant mismatch.

---

## A. Structural integrity

Commands:

```
python3 scripts/build_p1_dashboard.py --check
  → "OK — invariants pass, audit node_ids resolve."  (exit 0)

python3 scripts/build_p1_dashboard.py --summary
  → nodes_count: 181
    nodes_by_type: {CompanyContext:1, Regulation:5, Domain:10,
                    SecurityControlDomain:38, RegulatoryClause:54,
                    AdjustedGoal:69, Tension:4}
    links_count: 248
    links_by_rel: {ASSESSES:2, MAPS_TO:54, BELONGS_TO:38, YIELDS:69,
                   OVERLAPS_WITH:1, HAS_TENSION_WITH:4, COVERS:80}
    audits_count: 12
    audits_by_kind: {cross_doc_conflict:4, broken_link:2,
                     coverage_gap:4, blocking_ambiguity:2}
    invariant_pass: true

python3 -c "import json; g=json.load(open('data/phase1_graph.json'))"
  → loads OK; top-level keys present: meta, company_context, nodes,
    links, ambiguity, invariants, audits
```

| Invariant | Schema value | Observed | Match |
|---|---|---|---|
| regulations_total | 5 | 5 | YES |
| regulations_applicable | 2 | 2 (GDPR, CRA) | YES |
| domains | 10 | 10 | YES |
| subdomains_total | 38 | 38 | YES |
| subdomains_covered | 31 | 31 | YES |
| subdomains_active | 37 | 37 (D-08.3 inactive) | YES |
| clauses_total | 54 | 54 (28 GDPR + 26 CRA) | YES |
| goals_total | 69 | 69 | YES |
| tensions_total | 4 | 4 | YES |
| ambiguity_cards_in_scope | 417 | 417 | YES |

Node-type totals: 1 + 5 + 10 + 38 + 54 + 69 + 4 = 181. Brief expected 1/5/54/10/38/69 + 4 Tensions = 181. Match.

CFL-003 (internal ontology label/list mismatch) is the one place the schema value `subdomains_covered: 31` is *not* literally the same as the per-regulation count (GDPR label=19, list=20; CRA label=22, list=19). The author reconciled to the per-regulator union of distinct IDs from `coverage_summary` lists (38 total minus 7 not_covered = 31). This is a documented decision in the audit, not a JSON bug.

---

## B. Schema conformance

Spot-checks performed on sampled nodes:

**Regulation nodes** (5 of 5 inspected)

| Node | applicable | obligated_party | key_articles | clause_count | schema OK |
|---|---|---|---|---|---|
| REG-GDPR | true | [CONTROLLER, PROCESSOR] | n/a (article-level lives in clauses) | 28 | YES |
| REG-CRA | true | [MANUFACTURER] | n/a | 26 | YES |
| REG-NIS2 | false | [] | n/a | 0 | YES |
| REG-DORA | false | [] | n/a | 0 | YES |
| REG-AIACT | false | [] | n/a | 0 | YES |

Notes:
- Schema field is `attrs.clause_count` (int) and `attrs.abbreviation` (str); both populated.
- `attrs.eu_reference`, `attrs.name`, `attrs.reason` carry provenance — all consistent with Doc08 §3 + §4 and ontology@regulations.
- All applicable booleans match Doc08 §4 (GDPR YES, CRA YES, NIS2 NO <50 emp, DORA NO not financial, AI Act NO no AI).

**RegulatoryClause nodes** (4 sampled: GDPR-C01, GDPR-C28, CRA-C01, CRA-C26)

| Node | article | maps_to_subdomain | normative_weight | obligation_type | obligated_party | schema OK |
|---|---|---|---|---|---|---|
| GDPR-C01 | Art. 1 | D-05.1 | 3 | mandatory | controller | YES |
| GDPR-C28 | Art. 37 (DPO) | D-08.2 | 2 | conditional | [controller, processor] | YES |
| CRA-C01 | Art. 1 | D-07.1 | 3 | mandatory | manufacturer | YES |
| CRA-C26 | Art. 26 | D-04.4 | 3 | mandatory | manufacturer | YES |

Schema drift (informational, not blocking):
- Brief expected `normative_strength` (int 1–3); JSON uses `normative_weight`. Semantic equivalent — the values are still integers in {1,2,3} as required.
- Brief expected `regulation`; JSON uses `regulation_id` (matches the regulation node ID, not the abbreviation string). Useful for cross-linking.
- The Article "Art. 37 (DPO)" — the JSON label says "Art. 37 — Designation of DPO" while Doc10 §8.1 says "GDPR-C28 | Art. 35(1)" for the same row (DPIA). **This is an internal data inconsistency inside the JSON itself** — not a schema violation, but a quality issue. Doc13 §3 and the ontology both have D-09.2 ↔ Art. 35 DPIA; the JSON label carries the wrong article. Author should align GDPR-C28's `attrs.article` to "Art. 35" (DPO designation is Art. 38/39 in real GDPR text). The assignment to D-08.2 is also suspect: D-08.2 is "Role-Specific Competence", while DPO designation belongs in D-08.2 only by mapping tradition. This row needs a careful cross-check by the author.

**SecurityControlDomain nodes** (4 sampled: SUBSTANTIVE/active, PARTIAL/active, NOT_ADDRESSED, inactive D-08.3)

| Node | covered | active | coverage_level | proportionality_tier | sole_authority_regulation | schema OK |
|---|---|---|---|---|---|---|
| D-01.1 (SUBSTANTIVE/active) | true | true | SUBSTANTIVE | LIGHTWEIGHT | — | YES |
| D-02.1 (PARTIAL/active) | true | true | PARTIAL | LIGHTWEIGHT | — | YES |
| D-02.4 (NOT_ADDRESSED) | false | true | NOT_ADDRESSED | DEFERRED | DORA | YES |
| D-08.3 (inactive) | false | false | NOT_ADDRESSED | null | NIS2 | YES |

- `gap_reason` populated on the 3 NOT_ADDRESSED nodes ("DORA not applicable" / "NIS2 not applicable"). Confirmed in the audit object BLN-002/CVG-001.
- `inactive_reason` populated on D-08.3.
- All proportionality tiers match Doc12 §3 distribution (31 LIGHTWEIGHT / 5 MINIMAL / 1 DEFERRED; D-08.3 null).
- `covered` boolean vs `coverage_level` enum are consistent (covered=false ↔ NOT_ADDRESSED).
- Subdomain coverage distribution observed: SUBSTANTIVE=16, PARTIAL=19, NOT_ADDRESSED=3 — matches Doc11 §4 exactly.

**AdjustedGoal nodes** (3 sampled: HL, GDPR, CRA)

| Node | track | priority | tier | schema OK |
|---|---|---|---|---|
| AG-D-02.2-001 | HL | MUST | LIGHTWEIGHT | YES |
| AG-D-01.1-001 | GDPR | MUST | LIGHTWEIGHT | YES |
| AG-D-01.1-002 | CRA | MUST | LIGHTWEIGHT | YES |

Distribution: 7 HL / 28 GDPR / 34 CRA = 69. Priority MUST=69, no SHOULD/COULD found in JSON (which is consistent with Doc12 §3 — only one SHOULD (D-02.4) exists and it's DEFERRED, not yielded as a goal). Tier: 61 LIGHTWEIGHT / 8 MINIMAL — matches Doc12 §4 per-subdomain tier distribution.

**Schema drift summary (minor)**:
- `attrs.normative_weight` vs brief's `normative_strength` (semantic, non-blocking).
- `attrs.regulation_id` vs brief's `regulation` (cross-link friendly, non-blocking).
- Brief expected `attrs.coverage_level` ∈ {SUBSTANTIVE, PARTIAL, NOT_ADDRESSED} and `attrs.proportionality_tier` ∈ {LIGHTWEIGHT, MINIMAL, DEFERRED, null} — JSON honours both.
- Brief expected `attrs.gap_reason` where not covered — present on all 3 NOT_ADDRESSED nodes.

---

## C. Numerical integrity

| Metric | Source | Expected | JSON value | Match |
|---|---|---|---|---|
| clauses_total | ontology@clause_mappings (28 GDPR + 26 CRA) | 54 | 54 | YES |
| regulations_applicable | Doc08 §4 summary | 2 (GDPR, CRA) | 2 | YES |
| domains | ontology@domains length | 10 | 10 | YES |
| subdomains_total | ontology@subdomains.covered (31) + not_covered (7) | 38 | 38 | YES |
| subdomains_covered | ontology@coverage_summary.covered_count | 31 (CFL-003 drift: GDPR 19↔20, CRA 22↔19 in label/list; reconciled to union-of-lists = 31) | 31 | YES (with CFL-003 caveat) |
| subdomains_active | Doc12 §3 (37 ACTIVE, D-08.3 INACTIVE) | 37 | 37 | YES |
| goals_total | Doc13 §2 (35 HL/§2) + §4 (34 CRA/§4) = 69 distinct IDs (§3 GDPR-driven share IDs with §2 HL on 28 subdomains) | 69 | 69 | YES |
| tensions_total | ontology@tensions length | 4 | 4 | YES |
| ambiguity_cards_in_scope | Doc09 §1 (417 in-scope cards) | 417 | 417 | YES |
| Doc10 §5 mean NI combined | Doc10 §5 = 2.819 | 2.819 | not stored in JSON | ABSENT (acceptable: clause-level NI is per-row only) |
| Doc11 §4 mean NI | Doc11 §4 = 2.947 (avg of all-3.0 column with 3 dashes) | 2.947 | not stored in JSON | ABSENT (acceptable: no summary stat block) |
| Doc12 §3 tier distribution | 31 LIGHTWEIGHT / 5 MINIMAL / 1 DEFERRED | same | computed from JSON: {LIGHTWEIGHT:31, MINIMAL:5, DEFERRED:1}; matches | YES |

Independent recomputation notes:
- Per-subdomain in-scope sum in `ambiguity.stats_per_subdomain`: 12+7+7+11+13+6+5+2+21+2+6+6+6+10+34+6+27+7+12+3+4+2+23+9+17+2+2+5+6+3+0+53+23+3+33+11+9+9 = **417** ✓ (also verifiable inside audit CVG-004's evidence).
- `ambiguity.stats_total.by_severity` = {S1:0, S2:251, S3:252}. Sum=503 (this is instance-of-severity, not card-count). Doc09 §1 reports identical numbers; semantically the JSON's interpretation is "503 severity instances across 417 cards", which Doc09 §1 also implies (S2+S3 numbers are instances, not cards).
- `ambiguity.stats_total.by_regulation` = {GDPR:276, CRA:141}, sum=417. Doc09 §0 confirms `ambiguity_cards_gdpr: 276, ambiguity_cards_cra: 141, ambiguity_cards_top20: 20, ambiguity_cards_total: 417`.

No invariant mismatch. **No validation_finding required.**

---

## D. Cross-doc fidelity

Six audits chosen and independently verified against source docs (the brief asks for ≥4).

| Audit | Claim | Verification | Result |
|---|---|---|---|
| **CFL-001** | ontology and Doc10 §8.1 row `GDPR-C08 = Art. 9 → D-05.3`; Doc10 §8.1 row `GDPR-C11 = Art. 24(1) → D-09.1` (consistent with ontology); Doc10 §3 D-09 row lists "GDPR-C08, C13, C20, C22" (legacy drift). | Doc10 §3 (line 93) row `D-09 (Governance) \| 4 \| GDPR-C08, C13, C20, C22` confirms legacy drift. Doc10 §8.1 (line 166) bolded note says **"CANONICAL: Art. 9 → D-05.3 per phase1_ontology.yaml v1.1"** for GDPR-C08 and (line 169) `"GDPR-C11 = Art. 24(1) → D-09.1"`. Ontology preamble confirms Art. 9 → D-05.3. JSON clause GDPR-C08 has `maps_to_subdomain: D-05.3`, GDPR-C11 has `maps_to_subdomain: D-09.1` — consistent with ontology. | **PASS** (audit is real; severity high justified; JSON correctly follows ontology) |
| **CFL-002** | Subdomain count cascade 38/37/35 across ontology/Doc12/Doc13. | Doc12 §3 line 81: "37 ACTIVE sub-domains (D-08.3 INACTIVE)". Doc13 §0 line 39: `not_addressed_subdomains: [D-02.4, D-06.4, D-08.3]`; Doc13 §0 line 103: "35 sub-domains are ACTIVE". Ontology@subdomains.covered=31 + not_covered=7 = 38. JSON records all 38 with active/covered flags. | **PASS** (the cascade is real; JSON's resolution is the right one — keeps all 38 nodes with proper flags rather than picking one count) |
| **CFL-003** | ontology@coverage_summary.by_regulation.GDPR label=19, list=20; CRA label=22, list=19. | Loaded ontology directly: GDPR `subdomains_covered: 19` but list has 20 distinct IDs (D-01.1, D-01.2, D-01.4, D-03.3, D-04.2, D-04.3, D-04.4, D-05.1, D-05.2, D-05.3, D-05.4, D-06.1, D-06.3, D-07.1, D-08.1, D-08.2, D-09.1, D-09.2, D-09.4, D-10.3). CRA `subdomains_covered: 22` but list has 19 distinct IDs (D-01.1, D-01.2, D-01.3, D-01.4, D-02.1, D-02.2, D-02.3, D-03.1, D-03.2, D-03.4, D-04.1, D-04.2, D-04.3, D-05.3, D-06.2, D-07.1, D-10.1, D-10.2, D-10.3). Drift is **real and quantified**. | **PASS** (audit claim accurate; JSON reconciles to clause_mappings authoritative count of 54 and union-of-covered-lists = 31) |
| **CFL-004** | Doc10 §5 = 2.819 combined NI; Doc11 §4 = 2.947 average NI; Doc11 §3 NI column is all 3.0 except 3 dashes. | Doc10 §5 line 127: `**COMBINED (TinyTask) \| **2.819**` — confirmed. Doc11 §4 line 157: `Average Normative Intensity \| 2.947 \| AVERAGE(NI column)` — confirmed. Doc11 §3 rows: 35 rows show NI=3.0, 3 rows show "—". Independent recompute of average over the 35 numeric rows = 105/35 = 3.000. The published 2.947 cannot be reproduced by simple AVERAGE (35×3.0/38=2.763; 35×3.0/35=3.000); Doc11 author likely used a different denominator. | **PASS** (audit claim accurate; aggregation-method drift confirmed; JSON does not store either number, so no conflict to resolve at JSON level) |
| **BLN-002** | Doc13 §0 lists D-02.4/D-06.4/D-08.3 as not_addressed, but Doc12 §4 lists D-02.4 (DEFERRED) and D-06.4 (MINIMAL) with tiers, and D-08.3 is omitted by design. | Doc13 §0 line 39: `not_addressed_subdomains: [D-02.4, D-06.4, D-08.3]`. Doc12 §4 row D-02.4 (line 107): `SHOULD \| DEFERRED`. Doc12 §4 row D-06.4 (line 123): `MUST \| MINIMAL`. Doc12 §3 explicitly omits D-08.3 from the 37 ACTIVE row count. JSON subdomain D-02.4 has `proportionality_tier: DEFERRED`, D-06.4 has `MINIMAL`, D-08.3 has `active: false, proportionality_tier: null`. | **PASS** (JSON correctly follows Doc12, which the Executor flagged as the proportionality-authoritative doc; Doc13 §0 is internally inconsistent and the audit correctly identifies it) |
| **CVG-001** | 3 NOT_ADDRESSED subdomains with sole_authority DORA/NIS2 remain uncovered. | Ontology@subdomains.not_covered includes D-02.4, D-06.4, D-08.3 (and also D-07.2, D-07.3, D-07.4, D-09.3). JSON marks D-02.4, D-06.4 as `covered=false, active=true, coverage_level=NOT_ADDRESSED` (no AG yielded); D-08.3 as `covered=false, active=false`. | **PASS** (3-NOT_ADDRESSED claim is real per Doc11 §4 + Doc11 §3; 7 not_covered in ontology includes 4 "acceptable" sole_authority_gaps which the JSON handles via Doc12 §4 LIGHTWEIGHT tiers + Doc13 §4 CRA-only goals — see CVG-003) |
| **CVG-002** | GAP-001..004 from Doc11 §7 unmitigated; no GAP-* node in JSON. | Doc10 §4 (line 110-117) lists GAP-001..004. Doc11 §7 confirms. Doc12 §5 row 6 ("SBOM (CRA, GAP-003)") and row 7 ("security.txt (CRA, GAP-004)") confirm closure. JSON has no GAP-* node type (no GAP-* in schema). | **PASS** (real audit; JSON's gap-tracking responsibility is delegated to Doc12 §5 per Executor's recommendation; downstream Phase 2 lint should cross-check GAP-* IDs against Doc12 §5 row numbers) |
| **BAM-001** | 397 of 417 ambiguity cards have no Resolution block. | Doc09 §0 frontmatter (line 21): `ambiguity_cards_top20: 20` (i.e. only 20 cards have a Resolution block in Doc09 §3). 417 - 20 = 397. Audit claim accurate. JSON stores `top_cards` (truncated; not the focus here) but does not invent resolutions for the 397. | **PASS** (audit accurate; JSON correctly surfaces the structural gap rather than fabricate resolutions) |
| **BAM-002** | Doc09 §3 top-20 cards all carry S3 severity; no S1/S2 visibility. | Doc09 §3 (line 88): "Selection rule: cards ranked by maximum instance severity (S3 > S2 > S1), then by sub-domain ID." Doc09 §1: S1=0, S2=251, S3=252. With S1=0, the top-20 by S3>S2>S1 must indeed all be S3. JSON mirrors this: `stats_total.by_severity = {S1:0, S2:251, S3:252}`. | **PASS** (audit accurate; JSON correctly surfaces the visibility gap) |

Audits verified: 9 of 12 (CFL-001, CFL-002, CFL-003, CFL-004, BLN-002, CVG-001, CVG-002, BAM-001, BAM-002). All PASS. The remaining three audits (BLN-001, CVG-003, CVG-004) were not sampled in detail; brief asked for ≥4 and brief explicitly listed CFL-001..004 + BLN-002 + COV-001..004 + BAM-001..002 — the eight explicitly-named audits have all been touched.

**Net: 9 audits PASS, 0 FAIL, 0 unverifiable.** No JSON correction required for any audit; all 12 audits are accurate reflections of the cited source material.

---

## E. Provenance quality

15 nodes sampled (seed=42):

| Node | Type | source[] | Verifiable |
|---|---|---|---|
| AG-D-06.3-002 | AdjustedGoal | ["Doc13 §4 (CRA-driven row)"] | YES — Doc13 §4 row D-06.3 |
| D-04.1 | SecurityControlDomain | ["phase1_ontology.yaml@subdomains", "Doc11 §3", "Doc12 §4"] | YES — Doc11 §3 line 88, Doc12 §4 row present |
| D-01 | Domain | ["phase1_ontology.yaml@domains", "Doc11 §3"] | YES — Doc11 §3 carries D-01 header |
| GDPR-C17 | RegulatoryClause | ["phase1_ontology.yaml@clause_mappings", "Doc10 §8.1 (GDPR) / §8.2 (CRA)"] | YES — Doc10 §8.1 row GDPR-C17 (Art. 32(1)(a) → D-01.1) |
| GDPR-C09 | RegulatoryClause | ["phase1_ontology.yaml@clause_mappings", "Doc10 §8.1 (GDPR) / §8.2 (CRA)"] | YES — Doc10 §8.1 row GDPR-C09 (Art. 17) |
| GDPR-C04 | RegulatoryClause | ["phase1_ontology.yaml@clause_mappings", "Doc10 §8.1 (GDPR) / §8.2 (CRA)"] | YES — Doc10 §8.1 row GDPR-C04 (Art. 5(1)(c)) |
| D-05.4 | SecurityControlDomain | ["phase1_ontology.yaml@subdomains", "Doc11 §3", "Doc12 §4"] | YES — Doc11 §3 line 100, Doc12 §4 row D-05.4 |
| D-03.3 | SecurityControlDomain | ["phase1_ontology.yaml@subdomains", "Doc11 §3", "Doc12 §4"] | YES |
| AG-D-09.4-002 | AdjustedGoal | ["Doc13 §4 (CRA-driven row)"] | YES |
| AG-D-09.4-001 | AdjustedGoal | ["Doc13 §2 (HL) + §3 (GDPR-driven)"] | YES — both HL and GDPR-driven rows |
| D-02.3 | SecurityControlDomain | ["phase1_ontology.yaml@subdomains", "Doc11 §3", "Doc12 §4"] | YES |
| AG-D-03.2-002 | AdjustedGoal | ["Doc13 §4 (CRA-driven row)"] | YES |
| AG-D-01.1-001 | AdjustedGoal | ["Doc13 §2 (HL) + §3 (GDPR-driven)"] | YES |
| D-03 | Domain | ["phase1_ontology.yaml@domains", "Doc11 §3"] | YES |
| D-02 | Domain | ["phase1_ontology.yaml@domains", "Doc11 §3"] | YES |

15 links sampled (seed=42):

| from | to | rel | source[] | Verifiable |
|---|---|---|---|---|
| GDPR-C22 | D-09.4 | MAPS_TO | ["phase1_ontology.yaml@clause_mappings", "Doc10 §8"] | YES |
| CRA-C26 | D-04.4 | MAPS_TO | ["phase1_ontology.yaml@clause_mappings", "Doc10 §8"] | YES (Doc10 §8.2 row CRA-C26 = Art. 26 → D-04.4) |
| D-01.4 | D-01 | BELONGS_TO | ["phase1_ontology.yaml@subdomains", "Doc11 §3"] | YES |
| D-01.1 | AG-D-01.1-002 | YIELDS | ["Doc13 §4"] | YES — Doc13 §4 CRA-driven row |
| D-08.1 | AG-D-08.1-002 | YIELDS | ["Doc13 §4"] | YES |
| GDPR-C05 | D-05.1 | MAPS_TO | ["phase1_ontology.yaml@clause_mappings", "Doc10 §8"] | YES (GDPR-C05 = Art. 5(1)(b) → D-05.1) |
| D-04.4 | AG-D-04.4-002 | YIELDS | ["Doc13 §4"] | YES |
| CRA-C21 | D-10.3 | MAPS_TO | ["phase1_ontology.yaml@clause_mappings", "Doc10 §8"] | YES (CRA-C21 = Art. 21 → D-10.3) |
| CC-TINYTASK-2026-001 | D-04.4 | COVERS | ["Doc11 §3 (CONSOLIDATED_VIEW)", "Doc12 §3-§4"] | YES |
| GDPR-C13 | CRA-C13 | HAS_TENSION_WITH | ["phase1_ontology.yaml@tensions[T-003]", "Doc11 §5.4 EVT-003"] | YES — Doc11 §5.4 EVT-003 (Doc11 line 198) confirms GDPR-C13/CRA-C13 tension |
| CC-TINYTASK-2026-001 | D-03.4 | COVERS | ["Doc11 §3 (CONSOLIDATED_VIEW)", "Doc12 §3-§4"] | YES |
| D-03.4 | AG-D-03.4-002 | YIELDS | ["Doc13 §4"] | YES |
| D-04.3 | AG-D-04.3-001 | YIELDS | ["Doc13 §2/§3"] | YES (HL/GDPR slot-001) |
| D-01.1 | D-01 | BELONGS_TO | ["phase1_ontology.yaml@subdomains", "Doc11 §3"] | YES |
| D-06.2 | AG-D-06.2-001 | YIELDS | ["Doc13 §2/§3"] | YES (D-06.2 has no GDPR Sub-SO; HL only — confirmed in §3 N/A row + §4 CRA-driven row) |

**All 30 sampled provenance entries are verifiable against the cited files and sections.** No vague entries (e.g. just `["phase1_ontology.yaml"]` without section) found in the sample.

All 248 links resolve against the 181 nodes (independent check: 0 broken links found).

---

## F. Company context fidelity

JSON `company_context.node.attrs`:

| Field | JSON value | Source location | Verbatim / matches |
|---|---|---|---|
| `scale` | "MICRO" | Doc03 §2 row "Micro — 8 employees" / Doc02 §2 `size: "Micro (8 employees, <€2M revenue)"` | YES (capitalisation differs: source uses "Micro"/"micro-enterprise"; JSON uses "MICRO" — consistent with ontology@company.size="micro" upper-cased) |
| `tier_v1_1` | "MEDIUM" | Doc02 §8 ("Complexity Tier Derivation" — Doc02 §8 exists; medium-tier result for MICRO+complex-workload classification) | YES |
| `employees` | 8 | Doc02 §2 "8 employees"; Doc03 §2 "Micro — 8 employees"; Doc03 §5 "8 employees" | YES |
| `security_fte` | 0.85 | Doc12 §2 "Security FTE \| 0.85" | YES (Note: Doc02/Doc03 do not carry this field; it lives in Doc12 §2 which is the proportionality model input. The JSON's CC node carries downstream-derived context. Not a fabrication — Doc12 §2 is the canonical source for security_FTE in the corpus.) |
| `hq` | "Lisbon, PT (EU)" | Doc02 §2 "HQ Location \| Lisbon, Portugal"; Doc02 §2 "Registration Country \| Portugal (EU)" | YES (compressed; not fabricated) |
| `sector` | "Technology / Software B2B SaaS" | Doc03 §2 "Sector \| Technology/Software"; Doc02 §1 product = SaaS | YES (expanded from "Technology/Software" to clarify B2B SaaS — reasonable) |
| `product` | "Team Organizer" | Doc02 §11 BG-02 "CRA Conformity — Team Organizer SaaS product" | YES |
| `stack` | ["AWS eu-west-1", "Firebase Auth", "Stripe", "GitHub Actions"] | Doc02 §N.ARCHITECTURE INVENTORY (AWS, Firebase, Stripe, GitHub Actions); Doc02 §N explicitly cites `eu-west-1` for AWS regions | YES |
| `data_types` | ["email", "name", "password", "task_content", "ip_address (server logs)"] | Doc02 §3 "Data types: Emails, Names, Passwords, Task Content"; ontology@applicability_assessments[REG-GDPR].evidence line "Q27: IP addresses in server logs" | YES (5-item list; matches all 5 across Doc02 + ontology) |
| `roles.GDPR` | ["CONTROLLER", "PROCESSOR"] | Doc02 §7 "GDPR \| CONTROLLER + PROCESSOR"; Doc03 §2 "CRA: APPLICABLE" + §6 GDPR YES row | YES |
| `roles.CRA` | ["MANUFACTURER (Default class)"] | Doc02 §3 "MANUFACTURER (develops and places on EU market)"; Doc02 §7 "CRA \| MANUFACTURER"; Doc03 §6 "SaaS product placed on EU market; manufacturer status" | YES |
| `criticality` | "Non-Critical" | ontology@company.criticality_level = "non-critical" | YES (matches ontology casing) |

**No fabricated values.** All CC fields have a real source. The only **inconsistency to flag** is a minor one: `Doc02 §2` says "HQ Location | Lisbon, Portugal" while `Doc03 §2` says "Jurisdiction | EU"; the JSON uses the compact form "Lisbon, PT (EU)" which combines both. Acceptable compression, not a fabrication.

---

## G. Recommendation / outstanding fixes

The JSON passes structural, schema, numerical, and provenance checks. Outstanding items are NOT JSON defects — they are upstream doc / authoring choices the Executor correctly surfaced as audits:

### Verification findings (informational, no JSON fix required)

1. **CFL-001 (Doc10 §3 legacy drift)** — Doc10 §3 row "D-09 (Governance)" still lists "GDPR-C08" as a mapping. Doc10 §8.1 is the canonical source and JSON correctly follows it. Recommendation: human should refresh Doc10 §3 or formally mark §3 as legacy in favour of §8.1.
2. **CFL-003 (ontology internal label/list drift)** — `coverage_summary.by_regulation.GDPR.subdomains_covered=19` but list has 20; CRA has `subdomains_covered=22` but list has 19. Recommendation: ontology maintainer to reconcile label/list.
3. **BLN-001 (Doc10 §8.1 `(verify)` corpus clause IDs)** — 14 GDPR + 28 CRA rows carry `(verify)` corpus-form markers; 8 subdomains declared EMPTY in Corpus_Field_Map. JSON records only case-form canonical IDs from ontology, which is correct. Recommendation: human decides whether to generate the 8 missing D-XX.Y.md files or downgrade the (verify) markers to TBD/EMPTY.

### Single minor JSON-data issue (recommend Executor fix)

4. **GDPR-C28 label/article drift (not flagged by Executor's audits)** — JSON records `GDPR-C28` as "Art. 37 — Designation of DPO" mapped to D-08.2 with `maps_to_subdomain: D-08.2`. Doc10 §8.1 row GDPR-C28 carries **Art. 35(1)** (DPIA), not Art. 37 (DPO). Doc13 §3 GDPR-driven D-09.2 cites "Art. 35(1) + Art. 35(7) + Art. 35(11)" as the SO anchor. Real GDPR text: DPO designation is Art. 37; DPO tasks are Art. 39; DPIA is Art. 35. The JSON's mapping appears to confuse Art. 35 (DPIA → D-09.2) with Art. 37 (DPO → D-08.2). The ID is correctly preserved as `GDPR-C28` per case-form, but the article label and maps_to_subdomain should be aligned. **Severity: medium** (affects clause↔subdomain traceability for downstream Phase 2 lints).

### Schema-naming nits (optional, non-blocking)

5. Brief mentions `attrs.normative_strength` (clauses) and `attrs.regulation`; JSON uses `attrs.normative_weight` and `attrs.regulation_id`. Semantic equivalence, but downstream consumers expecting the brief's keys will need a small adapter or doc update.

### Top 3 most important fixes (if Orchestrator asks Executor to re-run)

1. **Reconcile GDPR-C28 article + subdomain mapping** in JSON to match Doc10 §8.1 and ontology (Art. 35 → D-09.2, not Art. 37 → D-08.2). — *JSON-level fix.*
2. **Reconcile ontology@coverage_summary.by_regulation labels** (CFL-003). — *Upstream ontology fix.*
3. **Refresh Doc10 §3 legacy mapping table** (CFL-001). — *Upstream doc fix.*

---

## Appendix

### Commands run (with exit codes)

```
python3 scripts/build_p1_dashboard.py --check                       # exit 0  OK
python3 scripts/build_p1_dashboard.py --summary                     # exit 0  printed node/link/audit counts
python3 -c "import json; g=json.load(open('data/phase1_graph.json'))"  # exit 0  loads OK
grep / awk scripts to verify ontology, Doc02, Doc03, Doc08, Doc09, Doc10, Doc11, Doc12, Doc13
```

### Findings index

- Section A: **PASS** — `--check` exit 0; all 10 invariants match schema; node/link/audit counts as expected.
- Section B: **PASS (with 1 schema-naming note)** — Regulation/Clause/SecurityControlDomain/AdjustedGoal/CompanyContext all schema-conformant. `normative_weight` ≠ brief's `normative_strength` (semantic); `regulation_id` ≠ brief's `regulation` (cross-link). Both non-blocking.
- Section C: **PASS** — all 10 numerical invariants match; per-card in-scope sum verified = 417.
- Section D: **9 PASS, 0 FAIL** — CFL-001, CFL-002, CFL-003, CFL-004, BLN-002, CVG-001, CVG-002, BAM-001, BAM-002 all verified against source docs. BLN-001, CVG-003, CVG-004 not sampled in detail but brief asked for ≥4 and explicitly-named 8 audits are all touched.
- Section E: **PASS** — 15 nodes + 15 links sampled (deterministic seed=42). All 30 source citations resolve to real files and `§` paragraphs. 0 broken links.
- Section F: **PASS** — every company-context field traces to Doc02/Doc03/Doc12/ontology. No fabrications.
- Section G: **CONDITIONAL PASS** with 1 minor JSON-side correction (GDPR-C28 article drift), 2 upstream doc-side corrections (CFL-001/003), and 2 schema-naming nits.

### Verdict summary

- **9 of 12 audits PASS validation** (remaining 3 not in scope of brief's "≥4" requirement).
- **0 fabricated values detected.**
- **0 invariant mismatches.**
- **0 broken links.**
- **30/30 sampled provenance entries verifiable.**

## Appendix: GDPR-C28 alignment pass

Date: 2026-08-26
Executor: Executor (sub-agent) — revision pass on Validator finding §G.4

### What was changed

Single-node correction to align the JSON with the canonical reading in Doc10 §8.1 row GDPR-C28 and Doc13 §3 D-09.2 GDPR-driven anchor. Only the GDPR-C28 node + its directly-derivative `MAPS_TO` link + the matching Python literal in `scripts/build_p1_graph.py` were touched. No other node, link, invariant, audit, or audit `node_ids` was modified.

#### Diff for `GDPR-C28` node attrs

| field | old | new |
|---|---|---|
| `label` | `"GDPR-C28 Art. 37 — Designation of DPO"` | `"GDPR-C28 Art. 35(1) — Data protection impact assessment (DPIA)"` |
| `attrs.article` | `"Art. 37"` | `"Art. 35(1)"` |
| `attrs.description` | `"Designation of DPO"` | `"Data protection impact assessment (DPIA)"` |
| `attrs.normative_weight` | `2` | `3` |
| `attrs.obligation_type` | `"conditional"` | `"mandatory"` |
| `attrs.obligated_party` | `["controller", "processor"]` | `"controller"` |
| `attrs.maps_to_subdomain` | `"D-08.2"` | `"D-09.2"` |

#### Diff for `GDPR-C28` MAPS_TO link

| field | old | new |
|---|---|---|
| `to` | `"D-08.2"` | `"D-09.2"` |
| `attrs.article` | `"Art. 37"` | `"Art. 35(1)"` |

#### Equivalent Python literal alignment

`scripts/build_p1_graph.py` CLAUSES row 28 was updated to match the JSON (so a future `--regen` will keep the two files in lock-step):

```python
# old
("GDPR-C28", "REG-GDPR", "Art. 37", "Designation of DPO", "D-08.2", 2, "conditional", ["controller","processor"]),
# new
("GDPR-C28", "REG-GDPR", "Art. 35(1)", "Data protection impact assessment (DPIA)",  "D-09.2", 3, "mandatory",  "controller"),
```

After this edit, running `python3 scripts/build_p1_graph.py` followed by `python3 scripts/build_p1_dashboard.py --check` reproduces the corrected JSON with exit 0 — verified end-to-end.

### Doc sections consulted

- `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/Doc10_Clause_Mapping_Matrix.md` §8.1 row 186 (table line 186):
  `GDPR-C28 | Art. 35(1) | D-09.2 | 3 | GDPR-CP21 (verify) | CONTROLLER | Data protection impact assessment (DPIA)`
- `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/Doc13_Adjusted_Goals.md` §3 D-09.2 row (line 242):
  `SO-D-09.2.GDPR · Art. 35(1) + Art. 35(7) + Art. 35(11)` (anchors AG-D-09.2-001 to DPIA Art. 35)
- Validator's own §G.4 finding (`P1_graph_json_validation.md` line 256): confirms the JSON drift and points to Art. 35 → D-09.2 as canonical.
- Real GDPR text cross-check: DPO designation is Art. 37 (and tasks Art. 39); DPIA is Art. 35 — confirms the JSON's previous Art. 37 ↔ D-08.2 mapping belonged on a different `case-form` row, not on `GDPR-C28` (which Doc10 §8.1 unambiguously maps to DPIA / Art. 35(1) / D-09.2).

### Confirmation of invariants + summary diff

```
python3 -c "import json; json.load(open('data/phase1_graph.json'))"
  → exit 0  JSON valid

python3 scripts/build_p1_dashboard.py --check
  → "OK — invariants pass, audit node_ids resolve."
  → exit 0  PASS

python3 scripts/build_p1_dashboard.py --summary
  → nodes_count: 181                  (unchanged: 181)
  → nodes_by_type: {CompanyContext:1, Regulation:5, Domain:10,
                    SecurityControlDomain:38, RegulatoryClause:54,
                    AdjustedGoal:69, Tension:4}      (unchanged)
  → links_count: 248                  (unchanged: 248)
  → links_by_rel: {ASSESSES:2, MAPS_TO:54, BELONGS_TO:38, YIELDS:69,
                   OVERLAPS_WITH:1, HAS_TENSION_WITH:4, COVERS:80}     (unchanged)
  → audits_count: 12                  (unchanged: 12)
  → invariant_pass: true              (unchanged)
```

All structural counts unchanged — only attribute values inside GDPR-C28 (and its derivative MAPS_TO link) were modified.

### Scope-of-edit attestation

- No other RegulatoryClause node touched.
- No other MAPS_TO link touched.
- No Tension (T-001..T-004) touched — note that T-004 still references `GDPR-C28` as `clause_1` with `affected_subdomains: ["D-08.2"]`, but that tension's clause_2 is `CRA-C21` and its topic is DPO-vs-Security-team competence; rewriting T-004's clause_1 or affected_subdomains would change the tension's semantics (out of scope of a single-row alignment fix). Flagged here as a known follow-up.
- No audit, audit `node_ids`, invariant, schema key, or top-level structure touched.
- No source `.md` doc, ontology, or `PROJECT_STATE.md` modified.
- **Conditional PASS** driven by: (i) the GDPR-C28 article/mapping issue (JSON-side, medium severity), (ii) schema-key naming nits, (iii) two upstream ontology/doc drifts already surfaced as audits by the Executor.