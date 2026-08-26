---
document_id: AEGIS-P2-RICH-VALIDATOR-TIER2
title: Validator Tier 2 — Case_02 Phase 1 Rich
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-06
author: Sprint Validator (tier2-verifier)
status: FINAL
case: Case_02_SecureBorder_Solutions
tier: 2 (Realism + Business Alignment + Scale)
---

# Validator Tier 2 — Case_02 Phase 1 Rich

> Tier 2 = Realism / Company-Specificity + Business Alignment + Scale Alignment.
> Tier 1 (Completeness + Internal Consistency) verified in parallel.
> Read-only independent verification of the Case_02 Phase 1 Rich corpus. No source files modified.

## §1 Summary

| Tier 2 Criterion | Verdict | Severity |
|-----------------|---------|----------|
| C3.1 example_controls mention concrete tools | **PASS** | — |
| C3.2 Verification criteria are checkable | **PASS** | — |
| C3.3 Owner roles reflect real org chart | **PASS** | — |
| C3.4 Affected Stakeholders include real external roles | **PASS** | — |
| C3.5 Affected Stakeholders appropriate for sector | **PASS** | — |
| C3.6 Documents reference real infrastructure | **PASS** | — |
| C4.1 Each BG has ≥ 1 PG or SG aligned | **PARTIAL** | M |
| C4.2 PG/SG priority aligns with BG priority | **PASS** | — |
| C4.3 Stakeholders of BG overlap with PG/SG | **PASS** | — |
| C4.4 Quantitative metrics of BG reflected in PG/SG verification | **PARTIAL** | L |
| C4.5 BG deadlines align with PG/SG Implementation Priority | **PASS** | — |
| C4.6 Detail depth matches MEDIUM scale | **PASS** | — |
| C4.7 Track B tiers reflect MEDIUM (8 RIGOROUS + 27 STANDARD) | **CONDITIONAL_PASS** | H (provisional — see F-01) |
| C4.8 Effort expectations implicit in tier match capacity | **PASS** | — |

**Overall Tier 2 verdict: CONDITIONAL_PASS** — strong realism, business alignment, and scale proportionality overall; one HIGH-severity open item (Doc 07b §11.3 F-01, Scale-input contradiction) that makes the Track B tier distribution provisional, and one MEDIUM gap (BG-005/006/007 lack explicit PG/SG mapping). No realism/company-specificity failures.

---

## §2 Per-Criterion Detail

### C3.1 — example_controls mention concrete tools (not generic "security tools")

- **Verdict:** **PASS**.
- **Evidence (cross-document, sampled):**
  - **HSM cluster (concrete vendor + certification):** `04a §1.1` SYS-07 = "FIPS 140-2 Level 3 HSM cluster (Thales / Utimaco) in EU; key ceremonies quarterly"; `04a §1.3` cloud table row 2 = Thales/Utimaco HSM cluster. Repeated in `04b §2 D-01 (target 4)` and `07b §4 D-01.1` "FIPS 140-2 Level 3 HSM".
  - **Dedicated IAM (not generic):** `07b §4 D-03.1` "Dedicated IAM (SailPoint/Keycloak) — NOT Firebase INHERIT"; `04d §2 Key Roles` reflects dedicated CISO + DPO + AI Governance Lead + SOC Manager + IR Lead; `07c PG-D-03.1` and PG-D-03.2 reference SCIM provisioning + FIDO2/YubiKey hardware MFA.
  - **SOC tooling (named products):** `04a §1.1` SYS-12 = "Splunk ES + CrowdStrike Falcon EDR + Tenable Nessus + custom playbooks; 24/7 staffed"; `04b §2 D-04` "Splunk Enterprise Security SIEM (13 SOC analysts 24/7; 4 across 3 shifts + 1 on-call) + CrowdStrike Falcon EDR + Tenable vulnerability feed + custom ML anomaly detection".
  - **CI/CD + SBOM (specific tools):** `04a §1.1` SYS-11 = "GitHub Enterprise + Jenkins + JFrog Artifactory (EU); CycloneDX SBOM emission per release; cosign-signed OTA packages"; `07b §4 D-07.3` "SLSA Level 3" and `07c PG-D-07.3` "Trivy + npm audit + cosign + SBOM gate".
  - **Edge AI stack:** `04a §1.1` SYS-04 = "ARM SoC, TensorRT-accelerated CNN face match + liveness, TPM 2.0 secure boot, signed firmware".
  - **Backup backhaul:** `04a §1.3` "T-Systems / Deutsche Telekom | Managed private 5G / LTE".
  - **Static analysis (specific tool):** `07b §4 D-07.2` "SAST (Semgrep) + DAST in CI; secure coding standards; OWASP SAMM Level 2 for AI components; pre-commit secret scanning".
  - **Pen test accreditation (named):** `04b §2 D-02` "Annual external (CREST-accredited) pen test + 6-monthly internal red team exercises"; `07b §4 D-02.4` "CREST/OSCP-accredited testers".
- **Gap / Severity:** None. Tools are product-named (Thales, Utimaco, AWS, Splunk, CrowdStrike, Tenable, Okta, GitHub, Jenkins, JFrog, SailPoint, Keycloak, Semgrep, Trivy, CycloneDX, cosign, TensorRT, YubiKey, FIDO2, TPM 2.0, T-Systems, Snyk, SAP S/4HANA), not placeholder labels.

### C3.2 — Verification criteria are checkable (specific audit procedures, KPI tests, etc.)

- **Verdict:** **PASS**.
- **Evidence:**
  - **Operational KPI tests (concrete numbers):** `07c §8 PG-D-04.3` "Mean-time-to-detect (MTTD) tracked quarterly"; `07c PG-D-04.4` "RTO 24h, RPO 1h, immutable backup with 10-year retention"; `07c PG-D-01.1` "AES-256-GCM cipher confirmed on every at-rest eGate kiosk datastore via cryptographic configuration audit"; `07c PG-D-03.1` "Quarterly access reviews cover all biometric-data scopes with documented sign-off by DPO".
  - **Audit procedures (specific + testable):** `07c PG-D-01.3` "De-attribution test procedure documented and executed at least once per year"; `07c PG-D-02.4` "Annual external pen test by CREST/OSCP-accredited testers with publicly available executive summary"; `07c PG-D-04.1` "Detection capability tested annually via tabletop exercise with documented detection outcomes".
  - **Tension-resolution tests:** `07c §4 T-002` "Erasure endpoint demonstrates biometric↔identity mapping destroyed via HSM key destruction; audit log retains anonymised trail; re-identification attempt fails (documented test); AI_Act log integrity verified via hash chain"; `07c §4 T-001` "Tabletop exercise demonstrating 24h delivery to DPA, ENISA, CSIRT, and Notified Body on a single timeline; quarterly review of the routing pipeline; annual audit (RIGOROUS tier)".
  - **BG-level KPIs (Doc 04 §4):** BG-003 "MTTD/MTTR/24h routing pipeline test pass-rate"; BG-004 "DPO oversight hours; DPIA refresh cadence; Art. 9 violation count"; BG-005 "Uptime %; SLA breach count; MTTR for service incidents"; BG-007 "Surveillance audit pass-rate; non-conformity count".
- **Gap / Severity:** None.

### C3.3 — Owner roles reflect real org chart

- **Verdict:** **PASS**.
- **Evidence:** `04d §2 Key Roles` enumerates 22 named roles with FTE allocation, backup, and reporting lines. Required personas all present:
  - **CISO** (1.0 FTE + 25-person security team) — required by ISO 27001 + NIS 2 supplier obligations.
  - **DPO** (1.0 FTE + 3-person privacy team; Art. 37(1)(c) mandatory) — independent access to CEO per Art. 38(3).
  - **AI Governance Lead** (1.0 FTE + 4-person AI-governance team incl. AI Bias & Robustness Specialist) — required by AI_Act Art. 9 risk-management.
  - **SOC Manager + IR Lead** (13-person SOC, 4 shifts × 3 + 1 on-call) — NIS 2 Art. 23(4)(a) named-point-of-contact for 24h notification.
  - **Internal Audit Lead** (3-person team reporting to Audit Committee) — ISO 27001 surveillance + NIS 2 + AI_Act internal audit.
  - **External Legal Counsel** (multi-jurisdiction retainer, NL primary + EU coverage).
  - **CTO + Engineering leads** (Edge AI + Hardware + DevSecOps + ML + Integration = ~30 people).
  - **CFO + Procurement Director** (5-person procurement team); **COO + HR Director** (8-person HR team); **5-director Management Board** incl. Non-Exec with border-security industry experience.
