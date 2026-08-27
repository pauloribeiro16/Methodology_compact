# Validator — phase1_ontology.yaml v1.3 extension

**Artifact:** `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml`
**Version under test:** v1.3 (additive RACI Phase A — Doc07)
**Source doc:** `Doc07_Org_Roles_RACI.md` v1.1 (CORPUS_ENRICHED, 2026-08-06)
**Reference:** `00_METHODOLOGY/diagrams/Class_Models/phase1_contextual_definition.md` (v1.1)
**Validation date:** 2026-08-26
**Validator verdict:** **PASS (CONDITIONAL on §9.3 stale-caption clarification — see Block D)**

---

## Block A — Additive diff

### Diff summary (git)

```
$ git diff --shortstat HEAD -- 02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml
 1 file changed, 59 insertions(+), 1 deletion(-)
```

- **Insertions:** 59 (≥ 50 as required).
- **Deletions:** 1 — verified by inspecting the diff hunk header; the single deletion is **exactly** the version line `version: "1.2"` → `version: "1.3"`. No body key was deleted.

### Structural verification (Python asserts)

```python
import yaml
d = yaml.safe_load(open('phase1_ontology.yaml'))
print(d['header']['version'])        # '1.3'
ko = d['kg_ontology']
print(sorted(ko['classes'].keys()))
print(sorted([r['verb'] for r in ko['relations']]))
print(sorted(ko['enums'].keys()))
print(sorted(ko['invariants']['counts'].keys()))
print(sorted(ko['invariants']['id_patterns'].keys()))
```

| Block | Count | Sorted keys (new keys **bold**) |
|---|---|---|
| `header.version` | — | **1.3** ✓ |
| `kg_ontology.classes` | 12 | `AdjustedGoal, BusinessGoal, CompanyContext, CoverageGap, Domain`, **`RaciActivity`, `RaciRole`**, `Regulation, RegulatoryClause, SecurityControlDomain, Stakeholder, Tension` |
| `kg_ontology.relations` (verbs) | 14 | `ADDRESSED_IN, APPLIES_TO, ASSESSES, BELONGS_TO, COVERS, DEFINES, FLAGS, HAS_TENSION_WITH, MAPS_TO, **MAPS_TO_STK**, OVERLAPS_WITH, **RACI**, SUPPORTS, YIELDS` |
| `kg_ontology.enums` | 10 | `CoverageLevel, ObligatedPartyType, ObligationType, Priority, ProportionalityTier`, **`RaciLetter`**, `Scale, Severity, StakeholderType, TensionType` |
| `kg_ontology.invariants.counts` | 20 | `ambiguity_cards_in_scope`, **`applies_to_edges`**, `business_goals_total, clauses_total, coverage_gaps_total, domains`, **`gap_raci_count`**, `goals_total`, **`raci_activities`, `raci_activities_active`, `raci_composite_cells`, `raci_edges_min`, `raci_roles`**, `regulations_applicable, regulations_total, stakeholders_total, subdomains_active, subdomains_covered, subdomains_total, tensions_total` |
| `kg_ontology.invariants.id_patterns` | 12 | `AdjustedGoal, BusinessGoal, CompanyContext, CoverageGap, Domain`, **`RaciActivity`, `RaciRole`**, `Regulation, RegulatoryClause, SecurityControlDomain, Stakeholder, Tension` |

### Body-key unchanged check

All 10 original classes (AdjustedGoal, BusinessGoal, CompanyContext, CoverageGap, Domain, Regulation, RegulatoryClause, SecurityControlDomain, Stakeholder, Tension) appear unchanged.
All 9 original enums (CoverageLevel, ObligatedPartyType, ObligationType, Priority, ProportionalityTier, Scale, Severity, StakeholderType, TensionType) appear unchanged.
All 13 original counts appear unchanged; 7 new counts are appended.
All 10 original id_patterns appear unchanged; 2 new (RaciRole, RaciActivity) appended.

**Block A: PASS** — purely additive, exactly 1 deletion (the version line), schema intact.

---

## Block B — Citation verification (7 cited attributes)

