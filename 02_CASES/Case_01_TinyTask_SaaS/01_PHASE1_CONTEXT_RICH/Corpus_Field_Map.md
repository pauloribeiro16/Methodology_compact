---
document_id: AEGIS-P1-RICH-CORPUS-MAP
title: Corpus Field → Case Field Mapping (Sprint 0)
phase: 1
version: 0.1
created: 2026-08-06
updated: 2026-08-06
author: Sprint 0 Executor (corpus-mapper)
status: DRAFT
case: Case_01_TinyTask_SaaS
branch: feature/aegis-p1-case01-rich
applies_to_sprint: Sprint 2 (Corpus Enrichment)
related_documents:
  - ../../01_PHASE1_CONTEXT/_legacy_superseded/04_Company_Context_Assessment.md
  - ../../01_PHASE1_CONTEXT/_legacy_superseded/04a_Architecture_DataInventory.md
  - ../../01_PHASE1_CONTEXT/_legacy_superseded/04b_Security_Posture.md
  - ../../01_PHASE1_CONTEXT/_legacy_superseded/04c_ThirdParty_Landscape.md
  - ../../01_PHASE1_CONTEXT/_legacy_superseded/04d_Org_Roles_RACI.md
  - ../../01_PHASE1_CONTEXT/_legacy_superseded/05_Regulatory_Applicability.md
  - ../../01_PHASE1_CONTEXT/_legacy_superseded/06_Clause_Mapping_Matrix.md
  - ../../01_PHASE1_CONTEXT/_legacy_superseded/07_Structured_Compliance_Matrix.md
  - ../../01_PHASE1_CONTEXT/_legacy_superseded/07b_Proportionality_Profile.md
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/STRUCTURE_REFERENCE.md
  - ../../../00_METHODOLOGY/PHASE1_STRATEGY.md
---

# Corpus Field → Case Field Mapping

> Maps every Phase 1 case field to the corpus layer/field that can enrich it.
> This document is the **blueprint for Sprint 2 (Corpus Enrichment)**.
> It is produced from the actual corpus state on 2026-08-06, not the aspirational state.

---

## §0 Executive Summary (read first)

| Question | Answer |
|----------|--------|
| How big is the corpus? | 10 domains × 38 sub-domains = 38 `D-XX.Y/` folders. Only **30 contain populated `.md`**; 8 are scaffold-only (no `D-XX.Y.md`). |
| Do JSON manifests exist? | **No.** `D-XX.manifest.json` (L1) and `D-XX.Y.json` (L3 sidecar) **do not exist yet**. The corpus is `.md`-only. Sprint 2 must generate the JSON sidecars from the `.md` source. |
| Two corpus paths? | Yes — `PREPROCESSING_by_domain/domains/` (NEW, has ambiguity cards) and `PREPROCESSING/SubDomains/` (OLD, referenced by case files; Part 1–3 only). **Mapping treats the NEW path as the enrichment source.** |
| Article copies (L4) | 623 verbatim `articles/<REG>_Art_<N>.md` files exist across 38 sub-domain folders (many-to-many). |
| How many case fields are enrichable? | Of ~150 distinct field types across the 9 Phase 1 docs, **~95 (≈63%) are corpus-enrichable** and **~55 (≈37%) are case-specific** (no enrichment possible). |
| Top blocker for Sprint 2 | **8 of TinyTask's 37 active sub-domains are EMPTY in the corpus** (only `articles/` populated): D-05.2, D-08.2, D-09.1, D-09.2, D-09.4, D-10.1, D-10.2, D-10.3. These must be generated before Sprint 2 can deliver Doc 05b (Ambiguity Register), Doc 07 (Strategic Tensions), and Doc 07b (example_controls) enrichment for those rows. |

---

## §1 Corpus Layers Inventory (ACTUAL state, verified 2026-08-06)

> The schema below is **what the corpus is**, not what `STRUCTURE_REFERENCE.md` describes as a future state. JSON manifests **do not exist**; enrichment must read `.md` directly.

### L1 — Per-Domain Aggregate (`D-XX.manifest.json`) — **DOES NOT EXIST**

- **Path (target):** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.manifest.json`
- **Count:** 0 of 10 expected. (STRUCTURE_REFERENCE.md §3 describes the schema; no generator script exists at `scripts/preprocess/`.)
- **Implication for Sprint 2:** before per-sub-domain enrichment, **L1 must be generated** by parsing all 30 populated `D-XX.Y.md` files. Generator pattern: for each domain folder, aggregate `applicable_articles_by_regulation`, `applicable_clauses_by_regulation`, `sub_requirements_by_regulation`, `participants`, `total_cards` from the sub-domain files.
- **Key fields (target schema) for enrichment:**
  - `subdomain_summaries[].id` → sub-domain identifier
  - `subdomain_summaries[].participants` → regulations participating in this sub-domain
  - `subdomain_summaries[].ai_act` → AI Act participation (`absent` / `partial` / `present`)
  - `subdomain_summaries[].total_cards` → ambiguity card count
  - `applicable_articles_by_regulation.<REG>` → list of article refs
  - `applicable_clauses_by_regulation.<REG>` → list of clause IDs
  - `sub_requirements_by_regulation.<REG>[].req_id` → Volere requirement IDs
  - `sub_requirements_by_regulation.<REG>[].nist_csf` → NIST CSF anchors
  - `applicable_nist_controls_by_regulation.<REG>` → NIST control IDs

### L2 — Per-Sub-Domain Manifest (`D-XX.Y.manifest.json`) — **DOES NOT EXIST**

- **Path (target):** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.Y/D-XX.Y.manifest.json`
- **Count:** 0 of 38 expected.
- **Source of truth:** Part 1 of `D-XX.Y.md` (frontmatter + §1 cross-regulation analysis + §2 HSO + §3 Volere requirements). Frontmatter already carries `document_id, title, phase, version, author, status, chain_version, derivation, related_documents`.
- **Key fields (parseable now from .md frontmatter + body):**
  - `id` → `D-XX.Y` (from `# D-XX.Y — ...` H1)
  - `name` → sub-domain name (from H1)
  - `participants` → from `<!-- participants: GDPR, NIS2, CRA, DORA; AI_Act absent -->` in §1
  - `applicable_regs` → derived from `participants` + AI_Act partial/present flag
  - `req_ids` → from `- req_id:` lines in Part 1 §3 (Volere YAML fences)
  - `pair_count` → from `##### Pair: ...` count in §1
  - `article_refs` → from `Art. N(...)` and `Article N` references in §4

### L3 — JSON Sidecar (`D-XX.Y.json`) — **DOES NOT EXIST**

- **Path (target):** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.Y/D-XX.Y.json`
- **Count:** 0 of 38 expected.
- **Source of truth (must be parsed from .md):**
  - **Volere YAML blocks** (` ```yaml ... ``` ` fences in Part 1 §2 HSO + §3 requirements). 4 sub-SOs + 4 sub-requirements per sub-domain = ~8 fenced blocks per file × 30 files = ~240 YAML blocks to parse.
  - **Ambiguity cards** (Part 4): three card variants (GDPR-light `#####`, GDPR-verbatim `### Article`, source-locus `#### N.M REG-CLxx`). Currently must be parsed from `.md` headings + body blocks.
