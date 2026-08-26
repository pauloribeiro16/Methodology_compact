---
document_id: AEGIS-P3-RICH-07c-Appendix-A-OLD
title: 07c Appendix A (DEPRECATED — Detail Cards Migration)
phase: 1
version: 1.0-DEPRECATED
created: 2026-08-06
updated: 2026-08-14
author: Migrated from 07c_Adjusted_Goals.md §2a/§3a by Sprint 6 Executor (corr-010)
status: DEPRECATED
status_history:
  - { date: 2026-08-06, status: DEEP_ENRICHED, sprint: 5, by: "Sprint 5 deep-enrichment-builder" }
  - { date: 2026-08-14, status: DEPRECATED, sprint: 6, by: "Sprint 6 corr-010 standardisation (moved out of 07c to _deprecated/)" }
deprecation_reason: "corr-010 standardisation moved 76 detail cards out of main 07c to reduce 3805-line monolith. Main 07c now focuses on multi-regulation merged objectives; full per-card detail retained here for reference."
supersedes: null
superseded_by: "07c_Adjusted_Goals.md (no longer embeds cards; this file is the authoritative detail-card archive for Case_03)"
detail_cards_count: 76
fields_per_card: 18
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
---

# Appendix A — DEPRECATED — Privacy/Security Goal Detail Cards (76 cards)

> **DEPRECATED FILE — corr-010 (2026-08-14).** This file was extracted verbatim from `07c_Adjusted_Goals.md §2a` (38 PG detail cards) and `§3a` (38 SG detail cards) during the corr-010 standardisation commit. The main `07c_Adjusted_Goals.md` now uses a **multi-regulation merged objectives table** (§2) with no embedded detail cards; cross-regulation detail is preserved here for reference.
>
> **Why moved:** Original 07c had grown to 3805 lines (over 150 KB), exceeding the methodology's 1500-line recommendation for Phase 1 documents. Detail cards (76 × ~40 lines each = ~3000 lines) were split out so that the main 07c focuses on the **decision-relevant content**: baseline, merged objectives, tensions, track B decision trail, NIST controls mapping, cross-references, validation, and approval.
>
> **ID migration:** PG-D-/SG-D- legacy IDs were migrated to AG-D- (slot 001 for PG-origin, slot 002 for SG-origin) in the prior §2 rename commit. This file preserves the migrated AG-D- IDs as-is. See **Alias Table** (§A.3) at the end of this document for the full PG/SG → AG-D- mapping.
>
> **Card content:** Each card retains all 18 fields (Description, Scope, Out-of-Scope, Source Article, NIST CSF Anchors, Verification Criteria, Verification Method, Owner, Status, Dependencies, Risk, Stakeholders, Maturity, Implementation Priority, Regulatory Reporting, External Auditor, Supervisory Body, plus Sub-Domain-Name-in-header). Effort/Cost/Timeline remain excluded per Sprint 5 scope.

---

## §A.1 Privacy Goal Detail Cards (38 cards — slot 001, PG origin)

> Verbatim extraction from 07c §2a (lines 169-1815, original). All 38 PG cards with AG-D-XX.X-001 IDs.

## §2a Privacy Goal Detail Cards (38 cards)

> 38 detail cards — one per sub-domain. Each card provides **18 fields** including multi-paragraph Description (Context + Scope + Out-of-Scope), Source Article, NIST CSF Anchors, operational Verification Criteria, Verification Method, Owner, Status, Dependencies, Risk, Stakeholders, Maturity, Implementation Priority, Regulatory Reporting (DORA + GDPR + AI Act), External Auditor (ISO 27001 + DORA + AI Act), and Supervisory Body (ECB + BaFin + EDPB + AI Office). **NO Effort Estimate, Cost Estimate, or Target Timeline** per Sprint 5 scope (DEEP enrichment without quantitative estimates).

### AG-D-01.1-001 — Data at Rest Encryption

**Description:**

Data at Rest Encryption is the **PG goal binding** for D-01.1 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** All core banking DB2 z/OS data sets, payment systems, model store, data lake, EU cloud backups, audit log archives.

**Out of Scope:** Customer-managed CMK (overkill at MAX); legacy DES/3DES retained for backward-compat systems.

**Source Article:** GDPR Art. 5(1)(f) + Art. 32(1)(a) + CRA Annex I Part I (2)(e) + NIS 2 Art. 21(2)(h) + DORA Art. 9(2) + AI Act Art. 10

**NIST CSF Anchors:** PR.DS-01, PR.DS-10, PR.DS-01

**Verification Criteria (operational):**
- HSM audit log shows 100% key-usage events; AES-256-GCM enabled on all production volumes; FIPS 140-2 Level 3 HSM cluster annual certification; quarterly key-rotation audit by external auditor
- Doc 07b §4 row D-01.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + Head of Crypto (backup)

**Status:** TODO

**Dependencies:** D-01.2, D-01.3, D-01.4

**Risk if not met:** HIGH — financial data exposure + DORA Art. 87 violation + ECB supervisory finding

**Affected Stakeholders:** Customers (data subjects), regulators (ECB, BaFin, EDPB), CEO, CISO, DPO, CTO

**Maturity Score:** Current 2/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report (Art. 17/RTS) if breach; ECB annual ICT risk inspection; AI Act Art. 72 PMM if data affects AI model

**External Auditor:** ISO 27001 surveillance auditor (annual) + DORA Art. 27 TLPT (triennial) + AI Act Art. 43 conformity

**Supervisory Body:** ECB JST (Joint Supervisory Team) + BaFin + EDPB + AI Office

<a name="ag-D-01-1-001"></a>

### AG-D-01.2-001 — Data in Transit Encryption

**Description:**

Data in Transit Encryption is the **PG goal binding** for D-01.2 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** All ingress (CloudFront, API Gateway), egress (SEPA/SWIFT, payment networks), inter-service (mTLS, internal CA), mobile app (cert pinning).

**Out of Scope:** TLS 1.2 fallback (deprecated); self-signed cert (banned in production).

**Source Article:** GDPR Art. 5(1)(f) + Art. 32(1)(a) + CRA Annex I Part I (2)(e) + NIS 2 Art. 21(2)(h) + DORA Art. 9(2) + AI Act Art. 15

**NIST CSF Anchors:** PR.DS-02, PR.IR-01, PR.IR-04

**Verification Criteria (operational):**
- TLS 1.3 enforced across all endpoints; mTLS for service-to-service; quarterly cert rotation audit; quarterly penetration test
- Doc 07b §4 row D-01.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + Network Architect (backup)

**Status:** TODO

**Dependencies:** D-01.1, D-01.3, D-01.4

**Risk if not met:** HIGH — clear-text data exposure + PCI-DSS violation + DORA Art. 9 breach

**Affected Stakeholders:** Customers, payment networks, ECB, BaFin, CISO, Network Ops

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; PCI-DSS QSA annual report; ECB on-site inspection

**External Auditor:** ISO 27001 + DORA conformity + PCI-DSS QSA annual

**Supervisory Body:** BaFin + ECB + PCI SSC

<a name="ag-D-01-2-001"></a>

### AG-D-01.3-001 — Cryptographic Key Management

**Description:**

Cryptographic Key Management is the **PG goal binding** for D-01.3 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** HSM cluster (Thales/Utimaco), key ceremonies, KMS rotation policies, separation of duties (key custodian ≠ data owner).

**Out of Scope:** Cloud-native KMS only (must be HSM-backed for ECB supervision); shared keys across business units.

**Source Article:** CRA Annex I Part I (2)(e) + NIS 2 Art. 21(2)(h) + DORA Art. 9(2) + AI Act Art. 10

**NIST CSF Anchors:** PR.AA-03, PR.AA-04, PR.AA-05, PR.DS-01, PR.IR-03

**Verification Criteria (operational):**
- HSM key-ceremony audited annually; KMS rotation policy enforced (90d for data keys); separation-of-duties enforcement; quarterly log review
- Doc 07b §4 row D-01.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** Head of Crypto (primary) + CISO (backup)

**Status:** TODO

**Dependencies:** D-01.1, D-01.2, D-01.4

**Risk if not met:** MEDIUM — key compromise exposure + ECB finding + DORA Art. 9 violation

**Affected Stakeholders:** CISO, Head of Crypto, DPO, ECB, external auditor

**Maturity Score:** Current 2/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; ECB JST inspection; AI Act Art. 10 data governance audit

**External Auditor:** FIPS 140-2 + Common Criteria EAL4+ annual + DORA conformity

**Supervisory Body:** ECB JST + BaFin + BSI (FIPS)

<a name="ag-D-01-3-001"></a>

### AG-D-01.4-001 — Data Integrity Mechanisms

**Description:**

Data Integrity Mechanisms is the **PG goal binding** for D-01.4 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** DB constraints, application HMAC, Merkle tree integrity for transaction logs, WORM audit log storage.

**Out of Scope:** Blockchain anchoring (out of scope); TPM attestation (RIGOROUS-only).

**Source Article:** GDPR Art. 5(1)(d) + Art. 32(1)(b) + CRA Annex I Part I (2)(e) + DORA Art. 9(2) + AI Act Art. 10

**NIST CSF Anchors:** PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-01, PR.DS-10, PR.IR-03, PR.IR-04, PR.PS-04

**Verification Criteria (operational):**
- Merkle root verified daily; HMAC on compliance records quarterly test; WORM audit log integrity hash chain validated
- Doc 07b §4 row D-01.4 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + Data Engineer (backup)

**Status:** TODO

**Dependencies:** D-01.1, D-01.2, D-01.3

**Risk if not met:** MEDIUM — silent data corruption + DORA Art. 9 integrity violation

**Affected Stakeholders:** CISO, Data Engineer, DPO, internal audit, ECB

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** DORA 4h incident report; ECB annual ICT inspection; AI Act Art. 10 data integrity

**External Auditor:** ISO 27001 + DORA conformity annual

**Supervisory Body:** ECB JST + BaFin

<a name="ag-D-01-4-001"></a>

### AG-D-02.1-001 — Vulnerability Identification

**Description:**

Vulnerability Identification is the **PG goal binding** for D-02.1 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** SAST (Checkmarx), DAST (Burp Enterprise), SCA (Snyk), container (Trivy), IaC (Checkov), AI model (Adversarial Robustness Toolbox).

**Out of Scope:** DAST-only (must be combined with SAST); bug bounty only (must be combined with internal red team).

**Source Article:** CRA Annex I Part I (2)(d) + (h) + NIS 2 Art. 21(2)(e) + DORA Art. 24-27 + AI Act Art. 9

**NIST CSF Anchors:** ID.RA-01, ID.RA-03, ID.RA-05, PR.PS-02, PR.PS-06, DE.CM-09

**Verification Criteria (operational):**
- SAST blocks CI merge on High+; DAST weekly on staging; SCA on every PR; AI model adversarial sample testing quarterly
- Doc 07b §4 row D-02.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + DevSecOps Lead (backup)

**Status:** TODO

**Dependencies:** D-02.2, D-02.4, D-07.1, D-07.2

**Risk if not met:** HIGH — undetected vulnerability + DORA Art. 24-27 testing programme gap + AI Act Art. 9 risk

**Affected Stakeholders:** CISO, DevSecOps, CTO, AI Gov Lead, ECB, BaFin, ENISA

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; CRA Art. 14 24h+72h reporting; AI Act Art. 72 PMM; ECB TLPT scope

**External Auditor:** ISO 27001 + DORA TLPT + AI Act conformity annual

**Supervisory Body:** ECB JST + BaFin + ENISA + AI Office

<a name="ag-D-02-1-001"></a>

### AG-D-02.2-001 — Patch Management & Updates

**Description:**

Patch Management & Updates is the **PG goal binding** for D-02.2 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** OS patches (Amazon Linux 2/2023), container base-image rebuilds, dependency upgrades, mobile app releases.

**Out of Scope:** Zero-day emergency patches outside maintenance window (procedural exception with CISO approval).

**Source Article:** CRA Art. 13(8) 5y support + Art. 13(9) 10y update + NIS 2 Art. 21(2)(e) + DORA Art. 9(4)(f)

**NIST CSF Anchors:** ID.RA-01, PR.IR-03, PR.PS-01, PR.PS-02

**Verification Criteria (operational):**
- Critical CVE patched within 24h; High within 7d; quarterly mobile app release; 5-year support window documented
- Doc 07b §4 row D-02.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** DevSecOps Lead (primary) + CISO (backup)

**Status:** TODO

**Dependencies:** D-02.1, D-07.3, D-07.4

**Risk if not met:** HIGH — known CVE exploitation + DORA Art. 9(4)(f) violations + CRA Art. 13(8) 5y support

**Affected Stakeholders:** DevSecOps, CTO, CISO, customers, regulators

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; CRA Art. 14 24h reporting; ECB JST inspection

**External Auditor:** ISO 27001 + DORA Art. 26 TLPT + CRA internal

**Supervisory Body:** ECB JST + BaFin + ENISA

<a name="ag-D-02-2-001"></a>

### AG-D-02.3-001 — Coordinated Vulnerability Disclosure

**Description:**

Coordinated Vulnerability Disclosure is the **PG goal binding** for D-02.3 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** security.txt at /.well-known/security.txt, dedicated security@omnibank.de, CVD page, ISO 29147 process.

**Out of Scope:** Bug bounty programme (separate programme, deferred beyond Track B); financial rewards for researchers.

**Source Article:** CRA Art. 12 + NIS 2 Art. 12

**NIST CSF Anchors:** GV.PO-01, GV.SC-04, ID.RA-01, RS.CO-03

**Verification Criteria (operational):**
- security.txt valid + readable; 24h ack SLA verified; 72h triage SLA; quarterly test with external researcher
- Doc 07b §4 row D-02.3 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** CISO (primary) + DevSecOps Lead (backup)

**Status:** TODO

**Dependencies:** D-02.1, D-02.2

**Risk if not met:** MEDIUM — uncoordinated disclosure + CRA Art. 12 CVD obligation + NIS 2 Art. 12

**Affected Stakeholders:** External researchers, customers, CISO, ENISA, CSIRT

**Maturity Score:** Current 2/4 → Target 3/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** CRA Art. 14 24h reporting; NIS 2 Art. 12 coordinated disclosure

**External Auditor:** ISO 27001 A.6.8 + CRA Art. 12 + NIS 2 Art. 12

**Supervisory Body:** ENISA + BSI CSIRT + BaFin

<a name="ag-D-02-3-001"></a>

### AG-D-02.4-001 — Threat-Led Penetration Testing

**Description:**

Threat-Led Penetration Testing is the **PG goal binding** for D-02.4 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** External TLPT (BIG-4 TLPT provider), internal red team, purple team exercises, AI model adversarial testing.

**Out of Scope:** Single pentest cycle (must be combined with ISO 27001 annual + AI model adversarial).

**Source Article:** DORA Art. 26-27 + NIS 2 Art. 21(2)(e) + AI Act Art. 9 + Art. 43

**NIST CSF Anchors:** DE.CM-09, GV.OV-02, GV.SC-04, ID.RA-01, ID.RA-04, PR.PS-06

**Verification Criteria (operational):**
- TLPT cycle every 3y (annual per ECB adjustment); ECB scoping letter on file; closure report to ECB within 90d; AI model adversarial tested quarterly
- Doc 07b §4 row D-02.4 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + TLPT Programme Manager (backup)

**Status:** TODO

