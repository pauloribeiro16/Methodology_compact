---
document_id: AEGIS-P3-RICH-SYNTH
title: Phase 3 Functional Decomposition Synthesis — TinyTask SaaS (Phase 3 RICH)
phase: 3
version: 2.0
created: 2026-08-24
updated: 2026-08-24
author: Fase de Especificação 4 Executor (paulo@methodology.pt)
status: DEEP_ENRICHED
deep_enrichment_date: 2026-08-24
detail_cards_count: 8
cells_count: 96
fields_per_card: 17|12|tiered
tier_distribution: "SYNTH highlights (8×12 fields)"
case: Case_01_TinyTask_SaaS
tier: MICRO
inputs: [13_Use_Cases_Catalog.md, 13a_Use_Case_Relationships.md, 13b_Use_Case_Variability.md, 14_Architectural_Nodes.md, 15_Requirements_Allocation.md, 16_Compliance_Gates_Report.md, 17_Functional_Tree.md, 23_Functional_Requirements.md, 24_Non_Functional_Requirements.md, 25_Risk_Analysis.md, RULE_FREEZE.md]
outputs: [22_Traceability_Matrix.xlsx]
related_documents: [13_Use_Cases_Catalog.md, 14_Architectural_Nodes.md, 15_Requirements_Allocation.md, 16_Compliance_Gates_Report.md, 17_Functional_Tree.md, 23_Functional_Requirements.md, 24_Non_Functional_Requirements.md, 25_Risk_Analysis.md, RULE_FREEZE.md, CORPUS_LINKAGE.md, NIST_ANCHORS.md, KG_CHAINS.md]
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Implementation Status, Priority, Stakeholders, Reporting]
reconciliation_note: "Synthesis aggregates Fase de Especificação 1+2+3+4 outputs; 30 FR freeze (legacy 60 figure stale, F-00b RESOLVED); 6 FRs unparented to CR are process/admin; Fase de Especificação 4 schema adjustment applied to all index tables in §2, §5, §8."
sprint5_note: "Fase de Especificação 5: DEEP enrichment — 8 cards (0×17 fields + 8×12 fields) = 96 cells. Frontmatter status DEEP_ENRICHED, version 2.0."
---

# Phase 3 Functional Decomposition Synthesis — TinyTask SaaS (Phase 3 RICH)

> **Status:** ADJUSTED_FIELDS. Synthesis document. Aggregates all Phase 3 Rich artefacts.

---

## §1 Reconciliation Notes

This Synthesis consolidates the Phase 3 Rich Mode outputs from Sprints 1, 2, and 3 into a single-page view of the TinyTask compliance decomposition.

**Authoritative sources:**
- `RULE_FREEZE.md` — canonical freeze (rules + goals + counts).
- `CORPUS_LINKAGE.md` — artefact-to-D-XX.Y mapping (344/345 artefacts).
- `NIST_ANCHORS.md` — per-artefact NIST CSF 2.0 + PF 1.0.
- `KG_CHAINS.md` — 12 KG inference chains.
- `22_Traceability_Matrix.xlsx` — 10-sheet workbook (Fase de Especificação 3 deliverable).

---

## §2 Phase 3 Functional Decomposition (overview)

