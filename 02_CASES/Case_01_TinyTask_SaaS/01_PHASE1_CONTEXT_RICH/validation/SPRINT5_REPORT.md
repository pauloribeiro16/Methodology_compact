# Fase de Especificação 5 Report — Deep Enrichment (Phase 1 Rich Mode)

> **Sprint:** 5 — Deep Enrichment (without Effort/Cost/Timeline)
> **Case:** Case_01_TinyTask_SaaS
> **Branch:** `feature/aegis-p1-case01-rich`
> **Date:** 2026-08-06
> **Author:** Fase de Especificação 5 Executor (deep-enrichment-builder)
> **Status:** DEEP_ENRICHED — 6/6 lints PASS

> **Historical Note (added 2026-08-10, Fase de Especificação 8 corr-009):** Historical report from corr-007 era. Current 07c version is v4.0 with AO ID model (corr-008 supersedes corr-007). Content below preserved verbatim; the 74 detail cards referenced throughout this report retain their legacy PG/SG headings for Phase 2 traceability — see `07c_Adjusted_Objectives.md` Appendix A §A.0 alias table for the corr-008 AO ID equivalents.

---

## §1 Summary

Fase de Especificação 5 adds deep operational + qualitative provenance to the Phase 1 Rich docs that Fase de Especificação 4 produced (Fase de Especificação 4 created the table skeletons + summary). Specifically:

- **5 docs enriched** — Doc 04, 05, 05b, 07b, 07c
- **74 detail cards** added to Doc 07c §2a (37 PG) + §3a (37 SG) — 12 fields each, NO Effort/Cost/Timeline
- **4 tensions** expanded to multi-paragraph root cause analysis + resolution options + implementation + verification
- **Per-doc line delta:**
  | Doc | Fase de Especificação 4 → Fase de Especificação 5 | Δ | Notes |
  |-----|---------------------|---|-------|
  | 04 (BG table) | 192 → 196 | +4 | BG table 7→13 cols |
  | 05 (per-article) | 284 → 381 | +97 | New §9 with 54 article rows |
  | 05b (resolutions) | 918 → 1102 | +184 | 20 Resolution sub-sections added |
  | 07b (proportionality table) | 378 → 383 | +5 | §4 table 10→13 cols |
  | 07c (detail cards + tensions) | 292 → 3451 | +3159 | §2a (37 PG) + §3a (37 SG) + §4 expansion |
  | **Total** | **2064 → 5513** | **+3449** | |

**Lints:** 6/6 PASS (regression-free vs Fase de Especificação 4 baseline). See `01_IMPLEMENTATION_TOOLS/lints/reports/lint_report_phase1_20260806_125633.md`.

---

## §2 Per-doc change list

### §2.1 Doc 04 — `04_Company_Context_Assessment.md`

**Section §4 BG table** extended from 7 to 13 columns. **6 new columns added** (NO Effort/Cost/Timeline):

| New col | Description |
|---------|-------------|
| Owner | Role responsible for goal (e.g., "CTO + DPO") |
| Quantitative Metric | Numeric/observable success criterion |
| Affected Stakeholders | Internal + external parties affected by the goal |
| Status | TODO / IN_PROGRESS / DONE |
| Risk if not met | Qualitative H/M/L + 1-line rationale |

Per-BG enrichment data:

| BG ID | Owner | Status | Risk |
|-------|-------|--------|------|
| BG-01 GDPR Compliance Baseline | CTO + DPO | IN_PROGRESS | HIGH |
| BG-02 CRA Conformity | Lead Dev | TODO | HIGH |
| BG-03 Data Subject Rights | DPO + CTO | TODO | HIGH |
| BG-04 Security by Design | Lead Dev + CTO | IN_PROGRESS | MEDIUM |
| BG-05 Supplier Due Diligence | CTO + Procurement | IN_PROGRESS | MEDIUM |

**Frontmatter updated:** version 2.1 → 2.2, status RECONCILED → DEEP_ENRICHED, fase de especificação 1 → 5, sprint_role → deep_enrichment_bg_table.

### §2.2 Doc 05 — `05_Regulatory_Applicability.md`

**New §9 Per-Article Detailed Breakdown** with 54 rows (28 GDPR + 26 CRA). **8 fields per row:**

