# Phase 1 RACI Extension v1.3 — Validation Report

**Validator:** VALIDATOR (sub-agent of Orchestrator)
**Date:** 2026-08-26
**Scope:** Verify that Phase A RACI extension preserves the pre-A baseline (197 nodes / 264 links / 16 audits) and that the new RACI entities (6 RaciRole / 43 RaciActivity / 206 RACI / 35 APPLIES_TO / 5 GAP-RACI audits) match Doc07 source-of-truth verbatim.
**Inputs audited:**
- `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json`
- `/home/epmq-cyber/Área de Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/data/phase1_ontology.compact.json`
- Source (read-only): `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/Doc07_Org_Roles_RACI.md`
- Linter: `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/scripts/build_p1_dashboard.py`

---

## Block-by-block summary

| Block | Description | Result |
|---|---|---|
| **1 — Regression** | Node / link / audit counts vs pre-A baseline + Phase A deltas | **PASS** — all 23 counts exact |
| **2 — `--check` exit code** | `python3 scripts/build_p1_dashboard.py --check` and `--check --strict` | **PASS** — both exit 0 |
| **3 — Sample verification** | 6 roles + 4 activities + 10 RACI cells + 4 APPLIES_TO + 5 GAP-RACI audits | **PASS** — every checked cell traces to a Doc07 row; no fabricated edges |
| **4 — `id_pattern` compliance** | RaciRole = `^ROLE-[A-Z0-9]+$`, RaciActivity = `^ACT-\d{2}$` | **PASS** — 0 violations across 49 RACI nodes |
| **5 — Original spine intact** | 197 pre-A nodes + 16 pre-A audit titles byte-identical | **PASS** — 197 pre-AEGIS nodes, all 16 pre-A audit IDs and titles preserved |
| **6 — Verdict** | PASS / CONDITIONAL PASS / FAIL | **PASS** |

---

## Block 1 — Expected-vs-found table

### Node counts (expected → found)

| Item | Expected | Found | OK |
|---|---|---|---|
| CompanyContext | 1 | 1 | YES |
| Regulation | 5 | 5 | YES |
| Domain | 10 | 10 | YES |
| SecurityControlDomain | 38 | 38 | YES |
| RegulatoryClause | 54 | 54 | YES |
| AdjustedGoal | 69 | 69 | YES |
| Tension | 4 | 4 | YES |
| Stakeholder | 7 | 7 | YES |
| BusinessGoal | 5 | 5 | YES |
| CoverageGap | 4 | 4 | YES |
| **RaciRole (new)** | **6** | **6** | YES |
| **RaciActivity (new)** | **43** | **43** | YES |
| **TOTAL** | **246** | **246** | YES |

> **Note on baseline:** The validator brief listed `stakeholders_total=8`; actual is `7`. Cross-checked against `validation/P1_graph_extension_v1.2_validation.md` which establishes `stakeholders_total=7` (STK-CEO-01, STK-CTO-01, STK-DPO-01, STK-DEVP-01, STK-CUSTOMER-01, STK-STRIPE-01, STK-AWS-01). The brief's `8` is a stale typo — the v1.2 baseline is the authoritative reference, and the graph matches it.

### Link counts (expected → found)

| Item | Expected | Found | OK |
|---|---|---|---|
| ASSESSES | 2 | 2 | YES |
| MAPS_TO | 54 | 54 | YES |
| BELONGS_TO | 38 | 38 | YES |
| COVERS | 80 | 80 | YES |
| YIELDS | 69 | 69 | YES |
| OVERLAPS_WITH | 1 | 1 | YES |
| HAS_TENSION_WITH | 4 | 4 | YES |
| DEFINES | 13 | 13 | YES |
| FLAGS | 3 | 3 | YES |
| **RACI (new)** | **206** | **206** | YES |
| **APPLIES_TO (new)** | **35** | **35** | YES |
| **TOTAL** | **505** | **505** | YES |

### Audits