**Dependencies:** D-02.1, D-07.1, D-10.3

**Risk if not met:** HIGH — DORA Art. 26-27 mandate missed + ECB TLPT scoping failure + AI Act Art. 9 risk

**Affected Stakeholders:** CISO, CRO, ECB TLPT team, external TLPT provider, AI Gov Lead, board

**Maturity Score:** Current 1/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA Art. 26 TLPT cycle; ECB scoping letter; AI Act Art. 43 conformity assessment

**External Auditor:** ECB-recognised TLPT provider + ISO 27001 + AI Act conformity

**Supervisory Body:** ECB JST + BaFin + AI Office

<a name="ag-D-02-4-001"></a>

### AG-D-03.1-001 — Identity Lifecycle Management

**Description:**

Identity Lifecycle Management is the **PG goal binding** for D-03.1 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Hybrid identity (on-prem AD + Azure AD), Saviynt governance, CyberArk PAM, HR-feed joiner/mover/leaver.

**Out of Scope:** Self-hosted IdP (cloud-managed); legacy LDAP for production (decommissioned).

**Source Article:** GDPR Art. 5(1)(f) + Art. 30(1)(b) + CRA + NIS 2 Art. 21(2)(i) + DORA Art. 9 + AI Act Art. 14

**NIST CSF Anchors:** PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02

**Verification Criteria (operational):**
- Joiner/mover/leaver workflow automated via HR feed; quarterly orphan-account scan with zero stale; annual recertification
- Doc 07b §4 row D-03.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CIO (primary) + Identity Lead (backup)

**Status:** TODO

**Dependencies:** D-03.2, D-03.3, D-06.1, D-06.4

**Risk if not met:** HIGH — orphan account + DORA Art. 9 violation + ECB operational risk finding

**Affected Stakeholders:** CIO, HR, all employees, contractors, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; ISO 27001 A.5.16; ECB annual ICT inspection

**External Auditor:** ISO 27001 surveillance + DORA annual

**Supervisory Body:** ECB JST + BaFin + BfDI (Federal DPA)

<a name="ag-D-03-1-001"></a>

### AG-D-03.2-001 — Multi-Factor Authentication

**Description:**

Multi-Factor Authentication is the **PG goal binding** for D-03.2 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** YubiKey FIDO2 hardware tokens (privileged), Authenticator TOTP (standard), certificate-based auth (service).

**Out of Scope:** SMS MFA (deprecated); password-only (no MFA — violation).

**Source Article:** CRA + NIS 2 Art. 21(2)(i) + DORA Art. 9(4)(d) + AI Act Art. 14 + PSD2 SCA

**NIST CSF Anchors:** PR.AA-01, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02

**Verification Criteria (operational):**
- 100% privileged users with FIDO2 hardware tokens; quarterly MFA enforcement audit; no SMS in production
- Doc 07b §4 row D-03.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CIO (primary) + Identity Lead (backup)

**Status:** TODO

**Dependencies:** D-03.1, D-03.3

**Risk if not met:** HIGH — credential compromise + DORA Art. 9(4)(d) strong auth + PSD2 SCA

**Affected Stakeholders:** CIO, all employees, customers, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; PSD2 SCA; ECB security inspection

**External Auditor:** ISO 27001 + DORA + PSD2 QSA annual

**Supervisory Body:** ECB JST + BaFin + BSI

<a name="ag-D-03-2-001"></a>

### AG-D-03.3-001 — Authorization & Least Privilege

**Description:**

Authorization & Least Privilege is the **PG goal binding** for D-03.3 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** RBAC + ABAC engine, privileged access workstation (PAW), just-in-time (JIT) via CyberArk, zero standing privilege.

**Out of Scope:** Static admin roles (deprecated); shared service accounts.

**Source Article:** GDPR Art. 5(1)(c) + Art. 22 + NIS 2 + DORA Art. 9 + AI Act Art. 14

**NIST CSF Anchors:** PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-02, PR.PS-04

**Verification Criteria (operational):**
- Zero standing privilege verified; JIT access logs 100% reviewed; quarterly access review by manager
- Doc 07b §4 row D-03.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CIO (primary) + Identity Lead (backup)

**Status:** TODO

**Dependencies:** D-03.1, D-03.2, D-07.1

**Risk if not met:** HIGH — privilege escalation + DORA Art. 9 violation + GDPR Art. 32 breach

**Affected Stakeholders:** CIO, all employees, AI Gov Lead, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; ISO 27001 A.5.15; AI Act Art. 14 human oversight

**External Auditor:** ISO 27001 + DORA + AI Act conformity

**Supervisory Body:** ECB JST + BaFin + BfDI

<a name="ag-D-03-3-001"></a>

### AG-D-03.4-001 — Secure System Defaults

**Description:**

Secure System Defaults is the **PG goal binding** for D-03.4 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** CIS Benchmarks (Ubuntu, Windows, K8s), AWS Config + Azure Policy, automated hardening scripts.

**Out of Scope:** Bespoke hardening (use CIS as baseline); manual configuration drift.

**Source Article:** CRA + ISO 27001 A.8.9

**NIST CSF Anchors:** GV.PO-01, GV.SC-03, PR.DS-10, PR.PS-01

**Verification Criteria (operational):**
- Quarterly CIS compliance scan; deviation approval workflow documented; <5% deviation baseline
- Doc 07b §4 row D-03.4 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** DevSecOps Lead (primary) + CISO (backup)

**Status:** TODO

**Dependencies:** D-07.1, D-07.3

**Risk if not met:** MEDIUM — CIS drift + CRA compliance weakness + ISO 27001 A.8.9

**Affected Stakeholders:** DevSecOps, CISO, IT Ops, ISO 27001 auditor

**Maturity Score:** Current 2/4 → Target 3/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** ISO 27001 annual surveillance; AWS/Azure audit

**External Auditor:** ISO 27001 internal + external + CSA STAR

**Supervisory Body:** BSI + cloud provider compliance

<a name="ag-D-03-4-001"></a>

### AG-D-04.1-001 — Incident Detection & Triage

**Description:**

Incident Detection & Triage is the **PG goal binding** for D-04.1 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** 24/7 SOC (in-house tier-1/2/3 + co-managed overflow), SIEM (Splunk), SOAR (Splunk SOAR), EDR (CrowdStrike), NDR (Vectra AI), UEBA (Exabeam).

**Out of Scope:** Reactive-only (must be 24/7 with proactive threat hunting); single-vendor stack (must be defence-in-depth).

**Source Article:** CRA + NIS 2 Art. 21(2)(b) + DORA Art. 10 + AI Act Art. 73

**NIST CSF Anchors:** DE.CM-01, DE.CM-02, DE.CM-03, DE.CM-06, DE.CM-09, RS.MA-02, RS.MA-02, RS.AN-03

**Verification Criteria (operational):**
- MTTD <15 min; SOC 24/7 staffed; quarterly purple-team exercise; monthly detection-coverage gap analysis
- KPI: MTTD <15min measured monthly; alert response time P95 <5min for critical alerts; SOC 24/7 staffing validated per shift roster (per Doc 04 §10 BG-005 readiness)
- Doc 07b §4 row D-04.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + SOC Director (backup)

**Status:** TODO

**Dependencies:** D-04.2, D-04.3, D-10.1, D-10.2

**Risk if not met:** HIGH — undetected incident + DORA Art. 10 violation + AI Act Art. 73 reporting

**Affected Stakeholders:** CISO, SOC, customers, ECB, BaFin, AI Gov Lead

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; AI Act Art. 73 15d/2d/10d reporting

**External Auditor:** ISO 27001 surveillance + DORA TLPT + AI Act conformity

**Supervisory Body:** ECB JST + BaFin + AI Office

<a name="ag-D-04-1-001"></a>

### AG-D-04.2-001 — Containment & Mitigation

**Description:**

Containment & Mitigation is the **PG goal binding** for D-04.2 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Dedicated IR team, SOAR playbooks (15+), forensic toolkit (EnCase), tabletop exercises quarterly.

**Out of Scope:** Ad-hoc containment (must be playbook-driven); single-team (must be cross-functional).

**Source Article:** GDPR Art. 32 + CRA + NIS 2 Art. 21(2)(c) + DORA Art. 17 + AI Act Art. 73

**NIST CSF Anchors:** RS.MA-02, RS.MA-02, RS.MI-01, RS.MI-02, ID.RA-06

**Verification Criteria (operational):**
- MTTC <4h for critical; monthly playbook drill; annual red team; SOAR MTTR <30min
- Doc 07b §4 row D-04.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + IR Lead (backup)

**Status:** TODO

**Dependencies:** D-04.1, D-04.3, D-04.4

**Risk if not met:** HIGH — uncontained incident + DORA Art. 17 violation + ECB finding

**Affected Stakeholders:** CISO, IR team, Legal, DPO, CRO, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; AI Act Art. 72 PMM; ECB on-site inspection

**External Auditor:** ISO 27001 + DORA + AI Act + ENISA CSIRT Network

**Supervisory Body:** ECB JST + BaFin + ENISA + AI Office

<a name="ag-D-04-2-001"></a>

### AG-D-04.3-001 — Regulatory Notification

**Description:**

Regulatory Notification is the **PG goal binding** for D-04.3 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** 5-regulation max-SLA routing pipeline — DORA 4h + NIS 2 24h + CRA 24h + GDPR 72h + AI Act 15d/2d/10d.

**Out of Scope:** Single-reg workflow (forces duplicate work); manual routing (must be SOAR-automated).

**Source Article:** DORA Art. 17-19 + RTS Art. 6 + NIS 2 Art. 23(4) + CRA Art. 14 + GDPR Art. 33 + AI Act Art. 73

**NIST CSF Anchors:** RS.CO-02, RS.MA-01, RS.MA-03, ID.RA-06

**Verification Criteria (operational):**
- Tabletop exercises quarterly; per-recipient template segregation; per-recipient channel gating; single clock-start discipline; MTTC <4h for DORA-critical
- Doc 07b §4 row D-04.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CEO (accountable) + CISO (responsible) + DPO + CRO + Legal

**Status:** TODO

**Dependencies:** D-04.1, D-04.2, D-09.1, D-09.4

**Risk if not met:** HIGH — 5 fine regimes possible + ECB + BaFin + EDPB + ENISA + AI Office + DPA scrutiny

**Affected Stakeholders:** Customers, CEO, board, CISO, DPO, CRO, Legal, ECB, BaFin, EDPB, ENISA, AI Office, DPA

**Maturity Score:** Current 2/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h (RTS Art. 6) + NIS 2 24h + CRA 24h + GDPR 72h + AI Act 15d/2d/10d — all 5 regulations simultaneously

**External Auditor:** Joint ECB/BaFin supervised drill (annual) + ISO 27001 + DORA + ENISA exercise

**Supervisory Body:** ECB JST + BaFin + EDPB + national DPA + ENISA + BSI CSIRT + AI Office

<a name="ag-D-04-3-001"></a>

### AG-D-04.4-001 — Data Restoration & Recovery

**Description:**

Data Restoration & Recovery is the **PG goal binding** for D-04.4 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** 2 active data centres + 1 cold standby, RTO 4h / RPO 15min for critical systems, quarterly DR test, annual full failover.

**Out of Scope:** Single-site (rejected); recovery-only (must include prevention and detection).

**Source Article:** NIS 2 Art. 21(2)(c) + DORA Art. 11-12

**NIST CSF Anchors:** PR.IR-01, PR.IR-02, PR.IR-03, PR.IR-04, RC.RP-01, RC.RP-02, RC.RP-03, RC.RP-05

**Verification Criteria (operational):**
- RTO 4h verified quarterly; RPO 15min verified; annual full failover test; cyber recovery test annually
- KPI: Quarterly DR test verifies RTO ≤24h (target ≤4h) and RPO ≤1h (target 15min) — measured in disaster simulation report (per BG-005 99.99% uptime SLA for core banking)
- Doc 07b §4 row D-04.4 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CTO (primary) + DR Manager (backup)

**Status:** TODO

**Dependencies:** D-04.1, D-04.2, D-09.3

**Risk if not met:** HIGH — extended outage + DORA Art. 12 BC violation + 99.99% SLA breach

**Affected Stakeholders:** CTO, DR Manager, customers, regulators, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; 99.99% SLA per BG-005; ECB annual inspection

**External Auditor:** ISO 27001 A.5.30 + DORA Art. 12 + cyber recovery test

**Supervisory Body:** ECB JST + BaFin

<a name="ag-D-04-4-001"></a>

### AG-D-05.1-001 — Data Minimisation

**Description:**

Data Minimisation is the **PG goal binding** for D-05.1 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Field-level enforcement in DB schema, automated data-classification scanner, consent management (OneTrust).

**Out of Scope:** Manual minimisation (must be automated); unlimited collection (must be bounded).

**Source Article:** GDPR Art. 5(1)(c) + CRA + AI Act Art. 10

**NIST CSF Anchors:** ID.AM-01, ID.AM-02, PR.DS-01

**Verification Criteria (operational):**
- Quarterly data minimisation audit; field-level enforcement validated annually; consent management audit-trail
- Doc 07b §4 row D-05.1 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** DPO (primary) + Data Engineer (backup)

**Status:** TODO

**Dependencies:** D-05.2, D-05.3, D-09.3

**Risk if not met:** MEDIUM — over-collection + GDPR Art. 5(1)(c) violation + AI Act Art. 10 data quality

**Affected Stakeholders:** DPO, Data Engineer, customers, EDPB, DPA

**Maturity Score:** Current 2/4 → Target 3/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** GDPR periodic audit; AI Act Art. 10 data governance

**External Auditor:** ISO 27701 + AI Act conformity

**Supervisory Body:** BfDI (Federal DPA) + EDPB + AI Office

<a name="ag-D-05-1-001"></a>

### AG-D-05.2-001 — Retention & Archiving

**Description:**

Retention & Archiving is the **PG goal binding** for D-05.2 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Retention policy (5-10y BaFin/ECB for financial transactions + 7y audit logs), archive tooling (Hadoop cold), automated deletion.

**Out of Scope:** Indefinite retention (prohibited); manual deletion (must be automated).

**Source Article:** GDPR Art. 5(1)(e) + AI Act Art. 10 + BaFin/ECB requirements

**NIST CSF Anchors:** PR.PS-02, PR.DS-01, ID.AM-01

**Verification Criteria (operational):**
- Quarterly deletion validation; 5-year + 7-year retention verified; BaFin retention rules applied
- Doc 07b §4 row D-05.2 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** DPO (primary) + Records Manager (backup)

**Status:** TODO

**Dependencies:** D-05.1, D-05.3, D-09.4

**Risk if not met:** MEDIUM — over-retention + GDPR Art. 5(1)(e) + BaFin retention non-compliance

**Affected Stakeholders:** DPO, Records Manager, customers, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** GDPR periodic audit; BaFin/ECB retention requirements; AI Act Art. 10

**External Auditor:** ISO 27001 A.5.34 + DORA Art. 11 + ECB retention

**Supervisory Body:** ECB JST + BaFin + BfDI

<a name="ag-D-05-2-001"></a>

### AG-D-05.3-001 — Right to Erasure

**Description:**

Right to Erasure is the **PG goal binding** for D-05.3 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Erasure API endpoint, cryptographic sharding (destroy identity, retain anonymised log per T-002), DSAR workflow (30-day SLA).

