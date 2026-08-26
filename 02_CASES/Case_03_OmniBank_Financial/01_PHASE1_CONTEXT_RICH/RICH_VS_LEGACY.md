---
document_id: AEGIS-P3-RICH-DIFF
title: Rich vs Legacy — Diff Summary (Case_03)
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-06
author: Sprint 3 Executor (diff-summary)
status: FINAL
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
sibling_of: ../01_PHASE1_CONTEXT/
sprints_complete: [0, 0.5, 0.6, 1, 2, 3]
---

# Rich vs Legacy — Diff Summary (Case_03)

> Sprint 3 final diff summary between `01_PHASE1_CONTEXT_RICH/` (corpus-enriched Rich Mode) and `01_PHASE1_CONTEXT/` (legacy Phase 1+2).
>
> This document is **the single source of truth** for "what changed when Case_03 was rebuilt as Rich Mode". Used by reviewers, future-sprint orchestrators, and cross-case comparisons.

## §1 Files Inventory

### §1.1 Per-doc comparison

| Doc | Path | Legacy (`01_PHASE1_CONTEXT/`) | Rich (`01_PHASE1_CONTEXT_RICH/`) | Diff summary |
|-----|------|-------------------------------|----------------------------------|--------------|
| 00 | `00_Taxonomy_Reference.md` | ✅ (was in `00_COMMON/`) | ✅ (placeholder → real content) | +corpus linkage (10 macro-domains) |
| 01 | `01_INTAKE_FORM.md` | ✅ | ✅ (frontmatter migrated to P3 prefix) | Identical body |
| 04 | `04_Company_Context_Assessment.md` | ✅ | ✅ (+ §13 TRACEABILITY; +DORA + AI Act + ISO 27001 sections) | +1 section (12→13) |
| 04a | `04a_Architecture_DataInventory.md` | ✅ | ✅ (38 sub-domains × corpus manifest path) | +corpus L2 manifest column |
| 04b | `04b_Security_Posture.md` | ✅ | ✅ (corpus L3 json sidecar linkage) | +corpus sub-requirements ref |
| 04c | `04c_ThirdParty_Landscape.md` | ✅ | ✅ (110+ verbatim Art. references including DORA Art. 28-30) | +DORA CTPP register (Case_03-specific) |
| 04d | `04d_Org_Roles_RACI.md` | ✅ (v1.0) | ✅ (v1.2 — Sprint 1 RECONCILED, +DORA-specific roles) | +DORA ICT Risk Officer + CRO + AI Governance Lead |
| 05 | `05_Regulatory_Applicability.md` | ✅ (4 regs) | ✅ (5/5 regs, normalization to canonical order) | +DORA + AI Act full sections |
| **05b** | `05b_Ambiguity_Register.md` | ❌ (did not exist) | ✅ (1,026 lines, 1,490 ambiguity cards) | **NEW — Rich only** |
| 06 | `06_Clause_Mapping_Matrix.md` | ❌ (only `.ods` + `.xlsx`) | ✅ (353 lines, generated from xlsx; lint blocker I-C03-01 RESOLVED) | **NEW MD companion** (xlsx preserved) |
| **06b** | `06b_DORA_ICT_Risk_Framework.md` | ❌ (did not exist) | ✅ (638 lines, 26 DORA articles, 5 tensions incl. T-005 TLPT) | **NEW — DORA-specific, Rich only** |
| 07 | `07_Structured_Compliance_Matrix.md` | ✅ (4 tensions) | ✅ (4 + T-005 tensions, by-design sections marked) | +T-005 DORA TLPT cycle tension |
| **07b** | `07b_Proportionality_Profile.md` | ❌ (did not exist) | ✅ (398 lines, 38 sub-domains × Track B MAX; §14 Sprint 3 cross-check) | **NEW — Track B MAX, Rich only** |
| 07c | `07c_Adjusted_Goals.md` | ✅ (placeholder) | ✅ (placeholder for Sprint 4 fill) | Placeholder; ready for Sprint 4 |
| **Citation** | `Citation_Index.md` | ❌ (did not exist) | ✅ (master citation registry) | **NEW — Rich only** |
| — | `phase1_ontology.yaml` | ✅ (legacy v1.0) | ✅ (Rich v1.1, +5 tensions section, obligated_party normalized) | +5 tensions, +canonical enum |
| — | `corpus_field_map.md` | ❌ (did not exist) | ✅ (500+ lines, corpus L1/L2/L3 → case fields) | **NEW — Rich only** |
| — | `Case_03_Phase1_RICH.xlsx` | ❌ (only legacy `.xlsx`) | ✅ (14 sheets parallel to legacy) | **NEW — Rich companion xlsx** |
| — | `README.md` | ✅ (legacy) | ✅ (319 lines — Sprint 0+3 update, +dashboard +navigation) | +sprint dashboard + §13 navigation |
| — | `scripts/*.py` | n/a | ✅ (3 stubs: generate_corpus_links, filter_ambiguity_cards, regenerate_ontology) | **NEW — Sprint tooling** |
| — | `validation/*.md` | n/a | ✅ (5 reports: LINT_BEFORE, LINT_AFTER_RECONCILE, SPRINT1, SPRINT2×2, SPRINT3, VALIDATOR_SPRINT3) | **NEW — sprint documentation** |

