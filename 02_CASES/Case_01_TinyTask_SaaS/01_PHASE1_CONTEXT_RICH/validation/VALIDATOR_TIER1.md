---
document_id: AEGIS-P1-RICH-VALIDATOR-TIER1
title: Validator Tier 1 — Case_01 Phase 1 Rich
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-10
author: Sprint Validator (tier1-verifier)
sprint_8_note: Fase de Especificação 8 Executor (corr-009 ao-migration historical-context)
status: HISTORICAL
historical_note: Historical report from corr-007 era. Current 07c version is v4.0 with AO ID model (corr-008 supersedes corr-007). Content below preserved verbatim; see `07c_Adjusted_Objectives.md` §9 Version History for the v4.0 AO ID migration entry.
case: Case_01_TinyTask_SaaS
tier: 1 (Completeness + Internal Consistency)
applicable_regs: [GDPR, CRA]
active_subdomains: 37
---

# Validator Tier 1 — Case_01 Phase 1 Rich

> Independent verification of Completeness (C1.1–C1.7) + Internal Consistency (C2.1–C2.6).
> Tier 2/3 criteria DEFERRED to next iteration per user direction.
> Read-only audit; no source files modified.

## §1 Summary

| Tier 1 Criterion | Verdict | Severity |
|------------------|---------|----------|
| C1.1 All 37 SDs have PG+SG | PASS | — |
| C1.2 All 54 clauses in Doc 06 | PASS | — |
| C1.3 All articles cited in Doc 07c exist in corpus | PARTIAL | LOW |
| C1.4 Doc 05 APP flags cover GDPR + CRA | PASS | — |
| C1.5 Doc 04 BG covers BG-01..BG-05 | PASS | — |
| C1.6 Doc 05b has ≥ 5 ambiguity cards (Berry lens R1/R2/R3) | PASS | — |
| C1.7 N/A (no Doc 06b DORA-specific) | PASS | — |
| C2.1 Tier matching Doc 07b §4 vs Doc 07c §6 (Track B) | PASS | — |
| C2.2 Doc 04 BG → Doc 07c PG/SG cross-refs (all 5 BGs) | PASS | — |
| C2.3 Doc 07 tensions implemented in Doc 07b example_controls | PASS | — |
| C2.4 Frontmatter status progression | PARTIAL | LOW |
| C2.5 applicable_regs consistent across all docs | PASS | — |
| C2.6 6 lints PASS | PASS | — |

**Overall Tier 1 verdict:** **CONDITIONAL_PASS** — All 13 criteria functionally PASS or PARTIAL with only LOW-severity gaps (documented corpus coverage gaps for CRA Annex I/Annex VII; missing intermediate `ADJUSTED_OBJECTIVES` frontmatter status). No HIGH-severity gaps; no blocking inconsistencies.

---

## §2 Per-Criterion Detail

### C1.1 — All 37 active sub-domains have ≥ 1 PG + 1 SG

- **Verdict:** PASS
- **Evidence:**
  - `07c_Adjusted_Objectives.md` Appendix A §A.1 — PG table has 37 rows (D-01.1 through D-10.3; no D-08.3) (lines see Appendix A)
  - `07c_Adjusted_Objectives.md` Appendix A §A.2 — SG table has 37 rows (matching set)
  - `07c_Adjusted_Objectives.md` Appendix A §A.1.1 — contains 37 PG detail cards (one per sub-domain)
  - `07c_Adjusted_Objectives.md` Appendix A §A.2.1 — contains 37 SG detail cards (one per sub-domain)
  - `07c_Adjusted_Objectives.md` frontmatter — `detail_cards_count: 74` (37 × 2)
  - `07c_Adjusted_Objectives.md` §8 Validation — "Distribution: 31 LIGHTWEIGHT + 5 MINIMAL + 1 DEFERRED = 37 total"
- **Gap:** NONE. All 37 active sub-domains have exactly 1 PG + 1 SG.
- **Severity:** —

### C1.2 — All 54 clauses (28 GDPR + 26 CRA) in Doc 06 with sub-domain mapping

