---
document_id: AEGIS-DIAG-P1B-REFERENCE
title: "Phase 1B — Nuances Catalog & Analytical Reference"
phase: Filter 1/2 reference companion
version: 1.2
created: 2026-06-15
updated: 2026-07-13
status: ACTIVE
parent_diagram: phase1b_regulatory_mapping.md
source: Cross-case analysis (Docs 05, 06, 07 from all 3 cases)
related_documents:
  - phase1b_regulatory_mapping.md
  - ../filter2_domain_relevance.md
  - ../subdomain_lanes.md
  - ../../../PHASE1_STRATEGY.md
  - ../../PROMPTS/P1B-LLM-01-INTERPRETATION.md
  - ../../PROMPTS/P1B-LLM-02-RATIONALE.md
  - ../../PROMPTS/catalogs/tipo2_interpretations.yaml
  - ../../PROMPTS/catalogs/tipo3_derogations.yaml
  - ../../../PREPROCESSING/SubDomains/index.md
changes: |
  v1.2 (2026-07-13): Updated frontmatter (status CREATED → ACTIVE, version 1.2). Added Legacy ID Cross-walk and sub-domain independence note. Cross-references to PROMPTS/catalogs/ for Tipo 2/3 interpretation + derogation catalogs.
  v1.1 (2026-07-13): Bumped version + updated date + status CREATED → ACTIVE. Renamed phase from 1B to "Filter 1/2 reference companion" (3-filter alignment). Fixed parent_diagram path. Added cross-references to filter2_domain_relevance.md and subdomain_lanes.md.
changes: |
  v1.1 (2026-07-13):
  - Bumped version + updated date
  - Added cross-references to filter2_domain_relevance.md and subdomain_lanes.md (v1.1 additions)
  - Renamed phase from 1B to "Filter 1/2 reference companion" to align with 3-filter naming
---

# Phase 1B — Nuances Catalog & Analytical Reference

**Version:** 1.0 — 2026-06-15
**Companion to:** [`phase1b_regulatory_mapping.md`](phase1b_regulatory_mapping.md) (flow diagrams + LLM spec tables)
**Sources:** Docs 05, 06, 07 from Case 01, Case 02, Case 03 + Master Mapping references

---

## Overview

This file is the **reference companion** to the Phase 1B detailed flow diagrams. It contains:

1. **Doc 05 vs Doc 07 relationship analysis** — why they are not duplicative
2. **Full nuances catalog** — all 4 types × all 5 regulations, with concrete examples from the 3 case studies
3. **Master Mapping reference** — where the static clause-to-subdomain mapping lives and how it works

The flow diagrams in [`phase1b_regulatory_mapping.md`](phase1b_regulatory_mapping.md) reference nuance types and LLM reasoning points. This file provides the underlying detail.

---

## 1. Doc 05 vs Doc 07 Relationship

### 1.1 Apparent Overlap — Why It Is Not Duplication

Both Doc 05 and Doc 07 contain sections on coverage, strategic implications, and gaps. This creates the impression of duplication. In reality, they represent **different analytical perspectives** at different stages:

| Dimension | Doc 05 (Phase 1B output) | Doc 07 (Phase 1C output) |
|---|---|---|
| **Analytical lens** | Single regulation in isolation | All regulations together |
| **Coverage** | Simple YES/NO per regulation × sub-domain | Full matrix WITH NI weights, sole-authority flags, compound coverage |
| **Strategic implications** | Per-regulation observations | Synthesized architectural impact across regulations |
| **Gaps** | Per-regulation uncovered sub-domains | Aggregated gaps with severity scoring and remediation |
| **Cross-regulation analysis** | Not present | Complementarity, conflict classification, compound events |
| **Role in pipeline** | INPUT to Doc 07 | OUTPUT of Phase 1C |

### 1.2 Progression Model

```
Doc 05 (per regulation)          Doc 07 (cross-regulation)
─────────────────────            ────────────────────────
GDPR coverage matrix      ─┐
CRA coverage matrix        ├──→  Consolidated coverage matrix
NIS 2 coverage matrix      │     (NI-weighted, with overlap %)
DORA coverage matrix       │
AI Act coverage matrix    ─┘

GDPR strategic implic.    ─┐
CRA strategic implic.      ├──→  Synthesized implications
NIS 2 strategic implic.    │     (compound obligations, shared controls)
DORA strategic implic.     │
AI Act strategic implic.   ┘

GDPR gaps                 ─┐
CRA gaps                   ├──→  Aggregated gaps
NIS 2 gaps                 │     (severity + remediation roadmap)
DORA gaps                  │
AI Act gaps               ─┘

                              ┌──→  Cross-regulation overlap (§5)
                              │     Complementarity opportunities
                              │     Conflict classification
                              │     Compound event scenarios
                              └──→  [NEW — not in Doc 05]
```