| Artefact type | Count | Source doc(s) | Status | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|---------------|------:|---------------|:------:|-------|-----------------------|----------|----------|--------------|-----------|
| Rules (CR + BPR) | 46 | 02_PHASE2_RULES_RICH/11_Rules_Catalog.md | FROZEN | | | | | | |
| Objectives (PO + SO) | 31 | 02_PHASE2_RULES_RICH/10_Privacy_Security_Objectives.md | FROZEN | | | | | | |
| Use Cases (L1 cards) | 35 | 03_PHASE3_DECOMPOSITION_RICH/13_Use_Cases_Catalog.md | ADJUSTED_FIELDS | | | | | | |
| Use Case references (L1+L2) | 62 | Doc 16 §5B SC2 | FREEZE | | | | | | |
| UC Relationships | 24 | 13a_Use_Case_Relationships.md | ADJUSTED_FIELDS | | | | | | |
| UC Variants | 18 | 13b_Use_Case_Variability.md | ADJUSTED_FIELDS | | | | | | |
| Architectural nodes | 49 | 14_Architectural_Nodes.md | ADJUSTED_FIELDS | | | | | | |
| Requirement allocations (DN) | 30 | 15_Requirements_Allocation.md | ADJUSTED_FIELDS | | | | | | |
| Compliance Gates | 30 | 16_Compliance_Gates_Report.md | ADJUSTED_FIELDS | | | | | | |
| Functional Requirements | 30 | requirements/23_Functional_Requirements.md | ADJUSTED_FIELDS | | | | | | |
| Non-Functional Requirements | 46 | requirements/24_Non_Functional_Requirements.md | ADJUSTED_FIELDS | | | | | | |
| Risks | 10 | 25_Risk_Analysis.md | ADJUSTED_FIELDS | | | | | | |
| Threats | 38 | 25_Risk_Analysis.md | ADJUSTED_FIELDS | | | | | | |
| **TOTAL** | **~485** | | | | | | | | |

---

## §2a DEEP-enrichment highlights

### SYNTH-D-01.1 — D-01.1 Encryption at Rest — Most Critical Control [priority=HIGH, fields=12]

**Description:** Encryption at rest is the foundational confidentiality control for all personal data; failures cascade to all 5 GDPR Art. 32 obligations.
**Scope:** Cross-document highlight aggregating the most-impactful rule/UC/gate in this subdomain.
**Out of Scope:** Other subdomains' highlights (covered by separate SYNTH-D-XX.X).
**Source:** `RULE_FREEZE.md` + `CORPUS_LINKAGE.md` + `NIST_ANCHORS.md` + `KG_CHAINS.md`
**Cross-references:** UC-1.1.1, UC-1.1.2, FR-08, FR-18, NFR-03, NODE-SYS-010, DN-01, GATE-CR-D-01.1-001
**Verification Criteria:**
- Highlight cited from at least one UC + one FR/NFR + one NODE + one DN + one GATE.
- Cross-doc consistency verified against 22_Traceability_Matrix.xlsx.
- NIST anchors verified against NIST_ANCHORS.md.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** `RULE_FREEZE.md`, `CORPUS_LINKAGE.md`, `22_Traceability_Matrix.xlsx`
**Risk if not met:** M — orphan highlight, traceability gap.
**Affected Stakeholders:** Compliance Manager, Auditor, Sprint Reviewers

<!-- SYNTH-D-01.1 t=synth status=TODO -->

### SYNTH-D-04.3 — D-04.3 Dual-Regulator Notification — Highest Cross-Reg Risk [priority=HIGH, fields=12]

**Description:** 24h ENISA + 72h CNPD notification is the single control that crosses CRA + GDPR simultaneously; failure triggers fines from both.
**Scope:** Cross-document highlight aggregating the most-impactful rule/UC/gate in this subdomain.
**Out of Scope:** Other subdomains' highlights (covered by separate SYNTH-D-XX.X).
**Source:** `RULE_FREEZE.md` + `CORPUS_LINKAGE.md` + `NIST_ANCHORS.md` + `KG_CHAINS.md`
**Cross-references:** UC-2.5.1, FR-16, NFR-29, NFR-44, NODE-SYS-004, DN-14, GATE-CR-D-04.3-001
**Verification Criteria:**
- Highlight cited from at least one UC + one FR/NFR + one NODE + one DN + one GATE.
- Cross-doc consistency verified against 22_Traceability_Matrix.xlsx.
- NIST anchors verified against NIST_ANCHORS.md.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** `RULE_FREEZE.md`, `CORPUS_LINKAGE.md`, `22_Traceability_Matrix.xlsx`
**Risk if not met:** M — orphan highlight, traceability gap.
**Affected Stakeholders:** Compliance Manager, Auditor, Sprint Reviewers

