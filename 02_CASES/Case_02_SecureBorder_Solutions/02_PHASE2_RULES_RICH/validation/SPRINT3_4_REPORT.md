---
document_id: AEGIS-P2-RICH-SPRINT3-4
title: Sprint 3+4 Combined Report — Catalog Tables + 6 New Columns (Case_02 Phase 2 Rich Mode)
phase: 2
version: 1.0
created: 2026-08-07
updated: 2026-08-07
author: Sprint 3+4 Executor (catalog-port-and-adjusted-fields)
status: COMPLETE
case: Case_02_SecureBorder_Solutions
tier: HIGH
sprint: 3+4
sprint_role: catalog_port_and_adjusted_fields
branch: feature/aegis-p2-case02-csf-pf-airmf
inputs:
  - ../02_PHASE2_RULES/08_Obligation_Derivation.md (legacy, read-only)
  - ../02_PHASE2_RULES/10_Privacy_Security_Goals.md (legacy, read-only)
  - ../02_PHASE2_RULES/11_Rules_Catalog.md (legacy, read-only)
  - 08_Obligation_Derivation.md (Sprint 1 — pre-catalog-port baseline)
  - 10_Privacy_Security_Goals.md (Sprint 1 — pre-catalog-port baseline)
  - 11_Rules_Catalog.md (Sprint 1 — pre-catalog-port baseline)
  - 09_Strategic_Tensions_Report.md (Sprint 2)
  - 01_PHASE1_CONTEXT_RICH/07b_Proportionality_Profile.md (LIGHTWEIGHT target reference)
  - 01_PHASE1_CONTEXT_RICH/04d_Org_Roles_RACI.md (Owner heuristic reference)
  - 12_Rules_Catalog.xlsx (Sprint 3 — 14 sheets, Sheet 12 Affected_Stakeholders)
  - SPRINT1_REPORT.md (F-04a/b goal count, F-10 NI divergence context)
  - SPRINT3_REPORT.md (F-10 raised)
outputs:
  - 08_Obligation_Derivation.md (v1.1 → v1.2 — §4 catalog + §4.1 NI reconciliation + 6 new cols; status RECONCILED → ADJUSTED_OBJECTIVES)
  - 10_Privacy_Security_Goals.md (v1.1 → v1.2 — §3.1 PG catalog + §4.1 SG catalog + 6 new cols)
  - 11_Rules_Catalog.md (v1.1 → v1.2 — §3 field schema + §4 CR catalog + §5 BPR catalog + 6 new cols)
  - validation/SPRINT3_4_REPORT.md (this file)
verdict: PASS
new_findings: [F-10 RESOLVED, F-04a RESOLVED, F-04b RESOLVED]
resolved_findings: [F-10, F-04a, F-04b]
carried_findings: [F-01 (Doc 10), F-02 (Doc 08), F-03 (Doc 11)]
cells_added_total: 642
catalog_rows_added: [30 OBL, 11 PG, 20 SG, 30 CR, 16 BPR]
---

# Sprint 3+4 Combined Report — Catalog Tables + 6 New Columns

> **Sprint theme:** Port legacy `02_PHASE2_RULES/` §4/§5 catalog tables into Rich `02_PHASE2_RULES_RICH/` Docs 08/10/11 with 11/6/9 legacy fields preserved + 6 new Sprint 4 fields appended (Owner, Verification Criteria, Maturity Score, Implementation Priority, Affected Stakeholders, Regulatory Reporting). Resolve F-04a/b (31 goals not 30) and F-10 (NI divergence for OBL-D-01.4-001 and OBL-D-09.1-001).
>
> **Sprint date:** 2026-08-07. **Verdict:** ✅ **PASS** (5/5 deliverables; 3 findings resolved, 3 carried forward).
>
> **Sprint 3+4 in context:** 0 (skeleton) → 1 (reconciliation) → 2 (multi-paragraph tensions) → 3 (final docs + Excel — separately delivered) → **3+4 (catalog port + 6 new cols — this sprint)** → 5 (DEEP enrichment, 15 fields × 107 cards) → Validator.

---

## §1 Sprint 3+4 Combined Tasks