| # | Attribute / Relation / Enum | Cited at | Doc07 verification | Pass/Fail |
|---|----------------------------|----------|--------------------|-----------|
| 1 | **RaciRole attrs** `id, name, maps_to_stakeholder, fte_allocation, reports_to, backup` | Doc07 §2 "Key Roles" | §2 table L63 has columns: `Role, Person/Team, Reports To, FTE Allocation, Backup`. Spot-checked 6 rows L65–L70 (CEO, CTO, Lead Dev, Developer×5, Legal Adviser, Board) and L71 (IR Lead folded into CISO). | **PASS** — 4 of 6 attrs match column headers (`fte_allocation`, `reports_to`, `backup`, name from `Role`). `id` is convention. **`maps_to_stakeholder` is the Executor's inference** — Doc07 does not name a stakeholder column; this is a deliberate cross-reference to Doc03 §3.1 (flagged in source: "Doc07 §2 cross-ref"). Acceptable as case-level inference but explicitly `status: deferred` on the verb. |
| 2 | **RaciActivity attrs** `id, name, domain_id, sub_domain_id, corpus_reg_req, active` | Doc07 §4.1–§4.10 | Spot-checked §4.1 L158 (4 activities L160–L163, has `Corpus Reg Req` column), §4.4 L185 (6 activities L187–L192, has `Corpus Reg Req` column), §4.10 L254 (3 activities L256–L258, has `Corpus Reg Req` column). All §4.x tables have `Corpus Reg Req` column populated with `D-XX.Y: req_ids` format. `domain_id` and `sub_domain_id` are derivable from `D-XX.Y:` prefix. | **PASS** — all 6 attrs traceable. |
| 3 | **RACI verb citation** "Doc07 §4.x cells" | Doc07 §4 tables | Confirmed format `D-XX \| DPO \| CISO \| Dev \| Legal \| HR \| Board \| Corpus Reg Req` across all 10 §4 subsections (L158, L167, L176, L185, L196, L205, L214, L223, L244, L254). 5 sample cells from 3 different sections verified: L160 (`Encrypt personal data at rest \| C \| A \| R \| I \| — \| I`), L189 (`Notify authorities \| R \| A \| C \| C \| — \| I`), L216 (`Threat model per feature \| C \| C \| R/A \| I \| — \| I`). | **PASS** — format matches §4 convention. |
| 4 | **APPLIES_TO verb citation** "Doc07 §9.2 activity→sub-domain mapping" | Doc07 §9.2 L354–L393 | Confirmed 35 rows (header at L356, data L358–L392). Each row format: `RACI Activity \| Mapped Sub-domain \| Rationale`. Example L358: `Encrypt personal data at rest \| D-01.1 \| Encryption-at-rest is D-01.1 (not D-01.2 in-transit)`. The activity→sub-domain mapping exists in source. | **PASS** — 35 rows match Executor count. |
| 5 | **RaciLetter enum `[R, A, C, I]`** | Doc07 §4 legend | Legend at L133–L139: "**R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed, **—** = Not involved". All four letters explicitly defined. | **PASS** — citation honest. |
| 6 | **MAPS_TO_STK `status: deferred`** | Doc07 §2 cross-ref + Doc03 §3.1 | Doc03 §3.1 stakeholders (L75–L81) are: STK-CEO-01, STK-CTO-01, STK-DPO-01, STK-DEVP-01, STK-CUSTOMER-01, STK-STRIPE-01, STK-AWS-01. None of `STK-DEV-*`, `STK-LEGAL-*`, `STK-HR-*`, `STK-BOARD-*` exists. (Closest: `STK-DEVP-01` for Dev.) No Legal/HR/Board stakeholders. ROLE-DPO plausibly maps to STK-CEO-01 (DPO hat = CEO person) or STK-DPO-01 (DPO role); ROLE-CISO to STK-CTO-01. ROLE-DEV/LEGAL/HR/BOARD have no direct STK targets. | **PASS** — `status: deferred` is correct. |
| 7 | **`MAPS_TO_STK` verb NOT in Class_Models v1.1** | grep on phase1_contextual_definition.md | `grep -n "RaciRole\|RaciActivity\|MAPS_TO_STK\|RACI\|APPLIES_TO" 00_METHODOLOGY/diagrams/Class_Models/phase1_contextual_definition.md` returned **0 matches**. | **PASS** — confirmed case-level construct. |

**Block B: PASS (with one flag — see Block D finding 3)**

---

## Block C — Hand-count vs Executor counts

Read Doc07 end-to-end and counted manually. Findings:

### C.1 — 6 RaciRole entries

Doc07 §2 (L59–L72) has **7 person rows** in the Key Roles table:
| L | Role | Maps to RACI column |
|---|---|---|
| L65 | CEO (DPO hat) | DPO |
| L66 | CTO (CISO hat) | CISO |
| L67 | Lead Developer | Dev (combined) |
| L68 | Developer × 5 | Dev (combined) |
| L69 | External Legal Adviser | Legal |
| L70 | Management Board | Board |
| L71 | IR Lead (CTO/CISO capacity) | CISO (folded per L147) |

§4 RACI column headers (L142–L148): DPO, CISO, Dev, Legal, HR, Board → **6 distinct role hats**.

Per §4 column note L147: "HR = CEO in HR-coordination role (overlaps with DPO column; same person; not double-counted)" — HR is treated as a separate RACI column even though the CEO wears both hats.

