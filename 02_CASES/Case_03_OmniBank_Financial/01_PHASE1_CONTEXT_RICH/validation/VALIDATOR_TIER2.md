---
document_id: AEGIS-P3-RICH-VALIDATOR-TIER2
title: Validator Tier 2 — Case_03 Phase 1 Rich
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-06
author: Sprint Validator (tier2-verifier)
status: FINAL
case: Case_03_OmniBank_Financial
tier: 2 (Realism + Business Alignment + Scale)
---

# Validator Tier 2 — Case_03 Phase 1 Rich

> Tier 2 = Realism / Company-Specificity + Business Alignment + Scale Alignment.
> Tier 1 (Completeness + Internal Consistency) verified in parallel (`VALIDATOR_TIER1.md`).
> Read-only independent verification of the Case_03 Phase 1 Rich corpus. No source files modified.

## §1 Summary

| Tier 2 Criterion | Verdict | Severity |
|-----------------|---------|----------|
| C3.1 example_controls mention concrete tools | **PASS** | — |
| C3.2 Verification criteria checkable (specific audit procedures, TEST + ANALYZE + external audit) | **PASS** | — |
| C3.3 Owner roles reflect real org (CISO, DPO, CRO, AI Gov Lead, Head of Crypto, SOC Director, DORA ICT Risk Mgr, BaFin/ECB Liaison) | **PASS** | — |
| C3.4 Affected Stakeholders include real external roles (ECB JST, BaFin, BfDI, EDPB, AI Office, ENISA, BSI CSIRT, SWIFT) | **PASS** | — |
| C3.5 Affected Stakeholders appropriate for banking sector (ECB + BaFin + payment networks + AI Office + SWIFT) | **PASS** | — |
| C3.6 Documents reference real infrastructure (DB2 z/OS + payment systems + model store + TLS 1.3 + mTLS + dedicated PKI + HSM cluster) | **PASS** | — |
| C4.1 Each BG has ≥ 1 PG or SG aligned (no orphan BGs) | **PARTIAL** | M |
| C4.2 PG/SG priority aligns with BG priority (CRITICAL/HIGH/MEDIUM) | **PASS** | — |
| C4.3 Stakeholders of BG overlap with Stakeholders of PG/SG | **PASS** | — |
| C4.4 Quantitative metrics of BG (DORA RTS score, uptime ≥99.99%, AI bias <1%) reflected in PG/SG verification | **PARTIAL** | M |
| C4.5 BG deadlines (DORA 17/01/2025, AI Act conformity, NIS 2 24h) align with PG/SG Implementation Priority | **PASS** | — |
| C4.6 Detail depth matches MAX scale (5000+ emp, €1.5B, ISO 27001 + ECB-supervised) | **PASS** | — |
| C4.7 Track B tiers reflect MAX reality (31 RIGOROUS + 7 STANDARD expected) | **PASS** | — |
| C4.8 Effort expectations match company capacity (100+ security FTE org chart) | **PASS** | — |

**Overall Tier 2 verdict: CONDITIONAL_PASS** — strong realism/company-specificity, scale proportionality, and stakeholder alignment across all 5 regulations; two MEDIUM-severity gaps (Doc 07 §6.1 BG table covers BG-001..BG-004 explicitly but BG-005/006/007/008 lack explicit mapping rows; BG quantitative metrics are mirrored generically but not always as discrete verification criteria). No realism/company-specificity failures; the gaps are documentation-only.

---

## §2 Per-Criterion Detail

### C3.1 — example_controls mention concrete tools (not generic "security tools")

- **Verdict:** **PASS**.
- **Evidence (cross-document, sampled):**
  - **HSM cluster (concrete vendor + certification):** `04a §1.1 SYS-22` = "FIPS 140-2 Level 3 HSM cluster (Thales payShield + Utimaco); payment HSMs (PIN translation) + general HSMs". Repeated in `04b §2 D-01` "Key management | FIPS 140-2 Level 3 HSM cluster (SYS-22: Thales payShield + Utimaco); dual-control key ceremonies; payment HSMs for PIN translation"; `07b §4 D-01.3` "Own HSM cluster (Thales / Utimaco) + dedicated crypto team + key ceremony procedure + HSM-backed root keys".
  - **Dedicated IAM (not generic):** `04a §1.1 SYS-24` = "Okta EU + on-prem ADFS; FIDO2 hardware keys for privileged (~250 staff); certificate-based authentication for admin consoles"; `07b §4 D-03.1` "Dedicated IAM platform — Active Directory (on-prem) + Azure AD (cloud) + custom RBAC/ABAC engine. Identity governance (Saviynt) + privileged access management (CyberArk)"; `07c PG-D-03.1-001` "Okta EU + mainframe RACF".
  - **SOC tooling (named products):** `04a §1.1 SYS-25` = "Splunk ES + CrowdStrike Falcon EDR + Tenable Nessus + dedicated fraud SIEM (BioCatch or similar); 24/7 staffed"; `04b §2 D-04` "Splunk Enterprise Security SIEM (EU region) + CrowdStrike Falcon EDR + Tenable Nessus + custom ML anomaly detection + dedicated fraud SIEM (BioCatch); 24 SOC analysts in 4 shifts + 1 on-call".
  - **AI-specific tooling:** `04a §1.1 SYS-03` = "Python + TensorFlow + SageMaker-compatible training; EU-Frankfurt region; explainability layer (SHAP); bias monitoring pipeline"; `07b §4 D-02.1` "AI model scanning (Adversarial Robustness Toolbox)".
  - **CI/CD + SBOM (specific tools):** `04a §1.1 SYS-11` = "GitHub Enterprise + Jenkins + JFrog Artifactory (EU); CycloneDX SBOM emission per release; cosign-signed OTA packages"; `07b §4 D-07.3` "SLSA Level 3" and `07c SG-D-07.3-001` (CycloneDX in CI/CD per release).
  - **Static analysis (specific tool):** `07b §4 D-02.1` "SAST (Checkmarx), DAST (Burp Enterprise), SCA (Snyk), container (Trivy), IaC (Checkov), AI model (Adversarial Robustness Toolbox)".
  - **Penetration testing (named methodology):** `04b §2 D-02` "Annual external (CREST-accredited) pen test + 6-monthly internal red team; DORA Art. 24 TLPT every 3 years on CBS mainframe + OmniScore AI"; `07b §4 D-02.4` "DORA Art. 26-27 — annual external TLPT by ECB-recognised TLPT provider (e.g. BIG-4 firm)".
  - **Payment systems (named):** `04a §1.1 SYS-04` = "Java + ISO 20022 message broker; SEPA Instant SCT Inst; mTLS to Deutsche Bundesbank RTGS"; `SYS-05` = "Mainframe-resident card ledger + cloud tokenisation vault (Visa MDES + Mastercard MDES); PCI-DSS scope"; `SYS-06` = "SWIFT Alliance Access + HSM-bound PKI".
  - **Mainframe infrastructure (named):** `04a §1.1 SYS-01` = "IBM z/OS + DB2 + COBOL (core accounts, ledger, deposits); 24/7 ops in Frankfurt + Munich data centres".
  - **AIOps / CDW (named):** `04a §1.1 SYS-13` = "Snowflake or equivalent; GDPR-compliant data lakehouse"; `SYS-11` = "SAS Fraud Management + custom ML".
  - **Consent management (named):** `07b §4 D-05.1` "consent management platform (OneTrust)".
  - **Privileged access management (named):** `07b §4 D-03.3` "privileged access workstation (PAW) + just-in-time (JIT) access via CyberArk".
- **Gap / Severity:** None. Tools are product-named (Thales payShield + Utimaco, Okta EU + ADFS + CyberArk + Saviynt, Splunk Enterprise Security + CrowdStrike Falcon + Tenable Nessus + BioCatch, Checkmarx + Burp Enterprise + Snyk + Trivy + Checkov + Adversarial Robustness Toolbox, OneTrust, Snowflake, IBM DB2 z/OS, SWIFT Alliance Access, Visa MDES + Mastercard MDES, SLSA Level 3, COsT-€), not placeholder labels.

### C3.2 — Verification criteria are checkable (specific audit procedures, TEST + ANALYZE + external audit cadence)

- **Verdict:** **PASS**.
- **Evidence:**
  - **Operational KPI tests (concrete numbers):** `07c PG-D-01.1-001` "HSM audit log shows 100% key-usage events; AES-256-GCM enabled on all production volumes; FIPS 140-2 Level 3 HSM cluster annual certification; quarterly key-rotation audit by external auditor"; `07c SG-D-01.2-001` "TLS 1.3 enforced across all endpoints; mTLS for service-to-service; quarterly cert rotation audit; quarterly penetration test"; `07c SG-D-04.4-001` (per Doc 04 §3 BG-005) "99.99% uptime SLA per BG-005"; `07c SG-D-02.4-001` (TLPT).
  - **Verification Method consistently applied:** `07c §2 PG table` and `§3 SG table` show "Verification Method: TEST + ANALYZE + external audit (RIGOROUS)" for 31 of 38 sub-domains and "TEST + DEMONSTRATE (STANDARD)" for the 7 STANDARD sub-domains (D-02.3, D-03.4, D-05.1, D-05.2, D-05.3, D-05.4, D-06.2). This is the deterministic application of `proportionality_model.md §6.3 / §6.4` to RIGOROUS/STANDARD tiers respectively.
  - **Tension-resolution tests:** `07c §4 T-001` "Single 4h DORA clock start; subsequent fan-out at 24h/72h/15d per per-reg pipeline | Tabletop exercises quarterly; per-recipient template segregation; per-recipient channel gating; single clock-start discipline; annual joint ECB/BaFin supervised drill; MTTC <4h for DORA-critical events"; `07c §4 T-002` "Quarterly deletion validation; annual external auditor review of cryptographic-sharding key-ceremony procedures; anonymised log integrity verified".
  - **External auditor + supervisory body explicitly listed:** `07c` every detail card lists "External Auditor: ISO 27001 surveillance auditor (annual) + DORA Art. 27 TLPT (triennial) + AI Act Art. 43 conformity" and "Supervisory Body: ECB JST (Joint Supervisory Team) + BaFin + EDPB + AI Office". This is checkable evidence.
  - **Regulatory reporting (per BG):** `07c PG/SG-D-04.3-001` "DORA 4h incident report; ECB annual ICT risk inspection; AI Act Art. 72 PMM if data affects AI model"; `07c SG-D-06.3-001` "100% critical vendor contracts with CTPP clauses; AI Act downstream provider clauses; annual contract review".
- **Gap / Severity:** None. Verification criteria are operationalised with measurable audit procedures and specific cadences.

### C3.3 — Owner roles reflect real org chart (CISO, DPO, CRO, AI Gov Lead, Head of Crypto, SOC Director, DORA ICT Risk Mgr, BaFin/ECB Liaison)

- **Verdict:** **PASS**.
- **Evidence:** `04d §2 Key Roles` enumerates **38 named roles** with FTE allocation, backup, and reporting lines. Required personas all present:
  - **CISO** (1.0 FTE + manages 100-person security team) — required for ISO 27001 + PCI-DSS + DORA Art. 6 + AI Act Art. 15 + NIS 2 24/7 SOC at MAX scale.
  - **DPO** (1.0 FTE + 8-person privacy team; mandatory per Art. 37(1)(b)) — independent access to CEO per Art. 38(3).
  - **CRO** (1.0 FTE + 35-person risk organisation + 8-person DORA ICT Risk team) — required for DORA Art. 5 ICT risk + Basel + MaRisk.
  - **AI Governance Lead** (1.0 FTE + 10-person AI-governance team incl. AI Bias & Robustness Specialist, FRIA Lead, AI Post-Market Monitoring Lead) — required for AI Act Annex III high-risk.
  - **Head of Crypto** (named in `07c PG/SG-D-01.3-001`) — HSM key custodian role distinct from CISO.
  - **SOC Manager** (1.0 FTE + 24-person SOC in 4 shifts × 6 + 1 on-call) — 24/7 SOC required.
  - **IR Lead / CSIRT Lead** (named IR lead per NIS 2 Art. 23; CSIRT for DORA Art. 17-19) — single point of accountability.
  - **DORA ICT Risk Manager** (1.0 FTE + 8-person DORA ICT risk team under CRO) — DORA Art. 5-16 requires dedicated function.
  - **Internal Audit Lead** (1.0 FTE + 6-person internal audit team, reporting to Audit Committee) — independent assurance for ISO 27001 + PCI-DSS + DORA Art. 24 + MaRisk AT 9 + AI Act.
  - **External Legal Counsel** (2.0 FTE in-house + multi-jurisdiction retainer) — DPA + DORA Art. 30 + CRA + AI Act contract templates.
  - **Compliance Lead** (1.0 FTE + 8-person team) — BaFin/ECB liaison.
  - **BaFin Liaison Officer + ECB Liaison Officer** — dedicated regulator-facing roles.
  - **CTO** (1.0 FTE + ~60 engineering staff across Mainframe + Cloud + Payments + DevSecOps + Mobile) — technical implementation.
  - **Non-Exec Directors** (3 external — banking, technology, AI ethics) — board-level governance.
  - **Fraud Detection Lead** (1.0 FTE + 20-person team) — AML/KYC + fraud.