### 1.3 What Doc 07 Adds (Genuinely New Analysis)

| Analysis | Description | Why Doc 05 Cannot Do This |
|---|---|---|
| **Overlap percentage** | For each pair of regulations, what % of sub-domains are shared | Requires comparing multiple regulations simultaneously |
| **Complementarity** | Where one implementation satisfies multiple regulations | Requires cross-regulation synthesis |
| **Conflict classification** | Synergistic (aligned requirements) vs Structural Tension (contradictory timelines) vs Contextual Tension (depends on company context) | Requires comparing requirement semantics across regulations |
| **Compound events** | Incident scenarios that trigger multiple regulations simultaneously (e.g., a CRA vulnerability disclosure that is also a GDPR breach and a DORA ICT incident) | Requires reasoning across regulatory boundaries |
| **Sole-authority identification** | Sub-domains covered by only ONE regulation (concentration risk) | Requires the full regulation set |

### 1.4 Concrete Example

**Scenario:** TinyTask (Case 01) implements TLS encryption for data in transit.

**Doc 05 (GDPR section, §7):**
> GDPR Art. 32 requires appropriate technical measures including encryption in transit and at rest. As TinyTask acts as both Controller (admin data) and Processor (customer data), Art. 32 applies natively to both roles. Implementation: TLS 1.3 for all API traffic, AES-256 for data at rest.

**Doc 05 (CRA section, §7):**
> CRA Art. 13(2) requires products to be delivered without known exploitable vulnerabilities. Encryption implementation must not introduce vulnerabilities (e.g., weak cipher suites). Product Class Default requires self-declaration of conformity.

**Doc 07 (§5 Complementarity, §6 Implications):**
> GDPR Art. 32 and CRA Art. 13(2) create a **complementary requirement** for encryption: GDPR drives the "what" (encryption required) while CRA drives the "how" (no exploitable vulnerabilities in implementation). A single cryptographic implementation that satisfies TLS 1.3 (GDPR-appropriate) with FIPS-validated libraries (CRA-secure) satisfies both regulations. **Estimated effort reduction: 40%** vs implementing separately.

The progression is clear: Doc 05 states the per-regulation requirement. Doc 07 synthesizes them into a single implementation recommendation with effort savings.

---

## 2. Nuances Catalog

### Overview

Regulatory nuances are interpretation-level factors that affect how articles apply to a specific company. They do NOT change the clause-to-subdomain mapping (which is static) — they change **which clauses apply**, **how they apply**, and **what concrete values they require**.

Four types, each handled at a different point in the Phase 1B flow:

| Type | Name | Flow Step | Handler | Effect |
|---|---|---|---|---|
| Tipo 1 | Classification | Step 3 | Deterministic lookup | Determines which clause subset applies |
| Tipo 2 | Interpretation | Step 4 | P1B-LLM-01-INTERPRETATION | Determines how specific articles apply |
| Tipo 3 | Derogation | Step 4 | P1B-LLM-01-INTERPRETATION | Determines exceptions and sector-specific rules |
| Tipo 4 | Threshold | Step 5 | Deterministic lookup | Determines concrete quantitative values |

---

### 2.1 Tipo 1: Classification Nuances

Classification determines which **sub-category** of a regulation applies to the company. This happens once per regulation, immediately after applicability is confirmed.

| Regulation | Classification | Options | How Determined | Impact on Clause Scope |
|---|---|---|---|---|
| **CRA** | Product Class | Default · Important I · Important II · Critical | Intended use + vulnerability profile | Default: self-declaration only. Important I: internal conformity + EU declaration. Important II: notified body involvement. Critical: EU technical assessment required |
| **AI Act** | Risk Level | Prohibited · High-risk · GPAI · Limited · Minimal | Use case (Annex III) + product type (Annex II) + capabilities | Prohibited: ban. High-risk: full Ch. 3 requirements (Arts. 8-17). GPAI: transparency (Arts. 53-55). Limited: disclosure (Art. 50). Minimal: no specific obligations |
| **NIS 2** | Entity Type | Essential · Important · Third-party Supplier | Sector (Annex I/II) + size thresholds | Essential: stricter obligations, ENISA reporting. Important: standard obligations. Supplier: obligations flow through contractual chain |
| **GDPR** | Role | Controller · Processor · Both | Who determines purposes/means vs who processes on behalf | Controller: full obligations. Processor: Art. 28 + Art. 32 + Art. 33(2). Both: full obligations for controller data + processor obligations for customer data |
| **DORA** | Entity Scope | Financial Entity · ICT Third-Party Provider | Art. 2(1) definition vs ICT service provider | Financial Entity: full scope (all chapters). ICT Third-Party: Chapter V only (oversight regime) |