**Out of Scope:** Hard-delete (collides with DORA Art. 12 immutable logs — T-002); manual erasure (must be tokenised).

**Source Article:** GDPR Art. 17 + CRA Art. 13 + DORA Art. 11-12 (T-002)

**NIST CSF Anchors:** PR.PS-02, PR.DS-01, PR.DS-10

**Verification Criteria (operational):**
- DSAR 30-day SLA verified; cryptographic sharding quarterly test; anonymised log integrity preserved
- Doc 07b §4 row D-05.3 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** DPO (primary) + Data Engineer (backup)

**Status:** TODO

**Dependencies:** D-05.1, D-05.2, D-10.2

**Risk if not met:** HIGH — data subject rights violation + GDPR Art. 17 fine + DORA Art. 11-19 conflict

**Affected Stakeholders:** DPO, customers, EDPB, BfDI, CRO, ECB

**Maturity Score:** Current 2/4 → Target 4/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** GDPR Art. 17 30-day SLA; CRA Art. 13; DORA Art. 11-19 (T-002 RESOLVED)

**External Auditor:** ISO 27001 + DORA Art. 12 + external auditor cryptographic sharding review

**Supervisory Body:** BfDI + EDPB + ECB JST + BaFin

<a name="ag-D-05-3-001"></a>

### AG-D-05.4-001 — Data Portability

**Description:**

Data Portability is the **PG goal binding** for D-05.4 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** JSON export endpoint (machine-readable), 30-day SLA, GDPR Art. 20 right to data portability.

**Out of Scope:** PDF-only (must be machine-readable); manual export (must be API-driven).

**Source Article:** GDPR Art. 20

**NIST CSF Anchors:** PR.DS-10, PR.PS-02

**Verification Criteria (operational):**
- JSON export endpoint tested; 30-day SLA verified; CSV format supported
- Doc 07b §4 row D-05.4 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** DPO (primary) + Data Engineer (backup)

**Status:** TODO

**Dependencies:** D-05.1, D-05.2

**Risk if not met:** MEDIUM — GDPR Art. 20 violation + customer rights denial

**Affected Stakeholders:** DPO, customers, BfDI

**Maturity Score:** Current 2/4 → Target 3/4

**Implementation Priority:** MEDIUM

**Regulatory Reporting:** GDPR Art. 20 30-day SLA

**External Auditor:** ISO 27001 + GDPR audit

**Supervisory Body:** BfDI

<a name="ag-D-05-4-001"></a>

### AG-D-06.1-001 — Vendor Risk Assessment

**Description:**

Vendor Risk Assessment is the **PG goal binding** for D-06.1 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Own vendor risk programme, DORA Art. 28 pre-contractual assessment, Art. 30 CTPP register, annual + critical-vendor quarterly review.

**Out of Scope:** Lightweight questionnaire (must be DORA-grade); ad-hoc assessment (must be annual).

**Source Article:** NIS 2 + DORA Art. 28 + GDPR + CRA

**NIST CSF Anchors:** GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, GV.SC-03, UNMAPPED_CSF, PR.DS-01

**Verification Criteria (operational):**
- Critical vendor quarterly review; DORA Art. 30 CTPP register maintained; annual vendor review 100% completion
- Doc 07b §4 row D-06.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CRO (primary) + Procurement (backup)

**Status:** TODO

**Dependencies:** D-06.2, D-06.3, D-06.4, D-09.3

**Risk if not met:** HIGH — critical ICT vendor failure + DORA Art. 28 violation + ECB finding

**Affected Stakeholders:** CRO, Procurement, CISO, Legal, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 30 CTPP register; ECB annual inspection

**External Auditor:** ISO 27001 + DORA Art. 30 + ECB JST inspection

**Supervisory Body:** ECB JST + BaFin + ESAs Joint Committee (if CTPP)

<a name="ag-D-06-1-001"></a>

### AG-D-06.2-001 — Software Bill of Materials (SBOM)

**Description:**

Software Bill of Materials (SBOM) is the **PG goal binding** for D-06.2 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** CycloneDX SBOM in CI/CD per release, CRA Art. 13(13) 10-year documentation, machine-readable formats (SPDX + CycloneDX).

**Out of Scope:** Per-quarter SBOM (must be per-release); proprietary format (must be machine-readable).

**Source Article:** CRA Annex I Part II + Art. 13(13)

**NIST CSF Anchors:** ID.AM-08, PR.DS-01, PR.PS-02

**Verification Criteria (operational):**
- Per-release SBOM <2hr generation; 10-year retention; SPDX + CycloneDX supported
- Doc 07b §4 row D-06.2 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** DevSecOps Lead (primary) + CISO (backup)

**Status:** TODO

**Dependencies:** D-02.1, D-07.3

**Risk if not met:** MEDIUM — unknown dependency + CRA Art. 13(13) violation + DORA Art. 8 inventory gap

**Affected Stakeholders:** DevSecOps, CISO, CTO, customers, ENISA

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** CRA Art. 13(13) 10y retention; NIS 2 supply chain transparency

**External Auditor:** ISO 27001 + CRA conformity + ENISA supply chain

**Supervisory Body:** ENISA + BaFin (if material)

<a name="ag-D-06-2-001"></a>

### AG-D-06.3-001 — Contractual Security Obligations

**Description:**

Contractual Security Obligations is the **PG goal binding** for D-06.3 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** DPA + DORA Art. 30 CTPP clauses + NIS 2 supply chain + AI Act Art. 25 downstream, Legal review workflow.

**Out of Scope:** Standard MSA (must be DORA-grade); ad-hoc clauses (must be clause-bank).

**Source Article:** GDPR + NIS 2 + DORA Art. 30 + AI Act Art. 25

**NIST CSF Anchors:** GV.SC-01, GV.SC-02, GV.SC-04, GV.SC-05, PR.DS-01

**Verification Criteria (operational):**
- 100% critical vendor contracts with CTPP clauses; AI Act downstream provider clauses; annual contract review
- Doc 07b §4 row D-06.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** Legal (primary) + CRO + CISO (review)

**Status:** TODO

**Dependencies:** D-06.1, D-06.4

**Risk if not met:** HIGH — CTPP contractual gap + DORA Art. 30 violation + AI Act Art. 25 gap

**Affected Stakeholders:** Legal, CRO, CISO, Procurement, ECB, BaFin, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA Art. 30; AI Act Art. 25; GDPR DPA; ECB JST inspection

**External Auditor:** ISO 27001 + DORA Art. 30 + AI Act conformity

**Supervisory Body:** ECB JST + BaFin + BfDI + AI Office

<a name="ag-D-06-3-001"></a>

### AG-D-06.4-001 — Third-Party Boundary Management

**Description:**

Third-Party Boundary Management is the **PG goal binding** for D-06.4 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Boundary management (API gateway + dedicated circuits to AWS/Azure/payment networks/credit bureaus), supplier incident playbook, DORA Art. 28 exit strategy.

**Out of Scope:** Implicit boundary (must be explicit); no exit strategy (DORA Art. 28 requires).

**Source Article:** NIS 2 + DORA Art. 28

**NIST CSF Anchors:** PR.DS-01, PR.PS-04, GV.SC-04

**Verification Criteria (operational):**
- API gateway enforces schema validation + rate limiting; exit strategy tested annually; supplier incident playbook
- Doc 07b §4 row D-06.4 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + Cloud Architect (backup)

**Status:** TODO

**Dependencies:** D-06.1, D-06.3, D-09.3

**Risk if not met:** HIGH — boundary breach + DORA Art. 28 exit strategy gap + ECB finding

**Affected Stakeholders:** CISO, Cloud Architect, CRO, ECB, BaFin, vendor

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 28 exit strategy; ECB annual inspection

**External Auditor:** ISO 27001 + DORA Art. 28 + ECB JST

**Supervisory Body:** ECB JST + BaFin + ESAs Joint Committee (if CTPP)

<a name="ag-D-06-4-001"></a>

### AG-D-07.1-001 — Secure-by-Design Principles

**Description:**

Secure-by-Design Principles is the **PG goal binding** for D-07.1 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** NIST SSDF SP 800-218 + OWASP SAMM Level 3 + STRIDE threat modelling + architecture review board.

**Out of Scope:** Ad-hoc design (must be STRIDE-driven); single-source-of-truth (must be review-board).

**Source Article:** CRA Art. 13(1) + NIS 2 Art. 21 + DORA Art. 10 + GDPR Art. 25 + AI Act Art. 9

**NIST CSF Anchors:** PR.PS-01, PR.PS-02, PR.PS-06, , ID.RA-04, GV.SC-04

**Verification Criteria (operational):**
- Architecture review board mandatory for all new systems; STRIDE applied; SAMM Level 3 verified
- KPI: Monthly bias audit on OmniScore AI Platform; bias metrics must remain <1% across all protected characteristics (per AI Act Art. 10 data quality governance + BG-008 AI bias <1% target)
- Doc 07b §4 row D-07.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CTO (primary) + Security Architect (backup)

**Status:** TODO

**Dependencies:** D-07.2, D-07.3, D-07.4, D-09.1

**Risk if not met:** HIGH — design weakness + CRA Art. 13(1) violation + AI Act Art. 9 risk + DORA Art. 10

**Affected Stakeholders:** CTO, AI Gov Lead, DPO, CISO, ECB, BaFin, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; AI Act Art. 9 risk management; CRA Art. 13(1); ECB annual inspection

**External Auditor:** ISO 27001 + DORA + AI Act conformity + CRA

**Supervisory Body:** ECB JST + BaFin + AI Office + ENISA

<a name="ag-D-07-1-001"></a>

### AG-D-07.2-001 — Secure Coding Practices

**Description:**

Secure Coding Practices is the **PG goal binding** for D-07.2 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** SAST (Checkmarx) blocking CI merge, DAST (Burp Enterprise), secret scanning (GitGuardian), AI code review (Copilot + custom), secure coding standards (CERT + OWASP).

**Out of Scope:** Periodic scans (must be CI gates); standards-only (must be automated).

**Source Article:** CRA + NIS 2 + DORA + AI Act

**NIST CSF Anchors:** PR.PS-02, PR.PS-03, PR.PS-06, ID.RA-01, DE.CM-09

**Verification Criteria (operational):**
- SAST >High blocks merge; annual secure coding training; secret scanning zero plaintext in repos
- Doc 07b §4 row D-07.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** Lead Dev (primary) + CISO (backup)

**Status:** TODO

**Dependencies:** D-07.1, D-07.3, D-09.2

**Risk if not met:** HIGH — vulnerability injection + CRA + DORA + AI Act compliance gap

**Affected Stakeholders:** Lead Dev, CISO, CTO, customers

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; CRA Art. 13; AI Act Art. 9

**External Auditor:** ISO 27001 + DORA + CRA conformity

**Supervisory Body:** ECB JST + BaFin + ENISA

<a name="ag-D-07-2-001"></a>

### AG-D-07.3-001 — CI/CD Pipeline Security

**Description:**

CI/CD Pipeline Security is the **PG goal binding** for D-07.3 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Hardened CI/CD (GitLab + ArgoCD), signed artefacts (Cosign), SBOM attestation, SLSA Level 3, pipeline-as-code, ephemeral runners.

**Out of Scope:** Manual release (must be automated); unprotected pipeline (must be signed).

**Source Article:** NIS 2 + DORA Art. 10 + CRA Art. 13(5)

**NIST CSF Anchors:** PR.PS-01, PR.PS-02, PR.PS-06, PR.DS-01, UNMAPPED_CSF

**Verification Criteria (operational):**
- SLSA Level 3 maintained; image signing mandatory; ephemeral runners; pipeline-as-code reviewed
- Doc 07b §4 row D-07.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** DevSecOps Lead (primary) + CTO (backup)

**Status:** TODO

**Dependencies:** D-07.1, D-07.2, D-07.4

**Risk if not met:** HIGH — supply chain attack + CRA + DORA Art. 10 violation

**Affected Stakeholders:** DevSecOps, CTO, CISO, customers, ECB

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; CRA Art. 13(5); ENISA supply chain

**External Auditor:** ISO 27001 + DORA + SLSA + CRA

**Supervisory Body:** ECB JST + BaFin + ENISA

<a name="ag-D-07-3-001"></a>

### AG-D-07.4-001 — Change Management

**Description:**

Change Management is the **PG goal binding** for D-07.4 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** ServiceNow change management, 4-eyes principle, CAB review for critical changes, emergency change procedure, DORA Art. 10 ICT change management.

**Out of Scope:** Ad-hoc change (must be ServiceNow-tracked); no emergency procedure (must have documented).

**Source Article:** NIS 2 + DORA Art. 10

**NIST CSF Anchors:** PR.PS-01, PR.PS-01, PR.DS-01, PR.PS-01

**Verification Criteria (operational):**
- 100% prod changes via ServiceNow; 4-eyes verification; emergency procedure with retrospective CAB
- Doc 07b §4 row D-07.4 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CTO (primary) + Change Manager (backup)

**Status:** TODO

**Dependencies:** D-07.1, D-07.3, D-09.4

**Risk if not met:** HIGH — uncontrolled change + DORA Art. 10 violation + ECB finding

**Affected Stakeholders:** CTO, Change Manager, CRO, CISO, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 10; ECB annual inspection

**External Auditor:** ISO 27001 + DORA Art. 10 + ITIL-aligned

**Supervisory Body:** ECB JST + BaFin

<a name="ag-D-07-4-001"></a>

### AG-D-08.1-001 — General Security Awareness

**Description:**

General Security Awareness is the **PG goal binding** for D-08.1 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Monthly phishing simulation, quarterly awareness training, annual certification, role-based content, ISO 27001 A.7.2.2.

**Out of Scope:** Annual-only (must be monthly); uniform training (must be role-based).

**Source Article:** NIS 2 + DORA + GDPR

**NIST CSF Anchors:** PR.AT-01, PR.AT-02, PR.AT-01, PR.AT-02, PR.AT-02

**Verification Criteria (operational):**
- Phishing click rate <5%; annual certification 100% completion; quarterly awareness training
- Doc 07b §4 row D-08.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + HR (backup)

**Status:** TODO

**Dependencies:** D-08.2, D-08.3

**Risk if not met:** MEDIUM — human factor + DORA Art. 9 violation + ISO 27001 A.7.2.2

**Affected Stakeholders:** All employees, CISO, HR, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** DORA 4h incident report; ISO 27001 A.7.2.2; ECB annual inspection

**External Auditor:** ISO 27001 surveillance + DORA

**Supervisory Body:** ECB JST + BaFin

<a name="ag-D-08-1-001"></a>

### AG-D-08.2-001 — Role-Specific Competence

**Description:**

Role-Specific Competence is the **PG goal binding** for D-08.2 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Role-based training paths — developers (Secure Code Warrior), SOC (SANS), DPO (IAPP), AI engineers (AI Act + ISO 42001), annual certification.

**Out of Scope:** Single curriculum (must be role-based); no AI training (must include AI Act).

**Source Article:** GDPR + NIS 2 + DORA + AI Act

**NIST CSF Anchors:** PR.AT-01, PR.AT-02, PR.AT-01, PR.AT-02, PR.AT-02

**Verification Criteria (operational):**
- AI engineers AI Act Annex III training mandatory; DPO CIPP/E; SOC SANS; annual recertification
- Doc 07b §4 row D-08.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + HR + AI Gov Lead (backup)

**Status:** TODO

