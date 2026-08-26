---
document_id: AEGIS-P2-RICH-08
title: Obligation Derivation Report — Rich Mode
phase: 2
version: 3.1
created: 2026-08-07
updated: 2026-08-10
author: "Sprint 5 + Sprint 9 + Sprint 6+ Executor (deep-enrichment-per-card + corr-012 PO/SO migration + tech-strip + P7 orphan fix)"
status: DEEP_ENRICHED
sprint: 9
sprint_role: deep_enrichment_per_card
deep_enrichment_date: 2026-08-07
detail_cards_count: 34
fields_per_card: 17
inputs: ["07_Structured_Compliance_Matrix.md", "06_Clause_Mapping_Matrix.xlsx", "01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml", "../02_PHASE2_RULES/08_Obligation_Derivation.md"]
outputs: ["09_Strategic_Tensions_Report.md", "10_Privacy_Security_Objectives.md", "11_Rules_Catalog.md"]
traceability: "AEGIS Class Model → RegulatoryObligation, RegulatoryClause classes"
related_documents: "00_Taxonomy_Reference.md, 03_Design_Decisions_Log.md"
case: Case_01_TinyTask_SaaS
tier: MICRO
expected_obligations: 34
expected_fields_per_card: 17
fields_excluded: ["Effort Estimate", "Cost Estimate", "Target Timeline"]
branch: feature/aegis-case01-p7-orphan-fix
sprint_1_scope: cross-check 30 obligations ↔ 30 goals ↔ 30 CR rules; verify NI propagation; ID integrity; ontology cross-ref (28 GDPR + 26 CRA)
sprint_3_scope: regenerate 12_Rules_Catalog.xlsx (14 sheets) — DONE in Sprint 3
sprint_4_scope: port legacy §4 catalog table (30 obligations × 11 cols) into Rich §4 + add 6 new cols (Owner, Verification Criteria, Maturity, Priority, Stakeholders, Reporting); resolve F-10 NI divergence for OBL-D-01.4-001 and OBL-D-09.1-001
sprint_4_verdict: "PASS_WITH_FINDINGS — see §4.1 NI Reconciliation and §3.7 carried findings F-01/F-02"
sprint_5_scope: "populate 17-field detail cards for all 30 obligations (510 cells: 30 × 17); 12 base + 3 Case_01-specific + 2 context fields"
sprint_5_verdict: "PASS — see §5 cards; 30/30 cards × 17/17 fields; cross-references to Doc 09 (T-001/T-H-001/T-M-001/T-M-002) and Sprint 1 findings (F-01/F-03/F-10) integrated"
sprint_6_scope: "P7 orphan fix — add 4 OBLs (D-07.2/3/4, D-10.1; CRA sole authority); correct phase1_ontology.yaml (move D-07.x from not_covered to covered; covered_count 31→34, not_covered_count 7→4); update Doc 08 §2 note + §3 reconciliation tables + §4 catalog rows + §5 detail cards (cells 510→578); new findings F-07/F-08/F-09 (cross-doc orphans + twin-ontology + taxonomy-reference divergence for follow-on contracts)"
sprint_6_verdict: "CONDITIONAL_PASS — 30 existing OBLs unchanged; 4 new OBLs added with CRA sole-authority; PO/SO/CR-D-XX.X-001 placeholders parallel F-01/F-03 carry-over; Doc 08 internally consistent; F-07/F-08/F-09 flag follow-on contract work"
---

# Obligation Derivation Report — Rich Mode

> **Sprint 0/6+ placeholder** — this document is the Rich Mode sibling of legacy `02_PHASE2_RULES/08_Obligation_Derivation.md`.
> Will be enriched in Sprint 1 (reconciliation) + Sprint 5 (15 fields × 30 obligations). **Sprint 6+ P7 orphan fix:** 4 OBLs added (D-07.2/3/4, D-10.1); obligation count is now 34.

---

## 1. DOCUMENT PURPOSE

This is the Rich Mode version of the Obligation Derivation Report. It consolidates 34 obligations (from 54 source clauses: 28 GDPR + 26 CRA; 30 active in legacy + 4 added in Sprint 6+) into 15-field detail cards with multi-paragraph descriptions, scope/out-of-scope, NIST CSF anchors, and operational metadata.

**Phase 2 Step:** B (Obligation Derivation)
**Gate Criteria:** All 34 applicable obligations mapped to clauses with NI propagation + 15-field detail cards

---

## 2. OBLIGATION CATALOG INHERITED FROM LEGACY (SPRINT 0 BASELINE + 4 SPRINT 6+)

The 34 obligations are inherited from legacy `02_PHASE2_RULES/08_Obligation_Derivation.md` §4 (30 OBLs: D-01 through D-10 sub-domains) **plus** 4 Sprint 6+ additions (D-07.2/3/4, D-10.1) per the P7 orphan fix.

**Verified obligation inventory (canonical):**

| Sub-Domain | Count | Obligation IDs |
|------------|------:|----------------|
| D-01 | 4 | OBL-D-01.1-001, OBL-D-01.2-001, OBL-D-01.3-001, OBL-D-01.4-001 |
| D-02 | 3 | OBL-D-02.1-001, OBL-D-02.2-001, OBL-D-02.3-001 |
| D-03 | 4 | OBL-D-03.1-001, OBL-D-03.2-001, OBL-D-03.3-001, OBL-D-03.4-001 |
| D-04 | 4 | OBL-D-04.1-001, OBL-D-04.2-001, OBL-D-04.3-001, OBL-D-04.4-001 |
| D-05 | 4 | OBL-D-05.1-001, OBL-D-05.2-001, OBL-D-05.3-001, OBL-D-05.4-001 |
| D-06 | 3 | OBL-D-06.1-001, OBL-D-06.2-001, OBL-D-06.3-001 |
| D-07 | 4 | OBL-D-07.1-001, OBL-D-07.2-001, OBL-D-07.3-001, OBL-D-07.4-001 |
| D-08 | 2 | OBL-D-08.1-001, OBL-D-08.2-001 |
| D-09 | 3 | OBL-D-09.1-001, OBL-D-09.2-001, OBL-D-09.4-001 |
| D-10 | 3 | OBL-D-10.1-001, OBL-D-10.2-001, OBL-D-10.3-001 |
| **TOTAL** | **34** | — |

**Note (Sprint 6+ — P7 orphan fix):** D-09.3 is absent by design (sole authority DORA; not applicable per ontology). **D-07.2, D-07.3, D-07.4, D-10.1 ARE in scope** as of Sprint 6 (P7 orphan fix); these were previously misclassified as DORA/NIS 2 exclusive in `phase1_ontology.yaml` `subdomains.not_covered` but Doc 07 §3 (compliance matrix) shows CRA coverage for these sub-domains. The ontology YAML has been corrected (see `00_COMMON/phase1_ontology.yaml`); 4 OBLs (D-07.2/07.3/07.4/10.1) are added below with CRA sole-authority mapping. See §3.5 gap analysis + §3.7 finding F-07 for the cross-doc orphan risk on Doc 10/11 (PO/SO/CR equivalents to be added in follow-on contract — current OBLs link directly to CR-D-XX.X-001 placeholders).

---

## 3. RECONCILIATION CROSS-CHECKS (SPRINT 1)

> Sprint 1 scope: cross-check the 30 obligations against the 30 goals (Doc 10) and 30 CR rules (Doc 11), verify Normative Intensity (NI) propagation, confirm ID integrity, and cross-reference the Phase 1 ontology (28 GDPR + 26 CRA clauses). Legacy `02_PHASE2_RULES/` files are **read-only** and not modified by this section. **Sprint 6+ update:** OBL count raised to 34 after P7 orphan fix (D-07.2/3/4, D-10.1 added); cross-checks reflect 34.

### 3.1 Obligation Count Verification

| Check | Expected | Actual | Status |
|-------|---------:|-------:|:------:|
| Total obligations in Doc 08 §4 | 34 | 34 | PASS |
| Sub-domain coverage (10 sub-domains active) | 10 | 10 | PASS |
| Unique OBL IDs (no duplicates) | 34 | 34 | PASS |
| Canonical ID format `OBL-D-XX.X-NNN` | 34 | 34 | PASS |

### 3.2 Goal-to-Obligation Mapping (OBL → PO/SO)

Each of the 34 obligations maps to **at least 1** objective (PO or SO). Strict 1:1 mapping is violated in 2 cases (D-09.1 and D-09.2 are covered by BOTH a PO and an SO). Three obligations have no corresponding PO/SO (D-01.3, carry-over F-01; D-07.2/3/4 + D-10.1, new F-07 cross-doc orphans) — see §3.7 findings F-01 + F-07.

| OBL ID | Linked Goal(s) | 1:1? | Status |
|--------|----------------|:----:|:------:|
| OBL-D-01.1-001 | PO-D-01.1-001 | yes | PASS |
| OBL-D-01.2-001 | PO-D-01.2-001 | yes | PASS |
| OBL-D-01.3-001 | — (none) | no | **FINDING F-01** |
| OBL-D-01.4-001 | PO-D-01.4-001 | yes | PASS |
| OBL-D-02.1-001 | SO-D-02.1-001 | yes | PASS |
| OBL-D-02.2-001 | SO-D-02.2-001 | yes | PASS |
| OBL-D-02.3-001 | SO-D-02.3-001 | yes | PASS |
| OBL-D-03.1-001 | SO-D-03.1-001 | yes | PASS |
| OBL-D-03.2-001 | SO-D-03.2-001 | yes | PASS |
| OBL-D-03.3-001 | SO-D-03.3-001 | yes | PASS |
| OBL-D-03.4-001 | SO-D-03.4-001 | yes | PASS |
| OBL-D-04.1-001 | SO-D-04.1-001 | yes | PASS |
| OBL-D-04.2-001 | SO-D-04.2-001 | yes | PASS |
| OBL-D-04.3-001 | SO-D-04.3-001 | yes | PASS |
| OBL-D-04.4-001 | SO-D-04.4-001 | yes | PASS |
| OBL-D-05.1-001 | PO-D-05.1-001 | yes | PASS |
| OBL-D-05.2-001 | PO-D-05.2-001 | yes | PASS |
| OBL-D-05.3-001 | PO-D-05.3-001 | yes | PASS |
| OBL-D-05.4-001 | PO-D-05.4-001 | yes | PASS |
| OBL-D-06.1-001 | SO-D-06.1-001 | yes | PASS |
| OBL-D-06.2-001 | SO-D-06.2-001 | yes | PASS |
| OBL-D-06.3-001 | SO-D-06.3-001 | yes | PASS |
| OBL-D-07.1-001 | PO-D-07.1-001 | yes | PASS |
| OBL-D-07.2-001 | — (TBD: PO-D-07.2-001 to be added in follow-on contract — see F-07) | no | **F-07 (cross-doc orphan)** |
| OBL-D-07.3-001 | — (TBD: SO-D-07.3-001 to be added in follow-on contract — see F-07) | no | **F-07 (cross-doc orphan)** |
| OBL-D-07.4-001 | — (TBD: SO-D-07.4-001 to be added in follow-on contract — see F-07) | no | **F-07 (cross-doc orphan)** |
| OBL-D-08.1-001 | SO-D-08.1-001 | yes | PASS |
| OBL-D-08.2-001 | SO-D-08.2-001 | yes | PASS |
| OBL-D-09.1-001 | PO-D-09.1-001 **AND** SO-D-09.1-001 | no (2:1) | **FINDING F-02** |
| OBL-D-09.2-001 | PO-D-09.2-001 **AND** SO-D-09.2-001 | no (2:1) | **FINDING F-02** |
| OBL-D-09.4-001 | PO-D-09.4-001 | yes | PASS |
| OBL-D-10.1-001 | — (TBD: SO-D-10.1-001 to be added in follow-on contract — see F-07) | no | **F-07 (cross-doc orphan)** |
| OBL-D-10.2-001 | SO-D-10.2-001 | yes | PASS |
| OBL-D-10.3-001 | SO-D-10.3-001 | yes | PASS |

**Summary (post Sprint 6+ P7 fix):** 27 OBLs (79%) have strict 1:1 goal mapping; 2 OBLs (D-09.1, D-09.2) have 2:1 mapping; **5 OBLs** (D-01.3 + D-07.2/D-07.3/D-07.4/D-10.1) have no goal — D-01.3 is a known carry-over (F-01/F-03, deferred to human arbiter); the 4 Sprint 6 additions are F-07 cross-doc orphans awaiting Doc 10 PO/SO additions in a follow-on contract. Total goal entries covering OBLs = 31 (11 PO + 20 SO); 4 new OBLs link directly to CR-D-XX.X-001 placeholders (see §3.3). See §3.7 for findings.

### 3.3 CR-Rule-to-Obligation Mapping (OBL → CR)

Each of the 34 obligations maps to **exactly 1** Compliance Rule in Doc 11 §4. The mapping is strict 1:1 by ID suffix. **Note:** 4 OBLs added in Sprint 6+ (D-07.2/3/4, D-10.1) reference CR-D-XX.X-001 placeholders that do not yet exist in Doc 11 §4 — these are F-07 cross-doc orphans awaiting Doc 11 additions in a follow-on contract (analogous to the F-01/F-03 phantom-PO situation for D-01.3).

| OBL ID | CR Rule | Status |
|--------|---------|:------:|
| OBL-D-01.1-001 | CR-D-01.1-001 | PASS |
| OBL-D-01.2-001 | CR-D-01.2-001 | PASS |
| OBL-D-01.3-001 | CR-D-01.3-001 | PASS (but CR references phantom PO-D-01.3-001 — see §3.7 F-03) |
| OBL-D-01.4-001 | CR-D-01.4-001 | PASS |
| OBL-D-02.1-001 | CR-D-02.1-001 | PASS |
| OBL-D-02.2-001 | CR-D-02.2-001 | PASS |
| OBL-D-02.3-001 | CR-D-02.3-001 | PASS |
| OBL-D-03.1-001 | CR-D-03.1-001 | PASS |
| OBL-D-03.2-001 | CR-D-03.2-001 | PASS |
| OBL-D-03.3-001 | CR-D-03.3-001 | PASS |
| OBL-D-03.4-001 | CR-D-03.4-001 | PASS |
| OBL-D-04.1-001 | CR-D-04.1-001 | PASS |
| OBL-D-04.2-001 | CR-D-04.2-001 | PASS |
| OBL-D-04.3-001 | CR-D-04.3-001 | PASS |
| OBL-D-04.4-001 | CR-D-04.4-001 | PASS |
| OBL-D-05.1-001 | CR-D-05.1-001 | PASS |
| OBL-D-05.2-001 | CR-D-05.2-001 | PASS |
| OBL-D-05.3-001 | CR-D-05.3-001 | PASS |
| OBL-D-05.4-001 | CR-D-05.4-001 | PASS |
| OBL-D-06.1-001 | CR-D-06.1-001 | PASS |
| OBL-D-06.2-001 | CR-D-06.2-001 | PASS |
| OBL-D-06.3-001 | CR-D-06.3-001 | PASS |
| OBL-D-07.1-001 | CR-D-07.1-001 | PASS |
| OBL-D-07.2-001 | CR-D-07.2-001 (TBD — added in follow-on contract — see F-07) | **F-07 (cross-doc orphan)** |
| OBL-D-07.3-001 | CR-D-07.3-001 (TBD — added in follow-on contract — see F-07) | **F-07 (cross-doc orphan)** |
| OBL-D-07.4-001 | CR-D-07.4-001 (TBD — added in follow-on contract — see F-07) | **F-07 (cross-doc orphan)** |
| OBL-D-08.1-001 | CR-D-08.1-001 | PASS |
| OBL-D-08.2-001 | CR-D-08.2-001 | PASS |
| OBL-D-09.1-001 | CR-D-09.1-001 | PASS |
| OBL-D-09.2-001 | CR-D-09.2-001 | PASS |
| OBL-D-09.4-001 | CR-D-09.4-001 | PASS |
| OBL-D-10.1-001 | CR-D-10.1-001 (TBD — added in follow-on contract — see F-07) | **F-07 (cross-doc orphan)** |
| OBL-D-10.2-001 | CR-D-10.2-001 | PASS |
| OBL-D-10.3-001 | CR-D-10.3-001 | PASS |

**Summary:** 30/34 OBLs mapped 1:1 to existing CR rules (88%); 4/34 OBLs have placeholder CR-D-XX.X-001 references (F-07, follow-on contract).

### 3.4 Normative Intensity (NI) Propagation

NI propagation follows rule **DR-002**: `obligationNI = AVG(clauseNIs)` (legacy Doc 08 §3.1). All 34 obligations verified against legacy §6 table (Sprint 6+ adds 4 OBLs each with single CRA source → NI=3.000).

| OBL ID | Source Clause NIs | Derived NI | Propagation Rule | Status |
|--------|-------------------|-----------:|------------------|:------:|
| OBL-D-01.1-001 | 2, 2, 3 | 2.667 | AVG(2,2,3) | PASS |
| OBL-D-01.2-001 | 2, 3 | 2.500 | AVG(2,3) | PASS |
| OBL-D-01.3-001 | 3 | 3.000 | Single source (CRA-C15) | PASS |
| OBL-D-01.4-001 | 2, 3 | 2.500 | AVG(2,3) | PASS |
| OBL-D-02.1-001 | 3, 3 | 3.000 | AVG(3,3) | PASS |
| OBL-D-02.2-001 | 3, 3 | 3.000 | AVG(3,3) | PASS |
| OBL-D-02.3-001 | 3, 3 | 3.000 | AVG(3,3) | PASS |
| OBL-D-03.1-001 | 3 | 3.000 | Single source (CRA-C05) | PASS |
| OBL-D-03.2-001 | 2 | 2.000 | Single source (CRA-C06) | PASS |
| OBL-D-03.3-001 | 3, 3 | 3.000 | AVG(3,3) | PASS |
| OBL-D-03.4-001 | 3 | 3.000 | Single source (CRA-C03) | PASS |
| OBL-D-04.1-001 | 3 | 3.000 | Single source (CRA-C13) | PASS |
| OBL-D-04.2-001 | 2, 3 | 2.500 | AVG(2,3) | PASS |
| OBL-D-04.3-001 | 3, 3, 3 | 3.000 | AVG(3,3,3) | PASS |
| OBL-D-04.4-001 | 2 | 2.000 | Single source (GDPR-C16) | PASS |
| OBL-D-05.1-001 | 3, 3 | 3.000 | AVG(3,3) | PASS |
| OBL-D-05.2-001 | 3, 3 | 3.000 | AVG(3,3) | PASS |
| OBL-D-05.3-001 | 3, 3 | 3.000 | AVG(3,3) | PASS |
| OBL-D-05.4-001 | 3 | 3.000 | Single source (GDPR-C07) | PASS |
| OBL-D-06.1-001 | 3 | 3.000 | Single source (GDPR-C11) | PASS |
| OBL-D-06.2-001 | 3 | 3.000 | Single source (CRA-C18) | PASS |
| OBL-D-06.3-001 | 3 | 3.000 | Single source (GDPR-C12) | PASS |
| OBL-D-07.1-001 | 2, 3, 3 | 2.667 | AVG(2,3,3) | PASS |
| OBL-D-07.2-001 | 3 | 3.000 | Single source (CRA-C02; secure-coding adjacent — dedicated clause TBD) | PASS |
| OBL-D-07.3-001 | 3 | 3.000 | Single source (CRA-C22; CI/CD adjacent — dedicated clause TBD) | PASS |
| OBL-D-07.4-001 | 3 | 3.000 | Single source (CRA-C22; change-management adjacent — dedicated clause TBD) | PASS |
| OBL-D-08.1-001 | 3 | 3.000 | Single source (GDPR-C27) | PASS |
| OBL-D-08.2-001 | 3 | 3.000 | Single source (GDPR-C28) | PASS |
| OBL-D-09.1-001 | 2, 3, 2, 3 | 2.500 | AVG(2,3,2,3) | PASS |
| OBL-D-09.2-001 | 2, 3, 3 | 2.667 | AVG(2,3,3) | PASS |
| OBL-D-09.4-001 | 3, 3 | 3.000 | AVG(3,3) | PASS |
| OBL-D-10.1-001 | 3 | 3.000 | Single source (CRA-C12) | PASS |
| OBL-D-10.2-001 | 3 | 3.000 | Single source (CRA-C14) | PASS |
| OBL-D-10.3-001 | 3, 2 | 2.500 | AVG(3,2) | PASS |

**NI distribution (matches legacy §6 + Sprint 6+ additions):**

| Weight | Count | Percentage |
|--------|------:|-----------:|
| 3.000 | 24 | 70.6% |
| 2.500–2.999 | 7 | 20.6% |
| 2.000–2.499 | 3 | 8.8% |
| <2.000 | 0 | 0.0% |
| **TOTAL** | **34** | **100%** |

**Note:** Legacy §6 reports "Weight 3 Obligations: 20 (87.0%) / Weight 2 Obligations: 3 (13.0%)" — this conflates raw count (20) with legacy "weight-3 bucket" semantics. Sprint 6+ adds 4 OBLs each with NI=3.000 (single CRA source), pushing the Weight-3 bucket from 20 → 24 OBLs. The fine-grained distribution above is authoritative for both Sprint 1 baseline + Sprint 6+ additions.

### 3.5 ID Integrity Check

| Check | Expected | Actual | Status |
|-------|---------:|-------:|:------:|
| Duplicate OBL IDs across Doc 08 | 0 | 0 | PASS |
| Canonical format `OBL-D-XX.X-NNN` | 34/34 | 34/34 | PASS |
| Unique sequence numbers per sub-domain | 34/34 | 34/34 | PASS |
| Gap analysis (any sub-domain skipped) | D-09.3 only (DORA exclusive) | matches corrected ontology | PASS |

**Sub-domain gaps (expected, not findings):**
- `D-09.3` (Asset Inventories) — sole authority DORA, not applicable to TinyTask per ontology (Sprint 6+ after P7 fix removes D-07.2/3/4 and D-10.1 from gaps)
- ~~`D-10.1` (Continuous Security Monitoring) — partially covered via BPR-D-10.2-001 (inherited managed audit-trail) but no dedicated OBL~~ **RESOLVED (Sprint 6+):** D-10.1 now has OBL-D-10.1-001 (added below; CRA sole-authority NI=3.000)
- ~~`D-07.2`, `D-07.3`, `D-07.4` (Secure Coding / CI/CD / Change Mgmt)~~ **RESOLVED (Sprint 6+):** all three now have dedicated OBLs (added below; CRA sole-authority NI=3.000 each)

### 3.6 Phase 1 Ontology Cross-Reference (28 GDPR + 26 CRA)

The 34 obligations derive from 54 source clauses per legacy Doc 08 §5 traceability matrix (Sprint 6+ adds 4 OBLs using shared CRA clause IDs CRA-C02/C22/C12 — dedicated clause allocation deferred to follow-on contract per F-07). These must match the Phase 1 ontology (`00_COMMON/phase1_ontology.yaml` — updated by this contract to `covered_count=34, not_covered_count=4`).

| Regulation | Clauses in Ontology | Clauses in Doc 08 §5 | Status |
|------------|--------------------:|---------------------:|:------:|
| GDPR | 28 | 28 (GDPR-C01..GDPR-C28) | PASS |
| CRA | 26 | 26 (CRA-C01..CRA-C26) | PASS |
| NIS 2 | 0 (not applicable) | 0 | PASS |
| DORA | 0 (not applicable) | 0 | PASS |
| AI Act | 0 (not applicable) | 0 | PASS |
| **TOTAL** | **54** | **54** | **PASS** |

**Ontology cross-reference by sub-domain (canonical mappings):**

| Sub-Domain | GDPR Clauses | CRA Clauses | OBL Count |
|------------|--------------|-------------|----------:|
| D-01.1 | GDPR-C04 | CRA-C07 | 1 |
| D-01.2 | GDPR-C15 | CRA-C08 | 1 |
| D-01.3 | — | CRA-C15 | 1 |
| D-01.4 | GDPR-C05 | CRA-C09 | 1 |
| D-02.1 | — | CRA-C01, CRA-C17 | 1 |
| D-02.2 | — | CRA-C04, CRA-C19 | 1 |
| D-02.3 | — | CRA-C21, CRA-C26 | 1 |
| D-03.1 | — | CRA-C05 | 1 |
| D-03.2 | — | CRA-C06 | 1 |
| D-03.3 | GDPR-C10, GDPR-C17 | — | 1 |
| D-03.4 | — | CRA-C03 | 1 |
| D-04.1 | — | CRA-C13 | 1 |
| D-04.2 | GDPR-C18 | CRA-C11 | 1 |
| D-04.3 | GDPR-C21, GDPR-C23 | CRA-C25 | 1 |
| D-04.4 | GDPR-C16 | — | 1 |
| D-05.1 | GDPR-C01 | CRA-C10 | 1 |
| D-05.2 | GDPR-C02, GDPR-C03 | — | 1 |
| D-05.3 | GDPR-C06 | CRA-C16 | 1 |
| D-05.4 | GDPR-C07 | — | 1 |
| D-06.1 | GDPR-C11 | — | 1 |
| D-06.2 | — | CRA-C18 | 1 |
| D-06.3 | GDPR-C12 | — | 1 |
| D-07.1 | GDPR-C09 | CRA-C02, CRA-C22 | 1 |
| D-07.2 | — | CRA-C02 (shared with D-07.1; dedicated clause TBD in follow-on contract) | 1 |
| D-07.3 | — | CRA-C22 (shared with D-07.1; dedicated clause TBD in follow-on contract) | 1 |
| D-07.4 | — | CRA-C22 (shared with D-07.1; dedicated clause TBD in follow-on contract) | 1 |
| D-08.1 | GDPR-C27 | — | 1 |
| D-08.2 | GDPR-C28 | — | 1 |
| D-09.1 | GDPR-C08, GDPR-C25, GDPR-C26 | CRA-C24 | 1 |
| D-09.2 | GDPR-C20, GDPR-C24 | CRA-C23 | 1 |
| D-09.4 | GDPR-C13, GDPR-C22 | — | 1 |
| D-10.1 | — | CRA-C12 (per `00_Taxonomy_Reference.md` §3 D-10 mapping; unmapped in Doc 08 prior to Sprint 6+) | 1 |
| D-10.2 | — | CRA-C14 | 1 |
| D-10.3 | GDPR-C19 | CRA-C20 | 1 |

**Known ontology issue (preserved from ontology file header):** The ontology YAML notes a data integrity issue where `GDPR-C08` is mapped to different articles in the ontology vs the Python scripts. Doc 08 §5 follows the ontology mapping (GDPR-C08 → D-09.1). This is out of scope for Sprint 1 and is documented in the ontology file.

### 3.7 Findings — Flagged for Human Review

| ID | Severity | Description | Recommendation |
|----|----------|-------------|----------------|
| **F-01** | LOW | OBL-D-01.3-001 (Cryptographic Key Management) has no corresponding PO or SO in Doc 10. CR-D-01.3-001 exists and references `PO-D-01.3-001` — but that goal ID does not exist in Doc 10. | Either (a) add PO-D-01.3-001 to Doc 10, or (b) update CR-D-01.3-001 to reference an alternative goal. Sprint 5 DEEP enrichment cannot proceed for this OBL until resolved. |
| **F-02** | MEDIUM | OBL-D-09.1-001 and OBL-D-09.2-001 each have BOTH a PO and an SO. The strict 1:1 mapping rule is violated for these 2 OBLs. | Acceptable as-designed (D-09 governance covers both privacy policy and security policy objectives); document the dual-coverage as intentional in the 1:1 mapping definition. |
| **F-03** | LOW | Doc 11 §4 row for `CR-D-01.3-001` references `PO-D-01.3-001` in the "Related Goals" column — but no PO-D-01.3-001 exists. | Same root cause as F-01. Fixing the goal either creates or removes this reference. |
| **F-04** | INFO | Doc 10 §3.2 summary claims "12 Privacy Operational Objectives" but §3.1 lists only 11; Doc 10 §4.2 summary claims "18 Security Operational Objectives" but §4.1 lists 20. Total goal IDs = 31, not 30. | Stale summary counts from Doc 10 v1.0/v1.1. Doc 10 §3 has its own §3 findings. |
| **F-05** | INFO | Ontology file (`phase1_ontology.yaml` header) flags a known `GDPR-C08` mapping discrepancy between the YAML and Python scripts. Doc 08 follows the YAML. | Out of scope for Sprint 1. Tracked as legacy data integrity issue per ontology file. |
| **F-06** | INFO | Stale `SO-D-02.4-001` reference in Doc 10 §10 version history (renamed to `SO-D-06.2-001` in v1.1). | Cosmetic only — version history note, not a data row. |
| **F-07** | MEDIUM | **Sprint 6+ (P7 orphan fix):** 4 new OBLs added (D-07.2/3/4, D-10.1) reference placeholder PO/SO/CR-D-XX.X-001 IDs that do not yet exist in Doc 10 §3/§4 (no PO/SO-D-07.2/3/4 or D-10.1) or Doc 11 §4 (no CR-D-07.2/3/4 or CR-D-10.1). Cross-doc orphan risk is structural until the follow-on contract populates Doc 10 + Doc 11. | Add PO-D-07.2-001 to Doc 10 §3.1; add SO-D-07.3-001, SO-D-07.4-001, SO-D-10.1-001 to Doc 10 §4.1; add CR-D-07.2-001, CR-D-07.3-001, CR-D-07.4-001, CR-D-10.1-001 to Doc 11 §4 in a follow-on contract. Current Doc 08 entries use `(TBD)` markers explicitly so validators do not flag false-positive orphan cycles. |
| **F-08** | INFO | `phase1_ontology.yaml` exists in both `00_COMMON/` (canonical, updated by this contract) and `01_PHASE1_CONTEXT_RICH/` (Rich Mode twin, NOT updated by this contract — out-of-scope per user constraint). Doc 08 now references the corrected 00_COMMON ontology (covered_count=34, not_covered_count=4). | Update `01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` in a follow-on contract to restore twin consistency. |
| **F-09** | INFO | `00_Taxonomy_Reference.md` §3 lines 117-119 still classifies D-07.2/3/4 as "DORA sole authority" / "NIS 2 sole authority" — contradicts the corrected ontology (which now classifies them as CRA-covered per Doc 07 §3). The reference is the canonical taxonomy outside Case_01 scope; Doc 08 is internally consistent against the corrected ontology. | Reconcile `00_Taxonomy_Reference.md` §3 with the per-case ontology correction in a follow-on cross-case contract. |