**Note: Doc 06b NEW (DORA-specific, not in legacy)** — the dedicated DORA ICT Risk Framework doc is a Case_03-specific Rich addition. It is the canonical reference for DORA Art. 5-16 → D-09.1/D-09.3/D-09.4 mapping, and it registered T-005 (DORA TLPT cycle) as a 5th strategic tension.

**Note: Doc 07c NEW (placeholder, to be filled in Sprint 4)** — `07c_Adjusted_Goals.md` is a Rich placeholder carrying the tensions-resolved narrative (T-001 max-SLA routing, T-002 cryptographic sharding, T-003 IPSARA framework, T-004 CRA-following). The full sub-SO × 38 sub-domains × 18 fields Adjusted Objectives is **deferred to Sprint 4** (per Phase 1 §8.3 Adjusted Objectives scope).

**Note: Doc 07b NEW (Track B MAX)** — `07b_Proportionality_Profile.md` is the **case instance** of the Track B Proportionality Model for OmniBank (MAX tier). 38/38 sub-domains assigned: 31 RIGOROUS + 7 STANDARD. Decision trail per `proportionality_model.md §5.1` documented row-by-row in §11; corpus provenance in §12; cross-case monotonicity check in §13; Sprint 3 corpus cross-check (14 representative rows) in §14.

## §2 Corpus Linkage Summary

| Layer | Path | Count | Used by |
|-------|------|------:|---------|
| **L1 — Domain Manifests** | `domains/D-XX_<Name>/D-XX.manifest.json` | 10 | Doc 00, Doc 04 (overview) |
| **L2 — Sub-domain Manifests** | `domains/D-XX_<Name>/D-XX.Y/D-XX.Y.manifest.json` | 38 | Doc 04a (full), Doc 04c, Doc 04d, Doc 06 (full) |
| **L3 — JSON Sidecars** | `domains/D-XX_<Name>/D-XX.Y/D-XX.Y.json` | 38 | Doc 04b, Doc 05b (1490 cards), Doc 07b (§14), Doc 07c |
| **L4 — Merged Markdown** | `domains/D-XX_<Name>/D-XX.Y/D-XX.Y.md` | 38 | Doc 04b, Doc 05b (when L3 insufficient) |
| **L5 — Verbatim Articles** | `domains/D-XX_<Name>/D-XX.Y/articles/<REG>_Art_<N>.md` | 623 | Doc 04c, Doc 06, Doc 06b, Citation_Index |

**Total corpus linkage cells added across Sprint 2 (actual):** ~250 cells in 4 existing docs + 1,490 ambiguity cards in Doc 05b + ~40 unique citations in Citation_Index + 4 corpus-field-map sections.

**Regulations applicable (Rich vs Case_02 vs Case_01):**

| Case | GDPR | CRA | NIS 2 | DORA | AI Act | Total |
|------|:----:|:---:|:-----:|:----:|:------:|:-----:|
| Case_01 (TinyTask SaaS) | ✅ | ✅ | — | — | — | 2 |
| Case_02 (SecureBorder Solutions) | ✅ | ✅ | ✅ | — | ✅ | 4 |
| **Case_03 (OmniBank Financial)** | ✅ | ✅ | ✅ | ✅ | ✅ | **5** |

