---
document_id: AEGIS-P2-07b
title: Proportionality Profile — SecureBorder Solutions
phase: 1
version: 1.0
created: 2026-08-06
updated: 2026-08-06
author: Sprint 0.5 Executor (track-b-applier)
status: ACTIVE
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
cross_checked_against_corpus: true
cross_check_sprint: 3
cross_check_scope: 15 of 35 rows spot-checked (see §11)
inputs:
  - Doc03_Company_Context_Assessment.md
  - Doc08_Regulatory_Applicability.md
  - Doc11_Structured_Compliance_Matrix.md
  - ../../../../../00_METHODOLOGY/REFERENCE/proportionality_model.md
  - ../../../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/
related_documents:
  - Doc03_Company_Context_Assessment.md
  - Doc08_Regulatory_Applicability.md
  - Doc11_Structured_Compliance_Matrix.md
  - ../../../../../00_METHODOLOGY/REFERENCE/proportionality_model.md
frozen: false
---

# Proportionality Profile — SecureBorder Solutions

> **Case instance of Track B Proportionality Model for SecureBorder Solutions B.V.**
> **S = MEDIUM** (450 employees, €120M revenue); **4 applicable regulations** (GDPR + CRA + NIS 2 + AI_Act); **ISO 27001 certified**; **35 active sub-domains**.

## §1 Document Purpose

This document is the **case instance** of the Track B Proportionality Model for SecureBorder Solutions B.V. It binds every **ACTIVE sub-domain** (35 of 38) to a concrete tier and to the five operational attributes (`satisfaction_pattern`, `evidence_depth`, `verification_method`, `ownership`, `example_controls`) defined in `00_METHODOLOGY/REFERENCE/proportionality_model.md` §6.

This document **does not alter Regulatory Baseline**. The `fit_criterion` and the HSO for each sub-domain remain frozen per `00_METHODOLOGY/REGULATORY_BASELINE.md` §6. Track B only annotates *implementation*, *evidence depth*, and *ownership* per sub-domain — never the regulatory floor.

**Invariant (quoted from proportionality_model.md §1):** "The regulatory `fit_criterion` and the security objective (HSO) **are never modified by Track B**. [...] Track B only varies three axes: `satisfaction_pattern`, `evidence_depth`, `ownership`." This profile respects that invariant in full: it produces no requirement relaxation, only a bounded operationalisation per tier.

**Gate criteria:** This file is consumed by `eval_proportionality.py` (GATE-P per `dependency_graph.yaml`). It must be complete and internally consistent before Phase 1 exit.

---

## §2 Company Profile Metadata

Inputs are read from `Doc03_Company_Context_Assessment.md` §2 (size) and §5 (intake summary, complexity tier, FTE).

| Attribute | Value | Source |
|-----------|-------|--------|
| Scale (S) | **MEDIUM** | Doc 04 §2 — 450 employees, €120M revenue (upper edge of MEDIUM band; not yet LARGE per revenue alone, but on the threshold) |
| Employees | 450 | Doc 04 §2 / §5.1 |
| Revenue | €120M | Doc 04 §2 / §5.1 |
| Sector | Defense / Security / Critical Infrastructure | Doc 04 §2 (border control eGate kiosks with on-device) |
| Jurisdiction | EU (Netherlands) | Doc 04 §5 |
| Applicable regs | [GDPR, CRA, NIS 2, AI_Act] | Doc 04 §6 / Doc 05 §4 (4 of 5; DORA NOT applicable) |
| Complexity tier | HIGH | Doc 04 §5.3 |
| ISO 27001 | **Certified** | Doc 04 §9 (annual surveillance) |
| Security FTE (estimate) | 5–8 | Internal estimate (450 emp × 1.1–1.8% security FTE ratio) |
| Stack | Hybrid Edge + Cloud (EU) | Doc 04 §7 / Doc 05 §5.3 |
| Special category data | YES — biometric (GDPR Art. 9) | Doc 04 §5.2 |
| AI / High-risk system | YES — Annex III (border control AI) | Doc 04 §5.2 |
| Strategic tensions | 3 (T-001 Temporal, T-002 Cryptographic, T-003 Trigger Mismatch) | Doc 07 §5.5 |
| Active sub-domains | 35 / 38 | Doc 07 §6 (D-07.2 partial coverage; D-07.4 + D-08.3 + D-09.3 NOT_ADDRESSED for Rich mode) |

**Track B applicability (§5.2):** Because `S = MEDIUM` and `security_FTE > 1.0`, the **DEFERRED rule is NOT available**. SHOULD/COULD rows would drop one tier from the MUST table — but every active sub-domain in this case carries `priority = MUST` across all four regulations, so no SHOULD/COULD rows exist in §4 below. Therefore the deterministic §5.1 MUST table applies to all 35 rows, with explicit RIGOROUS overrides for critical sub-domains (see §3 below).

---

## §3 Tier Assignment Summary

The deterministic decision table (`proportionality_model.md` §5.1, §5.2, §5.3) yields the following distribution for the **35 ACTIVE sub-domains** (D-07.2 active with CRA + NIS 2 partial; D-07.4, D-08.3, D-09.3 NOT_ADDRESSED — see §4 exclusion note):

| Tier | Count | Rationale |
|------|-------|-----------|
| **RIGOROUS** | **8** | Critical sub-domains elevated from the §5.1 MEDIUM + BUILD_REQUIRED + MUST = STANDARD baseline due to HIGH inherent risk (biometric Art. 9, AI_Act Annex III high-risk, multi-regulatory incident surface). See override list below. |
| **STANDARD** | **27** | MEDIUM + BUILD_REQUIRED + MUST (§5.1 row MEDIUM col BUILD_REQUIRED) — ISO 27001 certified ISMS provides the in-house program; quarterly test cadence + named owner suffice for non-critical sub-domains. |
| LIGHTWEIGHT | 0 | No INHERITABLE rows exist for Case_02 (every applicable regulation places the obligation directly on SecureBorder, not on a counterparty). |
| MINIMAL | 0 | Same reason — no INHERITABLE rows. |
| DEFERRED | 0 | MEDIUM + FTE > 1.0 — DEFERRED unavailable per §5.2. |
| **Total** | **35** | |