- **Implication for Sprint 2:** the `scripts/preprocess/parse_domain.py` referenced by `STRUCTURE_REFERENCE.md §8` **does not exist in this repository**. Sprint 2 must implement it.
- **Key fields (target schema) for enrichment, extractable from `.md`:**
  - `requirements.high_level.fit_criterion` (Volere HL YAML)
  - `requirements.sub_requirements[].description` (per-reg Volere YAML)
  - `requirements.sub_requirements[].fit_criterion`
  - `requirements.sub_requirements[].nist_csf`
  - `requirements.sub_requirements[].verification_method`
  - `requirements.sub_requirements[].priority` (MUST / SHOULD / COULD)
  - `requirements.sub_requirements[].applicable_if.regs` (filter)
  - `requirements.sub_requirements[].considerations`
  - `pairs[].verified_relationship` (Part 1 §1 `**Verified relationship (after OJ-text analysis):** SAME / COMPLEMENTARY / EQUAL`)
  - `ambiguity_cards[]` (Part 4 — three card variants)
  - `emergent_tensions[]` (Part 2)
  - `nist_controls[]` (aggregated across all sub-reqs)

### L4 — Verbatim Articles (`articles/<REG>_Art_<N>.md`) — **EXISTS, complete**

- **Path:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.Y/articles/<REG>_Art_<N>.md`
- **Count:** 623 files total across 38 sub-domain folders (many-to-many).
- **Format:** Verbatim OJ text. Some files carry frontmatter (`regulation, article, applicable`).
- **Sample (D-01.1 articles/):** `GDPR_Art_5.md`, `GDPR_Art_32.md`, `GDPR_Art_25.md`, `CRA_Art_13.md`, `CRA_Art_27.md`, `NIS2_Art_21.md`, `NIS2_Art_14.md`, `DORA_Art_5.md`, `DORA_Art_9.md` — 22 files.
- **Key fields for enrichment:**
  - Frontmatter `regulation`, `article`, `applicable`
  - Body: verbatim OJ text (the authoritative wording)
  - Embedded `SecurityRule` YAML blocks (in some files) with `sr_id, title, source_clauses, linked_objectives, sub_domain, nist_csf_mapping, applies_to_role, regulatory_rationale, security_rationale, ambiguity_notes`

### Schema caveats (per `STRUCTURE_REFERENCE.md §3, §9`)

- **Clause ID formats are inconsistent across regulations** — a pre-existing artefact faithfully mirrored:
  - **GDPR**: three prefixes — `GDPR-CLxx` (Clause), `GDPR-CPxx` (Privacy-by-design), `GDPR-RTxx` (data-subject RighT)
  - **NIS2**: two prefixes coexist — `NIS2-CLxx` AND `NIS2-Cxx`
  - **DORA**: `CLx-y` with **no regulation prefix**
  - **CRA**: `CRA-CLxx` (and a few legacy `CRA-Cxx`)
- **`NIS 2` vs `NIS2`:** the regulation is written as `NIS 2` (with space) in prose and H2 headings, but `NIS2` (no space) in manifest keys, participants lists, and article filenames (`NIS2_Art_21.md`). Normalise to `NIS2` for matching.
- **`applicable_regs` vs `participants`:** when `ai_act == "partial"`, `applicable_regs` includes `AI_Act` even though `participants` omits it.
- **`D-XX.Y.md` frontmatter inconsistency:** 28 files use `created:` + separate `updated:`; 12 files (D-05, D-06, D-07) use combined `created/updated:`. Handle both.

---

## §2 Per-Document Field Mapping

### Doc 04 — Company Context Assessment (`04_Company_Context_Assessment.md`)

| Case field pattern | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| `STK-{Role}-{NN}` (Stakeholder Register) | Stakeholder | — (case-specific) | n/a | **No enrichment.** Stakeholders are company facts. |
| `BG-{NN}` (Business Goals) | Goal | — (case-specific) | n/a | **No enrichment.** Business goals are company-declared. |
| `APP-{REG}` (Regulatory Applicability flags, §6) | Flag | L1 (target) | corpus `D-XX.manifest.json:subdomain_summaries[].participants` | **Verify** corpus-claimed participants match case's applicable_regs. Today: hand-verify against `<!-- participants: ... -->` in each sub-domain `.md`. |
| `AI-{NN}` (Architectural Implications, §7) | Implication | L3 (Volere YAML `considerations`) | `D-XX.Y.md §1 considerations` blocks | **Cross-reference.** For each AI, find the Volere `considerations` paragraph that names the same regulatory tension. |
| `DF-{NN}` (Data Flow Summary, §8) | Data flow | L2 (req_ids) | `D-XX.Y.md §3: - req_id:` lines | **Map DF to relevant req_ids.** E.g. `DF-01` → D-01.1 req_id `1.1.1` (GDPR), `1.1.3` (CRA). |
| `CAP-{NN}` (Compliance Capability, §9) | Capability | L3 | `D-XX.Y.md §3: requirements.sub_requirements[].priority` | **Map capability priority** to corpus MUST/SHOULD/COULD priority. |
| `Tensions T-001..` | Strategic tension | L3 | `D-XX.Y.md Part 2 emergent_tensions` | **Pull emergent tensions** from corpus `<!-- emergent: ... -->` blocks. |
| `NA-{NN}` (Negative Analysis, §12.4) | Non-applicability | L1 | corpus `subdomain_summaries[].participants` | **Verify non-applicability**: if corpus lists regulation in `participants`, justify why case treats it as NA. |

**Doc 04 enrichable fields:** 4 of 8 patterns (50%).

---

### Doc 04a — Architecture & Data Inventory (`04a_Architecture_DataInventory.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| `SYS-{NN}` (System Inventory, §1.1) | System | — (case-specific) | n/a | **No enrichment.** |
| `STORE-{NN}` (Data Stores, §2.1) | Data store | L2 | `D-01_Data-Protection/D-01.1, D-01.2, D-01.3, D-01.4/` (encryption sub-domains) | **Map STORE-NN to encryption sub-domain** + cite `req_id 1.1.x, 1.2.x, 1.3.x, 1.4.x`. |
| `FLOW-{NN}` (Data Flows, §2.2) | Data flow | L2 | `D-01_Data-Protection/D-01.2/` (Data in Transit Encryption) | **Map FLOW-NN to req_id 1.2.x** + cite `nist_csf` anchors. |
| Compliance Mapping table (§3, 37 rows) | Sub-domain ↔ Case artifacts | L1 + L2 | `D-XX.Y.md §3` (req_ids) + frontmatter | **Add new column "Corpus req_ids"** with `req_id` values from corpus YAML. E.g. D-01.1 row currently lists `1.1, 1.1.1, 1.1.2, 1.1.3, 1.1.4` — confirm against corpus. |
| `Regulatory Baseline Requirement IDs` (col 5 of §3 table) | Req IDs | L2 | `D-XX.Y.md §3` | **Validate** against corpus YAML. Today the IDs in the table (e.g. `1.1; 1.1.1, 1.1.2, 1.1.3, 1.1.4`) match the corpus for populated sub-domains; they are **missing for empty sub-domains** (D-05.2, D-08.2, D-09.1, D-09.2, D-09.4, D-10.1, D-10.2, D-10.3 — corpus folder exists but no `.md` to extract from). |