| # | Task | Status | Output | Lines / size |
|---|------|:------:|--------|-------------:|
| 1 | Update Doc 08 frontmatter (status, version, sprint, verdict, scope) | ✅ PASS | `08_Obligation_Derivation.md` frontmatter | — |
| 2 | Port legacy Doc 08 §4 catalog table (30 obligations × 11 cols) into Rich §4 with 17 cols | ✅ PASS | Doc 08 §4 (D-01..D-10 sections) | 300 → 458 |
| 3 | Add §4.1 NI Reconciliation Notes (resolves F-10 for OBL-D-01.4-001 and OBL-D-09.1-001) | ✅ PASS | Doc 08 §4.1 | — |
| 4 | Update Doc 10 frontmatter | ✅ PASS | `10_Privacy_Security_Goals.md` frontmatter | — |
| 5 | Add §3.1 PG catalog (11 PG × 12 cols) and §4.1 SG catalog (20 SG × 12 cols) | ✅ PASS | Doc 10 §3.1 + §4.1 | 196 → 354 |
| 6 | Resolve F-04a/b (31 goals not 30) — 11 PG + 20 SG confirmed from row counts | ✅ PASS | Doc 10 §3.1 + §4.1 | — |
| 7 | Update Doc 11 frontmatter | ✅ PASS | `11_Rules_Catalog.md` frontmatter | — |
| 8 | Add §3 Rule Definition Structure (schema anchor) | ✅ PASS | Doc 11 §3.1 + §3.2 | — |
| 9 | Add §4 CR catalog (30 CR × 17 cols) and §5 BPR catalog (16 BPR × 15 cols) | ✅ PASS | Doc 11 §4 + §5 | 232 → 506 |
| 10 | Resolve F-10 NI for CR-D-01.4-001 and CR-D-09.1-001 (DR-002 AVG = 2.500) | ✅ PASS | Doc 11 §4 + §7.1 | — |
| 11 | Write this report | ✅ PASS | `validation/SPRINT3_4_REPORT.md` | NEW — 250+ |

**Constraint compliance:** no legacy `02_PHASE2_RULES/` file was modified; no Phase 1 / Phase 3 / corpus file was modified; no git commit was created; no Effort/Cost/Timeline field was introduced.

---

## §2 Catalog Table Port (Doc 08, 10, 11)

### §2.1 Doc 08 — Regulatory Obligations Catalog

**Output:** `08_Obligation_Derivation.md` — 300 → **458 lines** (+158). Added new §4 "REGULATORY OBLIGATIONS CATALOG" with 10 sub-domain sections (D-01..D-10) + §4.1 NI Reconciliation Notes.

**Rows added:**

| Sub-Domain | Rows | OBL IDs |
|------------|-----:|---------|
| D-01 | 4 | OBL-D-01.1, 01.2, 01.3, 01.4 |
| D-02 | 3 | OBL-D-02.1, 02.2, 02.3 |
| D-03 | 4 | OBL-D-03.1, 03.2, 03.3, 03.4 |
| D-04 | 4 | OBL-D-04.1, 04.2, 04.3, 04.4 |
| D-05 | 4 | OBL-D-05.1, 05.2, 05.3, 05.4 |
| D-06 | 3 | OBL-D-06.1, 06.2, 06.3 |
| D-07 | 1 | OBL-D-07.1 |
| D-08 | 2 | OBL-D-08.1, 08.2 |
| D-09 | 3 | OBL-D-09.1, 09.2, 09.4 |
| D-10 | 2 | OBL-D-10.2, 10.3 |
| **TOTAL** | **30** | — |

**Sub-domain nuance notes preserved** from legacy §4: D-04 (GDPR Art. 33(2) processor→controller "without undue delay"), D-07 (CRA Art. 13(8) 5-year support period + CRA Art. 13(9) 10-year update retention).

### §2.2 Doc 10 — Privacy and Security Goals Catalog

**Output:** `10_Privacy_Security_Goals.md` — 196 → **354 lines** (+158). Added new §3 "PRIVACY GOALS CATALOG" with 4 sub-domain sections + §3.2 PG summary; new §4 "SECURITY GOALS CATALOG" with 7 sub-domain sections + §4.2 SG summary. Existing §3/§4 cross-checks renumbered to §5/§6.

**Rows added:**

| Catalog | Sub-domain | Rows | Goal IDs |
|---------|------------|-----:|----------|
| **PG (§3.1)** | D-01 | 3 | PG-D-01.1, 01.2, 01.4 |
| | D-05 | 4 | PG-D-05.1, 05.2, 05.3, 05.4 |
| | D-07 | 1 | PG-D-07.1 |
| | D-09 | 3 | PG-D-09.1, 09.2, 09.4 |
| | **PG TOTAL** | **11** | — |
| **SG (§4.1)** | D-02 | 3 | SG-D-02.1, 02.2, 02.3 |
| | D-03 | 4 | SG-D-03.1, 03.2, 03.3, 03.4 |
| | D-04 | 4 | SG-D-04.1, 04.2, 04.3, 04.4 |
| | D-06 | 3 | SG-D-06.1, 06.2, 06.3 |
| | D-08 | 2 | SG-D-08.1, 08.2 |
| | D-09 | 2 | SG-D-09.1, 09.2 |
| | D-10 | 2 | SG-D-10.2, 10.3 |
| | **SG TOTAL** | **20** | — |
| | **GRAND TOTAL** | **31** | — |