### 3.8 Reconciliation Verdict

| Dimension | Status |
|-----------|:------:|
| Obligation count (34) | PASS |
| OBL ↔ CR mapping (30/34 existing + 4/34 TBD placeholders) | **CONDITIONAL_PASS** (F-07 cross-doc orphans) |
| NI propagation (34/34) | PASS |
| ID integrity (no duplicates, canonical format) | PASS |
| Phase 1 ontology cross-reference (54 clauses) | PASS |
| OBL ↔ Goal mapping (strict 1:1) | **CONDITIONAL_PASS** (F-01 carry-over + F-07 cross-doc orphans) |

**Sprint 6+ verdict for Doc 08 (post P7 orphan fix):** **CONDITIONAL_PASS** — 30 OBLs unchanged from Sprint 5; 4 new OBLs (D-07.2/3/4, D-10.1) added with CRA sole-authority mapping and `(TBD)` placeholders for PO/SO/CR. F-07 cross-doc orphan tracking is explicit and parallels F-01/F-03 carry-over. Doc 08 is internally consistent against the corrected `phase1_ontology.yaml` (`covered_count=34, not_covered_count=4`); F-08/F-09 flag out-of-scope follow-on contracts for the twin ontology + Taxonomy Reference.

---

## 4. REGULATORY OBLIGATIONS CATALOG

> **Sprint 4 (this sprint):** Ported legacy `02_PHASE2_RULES/08_Obligation_Derivation.md` §4 catalog tables into Rich Mode with 17 columns (11 legacy fields + 6 new Sprint 4 fields: Owner, Verification Criteria, Maturity Score, Implementation Priority, Affected Stakeholders, Regulatory Reporting). 30 obligations × 17 columns = 510 cells (Sprint 4 baseline; Sprint 6+ adds 4 OBLs → 34 × 17 = 578 cells). The 6 new columns contribute 30 × 6 = **180 cells** (the Sprint 4 deliverable count).

### D-01: Data Protection & Encryption Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | implementation_tier | evidence_depth | control_selection | Activation Nature | Owner | Verification Criteria | Maturity Score | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----: | ---------------- | ---------------- | --------------------- | ---------------- | ------------------- | ------------------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- |
| OBL-D-01.1-001 | Encrypt all personal and sensitive data at rest using industry-standard algorithms | GDPR-C04, GDPR-C14, CRA-C07 | D-01.1 | 2.667 | CONTINUOUS | CONTROLLER, PROCESSOR | LIGHTWEIGHT | Managed-service config documented + annual review; no dedicated in-house program | managed hosting encryption with managed key custody (strong symmetric encryption with documented rotation cadence); no company-owned key custody program | STRUCTURAL | CTO + Lead Dev | strong symmetric encryption + key rotation audit | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.DS-01, PR.DS-02, PR.DS-10, PR.IR-01, PR.PS-06 |
| OBL-D-01.2-001 | Encrypt all data transmitted across networks using protection cryptographic for confidentiality and integrity in transit | GDPR-C15, CRA-C08 | D-01.2 | 2.500 | CONTINUOUS | CONTROLLER, PROCESSOR | LIGHTWEIGHT | Managed-service config documented + annual review | managed edge TLS termination with documented certificate auto-renewal | STRUCTURAL | CTO + Lead Dev | modern TLS cert audit | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.DS-02, PR.IR-01 |
| OBL-D-01.3-001 | Implement secure cryptographic key management with authentication and integrity verification | CRA-C15 | D-01.3 | 3.000 | CONTINUOUS | MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | managed key lifecycle with documented rotation cadence (managed by hosting platform) | STRUCTURAL | CTO + Lead Dev | key rotation evidence | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | — |
| OBL-D-01.4-001 | Protect data against unauthorised manipulation and accidental loss | GDPR-C05, CRA-C09 | D-01.4 | 2.500 | CONTINUOUS | CONTROLLER, PROCESSOR | LIGHTWEIGHT | Managed-service config documented + annual review | cryptographic integrity check + database constraints via managed database | STRUCTURAL | CTO + Lead Dev | HMAC + DB constraint check | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.DS-01, PR.DS-10 |

**D-01 Summary:** 4 obligations | Avg NI: 2.667 | All CONTINUOUS | All STRUCTURAL

---

### D-02: Vulnerability Management Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | implementation_tier | evidence_depth | control_selection | Activation Nature | Owner | Verification Criteria | Maturity Score | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----: | ---------------- | ---------------- | --------------------- | ---------------- | ------------------- | ------------------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- |
| OBL-D-02.1-001 | Deliver product with no known exploitable vulnerabilities; maintain SBOM | CRA-C01, CRA-C17 | D-02.1 | 3.000 | ONE_TIME, CONTINUOUS | MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | automated vulnerability scanner + managed dependency audit in CI; OSS advisories | STRUCTURAL | CTO + Lead Dev + Procurement | automated vulnerability scanner + managed dependency audit zero-CVE | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | ENISA 24h (CRA) | ID.IM-02, ID.RA-01, ID.RA-05, PR.PS-02 |
| OBL-D-02.2-001 | Enable automatic security updates; remediate vulnerabilities promptly | CRA-C04, CRA-C19 | D-02.2 | 3.000 | ONE_TIME, TRIGGERED | MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | managed automated patch pipeline for OS + dependency updates | STRUCTURAL | CTO + Lead Dev + Procurement | 72h SLA patch test | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | ENISA 24h (CRA) | — |
| OBL-D-02.3-001 | Publish coordinated vulnerability disclosure policy; report severe incidents to ENISA/CSIRT | CRA-C21, CRA-C26 | D-02.3 | 3.000 | CONTINUOUS, TRIGGERED | MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | security.txt at `/.well-known/security.txt`; CVD page | STRUCTURAL | CTO + Lead Dev + Procurement | security.txt + 24h report | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | ENISA 24h (CRA) | — |

**D-02 Summary:** 3 obligations | Avg NI: 3.000 | CRA-only domain (GDPR gap)

---

### D-03: Access Control Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | implementation_tier | evidence_depth | control_selection | Activation Nature | Owner | Verification Criteria | Maturity Score | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----: | ---------------- | ---------------- | --------------------- | ---------------- | ------------------- | ------------------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- |
| OBL-D-03.1-001 | Implement authentication and access control measures for all users | CRA-C05 | D-03.1 | 3.000 | ONE_TIME | MANUFACTURER | MINIMAL | Supplier attestation on file (provider ISO 27001 attestation) + 1-page internal statement | managed identity service baseline; managed identity provider security documentation | STRUCTURAL | CTO + Lead Dev | managed identity service baseline | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | GV.OC-03, GV.PO-02, PR.AA-02, PR.AA-03, PR.DS-10 |
| OBL-D-03.2-001 | Enable multi-factor authentication where appropriate | CRA-C06 | D-03.2 | 2.000 | ONE_TIME | MANUFACTURER | MINIMAL | Supplier attestation on file + 1-page internal statement | managed identity service MFA; documented key custody | STRUCTURAL | CTO + Lead Dev | MFA enforcement test | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | — |
| OBL-D-03.3-001 | Restrict access to authorised personnel only; enforce least privilege | GDPR-C10, GDPR-C17 | D-03.3 | 3.000 | ONE_TIME, CONTINUOUS | CONTROLLER, PROCESSOR | LIGHTWEIGHT | Managed-service config documented + annual review | managed identity service RBAC | STRUCTURAL | CTO + Lead Dev | RBAC quarterly review | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.AA-05, PR.AA-06, PR.AT-02 |
| OBL-D-03.4-001 | Disable unused ports/services; no default passwords; secure default configuration | CRA-C03 | D-03.4 | 3.000 | ONE_TIME | MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | Secure defaults via managed identity provider configuration | STRUCTURAL | CTO + Lead Dev | hardened-default review | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.DS-10, PR.PS-01, PR.PS-06 |

**D-03 Summary:** 4 obligations | Avg NI: 2.750 | Mixed GDPR/CRA coverage

---

### D-04: Incident Response Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | implementation_tier | evidence_depth | control_selection | Activation Nature | Owner | Verification Criteria | Maturity Score | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----: | ---------------- | ---------------- | --------------------- | ---------------- | ------------------- | ------------------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- |
| OBL-D-04.1-001 | Design system to limit severity of exploits; implement fail-safe mechanisms | CRA-C13 | D-04.1 | 3.000 | ONE_TIME | MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | managed monitoring with documented incident classification + managed notification routing | STRUCTURAL (always active) | CTO + DPO + Compliance Lead | managed monitoring alarms active | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | CNPD 72h (GDPR) | DE.AE-02, DE.CM-01, DE.CM-03, DE.CM-09, RS.MA-02 |
| OBL-D-04.2-001 | Restore availability after incidents; build resilience against DoS attacks | GDPR-C18, CRA-C11 | D-04.2 | 2.500 | TRIGGERED, ONE_TIME | CONTROLLER, PROCESSOR, MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | Documented 4h containment playbook | STRUCTURAL (always active) | CTO + DPO + Compliance Lead | DoS resilience drill | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | CNPD 72h (GDPR) | PR.DS-01, RS.MI-01, RS.MI-02 |
| OBL-D-04.3-001 | Notify supervisory authority within 72h (GDPR) / 24h (CRA) of breaches; processor→controller without undue delay (GDPR Art. 33(2)) | GDPR-C21, GDPR-C23, CRA-C25 | D-04.3 | 3.000 | TRIGGERED | CONTROLLER, PROCESSOR, MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | max-SLA 24h internal; unified incident workflow | **CONTEXTUAL** — GDPR triggers on personal data breach; CRA triggers on exploited vulnerability. Both activate simultaneously only in compound event (EVT-001). See T-H-001. | CTO + DPO + Compliance Lead | 24h dual-notification SLA | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | CNPD 72h + ENISA 24h (max-SLA routing) | GV.OC-03, ID.RA-06, PR.DS-01, PR.DS-10, PR.IR-03 |
| OBL-D-04.4-001 | Ensure ongoing availability and ability to restore data after incident | GDPR-C16 | D-04.4 | 2.000 | CONTINUOUS | CONTROLLER, PROCESSOR | LIGHTWEIGHT | Managed-service config documented + annual review | managed backup with documented RTO/RPO; RTO 24h (per Critical Analysis §4) | STRUCTURAL (always active) | CTO + DPO + Compliance Lead | managed backup RTO 24h | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | CNPD 72h (GDPR) | PR.DS-01, PR.IR-04, RC.RP-04 |

**D-04 Summary:** 4 obligations | Avg NI: 2.625 | **1 contextual (OBL-D-04.3-001)** | **Tension T-H-001:** D-04.3 timing conflict (72h vs 24h) — only active when compound event occurs

**Nuance — Processor Breach Notification (GDPR Art. 33(2)):** As a processor for B2B client content, TinyTask must notify its clients (controllers) of personal data breaches "without undue delay" — a distinct obligation from the 72h controller→SA notification in Art. 33(1). The processor→controller clock has no fixed numeric deadline. For TinyTask, this means an internal SLA should be defined (e.g., notify clients within 4-8 hours of breach awareness), separate from the client's 72h SA notification obligation. OBL-D-04.3-001 (which now carries `obligatedParty: CONTROLLER, PROCESSOR, MANUFACTURER`) covers the controller→SA timing (72h, Art. 33(1)) and the processor→controller "without undue delay" timing (Art. 33(2)) as parallel obligations under the same row; a split into two obligation IDs (one for the controller→SA clock, one for the processor→controller clock) is recommended in a future refinement but is intentionally left unified here to keep the tension T-H-001 (D-04.3 72h vs 24h) co-located.

---

### D-05: Data Lifecycle Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | implementation_tier | evidence_depth | control_selection | Activation Nature | Owner | Verification Criteria | Maturity Score | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----: | ---------------- | ---------------- | --------------------- | ---------------- | ------------------- | ------------------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- |
| OBL-D-05.1-001 | Process only data adequate, relevant and limited to what is necessary | GDPR-C01, CRA-C10 | D-05.1 | 3.000 | CONTINUOUS, ONE_TIME | CONTROLLER, MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | Field-level enforcement in schema | STRUCTURAL | CTO + DPO | Field-level enforcement | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | GV.OC-03, GV.PO-01, GV.PO-02, ID.AM-03, PR.AA-02, PR.DS-10 |
| OBL-D-05.2-001 | Do not keep personal data longer than necessary for purpose | GDPR-C02, GDPR-C03 | D-05.2 | 3.000 | CONTINUOUS | CONTROLLER, PROCESSOR | LIGHTWEIGHT | Managed-service config documented + annual review | Retention policy (7y audit logs; 30d DSAR working data) | STRUCTURAL | CTO + DPO | Retention policy audit | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | ID.AM-03, PR.DS-10 |
| OBL-D-05.3-001 | Enable complete and secure data deletion on user request | GDPR-C06, CRA-C16 | D-05.3 | 3.000 | TRIGGERED, ONE_TIME | CONTROLLER, PROCESSOR, MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | Erasure API endpoint | STRUCTURAL | CTO + DPO | Erasure API test (7d) | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | GV.SC-04, PR.DS-10, RS.CO-02 |
| OBL-D-05.4-001 | Provide data export in structured, machine-readable format on request | GDPR-C07 | D-05.4 | 3.000 | TRIGGERED | CONTROLLER | LIGHTWEIGHT | Managed-service config documented + annual review | JSON export endpoint | STRUCTURAL | CTO + DPO | JSON export test (48h) | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.DS-10 |

**D-05 Summary:** 4 obligations | Avg NI: 3.000 | GDPR-dominant domain

---

### D-06: Supply Chain Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | implementation_tier | evidence_depth | control_selection | Activation Nature | Owner | Verification Criteria | Maturity Score | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----: | ---------------- | ---------------- | --------------------- | ---------------- | ------------------- | ------------------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- |
| OBL-D-06.1-001 | Use only processors providing sufficient guarantees | GDPR-C11 | D-06.1 | 3.000 | ONE_TIME | CONTROLLER | MINIMAL | Supplier attestation on file + 1-page internal statement | DPA validation against GDPR Art. 28; supplier security clauses | STRUCTURAL | CTO + Lead Dev + Procurement | DPA + documented third-party security attestation | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | GV.SC-02, GV.SC-03 |
| OBL-D-06.2-001 | Document all third-party components in machine-readable format (SBOM) | CRA-C18 | D-06.2 | 3.000 | CONTINUOUS | MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | machine-readable SBOM in CI/CD per release | STRUCTURAL | CTO + Lead Dev + Procurement | machine-readable SBOM per release | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | — |
| OBL-D-06.3-001 | Bind processors to security obligations via Data Processing Agreement | GDPR-C12 | D-06.3 | 3.000 | ONE_TIME | CONTROLLER, PROCESSOR | LIGHTWEIGHT | Managed-service config documented + annual review | DPA template + supplier security clauses | STRUCTURAL | CTO + Lead Dev + Procurement | DPA template + clauses | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | DE.CM-06, GV.OC-03, GV.RR-02, GV.SC-01, GV.SC-02, GV.SC-03 |

**D-06 Summary:** 3 obligations | Avg NI: 3.000 | **OBL-D-06.2-001:** CRA sole authority

---

### D-07: Secure Development Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | implementation_tier | evidence_depth | control_selection | Activation Nature | Owner | Verification Criteria | Maturity Score | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----: | ---------------- | ---------------- | --------------------- | ---------------- | ------------------- | ------------------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- |
| OBL-D-07.1-001 | Integrate data protection and security into design from outset; secure by default | GDPR-C09, CRA-C02, CRA-C22 | D-07.1 | 2.667 | ONE_TIME | CONTROLLER, PROCESSOR, MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | secure-development-framework + maturity assessment baseline | STRUCTURAL (always active — both regulations apply during any design phase) | CTO + Lead Dev | secure-development-framework + maturity assessment | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.DS-01, PR.DS-10, PR.PS-01, PR.PS-06 |
| OBL-D-07.2-001 | Apply secure coding standards to product source code; limit attack surface through code review and static analysis | CRA-C02 (shared with D-07.1 — dedicated TBD) | D-07.2 | 3.000 | CONTINUOUS | MANUFACTURER | LIGHTWEIGHT | Managed dependency scan + SAST + PR review evidence | secure coding standards + SAST + peer review | STRUCTURAL | CTO + Lead Dev | secure-coding-standards + SAST + peer-review evidence | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.PS-01, PR.PS-02, PR.IP-12 (legacy CSF 1.1; PR.PS-02 CSF 2.0) |
| OBL-D-07.3-001 | Implement security gates in CI/CD pipeline; ensure build-time artefact integrity; SBOM gate | CRA-C22 (shared with D-07.1 — dedicated TBD) | D-07.3 | 3.000 | CONTINUOUS | MANUFACTURER | LIGHTWEIGHT | GitHub Actions workflow + SBOM artefact on each release | CI security gates + SBOM generation + dependency gate | STRUCTURAL | CTO + Lead Dev | CI security gates pass + SBOM on every release | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.IP-12 (legacy CSF 1.1; PR.PS-02 CSF 2.0), ID.SC-04 |
| OBL-D-07.4-001 | Implement documented change management procedures; secure update delivery channel | CRA-C22 (shared with D-07.1 — dedicated TBD) | D-07.4 | 3.000 | CONTINUOUS | MANUFACTURER | LIGHTWEIGHT | CAB approval log + signed release artefacts | CAB approval + signed artefacts + change-management log | STRUCTURAL | CTO + Lead Dev | CAB approval + signed artefacts on every production release | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.IP-12 (legacy CSF 1.1; PR.PS-02 CSF 2.0), ID.SC-04 |

**D-07 Summary:** 4 obligations | Avg NI: 2.917 | **Tension T-M-002:** Intensity gap (GDPR NI=2 vs CRA NI=3) — structural, always active

**Nuance — CRA Support Period (Art. 13(8)):** The CRA requires a minimum **5-year support period** from product placement (or expected use time if less). For TinyTask's SaaS, each release has its own 5-year support clock. This translates to an ongoing obligation to provide security patches and vulnerability fixes for at least 5 years per release. This is captured under the existing CRA clauses (CRA-C04, CRA-C19) but the 5-year quantitative threshold should be noted in the Rules Catalog.

**Nuance — CRA Security Update Retention (Art. 13(9)):** Security updates must remain available for a minimum of **10 years** or the support period, whichever is longer. This means old TinyTask SaaS versions' patches must be archived for at least a decade. This is a separate quantitative threshold from the 5-year support period.

---

### D-08: Human Factors Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | implementation_tier | evidence_depth | control_selection | Activation Nature | Owner | Verification Criteria | Maturity Score | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----: | ---------------- | ---------------- | --------------------- | ---------------- | ------------------- | ------------------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- |
| OBL-D-08.1-001 | Train staff involved in processing operations on security awareness | GDPR-C27 | D-08.1 | 3.000 | PERIODIC | CONTROLLER, PROCESSOR | MINIMAL | Supplier attestation on file + 1-page internal statement | Vendor security awareness documentation on file | STRUCTURAL | CTO + HR + DPO | Annual security training | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | GV.OV-03, ID.IM-02, PR.AA-05, PR.AT-01, PR.AT-02 |
| OBL-D-08.2-001 | Raise awareness and train staff with role-specific security obligations | GDPR-C28 | D-08.2 | 3.000 | PERIODIC | CONTROLLER, PROCESSOR | LIGHTWEIGHT | Managed-service config documented + annual review | Annual security awareness email + role-specific docs (admin/dev/DPO) | STRUCTURAL | CTO + HR + DPO | Role-specific training | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | PR.AT-01, PR.AT-02 |

**D-08 Summary:** 2 obligations | Avg NI: 3.000 | GDPR-only domain

---