**Classification is deterministic:** The company facts from Doc 04 (sector, size, product type, data types, roles) map to exactly one classification per regulation. No interpretation needed — the criteria are defined in the regulation itself.

---

### 2.2 Tipo 2: Interpretation Nuances

Interpretation nuances determine **how** a specific article applies. These require cross-referencing the regulation text with implementing acts, delegated acts, and guidance documents. This is why Step 4 is an LLM reasoning task (`P1B-LLM-01-INTERPRETATION`).

| Regulation | Article/Provision | Nuance | Source | Impact |
|---|---|---|---|---|
| **DORA** | Art. 19 (incident reporting) | Deadlines (4h/72h/1m) come from RTS JC 2024-33, not Art. 19 itself. Art. 19 says "without undue delay" — the RTS specifies exact hours | RTS JC 2024-33, Art. 18-20 | Must implement 3-stage reporting with RTS deadlines, not a single "undue delay" notification |
| **CRA** | Art. 14 (vulnerability & incident reporting) | Two distinct reporting flows: Art. 14(1) vulnerabilities/compliance issues (24h notification) vs Art. 14(3) security incidents (1 month report) | Art. 14(1) vs Art. 14(3) | Must implement separate workflows for vulnerability disclosure and incident reporting |
| **CRA** | Art. 15 (voluntary reporting) | Art. 15 is VOLUNTARY — commonly misattributed as mandatory. Article title literally says "voluntary reporting" | Art. 15 title + recital context | Do NOT create mandatory FRs for Art. 15. Only include if company opts in voluntarily |
| **GDPR** | Art. 32 (security of processing) | Applies to BOTH controllers AND processors natively. Text: "the controller AND the processor shall implement..." | Art. 32(1) text | Processors have NATIVE obligation for security measures, not inherited from controller |
| **GDPR** | Art. 33(2) (processor breach notification) | Processor notifies controller "without undue delay" — this is NOT the 72h deadline (that is Art. 33(1) controller to SA) | Art. 33(1) vs Art. 33(2) | Two different timelines in the same article: 72h (controller to SA) vs no-fixed-deadline (processor to controller) |
| **AI Act** | Art. 73 (serious incident reporting) | Three-tier reporting: Art. 73(1)(a) serious incident 15 days, (b) pervasive infringement 2 days, (c) global disruption 10 days | Art. 73(1)(a)(b)(c) | Three separate reporting workflows with different triggers and deadlines |
| **AI Act** | Art. 25 (responsibilities along the value chain) | Requirements apply downstream: distributors, importers, deployers all have obligations, not just the provider | Art. 25(1)-(6) | Company may have obligations as deployer even if not the provider |
| **NIS 2** | Directive (not Regulation) | NIS 2 is a Directive — member states transpose into national law. Creates national variation in implementation deadlines, sector definitions, and enforcement | Treaty on EU Functioning, Art. 288 | Must check national transposition law, not just the Directive text. Different countries may have different deadlines or scope |

---

### 2.3 Tipo 3: Derogation Nuances

Derogation nuances are sector-specific or entity-specific exceptions that modify how articles apply. These are also handled by `P1B-LLM-01-INTERPRETATION` in Step 4.