- **Verdict:** PASS
- **Evidence:**
  - `06_Clause_Mapping_Matrix.md:54-61` — GDPR 28 clauses confirmed (`Total GDPR Clauses | 28`)
  - `06_Clause_Mapping_Matrix.md:68-73` — CRA 26 clauses confirmed (`Total CRA Clauses | 26`)
  - `06_Clause_Mapping_Matrix.md:155-186` — §8.1 lists all 28 GDPR cross-references (GDPR-C01..GDPR-C28) with article + sub-domain mapping
  - `06_Clause_Mapping_Matrix.md:192-219` — §8.2 lists all 26 CRA cross-references (CRA-C01..CRA-C26) with article + sub-domain mapping
  - `06_Clause_Mapping_Matrix.md:225` — "28 GDPR + 26 CRA = 54 clauses" total
  - `phase1_ontology.yaml:512` — `clause_mappings:` block; 54 `- clause_id:` entries counted
- **Gap:** NONE. 28 + 26 = 54 clauses all mapped to sub-domains.
- **Note (informational):** 14 GDPR + 28 CRA rows in §8.1/§8.2 carry `(verify)` markers for corpus clause IDs — this is a follow-up corpus verification task noted in §8.3 Migration Notes, not a Tier 1 gap.
- **Severity:** —

### C1.3 — All articles cited in Doc 07c exist in corpus

- **Verdict:** PARTIAL
- **Evidence:**
  - Doc 07c cites **GDPR Articles** (Art. 5, 17, 20, 25, 30, 32, 33, 35, 37, 39) and **CRA Articles** (Art. 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25, 26) — all of which exist in corpus per `Citation_Index.md:39-79` (12 found, 0 article-level failures)
  - However, Doc 07c also references **CRA Annex I §1.2(c)**, **§1.3(c)**, **§1.3(d)**, **§1.4**, **§2** and **CRA Annex VII §1**, **§1-§2**, **§2** — see Appendix A for ID locations
  - `Citation_Index.md:111-113` — these Annex references are listed as **coverage gaps**: "CRA Annex I (essential cybersecurity requirements) is referenced heavily but the corpus only contains Articles, not Annexes" and "CRA Annex VII (conformity assessment) — corpus gap"
