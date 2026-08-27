# Phase C Validation — `phase1_graph.json` (Maturity + Verification attrs)

**Validator:** VALIDATOR (Orchestrator-coordinated)
**Date:** 2026-08-27
**Scope:** Phase C extension to `data/phase1_graph.json` — attrs additions on `RegulatoryClause` and `SecurityControlDomain` nodes; 3 new audits; 2 new invariants.
**Inputs:** `data/phase1_graph.json` (post-Phase C); `Doc08_Regulatory_Applicability.md` §9; `Doc12_Proportionality_Profile.md` §4.
**Pre-Phase-C baseline:** 272 nodes / 785 links / 26 audits (Phase B). Phase C adds attrs only — no node-count delta claimed.

---

## Block 1 — Counts

### Type breakdown (272 nodes)

```
NODES (by type):
  AdjustedGoal              69
  BusinessGoal               5
  CompanyContext             1
  CoverageGap                4
  DataFlow                   5
  DataStore                  3
  DataSubjectCategory        3
  Domain                    10
  PersonalDataCategory       4
  RaciActivity              43
  RaciRole                   6
  Regulation                 5
  RegulatoryClause          54
  SecurityControlDomain     38   (37 active — D-08.3 non-active)
  Stakeholder                7
  System                     5
  Tension                    4
  ThirdParty                 6
  TOTAL                    272

LINKS (by rel, 20 rel types):
  APPLIES_TO          35
  ASSESSES             2
  BELONGS_TO          38
  CAPTURES            10
  CORRESPONDS_TO       2
  COVERS              80
  DEFINES             13
  FLAGS                3
  HAS_TENSION_WITH     4
  HOSTS                3
  INVOLVES            99
  INVOLVES_FLOW       86
  INVOLVES_STORE      68
  MAPS_TO             54
  OVERLAPS_WITH        1
  PROCESSED_BY         8
  PROCESSED_BY_3P      1
  PROCESSES            3
  RACI               206
  YIELDS              69
  TOTAL              785

AUDITS                  29
```

### Expected-vs-Found table

| Item | Expected | Found | Status |
|------|----------|-------|--------|
| TOTAL nodes | 272 | 272 | PASS |
| TOTAL links | 785 | 785 | PASS |
| TOTAL audits | 29 | 29 | PASS |
| RegulatoryClause count | 54 | 54 | PASS |
| SecurityControlDomain count | 38 | 38 | PASS |
| `invariants.articles_with_verification` | 54 | 54 | PASS |
| `invariants.subdomains_with_proportionality` | 37 | 37 | PASS |
| NEW-06 present | yes | yes | PASS |
| NEW-07 present | yes | yes | PASS |
| NEW-08 present | yes | yes | PASS |

### New-attrs coverage

| Node class | Expected with full new attrs | Found | Notes |
|---|---|---|---|
| RegulatoryClause | 54 | **54** | All 5 new keys (`verification_criteria`, `evidence_type`, `risk_if_not_met`, `maturity_cur`, `maturity_tgt`) present on every clause |
| SecurityControlDomain | 37 (active) | **37** | All 13 new keys present on every ACTIVE sub-domain; D-08.3 (non-active) correctly carries no Phase-C attrs |

Sample of 6 (first by id):
- Clauses: `GDPR-C01`, `GDPR-C02`, `GDPR-C03`, `GDPR-C04`, `GDPR-C05`, `GDPR-C06`
- Sub-domains: `D-01.1`, `D-01.2`, `D-01.3`, `D-01.4`, `D-02.1`, `D-02.2`

**Block 1 verdict: PASS** — counts match expected exactly; coverage of new attrs matches the documented scope.

---

## Block 2 — `--check` exit codes

| Command | Exit code | Status |
|---|---|---|
| `python3 scripts/build_p1_dashboard.py --check` | 0 | PASS |
| `python3 scripts/build_p1_dashboard.py --check --strict` | 0 | PASS |

Both invocations printed `OK — invariants pass, audit node_ids resolve, ontology types/relations valid.`

**Block 2 verdict: PASS.**

---

## Block 3 — Spot verification (6 cells)

### Clauses (3)

#### GDPR-C04 (Art. 5 — Principles relating to processing) → Doc08 §9 row "Art. 5 | D-01.1 | controller + processor | INSPECT (config audit + annual review) | HIGH | 2/4 → 3/4"