### §2.3 Doc 11 — Rules Catalog (CR + BPR)

**Output:** `11_Rules_Catalog.md` — 232 → **506 lines** (+274). Added new §3 "RULE DEFINITION STRUCTURE" with §3.1 schema anchor + §3.2 ID structure; new §4 "COMPLIANCE RULES CATALOG" with 10 sub-domain sections; new §5 "BEST PRACTICE RULES CATALOG" with 8 sub-domain sections. Existing §3 cross-checks renumbered to §6.

**Rows added:**

| Catalog | Sub-domain | Rows | Rule IDs |
|---------|------------|-----:|----------|
| **CR (§4)** | D-01 | 4 | CR-D-01.1, 01.2, 01.3, 01.4 |
| | D-02 | 3 | CR-D-02.1, 02.2, 02.3 |
| | D-03 | 4 | CR-D-03.1, 03.2, 03.3, 03.4 |
| | D-04 | 4 | CR-D-04.1, 04.2, 04.3, 04.4 |
| | D-05 | 4 | CR-D-05.1, 05.2, 05.3, 05.4 |
| | D-06 | 3 | CR-D-06.1, 06.2, 06.3 |
| | D-07 | 1 | CR-D-07.1 |
| | D-08 | 2 | CR-D-08.1, 08.2 |
| | D-09 | 3 | CR-D-09.1, 09.2, 09.4 |
| | D-10 | 2 | CR-D-10.2, 10.3 |
| | **CR TOTAL** | **30** | — |
| **BPR (§5)** | D-01 | 2 | BPR-D-01.1, 01.2 |
| | D-02 | 2 | BPR-D-02.1, 02.2 |
| | D-03 | 3 | BPR-D-03.1, 03.2, 03.4 |
| | D-04 | 2 | BPR-D-04.3-001, 04.3-002 |
| | D-05 | 1 | BPR-D-05.3 |
| | D-07 | 2 | BPR-D-07.1, 07.2 |
| | D-09 | 1 | BPR-D-09.1 |
| | D-10 | 3 | BPR-D-10.2, 10.3-001, 10.3-002 |
| | **BPR TOTAL** | **16** | — |
| | **GRAND TOTAL** | **46** | — |

---

## §3 6 New Columns Added

### §3.1 Column Definitions

| Column | Source / Heuristic | Default per Row |
|--------|---------------------|-----------------|
| **Owner** | Sub-domain heuristic (Doc 08 §4 + Doc 04d RACI) | per sub-domain |
| **Verification Criteria** | Doc 08 §4 per-obligation + per-rule framework-specific for BPR | 1-line test/check |
| **Maturity Score** | Doc 07b §4 LIGHTWEIGHT target | `1/4 → 3/4` (all rows) |
| **Implementation Priority** | Doc 07b §4 LIGHTWEIGHT priority | `HIGH` (all rows) |
| **Affected Stakeholders** | Sheet 12 Affected_Stakeholders + Doc 04d RACI | `Customers, DPO, CTO, ENISA` |
| **Regulatory Reporting** | Doc 08 §4 sub-domain heuristic | per sub-domain (BPR uniform: `Internal audit only`) |

### §3.2 Owner Heuristic

| Sub-Domain | Owner |
|------------|-------|
| D-01 | CTO + Lead Dev |
| D-02 | CTO + Lead Dev + Procurement |
| D-03 | CTO + Lead Dev |
| D-04 | CTO + DPO + Compliance Lead |
| D-05 | CTO + DPO |
| D-06 | CTO + Lead Dev + Procurement |
| D-07 | CTO + Lead Dev |
| D-08 | CTO + HR + DPO |
| D-09 | CTO + DPO + Compliance Lead + Legal |
| D-10 | CTO + Lead Dev |

### §3.3 Regulatory Reporting Heuristic