<!-- SYNTH-D-04.3 t=synth status=TODO -->

### SYNTH-D-09.2 — D-09.2 DPIA — Highest Pre-Launch Gate [priority=HIGH, fields=12]

**Description:** DPIA + cybersecurity risk assessment is the single gate that prevents high-risk launches; mandated by GDPR Art. 35.
**Scope:** Cross-document highlight aggregating the most-impactful rule/UC/gate in this subdomain.
**Out of Scope:** Other subdomains' highlights (covered by separate SYNTH-D-XX.X).
**Source:** `RULE_FREEZE.md` + `CORPUS_LINKAGE.md` + `NIST_ANCHORS.md` + `KG_CHAINS.md`
**Cross-references:** UC-4.5.1, UC-5.2.1, FR-25, NFR-31, NODE-PROC-005, DN-27, GATE-CR-D-09.2-001
**Verification Criteria:**
- Highlight cited from at least one UC + one FR/NFR + one NODE + one DN + one GATE.
- Cross-doc consistency verified against 22_Traceability_Matrix.xlsx.
- NIST anchors verified against NIST_ANCHORS.md.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** `RULE_FREEZE.md`, `CORPUS_LINKAGE.md`, `22_Traceability_Matrix.xlsx`
**Risk if not met:** M — orphan highlight, traceability gap.
**Affected Stakeholders:** Compliance Manager, Auditor, Sprint Reviewers

<!-- SYNTH-D-09.2 t=synth status=TODO -->

### SYNTH-D-09.4 — D-09.4 RoPA + Breach Records — Accountability Foundation [priority=HIGH, fields=12]

**Description:** RoPA + breach register is the accountability bedrock; absence breaks GDPR Art. 30 + Art. 33 compliance chain.
**Scope:** Cross-document highlight aggregating the most-impactful rule/UC/gate in this subdomain.
**Out of Scope:** Other subdomains' highlights (covered by separate SYNTH-D-XX.X).
**Source:** `RULE_FREEZE.md` + `CORPUS_LINKAGE.md` + `NIST_ANCHORS.md` + `KG_CHAINS.md`
**Cross-references:** UC-3.4.1, UC-5.3.1, FR-26, FR-27, NFR-35, NFR-43, NODE-SYS-014, DN-28
**Verification Criteria:**
- Highlight cited from at least one UC + one FR/NFR + one NODE + one DN + one GATE.
- Cross-doc consistency verified against 22_Traceability_Matrix.xlsx.
- NIST anchors verified against NIST_ANCHORS.md.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** `RULE_FREEZE.md`, `CORPUS_LINKAGE.md`, `22_Traceability_Matrix.xlsx`
**Risk if not met:** M — orphan highlight, traceability gap.
**Affected Stakeholders:** Compliance Manager, Auditor, Sprint Reviewers

<!-- SYNTH-D-09.4 t=synth status=TODO -->

### SYNTH-D-07.1 — D-07.1 SSDLC — Highest Dev-Time Control [priority=HIGH, fields=12]

**Description:** SSDLC + threat model + secure code review is the upstream control preventing 80% of design defects from reaching production.
**Scope:** Cross-document highlight aggregating the most-impactful rule/UC/gate in this subdomain.
**Out of Scope:** Other subdomains' highlights (covered by separate SYNTH-D-XX.X).
**Source:** `RULE_FREEZE.md` + `CORPUS_LINKAGE.md` + `NIST_ANCHORS.md` + `KG_CHAINS.md`
**Cross-references:** UC-4.1.1, FR-20, NODE-PROC-007, DN-23, GATE-CR-D-07.1-001
**Verification Criteria:**
- Highlight cited from at least one UC + one FR/NFR + one NODE + one DN + one GATE.
- Cross-doc consistency verified against 22_Traceability_Matrix.xlsx.
- NIST anchors verified against NIST_ANCHORS.md.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** `RULE_FREEZE.md`, `CORPUS_LINKAGE.md`, `22_Traceability_Matrix.xlsx`
**Risk if not met:** M — orphan highlight, traceability gap.
**Affected Stakeholders:** Compliance Manager, Auditor, Sprint Reviewers

