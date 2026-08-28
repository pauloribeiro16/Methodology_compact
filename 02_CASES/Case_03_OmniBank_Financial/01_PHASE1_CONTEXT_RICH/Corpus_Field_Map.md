---
document_id: AEGIS-P3-RICH-CORPUS-MAP
title: Corpus Field → Case Field Mapping (Case_03)
phase: 1
version: 0.1
created: 2026-08-06
author: Sprint 0 Executor (corpus-mapper)
status: ACTIVE
status_history:
  - { date: 2026-08-06, status: DRAFT, sprint: 0, by: 'Sprint 0 skeleton' }
  - { date: 2026-08-06, status: ACTIVE, sprint: 2, by: 'Sprint 2 corpus enrichment' }
case: Case_03_OmniBank_Financial
branch: feature/aegis-p1-case03-rich
applies_to_sprint: Sprint 2 (Corpus Enrichment)
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
corpus_root: 00_METHODOLOGY/PREPROCESSING_by_domain/domains/
tool: /tmp/extract_case03_corpus.py
related_documents:
  - ../01_PHASE1_CONTEXT_RICH/Doc03_Company_Context_Assessment.md
  - ../01_PHASE1_CONTEXT_RICH/Doc04_Architecture_DataInventory.md
  - ../01_PHASE1_CONTEXT_RICH/Doc05_Security_Posture.md
  - ../01_PHASE1_CONTEXT_RICH/Doc06_ThirdParty_Landscape.md
  - ../01_PHASE1_CONTEXT_RICH/Doc07_Org_Roles_RACI.md
  - ../01_PHASE1_CONTEXT_RICH/Doc08_Regulatory_Applicability.md
  - ../01_PHASE1_CONTEXT_RICH/Doc10_Clause_Mapping_Matrix.ods
  - ../01_PHASE1_CONTEXT_RICH/Doc12_Structured_Compliance_Matrix.md
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/STRUCTURE_REFERENCE.md
  - ../../../00_METHODOLOGY/PHASE1_STRATEGY.md
---

# Corpus Field → Case Field Mapping (Case_03)

> Maps every Phase 1 case field to the corpus layer/field that can enrich it.
> This document is the **blueprint for Sprint 2 (Corpus Enrichment)**.
> It is produced from the actual corpus state on 2026-08-06, not the aspirational state.

---

## §0 Executive Summary (read first)

| Question | Answer |
|----------|--------|
| How big is the corpus? | 10 domains × 38 sub-domains = 38 `D-XX.Y/` folders. **All 38 contain populated `.md` + `.json` sidecar + `.manifest.json`** (corpus is **COMPLETE**). |
| Do JSON manifests exist? | **YES.** 10 per-domain `D-XX.manifest.json` + 38 per-sub-domain `D-XX.Y.manifest.json` = **48 manifests**. 38 per-sub-domain `D-XX.Y.json` sidecars. |
| Article copies (L4) | **623 verbatim `articles/<REG>_Art_<N>.md`** files exist across 38 sub-domain folders (many-to-many). |
| How many case fields are enrichable? | Of ~60 distinct field types across the 10 Phase 1 docs (incl. 05b, 07b, 07c, Citation), **~52 (≈87%) are corpus-enrichable** and **~8 (≈13%) are case-specific**. |
| Active sub-domains for Case_03? | **38 / 38 (100%)** — all 5 applicable regulations (GDPR + CRA + NIS 2 + DORA + AI Act) cover every sub-domain in the taxonomy. |
| Total ambiguity cards in scope | **1490** (estimated heading counts across 38 active sub-domains). After (clause_id, article_ref) dedup, expect ~700-900 unique cards. |
| Top blocker for Sprint 1 | **Doc 06 missing `.md`** — only `.ods`/`.xlsx` exist; `lint_cross_document_consistency.py` FAILS. Sprint 1 must generate a Markdown companion. |
| Track B tier | **MAX** (5/5 regs, 38/38 sub-domains, 5000+ employees, €1.5B+ revenue). Most sub-domains get RIGOROUS depth; only D-07.4, D-08.3 get STANDARD (low clause density). |

---

## §1 Corpus Layers Inventory (ACTUAL state, verified 2026-08-06)

The corpus is **fully populated** under `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`. Verified against `STRUCTURE_REFERENCE.md §1`.

| Layer | Path | Count | Format | Query method |
|-------|------|------:|--------|--------------|
| **L1 — Domain Manifests** | `domains/D-XX_<Name>/D-XX.manifest.json` | 10 | JSON | `jq` direct |
| **L2 — Sub-domain Manifests** | `domains/D-XX_<Name>/D-XX.Y/D-XX.Y.manifest.json` | 38 | JSON | `jq` direct |
| **L3 — JSON Sidecars** | `domains/D-XX_<Name>/D-XX.Y/D-XX.Y.json` | 38 | JSON | `jq` direct |
| **L4 — Merged Markdown** | `domains/D-XX_<Name>/D-XX.Y/D-XX.Y.md` | 38 | Markdown (4-Part) | parse if needed |
| **L5 — Verbatim Articles** | `domains/D-XX_<Name>/D-XX.Y/articles/<REG>_Art_<N>.md` | 623 | Markdown | read directly |

**Total corpus linkage cells potentially added across Sprint 2 (estimate):** ~250 cells in 4 existing docs + 1490 ambiguity cards (filtered) + ~40 unique citations + 4 corpus-field-map sections.

### L1 — Per-Domain Aggregate (`D-XX.manifest.json`) — EXISTS

- **Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.manifest.json`
- **Count:** 10 of 10 ✓
- **Schema:** per `STRUCTURE_REFERENCE.md §3` — `subdomain_summaries[]`, `applicable_articles_by_regulation`, `applicable_clauses_by_regulation`, `sub_objectives_by_regulation`, `sub_requirements_by_regulation`, `applicable_nist_controls_by_regulation`, `counts`.
- **Per-domain `counts` example (D-01):** `total_cards: 108, applicable_articles_total: 45, applicable_clauses_total: 54, sub_objectives_total: 14, sub_requirements_total: 14, applicable_nist_controls_total: 26`.

### L2 — Per-Sub-Domain Manifest (`D-XX.Y.manifest.json`) — EXISTS

- **Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.Y/D-XX.Y.manifest.json`
- **Count:** 38 of 38 ✓
- **Schema (different from L1!):** `subdomain_id`, `subdomain_name`, `domain_id`, `domain_name`, `participants`, `ai_act`, `applicable_articles_by_regulation`, `applicable_clauses_by_regulation`, `sub_objectives_by_regulation`, `sub_requirements_by_regulation`, `applicable_nist_controls_by_regulation`, `counts`, `generated_at`.
- **Note:** No `subdomains[]` field at per-sub-domain level (single sub-domain per manifest). The `id` is `subdomain_id`, not `id`.