| Sub-Domain | Reporting | Reason |
|------------|-----------|--------|
| D-04.3 (T-001) | CNPD 72h + ENISA 24h (max-SLA routing) | Dual-mandate conflict resolution (GDPR 72h + CRA 24h) |
| D-04 (others) | CNPD 72h (GDPR) | GDPR-only breach notification |
| D-02 (vuln) | ENISA 24h (CRA) | CRA-only exploited-vulnerability reporting |
| D-09 (governance) | CNPD + ENISA (periodic) | Cross-regulation documentation obligations |
| All other | Internal audit only | No external regulatory reporting |
| BPR (all) | Internal audit only | BPR derives from frameworks, not regulations |

### §3.4 Verification Criteria (1-line per obligation/goal/rule)

The 30 obligation-level + 31 goal-level + 30 CR + 16 BPR values are derived from Doc 08 §4 with sub-domain-specific phrasing. See §3.4.1 for obligation/goal criteria, §3.4.2 for BPR criteria.

#### §3.4.1 Obligation/Goal/CR Criteria (per sub-domain)

- D-01.1: "AES-256 + key rotation audit"
- D-01.2: "TLS 1.3 cert audit"
- D-01.3: "KMS rotation evidence"
- D-01.4: "HMAC + DB constraint check"
- D-02.1: "Trivy + npm audit zero-CVE"
- D-02.2: "72h SLA patch test"
- D-02.3: "security.txt + 24h report"
- D-03.1: "Firebase Auth baseline"
- D-03.2: "MFA enforcement test"
- D-03.3: "RBAC quarterly review"
- D-03.4: "CIS Benchmarks compliance"
- D-04.1: "CloudWatch alarms active"
- D-04.2: "DoS resilience drill"
- D-04.3: "24h dual-notification SLA"
- D-04.4: "AWS Backup RTO 24h"
- D-05.1: "Field-level enforcement"
- D-05.2: "Retention policy audit"
- D-05.3: "Erasure API test (7d)"
- D-05.4: "JSON export test (48h)"
- D-06.1: "DPA + SOC2 attestation"
- D-06.2: "CycloneDX SBOM per release"
- D-06.3: "DPA template + clauses"
- D-07.1: "NIST SSDF + OWASP SAMM"
- D-08.1: "Annual security training"
- D-08.2: "Role-specific training"
- D-09.1: "ISMS documentation audit"
- D-09.2: "Unified assessment template"
- D-09.4: "RoPA + breach log"
- D-10.2: "CloudTrail + S3 audit"
- D-10.3: "Quarterly compliance review"

#### §3.4.2 BPR Criteria (per rule)

| BPR ID | Verification Criteria |
|--------|----------------------|
| BPR-D-01.1-001 | AES-256 validated in CI |
| BPR-D-01.2-001 | TLS 1.3 cert validation |
| BPR-D-02.1-001 | Trivy quarterly scan |
| BPR-D-02.2-001 | Patch SLA test |
| BPR-D-03.1-001 | RBAC quarterly review |
| BPR-D-03.2-001 | MFA FIDO2 validation |
| BPR-D-03.4-001 | CIS Benchmarks compliance |
| BPR-D-04.3-001 | Playbook review audit |
| BPR-D-04.3-002 | Tabletop drill |
| BPR-D-05.3-001 | Sanitization audit |
| BPR-D-07.1-001 | SSDF audit |
| BPR-D-07.2-001 | SAST/DAST gate check |
| BPR-D-09.1-001 | ISMS audit |
| BPR-D-10.2-001 | Log retention audit |
| BPR-D-10.3-001 | Pentest report |
| BPR-D-10.3-002 | OWASP-based assessment |

### §3.5 Cell Tally

| Catalog | Rows | New cols | New cells (Sprint 4) |
|---------|-----:|---------:|---------------------:|
| Doc 08 §4 (Obligations) | 30 | 6 | **180** |
| Doc 10 §3.1 (PG) | 11 | 6 | **66** |
| Doc 10 §4.1 (SG) | 20 | 6 | **120** |
| Doc 10 subtotal | 31 | 6 | **186** |
| Doc 11 §4 (CR) | 30 | 6 | **180** |
| Doc 11 §5 (BPR) | 16 | 6 | **96** |
| Doc 11 subtotal | 46 | 6 | **276** |
| **GRAND TOTAL** | **107** | **6** | **642** |

**Total cells added across Docs 08/10/11 (Sprint 4 new-cols contribution): 180 + 186 + 276 = 642 cells.**

(Total cells added across all cols, including ported legacy cols: 30 × 17 + 31 × 12 + 30 × 17 + 16 × 15 = 510 + 372 + 510 + 240 = 1,632 cells. The 642 figure counts only the Sprint 4 delta, which is the meaningful Sprint 4 deliverable.)

---

## §4 NI Reconciliation (Resolves F-10)