**Dependencies:** D-08.1, D-08.3

**Risk if not met:** MEDIUM — competency gap + DORA + AI Act + GDPR

**Affected Stakeholders:** All employees, CISO, HR, AI Gov Lead, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** GDPR + NIS 2 + DORA + AI Act

**External Auditor:** ISO 27001 + DORA + AI Act conformity

**Supervisory Body:** ECB JST + BaFin + EDPB + AI Office

<a name="ag-D-08-2-001"></a>

### AG-D-08.3-001 — Management Board Training

**Description:**

Management Board Training is the **PG goal binding** for D-08.3 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Management board briefing programme — annual cybersecurity, NIS 2 Art. 21 management liability, DORA Art. 5 management accountability, AI Act Art. 14 human oversight.

**Out of Scope:** CISO-only briefing (must include board); one-time (must be annual).

**Source Article:** NIS 2 Art. 21 + DORA Art. 5(2) + AI Act Art. 14

**NIST CSF Anchors:** GV.OC-01, GV.OC-02, GV.OC-04, GV.OC-05, ID.RA-04

**Verification Criteria (operational):**
- Annual board briefing documented in minutes; personal liability acknowledged in writing; ECB inspection-ready
- Doc 07b §4 row D-08.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CEO (primary) + Board Secretary (backup)

**Status:** TODO

**Dependencies:** D-08.1, D-08.2, D-09.1

**Risk if not met:** HIGH — management liability + NIS 2 Art. 21 + DORA Art. 5(2) + AI Act Art. 14

**Affected Stakeholders:** Board, CEO, shareholders, ECB, BaFin, EDPB

**Maturity Score:** Current 2/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** NIS 2 Art. 21 management liability + DORA Art. 5(2) + AI Act Art. 14

**External Auditor:** ISO 27001 A.5.2 + DORA Art. 5 + ECB JST inspection

**Supervisory Body:** ECB JST + BaFin + BfDI + AI Office

<a name="ag-D-08-3-001"></a>

### AG-D-09.1-001 — Information Security Policies

**Description:**

Information Security Policies is the **PG goal binding** for D-09.1 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Full ISMS (ISO 27001 certified) + DORA Art. 5 ICT risk management framework + AI Act Art. 9 risk management system + 5-policy architecture (DPO / mgmt body / manufacturer / DORA / AI Gov) with 5 distinct governance bodies.

**Out of Scope:** Single policy (must be 5-architecture); sub-domain coverage (must be ISMS-wide).

**Source Article:** GDPR + CRA + NIS 2 + DORA Art. 5 + AI Act Art. 9

**NIST CSF Anchors:** GV.OC-01, GV.OC-02, GV.PO-01, GV.PO-02, GV.RM-01, GV.RM-04

**Verification Criteria (operational):**
- ISMS surveillance audit annual; 5-policy architecture documented; DORA Art. 5 framework documented; AI Act Art. 9 risk system
- Doc 07b §4 row D-09.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + CRO + DPO + AI Gov Lead (5-policy architecture)

**Status:** TODO

**Dependencies:** D-09.2, D-09.3, D-09.4, D-08.3

**Risk if not met:** HIGH — policy fragmentation + DORA Art. 5 + AI Act Art. 9 + ECB finding

**Affected Stakeholders:** All staff, board, CEO, CISO, CRO, DPO, AI Gov Lead, ECB, BaFin, EDPB, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 5; AI Act Art. 9; GDPR DPA; ISO 27001 annual

**External Auditor:** ISO 27001 surveillance + DORA Art. 26 + AI Act conformity + ECB JST

**Supervisory Body:** ECB JST + BaFin + BfDI + EDPB + AI Office + ENISA

<a name="ag-D-09-1-001"></a>

### AG-D-09.2-001 — Impact & Risk Assessments

**Description:**

Impact & Risk Assessments is the **PG goal binding** for D-09.2 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** IPSARA Unified Assessment Framework (T-003 RESOLVED) — DPIA (GDPR Art. 35) + FRIA (AI Act Art. 27) + ICT risk (DORA Art. 6) + CRA + NIS 2.

**Out of Scope:** Single-purpose (must be unified); ad-hoc (must be annual).

**Source Article:** GDPR Art. 35 + AI Act Art. 27 + DORA Art. 6 + CRA + NIS 2 Art. 21(2)(d)

**NIST CSF Anchors:** ID.RA-01, ID.RA-04, ID.RA-05, GV.RM-01, GV.RM-04

**Verification Criteria (operational):**
- IPSARA annual review; per-regulation output generated; 5-framework discharges; ECB + AI Act + GDPR inspection-ready
- KPI: Annual DPIA + FRIA review cycle; quantified risk reduction targets per GDPR Art. 35(7) and AI Act Art. 27(4) — IPSARA unified discharge of 5 obligations (DPIA + FRIA + DORA ICT risk + CRA RA + NIS 2)
- Doc 07b §4 row D-09.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CRO (primary) + DPO + AI Gov Lead (5-assessment integration)

**Status:** TODO

**Dependencies:** D-09.1, D-09.3, D-09.4, D-07.1

**Risk if not met:** HIGH — assessment fragmentation + 5-assessment obligation + ECB + AI Act + GDPR fines

**Affected Stakeholders:** Customers, DPO, CRO, AI Gov Lead, ECB, BaFin, EDPB, AI Office

**Maturity Score:** Current 2/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** GDPR Art. 35 DPIA + AI Act Art. 27 FRIA + DORA Art. 6 ICT risk + CRA + NIS 2 risk analysis

**External Auditor:** ISO 27001 + DORA + AI Act conformity + ECB JST

**Supervisory Body:** ECB JST + BaFin + EDPB + BfDI + AI Office

<a name="ag-D-09-2-001"></a>

### AG-D-09.3-001 — Asset Inventories

**Description:**

Asset Inventories is the **PG goal binding** for D-09.3 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** ServiceNow CMDB + dedicated DORA Art. 8 ICT systems inventory + automated discovery (Qualys + Azure Arc) + quarterly reconciliation.

**Out of Scope:** Manual inventory (must be automated); ad-hoc reconciliation (must be quarterly).

**Source Article:** DORA Art. 8 + NIS 2 + CRA Annex VII

**NIST CSF Anchors:** ID.AM-01, ID.AM-02, ID.AM-03, ID.AM-04, ID.AM-08, PR.PS-02

**Verification Criteria (operational):**
- Critical ICT assets identified per DORA; annual full reconciliation; <2% drift between CMDB and Qualys
- Doc 07b §4 row D-09.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + IT Ops + DevSecOps (backup)

**Status:** TODO

**Dependencies:** D-09.1, D-09.4, D-06.1

**Risk if not met:** HIGH — unknown asset + DORA Art. 8 violation + ECB finding

**Affected Stakeholders:** CISO, IT Ops, DevSecOps, CRO, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 8; ECB annual inspection

**External Auditor:** ISO 27001 + DORA Art. 8 + ECB JST

**Supervisory Body:** ECB JST + BaFin + ENISA

<a name="ag-D-09-3-001"></a>

### AG-D-09.4-001 — Records of Processing

**Description:**

Records of Processing is the **PG goal binding** for D-09.4 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Own RoPA (GDPR Art. 30) + DORA Art. 17-19 ICT incident records + AI Act Art. 12 technical documentation + CRA Art. 13 technical documentation.

**Out of Scope:** Single-record (must be 5-architecture); ad-hoc (must be RoPA).

**Source Article:** GDPR Art. 30 + DORA Art. 17-19 + AI Act Art. 12 + CRA Art. 13

**NIST CSF Anchors:** ID.AM-01, PR.PS-01, PR.PS-02, GV.OC-04

**Verification Criteria (operational):**
- 5y retention (DORA) + 10y (AI Act) + GDPR RoPA; ECB + AI Office + EDPB inspection-ready
- Doc 07b §4 row D-09.4 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** DPO (primary) + CRO + AI Gov Lead (5-record integration)

**Status:** TODO

**Dependencies:** D-09.1, D-09.2, D-09.3

**Risk if not met:** HIGH — record fragmentation + GDPR Art. 30 + DORA Art. 17-19 + AI Act Art. 12

**Affected Stakeholders:** DPO, CRO, AI Gov Lead, customers, ECB, BaFin, EDPB, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** GDPR Art. 30 RoPA + DORA Art. 17-19 records + AI Act Art. 12 docs + CRA Art. 13 docs

**External Auditor:** ISO 27001 + DORA + AI Act conformity + GDPR

**Supervisory Body:** ECB JST + BaFin + EDPB + BfDI + AI Office

<a name="ag-D-09-4-001"></a>

### AG-D-10.1-001 — Continuous Security Monitoring

**Description:**

Continuous Security Monitoring is the **PG goal binding** for D-10.1 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** 24/7 SOC + SIEM (Splunk Enterprise) + ISO 27001 A.8.16 monitoring + DORA Art. 13 ICT monitoring + AI Act post-market monitoring (Art. 72).

**Out of Scope:** Business-hours only (must be 24/7); single platform (must be layered).

**Source Article:** CRA + NIS 2 + DORA Art. 13 + AI Act Art. 72

**NIST CSF Anchors:** DE.CM-01, DE.CM-02, DE.CM-03, DE.CM-06, DE.CM-09, ID.AM-03

**Verification Criteria (operational):**
- SIEM 1y hot + 7y cold; AI model monitoring integrated; 24/7 SOC staffed; MTTD <15min
- KPI: 24/7 SOC staffing validated quarterly (4 shifts × 6 + 1 on-call); alert response time P95 <5min for critical alerts measured monthly; AI model drift detection latency <1h
- Doc 07b §4 row D-10.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + SOC Director (backup)

**Status:** TODO

**Dependencies:** D-04.1, D-10.2, D-10.3

**Risk if not met:** HIGH — undetected incident + DORA Art. 13 violation + AI Act Art. 72 PMM

**Affected Stakeholders:** CISO, SOC, customers, ECB, BaFin, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; AI Act Art. 72 PMM; ECB annual inspection

**External Auditor:** ISO 27001 + DORA + AI Act conformity

**Supervisory Body:** ECB JST + BaFin + AI Office

<a name="ag-D-10-1-001"></a>

### AG-D-10.2-001 — Audit Logging & Traceability

**Description:**

Audit Logging & Traceability is the **PG goal binding** for D-10.2 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Tamper-evident audit logs (WORM) + cryptographic hash chains + DORA Art. 12 ICT change records + 5-10y retention (BaFin/ECB) + GDPR Art. 30 RoPA traceability + AI Act Art. 12 technical documentation.

**Out of Scope:** Mutable logs (must be WORM); plaintext (must be hash-chained).

**Source Article:** DORA Art. 12 + GDPR Art. 30 + AI Act Art. 12 + CRA

**NIST CSF Anchors:** PR.PS-04, PR.IR-01, PR.IR-03, PR.DS-10, DE.AE-03

**Verification Criteria (operational):**
- 7y retention audit logs; cryptographic sharding (T-002); hash chain integrity verified; ECB + AI Office inspection-ready
- Doc 07b §4 row D-10.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + Data Engineer (backup)

**Status:** TODO

**Dependencies:** D-04.3, D-09.4, D-05.3

**Risk if not met:** HIGH — T-002 conflict + DORA Art. 12 + GDPR Art. 30 + AI Act Art. 12

**Affected Stakeholders:** CISO, DPO, CRO, AI Gov Lead, ECB, BaFin, EDPB, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 12; GDPR Art. 30; AI Act Art. 12; ECB annual inspection

**External Auditor:** ISO 27001 + DORA + AI Act + GDPR

**Supervisory Body:** ECB JST + BaFin + EDPB + BfDI + AI Office

<a name="ag-D-10-2-001"></a>

### AG-D-10.3-001 — Compliance Testing

**Description:**

Compliance Testing is the **PG goal binding** for D-10.3 and derives from the GDPR Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this PG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** DORA Art. 24-27 testing programme (TLPT + scenario + performance + security) + AI Act Art. 43 conformity assessment + ISO 27001 surveillance + GDPR DPIA review + CRA self-declaration.

**Out of Scope:** Single test (must be 5-parallel); periodic (must be annual TLPT).

**Source Article:** DORA Art. 24-27 + AI Act Art. 43 + ISO 27001 + GDPR + CRA

**NIST CSF Anchors:** ID.RA-04, UNMAPPED_CSF, PR.PS-06, DE.CM-09

**Verification Criteria (operational):**
- Annual TLPT (ECB frequency adjustment); AI Act Art. 43 conformity before market placement; ISO 27001 surveillance; GDPR DPIA review
- KPI: Quarterly compliance review covering all 5 regulations (GDPR + CRA + NIS 2 + DORA + AI Act); documented in compliance dashboard with closure rate per BG-007 (ISO 27001 + DORA unified ISMS)
- Doc 07b §4 row D-10.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + CRO + AI Gov Lead (backup)

**Status:** TODO

**Dependencies:** D-02.1, D-02.4, D-09.1, D-09.2

**Risk if not met:** HIGH — missed testing obligation + DORA Art. 24-27 + AI Act Art. 43

**Affected Stakeholders:** CISO, CRO, AI Gov Lead, ECB, BaFin, ENISA, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 26 TLPT; AI Act Art. 43; ISO 27001; GDPR DPIA

**External Auditor:** ECB-recognised TLPT provider + ISO 27001 + AI Act conformity + CRA

**Supervisory Body:** ECB JST + BaFin + AI Office + ENISA

<a name="ag-D-10-3-001"></a>


---


---

## §A.2 Security Goal Detail Cards (38 cards — slot 002, SG origin)

> Verbatim extraction from 07c §3a (lines 1863-3509, original). All 38 SG cards with AG-D-XX.X-002 IDs.

## §3a Security Goal Detail Cards (38 cards)

> 38 detail cards — one per sub-domain. Same 18-field structure as §2a. **NO Effort/Cost/Timeline fields**.

### AG-D-01.1-002 — Data at Rest Encryption

**Description:**

Data at Rest Encryption is the **SG goal binding** for D-01.1 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** All core banking DB2 z/OS data sets, payment systems, model store, data lake, EU cloud backups, audit log archives.

**Out of Scope:** Customer-managed CMK (overkill at MAX); legacy DES/3DES retained for backward-compat systems.

**Source Article:** GDPR Art. 5(1)(f) + Art. 32(1)(a) + CRA Annex I Part I (2)(e) + NIS 2 Art. 21(2)(h) + DORA Art. 9(2) + AI Act Art. 10

**NIST CSF Anchors:** PR.DS-01, PR.DS-10, PR.DS-01

**Verification Criteria (operational):**
- HSM audit log shows 100% key-usage events; AES-256-GCM enabled on all production volumes; FIPS 140-2 Level 3 HSM cluster annual certification; quarterly key-rotation audit by external auditor
- Doc 07b §4 row D-01.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + Head of Crypto (backup)

**Status:** TODO

**Dependencies:** D-01.2, D-01.3, D-01.4

**Risk if not met:** HIGH — financial data exposure + DORA Art. 87 violation + ECB supervisory finding

**Affected Stakeholders:** Customers (data subjects), regulators (ECB, BaFin, EDPB), CEO, CISO, DPO, CTO

**Maturity Score:** Current 2/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report (Art. 17/RTS) if breach; ECB annual ICT risk inspection; AI Act Art. 72 PMM if data affects AI model