### L3 — JSON Sidecar (`D-XX.Y.json`) — EXISTS

- **Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.Y/D-XX.Y.json`
- **Count:** 38 of 38 ✓
- **Source of truth (parsed from `.md` at generation time):** Volere requirements (4 sub-reqs + 1 HL per sub-domain = 5 YAML blocks per file × 38 = ~190 YAML blocks), ambiguity cards (Part 4), pair relationships (Part 1 §1), emergent tensions (Part 2), NIST controls aggregated.
- **Implication for Sprint 2:** NO need to write a parser. All 38 sidecars are ready. Use `jq` to read fields.

### L4 — Merged Markdown (`D-XX.Y.md`) — EXISTS

- **Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.Y/D-XX.Y.md`
- **Count:** 38 of 38 ✓ (full corpus — see PR c101676)
- **Structure:** 4-Part H1 skeleton (Parts 1-4) per `STRUCTURE_REFERENCE.md §4`.
- **Use case:** Source of truth for prose (L3 is a generated snapshot — L4 is authoritative if they diverge).

### L5 — Verbatim Articles (`articles/<REG>_Art_<N>.md`) — EXISTS

- **Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.Y/articles/<REG>_Art_<N>.md`
- **Count:** 623 files (many-to-many).
- **Use case:** Doc 04c + Doc 06 + Citation_Index verbatim quotes.

### Schema caveats (per `STRUCTURE_REFERENCE.md §3, §9`)

- **Clause ID formats differ per regulation** — a pre-existing artefact faithfully mirrored:
  - **GDPR**: three prefixes — `GDPR-CLxx` (Clause), `GDPR-CPxx` (Privacy-by-design), `GDPR-RTxx` (data-subject RighT)
  - **NIS2**: two prefixes coexist — `NIS2-CLxx` AND `NIS2-Cxx`
  - **DORA**: `CLx-y` with **no regulation prefix** (e.g. `CL4-1`, `CL25-2`)
  - **CRA**: `CRA-CLxx`
- **`NIS 2` vs `NIS2`:** the regulation is written as `NIS 2` (with space) in prose and H2 headings, but `NIS2` (no space) in manifest keys, participants lists, and article filenames.
- **`applicable_regs` vs `participants`:** when `ai_act == "partial"`, `applicable_regs` includes `AI_Act` even though `participants` omits it.
- **One sub-domain (`D-08.1`) lists `'CRA (partial)'` in participants** — the parentheses indicate CRA participates tangentially; this affects filter logic.
- **Frontmatter inconsistency:** 12 files use `created/updated:` combined key (D-05, D-06, D-07). Handle both per `STRUCTURE_REFERENCE.md §9.11`.

---

## §2 Case → Corpus Field Mapping (per doc)

### Doc 04 — Company Context Assessment (`Doc03_Company_Context_Assessment.md`)

| Case field pattern | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| `STK-{Role}-{NN}` (Stakeholder Register) | Stakeholder | — (case-specific) | n/a | **No enrichment.** Stakeholders are company facts. |
| `BG-{NN}` (Business Goals) | Goal | — (case-specific) | n/a | **No enrichment.** Business goals are company-declared. |
| `APP-{REG}` (Regulatory Applicability, §6) | Flag | L1 | `D-XX.manifest.json:subdomain_summaries[].participants` | **Verify** corpus-claimed participants match case's applicable_regs. All 5 regs in case match corpus coverage (see §3.4). |
| `AI-{NN}` (Architectural Implications, §7) | Implication | L3 | `D-XX.Y.json:requirements.sub_requirements[].considerations` | **Cross-reference.** For each AI, find the Volere `considerations` paragraph naming the same regulatory tension. |
| `DF-{NN}` (Data Flow Summary, §8) | Data flow | L2 | `D-XX.Y.manifest.json:applicable_clauses_by_regulation` | **Map DF to relevant clauses.** E.g. `DF-01` (customer PII) → D-01.1, D-01.2 (encryption sub-domains) + D-05.1 (minimisation) + D-05.4 (portability). |
| `CAP-{NN}` (Compliance Capability, §9) | Capability | L3 | `D-XX.Y.json:requirements.sub_requirements[].priority` | **Map capability priority** to corpus MUST/SHOULD/COULD priority. |
| `Tensions T-001..T-004` | Strategic tension | L3 | `D-XX.Y.json:emergent_tensions[]` | **Pull emergent tensions** from corpus. Note: case's 4 tensions (T-001..T-004) are case-declared; corpus may surface more from D-04.3, D-09.2, D-09.1. |
| `NA-{NN}` (Negative Analysis) | Non-applicability | L1 | `subdomain_summaries[].participants` | **Verify non-applicability:** if corpus lists a regulation in `participants`, justify why case treats it as NA. For Case_03 (MAX), **no negatives** — all 38 sub-domains have at least one of the 5 case regs. |

**Doc 04 enrichable fields:** 4 of 8 patterns (50%). Case-specific = 4 (stakeholders, goals, capabilities-with-judgment, NAs).

---

### Doc 04a — Architecture & Data Inventory (`Doc04_Architecture_DataInventory.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| `SYS-{NN}` (System Inventory, §1.1) | System | — (case-specific) | n/a | **No enrichment.** |
| `STORE-{NN}` (Data Stores, §2.1) | Data store | L2 | `D-01_Data-Protection/D-01.1, D-01.2, D-01.3, D-01.4/` (encryption sub-domains) | **Map STORE-NN to encryption sub-domain** + cite clauses. Case_03 specifics: mainframe cores (encryption at rest D-01.1), data warehouse transit (D-01.2), KMS/HSM (D-01.3). |
| `FLOW-{NN}` (Data Flows, §2.2) | Data flow | L2 | `D-01.2/` (Data in Transit) + `D-04.3/` (Notification flows) | **Map FLOW-NN to req_id** + cite `nist_csf` anchors. |
| Compliance Mapping table (§3, 38 rows — all 38 active for Case_03) | Sub-domain ↔ Case artifacts | L1 + L2 | `D-XX.Y.manifest.json:applicable_clauses_by_regulation[REG]` + frontmatter | **Add new column "Corpus clause IDs"** with clause ID values from corpus. For MAX case, every row is populated. |
| `Regulatory Baseline Requirement IDs` (col 5 of §3 table) | Req IDs | L2 | `D-XX.Y.manifest.json:applicable_clauses_by_regulation` | **Validate** against corpus. Case_03 has 150 clauses mapped across 38 sub-domains; corpus has 1363 clauses total (across active sub-domains). Per-reg averages: GDPR 30, CRA 36, NIS 2 27, DORA 30, AI Act 15. |