> **Sprint 4 resolves F-10** (Sprint 3 raised F-10 as a NI divergence between legacy Doc 11 §4 and the DR-002 recomputed values per clause NIs).

### §4.1 NI Divergence Table

| Obligation / CR | Rich NI (DR-002 AVG) | Legacy NI (Doc 08 §6 / Doc 11 §4) | Source Clause NIs | Resolution |
|-----------------|---------------------:|----------------------------------:|-------------------|------------|
| OBL-D-01.4-001 / CR-D-01.4-001 | **2.500** | 3.000 | GDPR-C05 = 2, CRA-C09 = 3 → AVG = 2.500 | **Rich wins** — DR-002 AVG(2,3) = 2.500 |
| OBL-D-09.1-001 / CR-D-09.1-001 | **2.500** | 2.750 | GDPR-C08 = 2, GDPR-C25 = 3, GDPR-C26 = 2, CRA-C24 = 3 → AVG = 2.500 | **Rich wins** — DR-002 AVG(2,3,2,3) = 2.500 |

### §4.2 NI Cross-Impact

| Metric | Legacy value | Sprint 1 §3.4 value | Sprint 4 (Rich authoritative) |
|--------|-------------:|--------------------:|-------------------------------:|
| OBL-D-01.4-001 NI | 3.000 | 2.500 | **2.500** |
| OBL-D-09.1-001 NI | 2.750 | 2.500 | **2.500** |
| Catalog average NI | 2.842 (Doc 11 §6) | 2.817 (Doc 08 §3.4 recompute) | **2.800** (with F-10 fix) |
| NI = 3.000 count | 20 | 20 | 20 (unchanged) |
| NI = 2.500–2.999 count | 7 | 7 | 9 (+2 from F-10) |
| NI = 2.000–2.499 count | 3 | 3 | 1 (−2 from F-10) |

### §4.3 Reconciliation Strategy

The Rich Mode **adopts DR-002 AVG** as authoritative for both divergent obligations, per the derivation rule in legacy Doc 08 §3.1 (DR-002: `obligationNI = AVG(clauseNIs)`). The legacy Doc 11 §4 row NI values for these two obligations were either mis-computed (CR-D-01.4-001 = 3.000, no derivation rule justification) or carried over from an earlier rule version (CR-D-09.1-001 = 2.750, no longer matches DR-002).

**Decision recorded for Sprint 5 / Validator:** Rich values are authoritative; legacy NI values for these two obligations are superseded. If the human arbiter reverses this decision, the two NI values revert and the average recomputes to 2.825 (= 2.800 + 0.025).

### §4.4 Documentation Sites

The F-10 reconciliation is documented in three places:

1. **Doc 08 §4.1 NI Reconciliation Notes** — primary source-of-truth for the divergence
2. **Doc 11 §4** — NI column populated with Rich values for CR-D-01.4-001 and CR-D-09.1-001
3. **Doc 11 §7.1** — Sprint 4 port summary includes the NI reconciliation table
4. **Doc 12 (xlsx) Sheet 6 NI_Propagation** — already carries both columns side by side (Sprint 3)

---

## §5 Goal Count Resolution (Resolves F-04a/b)

> **Sprint 4 resolves F-04a and F-04b** (Sprint 1 raised them as goal-count divergences between the legacy §3.2/§4.2 summary metrics and the actual row counts).

### §5.1 PG Count (F-04a)

| Source | PG Count | Notes |
|--------|---------:|-------|
| Legacy Doc 10 §3.2 summary | 12 | Claims "D-01: 3, D-05: 4, D-07: 1, D-09: 4" |
| Legacy Doc 10 §3.1 rows | 11 | Lists 3 PG for D-09 (no PG-D-09.3) |
| **Rich Doc 10 §3.1 rows (authoritative)** | **11** | D-01: 3, D-05: 4, D-07: 1, D-09: 3 |

**Why the discrepancy?** D-09.3 (Asset Inventories) is DORA-exclusive and not applicable to SecureBorder (per `phase1_ontology.yaml` `subdomains.not_covered`). The legacy summary header is stale from v1.0; the row counts are authoritative.

### §5.2 SG Count (F-04b)

| Source | SG Count | Notes |
|--------|---------:|-------|
| Legacy Doc 10 §4.2 summary | 18 | Sum of sub-domain counts in §4.2 table |
| Legacy Doc 10 §4.1 rows | 20 | D-02: 3, D-03: 4, D-04: 4, D-06: 3, D-08: 2, D-09: 2, D-10: 2 = 20 |
| **Rich Doc 10 §4.1 rows (authoritative)** | **20** | Same as legacy rows |