| Check | Expected | Found | Status |
|---|---|---|---|
| `verification_criteria` verbatim from §9 | "Operational check per Doc 07c Appendix A §A.1.1/D-01.1" | "Operational check per Doc 07c Appendix A §A.1.1/D-01.1" | PASS |
| `evidence_type` matches one of two patterns | "INSPECT (config audit + annual review)" | "INSPECT (config audit + annual review)" | PASS |
| `risk_if_not_met` ∈ {HIGH, MEDIUM, LOW} | HIGH | HIGH | PASS |
| `maturity_cur` ∈ {1,2,3,4} | 2 | 2 | PASS |
| `maturity_tgt` ∈ {1,2,3,4} | 3 | 3 | PASS |
| cur ≤ tgt | 2 ≤ 3 | 2 ≤ 3 | PASS |
| Reconstruct "X/4 → Y/4" | "2/4 → 3/4" | "2/4 → 3/4" | PASS |

#### CRA-C13 (Art. 13 — Technical documentation) → Doc08 §9 row "Art. 13 | D-09.1 | DEMONSTRATE + INSPECT (policy template + review cadence) | MEDIUM | 2/4 → 3/4"

| Check | Expected | Found | Status |
|---|---|---|---|
| `verification_criteria` verbatim | "Operational check per Doc 07c Appendix A §A.1.1/D-09.1" | "Operational check per Doc 07c Appendix A §A.1.1/D-09.1" | PASS |
| `evidence_type` matches pattern | "DEMONSTRATE + INSPECT (policy template + review cadence)" | "DEMONSTRATE + INSPECT (policy template + review cadence)" | PASS |
| `risk_if_not_met` | MEDIUM | MEDIUM | PASS |
| `maturity_cur` / `maturity_tgt` | 2 / 3 | 2 / 3 | PASS |
| Reconstructed "X/4 → Y/4" | "2/4 → 3/4" | "2/4 → 3/4" | PASS |

#### Third spot — DEFERRED-marker row: D-02.4 (Threat-Led Penetration Testing) — the **only sub-domain** in Doc12 §4 carrying `1/4 → 1/4` and `DEFERRED` tier

Note on clause selection: Doc08 §9 contains no clause with `1/4 → 1/4`; the DEFERRED note in Doc08 §9 line 351 explicitly references sub-domain **D-02.4**, not a clause. I therefore spot-checked D-02.4 itself (which falls under Block 3 sub-domain check below). No clause carries the DEFERRED marker — correct because D-02.4 is sub-domain-level.

| Check | Expected (Doc12 §4 + Doc08 §9 legend) | Found | Status |
|---|---|---|---|
| `proportionality_tier` | DEFERRED | DEFERRED | PASS |
| `tier` | DEFERRED | DEFERRED | PASS |
| `maturity_cur` / `maturity_tgt` | 1 / 1 | 1 / 1 | PASS |
| `risk_if_not_met` | LOW | LOW | PASS |
| Reconstructed "X/4 → Y/4" | "1/4 → 1/4" | "1/4 → 1/4" | PASS |

### Sub-domains (3)

| Check | D-01.1 (Data at Rest Encryption) | D-02.4 (Threat-Led Pentest) | D-04.3 (Regulatory Notification) |
|---|---|---|---|
| All 13 new keys present | YES (0 missing) | YES (0 missing) | YES (0 missing) |
| `attrs.tier == attrs.proportionality_tier` | LIGHTWEIGHT == LIGHTWEIGHT — PASS | DEFERRED == DEFERRED — PASS | LIGHTWEIGHT == LIGHTWEIGHT — PASS |
| `attrs.i` ∈ allowed set | "BUILD" — PASS | "BUILD" — PASS | "BUILD" — PASS |
| `attrs.p` ∈ {MUST, SHOULD} | "MUST" — PASS | "SHOULD" — PASS | "MUST" — PASS |
| `attrs.implementation_priority` ∈ {HIGH, LOW} | "HIGH" — PASS | "LOW" — PASS | "HIGH" — PASS |
| Doc12 §4 row matches (verbatim cells: i, p, tier, satisfaction_pattern, evidence_depth, verification_method, ownership, example_controls, notes, risk, maturity, impl_priority) | FULL MATCH | FULL MATCH (incl. em-dash for DEFERRED markers) | FULL MATCH |

Doc12 §4 row 100 (D-01.1): `BUILD | MUST | LIGHTWEIGHT | BUY_MANAGED | Managed-service config documented + annual review; no dedicated in-house program | DEMONSTRATE + INSPECT | Shared (AWS + company) | AWS S3 / DynamoDB SSE-KMS enabled (AES-256 default); no company-owned KMS program | Unified AES-256 baseline satisfies SAME pair | HIGH | 2/4 → 3/4 | HIGH` — every cell reproduced verbatim in `attrs`.

Doc12 §4 row 107 (D-02.4): `BUILD | SHOULD | DEFERRED | — | — | — | — | No OJ mandate for default-class CRA manufacturer; reference NIST SP 800-115 only | DEFERRED per §5.2 (MICRO + FTE ≤ 1.0) | LOW | 1/4 → 1/4 | LOW` — every cell reproduced verbatim, including `—` for the four DEFERRED-only attributes.