- **Gap / Severity:** None. All required named personas for a 5-regulation MAX-tier credit institution are present and proportionate (100+ security FTE matches the 5000+ employee scale). `04d §7 GAP-RACI-01..-04` openly lists 4 LOW-severity risk-accepted items — P0 (Reasoned Disagreement) honoured, gaps surfaced not hidden.

### C3.4 — Affected Stakeholders include real external roles (ECB JST, BaFin, BfDI, EDPB, AI Office, ENISA, BSI CSIRT, AI Act Notified Body)

- **Verdict:** **PASS**.
- **Evidence (real external roles, not placeholders):**
  - `04 §3 Stakeholder Register` SH-001..SH-013:
    - SH-007 = "ECB/BaFin Supervisors | External | Regulatory oversight, DORA/NIS 2 enforcement"
    - SH-009 = "Cloud Provider (EU)"
    - SH-010 = "Payment Networks (SEPA/SWIFT) | External | Transaction processing, interoperability"
    - SH-011 = "Credit Bureaus | External | Credit data providers, scoring data sources"
    - SH-012 = "National CSIRT | External | NIS 2 incident reporting (24h early warning)"
    - SH-013 = "Data Subjects (Customers) | External | Personal data subjects, AI decision recipients"
  - `04 §4 BG table` repeatedly names supervisors: BG-001 ("ECB JST + BaFin + DORA jurisdiction"), BG-002 ("AI Office + EDPB + national DPA"), BG-003 ("BaFin + BSI CSIRT + ENISA"), BG-004 ("BfDI + EDPB + national DPA"), BG-005 ("ECB JST + BaFin"), BG-006 ("AI Office + national competent authorities"), BG-008 ("AI Office + EDPB + national DPA").
  - `04c §5` Card Networks, Payment Systems, Correspondent Banks — Visa (CTPP-eligible), Mastercard (CTPP-eligible), SWIFT (CTPP per DORA Art. 28), Deutsche Bundesbank (statutory), ECB/EBA (statutory), BaFin (statutory), ENISA (EU Agency + CVD hub), AI Act Notified Body.
  - `05 §3.4 DORA` "CTPP Direct Obligations (Arts. 28-44)" — explicit reference to ESA Joint Committee (EBA/ESMA/EIOPA) Lead Overseers and CTPP oversight framework.
  - `07c §2/§3` per-card "Supervisory Body" lists ECB JST + BaFin + EDPB + AI Office (per sub-domain).
  - `07c §4 T-002` stakeholder alignment: "DPO + CRO + CISO + AI Gov Lead agree; ECB inspection-ready".
  - `07c §4 T-005` stakeholder alignment: "CISO + CRO + ECB TLPT team + TLPT provider agree; parallel cycles coordinated" — explicit ECB TLPT team naming.
- **Gap / Severity:** None. All required external stakeholders for a MAX-tier ECB-supervised credit institution are present by name.

### C3.5 — Affected Stakeholders appropriate for sector (banking: ECB + BaFin + payment networks + AI Office + SWIFT)

- **Verdict:** **PASS**.
- **Evidence:**
  - **Banking sector reality captured correctly:** `04 §2` "Banking/Financial Services | Germany (EU)" + `04 §3` ECB-supervised credit institution + `04a §1.1` core banking mainframe (DB2 z/OS) + payment systems (SEPA/SWIFT) + card networks (Visa/Mastercard) — accurate banking reality.
  - **ECB-supervised status:** `04 §3 SH-007` "ECB/BaFin Supervisors | High Influence"; `04 §9` "DORA Compliance | PARTIAL (existing BSI, but DORA is new) | MEDIUM"; `05 §3.4` "OmniBank is a credit institution per DORA Art. 2(1)(a) — supervised by ECB/BaFin. All DORA requirements apply".
  - **BaFin-specific German context:** `04 §4 BG-001` "BaFin + ECB JST + DORA jurisdiction"; `04 §4 BG-003` "BaFin + BSI CSIRT + ENISA" (correct German competent authority + national CSIRT).
  - **BfDI-specific (German DPA):** `04 §4 BG-004` "BfDI + EDPB + national DPA" — correct German supervisory authority for GDPR (not BaFin which is financial-specific).
  - **AI Office + EDPB + national DPA:** `04 §4 BG-002` "AI Office + EDPB + DPO" — correct AI Act supervisory architecture (national competent authority + EU AI Office + EDPB coordination).
  - **Payment networks (SWIFT, Visa, Mastercard):** `04c §5` names all three with CTPP-eligible designations per DORA Art. 28 — correct DORA treatment for major card networks.
  - **AI Act Notified Body:** `04c §5` "AI Act Notified Body (Annex III) | AI Act conformity assessment | AI Act Art. 43 conformity documentation + FRIA | Contract + designation letter | Assessment scheduled 2026-Q3" — accurate for Annex III high-risk AI conformity.
  - **AI Act specific:** `05 §3.5` "AI Act Annex III §5 credit scoring" — correct Annex III section.
  - **MaRisk AT 9 (German banking regulator):** `04b §2 D-09` "MaRisk AT 9 compliance (German banking regulator)" — correct German financial regulator framework.
  - **ECB JST structure:** `07c §2/§3` "Supervisory Body: ECB JST (Joint Supervisory Team)" — correct ECB supervisory mechanism.
  - **ECB TLPT team:** `07c §4 T-005` stakeholder alignment includes "ECB TLPT team" — accurate ECB TLPT scoping.
  - **Hochrangig relevant external role:** `04c §5 BaFin/ECB Joint Supervisory Forum` "Sector-specific information sharing (BaFin + Deutsche Bundesbank)" — accurate German financial-sector ISAC.
- **Gap / Severity:** None. Stakeholder map matches banking-sector supervisory reality for ECB-supervised German credit institution with AI Act + DORA + NIS 2 obligations.

### C3.6 — Documents reference real infrastructure (DB2 z/OS + payment systems + model store + TLS 1.3 + mTLS + dedicated PKI + HSM cluster)

- **Verdict:** **PASS**.
- **Evidence:**
  - **HSM cluster (concrete + certified):** `04a §1.1 SYS-22` "FIPS 140-2 Level 3 HSM cluster (Thales payShield + Utimaco); payment HSMs (PIN translation) + general HSMs". Concrete vendor + certification level + payment HSM use case.
  - **DB2 z/OS mainframe (financial-sector real):** `04a §1.1 SYS-01` "IBM z/OS + DB2 + COBOL (core accounts, ledger, deposits); 24/7 ops in Frankfurt + Munich data centres" — accurate German banking mainframe reality. STORE-01 "DB2 z/OS (core banking ledger + accounts + customer master) | On-prem Frankfurt DC1 + Munich DC2".
  - **Payment systems (concrete):** `04a §1.1 SYS-04` "Java + ISO 20022 message broker; SEPA Instant SCT Inst; mTLS to Deutsche Bundesbank RTGS"; `SYS-05` "Mainframe-resident card ledger + cloud tokenisation vault (Visa MDES + Mastercard MDES); PCI-DSS scope"; `SYS-06` "SWIFT Alliance Access + HSM-bound PKI; MT/MX message types".
  - **AI model store (concrete EU cloud):** `04a §1.1 SYS-03` "Python + TensorFlow + SageMaker-compatible training; EU-Frankfurt region; explainability layer (SHAP); bias monitoring pipeline" + `STORE-03` "S3 object storage (OmniScore AI training data + explainability logs) | EU cloud (AWS Frankfurt) ... immutable WORM for AI Act Art. 12 technical documentation" + `STORE-10` "OmniScore model artefact registry + signed models".
  - **mTLS + dedicated PKI:** `04a §1.1 SYS-24` "Okta EU + on-prem ADFS; FIDO2 hardware keys for privileged (~250 staff); certificate-based authentication for admin consoles"; `04a §1.2` "Inter-zone traffic uses mTLS over TLS 1.3; intra-zone traffic uses internal mTLS or dedicated high-speed channels" + "Production on-prem and EU cloud are connected via redundant IPSec tunnels".
  - **Three-zone architecture (financial-sector accurate):** `04a §1.2` "(1) Production on-premise (CBS mainframe, payments, treasury, cards, loan systems) hosted across Frankfurt + Munich data centres with synchronous replication and disaster-recovery site in Berlin; (2) EU cloud production (digital channels, AI/ML, analytics, regulatory reporting) in AWS Frankfurt + Microsoft Azure Frankfurt regions under DORA-compliant multi-cloud contract; (3) Security zone with HSM cluster (SYS-22), SIEM (SYS-23), and SOC tooling (SYS-25) in segregated VPC + on-prem with physical dual-control access".
  - **DORA data residency (regulated):** `04 §4 BG-001` "EU data residency with legacy mainframe integration" + `04a §1.2` "The architecture intentionally aligns regulatory data residency (BaFin/ECB data must stay in EU) with DORA Art. 24 digital operational resilience testing (annual TLPT for the CBS mainframe + OmniScore AI) and AI Act Art. 9 risk-management system".
  - **PCI-DSS scope:** `04a §1.1 SYS-05` "PCI-DSS scope" + `04b §2 D-10` "annual PCI-DSS ROC" — accurate payment-card scope.
  - **SEPA / SWIFT interop:** `04c §5` enumerates SEPA / SWIFT / Visa / Mastercard / Deutsche Bundesbank / BaFin / ECB / EBA / ENISA / AI Act Notified Body / TIBER-EU — accurate banking infrastructure.
  - **mTLS + TLS 1.3 enforcement (specific):** `07c SG-D-01.2-001` "TLS 1.3 enforced across all endpoints; mTLS for service-to-service; quarterly cert rotation audit" + `04a §1.3` "mTLS over TLS 1.3; certificate-pinned" + `04a §1.4` "FIDO2 hardware keys for privileged; certificate-based for admin consoles".
- **Gap / Severity:** None. Infrastructure naming is concrete and vendor-accurate for a German MAX-tier credit institution.

### C4.1 — Each BG has ≥ 1 PG or SG aligned (no orphan BGs)

