# Case_03 Traceability Audit

**Generated:** 2026-08-13T12:22:46
**Case:** Case_03_OmniBank_Financial (OmniBank Financial Systems, MAX tier, 5 regulations)
**Scope:** Phase 1+2 — HSO → PG/SG (P1) → OBL → PG/SG (P2) → CR/BPR
**Mode:** STRICT (zero unknown orphans required)
**Generator:** `scripts/audit_case03_traceability.py`

> Parsing is section-scoped and table-row-anchored: an ID counts as CANONICAL only when it opens a catalog-table row inside its defining section (07c §2/§3, Doc 08 §4, Doc 10 §3/§4, Doc 11 §4/§5). Prose mentions, reconciliation tables, version history, and DEPRECATED appendices are not counted as definitions.

> **Case_03 ID conventions** (post-corr-010: PG/SG → AG-D- migration applied):
>
> - Phase 1: `AG-D-XX.Y-001` (was corr-007 PG-D slot 001) and `AG-D-XX.Y-002` (was corr-007 SG-D slot 002). 07c §2/§3 contains 38 + 38 = 76 AG IDs (all sub-domains active).
> - Phase 2: `OBL-D-XX.Y-001` (38), `AG-D-XX.Y-001`/`AG-D-XX.Y-002` (12+26=38 unique, post-corr-010 migration), `CR-D-XX.Y-001` (38), `BPR-D-XX.Y-NNN` (40 incl. 4 D-12.x AI-specific).
> - Doc 10 was migrated from PG/SG namespace to AG-D- (corr-010). PO/SO split remains future work (corr-012 for Case_03).

## 1. Summary

| Layer | Definition site | Canonical IDs | Sub-domains |
|-------|-----------------|--------------:|------------:|
| HSO (Phase 1 corpus, referenced) | 07c §2/§3 *Generic Sub-SO* column | 122 | 38 |
| PG — Phase 1 (07c) | 07c §2 (Adjusted Privacy Goals) | 38 | 38 |
| SG — Phase 1 (07c) | 07c §3 (Adjusted Security Goals) | 38 | 38 |
| OBL | Doc 08 §4 | 38 | 38 |
| PG — Phase 2 (Doc 10) | Doc 10 §3 | 12 | 12 |
| SG — Phase 2 (Doc 10) | Doc 10 §4 | 26 | 26 |
| **PG/SG — Phase 2 total** | Doc 10 (unique IDs) | **38** | 38 |
| CR | Doc 11 §4 | 38 | 38 |
| BPR | Doc 11 §5 (36 D-XX.Y + 4 D-12.x AI-specific) | 40 | 40 |

**Edge counts:** HSO→PG/SG(P1) 43 · OBL→PG/SG(P2) 38 · PG/SG(P2)→CR 83 · CR↔OBL 38 (1:1 implicit identity)

## 2. Coverage Matrix (sub-domain × layer)

Legend: ✓ = at least one canonical ID, — = none. **Phase 1** columns (PG_p1, SG_p1) show 07c §2/§3 presence. **Phase 2** columns (PG_p2, SG_p2, CR, BPR) show Doc 10/11 catalog presence. [SOLE] sub-domains have only one Phase 2 goal type (Doc 11 §7).

| Sub-Domain | PG_p1 | SG_p1 | OBL | PG_p2 | SG_p2 | CR | BPR | Notes |
|------------|:-----:|:-----:|:---:|:-----:|:-----:|:--:|:---:|-------|
| D-01.1 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | PG-only in Doc 10 |
| D-01.2 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | PG-only in Doc 10 |
| D-01.3 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | PG-only in Doc 10 |
| D-01.4 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | PG-only in Doc 10 |
| D-02.1 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-02.2 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-02.3 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | SG-only in Doc 10 |
| D-02.4 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-03.1 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-03.2 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-03.3 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-03.4 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | [SOLE] per Doc 11 §7, SG-only in Doc 10 |
| D-04.1 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-04.2 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-04.3 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-04.4 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-05.1 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | PG-only in Doc 10 |
| D-05.2 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | PG-only in Doc 10 |
| D-05.3 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | PG-only in Doc 10 |
| D-05.4 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | [SOLE] per Doc 11 §7, PG-only in Doc 10 |
| D-06.1 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-06.2 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | [SOLE] per Doc 11 §7, SG-only in Doc 10 |
| D-06.3 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-06.4 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-07.1 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | PG-only in Doc 10 |
| D-07.2 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-07.3 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-07.4 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-08.1 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-08.2 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-08.3 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-09.1 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | PG-only in Doc 10 |
| D-09.2 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | PG-only in Doc 10 |
| D-09.3 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | SG-only in Doc 10 |
| D-09.4 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | PG-only in Doc 10 |
| D-10.1 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-10.2 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |
| D-10.3 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | SG-only in Doc 10 |