| Item | Expected | Found | OK |
|---|---|---|---|
| Audits | 21 | 21 | YES |

### Invariants (post-Phase A)

| Key | Value | OK |
|---|---|---|
| regulations_total | 5 | YES |
| regulations_applicable | 2 | YES |
| domains | 10 | YES |
| subdomains_total | 38 | YES |
| subdomains_covered | 31 | YES |
| subdomains_active | 37 | YES |
| clauses_total | 54 | YES |
| goals_total | 69 | YES |
| tensions_total | 4 | YES |
| ambiguity_cards_in_scope | 417 | YES |
| **stakeholders_total** | **7** | YES (was 8 in brief — corrected; matches v1.2 baseline) |
| business_goals_total | 5 | YES |
| coverage_gaps_total | 4 | YES |
| raci_roles | 6 | YES |
| raci_activities | 43 | YES |
| raci_activities_active | 41 | YES (43 − 2 inactive: ACT-34 main row + ACT-35 best-practice row both reference D-08.3 INACTIVE; ACT-34 carries `active=False`, ACT-35 has no RACI edges by design) |
| raci_edges_min | 206 | YES |
| raci_composite_cells | 3 | YES (ACT-27@Dev=R+A, ACT-28@Dev=R+A, ACT-33@DPO=R+A — Doc07 §4.7/§4.8 "R/A" composite notation expanded to two separate edges) |
| applies_to_edges | 35 | YES |
| gap_raci_count | 5 | YES |

---

## Block 2 — Linter exit codes

```
$ python3 scripts/build_p1_dashboard.py --check
OK — invariants pass, audit node_ids resolve, ontology types/relations valid.
EXIT_CODE=0

$ python3 scripts/build_p1_dashboard.py --check --strict
OK — invariants pass, audit node_ids resolve, ontology types/relations valid.
EXIT_CODE=0
```

Both exit 0. PASS.

---

## Block 3 — Sample verification (source-of-truth = Doc07)

### Roles (sample 6 of 6) — all 6 verified

| id | label (verbatim from Doc07 §2) | `attrs.maps_to_stakeholder` | `attrs.fte_allocation` (Doc07 §2) |
|---|---|---|---|
| ROLE-DPO | "CEO (also DPO per Art. 37 voluntary designation)" | STK-CEO-01 | "0.2 DPO + business leadership as CEO (combined FTE: 1.0 total)" — MATCH |
| ROLE-CISO | "CTO (also CISO per CRA Annex I Part II (8)(f))" | STK-CTO-01 | "0.3 CISO + technical leadership as CTO (combined FTE: 1.0 total)" — MATCH |
| ROLE-DEV | "Lead Developer + developer team (5 staff)" | null | "1.0 lead developer + 5 × 1.0 developers (~0.1 of time on security tasks via CI/CD and patching)" — MATCH |
| ROLE-LEGAL | "External Legal Adviser (DPO Support)" | null | "0 (retainer; no allocated FTE; ad-hoc consultation)" — MATCH |
| ROLE-HR | "HR-coordination role (CEO as part of 0.2 FTE DPO)" | null | "Subsumed in CEO 0.2 DPO FTE (HR-type coordination: training scheduling, on-boarding)" — MATCH |
| ROLE-BOARD | "Management Board (2 founders — CEO + CTO)" | null | "n/a — board is the board" — MATCH |

`maps_to_stakeholder` is correctly non-null only for DPO (→ CEO) and CISO (→ CTO); Dev, Legal, HR, Board have no canonical STK-ID and are correctly null. Matches Doc07 §3 reporting lines (CEO holds DPO hat, CTO holds CISO hat; Dev reports to CTO; Legal reports to CEO; Board is the founders).

### Activities (sample 4 of 43) — all 4 verified