- **Verdict:** **PARTIAL**.
- **Evidence (8 BGs + 8 AI-* architectural implications per `04 §4` + `04 §7`):**
  - **BG-001 (DORA compliance 17/01/2025, CRITICAL) →** Doc 07 §6.1 "BG-001: DORA compliance (2025-01-17) | D-05, D-07, D-09, D-10 | DORA | CRITICAL" + `06b §3` Art. 5/6/9/17-19 mapping to D-09.1 + D-09.3 + D-04.3 + D-06.x RIGOROUS rows + `07c §4 T-001` (max-SLA routing pipeline) + `07c PG/SG-D-09.1-001` (DORA Art. 5 governance) + `07c PG-D-04.3-001` (DORA 4h RTS). **MAPPED**.
  - **BG-002 (AI Act conformity for High-Risk credit scoring, CRITICAL) →** Doc 07 §6.1 "BG-002: AI Act conformity | D-07.1, D-09.1, D-09.2, D-10.3 | AI Act | CRITICAL" + `07c §4 T-003` (IPSARA Unified Assessment Framework) + `07c PG-D-09.4-001` (AI Act Art. 11 technical file) + `07c SG-D-07.1-001` (AI Act Art. 9 risk management) + `07c SG-D-10.1-001` (AI Act Art. 72 post-market monitoring). **MAPPED**.
  - **BG-003 (NIS 2 Essential Entity 24h notification, HIGH) →** Doc 07 §6.1 "BG-003: NIS 2 compliance (24h) | D-04.1, D-04.3, D-10.1 | NIS 2 | HIGH" + `07c §4 T-001` + `07c SG-D-04.3-001` (NIS 2 24h CSIRT routing). **MAPPED**.
  - **BG-004 (GDPR PII/financial, CRITICAL) →** Doc 07 §6.1 "BG-004: GDPR compliance | D-05, D-09.4, D-10.2 | GDPR | CRITICAL" + `07c PG-D-01.1-001` (AES-256-GCM + HSM) + `07c PG-D-05.3-001` (cryptographic sharding per T-002) + `07c SG-D-09.4-001` (GDPR Art. 30 RoPA). **MAPPED**.
  - **BG-005 (99.99% uptime SLA, HIGH) →** NOT explicitly listed in Doc 07 §6.1 BG table (which stops at BG-004). Implicit coverage: `04 §7 AI-003` "serviceCriticality + reliabilityTarget ... Hybrid | BG-003 (NIS 2), BG-005 (99.99%)" — architectural implication mapping; `04 §4 BG-005` "Achieve 99.99% uptime SLA" + `04b §2 D-04` "RTO 4h, RPO 15min for critical CBS mainframe; 99.99% uptime SLA"; `07c SG-D-04.4-001` (DR programme + 99.99% uptime SLA). **IMPLICIT ONLY** — no explicit Doc 07 §6.1 mapping row.
  - **BG-006 (AI expansion to 3 EU markets, MEDIUM) →** NOT explicitly listed in Doc 07 §6.1. Implicit coverage: `04 §4 BG-006` "Expand AI-powered services to 3 additional EU markets within 24 months" + `04 §7 AI-004` "productType + distributionModel ... Native | BG-006 (market expansion)" + `04d §2` "AI Governance Lead" + AI Act Notified Body coordination row. No dedicated PG/SG for market expansion. **IMPLICIT ONLY**.
  - **BG-007 (ISO 27001 + DORA unified ISMS, HIGH) →** NOT explicitly listed in Doc 07 §6.1. Implicit coverage: `04 §4 BG-007` "Maintain ISO 27001 certification and extend to DORA compliance" + `04b §2 D-09` "ISO 27001 v6.2 policy set with full Annex A coverage + PCI-DSS scope + DORA ISMS overlay + AI-specific addendum" + `07c SG-D-09.1-001` (5-policy architecture with DORA overlay). **IMPLICIT ONLY**.
  - **BG-008 (AI model bias <1%, HIGH) →** NOT explicitly listed in Doc 07 §6.1. Implicit coverage: `04 §4 BG-008` "Reduce AI model bias to <1% across all protected characteristics" + `04a §1.1 SYS-03` "explainability layer (SHAP); bias monitoring pipeline" + `07c SG-D-10.1-001` (AI Act post-market monitoring includes bias detection). **IMPLICIT ONLY**.
  - **AI-001..AI-008 (Architectural implications) →** Doc 04 §7 lists 8 AI-* rows each mapped to BG-XXX. AI-001 (DORA financial entity + critical 3rd-party) → BG-001 (DORA), BG-007 (ISO 27001). AI-002 (AI Act high-risk) → BG-002, BG-008. AI-003 (essential entity + 99.99%) → BG-003, BG-005. AI-004 (mobile app + web) → BG-006. AI-005 (massive scale financial data) → BG-004. AI-006 (EU data residency + mainframe) → BG-001, BG-005. AI-007 (hybrid architecture + regulated change) → BG-001, BG-007. AI-008 (eIDAS/PSD2 + logical isolation) → BG-004, BG-006. **MAPPED** (each AI-* is mapped to ≥1 BG).
- **Gap / Severity:** MEDIUM. Doc 07 §6.1 Business Goal Alignment table only explicitly maps BG-001..BG-004 (4 of 8 BGs). BG-005/006/007/008 have implicit coverage via `04 §7` AI-* architectural implications + `04b §2` maturity notes + `07c PG/SG` Stakeholders + `07c §4` tension resolutions, but no explicit Doc 07 §6.1 row. For a MAX-tier case with 8 BGs, the explicit BG table should cover all 8. Recommended: add BG-005/006/007/008 rows to Doc 07 §6.1 (similar to Case_02 validator recommendation R-01, but with 4 unaccounted BGs not 3).

### C4.2 — PG/SG priority aligns with BG priority (CRITICAL/HIGH/MEDIUM)

- **Verdict:** **PASS**.
- **Evidence:**
  - **All 4 CRITICAL BGs (BG-001/002/004 + AI-002/004) →** map to sub-domains where PG/SG are at MUST priority with RIGOROUS tier (D-01.1, D-01.3, D-04.3, D-09.1, D-09.2, D-09.3, D-09.4, D-10.1, D-10.3 all RIGOROUS). `07c §2 PG table` consistently shows "Priority: CRITICAL" for these. **PASS**.
  - **HIGH BGs (BG-003/007/008) →** P0/MUST on D-04.1, D-04.2, D-04.4, D-05.1, D-05.2, D-08.1, D-08.2 (RIGOROUS sub-domains). `07c §2 PG table` "Priority: HIGH" for these. **PASS**.
  - **MEDIUM BG (BG-006) →** appropriate priority on AI market expansion (TO DO per `04 §4`); no conflicting RIGOROUS sub-domain is parked on this BG.
  - **No P1/P2 row implements a CRITICAL BG.** All CRITICAL BGs are mapped to RIGOROUS rows; all HIGH BGs are mapped to RIGOROUS rows; MEDIUM BG is appropriately lower priority.
- **Gap / Severity:** None.

### C4.3 — Stakeholders of BG overlap with Stakeholders of PG/SG

- **Verdict:** **PASS**.
- **Evidence (sampled):**
  - **BG-001 (DORA) →** `04 §4` stakeholders = "Customers, ECB, BaFin, board, CEO". `07c PG-D-09.1-001` Affected Stakeholders = "Customers (data subjects), regulators (ECB, BaFin, EDPB), CEO, CISO, DPO, CTO". `07c SG-D-04.3-001` Affected Stakeholders = "Customers, payment networks, ECB, BaFin, CISO, Network Ops". **OVERLAP** (Customers, ECB, BaFin, CEO all present).
  - **BG-002 (AI Act) →** `04 §4` stakeholders = "Customers, AI Office, EDPB, DPO". `07c SG-D-09.2-001` Affected Stakeholders = "CISO, DPO, AI Gov Lead, ECB, BaFin, AI Office" + `07c SG-D-10.1-001` Affected Stakeholders = "CISO, AI Gov Lead, ECB, BaFin, AI Office". **OVERLAP** (AI Office + EDPB + DPO + ECB all present).
  - **BG-003 (NIS 2) →** `04 §4` stakeholders = "Customers, BaFin, CSIRT, ENISA". `07c SG-D-04.3-001` Affected Stakeholders = "Customers, payment networks, ECB, BaFin, CISO, Network Ops" + `04b §2 D-04` "CISO-owned 24h DORA RTS routing (per RTS Art. 6(1)(a)); 24h CSIRT routing (NIS 2 Art. 23(4)(a) + CRA Art. 14(1)); 72h DPA routing (GDPR Art. 33) via DPO". **OVERLAP** (BaFin + CSIRT both present).
  - **BG-004 (GDPR) →** `04 §4` stakeholders = "Customers, DPO, EDPB, BfDI". `07c PG-D-09.4-001` Affected Stakeholders = "DPO, CISO, ECB JST, BfDI, EDPB, AI Office". **OVERLAP** (BfDI + EDPB + DPO + Customers all present).
  - **BG-005 (uptime SLA) →** `04 §4` stakeholders = "Customers, ECB, BaFin, payment networks". `07c SG-D-04.4-001` Affected Stakeholders = "CISO, Cloud Architect, DPO, internal audit, ECB" (DR perspective). Uptime-related stakeholders implicit via D-10.1 monitoring. **OVERLAP** (ECB + Customers implicit).
  - **BG-008 (AI bias) →** `04 §4` stakeholders = "Customers, AI Office, EDPB, DPO". `07c SG-D-10.1-001` Affected Stakeholders = "AI Gov Lead, CISO, ECB, BaFin, AI Office, DPO, customers (data subjects)". **OVERLAP** (AI Office + EDPB + Customers + DPO all present).
- **Gap / Severity:** None. Stakeholder overlap is consistent across BGs and corresponding PG/SG.

### C4.4 — Quantitative metrics of BG (DORA RTS score, uptime ≥99.99%, AI bias <1%) reflected in PG/SG verification

- **Verdict:** **PARTIAL**.
- **Evidence (per BG):**
  - **BG-001 "DORA RTS compliance score, zero findings" →** `07c PG-D-09.1-001` Risk if not met = "HIGH — financial data exposure + DORA Art. 87 violation + ECB supervisory finding" + `07c SG-D-10.3-001` "DORA Art. 24-27 testing programme (TLPT + scenario-based + performance + security) + AI Act Art. 43 conformity assessment + ISO 27001 surveillance". The "DORA RTS compliance score" is mirrored indirectly via the DORA Art. 24-27 testing programme; explicit "RTS compliance score" verification criterion is not a discrete PG/SG criterion. **PARTIAL** (generic verification, not discrete BG KPI).
  - **BG-002 "AI Act Art. 43 conformity, Art. 72 PMM coverage" →** `07c SG-D-10.3-001` "AI Act Art. 43 conformity assessment" + `07c SG-D-10.1-001` (post-market monitoring) explicitly mirror the BG KPIs. **MAPPED**.
  - **BG-003 "NIS 2 24h EA + 72h notification tested, zero breaches" →** `07c SG-D-04.3-001` (max-SLA routing + quarterly tabletop + per-recipient template segregation + annual ECB/BaFin drill) + `07c §4 T-001` "MTTC <4h for DORA-critical events". **MAPPED**.
  - **BG-004 "Zero Art. 17 violations, DSAR 30-day SLA 100%" →** `07c PG-D-05.3-001` "Right to Erasure ... Per Doc 07b §4 row D-05.3 cross-reference verified ... crypto-sharding balances GDPR erasure with DORA immutable logs" + `07c SG-D-05.4-001` "30-day SLA". **MAPPED**.
  - **BG-005 "Uptime ≥99.99%, zero SLA penalties" →** `07c SG-D-04.4-001` "Own DR programme + 2 active data centres + 1 cold standby + RTO 4h / RPO 15min for critical systems. Quarterly DR test + annual full failover test. 99.99% uptime SLA per BG-005". The 99.99% uptime is explicitly mirrored. **MAPPED**.
  - **BG-006 "3 new market approvals, AI Act compliance" →** Not directly mirrored as verification criteria in any PG/SG. The expansion project is implicitly covered via AI Act Art. 43 conformity (BG-002) + D-06.3 (DPA chain per country). **PARTIAL** (no discrete PG/SG for market expansion).
  - **BG-007 "ISO 27001 zero non-conformities, DORA unified ISMS" →** `07c SG-D-09.1-001` "5-policy architecture (DPO / management body / manufacturer / DORA / AI Governance)" mirrors the unified ISMS. ISO 27001 surveillance audit (annual) is implied via `07c SG-D-10.3-001` "Annual ISO 27001 surveillance audit + PCI-DSS ROC + SOC 2 Type II + MaRisk audit + AI Act conformity assessment (in progress) + DORA Art. 24 TLPT every 3 years". **MAPPED** (surveillance audit cadence explicit).
  - **BG-008 "Bias metrics <1%, AI Act Art. 10 governance" →** `07c SG-D-10.1-001` (AI Act post-market monitoring + AI Act Art. 72) + `04a §1.1 SYS-03` "explainability layer (SHAP); bias monitoring pipeline" + `04 §4 BG-008` KPI "Bias metrics <1%". The bias monitoring pipeline is in place; explicit "<1% bias metric" verification criterion is not a discrete PG/SG criterion. **PARTIAL** (monitoring is mirrored, specific metric is not).
- **Gap / Severity:** MEDIUM. Most BG quantitative metrics are mirrored generically (monitoring, audit, conformity assessment) but the specific KPIs (DORA RTS compliance score, AI market expansion approvals, bias <1% metric) are not always captured as discrete verification criteria. Recommended: add BG-specific verification criteria (e.g., "DORA RTS compliance score ≥95%" + "3 new market approvals obtained by 2028-Q1" + "Bias metrics <1% on protected characteristics" + "ISO 27001 surveillance pass-rate 100% + zero non-conformities") to the relevant PG/SG detail cards or to Doc 07 §6.1.

### C4.5 — BG deadlines (regulatory) align with PG/SG Implementation Priority

