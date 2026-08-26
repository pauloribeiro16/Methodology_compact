---
document_id: AEGIS-P2-RICH-CORPUS-MAP
title: Corpus Field → Case Field Mapping (Case_02)
phase: 1
version: 0.1
created: 2026-08-06
author: Sprint 0 Executor (corpus-mapper)
status: ACTIVE
case: Case_02_SecureBorder_Solutions
corpus_root: 00_METHODOLOGY/PREPROCESSING/SubDomains/
tool: /tmp/extract_case02_corpus.py
applies_to: case_applicable_regs = [GDPR, NIS2, CRA, AI_Act]
active_subdomains: 35
inactive_documented: [D-08.3 INACTIVE, 3 NOT_ADDRESSED]
---

# Corpus Field → Case Field Mapping (Case_02)

## §0 Provenance & Discrepancy Note

> **Discrepancy with task description.** The task description referenced
> `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` as the corpus root, with
> counts of "48 manifests, 38 sidecars, 623 articles". In this repository the
> `PREPROCESSING_by_domain/` directory contains only `__pycache__` (compiled
> Python bytecode from prior runs); the actual corpus lives at
> **`00_METHODOLOGY/PREPROCESSING/SubDomains/`**, with 38 sub-domain `.md`
> files (one per `D-XX.X`), and manifest data embedded in YAML frontmatter
> plus an HTML `<!-- participants: ... -->` comment in the body. There are
> no separate `.json` manifest files or sidecar files. Article counts (per
> the `Regulation/<REG>/Articles/Art_N.md` split) sum to 140 across 5
> regulations (GDPR 48, DORA 30, CRA 25, AI_Act 24, NIS2 13), not 623.
> This document uses the actual corpus.

## §1 Corpus Layers Inventory

The AEGIS corpus has 4 layers per `AGA-METHOD-REG-BASELINE` (the frozen Regulatory Baseline). The Rich version of Case_02 Phase 1 reads all 4 layers from `00_METHODOLOGY/PREPROCESSING/`.

| Layer | Path | Format | What it holds |
|-------|------|--------|---------------|
| **L1 — SubDomains** | `PREPROCESSING/SubDomains/D-<XX>_<Name>/D-<XX>.<Y>.md` | 38 `.md` files, one per sub-domain | Per sub-domain: cross-reg analysis + HSO + SecurityRequirements (Volere-adapted). Frontmatter has `document_id`, `title`, `version`, `derivation`, `related_documents`. Body has `<!-- participants: ... -->` and SR-* article references. |
| **L2 — Regulation** | `PREPROCESSING/Regulation/<REG>/` | Folder per regulation (5 folders: AI_Act, CRA, DORA, GDPR, NIS2) | Per-regulation: `00_README.md`, `01_SecurityObjectives.md`, `02_SecurityRules_NIST.md`, `03_validation_report.md`, `04_deduction_audit.md`, `Articles/Art_N.md` (per-article), `Ambiguity/` (clause cards). |
| **L3 — CrossRegulation** | `PREPROCESSING/CrossRegulation/` | Per sub-domain & per pair | `DomainAnalysis/D-<XX>_<Name>/D-<XX>.<Y>.md` (4-type taxonomy) + `DeepAnalysis/D-<XX>_<Name>/D-<XX>.<Y>.md` (5-option taxonomy incl. scope-disjoint). |
| **L4 — Shared** | `PREPROCESSING/AMBIGUITY_ANALYSIS/`, `PREPROCESSING/00_Hierarchical_SecurityObjectives.md`, `PREPROCESSING/NIST_CSF_2.0_subcategories.md` | Shared methodology + frozen CSF 2.0 ID list | Berry lens (4 categories S1–S3), HSO activation model, NIST CSF 2.0 subcategory list. |

**Total counts**:

| Resource | Count |
|----------|-------|
| Sub-domain `.md` files (L1) | **38** |
| Macro-domain folders (L1) | 10 (D-01 through D-10) |
| Regulation folders (L2) | 5 (GDPR, NIS2, CRA, DORA, AI_Act) |
| Article splits (L2) | 140 (GDPR 48 + DORA 30 + CRA 25 + AI_Act 24 + NIS2 13) |
| DomainAnalysis pairs (L3) | 38 |
| DeepAnalysis pairs (L3) | 38 |