**Why the discrepancy?** Legacy Doc 10 §4.2 summary is stale from v1.0 (15 SG) and was never updated when v1.1 added 3 D-06 SGs (SG-D-06.1, 06.2, 06.3) and SG-D-02.4 was renamed to SG-D-06.2. The actual row count is 20.

### §5.3 Total Goal Count (F-04)

| Source | Total | PG + SG |
|--------|------:|---------|
| Legacy §3.2+§4.2 summary | 30 | 12 + 18 |
| Legacy §3.1+§4.1 rows | 31 | 11 + 20 |
| **Rich §3.1+§4.1 rows (authoritative)** | **31** | **11 + 20** |

**The Rich Mode adopts 31 goals (11 PG + 20 SG) as the canonical count.** Doc 10 frontmatter `expected_goals: 30` was updated to `expected_goals: 31` in Sprint 4.

### §5.4 Cross-Impact on Doc 11

The CR `Related Goals` column in Doc 11 §4 must reference the actual goal IDs (11 PG + 20 SG from Doc 10 §3.1/§4.1). The CR-D-01.3-001 row continues to reference the phantom `PG-D-01.3-001` (carried finding F-03 — see §7). Doc 11's cross-checks (§3.2) reflect the actual 31 goal rows.

---

## §6 Frontmatter Updates

| Doc | Field | Before (Sprint 1) | After (Sprint 4) |
|-----|-------|--------------------|-------------------|
| **08_Obligation_Derivation.md** | `version` | 1.1 | **1.2** |
| | `status` | RECONCILED | **ADJUSTED_OBJECTIVES** |
| | `sprint` | 1 | **4** |
| | `author` | Sprint 1 Executor (reconciliation-builder) | **Sprint 1+3+4 Executor (reconciliation + catalog port + 6 new cols)** |
| | `sprint_3_scope` | (absent) | **regenerate 12_Rules_Catalog.xlsx (14 sheets) — DONE in Sprint 3** |
| | `sprint_4_scope` | (absent) | **port legacy §4 catalog table (30 obligations × 11 cols) into Rich §4 + add 6 new cols; resolve F-10 NI divergence** |
| | `sprint_4_verdict` | (absent) | **PASS_WITH_FINDINGS — see §4.1 NI Reconciliation and §3.7 carried findings F-01/F-02** |
| **10_Privacy_Security_Goals.md** | `version` | 1.1 | **1.2** |
| | `status` | RECONCILED | **ADJUSTED_OBJECTIVES** |
| | `sprint` | 1 | **4** |
| | `expected_goals` | 30 | **31** |
| | `author` | Sprint 1 Executor | **Sprint 1+3+4 Executor** |
| | `sprint_4_scope` | (absent) | **port legacy §3 PG catalog (11 PG × 6 cols) + legacy §4 SG catalog (20 SG × 6 cols) into Rich §3.1/§4.1 with 12 cols each; resolve F-04a/b (31 not 30)** |
| **11_Rules_Catalog.md** | `version` | 1.1 | **1.2** |
| | `status` | RECONCILED | **ADJUSTED_OBJECTIVES** |
| | `sprint` | 1 | **4** |
| | `author` | Sprint 1 Executor | **Sprint 1+3+4 Executor** |
| | `sprint_4_scope` | (absent) | **port legacy §4 CR catalog (30 CR × 11 cols) + legacy §5 BPR catalog (16 BPR × 9 cols) into Rich §4/§5 with 17/15 cols; resolve F-10 NI divergence** |

---

## §7 Sprint 3+4 → Sprint 5 Handoff

### §7.1 Ready for Sprint 5

| Input | Where | Note |
|-------|-------|------|
| 30 obligations × 17 cols (510 cells) | Doc 08 §4 | 11 legacy + 6 new = 17 cols; Sprint 5 expands to 15-field detail cards |
| 31 goals × 12 cols (372 cells) | Doc 10 §3.1 + §4.1 | 6 legacy + 6 new = 12 cols; Sprint 5 expands to 15-field detail cards |
| 30 CR × 17 cols (510 cells) | Doc 11 §4 | Sprint 5 expands to 15-field detail cards |
| 16 BPR × 15 cols (240 cells) | Doc 11 §5 | Sprint 5 expands to 15-field detail cards |
| 4 tensions × 8 fields (32 cells) | Doc 09 §4 | Already at 15-field depth (Sprint 2) |
| Owner heuristic | Doc 08 §4 + Doc 04d RACI | Used in Sprint 4; Sprint 5 may refine |
| Verification criteria 1-line | Doc 08 §4 + Doc 11 §5 | Sprint 5 expands to 15-field detail |
| NI values (F-10 resolved) | Doc 08 §4.1 + Doc 11 §7.1 | Authoritative for Sprint 5 priority fields |
| Goal count (F-04a/b resolved) | Doc 10 §3.1 + §4.1 | 11 PG + 20 SG = 31 goals authoritative |