| Field | Description |
|-------|-------------|
| Article | Regulation article (e.g., "Art. 5", "Art. 32(1)") |
| Topic | One-line clause description |
| Sub-Domains | Sub-domain(s) mapped from `phase1_ontology.yaml:clause_mappings[].maps_to_subdomain` |
| Obligated Party | controller / processor / manufacturer / CONTROLLER + PROCESSOR |
| Verification Criteria | Pointer to operational check in Doc 07c §2a (PG detail card) |
| Evidence Type | INSPECT (MINIMAL) or DEMONSTRATE + INSPECT (LIGHTWEIGHT) |
| Risk if not met | Qualitative H/M/L |
| Posture (cur→tgt) | Current 2/4 → Target 3/4 (MUST LIGHTWEIGHT) or 1/4 → 1/4 (DEFERRED) |

**§10 Version History (Fase de Especificação 5 addition)** added with row v2.0.

**Frontmatter updated:** version 1.1 → 2.0, status RECONCILED → DEEP_ENRICHED, fase de especificação 1 → 5, sprint_role → deep_enrichment_per_article.

### §2.3 Doc 05b — `05b_Ambiguity_Register.md`

**20 Resolution sub-sections** added (one per top-20 card). **3 fields per Resolution:**

| Field | Description |
|-------|-------------|
| Recommended Variant | R1 / R2 / R3 with rationale |
| Stakeholder Impact | DPO / CTO / Customers / etc. affected by the chosen reading |
| Risk if not resolved | Qualitative H/M/L + 1-line rationale |

Per-card reasoning: R2 (EDPB Guidelines) is dominant for GDPR clauses (authoritative interpretation standard); R1 (in-Directive disambiguation) for CRA clauses; R3 (open-list / illustrative) for ambiguous CRA Annex I lists.

**§7 Gate Criteria** updated with Fase de Especificação 5 enrichment checkbox.

**Frontmatter updated:** version 1.0 → 2.0, status CORPUS_ENRICHED → DEEP_ENRICHED, resolution_sections_added = 20.

### §2.4 Doc 07b — `07b_Proportionality_Profile.md`

**Section §4 table** extended from 10 to 13 columns. **3 new columns added** (NO Effort/Cost/Timeline):

| New col | Description |
|---------|-------------|
| Risk if not met | Qualitative H/M/L derived from priority + tier + sub-domain risk profile |
| Posture (cur→tgt) | Current 2/4 → Target 3/4 for MUST LIGHTWEIGHT; 1/4 → 1/4 for DEFERRED |
| Implementation Priority | HIGH (MUST + non-DEFERRED) / MEDIUM (SHOULD) / LOW (DEFERRED) |

Risk heuristic (HIGH cases):
- D-01.1 / D-01.2 / D-01.4 — encryption (Art. 32 canonical)
- D-04.2 / D-04.3 / D-04.4 — incident response (Art. 33 72h)
- D-05.3 — erasure (Art. 17 hard right)
- D-06.3 — DPA template (Art. 28)
- D-09.2 / D-09.4 — DPIA + RoPA (Art. 35 + Art. 30)
- D-10.2 / D-10.3 — audit + compliance testing

**§8 Version History** added Fase de Especificação 5 row v1.4.

**Frontmatter updated:** version 1.3 → 1.4, status ACTIVE → DEEP_ENRICHED, fase de especificação 4 → 5, sprint_role → deep_enrichment_per_subdomain.

### §2.5 Doc 07c — `07c_Adjusted_Objectives.md`

This is the central enrichment. **74 detail cards** (37 PG + 37 SG) + **4 multi-paragraph tension expansions**.

#### §2.5.1 §2a Privacy Goal Detail Cards (37 cards)

Each PG card has **15 fields** (12 functional + Scope/Out-of-scope):

1. **Description** (multi-paragraph: what/why/scope/out-of-scope, with corpus-derived Sub-SO reference)
2. **Source Article** (GDPR article, e.g., "GDPR Art. 5(1)(f) + Art. 32(1)(b)")
3. **Corpus path** (pointing to `00_METHODOLOGY/PREPROCESSING_by_domain/...`)
4. **NIST CSF Anchors** (PR.DS-01, PR.DS-10 etc., from corpus JSON sidecar)
5. **Verification Criteria (operational)** — 3 specific, actionable checks per sub-domain
6. **Verification Method** (Track B tier-specific: DEMONSTRATE + INSPECT or INSPECT)
7. **Owner** (primary + backup roles)
8. **Status** (TODO)
9. **Dependencies** (3 related sub-domains in same tier)
10. **Risk if not met** (H/M/L + 1-line rationale)
11. **Affected Stakeholders** (internal + external parties)
12. **Implementation Posture** (current → target, 0-4 scale)
13. **Implementation Priority** (HIGH/MEDIUM/LOW)
14. **Scope** (what is included)
15. **Out of scope** (what is excluded)

**§2 (existing) PG table** also got a "See full details" column with anchor link to each card.

#### §2.5.2 §3a Security Goal Detail Cards (37 cards)