## §2 Case → Corpus Field Mapping (per doc)

For each of the 14 Rich Phase 1 docs, the table below maps the legacy doc's surface fields to the corpus layer(s) that will enrich it.

### 2.1 `00_Taxonomy_Reference.md`

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| 10 macro-domains (D-01 … D-10) | `PREPROCESSING/SubDomains/D-<XX>_<Name>/` folder names | L1 | Folder naming IS the taxonomy. |
| 38 sub-domains (D-XX.X) | 38 `.md` files in L1 | L1 | Each title (`title:` in frontmatter) gives the sub-domain name. |
| Regulation codes | `PREPROCESSING/Regulation/<REG>/` folder names | L2 | Canonical enum: GDPR, NIS2, CRA, DORA, AI_Act. |

### 2.2 `01_INTAKE_FORM.md`

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| Layer 1 (Regulatory Decision Tree) | `PREPROCESSING/00_Hierarchical_SecurityObjectives.md` | L4 | Mapping from regulation → sub-domain. |
| Layer 2 (Conditional Blocks) | `PREPROCESSING/Regulation/<REG>/Ambiguity/` | L2 | Per-regulation ambiguity cards. |
| Layer 3 (Regulatory Interaction Scan) | `PREPROCESSING/CrossRegulation/DeepAnalysis/` | L3 | Per-pair 5-option analysis (incl. scope-disjoint). |

### 2.3 `04_Company_Context_Assessment.md`

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| Stakeholder analysis | `PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.1.md` (roles) | L1 | Internal/external stakeholder set. |
| Business goals | `PREPROCESSING/SubDomains/D-09.2.md` (DPIA + FRIA) | L1 | Sub-domain D-09.2 covers both DPIA (GDPR) and FRIA (AI_Act). |
| Special category data (Art. 9) | `PREPROCESSING/SubDomains/D-01.1.md` (data at rest) + `D-05.1` (data lifecycle) | L1 | Sub-domain mapping for biometric data. |
| High-risk AI (Annex III) | `PREPROCESSING/SubDomains/D-09.3.md` + `D-02.4.md` | L1 | AI risk-management + adversarial robustness. |

### 2.4 `04a_Architecture_DataInventory.md`

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| Data categories (biometric, passport, watchlist) | `PREPROCESSING/SubDomains/D-01.1`, `D-01.2`, `D-01.3`, `D-01.4` | L1 | Encryption in transit/at rest, key management, integrity. |
| Data flows | `PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.1.md` through `D-05.4.md` | L1 | Data lifecycle coverage. |
| Process nodes (kiosk, edge AI, cloud) | `PREPROCESSING/SubDomains/D-04.3.md` (incident response — high-criticality for 99.99% SLA) | L1 | Operational architecture. |

### 2.5 `04b_Security_Posture.md`

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| ISO 27001 certification | `PREPROCESSING/SubDomains/D-09.1.md` (ISMS) | L1 | Governance foundation. |
| SOC / monitoring | `PREPROCESSING/SubDomains/D-10.1.md` (continuous monitoring) | L1 | Operational monitoring. |
| Audit logging | `PREPROCESSING/SubDomains/D-10.2.md` (audit logging & traceability) | L1 | Traceability in Hybrid Architecture. |

### 2.6 `04c_ThirdParty_Landscape.md`

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| Supplier security | `PREPROCESSING/SubDomains/D-06.1.md` (supplier assessment) | L1 | Supplier risk-assessment. |
| Cloud providers | `PREPROCESSING/SubDomains/D-06.2.md` (cloud-specific) | L1 | Cloud supply chain. |
| Hardware suppliers | `PREPROCESSING/SubDomains/D-06.3.md` (hardware) | L1 | **Top clause density: 21 SR-* refs**, 17 Case_02-applicable. |
| Notified body | `PREPROCESSING/SubDomains/D-06.4.md` (conformity assessment) | L1 | CRA Critical Class + AI_Act High-Risk conformity. |