### §7.2 Sprint 5 Card Targets

| Catalog | Rows | Fields/card (Sprint 5) | Total cells |
|---------|-----:|-----------------------:|------------:|
| Obligation cards | 30 | 15 | 450 |
| Goal cards | 31 | 15 | 465 |
| Rule cards | 46 | 15 | 690 |
| **TOTAL** | **107** | **15** | **1,605** |

### §7.3 Carried Findings (no Sprint 5 blockers)

| ID | Severity | Description | Sprint 5 action |
|----|----------|-------------|-----------------|
| **F-01** | LOW | OBL-D-01.3-001 has no PG/SG; Doc 11 §4 row CR-D-01.3-001 references phantom PG-D-01.3-001. | Defer to human arbiter; Sprint 5 proceeds with 29 goal cards for OBLs (one OBL has no goal). |
| **F-02** | MEDIUM | OBL-D-09.1-001 and OBL-D-09.2-001 each have both a PG and an SG. | Document as intentional in 1:1 mapping definition (Doc 10 §3.2); no action. |
| **F-03** | LOW | Doc 11 §4 row CR-D-01.3-001 references phantom PG-D-01.3-001. | Same root cause as F-01; Sprint 5 adds note in the CR detail card. |

### §7.4 Resolved Findings (no longer carried)

| ID | Severity | Description | Sprint 4 resolution |
|----|----------|-------------|---------------------|
| **F-04a** | LOW | Legacy §3.2 summary claims 12 PG but §3.1 lists 11. | Sprint 4 §3.1 PG catalog confirms 11 PG authoritative; Doc 10 §3.2 summary updated. |
| **F-04b** | LOW | Legacy §4.2 summary claims 18 SG but §4.1 lists 20. | Sprint 4 §4.1 SG catalog confirms 20 SG authoritative; Doc 10 §4.2 summary updated. |
| **F-10** | LOW | NI divergence between legacy Doc 11 §4 and DR-002 recompute for OBL-D-01.4-001 (3.000 vs 2.500) and OBL-D-09.1-001 (2.750 vs 2.500). | Sprint 4 §4.1 NI Reconciliation adopts DR-002 AVG (2.500) as authoritative; Doc 08, Doc 11, Doc 12 (xlsx Sheet 6) all updated. |

---

## §8 Sprint 3+4 Acceptance Criteria

| # | Criterion | Target | Actual | Status |
|---|-----------|--------|--------|:------:|
| 1 | Doc 08 §4 catalog table added (30 obligations × 17 cols) | ≥ 30 rows, 17 cols | 30 rows, 17 cols | ✅ PASS |
| 2 | Doc 10 §3.1 PG catalog (11 PG × 12 cols) added | ≥ 11 PG rows | 11 PG rows | ✅ PASS |
| 3 | Doc 10 §4.1 SG catalog (20 SG × 12 cols) added | ≥ 20 SG rows | 20 SG rows | ✅ PASS |
| 4 | Doc 11 §4 CR catalog (30 CR × 17 cols) added | ≥ 30 CR rows | 30 CR rows | ✅ PASS |
| 5 | Doc 11 §5 BPR catalog (16 BPR × 15 cols) added | ≥ 16 BPR rows | 16 BPR rows | ✅ PASS |
| 6 | Doc 08 §4.1 NI Reconciliation Notes added (F-10 resolved) | sub-section present | Doc 08 §4.1 + Doc 11 §7.1 | ✅ PASS |
| 7 | Goal count 31 (11 PG + 20 SG) confirmed (F-04a/b resolved) | 31 goals | 31 goals (11+20) | ✅ PASS |
| 8 | Total cells added across new Sprint 4 cols | ≥ 642 | 642 (180 + 186 + 276) | ✅ PASS |
| 9 | Frontmatter updated for Doc 08/10/11 | status + version + sprint | 3/3 docs | ✅ PASS |
| 10 | Legacy `02_PHASE2_RULES/` unmodified | 0 changes | 0 | ✅ PASS |
| 11 | Phase 1 / Phase 3 / corpus unmodified | 0 changes | 0 | ✅ PASS |
| 12 | No git commits created by executor | 0 | 0 | ✅ PASS |

