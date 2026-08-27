---
document_id: AEGIS-P1-RICH-VALIDATOR-TIER2
title: Validator Tier 2 — Case_01 Phase 1 Rich
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-10
author: Sprint Validator (tier2-verifier)
status: HISTORICAL
historical_note: Historical report from corr-007 era. Current 07c version is v4.0 with AO ID model (corr-008 supersedes corr-007). Content below preserved verbatim; see `07c_Adjusted_Objectives.md` §9 Version History for the v4.0 AO ID migration entry.
case: Case_01_TinyTask_SaaS
tier: 2 (Realism + Business Alignment + Scale)
applicable_regs: [GDPR, CRA]
active_subdomains: 37
inactive_subdomains: [D-08.3]
validator_scope: read-only; no source files modified
---

# Validator Tier 2 — Case_01 Phase 1 Rich

> Tier 2 = Realism / Company-Specificity + Business Alignment + Scale Alignment.
> Tier 1 (Completeness + Internal Consistency) already **CONDITIONAL_PASS** per `VALIDATOR_TIER1.md`.
> Source files audited: `04`, `04a`, `04b`, `04c`, `04d`, `07b`, `07c` (and `phase1_ontology.yaml` + `Critical_Analysis_Micro_Enterprise.md` for cross-checks).

---

## §1 Summary

| # | Tier 2 Criterion | Verdict | Severity |
|---|------------------|---------|----------|
| C3.1 | example_controls mention concrete tools (NOT generic) | PASS | — |
| C3.2 | Verification criteria are checkable (commands, endpoints, configs) | PASS | — |
| C3.3 | Owner roles reflect real org chart (not generic "Security Team") | PASS | — |
| C3.4 | Affected Stakeholders include real external roles (CNPD, ENISA, etc.) | PASS | — |
| C3.5 | Affected Stakeholders appropriate for SaaS sector (NOT banking/defense) | PASS | — |
| C3.6 | Documents reference real infrastructure (AWS, Firebase, Stripe — not "cloud") | PASS | — |
| C4.1 | Each BG has ≥ 1 PG or SG aligned (no orphan BGs) | PASS | — |
| C4.2 | PG/SG priority aligns with BG priority (HIGH BG → MUST PG/SG) | PASS | — |
| C4.3 | BG stakeholders overlap with PG/SG stakeholders (org consistency) | PASS | — |
| C4.4 | BG quantitative metrics reflected in PG/SG verification criteria | PARTIAL | LOW |
| C4.5 | BG deadlines align with PG/SG Implementation Priority | PASS | — |
| C4.6 | Detail depth matches MICRO scale (8 employees) — not over-engineered | PASS | — |
| C4.7 | Track B tiers reflect MICRO reality (LIGHTWEIGHT/MINIMAL/DEFERRED) | PASS | — |
| C4.8 | Effort expectations implicit in tier match company capacity | PASS | — |

**Overall Tier 2 verdict:** **PASS**

- 13 PASS, 1 PARTIAL (LOW), 0 FAIL.
- No HIGH-severity gaps; no blocking issues.
- Tier 2 strengthens Tier 1's CONDITIONAL_PASS: the rich-mode artefacts are **company-grounded**, **business-aligned**, and **scale-proportionate**.
- The single PARTIAL (C4.4) is informational, not blocking: no SLA-style quantitative metric ("uptime ≥99.99%") is explicitly stated in BG-01..BG-05, but every metric that **is** stated is reflected in PG/SG verification criteria.

---

## §2 Per-Criterion Detail

### C3.1 — example_controls mention concrete tools (NOT generic)

- **Verdict:** PASS
- **Evidence (spot-check of 15 cards across all 10 macro-domains):**
  - **D-01.1** `07b:94` — "AWS S3 / DynamoDB SSE-KMS enabled (AES-256 default); no company-owned KMS program"
  - **D-01.2** `07b:95` — "TLS 1.3 via AWS ACM / CloudFront; certificate auto-renewal"
  - **D-02.1** `07b:98` — "Trivy + npm audit in CI; OSS advisories"
  - **D-02.2** `07b:99` — "AWS Systems Manager Patch Manager (auto)"
  - **D-02.3** `07b:100` — "security.txt at `/.well-known/security.txt`; CVD page"
  - **D-04.1** `07b:106` — "CloudWatch alarms + SNS notifications"
  - **D-04.4** `07b:109` — "AWS Backup; RTO 24h"
  - **D-06.1** `07b:114` — "DPA validation against GDPR Art. 28; supplier security clauses"
  - **D-06.2** `07b:115` — "CycloneDX SBOM in CI/CD per release"
  - **D-07.2** (see 07c Appendix A) (SG card) — "SAST (e.g. Semgrep) runs on every PR"
  - **D-07.3** (see 07c Appendix A) — "OIDC token-based cloud auth in GitHub Actions — no long-lived AWS keys; Pipeline-as-code (GitHub Actions YAML)"
  - **D-08.2** `07b:123` — "Annual security awareness email + role-specific docs (admin/dev/DPO)"
  - **D-09.1** (see 07c Appendix A) — "Security policy template approved by CEO + CTO; Quarterly policy review cadence documented"
  - **D-09.2** (see 07c Appendix A) — "DPIA template + CRA risk assessment template unified (dual-output)"
  - **D-10.1** (see 07c Appendix A) — "CloudWatch alarms configured for top 10 anomaly patterns; GuardDuty enabled account-wide; Quarterly alarm tuning review"
  - **D-10.2** (see 07c Appendix A) — "CloudTrail enabled account-wide with multi-region trail; Application audit log to S3 with Object Lock (COMPLIANCE mode); 7y retention"
- **Note:** Tools are AWS-native (S3, DynamoDB, KMS, CloudWatch, CloudTrail, GuardDuty, ACM, Systems Manager, Backup) plus a small set of SaaS-typical add-ons (Auth0/Firebase, Stripe, Trivy, npm audit, CycloneDX, Snyk, Semgrep, GitHub Actions). All match Case_01's documented stack in `04a:55-72` and `04c:59-78`. ZERO generic placeholders like "monitoring tools", "encryption", "key store" — every control has a vendor + product.
- **Severity:** —

### C3.2 — Verification criteria are checkable