Same structure as PG cards but tied to CRA articles + Sub-SOs.

**§3 (existing) SG table** also got the "See full details" anchor column.

#### §2.5.3 §4 Tensions Multi-Paragraph Expansion (4 tensions)

The existing §4 was a 1-line summary table; it is now replaced by **multi-paragraph root cause analysis + resolution options + implementation + verification** for each of T-001..T-004.

Each tension has 8 fields:
1. **Type** + **Severity**
2. **Root Cause Analysis** (3 paragraphs per tension, citing verbatim article text from corpus)
3. **Source Citations** (pointing to corpus JSON sidecars)
4. **Resolution Options Considered** (3 options per tension, with CHOSEN/REJECTED markers)
5. **Implementation** (4 numbered steps per tension, NO timeline)
6. **Verification Criteria** (3 specific checks per tension)
7. **Risk if not resolved** (qualitative H/M/L + 1-line rationale)
8. **Stakeholder Alignment** (CTO + DPO + etc.)
9. **Status** (AGREED per Doc 05 §7 + phase1_ontology.yaml)

**Frontmatter updated:** version 1.0 → 2.0, status ADJUSTED_OBJECTIVES → DEEP_ENRICHED, fase de especificação 4 → 5, sprint_role → deep_enrichment_per_subdomain.

---

## §3 Fields added per document (summary)

| Doc | Fields added | Total fields in new content |
|-----|--------------|-----------------------------|
| 07c (PG card) | Description, Scope, Out of scope, Source Article, Corpus path, NIST CSF Anchors, Verification Criteria (3 bullets), Verification Method, Owner, Status, Dependencies, Risk, Stakeholders, Posture, Implementation Priority | **15 per card × 37 = 555 fields** |
| 07c (SG card) | same as PG | **15 per card × 37 = 555 fields** |
| 07c (tension) | Root Cause (3 paragraphs), Source Citations, Resolution Options, Implementation (4 steps), Verification (3 criteria), Risk, Stakeholder Alignment, Status | **~17 per tension × 4 = 68 fields** |
| 07b (§4 col) | Risk if not met, Posture (cur→tgt), Implementation Priority | **3 × 37 = 111 cells** |
| 04 (BG col) | Owner, Quantitative Metric, Affected Stakeholders, Status, Risk if not met | **5 × 5 = 25 cells** |
| 05 (§9 row) | Article, Topic, Sub-Domains, Obligated Party, Verification Criteria, Evidence Type, Risk if not met, Posture (cur→tgt) | **8 × 54 = 432 cells** |
| 05b (resolution) | Recommended Variant, Stakeholder Impact, Risk if not resolved | **3 × 20 = 60 fields** |

**Fields explicitly excluded** (per Fase de Especificação 5 scope): Effort Estimate (FTE-weeks), Cost Estimate (€/month), Target Timeline (Q1/Q2/Q3/Q4).

---

## §4 Validation

### §4.1 Lint status

**6/6 PASS** — see `01_IMPLEMENTATION_TOOLS/lints/reports/lint_report_phase1_20260806_125633.md`.

| Lint | Status |
|------|--------|
| Company Context (38 questions) | ✅ PASSED |
| Regulatory Mapping | ✅ PASSED |
| Regulatory References (Anti-Hallucination) | ✅ PASSED |
| Regulatory Ground Truth | ✅ PASSED |
| Cross-Document Consistency | ✅ PASSED |
| Template Compliance | ✅ PASSED |

### §4.2 Completeness check

- 74 detail cards: 37 PG (§2a) + 37 SG (§3a) = **74/74 ✅**
- 4 tensions multi-paragraph (T-001..T-004) — **4/4 ✅**
- 5 docs enriched (04, 05, 05b, 07b, 07c) — **5/5 ✅**
- Doc 07b §4 table: 13 cols × 37 rows = **481/481 cells ✅**
- Doc 04 BG table: 13 cols × 5 rows = **65/65 cells ✅**
- Doc 05 §9: 8 cols × 54 rows = **432/432 cells ✅**
- Doc 05b: 20 Resolution sections × 3 fields = **60/60 fields ✅**

### §4.3 Frontmatter status

All 5 enriched docs updated:
- `status: DEEP_ENRICHED` ✅
- `sprint: 5` ✅
- `version` incremented (1.4 / 2.0 / 2.2 etc.) ✅
- `deep_enrichment_date: 2026-08-06` ✅

### §4.4 Cross-references