**Doc 04a enrichable fields:** 5 of 5 patterns (100%). **All 38 sub-domain rows have corpus data** (no blockers — corpus is complete).

---

### Doc 04b — Security Posture (`Doc05_Security_Posture.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Current maturity (per macro-domain, 0-4) | Number | L3 | `D-XX.Y.json:requirements.sub_requirements[].priority` | **Anchor target maturity.** A sub-domain with 3+ MUST reqs should target maturity 3; 1-2 MUST should target 2. Case_03 has ISO 27001 → most sub-domains start at maturity 3. |
| Target maturity (per macro-domain) | Number | L3 | `D-XX.Y.json:requirements.sub_requirements[].fit_criterion` | **Cite target fit_criterion** from corpus. |
| Evidence (column in §2 tables) | Text | L2 | `D-XX.Y.manifest.json:nist_csf` | **Add NIST control IDs** as evidence anchors. |
| Top 5 gaps (Section 4) | List | L3 | `D-XX.Y.json:emergent_tensions[]` + `considerations` | **Cross-reference corpus-detected tensions.** |
| Per-control row in §2 tables | Row | L2 | `D-XX.Y.manifest.json:applicable_nist_controls_by_regulation` | **Add req_id column** showing which Volere reqs the control discharges. |

**Doc 04b enrichable fields:** 5 of 5 patterns (100%). Note: T-002 reference in Doc 04b is flagged in lint baseline — Sprint 1 must register T-002 in ground truth ontology.

---

### Doc 04c — Third-Party Landscape (`Doc06_ThirdParty_Landscape.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Cloud provider (Section 2) | Vendor | L2 | `D-01_Data-Protection/D-01.1/` (encryption at rest), `D-01.3/` (key mgmt) | **Map to encryption sub-domains** + cite `fit_criterion` (strong symmetric encryption, HSM-grade). |
| Software vendor (Section 3) | Vendor | L2 | `D-06_Supply-Chain/D-06.1/` (vendor risk), `D-06.4/` (boundary) | **Map to vendor risk sub-domain** + cite clauses (D-06.1 has 31 cards: GDPR-CP07/08, NIS2-C03-07, DORA-CL21-1/28-1, CRA-CL23a). |
| Subprocessor (Section 4) | Vendor | L2 | `D-06.3/` (Contractual Security Obligations, 76 cards) | **Map Art. 28 GDPR + DORA Art. 30 CTPP** to corpus clauses (D-06.3 GDPR: 21 clauses incl. GDPR-CP07/08/09/11; DORA: 15 clauses incl. CL30-1..CL30-x). |
| SBOM applicability (Section 5 col "SBOM Available?") | Bool | L2 | `D-06.2/` (CRA sole-authority — NOT in Case_03 in-scope as sole, but CRA covered) | **Verify CRA applicability**: corpus D-06.2 participants = `{CRA, NIS2}`; CRA is in scope for Case_03. |
| DPA coverage matrix (Section 6) | Matrix | L2 | `D-06.3.json:requirements.sub_requirements[]` | **Map DPA elements** to corpus clauses. |
| Risk Score (Section 5) | Score | L3 | `D-06.1.json Part 2 emergent_tensions` | **Pull risk signals** from corpus emergent tensions. |
| DORA CTPP register (Section 7 — NEW for Case_03) | Register | L2 | `D-09.3/` (Asset Inventories, 61 cards, DORA-heavy: 28 clauses) | **Map CTPP register** to corpus D-09.3 (DORA Art. 28-30 ICT third-party register). |

**Doc 04c enrichable fields:** 7 of 7 patterns (100%). **DORA CTPP register is Case_03-specific** (DORA Art. 28-30 not applicable to Case_01/C02).

---

### Doc 04d — Org Roles & RACI (`Doc07_Org_Roles_RACI.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Key roles (Section 2) | Roles | — (case-specific) | n/a | **No enrichment.** Roles are company facts. |
| RACI matrix (Section 4) | Matrix | L2 | `D-08_Human-Factors/D-08.1, D-08.2, D-08.3/` | **Map RACI rows** to corpus sub-SO and sub-requirement activities. **Case_03 note:** D-08.3 (Management Board Training) IS active for Case_03 (DORA + NIS 2 participation, 7 cards) — unlike Case_01 where it was INACTIVE. |
| Training status table (Section 5) | Table | L2 | `D-08.1, D-08.2.json:requirements.sub_requirements[]` | **Cross-link to competence reqs.** |
| Active sub-domains count (frontmatter `active_subdomains: 38`) | Number | L1 | `subdomain_summaries[]` filtered by `participants ∩ {GDPR, CRA, NIS2, DORA, AI_Act}` | **Reconcile to canonical 38.** Case_03 has ALL 38 active (MAX) — no INACTIVE rows. |
| DORA-specific roles (Section 6 — NEW for Case_03) | Roles | L2 | `D-09.1.json` (Information Security Policies, 131 cards, DORA Art. 5-16 ICT risk mgmt) | **Map DORA ICT risk roles** to corpus D-09.1 (CTO/CISO/CRO/DORA ICT Risk Officer). |
| AI Act AI Governance Lead (Section 7 — NEW for Case_03) | Roles | L2 | `D-08.2.json` (Role-Specific Competence, 33 cards, AI Act 31 clauses) | **Map AI Act Art. 14 human oversight + Art. 17 post-market** to corpus D-08.2 (AI Governance Lead). |

**Doc 04d enrichable fields:** 6 of 7 patterns (86%). Note: D-08.3 ACTIVE for Case_03 (DORA + NIS 2 participate).

---

### Doc 05 — Regulatory Applicability (`Doc08_Regulatory_Applicability.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| `APP-{REG}-{NN}` (§3) | Applicability rule | L1 | `D-XX.manifest.json:subdomain_summaries[].participants` | **Verify participants match.** Case_03: all 5 regs applicable; corpus coverage is GDPR 30/38, CRA 36/38, NIS 2 27/38, DORA 30/38, AI Act 15/38. |
| Key Clauses in Scope (§3.1, 150 clauses) | List | L2 | `D-XX.Y.manifest.json:applicable_clauses_by_regulation[REG]` | **Cross-reference corpus clause IDs** (case uses `GDPR-C01..C28` etc; corpus uses `GDPR-CLxx/CPxx/RTxx`). See §4 for migration map. |
| `Obligated Party` (§3.1) | Enum | L2 | `D-XX.Y.json:requirements.sub_requirements[].applies_to_role` | **Cite corpus obligated_party.** Case_03 roles: GDPR=C, CRA=MANUFACTURER, NIS2=ESSENTIAL_ENTITY, DORA=FINANCIAL_ENTITY, AI Act=PROVIDER (HIGH-RISK). |
| Sub-domains affected (per regulation, §6) | List | L1 | `subdomain_summaries[].id` filtered by `participants ∩ {REG}` | **Cross-reference sub-domain IDs.** |
| `Native vs Inherited` (judgment) | Annotation | — | n/a | **No enrichment.** Native/Inherited is case-level. |
| Complexity Tier (HIGH/MAX) | Annotation | — | n/a | **No enrichment.** Derived from §8 of template + case facts. **Case_03 = MAX** (5/5 regs, 38/38 sub-domains, 5000+ employees). |