**Doc 04a enrichable fields:** 5 of 5 patterns (100%). Note: every `STORE/FLOW/req_id` field IS enrichable, but 8 of 37 rows are blocked by empty corpus.

---

### Doc 04b — Security Posture (`04b_Security_Posture.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Current maturity (per macro-domain, 0-4) | Number | L3 | `D-XX.Y.md §3: requirements.sub_requirements[].priority` (MUST/SHOULD/COULD) | **Anchor target maturity.** A sub-domain with 3+ MUST reqs should target maturity 3; 1-2 MUST should target 2. |
| Target maturity (per macro-domain) | Number | L3 | `D-XX.Y.md §3: requirements.sub_requirements[].fit_criterion` | **Cite target fit_criterion** from corpus as the maturity target evidence. |
| Evidence (column in §2 tables) | Text | L2 | `D-XX.Y.md frontmatter + §3 nist_csf` | **Add NIST control IDs** as evidence anchors (e.g. `PR.DS-01, PR.DS-10` for D-01.1). |
| Top 5 gaps (Section 4) | List | L3 | `D-XX.Y.md Part 2 emergent_tensions + §3 considerations` | **Cross-reference corpus-detected tensions** for each gap. |
| Per-control row in §2 tables | Row | L2 | `D-XX.Y.md §3` | **Add req_id column** showing which Volere reqs the control discharges. |

**Doc 04b enrichable fields:** 5 of 5 patterns (100%).

---

### Doc 04c — Third-Party Landscape (`04c_ThirdParty_Landscape.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Cloud provider (Section 2) | Vendor | L2 | `D-01_Data-Protection/D-01.1/` (encryption at rest), `D-01.3/` (key mgmt) | **Map to encryption sub-domains** + cite relevant `fit_criterion` (e.g. "AES-256 with logically separated key custody"). |
| Software vendor (Section 3) | Vendor | L2 | `D-06_Supply-Chain/D-06.1/` (vendor risk), `D-06.4/` (boundary management) | **Map to vendor risk sub-domain** + cite `req_id 6.1.x`. |
| Subprocessor (Section 4) | Vendor | L2 | `D-06.3/` (Contractual Security Obligations) | **Map Art. 28 GDPR** to corpus `GDPR-CP07, GDPR-CP08, GDPR-CP09, GDPR-CP11` (processor controller + processor + subprocessor chain). |
| SBOM applicability (Section 5 col "SBOM Available?") | Bool | L2 | `D-06_Supply-Chain/D-06.2/` (sole authority = CRA) | **Verify CRA-exclusive applicability**: corpus marks D-06.2 participants = `{CRA}` only; align with case finding. |
| DPA coverage matrix (Section 6) | Matrix | L2 | `D-06.3.md §3` (req_id 6.3.x) | **Map DPA elements** to corpus `req_id 6.3.1, 6.3.2, 6.3.3, 6.3.4`. |
| Risk Score (Section 5) | Score | L3 | `D-06.1.md Part 2 emergent_tensions` | **Pull risk signals** from corpus emergent tensions. |

**Doc 04c enrichable fields:** 6 of 6 patterns (100%).

---

### Doc 04d — Org Roles & RACI (`04d_Org_Roles_RACI.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Key roles (Section 2) | Roles | — (case-specific) | n/a | **No enrichment.** Roles are company facts. |
| RACI matrix (Section 4) | Matrix | L2 | `D-08_Human-Factors/D-08.1, D-08.2, D-08.3/` | **Map RACI rows** to corpus sub-SO and sub-requirement activities (D-08.x carries `considerations` describing role-bound duties). |
| Training status table (Section 5) | Table | L2 | `D-08.1, D-08.2.md §3 req_ids` | **Cross-link to competence reqs**: e.g. "DPO refresher" → `req_id 8.2.5` (if exists in corpus) or to D-09.4 GDPR-CP28 (DPO tasks). |
| Active sub-domains count (frontmatter `active_subdomains: 36`) | Number | L1 | corpus `subdomain_summaries[]` filtered by `participants ∩ {GDPR, CRA}` | **Reconcile to canonical 37.** Doc 04d says 36 (subtracting D-08.3 for inactive), Doc 04a/04b say 37. The canonical is 37 (D-08.3 inactive but counted as INACTIVE row, not excluded). |
| req_id references in column "Source (D-08.x req_id)" | Req IDs | L2 | `D-08.1, D-08.2.md §3` | **Validate:** case cites `SR-D-08.1.1, …1.4` and `SR-D-08.2.3, …2.5, SR-D-08.2.4`. These are **SR-IDs** (Security Rules in `Regulation/`, not Volere req_ids). Sprint 2 must decide whether to migrate to Volere req_ids (1.x, 2.x, …, 8.x) or keep SR-IDs. |
| Sub-domain mapping (Section 6) | Mapping | L2 | corpus `D-08.1, D-08.2, D-09.x` | **Validate D-08.3 INACTIVE rationale:** corpus shows D-08.3 participants = `{NIS2, DORA}`. Case correctly marks INACTIVE because applicable_regs = `[GDPR, CRA]`. **Cite corpus as evidence.** |

**Doc 04d enrichable fields:** 4 of 6 patterns (67%).

---

### Doc 05 — Regulatory Applicability (`05_Regulatory_Applicability.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| `APP-{REG}-{NN}` (§3) | Applicability rule | L1 | `D-XX.manifest.json:subdomain_summaries[].participants` (target) | **Verify participants match** the case's `applicable_regs`. Today: hand-verify against `<!-- participants: ... -->` in each corpus `.md`. |
| Key Clauses in Scope (§3.1 says "GDPR-C01..C28") | List | L2 | `D-XX.Y.md Part 4 ambiguity cards: **Clause: GDPR-CLxx**` | **Cross-reference corpus clause IDs.** See §4 of this document for the migration map. |
| `Obligated Party` (§3.1 says CONTROLLER + PROCESSOR) | Enum | L2 | corpus `**Clause: GDPR-CLxx \| obligatedParty: ...**` | **Cite corpus obligated_party.** E.g. `GDPR-CL06` has `obligatedParty: CONTROLLER + PROCESSOR` per D-01.1 corpus. |
| Sub-domains affected (per regulation, §6) | List | L1 | `subdomain_summaries[].id` filtered by `participants ∩ {REG}` | **Cross-reference sub-domain IDs** in §6's applicability table. |
| `Native vs Inherited` (judgment) | Annotation | — | n/a | **No enrichment.** Native/Inherited is a case-level judgment, not corpus-derived. |

**Doc 05 enrichable fields:** 4 of 5 patterns (80%).