- **Gap / Severity:** None. `04d §7 GAP-RACI-01 to -05` openly lists 5 LOW-severity risk-accepted items (e.g., "Acting DPO legally suboptimal" risk-accepted by Board). This is P0 (Reasoned Disagreement) honoured — gaps are surfaced, not hidden.

### C3.4 — Affected Stakeholders include real external roles

- **Verdict:** **PASS**.
- **Evidence (real external roles, not placeholders):**
  - `04 §3.1 Stakeholder Register` SH-006 through SH-013: Government Contract Managers, Border Control Authorities, Airport Operators, Cloud Provider (EU), Hardware Suppliers, **Notified Body (CRA)**, **National CSIRT**, Data Subjects (Travelers).
  - `04c §5 Regulators, Notified Bodies, Sub-DPA Chain`: Government Authority Data Controller (per country), **National CSIRT (NCSC NL, BSI DE)**, **Notified Body (CRA Critical Class)**, **AI_Act Notified Body (Annex III)**, **ENISA**.
  - `07c §8` per-card "Affected Stakeholders": CISO + DPO + AI Governance Lead + travelers + Regulators (DPA, ENISA, CSIRT) consistently.
  - `04 §6.5 AI_Act`: **AI Supervisory Authority**, **Notified Body**.
  - `05 §3.3 NIS 2`: **CSIRT or competent authority** (per Member State).
  - `05 §3.2 CRA`: **Notified Body**.
- **Gap / Severity:** None. EDPB not named verbatim (the EDPB equivalent per jurisdiction is the DPA), but per-Member-State DPAs are listed. ENISA + AI Supervisory Authority + market surveillance authority + notified body (CRA + AI_Act) all appear by name.

### C3.5 — Affected Stakeholders appropriate for sector (defense/border control/eGate)

- **Verdict:** **PASS**.
- **Evidence:**
  - **Defense / border-control sector relevance:** `04 §3.2 SH-006 Government Contract Managers (High Influence)`, `SH-007 Border Control Authorities (High Influence)` — correctly identified as High Influence. SH-013 Data Subjects (Travelers) High Influence on fundamental rights grounds.
  - **eGate kiosk sector:** `04c §5` row 1 "Government Authority Data Controller (per country) — Data controller (per GDPR Art. 4(7)); regulates SecureBorder's deployments | Biometric templates (transient), passport data, match decisions | Bilateral DPA per country + ENISA-aligned cross-border SCCs | Multiple authorities (DE, NL, FR, IT, ES, AT present in current deployments; expand to 5 additional Schengen countries per BG-006)" — correctly captures the multi-jurisdiction Schengen reality.
  - **NIS 2 supplier (not direct entity):** `04 §6.3` obligated party = "ESSENTIAL_ENTITY_SUPPLIER" — correctly identifies that SecureBorder is a supplier to essential entities, not an essential entity itself, which is the right classification for a 450-person border-control supplier.
  - **AI_Act Annex III:** `05 §3.5` correctly identifies "Provider (High-Risk AI System per Annex III)" with explicit reference to Annex III §1 (biometric) + §7 (border control).
  - **Schengen border policy (not just generic EU):** `04a §1.2` "vendor-managed private LTE/5G" + `04a §1.3` "T-Systems / Deutsche Telekom" (German telco) reflects the realistic Schengen/eGate backhaul dependency.
- **Gap / Severity:** None.

### C3.6 — Documents reference real infrastructure (HSM, biometric, Edge AI on kiosks, government watchlist)

- **Verdict:** **PASS**.
- **Evidence:**
  - **HSM-backed KMS for biometric key custody:** `04a §1.1 SYS-07` + `STORE-05 Biometric template cache (transient, on-kiosk only)` + `04b §2 D-01` and `07b §4 D-01.1/D-01.3` (both RIGOROUS). AES-256-GCM with HSM-bound CMK (not just "encryption") — concrete.
  - **Edge AI inference engine (specific stack):** `04a §1.1 SYS-04` = "ARM SoC, TensorRT-accelerated CNN face match + liveness, TPM 2.0 secure boot, signed firmware". Specific hardware (ARM SoC) + AI runtime (TensorRT) + secure boot (TPM 2.0) — not generic "Edge AI".
  - **Government watchlist data (specific pattern):** `04a §1.1 SYS-03` = "Bilateral sFTP feed for judicial + immigration watchlists; HSM-bound decryption"; `04a §2.3 Watchlist data` legal basis `Art. 6(1)(c) and (e)`; `04a §2.1 STORE-03` watchlist cache "isolated VPC subnetwork; air-gap-style ingress controls (only SYS-02 + SYS-04 read endpoints)".
  - **mTLS over QUIC, kiosk outbound-only:** `04a §1.2 Network Topology` "All kiosk-to-cloud traffic is mTLS over QUIC; the kiosk maintains an outbound-only persistent channel — it does not accept inbound network connections" — realistic kiosk hardening.
  - **Government authority as controller (not SecureBorder):** `04 §6.1 GDPR` "SecureBorder is a processor (for government biometric data)" — correctly maps the controller-processor relationship for Art. 28 DPA.
  - **Architecture matches real kiosk deployment:** 13 systems SYS-01..SYS-13 with concrete tech stacks (AWS Frankfurt, Okta, Splunk Cloud EU, CrowdStrike, Snyk, JFrog, GitHub, T-Systems/Deutsche Telekom, Thales/Utimaco HSM) — these are the actual vendor products that eGate-class vendors use.
- **Gap / Severity:** None. Infrastructure naming is concrete and vendor-accurate.

### C4.1 — Each BG has ≥ 1 PG or SG aligned (no orphan BGs)

- **Verdict:** **PARTIAL**.
- **Evidence (7 BGs total per Doc 04 §4 BG-001..BG-007):**
  - **BG-001 (CRA Critical Class) →** Doc 07 §6.1 "D-02, D-06.2, D-07, D-09.1" + Doc 07b §4 RIGOROUS overrides D-06.3 + D-07.1 cover BG-001. **MAPPED**.
  - **BG-002 (AI_Act conformity) →** Doc 07 §6.1 "D-07.1, D-09.1, D-09.2, D-10.3" + SG-D-07.1 (RIGOROUS — AI_Act risk mgmt) + SG-D-09.2 (DPIA+FRIA per T-003) + SG-D-10.1 (post-market monitoring). **MAPPED**.
  - **BG-003 (NIS 2 24h) →** Doc 07 §6.1 "D-04.1, D-04.3, D-10.1" + PG-D-04.3 (RIGOROUS — max-SLA 24h routing per T-001). **MAPPED**.
  - **BG-004 (GDPR Art. 9) →** Doc 07 §6.1 "D-05, D-09.4, D-10.2" + PG-D-01.1 (RIGOROUS — biometric HSM) + PG-D-05.1 (biometric ephemeral) + SG-D-05.3 (cryptographic sharding per T-002). **MAPPED**.
  - **BG-005 (99.99% uptime SLA) →** NOT explicitly listed in Doc 07 §6.1 BG table (which stops at BG-004). Implicit coverage: `04 §7 AI-003` architectural implication notes "BG-003 (NIS 2), BG-005 (99.99%)"; `04a §1.4 SYS-12` SOC tooling for availability; `04b §2 D-04` "RTO 4h, RPO 15min; immutable backup via SYS-01 + STORE-02 + cross-region replication ... Critical Class CRA + 99.99% SLA for airport ops requires tested sub-4h recovery"; PG-D-04.4 (RTO 24h, RPO 1h) — but 99.99% uptime is not a discrete PG/SG. **IMPLICIT ONLY**.
  - **BG-006 (5 Schengen countries expansion) →** NOT explicitly listed in Doc 07 §6.1. Implicit coverage: `04 §7 AI-005` "dataResidency + tenantArchitecture ... BG-006 (Schengen expansion)"; `04c §5 GAP-TPL-04` "5 additional Schengen countries expansion pending country-by-country DPA in BG-006 (18-month expansion project)" links to D-06.1, D-06.3. PG-D-06.3 (RIGOROUS — DPA chain) covers it generically; no Schengen-specific PG/SG exists. **IMPLICIT ONLY**.
  - **BG-007 (ISO 27001 certification maintenance) →** NOT explicitly listed in Doc 07 §6.1. Implicit coverage: `04 §9` "ISO 27001 Maintenance CERTIFIED (annual surveillance)"; `04b §2 D-09` "ISO 27001 v4.7 policy set with full Annex A coverage"; SG-D-09.1 "ISO 27001 certified ISMS discharges all four on a single policy artefact". But SG-D-09.1 is not the maintenance-of-certification objective per se; no PG/SG specifically anchors "annual surveillance audit pass-rate". **IMPLICIT ONLY**.