### 2.7 `04d_Org_Roles_RACI.md`

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| DPO | `PREPROCESSING/SubDomains/D-09.1.md` (compliance roles) | L1 | GDPR-mandated role. |
| CISO | `PREPROCESSING/SubDomains/D-09.1.md`, `D-10.1.md` | L1 | Cybersecurity governance + monitoring. |
| AI Governance Lead | `PREPROCESSING/SubDomains/D-09.3.md` (AI_Act roles) | L1 | AI_Act-mandated role. |
| Management liability | `PREPROCESSING/SubDomains/D-09.1.md` (NIS2 management) | L1 | NIS 2 Art. 20 liability. |

### 2.8 `05_Regulatory_Applicability.md`

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| Trigger predicates | `PREPROCESSING/00_Hierarchical_SecurityObjectives.md` | L4 | Per-regulation activation rules. |
| Per-reg clause count | `PREPROCESSING/Regulation/<REG>/02_SecurityRules_NIST.md` (V1–V13) | L2 | Each clause has an SR-* identifier. |
| Sub-domain coverage | `PREPROCESSING/SubDomains/D-*.md` (participants HTML comment) | L1 | Per-sub-domain participant list. |

### 2.9 `05b_Ambiguity_Register.md` (NEW in Rich)

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| Linguistic ambiguity (S1–S3) | `PREPROCESSING/AMBIGUITY_ANALYSIS/01_Framework.md` + `Regulation/<REG>/Ambiguity/` per-regulation cards | L4 / L2 | Berry lens 4 categories. |
| Cross-regulation ambiguity | `PREPROCESSING/CrossRegulation/DeepAnalysis/D-*.md` (5-option taxonomy) | L3 | scope-disjoint, scope-overlap, contradictory, scope-correct, etc. |
| Case-specific ambiguity | `02_CASES/Case_02.../01_PHASE1_CONTEXT/02_Regulatory_Mapping_Master.md` | Legacy | The 3 strategic tensions T-001, T-002, T-003. |

### 2.10 `06_Clause_Mapping_Matrix.md` (and `.xlsx`)

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| 112 clauses (GDPR 28 + CRA 26 + NIS2 29 + AI_Act 29) | `PREPROCESSING/Regulation/<REG>/02_SecurityRules_NIST.md` | L2 | Each rule has an SR-REG-NNN id. |
| Clause → sub-domain mapping | `PREPROCESSING/SubDomains/D-*.md` (per-pair analysis) | L1 | Each clause appears in N sub-domains. |
| Per-article text | `PREPROCESSING/Regulation/<REG>/Articles/Art_N.md` | L2 | Token-efficient per-article reads. |
| NIST CSF mapping | `PREPROCESSING/NIST_CSF_2.0_subcategories.md` | L4 | Frozen CSF 2.0 ID list. |

### 2.11 `07_Structured_Compliance_Matrix.md`

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| SUBSTANTIVE / PARTIAL / NOT_ADDRESSED classification | `PREPROCESSING/SubDomains/D-*.md` (Classified relationship: COMPLEMENTARY, SAME, etc.) | L1 | Per-pair classification. |
| Coverage % per sub-domain | `PREPROCESSING/SubDomains/D-*.md` (Scope overlap Y/N/Conditional) | L1 | Scope overlap = presence of clause. |
| Sole-authority gaps | `PREPROCESSING/SubDomains/D-*.md` (sole_authority tag) | L1 | When only 1 reg covers a sub-domain. |

### 2.12 `07b_Proportionality_Profile.md` (NEW in Rich)

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| Tier assignment (Track B: MEDIUM) | `07b` is new — must be derived from `01_INTAKE_FORM.md` Layer 0 + Design Decisions | Legacy | Active conditional blocks → tier. |
| Per-sub-domain depth | `PREPROCESSING/SubDomains/D-*.md` (Compliance Score) | L1 | Some sub-domains have HIGH participation → RIGOROUS depth. |
| Resource envelope | `02_CASES/Case_02.../00_COMMON/03_Design_Decisions_Log.md` | Legacy | Case-by-case effort estimates. |