## §3 Track B Distribution

Per `07b_Proportionality_Profile.md §3 Tier Assignment Summary`:

| Tier | Count | Decision-table entry |
|------|------:|----------------------|
| **RIGOROUS** | **31** | MAX + BUILD_REQUIRED + MUST (`proportionality_model.md §5.1` row MAX col BUILD_REQUIRED) |
| **STANDARD** | **7** | MAX + INHERITABLE + MUST (`proportionality_model.md §5.1` row MAX col INHERITABLE) |
| LIGHTWEIGHT | 0 | No SHOULD/COULD rows exist for Case_03 (all MUST per corpus `requirements.high_level.yaml.priority`) |
| MINIMAL | 0 | No SHOULD/COULD rows exist; §5.3 floor rule does not bind |
| DEFERRED | 0 | §5.2 — MAX + FTE > 1.0 excludes DEFERRED; also no SHOULD/COULD rows |
| **Total** | **38** | 38/38 ACTIVE sub-domains — full MAX coverage |

**Inheritability (`I`) distribution:**

| `I` | Count | Rationale |
|-----|------:|-----------|
| `BUILD_REQUIRED` | 31 | Bank owns full control programme (ISO 27001 ISMS, DORA Art. 5-16 ICT risk framework, ECB-supervised owned controls, AI Act Annex III owned governance) |
| `INHERITABLE` | 7 | Generic tooling genuinely offloads the baseline (security.txt, SBOM tooling, CIS-benchmark defaults, data lifecycle APIs) |

**STANDARD sub-domains (7):** D-02.3 (CVD static infrastructure), D-03.4 (CIS-benchmark defaults), D-05.1 (DB-level minimisation), D-05.2 (archive tooling), D-05.3 (erasure API endpoint), D-05.4 (JSON export), D-06.2 (CycloneDX in CI/CD).

## §4 DORA-specific additions

DORA (Regulation (EU) 2022/2554) is the **defining characteristic** of Case_03 — it is the only case in the AEGIS methodology where DORA applies. DORA-specific Rich additions:

1. **Doc 06b** (NEW, 638 lines) — Dedicated DORA ICT Risk Framework mapping:
   - 26 DORA articles mapped (Art. 4–30, covering governance, risk management, incident reporting, operational resilience, third-party risk)
   - 5 tensions identified:
     - **T-003** IPSARA Unified Assessment Framework (DORA Art. 6 + AI Act FRIA Art. 27 + GDPR DPIA Art. 35)
     - **T-005** DORA Art. 26-27 TLPT cycle (annual vs ECB-recognised TLPT provider cadence) — *new in Sprint 0.6*
     - 3 additional DORA-specific tensions from corpus `emergent_tensions` field
   - DORA Art. 28-30 CTPP register mandatory alignment with Doc 04c

2. **Doc 04d** (v1.2) — DORA-specific organisational roles registered:
   - CRO (Chief Risk Officer) — accountable for ICT risk
   - DORA ICT Risk Officer — entity-level DORA Art. 5 owner
   - DORA Operational Resilience Lead — DORA Art. 12 BC/DR owner
   - AI Governance Lead — AI Act + DORA Art. 5 alignment
   - DPO (existing) — GDPR Art. 37-39 alignment
   - 38 active sub-domains confirmed (D-08.3 ACTIVE under dual NIS 2 Art. 20 + DORA Art. 5(4))

3. **Doc 07b §3 Engineering rationale** — corpus `scope_overlap = N` (INHERITABLE) is GENERIC; Case_03 operational reality mandates BUILD_REQUIRED for 31 sub-domains due to ISO 27001 + DORA Art. 5-16 + ECB + AI Act Annex III.

4. **Doc 04c** — DORA Art. 28-30 CTPP register with verbatim Art. 28 + DORA Art. 30 + AI Act downstream provider references.

## §5 Lint Status

**Aggregate diff:**

| Phase | Lint status | Errors | Warnings |
|-------|-------------|-------:|---------:|
| **Legacy** (`01_PHASE1_CONTEXT/`) baseline (Sprint 0) | 5/6 PASS | 1 (cross-doc consistency FAIL — Doc 06 missing) | 29 |
| **Rich** (Sprint 1 reconciled) | 6/6 PASS | 0 | 6 |
| **Rich** (Sprint 3 final) | 6/6 PASS | 0 | 6 |