**Doc 05 enrichable fields:** 4 of 6 patterns (67%).

---

### Doc 05b — Ambiguity Register (NEW for Rich) (`05b_Ambiguity_Register.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Per-sub-domain ambiguity card | Card | L3 | `D-XX.Y.json:ambiguity_cards[]` filtered by `applicable_regs ⊆ {GDPR, CRA, NIS2, DORA, AI_Act}` | **Pull all in-scope cards.** For Case_03, ALL 5 regs are applicable, so filter is no-op — all 1490 cards are in-scope (across 38 sub-domains). |
| R1/R2/R3 variant readings | Variants | L3 | `D-XX.Y.json:ambiguity_cards[].variant_readings[]` | **Surface variant readings verbatim.** |
| Berry anchor | Anchor | L3 | `D-XX.Y.json:ambiguity_cards[].berry_anchor` | **Cite anchor.** |
| Disambiguation source | Source | L3 | `D-XX.Y.json:ambiguity_cards[].disambiguation_source` | **Cite source.** |
| Clause ID | ID | L2 | corpus `D-XX.Y.json:ambiguity_cards[].clause_id` | **Cite clause ID.** |

**Doc 05b enrichable fields:** 5 of 5 patterns (100%). Total expected cards: **~1490** (all sub-domains in-scope for MAX case).

---

### Doc 06 — Clause Mapping Matrix (`Doc10_Clause_Mapping_Matrix.ods/.xlsx` — NO .md companion yet)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| 150 clause rows (case-form IDs) | Case IDs | L2 | `D-XX.Y.manifest.json:applicable_clauses_by_regulation[REG]` | **Migrate case IDs to corpus IDs.** Per-reg clause counts: GDPR 28 → corpus GDPR (30 sub-domains × ~avg); CRA 26 → corpus CRA (36); NIS 2 29 → corpus NIS 2 (27); DORA 38 → corpus DORA (30); AI Act 29 → corpus AI Act (15). **Reverse map needed.** |
| Article reference (col 2 of xlsx) | Ref | L2 | `D-XX.Y.manifest.json:applicable_articles_by_regulation[REG]` | **Use corpus article refs.** |
| Normative Weight (col 8 of xlsx: 1, 2, 3) | Number | L3 | `D-XX.Y.json:requirements.sub_requirements[].priority` | **Map MUST→3, SHOULD→2, COULD→1.** |
| obligatedParty (col 6 of xlsx) | Enum | L2 | `D-XX.Y.json:requirements.sub_requirements[].applies_to_role` | **Cite corpus obligated_party.** |
| Sub-Domain ID (col 3 of xlsx) | Sub-domain ID | L1 | `D-XX_Y/` folder | **Validate mapping.** All 150 case clauses map to corpus sub-domains (38 active). |
| DORA-specific clauses (38 in xlsx) | Clause | L2 | `D-XX.Y.manifest.json:applicable_clauses_by_regulation.DORA` (e.g. D-09.1 has 43 DORA clauses incl. CL5-1, CL6-1, etc.) | **Map DORA CL{x}-{y} → corpus clause ID.** DORA uses bare `CLx-y` format — disambiguate by parent `regulation` key. |

**Doc 06 enrichable fields:** 6 of 6 patterns (100%). **Sprint 1 blocker:** generate Markdown companion (currently only `.ods`/`.xlsx` exist).

---