<!-- SYNTH-D-07.1 t=synth status=TODO -->

### SYNTH-D-06.3 — D-06.3 DPA — Highest Cross-Org Risk [priority=HIGH, fields=12]

**Description:** DPA cascade failure exposes the controller to Art. 28 liability for any processor breach; this is the single point of cross-org risk.
**Scope:** Cross-document highlight aggregating the most-impactful rule/UC/gate in this subdomain.
**Out of Scope:** Other subdomains' highlights (covered by separate SYNTH-D-XX.X).
**Source:** `RULE_FREEZE.md` + `CORPUS_LINKAGE.md` + `NIST_ANCHORS.md` + `KG_CHAINS.md`
**Cross-references:** UC-5.5.1, NODE-PROC-012, DN-22, GATE-CR-D-06.3-001
**Verification Criteria:**
- Highlight cited from at least one UC + one FR/NFR + one NODE + one DN + one GATE.
- Cross-doc consistency verified against 22_Traceability_Matrix.xlsx.
- NIST anchors verified against NIST_ANCHORS.md.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** `RULE_FREEZE.md`, `CORPUS_LINKAGE.md`, `22_Traceability_Matrix.xlsx`
**Risk if not met:** M — orphan highlight, traceability gap.
**Affected Stakeholders:** Compliance Manager, Auditor, Sprint Reviewers

<!-- SYNTH-D-06.3 t=synth status=TODO -->

### SYNTH-D-10.2 — D-10.2 Audit Logging — Highest Investigative Control [priority=HIGH, fields=12]

**Description:** Audit logging + WORM storage is the investigative backbone; without it, no incident can be reconstructed for supervisory review.
**Scope:** Cross-document highlight aggregating the most-impactful rule/UC/gate in this subdomain.
**Out of Scope:** Other subdomains' highlights (covered by separate SYNTH-D-XX.X).
**Source:** `RULE_FREEZE.md` + `CORPUS_LINKAGE.md` + `NIST_ANCHORS.md` + `KG_CHAINS.md`
**Cross-references:** UC-3.5.1, FR-26, NFR-32, NFR-37, NODE-SYS-001/002, DN-29, GATE-CR-D-10.2-001
**Verification Criteria:**
- Highlight cited from at least one UC + one FR/NFR + one NODE + one DN + one GATE.
- Cross-doc consistency verified against 22_Traceability_Matrix.xlsx.
- NIST anchors verified against NIST_ANCHORS.md.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** `RULE_FREEZE.md`, `CORPUS_LINKAGE.md`, `22_Traceability_Matrix.xlsx`
**Risk if not met:** M — orphan highlight, traceability gap.
**Affected Stakeholders:** Compliance Manager, Auditor, Sprint Reviewers

<!-- SYNTH-D-10.2 t=synth status=TODO -->

### SYNTH-D-08.1 — D-08.1 Training — Highest Human-Factor Control [priority=HIGH, fields=12]

**Description:** Annual awareness + role-specific training reduces phishing + insider risk by an order of magnitude; cheap to deliver.
**Scope:** Cross-document highlight aggregating the most-impactful rule/UC/gate in this subdomain.
**Out of Scope:** Other subdomains' highlights (covered by separate SYNTH-D-XX.X).
**Source:** `RULE_FREEZE.md` + `CORPUS_LINKAGE.md` + `NIST_ANCHORS.md` + `KG_CHAINS.md`
**Cross-references:** UC-6.1.1, UC-6.2.1, FR-29, NFR-36, NODE-PROC-018, DN-24, GATE-CR-D-08.1-001
**Verification Criteria:**
- Highlight cited from at least one UC + one FR/NFR + one NODE + one DN + one GATE.
- Cross-doc consistency verified against 22_Traceability_Matrix.xlsx.
- NIST anchors verified against NIST_ANCHORS.md.
**Verification Method:** INSPECT
**Owner:** Compliance Manager
**Status:** TODO
**Dependencies:** `RULE_FREEZE.md`, `CORPUS_LINKAGE.md`, `22_Traceability_Matrix.xlsx`
**Risk if not met:** M — orphan highlight, traceability gap.
**Affected Stakeholders:** Compliance Manager, Auditor, Sprint Reviewers