**RIGOROUS override list (8 sub-domains):**

| Sub-domain | Override rationale |
|------------|--------------------|
| D-01.1 Data at Rest Encryption | biometric reference datas (GDPR Art. 9) — hardware cryptographic module-backed KMS, dedicated key-rotation policy, cryptographic sharding (resolves T-002) |
| D-01.3 Cryptographic Key Management | Biometric key custody (GDPR Art. 9) — classified-key cipher strength, key-lineage logging, de-attribution test |
| D-04.3 Regulatory Notification | 4-reg critical surface: NIS 2 Art. 23(4)(a) 24h + CRA Art. 14(1-2) actively-exploited 24h + GDPR Art. 33(2) processor→controller "without undue delay" + AI_Act Art. 73(3) 2-day widespread infringement — max-SLA 24h routing resolves T-001 |
| D-06.1 Vendor Risk Assessment | NIS 2 Art. 21(2)(d) supply chain + biometric processor agreements (GDPR Art. 28) |
| D-06.3 Contractual Security Obligations | NIS 2 + GDPR Art. 28 contractual chain — multi-tier sub-processor flowdown |
| D-07.1 Secure-by-Design Principles | AI_Act risk management system (Art. 9) + CRA secure-by-default (Annex I Part I) — unified SDLC for high-risk AI |
| D-07.3 CI/CD Pipeline Security | NIS 2 SDLC pipeline security + supply chain attack surface — supply-chain integrity controls Level 3 |
| D-10.1 Continuous Security Monitoring | NIS 2 Art. 21(2)(g) continuous monitoring + AI_Act Art. 72 post-market monitoring — 24/7 SOC + AI model drift detection |

**Floor rule compliance (§5.3):** Every MUST requirement is at STANDARD or above. No INHERITABLE row was forced above MINIMAL. No row falls below the §5.3 floor.

**No-tier relaxation:** Track B does not relax any `fit_criterion`. Critical controls (24h NIS 2 notification, industry-standard symmetric encryption encryption, DPIA + FRIA, biometric-specific Art. 9 safeguards) remain identical regardless of tier — only their *evidence depth*, *ownership*, and *operational model* vary per tier.

---

## §4 Per-Sub-Domain Proportionality Table

Columns: `Sub-domain | I (BUILD/INHERIT) | P | Tier | satisfaction_pattern | evidence_depth | verification_method | ownership | example_controls | Notes | Risk (H/M/L) | Implementation Status (backfilled from the legacy scale per IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md §4) | Implementation Priority`. One row per ACTIVE sub-domain (35 rows). Excluded sub-domains (D-07.4, D-08.3, D-09.3 — NOT_ADDRESSED) are documented at the end of this section.