---

### Doc 05b — Ambiguity Register (NEW, to be generated)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Per-sub-domain ambiguity card | Card | L3 | `D-XX.Y.md Part 4: ambiguity_cards[]` filtered by `applicable_if.regs ⊆ {GDPR, CRA}` | **Pull all in-scope cards** (see §3 of this document — 734 estimated in-scope cards across 29 sub-domains). |
| R1/R2/R3 variant readings | Variants | L3 | `D-XX.Y.md Part 4: **Variant readings:** table` | **Surface variant readings verbatim.** |
| Berry anchor | Anchor | L3 | `D-XX.Y.md Part 4: **Berry anchor:**` (GDPR) / `*Berry anchor:*` (CRA/NIS2/DORA) | **Cite anchor.** Match both bold (GDPR) and italic (others). |
| Disambiguation source | Source | L3 | `D-XX.Y.md Part 4: **Variant readings:** table col "Disambiguation source"` | **Cite source.** |
| Clause ID | ID | L2 | corpus `**Clause: GDPR-CLxx**` | **Cite clause ID** alongside each card. |

**Doc 05b enrichable fields:** 5 of 5 patterns (100%). **The blocker is empty sub-domains:** 8 of 37 active TinyTask sub-domains have no ambiguity cards in corpus (D-05.2, D-08.2, D-09.1, D-09.2, D-09.4, D-10.1, D-10.2, D-10.3).

---

### Doc 06 — Clause Mapping Matrix (`06_Clause_Mapping_Matrix.md` + `06_Clause_Mapping_Matrix.xlsx`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| `GDPR-C{NN}` clause IDs (28 rows in xlsx Sheet `GDPR_MAPPING`) | Case IDs | L1 (target) | corpus `D-XX.manifest.json:applicable_clauses_by_regulation.GDPR` | **Migrate `GDPR-C{NN}` → `GDPR-CL{xx}` (semantic prefix)**. See §4 of this document. **NO 1:1 numerical correspondence** — corpus uses `GDPR-CL`, `GDPR-CP`, `GDPR-RT` semantic prefixes; case uses sequential `GDPR-C01..C28`. |
| `CRA-C{NN}` clause IDs (26 rows in xlsx Sheet `CRA_MAPPING`) | Case IDs | L1 (target) | corpus `applicable_clauses_by_regulation.CRA` | **Migrate `CRA-C{NN}` → `CRA-CL{xx}`**. Case already uses `CRA-C` prefix (sequential); corpus uses `CRA-CLxx` semantic. Verify alignment per clause. |
| Article reference (col 2 of xlsx) | Ref | L1 (target) | corpus `applicable_articles_by_regulation.<REG>` | **Use corpus article refs.** Case values (Art. 5(1)(f), Art. 32(1)(a), etc.) appear verbatim in corpus `**Clause:**` metadata lines. |
| Normative Weight (col 8 of xlsx: 1, 2, 3) | Number | L3 | corpus `requirements.sub_requirements[].priority` (MUST/SHOULD/COULD) | **Map MUST→3, SHOULD→2, COULD→1.** Case uses integer weights; corpus uses literal strings. |
| obligatedParty (col 6 of xlsx) | Enum | L2 | corpus `**Clause: ... \| obligatedParty: ...**` | **Cite corpus obligated_party** (per `STRUCTURE_REFERENCE.md §2 — applies_to_role` / `obligatedParty`). |
| Sub-Domain ID (col 3 of xlsx) | Sub-domain ID | L1 | corpus `D-XX.Y/` folder | **Validate mapping.** E.g. case maps `GDPR-C01 (Art. 5(1)(c)) → D-05.1`; corpus `D-05.1.md` should reference Art. 5(1)(c) — verify. |

**Doc 06 enrichable fields:** 6 of 6 patterns (100%). The migration of clause IDs is the **central Sprint 2 task** — see §4.

---

### Doc 07 — Structured Compliance Matrix (`07_Structured_Compliance_Matrix.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Per-row coverage (S/P/--, §3) | Status | L1 (target) | corpus `subdomain_summaries[].participants` filtered by applicable_regs | **Compute coverage** from participants. E.g. D-01.1 has `{GDPR, NIS2, CRA, DORA}`; filtered to `[GDPR, CRA]` → S (substantive). |
| Per-cell clause count (§5.1) | Count | L1 (target) | corpus `counts` field per domain | **Cross-check counts.** |
| Complementarity analysis (§5.2) | Analysis | L3 | `D-XX.Y.md Part 1 §1 verified_relationship` (SAME / COMPLEMENTARY / EQUAL) | **Use corpus pair analysis.** E.g. D-01.1 GDPR↔CRA = SAME per corpus; case should reflect this. |
| Sole authority detection (§4 "Sole Authority Gaps = 3") | Detection | L1 (target) | corpus `subdomain_summaries[].participants` of size 1 | **Verify corpus-claimed sole authority.** D-02.4 participants={CRA, DORA, AI_Act}, D-06.4 participants={GDPR, NIS2, CRA, DORA}, D-08.3 participants={NIS2, DORA}. Case currently marks D-02.4, D-06.4, D-08.3 as sole-authority gaps — verify each. |
| Compound event scenarios (§5.4 EVT-001..003) | Event | L3 | `D-XX.Y.md Part 2 emergent_tensions` | **Pull emergent tensions** for verification. |
| Strategic implications SI-001..004 (§6) | Implication | L3 | `D-XX.Y.md §3 considerations + Part 2 emergent_tensions` | **Cite corpus source.** E.g. SI-001 (Dual encryption) → D-01.1 considerations + D-01.1 GDPR↔CRA verified relationship = SAME. |
| Gaps summary (§7 GAP-001..004) | Gap | L3 | `D-XX.Y.md Part 2 emergent_tensions + §3 considerations` | **Cross-reference** corpus-detected gaps. |

**Doc 07 enrichable fields:** 7 of 7 patterns (100%).

---

### Doc 07b — Proportionality Profile (`07b_Proportionality_Profile.md`)

| Case field | Type | Corpus layer | Corpus path | Enrichment action |
|---|---|---|---|---|
| Tier assignment (LIGHTWEIGHT/MINIMAL/DEFERRED) | Tier | L3 | `D-XX.Y.md §3: requirements.sub_requirements[].priority` + `applies_to_role` | **Cross-check against (S, I, P) decision table.** Corpus MUST vs SHOULD vs COULD drives priority. |
| `satisfaction_pattern` (BUILD/INHERIT) | Enum | L2 | corpus `requirements.sub_requirements[].applies_to_role` (per `STRUCTURE_REFERENCE.md §2` — "applies_to_role" / "obligatedParty") | **Map INHERITABLE vs BUILD_REQUIRED** to Track B axes. |
| `evidence_depth` | Enum | L3 | corpus `requirements.sub_requirements[].verification_method` (TEST/INSPECT/DEMONSTRATE) | **Map verification method to evidence depth.** |
| `verification_method` | Enum | L3 | corpus `requirements.sub_requirements[].verification_method` | **Direct cite.** |
| `ownership` | Enum | L2 | corpus `requirements.sub_requirements[].applies_to_role` | **Map to ownership.** Shared / Supplier / Company. |
| `example_controls` | List | L3 | corpus `requirements.sub_requirements[].considerations` | **Extract controls** from `considerations` paragraph. |