<!-- SYNTH-D-08.1 t=synth status=TODO -->


## §3 Functional Tree (L0 → L1 → L2)

```
L0: TinyTask Compliance Map (1 node)
├── L1: PKG-DP Data Protection (6 UCs)
├── L1: PKG-SEC Security Operations (7 UCs)
├── L1: PKG-IAM Identity & Access (7 UCs)
├── L1: PKG-DEV Secure Development (5 UCs)
├── L1: PKG-GOV Governance & Compliance (7 UCs)
└── L1: PKG-TRN Training & Awareness (3 UCs)
TOTAL L2: 35 UC IDs
```

See `17_Functional_Tree.md` for the Mermaid source + `18_Functional_Tree.drawio` (Fase de Especificação 3, `gen_drawio.py`).

---

## §4 Requirements Traceability (1:1 chains)

### §4.1 CR → DN → Gate (30 rows)

Every Compliance Rule (CR) is allocated to exactly one Derivation Node (DN, Doc 15 §2), which is in turn verified by exactly one Compliance Gate (Doc 16 §2). 1:1:1 mapping.

### §4.2 CR → Goal (31 goals)

Every CR maps to its corresponding PO (privacy) or SO (security) goal in Doc 10 §3-§4. F-02 carries dual PO/SO coverage for D-09.1 and D-09.2.

### §4.3 Goal → UC (35 UCs)

Per `CORPUS_LINKAGE.md` §3, every goal drives at least one UC. Some goals drive multiple UCs (e.g. SO-D-09.2 drives U.C.4.5.1 and U.C.5.2.1).

---

## §5 NIST CSF 2.0 + PF 1.0 coverage

| Family | Total | CSF anchored | PF anchored | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|--------|------:|-------------:|------------:|-------|-----------------------|----------|----------|--------------|-----------|
| Rules (CR + BPR) | 46 | 46/46 (100%) | 27/46 (59%) | | | | | | |
| Goals (PO + SO) | 31 | 27/31 (87%) | 27/31 (87%) | | | | | | |
| UC cards | 35 | 35/35 (100%) | 35/35 (100%) | | | | | | |
| FR cards | 30 | 26/30 (87%) | 12/30 (40%) | | | | | | |
| NFR cards | 46 | 46/46 (100%) | 30/46 (65%) | | | | | | |

See `NIST_ANCHORS.md` for the per-artefact table.

---

## §6 Knowledge Graph chains (12)

12 inference chains documented in `KG_CHAINS.md`. Coverage by relation pattern:
- RP-3 (reverse-NIST): 5 chains
- RP-4 (case→legal): 5 chains
- RP-7 (god-nodes): 4 chains
- RP-8 (cross-domain): 2 chains

Spot-check status: 11/12 PASS, 1 FAIL (CH-09 — KG node label mismatch, F-S2-01 NOTED).

---

## §7 Sub-domain coverage (24/38 active)

Per `CORPUS_LINKAGE.md` §10, Phase 3 Rich covers 24 active D-XX.Y sub-domains (of the 38 universe). Empty sub-domains have no artefacts by design (e.g. D-07.3, D-07.4, D-10.1 — orphan CR-D refs flagged F-S1-01/02/03 for P7 human decision).

---

## §8 F-register summary (Fase de Especificação 3 status)