## 3. Forward Orphans (no downstream edge)

### 3.1 Known (documented exceptions)

| Edge | ID | Reason |
|------|----|--------|
| PG/SG→CR | `AG-D-01.2-001` | BY DESIGN — Phase 2 goal `AG-D-01.2-001` discharged via same-sub-domain CR (CR-D-01.2-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| PG/SG→CR | `AG-D-05.3-001` | BY DESIGN — Phase 2 goal `AG-D-05.3-001` discharged via same-sub-domain CR (CR-D-05.3-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| PG/SG→CR | `AG-D-07.1-001` | BY DESIGN — Phase 2 goal `AG-D-07.1-001` discharged via same-sub-domain CR (CR-D-07.1-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| PG/SG→CR | `AG-D-09.2-001` | BY DESIGN — Phase 2 goal `AG-D-09.2-001` discharged via same-sub-domain CR (CR-D-09.2-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| PG/SG→CR | `AG-D-02.2-002` | BY DESIGN — Phase 2 goal `AG-D-02.2-002` discharged via same-sub-domain CR (CR-D-02.2-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| PG/SG→CR | `AG-D-02.3-002` | BY DESIGN — Phase 2 goal `AG-D-02.3-002` discharged via same-sub-domain CR (CR-D-02.3-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| PG/SG→CR | `AG-D-03.2-002` | BY DESIGN — Phase 2 goal `AG-D-03.2-002` discharged via same-sub-domain CR (CR-D-03.2-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| PG/SG→CR | `AG-D-04.3-002` | BY DESIGN — Phase 2 goal `AG-D-04.3-002` discharged via same-sub-domain CR (CR-D-04.3-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| PG/SG→CR | `AG-D-06.2-002` | SOLE sub-domain — OBL-D-06.2-001 has only this Phase 2 goal (SOLE: CRA per Doc 08 §10 + Doc 11 §7 [SOLE: CRA] — SBOM is sole CRA authority. Has AG-D-06.2-002 (Doc 10 §4.4) but no AG-D-06.2-001 (Doc 10 §3).); CR-D-06.2-001 discharges the same sub-domain's obligation (1:1 implicit) |
| PG/SG→CR | `AG-D-06.3-002` | BY DESIGN — Phase 2 goal `AG-D-06.3-002` discharged via same-sub-domain CR (CR-D-06.3-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| PG/SG→CR | `AG-D-07.4-002` | BY DESIGN — Phase 2 goal `AG-D-07.4-002` discharged via same-sub-domain CR (CR-D-07.4-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| PG/SG→CR | `AG-D-08.3-002` | BY DESIGN — Phase 2 goal `AG-D-08.3-002` discharged via same-sub-domain CR (CR-D-08.3-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| PG/SG→CR | `AG-D-10.2-002` | BY DESIGN — Phase 2 goal `AG-D-10.2-002` discharged via same-sub-domain CR (CR-D-10.2-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| PG/SG→CR | `AG-D-10.3-002` | BY DESIGN — Phase 2 goal `AG-D-10.3-002` discharged via same-sub-domain CR (CR-D-10.3-001) per Doc 11 §10 traceability matrix. Doc 11 §4 'Related Goals' column contains CROSS-REFERENCES to other goals only, not the primary goal for the same sub-domain. |
| BPR upstream | all 40 BPR (`BPR-D-01.1-001` … `BPR-D-12.4-001`) | BY DESIGN — BPR derive from external frameworks (NIST CSF/PF/AI RMF, ISO 27001/42001, OWASP, CIS, MITRE ATLAS, IEEE 7000), not from OBL/PG/SG (Doc 11 §5 preambles). 40 BPR total (incl. 4 D-12.x AI-specific cross-domain rules). |

### 3.2 Unknown (potential defects)

(none)

## 4. Backward Orphans (references to non-canonical IDs)

### 4.1 Known (documented exceptions)

(none — HSO corpus IDs and `NOT_ADDRESSED` sentinels are excluded)

### 4.2 Unknown (potential defects)

(none)

## 5. Sole-Authority Sub-Domains ([SOLE] per Doc 08 §10 + Doc 11 §7)

Doc 08 §10 + Doc 11 §7 explicitly mark three sub-domains as [SOLE] (single-regulation coverage). These are TRUE sole-authority exceptions — only one regulation applies, so only one goal type (slot 001 or slot 002) is generated in Doc 10. **Note:** Most other sub-domains also have slot-001-only or slot-002-only Phase 2 coverage, but this is the post-corr-010 ID split (privacy sub-domains → slot 001; security sub-domains → slot 002) — see §5a below.

| Sub-Domain | Sole Authority | Reason |
|------------|----------------|--------|
| D-03.4 | CRA only | SOLE: CRA per Doc 08 §10 + Doc 11 §7 [SOLE: CRA] — secure default configuration is sole CRA authority. Has AG-D-03.4-002 (Doc 10 §4.2) but no AG-D-03.4-001 (Doc 10 §3). |
| D-05.4 | GDPR only | SOLE: GDPR per Doc 08 §10 + Doc 11 §7 [SOLE: GDPR] — data portability is sole GDPR authority. Has AG-D-05.4-001 (Doc 10 §3.2) but no AG-D-05.4-002 (Doc 10 §4). |
| D-06.2 | CRA only | SOLE: CRA per Doc 08 §10 + Doc 11 §7 [SOLE: CRA] — SBOM is sole CRA authority. Has AG-D-06.2-002 (Doc 10 §4.4) but no AG-D-06.2-001 (Doc 10 §3). |

### 5a. corr-007 PG/SG Split (informational)

Case_03 uses the AG-D- ID namespace (post-corr-010 migration, was the legacy PG/SG corr-007 namespace), not the corr-008 PO/SO split. As a result, privacy sub-domains (D-01, D-05, D-07, D-09) only carry AG-D-XX.Y-001 (slot 001, ex-PG) in Doc 10, and security sub-domains (D-02, D-03, D-04, D-06, D-08, D-10) only carry AG-D-XX.Y-002 (slot 002, ex-SG) in Doc 10. This is the EXPECTED post-corr-010 pattern — NOT a defect.

| Coverage | Count | Sub-Domains |
|----------|------:|-------------|
| PG+SG (both) | 0 | — |
| PG only (privacy sub-domains, corr-007) | 12 | D-01.1, D-01.2, D-01.3, D-01.4, D-05.1, D-05.2, D-05.3, D-05.4, D-07.1, D-09.1, D-09.2, D-09.4 |
| SG only (security sub-domains, corr-007) | 26 | D-02.1, D-02.2, D-02.3, D-02.4, D-03.1, D-03.2, D-03.3, D-03.4, D-04.1, D-04.2, D-04.3, D-04.4, D-06.1, D-06.2, D-06.3, D-06.4, D-07.2, D-07.3, D-07.4, D-08.1, D-08.2, D-08.3, D-09.3, D-10.1, D-10.2, D-10.3 |

## 6. Internal Doc Inconsistencies (INFO)

Case_03 has TWO internal metadata inconsistencies that this audit detected. Both are reporting discrepancies (metadata vs catalog), NOT data integrity bugs.

| Source | Claimed | Actual | Note |
|--------|--------:|-------:|------|
| Doc 10 §1/§2 metadata | 33 goals (11 PG + 22 SG) | 38 unique goals (12 PG + 26 SG) | Metadata count is wrong — actual catalog has 38 unique goals. Doc 10b 'Goal Count Reconciliation' flags this as F-01 carried legacy. |
| Doc 11 §2 metadata + §6 dashboard | 25 BPR | 40 BPR (incl. 4 D-12.x AI-specific cross-domain) | Dashboard count is wrong — actual §5 catalog has 40 BPR. Doc 13 §3 confirms 40 BPR; Doc 11 internal inconsistency. |

## 7. PG/SG (Phase 1) → OBL Coverage (inferred, INFO)

**Finding F-A1 (MEDIUM, informational):** Doc 08 references **0 AG IDs** (expected: 0 — confirmed by regex). The AG (P1) → OBL edge is therefore not machine-verifiable; it can only be inferred at sub-domain granularity (Phase 1 AG-D-XX.Y-001 ↔ Phase 2 OBL-D-XX.Y-001 by sub-domain XX.Y). Doc 10 §3/§4 preserves the AG-D- namespace explicitly — every Phase 1 AG with a matching sub-domain maps to the corresponding OBL via sub-domain. This is reported as INFO and is **not** a strict-mode gate.

### 7.1 PG/SG (P1) sub-domains with no OBL — documented status

(none — all 38 PG/SG (P1) sub-domains have a matching OBL)

### 7.2 PG/SG (P1) sub-domains with no OBL — undocumented (flagged for human review)

(none)

## 8. Findings Summary

| Severity | Count | Description |
|----------|------:|-------------|
| CRITICAL | 0 | (none) |
| HIGH | 0 | (none) |
| MEDIUM (INFO) | 3 | F-A1 (no PG/SG IDs in Doc 08) + 2 doc inconsistencies (Doc 10 §1/§2 33-vs-38, Doc 11 §2/§6 25-vs-40 BPR) + 0 undocumented PG/SG (P1) sub-domain gap(s) — §6, §7 |
| LOW (KNOWN) | 15 | 3× [SOLE] sub-domains (D-03.4/D-05.4/D-06.2), 14× Phase 2 goals discharged via same-sub-domain CR (per Doc 11 §10; §4 Related Goals col has cross-references only), 40× BPR framework-derived (incl. 4 BPR-D-12.x AI-specific) — §3.1, §5 |
| UNKNOWN | 0 | Forward 0 + backward 0 (must be 0 in strict mode) |

**Strict-mode verdict: PASS** — 0 unknown orphan(s).

## 9. Cross-Check with Manual Reconciliation Tables

| Manual table | Documented | Script-detected | Match |
|--------------|-----------:|----------------:|:-----:|
| Doc 08 §9 OBL count (all 38 sub-domains active) | 38 | 38 | ✓ |
| Doc 08 §9 OBL with ≥1 Phase 2 PG/SG | 38 | 38 | ✓ |
| Doc 08 §9 OBL → CR (1:1 implicit, all) | 38 | 38 | ✓ |
| Doc 08 §9 OBL with ≥1 PG (Phase 2) | 12 | 12 | ✓ |
| Doc 08 §9 OBL with ≥1 SG (Phase 2) | 26 | 26 | ✓ |
| Doc 10 §3 PG total (Phase 2) | 12 | 12 | ✓ |
| Doc 10 §4 SG total (Phase 2) | 26 | 26 | ✓ |
| Doc 10 §3/§4 unique goal total (Phase 2) | 38 | 38 | ✓ |
| Doc 11 §4 CR total | 38 | 38 | ✓ |
| Doc 11 §5 BPR total (§5 catalog — 36 D-XX.Y + 4 D-12.x) | 40 | 40 | ✓ |
| Doc 11 §5 BPR-D-12.x AI-specific cross-domain | 4 | 4 | ✓ |
| Doc 11 §7 [SOLE] sub-domains (D-03.4 + D-05.4 + D-06.2) | 3 | 3 | ✓ |
| corr-007 PG-only sub-domains (privacy: D-01/D-05/D-07/D-09) | 12 | 12 | ✓ |
| corr-007 SG-only sub-domains (security: D-02/D-03/D-04/D-06/D-08/D-10) | 26 | 26 | ✓ |
| corr-007 PG+SG both (none — split by sub-domain cluster) | 0 | 0 | ✓ |
| Doc 08 §10 [SOLE] GDPR sub-domains (D-05.4) | 1 | 1 | ✓ |
| Doc 08 §10 [SOLE] CRA sub-domains (D-03.4 + D-06.2) | 2 | 2 | ✓ |
| 07c §2 PG total (Phase 1, all 38 active) | 38 | 38 | ✓ |
| 07c §3 SG total (Phase 1, all 38 active) | 38 | 38 | ✓ |
| 07c §1/§2/§3 HSO corpus refs (unique) | 122 | 122 | ✓ |
| Doc 10 §1/§2 metadata claim (33) vs actual (38) | 38 | 38 | ✓ |
| Doc 11 §2/§6 dashboard claim (25 BPR) vs actual (40) | 40 | 40 | ✓ |

## 10. Known Exceptions (Reference)

| Code | Severity | Description |
|------|----------|-------------|
| F-A1 | MEDIUM (INFO) | Doc 08 carries no PG/SG IDs; the PG/SG (P1) → OBL edge is inferred by sub-domain only. Raised by this audit. |
| [SOLE] D-03.4 | LOW (BY DESIGN) | CRA sole authority for secure default configuration. Doc 10 §4 has AG-D-03.4-002 but §3 has no AG-D-03.4-001. Doc 08 §10 + Doc 11 §7. |
| [SOLE] D-05.4 | LOW (BY DESIGN) | GDPR sole authority for data portability. Doc 10 §3 has AG-D-05.4-001 but §4 has no AG-D-05.4-002. Doc 08 §10 + Doc 11 §7. |
| [SOLE] D-06.2 | LOW (BY DESIGN) | CRA sole authority for SBOM. Doc 10 §4 has AG-D-06.2-002 but §3 has no AG-D-06.2-001. Doc 08 §10 + Doc 11 §7. |
| sole-PG/SG Phase 2 goal | LOW (BY DESIGN) | Some Phase 2 PG/SG goals are sole-authority (only one of PG or SG present for the sub-domain). CR's Related Goals column references the PRIMARY goal only — secondary sole-authority goals have no CR reference but are discharged via the same sub-domain CR. |
| BPR | — | BPR derive from external frameworks (NIST CSF/PF/AI RMF, ISO 27001/42001, OWASP, CIS, MITRE ATLAS, IEEE 7000), not from OBL/PG/SG. Doc 11 §5 preambles. |
| BPR-D-12.x | — | 4 AI-specific cross-domain BPRs (D-12 sub-domain doesn't exist in canonical taxonomy). Linked to D-02.1, D-02.4, D-08.2, D-10.1 actual sub-domains. |
| F-01 (Doc 10 §1/§2) | LOW (INFO) | Doc 10 §1/§2 metadata claims 33 goals (11 PG + 22 SG) but actual unique catalog has 38 (12 PG + 26 SG). Doc 10b 'Goal Count Reconciliation' flags this. |
| Doc 11 §2/§6 BPR count | LOW (INFO) | Doc 11 §2 metadata + §6 dashboard claim 25 BPR but §5 catalog has 40 BPR (incl. 4 D-12.x). Doc 13 §3 confirms 40 BPR. |
| T-001 (D-04.3) | CRITICAL | 5-reg notification timeline conflict (GDPR 72h, CRA 24h, NIS 2 24h/72h, DORA 24h/72h, AI Act continuous). Resolved via unified 24h workflow. Doc 11 §8.1 + Doc 08 §10. |
| T-002 (D-05.3 ↔ D-10.2) | CRITICAL | GDPR Art. 17 erasure vs AI Act/DORA immutable log retention. Resolved via cryptographic sharding. Doc 11 §8.2 + Doc 08 §10. |
| T-003 (D-09.2) | MEDIUM | GDPR Art. 35 DPIA vs AI Act Art. 27 FRIA trigger mismatch. Resolved via unified DPIA+FRIA single process with dual output. Doc 11 §8.4. |
| T-004 (D-07.1) | LOW | GDPR NI=2 vs CRA NI=3 intensity gap. Resolved via AVG + AI-C MUST override. Doc 11 §8.5 + Doc 13 dr_002_resolution. |

---

*Generated by `scripts/audit_case03_traceability.py` at 2026-08-13T12:22:46. Informational audit — no source document is modified.*