| Regulation | Derogation | Applies To | Effect | Source |
|---|---|---|---|---|
| **NIS 2** | Trust service providers: 24h initial notification instead of 72h early warning | TSPs in NIS 2 scope (DNS, TLD, cloud, data center providers that are TSPs) | Tighter deadline — 24h instead of 72h for initial early warning | Implementing Regulation (EU) 2024/2690, Art. 4 |
| **DORA** | Weekend/holiday clause: reporting deadlines roll to next business day | Most financial entities EXCEPT credit institutions with >250 employees | Relaxed deadline for small/medium entities. Large banks (>250 emp) have strict deadlines even on weekends | RTS JC 2024-33, Art. 2(3) |
| **NIS 2** | Sector-specific technical requirements (IR 2024/2690) | DNS providers, IXPs, TLD registries, cloud computing providers, data centres, MSPs | Additional technical obligations for incident handling, reporting format, and forensics. Credit institutions are NOT in this list | Implementing Regulation (EU) 2024/2690 |
| **DORA** | Lex specialis: DORA prevails over NIS 2 for financial entities | Financial entities that fall under BOTH DORA and NIS 2 | DORA ICT risk management requirements REPLACE NIS 2 cybersecurity requirements. Do NOT apply NIS 2 Art. 21 to DORA entities | DORA Art. 4 + Recital 16 |
| **AI Act** | National security exemption | AI systems developed/used solely for national security, military, defense, or public security purposes | Completely out of scope — not just modified, excluded entirely | AI Act Art. 2(2) + Recital 19-21 |
| **GDPR** | Household exemption | Processing by a natural person in the course of purely personal/household activity | Out of scope entirely | GDPR Art. 2(2)(c) |

---

### 2.4 Tipo 4: Threshold Nuances

Threshold nuances are quantitative requirements that depend on the company's classification. These are deterministic lookups in Step 5.

| Regulation | Requirement | Value | Source | Applies To |
|---|---|---|---|---|
| **CRA** | Minimum support period | 5 years or expected product lifetime (whichever shorter) | Art. 13(8) | All product classes |
| **CRA** | Security update period | 10 years or expected product lifetime (whichever shorter) | Art. 13(9) | All product classes |
| **CRA** | Vulnerability notification | 24 hours from discovery | Art. 14(1) | All product classes |
| **CRA** | Vulnerability report | 14 days from notification | Art. 14(2) | All product classes |
| **CRA** | Incident report | 1 month from awareness | Art. 14(3) | All product classes |
| **GDPR** | Breach notification to SA | 72 hours from awareness | Art. 33(1) | Controllers |
| **GDPR** | Breach notification to data subjects | Without undue delay (if high risk) | Art. 34(1) | Controllers |
| **GDPR** | Processor to controller notification | Without undue delay | Art. 33(2) | Processors |
| **NIS 2** | Early warning to CSIRT | 24 hours from awareness | Art. 23(4) | Essential + Important entities |
| **NIS 2** | Incident notification | 72 hours from early warning | Art. 23(4) | Essential + Important entities |
| **NIS 2** | Final report | 1 month from initial notification | Art. 23(4) | Essential + Important entities |
| **NIS 2** | TSP early warning (derogation) | 24 hours (replaces 72h standard) | IR 2024/2690, Art. 4 | Trust service providers only |
| **DORA** | Initial incident notification | 4 hours from classification as major ICT incident | RTS JC 2024-33, Art. 18 | Financial entities |
| **DORA** | Intermediate incident report | 72 hours from initial notification | RTS JC 2024-33, Art. 19 | Financial entities |
| **DORA** | Final incident report | 1 month from intermediate report | RTS JC 2024-33, Art. 20 | Financial entities |
| **AI Act** | Serious incident report | 15 days from awareness | Art. 73(1)(a) | High-risk AI system providers |
| **AI Act** | Pervasive infringement report | 2 days from awareness | Art. 73(1)(b) | High-risk AI system providers |
| **AI Act** | Global disruption report | 10 days from awareness | Art. 73(1)(c) | High-risk AI system providers |

---

### 2.5 Cross-Case Nuance Activation

Which nuances fire for each case study:

| Nuance | Case 01 (TinyTask) | Case 02 (SecureBorder) | Case 03 (OmniBank) |
|---|---|---|---|
| **CRA Product Class** | Default (self-declaration) | Important II (notified body) | N/A (no CRA) |
| **AI Act Risk Level** | Minimal (no specific obligations) | High-risk Annex III (biometric) | High-risk Annex III (credit scoring) |
| **NIS 2 Entity Type** | N/A | Essential (defense sector) | Essential (banking) — but DORA prevails |
| **GDPR Role** | Both (ctrl: admin, proc: customer) | Processor (gov data) + Controller (employees) | Controller |
| **DORA Entity Scope** | N/A | N/A | Financial Entity (Art. 2(1)(a)) |
| **DORA RTS deadlines** | N/A | N/A | 4h/72h/1m applies |
| **DORA lex specialis** | N/A | N/A | DORA replaces NIS 2 for ICT risk |
| **DORA weekend clause** | N/A | N/A | NOT eligible (>250 emp credit institution) |
| **NIS 2 TSP 24h derogation** | N/A | Potentially (if trust services) | N/A |
| **NIS 2 IR 2024/2690** | N/A | Check if DNS/cloud provider | N/A (credit institutions excluded) |
| **CRA Art. 14 dual flow** | Both flows apply | Both flows apply | N/A |
| **CRA Art. 15 voluntary** | Flag: do NOT create FR | Flag: do NOT create FR | N/A |
| **GDPR Art. 32 native both** | Yes — processor obligations are native | Yes — processor obligations are native | Yes (but controller only, still native) |
| **GDPR Art. 33(2) timing** | Yes — processor to controller without undue delay | Yes — processor to controller | N/A (controller only) |
| **AI Act Art. 73 3-tier** | N/A (Minimal risk) | All 3 tiers apply | All 3 tiers apply |
| **AI Act Art. 25 downstream** | N/A (Minimal risk) | Yes — deployer obligations | Yes — deployer obligations |
| **NIS 2 Directive variation** | N/A | Check national law (PT/DE/etc.) | Check national law |

**Observation:** Case 03 (OmniBank) has the most nuance interactions because it falls under DORA + NIS 2 + AI Act + GDPR simultaneously. The DORA lex specialis rule (DORA replaces NIS 2 for ICT risk management) is particularly important — without this nuance, OmniBank would have conflicting cybersecurity requirements from two regulations.

---

## 3. Master Mapping Reference

### 3.1 Location & Structure

The Master Mapping is a **static reference** that pre-maps all 150 regulatory clauses to the 38-sub-domain taxonomy. It is NOT generated per case — it is authored once and referenced by all cases.

**Location:** `<case>/00_COMMON/02_Regulatory_Mapping_Master.md` (one per case, but content is identical across cases)

**Structure:** The Markdown file specifies an Excel workbook with 7 sheets:

| Sheet | Content | Rows (full) |
|---|---|---|
| S1: Coverage Matrix | Regulation × Sub-domain → coverage level + NI sum | 5 regs × 38 sub-domains = 190 |
| S2: Clause Inventory | Full clause list: ID, regulation, article, NI, sub-domain, obligated party, native/inherited | 150 clauses |
| S3: NI Distribution | Per regulation: Shall/Should/May counts + average NI | 5 rows |
| S4: Obligated Party Matrix | Per clause × per role (controller/processor/both × native/inherited) | 150 rows |
| S5: Coverage Gaps | Sub-domains with no clause from any regulation | ≤38 rows |
| S6: Summary Statistics | Total clauses, coverage %, sole-authority count, shared count | 1 row |
| S7: Raw Data | All clauses with all fields, no filtering | 150 rows |

**Clause counts per regulation:**

| Regulation | Articles Mapped | Clause Nodes |
|---|---|---|
| GDPR | 28 | 28 |
| CRA | 26 | 26 |
| NIS 2 | 29 | 29 |
| DORA | 38 | 38 |
| AI Act | 29 | 29 |
| **Total** | **150** | **150** |

### 3.2 Static vs Per-Case Work

The critical distinction:

| Aspect | Static (same for all cases) | Per-Case (filtered/annotated) |
|---|---|---|
| Clause-to-subdomain mapping | Yes — Article X maps to SD-Y regardless of company | No |
| NI per clause | Yes — Shall/Should/May from regulation text | No |
| Which clauses apply | No | Yes — depends on applicability (Phase 1A) |
| Which clauses are filtered out | No | Yes — depends on classification (Tipo 1) |
| Annotations (Tipos 2+3) | No | Yes — depends on company-specific interpretation |
| Concrete thresholds (Tipo 4) | No | Yes — depends on classification |

**Flow:** Master Mapping (150 clauses) → filter by applicability → filter by classification → annotate with nuances → company-specific Doc 06 Excel (subset of 150).

### 3.3 Relationship to Knowledge Graph

The Master Mapping has a direct correspondence to the AEGIS Knowledge Graph (Neo4j):

| Master Mapping Element | KG Node Type | Count |
|---|---|---|
| Each regulation | `Regulation` node | 5 |
| Each article | `Article` node | 47 |
| Each clause | `Clause` node | 150 |
| Each sub-domain | `SubDomain` node | 38 |
| Each domain | `Domain` node | 10 |
| Clause → SubDomain mapping | `MAPS_TO` relationship | 360 |