**External Auditor:** ISO 27001 surveillance auditor (annual) + DORA Art. 27 TLPT (triennial) + AI Act Art. 43 conformity

**Supervisory Body:** ECB JST (Joint Supervisory Team) + BaFin + EDPB + AI Office

<a name="ag-D-01-1-002"></a>

### AG-D-01.2-002 — Data in Transit Encryption

**Description:**

Data in Transit Encryption is the **SG goal binding** for D-01.2 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** All ingress (CloudFront, API Gateway), egress (SEPA/SWIFT, payment networks), inter-service (mTLS, internal CA), mobile app (cert pinning).

**Out of Scope:** TLS 1.2 fallback (deprecated); self-signed cert (banned in production).

**Source Article:** GDPR Art. 5(1)(f) + Art. 32(1)(a) + CRA Annex I Part I (2)(e) + NIS 2 Art. 21(2)(h) + DORA Art. 9(2) + AI Act Art. 15

**NIST CSF Anchors:** PR.DS-02, PR.IR-01, PR.IR-04

**Verification Criteria (operational):**
- TLS 1.3 enforced across all endpoints; mTLS for service-to-service; quarterly cert rotation audit; quarterly penetration test
- Doc 07b §4 row D-01.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + Network Architect (backup)

**Status:** TODO

**Dependencies:** D-01.1, D-01.3, D-01.4

**Risk if not met:** HIGH — clear-text data exposure + PCI-DSS violation + DORA Art. 9 breach

**Affected Stakeholders:** Customers, payment networks, ECB, BaFin, CISO, Network Ops

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; PCI-DSS QSA annual report; ECB on-site inspection

**External Auditor:** ISO 27001 + DORA conformity + PCI-DSS QSA annual

**Supervisory Body:** BaFin + ECB + PCI SSC

<a name="ag-D-01-2-002"></a>

### AG-D-01.3-002 — Cryptographic Key Management

**Description:**

Cryptographic Key Management is the **SG goal binding** for D-01.3 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** HSM cluster (Thales/Utimaco), key ceremonies, KMS rotation policies, separation of duties (key custodian ≠ data owner).

**Out of Scope:** Cloud-native KMS only (must be HSM-backed for ECB supervision); shared keys across business units.

**Source Article:** CRA Annex I Part I (2)(e) + NIS 2 Art. 21(2)(h) + DORA Art. 9(2) + AI Act Art. 10

**NIST CSF Anchors:** PR.AA-03, PR.AA-04, PR.AA-05, PR.DS-01, PR.IR-03

**Verification Criteria (operational):**
- HSM key-ceremony audited annually; KMS rotation policy enforced (90d for data keys); separation-of-duties enforcement; quarterly log review
- Doc 07b §4 row D-01.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** Head of Crypto (primary) + CISO (backup)

**Status:** TODO

**Dependencies:** D-01.1, D-01.2, D-01.4

**Risk if not met:** MEDIUM — key compromise exposure + ECB finding + DORA Art. 9 violation

**Affected Stakeholders:** CISO, Head of Crypto, DPO, ECB, external auditor

**Maturity Score:** Current 2/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; ECB JST inspection; AI Act Art. 10 data governance audit

**External Auditor:** FIPS 140-2 + Common Criteria EAL4+ annual + DORA conformity

**Supervisory Body:** ECB JST + BaFin + BSI (FIPS)

<a name="ag-D-01-3-002"></a>

### AG-D-01.4-002 — Data Integrity Mechanisms

**Description:**

Data Integrity Mechanisms is the **SG goal binding** for D-01.4 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** DB constraints, application HMAC, Merkle tree integrity for transaction logs, WORM audit log storage.

**Out of Scope:** Blockchain anchoring (out of scope); TPM attestation (RIGOROUS-only).

**Source Article:** GDPR Art. 5(1)(d) + Art. 32(1)(b) + CRA Annex I Part I (2)(e) + DORA Art. 9(2) + AI Act Art. 10

**NIST CSF Anchors:** PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-01, PR.DS-10, PR.IR-03, PR.IR-04, PR.PS-04

**Verification Criteria (operational):**
- Merkle root verified daily; HMAC on compliance records quarterly test; WORM audit log integrity hash chain validated
- Doc 07b §4 row D-01.4 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + Data Engineer (backup)

**Status:** TODO

**Dependencies:** D-01.1, D-01.2, D-01.3

**Risk if not met:** MEDIUM — silent data corruption + DORA Art. 9 integrity violation

**Affected Stakeholders:** CISO, Data Engineer, DPO, internal audit, ECB

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** DORA 4h incident report; ECB annual ICT inspection; AI Act Art. 10 data integrity

**External Auditor:** ISO 27001 + DORA conformity annual

**Supervisory Body:** ECB JST + BaFin

<a name="ag-D-01-4-002"></a>

### AG-D-02.1-002 — Vulnerability Identification

**Description:**

Vulnerability Identification is the **SG goal binding** for D-02.1 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** SAST (Checkmarx), DAST (Burp Enterprise), SCA (Snyk), container (Trivy), IaC (Checkov), AI model (Adversarial Robustness Toolbox).

**Out of Scope:** DAST-only (must be combined with SAST); bug bounty only (must be combined with internal red team).

**Source Article:** CRA Annex I Part I (2)(d) + (h) + NIS 2 Art. 21(2)(e) + DORA Art. 24-27 + AI Act Art. 9

**NIST CSF Anchors:** ID.RA-01, ID.RA-03, ID.RA-05, PR.PS-02, PR.PS-06, DE.CM-09

**Verification Criteria (operational):**
- SAST blocks CI merge on High+; DAST weekly on staging; SCA on every PR; AI model adversarial sample testing quarterly
- Doc 07b §4 row D-02.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + DevSecOps Lead (backup)

**Status:** TODO

**Dependencies:** D-02.2, D-02.4, D-07.1, D-07.2

**Risk if not met:** HIGH — undetected vulnerability + DORA Art. 24-27 testing programme gap + AI Act Art. 9 risk

**Affected Stakeholders:** CISO, DevSecOps, CTO, AI Gov Lead, ECB, BaFin, ENISA

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; CRA Art. 14 24h+72h reporting; AI Act Art. 72 PMM; ECB TLPT scope

**External Auditor:** ISO 27001 + DORA TLPT + AI Act conformity annual

**Supervisory Body:** ECB JST + BaFin + ENISA + AI Office

<a name="ag-D-02-1-002"></a>

### AG-D-02.2-002 — Patch Management & Updates

**Description:**

Patch Management & Updates is the **SG goal binding** for D-02.2 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** OS patches (Amazon Linux 2/2023), container base-image rebuilds, dependency upgrades, mobile app releases.

**Out of Scope:** Zero-day emergency patches outside maintenance window (procedural exception with CISO approval).

**Source Article:** CRA Art. 13(8) 5y support + Art. 13(9) 10y update + NIS 2 Art. 21(2)(e) + DORA Art. 9(4)(f)

**NIST CSF Anchors:** ID.RA-01, PR.IR-03, PR.PS-01, PR.PS-02

**Verification Criteria (operational):**
- Critical CVE patched within 24h; High within 7d; quarterly mobile app release; 5-year support window documented
- Doc 07b §4 row D-02.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** DevSecOps Lead (primary) + CISO (backup)

**Status:** TODO

**Dependencies:** D-02.1, D-07.3, D-07.4

**Risk if not met:** HIGH — known CVE exploitation + DORA Art. 9(4)(f) violations + CRA Art. 13(8) 5y support

**Affected Stakeholders:** DevSecOps, CTO, CISO, customers, regulators

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; CRA Art. 14 24h reporting; ECB JST inspection

**External Auditor:** ISO 27001 + DORA Art. 26 TLPT + CRA internal

**Supervisory Body:** ECB JST + BaFin + ENISA

<a name="ag-D-02-2-002"></a>

### AG-D-02.3-002 — Coordinated Vulnerability Disclosure

**Description:**

Coordinated Vulnerability Disclosure is the **SG goal binding** for D-02.3 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** security.txt at /.well-known/security.txt, dedicated security@omnibank.de, CVD page, ISO 29147 process.

**Out of Scope:** Bug bounty programme (separate programme, deferred beyond Track B); financial rewards for researchers.

**Source Article:** CRA Art. 12 + NIS 2 Art. 12

**NIST CSF Anchors:** GV.PO-01, GV.SC-04, ID.RA-01, RS.CO-03

**Verification Criteria (operational):**
- security.txt valid + readable; 24h ack SLA verified; 72h triage SLA; quarterly test with external researcher
- Doc 07b §4 row D-02.3 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** CISO (primary) + DevSecOps Lead (backup)

**Status:** TODO

**Dependencies:** D-02.1, D-02.2

**Risk if not met:** MEDIUM — uncoordinated disclosure + CRA Art. 12 CVD obligation + NIS 2 Art. 12

**Affected Stakeholders:** External researchers, customers, CISO, ENISA, CSIRT

**Maturity Score:** Current 2/4 → Target 3/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** CRA Art. 14 24h reporting; NIS 2 Art. 12 coordinated disclosure

**External Auditor:** ISO 27001 A.6.8 + CRA Art. 12 + NIS 2 Art. 12

**Supervisory Body:** ENISA + BSI CSIRT + BaFin

<a name="ag-D-02-3-002"></a>

### AG-D-02.4-002 — Threat-Led Penetration Testing

**Description:**

Threat-Led Penetration Testing is the **SG goal binding** for D-02.4 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** External TLPT (BIG-4 TLPT provider), internal red team, purple team exercises, AI model adversarial testing.

**Out of Scope:** Single pentest cycle (must be combined with ISO 27001 annual + AI model adversarial).

**Source Article:** DORA Art. 26-27 + NIS 2 Art. 21(2)(e) + AI Act Art. 9 + Art. 43

**NIST CSF Anchors:** DE.CM-09, GV.OV-02, GV.SC-04, ID.RA-01, ID.RA-04, PR.PS-06

**Verification Criteria (operational):**
- TLPT cycle every 3y (annual per ECB adjustment); ECB scoping letter on file; closure report to ECB within 90d; AI model adversarial tested quarterly
- Doc 07b §4 row D-02.4 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + TLPT Programme Manager (backup)

**Status:** TODO

**Dependencies:** D-02.1, D-07.1, D-10.3

**Risk if not met:** HIGH — DORA Art. 26-27 mandate missed + ECB TLPT scoping failure + AI Act Art. 9 risk

**Affected Stakeholders:** CISO, CRO, ECB TLPT team, external TLPT provider, AI Gov Lead, board

**Maturity Score:** Current 1/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA Art. 26 TLPT cycle; ECB scoping letter; AI Act Art. 43 conformity assessment

**External Auditor:** ECB-recognised TLPT provider + ISO 27001 + AI Act conformity

**Supervisory Body:** ECB JST + BaFin + AI Office

<a name="ag-D-02-4-002"></a>

### AG-D-03.1-002 — Identity Lifecycle Management

**Description:**

Identity Lifecycle Management is the **SG goal binding** for D-03.1 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Hybrid identity (on-prem AD + Azure AD), Saviynt governance, CyberArk PAM, HR-feed joiner/mover/leaver.

**Out of Scope:** Self-hosted IdP (cloud-managed); legacy LDAP for production (decommissioned).

**Source Article:** GDPR Art. 5(1)(f) + Art. 30(1)(b) + CRA + NIS 2 Art. 21(2)(i) + DORA Art. 9 + AI Act Art. 14

**NIST CSF Anchors:** PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02

**Verification Criteria (operational):**
- Joiner/mover/leaver workflow automated via HR feed; quarterly orphan-account scan with zero stale; annual recertification
- Doc 07b §4 row D-03.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CIO (primary) + Identity Lead (backup)

**Status:** TODO

**Dependencies:** D-03.2, D-03.3, D-06.1, D-06.4

**Risk if not met:** HIGH — orphan account + DORA Art. 9 violation + ECB operational risk finding

**Affected Stakeholders:** CIO, HR, all employees, contractors, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; ISO 27001 A.5.16; ECB annual ICT inspection

**External Auditor:** ISO 27001 surveillance + DORA annual

**Supervisory Body:** ECB JST + BaFin + BfDI (Federal DPA)

<a name="ag-D-03-1-002"></a>

### AG-D-03.2-002 — Multi-Factor Authentication

**Description:**

Multi-Factor Authentication is the **SG goal binding** for D-03.2 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** YubiKey FIDO2 hardware tokens (privileged), Authenticator TOTP (standard), certificate-based auth (service).

**Out of Scope:** SMS MFA (deprecated); password-only (no MFA — violation).

**Source Article:** CRA + NIS 2 Art. 21(2)(i) + DORA Art. 9(4)(d) + AI Act Art. 14 + PSD2 SCA

**NIST CSF Anchors:** PR.AA-01, PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02

**Verification Criteria (operational):**
- 100% privileged users with FIDO2 hardware tokens; quarterly MFA enforcement audit; no SMS in production
- Doc 07b §4 row D-03.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CIO (primary) + Identity Lead (backup)

**Status:** TODO

**Dependencies:** D-03.1, D-03.3

**Risk if not met:** HIGH — credential compromise + DORA Art. 9(4)(d) strong auth + PSD2 SCA

**Affected Stakeholders:** CIO, all employees, customers, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; PSD2 SCA; ECB security inspection

**External Auditor:** ISO 27001 + DORA + PSD2 QSA annual

**Supervisory Body:** ECB JST + BaFin + BSI

<a name="ag-D-03-2-002"></a>

### AG-D-03.3-002 — Authorization & Least Privilege

**Description:**

Authorization & Least Privilege is the **SG goal binding** for D-03.3 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** RBAC + ABAC engine, privileged access workstation (PAW), just-in-time (JIT) via CyberArk, zero standing privilege.

**Out of Scope:** Static admin roles (deprecated); shared service accounts.

**Source Article:** GDPR Art. 5(1)(c) + Art. 22 + NIS 2 + DORA Art. 9 + AI Act Art. 14

**NIST CSF Anchors:** PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-02, PR.PS-04

**Verification Criteria (operational):**
- Zero standing privilege verified; JIT access logs 100% reviewed; quarterly access review by manager
- Doc 07b §4 row D-03.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CIO (primary) + Identity Lead (backup)

**Status:** TODO

**Dependencies:** D-03.1, D-03.2, D-07.1

**Risk if not met:** HIGH — privilege escalation + DORA Art. 9 violation + GDPR Art. 32 breach

**Affected Stakeholders:** CIO, all employees, AI Gov Lead, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; ISO 27001 A.5.15; AI Act Art. 14 human oversight

**External Auditor:** ISO 27001 + DORA + AI Act conformity

**Supervisory Body:** ECB JST + BaFin + BfDI

<a name="ag-D-03-3-002"></a>

### AG-D-03.4-002 — Secure System Defaults

**Description:**

Secure System Defaults is the **SG goal binding** for D-03.4 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** CIS Benchmarks (Ubuntu, Windows, K8s), AWS Config + Azure Policy, automated hardening scripts.

**Out of Scope:** Bespoke hardening (use CIS as baseline); manual configuration drift.

**Source Article:** CRA + ISO 27001 A.8.9

**NIST CSF Anchors:** GV.PO-01, GV.SC-03, PR.DS-10, PR.PS-01

**Verification Criteria (operational):**
- Quarterly CIS compliance scan; deviation approval workflow documented; <5% deviation baseline
- Doc 07b §4 row D-03.4 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** DevSecOps Lead (primary) + CISO (backup)