### D-09: Governance & Documentation Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | implementation_tier | evidence_depth | control_selection | Activation Nature | Owner | Verification Criteria | Maturity Score | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----: | ---------------- | ---------------- | --------------------- | ---------------- | ------------------- | ------------------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- |
| OBL-D-09.1-001 | Implement appropriate technical/organisational measures; document policies; maintain technical documentation for 10 years | GDPR-C08, GDPR-C25, GDPR-C26, CRA-C24 | D-09.1 | 2.500 | CONTINUOUS, ONE_TIME | CONTROLLER, PROCESSOR, MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | Security policy template (Doc 09 family input) | STRUCTURAL (always active) | CTO + DPO + Compliance Lead + Legal | ISMS documentation audit | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | CNPD + ENISA (periodic) | GV.OC-02, GV.OC-03, GV.OV-03, GV.PO-01, GV.PO-02, GV.RM-04 |
| OBL-D-09.2-001 | Conduct DPIA prior to high-risk processing; cybersecurity risk assessment before market | GDPR-C20, GDPR-C24, CRA-C23 | D-09.2 | 2.667 | PERIODIC, ONE_TIME | CONTROLLER, MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | DPIA template + CRA risk assessment template (unified, dual-output) | STRUCTURAL (always active — both triggers permanently satisfied by TinyTask's business model) | CTO + DPO + Compliance Lead + Legal | Unified assessment template | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | CNPD + ENISA (periodic) | GV.OC-03, GV.OV-03, GV.PO-01, GV.RR-02, GV.SC-02, GV.SC-03 |
| OBL-D-09.4-001 | Maintain records of processing activities and breach documentation | GDPR-C13, GDPR-C22 | D-09.4 | 3.000 | CONTINUOUS, TRIGGERED | CONTROLLER, PROCESSOR | LIGHTWEIGHT | Managed-service config documented + annual review | RoPA template (Doc 09 input) | STRUCTURAL (always active) | CTO + DPO + Compliance Lead + Legal | RoPA + breach log | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | CNPD + ENISA (periodic) | DE.AE-03, GV.PO-02, ID.AM-03, PR.AA-02, PR.DS-10, PR.PS-04 |

**D-09 Summary:** 3 obligations | Avg NI: 2.722 | **Tension T-M-001:** Frequency alignment (both ONE_TIME) — structural, always active

---

### D-10: Monitoring & Audit Obligations

| Obligation ID | Obligation Description | Source Clauses | Sub-Domain | NI | obligationType | obligatedParty | implementation_tier | evidence_depth | control_selection | Activation Nature | Owner | Verification Criteria | Maturity Score | Implementation Priority | Affected Stakeholders | Regulatory Reporting | CSF Anchors |
| --------------- | ------------------------ | ---------------- | ------------ | ----: | ---------------- | ---------------- | --------------------- | ---------------- | ------------------- | ------------------- | ------- | ---------------------- | --------------- | ------------------------ | ---------------------- | ---------------------- | --- |
| OBL-D-10.1-001 | Establish continuous security monitoring for the product and supporting systems; vulnerability handling per CRA Art. 14 | CRA-C12 | D-10.1 | 3.000 | CONTINUOUS | MANUFACTURER | LIGHTWEIGHT | Managed-monitoring config documented + monthly review minutes | managed monitoring + alert taxonomy + vulnerability handling workflow | STRUCTURAL | CTO + Lead Dev | managed-monitoring + alert-taxonomy + monthly review | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | ENISA 24h (CRA Art. 14 — exploited-vulnerability reporting) | DE.CM-01, ID.RA-05, PR.PS-02, PR.IP-12 (legacy CSF 1.1; PR.PS-02 CSF 2.0) |
| OBL-D-10.2-001 | Log security-relevant events; maintain audit trail of access | CRA-C14 | D-10.2 | 3.000 | CONTINUOUS | MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | managed audit-trail service + tamper-evident managed object storage log bucket | STRUCTURAL | CTO + Lead Dev | managed audit-trail review | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | DE.AE-03, GV.OV-03, GV.PO-02, ID.AM-03, PR.DS-10, PR.PS-04 |
| OBL-D-10.3-001 | Regularly test effectiveness of technical and organisational measures | GDPR-C19, CRA-C20 | D-10.3 | 2.500 | PERIODIC | CONTROLLER, PROCESSOR, MANUFACTURER | LIGHTWEIGHT | Managed-service config documented + annual review | Quarterly compliance review checklist | STRUCTURAL | CTO + Lead Dev | Quarterly compliance review | 1/4 → 3/4 | HIGH | Customers, DPO, CTO, ENISA | Internal audit only | ID.IM-02, ID.IM-04, ID.RA-01, ID.RA-05, ID.RA-06, PR.PS-02 |

**D-10 Summary:** 3 obligations | Avg NI: 2.833 | Mixed coverage (D-10.1 + D-10.2 + D-10.3 all CRA-led)

---

### 4.1 NI Reconciliation Notes (Resolves F-10)

> **Sprint 4 sub-section.** This sub-section documents the deliberate divergence between Rich §4 NI values and legacy `02_PHASE2_RULES/08_Obligation_Derivation.md` §6 / `02_PHASE2_RULES/11_Rules_Catalog.md` §4 NI values. The Rich Mode adopts the **DR-002 recomputed values** (`AVG(clauseNIs)`) per the derivation rule in legacy §3.1.

**NI divergence table (Rich vs Legacy):**

| Obligation | Rich NI (DR-002 AVG) | Legacy NI (Doc 08 §6 / Doc 11 §4) | Source Clause NIs | Resolution |
|------------|---------------------:|----------------------------------:|-------------------|------------|
| **OBL-D-01.4-001** | **2.500** | 3.000 (legacy) | GDPR-C05 = 2, CRA-C09 = 3 → AVG = 2.500 | **Rich wins** — DR-002 AVG(2,3) = 2.500; legacy Doc 11 §4 row CR-D-01.4-001 incorrectly carried 3.000. |
| **OBL-D-09.1-001** | **2.500** | 2.750 (legacy) | GDPR-C08 = 2, GDPR-C25 = 3, GDPR-C26 = 2, CRA-C24 = 3 → AVG = 2.500 | **Rich wins** — DR-002 AVG(2,3,2,3) = 2.500; legacy Doc 11 §4 row CR-D-09.1-001 carried 2.750 (no derivation rule justification). |

**Cross-impact on Doc 11 §4 (CR-D-01.4-001 and CR-D-09.1-001):**

| CR Rule | Rich NI | Legacy NI | Notes |
|---------|--------:|----------:|-------|
| CR-D-01.4-001 | 2.500 | 3.000 | NI column in Doc 11 §4 will be 2.500 (carried into §4 catalog port in Doc 11) |
| CR-D-09.1-001 | 2.500 | 2.750 | NI column in Doc 11 §4 will be 2.500 |

**Catalog average NI recomputed:** Legacy Doc 11 §6 dashboard reports 2.842; Sprint 1 §3.4 reports 2.817 (DR-002 AVG recompute). With the F-10 reconciliation applied (Rich values authoritative), the average NI = **2.800** (lower than both legacy 2.842 and Sprint 1 2.817 because both F-10 corrections pull the average down: 3.000→2.500 is −0.500, 2.750→2.500 is −0.250; impact = (−0.500 + −0.250) / 30 = −0.025).

**Human arbiter decision (recorded for Sprint 5):** Rich Mode uses **DR-002 AVG = 2.500** as authoritative for OBL-D-01.4-001 and OBL-D-09.1-001. If legacy is later ratified as authoritative, the two rows revert; for now, all downstream Sprint 5 priority fields derive from the Rich NI values.

---

## 5. OBLIGATION DETAIL CARDS (Rich Mode — Sprint 5)


> **Sprint 5/6+ scope.** Each of the 34 obligations enumerated in §4 has a dedicated detail card below with 17 fields: description (2–3 paragraphs covering what + why + corpus-derived context), scope, out-of-scope, source article, NIST CSF anchors, verification criteria, verification method, owner, status, dependencies, risk-if-not-met, affected stakeholders, maturity score, implementation priority, regulatory reporting, external auditor, and supervisory body. Total cells populated = 34 cards × 17 fields = 578 cells (was 510 before Sprint 6+; +68 cells from 4 new OBLs).


> **Reporting routing defaults:** D-04.3 → max-SLA 24h (both CNPD 72h and ENISA 24h routed simultaneously per T-001); D-04 (others) → CNPD 72h (GDPR); D-02 → ENISA 24h (CRA); D-09 → CNPD + ENISA periodic; all others → Internal audit only.


> **Owner matrix (consistent across docs):** D-01 → CTO + Lead Dev | D-02 → CTO + Lead Dev + Procurement | D-03 → CTO + Lead Dev | D-04 → CTO + DPO + Compliance Lead | D-05 → CTO + DPO | D-06 → CTO + Lead Dev + Procurement | D-07 → CTO + Lead Dev | D-08 → CTO + HR + DPO | D-09 → CTO + DPO + Compliance Lead + Legal | D-10 → CTO + Lead Dev.


> **Maturity + Priority defaults:** Maturity = 1/4 → 3/4 (LIGHTWEIGHT target); Priority = HIGH for all P1 obligations, MEDIUM where proportionality allows (P2). Reporting routing per the rules above. External auditor is uniformly managed hosting provider ISO 27001 attestation leveraged under the managed-service configuration model.


> **F-10 NI reconciliation (from Sprint 4 §4.1):** OBL-D-01.4-001 and OBL-D-09.1-001 use Rich NI = 2.500 (DR-002 AVG) as authoritative. Priority for these two cards is HIGH (not MEDIUM) because the AVG pulls down from a CRA NI=3 component, which is the operationally dominant driver.


---


### 5.0 Sprint 5 Detail-Card Index


Compact navigation table — for the full 17-field card, jump to the corresponding subsection below.


| OBL ID | Sub-Domain | Title | Owner | Priority | Maturity (Current → Target) | Status | Reporting |

|--------|------------|-------|-------|----------|-----------------------------|--------|-----------|
| OBL-D-01.1-001 | D-01.1 | Data Encryption at Rest | CTO + Lead Dev | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-01.2-001 | D-01.2 | Data Encryption in Transit | CTO + Lead Dev | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-01.3-001 | D-01.3 | Cryptographic Key Management | CTO + Lead Dev | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-01.4-001 | D-01.4 | Data Integrity Protection | CTO + Lead Dev | HIGH | 1/4 → 3/4 | TODO | Internal audit only |
| OBL-D-02.1-001 | D-02.1 | No Known Vulnerabilities + SBOM | CTO + Lead Dev + Procurement | HIGH | 2/4 → 3/4 | TODO | ENISA 24h (CRA Art. 14 exploited-vulnerability reporting) |
| OBL-D-02.2-001 | D-02.2 | Automatic Security Updates | CTO + Lead Dev + Procurement | HIGH | 2/4 → 3/4 | TODO | ENISA 24h (CRA Art. 14 exploited-vulnerability reporting) |
| OBL-D-02.3-001 | D-02.3 | CVD Policy + ENISA Reporting | CTO + Lead Dev + Procurement | HIGH | 1/4 → 3/4 | TODO | ENISA 24h (CRA Art. 14 exploited-vulnerability reporting) |
| OBL-D-03.1-001 | D-03.1 | Authentication Controls | CTO + Lead Dev | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-03.2-001 | D-03.2 | Multi-Factor Authentication | CTO + Lead Dev | MEDIUM | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-03.3-001 | D-03.3 | Least Privilege + RBAC | CTO + Lead Dev | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-03.4-001 | D-03.4 | Secure Default Configuration | CTO + Lead Dev | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-04.1-001 | D-04.1 | Exploit Severity Limitation | CTO + DPO + Compliance Lead | HIGH | 2/4 → 3/4 | TODO | CNPD 72h (GDPR Art. 33 — controller notification) |
| OBL-D-04.2-001 | D-04.2 | Availability Restoration + DoS Resilience | CTO + DPO + Compliance Lead | HIGH | 2/4 → 3/4 | TODO | CNPD 72h (GDPR Art. 33 — controller notification) |
| OBL-D-04.3-001 | D-04.3 | Breach Notification (T-001) | CTO + DPO + Compliance Lead | HIGH | 2/4 → 3/4 | TODO | CNPD 72h + ENISA 24h (max-SLA routing — see T-001) |
| OBL-D-04.4-001 | D-04.4 | Data Restoration Post-Incident | CTO + DPO + Compliance Lead | HIGH | 2/4 → 3/4 | TODO | CNPD 72h (GDPR Art. 33 — controller notification) |
| OBL-D-05.1-001 | D-05.1 | Data Minimization | CTO + DPO | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-05.2-001 | D-05.2 | Storage Limitation | CTO + DPO | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-05.3-001 | D-05.3 | Right to Erasure | CTO + DPO | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-05.4-001 | D-05.4 | Right to Data Portability | CTO + DPO | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-06.1-001 | D-06.1 | Processor Sufficient Guarantees | CTO + Lead Dev + Procurement | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-06.2-001 | D-06.2 | SBOM Documentation | CTO + Lead Dev + Procurement | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-06.3-001 | D-06.3 | Data Processing Agreement | CTO + Lead Dev + Procurement | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-07.1-001 | D-07.1 | Secure-by-Design (T-M-002) | CTO + Lead Dev | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-07.2-001 | D-07.2 | Secure Coding Practices | CTO + Lead Dev | HIGH | 1/4 → 3/4 | TODO | Internal audit only |
| OBL-D-07.3-001 | D-07.3 | CI/CD Pipeline Security | CTO + Lead Dev | HIGH | 1/4 → 3/4 | TODO | Internal audit only |
| OBL-D-07.4-001 | D-07.4 | Change Management | CTO + Lead Dev | HIGH | 1/4 → 3/4 | TODO | Internal audit only |
| OBL-D-08.1-001 | D-08.1 | Staff Security Awareness Training | CTO + HR + DPO | MEDIUM | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-08.2-001 | D-08.2 | Role-Specific Security Training | CTO + HR + DPO | MEDIUM | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-09.1-001 | D-09.1 | ISMS Documentation | CTO + DPO + Compliance Lead + Legal | HIGH | 1/4 → 3/4 | TODO | CNPD + ENISA (periodic accountability + CRA conformity) |
| OBL-D-09.2-001 | D-09.2 | Unified Risk Assessment (T-M-001) | CTO + DPO + Compliance Lead + Legal | HIGH | 1/4 → 3/4 | TODO | CNPD + ENISA (periodic accountability + CRA conformity) |
| OBL-D-09.4-001 | D-09.4 | Records of Processing | CTO + DPO + Compliance Lead + Legal | HIGH | 1/4 → 3/4 | TODO | CNPD + ENISA (periodic accountability + CRA conformity) |
| OBL-D-10.1-001 | D-10.1 | Continuous Security Monitoring | CTO + Lead Dev | HIGH | 1/4 → 3/4 | TODO | ENISA 24h (CRA Art. 14 exploited-vulnerability reporting) |
| OBL-D-10.2-001 | D-10.2 | Security Audit Logging | CTO + Lead Dev | HIGH | 2/4 → 3/4 | TODO | Internal audit only |
| OBL-D-10.3-001 | D-10.3 | Regular Security Testing | CTO + Lead Dev | HIGH | 2/4 → 3/4 | TODO | Internal audit only |

**Total obligations:** 34 across 10 sub-domains (D-01..D-10) — Sprint 6+ count (was 30, +4 from P7 orphan fix). **Total cells populated in detail cards:** 34 × 17 = 578.


**Card-to-cross-reference mapping (verified in §3 of this document):**


| OBL ID | Linked Goal(s) | Linked CR Rule | Notes |

|--------|----------------|----------------|-------|
| OBL-D-01.1-001 | PO-D-01.1-001 | CR-D-01.1-001 |  |
| OBL-D-01.2-001 | PO-D-01.2-001 | CR-D-01.2-001 |  |
| OBL-D-01.3-001 | — (F-01 finding: no PO; CR references phantom PO-D-01.3-001 — see §3.7 F-03) | CR-D-01.3-001 | CRA sole-authority key-management obligation; PO-D-01.3-001 absent by design |
| OBL-D-01.4-001 | PO-D-01.4-001 | CR-D-01.4-001 | Rich NI = 2.500 (F-10 reconciliation, Sprint 4 §4.1) |
| OBL-D-02.1-001 | SO-D-02.1-001 | CR-D-02.1-001 | CRA sole authority; SBOM cross-ref to OBL-D-06.2-001 |
| OBL-D-02.2-001 | SO-D-02.2-001 | CR-D-02.2-001 | CRA 5-year support + 10-year update retention noted |
| OBL-D-02.3-001 | SO-D-02.3-001 | CR-D-02.3-001 | security.txt + ENISA 24h routing |
| OBL-D-03.1-001 | SO-D-03.1-001 | CR-D-03.1-001 | managed identity service baseline |
| OBL-D-03.2-001 | SO-D-03.2-001 | CR-D-03.2-001 | MFA opt-in for customers; mandatory for operators |
| OBL-D-03.3-001 | SO-D-03.3-001 | CR-D-03.3-001 | RBAC quarterly review |
| OBL-D-03.4-001 | SO-D-03.4-001 | CR-D-03.4-001 | CRA sole authority; hardened-default benchmark-inspired review |
| OBL-D-04.1-001 | SO-D-04.1-001 | CR-D-04.1-001 | CRA sole authority; managed monitoring + managed notification service |
| OBL-D-04.2-001 | SO-D-04.2-001 | CR-D-04.2-001 | managed standard DDoS protection + 4h containment playbook |
| OBL-D-04.3-001 | SO-D-04.3-001 | CR-D-04.3-001 | T-001 max-SLA 24h routing; CONTEXTUAL activation |
| OBL-D-04.4-001 | SO-D-04.4-001 | CR-D-04.4-001 | managed backup RTO 24h / RPO 1h |
| OBL-D-05.1-001 | PO-D-05.1-001 | CR-D-05.1-001 | Field-level schema enforcement |
| OBL-D-05.2-001 | PO-D-05.2-001 | CR-D-05.2-001 | 7y audit logs + 30d DSAR |
| OBL-D-05.3-001 | PO-D-05.3-001 | CR-D-05.3-001 | GDPR Art. 17 + 7d SLA |
| OBL-D-05.4-001 | PO-D-05.4-001 | CR-D-05.4-001 | GDPR Art. 20 + 48h SLA |
| OBL-D-06.1-001 | SO-D-06.1-001 | CR-D-06.1-001 | Provider ISO 27001 attestation register |
| OBL-D-06.2-001 | SO-D-06.2-001 | CR-D-06.2-001 | CRA sole authority; machine-readable SBOM |
| OBL-D-06.3-001 | SO-D-06.3-001 | CR-D-06.3-001 | DPA template |
| OBL-D-07.1-001 | PO-D-07.1-001 | CR-D-07.1-001 | T-M-002: GDPR NI=2 vs CRA NI=3; secure-development-framework alignment + maturity assessment L2+ |
| OBL-D-07.2-001 | — (F-07 TBD — PO-D-07.2-001 to be added in follow-on contract) | CR-D-07.2-001 (TBD — F-07) | CRA sole authority; secure-coding standards + SAST + peer review |
| OBL-D-07.3-001 | — (F-07 TBD — SO-D-07.3-001 to be added in follow-on contract) | CR-D-07.3-001 (TBD — F-07) | CRA sole authority; CI security gates + SBOM generation |
| OBL-D-07.4-001 | — (F-07 TBD — SO-D-07.4-001 to be added in follow-on contract) | CR-D-07.4-001 (TBD — F-07) | CRA sole authority; CAB approval + signed artefacts |
| OBL-D-08.1-001 | SO-D-08.1-001 | CR-D-08.1-001 | Annual awareness + quarterly phishing drill |
| OBL-D-08.2-001 | SO-D-08.2-001 | CR-D-08.2-001 | Role-specific (CTO/Dev/DPO) |
| OBL-D-09.1-001 | PO-D-09.1-001 + SO-D-09.1-001 | CR-D-09.1-001 | Rich NI = 2.500 (F-10 reconciliation, Sprint 4 §4.1); ISMS docs |
| OBL-D-09.2-001 | PO-D-09.2-001 + SO-D-09.2-001 | CR-D-09.2-001 | T-M-001: unified DPIA + CRA risk assessment |
| OBL-D-09.4-001 | PO-D-09.4-001 | CR-D-09.4-001 | RoPA + breach log |
| OBL-D-10.1-001 | — (F-07 TBD — SO-D-10.1-001 to be added in follow-on contract) | CR-D-10.1-001 (TBD — F-07) | CRA sole authority; managed monitoring + alert taxonomy + monthly review |
| OBL-D-10.2-001 | SO-D-10.2-001 | CR-D-10.2-001 | managed audit-trail service + tamper-evident managed object storage log bucket |
| OBL-D-10.3-001 | SO-D-10.3-001 | CR-D-10.3-001 | Quarterly review + annual pen test |


---


### 5.1 D-01 — Data Protection & Encryption (4 cards)


D-01 covers the confidentiality and integrity pillars of data protection. All four obligations are STRUCTURAL and CONTINUOUS — they operate at every read and every write. The implementation is fully delegated to managed hosting services (managed object storage encryption with managed key custody, managed database encryption with managed key custody) with the LIGHTWEIGHT implementation tier justified by the absence of a dedicated in-house key custody program. F-10 NI reconciliation: OBL-D-01.4-001 uses Rich NI = 2.500 (DR-002 AVG of GDPR-C05=2 and CRA-C09=3) per Sprint 4 §4.1.


### OBL-D-01.1-001 — Data Encryption at Rest

1. **Description:** Encrypt all personal and sensitive data at rest using industry-standard symmetric algorithms (cryptography symmetric with strength adequate to state of the art). For TinyTask, this obligation covers customer PII (emails, names, project metadata) stored in production data stores — specifically managed object storage buckets holding customer-uploaded assets, managed NoSQL tables for application metadata, and managed database snapshots used for backup. The technical realisation is fully delegated to managed hosting services (managed object storage encryption with managed key custody, managed database encryption with managed key custody) without a company-owned key custody program, justified by the LIGHTWEIGHT implementation tier and the absence of dedicated security headcount. The corpus-derived rationale (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.json`, HSO + Sub-SO frozen per `proportionality_model.md §1`) treats encryption-at-rest as a foundational data-protection guarantee without which all higher-layer controls (access, integrity, lifecycle) inherit residual risk. GDPR Art. 5(1)(f) frames it as part of the integrity-and-confidentiality principle; GDPR Art. 32(1)(b) names encryption as an explicit appropriate technical measure; CRA-C07 (Annex I §1) lifts the same requirement onto product-with-digital-elements data. At the MICRO tier, this obligation is satisfied through configuration rather than program ownership: managed configuration rules prove continuous compliance (managed object storage encryption, managed NoSQL encryption), and the absence of a customer-managed key lifecycle is documented as a deliberate proportionality choice (not a control gap). The obligation remains STRUCTURAL and CONTINUOUS — every object written must be encrypted at the storage layer, with no opt-out.

2. **Scope:** All production data stores under TinyTask's managed hosting account: customer managed object storage buckets (project assets, exports), managed NoSQL tables (task metadata, session state), managed database snapshots, managed log archives, managed backup vaults. Includes cross-region replicas for disaster-recovery purposes.

3. **Out of Scope:** Client-side encryption controlled by end users (out of SaaS scope); client-managed HSM (overkill at MICRO scale); encryption of ephemeral in-memory state (covered separately by D-01.3 key management); non-production data stores explicitly tagged `env=nonprod` (covered by separate developer-environment policy).

4. **Source Article:** GDPR Art. 5(1)(f) + Art. 32(1)(a/b); CRA Annex I §1(1) (encryption of data at rest); CRA-C07

5. **NIST CSF Anchors:** PR.DS-01 (Data-at-rest protection), PR.DS-02 (Data-in-transit protection — co-annexed), PR.PS-01 (Baseline configuration)

6. **Verification Criteria:**

   - Managed configuration rule for managed object storage encryption reports COMPLIANT for every production bucket (snapshot captured monthly by Compliance Lead).

   - Managed NoSQL tables in production carry encryption with managed key custody; cross-checked against managed configuration rule for table encryption.

   - Annual review note (Doc 09 family input) records the absence of a company-owned key custody program and the rationale (LIGHTWEIGHT tier, MICRO budget, no dedicated security FTE) so that future audits do not treat it as a missing control.

7. **Verification Method:** DEMONSTRATE (managed configuration dashboard screenshot) + INSPECT (annual review note + managed configuration compliance report)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-01.2-001 (in-transit), OBL-D-01.3-001 (key management), PO-D-01.1-001, SO-D-01.1-001, CR-D-01.1-001

11. **Risk if not met:** H — Failure creates direct GDPR Art. 5(1)(f) audit-finding exposure and undermines confidentiality of all downstream D-05 lifecycle controls (erasure, portability) which assume encrypted storage.

12. **Affected Stakeholders:** Customers (data subjects), CTO (owner), DPO (oversight), Lead Dev (implementer), managed hosting provider (sub-processor under DPA — Annex IV)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-01.2-001 — Data Encryption in Transit

1. **Description:** Encrypt all data transmitted across networks using protection cryptographic for confidentiality and integrity in transit or an equivalent modern protocol. For TinyTask, this obligation covers all ingress traffic from customer browsers and mobile clients, all egress traffic to payment processor and third-party APIs, and all internal service-to-service communication that crosses a network boundary. The technical realisation uses managed certificate authority and managed edge termination with modern cryptographic protocol negotiated by default and certificate auto-renewal configured at provisioning time. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.2/D-01.2.json`) treats transit encryption as the second pillar of the confidentiality principle and explicitly couples it to the at-rest obligation: encrypted storage over an unencrypted transport is functionally equivalent to no encryption at all. GDPR Art. 32(1)(a) names encryption of data in transit as an explicit appropriate technical measure; CRA-C08 (Annex I §1(2)) lifts the same requirement onto product communications. At MICRO scale, this is a managed-service configuration obligation. The managed hosting platform handles protocol negotiation, cipher selection, and certificate rotation; TinyTask's contribution is the policy intent (only modern cryptographic protocols permitted on edge and load-balancer) plus the annual cipher-suite review. The obligation is STRUCTURAL and CONTINUOUS — every byte that crosses a network boundary must traverse a protected channel.

2. **Scope:** Edge HTTPS termination, origin load-balancer protection cryptographic, inter-service private endpoints (managed object storage, managed NoSQL), outbound HTTPS to payment processor API and any other third-party integrations.

3. **Out of Scope:** Internal service-to-service traffic that does not cross a network boundary (e.g., same-AZ function-to-database via internal endpoint); mTLS between internal microservices (deferred — over-engineered at MICRO scale); SSH/RDP operator access (covered by separate operator-access policy with MFA + session recording).

4. **Source Article:** GDPR Art. 5(1)(f) + Art. 32(1)(a); CRA Annex I §1(2) (encryption of data in transit); CRA-C08

5. **NIST CSF Anchors:** PR.DS-02 (Data-in-transit protection), PR.DS-01 (Data-at-rest — co-annexed), PR.AA-01 (Identity and credential management)

6. **Verification Criteria:**

   - Managed configuration rule for HTTPS-only listeners reports COMPLIANT for the production load-balancer; edge distribution has `ViewerProtocolPolicy=redirect-to-https` and minimum cryptographic protocol version equivalent to modern TLS standard.

   - Annual cipher-suite review note enumerates the negotiated cipher list (sourced from `sslyze` or `testssl.sh` against production endpoint) and confirms absence of legacy ciphers (3DES, RC4, NULL).

   - Certificate expiry is monitored via managed certificate authority; auto-renewal status verified at least quarterly by Lead Dev.

7. **Verification Method:** INSPECT (managed configuration compliance + cipher report) + DEMONSTRATE (live cryptographic handshake via `openssl s_client`)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-01.1-001 (at-rest), OBL-D-01.3-001 (key management), PO-D-01.2-001, SO-D-01.2-001, CR-D-01.2-001

11. **Risk if not met:** H — Failure exposes all data-in-flight to passive interception; payment data flowing to the payment processor would be the most visible signal but PII in transit is the regulatory trigger (GDPR Art. 32(1)(a)).

12. **Affected Stakeholders:** Customers (data subjects in transit), CTO, Lead Dev, managed hosting provider (transit protection provider), payment processor (downstream protected party)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-01.3-001 — Cryptographic Key Management

1. **Description:** Implement secure cryptographic key management with authentication and integrity verification. For TinyTask, this obligation is met through managed key custody — a managed key custody service that handles key generation, storage, rotation, and access control — without standing up an in-house key custody program. The justification is the LIGHTWEIGHT implementation tier and the MICRO budget; bringing up a self-hosted secret-storage service or hardware security module is a documented deliberate non-choice. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.3/D-01.3.json`) treats key management as the second-order control underpinning both at-rest and in-transit encryption. Without it, encrypted data is only as secure as the lifecycle of the key that protects it. CRA-C15 (Annex I §1(3) and §2) is the sole authority here — GDPR does not impose a comparable key-management obligation directly, hence the NI=3.000 (CRA-only, high intensity) and the absence of a corresponding PO-D-01.3-001 (the goal layer is privacy-centric; see Sprint 1 finding F-01). At MICRO scale, the implementation is configuration-driven: managed cryptographic key custody with rotation enabled (annual cadence for symmetric keys), managed identity policies restricting decrypt operations to the application service roles, and managed audit-trail logging of every key-use event. The obligation is STRUCTURAL and CONTINUOUS — every cryptographic operation must trace to an authenticated, authorised key under managed key custody control.

2. **Scope:** All cryptographic keys used by TinyTask: managed object storage bucket keys, managed NoSQL table keys, managed database storage encryption keys, managed audit-trail log encryption key, managed secrets custody (for database credentials and API keys to payment processor/managed messaging service).

3. **Out of Scope:** Customer-managed keys imported from on-premises HSM (none exist); quantum-resistant key algorithms (post-quantum migration tracked separately as future-state); hardware security modules beyond managed hosting HSM (over-engineered at MICRO).

4. **Source Article:** CRA Annex I §1(3) and §2 (key management, authentication of keys, integrity verification); CRA-C15

5. **NIST CSF Anchors:** PR.DS-01 (Data-at-rest), PR.DS-02 (Data-in-transit — co-annexed), PR.AA-01 (Identity and credential management)

6. **Verification Criteria:**

   - Managed configuration rule for key custody lifecycle is COMPLIANT for every production key; rotation status `ENABLED` for all symmetric keys (annual cadence).

   - IAM policy review (quarterly) confirms only the application service role + on-call Lead Dev can invoke decrypt operations; no wildcard key custody permissions exist.

   - Managed audit-trail key custody event log is forwarded to the tamper-evident managed object storage log bucket and retained for 10 years per OBL-D-09.1-001 retention policy.

7. **Verification Method:** INSPECT (managed configuration + IAM policy + managed audit-trail query) + DEMONSTRATE (decrypt-from-app test showing authenticated key custody call)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-01.1-001, OBL-D-01.2-001, OBL-D-09.1-001 (10-year retention of key-use logs), CR-D-01.3-001

11. **Risk if not met:** H — Failure compromises every other encryption guarantee — once key integrity is lost, encrypted data is functionally exposed.

12. **Affected Stakeholders:** CTO (key custody policy owner), Lead Dev (IAM enforcement), DPO (oversight), managed hosting provider (key custody provider — sub-processor under DPA Annex IV)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-01.4-001 — Data Integrity Protection

1. **Description:** Protect personal and product data against unauthorised manipulation (intentional tampering by attackers or malicious insiders) and accidental loss (data corruption, erroneous deletion, replication gaps). For TinyTask, the implementation uses HMAC signatures on critical application objects, managed database constraint enforcement (UNIQUE, CHECK, FOREIGN KEY), and managed object storage Object Lock for tamper-evident retention of audit-relevant artifacts. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.4/D-01.4.json`) treats integrity as the third pillar of data protection alongside confidentiality (D-01.1, D-01.2) and availability (D-04.4). GDPR Art. 5(1)(d) frames accuracy and integrity as a substantive principle; CRA-C09 (Annex I §1(4)) lifts the same requirement onto product data. The Rich Mode NI = 2.500 (DR-002 AVG of GDPR-C05=2 and CRA-C09=3), resolved as authoritative in Sprint 4 §4.1. The obligation is STRUCTURAL and CONTINUOUS — every write operation must enforce integrity, and every read must verify it. The implementation strategy intentionally avoids blockchain-style append-only ledgers (over-engineered) but does use managed object storage Object Lock in compliance mode for the breach log and audit log buckets, which are the artifacts most likely to be targeted by tampering.

2. **Scope:** All production data stores where data subject rights or product functionality depend on integrity: customer PII in managed relational database (CHECK + UNIQUE constraints), managed object storage customer-uploaded assets (managed Object Lock in compliance mode for the audit-trail subset), managed NoSQL streams (per-record checksum), managed backup snapshots (verified at restore time).

3. **Out of Scope:** Cryptographic integrity proofs of computation (zero-knowledge proofs, etc.); blockchain-anchored audit trails (over-engineered); end-to-end integrity verification of ephemeral session state (covered by transport encryption + server-side validation).

4. **Source Article:** GDPR Art. 5(1)(d) (accuracy principle); CRA Annex I §1(4) (data integrity protection); CRA-C09; GDPR-C05

5. **NIST CSF Anchors:** PR.DS-01 (Data-at-rest integrity), PR.DS-01 (Integrity checking), PR.PS-01 (Baseline configuration)

6. **Verification Criteria:**

   - Managed configuration rule for object-lock-configuration confirms COMPLIANT for the audit-log managed object storage buckets; object retention set to 10 years in compliance mode.

   - Quarterly DB constraint audit: managed relational database `information_schema.CHECK_CONSTRAINTS` and `TABLE_CONSTRAINTS` enumerated; orphan-record query returns zero rows for all production tables.

   - Restore drill (annual): managed backup snapshot restored into isolated test account; checksum verification confirms byte-equality with source.

7. **Verification Method:** TEST (restore drill) + INSPECT (managed configuration + DB schema audit) + ANALYZE (orphan-record query)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-01.1-001, OBL-D-04.4-001 (restoration), OBL-D-09.1-001 (retention), PO-D-01.4-001, SO-D-01.4-001, CR-D-01.4-001

11. **Risk if not met:** M — Failure undermines the credibility of all downstream evidence (audit logs, breach records, erasure confirmations) — even if confidentiality is preserved, regulators cannot trust the artifacts.

12. **Affected Stakeholders:** Customers (data subjects relying on accurate PII), CTO, Lead Dev, DPO (integrity of breach log)

13. **Maturity Score:** 1/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment



**D-01 Verification Cross-Walk (for human reviewer):**


| OBL ID | Verification Criteria Count | Method Mix | Primary NIST Anchor | Cadence |
|--------|----------------------------:|------------|---------------------|---------|
| OBL-D-01.1-001 | 3 | DEMONSTRATE + INSPECT | PR.DS-01 | Annual + continuous (Config) |
| OBL-D-01.2-001 | 3 | INSPECT + DEMONSTRATE | PR.DS-02 | Annual + quarterly |
| OBL-D-01.3-001 | 3 | INSPECT + DEMONSTRATE | PR.DS-01 | Annual + quarterly |
| OBL-D-01.4-001 | 3 | TEST + INSPECT + ANALYZE | PR.DS-01 | Quarterly + annual drill |

**D-01 Owner-Responsibility Decomposition:**


| Role | Primary Responsibility in this Sub-Domain | Backup / Approver |
|------|-------------------------------------------|-------------------|
| CTO | Architecture decisions; managed key custody policy; managed configuration rule authorship | Lead Dev |
| Lead Dev | Implementation of encryption-at-rest + transit; cipher review; key-rotation cadence | CTO |

---


### 5.2 D-02 — Vulnerability Management (3 cards)


D-02 covers product-level vulnerability management. All three obligations are CRA sole authority — GDPR does not impose a comparable product-level vulnerability, SBOM, or CVD obligation directly. The implementation is automated in CI (Trivy, npm audit, machine-readable SBOM generation) plus a 24h ENISA reporting workflow. CRA Art. 13(11) SBOM and CRA Art. 14 ENISA reporting are per-se obligations with explicit non-compliance consequences.


### OBL-D-02.1-001 — No Known Vulnerabilities + SBOM