- **Verdict:** **PASS**.
- **Evidence:**
  - **BG-001 DORA compliance 17/01/2025 (CRITICAL) →** P0 implementation priority + RIGOROUS on D-01.3 (HSM), D-04.3 (max-SLA 4h), D-06.1 (vendor risk + DORA Art. 28), D-09.1 (5-policy architecture) — appropriate for hard deadline.
  - **BG-002 AI Act conformity for High-Risk credit scoring (CRITICAL) →** P0 + RIGOROUS on D-07.1 (secure-by-design + AI Act Art. 9), D-09.1, D-09.2 (IPSARA unified assessment), D-09.4 (AI Act Art. 11 technical file), D-10.3 (AI Act Art. 43 conformity). AI Act phased dates per `05 §3.5` — Annex III high-risk obligations applicable from 2026-08-02 (now past), 2027-08-02 (full scope).
  - **BG-003 NIS 2 24h notification (HIGH) →** P0 + RIGOROUS on D-04.3 (max-SLA routing).
  - **BG-004 GDPR compliance (CRITICAL) →** P0 + RIGOROUS on D-01.1/1.3, D-05.3 (cryptographic sharding per T-002), D-09.4 (RoPA).
  - **BG-007 ISO 27001 + DORA unified ISMS (HIGH) →** P1 mapping via D-09.1 RIGOROUS — appropriate for continuous certification maintenance (ISO 27001 annual surveillance + DORA ISMS overlay).
  - **BG-005 99.99% uptime (HIGH) →** implicit P1/P2 mapping to D-04.4 (RIGOROUS) + D-10.1 (RIGOROUS) — appropriate for continuous SLA maintenance.
  - **BG-006 3 EU markets 24 months (MEDIUM) →** P1/P2 — appropriate for expansion project (not a regulatory deadline).
  - **BG-008 AI bias <1% (HIGH) →** P0 + RIGOROUS on D-07.1 (AI risk management) + D-10.1 (post-market monitoring).
- **Gap / Severity:** None. Implementation priorities are consistent with deadline criticality.

### C4.6 — Detail depth matches MAX scale (5000+ emp, €1.5B, ISO 27001 + ECB-supervised)

- **Verdict:** **PASS**.
- **Evidence:**
  - **Doc coverage depth:** 38 active sub-domains × (1 PG + 1 SG + 18 fields per card) = 76 detail cards (`07c §2a` + `§3a`). Each card has Description (multi-paragraph), Source Article, NIST CSF Anchors, Verification Criteria (operational), Verification Method, Owner, Status, Dependencies, Risk, Stakeholders, Maturity Score, Implementation Priority, Regulatory Reporting, External Auditor, Supervisory Body, Scope, Out-of-Scope, Sub-Domain-Name-in-header — 18 fields.
  - **Tensions resolved to multi-paragraph depth:** `07c §4` expands all 5 tensions (T-001..T-005) with Root Cause Analysis, Resolution Options Considered, Implementation, Verification Criteria, Risk, Stakeholder Alignment, Status — appropriate for MAX-tier cross-regulation tension resolution.
  - **Track B depth:** `07b §4` has per-sub-domain table with 12 columns (Sub-domain, I, P, Tier, satisfaction_pattern, evidence_depth, verification_method, ownership, example_controls, Risk if not met, Maturity, Implementation Priority, Notes) — comprehensive for MAX scale.
  - **Architecture depth:** `04a §1.1` enumerates **25 systems** (SYS-01..SYS-25) with tech stack, owner, criticality, personal-data flag; `04a §1.3` enumerates **16 cloud providers** with DPA + DORA Art. 30 status; `04a §2.1` enumerates **12 data stores** with encryption + retention + backup; `04a §2.2` enumerates **25 data flows** with encryption + protocol + subprocessor.
  - **RACI depth:** `04d §4` has 10 sub-domain RACI tables covering D-01 through D-10 with 15 columns (15 roles × activity rows) — comprehensive for MAX scale + 5 regulations.
  - **Org depth:** `04d §2` enumerates **38 named roles** with FTE allocation, backup, reporting line — appropriate for 5000+ employee org.
  - **No under-engineering:** No mention of "CISO-as-a-service" or fractional CISO — appropriate full-time functional structure for MAX scale.
  - **No over-engineering:** No 200-page annexes or CISO-of-CISO governance structures; depth is comprehensive but proportionate.
- **Gap / Severity:** None. Detail depth is appropriate for a 5000+ employee, €1.5B revenue, ECB-supervised credit institution with 5 regulations and 38 sub-domains.

### C4.7 — Track B tiers reflect MAX reality (31 RIGOROUS + 7 STANDARD expected)