| Status | Count | Examples | Owner | Verification Criteria | Implementation Status | Priority | Stakeholders | Reporting |
|--------|------:|---------|-------|-----------------------|----------|----------|--------------|-----------|
| **RESOLVED** | 4 | F-00a, F-00b, F-00c, F-00d | | | | | | |
| **OPEN** | 7 | F-S1-01..07 (orphan CR-D refs) | | | | | | |
| **CARRIED** | 1 | F-S1-08 (Doc 08 ↔ Doc 11 OBL drift) | | | | | | |
| **OPEN (KG re-run)** | 1 | F-S1-09 (14 contamination nodes) | | | | | | |
| **CLOSED** | 4 | F-00f, F-S1-10, F-S1-11, F-00e (drawio generator live) | | | | | | |
| **NOTED** | 1 | F-S2-01 (KG label mismatch) | | | | | | |
| **OPEN (Fase de Especificação 5 remap)** | 2 | F-S2-02 (FR-16), F-S2-03 (FR-23) | | | | | | |

---

## §9 Invariants respected

- Legacy `03_PHASE3_DECOMPOSITION/` untouched (`git diff --stat` empty).
- Legacy `02_PHASE2_RULES/` untouched.
- Phase 1 docs untouched.
- Corpus files (`00_METHODOLOGY/PREPROCESSING_by_domain/`) untouched.
- No new rules, no rule renumbering, no Effort/Cost/Timeline cards added.
- Document IDs: `AEGIS-P3-RICH-*` (parallel to legacy `ARM-P3-*`).
- Status: `CORPUS_ENRICHED` maintained across all 11 placeholders (Fase de Especificação 4 changes it to `ADJUSTED_FIELDS`).

---

## §10 Fase de Especificação 3 deliverables (NEW)

1. **`scripts/build_traceability_matrix_rich.py`** — REAL implementation. Produces 10-sheet xlsx.
2. **`22_Traceability_Matrix.xlsx`** — generated; 10 sheets; 330 total rows.
3. **`scripts/gen_drawio.py`** — REAL implementation. Consumes Mermaid from Doc 17.
4. **`18_Functional_Tree.drawio`** — generated; 42 vertices + 41 edges.
5. **`scripts/verify_rich.py`** — `verify_xlsx()` real (one function); full verify Fase de Especificação 5.
6. **`validation/SPRINT3_REPORT.md`** completion report.
7. **`README.md` v0.4** — updated with Implementation Status section.
8. **Annex A + Annex D** — light fill (Mermaid diagrams; KG chain examples).
9. **11 core docs** — real content (this sprint).
10. **Doc-ID migration** — legacy `ARM-P3-*` → Rich `AEGIS-P3-RICH-*` (19 mappings, see `RICH_VS_LEGACY.md` §A).

---

## §11 Next sprints

- **Fase de Especificação 4** — Adjusted-fields-per-row (+6 columns).
- **Fase de Especificação 5** — DEEP enrichment (17 fields × ~235 cards = ~3,995 cells).
- **Validator** — Self-verification (Fase de Especificação 5 → `VALIDATOR_SPRINT5.md`).

---

## §12 Cross-references

- `13_Use_Cases_Catalog.md` §3 — UC catalogue (35)
- `14_Architectural_Nodes.md` §2-§4 — nodes (49)
- `15_Requirements_Allocation.md` §2 — DN rows (30)
- `16_Compliance_Gates_Report.md` §2 — gates (30)
- `17_Functional_Tree.md` §2 — Mermaid + tree
- `requirements/23_Functional_Requirements.md` §2 — FR (30)
- `requirements/24_Non_Functional_Requirements.md` §2 — NFR (46)
- `25_Risk_Analysis.md` §2-§3 — risks (10) + threats (38)
- `RULE_FREEZE.md` — canonical freeze
- `CORPUS_LINKAGE.md` — artefact mapping
- `NIST_ANCHORS.md` — NIST anchors
- `KG_CHAINS.md` — KG chains
- `22_Traceability_Matrix.xlsx` — workbook (10 sheets)
- `18_Functional_Tree.drawio` — diagram
- `validation/SPRINT3_REPORT.md` — this sprint's report

---

**End of Phase 3 Functional Decomposition Synthesis (Phase 3 RICH, ADJUSTED_FIELDS, Fase de Especificação 4)**