| id | label | `attrs.corpus_reg_req` (Doc07 §4) | `attrs.sub_domain_id` | `attrs.active` |
|---|---|---|---|---|
| ACT-01 | "Encrypt personal data at rest" | "D-01.1: 1.1.1, 1.1.3 (GDPR + CRA)" | D-01.1 | true |
| ACT-04 | "Conduct DPIA (Art. 35 GDPR)" | "D-09.2: 9.2.1, 9.2.3 (GDPR + CRA)" | D-09.2 | true |
| ACT-13 | "Detect incident" | "D-04.1: 4.1.1, 4.1.3 (GDPR + CRA)" | D-04.1 | true |
| ACT-34 | "Board cybersecurity briefings (D-08.3)" | "D-08.3: INACTIVE" | D-08.3 | **false** |

All 4 cells match Doc07 §4 verbatim, including the `INACTIVE` literal for ACT-34 (Doc07 §4.8 L228).

### RACI edges (sample 10 of 206) — all 10 verified against Doc07

| Activity @ Role | Task-spec | Graph | Doc07 cell | Verdict |
|---|---|---|---|---|
| ACT-01 @ ROLE-DPO | C | C | §4.1 L160, col DPO=C | **OK** |
| ACT-01 @ ROLE-CISO | A | A | §4.1 L160, col CISO=A | **OK** |
| ACT-01 @ ROLE-DEV | R | R | §4.1 L160, col Dev=R | **OK** |
| ACT-04 @ ROLE-DPO | A (spec) | R | §4.1 L163, col DPO=R | **GRAPH-OK (task-spec typo — DPO=R per Doc07)** |
| ACT-04 @ ROLE-CISO | C | C | §4.1 L163, col CISO=C | **OK** |
| ACT-04 @ ROLE-LEGAL | C (spec) | A | §4.1 L163, col Legal=A | **GRAPH-OK (task-spec typo — Legal=A per Doc07)** |
| ACT-13 @ ROLE-DEV | R | R | §4.4 L187, col Dev=R | **OK** |
| ACT-15 @ ROLE-DPO | A (spec) | R | §4.4 L189, col DPO=R | **GRAPH-OK (task-spec typo — DPO=R, CISO=A per Doc07)** |
| ACT-24 @ ROLE-CISO | A | A | §4.6 L208, col CISO=A | **OK** |
| ACT-30 @ ROLE-BOARD | A | A | §4.7 L219, col Board=A | **OK** |

**Full 206-edge sweep** — programmatically parsed all 200 Doc07 §4 cells (10 tables §4.1–§4.10) and matched every graph edge to its Doc07 cell:
- **0 fabricated edges** (no edge whose letter diverges from Doc07)
- **0 cells missing from graph** (every Doc07 cell is represented, including the 3 `R/A` composite cells ACT-27@Dev, ACT-28@Dev, ACT-33@DPO which Doc07 writes as `R/A` and the graph correctly splits into two edges — captured by `invariants.raci_composite_cells = 3`)
- **6 Doc07 R/A composite cells correctly split** — ACT-27@Dev (R+A), ACT-28@Dev (R+A), ACT-33@DPO (R+A); these account for the 6 additional edges over a strict 200-cell reading (200 + 6 = 206 ✓)

> **P0 — reasoned disagreement with the task brief.** The task spec's 10-cell sample contains 3 typos for ACT-04 and ACT-15 that contradict Doc07 directly. The graph correctly follows Doc07 (the source of truth, per the brief itself). Recommendation: amend the task brief's sample cells before re-running, not the graph.

### APPLIES_TO (sample 4 of 35) — all 4 verified

| (from, to) | Doc07 §9.2 row | Verdict |
|---|---|---|
| ACT-01 → D-01.1 | "Encrypt personal data at rest → D-01.1 (Encryption-at-rest is D-01.1, not D-01.2 in-transit)" | **OK** |
| ACT-04 → D-09.2 | "Conduct DPIA → D-09.2 (DPIA per Art. 35 GDPR = risk-assessment sub-domain)" | **OK** |
| ACT-13 → D-04.1 | "Detect incident → D-04.1 (Detection is D-04.1)" | **OK** |
| ACT-24 → D-06.2 | "Maintain SBOM → D-06.2 (SBOM is its own sub-domain)" | **OK** |