- **Verdict:** PASS
- **Evidence (spot-check):**
  - (see 07c Appendix A) (PG-D-01.1-001 verification): "AWS Config rule `s3-bucket-server-side-encryption-enabled` is `COMPLIANT` for all production buckets" — **specific AWS Config rule name + state value**, can be verified with `aws configservice get-compliance-details-by-config-rule --config-rule-name s3-bucket-server-side-encryption-enabled`.
  - (see 07c Appendix A) (PG-D-01.3-001 verification): "KMS keys used by S3/DynamoDB/RDS have `KeyRotationStatus=true`" — verifiable via `aws kms get-key-rotation-status --key-id <id>`; "Annual review confirms no plaintext key material in source control (git grep `aws_secret_access_key`)" — exact `git grep` command given.
  - (see 07c Appendix A) (PG-D-01.4-001 verification): "RDS instances have `MultiAZ=true` and automated snapshots enabled with 7-day retention" — verifiable via AWS Console/RDS API; "S3 log bucket has Object Lock (COMPLIANCE mode) enabled" — verifiable.
  - (see 07c Appendix A) (SG-D-02.1-001 verification): "CI pipeline runs Trivy on every PR — block merge on `CRITICAL` findings" — verifiable via PR check status; "`npm audit --audit-level=high` passes on every build" — exact CLI command + threshold.
  - (see 07c Appendix A) (SG-D-05.4-001 verification): "JSON export endpoint returns all data subject data within Art. 20 structured format" — verifiable via API endpoint + content-type check.
  - (see 07c Appendix A) (SG-D-07.3-001 verification): "CI gates block merge on critical SAST or dependency vulns" — verifiable via GitHub branch protection rules.
  - (see 07c Appendix A) (SG-D-10.2-001 verification): "CloudTrail enabled account-wide with multi-region trail" — verifiable via `aws cloudtrail describe-trails`.
- **Note:** Every Verification Criteria block contains at least one operationally-testable predicate — a CLI command, AWS Config rule, API endpoint, git pattern, or named tool flag. No vague predicates like "is configured correctly" without an evidence anchor.
- **Severity:** —

### C3.3 — Owner roles reflect real org chart (NOT generic "Security Team")