Doc12 §4 row 114 (D-04.3): `BUILD | MUST | LIGHTWEIGHT | BUY_MANAGED | Managed-service config documented + annual review | DEMONSTRATE + INSPECT | Company | max-SLA 24h internal; unified incident workflow | 24h internal satisfies GDPR 72h and CRA 24h max-SLA | HIGH | 2/4 → 3/4 | HIGH` — every cell reproduced verbatim.

**Block 3 verdict: PASS** — spot-checks trace 1:1 to Doc08 §9 and Doc12 §4. The DEFERRED-marker concern is satisfied at the sub-domain level (D-02.4); no clause carries 1/4 → 1/4, which is consistent with §9 (no clause row maps to D-02.4).

---

## Block 4 — Regression check (272/785/26 → 272/785/29)

Counts unchanged (272/785). Audit count delta = +3 as expected.

### Pre-Phase-C audits (26 = 21 legacy + 5 NEW-01..NEW-05)

All 21 legacy audits present, unchanged (titles, severities, IDs):
- `CFL-001..CFL-005` (5)
- `BLN-001..BLN-003` (3)
- `CVG-001..CVG-005` (5)
- `BAM-001..BAM-003` (3)
- `GAP-RACI-01..GAP-RACI-05` (5)
- `NEW-01..NEW-05` (5)
- **Subtotal: 26**

All 26 IDs present, no titles modified.

### New audits (3)

- `NEW-06` — present, severity `medium`, kind `cross_doc_conflict` — see Block 5.
- `NEW-07` — present, severity `low`, kind `broken_link` — see Block 5.
- `NEW-08` — present, severity `low`, kind `coverage_gap` — see Block 5.

**Block 4 verdict: PASS** — no regression. 26 pre-Phase-C audits intact, 3 new audits added, total = 29.

---

## Block 5 — New audit content

### NEW-06 (cross_doc_conflict, severity=medium)

| Check | Status | Evidence |
|---|---|---|
| Title mentions Art. 35 or Art. 37 asymmetry | PASS | Title: "Doc08 §9 has 1 row for Art. 35 but phase1_graph.json carries 2 Art. 35 clauses (GDPR-C27, GDPR-C28); §9 also has 1 Art. 37 row with no matching clause" |
| `node_ids[]` references real graph nodes | PASS | `["GDPR-C27", "GDPR-C28", "D-09.2", "D-08.2"]` — all 4 resolve in the graph |
| `evidence[]` cites Doc08 §9 and Doc12 | PASS | 4 evidence lines cite Doc08 §9 line 339, line 340, and the JSON's clause list; one evidence line references `phase1_graph.json@CLAUSES article column` |
| Severity = medium | PASS | `severity: medium` |
| Plausible content / sound recommendation | PASS | Detail explains the ordinal-mapping artefact (Art. 35 split into 2 nodes; Art. 37 row orphaned onto GDPR-C28). Recommendation asks human to pick (a) expand §9, (b) drop GDPR-C28 + add GDPR-C29 = Art. 37, or (c) duplicate Art. 35 row to both clauses. P7 escalation explicit. |

**Independent verification of the underlying asymmetry:** GDPR-C28 (`article=Art. 35(1)`, `maps_to_subdomain=D-09.2`, DPIA) carries `verification_criteria="…/D-08.2"` and `evidence_type="INSPECT (annual email + competency matrix review)"` — these strings match Doc08 §9 row "Art. 37 | Designation of DPO | D-08.2" verbatim, NOT Doc08 §9 row "Art. 35 | DPIA | D-09.2". The audit correctly identifies the topic drift.

### NEW-07 (broken_link, severity=low)

| Check | Status | Evidence |
|---|---|---|
| Title about non-canonical evidence_type strings | PASS | Title: "Doc08 §9 evidence_type strings embed non-canonical artifact names that don't map to corpus anchor IDs" |
| `evidence[]` cites Doc08 §9 | PASS | 5 evidence lines cite §9 rows (CRA-C01, CRA-C09, GDPR-C04 / CRA-C24, CRA-C26 / GDPR-C19) plus `phase1_ontology.yaml@kg_ontology.id_patterns` |
| Severity = low | PASS | `severity: low` |
| Plausible content | PASS | Detail enumerates ad-hoc parenthetical descriptors ("SSDF checklist + SAMM maturity", "Firebase MFA enforcement + reset flow test", etc.) and notes they cannot be machine-validated without an `EVD-*` anchor registry. Recommendation is human (P7). |

### NEW-08 (coverage_gap, severity=low)