### Doc 07 — Structured Compliance Matrix (`Doc12_Structured_Compliance_Matrix.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Per-row coverage (S/P/--, §3) | Status | L1 | `subdomain_summaries[].participants` filtered by applicable_regs | **Compute coverage.** For Case_03, every row is `S` (substantive) — all 5 regs applicable. |
| Per-cell clause count (§5.1) | Count | L1 | `counts` field per domain | **Cross-check counts.** |
| Complementarity analysis (§5.2) | Analysis | L3 | `D-XX.Y.json:pairs[].verified_relationship` (SAME / COMPLEMENTARY / EQUAL) | **Use corpus pair analysis.** |
| Sole authority detection (§4) | Detection | L1 | `subdomain_summaries[].participants` of size 1 | **Verify corpus-claimed sole authority.** For Case_03, sole authority (where Case's 5 regs don't cover a sub-domain's participants) is **none** — all 38 sub-domains have ≥1 of the 5 case regs. |
| Compound event scenarios (§5.4 EVT-001..003) | Event | L3 | `D-XX.Y.json:emergent_tensions[]` | **Pull emergent tensions.** |
| Strategic tensions T-001..T-004 (case-declared) | Tension | L3 | `D-XX.Y.json:emergent_tensions[]` (corpus-detected) | **Map case tensions to corpus tensions.** T-001 (Temporal, D-04.3) ↔ D-04.3 corpus emergent; T-002 (Cryptographic, D-05.3 vs D-10.2) ↔ D-05.3 + D-10.2 corpus; T-003 (Frequency Mismatch, D-09.2) ↔ D-09.2 IPSARA corpus; T-004 (Intensity Gap, D-07.1) ↔ D-07.1 corpus. **Sprint 1 must register these 4 in the ontology** (lint baseline warning). |
| Strategic implications SI-001..004 (§6) | Implication | L3 | `D-XX.Y.json:requirements.sub_requirements[].considerations` + `emergent_tensions` | **Cite corpus source.** |
| Gaps summary (§7 GAP-001..004) | Gap | L3 | `D-XX.Y.json:emergent_tensions[]` + `considerations` | **Cross-reference.** |

**Doc 07 enrichable fields:** 8 of 8 patterns (100%). **Note:** the 5 unused gaps (I-C03-01 missing 06.md; I-C03-02 T-001..T-004 ontology; I-C03-03 obligated_party values; I-C03-04 17 extra sections; I-C03-05 1 missing Doc 04 section) are Sprint 1 reconciliation targets.

---

### Doc 07b — Proportionality Profile (NEW for Rich) (`Doc13_Proportionality_Profile.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Tier assignment (LIGHTWEIGHT/STANDARD/RIGOROUS) | Tier | L3 | `D-XX.Y.json:requirements.sub_requirements[].priority` + `applies_to_role` | **Cross-check.** Case_03 = MAX = most sub-domains → RIGOROUS. D-07.4 + D-08.3 get STANDARD (low clause density). |
| `satisfaction_pattern` (BUILD/INHERIT) | Enum | L2 | `D-XX.Y.json:requirements.sub_requirements[].applies_to_role` | **Map INHERITABLE vs BUILD_REQUIRED** to Track B axes. |
| `evidence_depth` | Enum | L3 | `D-XX.Y.json:requirements.sub_requirements[].verification_method` | **Map to evidence depth.** |
| `verification_method` | Enum | L3 | `D-XX.Y.json:requirements.sub_requirements[].verification_method` | **Direct cite.** |
| `ownership` | Enum | L2 | `D-XX.Y.json:requirements.sub_requirements[].applies_to_role` | **Map to ownership.** |
| `example_controls` | List | L3 | `D-XX.Y.json:requirements.sub_requirements[].considerations` | **Extract controls** from `considerations` paragraph. |

**Doc 07b enrichable fields:** 6 of 6 patterns (100%).

---

### Doc 07c — Adjusted Objectives (NEW for Rich) (`Doc14_Adjusted_Goals.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Adjusted Privacy Goals | Goal | L3 | `D-XX.Y.json:requirements.sub_requirements[].description` | **Generate per-sub-domain privacy goals** from corpus description fields. Case_03 expected ~37 PG. |
| Adjusted Security Goals | Goal | L3 | `D-XX.Y.json:requirements.sub_requirements[].fit_criterion` | **Generate per-sub-domain security goals** from corpus fit_criteria. Case_03 expected ~37 SG. |
| Cross-references to Doc 05b ambiguities | Reference | L3 | `D-XX.Y.json:ambiguity_cards[]` | **Cite per-objective** the ambiguities that drive the adjustment. |
| DORA Art. 5-16 ICT Risk Framework mapping (NEW for Case_03) | Mapping | L3 | `D-09.1.json` (131 cards) | **Map DORA ICT Risk Framework** to corpus D-09.1 sub-requirements. |
| AI Act Art. 9-15 + Art. 17 mapping (NEW for Case_03) | Mapping | L3 | `D-07.1.json, D-08.2.json, D-09.2.json` (AI Act 31+ clauses across these) | **Map AI Act high-risk requirements** to corpus sub-domains. |

**Doc 07c enrichable fields:** 5 of 5 patterns (100%).

---

### Citation_Index.md (NEW for Rich)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Per-doc citation list | Citation | L5 | `articles/<REG>_Art_<N>.md` | **Cite verbatim article files** per Doc 04c/06/07. |
| Coverage gaps | Gap | — | n/a | **Identify under-cited (reg, ref) pairs.** |
| Coverage of GDPR Art. 28 + DORA Art. 30 | Citation | L5 | `articles/GDPR_Art_28.md, articles/DORA_Art_30.md` | **Cite processor obligations** across Doc 04c, Doc 06, Doc 07. |
| Coverage of AI Act Art. 9 + Art. 14 + Art. 17 | Citation | L5 | `articles/AI_Act_Art_*.md` | **Cite AI Act high-risk provider requirements.** |

**Citation_Index enrichable fields:** 4 of 4 patterns (100%).

---

## §3 In-Scope Ambiguity Card Filter (programmatic result)

For **Case_03 (MAX)**, all 5 regulations are applicable, so the in-scope filter is essentially "all cards in all 38 sub-domains". Filtered programmatically on 2026-08-06.

### §3.1 Filter Methodology

- **Corpus scanned:** All 38 `D-XX.Y.json` sidecars (fully populated).
- **In-scope filter:** keep sub-domains where `applicable_regs ∩ {GDPR, NIS2, CRA, DORA, AI_Act} ≠ ∅`.
- **Case_03's active scope:** **38 / 38** sub-domains (100%). D-08.3 ACTIVE (DORA + NIS 2 participate). D-07.4 ACTIVE (CRA + DORA). D-09.3 ACTIVE (CRA + DORA + NIS 2). **No INACTIVE rows for Case_03** — unlike Case_01 (D-08.3 INACTIVE) or Case_02 (D-08.3 + 3 NOT_ADDRESSED).

### §3.2 Top 20 In-Scope Sub-Domains by Card Count

| Rank | Sub-domain | Participants | Cards | Top Reg Driver | Notes |
|---:|---|---|---:|---|---|
| 1 | **D-09.1** | AI_Act, CRA, DORA, GDPR, NIS2 | **131** | DORA (43 clauses) | **Information Security Policies** — DORA Art. 5-16 ICT Risk Framework. The "Heart" of DORA compliance for Case_03. |
| 2 | **D-09.4** | AI_Act, CRA, DORA, GDPR, NIS2 | **116** | DORA (51) | **Records of Processing** — DORA Art. 17-19 incident + GDPR Art. 30 RoPA + AI Act Art. 12 records. |
| 3 | **D-04.3** | AI_Act, CRA, DORA, GDPR, NIS2 | **94** | DORA (37) | **Incident Notification & Reporting** — T-001 Temporal tension source. 4 notification timelines (GDPR 72h, NIS 2 24h, DORA 4h/24h, CRA 24h, AI Act 15d/2d/10d). |
| 4 | **D-09.2** | AI_Act, CRA, DORA, GDPR, NIS2 | **87** | DORA (33) | **Impact & Risk Assessments** — T-003 Frequency Mismatch source. DPIA + FRIA + ICT risk assessment. |
| 5 | **D-06.3** | CRA, DORA, GDPR, NIS2 | **76** | NIS2 (37) | **Contractual Security Obligations** — GDPR Art. 28 + DORA Art. 30 CTPP. |
| 6 | **D-03.1** | CRA, DORA, GDPR, NIS2 | **75** | DORA (30) | **Identity Lifecycle Management** — auth/IAM across 4 regs. |
| 7 | **D-02.1** | AI_Act, CRA, DORA, GDPR, NIS2 | **70** | DORA (29) | **Vulnerability Identification** — CRA Annex I (2)(f) + GDPR Art. 32 + DORA Art. 18 + AI Act Art. 15. |
| 8 | **D-10.1** | AI_Act, CRA, DORA, GDPR, NIS2 | **66** | DORA (30) | **Continuous Security Monitoring** — DORA Art. 10-12 + NIS 2 Art. 21. |
| 9 | **D-09.3** | CRA, DORA, NIS2 | **61** | DORA (28) + NIS 2 (29) | **Asset Inventories** — DORA Art. 28-30 CTPP register. **ACTIVE for Case_03 (not Case_01).** |
| 10 | **D-07.1** | AI_Act, CRA, DORA, GDPR, NIS2 | **53** | NIS2 (29) | **Secure-by-Design Principles** — T-004 Intensity Gap source. GDPR Art. 25 vs CRA Annex I (2)(g). |
| 11 | D-01.1 | CRA, DORA, GDPR, NIS2 | 46 | NIS2 (26) | Data at Rest Encryption |
| 12 | D-04.2 | CRA, DORA, GDPR, NIS2 | 43 | NIS2 (26) | Incident Containment & Response |
| 13 | D-04.4 | CRA, DORA, GDPR, NIS2 | 41 | NIS2 (30) | Incident Recovery & Lessons Learned |
| 14 | D-08.1 | CRA, DORA, GDPR, NIS2 | 39 | NIS2 (26) | General Security Awareness |
| 15 | D-10.3 | AI_Act, CRA, DORA, GDPR, NIS2 | 39 | NIS2 (25) | Compliance Testing |
| 16 | D-05.1 | AI_Act, CRA, GDPR | 38 | GDPR (23) | Data Minimisation |
| 17 | D-06.4 | CRA, DORA, GDPR, NIS2 | 36 | DORA (19) | Third-Party Boundary Management |
| 18 | D-03.3 | CRA, DORA, GDPR, NIS2 | 35 | NIS2 (23) | Authorisation & Least Privilege |
| 19 | D-04.1 | CRA, DORA, GDPR, NIS2 | 34 | NIS2 (24) | Incident Detection & Triage |
| 20 | D-01.2 | CRA, DORA, GDPR, NIS2 | 33 | NIS2 (23) | Data in Transit Encryption |

**Top 20 subtotal:** 1207 cards (~81% of total 1490). The remaining 18 sub-domains contribute 283 cards.

### §3.3 Sub-domain Coverage per Regulation (Case_03)

| Regulation | Sub-domains where it participates | % of 38 |
|------------|-----------------------------------:|-------:|
| **CRA** | 36 / 38 | 94.7% |
| **DORA** | 30 / 38 | 78.9% |
| **GDPR** | 30 / 38 | 78.9% |
| **NIS 2** | 27 / 38 | 71.1% |
| **AI Act** | 15 / 38 | 39.5% |

**Observation:** CRA has the broadest corpus coverage (36 sub-domains) — it's the "default" product security regulation. AI Act is narrowest (15) — only sub-domains where high-risk AI systems have obligations. **This matches the case profile:** OmniBank's OmniScore AI is the AI Act driver, covering only the AI-relevant sub-domains.

### §3.4 EMPTY Sub-Domains — NONE

For Case_03, **NO sub-domain is EMPTY in the corpus**. All 38 have populated `.md` + `.json` sidecar + `.manifest.json`. The 8-empty-sub-domains blocker that affected Case_01 (D-05.2, D-08.2, D-09.1, D-09.2, D-09.4, D-10.1, D-10.2, D-10.3) has been resolved by corpus augmentation commit c101676. **Sprint 2 has no corpus-side blockers.**

### §3.5 Strategic Tension Predictions (case-declared T-001..T-004 + corpus-detected)

| Tension | Case Declared | Corpus Sub-domain | Expected Cardinality |
|---------|--------------|-------------------|----------------------|
| **T-001** Temporal (incident reporting deadlines) | YES | D-04.3 (94 cards, 5 regs) | ~20 emergent tensions across 4 notification timelines |
| **T-002** Cryptographic Sharding (erasure vs immutable logs) | YES | D-05.3 + D-10.2 | ~10 emergent tensions on retention vs integrity |
| **T-003** Frequency Mismatch (assessment cycles) | YES | D-09.2 (87 cards) | ~15 emergent tensions on DPIA vs FRIA vs ICT risk |
| **T-004** Intensity Gap (secure-by-default standard) | YES | D-07.1 (53 cards) | ~5 emergent tensions on GDPR Art. 25 vs CRA Annex I (2)(g) |
| (corpus-detected) D-09.1 ICT Risk Framework gaps | TBD | D-09.1 (131 cards) | New emergent tensions likely — DORA Art. 5-16 heavy |
| (corpus-detected) AI Act high-risk assessment overlap | TBD | D-09.2 (87 cards, AI Act 0 clauses but present) | DPIA + FRIA overlap |

**Implication:** Case_03 likely has **more than 4 strategic tensions** (5+ predicted). Sprint 2 must surface corpus-detected ones and register them in the ontology.

---

## §4 Migration Map — Clause IDs (Case-form → Corpus-form)

Per `STRUCTURE_REFERENCE.md §3` caveats: case uses sequential `GDPR-C{NN}` (01-28); corpus uses semantic `GDPR-CL{xx}` (Clause), `GDPR-CP{xx}` (Privacy-by-design), `GDPR-RT{xx}` (data-subject RighT). There is **NO 1:1 numerical correspondence**. The migration is a **semantic remap**, not a renumbering.

### §4.1 Per-Regulation Clause Migration (Case_03 = MAX = 150 case clauses across 5 regs)

| Regulation | Case count | Case-form ID | Corpus-form ID | Migration pattern |
|------------|---:|---|---|---|
| **GDPR** | 28 | `GDPR-C01..C28` | `GDPR-CLxx` / `GDPR-CPxx` / `GDPR-RTxx` | Semantic remap. See Case_01 §4.1 for full table (reusable). |
| **CRA** | 26 | `CRA-C01..C26` | `CRA-CL01..CL24` (some legacy `CRA-Cxx`) | Mostly 1:1 if numerical, but CRA has 24 distinct CL clauses vs 26 case rows — some many-to-one. |
| **NIS 2** | 29 | `NIS2-C01..C29` | `NIS2-CLxx` AND `NIS2-Cxx` (DUAL prefixes) | Two prefixes coexist in corpus. Case must declare which to use as canonical (recommend `NIS2-CL` per `STRUCTURE_REFERENCE.md`). |
| **DORA** | 38 | `DORA-C01..C38` | `CLx-y` (NO DORA prefix) | **Disambiguate by parent `regulation` key.** Bare `CL4-1` is DORA in the case-form, but the case-form prefix `DORA-C` makes this explicit. **Highest risk of collision** — e.g. `CL17-1` appears in multiple sub-domains (D-04.1, D-07.1). |
| **AI Act** | 29 | `AIA-C01..C29` | `AI_Act-CLxx` (with `AI_Act-` prefix) | One prefix. ~15 sub-domains carry AI Act clauses (see §3.3). |

**Sprint 1 deliverable:** produce per-regulation migration tables (parallel to Case_01 §4.1 + Case_02 equivalent). For DORA, include a warning note about prefix disambiguation.

### §4.2 Migration Summary (estimates)

| Metric | Count | Notes |
|---|---:|---|
| Total case clauses (GDPR + CRA + NIS2 + DORA + AI Act) | 150 | All from `Doc10_Clause_Mapping_Matrix.xlsx` (5 sheets) |
| Corpus clauses total across active sub-domains | 1363 | Distributed: GDPR ~250, CRA ~190, NIS2 ~270, DORA ~470, AI Act ~120 (rough estimate from `clauses_per_reg` totals) |
| Many-to-one mappings expected | ~30 | DORA + CRA + GDPR + NIS 2 all reuse clause IDs across sub-domains |
| Unique (reg, clause_id) pairs | ~150 | After dedup, expect 150 unique case clauses + 50-100 corpus-only |

---

## §5 Cross-Reference Statistics (for Sprint 2 planning)

| Metric | Value | Source |
|---|---:|---|
| Phase 1 docs in scope | 11 | Docs 00, 01, 04, 04a, 04b, 04c, 04d, 05, 06, 07, 07b, 07c (plus 05b + Citation_Index = 14) |
| Distinct field patterns identified | 60+ | Across all 14 docs |
| Case-specific (no enrichment) | ~8 patterns | Stakeholders, roles, business goals, native/inherited |
| Corpus-enrichable field patterns | ~52 patterns | All req_id, clause, fit_criterion, NIST, priority fields |
| **Total corpus references needed** | **~250** | ~15-20 per doc × 11 docs |
| L1 references needed (per-domain aggregate) | 10 | One per domain |
| L2 references needed (per-sub-domain) | 38 | One per sub-domain |
| L3 references needed (Volere reqs) | ~190 | 5 YAML blocks × 38 sub-domains |
| L4 references needed (verbatim articles) | ~80 | For Doc 04c + Doc 06 + Citation + Doc 07; ~15 distinct articles cited |
| Ambiguity cards filtered in-scope | **1490** (estimated headings) | Across 38 active sub-domains; expected ~700-900 unique after (clause_id, article_ref) dedup |

### §5.1 Field-enrichment coverage by doc

| Doc | Total patterns | Corpus-enrichable | Case-specific | Coverage % |
|---|---:|---:|---:|---:|
| 00 Taxonomy Reference | 1 (manifest paths) | 1 | 0 | 100% |
| 01 Intake Form | 6 (sections) | 4 | 2 | 67% |
| 04 Company Context | 8 | 4 | 4 | 50% |
| 04a Architecture | 5 | 5 | 0 | 100% |
| 04b Security Posture | 5 | 5 | 0 | 100% |
| 04c Third-Party | 7 | 7 | 0 | 100% |
| 04d Org Roles | 7 | 6 | 1 | 86% |
| 05 Regulatory Applicability | 6 | 4 | 2 | 67% |
| 05b Ambiguity Register (NEW) | 5 | 5 | 0 | 100% |
| 06 Clause Mapping | 6 | 6 | 0 | 100% |
| 07 Structured Compliance Matrix | 8 | 8 | 0 | 100% |
| 07b Proportionality Profile | 6 | 6 | 0 | 100% |
| 07c Adjusted Objectives | 5 | 5 | 0 | 100% |
| Citation Index | 4 | 4 | 0 | 100% |
| **TOTAL** | **79** | **70 (89%)** | **9 (11%)** | **89%** |

> **Coverage by doc:** All non-context docs are 86-100% enrichable. Context docs (00, 01, 04, 05) are 50-100%. **89% overall** — highest of the 3 cases (vs Case_01 88% and Case_02 ~85%).

### §5.2 Sub-domain by clause-density (top 10 — for Track B proportionality)

| Sub-domain | Total cards | Total clauses | Per-reg clause spread | Track B depth |
|---|---:|---:|---|---|
| D-09.1 | 131 | 129 | DORA 43 / NIS2 34 / GDPR 35 / CRA 17 | RIGOROUS |
| D-09.4 | 116 | 114 | DORA 51 / NIS2 30 / GDPR 15 / CRA 18 | RIGOROUS |
| D-04.3 | 94 | 91 | DORA 37 / NIS2 22 / GDPR 16 / CRA 16 | RIGOROUS |
| D-09.2 | 87 | 86 | DORA 33 / NIS2 30 / GDPR 14 / CRA 9 | RIGOROUS |
| D-06.3 | 76 | 75 | NIS2 37 / GDPR 21 / DORA 15 / CRA 2 | RIGOROUS |
| D-03.1 | 75 | 74 | DORA 30 / NIS2 23 / GDPR 12 / CRA 9 | RIGOROUS |
| D-02.1 | 70 | 68 | DORA 29 / NIS2 27 / GDPR 7 / CRA 5 | RIGOROUS |
| D-10.1 | 66 | 65 | DORA 30 / NIS2 24 / GDPR 6 / CRA 5 | RIGOROUS |
| D-09.3 | 61 | 59 | NIS2 29 / DORA 28 / CRA 2 | RIGOROUS |
| D-07.1 | 53 | 51 | NIS2 29 / GDPR 8 / CRA 8 / DORA 6 | STANDARD (T-004 trigger) |

**Heuristic (from Case_01 + Case_02):** Sub-domains with > 50 cards AND > 50 clauses get RIGOROUS depth in Doc 05b + Doc 07b + Doc 07c. Standard depth for 30-50 cards. Lightweight for < 30 cards.

---

## §6 Case_03-Specific Track B Implications

Track B = AEGIS Track B (proportionality): scale tier (LOW / MEDIUM / HIGH / MAX) drives the depth of analysis.

| Attribute | Case_03 value | Track B tier |
|-----------|---------------|---------------|
| Applicable regulations | 5 / 5 | **MAX** (5/5 threshold) |
| Active sub-domains | 38 / 38 (100%) | **MAX** (≥ 75% threshold) |
| Employees | 5,000+ | **MAX** (> 250) |
| Revenue | > €1.5B | **MAX** (> €50M) |
| AI/ML systems | YES (OmniScore high-risk) | **MAX** (AI Act high-risk + Annex III) |
| Sector criticality | Banking (essential entity NIS 2 + DORA financial entity) | **MAX** (NIS 2 Annex I + DORA Art. 2) |
| ISO 27001 | Certified | Mature (not directly driving tier) |
| Special category data | NO (financial, not Art. 9) | — |

**MAX tier consequences:**
- All 5 regulatory blocks activated
- All 8 conditional blocks activated (B1-B8)
- All 4 interaction scans required (TC, RC, TM, NA)
- Most sub-domains → RIGOROUS depth
- Doc 07b (proportionality) just confirms MAX — no down-scaling
- 4 strategic tensions (T-001..T-004) already identified; Sprint 2 may surface 2-3 more

**Sprint 0.6 special note (per task description):** DORA ICT risk framework (Art. 5-16) gets a **dedicated sprint** (Sprint 0.6) to map Doc 04d + Doc 07b + Doc 07c to DORA's framework. This is **Case_03-specific** (DORA doesn't apply to Case_01, and Case_02 has fewer DORA obligations).