- Doc 07c §2a PG cards reference `phase1_ontology.yaml:clause_mappings[]` (28 GDPR clauses)
- Doc 07c §3a SG cards reference `phase1_ontology.yaml:clause_mappings[]` (26 CRA clauses)
- Doc 05 §9 references Doc 07c §2a for verification criteria
- Doc 07b §4 Risk if not met + Posture values cross-checked against Doc 04 BG table
- Doc 05b §3 Resolution sections reference corpus D-XX.Y.json sidecars

---

## §5 Corpus linkage (Fase de Especificação 5 enrichment sources)

| Source | Path | Used for |
|--------|------|----------|
| `phase1_ontology.yaml` | `02_CASES/Case_01_TinyTask_SaaS/00_COMMON/phase1_ontology.yaml` | 54 clause mappings (28 GDPR + 26 CRA); 4 tensions; sub-domain coverage |
| Corpus JSON sidecars | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Domain>/D-XX.Y/D-XX.Y.json` | HSO + Sub-SOs + fit_criterion + considerations + NIST CSF anchors |
| Doc 07b §4 | `07b_Proportionality_Profile.md` | Tier + I + example_controls per sub-domain |
| Doc 07c §2/§3 | `07c_Adjusted_Objectives.md` | PG/SG IDs + Tier + Priority per sub-domain |
| `proportionality_model.md` | `00_METHODOLOGY/REFERENCE/proportionality_model.md` | Track B tier definitions + invariant |
| Phase 2 legacy `09_Strategic_Tensions_Report.md` + `10_Privacy_Security_Goals.md` | `02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES/` | T-001..T-004 IDs preserved |

**No corpus files modified** is read-only against the corpus.

---

## §6 Files inventory (Fase de Especificação 5 deliverables)

| File | Status | Sprint role |
|------|--------|-------------|
| `07c_Adjusted_Objectives.md` | DEEP_ENRICHED v2.0 | 74 detail cards + 4 tension expansions |
| `07b_Proportionality_Profile.md` | DEEP_ENRICHED v1.4 | §4 table 10→13 cols |
| `04_Company_Context_Assessment.md` | DEEP_ENRICHED v2.2 | BG table 7→13 cols |
| `05_Regulatory_Applicability.md` | DEEP_ENRICHED v2.0 | §9 per-article 54 rows |
| `05b_Ambiguity_Register.md` | DEEP_ENRICHED v2.0 | 20 Resolution sub-sections |
| `validation/SPRINT5_REPORT.md` | NEW | This file |
| `validation/VALIDATOR_SPRINT5.md` | NEW | Self-verification report |

---

## §7 Outstanding (P7 — Human Decisions Required)

Per AEGIS Orchestrator P7 ("Human is final arbiter"), the following decisions remain **PENDING HUMAN SIGN-OFF**:

1. **PG/SG resolutions** — Doc 07c §2a / §3a status fields are all `TODO`. The 12 fields per card (Description, Verification Criteria, etc.) are Executor-generated; the CEO/CTO/DPO need to sign off on each before Phase 2 consumes them.
2. **Tension resolutions (T-001..T-004)** — Doc 07c §4 status is `AGREED` per phase1_ontology.yaml + Doc 05 §7, but formal CTO + CEO + DPO sign-off on the max-SLA routing approach (T-001 specifically) is required.
3. **Risk heuristic** — Risk if not met values in Doc 07b §4 / 04 BG / 05 §9 are Executor-derived (HIGH/MEDIUM/LOW). CTO sign-off needed.
4. **Posture targets** — Target 3/4 (MUST LIGHTWEIGHT) is heuristic; quarterly review may revise.
5. **Implementation Priority (HIGH/MEDIUM/LOW)** — Derived from MUST/SHOULD/COULD + DEFERRED status; CTO sign-off needed for actual sequencing.

---

## §8 Fase de Especificação 6 readiness

After Fase de Especificação 5 + human sign-off, Fase de Especificação 6 can:

- Promote `Status: TODO` → `IN_PROGRESS` for first batch (Doc 07c §2a PG cards with HIGH implementation priority)
- Begin Phase 2 obligations derivation (Doc 08) using Doc 07c §2a + §3a as input
- Run GATE-P proportionality eval against Doc 07b v1.4 (track B decision table remains consistent)

---

## §9 See also

- `00_METHODOLOGY/REFERENCE/proportionality_model.md` — Track B spec
- `phase1_ontology.yaml` — canonical Phase 1 facts (54 clauses, applicability, tensions)
- `validation/VALIDATOR_SPRINT5.md` — Self-verification report (PASS / CONDITIONAL_PASS / FAIL)
- `validation/SPRINT4_REPORT.md` baseline (table skeletons)
- `01_IMPLEMENTATION_TOOLS/lints/reports/lint_report_phase1_20260806_125633.md` — Lint pass evidence