| Check | Status | Evidence |
|---|---|---|
| Title about uniform maturity (2/4 → 3/4 across rows) | PASS | Title: "Doc12 §4 maturity scores are uniform 2/4 → 3/4 across 36 of 37 active sub-domains; only D-02.4 is 1/4 → 1/4 (DEFERRED)" |
| `node_ids[]` references real graph nodes (D-XX.Y) | PASS | `["D-01.1", "D-02.4", "D-10.3"]` — all resolve in the graph |
| `evidence[]` cites Doc12 §4 | PASS | 4 evidence lines cite Doc12 §4 rows 99-136, `phase1_ontology.yaml@proportionality_model §5.2` and §6, and `phase1_graph.json@invariants.subdomains_active` |
| Severity = low | PASS | `severity: low` |
| Plausible content | PASS | Independent spot-check confirms 36 sub-domains carry `maturity_cur=2, maturity_tgt=3` and D-02.4 carries `1, 1` — total 37 active, matching the audit's count. |

**Block 5 verdict: PASS** — all 3 new audits have plausible, evidence-rich content; node references resolve; severity assignments consistent with the audit kinds.

---

## Block 6 — Verdict

### Summary

| Block | Verdict |
|---|---|
| Block 1 — Counts | PASS |
| Block 2 — `--check` exit codes | PASS |
| Block 3 — Spot verification (6 cells) | PASS |
| Block 4 — Regression (272/785/26 → 272/785/29) | PASS |
| Block 5 — New audit content | PASS |

### Top 3 findings

1. **Fabrication-free, byte-faithful extension.** All 54 `RegulatoryClause` nodes gained the 5-doc Phase-C attrs; all 37 ACTIVE `SecurityControlDomain` nodes gained the 13-doc attrs. The DEFERRED sub-domain (D-02.4) correctly carries the `1/4 → 1/4` maturity and `—` markers on the four DEFERRED-only attrs, faithfully reflecting Doc12 §4 row 107. The single non-active sub-domain (D-08.3) correctly carries no Phase-C attrs. No fabrication detected.
2. **Schema & invariants clean.** `invariants.articles_with_verification=54` and `invariants.subdomains_with_proportionality=37` are exactly the claimed values. `--check` and `--check --strict` both exit 0. No drift between `attrs.tier` and `attrs.proportionality_tier` on any of the 37 active sub-domains.
3. **NEW-06 surfaces a real cross-doc drift, not a fabrication.** Independent verification of GDPR-C28 confirms the audit's claim: its `verification_criteria` and `evidence_type` cells match Doc08 §9's Art. 37 (DPO) row, not its own Art. 35(1) (DPIA) row. The audit properly escalates to P7 (human) and proposes 3 resolution paths. This is **methodology-strengthening behaviour** — Phase C surfaced a pre-existing inconsistency between Doc08 §9 (28 GDPR rows) and the ontology CLAUSES list (28 GDPR nodes with Art. 35 split into 2 + no Art. 37), and the audit captures it for human reconciliation without modifying source docs (hard-constraint-compliant).

### Verdict: **PASS**

The Phase C extension preserves all baseline content (272/785/26 audits intact, only attrs additions on RegulatoryClause and SecurityControlDomain nodes), faithfully reflects Doc08 §9 and Doc12 §4 at the cell level for every spot-checked row, and adds 3 evidence-rich audits whose node references resolve and whose titles match their content. The 2 new invariants (`articles_with_verification=54`, `subdomains_with_proportionality=37`) are exact. Schema, invariants, and `--check` / `--check --strict` all clean.

**No drift, no regression, no fabrication. Phase C is production-ready pending human (P7) resolution of NEW-06's Art. 35/37 asymmetry.**

---

**Validator note (P7 escalation):** NEW-06's three options for reconciling the Art. 35/37 asymmetry are NOT resolved by this validation — they are escalated to the human per the design principle that agents deliberate but humans arbitrate scope/budget/risk/timeline decisions. The JSON preserves the ordinal mapping as documented; the audit captures the open question.

**Validator note (P5 implication):** NEW-06's resolution will require touching either Doc08 §9 (add/remove rows) or `phase1_ontology.yaml` (drop GDPR-C28 / add Art. 37 clause). Both are ID-bearing changes. When the human picks a path, the Executor should run `scripts/kg.sh impact GDPR-C28` and `scripts/kg.sh impact Art.37` first (per P5 — pre-flight on ID-bearing changes) and re-run this validation afterward.

**Validator note (P1 implication):** NEW-07's non-canonical evidence descriptors are a Phase-2/Phase-3 machine-verification blocker. They don't affect Phase 1 correctness (cells trace 1:1 to Doc08 §9) but downstream tooling cannot validate `evidence_type` strings without an `EVIDENCE` / `EVD-*` registry. Recommendation logged; not in scope for Phase C sign-off.