- **Gap / Severity:** MEDIUM — three BGs (BG-005, BG-006, BG-007) lack explicit mapping rows in Doc 07 §6.1 or a dedicated PG/SG. The implicit coverage via PG/SG on D-04.4 / D-06.3 / D-09.1 is reasonable but the BG → PG/SG chain is not closed. Recommend explicit rows in Doc 07 §6.1 or 07c for BG-005 (uptime SLA → PG-D-04.4 + PG-D-10.1), BG-006 (Schengen → PG-D-06.3 + new PG if needed), BG-007 (ISO 27001 surveillance → PG-D-09.1 + new PG/SG if needed).

### C4.2 — PG/SG priority aligns with BG priority

- **Verdict:** **PASS**.
- **Evidence:**
  - All 4 HIGH/CRITICAL BGs (BG-001/002/003/004) map to sub-domains where ALL relevant PG/SG are at P0/MUST priority (per `07c §5 Track B Decision Trail` and Doc 07b §4). No P1/P2 row implements a CRITICAL BG.
  - RIGOROUS tier is reserved for the 4 critical sub-domains that implement the 4 critical BGs (D-01.1 biometric encryption → BG-004; D-01.3 key custody → BG-004; D-04.3 24h notification → BG-003; D-06.1/D-06.3 supply chain → BG-002/004 AI_Act supply-chain clauses; D-07.1 secure-by-design → BG-002; D-07.3 CI/CD → BG-002 SBOM-Annex III; D-10.1 monitoring → BG-002 post-market).
  - Implementation priorities: Doc 04b §4 ranks top 5 gaps (D-07, D-10, D-03, D-04, D-09) all aligned with HIGH/CRITICAL BG priorities.
- **Gap / Severity:** None.

### C4.3 — Stakeholders of BG overlap with Stakeholders of PG/SG

- **Verdict:** **PASS**.
- **Evidence:**
  - BG-001 owner = "CTO + Notified Body project lead"; stakeholders include "ENISA, government customers". PG/SG-D-07.1 (RIGOROUS) owner = CISO + CTO with AI Governance Lead + Legal + Notified Body in stakeholder set (per `07c §8 PG/SG-D-07.1`). CTO ↔ CTO. Notified Body ↔ Notified Body (Notified Body coordination row in `04d §4.6` RACI). Government customer ↔ government customer (implied via SYS-02/SYS-03 government data sources). **CONSISTENT**.
  - BG-002 owner = "AI Governance Lead + CTO"; stakeholders = "AI Governance Lead, CTO, DPO, Notified Body, AI Supervisory Authority". PG/SG-D-07.1 + SG-D-09.2 + SG-D-10.1 all include AI Governance Lead as A/R and DPO as C/A. **CONSISTENT**.
  - BG-003 owner = "CISO + SOC"; stakeholders = "CISO, SOC, DPO, CSIRT, CEO". PG-D-04.3 owner = CISO, SOC, DPO; affected stakeholders = "Regulators (DPA, ENISA, CSIRT), Internal: CISO, SOC". CEO mentioned in D-08.3 (board briefing). **CONSISTENT**.
  - BG-004 owner = "DPO + Legal Counsel"; stakeholders = "DPO, travelers (data subjects), DPA, CEO". PG-D-01.1/D-01.3 owner = CISO; DPO = C. PG/SG-D-05.1 owner = DPO. Affected stakeholders include travelers + DPA + CISO + DPO. **CONSISTENT**.
- **Gap / Severity:** None.

### C4.4 — Quantitative metrics of BG reflected in PG/SG verification criteria

- **Verdict:** **PARTIAL**.
- **Evidence:**
  - **BG-005 "99.99% uptime" →** PG-D-04.4 "RTO 24h, RPO 1h" — the 24h RTO supports 99.99% but is not a 1:1 reflection. PG-D-10.1 "MTTD tracked quarterly" indirectly supports uptime but is not uptime-specific. **PARTIAL** (not a discrete PG/SG for uptime).
  - **BG-001 "Time to certification (months); conformity assessment pass-rate" →** SG-D-10.3 "Annual ISO 27001 surveillance audit + AI_Act conformity re-assessment"; PG-D-07.1 "Threat model per feature ... AI_Act risk management system". Conformity assessment is the trigger for certification but pass-rate is not explicitly a verification criterion. **PARTIAL** (certification time + pass-rate are BG KPIs not mirrored as discrete verification criteria).
  - **BG-002 "post-market monitoring uptime" →** SG-D-10.1 (RIGOROUS) "AI_Act Art. 72 post-market monitoring ... AI model drift detection ... serious-incident detection (Art. 73)". **MAPPED** — the monitoring uptime maps to AI_Act Art. 72 monitoring system.
  - **BG-003 "MTTD/MTTR/24h routing pipeline test pass-rate" →** PG-D-04.3 verification criteria "Mean-time-to-detect (MTTD) tracked quarterly"; "Multi-reg max-SLA 24h routing" (T-001 resolution); SG-D-04.3 "24h clock; AI_Act 2d widespread-infringement sub-workflow attached; 4h containment playbook gates the 24h notification decision; per-recipient evidence packs ... quarterly tabletop exercise verifies the 24h delivery". **MAPPED**.
  - **BG-006 "Country certifications obtained; revenue from new countries" →** Not directly mirrored as verification criteria in any PG/SG. The country DPA chain (PG-D-06.3) is the legal vehicle but country-by-country certification pass-rate is not a tracked verification criterion. **GAP**.
  - **BG-007 "Surveillance audit pass-rate; non-conformity count" →** SG-D-09.1 "ISO 27001 certified ISMS discharges all four on a single policy artefact" + PG-D-10.3 "Annual ISO 27001 surveillance audit + DPIA re-assessment + GDPR Art. 35(11) review on material change; CISO sign-off". Surveillance audit is captured but pass-rate / non-conformity count are BG KPIs not explicitly mirrored. **PARTIAL**.
  - **BG-008 (AI false match rate <0.1%) →** explicitly moved to Phase 3 per Doc 04 §4 (not a Phase 1 PG/SG concern).
- **Gap / Severity:** LOW. BG quantitative metrics are partially mirrored. The most operational KPIs (MTTD/MTTR/24h, post-market monitoring uptime, RTO/RPO) are well-mapped. The BG-level strategic KPIs (certification months, country cert pass-rate, surveillance audit pass-rate, 99.99% uptime) are not directly mirrored as verification criteria in PG/SG. Recommended: add BG-005 → PG-D-04.4 + PG-D-10.1 explicit cross-reference row in Doc 07 §6.1; BG-007 → PG-D-10.3 explicit "ISO 27001 surveillance pass-rate + non-conformity count" verification criteria.