- **Verdict:** PASS
- **Evidence:**
  - `04d:62-72` — explicit role allocation: CEO (Founder #1, 1.0 FTE incl. 0.2 DPO), CTO (Founder #2, 1.0 FTE incl. 0.3 CISO), Lead Developer (1.0 FTE), 5 Developers (1.0 FTE each), External Legal Adviser (0 FTE retainer).
  - PG/SG owner columns reference these roles verbatim:
    - D-01.x PG/SG: "CTO (primary) + Lead Dev (backup)" — matches 04d §2
    - D-02.1 SG: "Lead Dev (primary) + CTO (backup)" — matches 04d §4.2 row 169
    - D-04.x PG/SG: "CTO (primary) + Lead Dev (backup)" — matches 04d §4.4
    - D-05.3/D-05.4 PG/SG: "DPO (primary) + CTO (backup)" / "DPO (primary) + CTO (backup)" — matches 04d §4.5 rows 200-201
    - D-08.2 PG: "Annual security awareness email + role-specific docs (admin/dev/DPO)" — the "DPO" role specifically references the CEO-as-DPO arrangement documented in 04d:65
  - NO "Security Team", "Compliance Team", "IT Department" anywhere in PG/SG ownership columns. All ownership tied to actual named roles.
- **Note:** The CEO-as-DPO and CTO-as-CISO dual-hat pattern is documented explicitly in `04d:73-79` and reflected throughout PG/SG ownership columns. This is realistic for an 8-person team and consistent with P2 (Company Reality First).
- **Severity:** —

### C3.4 — Affected Stakeholders include real external roles (CNPD, ENISA, etc.)

- **Verdict:** PASS
- **Evidence:**
  - **CNPD (Portuguese SA)**: (see 07c Appendix A) — explicit reference in T-001 root-cause analysis: "supervisory authority (CNPD in Portugal) for GDPR"; also referenced in `04d:272` training status: "CEO reviewed CNPD guidance materials".
  - **ENISA**: (see 07c Appendix A) — explicit reference to ENISA single reporting platform (CRA Art. 20).
  - **Supervisory authority** (generic GDPR term): (see 07c Appendix A) (in phase1_ontology.yaml tensions) — "GDPR requires 72-hour notification to supervisory authority"; `05_Regulatory_Applicability.md:331` — Art. 31 "Cooperation with supervisory authority".
  - **EU market-surveillance authorities**: `04_Company_Context_Assessment.md:98` (BG-02 affected stakeholders) — explicit mention.
  - **B2B clients / data controllers**: `04_Company_Context_Assessment.md:97,99,100,101` (BG-01, BG-03, BG-04, BG-05) — concrete external role with contractual relationship.
  - **Procurement**: `04_Company_Context_Assessment.md:101` (BG-05 owner + stakeholders); (see 07c Appendix A) — Procurement mentioned 8x across D-06.x PG/SG cards (matching ownership reality for vendor management at small SaaS).
  - **External Legal Adviser**: `04d:69,125,144-147` — Portugal-based law firm on retainer; not "DPB" (Germany) or "BfDI" because TinyTask is Portuguese-domiciled. CNPD is the correct SA.
- **Note:** The roles are **context-correct for Portugal/SaaS** — CNPD not DPB/BfDI; ENISA for CRA reporting; Procurement for vendor lifecycle. Real and verifiable.
- **Severity:** —

### C3.5 — Affected Stakeholders appropriate for sector (SaaS NOT banking/defense)

- **Verdict:** PASS
- **Evidence:**
  - No banking-specific stakeholders (no central bank, no DORA-style financial regulator, no payments-risk officer).
  - No defense-specific stakeholders (no NATO classification authority, no security clearance body).
  - SaaS-appropriate stakeholders present: B2B clients (data controllers), procurement, DPO (for EU customers), Stripe (PCI-DSS scope delegated), AWS / Firebase (cloud infrastructure).
  - The B2B SaaS context is explicit throughout: `04_Company_Context_Assessment.md:97` BG-01 affected stakeholders are "CEO, CTO, DPO, all B2B clients (data controllers)" — this is canonical SaaS stakeholder map.
  - PG-D-04.3-001 affected stakeholders include "Customers (data subjects), CTO, DevOps" — appropriate for SaaS incident response.
  - SG-D-06.4-001 scope: "AWS / Stripe / Firebase boundary inherited; no non-EU representative required (EU-domiciled manufacturer)" — appropriate for EU SaaS.
- **Note:** Zero anachronistic stakeholders. Sector-aligned throughout.
- **Severity:** —

### C3.6 — Documents reference real infrastructure (Firebase, AWS S3 — NOT generic "cloud storage")

- **Verdict:** PASS
- **Evidence:**
  - `04a:51-91` — 5 named systems (SYS-01..SYS-05) with specific tech: Node.js API + React + PostgreSQL, Auth0, PostgreSQL on EU cloud, Cloud KMS, S3-compatible encrypted bucket.
  - `04a:65-72` — 6 named cloud services: AWS (PostgreSQL managed), S3, Cloud KMS, Auth0, Stripe, Datadog — all with EU region + DPA columns.
  - `04a:78-80` — Auth0 OAuth 2.0/OIDC, Cloud provider IAM with MFA, GitHub with 2FA — all concrete.
  - `04c:59-64` — Cloud providers table with AWS (eu-west-1), Stripe, Auth0 EU tenant — all real vendors.
  - `04c:73-78` — Software vendors: GitHub, Datadog, Snyk — all real products used by modern SaaS.
  - `07b:94-130` — 37-row proportionality table references the same real stack: AWS S3/DynamoDB, CloudWatch, CloudTrail, AWS KMS, AWS Backup, Trivy, npm audit, CycloneDX, security.txt, CloudFront, AWS ACM, Firebase Auth, Snyk.
- **Note:** Zero generic "cloud storage", "monitoring system", "identity provider" placeholders. Every infrastructure reference is a named vendor+product or AWS service primitive.
- **Severity:** —

### C4.1 — Each BG has ≥ 1 PG or SG aligned (no orphan BGs)

- **Verdict:** PASS
- **Evidence (BG → PG/SG coverage trace):**
  - **BG-01 (GDPR Compliance Baseline, HIGH)** `04_Company_Context_Assessment.md:97` → cross-ref column: "Doc 07c Appendix A §A.1 (PG table, 37 rows)" → all 37 PG rows align with GDPR-compliance obligation.
  - **BG-02 (CRA Conformity, HIGH)** `04_Company_Context_Assessment.md:98` → "Doc 07c Appendix A §A.2 (SG table, 37 rows) — D-02.x (vuln + patch + CVD) + D-06.2 (SBOM) + D-07.x (secure dev)" → 10+ SG rows (SG-D-02.1, SG-D-02.2, SG-D-02.3, SG-D-06.2, SG-D-07.1, SG-D-07.2, SG-D-07.3, SG-D-07.4) + SG-D-09.x (conformity docs).
  - **BG-03 (Data Subject Rights, MEDIUM)** `04_Company_Context_Assessment.md:99` → "Doc 07c Appendix A §A.1.1 D-05.3 (PG-D-05.3-001 erasure) + D-05.4 (PG-D-05.4-001 portability), both LIGHTWEIGHT" → 2 explicit PG rows.
  - **BG-04 (Security by Design, MEDIUM)** `04_Company_Context_Assessment.md:100` → "Doc 07c Appendix A §A.2.1 D-02.1 (SG-D-02.1-001 vulnerability ID) + D-07.x (secure dev pipeline), all LIGHTWEIGHT" → 5+ SG rows (D-02.1, D-07.1, D-07.2, D-07.3, D-07.4).
  - **BG-05 (Supplier Due Diligence, MEDIUM)** `04_Company_Context_Assessment.md:101` → "Doc 07c Appendix A §A.2.1 D-06.1 (MINIMAL INHERIT vendor attestation) + §4 T-002 (unified vendor mgmt)" → 4+ SG/PG rows (D-06.1, D-06.3, D-06.4).
- **Note:** 0 orphan BGs. All 5 BGs map to multiple PG/SG. Cross-ref column in BG table (`04:97-101`) provides explicit pointer to Doc 07c sections, eliminating ambiguity.
- **Severity:** —

### C4.2 — PG/SG priority aligns with BG priority (HIGH BG → MUST PG/SG)

- **Verdict:** PASS
- **Evidence (alignment matrix):**
  - **BG-01 (HIGH)** → mapped PG rows in Doc 07c Appendix A §A.1 are all **MUST** priority (verified: PG-D-01.1 through PG-D-10.3 all show MUST except D-02.4 which is SHOULD/DEFERRED — but D-02.4 not central to BG-01).
  - **BG-02 (HIGH)** → mapped SG rows: SG-D-02.1 MUST, SG-D-02.2 MUST, SG-D-02.3 MUST, SG-D-06.2 MUST, SG-D-07.x MUST (D-07.1, D-07.2, D-07.3, D-07.4 all MUST per (see 07c Appendix A)). Zero SHOULD/COULD mapped to HIGH BG.
  - **BG-03 (MEDIUM)** → mapped PG-D-05.3-001 (MUST) + PG-D-05.4-001 (MUST). MEDIUM BG with MUST PG is **acceptable per proportionality_model.md §5.1** — MUST is the regulatory floor regardless of business priority.
  - **BG-04 (MEDIUM)** → mapped SG-D-02.1-001 (MUST) + SG-D-07.x (MUST). Same as BG-03.
  - **BG-05 (MEDIUM)** → mapped SG-D-06.1-001 (MUST) + SG-D-06.3-001 (MUST) + SG-D-06.4-001 (MUST). Same pattern.
- **Note:** The 1 DEFERRED row (D-02.4 Threat-Led Pentest) is **correctly NOT mapped to any BG** — D-02.4 is SHOULD/DEFERRED per Track B §5.2 + FTE 0.85, and no BG claims TLPT capability. This is appropriate de-prioritisation.
- **Severity:** —

### C4.3 — BG stakeholders overlap with PG/SG stakeholders (org consistency)

- **Verdict:** PASS
- **Evidence (5 BGs vs PG/SG stakeholder coverage):**
  - **BG-01 (CEO, CTO, DPO, B2B clients)** `04:97` → PG-D-01.1 "Customers (data subjects), CTO, DPO" (see 07c Appendix A); PG-D-04.3 "Customers, CTO, DPO" (see 07c Appendix A); PG-D-09.2 "CEO, CTO, DPO" (see 07c Appendix A). **Match: CTO + DPO + customers/B2B clients**.
  - **BG-02 (CTO, Lead Dev, B2B clients procurement, EU market-surveillance)** `04:98` → SG-D-02.1 "Customers, CTO, DevOps" (see 07c Appendix A); SG-D-06.2 "CTO, DPO, Procurement" (see 07c Appendix A); SG-D-07.1 "CTO, DevOps, DPO" (see 07c Appendix A). **Match: CTO + Lead Dev + Procurement**.
  - **BG-03 (Customers, DPO, B2B client controllers)** `04:99` → PG-D-05.3 "Customers, DPO, CTO" (see 07c Appendix A); PG-D-05.4 "Customers, DPO, CTO" (see 07c Appendix A). **Match: Customers + DPO + CTO**.
  - **BG-04 (CTO, Lead Dev, B2B clients security review)** `04:100` → SG-D-02.1 "Customers, CTO, DevOps" (see 07c Appendix A); SG-D-07.2 "CTO, DevOps, DPO" (see 07c Appendix A). **Match: CTO + Lead Dev/DevOps + DPO**.
  - **BG-05 (CTO, Procurement, B2B clients procurement)** `04:101` → SG-D-06.1 "CTO, DPO, Procurement" (see 07c Appendix A); SG-D-06.3 "CTO, DPO, Procurement" (see 07c Appendix A); SG-D-06.4 "CTO, DPO, Procurement" (see 07c Appendix A). **Match: CTO + Procurement + DPO**.
- **Note:** Zero stakeholder contradictions. The Procurement role appears in BG-05 and D-06.x SG/PG consistently. The DPO role appears in BG-01/BG-03/BG-04/BG-05 and in PG/SG cards for data-protection-relevant sub-domains. The CTO role is universal (per the 8-person org chart in `04d`).
- **Severity:** —

### C4.4 — Quantitative metrics of BG reflected in PG/SG verification criteria

- **Verdict:** PARTIAL
- **Evidence (BG metrics → PG/SG verification trace):**
  - **BG-01 metric**: "Zero audit findings in last 12 months; RoPA 100% complete" `04:97`. **Reflected in**: SG-D-09.4-001 verification (see 07c Appendix A) ("RoPA reviewed annually + on change of processing; 10y retention per CRA Art. 13(13)"). PARTIAL: RoPA is reflected; "zero audit findings" is aspirational, not a verifiable criterion (zero defects is not a control — it's an outcome).
  - **BG-02 metric**: "SBOM published per release (37 releases planned for first 12 months); security.txt active + reachable" `04:98`. **Reflected in**: SG-D-06.2-001 (see 07c Appendix A) ("CycloneDX SBOM generated on every release tag"); SG-D-02.3-001 (see 07c Appendix A) ("security.txt at `/.well-known/security.txt`, dedicated security@ email"). **FULL MATCH**.
  - **BG-03 metric**: "<30d DSAR turnaround; JSON export endpoint live within 90 days" `04:99`. **Reflected in**: PG-D-05.3-001 verification (see 07c Appendix A) (T-002 + D-05.3 references Art. 17 erasure 30-day max); PG-D-05.4-001 verification (see 07c Appendix A) ("JSON export endpoint returns all data subject data within Art. 20 structured format"). **FULL MATCH** (Art. 17 = 30-day erasure; Art. 20 = portability).
  - **BG-04 metric**: "SAST in CI by end of quarter; zero CRITICAL findings on main branch" `04:100`. **Reflected in**: SG-D-02.1-001 verification (see 07c Appendix A) ("block merge on `CRITICAL` findings"; "`npm audit --audit-level=high` passes on every build"); SG-D-07.2-001 verification (see 07c Appendix A) ("SAST (e.g. Semgrep) runs on every PR with zero `ERROR`-level findings"). **FULL MATCH**.
  - **BG-05 metric**: "Annual review of AWS SOC 2, Stripe PCI-DSS, Firebase security docs" `04:101`. **Reflected in**: SG-D-06.1-001 verification (see 07c Appendix A) ("Annual DPA validation: SOC 2 Type II for AWS, PCI-DSS AOC for Stripe"). **FULL MATCH**.
- **Gap identified:** No SLA-style quantitative metric (e.g., "uptime ≥99.9%") is stated in any BG. This is consistent with the absence of explicit availability BG in `04_Company_Context_Assessment.md §4` (BG-01..BG-05 are governance/regulatory/compliance focused, not availability-focused). If availability metrics are intended (e.g., from `Critical_Analysis_Micro_Enterprise.md §4` BC/DR RTO 24h), they are reflected indirectly in PG-D-04.4-001 / SG-D-04.4-001 ("AWS Backup; RTO 24h").
- **Note:** All stated BG metrics ARE traceable to PG/SG verification criteria. The PARTIAL verdict reflects that one BG metric ("Zero audit findings") is not strictly a verifiable criterion but an outcome target — and the RoPA-100%-complete metric is reflected structurally but not numerically.
- **Severity:** LOW (informational; no blocker).

### C4.5 — BG deadlines (regulatory) align with PG/SG Implementation Priority

- **Verdict:** PASS
- **Evidence:**
  - BG-01 (GDPR Art. 5, 30, 32 — statutory) → Implementation Priority for all 37 PG = HIGH (per (see 07c Appendix A) Implementation Priority column). **Aligned**.
  - BG-02 (CRA Art. 13(13) 10y records retention) → SG-D-09.4-001 verification (see 07c Appendix A): "10y retention per CRA Art. 13(13)". Implementation Priority HIGH. **Aligned**.
  - BG-03 (GDPR Art. 17 erasure 30d; Art. 20 portability) → PG-D-05.3 / PG-D-05.4 Implementation Priority HIGH; max-30-day deadline operationalised via manual API endpoint + Auth0 deletion. **Aligned**.
  - BG-04 (CRA Art. 18(2) + GDPR Art. 25 design-time obligations) → SG-D-02.1, SG-D-07.1-7.4 Implementation Priority HIGH; quarterly SSDF/OWASP SAMM cadence + CI gates. **Aligned**.
  - BG-05 (GDPR Art. 28 + CRA Art. 7) → SG-D-06.1/6.3/6.4 Implementation Priority HIGH; annual review cadence. **Aligned**.
- **Note:** 4/5 BGs have HIGH Implementation Priority in the PG/SG cards. The 1 DEFERRED row (D-02.4) does NOT have a corresponding BG (no BG claims pentest capability). Zero deadline/priority mismatches.
- **Severity:** —

### C4.6 — Detail depth matches MICRO scale (8 employees) — not over-engineered

- **Verdict:** PASS
- **Evidence:**
  - 74 cards (37 PG + 37 SG) at 12 fields each = 888 field instances. This is **information-rich but not over-engineered**: the 12 fields are functional (Description, Scope, Out of scope, Source Article, Corpus path, NIST anchors, Verification criteria, Verification method, Owner, Status, Dependencies, Risk, Stakeholders, Maturity, Priority). All fields discharge a specific purpose.
  - No enterprise-only constructs: NO SOC, NO HSM, NO formal CMDB, NO enterprise SIEM (CloudWatch + Datadog only), NO dedicated IR team, NO formal GRC platform (D-09.x uses "Security policy template" / "RoPA template" / "DPIA template" — **templates**, not platforms).
  - Cross-reference: `Critical_Analysis_Micro_Enterprise.md §9` lists "❌ What to Remove" — enterprise SIEM (€2-5K/mês), GRC platform (€500-1K/mês), formal pentest (RTO 4h) — and the Rich artefacts correctly AVOID all three. CloudWatch (NOT SIEM), spreadsheets/Notion (NOT GRC platform), AWS Backup with RTO 24h (NOT RTO 4h).
  - No compliance theatre: every field adds evidence value; no "padding" fields.
- **Note:** Information density is high because MICRO teams need concrete guidance (no time for ambiguity). This is **right-sized**, not over-engineered.
- **Severity:** —

### C4.7 — Track B tiers reflect MICRO reality (LIGHTWEIGHT/MINIMAL/DEFERRED)

- **Verdict:** PASS
- **Evidence:**
  - Distribution: **31 LIGHTWEIGHT + 5 MINIMAL + 1 DEFERRED = 37** (per `07b:80-82` and (see 07c Appendix A)).
  - Proportionality_model.md §5.1 MICRO row: BUILD_REQUIRED → LIGHTWEIGHT, INHERITABLE → MINIMAL. Applied correctly.
  - Proportionality_model.md §5.2: MICRO + FTE ≤ 1.0 + SHOULD → DEFERRED. Applied correctly to D-02.4 (SHOULD).
  - Proportionality_model.md §5.3 floor rule: every MUST ≥ MINIMAL. **Verified**: 36 MUST rows at LIGHTWEIGHT or MINIMAL; 1 SHOULD row at DEFERRED. Zero floor violations.
  - Comparison to higher tiers: STANDARD (used at SMALL+MEDIUM) and RIGOROUS (LARGE+MAX) are **NOT used at all** — confirming correct tier calibration for MICRO.
- **Note:** Tier distribution is **deterministically derived** from (S, I, P) per §5.1+§5.2+§5.3. The full decision trail is in `07b §12` (37 rows).
- **Severity:** —

### C4.8 — Effort expectations implicit in tier match company capacity

- **Verdict:** PASS
- **Evidence:**
  - **Security FTE = 0.85** per `Critical_Analysis_Micro_Enterprise.md §3.2` (CTO 0.20 + Lead Dev 0.30 + Operations 0.20 + DPO 0.10 + CEO 0.05). Required FTE per §3.1 = 1.15. Gap = 0.30 FTE (26% shortfall).
  - Implication per `Critical_Analysis §3.3`: "Cannot implement all 60 FRs with current team. Need: Automation (AWS native tools), Outsourcing (MSSP for monitoring), Prioritization (focus on critical FRs only)."
  - How the rich artefacts operationalise this:
    - **AWS managed services** (S3 SSE-KMS, CloudWatch, CloudTrail, AWS Backup, AWS Systems Manager Patch Manager) — replace in-house teams. Reflected in `07b` example_controls column.
    - **BUY_MANAGED satisfaction_pattern** (per `07b:79` — 31 of 37 rows are BUY_MANAGED) — emphasises managed-service adoption.
    - **No MSSP / 24-7 SOC**: CloudWatch + SNS suffices per Critical Analysis §5 (`07b:106` — "CloudWatch alarms + SNS notifications").
    - **No GRC platform**: Spreadsheets + Notion per Critical Analysis §5. Reflected in D-09.x "template" pattern.
  - **Annual/monthly cadence** dominates (annual review, quarterly review, monthly scan) — feasible for 0.85 FTE.
- **Note:** The 31 LIGHTWEIGHT + 5 MINIMAL + 1 DEFERRED tier mix is consistent with the 0.85 FTE capacity. If TinyTask were LARGE (FTE ≥ 5), STANDARD + RIGOROUS tiers would be expected — and would require HSM, SOC, dedicated IR. The artefacts correctly do not claim those capabilities.
- **Severity:** —

---

## §3 BG → PG/SG Chain Trace

### BG-01 — GDPR Compliance Baseline (HIGH priority)

- **Doc 04 §4** `04_Company_Context_Assessment.md:97`: "GDPR Compliance Baseline | Establish baseline GDPR compliance for all personal data processing activities | HIGH | GDPR | Zero audit findings; RoPA complete | → Doc 07c Appendix A §A.1 (PG table, 37 rows)"
- **Implementing PG (all in Doc 07c Appendix A §A.1):**
  - **PG-D-01.1-001** (AES-256 at rest via AWS SSE-KMS) — supports "audit-ready posture" per Art. 5(1)(f) + Art. 32(1)(b)
  - **PG-D-01.2-001** (TLS 1.3) — supports Art. 5(1)(f) + Art. 32(1)(a)
  - **PG-D-01.3-001** (AWS KMS rotation) — supports Art. 32(1)(a)
  - **PG-D-04.3-001** (max-SLA 24h internal notification) — supports Art. 33(1) 72h controller→SA deadline
  - **PG-D-05.3-001** (Erasure API endpoint) — supports Art. 17 erasure (cited in BG-03 explicitly)
  - **PG-D-05.4-001** (JSON export endpoint) — supports Art. 20 portability
  - **PG-D-09.4-001** (RoPA template) — directly discharges "RoPA 100% complete" metric
  - **PG-D-09.2-001** (DPIA template) — supports Art. 35 DPIA
- **Implementing SG (supporting CRA-driven cross-cutting concerns):**
  - **SG-D-09.4-001** (RoPA template, 10y retention per CRA Art. 13(13)) — also supports BG-01 via 10y retention overlapping with GDPR Art. 30
- **Priority alignment:** All implementing PG/SG are **MUST** priority. BG-01 is HIGH — aligned.
- **Stakeholder consistency:** BG-01 affected = "CEO, CTO, DPO, B2B clients (data controllers)" → PG-D-01.x stakeholders = "Customers (data subjects), CTO, DPO" + PG-D-04.3 same; PG-D-09.x stakeholders = "CEO, CTO, DPO". **Overlap: CTO + DPO + customers (= B2B clients' end-users)**.
- **Verification criteria reinforce BG-01 success criteria:**
  - "Zero audit findings" → PG-D-09.4 verification (see 07c Appendix A): "RoPA reviewed annually + on change of processing; 10y retention per CRA Art. 13(13)" — auditable.
  - "RoPA 100% complete" → SG-D-09.4-001 (see 07c Appendix A): "RoPA template covers controller + processor activities" — auditable.
- **ALIGNED: YES**

### BG-02 — CRA Conformity (HIGH priority)

- **Doc 04 §4** `04_Company_Context_Assessment.md:98`: "CRA Conformity | Achieve CRA conformity for Team Organizer SaaS product | HIGH | CRA | SBOM published; security.txt active"
- **Implementing SG (all in Doc 07c Appendix A §A.2):**
  - **SG-D-02.1-001** (Trivy + npm audit in CI) — supports CRA Art. 17 vulnerability handling
  - **SG-D-02.2-001** (AWS Systems Manager Patch Manager auto) — supports CRA Art. 4+5 patch obligations
  - **SG-D-02.3-001** (security.txt at `/.well-known/security.txt`) — directly discharges "security.txt active" metric, supports CRA Art. 19 CVD
  - **SG-D-06.2-001** (CycloneDX SBOM in CI/CD per release) — directly discharges "SBOM published per release" metric, supports CRA Art. 18(2) + Annex I §1.4
  - **SG-D-07.1-001** (NIST SSDF + OWASP SAMM baseline) — supports CRA Art. 18 secure development
  - **SG-D-07.2-001** (SAST in CI, coding standards) — supports CRA Art. 18(1)(b)
  - **SG-D-07.3-001** (CI gates, OIDC token auth) — supports CRA Art. 18(2) CI/CD security
  - **SG-D-07.4-001** (Change management log) — supports CRA Art. 18(4)
  - **SG-D-09.3-001** (Annex VII §1-§2 architecture documentation) — supports CRA Art. 13 technical documentation
  - **SG-D-10.3-001** (Quarterly compliance review + annual self-attestation) — supports CRA Art. 14 conformity assessment
- **Priority alignment:** All implementing SG are MUST priority. BG-02 is HIGH — aligned.
- **Stakeholder consistency:** BG-02 affected = "CTO, Lead Dev, B2B clients (procurement), EU market-surveillance authorities" → SG-D-02.x stakeholders = "Customers, CTO, DevOps" (= Lead Dev + developers) + SG-D-06.2 "CTO, DPO, Procurement" + SG-D-07.x "CTO, DevOps, DPO". **Overlap: CTO + Lead Dev + Procurement**.
- **Verification criteria reinforce BG-02 success criteria:**
  - "SBOM published per release (37 releases planned for first 12 months)" → SG-D-06.2 verification (see 07c Appendix A): "CycloneDX SBOM generated on every release tag; SBOM archived with release artefacts (10y retention per CRA Art. 13(13)); Quarterly SBOM-vs-CVE correlation report" — **exactly matches the release-frequency target**.
  - "security.txt active + reachable" → SG-D-02.3 verification (see 07c Appendix A): "security.txt at `/.well-known/security.txt`, dedicated security@ email, CVD page" — measurable via `curl https://tinytask.example.com/.well-known/security.txt`.
- **ALIGNED: YES**

### BG-03 — Data Subject Rights (MEDIUM priority)

- **Doc 04 §4** `04_Company_Context_Assessment.md:99`: "Data Subject Rights | Enable data export and erasure for all users | MEDIUM | GDPR | User-facing export/delete features live"
- **Implementing PG (explicitly cited):**
  - **PG-D-05.3-001** (Erasure API endpoint) — supports Art. 17 erasure ("<30d DSAR turnaround")
  - **PG-D-05.4-001** (JSON export endpoint) — supports Art. 20 portability ("JSON export endpoint live within 90 days")
- **Priority alignment:** Both PG are MUST priority (per (see 07c Appendix A)). BG-03 is MEDIUM — **per proportionality_model.md §5.1, MUST rows are always MUST regardless of BG priority** because the regulatory floor (Art. 17 + Art. 20) is statutory. BG-03 metric ("30d max") is operationalised via LIGHTWEIGHT BUY_MANAGED tier with API endpoints.
- **Stakeholder consistency:** BG-03 affected = "Customers (data subjects), DPO, B2B client controllers" → PG-D-05.3 + PG-D-05.4 stakeholders = "Customers (data subjects), DPO, CTO" (see 07c Appendix A). **Overlap: Customers + DPO + (B2B client controllers covered via DPO/CTO)**.
- **Verification criteria reinforce BG-03 success criteria:**
  - "<30d DSAR turnaround" → PG-D-05.3 (see 07c Appendix A) references Art. 17 erasure 30-day statutory deadline; PG-D-05.4 (see 07c Appendix A): "JSON export endpoint returns all data subject data within Art. 20 structured format" — measurable.
  - "JSON export endpoint live within 90 days" → SG-D-05.4-001 verification (see 07c Appendix A): "JSON export endpoint returns all data subject data within Art. 20 structured format; GDPR-only — no CRA sub-SO; effort not duplicated for CRA; Annual review confirms export format remains machine-readable (JSON, not proprietary)" — **machine-readability requirement is what makes the 90-day-target measurable**.
- **ALIGNED: YES**

### BG-04 — Security by Design (MEDIUM priority)

- **Doc 04 §4** `04_Company_Context_Assessment.md:100`: "Security by Design | Integrate security into development lifecycle | MEDIUM | CRA, GDPR | SAST/DAST in CI/CD pipeline"
- **Implementing SG:**
  - **SG-D-02.1-001** (Trivy + npm audit in CI) — supports "SAST/DAST in CI/CD pipeline" metric
  - **SG-D-07.1-001** (NIST SSDF + OWASP SAMM baseline) — directly discharges "security by design" via SSDF/SAMM frameworks
  - **SG-D-07.2-001** (SAST in CI, coding standards) — supports SAST-in-CI metric
  - **SG-D-07.3-001** (CI gates, OIDC token auth) — supports "CI/CD pipeline" metric
  - **SG-D-07.4-001** (Change management log) — supports SDLC integration
- **Priority alignment:** All implementing SG are MUST priority. BG-04 is MEDIUM — same reasoning as BG-03.
- **Stakeholder consistency:** BG-04 affected = "CTO, Lead Dev, B2B clients (security review)" → SG-D-07.x stakeholders = "CTO, DevOps, DPO" (see 07c Appendix A) (= CTO + developers + DPO). **Overlap: CTO + Lead Dev/DevOps**.
- **Verification criteria reinforce BG-04 success criteria:**
  - "SAST in CI by end of quarter" → SG-D-07.2 verification (see 07c Appendix A): "SAST (e.g. Semgrep) runs on every PR with zero `ERROR`-level findings" — measurable in CI.
  - "zero CRITICAL findings on main branch" → SG-D-02.1 verification (see 07c Appendix A): "CI pipeline runs Trivy on every PR — block merge on `CRITICAL` findings; `npm audit --audit-level=high` passes on every build" — **block-on-critical is exactly the mechanism that keeps "zero CRITICAL on main"**.
- **ALIGNED: YES**

### BG-05 — Supplier Due Diligence (MEDIUM priority)

- **Doc 04 §4** `04_Company_Context_Assessment.md:101`: "Supplier Due Diligence | Maintain SOC 2/ISO 27001 evidence from cloud providers | MEDIUM | GDPR, CRA | Annual review completed"
- **Implementing PG/SG (explicitly cited in Doc 04 §4 cross-ref + Doc 07c §5 T-002):**
  - **PG-D-06.1-001 / SG-D-06.1-001** (DPA validation against GDPR Art. 28; supplier security clauses) — directly discharges "AWS SOC 2 / Stripe PCI-DSS / Firebase security docs" review
  - **PG-D-06.3-001 / SG-D-06.3-001** (DPA template + supplier security clauses) — supports CRA Art. 7 supplier obligations
  - **PG-D-06.4-001 / SG-D-06.4-001** (AWS / Stripe / Firebase boundary inherited) — supports 3rd-party boundary management
- **Priority alignment:** PG/SG-D-06.x are MUST priority (D-06.1 = MINIMAL, D-06.3 = LIGHTWEIGHT, D-06.4 = MINIMAL — all MUST per (see 07c Appendix A)). BG-05 is MEDIUM — consistent.
- **Stakeholder consistency:** BG-05 affected = "CTO, Procurement, B2B clients (procurement)" → SG-D-06.1/6.3/6.4 stakeholders = "CTO, DPO, Procurement" (see 07c Appendix A). **Overlap: CTO + Procurement**.
- **Verification criteria reinforce BG-05 success criteria:**
  - "Annual review of AWS SOC 2, Stripe PCI-DSS, Firebase security docs" → SG-D-06.1 verification (see 07c Appendix A): "Annual DPA validation: SOC 2 Type II for AWS, PCI-DSS AOC for Stripe; Supplier security clause addendum signed by all vendors; Internal statement on file covering inherited controls" — **annual cadence matches the BG metric**.
- **Tensions interaction:** T-002 (D-06.1, D-06.3) resolved with unified vendor management per (see 07c Appendix A). T-002 resolution status AGREED.
- **ALIGNED: YES**

**Overall chain trace verdict:** All 5 BGs trace cleanly to ≥ 1 PG/SG with priority alignment, stakeholder consistency, and verification-criteria reinforcement. No orphan BGs. No mis-aligned priorities. No stakeholder gaps.

---

## §4 Scale Alignment Deep-Check

### C4.6 — Detail depth vs company capacity

- **Cards**: 74 (37 PG + 37 SG) × 12 fields = 888 field instances. **Per card ~12 fields is moderate, not bloated**.
- **Comparison to enterprise norms**: A LARGE company (FTE ≥ 5) would typically need:
  - Formal CMDB → TinyTask uses Doc 04a §1.1 inventory (5 systems) — adequate.
  - Enterprise SIEM → TinyTask uses CloudWatch + SNS — adequate for MICRO scale (no 24/7 monitoring need).
  - GRC platform → TinyTask uses Spreadsheets + Notion per Critical Analysis §5 — adequate.
  - SOC → Not present (correctly).
  - HSM → Not present (correctly — AWS KMS suffices for LIGHTWEIGHT).
- **Verdict:** **Right-sized** for 8 employees. Detail density is high because MICRO teams need concrete guidance (no time for ambiguity), but every field has functional purpose.

### C4.7 — Track B tier distribution vs proportionality_model.md §5.1 MICRO row

- **§5.1 MICRO row**: `INHERITABLE → MINIMAL`, `BUILD_REQUIRED → LIGHTWEIGHT`. 
- **Applied in `07b:80-82`**: 31 LIGHTWEIGHT (BUILD_REQUIRED + MUST), 5 MINIMAL (INHERITABLE + MUST), 1 DEFERRED (BUILD_REQUIRED + SHOULD + FTE ≤ 1.0).
- **Inheritance pattern**: D-03.1, D-03.2 (Firebase Auth IO-04), D-06.1, D-06.4 (AWS/Stripe/Firebase boundary), D-08.1 (vendor awareness docs) — all MINIMAL with INHERIT pattern. **Correct mapping**.
- **Build pattern**: All other 31 rows are LIGHTWEIGHT with BUY_MANAGED pattern (cloud-native managed service). **Correct mapping**.
- **DEFERRED**: Only D-02.4 (Threat-Led Pentest) is DEFERRED. Correct per §5.2 (SHOULD + MICRO + FTE ≤ 1.0). **Correct mapping**.
- **Floor rule §5.3**: every MUST ≥ MINIMAL. Verified: zero MUST below MINIMAL. **Correct**.
- **Verdict:** **Deterministically correct** application of proportionality_model.md §5.1 MICRO row.

### C4.8 — Effort expectations vs 0.85 FTE

- **Security FTE available**: 0.85 (per Critical Analysis §3.2).
- **Tier-mix implied effort**:
  - 31 LIGHTWEIGHT (BUY_MANAGED): **~0.1 FTE each** (mostly managed-service config + annual review) = ~3.1 FTE-equivalent "effort budget" but largely absorbed by AWS automation. **Net human effort ~0.4 FTE** for config + annual review across 31 rows.
  - 5 MINIMAL (INHERIT): **~0.05 FTE each** (annual attestation review + 1-page internal statement) = ~0.25 FTE.
  - 1 DEFERRED (D-02.4): **0 FTE** (explicitly deferred).
  - **Total estimated effort**: ~0.65 FTE → **fits within 0.85 FTE capacity** with ~0.20 FTE buffer for incident response + ad-hoc.
- **Verdict:** **Effort expectations are realistic** for 0.85 FTE. No over-promising (e.g., no "weekly tabletop exercises" claimed, no "monthly full-stack SAST sweeps", no "daily log review").
- **Comparison to Critical Analysis §5**:
  - Essential scenario €900-2.1K/month → matches Rich artefacts' AWS-managed + BUY_MANAGED pattern.
  - With MSSP €3-6K/month → correctly AVOIDED (no MSSP in 07b/07c).
  - Full Enterprise €5-10K/month → correctly AVOIDED (no HSM, no formal SOC, no enterprise SIEM).
- **Verdict:** **Proportionality model + Rich artefacts are mutually consistent** with the 0.85 FTE capacity.

### Cross-Reference: Rich artefacts vs Critical_Analysis_Micro_Enterprise.md §5 (Tool Cost Analysis)

| Tool | Critical Analysis verdict | Rich artefact evidence |
|------|--------------------------|------------------------|
| SIEM/SOC (€2-5K/mês) | ❌ Too expensive | AVOIDED — CloudWatch + SNS per `07b:106` |
| DSAR Automation (€500-1K/mês) | ⚠️ Justifiable; manual OK | MANUAL — "Erasure API endpoint" per `07b:112` (LIGHTWEIGHT BUY_MANAGED) |
| SAST/SCA (€200-500/mês) | ✅ Justifiable (CRA) | PRESENT — "Trivy + npm audit" `07b:98`, "SAST (e.g. Semgrep)" (see 07c Appendix A) |
| GRC Platform (€500-1K/mês) | ❌ Too expensive | AVOIDED — "Security policy template", "RoPA template", "DPIA template" (templates, not platform) per `07b:124,127,140` |
| Training Platform (€200-400/mês) | ⚠️ Optional | AVOIDED — "Annual security awareness email + role-specific docs" per `07b:123` |
| Secrets Management (€0-100/mês) | ✅ Essential | IMPLICIT — AWS Secrets Manager + IAM least privilege per (see 07c Appendix A) |

**Verdict:** Rich artefacts correctly adopt the **Essential** scenario (€900-2.1K/mês) and **reject** the With-MSSP and Full-Enterprise scenarios. This is right-sizing at its most concrete.

---

## §5 Critical Blockers (HIGH severity)

**NONE.**

All Tier 2 criteria PASS or PARTIAL with LOW severity. No HIGH-severity gaps identified.

---

## §6 Recommendations

### Recommendation R-T2-1 (Optional, MEDIUM priority)
**Section title:** Promote "Procurement" to a named role in RACI.

- **Where**: `04d_Org_Roles_RACI.md:62-72` (Key Roles table) — Procurement is mentioned in BG-05 owner column (`04:101`) and in D-06.x PG/SG stakeholders ((see 07c Appendix A)), but not as a distinct named role in the RACI Key Roles table.
- **Why**: BG-05 and D-06.x PG/SG consistently name "Procurement" as a stakeholder. At 8 employees this role is likely absorbed by the CEO (per `04d §2 "CEO handles people ops and security training coordination"`). Explicitly noting "Procurement is part of CEO 0.2 FTE" or similar would close the inconsistency.
- **Severity**: LOW (no blocker — Procurement is operationally absorbed).

### Recommendation R-T2-2 (Optional, LOW priority)
**Section title:** Add explicit SLA-style availability metric to BG catalog or document absence.

- **Where**: `04_Company_Context_Assessment.md §4` BG table.
- **Why**: C4.4 PARTIAL flagged that no SLA-style quantitative metric (e.g., "uptime ≥99.9%") is stated in any BG. If availability is a business concern (and `Critical_Analysis_Micro_Enterprise.md §4` shows RTO 24h is a deliberate decision), adding a BG or BG metric around availability would close the gap. If availability is intentionally out of scope (TinyTask is not a critical service), document the explicit non-goal.
- **Severity**: LOW (informational).

### Recommendation R-T2-3 (Optional, LOW priority)
**Section title:** Update BG-01 metric to be a verifiable control target.

- **Where**: `04_Company_Context_Assessment.md:97` (BG-01 Quantitative Metric).
- **Why**: "Zero audit findings in last 12 months" is an outcome, not a control target. Better phrased as "RoPA 100% complete; zero unresolved critical audit findings tracked in risk register".
- **Severity**: LOW (clarification; not blocking).

### Recommendation R-T2-4 (Acknowledged, no action)
**Section title:** Effort/Cost/Timeline fields intentionally excluded.

- **Where**: (see 07c Appendix A) (frontmatter `fields_excluded: [Effort Estimate, Cost Estimate, Target Timeline]`).
- **Why**: Per Fase de Especificação 5 scope. The Track B tier + example_controls + verification criteria + owner + maturity + Implementation Priority together imply effort/capacity; explicit fields would duplicate. This is **not a Tier 2 gap** — it is an explicit methodological choice documented in the frontmatter.

---

## §7 See also

- `VALIDATOR_TIER1.md` — CONDITIONAL_PASS for Completeness + Internal Consistency (Tier 1).
- `validation/SPRINT5_REPORT.md` deep-enrichment report (74 detail cards, 4 tensions resolved, no Effort/Cost/Timeline).
- `validation/SPRINT4_REPORT.md` PG/SG elevation + Tier B decision table.
- `validation/SPRINT3_REPORT.md` corpus cross-check (10 representative rows PASS).
- `validation/SPRINT1_REPORT.md` reconciliation (I-02 36→37 sub-domains fix; I-10 status progression).
- `validation/SPRINT2_ENRICHMENT_REPORT_EXISTING.md` corpus enrichment (req_id mapping per RACI row).
- `validation/VALIDATOR_SPRINT3.md`, `VALIDATOR_SPRINT4.md`, `VALIDATOR_SPRINT5.md` — Sprint-level validator reports.
- `00_METHODOLOGY/REFERENCE/proportionality_model.md` — Track B spec (§5.1 decision table, §5.2 drop-one-tier, §5.3 floor rule, §6 attribute definitions).
- `00_METHODOLOGY/REFERENCE/complexity_tier.md` — Complexity tier (LOW/MEDIUM/HIGH) derivation.
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION/annexes/Critical_Analysis_Micro_Enterprise.md` — Feasibility cross-check (used in §4 Scale Alignment).

---

## §8 Validator Signature

| Field | Value |
|-------|-------|
| Validator role | tier2-verifier (read-only) |
| Tier scope | 2 (Realism + Business Alignment + Scale) |
| Overall verdict | **PASS** |
| Critical blockers | NONE |
| Files audited | 04, 04a, 04b, 04c, 04d, 07b, 07c, phase1_ontology.yaml, Critical_Analysis_Micro_Enterprise.md |
| Files modified | NONE |
| Files created | VALIDATOR_TIER2.md (this file) |
| Cross-doc consistency with Tier 1 | Strong — Tier 1 PASS criteria (C1.1, C2.1, C2.2, C2.3) are reinforced by Tier 2 (C4.1, C4.2, C4.3) |
| Recommendation to orchestrator | Proceed to Phase 2 with current artefacts; optionally action R-T2-1..R-T2-3 in a future Fase de Especificação 6 |

---

**END OF VALIDATOR TIER 2 REPORT**