**Net effect:** −79% warnings eliminated (29 → 6). 0 errors maintained. 1 FAIL resolved (Doc 06 `.md` generated).

**Remaining 6 warnings (all non-blocking):**
- 1 × `lint_company_context.py`: "Complexity Tier regex doesn't include MAXIMUM" — lint regex limitation, not a doc issue
- 5 × `lint_template_compliance.py`: "Template not found: 00_METHODOLOGY/TEMPLATES/..." — TEMPLATES directory missing (carries over from Case_01)

## §6 Outstanding Items

| Item | Sprint target | Notes |
|------|---------------|-------|
| Doc 07c (Adjusted Objectives) full fill | Sprint 4 | Placeholder; ready for 38 sub-domains × 18 fields |
| Doc 07b §14 cross-check expansion | Optional Sprint 4 | 14 spot-checked → 38 full (Sprint 4 candidate) |
| Register 5 tensions in canonical `00_METHODOLOGY/SCHEMA/tensions.yaml` | Optional Sprint 4 | Currently case-specific registration in `phase1_ontology.yaml` |
| Migrate `02_Regulatory_Mapping_Master.md` to canonical obligated_party enum | Optional Sprint 4 | Legacy file, not in Rich folder, lint-blind |
| `run_phase1_lints.py --phase-dir` flag | Sprint 4+ tooling | Currently uses custom Python wrapper for Rich lint |
| `lint_company_context.py` regex update for MAXIMUM | Sprint 4+ tooling | Lint regex `(LOW|MEDIUM|HIGH)` → `(LOW|MEDIUM|HIGH|MAXIMUM)` |
| Provision `00_METHODOLOGY/TEMPLATES/` directory | Sprint 4+ tooling | 5 template warnings will disappear |
| Excel → MD migration decision | Sprint 4+ | Doc 06 has both `.md` (353 lines) and `.xlsx` (source of truth); consolidation candidate |

## §7 Reviewer Quick-Start

For a reviewer new to Case_03 Rich Mode, the recommended reading order is:

1. **`README.md`** (this Rich folder) — orientation, Sprint status, navigation (§13)
2. **`07b_Proportionality_Profile.md` §3 + §11** — tier distribution + decision trail (the core of Rich Mode)
3. **`06b_DORA_ICT_Risk_Framework.md` §3** — DORA-specific (the defining characteristic of Case_03)
4. **`05b_Ambiguity_Register.md` §3** — 1,490 ambiguity cards (the corpus depth)
5. **`corpus_field_map.md`** — exact corpus → case field mapping
6. **`validation/LINT_REPORT_AFTER_RECONCILE.md` §3** — lint diff (BEFORE vs AFTER)
7. **`validation/SPRINT3_REPORT.md`** — Sprint 3 completion summary
8. **`validation/VALIDATOR_SPRINT3.md`** — independent Validator verdict
9. **`PROJECT_STATE.md`** — Phase 1 Rich Mode status snapshot

For comparison with legacy, see `01_PHASE1_CONTEXT/` (frozen, read-only) and `../PROJECT_STATE.md` (legacy case-level state).

## §8 See also

- `../01_PHASE1_CONTEXT/` — legacy (read-only, Phase 1+2 complete)
- `../PROJECT_STATE.md` — legacy case-level project state
- `README.md` — Rich folder orientation
- `corpus_field_map.md` — corpus field mapping
- `phase1_ontology.yaml` v1.1 — ontology with 5 tensions
- `07b_Proportionality_Profile.md` — Track B MAX proportionality profile
- `06b_DORA_ICT_Risk_Framework.md` — DORA-specific Rich addition
- `05b_Ambiguity_Register.md` — ambiguity cards (1,490)
- `validation/SPRINT3_REPORT.md` — Sprint 3 completion
- `validation/VALIDATOR_SPRINT3.md` — Validator verdict
- `validation/LINT_REPORT_AFTER_RECONCILE.md` — lint state
- `00_METHODOLOGY/REFERENCE/proportionality_model.md` — Track B spec
- `00_METHODOLOGY/PREPROCESSING_by_domain/STRUCTURE_REFERENCE.md` — corpus structure