### C4.5 — BG deadlines (regulatory) align with PG/SG Implementation Priority

- **Verdict:** **PASS**.
- **Evidence:**
  - **CRITICAL BGs (BG-001/002/004) →** P0 implementation priority in `07c §5` Track B Decision Trail for D-01.1, D-01.3, D-04.3, D-06.1, D-06.3, D-07.1, D-10.1 (the RIGOROUS rows aligned with the 4 critical BGs).
  - **HIGH BG (BG-003 NIS 2) →** P0 (D-04.3 RIGOROUS for max-SLA 24h routing).
  - **HIGH BG (BG-007 ISO 27001) →** P1/P2 mapping via D-09.1 (STANDARD) + D-10.3 (STANDARD) — appropriate since ISO 27001 is a maintenance activity, not a project deadline. Not a regulatory deadline but a continuous certification.
  - **MEDIUM BG (BG-006 5 Schengen countries, 18-month project) →** P1 implementation priority across D-06.1, D-06.3 per GAP-TPL-04 in `04c §9` — appropriate for medium-priority MEDIUM BG.
  - **HIGH BG (BG-005 99.99% uptime) →** implicit P1/P2 mapping to D-04.4 + D-10.1 — appropriate for SLA maintenance (continuous, not deadline-driven).
- **Gap / Severity:** None.

### C4.6 — Detail depth matches MEDIUM scale (450 emp, €120M, ISO 27001 certified)

- **Verdict:** **PASS**.
- **Evidence:**
  - **Doc coverage depth:** 35 active sub-domains × (1 PG + 1 SG + verification criteria + owner + status + dependencies + risk + stakeholders + maturity + implementation priority) = ~70 detailed cards with multi-paragraph descriptions (per `07c §8 DEEP Detail Cards`).
  - **Maturity scale used consistently:** `04b §3` summary dashboard shows current 3.0 / target 3.3 / overall gap 0.3 — moderate maturity profile consistent with ISO 27001 certified MEDIUM-tier org (not over-engineered like MAX, not under-developed like MICRO).
  - **Companion to legacy:** The Rich copy is structurally deeper than `01_PHASE1_CONTEXT/` legacy (e.g., legacy 04a is 33KB vs Rich 04a at 55KB with 13 systems / 7 stores / 12 flows + corpus enrichment + §4 Corpus Provenance) — appropriate enrichment depth for a MEDIUM-tier company with HIGH regulatory complexity (4 regulations).
  - **No over-engineering:** HSM + SIEM + EDR + dedicated 25-person security team + dedicated DPO + dedicated AI Governance Lead are realistic for a 450-person MEDIUM org with €120M revenue. No mention of CISO-as-a-service, fractional CISO, or shared SOC — appropriate full-time functional structure.
- **Gap / Severity:** None.

### C4.7 — Track B tiers reflect MEDIUM (8 RIGOROUS + 27 STANDARD expected for MEDIUM)