---

## §7 Blockers Encountered

| # | Blocker | Impact | Mitigation |
|---|---|---|---|
| B1 | **Doc 06 missing `.md`** — only `.ods` + `.xlsx` exist. Lint FAILS. | Sprint 1 reconciliation blocked. | Sprint 1 generates Markdown companion (parallel to xlsx) with 150 clause summary rows. |
| B2 | **T-001..T-004 not in ground-truth ontology** (4 in Doc 07 + 1 in Doc 04b). | `lint_regulatory_ground_truth.py` warns 5 times. | Sprint 1 registers the 4 tensions in the ontology, OR refactors docs to use ontology tension IDs. |
| B3 | **5 obligated_party values in `02_Regulatory_Mapping_Master.md`** map to wrong regulations (e.g. `MANUFACTURER` not valid for GDPR). | `lint_regulatory_ground_truth.py` warns 5 times. | Sprint 1 corrects the obligated_party field per row, OR updates the schema to allow cross-regulation roles (canonical obligation per cell). |
| B4 | **17 template-extras across 4 docs** flagged by `lint_template_compliance.py`. | Sprint 1 noise. | Sprint 1 registers extras as canonical OR leaves as warnings (by-design for MAX). |
| B5 | **1 missing Doc 04 section** (12/13 layered coverage). | `lint_company_context.py` warns. | Sprint 1 fills the missing section. |
| B6 | **DORA bare `CLx-y` clause IDs** in corpus (no DORA prefix). | Migration ambiguity. | Sprint 1 + Sprint 2 disambiguate by parent `regulation` key (NOT by ID string). |
| B7 | **`participants` lists `'CRA (partial)'`** for D-08.1 (one sub-domain). | Filter logic edge case. | Sprint 2 parser strips `(partial)` suffix when computing `applicable_regs` intersection. |
| B8 | **No corpus-side blockers** (all 38 sub-domains populated). | None — Sprint 2 has full corpus. | No action needed. |