**Status:** TODO

**Dependencies:** D-07.1, D-07.3

**Risk if not met:** MEDIUM — CIS drift + CRA compliance weakness + ISO 27001 A.8.9

**Affected Stakeholders:** DevSecOps, CISO, IT Ops, ISO 27001 auditor

**Maturity Score:** Current 2/4 → Target 3/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** ISO 27001 annual surveillance; AWS/Azure audit

**External Auditor:** ISO 27001 internal + external + CSA STAR

**Supervisory Body:** BSI + cloud provider compliance

<a name="ag-D-03-4-002"></a>

### AG-D-04.1-002 — Incident Detection & Triage

**Description:**

Incident Detection & Triage is the **SG goal binding** for D-04.1 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** 24/7 SOC (in-house tier-1/2/3 + co-managed overflow), SIEM (Splunk), SOAR (Splunk SOAR), EDR (CrowdStrike), NDR (Vectra AI), UEBA (Exabeam).

**Out of Scope:** Reactive-only (must be 24/7 with proactive threat hunting); single-vendor stack (must be defence-in-depth).

**Source Article:** CRA + NIS 2 Art. 21(2)(b) + DORA Art. 10 + AI Act Art. 73

**NIST CSF Anchors:** DE.CM-01, DE.CM-02, DE.CM-03, DE.CM-06, DE.CM-09, RS.MA-02, RS.MA-02, RS.AN-03

**Verification Criteria (operational):**
- MTTD <15 min; SOC 24/7 staffed; quarterly purple-team exercise; monthly detection-coverage gap analysis
- KPI: MTTD <15min measured monthly; alert response time P95 <5min for critical alerts; SOC 24/7 staffing validated per shift roster (per Doc 04 §10 BG-005 readiness)
- Doc 07b §4 row D-04.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + SOC Director (backup)

**Status:** TODO

**Dependencies:** D-04.2, D-04.3, D-10.1, D-10.2

**Risk if not met:** HIGH — undetected incident + DORA Art. 10 violation + AI Act Art. 73 reporting

**Affected Stakeholders:** CISO, SOC, customers, ECB, BaFin, AI Gov Lead

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; AI Act Art. 73 15d/2d/10d reporting

**External Auditor:** ISO 27001 surveillance + DORA TLPT + AI Act conformity

**Supervisory Body:** ECB JST + BaFin + AI Office

<a name="ag-D-04-1-002"></a>

### AG-D-04.2-002 — Containment & Mitigation

**Description:**

Containment & Mitigation is the **SG goal binding** for D-04.2 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Dedicated IR team, SOAR playbooks (15+), forensic toolkit (EnCase), tabletop exercises quarterly.

**Out of Scope:** Ad-hoc containment (must be playbook-driven); single-team (must be cross-functional).

**Source Article:** GDPR Art. 32 + CRA + NIS 2 Art. 21(2)(c) + DORA Art. 17 + AI Act Art. 73

**NIST CSF Anchors:** RS.MA-02, RS.MA-02, RS.MI-01, RS.MI-02, ID.RA-06

**Verification Criteria (operational):**
- MTTC <4h for critical; monthly playbook drill; annual red team; SOAR MTTR <30min
- Doc 07b §4 row D-04.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + IR Lead (backup)

**Status:** TODO

**Dependencies:** D-04.1, D-04.3, D-04.4

**Risk if not met:** HIGH — uncontained incident + DORA Art. 17 violation + ECB finding

**Affected Stakeholders:** CISO, IR team, Legal, DPO, CRO, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; AI Act Art. 72 PMM; ECB on-site inspection

**External Auditor:** ISO 27001 + DORA + AI Act + ENISA CSIRT Network

**Supervisory Body:** ECB JST + BaFin + ENISA + AI Office

<a name="ag-D-04-2-002"></a>

### AG-D-04.3-002 — Regulatory Notification

**Description:**

Regulatory Notification is the **SG goal binding** for D-04.3 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** 5-regulation max-SLA routing pipeline — DORA 4h + NIS 2 24h + CRA 24h + GDPR 72h + AI Act 15d/2d/10d.

**Out of Scope:** Single-reg workflow (forces duplicate work); manual routing (must be SOAR-automated).

**Source Article:** DORA Art. 17-19 + RTS Art. 6 + NIS 2 Art. 23(4) + CRA Art. 14 + GDPR Art. 33 + AI Act Art. 73

**NIST CSF Anchors:** RS.CO-02, RS.MA-01, RS.MA-03, ID.RA-06

**Verification Criteria (operational):**
- Tabletop exercises quarterly; per-recipient template segregation; per-recipient channel gating; single clock-start discipline; MTTC <4h for DORA-critical
- Doc 07b §4 row D-04.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CEO (accountable) + CISO (responsible) + DPO + CRO + Legal

**Status:** TODO

**Dependencies:** D-04.1, D-04.2, D-09.1, D-09.4

**Risk if not met:** HIGH — 5 fine regimes possible + ECB + BaFin + EDPB + ENISA + AI Office + DPA scrutiny

**Affected Stakeholders:** Customers, CEO, board, CISO, DPO, CRO, Legal, ECB, BaFin, EDPB, ENISA, AI Office, DPA

**Maturity Score:** Current 2/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h (RTS Art. 6) + NIS 2 24h + CRA 24h + GDPR 72h + AI Act 15d/2d/10d — all 5 regulations simultaneously

**External Auditor:** Joint ECB/BaFin supervised drill (annual) + ISO 27001 + DORA + ENISA exercise

**Supervisory Body:** ECB JST + BaFin + EDPB + national DPA + ENISA + BSI CSIRT + AI Office

<a name="ag-D-04-3-002"></a>

### AG-D-04.4-002 — Data Restoration & Recovery

**Description:**

Data Restoration & Recovery is the **SG goal binding** for D-04.4 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** 2 active data centres + 1 cold standby, RTO 4h / RPO 15min for critical systems, quarterly DR test, annual full failover.

**Out of Scope:** Single-site (rejected); recovery-only (must include prevention and detection).

**Source Article:** NIS 2 Art. 21(2)(c) + DORA Art. 11-12

**NIST CSF Anchors:** PR.IR-01, PR.IR-02, PR.IR-03, PR.IR-04, RC.RP-01, RC.RP-02, RC.RP-03, RC.RP-05

**Verification Criteria (operational):**
- RTO 4h verified quarterly; RPO 15min verified; annual full failover test; cyber recovery test annually
- KPI: Quarterly DR test verifies RTO ≤24h (target ≤4h) and RPO ≤1h (target 15min) — measured in disaster simulation report (per BG-005 99.99% uptime SLA for core banking)
- Doc 07b §4 row D-04.4 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CTO (primary) + DR Manager (backup)

**Status:** TODO

**Dependencies:** D-04.1, D-04.2, D-09.3

**Risk if not met:** HIGH — extended outage + DORA Art. 12 BC violation + 99.99% SLA breach

**Affected Stakeholders:** CTO, DR Manager, customers, regulators, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; 99.99% SLA per BG-005; ECB annual inspection

**External Auditor:** ISO 27001 A.5.30 + DORA Art. 12 + cyber recovery test

**Supervisory Body:** ECB JST + BaFin

<a name="ag-D-04-4-002"></a>

### AG-D-05.1-002 — Data Minimisation

**Description:**

Data Minimisation is the **SG goal binding** for D-05.1 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Field-level enforcement in DB schema, automated data-classification scanner, consent management (OneTrust).

**Out of Scope:** Manual minimisation (must be automated); unlimited collection (must be bounded).

**Source Article:** GDPR Art. 5(1)(c) + CRA + AI Act Art. 10

**NIST CSF Anchors:** ID.AM-01, ID.AM-02, PR.DS-01

**Verification Criteria (operational):**
- Quarterly data minimisation audit; field-level enforcement validated annually; consent management audit-trail
- Doc 07b §4 row D-05.1 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** DPO (primary) + Data Engineer (backup)

**Status:** TODO

**Dependencies:** D-05.2, D-05.3, D-09.3

**Risk if not met:** MEDIUM — over-collection + GDPR Art. 5(1)(c) violation + AI Act Art. 10 data quality

**Affected Stakeholders:** DPO, Data Engineer, customers, EDPB, DPA

**Maturity Score:** Current 2/4 → Target 3/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** GDPR periodic audit; AI Act Art. 10 data governance

**External Auditor:** ISO 27701 + AI Act conformity

**Supervisory Body:** BfDI (Federal DPA) + EDPB + AI Office

<a name="ag-D-05-1-002"></a>

### AG-D-05.2-002 — Retention & Archiving

**Description:**

Retention & Archiving is the **SG goal binding** for D-05.2 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Retention policy (5-10y BaFin/ECB for financial transactions + 7y audit logs), archive tooling (Hadoop cold), automated deletion.

**Out of Scope:** Indefinite retention (prohibited); manual deletion (must be automated).

**Source Article:** GDPR Art. 5(1)(e) + AI Act Art. 10 + BaFin/ECB requirements

**NIST CSF Anchors:** PR.PS-02, PR.DS-01, ID.AM-01

**Verification Criteria (operational):**
- Quarterly deletion validation; 5-year + 7-year retention verified; BaFin retention rules applied
- Doc 07b §4 row D-05.2 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** DPO (primary) + Records Manager (backup)

**Status:** TODO

**Dependencies:** D-05.1, D-05.3, D-09.4

**Risk if not met:** MEDIUM — over-retention + GDPR Art. 5(1)(e) + BaFin retention non-compliance

**Affected Stakeholders:** DPO, Records Manager, customers, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** GDPR periodic audit; BaFin/ECB retention requirements; AI Act Art. 10

**External Auditor:** ISO 27001 A.5.34 + DORA Art. 11 + ECB retention

**Supervisory Body:** ECB JST + BaFin + BfDI

<a name="ag-D-05-2-002"></a>

### AG-D-05.3-002 — Right to Erasure

**Description:**

Right to Erasure is the **SG goal binding** for D-05.3 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Erasure API endpoint, cryptographic sharding (destroy identity, retain anonymised log per T-002), DSAR workflow (30-day SLA).

**Out of Scope:** Hard-delete (collides with DORA Art. 12 immutable logs — T-002); manual erasure (must be tokenised).

**Source Article:** GDPR Art. 17 + CRA Art. 13 + DORA Art. 11-12 (T-002)

**NIST CSF Anchors:** PR.PS-02, PR.DS-01, PR.DS-10

**Verification Criteria (operational):**
- DSAR 30-day SLA verified; cryptographic sharding quarterly test; anonymised log integrity preserved
- Doc 07b §4 row D-05.3 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** DPO (primary) + Data Engineer (backup)

**Status:** TODO

**Dependencies:** D-05.1, D-05.2, D-10.2

**Risk if not met:** HIGH — data subject rights violation + GDPR Art. 17 fine + DORA Art. 11-19 conflict

**Affected Stakeholders:** DPO, customers, EDPB, BfDI, CRO, ECB

**Maturity Score:** Current 2/4 → Target 4/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** GDPR Art. 17 30-day SLA; CRA Art. 13; DORA Art. 11-19 (T-002 RESOLVED)

**External Auditor:** ISO 27001 + DORA Art. 12 + external auditor cryptographic sharding review

**Supervisory Body:** BfDI + EDPB + ECB JST + BaFin

<a name="ag-D-05-3-002"></a>

### AG-D-05.4-002 — Data Portability

**Description:**

Data Portability is the **SG goal binding** for D-05.4 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** JSON export endpoint (machine-readable), 30-day SLA, GDPR Art. 20 right to data portability.

**Out of Scope:** PDF-only (must be machine-readable); manual export (must be API-driven).

**Source Article:** GDPR Art. 20

**NIST CSF Anchors:** PR.DS-10, PR.PS-02

**Verification Criteria (operational):**
- JSON export endpoint tested; 30-day SLA verified; CSV format supported
- Doc 07b §4 row D-05.4 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** DPO (primary) + Data Engineer (backup)

**Status:** TODO

**Dependencies:** D-05.1, D-05.2

**Risk if not met:** MEDIUM — GDPR Art. 20 violation + customer rights denial

**Affected Stakeholders:** DPO, customers, BfDI

**Maturity Score:** Current 2/4 → Target 3/4

**Implementation Priority:** MEDIUM

**Regulatory Reporting:** GDPR Art. 20 30-day SLA

**External Auditor:** ISO 27001 + GDPR audit

**Supervisory Body:** BfDI

<a name="ag-D-05-4-002"></a>

### AG-D-06.1-002 — Vendor Risk Assessment

**Description:**

Vendor Risk Assessment is the **SG goal binding** for D-06.1 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Own vendor risk programme, DORA Art. 28 pre-contractual assessment, Art. 30 CTPP register, annual + critical-vendor quarterly review.

**Out of Scope:** Lightweight questionnaire (must be DORA-grade); ad-hoc assessment (must be annual).

**Source Article:** NIS 2 + DORA Art. 28 + GDPR + CRA

**NIST CSF Anchors:** GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, GV.SC-03, UNMAPPED_CSF, PR.DS-01

**Verification Criteria (operational):**
- Critical vendor quarterly review; DORA Art. 30 CTPP register maintained; annual vendor review 100% completion
- Doc 07b §4 row D-06.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CRO (primary) + Procurement (backup)

**Status:** TODO

**Dependencies:** D-06.2, D-06.3, D-06.4, D-09.3

**Risk if not met:** HIGH — critical ICT vendor failure + DORA Art. 28 violation + ECB finding

**Affected Stakeholders:** CRO, Procurement, CISO, Legal, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 30 CTPP register; ECB annual inspection

**External Auditor:** ISO 27001 + DORA Art. 30 + ECB JST inspection

**Supervisory Body:** ECB JST + BaFin + ESAs Joint Committee (if CTPP)

<a name="ag-D-06-1-002"></a>

### AG-D-06.2-002 — Software Bill of Materials (SBOM)

**Description:**

Software Bill of Materials (SBOM) is the **SG goal binding** for D-06.2 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** CycloneDX SBOM in CI/CD per release, CRA Art. 13(13) 10-year documentation, machine-readable formats (SPDX + CycloneDX).

**Out of Scope:** Per-quarter SBOM (must be per-release); proprietary format (must be machine-readable).

**Source Article:** CRA Annex I Part II + Art. 13(13)

**NIST CSF Anchors:** ID.AM-08, PR.DS-01, PR.PS-02

**Verification Criteria (operational):**
- Per-release SBOM <2hr generation; 10-year retention; SPDX + CycloneDX supported
- Doc 07b §4 row D-06.2 cross-reference verified
- TEST + DEMONSTRATE (STANDARD) cadence aligned with §4 verification_method column

**Verification Method:** TEST + DEMONSTRATE (STANDARD)

**Owner:** DevSecOps Lead (primary) + CISO (backup)

**Status:** TODO

**Dependencies:** D-02.1, D-07.3

**Risk if not met:** MEDIUM — unknown dependency + CRA Art. 13(13) violation + DORA Art. 8 inventory gap

**Affected Stakeholders:** DevSecOps, CISO, CTO, customers, ENISA

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** CRA Art. 13(13) 10y retention; NIS 2 supply chain transparency

**External Auditor:** ISO 27001 + CRA conformity + ENISA supply chain

**Supervisory Body:** ENISA + BaFin (if material)

<a name="ag-D-06-2-002"></a>