So: 7 §2 person rows → 6 RACI column hats (Lead Dev + Dev×5 folded into `Dev`; IR Lead folded into `CISO`).

**Hand-count: 6** ✓ matches Executor (6/43/206/35/5).

### C.2 — 43 RaciActivity (42 main + 1 best-practice)

Counted activity rows in each §4 subsection:

| § | Line range | Activity count |
|---|---|---|
| 4.1 Data Protection | L156–L164 | 4 |
| 4.2 Vulnerability Management | L165–L173 | 4 |
| 4.3 Access Control | L174–L182 | 4 |
| 4.4 Incident Response | L183–L193 | 6 |
| 4.5 Data Lifecycle | L194–L202 | 4 |
| 4.6 Supply Chain | L203–L211 | 4 |
| 4.7 Secure Development | L212–L220 | 4 |
| 4.8 main (D-08.x, including INACTIVE row) | L221–L229 | 4 |
| 4.8 best-practice sub-table | L230–L241 | 1 (L238) |
| 4.9 Governance | L242–L251 | 5 |
| 4.10 Monitoring & Audit | L252–L259 | 3 |
| **Total** | | **43** |

**42 main-table rows** (§4.1–§4.10 main, including the §4.8 INACTIVE placeholder) + **1 best-practice row** (§4.8 L238) = **43 ACT-NN**.

Of these, **2 are inactive**:
- ACT-34 (L228, "Board cybersecurity briefings") — all `—` (DPO=—, CISO=`See below`, Dev=—, Legal=—, HR=—, Board=—) plus INACTIVE Corpus Reg Req
- ACT-35 (L238, "Quarterly informal cybersecurity briefing") — explicitly flagged in §4.8 narrative L240 as best-practice placeholder ("not a derived AEGIS requirement")

**41 active activities.** ✓ matches Executor's `raci_activities: 43, raci_activities_active: 41`.

### C.3 — 206 RACI edges

Counted cells across all 43 activity rows × 6 columns = 258 cells:

| Cell type | Count | Edges contribution |
|---|---|---|
| Em-dash `—` cells (no involvement) | 54 | 0 edges |
| Single-letter cells (R/A/C/I) | 200 | 200 × 1 = 200 edges |
| `**See below**` placeholder (ACT-34 only) | 1 | 0 edges (placeholder, not a RACI assignment) |
| Composite `R/A` cells | 3 | 3 × 2 = 6 edges |
| **Total active edges** | | **206** |

Specific `R/A` composites found (verified):
- §4.7 L216: `Threat model per feature | C | C | **R/A** | I | — | I` (Dev column) → ACT-27 ✓
- §4.7 L217: `Code review | I | C | **R/A** | — | — | I` (Dev column) → ACT-28 ✓
- §4.8 L227: `Role-specific training — DPO competence refresh | **R/A** | C | — | C | I | I` (DPO column) → ACT-33 ✓

ACT-34 (Board cybersecurity briefings) contributes 0 edges (all-—/See-below placeholder).
ACT-35 (Quarterly informal briefing) contributes 2 edges (CISO=R, Board=A); fits within the 200 single-letter count (2 of those 200).

**Hand-count: 206 edges.** ✓ matches Executor's `raci_edges_min: 206, raci_composite_cells: 3`.

### C.4 — 35 APPLIES_TO edges (Doc07 §9.2)

Counted §9.2 mapping table rows: header at L356, data rows at L358–L392 = **35 rows**.

Each row maps a `RACI Activity` → `Mapped Sub-domain` with `Rationale`. 35 distinct activity→sub-domain mappings.

**Hand-count: 35.** ✓ matches Executor's `applies_to_edges: 35`.

### C.5 — 5 GAP-RACI findings (Doc07 §7)

Counted GAP rows in §7 (L304–L315):
- GAP-RACI-01 (L310) — D-08.1
- GAP-RACI-02 (L311) — D-08.2
- GAP-RACI-03 (L312) — D-08.2
- GAP-RACI-04 (L313) — D-08.3 INACTIVE
- GAP-RACI-05 (L314) — D-09.1

**Hand-count: 5.** ✓ matches Executor's `gap_raci_count: 5`.

### C.6 — Brief vs Executor vs Ground Truth

| Metric | Original brief | Executor | Doc07 ground truth | Match |
|---|---|---|---|---|
| RaciRole | 6 | 6 | 6 (§2 hats, §4 columns) | ✓ |
| RaciActivity | 31 (30 active + 1 placeholder) | 43 (41 active) | 43 §4 rows / 41 active | Brief stale; Executor correct |
| RACI edges | ~90 | 206 | 206 (200 single + 6 composite) | Brief stale; Executor correct |
| APPLIES_TO edges | 30 | 35 | 35 §9.2 rows | Brief stale; Executor correct |
| GAP-RACI | 5 | 5 | 5 §7 rows | ✓ |