---

## §8 Deliverables Hand-Off (for Sprint 1 / Sprint 2 Executor)

This document is the **blueprint for Sprint 1 (Reconciliation) + Sprint 2 (Corpus Enrichment)**.

### Sprint 1 deliverables
1. **Generate Doc 06 Markdown companion** — `Doc10_Clause_Mapping_Matrix.md` with 150-row summary table from `.xlsx`. Resolve lint cross-doc consistency.
2. **Register T-001..T-004 in ontology** — update `01_IMPLEMENTATION_TOOLS/lints/phase1/lint_regulatory_ground_truth.py` ground truth ontology OR refactor Doc 07 to use ontology tension IDs.
3. **Fix 5 obligated_party values** in `02_Regulatory_Mapping_Master.md`.
4. **Fill 1 missing Doc 04 section** (12/13 layered coverage).
5. **Run validation** — `python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_03_OmniBank_Financial"` to confirm 6/6 PASS.

### Sprint 2 deliverables
1. **Enrich 4 existing docs (04a/04b/04c/04d)** with corpus linkage cells.
2. **Fill Doc 05b (Ambiguity Register)** — top 20 sub-domains, ~1200 cards (estimated, after dedup).
3. **Fill Doc 07b (Proportionality Profile)** — 38-row per-sub-domain tier table.
4. **Fill Doc 07c (Adjusted Objectives)** — ~37 PG + ~37 SG.
5. **Fill Citation_Index.md** — verbatim article quotes for GDPR Art. 28, DORA Art. 30, AI Act Art. 9 + Art. 14 + Art. 17.
6. **Run validation** — confirm no regressions; all 6 lints still pass.