**KG integrity baseline (from AGENTS.md):**

| Check | Expected |
|---|---|
| Total Nodes | 252 |
| Total Relationships | 360 |

The Master Mapping Markdown file is the human-readable specification; the Neo4j graph is the machine-queryable representation. Both contain the same regulatory mapping data. Phase 1B work operates on the Markdown/Excel representation; Phase 2+ work can leverage the KG for Cypher queries.

---

## Summary: How to Use This File

| If you need to... | Read this section |
|---|---|
| Understand why Doc 05 and Doc 07 are not duplicative | §1 — Doc 05 vs Doc 07 Relationship |
| Know which classification applies to a company | §2.1 — Tipo 1 |
| Know how a specific article applies differently than expected | §2.2 — Tipo 2 |
| Know if a sector-specific exception applies | §2.3 — Tipo 3 |
| Know the concrete deadline or quantitative requirement | §2.4 — Tipo 4 |
| Compare which nuances fire across case studies | §2.5 — Cross-Case Activation |
| Understand the Master Mapping structure | §3.1 — Location & Structure |
| Understand what is static vs per-case | §3.2 — Static vs Per-Case |
| Connect the Master Mapping to the Knowledge Graph | §3.3 — Relationship to KG |

---

**See also:**
- [`phase1b_regulatory_mapping.md`](phase1b_regulatory_mapping.md) — Flow diagrams + LLM spec tables (companion)
- [`phase1a_context_capture.md`](phase1a_context_capture.md) — Phase 1A detailed flow (predecessor)
- [`../phase1_contextual_definition.md`](../phase1_contextual_definition.md) — Phase 1 overview (parent)
- [`../../../TEMPLATES/05_Regulatory_Applicability.md`](../../../TEMPLATES/05_Regulatory_Applicability.md) — Doc 05 template
- [`../../../TEMPLATES/06_Clause_Mapping_Matrix.md`](../../../TEMPLATES/06_Clause_Mapping_Matrix.md) — Doc 06 template
- [`../../PROMPTS/P1B-LLM-01-INTERPRETATION.md`](../../PROMPTS/P1B-LLM-01-INTERPRETATION.md) — Canonical prompt template (v1.2)
- [`../../PROMPTS/P1B-LLM-02-RATIONALE.md`](../../PROMPTS/P1B-LLM-02-RATIONALE.md) — Canonical prompt template (v1.2)
- [`../../PROMPTS/catalogs/tipo2_interpretations.yaml`](../../PROMPTS/catalogs/tipo2_interpretations.yaml) — Tipo 2 catalog (canonical, v1.2)
- [`../../PROMPTS/catalogs/tipo3_derogations.yaml`](../../PROMPTS/catalogs/tipo3_derogations.yaml) — Tipo 3 catalog (canonical, v1.2)

---

## Legacy ID Cross-walk (v1.2, 2026-07-13)

| Legacy | Canonical | Invocation | Function |
|---|---|---|---|
| LLM-A | `P1B-LLM-01-INTERPRETATION` | per_regulation | Per-regulation interpretation + derogation catalog activation |
| LLM-B | `P1B-LLM-02-RATIONALE` | per_regulation | Per-regulation synthesis (rationale + implications + gaps merged) |
| LLM-C | (merged into P1B-LLM-02) | per_regulation | Eliminated — merged with LLM-B/D for single-call synthesis |
| LLM-D | (merged into P1B-LLM-02) | per_regulation | Eliminated — merged with LLM-B/C for single-call synthesis |

## Sub-domain independence (v1.2)

The 4 nuance types (Classification / Interpretation / Derogation / Threshold) are classified at the Regulatory Baseline in `SubDomains/D-XX.Y.md §2 HSO`. Phase 1B invokes `P1B-LLM-01-INTERPRETATION` per applicable_reg to activate Tipo 2 (interpretation) and Tipo 3 (derogation) entries against company facts. Tipo 1 (classification) and Tipo 4 (threshold) are deterministic lookups computed upstream by Filter 1.

The deterministic catalogs `PROMPTS/catalogs/tipo2_interpretations.yaml` and `PROMPTS/catalogs/tipo3_derogations.yaml` replace the prior LLM-A reasoning with bit-exact lookups; `P1B-LLM-01` becomes a narrow validator LLM that cross-checks the lookup output against the regulation text.