- **Verdict:** **PASS**.
- **Evidence:**
  - `07b §3` distribution: **31 RIGOROUS + 7 STANDARD = 38 total**. Matches expected MAX + BUILD_REQUIRED/INHERITABLE + MUST per `proportionality_model.md §5.1`:
    - MAX + BUILD_REQUIRED + MUST = **RIGOROUS** (31 rows)
    - MAX + INHERITABLE + MUST = **STANDARD** (7 rows: D-02.3 CVD static infra, D-03.4 CIS benchmarks, D-05.1 DB-level minimisation, D-05.2 archive tooling, D-05.3 erasure API, D-05.4 JSON export, D-06.2 SBOM)
  - The 7 STANDARD rows are documented as INHERITABLE per `07b §3` engineering rationale (corpus `scope_overlap` is GENERIC; Case_03 operational reality requires BUILD_REQUIRED for most sub-domains due to ISO 27001 + DORA + ECB + AI Act mandates).
  - `07b §6` GATE-P check (c) "Tier consistent with §5 decision table for (S=MAX, I, P)" — PASS.
  - `07b §6` GATE-P check (d) "Critical-overload rule satisfied under chosen priorities" — PASS (no SHOULD/COULD rows; MAX + FTE > 1.0 excludes DEFERRED).
  - `07c §5 Track B Decision Trail` documents per-row rationale (38 rows) — full audit trail.
  - **The MAX classification is unambiguous:** `04 §2` reads "Large (5000+ employees, >€1.5B revenue)" + `04 §6` Multi-Actor Note + `04 §10` DORA applicability (ECB-supervised) + `04 §10.2` AI Act applicability (Annex III high-risk) + `05 §6` "MAXIMUM" + `05 §11` 100% Sub-Domain Coverage + `07b §2` S = MAX (5000+ employees, >€1.5B revenue, ECB-supervised, ISO 27001, 100+ security FTE). No `proportionality_model.md §2` ambiguity (unlike Case_02's MEDIUM/LARGE F-01).
- **Gap / Severity:** None. Track B tier distribution is the deterministic MAX outcome and matches the expected 31 RIGOROUS + 7 STANDARD profile.

### C4.8 — Effort expectations match company capacity (100+ security FTE org chart)

- **Verdict:** **PASS**.
- **Evidence:**
  - **Headcount by function (`04d §2`):**
    - CISO + **100-person security team** (incl. SOC Manager + IR Lead + **24 SOC analysts** in 4 shifts × 6 + 1 on-call + DevSecOps Lead + Product Security Lead).
    - DPO + 8-person privacy team.
    - AI Governance Lead + **10-person AI-governance team** (incl. AI Bias & Robustness Specialist, FRIA Lead, AI Post-Market Monitoring Lead).
    - CRO + **35-person risk organisation** (credit risk + market risk + operational risk + DORA ICT risk) + **8-person DORA ICT risk team**.
    - CTO + **~60 engineering staff** (Mainframe 8 + Cloud 15 + Payments 6 + DevSecOps 8 + Mobile 10 + AI/ML 12).
    - Compliance Lead + 8-person compliance team.
    - Internal Audit Lead + 6-person internal audit team.
    - Procurement Director + 8-person procurement team.
    - HR Director + 12-person HR team.
    - Fraud Detection Lead + 20-person financial crime team.
    - In-house Legal Counsel + 2.0 FTE-equivalent + multi-jurisdiction external retainer.
    - **Total compliance + security + privacy + AI + audit footprint: ~178 FTE (3.5% of 5,000+)** — realistic for a MAX-tier regulated credit institution (15-20% of headcount in financial-sector compliance/security is industry-standard for ECB-supervised banks).
  - **RIGOROUS-tier effort expectations (31 rows):** HSM-backed KMS (RIGOROUS already in place per `04a §1.1 SYS-22`), 24/7 SOC (in place per `04a §1.1 SYS-25` + `04d §2` SOC Manager + 24 analysts), dedicated DORA ICT Risk team (8 people under CRO), AI Governance Lead + 10-person AI team, ISO 27001 certified ISMS extending to DORA scope, external CREST-accredited pen test + DORA TLPT (BIG-4 firm or equivalent), annual SOC 2 Type II + ISO 27001 surveillance + PCI-DSS ROC. Each RIGOROUS row has the named owner + dedicated tooling + external certification path that the tier requires per `proportionality_model.md §6.4`.
  - **STANDARD-tier effort expectations (7 rows):** Dedicated tooling + documented procedure + quarterly test cadence — `04d §5 Training Status` shows quarterly cadence (quarterly phishing simulation, quarterly access reviews, quarterly vulnerability review board, quarterly tabletop, quarterly restore drill). This matches STANDARD `proportionality_model.md §6.3`.
  - **No example control demands more headcount than the documented org chart provides.**
- **Gap / Severity:** None. Effort expectations align with the 100+ security FTE org chart documented in `04d §2`.

---

## §3 BG → PG/SG Chain Trace (full)

For each BG in Doc 04 §4 (and AI-* in Doc 04 §7), trace to specific PG/SG and assess coverage.

### BG-001 → DORA compliance 17/01/2025 (CRITICAL, IN_PROGRESS)

- **Owner:** CRO + CISO. **Quantitative KPI:** DORA RTS compliance score, zero findings. **Stakeholders:** Customers, ECB, BaFin, board, CEO.
- **PG/SG mapping (per `07c §2/§3`):**
  - PG-D-01.3-001 (RIGOROUS) — HSM cluster + dedicated crypto team + KMS rotation.
  - PG-D-04.3-001 (RIGOROUS) — Multi-reg max-SLA 4h DORA RTS routing per T-001.
  - PG-D-06.1-001 (RIGOROUS) — DORA Art. 28 ICT third-party register + critical-vendor quarterly review.
  - PG-D-06.4-001 (RIGOROUS) — DORA Art. 28 exit strategy + boundary management.
  - PG-D-09.1-001 (RIGOROUS) — 5-policy architecture with DORA overlay.
  - PG-D-09.3-001 (RIGOROUS) — DORA Art. 8 ICT asset inventory.
  - SG-D-10.3-001 (RIGOROUS) — DORA Art. 24-27 testing programme (TLPT + scenario-based + performance + security).
- **Priority alignment:** All P0/RIGOROUS — **PASS** (the highest criticality priority matches the BG CRITICAL).
- **Stakeholder consistency:** Customers + ECB + BaFin + CEO all present in PG/SG stakeholders + `04d §4` RACI (CEO = A on D-09.1 + D-08.3, CRO = A on D-06.1, CISO = A on D-04.3). **CONSISTENT**.
- **Verification criteria reinforce BG KPI:** `07c §4 T-001` "5-reg max-SLA routing pipeline" + "annual joint ECB/BaFin supervised drill" + "MTTC <4h for DORA-critical events". The RTS compliance score is mirrored via the testing programme + surveillance audit cadence. **REINFORCED**.
- **Verdict:** **PASS** — full BG → PG/SG chain with explicit Doc 07 §6.1 mapping.

### BG-002 → AI Act conformity for High-Risk credit scoring (CRITICAL, IN_PROGRESS)

- **Owner:** AI Governance Lead + CTO. **Quantitative KPI:** AI Act Art. 43 conformity, Art. 72 PMM coverage. **Stakeholders:** Customers, AI Office, EDPB, DPO.
- **PG/SG mapping:**
  - PG-D-09.1-001 (RIGOROUS) — 5-policy architecture with AI Act addendum.
  - PG-D-09.2-001 (RIGOROUS) — IPSARA Unified Assessment Framework (resolves T-003).
  - PG-D-09.4-001 (RIGOROUS) — AI Act Art. 11 technical documentation (Annex IV).
  - SG-D-07.1-001 (RIGOROUS) — AI Act Art. 9 risk-management system + Art. 15 cybersecurity.
  - SG-D-10.1-001 (RIGOROUS) — AI Act Art. 72 post-market monitoring.
  - SG-D-10.3-001 (RIGOROUS) — AI Act Art. 43 conformity assessment.
- **Priority alignment:** All P0/RIGOROUS — **PASS**.
- **Stakeholder consistency:** AI Governance Lead (A on D-09.2 per `04d §4.9` RACI; FRIA Lead + Post-Market Lead on his team), CTO (A on D-07.x per `04d §4.7`), DPO (C/A on D-09.2 per `04d §4.9` RACI), AI Office + EDPB (Supervisory Body per `07c §2/§3`). **CONSISTENT**.
- **Verification criteria reinforce BG KPI:** `07c §4 T-003` "IPSARA annual review; per-regulation output generated; 5-framework discharges; ECB + AI Act + GDPR + CRA + NIS 2 inspection-ready" + `07c SG-D-10.1-001` "AI Act post-market monitoring (Art. 72 — OmniScore)". **REINFORCED**.
- **Verdict:** **PASS** — full BG → PG/SG chain with explicit Doc 07 §6.1 mapping.

### BG-003 → NIS 2 Essential Entity 24h incident notification (HIGH, IN_PROGRESS)

- **Owner:** CISO + SOC Director. **Quantitative KPI:** NIS 2 24h EA + 72h notification tested, zero breaches. **Stakeholders:** Customers, BaFin, CSIRT, ENISA.
- **PG/SG mapping:**
  - PG-D-04.1-001 (RIGOROUS) — 24/7 SOC (Splunk ES + SOAR + CrowdStrike + Vectra AI + Exabeam + dedicated fraud SIEM).
  - PG-D-04.3-001 (RIGOROUS) — Multi-reg max-SLA routing per T-001 (NIS 2 24h satisfied by DORA 4h).
  - SG-D-04.1-001 (RIGOROUS) — MTTD <15 min.
  - SG-D-04.2-001 (RIGOROUS) — MTTC <4h.
  - PG-D-10.1-001 (RIGOROUS) — Continuous monitoring.
- **Priority alignment:** All P0/RIGOROUS — **PASS**.
- **Stakeholder consistency:** CISO (A on D-04.x per `04d §4.4` RACI), SOC Manager + IR Lead (R on D-04.x), BaFin + CSIRT + ENISA (per `04 §4 BG-003`). **CONSISTENT**.
- **Verification criteria reinforce:** `07c §4 T-001` "Tabletop exercises quarterly; per-recipient template segregation; per-recipient channel gating; single clock-start discipline; annual joint ECB/BaFin supervised drill; MTTC <4h for DORA-critical events" mirrors BG-003 24h routing + zero-breach KPI. **REINFORCED**.
- **Verdict:** **PASS** — full BG → PG/SG chain with explicit Doc 07 §6.1 mapping.

### BG-004 → GDPR compliance for customer PII and financial data (CRITICAL, IN_PROGRESS)

- **Owner:** DPO + CISO. **Quantitative KPI:** Zero Art. 17 violations, DSAR 30-day SLA 100%. **Stakeholders:** Customers, DPO, EDPB, BfDI.
- **PG/SG mapping:**
  - PG-D-01.1-001 (RIGOROUS) — AES-256-GCM + HSM-bound CMK across all 12 production stores.
  - PG-D-01.3-001 (RIGOROUS) — FIPS 140-2 Level 3 HSM cluster + dedicated crypto team.
  - PG-D-05.1-001 (STANDARD) — Data minimisation.
  - PG-D-05.2-001 (STANDARD) — Retention & archiving (5-10y BaFin/GoBD).
  - PG-D-05.3-001 (STANDARD) — Cryptographic sharding per T-002 (GDPR Art. 17 erasure vs DORA immutable logs).
  - SG-D-09.4-001 (RIGOROUS) — GDPR Art. 30 RoPA maintained.
- **Priority alignment:** RIGOROUS/P0 on encryption + lifecycle anchors; STANDARD/P0 on data lifecycle — **PASS**.
- **Stakeholder consistency:** DPO (A on D-05.x + D-09.4 per `04d §4.5` RACI), CISO (A on D-01.x + D-10.x), Customers + DPO + EDPB + BfDI all named in `04 §4 BG-004` + `07c §2/§3` Affected Stakeholders. **CONSISTENT**.
- **Verification criteria reinforce:** `07c §4 T-002` "Cryptographic sharding — destroy identity token, retain anonymised log | Quarterly deletion validation; annual external auditor review of cryptographic-sharding key-ceremony procedures; anonymised log integrity verified". **REINFORCED**.
- **Verdict:** **PASS** — full BG → PG/SG chain with explicit Doc 07 §6.1 mapping.

### BG-005 → 99.99% uptime SLA for core banking and digital services (HIGH, IN_PROGRESS)

- **Owner:** CTO + DR Manager. **Quantitative KPI:** Uptime ≥99.99%, zero SLA penalties. **Stakeholders:** Customers, ECB, BaFin, payment networks.
- **PG/SG mapping:**
  - SG-D-04.4-001 (RIGOROUS) — "Own DR programme + 2 active data centres + 1 cold standby + RTO 4h / RPO 15min for critical systems. Quarterly DR test + annual full failover test. **99.99% uptime SLA per BG-005**" — explicit BG-005 reference in `07b §4` and `07c SG-D-04.4-001`.
  - PG-D-10.1-001 (RIGOROUS) — 24/7 SOC + SIEM (incidents affect uptime).
  - `04 §7 AI-003` "serviceCriticality + reliabilityTarget ... Hybrid | BG-003 (NIS 2), BG-005 (99.99%)" — architectural implication mapping.
  - `04b §2 D-04` "RTO 4h, RPO 15min; immutable backup via SYS-01 + STORE-02 + cross-region replication" — explicit BG-005 anchor in posture document.
- **Priority alignment:** RIGOROUS/P0 on D-04.4 + D-10.1 — appropriate for continuous SLA maintenance.
- **Stakeholder consistency:** CTO (A on D-04.4 per `04d §4.4` RACI), Customers + ECB + BaFin + payment networks (per `04 §4 BG-005`). **CONSISTENT**.
- **Verification criteria reinforce BG KPI:** `07c SG-D-04.4-001` "99.99% uptime SLA per BG-005" + "quarterly DR test + annual full failover test". **REINFORCED**.
- **Verdict:** **PARTIAL** — chain exists implicitly via `04 §7` AI-003 + `07c SG-D-04.4-001` + `04b §2 D-04`, but Doc 07 §6.1 lacks explicit BG-005 mapping row.

### BG-006 → Expand AI-powered services to 3 additional EU markets within 24 months (MEDIUM, TODO)

- **Owner:** CEO + AI Governance Lead + Legal. **Quantitative KPI:** 3 new market approvals, AI Act compliance. **Stakeholders:** Customers, AI Office, market regulators.
- **PG/SG mapping:**
  - PG-D-09.1-001 (RIGOROUS) — 5-policy architecture extending to new markets.
  - SG-D-09.2-001 (RIGOROUS) — IPSARA per-market assessment.
  - `04 §7 AI-004` "productType + distributionModel ... Native | BG-006 (market expansion)" — architectural implication mapping.
  - `04 §7 AI-008` "identityProvider + tenantArchitecture ... Hybrid | BG-004 (GDPR), BG-006 (expansion)" — multi-tenant architecture for expansion.
  - `04d §2` AI Governance Lead + Legal Counsel + BaFin/ECB Liaison Officers — expansion governance.
- **Priority alignment:** RIGOROUS/P0 (the policy artefacts are RIGOROUS, but expansion is a project with its own timeline).
- **Stakeholder consistency:** AI Governance Lead + Legal + AI Office + market regulators. **CONSISTENT**.
- **Verification criteria reinforce BG KPI:** No discrete PG/SG for "3 market approvals obtained" verification criterion. **PARTIAL**.
- **Verdict:** **PARTIAL** — chain exists via D-09.x + `04 §7` AI-004 + `04 §7` AI-008 + AI Governance Lead + Legal ownership, but Doc 07 §6.1 lacks explicit BG-006 mapping row.

### BG-007 → Maintain ISO 27001 + extend to DORA compliance (HIGH, IN_PROGRESS)

- **Owner:** CISO + CRO. **Quantitative KPI:** ISO 27001 zero non-conformities, DORA unified ISMS. **Stakeholders:** Customers, ISO 27001 auditor, ECB, BaFin.
- **PG/SG mapping:**
  - PG-D-09.1-001 (RIGOROUS) — 5-policy architecture (DPO / management body / manufacturer / DORA / AI Governance).
  - SG-D-09.1-001 (RIGOROUS) — "Full ISMS (ISO 27001 certified) + DORA Art. 5 ICT risk management framework + AI Act Art. 9 risk management system + 5-policy architecture ... distinct governance bodies".
  - SG-D-10.3-001 (RIGOROUS) — "Annual ISO 27001 surveillance audit + PCI-DSS ROC + SOC 2 Type II + MaRisk audit + AI Act conformity assessment (in progress) + DORA Art. 24 TLPT every 3 years".
  - `04 §9` "ISO 27001 Maintenance | CERTIFIED (annual surveillance)".
  - `04b §2 D-09` "ISO 27001 v6.2 policy set with full Annex A coverage + PCI-DSS scope + DORA ISMS overlay + AI-specific addendum + BaFin MaRisk compliance; approved by Management Board".
- **Priority alignment:** RIGOROUS/P0 — appropriate for continuous certification maintenance.
- **Stakeholder consistency:** CISO (A on D-09.1, D-10.3 per `04d §4.9`/`4.10` RACI), CRO (A on D-09.1/D-09.2/D-06.x per `04d §4.9`), ISO 27001 auditor (external), ECB + BaFin (Supervisory Body per `07c §2/§3`). **CONSISTENT**.
- **Verification criteria reinforce:** `07c SG-D-10.3-001` "Annual ISO 27001 surveillance audit + PCI-DSS ROC + SOC 2 Type II + MaRisk audit + AI Act conformity assessment (in progress) + DORA Art. 24 TLPT every 3 years" mirrors BG-007 ISMS maintenance. **REINFORCED**.
- **Verdict:** **PARTIAL** — chain exists via D-09.1 + D-10.3 + `07c SG-D-09.1-001` + `04b §2 D-09`, but Doc 07 §6.1 lacks explicit BG-007 mapping row.

### BG-008 → Reduce AI model bias to <1% across all protected characteristics (HIGH, IN_PROGRESS)

- **Owner:** AI Governance Lead + CTO + DPO. **Quantitative KPI:** Bias metrics <1%, AI Act Art. 10 governance. **Stakeholders:** Customers, AI Office, EDPB, DPO.
- **PG/SG mapping:**
  - PG-D-09.4-001 (RIGOROUS) — AI Act Art. 11 technical documentation.
  - SG-D-07.1-001 (RIGOROUS) — AI Act Art. 9 risk-management system (includes bias detection).
  - SG-D-10.1-001 (RIGOROUS) — AI Act post-market monitoring (Art. 72) — bias monitoring.
  - `04a §1.1 SYS-03` "explainability layer (SHAP); bias monitoring pipeline".
  - `04d §2` AI Bias & Robustness Specialist (1.0 FTE + 3-person team) — dedicated role for BG-008.
- **Priority alignment:** RIGOROUS/P0 — appropriate for AI Act Art. 10 data governance.
- **Stakeholder consistency:** AI Governance Lead + CTO + DPO + AI Bias & Robustness Specialist + AI Office + EDPB. **CONSISTENT**.
- **Verification criteria reinforce:** Bias monitoring pipeline is in place per `04a §1.1 SYS-03` + AI Bias & Robustness Specialist team exists per `04d §2`. Specific "<1% bias metric on protected characteristics" is not a discrete PG/SG verification criterion but is captured in the BG KPI. **PARTIAL**.
- **Verdict:** **PARTIAL** — chain exists via D-09.4 + D-07.1 + D-10.1 + AI Bias & Robustness Specialist team, but Doc 07 §6.1 lacks explicit BG-008 mapping row.

### AI-001 → DORA financial entity + critical 3rd-party (Native, related to BG-001 + BG-007)

- **Description:** `04 §7 AI-001` "doraFinancialEntity + dependencyLevel + paymentProcessing | DORA financial entity with critical third-party dependencies | Native | BG-001 (DORA), BG-007 (ISO 27001)".
- **PG/SG mapping:** PG-D-06.1-001 (RIGOROUS) + PG-D-06.4-001 (RIGOROUS) + PG-D-09.3-001 (RIGOROUS) — directly implements the critical 3rd-party dependency on DORA Art. 28 + Art. 8 ICT inventory. **MAPPED**.
- **Verdict:** **PASS**.

### AI-002 → AI Act high-risk (credit scoring) with automated decisions (Native, related to BG-002 + BG-008)

- **Description:** `04 §7 AI-002` "aiactHighRiskSystem + decisionImpact | High-Risk AI (credit scoring) with automated decisions | Native | BG-002 (AI Act), BG-008 (bias)".
- **PG/SG mapping:** PG-D-09.4-001 + SG-D-07.1-001 + SG-D-10.1-001 — directly implements AI Act Art. 9 risk-management + Art. 15 cybersecurity + Art. 72 post-market monitoring. **MAPPED**.
- **Verdict:** **PASS**.

### AI-003 → Essential entity + 99.99% uptime (Hybrid, related to BG-003 + BG-005)

- **Description:** `04 §7 AI-003` "serviceCriticality + reliabilityTarget | Essential entity with 99.99% uptime requirement | Hybrid | BG-003 (NIS 2), BG-005 (uptime)".
- **PG/SG mapping:** SG-D-04.4-001 (RIGOROUS, explicit 99.99% reference per BG-005) + SG-D-04.3-001 (RIGOROUS, max-SLA 24h NIS 2 routing per T-001). **MAPPED**.
- **Verdict:** **PASS**.

### AI-004 → Mobile app + web platform (Native, related to BG-006)

- **Description:** `04 §7 AI-004` "productType + distributionModel | Mobile app + web platform (CRA scope) | Native | BG-006 (market expansion)".
- **PG/SG mapping:** SG-D-06.2-001 (STANDARD, SBOM per CRA Art. 13) + SG-D-07.1-001 (RIGOROUS, CRA secure-by-default) + SG-D-07.3-001 (RIGOROUS, CI/CD pipeline security for CRA). **PARTIALLY MAPPED** (no discrete BG-006 mapping).
- **Verdict:** **PARTIAL** (CRA mobile app is covered but BG-006 market expansion itself is not explicitly mapped).

### AI-005 → Massive scale financial data (Native, related to BG-004)

- **Description:** `04 §7 AI-005` "dataCategories + processingScale + financialData | Massive scale financial data processing | Native | BG-004 (GDPR)".
- **PG/SG mapping:** PG-D-01.1-001 + PG-D-01.3-001 + PG-D-05.2-001 + PG-D-09.4-001 — directly implements GDPR Art. 5(1)(c) data minimisation + Art. 32 encryption + Art. 30 RoPA. **MAPPED**.
- **Verdict:** **PASS**.

### AI-006 → EU data residency + mainframe integration (Native, related to BG-001 + BG-005)

- **Description:** `04 §7 AI-006` "dataResidency + legacySystems | EU data residency with legacy mainframe integration | Native | BG-001 (DORA), BG-005 (uptime)".
- **PG/SG mapping:** PG-D-01.1-001 (RIGOROUS, AES-256 + HSM on DB2 z/OS) + SG-D-04.4-001 (RIGOROUS, RTO 4h / RPO 15min mainframe DR) + PG-D-09.3-001 (RIGOROUS, DORA Art. 8 ICT inventory incl. mainframe). **MAPPED**.
- **Verdict:** **PASS**.

### AI-007 → Hybrid architecture + regulated change management (Hybrid, related to BG-001 + BG-007)

- **Description:** `04 §7 AI-007` "technologicalControlPlane + updateMechanism | Hybrid architecture with regulated change management | Hybrid | BG-001 (DORA), BG-007 (ISO 27001)".
- **PG/SG mapping:** PG-D-07.4-001 (RIGOROUS, change management per DORA Art. 10) + PG-D-07.3-001 (RIGOROUS, CI/CD pipeline security) + SG-D-09.1-001 (RIGOROUS, 5-policy architecture with DORA overlay). **MAPPED**.
- **Verdict:** **PASS**.

### AI-008 → eIDAS/PSD2 + logical isolation (Hybrid, related to BG-004 + BG-006)

- **Description:** `04 §7 AI-008` "identityProvider + tenantArchitecture | eIDAS/PSD2 integration with logical isolation | Hybrid | BG-004 (GDPR), BG-006 (expansion)".
- **PG/SG mapping:** PG-D-03.1-001 (RIGOROUS, identity lifecycle) + PG-D-03.2-001 (RIGOROUS, MFA + PSD2 SCA) + SG-D-09.1-001 (RIGOROUS, multi-tenant policy architecture). **MAPPED**.
- **Verdict:** **PASS**.

### BG → PG/SG chain summary

| BG | Priority | Explicit Doc 07 §6.1 mapping | Implicit coverage | Verdict |
|----|----------|--------------------------------|--------------------|---------|
| BG-001 DORA 17/01/2025 | CRITICAL | YES (D-05, D-07, D-09, D-10) | YES (RIGOROUS overrides + 5-policy architecture) | PASS |
| BG-002 AI Act conformity | CRITICAL | YES (D-07.1, D-09.1, D-09.2, D-10.3) | YES (IPSARA + AI Act technical file) | PASS |
| BG-003 NIS 2 24h | HIGH | YES (D-04.1, D-04.3, D-10.1) | YES (max-SLA routing per T-001) | PASS |
| BG-004 GDPR PII/financial | CRITICAL | YES (D-05, D-09.4, D-10.2) | YES (HSM + cryptographic sharding per T-002) | PASS |
| BG-005 99.99% uptime | HIGH | **NO** (not in Doc 07 §6.1) | YES (`04 §7 AI-003` + `07c SG-D-04.4-001` + `04b §2 D-04`) | **PARTIAL** |
| BG-006 3 EU markets | MEDIUM | **NO** (not in Doc 07 §6.1) | YES (`04 §7 AI-004/AI-008` + AI Gov Lead + Legal) | **PARTIAL** |
| BG-007 ISO 27001 + DORA ISMS | HIGH | **NO** (not in Doc 07 §6.1) | YES (`07c SG-D-09.1-001` + `07c SG-D-10.3-001` + `04b §2 D-09`) | **PARTIAL** |
| BG-008 AI bias <1% | HIGH | **NO** (not in Doc 07 §6.1) | YES (`04a §1.1 SYS-03` bias monitoring + `04d §2` AI Bias & Robustness Specialist + `07c SG-D-10.1-001`) | **PARTIAL** |

**4 of 8 BGs have explicit PG/SG mapping (BG-001/002/003/004). 4 of 8 (BG-005/006/007/008) have implicit coverage but no explicit mapping rows. All 8 AI-* have explicit architectural mapping in `04 §7` (each AI-* maps to ≥1 BG).**

---

## §4 Case_03-Specific Realism Checks

### DORA Art. 5 ICT risk framework (RIGOROUS: own ISMS, full DORA Art. 5-16 mapping)

- **Verdict:** **PASS**.
- **Evidence:**
  - **DORA Art. 5 governance framework mapped:** `06b §3.1 Art. 5` "Management body 4-verb coordination `define, approve, oversee, be responsible` (Art. 5(2)) ... Case_03 implementation: Board briefing programme (Doc 04d RACI: CEO accountable, CRO responsible)".
  - **DORA Art. 6 ICT risk management framework:** `06b §3.1 Art. 6` "Art. 6(1): Financial entities shall have a sound, comprehensive and well-documented ICT risk management framework ... Case_03 implementation: Unified ISMS extending ISO 27001 to DORA scope + IPSARA Unified Assessment Framework (Doc 07b §4.9 D-09.2 row + T-003 RESOLVED). Annual ISMS surveillance audit".
  - **Own ISMS (RIGOROUS):** `07b §4 D-09.1` "Full ISMS (ISO 27001 certified) + DORA Art. 5 ICT risk management framework + AI Act Art. 9 risk management system + 5-policy architecture (DPO / management body / manufacturer / DORA / AI Governance) with distinct governance bodies". 5-policy architecture is unique to Case_03 (not present in Case_02 or Case_01).
  - **Management board briefing (D-08.3 ACTIVE):** `04d §4.8 D-08.3` "D-08.3 ACTIVE — NIS 2 Art. 20 + DORA Art. 5 dual obligation" with quarterly briefings since 2024-Q4 + DORA Art. 5 management liability briefing (annual, by CRO). `04d §2 Board` "Management Board (8 directors: CEO + CTO + CFO + CRO + COO + CISO + 3 Non-Exec Directors)".
  - **DORA ICT risk team dedicated:** `04d §2 DORA ICT Risk Manager` "1.0 FTE + manages 8-person DORA ICT risk team" under CRO — DORA Art. 5-16 dedicated function.
  - **Art. 7-16 mapping (full):** `06b §3.1-§3.2` maps Art. 7/8/9/10/11/12/13/14/15/16 to D-02.1, D-09.3, D-01.x, D-03.x, D-04.1, D-04.4, D-10.2, D-07.4, D-04.3, D-10.3 (10 of 38 sub-domains). All RIGOROUS.

### DORA Art. 17 4h notification (RIGOROUS: incident notification procedure)

- **Verdict:** **PASS**.
- **Evidence:**
  - **4h internal DORA clock:** `06b §4.1 T-001` "4-hour internal DORA clock is then routed outward to: BaFin + ECB (DORA Art. 19(1) supervisor notification — 4h) — primary channel".
  - **No weekend deferral (credit institution):** `06b §2.3` "Weekend clause (RTS): Deadlines falling on weekends deferred to next business day at noon — EXCEPT for credit institutions, CCPs, trading venues, and essential entities with >250 employees / >€50M turnover. Case_03 ... is not eligible for the weekend deferral. Deadlines apply 24/7".
  - **DORA Art. 17 incident management process:** `06b §3.3 Art. 17` "Case_03 implementation: 5-regulation max-SLA routing pipeline per Doc 07b §4.4 D-04.3 row. CEO accountable for notification clock".
  - **Art. 19(3) client notification (conditional):** `06b §3.3 Art. 19` "Art. 19(3): Where a major ICT-related incident occurs AND HAS AN IMPACT ON THE FINANCIAL INTERESTS OF CLIENTS, financial entities shall, without undue delay as soon as they become aware of it, inform their clients ... and about the measures that have been taken to mitigate the adverse effects of such incident" (OJ-corrective: trigger condition `and has an impact on the financial interests of clients` — conditional, not unconditional per SR-DORA-017 OJ-corrective note).
  - **Art. 14 crisis communication (clients + counterparts + public):** `06b §3.2 Art. 14` "Case_03 implementation: Crisis communication plan integrated with Art. 19 client notification under Art. 19(3)".
  - **Max-SLA routing pipeline (RIGOROUS):** `07b §4 D-04.3` "5-regulation max-SLA routing pipeline: DORA 4h initial (RTS Art. 6(1)(a), never >24h) + NIS 2 24h early warning + CRA 24h early warning + GDPR 72h notification + AI Act Art. 73 (15d default, 2d widespread, 10d death). No weekend deferral (credit institution, >250 emp, >€50M turnover per RTS). Single underlying event record → per-regulation submission. Doc 07 §5.5 EVT-001 + TENSION-H-001".
  - **Verification cadence:** `07c §4 T-001` "Tabletop exercises quarterly; per-recipient template segregation; per-recipient channel gating; single clock-start discipline; annual joint ECB/BaFin supervised drill; MTTC <4h for DORA-critical events".

### DORA Art. 19 TLPT (RIGOROUS: triennial penetration testing)

- **Verdict:** **PASS**.
- **Evidence:**
  - **Art. 26 TLPT mandate (RIGOROUS, NOT DEFERRED):** `06b §3.4 Art. 26` "shall carry out at least every 3 years advanced testing by means of TLPT ... Case_03 likely qualifies as significant (per §2.2 above — ECB-supervised, 5,000+ employees, >€1.5B). Therefore D-02.4 MUST be RIGOROUS for Case_03, not DEFERRED as in Case_01/Case_02 (which lack DORA applicability). Doc 07b §4.2 row D-02.4 already states: DORA Art. 26 mandates TLPT for major financial entities. ECB-supervised OmniBank qualifies".
  - **TIBER-EU framework reference:** `06b §3.4 Art. 26` "Art. 26(11) defines TLPT by reference to the TIBER-EU framework or equivalent".
  - **Frequency adjustment clause:** `06b §3.4 Art. 26` "ECB may request reduction or increase of 3-year cycle per Art. 26(1) based on risk profile + operational circumstances".
  - **Case_03 TLPT scope:** `07b §4 D-02.4` "TLPT scope: core banking + payment systems + OmniScore AI".
  - **External TLPT provider (BIG-4):** `07b §4 D-02.4` "Annual external TLPT by ECB-recognised TLPT provider (e.g. BIG-4 firm)".
  - **T-005 (TLPT cycle vs ISO 27001 annual):** `07c §4 T-005` "ISO 27001 annual pentest + DORA TLPT every 3y (potentially annual per ECB frequency adjustment); unified findings backlog".
  - **AI Act Annex III adversarial testing:** `07b §4 D-02.1` "AI model vulnerability scanning specific to OmniScore (data poisoning, model evasion)".
  - **DORA Art. 27 advanced testing:** `06b §3.4 Art. 27` "Case_03 implementation: Quarterly internal red team + purple team exercises. Annual scenario-based testing. Continuous AI model adversarial testing (Adversarial Robustness Toolbox)".
  - **First TLPT scheduled:** `04c §9 GAP-TPL-03` "DORA Art. 24 TLPT first cycle scheduled 2026-Q4 (every 3 years thereafter) — preparation in progress".

### DORA Art. 26 critical ICT 3rd-party (RIGOROUS: D-06.4 controls)

- **Verdict:** **PASS**.
- **Evidence:**
  - **DORA Art. 28 ICT third-party risk (RIGOROUS):** `06b §3.5 Art. 28` "Art. 28(1): manage ICT third-party risk ... 4-way AND + service/process/function OR ... Case_03 implementation: Own vendor risk management programme + DORA Art. 28 pre-contractual assessment + Art. 30 register + annual vendor review + critical-vendor quarterly review".
  - **CTPP designations (AWS, Azure, SWIFT, Visa, Mastercard):** `04c §5` marks Visa (CTPP-eligible), Mastercard (CTPP-eligible), SWIFT (CTPP per DORA Art. 28 — OmniBank has CSP-compliant infrastructure). `06b §2.2` "Critical ICT third-party providers (CTPP) designation risk | Art. 28-30 | Cloud providers (AWS, Azure), payment networks (SEPA/SWIFT), credit bureaus — likely designated as CTPPs by Lead Overseers (ESAs)".
  - **Art. 30 contract addenda (every critical vendor):** `04c §2` "all 11 cloud / infrastructure providers; all 11 have DPA + SCCs + DORA Art. 30 ICT contract addenda in place" + `04c §7` "100% critical vendor contracts with CTPP clauses" (in `04c` table).
  - **Art. 30(3)(e)+(f) CIF-only audit rights + exit strategies:** `06b §3.5 Art. 30 OJ-corrective note` "SR-DORA-021 audit rights and exit strategies misattributed to Art. 30(2) when OJ places them in Art. 30(3)(e) and 30(3)(f) respectively (CIF-only). This document uses OJ-locus".
  - **Art. 34 information register:** `06b §3.6 Art. 34` "Own RoPA (GDPR Art. 30) + DORA Art. 34 ICT third-party register + AI Act Art. 12 technical documentation + CRA Art. 13 technical documentation per Doc 07b §4.9 D-09.4 row. DORA Art. 34 register 5-year retention; AI Act 10-year".
  - **D-06.4 boundary + exit strategy (RIGOROUS):** `07b §4 D-06.4` "Own boundary management (API gateway + dedicated circuits to cloud/payment/credit bureaus) + supplier incident playbook + DORA Art. 28 exit strategy".

### DORA Art. 30 critical contracts (RIGOROUS: vendor contract procedures)

- **Verdict:** **PASS**.
- **Evidence:**
  - **Art. 30(1) written contract requirement:** `06b §3.5 Art. 30` "Art. 30(1): the rights and obligations ... shall be clearly allocated and set out in writing".
  - **Art. 30(2) 9-element minimum:** `06b §3.5 Art. 30` "Art. 30(2): minimum 9 elements (description of functions, locations, data, access, audit-rights linkage, SLAs, termination, exit strategies, sub-outsourcing transparency)".
  - **Art. 30(3)(e)+(f) CIF-only:** `06b §3.5 Art. 30` "Art. 30(3)(e)(i)+(ii) CIF-only: unrestricted rights of access, inspection and audit by the financial entity ... the right to take copies of relevant documentation on-site".
  - **Case_03 contract templates:** `07b §4 D-06.3` "Own contract templates (DPA + DORA Art. 30 CTPP clauses + NIS 2 supply chain + AI Act downstream provider Art. 25) + Legal review workflow + supplier security clauses".
  - **27 vendor contracts with CTPP addenda:** `04c §7 Contractual Coverage` lists 27 vendors with DORA Art. 30 column — 100% coverage of Critical/Important vendors.
  - **DORA Art. 28(4) sub-outsourcing register:** `04c §7 Contractual Coverage` row "Y (subscriber to sub-processor change notification; DORA Art. 28(4))" for 100% of vendors.

### AI Act Art. 10 data quality (RIGOROUS: bias monitoring)

- **Verdict:** **PASS**.
- **Evidence:**
  - **AI Act Art. 10 data governance:** `05 §11 D-05.1/AI Act Art. 10` "Training data quality + bias detection + relevance + representativeness | Data governance | HIGH | Cur 2/4 → Tgt 2/4 | AI Office + EDPB + national DPA".
  - **Bias monitoring pipeline:** `04a §1.1 SYS-03` "Python + TensorFlow + SageMaker-compatible training; EU-Frankfurt region; **explainability layer (SHAP); bias monitoring pipeline**".
  - **AI Bias & Robustness Specialist role:** `04d §2` "AI Bias & Robustness Specialist | AI-system adversarial testing + fairness audit | AI Governance Lead | 1.0 FTE + manages 3-person team | AI Governance Lead".
  - **AI Act Art. 10 governance:** `04 §4 BG-008` "AI Act Art. 10 governance" + `04 §9` "AI Act Conformity | NOT STARTED | HIGH | Implement conformity assessment; FRIA; post-market monitoring".
  - **AI training data lineage:** `04d §4.5` RACI "AI-system training-data lineage (AI Act Art. 10) — AI Governance Lead = A".
  - **Verification:** `07c SG-D-10.1-001` "AI Act post-market monitoring (Art. 72 — OmniScore)" includes bias detection (covered by post-market monitoring + bias monitoring pipeline).

### AI Act Art. 43 conformity (RIGOROUS: conformity assessment process)

- **Verdict:** **PASS**.
- **Evidence:**
  - **AI Act Annex III Notified Body engagement:** `04c §5` "AI Act Notified Body (Annex III) | AI Act conformity assessment body | AI Act Art. 43 conformity documentation; technical file; FRIA | Contract + designation letter | Assessment scheduled 2026-Q3".
  - **AI Act Art. 43 conformity assessment (RIGOROUS):** `07b §4 D-10.3` "DORA Art. 24-27 testing programme (TLPT + scenario-based + performance + security) + AI Act Art. 43 conformity assessment + ISO 27001 surveillance + GDPR DPIA review + CRA self-declaration".
  - **Conformity assessment scheduled:** `04 §10.2 AI Act` "Conformity Assessment (Art. 43) | ⏳ Not started | Timeline defined".
  - **Verification cadence:** `07c SG-D-10.3-001` "AI Act conformity assessment (in progress) + DORA Art. 24 TLPT every 3 years".

### AI Act Art. 72 post-market monitoring (RIGOROUS: ongoing monitoring)

- **Verdict:** **PASS**.
- **Evidence:**
  - **AI Act Art. 72 post-market monitoring system:** `05 §11 D-10.1/AI Act Art. 60-62` "Post-market monitoring integrated with DORA Art. 13 | AI Act PMM | HIGH | Cur 2/4 → Tgt 4/4 | AI Office + ECB JST".
  - **AI Post-Market Monitoring Lead:** `04d §2` "AI Post-Market Monitoring Lead | AI Act Art. 72 post-market monitoring | AI Governance Lead | 1.0 FTE + manages 2-person team | AI Governance Lead".
  - **Post-market monitoring system:** `04 §10.2 AI Act` "Post-Market Monitoring (Art. 72) | ⏳ Not started | System design in progress".
  - **Integration with DORA monitoring:** `04b §2 D-10` "Includes AI Act post-market monitoring (Art. 72) overlay; DORA Art. 13 monitoring; ECB-supervised".
  - **Verification cadence:** `07c SG-D-10.1-001` "AI-post-market monitoring (AI Act Art. 72 — OmniScore)" + "Verification: TEST + ANALYZE + external audit (RIGOROUS)".

### NIS 2 Art. 23 24h notification (covered via T-001 max-SLA routing)

- **Verdict:** **PASS**.
- **Evidence:**
  - **NIS 2 Art. 23 24h early warning:** `05 §3.3` "NIS2-C25 | Art. 23(1) | D-04.3 (Early Warning (24h)) | Notify CSIRT within 24h of significant incident | ESSENTIAL_ENTITY | TRIGGERED | 3 | 24h notification".
  - **24h CSIRT routing:** `04b §2 D-04` "CISO-owned 4h DORA RTS routing (per RTS Art. 6(1)(a)); 24h CSIRT routing (NIS 2 Art. 23(4)(a) + CRA Art. 14(1)); 72h DPA routing (GDPR Art. 33) via DPO; 15d AI Act routing (Art. 73(2)) via AI Governance Lead".
  - **Named IR Lead (Art. 23 contact):** `04d §2` "IR Lead / CSIRT Lead | Incident Response Lead | SOC Manager | 1.0 (named IR lead per NIS 2 Art. 23; CSIRT for DORA Art. 17-19) | SOC Manager + CISO".
  - **T-001 resolution (4h DORA satisfies 24h NIS 2):** `07c §4 T-001` "4h DORA internal clock is then routed outward to: ... CSIRT + ENISA (NIS 2 Art. 23(4) early warning — 24h, satisfied by 4h)".
  - **Management liability (NIS 2 Art. 20):** `04d §4.8 D-08.3` "Management Board cybersecurity briefings — D-08.3 (NIS 2 Art. 20 + DORA Art. 5 dual obligation) | CISO=R (quarterly briefing); CRO=R (annual DORA briefing); AI-Gov=R (annual AI risk briefing); Board=A".
  - **Verification:** `07c SG-D-04.3-001` (RIGOROUS) "Quarterly tabletop exercise verifies the 24h delivery".

### GDPR (DSAR 30-day SLA, RoPA, Art. 17 erasure with cryptographic sharding)

- **Verdict:** **PASS**.
- **Evidence:**
  - **GDPR Art. 5-32 all addressed:** 28 GDPR clauses mapped per `06 §4` (GDPR-C01..GDPR-C28).
  - **DSAR 30-day SLA:** `04 §10.4 GDPR Financial Data` "Data Subject Rights (Art. 15-22) | ✅ Ready | DSAR process in place" + `07b §4 D-05.4` "JSON export endpoint (machine-readable) + 30-day SLA + GDPR Art. 20 right to data portability".
  - **RoPA:** `07b §4 D-09.4` "Own RoPA (GDPR Art. 30) + DORA Art. 17-19 ICT incident records + AI Act Art. 12 technical documentation + CRA Art. 13 technical documentation".
  - **T-002 cryptographic sharding (GDPR Art. 17 vs DORA immutable logs):** `07c §4 T-002` "Cryptographic sharding — destroy identity token, retain anonymised log | Tokenisation + hash-chain audit log | Per-DSAR 30-day SLA with cryptographic key destruction | Quarterly deletion validation; annual external auditor review of cryptographic-sharding key-ceremony procedures".
  - **DPIA (Art. 35):** `07b §4 D-09.2` "IPSARA Unified Assessment Framework (T-003 RESOLVED) — DPIA (GDPR Art. 35) + FRIA (AI Act Art. 27) + ICT risk assessment (DORA Art. 6) + CRA risk assessment + NIS 2 risk analysis".
  - **DPO mandatory (Art. 37(1)(b)):** `04d §2` "DPO | Datenschutzbeauftragter | CEO (independent access per Art. 38(3)) | 1.0 (DPO hat) + manages 8-person privacy team".

### ISO 27001 + DORA ISMS

- **Verdict:** **PASS**.
- **Evidence:**
  - **ISO 27001 v6.2 policy set:** `04b §2 D-09` "ISO 27001 v6.2 policy set with full Annex A coverage + PCI-DSS scope + DORA ISMS overlay + AI-specific addendum + BaFin MaRisk compliance; approved by Management Board".
  - **5-policy architecture (unique to Case_03 MAX):** `07b §4 D-09.1` "5-policy architecture (DPO / management body / manufacturer / DORA / AI Governance) with distinct governance bodies" — this is a DORA + AI Act overlay on ISO 27001.
  - **Annual surveillance + DORA TLPT every 3y:** `07c SG-D-10.3-001` "Annual ISO 27001 surveillance audit + PCI-DSS ROC + SOC 2 Type II + MaRisk audit + AI Act conformity assessment (in progress) + DORA Art. 24 TLPT every 3 years".
  - **Unified ISMS as policy artefact:** `07c SG-D-09.1-001` "Full ISMS (ISO 27001 certified) + DORA Art. 5 ICT risk management framework + AI Act Art. 9 risk management system + 5-policy architecture".
  - **Board briefing (D-08.3 ACTIVE under dual NIS 2 + DORA obligation):** `04d §4.8 D-08.3` "Quarterly cybersecurity + AI risk briefings to Management Board + Non-Exec Directors; annual external cyber-board training".

---

## §5 Scale Alignment Deep-Check

### Detail depth appropriate for 5000+ employee org with 100+ security FTE?

**PASS.** Detail depth is MAX-appropriate:
- **Doc 04 (CCA):** 8 BGs + 8 AI-* + 13 stakeholders + 5 OMNIBANK-SPECIFIC sub-sections (DORA / AI Act / NIS 2 / GDPR).
- **Doc 04a (Architecture):** 25 systems + 12 data stores + 25 data flows + 16 cloud providers + 3-zone architecture (Frankfurt + Munich DCs + Berlin DR + EU cloud + security zone).
- **Doc 04b (Posture):** 10 macro-domains × per-domain maturity + 2.1 corpus-derived target fit_criteria for 114 sub-requirements.
- **Doc 04c (Third-party):** 22 distinct vendors + 10 statutory/regulator/card-scheme/network entities = 32 relationships; 27-row risk assessment; 8 gaps explicitly listed.
- **Doc 04d (RACI):** 38 named roles + 8 reporting lines + 10 sub-domain RACI tables + 17-row training status.
- **Doc 05 (Applicability):** 5 regulations + 158 sub-clause rows + 9 KEY OBSERVATIONS + 8 strategic implications.
- **Doc 06 (Clause Mapping):** 150 clauses (28 + 26 + 29 + 38 + 29) + 8 clause-ID shim.
- **Doc 06b (DORA Framework):** 26 DORA articles + 5 cross-regulation tensions (T-001..T-005).
- **Doc 07b (Proportionality):** 38-row per-sub-domain table with 12 columns + 3-tier distribution summary + tension cross-reference.
- **Doc 07c (Adjusted Objectives):** 76 detail cards (38 PG + 38 SG) with 18 fields each + 5 tensions resolved to multi-paragraph depth.

Neither over-engineered (no 200-page annexes, no CISO-of-CISO governance) nor under-developed (all 38 active sub-domains have PG + SG + verification criteria + owner + status + dependencies + risk + stakeholders + maturity + implementation priority).

### Track B tiers match proportionality_model.md §5.1 MAX row?

**PASS.** Track B matches MAX per `proportionality_model.md §5.1`:

| Track B input | Value | §5.1 expected tier (MAX + INHERITABLE/BUILD_REQUIRED + MUST) | Actual | Verdict |
|---|---|---|---|---|
| S (scale) | MAX (5000+ emp, >€1.5B, ECB-supervised) | MAX row in §5.1 | MAX | PASS |
| I (inherit) | BUILD_REQUIRED (31 rows) or INHERITABLE (7 rows) | MAX + BUILD_REQUIRED + MUST = RIGOROUS / MAX + INHERITABLE + MUST = STANDARD | 31 RIGOROUS + 7 STANDARD | PASS |
| P (priority) | MUST (all 38 active sub-domains) | All rows MUST | All MUST | PASS |
| 31 RIGOROUS overrides | D-01.x, D-02.x (except D-02.3), D-03.x (except D-03.4), D-04.x, D-06.1, D-06.3, D-06.4, D-07.x, D-08.x, D-09.x, D-10.x | Documented with engineering rationale per `07b §3` | Documented | PASS |
| 7 STANDARD rows | D-02.3, D-03.4, D-05.1, D-05.2, D-05.3, D-05.4, D-06.2 | Inheritability preserved | Documented | PASS |

**The MAX classification is unambiguous.** No `proportionality_model.md §2` ambiguity (unlike Case_02's MEDIUM/LARGE F-01) — Case_03 has 5000+ employees + >€1.5B revenue + ECB-supervised + ISO 27001 + DORA financial entity + AI Act Annex III, all of which place it definitively in the MAX row of `proportionality_model.md §2`.

### Example controls imply realistic MAX effort?

**PASS.** Sampled example controls:
- **D-01.1 (RIGOROUS):** "Own HSM-backed KMS (FIPS 140-2 Level 3) + dedicated crypto team + AES-256-GCM at rest across core banking (DB2 z/OS), payment systems, model store, data lake". Realistic for a 5000+ employee org with a dedicated Head of Crypto + 100-person security team.
- **D-04.3 (RIGOROUS):** "5-regulation max-SLA routing pipeline: DORA 4h initial (RTS Art. 6(1)(a), never >24h) + NIS 2 24h early warning + CRA 24h early warning + GDPR 72h notification + AI Act Art. 73 (15d default, 2d widespread, 10d death). **No weekend deferral** (credit institution, >250 emp, >€50M turnover per RTS)". Realistic for a 24-person SOC + dedicated IR Lead + CISO + CRO + DPO + AI Governance Lead.
- **D-09.1 (RIGOROUS):** "Full ISMS (ISO 27001 certified) + DORA Art. 5 ICT risk management framework + AI Act Art. 9 risk management system + 5-policy architecture (DPO / management body / manufacturer / DORA / AI Governance) with distinct governance bodies". Realistic for a 100-person security team + 8-person DORA ICT risk team + 10-person AI governance team.
- **D-02.4 (RIGOROUS):** "Own TLPT programme per DORA Art. 26-27 — annual external TLPT by ECB-recognised TLPT provider (e.g., BIG-4 firm). Internal red team + purple team exercises". Realistic for a 24-person SOC + dedicated penetration testing budget.
- **D-06.3 (RIGOROUS):** "Own contract templates (DPA + DORA Art. 30 CTPP clauses + NIS 2 supply chain + AI Act downstream provider Art. 25) + Legal review workflow + supplier security clauses". Realistic for 2.0 FTE in-house Legal + multi-jurisdiction retainer + 8-person procurement team.
- **D-09.2 (RIGOROUS):** "IPSARA Unified Assessment Framework (T-003 RESOLVED) — DPIA (GDPR Art. 35) + FRIA (AI Act Art. 27) + ICT risk assessment (DORA Art. 6) + CRA risk assessment + NIS 2 risk analysis". Realistic for DPO + AI Governance Lead + CRO + CISO.

No example control demands more headcount than the documented org chart provides.

---

## §6 Critical Blockers (HIGH severity)

| ID | Severity | Finding | Source |
|----|----------|---------|--------|
| (none) | — | — | — |

**No HIGH-severity blockers identified.** The two MEDIUM gaps (Doc 07 §6.1 BG-005/006/007/008 mapping rows; discrete BG-KPI verification criteria for DORA RTS compliance score, market expansion approvals, bias <1% metric, ISO 27001 surveillance pass-rate) are documentation-only and do not block Phase 2.

---

## §7 Recommendations

### Medium-priority (before Phase 2)

1. **Add explicit BG → PG/SG mapping rows for BG-005/006/007/008 in Doc 07 §6.1:** four BGs (99.99% uptime, 3 EU markets expansion, ISO 27001 surveillance, AI bias <1%) lack explicit mapping rows. Add rows referencing the relevant PG/SG:
   - BG-005 → SG-D-04.4-001 (RIGOROUS, explicit 99.99% reference) + PG-D-10.1-001 (continuous monitoring) + `04 §7 AI-003`.
   - BG-006 → SG-D-09.2-001 (IPSARA per-market assessment) + SG-D-09.1-001 (5-policy architecture) + `04 §7 AI-004` + `04 §7 AI-008`.
   - BG-007 → PG-D-09.1-001 (5-policy architecture with DORA overlay) + SG-D-10.3-001 (annual ISO 27001 surveillance).
   - BG-008 → SG-D-10.1-001 (AI Act post-market monitoring + bias monitoring pipeline per `04a §1.1 SYS-03`) + `04d §2` AI Bias & Robustness Specialist team.
2. **Add discrete BG-specific verification criteria:** for BG-005 (uptime ≥99.99%), BG-006 (3 market approvals obtained), BG-007 (ISO 27001 surveillance pass-rate + zero non-conformities), BG-008 (bias metrics <1% on protected characteristics). Add to relevant PG/SG detail cards in `07c` or to Doc 07 §6.1.
3. **Tensions T-001..T-005 ontology registration:** `phase1_ontology.yaml` flags all 5 tensions as "Declared case-specific in legacy; not yet registered in `00_METHODOLOGY/SCHEMA/tensions.yaml` (Sprint 2+ candidate)". Recommend registering T-001..T-005 in canonical tensions.yaml for cross-case reuse (T-001 max-SLA routing + T-002 cryptographic sharding + T-003 IPSARA are reusable patterns).

### Low-priority

4. **T-001 "DORA 4h satisfies all shorter deadlines" framing:** `07b §11.3 F-02` style caution — DORA 4h satisfies the shortest clock but per-recipient template segregation + channel gating is still required (the routing pipeline is not a single workflow). The current framing in `07c §4 T-001` "Single 4h DORA clock start; subsequent fan-out at 24h/72h/15d" correctly captures this — no action needed.
5. **AI Act Art. 25 corpus gap (DECLARATION_GAP):** `Citation_Index §3` "AI Act Art. 25 — Provider-deployer interface clause; not yet parsed into corpus under D-06". Mitigation in place per `04c §6.1`: "provider-deployer clauses are embedded in the AWS Sagemaker contract addendum (OmniScore training environment). **Coverage gap flagged for Phase 2 disambiguation**". Recommend Phase 2 augmentation or explicit cross-reference.
6. **DORA Art. 87 "ICT data protection" corpus gap:** `Citation_Index §2.4` "DORA Art. 87 — corpus verbatim: NOT FOUND". `07c PG-D-01.1-001` Risk if not met = "HIGH — financial data exposure + DORA Art. 87 violation + ECB supervisory finding". Art. 87 is referenced but the corpus file does not exist; Phase 2 augmentation recommended.

---

## §8 See also

- `VALIDATOR_TIER1.md` (parallel validator — completeness + internal consistency)
- `VALIDATOR_SPRINT3.md` (Sprint 3 verification — corpus cross-check)
- `VALIDATOR_SPRINT5.md` (Sprint 5 verification — DEEP enrichment pass)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/04_Company_Context_Assessment.md` §4 (BG-001..BG-008 catalog), §7 (AI-001..AI-008 architectural implications)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/04a_Architecture_DataInventory.md` (infrastructure anchors: SYS-01..SYS-25 + STORE-01..STORE-12 + FLOW-01..FLOW-25 + 16 cloud providers)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/04b_Security_Posture.md` (maturity per macro-domain + corpus-derived target fit_criteria)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/04c_ThirdParty_Landscape.md` (22 vendors + 10 statutory + DORA Art. 30 CTPP register + 8 gaps)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/04d_Org_Roles_RACI.md` (38 named roles + 10 sub-domain RACI tables)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/05_Regulatory_Applicability.md` (5 regulations + 158 sub-clause rows + RTS weekend clause)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/05b_Ambiguity_Register.md` (1,490 corpus cards + Top 20 by clause_id with V-04 fixed distribution GDPR 5 + CRA 4 + NIS 2 4 + DORA 4 + AI Act 3)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/06_Clause_Mapping_Matrix.md` (150 clauses Markdown companion)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/06b_DORA_ICT_Risk_Framework.md` (26 DORA articles + 5 tensions T-001..T-005)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/07_Structured_Compliance_Matrix.md` (38 sub-domains × 5 regulations + 5 strategic tensions + 10 compound event scenarios + 5.5 T-005)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/07b_Proportionality_Profile.md` (Track B case instance — 31 RIGOROUS + 7 STANDARD; §3 distribution + §4 per-sub-domain table + §5 tension cross-reference + §6 GATE-P)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/07c_Adjusted_Objectives.md` (76 detail cards with 18 fields each + 5 tensions resolved to multi-paragraph depth + §5 Track B decision trail)
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/Citation_Index.md` (122 unique citations across 6 Rich docs; 94% corpus-matched; 7 DECLARATION_GAP entries)
- `00_METHODOLOGY/REFERENCE/proportionality_model.md` (Track B spec — §1 invariant, §2 scale, §5.1 decision table, §6 tier definitions, §9 validation)
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/validation/VALIDATOR_TIER2.md` (parallel Tier 2 validator for Case_02 MEDIUM-tier case)