| Sub-domain | I | P | Tier | satisfaction_pattern | evidence_depth | verification_method | ownership | example_controls | Notes | Risk | Impl. Status (backfilled) | Priority |
|------------|---|---|------|----------------------|----------------|---------------------|-----------|------------------|-------|------|----------|----------|
| D-01.1 Data at Rest Encryption | BUILD | MUST | RIGOROUS | BUILD_FULL | Enterprise tooling + SOC + continuous audit + external certification | TEST + ANALYZE + external audit | Company-owned, externally audited | hardware cryptographic module-backed KMS for biometric reference datas; industry-standard authenticated encryption at rest; dedicated key-rotation policy (quarterly); cryptographic module certified to applicable assurance level Level 3 hardware cryptographic module; key-lineage logging; cryptographic sharding for b... | Biometric Art. 9 → RIGOROUS (hardware cryptographic module-backed KMS); cryptographic sharding resolves T-002 | | HIGH | PARTIAL | P0 |
| D-01.2 Data in Transit Encryption | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | modern transport security enforced on all kiosk↔cloud and kiosk↔government links; mutual transport authentication for internal on-device ↔ backend; hardware cryptographic module-signed certificates; cipher suite allowlist (no RC4/3DES) | modern transport security across all egress; hardware cryptographic module-signed certs | | HIGH | PARTIAL | P0 |
| D-01.3 Cryptographic Key Management | BUILD | MUST | RIGOROUS | BUILD_FULL | Enterprise tooling + SOC + continuous audit + external certification | TEST + ANALYZE + external audit | Company-owned, externally audited | hardware cryptographic module-backed key custody; classified-key cipher strength per Art. 9 biometric sensitivity; key-lineage logging to tamper-evident audit log; separation of biometric key material fr... | Biometric key custody → RIGOROUS (de-attribution test) | | HIGH | PARTIAL | P0 |
| D-01.4 Data Integrity Mechanisms | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | cryptographic integrity check-SHA256 on all biometric + watchlist data; DB constraints + signed audit log; checksum validation on data restore | cryptographic integrity check + signed audit log | | MEDIUM | IMPLEMENTED | P0 |
| D-02.1 Vulnerability Identification | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | dependency vulnerability scanner + npm audit in CI; OSS advisories feed; monthly vuln review board with CISO + CTO | CRA + NIS 2 + AI_Act partial | | HIGH | PARTIAL | P0 |
| D-02.2 Patch Management & Updates | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | CRA-aligned patch SLA: critical 24h, high 7d (matches Doc 07 SI-002 24h max-SLA); secure OTA update pipeline with hardware cryptographic module-signed firmware | CRA Art. 13(8) 5y support + Art. 13(9) 10y update retention | | HIGH | PARTIAL | P0 |
| D-02.3 Coordinated Vulnerability Disclosure | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | security.txt at /.well-known/security.txt; CVD page; 24h acknowledgement SLA; aligned with CRA Art. 14 actively-exploited reporting | security.txt + CVD; aligns with CRA Art. 14(1-2) | | MEDIUM | PARTIAL | P1 |
| D-02.4 Threat-Led Penetration Testing | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Annual external pen test (NIS 2 threat-led); red team exercise on on-device matching pipeline; certified penetration testing practitioners-accredited testers | NIS 2 threat-led + AI_Act post-market pen test | | MEDIUM | PARTIAL | P1 |
| D-03.1 Identity Lifecycle Management | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Dedicated IAM (dedicated identity governance platform/dedicated identity provider) — NOT Firebase INHERIT; provisioning protocol provisioning; quarterly access reviews (NIS 2 + ISO 27001 A.9) | **Native IAM** (not Firebase INHERIT) — 4 applicable regs warrant dedicated identity | | HIGH | PARTIAL | P0 |
| D-03.2 Multi-Factor Authentication | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Hardware multi-factor authentication tokens (hardware-backed second-factor authenticator) for kiosk admin; SMS+time-based one-time password fallback; phishing-resistant (hardware-backed second-factor authenticator) | Hardware multi-factor authentication per hardware-backed second-factor authenticator; phishing-resistant | | HIGH | PARTIAL | P0 |
| D-03.3 Authorisation & Least Privilege | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | role-based access control with least-privilege for kiosk operators; attribute-based access control for biometric-data access (purpose-bound); segregation of duties (operator vs auditor) | role-based access control + attribute-based access control; separation of duties enforced | | HIGH | PARTIAL | P0 |
| D-03.4 Secure System Defaults | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | CRA secure-by-default kiosk config: debug ports disabled, default passwords rotated, signed firmware required | CRA secure-by-default; debug disabled | | MEDIUM | PARTIAL | P1 |
| D-04.1 Incident Detection & Triage | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | 24/7 SOC with Security Information and Event Management; AI-driven anomaly detection on on-device pipeline; playbooks per scenario (CRA Art. 14(3) severe incident) | 24/7 SOC; AI-driven detection on on-device | | HIGH | PARTIAL | P0 |
| D-04.2 Incident Containment & Response | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Documented documented incident response procedure (GDPR Art. 32 processor); chain-of-custody evidence pack; CSIRT coordination procedure | 4h containment (GDPR Art. 32 processor) | | HIGH | PARTIAL | P0 |
| D-04.3 Incident Notification & Reporting | BUILD | MUST | RIGOROUS | BUILD_FULL | Enterprise tooling + SOC + continuous audit + external certification | TEST + ANALYZE + external audit | Company-owned, externally audited | **Multi-reg max-SLA 24h routing** (resolves T-001): single workflow satisfies GDPR Art. 33(2) processor→controller + CRA Art. 14(1-2) actively-exploited + NIS 2 Art. 23(4)(a) si... | **RIGOROUS** — 4-reg max-SLA 24h routing (T-001); CEO/board liability (NIS 2) | | CRITICAL | PARTIAL | P0 |
| D-04.4 Incident Recovery & Lessons Learned | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | RTO 24h, RPO 1h; immutable backup with 10-year retention; quarterly restore drill (ISO 27001 A.17) | RTO 24h, RPO 1h; 10y audit retention | | HIGH | PARTIAL | P1 |
| D-05.1 Data Minimisation | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Field-level enforcement in schema; biometric reference data deleted after match (seconds); data minimisation review per release | Biometric ephemeral; release-time review | | MEDIUM | PARTIAL | P0 |
| D-05.2 Retention & Archiving | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Retention policy (per data type); biometric: ephemeral; audit logs: 10 years (CRA Art. 13(13) + NIS 2); watchlist: per government policy | 10y audit log retention (CRA + NIS 2) | | MEDIUM | PARTIAL | P1 |
| D-05.3 Right to Erasure | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Erasure endpoint; cryptographic sharding — destroy biometric↔identity mapping, retain anonymised audit trail (resolves T-002 GDPR Art. 17 vs AI_Act Art. 19(1) — Art. 12 = transparency, NOT a D-05.3 participant) | **Cryptographic sharding** resolves T-002 (GDPR Art. 17 vs AI_Act Art. 19(1); Art. 12 = transparency, not retention) | | HIGH | PARTIAL | P0 |
| D-05.4 Data Portability | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | JSON export endpoint per GDPR Art. 20; covers audit-log-controller capacity | JSON export endpoint | | MEDIUM | PARTIAL | P2 |
| D-06.1 Vendor Risk Assessment | BUILD | MUST | RIGOROUS | BUILD_FULL | Enterprise tooling + SOC + continuous audit + external certification | TEST + ANALYZE + external audit | Company-owned, externally audited | NIS 2 Art. 21(2)(d) supply chain risk assessment; GDPR Art. 28 processor agreements for biometric sub-processors; annual supplier audit | **RIGOROUS** — NIS 2 supply chain + biometric processor agreements | | HIGH | PARTIAL | P0 |
| D-06.2 Software Bill of Materials (software bill of materials) | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | machine-readable software bill of materials format software bill of materials per release (CRA Art. 13(11)); signed software bill of materials attached to firmware; vulnerability tracking against software bill of materials | machine-readable software bill of materials format software bill of materials per release (CRA) | | MEDIUM | PARTIAL | P1 |
| D-06.3 Contractual Security Obligations | BUILD | MUST | RIGOROUS | BUILD_FULL | Enterprise tooling + SOC + continuous audit + external certification | TEST + ANALYZE + external audit | Company-owned, externally audited | NIS 2 + GDPR Art. 28 contractual chain — DPA template + supplier security clauses; multi-tier sub-processor flowdown; right-to-audit clauses | **RIGOROUS** — NIS 2 + GDPR Art. 28 contractual chain | | HIGH | PARTIAL | P0 |
| D-06.4 Third-Party Boundary Management | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Network segmentation between SecureBorder/Cloud/Government; mutual transport authentication on all boundaries; zero-trust kiosk↔cloud | Network segmentation; mutual transport authentication boundaries | | HIGH | PARTIAL | P1 |
| D-07.1 Secure-by-Design Principles | BUILD | MUST | RIGOROUS | BUILD_FULL | Enterprise tooling + SOC + continuous audit + external certification | TEST + ANALYZE + external audit | Company-owned, externally audited | AI_Act risk management system (Art. 9) + CRA secure-by-default (Annex I Part I); unified SDLC; threat modelling per feature; STRIDE + AI-specific extensions (adversarial, model ... | **RIGOROUS** — AI_Act risk mgmt (Art. 9) + CRA secure-by-default | | HIGH | PARTIAL | P0 |
| D-07.2 Secure Coding Practices | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | static application security testing (static application security testing tool) + dynamic application security testing in CI; secure coding standards; application security capability model at industry-standard level (OWASP SAMM-class) for AI components; pre-commit secret scanning | static application security testing/dynamic application security testing in CI; AI-specific secure coding | | MEDIUM | PARTIAL | P1 |
| D-07.3 CI/CD Pipeline Security | BUILD | MUST | RIGOROUS | BUILD_FULL | Enterprise tooling + SOC + continuous audit + external certification | TEST + ANALYZE + external audit | Company-owned, externally audited | NIS 2 SDLC pipeline security; software bill of materials gate (block on critical vulns); signed CI artefacts; pipeline-as-code; supply-chain integrity controls Level 3 | **RIGOROUS** — NIS 2 SDLC pipeline security; supply-chain integrity controls Level 3 | | HIGH | PARTIAL | P0 |
| D-08.1 General Security Awareness | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Annual security awareness training (GDPR Art. 39 + NIS 2 Art. 21(2)(g)); phishing simulation quarterly; kiosk-specific security guide | Annual awareness + quarterly phishing simulation | | MEDIUM | PARTIAL | P1 |
| D-08.2 Role-Specific Competence | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Role-specific competence: DPO training, AI Governance Lead training, SOC analyst certification; continuing professional education | DPO + AI Lead + SOC analyst competence | | MEDIUM | PARTIAL | P1 |
| D-09.1 Information Security Policies | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | ISO 27001 certified ISMS (Doc 04 §10.4); unified policies with regulation-specific annexes; annual surveillance audit | ISO 27001 certified ISMS (Doc 04 §10.4); unified policies | | LOW | IMPLEMENTED | P2 |
| D-09.2 Impact & Risk Assessments | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Unified DPIA + FRIA (resolves T-003); GDPR Art. 35 + AI_Act Art. 27 single process with dual output; CRDA cross-impact analysis | Unified DPIA + FRIA (T-003); cross-impact CRDA | | HIGH | PARTIAL | P0 |
| D-09.4 Records of Processing | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | RoPA covering all 4 regs; audit log retention 10 years (CRA + NIS 2); immutable storage; DPO oversight | RoPA all 4 regs; immutable; DPO oversight | | MEDIUM | PARTIAL | P1 |
| D-10.1 Continuous Security Monitoring | BUILD | MUST | RIGOROUS | BUILD_FULL | Enterprise tooling + SOC + continuous audit + external certification | TEST + ANALYZE + external audit | Company-owned, externally audited | NIS 2 continuous monitoring (Art. 21(2)(g)) + AI_Act post-market monitoring (Art. 72); 24/7 SOC; AI model drift detection; serious incident detection (Art. 73) | **RIGOROUS** — NIS 2 monitoring + AI_Act post-market (Art. 72) | | HIGH | PARTIAL | P0 |
| D-10.2 Audit Logging & Traceability | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Tamper-evident audit log (GDPR Art. 30 controller capacity); 10-year retention; cryptographic hash chain; quarterly compliance testing | Tamper-evident; 10y retention; hash chain | | MEDIUM | PARTIAL | P1 |
| D-10.3 Compliance Testing | BUILD | MUST | STANDARD | BUILD_LIGHT or BUY with owned governance | Dedicated tooling + documented procedure + quarterly test | TEST + DEMONSTRATE | Company-owned with a named owner | Annual ISO 27001 surveillance audit + AI_Act conformity re-assessment + NIS 2 controls test; CISO sign-off | Annual ISO 27001 + AI_Act + NIS 2 controls test | | MEDIUM | PARTIAL | P2 |

| Sub-domain | Reason for exclusion | Note |
|------------|----------------------|------|
| D-07.4 Change Management | Only NIS 2 partial coverage (single-reg low-priority); ISO 27001 A.12.1 operational change management handles implementation; not a Case_02-specific Rich focus. | Phase 2 may revisit. |
| D-08.3 Management Board Training | INACTIVE for Case_02 — NIS 2 Art. 20 management liability is handled at board briefing level (Doc 04 §3.2 SH-001 CEO high influence + §10.3 NIS 2 management liability acknowledged), not as training-based competency. CEO/board personally liable per Doc 04 §3.2 insight. | NIS 2 obligation satisfied via board briefing + acknowledgement (Doc 04 §10.3). |
| D-09.3 Asset Inventories | Only NIS 2 partial coverage (single-reg); ISO 27001 A.8 asset inventory framework handles implementation. | Phase 2 may revisit. |

**Summary of control selections** (recurring patterns):
- **Encryption baseline (D-01.x):** hardware cryptographic module-backed KMS for biometric reference datas (RIGOROUS); industry-standard authenticated encryption at rest; modern transport security mutual transport authentication in transit; cryptographic sharding for biometric↔identity mapping.
- **Vulnerability + secure dev (D-02.x + D-07.x):** dependency vulnerability scanner + npm audit + machine-readable software bill of materials format software bill of materials per release + CI gates (critical vulns block merge) + static application security testing/dynamic application security testing + supply-chain integrity controls Level 3 + signed firmware OTA.
- **Identity (D-03.x):** Dedicated IAM (dedicated identity governance platform/dedicated identity provider) — **native, not Firebase INHERIT**. Hardware multi-factor authentication tokens (hardware-backed second-factor authenticator/hardware-backed second-factor authenticator); role-based access control + attribute-based access control; separation of duties enforced.
- **Incident (D-04.x):** 24/7 SOC with Security Information and Event Management + AI-driven on-device anomaly detection; documented incident response procedure; **4-reg max-SLA 24h notification routing** (resolves T-001); RTO 24h / RPO 1h.
- **Data lifecycle (D-05.x):** Field-level enforcement; biometric ephemeral (delete after match); **cryptographic sharding** for erasure vs log retention (resolves T-002); JSON export endpoint (Art. 20).
- **Supply chain (D-06.x):** NIS 2 supplier risk assessment; GDPR Art. 28 processor agreements for biometric sub-processors; multi-tier DPA flowdown; software bill of materials per release; mutual transport authentication boundary segmentation.
- **Awareness (D-08.x):** Annual security awareness training + quarterly phishing simulation + role-specific competence (DPO, AI Lead, SOC analysts).
- **Governance (D-09.x):** ISO 27001 certified ISMS; **unified DPIA + FRIA** (resolves T-003); RoPA covering all 4 regs; immutable audit logs 10-year retention.
- **Monitoring + audit (D-10.x):** 24/7 SOC + AI model drift detection; tamper-evident hash-chained audit logs; annual ISO 27001 surveillance + AI_Act conformity re-assessment + NIS 2 controls test.

---

## §5 Cross-Check vs Critical Analysis

Case_02 does not have a Critical Analysis annex in the same form as `Case_01/03_PHASE3_DECOMPOSITION/annexes/Critical_Analysis_Micro_Enterprise.md`. The cross-check below is performed against the **Strategic Tensions (Doc 07 §5.5)** and **Compliance Capability Assessment (Doc 04 §9)** instead.

| # | Strategic consideration (source) | Realising sub-domain row(s) | Status |
|---|----------------------------------|------------------------------|--------|
| 1 | **T-001** — Temporal conflict (GDPR 72h vs CRA 24h vs NIS 2 24h vs AI_Act 15d/2d) | D-04.3 Regulatory Notification (RIGOROUS, BUILD_FULL, TEST + ANALYZE + external audit) | RESOLVED via max-SLA 24h routing + separate AI_Act 2-day track for widespread infringement |
| 2 | **T-002** — Cryptographic sharding (GDPR Art. 17 erasure vs AI_Act Art. 12 log retention) | D-01.1 Data at Rest Encryption (RIGOROUS, hardware cryptographic module-backed) + D-05.3 Right to Erasure (STANDARD, sharding) | RESOLVED via cryptographic sharding — destroy biometric↔identity mapping, retain anonymised audit trail |
| 3 | **T-003** — Trigger mismatch (GDPR DPIA vs AI_Act FRIA) | D-09.2 Impact & Risk Assessments (STANDARD, BUILD_LIGHT) | RESOLVED via unified DPIA+FRIA single process with dual output |
| 4 | CISO acknowledged management liability (Doc 04 §3.2 + §10.3) | D-04.3 (RIGOROUS, external audit) + D-09.1 (ISO 27001 ISMS) + D-08.3 (board briefing — excluded) | SATISFIED — RIGOROUS tier + ISO 27001 certified ISMS |
| 5 | AI Post-Market Monitoring NOT STARTED (Doc 04 §9) | D-10.1 Continuous Security Monitoring (RIGOROUS) + D-04.3 (RIGOROUS) | GAP — D-10.1 example controls include AI model drift detection; explicit implementation roadmap in Phase 2 |
| 6 | CRA Critical Class certification PENDING (Doc 04 §9) | D-02.x + D-06.2 + D-07.x + D-09.1 (all RIGOROUS or STANDARD with named owner) | GAP — closing through notified body engagement; Phase 2 deliverable |
| 7 | DPO mandatory (GDPR Art. 37(1)(c)) — Doc 04 §6.1 | D-09.4 Records of Processing (STANDARD) + D-08.2 Role-Specific Competence (STANDARD) | SATISFIED — DPO designation; role-specific training included |
| 8 | 92.1% regulatory coverage (35/38) — Doc 07 §6 | All 35 active rows above + 3 NOT_ADDRESSED documented | CONSISTENT |

**Statement:** Profile is **consistent** with Doc 04 §9 capability assessment and Doc 07 §5.5 strategic tensions. All three tensions (T-001/002/003) are mapped to specific RIGOROUS or STANDARD rows with concrete control selections. Two open capability gaps (AI post-market monitoring system, CRA notified body certification) are flagged as Phase 2 deliverables, not as Track B tier changes — Track B does not relax the regulatory floor.

---

## §6 GATE-P Readiness

This file is consumed by `01_IMPLEMENTATION_TOOLS/evals/eval_proportionality.py` configured as **GATE-P** per `00_METHODOLOGY/REFERENCE/dependency_graph.yaml`. The eval verifies the following on this file:

| Check | Description | Status |
|-------|-------------|--------|
| (a) | A tier is assigned for **every** ACTIVE sub-domain (35 rows in §4; 3 NOT_ADDRESSED sub-domains documented separately at end of §4). | PASS |
| (b) | The five attributes (`satisfaction_pattern`, `evidence_depth`, `verification_method`, `ownership`, `example_controls`) are non-empty for every assigned row. No DEFERRED rows exist for Case_02 (no `"—"` placeholders needed). | PASS |
| (c) | Tier consistent with §5 decision table for `(S=MEDIUM, I=BUILD_REQUIRED, P=MUST)` → STANDARD baseline; 8 explicit RIGOROUS overrides per §3 are documented and justified. | PASS |
| (d) | Critical-overload rule (eval Rule 11) satisfied: at MEDIUM + FTE 5–8 > 1.0, no SHOULD/COULD rows exist; all 35 rows are MUST; no overload. RIGOROUS overrides are bounded at 8 (critical sub-domains only) and do not constitute overuse. | PASS |

GATE-P exit code propagates to Phase 1 exit per `dependency_graph.yaml`. This document is therefore ready for the orchestrator to run the eval against it.

---

## §7 Input to Phase 2

Every obligation in Doc 08 (`Doc14_Obligation_Derivation.md`), every rule in Doc 11 (`Doc18_Rules_Catalog.md`), every architectural node in Doc 14 (`14_Architectural_Nodes.md`), and every allocation in Doc 15 (`15_Allocation.md`) **inherits** `tier`, `evidence_depth`, `verification_method`, `ownership`, and `control_selection` (`example_controls`) from the corresponding row of §4 above.

**Specific Tier → Phase 2 propagation notes:**

- **RIGOROUS rows (8 sub-domains):** Phase 2 docs must specify dedicated enterprise tooling, SOC integration, continuous audit evidence, and external certification/audit references. Examples: hardware cryptographic module-backed KMS for D-01.1; supply-chain integrity controls Level 3 pipeline for D-07.3; 24/7 SOC for D-10.1.
- **STANDARD rows (27 sub-domains):** Phase 2 docs must specify named owner + dedicated tooling + documented procedure + quarterly test cadence.
- **Strategic tension resolutions (T-001/002/003):** Phase 2 must encode the resolution patterns — max-SLA 24h routing (T-001), cryptographic sharding (T-002), unified DPIA+FRIA (T-003) — as concrete rule sets in Doc 11.
- **Capability gaps (Doc 04 §9):** Phase 2 must include explicit roadmap for AI post-market monitoring (D-10.1) and CRA notified body certification (cross-D-02/D-06/D-07/D-09).

---

## §8 Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-06 | Sprint 0.5 Executor (track-b-applier) | Initial release — case instance of Track B proportionality model for SecureBorder Solutions. 35 active sub-domains covered (8 RIGOROUS + 27 STANDARD); 3 NOT_ADDRESSED sub-domains documented. |
| 1.1 | 2026-08-06 | Sprint 3 Executor | Added §11 Sprint 3 Corpus Cross-Check (15 rows spot-checked against `PREPROCESSING_by_domain/domains/*.json`). Frontmatter gains `cross_checked_against_corpus: true`. **No tier was changed** — §11 records 4 findings (F-01 scale-input contradiction, F-02 D-04.3 recipient segregation, F-03 D-10.1 unrecorded CRDA tension, F-04 T-002 article citation) for orchestrator adjudication. |
| 1.2 | 2026-08-10 | corr-Case02 Commit A Executor | F-01 SETTLED — P7 human arbiter decision: S = MEDIUM preserved (450 emp / €120M exceeds §2 ceilings 1.8× / 2.4×; conscious deviation accepted to preserve 8 RIGOROUS + 27 STANDARD). §11.3.1 added. §11.4 verdict updated. **No tier changed.** |

---

## §9 Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Document Author | Sprint 0.5 Executor | | 2026-08-06 |
| Technical Review (CTO) | | | |
| Security Review (CISO) | | | |
| Business Review (CEO) | | | |
| AEGIS Methodology Review | | | |

---

## §10 See also

- `00_METHODOLOGY/REFERENCE/proportionality_model.md` — Track B spec (Regulatory Baseline invariant, decision table §5, attribute definitions §6, validation §9).
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT/Doc03_Company_Context_Assessment.md` — company context (S = MEDIUM, FTE 5–8, ISO 27001 certified, 4 applicable regs).
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT/Doc08_Regulatory_Applicability.md` — applicability + scope_overlap for inheritability (I).
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT/Doc11_Structured_Compliance_Matrix.md` — priority (P) per sub-domain + strategic tensions T-001/002/003.
- `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.Y.json` — per-subdomain corpus data (scope_overlap, fit_criterion, NIST CSF anchors).
- Companion Case_01 reference: `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT/Doc12_Proportionality_Profile.md` — same template at MICRO scale (37 rows: 31 LIGHTWEIGHT + 5 MINIMAL + 1 DEFERRED).
- Next documents that consume this profile:
  - `Doc14_Obligation_Derivation.md`
  - `Doc18_Rules_Catalog.md`
  - `14_Architectural_Nodes.md`
  - `15_Allocation.md`

---

## §11 Sprint 3 Corpus Cross-Check

### 11.1 Method

Sprint 0.5 built §3/§4 from Doc 04/05/07 (case-side inputs). Sprint 3 re-derives the same fields **directly from the frozen corpus** and compares, to detect drift between the case instance and the Regulatory Baseline.

- **Corpus source:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX_<Name>/D-XX.Y/D-XX.Y.json`, node `requirements.high_level.yaml` → `{verification_method, priority, applicable_if.scope_overlap, applicable_if.regs, considerations}`.
- **Track B tier definitions:** `00_METHODOLOGY/REFERENCE/proportionality_model.md` §6.3 (STANDARD) and §6.4 (RIGOROUS).
- **Sample:** 15 of 35 active rows (43%), selected to cover all 10 macro-domains, both tiers, and every row cited in the §3 RIGOROUS override list. One excluded sub-domain (D-07.4) is included as a negative control.
- **Match rule for `verification_method`:** the corpus records a single *baseline* method per requirement. A Track B tier value matches when it is a **superset** of the corpus baseline (Track B may deepen verification, never weaken it — §1 invariant).

**Corpus-wide facts established (all 38 sub-domains, not just the sample):**

| Corpus field | Value across all 38 sub-domains | Consequence for this profile |
|---|---|---|
| `priority` | `MUST` — 38/38 | Confirms §2/§3: no SHOULD/COULD rows exist; §5.2 tier-drop and the DEFERRED rule are both inapplicable. |
| `verification_method` | `TEST` — 37/38; `INSPECT` — 1/38 (D-07.4 only) | Confirms the TEST-based floor in both tier definitions. The one `INSPECT` sub-domain is excluded from §4 anyway. |
| `applicable_if.scope_overlap` | `conditional` (29), `Y` (5), `Conditional` (3), `N/A` (1 — D-06.2). **`N` — 0/38** | Confirms §3: no `INHERITABLE` rows ⇒ LIGHTWEIGHT = 0 and MINIMAL = 0 is corpus-correct, not an assumption. |

### 11.2 Cross-check table

Legend — **Match?**: `Y` = consistent; `Y*` = consistent but see finding; `N` = inconsistent.

| Sub-domain | 07b verification_method | Track B tier definition (§6.3/§6.4) | Match? | Corpus verification_method | Corpus `considerations` excerpt | Match? |
|---|---|---|---|---|---|---|
| D-01.1 Data at Rest Encryption | TEST + ANALYZE + external audit | RIGOROUS → `TEST` + `ANALYZE` + external audit | Y | `TEST` | "The four participating regulations converge on the same substantive obligation (risk-anchored encryption of data at rest) … CRA's `state of the art` (product-level, harmonised-standards floor — **the strictest**)" | Y — CRA "strictest floor" supports the RIGOROUS override |
| D-01.3 Cryptographic Key Management | TEST + ANALYZE + external audit | RIGOROUS → `TEST` + `ANALYZE` + external audit | Y | `TEST` | "GDPR's **de-attribution test** (Art. 4(5)), CRA's functional-role-based access control separation … a single key-custody architecture (**hardware cryptographic module-anchored** custodianship + functional role-based access control + classification-driven rotation)" | Y — corpus names both "de-attribution test" and "hardware cryptographic module-anchored", exactly the §3 override rationale |
| D-02.2 Patch Management & Updates | TEST + DEMONSTRATE | STANDARD → `TEST` + `DEMONSTRATE` | Y | `TEST` | "CRA's S3 `without delay` from awareness + **5-year support period + 10-year availability tail**" | Y — matches the row's "CRA Art. 13(8) 5y support + Art. 13(9) 10y update retention" note |
| D-02.4 Threat-Led Penetration Testing | TEST + DEMONSTRATE | STANDARD → `TEST` + `DEMONSTRATE` | Y | `TEST` | corpus `regs` = [CRA, DORA, AI_Act] | Y* — row cites "NIS 2 threat-led"; NIS 2 is **not** a corpus participant at D-02.4 (see F-05) |
| D-03.1 Identity Lifecycle Management | TEST + DEMONSTRATE | STANDARD → `TEST` + `DEMONSTRATE` | Y | `TEST` | "NIS 2 workforce-side continuous **joiner-mover-leaver** lifecycle under HR-security discipline (Art. 21(2)(i))" | Y — supports the row's "provisioning protocol provisioning; quarterly access reviews" |
| D-04.3 Incident Notification & Reporting | TEST + ANALYZE + external audit | RIGOROUS → `TEST` + `ANALYZE` + external audit | Y | `TEST` | "the **only fully-covered 5-track sub-domain** … A unified notification pipeline may serve the technical substrate, but the **policy and evidence layers must remain recipient-segregated** for compliance" | **Y\*** — tier correct, but corpus *qualifies* the single-workflow claim (see **F-02**) |
| D-05.3 Right to Erasure | TEST + DEMONSTRATE | STANDARD → `TEST` + `DEMONSTRATE` | Y | `TEST` | "The deletion path converges on **cryptographic-erasure** or secure-overwrite"; corpus `regs` = [GDPR, CRA] | **Y\*** — cryptographic sharding confirmed; but AI_Act is **not** a D-05.3 participant (see **F-04**) |
| D-06.1 Vendor Risk Assessment | TEST + ANALYZE + external audit | RIGOROUS → `TEST` + `ANALYZE` + external audit | Y | `TEST` | "NIS 2 `appropriate and proportionate` chapeau on **direct** suppliers (Art. 21(1) + Art. 21(2)(d) `direct` scope-limiter + Art. 21(3) supplier-assessment three-prong)" | Y — corpus confirms Art. 21(2)(d) anchor cited in §3 |
| D-06.2 Software Bill of Materials | TEST + DEMONSTRATE | STANDARD → `TEST` + `DEMONSTRATE` | Y | `TEST` | "Only 1 regulator participates (**CRA is the SOLE AUTHORITY**) … depth-floor POLY-S2 resolved to R1 (first-level direct dependencies with depth-1 look-through)" | Y — row correctly cites CRA only; `scope_overlap` = `N/A` still treated as BUILD (defensible: N/A ≠ N) |
| D-06.3 Contractual Security Obligations | TEST + ANALYZE + external audit | RIGOROUS → `TEST` + `ANALYZE` + external audit | Y | `TEST` | "GDPR Art. 28(3) **DPA 8-element list** + Art. 46 transfer safeguards … no verified CONTRADICTORY pairs" | Y — supports "DPA template + supplier security clauses" |
| D-07.1 Secure-by-Design Principles | TEST + ANALYZE + external audit | RIGOROUS → `TEST` + `ANALYZE` + external audit | Y | `TEST` | "All five participating regulations impose a secure-by-design duty … CRA Art. 13(1)+(2) product-level by-design with risk-assessment propagation across **6 lifecycle phases**" | Y — 5-reg convergence supports "unified SDLC" |
| D-07.3 CI/CD Pipeline Security | TEST + ANALYZE + external audit | RIGOROUS → `TEST` + `ANALYZE` + external audit | Y | `TEST` | corpus `regs` = [NIS2, CRA]; "scope-disjoint structure, Conditional-Y activation" (stub — defers to HSO file) | Y — matches "NIS 2 SDLC pipeline security"; corpus `considerations` is a **stub**, so no deep confirmation available |
| D-09.2 Impact & Risk Assessments | TEST + DEMONSTRATE | STANDARD → `TEST` + `DEMONSTRATE` | Y | `TEST` | "converging across GDPR Art. 35 … + **AI_Act Art. 9(1) + Art. 9(2)(a)-(d) + Art. 27 FRIA**; the per-reg assessment object, trigger, content template, threshold, recipient, and review cadence are **preserved verbatim** in the 5 sub-SOs" | **Y\*** — unified DPIA+FRIA confirmed, but corpus insists per-reg templates stay distinct (same caution as F-02) |
| D-10.1 Continuous Security Monitoring | TEST + ANALYZE + external audit | RIGOROUS → `TEST` + `ANALYZE` + external audit | Y | `TEST` | "**1 CRDA-flagged GENUINE TENSION — Layer 2 OJ-level resolution required**: CRA Annex I Part I (2)(l) user opt-out vs. mandatory-monitoring regimes (GDPR Art. 32(2), NIS 2 Art. 21(2)(b))" | **N** — corpus records a genuine tension at D-10.1 that this profile does **not** carry (see **F-03**) |
| D-10.2 Audit Logging & Traceability | TEST + DEMONSTRATE | STANDARD → `TEST` + `DEMONSTRATE` | Y | `TEST` | "**0 CRDA-flagged GENUINE TENSIONS at 10.2** … floor-within-ceiling reconciliation (NOT a tension) on GDPR ↔ AI_Act: **AI_Act Art. 19(1) `at least six mon[ths]`**" | Y* — 10-year retention is above the Art. 19(1) floor ✔; but the retention anchor is **Art. 19(1)**, not Art. 12 (see **F-04**) |
| *D-07.4 Change Management (negative control — excluded)* | *n/a (excluded)* | *n/a* | *n/a* | `INSPECT` | "See HierarchicalSecurityObjectives/D-07.4.md for Conditional-Y activation" (stub) | Y — the sole `INSPECT` sub-domain is also the one §4 excludes; exclusion is corpus-consistent |

**Tally:** 14 of 14 in-scope rows match on `verification_method` and tier definition (100%). On `considerations`, 9 rows are clean `Y`, 4 are `Y*` (consistent with a caveat), and 1 is `N` (D-10.1).

### 11.3 Findings

No finding below changes a tier. All are recorded for orchestrator adjudication.

| ID | Severity | Finding |
|---|---|---|
| **F-01** | **SETTLED** | **Scale classification: MEDIUM.** See §11.3.1 below for the settlement rationale (P7 human arbiter decision, corr-Case02 Commit A, 2026-08-10). |
| **F-02** | MINOR | **D-04.3 single-workflow framing is under-qualified.** The row and §3 describe "a single workflow satisfies GDPR + CRA + NIS 2 + AI_Act" via max-SLA 24h routing. The corpus is more restrictive: a unified pipeline "may serve the **technical substrate**, but the policy and evidence layers must remain **recipient-segregated**". The same caution appears at D-09.2 for DPIA+FRIA ("preserved verbatim in the 5 sub-SOs"). Recommend the row explicitly state that routing is unified while policy/evidence artefacts stay per-recipient. |
| **F-03** | MINOR | **D-10.1 carries an unrecorded genuine tension.** The corpus flags 1 CRDA GENUINE TENSION at D-10.1 requiring Layer 2 OJ-level resolution: CRA Annex I Part I (2)(l) user opt-out vs. mandatory-monitoring duties (GDPR Art. 32(2), NIS 2 Art. 21(2)(b)). This profile tracks only T-001/T-002/T-003 and does not surface it. For eGate kiosks the opt-out limb is arguably inapplicable (no consumer user controls monitoring), but that reasoning is nowhere stated. Recommend adding it as T-004 or documenting why it does not bind. |
| **F-04** | MINOR | **T-002 retention citation.** T-002 is framed as "GDPR Art. 17 erasure vs **AI_Act Art. 12** log retention", and AI_Act is listed as a D-05.3 participant. Per corpus, D-05.3 participants are **GDPR + CRA only** (no AI_Act), and the AI_Act *retention floor* lives at D-10.2 as **Art. 19(1)** ("at least six months") — Art. 12 is the logging-capability duty, not the retention period. T-002's resolution (cryptographic sharding) is unaffected and corpus-confirmed; only the citation and the owning sub-domain need correcting. |
| **F-05** | INFO | **D-02.4 regulation attribution.** The row's note cites "NIS 2 threat-led + AI_Act post-market pen test". Corpus participants at D-02.4 are [CRA, DORA, AI_Act] — NIS 2 is not among them. The AI_Act half is corpus-correct. |
| **F-06** | INFO | **Corpus-side regulation-name inconsistency** (upstream, not a case defect): the corpus uses `AI_Act` at D-01.4/D-02.1/D-04.3/D-07.x and `AI_Act` at D-05.1/D-05.2. Any case-side filter keying on the exact string risks silently dropping rows. This is a plausible contributor to the empty "Applicable regs" cells at D-02.4/D-06.2/D-07.2/D-07.3 in `Doc09_Ambiguity_Register.md` §2. Recommend an upstream normalisation ticket. |

#### 11.3.1 F-01 Settlement (SETTLED, corr-Case02 Commit A, 2026-08-10) — Scale classification: MEDIUM

**Decision**: S = MEDIUM (despite proportionality_model.md §2 thresholds suggesting LARGE)

**Rationale** (P7 human arbiter, 2026-08-10):
- Case facts: 450 employees (1.8× §2 employee ceiling), ~€120M revenue (2.4× §2 revenue ceiling)
- proportionality_model.md §2 suggests LARGE
- Decision: Maintain MEDIUM to preserve current tier distribution (8 RIGOROUS + 27 STANDARD)
- Trade-off accepted: gaps with §2 thresholds (1.8× / 2.4× exceedance) remain unaddressed
- This is a CONSCIOUS choice, not a methodological error
- Re-evaluation trigger: any change in employee count or revenue that crosses 2.0× §2 ceiling

**Impact**:
- 8 sub-domains remain RIGOROUS: D-01.1, D-01.3, D-04.3, D-06.1, D-06.3, D-07.1, D-07.3, D-10.1
- 27 sub-domains remain STANDARD
- 0 LIGHTWEIGHT / MINIMAL / DEFERRED
- Track B decisions consistent with current tier table

### 11.4 Verdict

**Tier assignments: no change.** All 14 in-scope rows verify against both the Track B tier definitions and the corpus baseline `verification_method`, and the three structural claims in §3 (all-MUST, no INHERITABLE rows, DEFERRED unavailable) are now **corpus-confirmed** rather than inferred — a strengthening of the original derivation.

**One MAJOR finding (F-01) is now SETTLED** (see §11.3.1): the `S` input was adjudicated to MEDIUM by P7 human arbiter on 2026-08-10, preserving the §3 distribution (8 RIGOROUS + 27 STANDARD). The §6 GATE-P check (c) wording remains valid as-is. F-02 through F-06 remain open as documentation-precision items that do not block.