### 2.13 `07c_Adjusted_Objectives.md` (NEW in Rich)

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| Adjusted objectives (sub-SOs) | `PREPROCESSING/SubDomains/D-*.md` Section "2. Hierarchical Security Objective" | L1 | Each sub-domain has its own HSO. |
| HL objectives (cross-reg) | `PREPROCESSING/SubDomains/D-*.md` Section "HL activation" | L1 | E.g. D-03.1.HL activates when ≥2 regs overlap. |
| Voluntary / hard-wired | `PREPROCESSING/00_Hierarchical_SecurityObjectives.md` | L4 | Activation rules. |

### 2.14 `Citation_Index.md` (NEW in Rich)

| Legacy field | Corpus source | Layer | Notes |
|--------------|---------------|-------|-------|
| Article verbatim quotations | `PREPROCESSING/Regulation/<REG>/Articles/Art_N.md` | L2 | Source of truth for OJ text. |
| OJ reference | `PREPROCESSING/03_REFERENCE_MATERIAL/Regulatory_References/{REG}.txt` | L2 | Full OJ text per regulation. |
| SR-* identifier | `PREPROCESSING/Regulation/<REG>/02_SecurityRules_NIST.md` | L2 | Unambiguous citation. |
| Cross-domain citations | `PREPROCESSING/SubDomains/D-*.md` (related_documents) | L1 | Per-sub-domain regulation paths. |

## §3 In-Scope Ambiguity Cards (filtered preview)

Top 5 sub-domains by clause density, filtered for Case_02 applicable regs (GDPR + NIS2 + CRA + AI_Act):

| Rank | Sub-domain | Article refs (total) | Case_02-applicable refs | Participants | Notes |
|------|------------|----------------------|-------------------------|--------------|-------|
| 1 | **D-09.1 ISMS / Cybersecurity Governance** | 21 | 18 | GDPR, NIS2, CRA, DORA, AI_Act | Per-sub-domain: information security management system. T-004 (RESOURCE_CONFLICT) flagged here. |
| 2 | **D-06.3 Hardware / Component Suppliers** | 21 | 17 | GDPR, NIS2, CRA, DORA | Top clause-density sub-domain. Edge AI kiosks depend on hardware suppliers. |
| 3 | **D-09.2 DPIA + FRIA** | 17 | 14 | GDPR, NIS2, CRA, DORA, AI_Act | T-003 (TRIGGER_MISMATCH) flagged here — DPIA vs FRIA. |
| 4 | **D-09.4 Documentation / Records** | 14 | 12 | GDPR, NIS2, CRA, DORA, AI_Act | Documentation requirements are the most cross-cutting. |
| 5 | **D-06.4 Conformity Assessment** | 13 | 11 | GDPR, NIS2, CRA, DORA | CRA Critical Class + AI_Act High-Risk: notified body involvement. |

The **Strategic Tensions** (T-001 temporal conflict, T-002 cryptographic sharding, T-003 dual-mandate assessment) all map to the top of this table.

## §4 Migration Map — GDPR-C → GDPR-CL

Not applicable to Case_02. The "GDPR-C → GDPR-CL" migration map is for the corpus' internal migration between clause IDs, NOT a case-level mapping. Sprint 1 Block 2 will revisit if needed.

## §5 Cross-Reference Statistics

From extracted corpus:

| Metric | Value |
|--------|-------|
| Sub-domains with `participants` field present | 38 / 38 (100%) |
| Sub-domains where any participant matches Case_02 applicable regs | 38 / 38 (100%) |
| Sub-domains with SR-* clause references for Case_02-applicable regs | (to be computed in Sprint 1) |
| Article references found across all sub-domains | exceeds 200 |
| Active sub-domains per PROJECT_STATE.md | 35 / 38 (D-08.3 INACTIVE + 3 NOT_ADDRESSED) |

**Discrepancy with spec**: The task framed "active subdomains = 35" but the corpus has 38 sub-domain files with Case_02-applicable participants. The 35 figure represents **substantive clause coverage** (clauses actually map to those sub-domains), not participant overlap. Sprint 1 Block 3 will reconcile this — likely by introducing a 3-tier classification (active by participant, active by clause, NOT_ADDRESSED).

---

**See also**: `LINT_REPORT_BEFORE.md` (lint baseline), `README.md` (this folder's purpose), `../PROJECT_STATE.md` (case profile).