### Sprint 0.6 (DORA ICT Risk Framework dedicated sprint)
1. **Map DORA Art. 5-16** (ICT Risk Management Framework) to corpus D-09.1 (131 cards).
2. **Update Doc 04d** with DORA-specific roles (CTO, CISO, CRO, DORA ICT Risk Officer).
3. **Update Doc 07b** with DORA-specific RIGOROUS depth for D-09.1.
4. **Update Doc 07c** with DORA-specific ICT Risk objectives.

---

## §9 Versioning

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.1 | 2026-08-06 | Sprint 0 Executor (corpus-mapper) | Initial draft. Verified corpus state on 2026-08-06 (FULL corpus, 38/38 populated). Documented 8 blockers + 6 open items + per-doc enrichment map for 14 docs. |

---

## §10 Track B Case Comparison

| Case | Tier | Active sub-domains | Total cards | Total clauses | Notes |
|------|------|-------------------:|------------:|--------------:|-------|
| **Case_01 (TinyTask SaaS)** | MEDIUM | 37/38 (D-08.3 INACTIVE) | ~702 | ~140 | MICRO size; 2 regs (GDPR + CRA) |
| **Case_02 (SecureBorder Solutions)** | MEDIUM | 35/38 (D-08.3 + 3 NOT_ADDRESSED) | ~600 | ~112 | MEDIUM size; 4 regs |
| **Case_03 (OmniBank Financial)** | **MAX** | **38/38** | **1490** | **150** | **MAX size; 5 regs; banking + AI** |

**Case_03 is the maximum-completeness test:**
- All 38 sub-domains active (vs 37 for Case_01, 35 for Case_02)
- 5/5 regulations applicable (vs 2, 4)
- 2.1× more ambiguity cards than Case_01, 2.5× more than Case_02
- 5 strategic tensions (vs 4, 3)
- Banking sector: DORA + ECB supervision + ISO 27001 = highest regulatory density
- AI Act high-risk (OmniScore) = extra cross-regulation tension with GDPR (DPIA + FRIA overlap)

**This makes Case_03 the most rigorous test of the AEGIS methodology.** Sprints 2-5 will reveal whether the proportionality + corpus linkage approach scales to MAX complexity.

---

**See also:**
- `../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/STRUCTURE_REFERENCE.md` — corpus data dictionary
- `../../../00_METHODOLOGY/PHASE1_STRATEGY.md` — Phase 1 strategy + Three Filters
- `../scripts/generate_corpus_links.py` — Sprint 0 stub to be implemented in Sprint 2
- `../scripts/filter_ambiguity_cards.py` — Sprint 0 stub to be implemented in Sprint 2
- `../scripts/regenerate_ontology.py` — Sprint 0 stub to be implemented in Sprint 1 (resolve T-001..T-004)
- `../validation/LINT_REPORT_BEFORE.md` — Sprint 0 lint baseline (5/6 PASS, 1 FAIL on cross-doc consistency)