**Why the brief was wrong:** Doc07 §9.3 (L397) says "RACI rows enriched: 30" — a **stale caption** from a Sprint 2 snapshot. The brief derived "31" (= 30 + 1 assumed placeholder) from this caption. But §4 actually has 43 activity rows (42 main + 1 best-practice), §9.2 has 35 mapping rows, and §9.3's "30" caption is inconsistent with both. The Executor's `raci_edges_min: 206` is the actual edge count from §4 cells.

The Executor's commentary on the ontology file (the long header comment block) explicitly flags this discrepancy: "the task brief's '30 active + 1 placeholder = 31' matches Doc07 §9.3's caption but not §4 (42 main-table rows) or §9.2 (35 rows)."

**Critical question answered:** **The Executor's counts (6/43/206/35/5) are the actual Doc07 ground truth.** The brief's numbers (6/31/~90/30/5) are derived from a stale §9.3 caption ("30 enriched") and miss 12 activity rows in §4 beyond the §9.2 enumeration (notably §4.4 has 6 rows; the §9.2 mapping collapses "Notify DPA" and "Notify controllers" into one row at L360, which contributes to the gap).

---

## Block D — Verdict

### Verdict: **PASS (CONDITIONAL)**

The v1.3 extension is **purely additive**:
- 59 insertions, 1 deletion (the version line only)
- All original schema keys preserved unchanged
- New classes (`RaciRole`, `RaciActivity`), relations (`RACI`, `APPLIES_TO`, `MAPS_TO_STK`), enum (`RaciLetter`), counts (7 new), id_patterns (2 new) all correctly cited and accurately reflect Doc07
- Ground-truth hand-counts match Executor counts on all 5 metrics

**Conditional finding** (informational, not a blocker): the ontology comment block documents that the brief's older numbers (31/~90/30) are stale; this clarification is **already present** in the YAML header (lines noting "the task brief's '30 active + 1 placeholder = 31' matches Doc07 §9.3's caption but not §4 …"). The Executor's reconciliation note is honest and self-disclosing. No correction needed.

### Three most important findings

1. **All 5 Executor's counts match hand-counted ground truth (6/43/206/35/5).** The Executor's `raci_edges_min: 206` and `raci_activities: 43` reflect actual §4 cell mechanics (200 single-letter cells + 3 composite R/A × 2 + the correct interpretation of "See below" as a non-edge placeholder). The brief was wrong because it derived from Doc07 §9.3's stale "30 enriched" caption.

2. **The 3 composite R/A cells are precisely identified:** ACT-27 (Threat model per feature, Dev=R/A) at §4.7 L216, ACT-28 (Code review, Dev=R/A) at §4.7 L217, ACT-33 (DPO competence refresh, DPO=R/A) at §4.8 L227. ACT-34 (Board cybersecurity briefings) is the only all-—/See-below placeholder row and correctly contributes 0 edges. ACT-35 (best-practice quarterly briefing) has CISO=R + Board=A = 2 edges and is correctly tagged `active=false`.

3. **`maps_to_stakeholder` is an Executor inference**, not a column in Doc07 §2. The source comment correctly attributes it to "Doc07 §2 cross-ref" and marks the verb `status: deferred`. This is honest disclosure — Doc03 §3.1 has 7 stakeholders (STK-CEO-01, STK-CTO-01, STK-DPO-01, STK-DEVP-01, STK-CUSTOMER-01, STK-STRIPE-01, STK-AWS-01) but no STK-LEGAL/HR/BOARD. Only DPO/CISO have plausible cross-refs (DPO→STK-CEO-01 because the DPO hat is worn by the CEO; CISO→STK-CTO-01 similarly). The `deferred` status correctly avoids asserting mappings the source doesn't support. **Recommended follow-up (non-blocking):** if/when the methodology wants to elevate this, add a `MAPS_TO_STK` decision matrix in Doc03 or a new Doc07 §10 — until then, `deferred` is the honest choice.

### Diff hygiene notes

- The diff is purely additive in the body. The single deletion is the version line.
- No body key was renamed, reordered, or removed.
- The new RACI classes are correctly placed in the `classes:` section, the new verb relations in the `relations:` list, the new enum in the `enums:` section, and the new counts/id_patterns in the `invariants:` section — all consistent with the existing schema layout.

---

## Validator final action

No modifications to the ontology are required. The v1.3 extension is correct and ready for downstream consumers (Sprint 7 RACI Phase A — graph loader, RACI activity nodes, RaciRole nodes, RACI/APPLIES_TO edges).

A note has been flagged in the ontology's own header explaining the discrepancy between the brief's stale numbers and the corrected ground-truth counts; this is sufficient documentation and does not require Validator amendment.