- **Verdict:** **CONDITIONAL_PASS**.
- **Evidence:**
  - `07b §3` distribution: **8 RIGOROUS + 27 STANDARD = 35 total**. Matches expected MEDIUM + BUILD_REQUIRED + MUST = STANDARD baseline + 8 RIGOROUS overrides for the 8 critical sub-domains (D-01.1, D-01.3, D-04.3, D-06.1, D-06.3, D-07.1, D-07.3, D-10.1).
  - The 8 RIGOROUS overrides are documented and justified per `07b §3` "RIGOROUS override list".
  - **BUT — `07b §11.3 F-01 MAJOR finding still open:** "Scale input contradicts proportionality_model.md §2. The model's table reads MEDIUM = ≤250 employees, <€50M revenue and LARGE = >250 employees, ≥€50M. SecureBorder is 450 employees / €120M revenue, which is LARGE on both axes (1.8× the employee ceiling, 2.4× the revenue ceiling)." Doc 04 §2 itself records size as "Medium-Large". If S = LARGE, then §5.1 gives LARGE + BUILD_REQUIRED + MUST = RIGOROUS for all 35 rows — **all 35 rows would be RIGOROUS**, not 8 + 27.
  - Doc 07b §11.4 verdict: "Tier assignments: no change. [...] the §3 distribution (8 RIGOROUS + 27 STANDARD) and §6 GATE-P check (c) should be read as **provisional** until F-01 is adjudicated."
- **Gap / Severity:** HIGH (provisional). F-01 is upstream of every row in `07b §4`. The 27 STANDARD rows would all flip to RIGOROUS if scale is correctly classified as LARGE. Either:
  - (a) Reclassify to LARGE and re-tier — 27 rows move from STANDARD to RIGOROUS, dramatically increasing implementation burden (HSM-backed for everything, SOC for everything, external audit for everything, SLSA Level 3 for everything).
  - (b) Record an explicit, justified deviation from `proportionality_model.md` §2 (e.g., "MEDIUM-effective because no sub-domain above MUST"; "MEDIUM-effective because 4 applicable regs but single-product"); "MEDIUM-effective because revenue capped by single product line").
  - **The validator does not resolve this.** It is an orchestrator-level decision. Until adjudicated, Track B tier assignments are conditional.

### C4.8 — Effort expectations implicit in tier match company capacity (450-person team can support RIGOROUS + STANDARD)

- **Verdict:** **PASS**.
- **Evidence:**
  - **Headcount by function (`04d §2`):**
    - CISO + 25-person security team (incl. SOC Manager + IR Lead + 13 SOC analysts + SOC analysts + DevSecOps).
    - DPO + 3-person privacy team.
    - AI Governance Lead + 4-person AI-governance team (incl. AI Bias & Robustness Specialist).
    - CTO + ~30 engineering (Edge AI 8 + Hardware 6 + DevSecOps 5 + ML 5 + Integration 4).
    - Compliance Lead + 2-person compliance team.
    - Internal Audit Lead + 3-person internal audit team.
    - Procurement Director + 4-person procurement team.
    - HR Director + 8-person HR team.
    - Total compliance + security + privacy + AI + audit footprint: ~80 FTE (18% of 450) — **realistic for a HIGH-complexity, 4-regulation, ISO 27001 certified MEDIUM-tier org**.
  - **RIGOROUS-tier effort expectations (8 rows):** HSM-backed KMS (RIGOROUS sub-domain already in place per `04a §1.1 SYS-07`), 24/7 SOC (in place per `04a §1.1 SYS-12`), SLSA Level 3 (achievable with existing DevSecOps 5-person team), continuous monitoring (in place), external audit (already on ISO 27001 surveillance cycle). Each RIGOROUS row has the named owner + dedicated tooling + external certification path that the tier requires per `proportionality_model.md §6.4`.
  - **STANDARD-tier effort expectations (27 rows):** Dedicated tooling + documented procedure + quarterly test cadence — `04d §5 Training Status` shows quarterly cadence (quarterly phishing simulation, quarterly access reviews, quarterly vulnerability review board, quarterly tabletop, quarterly restore drill). This matches STANDARD §6.3.
- **Gap / Severity:** None.

---

## §3 BG → PG/SG Chain Trace

For each BG in Doc 04 §4, trace to specific PG/SG and assess coverage.

### BG-001 → CRA Critical Class certification (CRITICAL, IN_PROGRESS)
- **Owner:** CTO + Notified Body project lead. **Quantitative KPI:** Time to certification (months); conformity assessment pass-rate. **Stakeholders:** CTO, CEO, Notified Body, ENISA, government customers.
- **PG/SG mapping:**
  - PG-D-06.2 (STANDARD) — CycloneDX SBOM per release (CRA Art. 13(11) anchor).
  - PG-D-07.1 (RIGOROUS) — Secure-by-design + AI_Act risk-management.
  - PG-D-07.3 (RIGOROUS) — CI/CD security + SLSA Level 3.
  - SG-D-09.1 — ISO 27001 certified ISMS.
  - SG-D-10.3 — CRA conformity assessment.
- **Priority alignment:** All P0/RIGOROUS — **PASS**.
- **Stakeholder consistency:** CTO (A/R on D-02, D-06.2, D-07), Notified Body (coordination row in RACI `04d §4.6`), ENISA (AEV reporting recipient per CRA Art. 14(1)) — **CONSISTENT**.
- **Verification criteria reinforce BG success criterion:** SG-D-10.3 verification = "Annex VII + Annex VIII conformity assessment + Annual ISO 27001 surveillance audit". Certification is the direct output. **REINFORCED**.
- **Verdict:** **PASS** — full BG → PG/SG chain.

### BG-002 → AI_Act conformity assessment for High-Risk AI (CRITICAL, IN_PROGRESS)
- **Owner:** AI Governance Lead + CTO. **KPI:** Time to conformity certificate; post-market monitoring uptime. **Stakeholders:** AI Governance Lead, CTO, DPO, Notified Body, AI Supervisory Authority.
- **PG/SG mapping:**
  - SG-D-07.1 (RIGOROUS) — AI_Act Art. 9 risk-management system + Art. 13 transparency + Art. 14 human oversight (covers Art. 43 conformity assessment).
  - SG-D-09.2 (STANDARD) — Unified DPIA + FRIA per T-003 (Art. 27 FRIA).
  - SG-D-10.1 (RIGOROUS) — AI_Act Art. 72 post-market monitoring + Art. 73 serious-incident detection.
  - PG-D-10.3 — Compliance testing (conformity re-assessment).
- **Priority alignment:** All RIGOROUS/P0 — **PASS**.
- **Stakeholder consistency:** AI Governance Lead (A on D-07.1, D-09.2, D-10.1, D-10.3 per `04d §4.10`), Notified Body (D-07.1 + D-10.3 coordination rows), DPO (DPIA co-owner), AI Supervisory Authority (per `05 §3.5`) — **CONSISTENT**.
- **Verification criteria reinforce:** SG-D-07.1 "AI_Act risk management system (Art. 9) + CRA secure-by-default (Annex I Part I); unified SDLC; threat modelling per feature; STRIDE + AI-specific extensions (adversarial, model poisoning)". Conformity certificate is the direct output. **REINFORCED**.
- **Verdict:** **PASS** — full chain.

### BG-003 → NIS 2 compliance (24h incident notification) (HIGH, DONE)
- **Owner:** CISO + SOC. **KPI:** MTTD, MTTR, 24h routing pipeline test pass-rate. **Stakeholders:** CISO, SOC, DPO, CSIRT, CEO.
- **PG/SG mapping:**
  - PG-D-04.1 (STANDARD) — 24/7 SOC + AI-driven anomaly detection.
  - PG-D-04.3 (RIGOROUS) — Multi-reg max-SLA 24h routing (resolves T-001).
  - SG-D-04.3 (RIGOROUS) — CRA + NIS 2 + GDPR + AI_Act notification chain on single workflow.
  - PG-D-10.1 (RIGOROUS) — Continuous monitoring + AI_Act post-market.
- **Priority alignment:** RIGOROUS/P0 — **PASS**.
- **Stakeholder consistency:** CISO (A on D-04.x per RACI), SOC (R on D-04.x), DPO (C on D-04.3 for GDPR), CSIRT (recipient per T-001), CEO (Board liability per NIS 2 Art. 20) — **CONSISTENT**.
- **Verification criteria reinforce:** PG-D-04.3 "Mean-time-to-detect (MTTD) tracked quarterly; 24h delivery to DPA, ENISA, CSIRT, and Notified Body on a single timeline" maps directly to BG-003 KPIs. **REINFORCED**.
- **Verdict:** **PASS** — full chain.

### BG-004 → GDPR Art. 9 compliance for biometric processing (CRITICAL, DONE)
- **Owner:** DPO + Legal Counsel. **KPI:** DPO oversight hours; DPIA refresh cadence; Art. 9 violation count. **Stakeholders:** DPO, travelers (data subjects), DPA, CEO.
- **PG/SG mapping:**
  - PG-D-01.1 (RIGOROUS) — HSM-backed AES-256-GCM for biometric templates (biometric Art. 9 anchor).
  - PG-D-01.3 (RIGOROUS) — HSM-anchored key custody + classified-key cipher strength per Art. 9 biometric sensitivity + de-attribution test (GDPR Art. 4(5) pseudonymisation).
  - PG-D-05.1 (STANDARD) — Biometric ephemeral (seconds).
  - PG-D-05.3 (STANDARD) — Cryptographic sharding per T-002 (GDPR Art. 17 erasure).
  - PG-D-09.2 (STANDARD) — Unified DPIA + FRIA per T-003 (GDPR Art. 35).
  - PG-D-09.4 (STANDARD) — RoPA covering all 4 regs (GDPR Art. 30).
- **Priority alignment:** RIGOROUS/P0 for the encryption anchors; STANDARD/P0 for the lifecycle — **PASS**.
- **Stakeholder consistency:** DPO (A on D-05.x, D-09.x per RACI), DPA (per Member State, regulator), travelers (data subjects), CEO (NIS 2 management liability overlap) — **CONSISTENT**.
- **Verification criteria reinforce:** PG-D-01.3 "De-attribution test procedure documented and executed at least once per year" + PG-D-05.3 "Erasure endpoint demonstrates biometric↔identity mapping destroyed via HSM key destruction" — directly mirror DPIA refresh cadence + Art. 9 violation count KPIs. **REINFORCED**.
- **Verdict:** **PASS** — full chain (and biometric-specific RIGOROUS controls are exemplary).

### BG-005 → 99.99% uptime SLA for airport operations (HIGH, IN_PROGRESS)
- **Owner:** CTO + Operations Lead. **KPI:** Uptime %; SLA breach count; MTTR for service incidents. **Stakeholders:** CTO, airport operators, airport security, government customers.
- **PG/SG mapping:**
  - PG-D-04.4 (STANDARD) — RTO 24h, RPO 1h (supports uptime).
  - PG-D-10.1 (RIGOROUS) — 24/7 SOC + AI model drift detection (incidents affect uptime).
  - `04b §2 D-04` "RTO 4h, RPO 15min; immutable backup via SYS-01 + STORE-02 + cross-region replication" — explicit BG-005 anchor in posture document.
  - `04 §7 AI-003` "serviceCriticality + dependencyLevel ... Hybrid | BG-003 (NIS 2), BG-005 (99.99%)" — architectural implication mapping.
- **Priority alignment:** STANDARD/P0 on D-04.4; RIGOROUS/P0 on D-10.1 — appropriate for SLA maintenance (not deadline-driven).
- **Stakeholder consistency:** CTO (A on D-04.4 per `04d §4.4`), airport operators (external customer, mentioned in `04a §1.3`), government customers (per-country DPA chain) — **CONSISTENT**.
- **Verification criteria reinforce BG KPI:** **PARTIAL** — D-04.4 verification criteria cover RTO/RPO but not "uptime ≥99.99%". No PG/SG explicitly states "Uptime ≥99.99% measured by quarterly MTTR report". The BG KPI is not closed in PG/SG verification.
- **Verdict:** **PARTIAL** — chain exists implicitly but verification criteria do not explicitly mirror the 99.99% KPI. Recommend PG-D-04.4 add "Uptime ≥99.99% per quarterly SLA report; SLA breach count ≤0 per quarter" as a verification criterion.

### BG-006 → Expand to 5 additional Schengen countries within 18 months (MEDIUM, IN_PROGRESS)
- **Owner:** CEO + Sales Lead. **KPI:** Country certifications obtained; revenue from new countries. **Stakeholders:** CEO, Sales, Legal, country authorities.
- **PG/SG mapping:**
  - PG-D-06.1 (RIGOROUS) — NIS 2 Art. 21(2)(d) supply chain + biometric processor agreements (per-country DPA chain).
  - PG-D-06.3 (RIGOROUS) — Multi-tier sub-processor flowdown for new country DPAs.
  - `04c §5 GAP-TPL-04` "Per-country government authority DPA chain — 5 additional Schengen countries expansion pending country-by-country DPA in BG-006 (18-month expansion project)" — explicit BG-006 → D-06.1, D-06.3 mapping in third-party landscape doc.
  - `04 §7 AI-005` "dataResidency + tenantArchitecture ... Native | BG-006 (Schengen expansion)" — architectural anchor.
- **Priority alignment:** RIGOROUS/P0 — **PASS** (the supply chain RIGOROUS override already covers Schengen expansion).
- **Stakeholder consistency:** CEO (A on strategic), Legal (R on D-06.3 DPA contracts per `04d §4.6`), country authorities (DPA counterparties) — **CONSISTENT**.
- **Verification criteria reinforce:** PG-D-06.3 "GDPR Art. 28(3) 8-element DPA list enforced; multi-tier sub-processor flowdown; right-to-audit clauses" — covers per-country DPA chain. **PARTIAL** — country-by-country certification pass-rate is not a discrete verification criterion.
- **Verdict:** **PARTIAL** — implicit chain via D-06.x; no discrete PG/SG for "country certification obtained" KPI.

### BG-007 → Maintain ISO 27001 certification (annual surveillance) (HIGH, DONE)
- **Owner:** CISO + ISMS Manager. **KPI:** Surveillance audit pass-rate; non-conformity count. **Stakeholders:** CISO, ISMS team, surveillance auditor, customers.
- **PG/SG mapping:**
  - PG-D-09.1 (STANDARD) — ISO 27001 certified ISMS (policy artefact).
  - PG-D-10.3 (STANDARD) — Annual ISO 27001 surveillance audit + AI_Act + NIS 2 controls test.
  - SG-D-09.1 — "ISO 27001 certified ISMS discharges all four on a single policy artefact" (Doc 07c).
  - `04b §2 D-09` "ISO 27001 v4.7 policy set with full Annex A coverage + ISO 27701 privacy extension + AI-specific addendum; approved by Management Board".
  - `04 §9` "ISO 27001 Maintenance CERTIFIED (annual surveillance)".
- **Priority alignment:** STANDARD/P2 — appropriate for continuous maintenance (not deadline-driven project).
- **Stakeholder consistency:** CISO (A on D-09.1, D-10.3 per RACI), ISMS team (R), surveillance auditor (external customer), customers (downstream stakeholder) — **CONSISTENT**.
- **Verification criteria reinforce:** PG-D-10.3 verification = "Annual ISO 27001 surveillance audit + AI_Act conformity re-assessment + NIS 2 controls test; CISO sign-off". Surveillance audit pass-rate is captured generically. **PARTIAL** — non-conformity count is not explicitly tracked as a verification criterion.
- **Verdict:** **PARTIAL** — implicit chain via D-09.1 + D-10.3; surveillance pass-rate + non-conformity count are BG KPIs but not explicitly mirrored.

### BG-008 → AI false match rate <0.1% (deferred to Phase 3)
- Per Doc 04 §4 "BG-008 ... moved to Phase 3 — this is a technical requirement for Functional Node allocation, not a Phase 1 business goal."
- **Verdict:** **N/A** — explicitly out of Phase 1 scope. No gap.

### BG → PG/SG chain summary

| BG | Priority | Explicit mapping | Implicit coverage | Verdict |
|----|----------|------------------|--------------------|---------|
| BG-001 CRA Critical Class | CRITICAL | YES (D-02, D-06.2, D-07, D-09.1 per Doc 07 §6.1) | YES (RIGOROUS overrides) | PASS |
| BG-002 AI_Act conformity | CRITICAL | YES (D-07.1, D-09.1, D-09.2, D-10.3 per Doc 07 §6.1) | YES | PASS |
| BG-003 NIS 2 24h | HIGH | YES (D-04.1, D-04.3, D-10.1 per Doc 07 §6.1) | YES | PASS |
| BG-004 GDPR Art. 9 | CRITICAL | YES (D-05, D-09.4, D-10.2 per Doc 07 §6.1) | YES | PASS |
| BG-005 99.99% uptime | HIGH | **NO** (not in Doc 07 §6.1) | YES (D-04.4 + D-10.1 + `04b §2 D-04`) | **PARTIAL** |
| BG-006 5 Schengen countries | MEDIUM | **NO** (not in Doc 07 §6.1) | YES (D-06.1 + D-06.3 + GAP-TPL-04) | **PARTIAL** |
| BG-007 ISO 27001 surveillance | HIGH | **NO** (not in Doc 07 §6.1) | YES (D-09.1 + D-10.3 + SG-D-09.1) | **PARTIAL** |
| BG-008 AI false match rate | (Phase 3) | N/A | N/A | N/A |

**4 of 7 BGs have explicit PG/SG mapping. 3 of 7 (BG-005/006/007) have implicit coverage but no explicit mapping rows.**

---

## §4 Case_02-Specific Realism Checks

### Biometric Art. 9 compliance (D-01.1, D-01.3 RIGOROUS)
- **Verdict:** **PASS — exemplary**.
- **Evidence:**
  - **HSM-backed KMS:** `04a §1.1 SYS-07` = "FIPS 140-2 Level 3 HSM cluster (Thales / Utimaco) in EU; key ceremonies quarterly". Concrete vendor + certification level + key ceremony cadence.
  - **Classified-key cipher strength:** `07c §8 PG-D-01.1` "classified-key cipher strength per Art. 9 biometric sensitivity". Documented cipher-class choice for Art. 9 sensitivity.
  - **De-attribution test (GDPR Art. 4(5)):** `07c §8 PG-D-01.3` "De-attribution test procedure documented and executed at least once per year (GDPR Art. 4(5) pseudonymisation)". Specific test procedure + annual cadence.
  - **Cryptographic sharding (resolves T-002):** `07c §8 PG-D-01.1` + `PG-D-05.3` "cryptographic sharding separating biometric↔identity mapping".
  - **Biometric ephemeral by design:** `04a §2.1 STORE-05` "Biometric template cache (transient, on-kiosk only) ... deleted within seconds post-match per Art. 5(1)(c) data minimisation".
  - **TPM 2.0 secure boot on kiosk:** `04a §1.1 SYS-04` "TPM 2.0 secure boot, signed firmware". Hardware-rooted trust for kiosk.
  - **Key-lineage logging:** `07c §8 PG-D-01.1` "Tamper-evident key-lineage log demonstrates every key creation, rotation, and destruction event tied to biometric key custodian".
  - **Functional RBAC separation:** `07c §8 PG-D-01.3` "functional-RBAC separation (key-material custodian vs operational-environment custodian as distinct roles with distinct credentials)".

### AI_Act Annex III conformity (D-07.1 RIGOROUS)
- **Verdict:** **PASS**.
- **Evidence:**
  - **Notified Body engagement (Annex III):** `04c §5` "AI_Act Notified Body (Annex III) | AI_Act conformity assessment body | AI_Act Art. 43 conformity documentation; technical file; FRIA | Contract + designation letter | Assessment scheduled 2026-Q4 in parallel with CRA".
  - **Conformity assessment procedure (Art. 43(4) third-party):** `05 §3.5` "AI_Act Art. 43(4) — Annex III requires third-party assessment".
  - **Post-market monitoring (Art. 72):** `07c §8 SG-D-10.1` (RIGOROUS) "AI_Act Art. 72 post-market monitoring + Art. 73 serious-incident detection".
  - **Risk management system (Art. 9):** `07c §8 SG-D-07.1` (RIGOROUS) "AI_Act risk management system (Art. 9) + CRA secure-by-default (Annex I Part I); unified SDLC; threat modelling per feature; STRIDE + AI-specific extensions (adversarial, model poisoning)".
  - **Human oversight (Art. 14):** `04d §4.7` "AI model change-control (Annex III Art. 16)" + `04d §5` AI Governance Lead "AI_Act bootcamp + ISO 42001 AI management system lead-implementer" (D-08.2 row).
  - **FRIA + DPIA unified (resolves T-003):** `07c §8 SG-D-09.2` "AI_Act Art. 27 FRIA + Art. 9 risk-management system; CRA Art. 13(2) risk assessment + NIS 2 Art. 21(1) risk analysis; the unified DPIA+FRIA process discharges all four on a single impact-assessment artefact (resolves T-003)".
  - **Technical documentation (Annex IV):** `04c §5` "AI_Act Art. 43 conformity documentation; technical file; FRIA".

### NIS 2 Essential Entity Supplier (D-04.3 RIGOROUS — 24h notification)
- **Verdict:** **PASS — exemplary**.
- **Evidence:**
  - **24h CSIRT routing (Art. 23(4)(a)):** `04b §2 D-04` "CISO-owned 24h CSIRT routing (NIS 2 Art. 23(4)(a)); 72h DPA routing (GDPR Art. 33) via DPO; AI_Act 3-tier routing (Art. 73) per AI Governance Lead | FLOW-10 in `04a §2.2` | Tested quarterly; tabletop timings recorded in STORE-04 audit".
  - **Max-SLA 24h routing (resolves T-001):** `07c §8 PG-D-04.3` (RIGOROUS) "Multi-reg max-SLA 24h routing (resolves T-001): single workflow satisfies GDPR Art. 33(2) processor→controller `without undue delay` + CRA Art. 14(1-2) AEV + NIS 2 Art. 23(4)(a) significant incident + AI_Act Art. 73(3) 2-day widespread infringement".
  - **Named IR Lead (Art. 23 contact):** `04d §2` "IR Lead | Incident Response Lead | SOC Manager | 1.0 (named IR lead per NIS 2 Art. 23)".
  - **Tabletop exercise (tested quarterly):** `04b §2 D-04` "quarterly tabletop exercises; 2 annual full-scale exercises with airport authority".
  - **24/7 SOC staffing:** `04d §2` SOC Manager "1.0 + manages 13-person SOC (4 shifts × 3 + 1 on-call)".
  - **Management liability acknowledgement:** `04 §3.2` "NIS 2 management liability — CEO/board personally liable for non-compliance".
  - **3-tier AI_Act reporting integrated:** `04b §2 D-04` "AI_Act 3-tier routing (Art. 73) per AI Governance Lead".

### ISO 27001 certified ISMS (Doc 09 family)
- **Verdict:** **PASS**.
- **Evidence:**
  - **ISO 27001 v4.7 policy set:** `04b §2 D-09` "ISO 27001 v4.7 policy set with full Annex A coverage + ISO 27701 privacy extension + AI-specific addendum; approved by Management Board".
  - **Annual surveillance audit:** `04 §9` "ISO 27001 Maintenance CERTIFIED (annual surveillance)".
  - **Annual surveillance + AI_Act + NIS 2 controls test:** `07c §8 PG-D-10.3` "Annual ISO 27001 surveillance audit + AI_Act conformity re-assessment + NIS 2 controls test; CISO sign-off".
  - **Unified ISMS as policy artefact:** `07c §8 SG-D-09.1` "ISO 27001 certified ISMS discharges all four on a single policy artefact" (covers GDPR + CRA + NIS 2 + AI_Act).
  - **Board-level governance:** `04d §2 Non-Exec Director (Board)` "External — border-security industry experience".
  - **Board briefing cadence:** `04d §5` Management Board row "D-08.3 ACTIVE — Quarterly cybersecurity briefing by CISO + Annual AI risk briefing by AI Governance Lead + Biennial external cyber-board training | 2026-Q1 briefing complete (latest) | 2026-Q3 (next quarterly)".

### Edge AI kiosks (specific kiosk-related controls)
- **Verdict:** **PASS**.
- **Evidence:**
  - **ARM SoC + TensorRT CNN face match + liveness:** `04a §1.1 SYS-04` "ARM SoC, TensorRT-accelerated CNN face match + liveness, TPM 2.0 secure boot, signed firmware".
  - **3D camera + passive liveness module + MRZ scanner:** `04c §3` "Gemalto / Thales (Document & Identity Solutions) | 3D camera + passive liveness module + MRZ scanner | Captures biometric probe + passport MRZ; transmitted encrypted to SYS-04 firmware". Specific hardware supplier + sensor stack.
  - **Industrial-grade PC + tamper-evident enclosure + LTE/5G failover:** `04a §1.1 SYS-06` "Industrial-grade PC + 3D camera + passport MRZ scanner + display; tamper-evident enclosure; LTE/5G failover".
  - **mTLS over QUIC (kiosk outbound-only):** `04a §1.2` "All kiosk-to-cloud traffic is mTLS over QUIC; the kiosk maintains an outbound-only persistent channel — it does not accept inbound network connections". Realistic kiosk hardening pattern.
  - **Signed firmware via TPM:** `04a §1.4` "mTLS certificates rotated quarterly via internal CA chain; revocation via OCSP" + "FIDO device-bound credentials stored in TPM 2.0 for kiosk admin".
  - **Debug ports disabled (secure defaults):** `07c §8 PG-D-03.4` "CRA secure-by-default kiosk config document: debug ports disabled, default passwords rotated, signed firmware required".
  - **Auto-configuration verification in CI:** `07c §8 PG-D-03.4` "Auto-configuration verification in CI gates any commit that re-enables debug ports or default credentials".
  - **OTA update pipeline (signed):** `04a §1.1 SYS-11` "cosign-signed OTA packages" + `07c §8 PG-D-02.2` "Secure OTA update pipeline with HSM-signed firmware images prevents rollback to unsigned versions".
  - **SBOM per release (CRA Art. 13(11)):** `07c §8 PG-D-06.2` "CycloneDX SBOM per release (CRA Art. 13(11))".
  - **Kiosk-specific security awareness:** `07c §8 PG-D-08.1` "kiosk-specific security guide".

---

## §5 Scale Alignment Deep-Check

### Detail depth appropriate for 450-person team?

**PASS.** The Rich corpus shows moderate complexity — neither over-engineered (no 200-page annexes, no MAX-tier controls like full SOC-as-a-service or CISO-of-CISO governance) nor under-developed (all 35 active sub-domains have PG + SG + verification criteria + owner + status + dependencies + risk + stakeholders + maturity + implementation priority). Doc 07c §8 has ~70 detailed cards with multi-paragraph descriptions — appropriately detailed for a MEDIUM-tier org. Doc 04b §3 maturity dashboard shows current 3.0 / target 3.3 — a moderate profile consistent with ISO 27001 certified (not Optimised, not Ad-hoc).

### Track B tiers match proportionality_model.md §5.1 MEDIUM?

**CONDITIONAL_PASS — provisional pending F-01 resolution.**

| Track B input | Value | §5.1 expected tier (MEDIUM + BUILD_REQUIRED + MUST) | Actual | Verdict |
|---|---|---|---|---|
| S (scale) | MEDIUM (per Doc 04 §2; contested per F-01) | STANDARD baseline | 8 RIGOROUS + 27 STANDARD | PASS (if MEDIUM) / FAIL (if LARGE) |
| I (inherit) | BUILD_REQUIRED (all 35 rows per Doc 05 §5) | STANDARD (per §5.1 MEDIUM row) | STANDARD baseline | PASS |
| P (priority) | MUST (all 35 active sub-domains per Doc 07b §3) | STANDARD baseline | STANDARD baseline | PASS |
| 8 RIGOROUS overrides (D-01.1, D-01.3, D-04.3, D-06.1, D-06.3, D-07.1, D-07.3, D-10.1) | — | Justified (HIGH inherent risk override per Doc 07b §3) | Documented with biometric / AI_Act / NIS 2 multi-reg rationale | PASS |

The 8 RIGOROUS overrides are explicitly justified in `07b §3` per the methodology's allowance for HIGH-inherent-risk overrides (biometric Art. 9, AI_Act Annex III high-risk, multi-regulatory incident surface). Each override maps to a critical 4-regulatory surface (T-001 temporal conflict at D-04.3, biometric Art. 9 at D-01.1/D-01.3, NIS 2 + GDPR supply chain at D-06.1/D-06.3, AI_Act + CRA secure-by-design at D-07.1, NIS 2 SDLC at D-07.3, NIS 2 + AI_Act post-market at D-10.1).

**F-01 (HIGH) — Scale classification contested.** `proportionality_model.md §2` reads MEDIUM = ≤250 employees + <€50M revenue. SecureBorder is 450 employees + €120M revenue, which is LARGE on both axes. Doc 07b §11.3 F-01 explicitly flags this. If S = LARGE, then §5.1 says LARGE + BUILD_REQUIRED + MUST = RIGOROUS for **all 35 rows**, not 8. The current 8 RIGOROUS + 27 STANDARD distribution is **provisional** until the orchestrator adjudicates F-01 (re-classify to LARGE, or document explicit justified deviation from §2).

### Example controls imply realistic MEDIUM effort?

**PASS.** Sampled example controls:
- **D-01.1 (RIGOROUS):** "HSM-backed KMS for biometric templates; AES-256-GCM at rest; dedicated key-rotation policy (quarterly); FIPS 140-2 Level 3 HSM; key-lineage logging; cryptographic sharding for biometric↔identity mapping". Realistic for a 450-person org with €120M revenue and a 25-person security team. Already in place per `04a §1.1 SYS-07` Thales/Utimaco HSM cluster.
- **D-07.1 (RIGOROUS):** "AI_Act risk management system (Art. 9) + CRA secure-by-default (Annex I Part I); unified SDLC; threat modelling per feature; STRIDE + AI-specific extensions (adversarial, model poisoning)". Realistic for a 4-person AI-governance team + 8-person Edge AI engineering team.
- **D-04.3 (RIGOROUS):** "Multi-reg max-SLA 24h routing ... quarterly tabletop exercise verifies the 24h delivery to all four channels on a single timeline". Realistic for a 13-person SOC + dedicated IR Lead + CISO.
- **D-10.1 (RIGOROUS):** "NIS 2 continuous monitoring (Art. 21(2)(g)) + AI_Act post-market monitoring (Art. 72); 24/7 SOC; AI model drift detection; serious incident detection (Art. 73)". Realistic for 13 SOC analysts + 4 ML engineers + AI Governance Lead.
- **D-07.2 (STANDARD):** "SAST (Semgrep) + DAST in CI; secure coding standards; OWASP SAMM Level 2 for AI components; pre-commit secret scanning". Realistic for 80 developers.
- **D-06.1 (RIGOROUS):** "NIS 2 Art. 21(2)(d) supply chain risk assessment; GDPR Art. 28 processor agreements for biometric sub-processors; annual supplier audit". Realistic for 4-person procurement team + DPO + Compliance Lead.
- **D-09.1 (STANDARD):** "ISO 27001 certified ISMS (Doc 04 §10.4); unified policies with regulation-specific annexes; annual surveillance audit". Already certified.

No example control demands more headcount than the documented org chart provides.

---

## §6 Critical Blockers (HIGH severity)

| ID | Severity | Finding | Source |
|----|----------|---------|--------|
| **C1 (Doc 07b §11.3 F-01)** | **HIGH** | **Scale input contradicts proportionality_model.md §2.** Doc 07b §2 declares S=MEDIUM; proportionality_model.md §2 reads MEDIUM = ≤250 employees + <€50M. SecureBorder is 450 employees + €120M revenue — LARGE on both axes per the model's strict table. The 8 RIGOROUS + 27 STANDARD distribution is **provisional**. If S=LARGE, all 35 rows would be RIGOROUS. Not a content defect per se, but the §6 GATE-P check (c) and downstream Phase 2 inheritance (`07b §7`) are affected. **Orchestrator decision required.** | `07b §2` + `07b §11.3 F-01` + `proportionality_model.md §2` |

---

## §7 Recommendations

### High-priority (before Phase 2)

1. **Resolve F-01 (scale classification):** Either (a) reclassify Case_02 to S=LARGE per `proportionality_model.md §2` (27 STANDARD → RIGOROUS, with evidence depth + ownership implications on Phase 2 docs) OR (b) document explicit justified deviation from §2 (e.g., "MEDIUM-effective because revenue concentrated in single product line" or "MEDIUM-effective because no sub-domain above MUST"). Without this, every Track B row in `07b §4` is conditional.
2. **Add explicit BG → PG/SG mapping rows for BG-005/006/007 in Doc 07 §6.1:** three BGs (99.99% uptime, 5 Schengen countries, ISO 27001 surveillance) lack explicit mapping rows. Add rows referencing PG-D-04.4 + PG-D-10.1 (BG-005), PG-D-06.1 + PG-D-06.3 (BG-006), PG-D-09.1 + PG-D-10.3 (BG-007).
3. **Document F-03 (D-10.1 unrecorded tension):** per `07b §11.3 F-03`, corpus flags CRA Annex I Part I (2)(l) user opt-out vs mandatory-monitoring (GDPR Art. 32(2), NIS 2 Art. 21(2)(b)) as a CRDA GENUINE TENSION at D-10.1 requiring Layer 2 OJ-level resolution. For eGate kiosks the opt-out limb is arguably inapplicable (no consumer user controls monitoring), but that reasoning is nowhere stated. Recommend documenting the inapplicability rationale (or adding as T-004).

### Medium-priority

4. **Correct T-002 retention citation:** `07b §11.3 F-04` flagged T-002 citation "GDPR Art. 17 erasure vs AI_Act Art. 12 log retention" — AI_Act Art. 12 is the logging-capability duty, not the retention period. The retention floor lives at D-10.2 as Art. 19(1) (`at least six months`). Correct the citation (T-002 is unaffected; only the citation is wrong).
5. **Correct F-02 single-workflow framing:** `07b §11.3 F-02` — D-04.3 "single workflow satisfies GDPR + CRA + NIS 2 + AI_Act" framing is under-qualified per corpus ("unified pipeline may serve the technical substrate, but the policy and evidence layers must remain recipient-segregated"). Add the qualification to PG/SG-D-04.3 detail card.
6. **Correct F-05 D-02.4 regulation attribution:** `07b §11.3 F-05` — D-02.4 corpus participants are CRA + AI_Act + DORA, not NIS 2. The "NIS 2 threat-led" attribution is wrong; the AI_Act attribution is correct. Correct the row note.

### Low-priority

7. **Add BG-specific verification criteria:** for BG-005 (99.99% uptime), BG-006 (country certifications), BG-007 (surveillance pass-rate) — add discrete verification criteria to the relevant PG/SG (PG-D-04.4, PG-D-06.3, PG-D-10.3) so the BG → PG/SG chain closes.
8. **Add §10.5 EU AI_Act regulatory balance note:** the corpus has 0 substantive AI_Act ambiguity cards in the top-20 (per `05b §3 selection logic`). The disambiguation conventions in `05b §4` cover AI_Act via §4.7-§4.11 but the corpus-side gap is documented, not addressed. Optional Phase 2 work.

---

## §8 See also

- `VALIDATOR_TIER1.md` (parallel validator — completeness + internal consistency)
- `VALIDATOR_SPRINT3.md` (Sprint 3 verification — corpus cross-check)
- `VALIDATOR_SPRINT5.md` (Sprint 5 verification — DEEP enrichment pass)
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/04_Company_Context_Assessment.md` §4 (BG catalog)
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/07b_Proportionality_Profile.md` §3, §4, §11 (Track B + corpus cross-check)
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/07c_Adjusted_Objectives.md` §2 (PG), §3 (SG), §4 (tensions), §5 (Track B decision trail), §8 (DEEP detail cards)
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/05b_Ambiguity_Register.md` §3 (top-20 cards), §4 (disambiguation conventions)
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/04a_Architecture_DataInventory.md` (infrastructure anchors)
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/04c_ThirdParty_Landscape.md` (vendor landscape + BG-006 GAP-TPL-04)
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/04d_Org_Roles_RACI.md` (named roles + RACI matrix)
- `00_METHODOLOGY/REFERENCE/proportionality_model.md` (Track B spec — §2 scale, §5.1 decision table, §6 tier definitions)