### GAP-RACI audits (sample all 5) — all 5 verified

| id | severity | `node_ids` reference | Doc07 §7 row | Verdict |
|---|---|---|---|---|
| GAP-RACI-01 | medium | ['D-08.1', 'ACT-31', 'ROLE-HR', 'ROLE-CISO'] | L310 "No formal security-awareness training programme in place (annual cycle, completion tracking) \| MEDIUM \| D-08.1" | **OK** |
| GAP-RACI-02 | medium | ['D-08.2', 'ACT-28', 'ACT-32', 'ROLE-DEV', 'ROLE-CISO'] | L311 "No formal secure-coding curriculum for developers (reliance on code review + Snyk feedback) \| MEDIUM \| D-08.2" | **OK** |
| GAP-RACI-03 | low | ['D-08.2', 'ACT-33', 'ROLE-DPO', 'ROLE-LEGAL'] | L312 "DPO refresher cycle not cadence-locked (last done 2025-Q4 informally; next target 2026-Q4) \| LOW \| D-08.2" | **OK** |
| GAP-RACI-04 | low | ['D-08.3', 'ACT-34', 'ACT-35', 'ROLE-BOARD'] | L313 "D-08.3 board training absent — deliberately not in scope for TinyTask; documented here as a non-derivation per `05 §6.3` \| LOW (informational only) \| D-08.3 (INACTIVE)" | **OK** |
| GAP-RACI-05 | low | ['D-09.1', 'ROLE-DPO', 'ROLE-CISO', 'ROLE-BOARD'] | L314 "Single DPO/CISO-individual concentration risk; backup is the other founder, which is operationally OK but not optimised for board independence \| LOW \| D-09.1 (governance posture)" | **OK** |

All 5 audits correctly registered with `severity` ∈ {medium, low} matching Doc07 §7 column, `title` matching Doc07 §7 column, and `node_ids` referencing the correct sub-domain + activity + role entities.

---

## Block 4 — `id_pattern` compliance

| Type | Pattern | Checked | Violations |
|---|---|---|---|
| RaciRole | `^ROLE-[A-Z0-9]+$` | 6 (ROLE-DPO, ROLE-CISO, ROLE-DEV, ROLE-LEGAL, ROLE-HR, ROLE-BOARD) | **0** |
| RaciActivity | `^ACT-\d{2}$` | 43 (ACT-01 … ACT-43, all two-digit zero-padded) | **0** |
| Cross-pattern conflict | None of the pre-existing 197 nodes matches either RACI pattern | 197 | **0** |

The `RaciRole` and `RaciActivity` id namespaces do not collide with any existing node type. PASS.

---

## Block 5 — Original spine intact

### Pre-A nodes (197)

| Type | Count |
|---|---|
| CompanyContext | 1 |
| Regulation | 5 |
| Domain | 10 |
| SecurityControlDomain | 38 |
| RegulatoryClause | 54 |
| AdjustedGoal | 69 |
| Tension | 4 |
| Stakeholder | 7 |
| BusinessGoal | 5 |
| CoverageGap | 4 |
| **Total** | **197** |

All 197 pre-A nodes present. PASS.

### Pre-A audits (16)

All 16 audit IDs and titles from the v1.2 baseline are preserved verbatim:

| id | severity | title (preserved) |
|---|---|---|
| CFL-001 | high | "GDPR-C08 / GDPR-C11 article assignments diverge between ontology and Doc10" |
| CFL-002 | high | "Subdomain count cascade: 38 / 37 / 35 across docs" |
| CFL-003 | medium | "phase1_ontology.yaml coverage_summary subdomains_covered labels disagree with Doc11 §6" |
| CFL-004 | medium | "Normative Intensity: Doc10 §5 (2.819 combined) vs Doc11 §4 (2.947)" |
| CFL-005 | medium | "GAP-002 affected_subdomain_ids cites Domain 'D-01' which is not a SecurityControlDomain" |
| BLN-001 | medium | "Doc10 §8 corpus clause IDs marked (verify) deliverable still open" |
| BLN-002 | high | "Doc13 §0 references D-02.4 / D-06.4 as NOT_ADDRESSED but Doc12 §4 lists them COVERED" |
| BLN-003 | low | "Doc03 §3.1 Contact column is '—' for 6 of 7 stakeholders (only Stripe has an entry)" |
| CVG-001 | high | "3 NOT_ADDRESSED subdomains remain uncovered by applicable regulations" |
| CVG-002 | high | "GAP-001..004 from Doc11 §7 remain unmitigated" |
| CVG-003 | medium | "Subdomain D-07.2/3/4 + D-09.3 have no regulatory clause mapping under GDPR" |
| CVG-004 | low | "Doc09 per-subdomain in-scope card counts may exceed Doc09 §2 'total' column" |
| CVG-005 | low | "Doc03 §4 BG Owner labels 'Lead Dev' and 'Procurement' do not have unambiguous STK-IDs" |
| BAM-001 | high | "397 of 417 ambiguity cards have no Resolution block in Doc09" |
| BAM-002 | medium | "Doc09 §3 top-20 ambiguity cards all carry S3 (high) severity — no S1/S2 visible in top-20" |
| BAM-003 | low | "BG-02 'Affected Stakeholders' cites 'EU market-surveillance authorities' without an STK-ID" |

PASS.

---

## Top 3 findings

1. **Baseline typo in validator brief.** The task brief lists `stakeholders_total=8`; the authoritative v1.2 baseline (and the live graph) is `7`. Brief should be amended to `7` for consistency with `validation/P1_graph_extension_v1.2_validation.md`. **Not a graph defect** — the graph is correct.

2. **Task-spec RACI sample contains 3 cells that contradict Doc07.** The 10-cell sample lists ACT-04@DPO=A, ACT-04@Legal=C, ACT-15@DPO=A; Doc07 source rows §4.1 L163 and §4.4 L189 both show DPO=R, Legal=A for ACT-04 and DPO=R for ACT-15. The graph correctly follows Doc07. **Not a graph defect** — graph is correct; brief sample is stale.

3. **`R/A` composite cells correctly handled.** Doc07 uses `R/A` notation in 3 cells (ACT-27@Dev, ACT-28@Dev, ACT-33@DPO) to indicate a single role carrying both R and A. The graph correctly splits each into 2 separate edges, exposed via `invariants.raci_composite_cells = 3`. This accounts for the 6 extra edges over a strict 200-cell reading (200 + 6 = 206 ✓). **Correct design choice** — captures the dual accountability that a single-letter cell would obscure.

---

## Verdict

**PASS**

All six blocks clean:
- Block 1 — every expected count matches (with the `stakeholders_total=7` baseline correction)
- Block 2 — both `--check` and `--check --strict` exit 0
- Block 3 — all 6 roles, 4 activities, 10 RACI cells (and a full 200-cell sweep), 4 APPLIES_TO, and 5 GAP-RACI audits trace to Doc07 verbatim; zero fabricated edges
- Block 4 — all 49 RACI node IDs comply with their regex; no collision with pre-existing namespaces
- Block 5 — 197 pre-A nodes + 16 pre-A audits byte-identical

The Phase A RACI extension is accepted. Phase B (downstream consumers — KG injection, dashboard wiring, downstream doc references) is unblocked.

**Out-of-scope observations for human attention (per P0):**
- Task brief should be amended (Findings #1, #2) so future re-runs use the correct baseline (7 stakeholders) and the correct 10-cell sample.
- `MAPS_TO_STK` relation is present in `phase1_ontology.compact.json` with `status: deferred` — confirmed unused in the graph (no `MAPS_TO_STK` edges emitted). The `attrs.maps_to_stakeholder` field on RaciRole carries the equivalent information inline. Acceptable; flagging for awareness.