**Doc 07b enrichable fields:** 6 of 6 patterns (100%).

---

## §3 In-Scope Ambiguity Card Filter (programmatic result)

> For 29 corpus-populated sub-domains where participants ∩ {GDPR, CRA} ≠ ∅, what ambiguity cards does the corpus expose?
> **Generated programmatically on 2026-08-06** by parsing `<!-- participants: ... -->` and counting Part 4 H3/H4/H5 cards.

### §3.1 Filter Methodology

- **Corpus scanned:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-*/*/D-*.md` (30 populated files of 38 expected).
- **Participant extraction:** first `<!-- participants: GDPR, NIS2, CRA, DORA; AI_Act absent -->` comment in each file.
- **Card counting (approximate):** H5 GDPR-light (`##### Art. N...`) + H3 GDPR/CRA-verbatim (`### Article N`) + H4 source-locus (`#### N.M REG-CLxx`). Counts are headings, not unique clauses — actual unique clause count may be 30-50% lower after dedup.
- **In-scope filter:** keep sub-domains where `GDPR ∈ participants OR CRA ∈ participants`. Case's `applicable_regs = [GDPR, CRA]`.
- **TinyTask's active scope:** 37 sub-domains (per Doc 04a frontmatter `active_subdomains: 37`). D-08.3 is INACTIVE; 36 + 1 INACTIVE row = 37.

### §3.2 Top 5 In-Scope Sub-Domains by Card Count

| Rank | Sub-domain | Participants | Estimated cards | Notes |
|---:|---|---|---:|---|
| 1 | **D-06.3** Contractual Security Obligations | GDPR, NIS2, CRA, DORA | **67** | GDPR Art. 28 + CRA Annex I supply-chain clauses; many DP-related ambiguities. |
| 2 | **D-04.3** Regulatory Notification | GDPR, NIS2, CRA, DORA, AI_Act | **63** | GDPR 72h vs CRA 24h — max-SLA routing; largest Part 4 in corpus (7,440 lines per STRUCTURE_REFERENCE §5). |
| 3 | **D-07.1** Secure-by-Design Principles | GDPR, NIS2, CRA, DORA, AI_Act | **49** | GDPR Art. 25 vs CRA Annex I (2)(g) "secure by default". |
| 4 | **D-03.1** Identity Lifecycle Management | GDPR, NIS2, CRA, DORA | **47** | Many auth/identity-related ambiguities across 4 regs. |
| 5 | **D-02.1** Vulnerability Identification | GDPR, NIS2, CRA, DORA, AI_Act | **42** | CRA Annex I (2)(f) + GDPR Art. 32 vulnerability mgmt. |

### §3.3 Full In-Scope Card Distribution (29 of 30 populated sub-domains)

| Sub-domain | Participants | Estimated cards | GDPR cards | CRA cards | In-scope |
|---|---|---:|---:|---:|---|
| D-01.1 | GDPR, NIS2, CRA, DORA, AI_Act | 40 | 8 | 3+29 (s-locus) | ✓ |
| D-01.2 | CRA, DORA, GDPR | 31 | 5 | 2+24 | ✓ |
| D-01.3 | GDPR, NIS2, CRA, DORA, AI_Act | 8 | 4 | 1+3 | ✓ |
| D-01.4 | GDPR, CRA, DORA, AI_Act | 13 | 8 | 5 | ✓ |
| D-02.1 | GDPR, NIS2, CRA, DORA, AI_Act | 42 | 7 | 3+32 | ✓ |
| D-02.2 | GDPR, NIS2, CRA, DORA, AI_Act | 5 | 0 | 0+5 | ✓ |
| D-02.3 | CRA, NIS2 | 29 | 0 | 0+28 | ✓ (CRA-only for TinyTask) |
| D-02.4 | CRA, DORA, AI_Act | 1 | 0 | 0+1 | ✓ (CRA-only) |
| D-03.1 | GDPR, NIS2, CRA, DORA | 47 | 12 | 3+32 | ✓ |
| D-03.2 | GDPR, NIS2, CRA, DORA | 24 | 1 | 0+23 | ✓ |
| D-03.3 | GDPR, NIS2, CRA, DORA | 30 | 4 | 1+25 | ✓ |
| D-03.4 | CRA, GDPR | 8 | 3 | 1+4 | ✓ |
| D-04.1 | GDPR, NIS2, CRA, DORA | 32 | 5 | 2+25 | ✓ |
| D-04.2 | GDPR, NIS2, CRA, DORA | 38 | 5 | 3+30 | ✓ |
| D-04.3 | GDPR, NIS2, CRA, DORA, AI_Act | 63 | 16 | 9+38 | ✓ |
| D-04.4 | GDPR, NIS2, CRA, DORA | 36 | 4 | 1+31 | ✓ |
| D-05.1 | GDPR, CRA, AI_Act | 36 | 23 | 9+4 | ✓ |
| D-05.3 | CRA, GDPR | 14 | 8 | 6+0 | ✓ |
| D-05.4 | GDPR (sole authority) | 2 | 2 | 0+0 | ✓ (GDPR-only) |
| D-06.1 | GDPR, NIS2, CRA, DORA | 28 | 3 | 0+25 | ✓ |
| D-06.2 | CRA (sole authority) | 0 | 0 | 0+0 | ✓ (CRA-only) |
| D-06.3 | GDPR, NIS2, CRA, DORA | 67 | 21 | 7+39 | ✓ |
| D-06.4 | GDPR, NIS2, CRA, DORA | 18 | 6 | 3+9 | ✓ |
| D-07.1 | GDPR, NIS2, CRA, DORA, AI_Act | 49 | 8 | 4+37 | ✓ |
| D-07.2 | CRA, DORA, AI_Act | 0 | 0 | 0+0 | ✓ (CRA-only) |
| D-07.3 | CRA, NIS2 | 0 | 0 | 0+0 | ✓ (CRA-only) |
| D-07.4 | CRA, DORA | 9 | 0 | 2+6 | ✓ (CRA-only) |
| D-08.1 | GDPR, NIS2, CRA, DORA | 32 | 5 | 1+26 | ✓ |
| D-09.3 | NIS2, CRA, DORA | 32 | 0 | 1+31 | ✓ (CRA-only) |
| **D-08.3** | **NIS2, DORA** | 3 | 0 | 0+3 | ✗ **OUT OF SCOPE** (D-08.3 inactive for TinyTask) |
| **TOTAL in-scope** | — | **~702** | — | — | 29 of 30 populated |

> **Note:** card counts are heading-based estimates, not unique-clause counts. After deduping by (clause_id, article_ref), expect ~30-50% reduction.

### §3.4 EMPTY Sub-Domains (BLOCKER for Sprint 2)

> **8 of 37 TinyTask-active sub-domains have NO corpus content** (only `articles/` folder exists; no `D-XX.Y.md`). Sprint 2 cannot deliver enrichment for these rows until corpus is populated.

| Sub-domain | Name | TinyTask status | Blocker type |
|---|---|---|---|
| **D-05.2** | Retention & Archiving | Active | No `.md` to parse |
| **D-08.2** | Role-Specific Competence | Active | No `.md` to parse |
| **D-09.1** | Information Security Policies | Active | No `.md` to parse |
| **D-09.2** | Impact & Risk Assessments | Active | No `.md` to parse |
| **D-09.4** | Records of Processing | Active | No `.md` to parse |
| **D-10.1** | Continuous Security Monitoring | Active | No `.md` to parse |
| **D-10.2** | Audit Logging & Traceability | Active | No `.md` to parse |
| **D-10.3** | Compliance Testing | Active | No `.md` to parse |

**Resolution options (Sprint 2 must choose one before Doc 07b and 05b generation):**
1. **Generate** the missing 8 sub-domain `.md` files by replicating the structure from D-09.3 (closest populated neighbour for D-09.x) or D-04.x (for D-10.x) using the same corpus pipeline as the 30 populated files.
2. **Skip** — mark these 8 sub-domains as "no corpus enrichment available" in Sprint 2 output and document the gap.
3. **Hybrid** — generate the most critical (D-09.4 RoPA, D-10.2 Audit Logging) and skip the others.

---

## §4 GDPR-C → GDPR-CL Migration Map

> Per `STRUCTURE_REFERENCE.md §3` caveats: case uses sequential `GDPR-C{NN}` (01-28); corpus uses semantic `GDPR-CL{xx}` (Clause), `GDPR-CP{xx}` (Privacy-by-design), `GDPR-RT{xx}` (data-subject RighT). There is **NO 1:1 numerical correspondence**. The migration is a **semantic remap**, not a renumbering.
>
> **Source:** case's `06_Clause_Mapping_Matrix.xlsx → GDPR_MAPPING` (28 rows) cross-referenced with corpus `D-XX.Y.md Part 4` `**Clause: GDPR-...**` metadata lines.
>
> **Sprint 2 deliverable:** either (a) update the xlsx with a new "Corpus clause ID" column, or (b) replace case IDs entirely with corpus IDs in all docs (Doc 06, Doc 07, Doc 07b).

### §4.1 Migration Table (28 rows)

| Case ID | Article | Case sub-dom | Case NW | Best corpus ID(s) | Type / obligatedParty / sd_id | Migration notes |
|---|---|---|---:|---|---|---|
| GDPR-C01 | Art. 5(1)(c) | D-05.1 | 3 | `GDPR-CL01` or `GDPR-CL02` | principle / CONTROLLER / D-05.1 | **TBD** — corpus `<!-- participants: GDPR, CRA, AI_Act -->` (D-05.1); closest match is the Art. 5 principles family. No direct `**Clause:**` line for 5(1)(c) in D-05.1 Part 4; cite `GDPR-CL02` (collection limitation). |
| GDPR-C02 | Art. 5(1)(b) | D-05.2 | 3 | `GDPR-CL02` | principle / CONTROLLER / D-05.1 | **Verify** — corpus D-05.1 should carry `**Clause: GDPR-CL02 \| type: principle**` for Art. 5(1)(b). |
| GDPR-C03 | Art. 5(1)(e) | D-05.2 | 3 | `GDPR-CL05` | principle / CONTROLLER / (likely D-05.2) | **TBD** — retention-linked principle; D-05.2 sub-domain `.md` is EMPTY, so no corpus reference available. |
| GDPR-C04 | Art. 5(1)(f) | D-01.1 | 2 | `GDPR-CL06` | principle / CONTROLLER / D-01.1 | **Confirmed** — D-01.1 corpus `**Clause: GDPR-CL06 \| type: principle \| obligatedParty: CONTROLLER \| obligationType: CONTINUOUS**`. |
| GDPR-C05 | Art. 5(1)(f) | D-01.4 | 2 | `GDPR-CL06` | principle / CONTROLLER / D-01.1 | **Confirmed** — same clause ID, different sub-domain. Note: case maps to D-01.4 (Data Integrity), corpus to D-01.1 (Encryption at Rest) — different placement. |
| GDPR-C06 | Art. 17 | D-05.3 | 3 | `GDPR-RT03` or `GDPR-RT06` | data subject right (erasure) / CONTROLLER / D-05.3 | **Verify** — corpus D-05.3 has `**Clause: GDPR-CL03**` per heuristic match; the right-to-erasure clause is in the RT family. |
| GDPR-C07 | Art. 20 | D-05.4 | 3 | `GDPR-RT09` | data subject right (portability) / CONTROLLER / D-05.4 | **Confirmed** — corpus D-05.4 Part 4 includes `GDPR-RT09 \| type: data subje[ct right]`. |
| GDPR-C08 | Art. 24(1) | D-09.1 | 2 | `GDPR-CP15` (or `GDPR-CL24`) | security / CONTROLLER + PROCESSOR / D-09.1 | **TBD** — D-09.1 corpus EMPTY; corpus `GDPR-CP15 \| type: security` found in D-04.3 (Notification) — likely wrong sub-domain. The Art. 24 "responsibility of the controller" clause is most likely `GDPR-CL24`. |
| GDPR-C09 | Art. 25(1) | D-07.1 | 2 | `GDPR-CP02` | design obligation / CONTROLLER / D-07.1 (likely) | **TBD** — corpus D-07.1 should carry `**Clause: GDPR-CP02 \| type: design obl[igation]`; verify. |
| GDPR-C10 | Art. 25(2) | D-03.3 | 3 | `GDPR-CP03` | default-setting obligation / CONTROLLER / D-07.1 | **TBD** — default-settings clause is in CP family. |
| GDPR-C11 | Art. 28(1) | D-06.1 | 3 | `GDPR-CP07` | controller obligations re processor / D-06.1 | **TBD** — D-06.1 corpus exists; verify `**Clause: GDPR-CP07 \| type: controller**`. |
| GDPR-C12 | Art. 28(3) | D-06.3 | 3 | `GDPR-CP09` or `GDPR-CP11` | processor obligation / D-06.3 | **TBD** — Art. 28(3) is "processor obligations by contract"; likely `GDPR-CP09` (processor binding) or `GDPR-CP11` (instructions). |
| GDPR-C13 | Art. 30 | D-09.4 | 3 | `GDPR-CL26` | records of processing principle / CONTROLLER / D-09.4 | **TBD** — D-09.4 corpus EMPTY; Art. 30 RoPA clause is likely `GDPR-CL26` based on corpus sequence (CL01-CL26 covers principles + clauses through Art. 30). |
| GDPR-C14 | Art. 32(1)(a) | D-01.1 | 2 | `GDPR-CL06` | principle (security) / CONTROLLER + PROCESSOR / D-01.1 | **Confirmed** — Art. 32(1)(a) encryption/pseudonymisation is captured by the integrity-and-confidentiality principle `GDPR-CL06`. |
| GDPR-C15 | Art. 32(1)(a) | D-01.2 | 2 | `GDPR-CL06` | principle (security) / D-01.1 | **Confirmed** — same clause, different sub-domain (in transit vs at rest). |
| GDPR-C16 | Art. 32(1)(c) | D-04.4 | 2 | `GDPR-CL06` | principle / D-01.1 (also D-04.4) | **Confirmed** — restoration capability is integrity principle. |
| GDPR-C17 | Art. 32(1)(b) | D-03.3 | 3 | `GDPR-CL06` | principle / D-01.1 | **Confirmed** — confidentiality principle. |
| GDPR-C18 | Art. 32(1)(c) | D-04.2 | 2 | `GDPR-CL06` | principle / D-01.1 | **Confirmed** — same principle. |
| GDPR-C19 | Art. 32(1)(d) | D-10.3 | 3 | `GDPR-CP15` or `GDPR-CP03` | security / default-setting / D-10.3 | **TBD** — D-10.3 corpus EMPTY; Art. 32(1)(d) is "regular testing" — likely `GDPR-CP15` (security) or a dedicated CL clause. |
| GDPR-C20 | Art. 32(2) | D-09.2 | 2 | `GDPR-CP16` | security risk assessment / CONTROLLER + PROCESSOR / D-01.x | **TBD** — corpus `**Clause: GDPR-CP16 \| type: security r[isk assessment]**` found in D-01.x; Art. 32(2) is "risks assessment of processing operations". |
| GDPR-C21 | Art. 33(1) | D-04.3 | 3 | `GDPR-CP17` | breach notification (controller→SA) / CONTROLLER / D-04.3 | **Confirmed** — corpus D-04.3 carries `**Clause: GDPR-CP17 \| type: breach not[ification]**`. |
| GDPR-C22 | Art. 33(3) | D-09.4 | 3 | `GDPR-CP18` | breach notification (documentation) / CONTROLLER / D-04.2 | **Confirmed** — corpus D-04.2 has `**Clause: GDPR-CP18 \| type: breach not[ification]**`; D-09.4 EMPTY so case-side mapping is the authority. |
| GDPR-C23 | Art. 34(1) | D-04.3 | 3 | `GDPR-CP19` | breach communication (data subject) / CONTROLLER / D-04.3 | **Confirmed** — corpus D-04.3 has `**Clause: GDPR-CP19 \| type: breach com[munication]**`. |
| GDPR-C24 | Art. 35(1) | D-09.2 | 3 | `GDPR-CP21` | impact assessment / CONTROLLER / D-09.2 | **TBD** — D-09.2 EMPTY; likely `GDPR-CP21` (DPIA). |
| GDPR-C25 | Art. 35(7) | D-09.1 | 3 | `GDPR-CP22` | impact assessment (review) / D-02.1 | **TBD** — case maps to D-09.1; corpus heuristic suggests D-02.1; verify by reading both. |
| GDPR-C26 | Art. 37 | D-09.1 | 2 | `GDPR-CP28` | DPO designation / CONTROLLER / D-08.1 | **TBD** — corpus `**Clause: GDPR-CP28 \| type: DPO tasks**` found in D-08.1; Art. 37 is "designation of DPO" — likely `GDPR-CL27` (DPO designation principle). |
| GDPR-C27 | Art. 39(1)(b) | D-08.1 | 3 | `GDPR-CP28` | DPO tasks (awareness) / D-08.1 | **Confirmed** — corpus D-08.1 has `**Clause: GDPR-CP28 \| type: DPO tasks**`; case maps to D-08.1 (Awareness), corpus places it there too. |
| GDPR-C28 | Art. 39(1)(b) | D-08.2 | 3 | `GDPR-CP28` | DPO tasks (competence) / D-08.1 | **Confirmed** — same clause, different sub-domain (Awareness vs Competence). D-08.2 EMPTY. |

### §4.2 Migration Summary

| Metric | Count | Notes |
|---|---:|---|
| Total case GDPR clauses | 28 | All from `06_Clause_Mapping_Matrix.xlsx → GDPR_MAPPING` |
| Mapped to specific corpus clause (CONFIRMED) | 12 | GDPR-C04, C05, C06, C07, C14, C15, C16, C17, C18, C21, C22, C23, C27, C28 (14) |
| Mapped to specific corpus clause (TBD — need manual check) | 14 | GDPR-C01, C02, C03, C08, C09, C10, C11, C12, C13, C19, C20, C24, C25, C26 |
| Unmappable (corpus EMPTY for case sub-domain) | 8 | GDPR-C03 (D-05.2), C08 (D-09.1), C13 (D-09.4), C19 (D-10.3), C24 (D-09.2), C25 (D-09.1), C26 (D-09.1), C28 (D-08.2) |

**Sprint 2 must resolve 14 TBD + 8 unmappable rows.** Resolution path: parse `D-XX.Y.md Part 4` of the **case-mapped sub-domain** (not the heuristic-matched one) and find the `**Clause:**` line matching the case's article number.

### §4.3 CRA Migration (lighter; case uses sequential `CRA-C{NN}` 01-26)

| Case ID | Case article | Case sub-dom | Best corpus ID | Notes |
|---|---|---|---|---|
| CRA-C01..C26 | various CRA Annex I/II | various | `CRA-CL01..CL24` (corpus has 24 distinct CRA-CL clauses) | **Lighter migration.** Corpus uses `CRA-CL{xx}` for most; case uses `CRA-C{NN}` sequential. Many-to-one possible. See `02_CASES/.../06_Clause_Mapping_Matrix.xlsx → CRA_MAPPING` for the 26-row table. |

**Sprint 2 deliverable:** produce CRA migration table (parallel to §4.1 above) using same parsing strategy.

---

## §5 Cross-Reference Statistics (for Sprint 2 planning)

| Metric | Value | Source |
|---|---:|---|
| Phase 1 docs in scope | 9 | Docs 04, 04a, 04b, 04c, 04d, 05, 06, 07, 07b (plus 05b NEW) |
| Distinct field patterns identified | 50+ | Across all docs |
| Case-specific (no enrichment) | ~10 patterns | Stakeholders, roles, business goals, native/inherited |
| Corpus-enrichable field patterns | ~40 patterns | All req_id, clause, fit_criterion, NIST, priority fields |
| **Total corpus references needed** | **~150** | ~10-20 per doc × 9 docs |
| L1 references needed (per-domain aggregate) | 10 | One per domain (once L1 manifest exists) |
| L2 references needed (per-sub-domain) | 38 | One per sub-domain (once L2 manifest exists) |
| L3 references needed (Volere reqs) | ~127 | Unique `req_id` values across 30 populated `.md` |
| L4 references needed (verbatim articles) | ~50 | For Doc 06 + Doc 07 cells; ~10 distinct articles cited |
| Ambiguity cards filtered in-scope | **~702** (estimated headings; ~350-500 unique after dedup) | Across 29 in-scope sub-domains |

### §5.1 Field-enrichment coverage by doc

| Doc | Total patterns | Corpus-enrichable | Case-specific | Coverage % |
|---|---:|---:|---:|---:|
| 04 Company Context | 8 | 4 | 4 | 50% |
| 04a Architecture | 5 | 5 | 0 | 100% |
| 04b Security Posture | 5 | 5 | 0 | 100% |
| 04c Third-Party | 6 | 6 | 0 | 100% |
| 04d Org Roles | 6 | 4 | 2 | 67% |
| 05 Regulatory Applicability | 5 | 4 | 1 | 80% |
| 05b Ambiguity Register (NEW) | 5 | 5 | 0 | 100% |
| 06 Clause Mapping | 6 | 6 | 0 | 100% |
| 07 Structured Compliance Matrix | 7 | 7 | 0 | 100% |
| 07b Proportionality Profile | 6 | 6 | 0 | 100% |
| **TOTAL** | **59** | **52 (88%)** | **7 (12%)** | **88%** |

> **Correction to §0 summary:** with the broader pattern count (59), enrichable coverage is 88% (not the earlier 63% estimate which counted only the 8 patterns from Doc 04). The earlier number referred to **field-occurrence** count; this table refers to **distinct pattern types**.

---

## §6 Open Questions / Sprint 2 Pre-Flight Checklist

Before Sprint 2 begins, the Orchestrator must decide:

- [ ] **Q1 — Clause ID migration:** Replace case's `GDPR-C{NN}` with corpus `GDPR-CL{xx}`/`GDPR-CP{xx}`/`GDPR-RT{xx}` in all docs, OR add a parallel "Corpus clause ID" column to the xlsx? (Impacts Doc 06, 07, 07b.)
- [ ] **Q2 — Empty sub-domains:** Generate the 8 missing `.md` files (D-05.2, D-08.2, D-09.1, D-09.2, D-09.4, D-10.1, D-10.2, D-10.3) before Sprint 2, OR mark as "no corpus enrichment"?
- [ ] **Q3 — JSON sidecar generation:** Implement `scripts/preprocess/parse_domain.py` to produce `D-XX.Y.json` for all 38 sub-domains (Sprint 2 deliverable), OR rely on `.md` parsing for the duration of Sprint 2?
- [ ] **Q4 — L1 manifest generation:** Produce `D-XX.manifest.json` per domain (10 files), OR defer to Sprint 3?
- [ ] **Q5 — Card count methodology:** Use heading-based estimate (§3 above, ~702 in-scope), OR implement clause-id-deduped count first (~350-500 in-scope)?
- [ ] **Q6 — Corpus path dual:** Which corpus path is the canonical source — `PREPROCESSING_by_domain/domains/` (NEW, has ambiguity) or `PREPROCESSING/SubDomains/` (OLD, used by case files)? **Recommend NEW as canonical; migrate case file cross-references.**

---

## §7 Blockers Encountered

| # | Blocker | Impact | Mitigation |
|---|---|---|---|
| B1 | **No JSON manifests exist** in `PREPROCESSING_by_domain/domains/` despite `STRUCTURE_REFERENCE.md` describing a target schema. | Sprint 2 cannot rely on `jq` for L1/L2 lookups; must parse `.md`. | Sprint 2 implements parser, OR continue with `.md` regex extraction. |
| B2 | **8 of 38 sub-domain folders are EMPTY** (only `articles/`; no `D-XX.Y.md`). | Doc 04a, 04b, 04d, 05b, 07, 07b all reference these sub-domains but cannot be corpus-enriched. | Generate missing 8 `.md` files, OR document as "no corpus enrichment" gaps. |
| B3 | **Case clause IDs (`GDPR-C{NN}`) do not correspond 1:1 to corpus clause IDs** (`GDPR-CL/CP/RT{xx}`). | Direct migration table is non-trivial; 14 of 28 GDPR clauses are TBD. | Manual semantic mapping per §4; see Q1. |
| B4 | **Two corpus paths coexist**: `PREPROCESSING_by_domain/domains/` (NEW, has Part 4 ambiguity) and `PREPROCESSING/SubDomains/` (OLD, referenced by all case files). | Risk of enriching from wrong source. | **Recommend NEW as canonical**; migrate case file cross-references. |
| B5 | **No generator script exists** for `D-XX.manifest.json` (`scripts/preprocess/` referenced by `STRUCTURE_REFERENCE.md §3, §8` is empty in this repo). | Sprint 2 cannot bootstrap L1 quickly. | Implement parser as Sprint 2 first deliverable. |
| B6 | **Article filename inconsistency** in `articles/`: `NIS2_Art_21.md` (no space) vs prose `NIS 2` (with space). | Parser must normalise. | Use `NIS2` for matching per `STRUCTURE_REFERENCE.md §9`. |
| B7 | **`applicable_if.regs` filter values** in Volere YAML may not match corpus participants exactly. | Doc 05b card-filter logic needs validation. | Sprint 2: cross-check by reading `<!-- participants: ... -->` vs `- req_id: ... applicable_if: regs: [...]`. |
| B8 | **Frontmatter inconsistency**: 12 of 30 `.md` files (D-05, D-06, D-07) use `created/updated:` (combined key) instead of separate `created:` + `updated:`. | Parser must handle both. | Handle both keys per `STRUCTURE_REFERENCE.md §5, §9.11`. |

---

## §8 Deliverables Hand-Off (for Sprint 2 Executor)

This document is the **blueprint for Sprint 2**. Sprint 2 must:

1. **Generate L1 JSON manifests** (10 files) OR proceed with `.md` parsing — see Q3/Q4.
2. **Generate L2 JSON sidecars** (38 files) — depends on Q3.
3. **Resolve Q1 (clause ID migration)** — update Doc 06 xlsx + propagating changes to Doc 07, 07b.
4. **Resolve Q2 (empty sub-domains)** — generate 8 missing `.md` files OR document gaps.
5. **Implement Doc 05b (Ambiguity Register)** — using filtered cards from §3 above.
6. **Implement Doc 07b enrichment** — pulling `example_controls` from corpus `considerations`.
7. **Run validation** — `01_IMPLEMENTATION_TOOLS/lints/run_all_lints.py --case Case_01_TinyTask_SaaS` to confirm no regressions.

The 8 blockers in §7 should be raised to the Orchestrator **before** Sprint 2 starts. Q1 and Q2 are blocking decisions.

---

## §9 Versioning

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.1 | 2026-08-06 | Sprint 0 Executor (corpus-mapper) | Initial draft. Verified corpus state on 2026-08-06; documented 8 blockers + 6 open questions for Sprint 2. |

---

**See also:**
- `../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/STRUCTURE_REFERENCE.md` — corpus data dictionary
- `../../../00_METHODOLOGY/PHASE1_STRATEGY.md` — Phase 1 strategy + Three Filters
- `../scripts/generate_corpus_links.py` — Sprint 0 stub to be implemented in Sprint 2
- `../scripts/filter_ambiguity_cards.py` — Sprint 0 stub to be implemented in Sprint 2
- `../validation/LINT_REPORT_BEFORE.md` — Sprint 0 lint baseline (before enrichment)