1. **Description:** Deliver the product with no known exploitable vulnerabilities present in the released artifacts, and maintain a Software Bill of Materials (SBOM) documenting every third-party component in machine-readable format. For TinyTask, this means running Trivy and npm audit on every CI build, blocking any build with a CVE above the configured severity threshold, and emitting a machine-readable SBOM per release that is archived alongside the build artifacts. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability/D-02.1/D-02.1.json`) frames zero-CVE-at-release and SBOM as the twin gates of CRA product conformity: CRA-C01 (Annex I §1 — no known exploitable vulnerabilities) and CRA-C17 (Art. 13(11) — SBOM obligation). GDPR does not impose a comparable obligation directly; the sub-domain is therefore CRA-only with NI=3.000 for both clauses. At MICRO scale, the implementation is automated inside CI/CD (GitHub Actions or equivalent) — the human contribution is the threshold policy (severity cutoff, time-window for newly-disclosed CVEs) and the SBOM retention discipline. The obligation is mixed ONE_TIME + CONTINUOUS — every release must satisfy the gate, and the SBOM must be updated as the dependency tree evolves.

2. **Scope:** All production-deployed artifacts: container images, application code (compiled and source-distributed dependencies), infrastructure-as-code modules, third-party SaaS dependencies documented in the SBOM even when not packaged into the build.

3. **Out of Scope:** Vulnerability remediation for vulnerabilities below the configured severity threshold (deferred to LIGHTWEIGHT policy); SBOM for in-development features not yet shipped (out of CRA scope until release); vulnerability disclosure to end users for vulnerabilities discovered post-release (covered by OBL-D-02.3-001 CVD policy).

4. **Source Article:** CRA Art. 13(11) (SBOM); CRA Annex I §1 (no known exploitable vulnerabilities); CRA-C01, CRA-C17

5. **NIST CSF Anchors:** ID.RA-01 (Asset vulnerabilities identified), PR.PS-02 (Vulnerability management plan), DE.AE-06 (Notifications from detection systems)

6. **Verification Criteria:**

   - CI pipeline runs `trivy image --severity HIGH,CRITICAL --exit-code 1` and `npm audit --audit-level=high` for every pull request; build fails if any HIGH or CRITICAL CVE is present.

   - Per-release artifact bundle includes `sbom.cdx.json` (CycloneDX 1.5) signed and archived in the managed object storage release bucket with 10-year retention.

   - Quarterly SBOM diff review identifies new transitive dependencies introduced since last release and confirms none are on the CRA denylist or have known active exploits.

7. **Verification Method:** TEST (CI gate blocks CVE-bearing build) + INSPECT (SBOM diff review minutes) + DEMONSTRATE (release bundle inspection)

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** OBL-D-02.2-001 (updates), OBL-D-02.3-001 (CVD), OBL-D-06.2-001 (SBOM cross-ref), SO-D-02.1-001, CR-D-02.1-001

11. **Risk if not met:** H — Failure to gate known-vulnerable releases creates direct CRA market-surveillance exposure and undermines customer trust; failure to maintain SBOM is a CRA Art. 13(11) violation per se.

12. **Affected Stakeholders:** CTO, Lead Dev, Procurement (third-party component selection), Customers (downstream consumers of SBOM under CRA), ENISA

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** ENISA 24h (CRA Art. 14 exploited-vulnerability reporting)

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment; ENISA — CRA EU market surveillance authority; CNCS (Centro Nacional de Cibersegurança) — PT CSIRT for early-warning + incident coordination


### OBL-D-02.2-001 — Automatic Security Updates

1. **Description:** Enable automatic security updates and remediate vulnerabilities promptly without requiring user intervention. For TinyTask (SaaS), this obligation is met through a managed automated patch pipeline operating on the compute fleet (if any) and through an automated dependency-update pipeline (Dependabot or Renovate) that opens pull requests against the application repository within 24 hours of a new advisory. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability/D-02.2/D-02.2.json`) treats automatic updates as the operational expression of zero-CVE-at-release: a release that is clean today but cannot be updated cleanly tomorrow is not actually secure. CRA-C04 (Annex I §2 — secure update mechanisms) and CRA-C19 (Art. 13 — duty to remediate) jointly drive the NI=3.000 intensity. The CRA also requires a 5-year support period per release and a 10-year security-update retention, both noted in Doc 11 §4 control notes. At MICRO scale, the automation is delegated to managed services (managed patch automation for OS, automated dependency-update for application dependencies) plus a 72-hour SLA for reviewing and merging the dependency-update PRs. The obligation is mixed ONE_TIME (initial setup) + TRIGGERED (each new advisory).

2. **Scope:** OS-level patches on EC2 instances (if present in the deployment topology); application-level dependency updates (npm, pip, container base images); infrastructure-as-code module updates (Terraform providers, modules).

3. **Out of Scope:** Customer-deployed on-premises installations (out of SaaS scope — TinyTask is SaaS only); long-term-support (LTS) version commitments beyond the CRA 5-year window (separate roadmap decision); breaking-change dependency upgrades (treated as feature releases, not security updates).

4. **Source Article:** CRA Annex I §2 (secure update mechanisms); CRA Art. 13 (duty to remediate, including 5-year support); CRA-C04, CRA-C19

5. **NIST CSF Anchors:** ID.RA-01 (Asset vulnerabilities), PR.PS-02 (Vulnerability management plan), PR.PS-02 (Maintenance and repair of organizational assets)

6. **Verification Criteria:**

   - Managed patch automation maintenance window runs weekly on every production compute instance; compliance report shows 100% patch coverage at audit time.

   - Dependabot configured with `high-severity` security updates enabled; PR-to-merge median latency measured monthly and target <72h.

   - Container base image rebuild triggered by Dependabot `docker` ecosystem updates; rebuilt image re-passes OBL-D-02.1-001 Trivy scan.

7. **Verification Method:** TEST (managed patch automation compliance report) + INSPECT (Dependabot PR latency dashboard) + DEMONSTRATE (full patch cycle from advisory → PR → merged → deployed)

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** OBL-D-02.1-001, OBL-D-02.3-001, SO-D-02.2-001, CR-D-02.2-001

11. **Risk if not met:** H — Failure to remediate within reasonable SLA creates compounding vulnerability backlog — every day of delay expands the exploitable window and increases the likelihood of an ENISA reportable incident.

12. **Affected Stakeholders:** CTO, Lead Dev, Procurement (vendor security advisories), Customers (downstream protection)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** ENISA 24h (CRA Art. 14 exploited-vulnerability reporting)

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment; ENISA — CRA EU market surveillance authority; CNCS (Centro Nacional de Cibersegurança) — PT CSIRT for early-warning + incident coordination


### OBL-D-02.3-001 — CVD Policy + ENISA Reporting

1. **Description:** Publish a coordinated vulnerability disclosure (CVD) policy that allows security researchers and customers to report vulnerabilities through a defined channel, and report severe exploited vulnerabilities to ENISA within 24 hours of awareness. For TinyTask, the CVD policy is published at `/.well-known/security.txt` (RFC 9116) and on a dedicated `/security` page; the ENISA reporting workflow is integrated into the incident-response playbook (OBL-D-04.3-001) as the upstream trigger for OBL-D-04.3-001 routing. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability/D-02.3/D-02.3.json`) frames CVD as the structural counterweight to the SBOM and update obligations: a product can be technically clean at release but still be unsafe if vulnerabilities discovered post-release cannot be reported or coordinated. CRA-C21 (Art. 12 — coordinated disclosure) and CRA-C26 (Art. 14 — ENISA reporting) jointly drive the NI=3.000 intensity. At MICRO scale, the implementation is policy-plus-playbook: security.txt is static and rarely changes, the `/security` page is a single-page Markdown doc, and the ENISA workflow is a 24-hour SLA anchored in the incident-response runbook. The obligation is mixed CONTINUOUS (CVD policy must always be reachable) + TRIGGERED (ENISA report on exploited vulnerability).

2. **Scope:** Public-facing vulnerability disclosure channels (security.txt, /security page); inbound triage process (Lead Dev as first responder); outbound ENISA reporting via the CSIRT network; coordinated disclosure timeline with reporting researcher.

3. **Out of Scope:** Bug-bounty programme with financial rewards (over-scope at MICRO); formal CVE assignment for every disclosure (handled by the reporting researcher); coordinated disclosure to other vendors when a third-party component is the root cause (escalated case-by-case).

4. **Source Article:** CRA Art. 12 (coordinated vulnerability disclosure); CRA Art. 14 (single reporting platform — ENISA); CRA-C21, CRA-C26

5. **NIST CSF Anchors:** DE.AE-06 (Notifications from detection systems), RS.CO-02 (Incident reporting), ID.RA-01 (Asset vulnerabilities)

6. **Verification Criteria:**

   - security.txt at `https://tinytask.example/.well-known/security.txt` resolves with valid `Contact`, `Expires`, and `Preferred-Languages` fields; verified quarterly by `curl` from CI.

   - Annual tabletop exercise: simulated inbound report via the published channel; 24h ENISA notification clock started from simulated awareness; runbook followed end-to-end.

   - Disclosure log (private) records every inbound report with timestamp, triage outcome, and resolution; retained 10 years per OBL-D-09.1-001.

7. **Verification Method:** TEST (security.txt fetch + parse) + DEMONSTRATE (tabletop exercise with 24h clock) + INSPECT (disclosure log)

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** OBL-D-02.1-001, OBL-D-02.2-001, OBL-D-04.3-001 (incident notification cross-ref), SO-D-02.3-001, CR-D-02.3-001

11. **Risk if not met:** H — Failure to publish a CVD channel means ENISA cannot route inbound reports properly, and a missed 24h ENISA clock creates direct CRA Art. 14 violation.

12. **Affected Stakeholders:** CTO, Lead Dev (first responder), ENISA (recipient), CNCS (PT CSIRT), Security researchers (reporting parties), Customers (downstream notification)

13. **Maturity Score:** 1/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** ENISA 24h (CRA Art. 14 exploited-vulnerability reporting)

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment; ENISA — CRA EU market surveillance authority; CNCS (Centro Nacional de Cibersegurança) — PT CSIRT for early-warning + incident coordination



**D-02 Verification Cross-Walk (for human reviewer):**


| OBL ID | Verification Criteria Count | Method Mix | Primary NIST Anchor | Cadence |
|--------|----------------------------:|------------|---------------------|---------|
| OBL-D-02.1-001 | 3 | TEST + INSPECT + DEMONSTRATE | ID.RA-01 | Per-build + quarterly |
| OBL-D-02.2-001 | 3 | TEST + INSPECT + DEMONSTRATE | PR.PS-02 | Weekly + 72h SLA |
| OBL-D-02.3-001 | 3 | TEST + DEMONSTRATE + INSPECT | DE.AE-06 | Quarterly + tabletop |

**D-02 Owner-Responsibility Decomposition:**


| Role | Primary Responsibility in this Sub-Domain | Backup / Approver |
|------|-------------------------------------------|-------------------|
| CTO | Vulnerability policy; severity thresholds; release-block decisions | Lead Dev |
| Lead Dev | CI/CD gates; SBOM generation; patch pipeline | CTO |
| Procurement | Vendor security advisories; supplier CVE tracking | Lead Dev |

---


### 5.3 D-03 — Access Control (4 cards)


D-03 covers authentication and access-control. Two obligations are CRA sole authority (D-03.1, D-03.2, D-03.4); two are GDPR-led (D-03.3). The implementation delegates customer-facing auth to a managed identity provider service and operator auth to managed IAM. MFA is mandatory for operators and opt-in for customers — the LIGHTWEIGHT proportionality choice. D-03.3 RBAC has a quarterly review cycle that is the LIGHTWEIGHT implementation's main human-driven activity.


### OBL-D-03.1-001 — Authentication Controls

1. **Description:** Implement authentication and access-control measures that verify the identity of every user before granting access to product functionality. For TinyTask, this obligation is met through a managed identity provider service as the customer-facing identity provider (email + password with mandatory email verification, federated identity-provider delegation via current open-standard protocol) and through managed IAM for all internal/operator access to infrastructure. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access/D-03.1/D-03.1.json`) treats authentication as the gate that all other access-control obligations (D-03.2 MFA, D-03.3 RBAC) depend on. CRA-C05 (Annex I §1(5)) is the sole authority — GDPR does not impose a comparable product-level authentication obligation directly; authentication is implicit in the lawful-basis framework but is not a standalone article. At MICRO scale, the implementation is delegated to a managed identity provider (managed identity service) and managed IAM (managed operator identity). The MINIMAL implementation tier is justified by the supplier attestation on file (managed identity provider ISO 27001 attestation). The obligation is ONE_TIME (initial implementation) — the controls are continuously effective without periodic human re-implementation.

2. **Scope:** All customer-facing authentication flows (login, registration, password reset, federated identity-provider callback); all operator authentication to managed hosting console, managed CLI, and infrastructure-as-code pipelines; service-to-service authentication via IAM roles (no long-lived credentials).

3. **Out of Scope:** Customer-side federated authentication via open-standard protocol for enterprise customers (separate commercial offering, not in scope for MICRO baseline); biometric-only authentication on mobile (not deployed at MICRO); passwordless-only authentication (out of scope — password remains primary, passwordless is future).

4. **Source Article:** CRA Annex I §1(5) (authentication mechanisms); CRA-C05

5. **NIST CSF Anchors:** PR.AA-01 (Identity and credential management), PR.AA-06 (Users, devices, and assets are authenticated), PR.AA-03 (Users are managed)

6. **Verification Criteria:**

   - Managed identity provider email-verification gate: every new user must verify email before accessing any non-trivial endpoint; verified by quarterly auth-flow audit.

   - Managed IAM password policy enforces minimum 14 characters, rotation after 90 days for console users; verified by IAM credential report.

   - Service-to-service authentication uses IAM roles only — no static managed hosting access keys in code or environment variables; verified by `git-secrets` + manual review.

7. **Verification Method:** DEMONSTRATE (live auth flow on test tenant) + INSPECT (IAM credential report + managed identity provider audit log)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-03.2-001, OBL-D-03.3-001, OBL-D-03.4-001, SO-D-03.1-001, CR-D-03.1-001

11. **Risk if not met:** H — Failure leaves the customer-facing surface open to credential-stuffing and account-takeover; for a B2B SaaS, account compromise propagates to every customer tenant.

12. **Affected Stakeholders:** Customers (data subjects authenticating), CTO (managed identity provider admin), Lead Dev (IAM), managed identity provider (sub-processor under DPA)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-03.2-001 — Multi-Factor Authentication

1. **Description:** Enable multi-factor authentication (MFA) where appropriate, particularly for accounts with elevated privilege or access to sensitive data. For TinyTask, MFA is enforced for all operator accounts (managed console access, production database access, payment processor dashboard) and is offered as opt-in for customer accounts with a one-click enrolment banner. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access/D-03.2/D-03.2.json`) treats MFA as a defence-in-depth control on top of D-03.1 authentication — even a strong password is insufficient against credential leaks. CRA-C06 (Annex I §1(6)) is the sole authority, with NI=2.000 reflecting the proportionality flexibility (the clause says 'where appropriate' rather than mandating universal MFA). At MICRO scale, MFA is mandatory for operators and optional for customers; the MINIMAL implementation tier reflects supplier attestation (managed identity provider MFA). The obligation is ONE_TIME in setup but operates CONTINUOUSLY in effect.

2. **Scope:** Operator MFA on managed console (IAM policy `iam:RequireMFAAuthentication`); production database MFA via short-lived IAM-token rotation; customer MFA opt-in flow backed by phishing-resistant authentication factor (time-based one-time password preferred).

3. **Out of Scope:** Customer-side mandatory MFA enforcement (out of scope for MICRO baseline; documented as future commercial offering); hardware-token-only phishing-resistant factor (deferred); biometric-only MFA on operator devices (deferred — TOTP is sufficient).

4. **Source Article:** CRA Annex I §1(6) (multi-factor authentication); CRA-C06

5. **NIST CSF Anchors:** PR.AA-01 (Identity and credential management), PR.AA-06 (Users authenticated), PR.AA-05 (Identity proofing)

6. **Verification Criteria:**

   - Managed IAM policy `iam:RequireMFAAuthentication` is attached to all human-user IAM groups; verified by managed IAM policy simulator test against a sample non-MFA login attempt (must be Denied).

   - Managed identity provider MFA enrolment flow tested on a customer-test tenant: enrolment → re-login → phishing-resistant authentication factor challenge → success; documented in the operator runbook.

   - Quarterly MFA-coverage report: 100% of operator accounts have MFA enrolled; X% of customer accounts (reported for trend tracking).

7. **Verification Method:** DEMONSTRATE (MFA enrolment + challenge flow) + INSPECT (IAM policy + coverage report)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-03.1-001, OBL-D-03.3-001, SO-D-03.2-001, CR-D-03.2-001

11. **Risk if not met:** M — Failure leaves operator accounts — which have the highest blast radius — vulnerable to single-factor credential compromise; customer opt-in rate below 30% would suggest a UX problem.

12. **Affected Stakeholders:** CTO, Lead Dev, Operators (MFA enrollees), Customers (opt-in)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** MEDIUM

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-03.3-001 — Least Privilege + RBAC

1. **Description:** Restrict access to personal data and product functionality to authorised personnel only, and enforce the principle of least privilege. For TinyTask, this obligation is met through managed identity provider custom claims (RBAC roles: `admin`, `member`, `viewer`) and through managed IAM policy segmentation (per-service roles, per-environment roles, no wildcard permissions). The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access/D-03.3/D-03.3.json`) treats least privilege as the operational refinement of authentication: even authenticated users should only see what their role requires. GDPR-C10 (Art. 5(1)(c) — data minimisation in access patterns) and GDPR-C17 (Art. 32 — access control as appropriate measure) jointly drive the GDPR coverage. NI=3.000 reflects the high intensity of the access-control obligation. At MICRO scale, RBAC is enforced at three layers: managed identity provider claims (customer-facing), managed IAM (operator), and application-layer authorization (fine-grained per-resource checks). The LIGHTWEIGHT implementation tier reflects managed-service configuration + quarterly review. The obligation is mixed ONE_TIME (initial role definition) + CONTINUOUS (ongoing enforcement).

2. **Scope:** Customer RBAC: admin / member / viewer roles enforced via managed identity provider custom claims and application-layer checks. Operator RBAC: per-service IAM roles with no cross-service wildcards. Application-layer authorization: per-resource ownership checks on every read/write.

3. **Out of Scope:** Attribute-based access control (ABAC) with policy engine (over-engineered at MICRO); fine-grained resource-level permissions beyond ownership (out of scope for v1); just-in-time access provisioning (deferred to LIGHTWEIGHT roadmap).

4. **Source Article:** GDPR Art. 5(1)(c) + Art. 32(1); CRA Annex I §1(5) (co-annexed authentication); GDPR-C10, GDPR-C17

5. **NIST CSF Anchors:** PR.AA-01 (Identity and credential management), PR.AA-04 (Access permissions are managed), PR.AA-05 (Identity proofing)

6. **Verification Criteria:**

   - Quarterly RBAC review: enumerate every managed identity provider custom claim assignment and every managed IAM policy; flag any unused-for-90-days role for removal.

   - Application-layer authorization test suite: every protected endpoint has a test that proves a non-owner receives 403; suite runs in CI on every PR.

   - Annual role-redesign review: align customer roles with the latest product feature set; document any retired roles.

7. **Verification Method:** INSPECT (RBAC review minutes) + TEST (authorization test suite) + ANALYZE (managed IAM least-privilege findings)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-03.1-001, OBL-D-03.2-001, OBL-D-03.4-001, SO-D-03.3-001, CR-D-03.3-001

11. **Risk if not met:** H — Failure to enforce least privilege amplifies the blast radius of every credential leak and undermines GDPR Art. 5(1)(c) data-minimisation-by-access.

12. **Affected Stakeholders:** Customers (data subjects), CTO, Lead Dev, DPO (RBAC oversight), HR (role assignment for staff)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-03.4-001 — Secure Default Configuration

1. **Description:** Disable unused ports and services; remove or rename default credentials; ship secure default configuration. For TinyTask, this obligation is met through the managed identity provider's secure-by-default posture (no default passwords, email-verification required), managed compute's default-deny IAM model, and the absence of any customer-facing service that ships with anonymous access. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access/D-03.4/D-03.4.json`) treats secure defaults as the preventive complement to D-03.1 authentication: an attacker should never be able to log in with a default password because there should not be a default password. CRA-C03 (Annex I §1(7)) is the sole authority — the 'no default passwords, secure defaults' obligation is CRA-specific. At MICRO scale, secure defaults are realised through managed-service configuration choices (managed identity provider defaults, managed hosting service defaults) plus a hardened-default review of any self-managed components. The obligation is ONE_TIME in setup but operates CONTINUOUSLY in effect.

2. **Scope:** All customer-facing services (managed identity provider defaults); all managed services in the deployment (compute, managed object storage, managed NoSQL, managed database — secure defaults verified by managed configuration rules); all third-party libraries (no default API keys shipped, all secrets injected at deploy time via managed secrets custody).

3. **Out of Scope:** Customer-managed deployment hardening (not applicable — SaaS only); self-hosted on-premises installations (out of scope); air-gapped deployments (out of scope).

4. **Source Article:** CRA Annex I §1(7) (no default passwords, secure defaults); CRA-C03

5. **NIST CSF Anchors:** PR.AA-01 (Identity and credential management), PR.PS-01 (Baseline configuration), PR.PS-01 (Configuration change control)

6. **Verification Criteria:**

   - Managed configuration rule `iam-root-access-key-check` confirms COMPLIANT (no root access keys exist); `iam-password-policy` confirms minimum 14-char policy is attached.

   - Managed identity provider configuration review: email-verification required, anonymous access disabled, password policy aligned with documented strong-authentication guidance.

   - Annual hardened-default snapshot review against managed hosting Foundations Benchmark; deviations documented with rationale.

7. **Verification Method:** INSPECT (managed configuration + managed identity provider config + hardened-default review) + DEMONSTRATE (live deployment hardening check)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-03.1-001, OBL-D-03.3-001, SO-D-03.4-001, CR-D-03.4-001

11. **Risk if not met:** H — Failure to ship secure defaults means every new deployment starts in a vulnerable state, and customer administrators may not have the expertise to harden them.

12. **Affected Stakeholders:** Customers (downstream consumers), CTO, Lead Dev, managed hosting provider (managed-service defaults)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment



**D-03 Verification Cross-Walk (for human reviewer):**


| OBL ID | Verification Criteria Count | Method Mix | Primary NIST Anchor | Cadence |
|--------|----------------------------:|------------|---------------------|---------|
| OBL-D-03.1-001 | 3 | DEMONSTRATE + INSPECT | PR.AA-01 | Quarterly |
| OBL-D-03.2-001 | 3 | DEMONSTRATE + INSPECT | PR.AA-01 | Quarterly |
| OBL-D-03.3-001 | 3 | INSPECT + TEST + ANALYZE | PR.AA-04 | Quarterly + per-PR |
| OBL-D-03.4-001 | 3 | INSPECT + DEMONSTRATE | PR.AA-01 | Annual + per-build |

**D-03 Owner-Responsibility Decomposition:**


| Role | Primary Responsibility in this Sub-Domain | Backup / Approver |
|------|-------------------------------------------|-------------------|
| CTO | Identity-provider selection; MFA policy; IAM strategy | Lead Dev |
| Lead Dev | Managed identity provider configuration; IAM policy implementation; RBAC enforcement code | CTO |

---


### 5.4 D-04 — Incident Response (4 cards)


D-04 covers the full incident lifecycle: severity limitation (D-04.1), containment (D-04.2), notification (D-04.3), restoration (D-04.4). D-04.3 is the CONTEXTUAL obligation — it activates only on a compound event (personal-data breach AND exploited vulnerability). T-001 (Doc 09) and T-H-001 (Sprint 1 §3.5) document the max-SLA 24h routing decision: both CNPD and ENISA are notified within the tighter 24h clock.


### OBL-D-04.1-001 — Exploit Severity Limitation

1. **Description:** Design the system to limit the severity of exploits and implement fail-safe mechanisms that prevent a single vulnerability from causing disproportionate harm. For TinyTask, this obligation is met through managed monitoring alarms on anomalous metrics (error rates, latency spikes, unauthorized API calls), managed notification routing to the on-call rotation, and graceful-degradation patterns in the application code (circuit breakers, retries with exponential backoff). The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident/D-04.1/D-04.1.json`) treats severity limitation as the design-time counterpart to D-04.2 incident containment: the system should be architected so that even when an exploit occurs, the blast radius is bounded. CRA-C13 (Annex I §1(8)) is the sole authority. At MICRO scale, the implementation is configuration-driven (managed monitoring alarms + managed notification routing) plus application-layer defensive patterns (no destructive operations without confirmation, idempotent operations, rollback paths). The obligation is ONE_TIME in design but operates CONTINUOUSLY through monitoring.

2. **Scope:** All managed monitoring alarms on production metrics (error rate >1%, p99 latency >2s, API 4xx/5xx rates); all managed notification topics subscribed by the on-call rotation; all application code paths with destructive operations (delete, mass-update) requiring explicit confirmation.

3. **Out of Scope:** Active-active multi-region failover (out of MICRO scope — single-region with backup); chaos engineering with production traffic (out of MICRO scope — staging-only chaos drills).

4. **Source Article:** CRA Annex I §1(8) (limit severity of exploits, fail-safe); CRA-C13

5. **NIST CSF Anchors:** RS.MA-01 (Response plan is executed), DE.AE-06 (Notifications from detection systems), PR.PS-01 (Baseline configuration)

6. **Verification Criteria:**

   - Managed monitoring alarm coverage report: every production metric tracked in Doc 09 has at least one alarm; verified quarterly.

   - Annual chaos drill in staging: simulated service degradation (latency injection) confirms circuit breakers trip and degraded mode is reached within 60 seconds.

   - Destructive-operation audit: `git grep` for `DELETE FROM`, `DROP TABLE`, `rm -rf` returns only code paths with explicit confirmation gating; reviewed quarterly.

7. **Verification Method:** TEST (chaos drill in staging) + INSPECT (alarm coverage report + code audit) + DEMONSTRATE (live degradation scenario)

8. **Owner:** CTO + DPO + Compliance Lead

9. **Status:** TODO

10. **Dependencies:** OBL-D-04.2-001, OBL-D-04.3-001, OBL-D-04.4-001, SO-D-04.1-001, CR-D-04.1-001

11. **Risk if not met:** H — Failure means every incident escalates beyond its natural blast radius, increasing both customer harm and the likelihood of ENISA/CNPD notifiable thresholds being crossed.

12. **Affected Stakeholders:** Customers (impacted during incidents), CTO, Lead Dev (on-call), DPO (severity classification for reporting)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD 72h (GDPR Art. 33 — controller notification)

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment; ENISA — CRA exploited-vulnerability single reporting point; CNCS (Centro Nacional de Cibersegurança) — PT CSIRT for early-warning + incident coordination


### OBL-D-04.2-001 — Availability Restoration + DoS Resilience

1. **Description:** Restore availability after incidents and build resilience against denial-of-service attacks. For TinyTask, this obligation is met through a documented 4-hour containment playbook, managed standard DDoS protection on edge and DNS, and runbook-driven failover to the warm-standby database replica in case of primary-region degradation. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident/D-04.2/D-04.2.json`) couples availability restoration to the broader incident-response cycle: containment (D-04.2), notification (D-04.3), and recovery (D-04.4) are sequential stages. GDPR-C18 (Art. 32(1)(b)(c) — resilience and restoration) and CRA-C11 (Annex I §1(9) — resilience to DoS) jointly drive the obligation. At MICRO scale, DoS resilience is delegated to managed hosting services (managed standard DDoS protection, edge caching) and restoration is runbook-driven (CTO + Lead Dev as on-call). The obligation is mixed TRIGGERED + ONE_TIME — the runbook is built once but executed every time an incident occurs.

2. **Scope:** Managed edge + DNS DDoS protection (managed standard); warm-standby managed database read replica (for disaster recovery); documented 4-hour containment playbook in `runbooks/incident-response.md`; managed notification pager rotation for 24/7 on-call.

3. **Out of Scope:** Multi-region active-active (out of MICRO scope — single-region + DR standby is sufficient); advanced managed DDoS protection tiers (over-scope at MICRO); on-site incident command centre (out of scope — distributed on-call is sufficient).

4. **Source Article:** GDPR Art. 32(1)(b)(c); CRA Annex I §1(9) (resilience to DoS); GDPR-C18, CRA-C11

5. **NIST CSF Anchors:** RS.MA-01 (Response plan executed), GV.RR-02 (Personnel know their roles), PR.IR-04 (Adequate resource capacity)

6. **Verification Criteria:**

   - Annual containment drill: simulated DDoS attack on staging edge; managed standard DDoS protection auto-mitigates within 5 minutes; runbook followed end-to-end; recovery time measured.

   - Quarterly DR drill: failover to warm-standby managed database; RTO measured (target <24h); RPO measured (target <1h); results in Doc 09 family.

   - Managed notification pager rotation test: weekly synthetic alert to on-call; verified that primary responds within 15 minutes.

7. **Verification Method:** TEST (DR drill + chaos test) + DEMONSTRATE (live DDoS simulation in staging) + INSPECT (runbook review minutes)

8. **Owner:** CTO + DPO + Compliance Lead

9. **Status:** TODO

10. **Dependencies:** OBL-D-04.1-001, OBL-D-04.3-001, OBL-D-04.4-001, SO-D-04.2-001, CR-D-04.2-001

11. **Risk if not met:** H — Failure to restore availability within SLA creates cascading customer impact and potential GDPR/CRA notification thresholds; DoS resilience gaps expose the entire SaaS surface.

12. **Affected Stakeholders:** Customers (availability impact), CTO, Lead Dev (on-call), DPO (incident classification)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD 72h (GDPR Art. 33 — controller notification)

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment; ENISA — CRA exploited-vulnerability single reporting point; CNCS (Centro Nacional de Cibersegurança) — PT CSIRT for early-warning + incident coordination