### AG-D-06.3-002 — Contractual Security Obligations

**Description:**

Contractual Security Obligations is the **SG goal binding** for D-06.3 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** DPA + DORA Art. 30 CTPP clauses + NIS 2 supply chain + AI Act Art. 25 downstream, Legal review workflow.

**Out of Scope:** Standard MSA (must be DORA-grade); ad-hoc clauses (must be clause-bank).

**Source Article:** GDPR + NIS 2 + DORA Art. 30 + AI Act Art. 25

**NIST CSF Anchors:** GV.SC-01, GV.SC-02, GV.SC-04, GV.SC-05, PR.DS-01

**Verification Criteria (operational):**
- 100% critical vendor contracts with CTPP clauses; AI Act downstream provider clauses; annual contract review
- Doc 07b §4 row D-06.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** Legal (primary) + CRO + CISO (review)

**Status:** TODO

**Dependencies:** D-06.1, D-06.4

**Risk if not met:** HIGH — CTPP contractual gap + DORA Art. 30 violation + AI Act Art. 25 gap

**Affected Stakeholders:** Legal, CRO, CISO, Procurement, ECB, BaFin, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA Art. 30; AI Act Art. 25; GDPR DPA; ECB JST inspection

**External Auditor:** ISO 27001 + DORA Art. 30 + AI Act conformity

**Supervisory Body:** ECB JST + BaFin + BfDI + AI Office

<a name="ag-D-06-3-002"></a>

### AG-D-06.4-002 — Third-Party Boundary Management

**Description:**

Third-Party Boundary Management is the **SG goal binding** for D-06.4 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Boundary management (API gateway + dedicated circuits to AWS/Azure/payment networks/credit bureaus), supplier incident playbook, DORA Art. 28 exit strategy.

**Out of Scope:** Implicit boundary (must be explicit); no exit strategy (DORA Art. 28 requires).

**Source Article:** NIS 2 + DORA Art. 28

**NIST CSF Anchors:** PR.DS-01, PR.PS-04, GV.SC-04

**Verification Criteria (operational):**
- API gateway enforces schema validation + rate limiting; exit strategy tested annually; supplier incident playbook
- Doc 07b §4 row D-06.4 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + Cloud Architect (backup)

**Status:** TODO

**Dependencies:** D-06.1, D-06.3, D-09.3

**Risk if not met:** HIGH — boundary breach + DORA Art. 28 exit strategy gap + ECB finding

**Affected Stakeholders:** CISO, Cloud Architect, CRO, ECB, BaFin, vendor

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 28 exit strategy; ECB annual inspection

**External Auditor:** ISO 27001 + DORA Art. 28 + ECB JST

**Supervisory Body:** ECB JST + BaFin + ESAs Joint Committee (if CTPP)

<a name="ag-D-06-4-002"></a>

### AG-D-07.1-002 — Secure-by-Design Principles

**Description:**

Secure-by-Design Principles is the **SG goal binding** for D-07.1 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** NIST SSDF SP 800-218 + OWASP SAMM Level 3 + STRIDE threat modelling + architecture review board.

**Out of Scope:** Ad-hoc design (must be STRIDE-driven); single-source-of-truth (must be review-board).

**Source Article:** CRA Art. 13(1) + NIS 2 Art. 21 + DORA Art. 10 + GDPR Art. 25 + AI Act Art. 9

**NIST CSF Anchors:** PR.PS-01, PR.PS-02, PR.PS-06, , ID.RA-04, GV.SC-04

**Verification Criteria (operational):**
- Architecture review board mandatory for all new systems; STRIDE applied; SAMM Level 3 verified
- KPI: Monthly bias audit on OmniScore AI Platform; bias metrics must remain <1% across all protected characteristics (per AI Act Art. 10 data quality governance + BG-008 AI bias <1% target)
- Doc 07b §4 row D-07.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CTO (primary) + Security Architect (backup)

**Status:** TODO

**Dependencies:** D-07.2, D-07.3, D-07.4, D-09.1

**Risk if not met:** HIGH — design weakness + CRA Art. 13(1) violation + AI Act Art. 9 risk + DORA Art. 10

**Affected Stakeholders:** CTO, AI Gov Lead, DPO, CISO, ECB, BaFin, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; AI Act Art. 9 risk management; CRA Art. 13(1); ECB annual inspection

**External Auditor:** ISO 27001 + DORA + AI Act conformity + CRA

**Supervisory Body:** ECB JST + BaFin + AI Office + ENISA

<a name="ag-D-07-1-002"></a>

### AG-D-07.2-002 — Secure Coding Practices

**Description:**

Secure Coding Practices is the **SG goal binding** for D-07.2 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** SAST (Checkmarx) blocking CI merge, DAST (Burp Enterprise), secret scanning (GitGuardian), AI code review (Copilot + custom), secure coding standards (CERT + OWASP).

**Out of Scope:** Periodic scans (must be CI gates); standards-only (must be automated).

**Source Article:** CRA + NIS 2 + DORA + AI Act

**NIST CSF Anchors:** PR.PS-02, PR.PS-03, PR.PS-06, ID.RA-01, DE.CM-09

**Verification Criteria (operational):**
- SAST >High blocks merge; annual secure coding training; secret scanning zero plaintext in repos
- Doc 07b §4 row D-07.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** Lead Dev (primary) + CISO (backup)

**Status:** TODO

**Dependencies:** D-07.1, D-07.3, D-09.2

**Risk if not met:** HIGH — vulnerability injection + CRA + DORA + AI Act compliance gap

**Affected Stakeholders:** Lead Dev, CISO, CTO, customers

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; CRA Art. 13; AI Act Art. 9

**External Auditor:** ISO 27001 + DORA + CRA conformity

**Supervisory Body:** ECB JST + BaFin + ENISA

<a name="ag-D-07-2-002"></a>

### AG-D-07.3-002 — CI/CD Pipeline Security

**Description:**

CI/CD Pipeline Security is the **SG goal binding** for D-07.3 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Hardened CI/CD (GitLab + ArgoCD), signed artefacts (Cosign), SBOM attestation, SLSA Level 3, pipeline-as-code, ephemeral runners.

**Out of Scope:** Manual release (must be automated); unprotected pipeline (must be signed).

**Source Article:** NIS 2 + DORA Art. 10 + CRA Art. 13(5)

**NIST CSF Anchors:** PR.PS-01, PR.PS-02, PR.PS-06, PR.DS-01, UNMAPPED_CSF

**Verification Criteria (operational):**
- SLSA Level 3 maintained; image signing mandatory; ephemeral runners; pipeline-as-code reviewed
- Doc 07b §4 row D-07.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** DevSecOps Lead (primary) + CTO (backup)

**Status:** TODO

**Dependencies:** D-07.1, D-07.2, D-07.4

**Risk if not met:** HIGH — supply chain attack + CRA + DORA Art. 10 violation

**Affected Stakeholders:** DevSecOps, CTO, CISO, customers, ECB

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; CRA Art. 13(5); ENISA supply chain

**External Auditor:** ISO 27001 + DORA + SLSA + CRA

**Supervisory Body:** ECB JST + BaFin + ENISA

<a name="ag-D-07-3-002"></a>

### AG-D-07.4-002 — Change Management

**Description:**

Change Management is the **SG goal binding** for D-07.4 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** ServiceNow change management, 4-eyes principle, CAB review for critical changes, emergency change procedure, DORA Art. 10 ICT change management.

**Out of Scope:** Ad-hoc change (must be ServiceNow-tracked); no emergency procedure (must have documented).

**Source Article:** NIS 2 + DORA Art. 10

**NIST CSF Anchors:** PR.PS-01, PR.PS-01, PR.DS-01, PR.PS-01

**Verification Criteria (operational):**
- 100% prod changes via ServiceNow; 4-eyes verification; emergency procedure with retrospective CAB
- Doc 07b §4 row D-07.4 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CTO (primary) + Change Manager (backup)

**Status:** TODO

**Dependencies:** D-07.1, D-07.3, D-09.4

**Risk if not met:** HIGH — uncontrolled change + DORA Art. 10 violation + ECB finding

**Affected Stakeholders:** CTO, Change Manager, CRO, CISO, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 10; ECB annual inspection

**External Auditor:** ISO 27001 + DORA Art. 10 + ITIL-aligned

**Supervisory Body:** ECB JST + BaFin

<a name="ag-D-07-4-002"></a>

### AG-D-08.1-002 — General Security Awareness

**Description:**

General Security Awareness is the **SG goal binding** for D-08.1 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Monthly phishing simulation, quarterly awareness training, annual certification, role-based content, ISO 27001 A.7.2.2.

**Out of Scope:** Annual-only (must be monthly); uniform training (must be role-based).

**Source Article:** NIS 2 + DORA + GDPR

**NIST CSF Anchors:** PR.AT-01, PR.AT-02, PR.AT-01, PR.AT-02, PR.AT-02

**Verification Criteria (operational):**
- Phishing click rate <5%; annual certification 100% completion; quarterly awareness training
- Doc 07b §4 row D-08.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + HR (backup)

**Status:** TODO

**Dependencies:** D-08.2, D-08.3

**Risk if not met:** MEDIUM — human factor + DORA Art. 9 violation + ISO 27001 A.7.2.2

**Affected Stakeholders:** All employees, CISO, HR, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** DORA 4h incident report; ISO 27001 A.7.2.2; ECB annual inspection

**External Auditor:** ISO 27001 surveillance + DORA

**Supervisory Body:** ECB JST + BaFin

<a name="ag-D-08-1-002"></a>

### AG-D-08.2-002 — Role-Specific Competence

**Description:**

Role-Specific Competence is the **SG goal binding** for D-08.2 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Role-based training paths — developers (Secure Code Warrior), SOC (SANS), DPO (IAPP), AI engineers (AI Act + ISO 42001), annual certification.

**Out of Scope:** Single curriculum (must be role-based); no AI training (must include AI Act).

**Source Article:** GDPR + NIS 2 + DORA + AI Act

**NIST CSF Anchors:** PR.AT-01, PR.AT-02, PR.AT-01, PR.AT-02, PR.AT-02

**Verification Criteria (operational):**
- AI engineers AI Act Annex III training mandatory; DPO CIPP/E; SOC SANS; annual recertification
- Doc 07b §4 row D-08.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + HR + AI Gov Lead (backup)

**Status:** TODO

**Dependencies:** D-08.1, D-08.3

**Risk if not met:** MEDIUM — competency gap + DORA + AI Act + GDPR

**Affected Stakeholders:** All employees, CISO, HR, AI Gov Lead, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** HIGH

**Regulatory Reporting:** GDPR + NIS 2 + DORA + AI Act

**External Auditor:** ISO 27001 + DORA + AI Act conformity

**Supervisory Body:** ECB JST + BaFin + EDPB + AI Office

<a name="ag-D-08-2-002"></a>

### AG-D-08.3-002 — Management Board Training

**Description:**

Management Board Training is the **SG goal binding** for D-08.3 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Management board briefing programme — annual cybersecurity, NIS 2 Art. 21 management liability, DORA Art. 5 management accountability, AI Act Art. 14 human oversight.

**Out of Scope:** CISO-only briefing (must include board); one-time (must be annual).

**Source Article:** NIS 2 Art. 21 + DORA Art. 5(2) + AI Act Art. 14

**NIST CSF Anchors:** GV.OC-01, GV.OC-02, GV.OC-04, GV.OC-05, ID.RA-04

**Verification Criteria (operational):**
- Annual board briefing documented in minutes; personal liability acknowledged in writing; ECB inspection-ready
- Doc 07b §4 row D-08.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CEO (primary) + Board Secretary (backup)

**Status:** TODO

**Dependencies:** D-08.1, D-08.2, D-09.1

**Risk if not met:** HIGH — management liability + NIS 2 Art. 21 + DORA Art. 5(2) + AI Act Art. 14

**Affected Stakeholders:** Board, CEO, shareholders, ECB, BaFin, EDPB

**Maturity Score:** Current 2/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** NIS 2 Art. 21 management liability + DORA Art. 5(2) + AI Act Art. 14

**External Auditor:** ISO 27001 A.5.2 + DORA Art. 5 + ECB JST inspection

**Supervisory Body:** ECB JST + BaFin + BfDI + AI Office

<a name="ag-D-08-3-002"></a>

### AG-D-09.1-002 — Information Security Policies

**Description:**

Information Security Policies is the **SG goal binding** for D-09.1 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Full ISMS (ISO 27001 certified) + DORA Art. 5 ICT risk management framework + AI Act Art. 9 risk management system + 5-policy architecture (DPO / mgmt body / manufacturer / DORA / AI Gov) with 5 distinct governance bodies.

**Out of Scope:** Single policy (must be 5-architecture); sub-domain coverage (must be ISMS-wide).

**Source Article:** GDPR + CRA + NIS 2 + DORA Art. 5 + AI Act Art. 9

**NIST CSF Anchors:** GV.OC-01, GV.OC-02, GV.PO-01, GV.PO-02, GV.RM-01, GV.RM-04

**Verification Criteria (operational):**
- ISMS surveillance audit annual; 5-policy architecture documented; DORA Art. 5 framework documented; AI Act Art. 9 risk system
- Doc 07b §4 row D-09.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + CRO + DPO + AI Gov Lead (5-policy architecture)

**Status:** TODO

**Dependencies:** D-09.2, D-09.3, D-09.4, D-08.3

**Risk if not met:** HIGH — policy fragmentation + DORA Art. 5 + AI Act Art. 9 + ECB finding

**Affected Stakeholders:** All staff, board, CEO, CISO, CRO, DPO, AI Gov Lead, ECB, BaFin, EDPB, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 5; AI Act Art. 9; GDPR DPA; ISO 27001 annual

**External Auditor:** ISO 27001 surveillance + DORA Art. 26 + AI Act conformity + ECB JST

**Supervisory Body:** ECB JST + BaFin + BfDI + EDPB + AI Office + ENISA

<a name="ag-D-09-1-002"></a>

### AG-D-09.2-002 — Impact & Risk Assessments

**Description:**

Impact & Risk Assessments is the **SG goal binding** for D-09.2 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** IPSARA Unified Assessment Framework (T-003 RESOLVED) — DPIA (GDPR Art. 35) + FRIA (AI Act Art. 27) + ICT risk (DORA Art. 6) + CRA + NIS 2.

**Out of Scope:** Single-purpose (must be unified); ad-hoc (must be annual).

**Source Article:** GDPR Art. 35 + AI Act Art. 27 + DORA Art. 6 + CRA + NIS 2 Art. 21(2)(d)

**NIST CSF Anchors:** ID.RA-01, ID.RA-04, ID.RA-05, GV.RM-01, GV.RM-04

**Verification Criteria (operational):**
- IPSARA annual review; per-regulation output generated; 5-framework discharges; ECB + AI Act + GDPR inspection-ready
- KPI: Annual DPIA + FRIA review cycle; quantified risk reduction targets per GDPR Art. 35(7) and AI Act Art. 27(4) — IPSARA unified discharge of 5 obligations (DPIA + FRIA + DORA ICT risk + CRA RA + NIS 2)
- Doc 07b §4 row D-09.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CRO (primary) + DPO + AI Gov Lead (5-assessment integration)

**Status:** TODO

**Dependencies:** D-09.1, D-09.3, D-09.4, D-07.1