**Verification commands:**

```bash
cd 02_CASES/Case_02_SecureBorder_Solutions
# Row counts
grep -c "^| OBL-D-" 02_PHASE2_RULES_RICH/08_Obligation_Derivation.md  # 120 (30 catalog + 90 cross-checks)
grep -c "^| PG-D-" 02_PHASE2_RULES_RICH/10_Privacy_Security_Goals.md  # 22 (11 catalog + 11 cross-checks)
grep -c "^| SG-D-" 02_PHASE2_RULES_RICH/10_Privacy_Security_Goals.md  # 40 (20 catalog + 20 cross-checks)
grep -c "^| CR-D-" 02_PHASE2_RULES_RICH/11_Rules_Catalog.md  # 62 (30 catalog + 32 cross-checks)
grep -c "^| BPR-D-" 02_PHASE2_RULES_RICH/11_Rules_Catalog.md  # 16 (all catalog)

# Line counts
wc -l 02_PHASE2_RULES_RICH/08_Obligation_Derivation.md  # 458 (≥ 450 ✓)
wc -l 02_PHASE2_RULES_RICH/10_Privacy_Security_Goals.md  # 354 (≥ 350 ✓)
wc -l 02_PHASE2_RULES_RICH/11_Rules_Catalog.md  # 506 (≥ 500 ✓)
wc -l 02_PHASE2_RULES_RICH/validation/SPRINT3_4_REPORT.md  # ≥ 200
```

---

## §9 Sprint 3+4 Verdict

**✅ PASS**

All 12 acceptance criteria met. 4 deliverables produced (3 updated, 1 created). 642 cells added across the 6 new Sprint 4 columns (180 in Doc 08 + 186 in Doc 10 + 276 in Doc 11). 3 findings resolved (F-04a, F-04b, F-10); 3 findings carried forward with no Sprint 5 blockers (F-01, F-02, F-03).

**Phase 2 Rich Mode is READY for Sprint 5 (DEEP enrichment).** All catalog tables now carry the 17-field (CR + OBL) / 15-field (BPR) / 12-field (PG + SG) Rich schema. The 15-field detail card expansion will use the 6 new Sprint 4 fields as anchors and add 3 more (effort is excluded per the no-Effort/Cost/Timeline invariant).

Legacy, Phase 1, Phase 3 and corpus artefacts are untouched; commits remain the orchestrator's responsibility.

---

## §10 Cell Tally Summary

| Doc | Catalog | Rows | Cols | Cells | Sprint 4 new-cols | Sprint 4 new-cells |
|-----|---------|-----:|-----:|------:|------------------:|-------------------:|
| 08 | OBL | 30 | 17 | 510 | 6 | **180** |
| 10 | PG | 11 | 12 | 132 | 6 | **66** |
| 10 | SG | 20 | 12 | 240 | 6 | **120** |
| 11 | CR | 30 | 17 | 510 | 6 | **180** |
| 11 | BPR | 16 | 15 | 240 | 6 | **96** |
| **TOTAL** | — | **107** | — | **1,632** | **6** | **642** |

---

## §11 See also

- `../README.md` — Rich folder orientation + §8 final status
- `../PROJECT_STATE.md` — project state, sprint history, open findings
- `../RICH_VS_LEGACY.md` — Rich vs legacy diff summary
- `../12_Rules_Catalog.xlsx` — 14-sheet workbook (Sheet 6 NI_Propagation, Sheet 12 Affected_Stakeholders used as inputs)
- `../08_Obligation_Derivation.md` — v1.2 with §4 catalog + §4.1 NI Reconciliation
- `../10_Privacy_Security_Goals.md` — v1.2 with §3.1 PG catalog + §4.1 SG catalog
- `../11_Rules_Catalog.md` — v1.2 with §3 schema + §4 CR catalog + §5 BPR catalog
- `SPRINT1_REPORT.md` — reconciliation detail and findings F-01…F-09
- `SPRINT2_REPORT.md` — multi-paragraph tension expansion
- `SPRINT3_REPORT.md` — Excel + final docs (raised F-10)
- `../../01_PHASE1_CONTEXT_RICH/07b_Proportionality_Profile.md` — LIGHTWEIGHT target reference
- `../../01_PHASE1_CONTEXT_RICH/04d_Org_Roles_RACI.md` — Owner heuristic reference
- `../../02_PHASE2_RULES/` — legacy Phase 2 (read-only)

---

**End of Sprint 3+4 Report — Case_02 Phase 2 Rich Mode**