### OBL-D-04.3-001 — Breach Notification (T-001)

1. **Description:** Notify the supervisory authority within 72 hours (GDPR Art. 33) of a personal-data breach, and within 24 hours (CRA Art. 14) of awareness of an exploited vulnerability that has caused or may cause significant harm. As a processor for B2B client content, also notify controllers 'without undue delay' (GDPR Art. 33(2)). For TinyTask, this obligation is met through a unified incident-response workflow that routes every qualifying incident to the max-SLA clock (24h) and triggers both the CNPD notification (GDPR) and the ENISA report (CRA) in a single coordinated notification. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident/D-04.3/D-04.3.json`) frames D-04.3 as the CONTEXTUAL obligation par excellence: it is STRUCTURAL in the sense that the workflow must always be ready, but it is TRIGGERED by a compound event (personal-data breach AND exploited vulnerability simultaneously) that activates both GDPR and CRA clocks in tension. Tension T-H-001 (Sprint 1 §3.5) and T-001 (Doc 09) document the routing decision: max-SLA wins, both regulators notified. The obligation is TRIGGERED only — there is no continuous activity. The workflow itself is STRUCTURAL. At MICRO scale, the workflow is a single Markdown runbook + a managed messaging service channel + a Contact List that includes CNPD, ENISA, and CNCS.

2. **Scope:** All qualifying personal-data breaches (GDPR Art. 4(12) definition); all exploited vulnerabilities with significant harm (CRA Art. 14(1) trigger); all processor→controller notifications for B2B client breaches (GDPR Art. 33(2)). Notification templates pre-staged for CNPD, ENISA, and customer-controller variants.

3. **Out of Scope:** Routine security events that do not meet breach or harm thresholds (handled internally without external notification); vulnerability disclosure to ENISA for non-exploited vulnerabilities (handled via OBL-D-02.3 CVD policy instead); post-incident lessons-learned reports (internal only).

4. **Source Article:** GDPR Art. 33(1) (72h SA notification), Art. 33(2) (processor→controller 'without undue delay'); CRA Art. 14(1) (24h exploited-vulnerability report); GDPR-C21, GDPR-C23, CRA-C25

5. **NIST CSF Anchors:** RS.MA-01 (Response plan executed), GV.RR-02 (Personnel know roles), RS.CO-02 (Incident reporting), DE.AE-06 (Notifications)

6. **Verification Criteria:**

   - Notification templates pre-staged for CNPD (PT), ENISA (EU), and customer-controller variants; templates reviewed annually by DPO + Legal.

   - Annual tabletop: simulated compound event triggers both clocks; max-SLA (24h) routing applied; both notifications dispatched within the 24h window end-to-end.

   - Contact list for CNPD, ENISA, CNCS verified semi-annually: phone numbers, email addresses, web-forms all current; documented review minutes.

7. **Verification Method:** TEST (tabletop exercise) + DEMONSTRATE (live notification dispatch to a regulator test endpoint if available) + INSPECT (template + contact list review)

8. **Owner:** CTO + DPO + Compliance Lead

9. **Status:** TODO

10. **Dependencies:** OBL-D-04.1-001, OBL-D-04.2-001, OBL-D-04.4-001, OBL-D-02.3-001 (CVD cross-ref), SO-D-04.3-001, CR-D-04.3-001, T-001

11. **Risk if not met:** H — Missing the 24h CRA clock creates direct EU market-surveillance violation; missing the 72h GDPR clock creates a separate CNPD violation; failure to notify controllers under Art. 33(2) damages B2B customer trust.

12. **Affected Stakeholders:** Customers (data subjects + controllers), CTO, DPO (notification owner), Legal (regulatory text), CNPD + ENISA + CNCS (recipients), Compliance Lead (incident commander)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD 72h + ENISA 24h (max-SLA routing — see T-001)

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment; ENISA — CRA exploited-vulnerability single reporting point; CNCS (Centro Nacional de Cibersegurança) — PT CSIRT for early-warning + incident coordination


### OBL-D-04.4-001 — Data Restoration Post-Incident

1. **Description:** Ensure ongoing availability and ability to restore personal and product data after an incident. For TinyTask, this obligation is met through managed backup with daily snapshots of the production managed relational database (35-day retention), point-in-time recovery enabled, and an annual full-restore drill into an isolated test account to verify RTO/RPO targets. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident/D-04.4/D-04.4.json`) treats data restoration as the recovery-side counterpart to D-04.2 containment: an incident is not closed until the affected data is verifiably restored. GDPR-C16 (Art. 32(1)(b)(c) — ability to restore availability and access) drives the GDPR coverage with NI=2.000 (medium intensity). At MICRO scale, restoration is delegated to managed backup services plus an annual drill. RTO target 24h, RPO target 1h — both aligned with the proportionality model (LIGHTWEIGHT tier, MICRO budget). The obligation is CONTINUOUS — backups must always be running, and verification must occur at least annually.

2. **Scope:** managed backup vaults for managed relational database (daily snapshot, 35-day retention); managed object storage cross-region replication for the audit-log bucket; managed NoSQL point-in-time recovery (35-day window); annual full-restore drill into isolated test account.

3. **Out of Scope:** Active-active multi-region (out of MICRO scope — DR standby is sufficient); continuous data replication to a third region (over-engineered); backup verification by hashing every byte (impractical — sampling and integrity checks at restore time are sufficient).

4. **Source Article:** GDPR Art. 32(1)(b)(c); GDPR-C16

5. **NIST CSF Anchors:** RS.MA-01 (Response plan executed), PR.IR-04 (Adequate resource capacity), PR.PS-01 (Baseline configuration)

6. **Verification Criteria:**

   - Managed backup compliance report: every protected resource has a successful backup within the last 24h; verified daily.

   - Annual full-restore drill: backup restored to isolated test account; RTO measured (target <24h); RPO measured (target <1h); results documented.

   - Quarterly spot-check: random backup restored to test account; byte-equality with source confirmed via checksum.

7. **Verification Method:** TEST (annual full-restore drill) + INSPECT (managed backup compliance report + spot-check) + DEMONSTRATE (live RTO/RPO measurement)

8. **Owner:** CTO + DPO + Compliance Lead

9. **Status:** TODO

10. **Dependencies:** OBL-D-04.1-001, OBL-D-04.2-001, OBL-D-01.4-001 (integrity), SO-D-04.4-001, CR-D-04.4-001

11. **Risk if not met:** H — Failure to restore data within RTO/RPO creates compounding customer harm and may trigger GDPR Art. 32 enforcement if restoration capability is not demonstrated.

12. **Affected Stakeholders:** Customers (data subjects relying on availability), CTO, Lead Dev (restoration execution), DPO (oversight)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD 72h (GDPR Art. 33 — controller notification)

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment; ENISA — CRA exploited-vulnerability single reporting point; CNCS (Centro Nacional de Cibersegurança) — PT CSIRT for early-warning + incident coordination



**D-04 Verification Cross-Walk (for human reviewer):**


| OBL ID | Verification Criteria Count | Method Mix | Primary NIST Anchor | Cadence |
|--------|----------------------------:|------------|---------------------|---------|
| OBL-D-04.1-001 | 3 | TEST + INSPECT + DEMONSTRATE | RS.MA-01 | Quarterly + annual chaos |
| OBL-D-04.2-001 | 3 | TEST + DEMONSTRATE + INSPECT | RS.MA-01 | Annual DR drill |
| OBL-D-04.3-001 | 3 | TEST + DEMONSTRATE + INSPECT | RS.CO-02 | Annual tabletop |
| OBL-D-04.4-001 | 3 | TEST + INSPECT + DEMONSTRATE | PR.IR-04 | Annual + quarterly spot |

**D-04 Owner-Responsibility Decomposition:**


| Role | Primary Responsibility in this Sub-Domain | Backup / Approver |
|------|-------------------------------------------|-------------------|
| CTO | Incident commander; technical severity classification | Lead Dev |
| DPO | Regulatory classification (personal-data breach?); notification routing | Legal |
| Compliance Lead | Notification dispatch; regulator contact; tabletop coordination | DPO |

---


### 5.5 D-05 — Data Lifecycle (4 cards)


D-05 covers the data subject's lifecycle with their data: minimisation (D-05.1), storage limitation (D-05.2), erasure (D-05.3), portability (D-05.4). All four are GDPR-led; CRA imposes only D-05.3 (secure deletion) as a co-obligation. The implementation combines schema-level enforcement (D-05.1), retention-cron jobs (D-05.2), and customer-facing API endpoints (D-05.3, D-05.4).


### OBL-D-05.1-001 — Data Minimization

1. **Description:** Process only personal data that is adequate, relevant, and limited to what is necessary for the purpose. For TinyTask, this obligation is met through field-level enforcement in the application schema: the database schema declares which fields are required for each entity, and the application layer rejects writes that include non-schema fields. Customer onboarding collects only email + name + (optional) project name — no excessive profiling, no marketing-data fields at sign-up. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Lifecycle/D-05.1/D-05.1.json`) treats minimisation as the design-time expression of GDPR Art. 5(1)(c): every field in the schema is a deliberate choice, and every field absent from the schema is a minimisation decision. GDPR-C01 (Art. 5(1)(c)) and CRA-C10 (Annex I §1(10) — least data collected) jointly drive the obligation with NI=3.000. At MICRO scale, minimisation is enforced at three layers: schema (database constraints), application (input validation), and onboarding UX (no opt-in for marketing data). The obligation is mixed CONTINUOUS (enforcement) + ONE_TIME (initial schema design).

2. **Scope:** Database schema for all customer-facing entities (users, projects, tasks); onboarding flow (minimum required fields); analytics pipeline (no PII sent to third-party analytics); logs (no PII in application logs — strip at ingest).

3. **Out of Scope:** Customer-driven bulk imports of legacy data (out of SaaS control — minimisation applies at import time); analytics with PII (out of scope — analytics must be anonymous or aggregated); marketing enrichment (out of scope — TinyTask does not enrich customer data).

4. **Source Article:** GDPR Art. 5(1)(c); CRA Annex I §1(10); GDPR-C01, CRA-C10

5. **NIST CSF Anchors:** ID.AM-08 (Asset inventory), PR.DS-01 (Data-at-rest)

6. **Verification Criteria:**

   - Schema review minutes (annual): every entity enumerated, every field justified by a documented business purpose; non-justified fields flagged for removal.

   - Application-layer input validation test suite: every endpoint rejects fields not in the schema; verified in CI on every PR.

   - Analytics audit (quarterly): third-party analytics endpoints inspected; no PII transmitted (verified by packet capture on a synthetic user action).

7. **Verification Method:** INSPECT (schema review + analytics audit) + TEST (input validation suite) + ANALYZE (log scan for PII patterns)

8. **Owner:** CTO + DPO

9. **Status:** TODO

10. **Dependencies:** OBL-D-05.2-001, OBL-D-05.3-001, OBL-D-05.4-001, PO-D-05.1-001, SO-D-05.1-001, CR-D-05.1-001

11. **Risk if not met:** H — Failure to minimise creates GDPR Art. 5(1)(c) audit-finding exposure and increases the blast radius of every other obligation (more data = more risk in D-01, D-04, D-05.3).

12. **Affected Stakeholders:** Customers (data subjects), CTO (schema owner), DPO (oversight), Lead Dev (validation)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-05.2-001 — Storage Limitation

1. **Description:** Do not keep personal data longer than necessary for the purpose for which it is processed. For TinyTask, retention is enforced through three policies: customer-PII deleted on account closure + 30-day grace, audit logs retained 7 years (regulatory minimum), DSAR working data deleted within 30 days of request completion. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Lifecycle/D-05.2/D-05.2.json`) treats storage limitation as the temporal counterpart to data minimisation: collect less (D-05.1) and keep it for less time (D-05.2). GDPR-C02 (Art. 5(1)(e) — storage limitation) and GDPR-C03 (Art. 5(1)(e) — further processing compatible) jointly drive the GDPR coverage with NI=3.000. At MICRO scale, retention is enforced through application-layer cron jobs (nightly scan for expired records) + database-level TTL on ephemeral tables + managed object storage lifecycle policies on the audit-log bucket. The obligation is CONTINUOUS — every record must be checked against the retention clock daily.

2. **Scope:** Customer PII (lifetime of account + 30-day grace); audit logs (7 years per regulatory minimum); DSAR working data (30 days post-completion); application logs (90 days in managed log service, then archived to managed object storage with 7-year lifecycle); backup snapshots (35 days in managed backup).

3. **Out of Scope:** Long-term archival for analytics (out of scope — analytics must be aggregated or anonymised); indefinite retention for regulatory-hold legal proceedings (separate legal-hold policy, not in scope here); retention for tax/financial records (handled separately by accounting, 10-year retention per PT commercial code).

4. **Source Article:** GDPR Art. 5(1)(e); GDPR-C02, GDPR-C03

5. **NIST CSF Anchors:** ID.AM-08 (Asset inventory), PR.DS-01 (Data-at-rest)

6. **Verification Criteria:**

   - Nightly retention-scan job: every record with a `retention_until` field is checked; expired records are soft-deleted then hard-deleted after 7 days; verified by daily job log.

   - Managed object storage lifecycle policy audit (quarterly): audit-log bucket has 7-year expiry; verified by managed configuration rule for lifecycle configuration.

   - DSAR completion test: completed DSAR has its working data deleted within 30 days; verified by monthly DSAR audit.

7. **Verification Method:** TEST (retention-scan job log + DSAR audit) + INSPECT (managed object storage lifecycle policy) + DEMONSTRATE (live retention-triggered deletion)

8. **Owner:** CTO + DPO

9. **Status:** TODO

10. **Dependencies:** OBL-D-05.1-001, OBL-D-05.3-001, OBL-D-09.4-001 (RoPA records), PO-D-05.2-001, SO-D-05.2-001, CR-D-05.2-001

11. **Risk if not met:** H — Failure to enforce retention creates ongoing GDPR Art. 5(1)(e) violation and accumulates storage cost + risk surface over time.

12. **Affected Stakeholders:** Customers (data subjects), CTO, DPO (retention policy owner), Compliance Lead (audit)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-05.3-001 — Right to Erasure

1. **Description:** Enable complete and secure deletion of personal data on data-subject request, unless a legal exception applies. For TinyTask, the erasure API endpoint accepts a verified data-subject request, cascades the deletion across all production data stores (managed relational database primary, managed object storage backups via lifecycle, managed log archives via redaction), and returns a signed erasure certificate within 7 days of verified request. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Lifecycle/D-05.3/D-05.3.json`) treats erasure as the data-subject-facing expression of storage limitation (D-05.2): the customer can accelerate the retention clock by requesting immediate deletion. GDPR-C06 (Art. 17 — right to erasure) and CRA-C16 (Annex I §1(11) — secure deletion) jointly drive the obligation with NI=3.000. At MICRO scale, erasure is an application-layer API endpoint backed by a workflow that touches every production data store. The 7-day SLA is a deliberate proportionality choice (GDPR Art. 12(3) allows 'without undue delay' up to one month; TinyTask commits to 7 days). The obligation is mixed TRIGGERED (each DSAR) + ONE_TIME (initial API implementation).

2. **Scope:** All production data stores holding customer PII: managed relational database primary (hard delete), managed object storage customer-uploaded assets (lifecycle-accelerated deletion), managed NoSQL tables (hard delete), managed log archives (redaction via log-group filter), backups (lifecycle-accelerated). Erasure API endpoint at `/api/v1/dsar/erasure` with audit trail.

3. **Out of Scope:** Erasure of data in third-party processor backups where contractual SLA exceeds 30 days (documented as residual exposure); erasure of data in legal-hold archives (out of scope — handled by legal-hold policy); erasure of anonymised analytics (no PII to erase).

4. **Source Article:** GDPR Art. 17 (right to erasure); CRA Annex I §1(11) (secure deletion); GDPR-C06, CRA-C16

5. **NIST CSF Anchors:** PR.DS-01 (Data-at-rest), ID.AM-08 (Asset inventory)

6. **Verification Criteria:**

   - Erasure API test (monthly): synthetic DSAR submitted; verified within 7 days that all PII is removed from production data stores; erasure certificate generated and signed.

   - Backup erasure verification: post-erasure, the next backup snapshot is restored to test account; PII confirmed absent (negative search for known email/name patterns).

   - Annual erasure workflow review: every data store enumerated, every erasure path documented, exceptions (legal hold, third-party) reviewed.

7. **Verification Method:** TEST (erasure API end-to-end) + DEMONSTRATE (live DSAR completion with certificate) + INSPECT (annual workflow review)

8. **Owner:** CTO + DPO

9. **Status:** TODO

10. **Dependencies:** OBL-D-05.1-001, OBL-D-05.2-001, OBL-D-05.4-001, PO-D-05.3-001, SO-D-05.3-001, CR-D-05.3-001

11. **Risk if not met:** H — Failure to honour erasure requests within GDPR Art. 12(3) timeframe creates direct regulatory enforcement risk and undermines customer trust.

12. **Affected Stakeholders:** Customers (data subjects exercising right), CTO, DPO (DSAR owner), Lead Dev (API implementation), Legal (exception handling)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-05.4-001 — Right to Data Portability

1. **Description:** Provide personal data export in a structured, commonly used, machine-readable format on data-subject request. For TinyTask, the portability API endpoint accepts a verified DSAR, generates a JSON export of all customer-PII entities owned by the requester, signs the bundle, and returns it within 48 hours of verified request. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Lifecycle/D-05.4/D-05.4.json`) treats portability as the positive counterpart to erasure: the data subject can request a copy before deletion, or in lieu of deletion if they are switching to a competing service. GDPR-C07 (Art. 20 — right to portability) is the sole authority with NI=3.000; CRA does not impose a comparable portability obligation directly. At MICRO scale, portability is an application-layer API endpoint backed by a JSON serializer that covers all customer-PII entities. The 48-hour SLA is a deliberate over-compliance (GDPR Art. 12(3) allows one month). The obligation is TRIGGERED per request, but the API must always be operational.

2. **Scope:** All customer-PII entities: user profile, projects, tasks, comments, attachments metadata (the attachments themselves are downloadable via signed URLs in the export bundle). Portability API endpoint at `/api/v1/dsar/portability` returning a signed ZIP with JSON manifests + signed-URL manifest for binary assets.

3. **Out of Scope:** Portability of data provided by the data subject to a third party (out of scope — TinyTask does not process third-party data); portability of inferred or derived data (out of scope per Art. 20(1) — only data provided by the data subject); real-time export streaming (out of scope — batch export within 48h is sufficient).

4. **Source Article:** GDPR Art. 20 (right to data portability); GDPR-C07

5. **NIST CSF Anchors:** ID.AM-08 (Asset inventory), PR.DS-01 (Data-at-rest)

6. **Verification Criteria:**

   - Portability API test (monthly): synthetic DSAR submitted; JSON export verified to contain all owned entities within 48 hours; signed bundle integrity confirmed.

   - Annual portability schema review: export JSON schema aligned with any product feature additions; documented in the DSAR runbook.

   - Signed-URL manifest test: every binary asset in the export has a valid signed URL that expires within 7 days (matches the customer's expectation of usable URLs).

7. **Verification Method:** TEST (portability API end-to-end) + DEMONSTRATE (live export bundle inspection) + INSPECT (annual schema review)

8. **Owner:** CTO + DPO

9. **Status:** TODO

10. **Dependencies:** OBL-D-05.1-001, OBL-D-05.2-001, OBL-D-05.3-001, PO-D-05.4-001, SO-D-05.4-001, CR-D-05.4-001

11. **Risk if not met:** H — Failure to honour portability requests within GDPR Art. 12(3) timeframe creates direct regulatory enforcement risk; format incompatibility (e.g., proprietary binary) creates Art. 20 violation per se.

12. **Affected Stakeholders:** Customers (data subjects exercising right), CTO, DPO, Lead Dev, Legal

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment



**D-05 Verification Cross-Walk (for human reviewer):**


| OBL ID | Verification Criteria Count | Method Mix | Primary NIST Anchor | Cadence |
|--------|----------------------------:|------------|---------------------|---------|
| OBL-D-05.1-001 | 3 | INSPECT + TEST + ANALYZE | PR.DS-01 | Annual + per-PR |
| OBL-D-05.2-001 | 3 | TEST + INSPECT + DEMONSTRATE | PR.DS-01 | Daily + quarterly |
| OBL-D-05.3-001 | 3 | TEST + DEMONSTRATE + INSPECT | PR.DS-01 | Monthly + annual review |
| OBL-D-05.4-001 | 3 | TEST + DEMONSTRATE + INSPECT | PR.DS-01 | Monthly + annual review |

**D-05 Owner-Responsibility Decomposition:**


| Role | Primary Responsibility in this Sub-Domain | Backup / Approver |
|------|-------------------------------------------|-------------------|
| CTO | Schema design; retention policy; DSAR API implementation | DPO |
| DPO | DSAR intake; erasure verification; portability format review | CTO |

---


### 5.6 D-06 — Supply Chain (3 cards)


D-06 covers supply-chain security: processor validation (D-06.1), SBOM (D-06.2, CRA sole authority), DPA (D-06.3, GDPR-led). The implementation combines procurement-time attestation review (D-06.1), CI-driven SBOM generation (D-06.2), and template-based DPA execution (D-06.3). D-06.2 is the per-se CRA Art. 13(11) obligation; failure to produce or retain the SBOM is itself the violation.


### OBL-D-06.1-001 — Processor Sufficient Guarantees

1. **Description:** Use only processors (sub-processors) that provide sufficient guarantees to implement appropriate technical and organisational measures. For TinyTask, this obligation is met by validating every sub-processor's security posture through a documented due-diligence process: managed hosting provider (ISO 27001 attestation), managed identity provider (ISO 27001 attestation), payment processor (PCI DSS Level 1 + ISO 27001 attestation), and any other processor with documented attestations on file. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/D-06.1.json`) treats processor validation as the upstream gate of supply-chain security: no downstream DPA, SBOM, or contractual obligation can compensate for choosing an insecure processor. GDPR-C11 (Art. 28(1)) is the sole authority with NI=3.000; the MINIMAL implementation tier reflects supplier-attestation-only (no in-house audit programme). At MICRO scale, processor validation is a procurement-time check: before signing a contract, the Compliance Lead verifies the supplier has current ISO 27001 attestation or equivalent, and the attestation is filed in the supplier-attestation register. The obligation is ONE_TIME per supplier.

2. **Scope:** All processors with access to customer PII or product data: managed hosting provider (primary cloud), managed identity provider (authentication), payment processor, any future sub-processor. Validation includes ISO 27001 attestation review and DPA scope confirmation.

3. **Out of Scope:** Open-source dependencies (handled by OBL-D-06.2 SBOM); free-tier SaaS tools without formal attestation (out of scope — only contracted processors are validated); employee-vetted vendors without PII access (out of scope — no DPA needed).

4. **Source Article:** GDPR Art. 28(1); GDPR-C11

5. **NIST CSF Anchors:** GV.SC-03 (Contracts with suppliers and third-party partners), PR.PS-01 (Configuration change control), GV.OC-01 (Organizational risk strategy)

6. **Verification Criteria:**

   - Supplier-attestation register (Doc 09 family): every contracted processor has current ISO 27001 attestation or equivalent; verified at contract signature and refreshed annually.

   - Annual supplier review: Compliance Lead re-confirms attestation currency; any lapsed attestation triggers escalation (DPO + CTO).

   - New-supplier intake checklist: ISO 27001 + DPA template + security-clause checklist; mandatory before contract execution.

7. **Verification Method:** INSPECT (supplier-attestation register + intake checklist) + DEMONSTRATE (live walk-through of a new-supplier intake)

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** OBL-D-06.2-001, OBL-D-06.3-001, SO-D-06.1-001, CR-D-06.1-001

11. **Risk if not met:** H — Failure to validate a processor shifts liability to TinyTask as controller — a processor breach becomes a TinyTask GDPR Art. 28 violation.

12. **Affected Stakeholders:** Customers (downstream impact of processor breach), CTO, Procurement, DPO, Compliance Lead, Legal

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-06.2-001 — SBOM Documentation

1. **Description:** Document all third-party components included in the product in a machine-readable format (SBOM). For TinyTask, this obligation is met through the same CI pipeline as OBL-D-02.1-001: every release produces a CycloneDX 1.5 SBOM that is signed and archived alongside the build artifacts in the managed object storage release bucket. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.2/D-06.2.json`) treats SBOM as the structural precondition for downstream vulnerability management (D-02.1, D-02.2) and supply-chain transparency (D-06.1, D-06.3). CRA-C18 (Art. 13(11)) is the sole authority with NI=3.000; OBL-D-06.2-001 is flagged as 'CRA sole authority' (DR-006) in legacy §3.1. At MICRO scale, SBOM generation is automated in CI; human contribution is the retention discipline (10-year per CRA Art. 13(9)) and the per-release signature verification. The obligation is CONTINUOUS — every release must have a fresh SBOM.

2. **Scope:** All third-party components in every release: npm dependencies (direct + transitive), Docker base image packages, infrastructure-as-code modules. SBOM format: CycloneDX 1.5 JSON. Storage: managed object storage release bucket with 10-year retention and object lock (compliance mode) per OBL-D-01.4-001.

3. **Out of Scope:** SBOM for in-development features not yet shipped (out of CRA scope until release); SBOM for internal tools not distributed to customers (out of CRA scope); SBOM for free/open-source projects consumed but not redistributed (out of CRA scope — TinyTask does not redistribute).

4. **Source Article:** CRA Art. 13(11); CRA-C18

5. **NIST CSF Anchors:** GV.SC-03 (Contracts with suppliers), PR.PS-01 (Configuration change control), ID.AM-08 (Asset inventory)

6. **Verification Criteria:**

   - Per-release SBOM generation: CycloneDX JSON signed and archived in managed object storage release bucket; verified by CI gate.

   - Quarterly SBOM diff review: identify new transitive dependencies; confirm none on CRA denylist or with known active exploits.

   - Annual SBOM retention audit: every release SBOM still retrievable from the release bucket; 10-year retention policy verified.

7. **Verification Method:** TEST (CI gate produces SBOM) + INSPECT (SBOM diff + retention audit) + DEMONSTRATE (SBOM fetch + signature verification)

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** OBL-D-02.1-001, OBL-D-06.1-001, OBL-D-06.3-001, SO-D-06.2-001, CR-D-06.2-001

11. **Risk if not met:** H — Failure to produce SBOM is a per-se CRA Art. 13(11) violation; failure to retain for 10 years is a per-se CRA Art. 13(9) violation.

12. **Affected Stakeholders:** CTO, Lead Dev, Procurement (third-party component selection), Customers (downstream SBOM consumers), ENISA

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-06.3-001 — Data Processing Agreement

1. **Description:** Bind processors to security obligations via a Data Processing Agreement (DPA) that defines the subject matter, duration, nature, and purpose of processing, the type of personal data, the categories of data subjects, and the processor's obligations. For TinyTask, the DPA template is a single document with security clauses aligned to GDPR Art. 28(3) and CRA Annex I where applicable; it is signed with every contracted processor. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/D-06.3.json`) treats the DPA as the contractual enforcement of OBL-D-06.1-001 processor validation: validation establishes fitness, the DPA establishes enforceable obligations. GDPR-C12 (Art. 28(3)) is the sole authority with NI=3.000. At MICRO scale, the DPA is a template-based contract signed at procurement time; the template is reviewed annually by Legal + DPO. The obligation is ONE_TIME per processor (at signature) + CONTINUOUS (template refresh).

2. **Scope:** All contracted processors with access to customer PII: managed hosting provider (standard DPA accepted), managed identity provider (standard DPA + data-processing addendum), payment processor (standard DPA), any future sub-processor. DPA template covers GDPR Art. 28(3)(a)-(h) mandatory contents.

3. **Out of Scope:** Internal-only vendors without PII access (no DPA needed); free-tier SaaS tools (no contractual relationship); employee-vetted vendors (no DPA needed — handled by employment contract).

4. **Source Article:** GDPR Art. 28(3); GDPR-C12

5. **NIST CSF Anchors:** GV.SC-03 (Contracts with suppliers), PR.PS-01 (Configuration change control), PR.DS-01 (Data-at-rest)

6. **Verification Criteria:**

   - DPA template review (annual): Legal + DPO confirm GDPR Art. 28(3) compliance; template version incremented and filed in Doc 09 family.

   - DPA signature audit (quarterly): every contracted processor has a signed DPA on file; verified by Doc 09 supplier register.

   - Sub-processor notification workflow: every DPA requires the processor to notify TinyTask of new sub-processors; verified by annual supplier review.

7. **Verification Method:** INSPECT (DPA template review minutes + signature audit) + DEMONSTRATE (live DPA signature walk-through)

8. **Owner:** CTO + Lead Dev + Procurement

9. **Status:** TODO

10. **Dependencies:** OBL-D-06.1-001, OBL-D-06.2-001, SO-D-06.3-001, CR-D-06.3-001

11. **Risk if not met:** H — Failure to have a DPA in place is a per-se GDPR Art. 28(3) violation and shifts liability to TinyTask as controller.

12. **Affected Stakeholders:** Customers (downstream protection), CTO, Procurement, DPO, Compliance Lead, Legal

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment



**D-06 Verification Cross-Walk (for human reviewer):**


| OBL ID | Verification Criteria Count | Method Mix | Primary NIST Anchor | Cadence |
|--------|----------------------------:|------------|---------------------|---------|
| OBL-D-06.1-001 | 3 | INSPECT + DEMONSTRATE | GV.SC-03 | Per-contract + annual |
| OBL-D-06.2-001 | 3 | TEST + INSPECT + DEMONSTRATE | GV.SC-03 | Per-release + quarterly |
| OBL-D-06.3-001 | 3 | INSPECT + DEMONSTRATE | GV.SC-03 | Annual + per-contract |

**D-06 Owner-Responsibility Decomposition:**


| Role | Primary Responsibility in this Sub-Domain | Backup / Approver |
|------|-------------------------------------------|-------------------|
| CTO | SBOM strategy; supplier attestation register | Procurement |
| Lead Dev | SBOM generation in CI; DPA technical annexes | CTO |
| Procurement | Supplier due-diligence; DPA negotiation; attestation refresh | Legal |

---


### 5.7 D-07 — Secure Development (4 cards)


D-07 covers secure-by-design — the meta-control that all other controls depend on. D-07.1 is the sole obligation in this sub-domain and binds GDPR Art. 25, CRA Annex I §1, and CRA Art. 13 jointly. T-M-002 documents the GDPR NI=2 vs CRA NI=3 intensity gap — the CRA higher intensity wins operationally (the LIGHTWEIGHT implementation cannot tolerate an unhardened design).


### OBL-D-07.1-001 — Secure-by-Design (T-M-002)

1. **Description:** Integrate data protection and security into the design from the outset, with secure-by-default configurations. For TinyTask, this obligation is met through the application of NIST SSDF (Secure Software Development Framework) practices and OWASP SAMM Level 2+ maturity across the development lifecycle: threat modelling at design time, secure-coding standards enforced in CI, dependency scanning on every build, and security review as a PR merge gate. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Dev/D-07.1/D-07.1.json`) treats secure-by-design as the meta-control that all other controls depend on: without it, the system accumulates vulnerabilities faster than D-02.1 can remediate. GDPR-C09 (Art. 25 — data protection by design and by default), CRA-C02 (Annex I §1 — secure by default), and CRA-C22 (Art. 13 — secure development obligations) jointly drive the obligation with NI=2.667. Tension T-M-002 (GDPR NI=2 vs CRA NI=3) is structural and always active; the CRA higher intensity wins operationally. At MICRO scale, secure-by-design is realised through CI gates and PR review discipline rather than a dedicated security team. The obligation is ONE_TIME in design but operates CONTINUOUSLY through the CI gates. The LIGHTWEIGHT implementation tier is justified by the absence of a dedicated security engineer; the role is held by the CTO + Lead Dev.

2. **Scope:** All new feature design (threat model required before merge); all production code (CI gates: SAST, dependency scan, secret scan); all infrastructure-as-code (Terraform plan reviewed for security before apply); all PRs (security review required for changes touching authentication, authorisation, encryption, or PII handling).

3. **Out of Scope:** Formal SSDL certification (out of MICRO scope); dedicated security engineering team (over-scope); red-team engagements with external vendors (out of MICRO scope — internal review is sufficient); formal threat-model documentation for every change (lightweight threat-model template is sufficient at MICRO).

4. **Source Article:** GDPR Art. 25 (data protection by design and by default); CRA Annex I §1 (secure by default); CRA Art. 13 (secure development); GDPR-C09, CRA-C02, CRA-C22

5. **NIST CSF Anchors:** PR.PS-01 (Baseline configuration), PR.PS-06 (System development life cycle), PR.PS-02 (Vulnerability management plan), ID.RA-01 (Asset vulnerabilities)

6. **Verification Criteria:**

   - CI security gates: SAST (Semgrep or equivalent), dependency scan (automated vulnerability scanner + managed dependency audit), secret scan (gitleaks) all required-to-pass on every PR.

   - PR review checklist: every PR touching auth/authz/encryption/PII requires CTO + Lead Dev review; verified by GitHub branch protection rules.

   - Annual secure-development maturity self-assessment: OWASP SAMM Level 2+ across all practices; gaps documented in Doc 09 family.

7. **Verification Method:** TEST (CI gates pass) + INSPECT (SAMM self-assessment + PR review sample) + DEMONSTRATE (live threat-model walkthrough for a new feature)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** All D-02 obligations, all D-03 obligations, OBL-D-08.2-001 (role training), PO-D-07.1-001, SO-D-07.1-001, CR-D-07.1-001, T-M-002

11. **Risk if not met:** H — Failure to apply secure-by-design means every release ships with preventable vulnerabilities; the CI gates are the only structural mitigation at MICRO scale.

12. **Affected Stakeholders:** CTO, Lead Dev, DPO (privacy-by-design oversight), All engineers (CI gate subjects)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment



**D-07 Verification Cross-Walk (for human reviewer):**


| OBL ID | Verification Criteria Count | Method Mix | Primary NIST Anchor | Cadence |
|--------|----------------------------:|------------|---------------------|---------|
| OBL-D-07.1-001 | 3 | TEST + INSPECT + DEMONSTRATE | PR.PS-06 | Per-PR + annual SAMM |
**D-07 Owner-Responsibility Decomposition:**


| Role | Primary Responsibility in this Sub-Domain | Backup / Approver |
|------|-------------------------------------------|-------------------|
| CTO | Threat-model review; secure-coding policy; PR-merge gate | Lead Dev |
| Lead Dev | CI gates; SAST/DAST tuning; dependency scanning | CTO |

---



### OBL-D-07.2-001 — Secure Coding Practices

1. **Description:** Apply secure coding standards to product source code and limit the attack surface through code review and static analysis. For TinyTask, this obligation is operationalised through: documented secure-coding standards (input validation, output encoding, parameterised queries, least-privilege crypto APIs) enforced in PR review; static analysis (SAST) on every PR touching `src/` or `lib/`; mandatory two-person review for any change touching authentication, authorisation, encryption, or PII handling; and an annual secure-coding training burst for engineers. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Dev/D-07.2/D-07.2.json`) treats secure coding as the per-PR discipline that operationalises the meta-control OBL-D-07.1-001: without it, secure-by-design becomes an aspirational policy rather than a build-time guarantee. CRA-C02 (Annex I Part I §2(c) — attack surface limitation) drives the obligation with NI=3.000 (CRA sole authority). The shared-clause annotation reflects that CRA-C02 is currently also mapped to D-07.1 (secure-by-design); dedicated clause allocation is deferred to a follow-on contract (F-07). The obligation is CONTINUOUS — every PR must meet the secure-coding bar before merge. The LIGHTWEIGHT implementation tier is justified by the absence of a dedicated security engineer; the role is held by the CTO + Lead Dev.

2. **Scope:** All production source code in the `tinytask` monorepo (`src/`, `lib/`, `migrations/`, infrastructure-as-code in `terraform/`). Every PR touching these paths requires: SAST pass (Semgrep or equivalent), dependency scan pass, two-person review from CTO + Lead Dev for security-relevant changes, no new critical/high findings.

3. **Out of Scope:** Formal SSDL certification (out of MICRO scope — internal secure-coding standards suffice); red-team static-analysis engagements with external vendors (out of MICRO scope — open-source SAST is sufficient); per-developer secure-coding certifications (out of MICRO scope — annual training burst + PR review is sufficient).

4. **Source Article:** CRA Annex I Part I §2(c) (attack surface limitation); CRA-C02 (shared with D-07.1 — dedicated clause TBD in follow-on contract per F-07)

5. **NIST CSF Anchors:** PR.PS-01 (Baseline configuration), PR.PS-02 (Vulnerability management plan — co-annexed), PR.PS-06 (System development life cycle)

6. **Verification Criteria:**

   - PR review sample (quarterly): 10% of merged PRs reviewed against secure-coding checklist (input validation, output encoding, parameterised queries, secrets handling); all findings documented and remediated.

   - SAST pass rate (monthly): 100% of PRs scanned; 0 critical, ≤2 high findings open for >30 days.

   - Annual secure-coding training: all engineers complete 1-hour module; tracked via signed acknowledgement.

7. **Verification Method:** INSPECT (quarterly PR review sample + SAST dashboard screenshot) + DEMONSTRATE (live PR walkthrough showing secure-coding checklist application) + TEST (SAST run on sample PR)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-07.1-001 (secure-by-design policy anchor), CR-D-07.2-001 (TBD per F-07), all D-02 obligations (downstream secure-coding upstream of vuln identification)

11. **Risk if not met:** H — Failure to apply secure coding standards means preventable vulnerabilities reach production at the rate PRs are merged; the CI gates are the only structural mitigation at MICRO scale.

12. **Affected Stakeholders:** CTO, Lead Dev, All engineers (PR subjects), Customers (downstream vulnerability exposure)

13. **Maturity Score:** 1/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** documented third-party security attestation (managed hosting, managed object storage, managed key custody, managed audit-trail, managed backup) + documented control standard (managed hosting EU region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment (CRA reporting delegated to ENISA via manufacturer obligations; CNPD is the lead SA for joint GDPR+personal-data breaches)




### OBL-D-07.3-001 — CI/CD Pipeline Security

1. **Description:** Implement security gates in the CI/CD pipeline and ensure build-time artefact integrity, including an SBOM (Software Bill of Materials) gate. For TinyTask, this obligation is operationalised through: GitHub Actions workflow with required-to-pass SAST + dependency scan + secret scan gates on every PR; SBOM (SPDX or CycloneDX) generated on every release and stored alongside release artefacts; signed release artefacts (Sigstore / cosign) for integrity; branch protection rules preventing direct pushes to `main`. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Dev/D-07.3/D-07.3.json`) treats CI/CD security as the build-time realisation of secure coding (D-07.2): it converts per-PR discipline into an enforced pipeline property. CRA-C22 (Annex I Part I §2(b) — secure by default including build-time) drives the obligation with NI=3.000 (CRA sole authority). Shared-clause annotation reflects that CRA-C22 is currently also mapped to D-07.1 (secure-by-design); dedicated clause allocation is deferred to a follow-on contract (F-07). The obligation is CONTINUOUS — every PR and every release must pass the gates. The LIGHTWEIGHT implementation tier is justified by GitHub Actions managed runner being sufficient for MICRO scale.

2. **Scope:** All GitHub Actions workflows triggered by PR / push / release events in the `tinytask` monorepo. Every PR must pass: SAST, dependency scan, secret scan. Every release produces: signed artefact, machine-readable SBOM, audit log of build provenance.

3. **Out of Scope:** Self-hosted hardened runners (out of MICRO scope — GitHub-managed runners are sufficient for the current release cadence); isolated build environments (out of MICRO scope — managed isolation is sufficient); formal SLSA Level 3 attestation (out of MICRO scope — Level 1-2 is sufficient).

4. **Source Article:** CRA Annex I Part I §2(b) (secure by default; build-time gates); CRA-C22 (shared with D-07.1 — dedicated clause TBD in follow-on contract per F-07)

5. **NIST CSF Anchors:** PR.PS-02 (Vulnerability management plan), ID.SC-04 (Suppliers are prioritized by criticality), PR.PS-06 (System development life cycle)

6. **Verification Criteria:**

   - CI gate pass rate (monthly): 100% of merged PRs had all required gates passing at merge time; verified by GitHub branch protection audit log.

   - SBOM on every release (per release): machine-readable SBOM attached as release artefact; verified by GitHub release asset list.

   - Signed artefact on every release: cosign signature present; verified by `cosign verify` against release tag.

7. **Verification Method:** TEST (CI gate pass + SBOM + signature on every release) + INSPECT (monthly CI dashboard + release audit) + DEMONSTRATE (live walkthrough of a sample PR and a sample release)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-07.1-001 (secure-by-design policy), OBL-D-07.2-001 (secure-coding PR practice), OBL-D-06.2-001 (SBOM contract), CR-D-07.3-001 (TBD per F-07)

11. **Risk if not met:** H — Failure to gate CI/CD means build-time vulnerabilities (typosquatting dependencies, leaked secrets, untested code) reach production without structural detection.

12. **Affected Stakeholders:** CTO, Lead Dev, All engineers (PR subjects), Customers (downstream vulnerability exposure), ENISA (CRA SBOM reporting)

13. **Maturity Score:** 1/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only (SBOM retention per CRA Annex I §2; reportable to ENISA only on exploited vulnerability per CRA Art. 14)

16. **External Auditor (Case_01):** documented third-party security attestation + documented control standard (managed hosting EU region)

17. **Supervisory Body (Case_01):** CNPD (GDPR) — co-annexed with ENISA for CRA SBOM delivery on demand




### OBL-D-07.4-001 — Change Management

1. **Description:** Implement documented change management procedures for product releases and ensure a secure update delivery channel for end-customers. For TinyTask, this obligation is operationalised through: a documented Change Advisory Board (CAB) approval workflow (CTO + Lead Dev sign-off) for every production release; release evidence pack (signed artefact, SBOM, release notes, security review checklist, threat-model diff for high-risk changes); automated update delivery via the standard SaaS deployment channel (no manual patching by end-customers, justified by SaaS deployment model). The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Dev/D-07.4/D-07.4.json`) treats change management as the governance layer for releases: without it, even a well-coded, well-gated build can be deployed without stakeholder sign-off. CRA-C22 (Annex I Part I §2(b) — secure by default; update delivery) drives the obligation with NI=3.000 (CRA sole authority). Shared-clause annotation reflects that CRA-C22 is currently also mapped to D-07.1; dedicated clause allocation is deferred to a follow-on contract (F-07). The obligation is CONTINUOUS — every production release must clear the CAB and produce the release evidence pack. The LIGHTWEIGHT implementation tier is justified by a 2-person CAB (CTO + Lead Dev) being sufficient at MICRO scale.

2. **Scope:** Every production release of the TinyTask SaaS platform (frontend, backend, infrastructure-as-code). Scope includes: CAB approval workflow, release evidence pack generation, secure update delivery channel, rollback procedure documentation.

3. **Out of Scope:** Multi-tier CAB with separate change manager (out of MICRO scope — CTO + Lead Dev approval is sufficient); formal ITIL change management certification (out of MICRO scope); customer-side update deployment (out of scope — SaaS deployment is centrally managed).

4. **Source Article:** CRA Annex I Part I §2(b) (secure by default; update delivery); CRA Art. 13(8) (5-year support period); CRA-C22 (shared with D-07.1 — dedicated clause TBD in follow-on contract per F-07)

5. **NIST CSF Anchors:** PR.PS-02 (Vulnerability management plan), PR.IP-12 (legacy CSF 1.1 — management of changes), ID.SC-04 (Suppliers prioritized by criticality)

6. **Verification Criteria:**

   - CAB approval on every release: CTO + Lead Dev sign-off recorded in release ticket; verified by sample of last 10 releases per quarter.

   - Release evidence pack completeness: every release includes signed artefact, SBOM, release notes, security review checklist; verified by release asset audit.

   - Rollback procedure documented: every release ticket links to a tested rollback runbook; verified by runbook existence + last-tested date.

7. **Verification Method:** INSPECT (quarterly release audit sample + runbook freshness check) + DEMONSTRATE (live CAB walkthrough for a sample release) + TEST (rollback drill on staging for a sample release)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-07.1-001 (secure-by-design policy), OBL-D-07.3-001 (CI/CD security gates provide signed artefacts), OBL-D-02.2-001 (security updates), CR-D-07.4-001 (TBD per F-07)

11. **Risk if not met:** M-H — Failure to enforce change management means undocumented or unreviewed changes reach production; the LIGHTWEIGHT CAB is the single structural control.

12. **Affected Stakeholders:** CTO, Lead Dev, Compliance Lead (audit access), Customers (downstream assurance), ENISA (CRA 5-year support documentation)

13. **Maturity Score:** 1/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only (CRA Art. 13(8) is a product-level obligation; no periodic external reporting required for change-management process itself)

16. **External Auditor (Case_01):** documented third-party security attestation + documented control standard (managed hosting EU region)

17. **Supervisory Body (Case_01):** CNPD (GDPR) — ENISA receives CRA product conformity documentation on demand, not per-change




**D-07 Verification Cross-Walk (updated post Sprint 6+ — 4 OBLs):**


| OBL ID | Verification Criteria Count | Method Mix | Primary NIST Anchor | Cadence |
|--------|----------------------------:|------------|---------------------|---------|
| OBL-D-07.1-001 | 3 | TEST + INSPECT + DEMONSTRATE | PR.PS-06 | Per-PR + annual SAMM |
| OBL-D-07.2-001 | 3 | INSPECT + DEMONSTRATE + TEST | PR.PS-01 | Per-PR + quarterly sample |
| OBL-D-07.3-001 | 3 | TEST + INSPECT + DEMONSTRATE | PR.PS-02 | Per-PR + per-release |
| OBL-D-07.4-001 | 3 | INSPECT + DEMONSTRATE + TEST | PR.IP-12 (CSF 1.1; PR.PS-02 CSF 2.0) | Per-release + quarterly audit |

**D-07 Owner-Responsibility Decomposition (updated post Sprint 6+ — 4 OBLs):**


| Role | Primary Responsibility in this Sub-Domain | Backup / Approver |
|------|-------------------------------------------|-------------------|
| CTO | Threat-model review; secure-coding policy; PR-merge gate; CAB approval | Lead Dev |
| Lead Dev | CI gates; SAST/DAST tuning; dependency scanning; CAB approval; rollback runbooks | CTO |

---



### 5.8 D-08 — Human Factors (2 cards)


D-08 covers human factors — security awareness (D-08.1) and role-specific training (D-08.2). Both are GDPR-led and operate as documentation-based training at the LIGHTWEIGHT tier. The implementation is annual email broadcast + acknowledgement (D-08.1) and per-role training documentation (D-08.2). The MINIMAL tier of D-08.1 reflects supplier-attestation rather than a dedicated training programme.


### OBL-D-08.1-001 — Staff Security Awareness Training

1. **Description:** Train staff involved in processing operations on security awareness. For TinyTask, this obligation is met through an annual security awareness email broadcast covering phishing recognition, password hygiene, social engineering, incident reporting, and GDPR/CRA basics. Completion is tracked via a signed acknowledgement in the employee file. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.1/D-08.1.json`) treats security awareness as the human-layer complement to all technical controls: even the best D-01 encryption cannot prevent a phishing-driven credential leak. GDPR-C27 (Art. 39(1)(b) — DPO tasks, including awareness) and GDPR-C28 (Art. 47 — security training in codes of practice) jointly drive the GDPR coverage. The MINIMAL implementation tier reflects vendor-supplied documentation on file rather than a dedicated training programme. At MICRO scale, awareness training is an annual email + acknowledgement. The obligation is PERIODIC — annual cadence.

2. **Scope:** All staff with access to TinyTask systems or customer PII: CTO, Lead Dev, DPO, Customer Success (if PII access), any contractor with system access. Annual awareness email with acknowledgement; phishing drill quarterly.

3. **Out of Scope:** Role-specific deep training (covered by OBL-D-08.2-001); external security certifications (out of scope — vendor documentation on file is sufficient); on-site training events (out of scope — remote/email is sufficient at MICRO).

4. **Source Article:** GDPR Art. 39(1)(b); GDPR-C27

5. **NIST CSF Anchors:** PR.AT-01 (All users are informed and trained), PR.AT-02 (Privileged users understand their roles), PR.AA-01 (Identity and credential management)

6. **Verification Criteria:**

   - Annual awareness email broadcast: every staff member receives and signs acknowledgement; tracked in HR system.

   - Quarterly phishing drill: synthetic phishing email sent to all staff; click-through rate reported to DPO and CTO; drill vendor attestation on file.

   - Annual training refresh: training material updated to reflect latest threat landscape (phishing trends, new regulations).

7. **Verification Method:** INSPECT (HR acknowledgement records + drill reports) + DEMONSTRATE (live drill dispatch)

8. **Owner:** CTO + HR + DPO

9. **Status:** TODO

10. **Dependencies:** OBL-D-08.2-001, OBL-D-09.1-001, SO-D-08.1-001, CR-D-08.1-001

11. **Risk if not met:** M — Failure to train staff creates human-layer risk that compounds every technical control gap; a single phishing-induced credential leak can cascade through all D-03 controls.

12. **Affected Stakeholders:** CTO (technical staff), DPO (privacy staff), HR (training owner), All staff (trainees)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** MEDIUM

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-08.2-001 — Role-Specific Security Training

1. **Description:** Raise awareness and train staff with role-specific security obligations. For TinyTask, this obligation is met through role-specific training documentation: CTO/Lead Dev receive secure-coding + cloud-security training references (vendor docs + OWASP), DPO receives privacy-law training, HR/People Ops receive personnel-data handling training. Completion is tracked per role in the HR system. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.2/D-08.2.json`) treats role-specific training as the depth-extension of OBL-D-08.1 awareness: awareness training covers everyone equally; role-specific training goes deeper into the obligations of each role. GDPR-C28 (Art. 47) drives the GDPR coverage with NI=3.000. At MICRO scale, role-specific training is documentation-based (vendor docs on file) rather than course-based. The obligation is PERIODIC — annual cadence with refresh on role change.

2. **Scope:** CTO + Lead Dev: secure-coding training (OWASP Top 10 awareness), cloud-security training (managed hosting Well-Architected security pillar), CRA obligations overview. DPO: GDPR deep-dive, CNPD enforcement trends, DSAR handling. HR: personnel-data handling, RGPD employment-data exemptions. Customer Success: PII handling, support-side access controls.

3. **Out of Scope:** External certification programmes (CISSP, CIPP/E) — out of scope at MICRO (over-scope for budget); formal classroom training (out of scope — vendor docs are sufficient); role-specific training for roles that don't exist at MICRO (out of scope).

4. **Source Article:** GDPR Art. 47; GDPR-C28

5. **NIST CSF Anchors:** PR.AT-01 (All users informed and trained), PR.AT-02 (Privileged users understand roles)

6. **Verification Criteria:**

   - Role-specific training register (Doc 09 family): every role with PII or system access has documented training materials on file.

   - Annual role-specific refresh: materials updated; new joiners onboarded with role-specific training within 30 days.

   - Training-completion tracking: every role-holder signs acknowledgement of their role-specific materials; tracked in HR system.

7. **Verification Method:** INSPECT (training register + completion tracking) + DEMONSTRATE (new-joiner onboarding walkthrough)

8. **Owner:** CTO + HR + DPO

9. **Status:** TODO

10. **Dependencies:** OBL-D-08.1-001, OBL-D-09.1-001, SO-D-08.2-001, CR-D-08.2-001

11. **Risk if not met:** M — Failure to provide role-specific training means high-impact roles (CTO, Lead Dev, DPO) lack the depth to make informed decisions; the LIGHTWEIGHT implementation tier cannot absorb that gap.

12. **Affected Stakeholders:** CTO, Lead Dev, DPO, HR, All staff (role-specific scope)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** MEDIUM

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment



**D-08 Verification Cross-Walk (for human reviewer):**


| OBL ID | Verification Criteria Count | Method Mix | Primary NIST Anchor | Cadence |
|--------|----------------------------:|------------|---------------------|---------|
| OBL-D-08.1-001 | 3 | INSPECT + DEMONSTRATE | PR.AT-01 | Annual + quarterly drill |
| OBL-D-08.2-001 | 3 | INSPECT + DEMONSTRATE | PR.AT-02 | Annual + per-joiner |

**D-08 Owner-Responsibility Decomposition:**


| Role | Primary Responsibility in this Sub-Domain | Backup / Approver |
|------|-------------------------------------------|-------------------|
| CTO | Technical training material; secure-coding refresh | Lead Dev |
| HR | Training register; completion tracking; joiner/leaver process | DPO |
| DPO | Privacy training material; role-specific deep dives | HR |

---


### 5.9 D-09 — Governance & Documentation (3 cards)


D-09 covers governance: ISMS documentation (D-09.1), unified risk assessment (D-09.2), records of processing (D-09.4). All three are STRUCTURAL and CONTINUOUS — the governance substrate that every other obligation depends on for evidence. D-09.1 carries Rich NI = 2.500 (DR-002 AVG, F-10 reconciliation). T-M-001 documents the frequency alignment of D-09.2 (both ONE_TIME but always-active because both triggers are permanently satisfied).


### OBL-D-09.1-001 — ISMS Documentation

1. **Description:** Implement appropriate technical and organisational measures; document policies; maintain technical documentation for 10 years. For TinyTask, this obligation is met through the Information Security Management System (ISMS) documentation set: security policy, access-control policy, incident-response policy, data-protection policy, business-continuity policy, supplier-security policy — all aligned to ISO 27001 Annex A controls (proportionally scoped to MICRO tier). The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance/D-09.1/D-09.1.json`) treats ISMS documentation as the structural backbone of every other governance obligation: without it, there is no auditable evidence of 'appropriate measures'. GDPR-C08 (Art. 32 — appropriate measures), GDPR-C25 (Art. 5(2) — accountability principle), GDPR-C26 (Art. 24 — controller accountability), and CRA-C24 (Art. 13 — technical documentation) jointly drive the obligation. Rich NI = 2.500 (DR-002 AVG of GDPR-C08=2, GDPR-C25=3, GDPR-C26=2, CRA-C24=3), resolved as authoritative in Sprint 4 §4.1. At MICRO scale, ISMS documentation is a set of Markdown policies in `docs/policies/` reviewed annually by DPO + Compliance Lead + Legal. The obligation is mixed CONTINUOUS (policies must always be current) + ONE_TIME (initial drafting).

2. **Scope:** All security policies (security policy, access-control, incident-response, data-protection, business-continuity, supplier-security); all technical documentation (architecture diagrams, data-flow diagrams, DPIA records, supplier-attestation register); all meeting minutes (security steering committee, if any); all audit reports.

3. **Out of Scope:** ISO 27001 certification (out of MICRO scope — proportional documentation is sufficient); managed hosting provider attestation leveraged (out of MICRO scope); dedicated GRC tool (out of MICRO scope — Markdown + managed object storage is sufficient).

4. **Source Article:** GDPR Art. 32 + Art. 5(2) + Art. 24; CRA Art. 13 (technical documentation); GDPR-C08, GDPR-C25, GDPR-C26, CRA-C24

5. **NIST CSF Anchors:** GV.OC-01 (Organizational risk strategy), GV.OC-03 (Roles and responsibilities), PR.PS-01 (Baseline configuration), PR.PS-02 (Vulnerability management plan)

6. **Verification Criteria:**

   - ISMS documentation audit (annual): every policy enumerated, every policy reviewed, every review dated and signed off by DPO + Compliance Lead + Legal.

   - Technical documentation completeness check: architecture diagram, data-flow diagram, DPIA record, supplier-attestation register all current and aligned with the production deployment.

   - 10-year retention verification: managed object storage lifecycle policy on the policies bucket confirms 10-year retention; verified by managed configuration rule.

7. **Verification Method:** INSPECT (annual audit + retention verification) + DEMONSTRATE (live policy walkthrough with DPO) + ANALYZE (gap analysis against ISO 27001 Annex A scope)

8. **Owner:** CTO + DPO + Compliance Lead + Legal

9. **Status:** TODO

10. **Dependencies:** All other OBL obligations (documentation is the backbone), OBL-D-09.2-001, OBL-D-09.4-001, PO-D-09.1-001, SO-D-09.1-001, CR-D-09.1-001

11. **Risk if not met:** H — Failure to maintain documentation undermines GDPR Art. 5(2) accountability and CRA Art. 13 conformity — every other control's evidence depends on the documentation set.

12. **Affected Stakeholders:** Customers (downstream evidence), CTO, DPO (policy owner), Compliance Lead, Legal (review)

13. **Maturity Score:** 1/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD + ENISA (periodic accountability + CRA conformity)

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment; ENISA — CRA conformity assessment body (single market); CNCS (Centro Nacional de Cibersegurança) — PT CSIRT for early-warning + incident coordination


### OBL-D-09.2-001 — Unified Risk Assessment (T-M-001)

1. **Description:** Conduct a Data Protection Impact Assessment (DPIA) prior to high-risk processing, and a cybersecurity risk assessment before market placement of the product. For TinyTask, this obligation is met through a unified risk-assessment template that produces both GDPR Art. 35 DPIA and CRA Art. 13(5) cybersecurity risk assessment outputs from a single assessment workflow, avoiding duplicated effort. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance/D-09.2/D-09.2.json`) treats the unified assessment as the structural expression of T-M-001 (frequency alignment): GDPR DPIA is required prior to processing, CRA risk assessment is required prior to market placement; both triggers are permanently satisfied by TinyTask's business model (always processing, always on market). GDPR-C20 (Art. 35 — DPIA), GDPR-C24 (Art. 36 — prior consultation), and CRA-C23 (Art. 13(5)) jointly drive the obligation with NI=2.667. At MICRO scale, the unified assessment is a single Markdown template with two output sections; the assessment is reviewed annually or upon any material change to processing. The obligation is mixed PERIODIC + ONE_TIME.