**Risk if not met:** HIGH — assessment fragmentation + 5-assessment obligation + ECB + AI Act + GDPR fines

**Affected Stakeholders:** Customers, DPO, CRO, AI Gov Lead, ECB, BaFin, EDPB, AI Office

**Maturity Score:** Current 2/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** GDPR Art. 35 DPIA + AI Act Art. 27 FRIA + DORA Art. 6 ICT risk + CRA + NIS 2 risk analysis

**External Auditor:** ISO 27001 + DORA + AI Act conformity + ECB JST

**Supervisory Body:** ECB JST + BaFin + EDPB + BfDI + AI Office

<a name="ag-D-09-2-002"></a>

### AG-D-09.3-002 — Asset Inventories

**Description:**

Asset Inventories is the **SG goal binding** for D-09.3 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** ServiceNow CMDB + dedicated DORA Art. 8 ICT systems inventory + automated discovery (Qualys + Azure Arc) + quarterly reconciliation.

**Out of Scope:** Manual inventory (must be automated); ad-hoc reconciliation (must be quarterly).

**Source Article:** DORA Art. 8 + NIS 2 + CRA Annex VII

**NIST CSF Anchors:** ID.AM-01, ID.AM-02, ID.AM-03, ID.AM-04, ID.AM-08, PR.PS-02

**Verification Criteria (operational):**
- Critical ICT assets identified per DORA; annual full reconciliation; <2% drift between CMDB and Qualys
- Doc 07b §4 row D-09.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + IT Ops + DevSecOps (backup)

**Status:** TODO

**Dependencies:** D-09.1, D-09.4, D-06.1

**Risk if not met:** HIGH — unknown asset + DORA Art. 8 violation + ECB finding

**Affected Stakeholders:** CISO, IT Ops, DevSecOps, CRO, ECB, BaFin

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 8; ECB annual inspection

**External Auditor:** ISO 27001 + DORA Art. 8 + ECB JST

**Supervisory Body:** ECB JST + BaFin + ENISA

<a name="ag-D-09-3-002"></a>

### AG-D-09.4-002 — Records of Processing

**Description:**

Records of Processing is the **SG goal binding** for D-09.4 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Own RoPA (GDPR Art. 30) + DORA Art. 17-19 ICT incident records + AI Act Art. 12 technical documentation + CRA Art. 13 technical documentation.

**Out of Scope:** Single-record (must be 5-architecture); ad-hoc (must be RoPA).

**Source Article:** GDPR Art. 30 + DORA Art. 17-19 + AI Act Art. 12 + CRA Art. 13

**NIST CSF Anchors:** ID.AM-01, PR.PS-01, PR.PS-02, GV.OC-04

**Verification Criteria (operational):**
- 5y retention (DORA) + 10y (AI Act) + GDPR RoPA; ECB + AI Office + EDPB inspection-ready
- Doc 07b §4 row D-09.4 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** DPO (primary) + CRO + AI Gov Lead (5-record integration)

**Status:** TODO

**Dependencies:** D-09.1, D-09.2, D-09.3

**Risk if not met:** HIGH — record fragmentation + GDPR Art. 30 + DORA Art. 17-19 + AI Act Art. 12

**Affected Stakeholders:** DPO, CRO, AI Gov Lead, customers, ECB, BaFin, EDPB, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** GDPR Art. 30 RoPA + DORA Art. 17-19 records + AI Act Art. 12 docs + CRA Art. 13 docs

**External Auditor:** ISO 27001 + DORA + AI Act conformity + GDPR

**Supervisory Body:** ECB JST + BaFin + EDPB + BfDI + AI Office

<a name="ag-D-09-4-002"></a>

### AG-D-10.1-002 — Continuous Security Monitoring

**Description:**

Continuous Security Monitoring is the **SG goal binding** for D-10.1 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** 24/7 SOC + SIEM (Splunk Enterprise) + ISO 27001 A.8.16 monitoring + DORA Art. 13 ICT monitoring + AI Act post-market monitoring (Art. 72).

**Out of Scope:** Business-hours only (must be 24/7); single platform (must be layered).

**Source Article:** CRA + NIS 2 + DORA Art. 13 + AI Act Art. 72

**NIST CSF Anchors:** DE.CM-01, DE.CM-02, DE.CM-03, DE.CM-06, DE.CM-09, ID.AM-03

**Verification Criteria (operational):**
- SIEM 1y hot + 7y cold; AI model monitoring integrated; 24/7 SOC staffed; MTTD <15min
- KPI: 24/7 SOC staffing validated quarterly (4 shifts × 6 + 1 on-call); alert response time P95 <5min for critical alerts measured monthly; AI model drift detection latency <1h
- Doc 07b §4 row D-10.1 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + SOC Director (backup)

**Status:** TODO

**Dependencies:** D-04.1, D-10.2, D-10.3

**Risk if not met:** HIGH — undetected incident + DORA Art. 13 violation + AI Act Art. 72 PMM

**Affected Stakeholders:** CISO, SOC, customers, ECB, BaFin, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; AI Act Art. 72 PMM; ECB annual inspection

**External Auditor:** ISO 27001 + DORA + AI Act conformity

**Supervisory Body:** ECB JST + BaFin + AI Office

<a name="ag-D-10-1-002"></a>

### AG-D-10.2-002 — Audit Logging & Traceability

**Description:**

Audit Logging & Traceability is the **SG goal binding** for D-10.2 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** Tamper-evident audit logs (WORM) + cryptographic hash chains + DORA Art. 12 ICT change records + 5-10y retention (BaFin/ECB) + GDPR Art. 30 RoPA traceability + AI Act Art. 12 technical documentation.

**Out of Scope:** Mutable logs (must be WORM); plaintext (must be hash-chained).

**Source Article:** DORA Art. 12 + GDPR Art. 30 + AI Act Art. 12 + CRA

**NIST CSF Anchors:** PR.PS-04, PR.IR-01, PR.IR-03, PR.DS-10, DE.AE-03

**Verification Criteria (operational):**
- 7y retention audit logs; cryptographic sharding (T-002); hash chain integrity verified; ECB + AI Office inspection-ready
- Doc 07b §4 row D-10.2 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + Data Engineer (backup)

**Status:** TODO

**Dependencies:** D-04.3, D-09.4, D-05.3

**Risk if not met:** HIGH — T-002 conflict + DORA Art. 12 + GDPR Art. 30 + AI Act Art. 12

**Affected Stakeholders:** CISO, DPO, CRO, AI Gov Lead, ECB, BaFin, EDPB, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 12; GDPR Art. 30; AI Act Art. 12; ECB annual inspection

**External Auditor:** ISO 27001 + DORA + AI Act + GDPR

**Supervisory Body:** ECB JST + BaFin + EDPB + BfDI + AI Office

<a name="ag-D-10-2-002"></a>

### AG-D-10.3-002 — Compliance Testing

**Description:**

Compliance Testing is the **SG goal binding** for D-10.3 and derives from the CRA Sub-SO preserved verbatim in §1. For OmniBank Financial Systems (DORA Financial Entity, ECB-supervised, AI Act High-Risk Annex III, ISO 27001 certified, 5,000+ employees, >€1.5B), this SG goal operationalises the corpus-derived Sub-SO with the bank-tier controls specified in Doc 07b §4 example_controls column.

**Scope:** DORA Art. 24-27 testing programme (TLPT + scenario + performance + security) + AI Act Art. 43 conformity assessment + ISO 27001 surveillance + GDPR DPIA review + CRA self-declaration.

**Out of Scope:** Single test (must be 5-parallel); periodic (must be annual TLPT).

**Source Article:** DORA Art. 24-27 + AI Act Art. 43 + ISO 27001 + GDPR + CRA

**NIST CSF Anchors:** ID.RA-04, UNMAPPED_CSF, PR.PS-06, DE.CM-09

**Verification Criteria (operational):**
- Annual TLPT (ECB frequency adjustment); AI Act Art. 43 conformity before market placement; ISO 27001 surveillance; GDPR DPIA review
- KPI: Quarterly compliance review covering all 5 regulations (GDPR + CRA + NIS 2 + DORA + AI Act); documented in compliance dashboard with closure rate per BG-007 (ISO 27001 + DORA unified ISMS)
- Doc 07b §4 row D-10.3 cross-reference verified
- TEST + ANALYZE + external audit (RIGOROUS) cadence aligned with §4 verification_method column

**Verification Method:** TEST + ANALYZE + external audit (RIGOROUS)

**Owner:** CISO (primary) + CRO + AI Gov Lead (backup)

**Status:** TODO

**Dependencies:** D-02.1, D-02.4, D-09.1, D-09.2

**Risk if not met:** HIGH — missed testing obligation + DORA Art. 24-27 + AI Act Art. 43

**Affected Stakeholders:** CISO, CRO, AI Gov Lead, ECB, BaFin, ENISA, AI Office

**Maturity Score:** Current 3/4 → Target 4/4

**Implementation Priority:** CRITICAL

**Regulatory Reporting:** DORA 4h incident report; DORA Art. 26 TLPT; AI Act Art. 43; ISO 27001; GDPR DPIA

**External Auditor:** ECB-recognised TLPT provider + ISO 27001 + AI Act conformity + CRA

**Supervisory Body:** ECB JST + BaFin + AI Office + ENISA

<a name="ag-D-10-3-002"></a>


---


---

## §A.3 Alias Table — PG-D-/SG-D- (legacy) → AG-D- (corr-008 standard)

| Sub-Domain | Legacy PG-D- | Current AG-D- (slot 001) | Legacy SG-D- | Current AG-D- (slot 002) |
|------------|--------------|--------------------------|--------------|--------------------------|
| D-01.1 | PG-D-D-01.1 | AG-D-D-01.1-001 | SG-D-D-01.1 | AG-D-D-01.1-002 |
| D-01.2 | PG-D-D-01.2 | AG-D-D-01.2-001 | SG-D-D-01.2 | AG-D-D-01.2-002 |
| D-01.3 | PG-D-D-01.3 | AG-D-D-01.3-001 | SG-D-D-01.3 | AG-D-D-01.3-002 |
| D-01.4 | PG-D-D-01.4 | AG-D-D-01.4-001 | SG-D-D-01.4 | AG-D-D-01.4-002 |
| D-02.1 | PG-D-D-02.1 | AG-D-D-02.1-001 | SG-D-D-02.1 | AG-D-D-02.1-002 |
| D-02.2 | PG-D-D-02.2 | AG-D-D-02.2-001 | SG-D-D-02.2 | AG-D-D-02.2-002 |
| D-02.3 | PG-D-D-02.3 | AG-D-D-02.3-001 | SG-D-D-02.3 | AG-D-D-02.3-002 |
| D-02.4 | PG-D-D-02.4 | AG-D-D-02.4-001 | SG-D-D-02.4 | AG-D-D-02.4-002 |
| D-03.1 | PG-D-D-03.1 | AG-D-D-03.1-001 | SG-D-D-03.1 | AG-D-D-03.1-002 |
| D-03.2 | PG-D-D-03.2 | AG-D-D-03.2-001 | SG-D-D-03.2 | AG-D-D-03.2-002 |
| D-03.3 | PG-D-D-03.3 | AG-D-D-03.3-001 | SG-D-D-03.3 | AG-D-D-03.3-002 |
| D-03.4 | PG-D-D-03.4 | AG-D-D-03.4-001 | SG-D-D-03.4 | AG-D-D-03.4-002 |
| D-04.1 | PG-D-D-04.1 | AG-D-D-04.1-001 | SG-D-D-04.1 | AG-D-D-04.1-002 |
| D-04.2 | PG-D-D-04.2 | AG-D-D-04.2-001 | SG-D-D-04.2 | AG-D-D-04.2-002 |
| D-04.3 | PG-D-D-04.3 | AG-D-D-04.3-001 | SG-D-D-04.3 | AG-D-D-04.3-002 |
| D-04.4 | PG-D-D-04.4 | AG-D-D-04.4-001 | SG-D-D-04.4 | AG-D-D-04.4-002 |
| D-05.1 | PG-D-D-05.1 | AG-D-D-05.1-001 | SG-D-D-05.1 | AG-D-D-05.1-002 |
| D-05.2 | PG-D-D-05.2 | AG-D-D-05.2-001 | SG-D-D-05.2 | AG-D-D-05.2-002 |
| D-05.3 | PG-D-D-05.3 | AG-D-D-05.3-001 | SG-D-D-05.3 | AG-D-D-05.3-002 |
| D-05.4 | PG-D-D-05.4 | AG-D-D-05.4-001 | SG-D-D-05.4 | AG-D-D-05.4-002 |
| D-06.1 | PG-D-D-06.1 | AG-D-D-06.1-001 | SG-D-D-06.1 | AG-D-D-06.1-002 |
| D-06.2 | PG-D-D-06.2 | AG-D-D-06.2-001 | SG-D-D-06.2 | AG-D-D-06.2-002 |
| D-06.3 | PG-D-D-06.3 | AG-D-D-06.3-001 | SG-D-D-06.3 | AG-D-D-06.3-002 |
| D-06.4 | PG-D-D-06.4 | AG-D-D-06.4-001 | SG-D-D-06.4 | AG-D-D-06.4-002 |
| D-07.1 | PG-D-D-07.1 | AG-D-D-07.1-001 | SG-D-D-07.1 | AG-D-D-07.1-002 |
| D-07.2 | PG-D-D-07.2 | AG-D-D-07.2-001 | SG-D-D-07.2 | AG-D-D-07.2-002 |
| D-07.3 | PG-D-D-07.3 | AG-D-D-07.3-001 | SG-D-D-07.3 | AG-D-D-07.3-002 |
| D-07.4 | PG-D-D-07.4 | AG-D-D-07.4-001 | SG-D-D-07.4 | AG-D-D-07.4-002 |
| D-08.1 | PG-D-D-08.1 | AG-D-D-08.1-001 | SG-D-D-08.1 | AG-D-D-08.1-002 |
| D-08.2 | PG-D-D-08.2 | AG-D-D-08.2-001 | SG-D-D-08.2 | AG-D-D-08.2-002 |
| D-08.3 | PG-D-D-08.3 | AG-D-D-08.3-001 | SG-D-D-08.3 | AG-D-D-08.3-002 |
| D-09.1 | PG-D-D-09.1 | AG-D-D-09.1-001 | SG-D-D-09.1 | AG-D-D-09.1-002 |
| D-09.2 | PG-D-D-09.2 | AG-D-D-09.2-001 | SG-D-D-09.2 | AG-D-D-09.2-002 |
| D-09.3 | PG-D-D-09.3 | AG-D-D-09.3-001 | SG-D-D-09.3 | AG-D-D-09.3-002 |
| D-09.4 | PG-D-D-09.4 | AG-D-D-09.4-001 | SG-D-D-09.4 | AG-D-D-09.4-002 |
| D-10.1 | PG-D-D-10.1 | AG-D-D-10.1-001 | SG-D-D-10.1 | AG-D-D-10.1-002 |
| D-10.2 | PG-D-D-10.2 | AG-D-D-10.2-001 | SG-D-D-10.2 | AG-D-D-10.2-002 |
| D-10.3 | PG-D-D-10.3 | AG-D-D-10.3-001 | SG-D-D-10.3 | AG-D-D-10.3-002 |

---

**End of deprecated Appendix A file.**

For current adjusted objectives, see `../07c_Adjusted_Goals.md` §2 (Multi-Regulation Adjusted Objectives table).