- **Gap:** Doc 07c references CRA Annex I (§1.2(c), §1.3(c), §1.3(d), §1.4, §2) and CRA Annex VII (§1-§2, §2) in PG/SG detail cards. These annexes are NOT present in corpus. Citation_Index flags these as documented gaps. Not a blocker because (a) Doc 07c cites them only as supporting references (not as the canonical clause ID), (b) the GDPR-CRA clause_mappings in Doc 06 §8 use Articles only (Annex gaps don't cascade), (c) the gap is explicitly documented in `Citation_Index.md §6` as future corpus augmentation target.
- **Severity:** LOW (functional impact is bounded; Article-level corpus linkage is complete; Annex-level gaps are documented and downstream-disclosed).

### C1.4 — Doc 05 APP flags cover GDPR + CRA (no missing applicability)

- **Verdict:** PASS
- **Evidence:**
  - `05_Regulatory_Applicability.md:67-87` — §3.1 GDPR APPLICABLE (CONTROLLER + PROCESSOR)
  - `05_Regulatory_Applicability.md:91-109` — §3.2 CRA APPLICABLE (MANUFACTURER, Default class)
  - `05_Regulatory_Applicability.md:112-125` — §3.3 NIS 2 NOT APPLICABLE (8 employees < 50, <€2M < €10M)
  - `05_Regulatory_Applicability.md:129-141` — §3.4 DORA NOT APPLICABLE (not financial entity)
  - `05_Regulatory_Applicability.md:145-156` — §3.5 AI Act NOT APPLICABLE (no AI/ML systems)
  - `05_Regulatory_Applicability.md:164-170` — §4 Applicability Matrix Summary: GDPR YES, CRA YES, NIS 2 NO, DORA NO, AI Act NO
  - All 5 regulations assessed; rationale documented per regulation
- **Gap:** NONE. All 5 regulations have applicability determination + rationale + clause count.
- **Severity:** —

### C1.5 — Doc 04 BG covers all legacy business goals (BG-01..BG-05)

- **Verdict:** PASS
- **Evidence:**
  - `04_Company_Context_Assessment.md:97` — BG-01 GDPR Compliance Baseline
  - `04_Company_Context_Assessment.md:98` — BG-02 CRA Conformity
  - `04_Company_Context_Assessment.md:99` — BG-03 Data Subject Rights
  - `04_Company_Context_Assessment.md:100` — BG-04 Security by Design
  - `04_Company_Context_Assessment.md:101` — BG-05 Supplier Due Diligence
  - ID pattern `BG-{NN}` (2-digit sequential) confirmed at `04_Company_Context_Assessment.md:103`
- **Gap:** NONE. 5/5 BGs present, all with cross-ref column to Doc 07c (see C2.2 below).
- **Severity:** —

### C1.6 — Doc 05b has ≥ 5 ambiguity cards (Berry lens R1/R2/R3 verbatim)

- **Verdict:** PASS
- **Evidence:**
  - `05b_Ambiguity_Register.md:18-21` — frontmatter: 417 total cards (276 GDPR + 141 CRA), 20 top-20 cards
  - `05b_Ambiguity_Register.md:36-43` — §1 Summary: 417 cards across 37 sub-domains
  - `05b_Ambiguity_Register.md:90-300+` — §3 Top 20 cards each include Berry lens R1/R2/R3 readings with disambiguation source
  - Berry lens format verified: Card #1 (GDPR-RT16) R1+R2 (lines 111-112), Card #2 (GDPR-CP02) R1+R2+R3 (lines 140-142), Card #3 (GDPR-CP15) R1+R2 (lines 192-194), Card #4 (CRA-CL02) R1+R2+R3 (lines 262-264 + 285-287)
  - 109 R1/R2/R3 occurrences across the doc (well above the ≥ 5 threshold)
- **Gap:** NONE. ≥ 5 cards with Berry lens format; criterion met by 20+ cards.
- **Severity:** —

### C1.7 — N/A (Case_01 doesn't have Doc 06b DORA-specific)

- **Verdict:** PASS (by design — N/A criterion)
- **Evidence:** Case_01 has `applicable_regs = [GDPR, CRA]`; Doc 06b (DORA-specific clause mapping) is only relevant when DORA is applicable. DORA = NOT APPLICABLE per `05_Regulatory_Applicability.md:129-141`. Criterion does not apply.
- **Severity:** —

### C2.1 — 0 contradictions between Doc 07b tier classification and Doc 07c PG/SG tier

- **Verdict:** PASS
- **Evidence:** See §3.1 Tier Matching Table below. 37/37 sub-domains have matching Tier values across Doc 07b §4 (`07b_Proportionality_Profile.md:92-130`) and Doc 07c §6 (Track B; line range removed — see Appendix A for IDs).
- **Gap:** NONE. 0 mismatches.
- **Severity:** —

### C2.2 — Doc 04 BG → Doc 07c PG/SG cross-references (all 5 BGs linked)

- **Verdict:** PASS
- **Evidence:** See §3.2 BG Cross-Reference Table below.
  - BG-01 → Doc 07c Appendix A §A.1 (PG table) + §5 (Tensions T-001..T-004) + §1/§6 (generic baseline + tier)
  - BG-02 → Doc 07c Appendix A §A.2 (SG table) + D-02.x + D-06.2 (SBOM) + D-07.x (secure dev)
  - BG-03 → Doc 07c Appendix A §A.1.1 D-05.3 (erasure) + D-05.4 (portability), both LIGHTWEIGHT
  - BG-04 → Doc 07c Appendix A §A.2.1 D-02.1 (vulnerability ID) + D-07.x (secure dev pipeline), all LIGHTWEIGHT
  - BG-05 → Doc 07c Appendix A §A.2.1 D-06.1 (MINIMAL INHERIT) + §5 T-002 (unified vendor mgmt)
- **Gap:** NONE for direct refs. Cross-refs don't include hypertext anchors (i.e., `#pg-D-01-1-001` anchors) but they cite section + sub-domain IDs which is functionally equivalent.
- **Severity:** —

### C2.3 — Doc 07 tensions resolved implemented consistently in Doc 07b example_controls

- **Verdict:** PASS
- **Evidence:** See §3.3 Tension Implementation Table below.
  - T-001 (D-04.3): Doc 07c §5 max-SLA 24h routing → Doc 07b §4 row 23 "max-SLA 24h internal; unified incident workflow" — IDENTICAL
  - T-002 (D-06.1, D-06.3): Doc 07c §5 unified vendor mgmt → Doc 07b §4 rows D-06.1 + D-06.3 (DPA validation + DPA template) — IDENTICAL
  - T-003 (D-09.4, D-09.1): Doc 07c §5 integrated documentation repo → Doc 07b §4 rows D-09.1 (policy template) + D-09.4 (RoPA template) + D-09.2 (DPIA/CRA-RA unified) — IDENTICAL
  - T-004 (D-08.2): Doc 07c §5 competency matrix → Doc 07b §4 row D-08.2 "Annual security awareness email + role-specific docs (admin/dev/DPO)" — IDENTICAL
  - `07b_Proportionality_Profile.md:337-348` — §13 Tensions Cross-Reference also confirms the same mapping
- **Gap:** NONE. 4/4 tensions fully reflected in Doc 07b example_controls.
- **Severity:** —

### C2.4 — Frontmatter status progression (DRAFT → RECONCILED → CORPUS_ENRICHED → ADJUSTED_OBJECTIVES → DEEP_ENRICHED)

- **Verdict:** PARTIAL
- **Evidence:**
  - Status progression observed across 14 Phase 1 case docs:
    - `00_Taxonomy_Reference.md:8` — RECONCILED
    - `01_INTAKE_FORM.md:8` — RECONCILED
    - `04a_Architecture_DataInventory.md:9` — CORPUS_ENRICHED
    - `04b_Security_Posture.md:9` — CORPUS_ENRICHED
    - `04c_ThirdParty_Landscape.md:9` — CORPUS_ENRICHED
    - `04d_Org_Roles_RACI.md:9` — CORPUS_ENRICHED
    - `04_Company_Context_Assessment.md:10` — DEEP_ENRICHED
    - `05_Regulatory_Applicability.md:10` — DEEP_ENRICHED
    - `05b_Ambiguity_Register.md:9` — DEEP_ENRICHED
    - `06_Clause_Mapping_Matrix.md:9` — RECONCILED
    - `07_Structured_Compliance_Matrix.md:9` — RECONCILED
    - `07b_Proportionality_Profile.md:10` — DEEP_ENRICHED
    - `07c_Adjusted_Objectives.md` frontmatter — `status: DEEP_ENRICHED`
    - `Citation_Index.md:9` — CORPUS_ENRICHED
  - **Gap:** The intermediate `ADJUSTED_OBJECTIVES` status (Fase de Especificação 4 marker per AGENTS.md / README) was NEVER materialised in any frontmatter. Doc 07c was created in Fase de Especificação 4 directly with `status: DEEP_ENRICHED` (jumping from non-existent → DEEP_ENRICHED via Fase de Especificação 5 enrichment). Doc 07b jumped from RECONCILED → DEEP_ENRICHED without an `ADJUSTED_OBJECTIVES` intermediate state. The Fase de Especificação 4 *work* is fully present (74 adjusted objectives in §2-§3, 4 tensions in §4, 37-row decision table in §5, 07b §12-§14); only the **status label** is missing.
  - No DRAFTs exist in the active case-form 14 Phase 1 docs (`corpus_field_map.md:9` is DRAFT but is a meta-doc).
- **Gap detail:** Functional progression is monotonic forward (no regressions); the missing intermediate label is a documentation gap, not a content gap.
- **Severity:** LOW (work is complete; only the status metadata is missing the ADJUSTED_OBJECTIVES state).

### C2.5 — applicable_regs consistent across all docs (always [GDPR, CRA])

- **Verdict:** PASS
- **Evidence:**
  - `04a_Architecture_DataInventory.md:9` — `applicable_regs: [GDPR, CRA]`
  - `04b_Security_Posture.md:9` — `applicable_regs: [GDPR, CRA]`
  - `04c_ThirdParty_Landscape.md:9` — `applicable_regs: [GDPR, CRA]`
  - `04d_Org_Roles_RACI.md:9` — `applicable_regs: [GDPR, CRA]`
  - `05b_Ambiguity_Register.md:15` — `applicable_regs: [GDPR, CRA]`
  - `07c_Adjusted_Objectives.md` frontmatter — `applicable_regs: [GDPR, CRA]`
  - `Citation_Index.md:11` — `applicable_regs: [GDPR, CRA]`
  - `05_Regulatory_Applicability.md:164-170` — Applicability Matrix: GDPR YES, CRA YES
  - 7 docs with explicit `applicable_regs` field all show `[GDPR, CRA]`. Doc 05 §4 matrix confirms the same applicability scope. No doc lists additional regulations as applicable.
- **Gap:** NONE. Consistent [GDPR, CRA] across all docs.
- **Severity:** —

### C2.6 — 6 lints PASS (Company Context, Regulatory Mapping, Regulatory References, Regulatory Ground Truth, Cross-Document Consistency, Template Compliance)

- **Verdict:** PASS
- **Evidence:**
  - Live lint run on 2026-08-06 (`python3 01_IMPLEMENTATION_TOOLS/lints/run_phase1_lints.py --case "Case_01_TinyTask_SaaS"`):
    - Company Context (38 questions) → ✅ PASSED
    - Regulatory Mapping → ✅ PASSED
    - Regulatory References (Anti-Hallucination) → ✅ PASSED
    - Regulatory Ground Truth → ✅ PASSED
    - Cross-Document Consistency → ✅ PASSED
    - Template Compliance → ✅ PASSED
  - Summary: 6/6 passed, 44 warnings, 0 errors
  - Latest report: `lints/reports/lint_report_phase1_20260806_183516.md`
- **Gap:** NONE. 6/6 lints PASS.
- **Severity:** —

---

## §3 Cross-Document Consistency Deep-Check

### §3.1 — C2.1 Tier Matching Table (Doc 07b §4 vs Doc 07c §6)

| Sub-Domain | Doc 07b §4 Tier | Doc 07c §6 Tier | Match? |
|-----------|----------------|----------------|:------:|
| D-01.1 Data at Rest Encryption | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-01.2 Data in Transit Encryption | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-01.3 Key Management | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-01.4 Data Integrity | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-02.1 Vulnerability Identification | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-02.2 Patch Management | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-02.3 Coordinated Vulnerability Disclosure | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-02.4 Threat-Led Penetration Testing | DEFERRED | DEFERRED | ✓ |
| D-03.1 Identity Lifecycle | MINIMAL | MINIMAL | ✓ |
| D-03.2 Multi-Factor Authentication | MINIMAL | MINIMAL | ✓ |
| D-03.3 Authorisation & Least Privilege | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-03.4 Secure System Defaults | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-04.1 Incident Detection & Triage | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-04.2 Containment & Mitigation | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-04.3 Regulatory Notification | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-04.4 Data Restoration & Recovery | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-05.1 Data Minimisation | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-05.2 Retention & Archiving | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-05.3 Right to Erasure | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-05.4 Data Portability | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-06.1 Vendor Risk Assessment | MINIMAL | MINIMAL | ✓ |
| D-06.2 Software Bill of Materials | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-06.3 Contractual Security Obligations | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-06.4 Third-Party Boundary Management | MINIMAL | MINIMAL | ✓ |
| D-07.1 Secure-by-Design Principles | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-07.2 Secure Coding Practices | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-07.3 CI/CD Pipeline Security | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-07.4 Change Management | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-08.1 General Security Awareness | MINIMAL | MINIMAL | ✓ |
| D-08.2 Role-Specific Competence | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-09.1 Information Security Policies | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-09.2 Impact & Risk Assessments | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-09.3 Asset Inventories | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-09.4 Records of Processing | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-10.1 Continuous Security Monitoring | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-10.2 Audit Logging & Traceability | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |
| D-10.3 Compliance Testing | LIGHTWEIGHT | LIGHTWEIGHT | ✓ |

**Match rate:** **37 of 37 sub-domains** have matching Tier (100%). **0 mismatches.**

**Distribution check:**
- Doc 07b §3 (line 75-82): 31 LIGHTWEIGHT + 5 MINIMAL + 1 DEFERRED = 37
- Doc 07c §8 Validation (see Appendix A for IDs): 31 LIGHTWEIGHT + 5 MINIMAL + 1 DEFERRED = 37
- Match ✓

### §3.2 — C2.2 BG Cross-Reference Table

| BG ID | BG Description | Doc 04 §4 cross-ref target | Doc 07c location |
|-----|----------------|---------------------------|------------------|
| BG-01 | GDPR Compliance Baseline | → Doc 07c Appendix A §A.1 (PG table, 37 rows) + §5 (Tensions T-001..T-004) + §1 §6 | `07c_Adjusted_Objectives.md` Appendix A §A.1, §5, §1, §6 ✓ |
| BG-02 | CRA Conformity | → Doc 07c Appendix A §A.2 (SG table, 37 rows) — D-02.x + D-06.2 + D-07.x | `07c_Adjusted_Objectives.md` Appendix A §A.2, §A.2.1 ✓ |
| BG-03 | Data Subject Rights | → Doc 07c Appendix A §A.1.1 D-05.3 (PG-D-05.3-001) + D-05.4 (PG-D-05.4-001), both LIGHTWEIGHT | `07c_Adjusted_Objectives.md` Appendix A §A.1.1 ✓ |
| BG-04 | Security by Design | → Doc 07c Appendix A §A.2.1 D-02.1 (SG-D-02.1-001) + D-07.x (secure dev), all LIGHTWEIGHT | `07c_Adjusted_Objectives.md` Appendix A §A.2.1 ✓ |
| BG-05 | Supplier Due Diligence | → Doc 07c Appendix A §A.2.1 D-06.1 (MINIMAL INHERIT) + §5 T-002 (unified vendor mgmt) | `07c_Adjusted_Objectives.md` Appendix A §A.2.1, §5 ✓ |

**Match rate:** **5 of 5 BGs** have explicit cross-references to Doc 07c sections + sub-domain IDs. **0 gaps.**

### §3.3 — C2.3 Tension Implementation Table

| Tension | Doc 07c §5 Resolution | Doc 07b §4 Implementation | Match? |
|---------|----------------------|--------------------------|:------:|
| T-001 (D-04.3) — timing | "max-SLA 24h internal clock ... single workflow generates per-recipient submissions from one underlying event record" | Doc 07b §4 row D-04.3 example_controls: "max-SLA 24h internal; unified incident workflow" | ✓ |
| T-002 (D-06.1, D-06.3) — scope | "Unified vendor management — single template ... DPA validation against GDPR Art. 28 + supply-chain security for CRA" | Doc 07b §4 rows D-06.1 (DPA validation against GDPR Art. 28; supplier security clauses) + D-06.3 (DPA template + supplier security clauses) | ✓ |
| T-003 (D-09.4, D-09.1) — requirement | "Integrated documentation repo ... Unified DPIA + CRA risk assessment template (dual-output)" | Doc 07b §4 rows D-09.1 (Security policy template) + D-09.2 (DPIA + CRA risk assessment unified) + D-09.4 (RoPA template) | ✓ |
| T-004 (D-08.2) — intensity | "Competency matrix — single training matrix covering both data protection + product security competence" | Doc 07b §4 row D-08.2: "Annual security awareness email + role-specific docs (admin/dev/DPO)" | ✓ |

**Match rate:** **4 of 4 tensions** fully reflected in Doc 07b example_controls. **0 gaps.**

Cross-confirmed by `07b_Proportionality_Profile.md:337-348` — §13 Tensions Cross-Reference provides additional 1-line cross-reference for each tension, confirming the same mapping.

---

## §4 Critical Blockers (HIGH severity)

**NONE.**

No HIGH-severity gaps detected across any of the 13 Tier 1 criteria. Both PARTIAL verdicts (C1.3, C2.4) are LOW severity.

---

## §5 Recommendations

### §5.1 LOW-severity improvements (optional, non-blocking)

1. **C1.3 — Document corpus Annex gaps explicitly in Doc 07c cards.** The 12 cards that reference CRA Annex I (D-01.4, D-02.4, D-05.1, D-05.2, D-06.2, D-09.2, D-09.3) and CRA Annex VII (D-09.1, D-09.3, D-10.3) could add a `Note:` line saying "Annex not yet in corpus — see Citation_Index §6". This makes the gap visible at point-of-use rather than only in Citation_Index. **Severity: LOW; cosmetic; no functional impact.**

2. **C2.4 — Materialise the ADJUSTED_OBJECTIVES status in frontmatter.** Add a one-line Fase de Especificação 4 commit to set `status: ADJUSTED_OBJECTIVES` on Doc 07c (and optionally Doc 07b) at the Fase de Especificação 4 milestone, then bump to DEEP_ENRICHED in Fase de Especificação 5. This would make the frontmatter status progression strictly monotonic through all 5 named states (DRAFT → RECONCILED → CORPUS_ENRICHED → ADJUSTED_OBJECTIVES → DEEP_ENRICHED). **Severity: LOW; metadata-only; Fase de Especificação 4 work is fully present.**

3. **C2.2 — Add hypertext anchors in Doc 04 §4 cross-ref column.** Replace the textual `→ Doc 07c Appendix A §A.1 (PG table, 37 rows)` with link `→ [Doc 07c Appendix A §A.1](#pg-table)` and per-card anchor links like `→ [D-05.3 erasure card](#pg-D-05-3-001)`. Improves navigability. **Severity: LOW; functional cross-refs already work.**

4. **C1.6 — Consider extending Doc 05b with full 417 cards** (currently top 20 in §3). Already flagged as future work in `RICH_VS_LEGACY.md:101` ("Extend Doc 05b with full ambiguity card set (currently top 20 of 417)"). Not a Tier 1 gap. **Severity: LOW; deferred to future sprint.**

5. **C1.2 — Resolve `(verify)` corpus clause IDs in Doc 06 §8.1/§8.2.** 14 GDPR + 28 CRA rows carry `(verify)` markers for corpus clause IDs (per `06_Clause_Mapping_Matrix.md:226`). This is a corpus cross-walk task noted in §8.3 Migration Notes. Not a Tier 1 gap (the case-form IDs are stable; corpus-form is parallel reference). **Severity: LOW; deferred to corpus verification sprint.**

---

## §6 Next Steps — Tier 2/3 Criteria DEFERRED

The user has explicitly deferred lower tiers to a next iteration. Future Tier 2/3 validation should cover:

- **Tier 2 — Realism**: Does the implementation match real AWS / Firebase / Stripe / GitHub primitives cited in Doc 07b example_controls? Are the verification methods (DEMONSTRATE + INSPECT) implementable by an 8-person team?
- **Tier 2 — Business**: Is the cost/feasibility realistic? Does the FTE=0.85 budget accommodate the 74 PG/SG × 12-field cards? (Fase de Especificação 5 explicitly excluded Effort/Cost/Timeline per scope.)
- **Tier 2 — Regulatory**: Are the GDPR Art. 32 + Art. 28 multi-actor obligations correctly differentiated between CONTROLLER and PROCESSOR roles? Is CRA Art. 13(8) 5-year support period correctly interpreted for SaaS?
- **Tier 3 — Track B**: Does the (S, I, P) → Tier mapping in Doc 07b §12 / Doc 07c §5 correctly apply proportionality_model.md §5.1-§5.3? Is the floor rule (§5.3) preserved?
- **Tier 3 — Traceability**: For each of 74 PG/SG, is there a complete chain clause_id → sub-domain → PG/SG → tier → example_control → owner → verification? Are any chains broken?

These are out of scope for Tier 1.

---

## §7 See also

- `validation/VALIDATOR_SPRINT0.md` skeleton validator
- `validation/VALIDATOR_SPRINT3.md` corpus-cross-check validator
- `validation/VALIDATOR_SPRINT4.md` adjusted-objectives validator
- `validation/VALIDATOR_SPRINT5.md` deep-enrichment validator
- `validation/SPRINT3_REPORT.md` final report (lint status, cross-check summary)
- `validation/SPRINT4_REPORT.md` adjusted objectives report (74 PG/SG + 4 tensions)
- `validation/SPRINT5_REPORT.md` deep enrichment report (74 detail cards × 12 fields)
- `01_IMPLEMENTATION_TOOLS/lints/reports/lint_report_phase1_20260806_183516.md` — live lint run (6/6 PASS)
- `00_METHODOLOGY/REFERENCE/proportionality_model.md` §1 (invariant) + §5 (decision table) + §6 (tier attributes) — Track B spec
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` — corpus source (38 sub-domains × 4 layers)

---

## §8 Validator Signature

| Role | Name | Date |
|------|------|------|
| Validator (Tier 1) | Sprint Validator (tier1-verifier) | 2026-08-06 |
| Methodology Review | (pending) | |
| Orchestrator Acceptance | (pending) | |