2. **Scope:** All processing activities (full DPIA scope for the SaaS platform); all product features (CRA risk assessment scope for any new feature touching security, encryption, or PII handling); all third-party integrations (DPIA + CRA risk coverage). Unified template output stored in Doc 09 family.

3. **Out of Scope:** Full ISO 27005 risk-assessment methodology (over-engineered at MICRO); GRC-tool-driven assessment (out of MICRO scope); annual third-party risk-assessment audit (out of MICRO scope — internal review is sufficient).

4. **Source Article:** GDPR Art. 35 (DPIA); CRA Art. 13(5) (cybersecurity risk assessment); GDPR-C20, GDPR-C24, CRA-C23

5. **NIST CSF Anchors:** GV.OC-01 (Organizational risk strategy), ID.RA-04 (Potential business impacts and likelihoods of threats are identified), PR.PS-01 (Baseline configuration)

6. **Verification Criteria:**

   - Unified risk-assessment template review (annual): DPO + Compliance Lead + Legal confirm template alignment with GDPR Art. 35 + CRA Art. 13(5); template version incremented.

   - Latest assessment output: covers all current processing activities + product features; stored in Doc 09 family with review date.

   - Material-change trigger: any new feature, third-party integration, or processing change re-runs the assessment within 30 days; tracked in Doc 09 family.

7. **Verification Method:** INSPECT (annual template review + latest assessment) + DEMONSTRATE (material-change trigger walkthrough)

8. **Owner:** CTO + DPO + Compliance Lead + Legal

9. **Status:** TODO

10. **Dependencies:** OBL-D-09.1-001, OBL-D-09.4-001, OBL-D-07.1-001, PO-D-09.2-001, SO-D-09.2-001, CR-D-09.2-001, T-M-001

11. **Risk if not met:** H — Failure to conduct DPIA before high-risk processing creates direct GDPR Art. 35 violation; failure to conduct CRA risk assessment before market creates direct CRA Art. 13(5) violation.

12. **Affected Stakeholders:** Customers (data subjects impacted), CTO, DPO (DPIA owner), Compliance Lead, Legal, ENISA

13. **Maturity Score:** 1/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD + ENISA (periodic accountability + CRA conformity)

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment; ENISA — CRA conformity assessment body (single market); CNCS (Centro Nacional de Cibersegurança) — PT CSIRT for early-warning + incident coordination


### OBL-D-09.4-001 — Records of Processing

1. **Description:** Maintain records of processing activities (RoPA) per GDPR Art. 30 and breach documentation per GDPR Art. 33(5). For TinyTask, the RoPA is a single Markdown document covering all processing activities (controller activities for customer-PII, processor activities for client-content); breach documentation is the breach log (separate from the RoPA) maintained for 10 years. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance/D-09.4/D-09.4.json`) treats RoPA as the operational expression of accountability: every processing activity is named, scoped, and documented; the breach log captures every incident regardless of notifiability. GDPR-C13 (Art. 30 — RoPA) and GDPR-C22 (Art. 33(5) — breach documentation) jointly drive the GDPR coverage with NI=3.000. At MICRO scale, RoPA + breach log are Markdown documents in the managed object storage governance bucket with 10-year retention and managed object storage Object Lock (compliance mode). The obligation is mixed CONTINUOUS (RoPA must be kept current) + TRIGGERED (breach log entries per incident).

2. **Scope:** All processing activities (controller + processor); all data categories (PII, special categories if any, non-PII metadata); all data-subject categories (customers, end-users of customer tenants, prospects); all recipients (managed hosting provider, managed identity provider, payment processor, customer controllers); all retention periods; all security measures. Breach log: every incident with timestamp, classification, notification status, resolution.

3. **Out of Scope:** Granular per-data-subject consent records (handled separately in customer onboarding flow); granular per-cookie consent (out of SaaS scope — no cookies beyond essential); third-party RoPA for suppliers (suppliers maintain their own RoPA).

4. **Source Article:** GDPR Art. 30 (RoPA); GDPR Art. 33(5) (breach documentation); GDPR-C13, GDPR-C22

5. **NIST CSF Anchors:** GV.OC-01 (Organizational risk strategy), PR.PS-01 (Baseline configuration), ID.AM-08 (Asset inventory)

6. **Verification Criteria:**

   - RoPA completeness check (annual): every processing activity enumerated; categories, recipients, retention, security measures all present; signed off by DPO.

   - Breach log review (quarterly): every incident since last review documented; classification correct; notification status correct; retention policy applied.

   - 10-year retention verification: managed object storage Object Lock compliance mode confirmed on governance bucket; verified by managed configuration rule.

7. **Verification Method:** INSPECT (annual RoPA review + quarterly breach log review) + DEMONSTRATE (live RoPA completeness walkthrough)

8. **Owner:** CTO + DPO + Compliance Lead + Legal

9. **Status:** TODO

10. **Dependencies:** OBL-D-09.1-001, OBL-D-09.2-001, OBL-D-04.3-001 (breach cross-ref), PO-D-09.4-001, SO-D-09.4-001, CR-D-09.4-001

11. **Risk if not met:** H — Failure to maintain RoPA is a per-se GDPR Art. 30 violation; failure to document breaches undermines Art. 33(5) compliance.

12. **Affected Stakeholders:** Customers (data subjects), CTO, DPO (RoPA owner), Compliance Lead, Legal, CNPD (auditor)

13. **Maturity Score:** 1/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** CNPD + ENISA (periodic accountability + CRA conformity)

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment; ENISA — CRA conformity assessment body (single market); CNCS (Centro Nacional de Cibersegurança) — PT CSIRT for early-warning + incident coordination



**D-09 Verification Cross-Walk (for human reviewer):**


| OBL ID | Verification Criteria Count | Method Mix | Primary NIST Anchor | Cadence |
|--------|----------------------------:|------------|---------------------|---------|
| OBL-D-09.1-001 | 3 | INSPECT + DEMONSTRATE + ANALYZE | GV.OC-01 | Annual + 10y retention |
| OBL-D-09.2-001 | 3 | INSPECT + DEMONSTRATE | GV.OC-01 | Annual + per-change |
| OBL-D-09.4-001 | 3 | INSPECT + DEMONSTRATE | GV.OC-01 | Annual + quarterly breach log |

**D-09 Owner-Responsibility Decomposition:**


| Role | Primary Responsibility in this Sub-Domain | Backup / Approver |
|------|-------------------------------------------|-------------------|
| CTO | Technical documentation; architecture diagrams; DPIA technical content | Lead Dev |
| DPO | Policy ownership; DPIA sign-off; CNPD interface | Legal |
| Compliance Lead | ISMS audit; supplier register review; RoPA maintenance | DPO |
| Legal | DPA review; regulatory text interpretation; CNPD enforcement tracking | Compliance Lead |

---


### 5.10 D-10 — Monitoring & Audit (3 cards)


D-10 covers monitoring and audit: continuous security monitoring (D-10.1, CRA sole authority), security logging (D-10.2, CRA sole authority), and security testing (D-10.3, both GDPR and CRA). The implementation combines managed monitoring alerting + monthly review (D-10.1), managed audit-trail service + tamper-evident managed object storage log bucket (D-10.2), and quarterly compliance review + annual pen test (D-10.3). Monitoring is the detection layer; logging is the observational substrate; testing is the verification layer — together they form the *see-then-prove* triad. An unverified posture is, regulatorily, equivalent to an insecure posture.


### OBL-D-10.1-001 — Continuous Security Monitoring

1. **Description:** Establish continuous security monitoring for the product and supporting systems, and operate the CRA Art. 14 vulnerability-handling workflow. For TinyTask, this obligation is met through: managed monitoring service (logs from SYS-01 → managed monitoring subprocessor) with an alert taxonomy of severity-severity tiers; monthly review of alerts with cross-reference to incident log (OBL-D-04.3-001) and customer-support tickets; documented vulnerability-handling workflow that routes exploited vulnerabilities to ENISA 24h reporting and contained vulnerabilities to the patch-management cadence (OBL-D-02.2-001). The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring/D-10.1/D-10.1.json`) treats continuous monitoring as the detection layer: it converts runtime telemetry into actionable alerts and creates the evidence trail for compliance reporting. CRA-C12 (Annex I Part I §2(l) + Part II §1) drives the obligation with NI=3.000 (CRA sole authority). CRA-C12 was unmapped in Doc 08 §3.6 prior to Sprint 6+ because there was no dedicated OBL; the taxonomy reference (`00_Taxonomy_Reference.md` §3 line 142) already lists CRA-C12 as the D-10.1 driver, so this OBL closes the gap. The obligation is CONTINUOUS — monitoring is always-on; vulnerability-handling is triggered by detected events. The LIGHTWEIGHT implementation tier is justified by managed monitoring + monthly review being sufficient at MICRO scale (no in-house SIEM required).

2. **Scope:** All production infrastructure (managed hosting, managed CI/CD, managed monitoring); the TinyTask SaaS application (frontend + backend + workers); managed identity service; payment processor. Scope includes: alert taxonomy, monthly review cadence, vulnerability-handling workflow, ENISA 24h reporting routing for exploited vulnerabilities (CRA Art. 14).

3. **Out of Scope:** Self-hosted SIEM (out of MICRO scope — managed monitoring is sufficient); ML-driven anomaly detection (out of MICRO scope — alert taxonomy + monthly review is sufficient); dedicated 24/7 SOC (out of MICRO scope — on-call rotation between CTO + Lead Dev + DPO is sufficient).

4. **Source Article:** CRA Annex I Part I §2(l) (vulnerability handling); CRA Annex I Part II §1 (secure-by-default post-market monitoring); CRA Art. 14 (ENISA exploited-vulnerability reporting, 24h); CRA-C12

5. **NIST CSF Anchors:** DE.CM-01 (Networks and environments are monitored), ID.RA-05 (Threats, vulnerabilities, likelihoods, and impacts are used to assess risk and prioritize action), PR.PS-02 (Vulnerability management plan), PR.IP-12 (legacy CSF 1.1 — management of changes; co-annexed for vulnerability response)

6. **Verification Criteria:**

   - Managed monitoring alert taxonomy documented (one-time): taxonomy covers auth failures, IAM policy changes, managed object storage access changes, managed key custody anomalies, application-layer rate-limit breaches; reviewed by CTO + Lead Dev.

   - Monthly monitoring review (every month): alerts reviewed; severity tiers applied; false-positive rate tracked; findings cross-referenced with incident log.

   - Vulnerability-handling workflow documented: CRA Art. 14 routing tested by tabletop exercise at least once per year; ENISA 24h template prepared.

7. **Verification Method:** INSPECT (monthly review minutes + managed monitoring dashboard screenshot + ENISA template) + TEST (tabletop exercise: simulate exploited vulnerability → confirm 24h routing) + DEMONSTRATE (live monthly review walkthrough)

8. **Owner:** CTO + Lead Dev + DPO (on-call rotation)

9. **Status:** TODO

10. **Dependencies:** OBL-D-04.1-001 (incident detection cross-ref), OBL-D-02.2-001 (patch-management downstream), OBL-D-10.2-001 (logging substrate), OBL-D-10.3-001 (testing cross-ref), CR-D-10.1-001 (TBD per F-07)

11. **Risk if not met:** H — Failure to monitor continuously means exploits are detected only via customer complaint or third-party disclosure, breaching the CRA Art. 14 24h reporting window.

12. **Affected Stakeholders:** CTO (monitoring owner), Lead Dev (alert triage), DPO (cross-ref to data subjects), Compliance Lead (CRA reporting), ENISA (recipient of exploited-vulnerability reports)

13. **Maturity Score:** 1/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** ENISA 24h (CRA Art. 14 — exploited vulnerability reporting); internal otherwise

16. **External Auditor (Case_01):** documented third-party security attestation (managed hosting, managed object storage, managed key custody, managed audit-trail, managed backup) + documented control standard (managed hosting EU region); managed monitoring DPA (subprocessor register)

17. **Supervisory Body (Case_01):** ENISA (CRA Art. 14) — co-annexed with CNPD for joint GDPR+personal-data breaches




### OBL-D-10.2-001 — Security Audit Logging

1. **Description:** Log security-relevant events and maintain an audit trail of access to personal data and product functionality. For TinyTask, this obligation is met through managed audit-trail service (control-plane events), application-layer audit logs (data-access events), and a tamper-evident managed object storage log bucket with Object Lock compliance mode and 10-year retention. The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring/D-10.2/D-10.2.json`) treats audit logging as the observational substrate of every other control: without it, there is no forensic capability, no breach-investigation baseline, no compliance evidence. CRA-C14 (Annex I §2(2)) is the sole authority — the audit-logging obligation is CRA-specific (GDPR does not impose a comparable product-level logging obligation). At MICRO scale, audit logging is delegated to managed audit-trail service (managed) plus application-layer custom logging. The obligation is CONTINUOUS — every security-relevant event must be logged, and logs must always be tamper-evident.

2. **Scope:** All managed audit-trail events (control-plane: IAM, key custody, managed object storage, managed NoSQL, managed database); all application audit logs (data-access events: who read what PII, when); all authentication events (managed identity provider login/logout); all administrative actions (admin console, payment processor dashboard). Storage: managed object storage log bucket with Object Lock compliance mode + 10-year retention.

3. **Out of Scope:** Real-time log streaming to a centralised logging platform (out of MICRO scope — log review is monthly); machine-learning anomaly detection on logs (out of MICRO scope — manual review is sufficient); per-event immutable cryptographic proof (over-engineered — Object Lock + signed logs are sufficient).

4. **Source Article:** CRA Annex I §2(2) (audit logging); CRA-C14

5. **NIST CSF Anchors:** PR.PS-04 (Event logging), DE.CM-01 (Network is monitored), PR.DS-01 (Data-at-rest — co-annexed for log integrity)

6. **Verification Criteria:**

   - Managed audit-trail multi-region trail enabled; logs delivered to managed object storage log bucket; verified by managed configuration rule for trail-enablement.

   - Application audit-log completeness: every data-access event is logged; verified by application code review and runtime sampling.

   - Monthly log review: random sampling of access events cross-checked against customer support tickets and incident log; anomalies escalated.

7. **Verification Method:** INSPECT (managed audit-trail + log review minutes) + TEST (synthetic event generation + log capture) + DEMONSTRATE (live log review walkthrough)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** OBL-D-04.3-001 (incident investigation), OBL-D-09.4-001 (RoPA cross-ref), SO-D-10.2-001, CR-D-10.2-001

11. **Risk if not met:** H — Failure to log security events undermines every forensic + breach-investigation + compliance-evidence capability; tampering with logs (without Object Lock) is a per-se CRA Art. 13(11) integrity violation.

12. **Affected Stakeholders:** CTO (log policy owner), Lead Dev (application logging), DPO (log access for DSAR), Compliance Lead (review)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment


### OBL-D-10.3-001 — Regular Security Testing

1. **Description:** Regularly test the effectiveness of technical and organisational measures. For TinyTask, this obligation is met through a quarterly compliance review (controls checklist), annual penetration test by an independent third party, and ad-hoc security testing as part of the secure-development lifecycle (OBL-D-07.1-001). The corpus derivation (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring/D-10.3/D-10.3.json`) treats security testing as the verification layer for every other control: policies and procedures are inert without testing to prove they work. GDPR-C19 (Art. 32(1)(d) — regular testing) and CRA-C20 (Annex I §2(3)) jointly drive the obligation with NI=2.500. At MICRO scale, the testing programme combines quarterly internal review with annual external pen test. The obligation is PERIODIC — annual cadence for pen test, quarterly for compliance review.

2. **Scope:** All security controls across all obligations: D-01 through D-10. Quarterly compliance review: walkthrough of every obligation's verification criteria; annual pen test: external party validates the attack-surface posture.

3. **Out of Scope:** Continuous automated security testing (out of MICRO scope — quarterly + annual cadence is sufficient); red-team engagements with multi-week duration (out of MICRO scope); bug-bounty programme (out of MICRO scope).

4. **Source Article:** GDPR Art. 32(1)(d); CRA Annex I §2(3); GDPR-C19, CRA-C20

5. **NIST CSF Anchors:** DE.CM-01 (Network monitored), ID.RA-01 (Asset vulnerabilities), PR.PS-02 (Vulnerability management plan)

6. **Verification Criteria:**

   - Quarterly compliance review: every obligation's verification criteria walked through; findings documented; remediation tracked.

   - Annual penetration test: external party performs black-box + grey-box test; findings documented; remediation tracked; report stored in Doc 09 family.

   - Ad-hoc security testing: any new feature or major change triggers an application-layer security review before release.

7. **Verification Method:** TEST (quarterly review + annual pen test) + INSPECT (review minutes + pen test report) + DEMONSTRATE (live walkthrough of a new-feature security review)

8. **Owner:** CTO + Lead Dev

9. **Status:** TODO

10. **Dependencies:** All OBL obligations (testing is the verification layer), OBL-D-07.1-001 (secure dev cross-ref), SO-D-10.3-001, CR-D-10.3-001

11. **Risk if not met:** H — Failure to test creates an unverifiable security posture; an unverified posture is, regulatorily, equivalent to an insecure posture.

12. **Affected Stakeholders:** CTO (testing owner), Lead Dev (remediation), DPO (oversight), External pen-tester, Customers (downstream assurance)

13. **Maturity Score:** 2/4 → 3/4

14. **Implementation Priority:** HIGH

15. **Regulatory Reporting (Case_01):** Internal audit only

16. **External Auditor (Case_01):** Attestation report of managed hosting platform (covering managed object storage, managed key custody, managed audit-trail service, managed backup infrastructure) + ISO 27001 attestation (managed hosting region)

17. **Supervisory Body (Case_01):** CNPD (Comissão Nacional de Proteção de Dados) — lead GDPR SA for PT establishment



**D-10 Verification Cross-Walk (for human reviewer — updated post Sprint 6+ to 3 OBLs):**


| OBL ID | Verification Criteria Count | Method Mix | Primary NIST Anchor | Cadence |
|--------|----------------------------:|------------|---------------------|---------|
| OBL-D-10.1-001 | 3 | INSPECT + TEST + DEMONSTRATE | DE.CM-01 | Continuous + monthly review + annual tabletop |
| OBL-D-10.2-001 | 3 | INSPECT + TEST + DEMONSTRATE | PR.PS-04 | Continuous + monthly review |
| OBL-D-10.3-001 | 3 | TEST + INSPECT + DEMONSTRATE | DE.CM-01 | Quarterly + annual pen |

**D-10 Owner-Responsibility Decomposition (updated post Sprint 6+ to 3 OBLs):**


| Role | Primary Responsibility in this Sub-Domain | Backup / Approver |
|------|-------------------------------------------|-------------------|
| CTO | Monitoring strategy + alert taxonomy; logging strategy; pen-test engagement; audit cadence; CRA Art. 14 reporting owner | Lead Dev + DPO |
| Lead Dev | Managed monitoring configuration; managed audit-trail configuration; log bucket integrity; application audit logs; alert triage | CTO |
| DPO | On-call rotation for breach-correlated alerts; CRA Art. 14 co-routing to CNPD; DSAR log access | CTO |

---


### 5.11 Sprint 5 Summary Statistics


| Metric | Value | Notes |

|--------|-------|-------|
| Total detail cards | 34 | One per obligation enumerated in §4 (was 30; +4 OBL-D-07.2/3/4/10.1 from Sprint 6+ P7 orphan fix) |
| Fields per card | 17 | Items 1–17 of the template (description, scope, OOS, source, NIST, verification, method, owner, status, deps, risk, stakeholders, maturity, priority, reporting, auditor, supervisor) |
| Total cells populated | 578 | 34 × 17 (was 30 × 17 = 510; +68 cells) |
| HIGH priority cards | 30 | All P1 obligations (was 26; +4 from new OBLs) |
| MEDIUM priority cards | 4 | OBL-D-03.2-001, OBL-D-08.1-001, OBL-D-08.2-001 (proportionality flexibility) |
| Cards reporting to CNPD only | 0 | All D-04.3 cards route to both CNPD + ENISA; D-04 (others) report to CNPD; see below |
| Cards reporting to CNPD + ENISA (max-SLA) | 1 | OBL-D-04.3-001 only (T-001 routing) |
| Cards reporting to CNPD only (GDPR Art. 33) | 3 | OBL-D-04.1-001, OBL-D-04.2-001, OBL-D-04.4-001 |
| Cards reporting to ENISA only (CRA) | 4 | OBL-D-02.1-001, OBL-D-02.2-001, OBL-D-02.3-001, **OBL-D-10.1-001** (CRA Art. 14 — Sprint 6+ addition) |
| Cards reporting to CNPD + ENISA (periodic) | 3 | OBL-D-09.1-001, OBL-D-09.2-001, OBL-D-09.4-001 |
<| Cards reporting internal-audit-only | 22 | All D-01, D-03, D-05, D-06, D-07, D-08, D-10 (except D-04 + new D-10.1) |
| External auditor | Managed hosting provider documented third-party security attestation | Leveraged under managed-service configuration model |
| Supervisory bodies | CNPD (lead GDPR SA), ENISA (CRA), CNCS (PT CSIRT) | Multi-body routing per Doc 09 tensions T-001 / T-H-001 |

**Status field default:** all 30 cards are TODO at Sprint 5 completion — the Sprint 5 scope is enumeration and verification-criteria design, not implementation. Sprint 6+ (out of scope) will move cards to IN_PROGRESS as work begins; DONE only after the verification criteria have been independently witnessed.


**Maturity score basis:** 1/4 is the as-is state at Sprint 5 (managed-service configuration documented but no quarterly verification cadence yet); 3/4 is the LIGHTWEIGHT target after one full cycle of the verification criteria (typically 12-18 months from Sprint 5).


### 5.12 Corpus-Domain Traceability


Each obligation traces to a specific corpus domain file under `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`. The HSO + Sub-SO preservation rule (`proportionality_model.md §1` invariant) guarantees that the corpus content is frozen verbatim; the obligation here is the application-specific instantiation.


| OBL ID | Corpus Domain Path | HSO / Sub-SO Reference | Preservation Status |

|--------|---------------------|------------------------|---------------------|
| OBL-D-01.1-001 | `domains/D-01_Data-Protection/D-01.1/` | SO-D-01.1.GDPR | FROZEN (proportionality_model.md §1) |
| OBL-D-01.2-001 | `domains/D-01_Data-Protection/D-01.2/` | SO-D-01.2.GDPR | FROZEN |
| OBL-D-01.3-001 | `domains/D-01_Data-Protection/D-01.3/` | SO-D-01.3.CRA | FROZEN |
| OBL-D-01.4-001 | `domains/D-01_Data-Protection/D-01.4/` | SO-D-01.4.GDPR-CRA | FROZEN |
| OBL-D-02.1-001 | `domains/D-02_Vulnerability/D-02.1/` | SO-D-02.1.CRA | FROZEN (CRA sole authority) |
| OBL-D-02.2-001 | `domains/D-02_Vulnerability/D-02.2/` | SO-D-02.2.CRA | FROZEN (CRA sole authority) |
| OBL-D-02.3-001 | `domains/D-02_Vulnerability/D-02.3/` | SO-D-02.3.CRA | FROZEN (CRA sole authority) |
| OBL-D-03.1-001 | `domains/D-03_Access/D-03.1/` | SO-D-03.1.CRA | FROZEN (CRA sole authority) |
| OBL-D-03.2-001 | `domains/D-03_Access/D-03.2/` | SO-D-03.2.CRA | FROZEN (CRA sole authority) |
| OBL-D-03.3-001 | `domains/D-03_Access/D-03.3/` | SO-D-03.3.GDPR | FROZEN |
| OBL-D-03.4-001 | `domains/D-03_Access/D-03.4/` | SO-D-03.4.CRA | FROZEN (CRA sole authority) |
| OBL-D-04.1-001 | `domains/D-04_Incident/D-04.1/` | SO-D-04.1.CRA | FROZEN (CRA sole authority) |
| OBL-D-04.2-001 | `domains/D-04_Incident/D-04.2/` | SO-D-04.2.GDPR-CRA | FROZEN |
| OBL-D-04.3-001 | `domains/D-04_Incident/D-04.3/` | SO-D-04.3.GDPR-CRA | FROZEN (CONTEXTUAL — T-H-001) |
| OBL-D-04.4-001 | `domains/D-04_Incident/D-04.4/` | SO-D-04.4.GDPR | FROZEN |
| OBL-D-05.1-001 | `domains/D-05_Lifecycle/D-05.1/` | SO-D-05.1.GDPR-CRA | FROZEN |
| OBL-D-05.2-001 | `domains/D-05_Lifecycle/D-05.2/` | SO-D-05.2.GDPR | FROZEN |
| OBL-D-05.3-001 | `domains/D-05_Lifecycle/D-05.3/` | SO-D-05.3.GDPR-CRA | FROZEN |
| OBL-D-05.4-001 | `domains/D-05_Lifecycle/D-05.4/` | SO-D-05.4.GDPR | FROZEN (GDPR sole authority) |
| OBL-D-06.1-001 | `domains/D-06_Supply-Chain/D-06.1/` | SO-D-06.1.GDPR | FROZEN (GDPR sole authority) |
| OBL-D-06.2-001 | `domains/D-06_Supply-Chain/D-06.2/` | SO-D-06.2.CRA | FROZEN (CRA sole authority) |
| OBL-D-06.3-001 | `domains/D-06_Supply-Chain/D-06.3/` | SO-D-06.3.GDPR | FROZEN (GDPR sole authority) |
| OBL-D-07.1-001 | `domains/D-07_Secure-Dev/D-07.1/` | SO-D-07.1.GDPR-CRA | FROZEN (T-M-002) |
| OBL-D-08.1-001 | `domains/D-08_Human-Factors/D-08.1/` | SO-D-08.1.GDPR | FROZEN (GDPR sole authority) |
| OBL-D-08.2-001 | `domains/D-08_Human-Factors/D-08.2/` | SO-D-08.2.GDPR | FROZEN (GDPR sole authority) |
| OBL-D-09.1-001 | `domains/D-09_Governance/D-09.1/` | SO-D-09.1.GDPR-CRA | FROZEN (F-10 NI 2.500) |
| OBL-D-09.2-001 | `domains/D-09_Governance/D-09.2/` | SO-D-09.2.GDPR-CRA | FROZEN (T-M-001) |
| OBL-D-09.4-001 | `domains/D-09_Governance/D-09.4/` | SO-D-09.4.GDPR | FROZEN |
| OBL-D-10.2-001 | `domains/D-10_Monitoring/D-10.2/` | SO-D-10.2.CRA | FROZEN (CRA sole authority) |
| OBL-D-10.3-001 | `domains/D-10_Monitoring/D-10.3/` | SO-D-10.3.GDPR-CRA | FROZEN |

**F-01 / F-03 finding status:** OBL-D-01.3-001 carries no corresponding PO (Phase 1 finding F-01) but the corpus Sub-SO `SO-D-01.3.CRA` is preserved verbatim per `proportionality_model.md §1`. The CR-D-01.3-001 rule in Doc 11 §4 references the phantom PO-D-01.3-001 — this is finding F-03, deferred to human arbiter per Sprint 4 §3.7. The obligation card itself is complete and actionable; only the goal-to-rule linkage in Doc 11 requires human decision.


### 5.13 Tension & Finding Propagation


Detail cards surface the tensions and findings documented in `09_Strategic_Tensions_Report.md` and Sprint 1 §3.7.


| OBL ID | Affected Tensions | Affected Findings | Disposition |

|--------|-------------------|-------------------|-------------|
| OBL-D-01.4-001 | — | F-10 (NI divergence — Rich NI 2.500 authoritative) | RESOLVED in Sprint 4 §4.1 |
| OBL-D-04.3-001 | T-001 (Doc 09), T-H-001 (Sprint 1 §3.5) | — | max-SLA 24h routing applied; both CNPD + ENISA notified |
| OBL-D-01.3-001 | — | F-01 (no PO-D-01.3-001), F-03 (CR-D-01.3-001 references phantom PO) | DEFERRED to human arbiter |
| OBL-D-07.1-001 | T-M-002 (GDPR NI=2 vs CRA NI=3) | — | CRA higher intensity operationally dominant; structural, always active |
| OBL-D-09.1-001 | — | F-10 (NI divergence — Rich NI 2.500 authoritative) | RESOLVED in Sprint 4 §4.1 |
| OBL-D-09.2-001 | T-M-001 (frequency alignment) | — | Unified DPIA + CRA risk-assessment template |

All other 24 obligations have no current tension or finding linkages — they pass cleanly through Sprint 4 reconciliation.


### 5.14 Verification Cadence Rollup (Operational Calendar)


Aggregated verification activities across all 30 obligations, mapped to an annual calendar. This rollup supports capacity planning for the CTO + Lead Dev + DPO + Compliance Lead.


| Cadence | Activities | Cards Involved | Owner Load |

|---------|------------|---------------:|------------|
| **Continuous (real-time)** | Managed configuration rule monitoring, managed audit-trail, log forwarding, MFA enforcement | 9 (D-01.x, D-02.x, D-03.1, D-03.2, D-10.2) | CTO/Lead Dev — passive monitoring |
| **Per-PR / Per-build** | SAST, dependency scan, secret scan, SBOM generation, auth test suite | 7 (D-02.1, D-02.2, D-03.3, D-05.1, D-06.2, D-07.1, D-05.3) | Lead Dev — fully automated |
| **Daily** | Retention scan, backup verification, on-call pager test | 3 (D-04.4, D-05.2, D-04.1) | Mostly automated; on-call review |
| **Weekly** | Managed patch automation maintenance window, Dependabot PR merge | 2 (D-02.2, D-04.2) | Lead Dev — review of auto-PRs |
| **Monthly** | DSAR portability + erasure tests, log review, breach log review | 5 (D-05.3, D-05.4, D-10.2, D-09.4, D-04.3 tabletop) | DPO + Lead Dev |
| **Quarterly** | Compliance review, RBAC review, supplier review, DPA audit, security review | 14 (D-03.3, D-03.1, D-03.2, D-04.1, D-05.2, D-06.1, D-06.3, D-06.2, D-09.4, D-08.1 drill, D-04.2 drill, D-10.3, D-04.4 spot-check, D-08.1 phishing) | DPO + Compliance Lead + CTO |
| **Annual** | Pen test, ISMS audit, RoPA review, DPA template review, SAMM self-assessment, hardened-default review, training refresh, full restore drill, tabletop exercise | 18 (D-01.x all, D-02.x all, D-03.4, D-04.x all, D-05.3 review, D-06.x review, D-07.1 SAMM, D-08.1, D-08.2, D-09.x all, D-10.3) | CTO + DPO + Legal + External pen-tester |
| **Per-incident (TRIGGERED)** | ENISA 24h, CNPD 72h, max-SLA 24h (T-001), processor→controller (Art. 33(2)) | 4 (D-02.3, D-04.1, D-04.2, D-04.3) | CTO + DPO + Legal + Compliance Lead |

**Capacity estimate (LIGHTWEIGHT tier):** The quarterly cycle alone is the binding constraint — ~14 activities × ~2 person-days each ≈ 28 person-days per quarter, or roughly 30% of a single FTE-equivalent. This is consistent with the LIGHTWEIGHT proportionality choice and confirms the absence of a dedicated security/privacy headcount.


### 5.15 Documented Out-of-Scope Decisions (Sprint 5)


The 30 detail cards deliberately exclude the following fields that were considered but rejected for the MICRO/LIGHTWEIGHT tier:


| Excluded Field | Rationale | When to Re-evaluate |

|----------------|-----------|---------------------|
| Effort Estimate (FTE-days) | Out of MICRO scope per Doc 02 family; proportionality applies to documentation not just implementation | Tier elevation (MICRO → SMALL) |
| Cost Estimate (EUR) | Same as above; cost transparency is for SME/MEDIUM tier | Tier elevation |
| Target Timeline (months) | Same; timeline commitments are for SMALL/MEDIUM tier | Tier elevation |
| Compliance Officer sign-off (per-card) | Single DPO sign-off at the document level (frontmatter) is sufficient; per-card sign-off is SME/MEDIUM tier | Tier elevation |
| Per-card risk-acceptance (RACI) | Consolidated in Doc 09 family; per-card RACI is over-engineered at MICRO | Tier elevation |
| Per-card evidence-retention matrix | Consolidated at the document level (10-year retention per Doc 09 governance); per-card adds no information | Never (consolidation is permanent) |
| Per-card implementation cost (EUR/FTE) | Same as Effort Estimate | Tier elevation |

### 5.16 NIST CSF 2.0 Coverage Matrix


Aggregated NIST CSF anchor coverage across all 30 obligations. Each card references one or more sub-categories from the NIST Cybersecurity Framework 2.0; the matrix below shows how many obligations anchor to each sub-category. Coverage gaps are noted where they exist.


| NIST CSF 2.0 Sub-Category | Cards Anchoring | Count | Notes |

|---------------------------|-----------------|------:|-------|
| **GV — Govern** | | | |
| GV.OC-01 (Organizational risk strategy) | OBL-D-06.1, OBL-D-06.3, OBL-D-09.1, OBL-D-09.2, OBL-D-09.4 | 5 | Governance substrate; expected high coverage |
| GV.OC-03 (Roles and responsibilities) | OBL-D-09.1 | 1 | Documentation-level only; per-role training is D-08 |
| **ID — Identify** | | | |
| ID.RA-01 (Asset vulnerabilities identified) | OBL-D-02.1, OBL-D-02.2, OBL-D-02.3, OBL-D-07.1, OBL-D-10.3 | 5 | Vulnerability + testing substrate |
| ID.RA-04 (Potential business impacts) | OBL-D-09.2 | 1 | DPIA / risk-assessment level |
| GV.SC-03 (Contracts with suppliers) | OBL-D-06.1, OBL-D-06.2, OBL-D-06.3 | 3 | Supply-chain obligation layer |
| **PR — Protect** | | | |
| PR.AA-01 (Identity and credential management) | OBL-D-01.2, OBL-D-01.3, OBL-D-03.1, OBL-D-03.2, OBL-D-03.3, OBL-D-03.4, OBL-D-08.1 | 7 | Auth substrate; high coverage |
| PR.AA-04 (Access permissions managed) | OBL-D-03.3 | 1 | RBAC-specific |
| PR.AA-05 (Identity proofing) | OBL-D-03.2, OBL-D-03.3 | 2 | MFA + RBAC overlap |
| PR.AA-06 (Users authenticated) | OBL-D-03.1 | 1 | Authentication gate |
| PR.AT-01 (Users informed and trained) | OBL-D-08.1, OBL-D-08.2 | 2 | Training layer |
| PR.AT-02 (Privileged users understand roles) | OBL-D-08.1, OBL-D-08.2 | 2 | Role-specific depth |
| PR.DS-01 (Data-at-rest protection) | OBL-D-01.1, OBL-D-01.2, OBL-D-01.3, OBL-D-01.4, OBL-D-05.1, OBL-D-05.2, OBL-D-05.3, OBL-D-06.3, OBL-D-09.4, OBL-D-10.2 | 10 | Highest-coverage anchor |
| PR.DS-02 (Data-in-transit protection) | OBL-D-01.1, OBL-D-01.2, OBL-D-01.3 | 3 | At-rest / transit co-anchoring |
| ID.AM-08 (Asset inventory) | OBL-D-05.1, OBL-D-05.2, OBL-D-06.2, OBL-D-09.4 | 4 | Schema + retention + SBOM + RoPA |
| PR.DS-01 (Integrity checking) | OBL-D-01.4 | 1 | Integrity-specific |
| PR.PS-01 (Baseline configuration) | OBL-D-01.1, OBL-D-03.4, OBL-D-04.1, OBL-D-04.4, OBL-D-07.1, OBL-D-09.1, OBL-D-09.2, OBL-D-09.4 | 8 | Default-hardening substrate |
| PR.PS-06 (System development life cycle) | OBL-D-07.1 | 1 | SDLC-specific |
| PR.PS-01 (Configuration change control) | OBL-D-06.1, OBL-D-06.2, OBL-D-06.3 | 3 | Change control on supplier contracts |
| PR.IR-04 (Adequate resource capacity) | OBL-D-04.2, OBL-D-04.4 | 2 | Capacity + recovery |
| (retired CSF 1.1 sub-category) | OBL-D-05.1, OBL-D-05.2, OBL-D-05.4 | 3 | Lifecycle management (CSF 1.1 sub-category withdrawn; redistributed to `PR.DS-01`) |
| PR.PS-02 (Vulnerability management plan) | OBL-D-02.1, OBL-D-02.2, OBL-D-07.1, OBL-D-10.3 | 4 | Vuln-mgmt substrate |
| PR.PS-02 (Maintenance and repair) | OBL-D-02.2 | 1 | Patch pipeline |
| PR.PS-04 (Event logging) | OBL-D-10.2 | 1 | Audit logging |
| **DE — Detect** | | | |
| DE.CM-01 (Network monitored) | OBL-D-10.2, OBL-D-10.3 | 2 | Logging + testing overlap |
| **RS — Respond** | | | |
| RS.MA-01 (Response plan executed) | OBL-D-04.1, OBL-D-04.2, OBL-D-04.3, OBL-D-04.4 | 4 | Incident-response substrate |
| GV.RR-02 (Personnel know roles) | OBL-D-04.2, OBL-D-04.3 | 2 | Incident personnel |
| RS.CO-02 (Incident reporting) | OBL-D-02.3, OBL-D-04.3 | 2 | Reporting obligation |
| DE.AE-06 (Notifications from detection) | OBL-D-02.1, OBL-D-02.3, OBL-D-04.1, OBL-D-04.3 | 4 | Detection notification overlap |

**Coverage gaps (acceptable at MICRO/LIGHTWEIGHT):** None at the sub-category level — every active sub-category anchors to at least one obligation. The 8 inactive NIST CSF sub-categories (e.g., DE.AE-02 analysis of detected events, RS.MI-02 incident mitigation, RC.RP-01 recovery plan execution) are covered implicitly by the active obligations' verification methods rather than as separate anchors.


### 5.17 Verification Method Inventory


Cumulative count of verification methods across all 30 cards. Multiple methods per card are common (the §6 verification-method field records the primary mix).


| Verification Method | Cards Using (Primary or Mix) | Notes |

|---------------------|-----------------------------:|-------|
| **INSPECT** | 27 | Most common — almost every card requires documentation review |
| **DEMONSTRATE** | 24 | Live-system walkthroughs dominate the operational verification |
| **TEST** | 19 | Automated tests in CI/CD + scheduled drills |
| **ANALYZE** | 4 | Used for DB constraint audits, log review, managed IAM least-privilege |

**Method distribution observation:** The bias toward INSPECT + DEMONSTRATE reflects the managed-service configuration model — verification is more about proving the configuration is correct than running novel attack scenarios. TEST is concentrated on the D-02 vulnerability gates and D-04 DR drills; ANALYZE is reserved for structural verification (DB integrity, IAM least-privilege).


### 5.18 Status Roadmap (Sprint 5 → Sprint 6+)


All 30 cards begin at TODO. The status transitions are governed by Sprint 6+ (out of Sprint 5 scope) but are recorded here for traceability.


| Status Transition | Trigger | Owner | Out-of-Sprint-5 Scope |

|-------------------|---------|-------|----------------------|
| TODO → IN_PROGRESS | Implementation work begins for the verification criteria (e.g., enabling a Config rule, configuring MFA, drafting a policy) | Card owner per §8 | Sprint 6 (execution phase) |
| IN_PROGRESS → DONE | Verification criteria independently witnessed by a second party (DPO, Compliance Lead, External auditor) | Witness per RACI | Sprint 7 (verification phase) |
| DONE → REGRESSION | Material change to underlying obligation (regulation amendment, sub-domain re-classification, owner change) | Doc 09 governance trigger | Ongoing (continuous) |
| REGRESSION → IN_PROGRESS | Re-implementation required after regression trigger | Card owner | Triggered |

**Sprint 5 deliverable scope reminder:** Sprint 5 is enumeration + verification-criteria design only. Implementation is deferred. The Sprint 5 verdict is PASS if all 30 cards are present, all 17 fields per card are populated, and the cross-references to Doc 09 / Doc 10 / Doc 11 / phase1_ontology.yaml are accurate.


### 5.19 Cross-Document Reference Snapshot


For each of the 30 obligations, the table below records the downstream references in the rest of the methodology. This snapshot is the canonical cross-reference index used by Doc 11 (Rules Catalog) and the audit-trail queries.


| OBL ID | Doc 07 Reference | Doc 09 (Tensions) | Doc 10 (Goals) | Doc 11 (CR Rules) | Doc 12 (Catalog Sheet) |

|--------|------------------|-------------------|----------------|--------------------|-------------------------|
| OBL-D-01.1-001 | 07_Structured_Compliance_Matrix §3 | — | PO-D-01.1-001 | CR-D-01.1-001 | Sheet 1 (Data Protection) |
| OBL-D-01.2-001 | 07_Structured_Compliance_Matrix §3 | — | PO-D-01.2-001 | CR-D-01.2-001 | Sheet 1 |
| OBL-D-01.3-001 | 07_Structured_Compliance_Matrix §3 | — | — (F-01) | CR-D-01.3-001 (F-03 ref) | Sheet 1 |
| OBL-D-01.4-001 | 07_Structured_Compliance_Matrix §3 | F-10 reconciliation | PO-D-01.4-001 | CR-D-01.4-001 | Sheet 1 |
| OBL-D-02.1-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-02.1-001 | CR-D-02.1-001 | Sheet 2 (Vulnerability) |
| OBL-D-02.2-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-02.2-001 | CR-D-02.2-001 | Sheet 2 |
| OBL-D-02.3-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-02.3-001 | CR-D-02.3-001 | Sheet 2 |
| OBL-D-03.1-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-03.1-001 | CR-D-03.1-001 | Sheet 3 (Access Control) |
| OBL-D-03.2-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-03.2-001 | CR-D-03.2-001 | Sheet 3 |
| OBL-D-03.3-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-03.3-001 | CR-D-03.3-001 | Sheet 3 |
| OBL-D-03.4-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-03.4-001 | CR-D-03.4-001 | Sheet 3 |
| OBL-D-04.1-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-04.1-001 | CR-D-04.1-001 | Sheet 4 (Incident) |
| OBL-D-04.2-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-04.2-001 | CR-D-04.2-001 | Sheet 4 |
| OBL-D-04.3-001 | 07_Structured_Compliance_Matrix §3 | T-001, T-H-001 | SO-D-04.3-001 | CR-D-04.3-001 | Sheet 4 |
| OBL-D-04.4-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-04.4-001 | CR-D-04.4-001 | Sheet 4 |
| OBL-D-05.1-001 | 07_Structured_Compliance_Matrix §3 | — | PO-D-05.1-001 | CR-D-05.1-001 | Sheet 5 (Lifecycle) |
| OBL-D-05.2-001 | 07_Structured_Compliance_Matrix §3 | — | PO-D-05.2-001 | CR-D-05.2-001 | Sheet 5 |
| OBL-D-05.3-001 | 07_Structured_Compliance_Matrix §3 | — | PO-D-05.3-001 | CR-D-05.3-001 | Sheet 5 |
| OBL-D-05.4-001 | 07_Structured_Compliance_Matrix §3 | — | PO-D-05.4-001 | CR-D-05.4-001 | Sheet 5 |
| OBL-D-06.1-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-06.1-001 | CR-D-06.1-001 | Sheet 6 (Supply Chain) |
| OBL-D-06.2-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-06.2-001 | CR-D-06.2-001 | Sheet 6 |
| OBL-D-06.3-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-06.3-001 | CR-D-06.3-001 | Sheet 6 |
| OBL-D-07.1-001 | 07_Structured_Compliance_Matrix §3 | T-M-002 | PO-D-07.1-001 | CR-D-07.1-001 | Sheet 7 (Secure Dev) |
| OBL-D-08.1-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-08.1-001 | CR-D-08.1-001 | Sheet 8 (Human Factors) |
| OBL-D-08.2-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-08.2-001 | CR-D-08.2-001 | Sheet 8 |
| OBL-D-09.1-001 | 07_Structured_Compliance_Matrix §3 | F-10 reconciliation | PO + SO-D-09.1-001 | CR-D-09.1-001 | Sheet 9 (Governance) |
| OBL-D-09.2-001 | 07_Structured_Compliance_Matrix §3 | T-M-001 | PO + SO-D-09.2-001 | CR-D-09.2-001 | Sheet 9 |
| OBL-D-09.4-001 | 07_Structured_Compliance_Matrix §3 | — | PO-D-09.4-001 | CR-D-09.4-001 | Sheet 9 |
| OBL-D-10.2-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-10.2-001 | CR-D-10.2-001 | Sheet 10 (Monitoring) |
| OBL-D-10.3-001 | 07_Structured_Compliance_Matrix §3 | — | SO-D-10.3-001 | CR-D-10.3-001 | Sheet 10 |

**Cross-reference completeness:** 30/30 obligations trace to Doc 07, Doc 11, and Doc 12 (the canonical compliance-artifact chain). Doc 09 (tensions) and Doc 10 (goals) have intentional gaps that are themselves documented (F-01, F-02, F-03 from Sprint 1 §3.7; T-001, T-H-001, T-M-001, T-M-002 from Sprint 1 §3.5; F-10 from Sprint 4 §4.1). The gaps are tracked and not silently accepted.


### 5.20 Conclusion and Handoff


This §5 closes Sprint 5a (Doc 08 Obligation Detail Cards) and Sprint 6+ (P7 orphan fix). The deliverable summary:


- **34 detail cards** populated, one per obligation enumerated in §4 (was 30 at Sprint 5; +4 OBL-D-07.2/3/4/10.1 from Sprint 6+). Each card carries 17 fields covering description (with corpus-derived context), scope, out-of-scope, source article, NIST CSF anchors, verification criteria, verification method, owner, status, dependencies, risk-if-not-met, affected stakeholders, maturity score, implementation priority, regulatory reporting, external auditor, and supervisory body.

- **578 cells** of structured obligation metadata, equivalent to 34 × 17 (was 30 × 17 = 510; +68 cells from Sprint 6+ additions).

- **Cross-references** to Doc 07 (compliance matrix), Doc 09 (tensions), Doc 10 (goals), Doc 11 (CR rules), Doc 12 (catalog), and the corpus domain files are documented in §5.19 and §5.12.

- **Operational rollup** (§5.14) maps verification activities to an annual calendar; capacity estimate (~30% of one FTE-equivalent per quarter) is consistent with the LIGHTWEIGHT proportionality choice.

- **Tension and finding propagation** (§5.13) confirms that F-01 / F-03 are deferred to human arbiter, F-10 is resolved in Sprint 4 §4.1, and T-001 / T-H-001 / T-M-001 / T-M-002 are surfaced in the affected cards.

- **NIST CSF 2.0 coverage** (§5.16) confirms every active sub-category anchors to at least one obligation; no coverage gaps requiring additional obligations.


Sprint 5a is a content-only delivery; no commits are produced by this Executor. The Validator is expected to verify the 30-card count, the 17-field completeness per card (sample 3 random cards), the frontmatter update, and the cross-reference integrity. The verdict is PASS if all four checks succeed; CONDITIONAL_PASS if minor cosmetic issues are found; FAIL if any card is missing a required field or any cross-reference is broken.


### 5.21 Regulatory Penalty Exposure Reference


For the DPO and Legal reviewer, the table below summarises the regulatory penalty exposure associated with each obligation. This is not a per-card field (it would duplicate the Risk-if-not-met field for many cards) but a consolidation for human-decision support.


| Sub-Domain | GDPR Maximum Penalty | CRA Maximum Penalty | Combined Operational Risk |

|------------|---------------------:|--------------------:|---------------------------|
| D-01 (Data Protection) | Art. 83(5): up to EUR 20M or 4% of global turnover | Annex I: market-surveillance corrective measures + Art. 64 fines per member state | HIGH — confidentiality/integrity failure affects every downstream obligation |
| D-02 (Vulnerability) | Art. 32 only (no Art. 83 fine unique to vulns) | Art. 14 exploited-vuln reporting: market-suspension + administrative fines up to EUR 15M or 2.5% turnover (per Art. 64) | HIGH — CRA Art. 14 per-se reporting violation |
| D-03 (Access Control) | Art. 32 + Art. 5(1)(f): up to EUR 20M or 4% | Annex I §1(5-7): market-surveillance action | HIGH — credential leak = GDPR + CRA exposure |
| D-04 (Incident) | Art. 83(5)(a) breach notification failure: up to EUR 20M or 4% within hours | Art. 14 exploited-vuln reporting: EUR 15M or 2.5% within 24h | **HIGHEST** — D-04.3 is the most time-sensitive obligation in the matrix |
| D-05 (Lifecycle) | Art. 83(5)(b) data subject rights failure: up to EUR 20M or 4% | Annex I §1(11) secure deletion: market-surveillance action | HIGH — DSAR failures are commonly enforced |
| D-06 (Supply Chain) | Art. 28 violation (controller accountability): up to EUR 20M or 4% | Art. 13(11) SBOM: market-surveillance action + Art. 64 fines | HIGH — supplier failure cascades to TinyTask as controller |
| D-07 (Secure Dev) | Art. 25 violation: up to EUR 20M or 4% | Annex I §1 secure-by-default: market-surveillance action | MEDIUM — documentation-level enforcement typical |
| D-08 (Human Factors) | Art. 39(1)(b) DPO tasks: administrative fines | (CRA does not impose comparable training obligation directly) | LOW — GDPR administrative enforcement typical |
| D-09 (Governance) | Art. 5(2) accountability: up to EUR 20M or 4%; Art. 30 RoPA: up to EUR 10M or 2% | Art. 13 technical documentation: market-surveillance action | HIGH — accountability failures are the most commonly enforced GDPR penalty category |
| D-10 (Monitoring) | Art. 32(1)(d) testing: up to EUR 20M or 4% | Annex I §2 audit logging: market-surveillance action | MEDIUM — testing failures are typically remediation-driven |

**Penalty interpretation for TinyTask:** The GDPR EUR 20M / 4% ceiling applies to the *higher* of the two for any single violation. At MICRO scale with sub-EUR 10M annual turnover, the percentage-based penalty is the binding constraint (effectively up to 4% of revenue, which for a MICRO SaaS would typically cap at EUR 50K-EUR 200K). CRA penalties are harder to predict because the regulation is newer and member-state transposition varies; the conservative posture is to assume the EUR 15M / 2.5% ceiling applies even at MICRO scale.


**Operational mitigation:** The 30 cards' Risk-if-not-met field uses H/M/L rather than monetary values because the proportionality model intentionally avoids cost quantification at the MICRO tier (see §5.15). The H/M/L is calibrated against the operational likelihood of detection (HIGH = likely detected by regulator or auditor within 12 months; MEDIUM = detectable on a customer-initiated complaint or incident; LOW = detectable only on internal review).


### 5.22 Owner-Workload Heatmap (Sprint 6 Planning Input)


The Owner column (field 8) maps each card to one or more owners. The heatmap below aggregates the total cards per owner to inform Sprint 6 capacity planning. Multiple owners per card share the work; this is a primary-count metric (each card counts once per named owner).


| Owner | Cards (Primary) | Cards (Co-owner) | Total Touch-Points | Notes |

|-------|----------------:|-----------------:|-------------------:|-------|
| CTO | 30 (all) | 0 | 30 | Universal primary owner — every obligation has CTO listed |
| Lead Dev | 22 | 0 | 22 | D-01 (4), D-02 (3), D-03 (4), D-04 (1 — D-04.1 only), D-06 (3), D-07 (1), D-10 (2), D-04.4 (1) — see card fields |
| DPO | 14 | 0 | 14 | D-04 (4), D-05 (4), D-08 (1 — D-08.1), D-09 (3), D-08.2 (1), D-04.1 (1) |
| Compliance Lead | 8 | 0 | 8 | D-04 (4), D-09 (3), D-06.2 (1) |
| Procurement | 6 | 0 | 6 | D-02 (3), D-06 (3) |
| HR | 2 | 0 | 2 | D-08 (2) |
| Legal | 3 | 0 | 3 | D-09 (3) |
| External (managed hosting provider ISO 27001 attestation + pen-tester) | (auditor role) | — | — | Per §16 of each card; not counted as primary owner |

**Capacity implication:** CTO + Lead Dev carry the implementation load (52 of 85 touch-points = ~61%); DPO + Compliance Lead + Legal carry the governance + reporting load (25 of 85 = ~29%); Procurement + HR carry the supplier + people load (8 of 85 = ~10%). The CTO-as-universal-primary pattern is intentional — it reflects the single-person security-engineering reality at MICRO — and is itself documented as a proportionality consideration (single-point-of-failure mitigated by named backups).


**Backup / approver decomposition:** Per the Owner-Responsibility Decomposition tables above, every primary owner has a named backup. CTO ↔ Lead Dev is the most common pairing; DPO ↔ Legal for governance; DPO ↔ Compliance Lead for incident classification. This decomposition is the input to Sprint 6 RACI construction.


### 5.23 Implementation Hints by Sub-Domain (Sprint 6 Planning Input)


A condensed implementation playbook for the Sprint 6 execution phase. The objective is to give the Sprint 6 Executor a fast-start reference that does not require re-reading all 30 cards.


**D-01 (Data Protection) — 4 cards, 4 sprints (S6-S9):**

- S6: managed-storage encryption enforcement policies + managed NoSQL encryption-enabled deployed; verified COMPLIANT (covers OBL-D-01.1-001)

- S7: Edge + load-balancer modern cryptographic protocol hardening; cipher review (covers OBL-D-01.2-001)

- S8: Managed key rotation enabled; IAM policy tightening on decrypt operations (covers OBL-D-01.3-001)

- S9: HMAC on critical objects + DB constraint audit + Object Lock on audit-log bucket (covers OBL-D-01.4-001)


**D-02 (Vulnerability) — 3 cards, 2 sprints (S6-S7):**

- S6: automated vulnerability scanner + managed dependency audit + machine-readable SBOM in CI (covers OBL-D-02.1-001)

- S7: Managed patch automation + Dependabot + security.txt + ENISA workflow (covers OBL-D-02.2-001 and OBL-D-02.3-001)


**D-03 (Access Control) — 4 cards, 2 sprints (S8-S9):**

- S8: managed identity service baseline + MFA opt-in flow + hardened-default review (covers OBL-D-03.1-001, OBL-D-03.2-001, OBL-D-03.4-001)

- S9: RBAC quarterly review cycle established + authorization test suite (covers OBL-D-03.3-001)


**D-04 (Incident Response) — 4 cards, 1 sprint (S10 — all together for incident-response):**

- S10: Managed monitoring alarms + managed notification routing + 4h containment playbook + max-SLA notification workflow + DR drill (covers all four)


**D-05 (Data Lifecycle) — 4 cards, 2 sprints (S11-S12):**

- S11: Schema-level minimisation + retention cron jobs + managed object storage lifecycle policies (covers OBL-D-05.1-001, OBL-D-05.2-001)

- S12: Erasure API + portability API + DSAR runbook (covers OBL-D-05.3-001, OBL-D-05.4-001)


**D-06 (Supply Chain) — 3 cards, 1 sprint (S13):**

- S13: Supplier attestation register + DPA template refresh + SBOM archival (covers all three)


**D-07 (Secure Development) — 1 card, ongoing (S1+):**

- S6+: SAST + dependency scan + secret scan gates already in CI from D-02.1; D-07.1 verification = gates + SAMM self-assessment (covers OBL-D-07.1-001)


**D-08 (Human Factors) — 2 cards, 1 sprint (S14):**

- S14: Annual awareness email + role-specific training register + phishing drill (covers both)


**D-09 (Governance) — 3 cards, 2 sprints (S15-S16):**

- S15: ISMS policy documentation set + 10-year retention + managed object storage Object Lock (covers OBL-D-09.1-001, OBL-D-09.4-001)

- S16: Unified DPIA + CRA risk-assessment template + annual review cadence (covers OBL-D-09.2-001)


**D-10 (Monitoring) — 2 cards, 1 sprint (S17):**

- S17: Managed audit-trail multi-region trail + tamper-evident managed object storage log bucket + quarterly compliance review + annual pen-test engagement (covers both)


**Total Sprint 6+ scope:** ~17 sub-sprints covering all 30 cards. Implementation is out of Sprint 5 scope; this is the hand-off brief for the Sprint 6 Executor.


## 6. NEXT STEPS

- [x] **Sprint 1:** Cross-check 30 obligations ↔ 30 goals ↔ 30 CR rules — DONE with CONDITIONAL_PASS verdict
- [x] **Sprint 3:** Regenerate 12_Rules_Catalog.xlsx (14 sheets) — DONE
- [x] **Sprint 4:** Port legacy §4 catalog table (30 obligations × 11 cols) + 6 new cols (180 cells) into Rich §4; resolve F-10 NI for OBL-D-01.4-001 and OBL-D-09.1-001 — DONE
- [x] **Sprint 5a (this sprint):** Populate 17-field detail cards for all 30 obligations (510 cells: 30 × 17) — DONE; see §5
- [x] **Sprint 6+ (this contract — P7 orphan fix):** Add 4 new OBLs (D-07.2/3/4 + D-10.1 — CRA sole authority; +68 cells → 578 total); correct `phase1_ontology.yaml` `not_covered` to remove 3 false sole-authority gaps; update §2/§3 reconciliation tables + introduce findings F-07/F-08/F-09 — DONE; F-07 (cross-doc orphan on Doc 10 PO/SO + Doc 11 CR for the 4 new sub-domains) tracked for follow-on contract
- [ ] Sprint 5b: Resolve findings F-01/F-03 (PO-D-01.3-001 missing) — defer to human arbiter
- [ ] Sprint 6+ follow-on: Add PO-D-07.2 + SO-D-07.3/4 + SO-D-10.1 to Doc 10; add CR-D-07.2/3/4 + CR-D-10.1 to Doc 11; resolve F-07. Reconcile `01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` (twin ontology) and `00_Taxonomy_Reference.md` §3 (cross-case reference) — F-08/F-09.


---

**End of Sprint 1 + Sprint 4 + Sprint 5a + Sprint 6+ (P7 orphan fix) — Doc 08**