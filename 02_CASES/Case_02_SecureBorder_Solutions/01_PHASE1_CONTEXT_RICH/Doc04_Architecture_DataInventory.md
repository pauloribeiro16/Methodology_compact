---
document_id: AEGIS-P2-RICH-04a-ARCH
title: Architecture & Data Inventory (Rich Mode)
phase: 1
version: 1.2
created: 2026-07-11
updated: 2026-08-06
author: Executor (Sprint 2 Corpus Enrichment, 2026-08-06)
status: CORPUS_ENRICHED
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS 2, AI_Act]
active_subdomains: 35
inactive_documented: [D-08.3 INACTIVE, 3 NOT_ADDRESSED]
inputs:
  - 04_Company_Context_Assessment.md
  - 01_INTAKE_FORM.md
  - 05_Regulatory_Applicability.md
outputs:
  - 04b_Security_Posture.md
  - 04c_ThirdParty_Landscape.md
  - 04d_Org_Roles_RACI.md
  - 07_Structured_Compliance_Matrix.md
related_documents:
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/
  - ../../../00_METHODOLOGY/TEMPLATES/04a_Architecture_DataInventory.md
  - ../../../00_METHODOLOGY/CONTEXT/CONTEXT_PHASE1.md
supersedes: none
reconciliation:
  sprint: 1
  role: reconciliation
  base_doc: ../01_PHASE1_CONTEXT/04a_Architecture_DataInventory.md (legacy, frozen)
  notes: |
    Sprint 1 reconciliation (Case_02, 2026-08-06):
    - Frontmatter updated to AEGIS-P2-RICH-* convention (P2 = Case_02).
    - status: DRAFT → RECONCILED.
    - active_subdomains aligned to 35 (legacy declared 38, canonical for Case_02 is 35).
    - applicable_regs aligned to [GDPR, CRA, NIS 2, AI_Act] (excludes DORA per Case_02).
    - inputs/outputs references updated (../00_COMMON/01_Company_Context.md → 01_INTAKE_FORM.md).
    - Body preserved verbatim (Sprint 1 is content-neutral; Sprint 2 adds corpus linkages).
    - Sprint 2 Corpus Enrichment:
      - §3 Compliance Mapping: added "Corpus Manifest Path" + "NIST CSF Anchors" columns (38 rows enriched).
      - §4 Corpus Provenance: new section documenting the per-sub-domain manifest paths.
---

<!-- CORPUS ENRICHMENT BANNER (Sprint 2, 2026-08-06):
     This is the Rich Mode copy of AEGIS-P1-04a.
     Source: ../01_PHASE1_CONTEXT/04a_Architecture_DataInventory.md.
     Sprint 2 added: §3 "Corpus Manifest Path" + "NIST CSF Anchors" columns per sub-domain;
                     new §4 Corpus Provenance.
     See SPRINT2_ENRICHMENT_REPORT_EXISTING.md for the per-doc change list.
-->

# Architecture & Data Inventory

## 1. Technical Architecture

SecureBorder Solutions B.V. is a medium-large enterprise (450 employees, ~€120M revenue) operating in the defence/security/critical-infrastructure sector. It manufactures and operates **GuardianGate** eGate kiosks — hardware + software systems with on-board Edge AI for biometric facial verification (1:1 match), deployed at Schengen border crossings. The architecture is hybrid: Edge AI on the kiosk for biometric matching, with European-region cloud services for model updates, audit log aggregation, and the corporate back-office. Four regulations apply (GDPR, CRA, NIS 2, AI_Act), with CRA classified as **Critical Class** and the AI system classified as **Annex III (border control)**. Maturity is medium-tier: a 24/7 SOC, ISO 27001 certified, dedicated CISO, DPO, AI Governance Lead.

### 1.1 System Inventory

| System ID | Name | Type | Tech Stack | Owner | Criticality | Hosts Personal Data? |
|---|---|---|---|---|---|---|
| SYS-01 | EU Cloud Platform (AWS EU region) | Managed cloud IaaS | AWS Frankfurt region — compute, networking, KMS, IAM | CTO and Security Architecture team | Critical | Y |
| SYS-02 | National Border Control Integration | External API gateway | mTLS-secured REST/SOAP gateway to government DBs; ISO/IEC 27001 + ENS Alto certified transport | Integration Engineering Lead | Critical | Y |
| SYS-03 | Watchlist Service (Government-supplied) | External data service | Bilateral sFTP feed for judicial + immigration watchlists; HSM-bound decryption | Integration Engineering Lead | Critical | Y |
| SYS-04 | Edge AI Inference Engine (GuardianGate kiosk firmware) | Edge appliance firmware + Edge AI runtime | ARM SoC, TensorRT-accelerated CNN face match + liveness, TPM 2.0 secure boot, signed firmware | CTO and Edge AI Engineering | Critical | Y |
| SYS-05 | Cloud Model Training & Update Distribution | Managed ML platform | EU-only SageMaker-compatible training; signed model artefact registry + OTA distribution via SYS-01 | AI Governance Lead and ML Engineering | Critical | N |
| SYS-06 | GuardianGate Kiosk Hardware | Embedded system + peripherals | Industrial-grade PC + 3D camera + passport MRZ scanner + display; tamper-evident enclosure; LTE/5G failover | Hardware Engineering Lead and Field Operations | Critical | Y |
| SYS-07 | HSM Cluster (key management) | Hardware Security Module | FIPS 140-2 Level 3 HSM cluster (Thales / Utimaco) in EU; key ceremonies quarterly | CISO and Security Architecture | Critical | N (key material only) |
| SYS-08 | Enterprise SSO / IdP | Managed identity service | Okta + on-prem ADFS for EU staff; MFA mandatory (FIDO2 + TOTP fallback) | CISO | Important | Y |
| SYS-09 | SIEM + Immutable Audit Store | Security operations platform | Splunk Enterprise Security in EU region; immutable WORM storage for 10-year audit retention | SOC Manager (CISO delegation) | Critical | Y (audit metadata) |
| SYS-10 | Corporate ERP / HR / Employee Data | Enterprise application | SAP S/4HANA on SYS-01; controller-side personal data for EU staff | HR Director (DPO supervision) | Important | Y |
| SYS-11 | OTA Update Gateway + SBOM Pipeline | CI/CD + artifact pipeline | GitHub Enterprise + Jenkins + JFrog Artifactory (EU); CycloneDX SBOM emission per release; cosign-signed OTA packages | DevSecOps Lead | Critical | N |
| SYS-12 | SOC Platform (Monitoring + Incident Response) | Security operations centre tooling | Splunk ES + CrowdStrike Falcon EDR + Tenable Nessus + custom playbooks; 24/7 staffed | SOC Manager | Critical | Y (security telemetry) |
| SYS-13 | Hardware Vendor Sandbox / Test Bench | Lab environment (test only) | Isolated lab bench with reference kiosk units and supplier development kits | Hardware Engineering Lead | Supporting | N |

### 1.2 Network Topology

Kiosks (SYS-04 + SYS-06) at airport installations use vendor-managed private LTE/5G (or fibre where installed) to reach the EU Cloud Platform (SYS-01). All kiosk-to-cloud traffic is mTLS over QUIC; the kiosk maintains an outbound-only persistent channel — it does not accept inbound network connections. Government data sources (SYS-02 National Border Control, SYS-03 Watchlist) terminate on a dedicated DMZ segment with HSM-bound TLS termination; only the eGate kiosk subservice account can initiate session establishment from the inside. Cloud Model Training (SYS-05) resides in a separate AWS account segregated from the production runtime; cross-account IAM with deny-by-default egress rules. The HSM cluster (SYS-07) is in a physically secured back-office room with dual-control access (FIPS 140-2 Level 3) — only four named individuals have access badges. The SOC platform (SYS-12) consumes flow logs, EDR telemetry, audit logs and SIEM events; analysts reach it from SSO (SYS-08) with MFA + IP allow-list from the CISO office. Corporate systems (SYS-10 ERP, SYS-11 OTA, SYS-08 SSO) sit on a separate VPC from production edge-cloud workloads; peering is denied by default. Hardware lab (SYS-13) is air-gapped from production but connected to the build pipeline (SYS-11) for SBOM ingestion only.

The deployment topology intentionally aligns **production edge** (kiosks + cloud) with a **non-production** VPC (corporate + dev) and a **segregated SOC + HSM** security zone (physical access + dual control). Network controls are zero-trust, deny-by-default, with explicit named flows documented (see §2.2 below).

### 1.3 Cloud Services

| Provider | Service | Data Stored | Region | Contract Basis | DPA in Place? |
|---|---|---|---|---|---|
| AWS (EU region — eu-central-1 / eu-west-1) | EC2 / VPC / RDS / S3 / KMS (SYS-01, SYS-04 admin plane) | EU staff personal data; government-supplied watchlist cache; audit logs | Frankfurt + Dublin (EU-only) | MSA + AWS DPA (GDPR addendum) + SCCs | Y |
| Thales / Utimaco | HSM cluster (SYS-07) | Signing keys, TLS keys, biometric template encryption keys, OTA signing keys | EU on-premises | HSM-as-a-Service contract + security addendum | Y (Article 28 processor terms) |
| Okta + on-prem ADFS | Identity (SYS-08) | EU staff credentials, MFA factors, SSO metadata | EU tenant + EU datacenter | Okta subscription + DPA | Y |
| Splunk Cloud (EU) | SIEM (SYS-09, SYS-12) | Audit logs, security telemetry, EDR events | EU region | Splunk MSA + DPA + SCCs | Y |
| CrowdStrike | EDR on endpoints (SYS-12 inputs) | Endpoint telemetry, hash listings | EU region | CrowdStrike subscription + DPA | Y |
| GitHub Enterprise | Source-code repo (SYS-11) | Source code, signed artefacts, SBOM manifests | EU region | GitHub MSA + DPA | Y |
| Jenkins + JFrog Artifactory (EU-managed) | CI/CD + artefact registry (SYS-11) | Build artefacts, signed containers, OTA packages | EU on-prem | Vendor contracts + DPA | Y |
| T-Systems / Deutsche Telekom | Managed private 5G / LTE (kiosk backhaul) | Encrypted telemetry + control plane | EU networks | Carrier service contract + DPA | Y |
| National CSIRT (per country deployment) | Regulatory reporting channel (NIS 2 Art. 23) | Incident reports only | EU jurisdiction | Statutory reporting obligation — not a DPA processor relationship | N/A (statutory) |
| Government Authority Data Controllers (per country) | National Border Control API (SYS-02) | Biometric templates, passport data, match decisions | EU jurisdiction | Bilateral DPA per country + ENISA-aligned cross-border SCCs | Y |

### 1.4 Authentication & Identity Systems

| System | Purpose | MFA? | SSO? | Password Policy |
|---|---|---|---|---|
| SYS-08 Okta + ADFS | Enterprise SSO for 450 EU staff + admins + developers; FIDO2 hardware keys for privileged users | Y (FIDO2 mandatory; TOTP fallback; adaptive risk-based re-auth for high-risk actions) | Y (SAML 2.0 / OIDC across all corporate apps) | NIST SP 800-63B-compliant: 12+ chars, breached-password checks, no rotation unless compromise suspected |
| SYS-04 Kiosk firmware | Mutual TLS with SYS-02 + SYS-03; FIDO device-bound credentials stored in TPM 2.0 for kiosk admin | Y (certificate-based; hardware-backed via TPM) | n/a (kiosk authenticates outbound) | mTLS certificates rotated quarterly via internal CA chain; revocation via OCSP |
| SYS-07 HSM cluster | Hardware-backed signing keys for OTA, audit log integrity, biometric template encryption | Y (dual-control key ceremony; FIDO2 admin keys) | n/a (on-prem; AD-bridged RBAC only) | FIPS 140-2 Level 3; key access logged in SIEM |
| SYS-12 SOC tooling | SOC analysts + IR Lead + CISO + DPO access (least privilege per role) | Y (FIDO2) | Y (via SYS-08 Okta) | Per SYS-08 policy; additional IP allow-list from CISO office only |

## 2. Data Inventory

### 2.1 Data Stores

| Store ID | Type | Location | System | Encryption at Rest? | Owner | Retention Period | Backup? |
|---|---|---|---|---|---|---|---|
| STORE-01 | RDS PostgreSQL (EU staff + operational data) | EU cloud region (eu-central-1) | SYS-01 | Y, AES-256 KMS-managed with customer-managed keys (CMK) bound to SYS-07 HSM | CISO and Security Architecture | Active employment + 7 years (per NL labour law + tax retention) | Y (encrypted, cross-region; tested quarterly) |
| STORE-02 | S3 object storage (audit logs, model artefacts, OTA packages) | EU cloud region (eu-central-1 + eu-west-1 cross-region replication) | SYS-01 + SYS-09 + SYS-11 | Y, SSE-KMS AES-256 with CMK from SYS-07 HSM; immutable WORM buckets for audit | SOC Manager + DevSecOps Lead | Audit logs: 10 years (immutable); OTA packages: lifetime of product + 5 years post-EOL; model artefacts: lifetime of model version | Y (cross-region + immutable) |
| STORE-03 | Watchlist cache (encrypted, isolated) | Dedicated secure partition of SYS-01 | SYS-01 + SYS-03 | Y, AES-256 with HSM-bound CMK; isolated VPC subnetwork; air-gap-style ingress controls (only SYS-02 + SYS-04 read endpoints) | Integration Engineering Lead + CISO | Per government policy (mirrored 1:1 from controller source; deleted on contract end) | N (data lives at controller — local cache is contingency only) |
| STORE-04 | Audit log WORM store (immutable, signature-chained) | SYS-09 SIEM | SYS-09 | Y, AES-256 KMS + cryptographic hash chaining (each entry signed by HSM key); tamper-evident | SOC Manager | 10 years (NIS 2 + GDPR + national archival requirements) | Y (cross-region immutable; WORM bucket) |
| STORE-05 | Biometric template cache (transient, on-kiosk only) | SYS-06 kiosk local encrypted flash | SYS-04 firmware + SYS-06 hardware | Y, AES-256 with HSM-bound key; no persistence across reboot; deleted within seconds post-match per Art. 5(1)(c) data minimisation | CTO and Edge AI Engineering | Seconds-to-minutes (match window only); immediate purge after decision recorded | N (intentional — minimisation by design) |
| STORE-06 | Okta identity store (EU staff credentials) | Okta EU tenant | SYS-08 | Y, Okta-managed AES-256 | CISO | Active employment + 90 days post-termination; biometric factors: 30 days post-termination | Y (Okta-managed, cross-tenant encrypted) |
| STORE-07 | Corporate ERP / HR data (SAP) | EU cloud region | SYS-10 | Y, AES-256 KMS with HSM-bound CMK; field-level encryption for sensitive PII (salary, BSN-equivalent identifiers) | HR Director + DPO supervision | Active employment + 7 years (per NL retention obligations); tax-relevant items: 10 years | Y (encrypted cross-region quarterly) |

### 2.2 Data Flows

| Flow ID | Source | Destination | Data Type | Volume | Encryption in Transit? | Protocol | Subprocessor? |
|---|---|---|---|---|---|---|---|
| FLOW-01 | Kiosk (SYS-04/SYS-06) | Government Border Control API (SYS-02) | Passport MRZ data + encrypted biometric probe (1:1 verification request) | Medium (variable; surges at peak hours) | Y, mTLS over QUIC; client cert from TPM 2.0 | mTLS + custom REST over QUIC | N (SecureBorder is processor for government authority — government authority is controller) |
| FLOW-02 | Kiosk (SYS-04/SYS-06) | National Watchlist Service (SYS-03) | Encrypted watchlist probe (subject identifier only; no name/birthdate exposed beyond minimum) | Medium | Y, mTLS over private 5G/LTE; HSM-bound session keys | mTLS + bilateral REST | Y (government watchlist provider; subprocessor relationship per government DPA) |
| FLOW-03 | Kiosk (SYS-04/SYS-06) | Cloud Audit Sink (SYS-09 store STORE-04) | Audit event: timestamp + decision outcome + edge node ID (no biometric data, no PII content) | Low-medium | Y, mTLS over QUIC | mTLS + HTTPS | Y (Splunk Cloud EU subprocessor) |
| FLOW-04 | Cloud Model Training (SYS-05) | Kiosk OTA (SYS-04) | Signed model artefact (cosign signature; CycloneDX SBOM attached) | Low (periodic; 1-4 per quarter) | Y, mTLS + signed packages; signature verified in TPM | mTLS + signed OTA via SYS-11 pipeline | Y (AWS S3 subprocessor for artefact hosting) |
| FLOW-05 | Kiosk Syslog/EDR agent (SYS-04 EDR) | CrowdStrike cloud (SYS-12 inputs) | Endpoint telemetry, process hashes, network connection metadata | Low-medium | Y, TLS 1.3 | HTTPS | Y (CrowdStrike subprocessor) |
| FLOW-06 | Developer workstation | GitHub Enterprise (SYS-11 source code repo) | Source code, signed commits, SBOM contributions | Low | Y, TLS 1.3 with FIDO2 MFA at session level | HTTPS + SSH + signed commits | Y (GitHub subprocessor for hosted Git) |
| FLOW-07 | CI/CD pipeline (SYS-11 Jenkins) | JFrog Artifactory (SYS-11) | Signed build artefacts, vulnerability scan results, SBOMs | Low | Y, mTLS internal | mTLS | N (self-hosted Artifactory; not a subprocessor) |
| FLOW-08 | EU staff end-user device | Okta SSO (SYS-08) | Username, MFA factor (FIDO2); session tokens | Low-medium | Y, TLS 1.3 | HTTPS + SAML/OIDC | N (Okta in-scope as processor; DPA in place) |
| FLOW-09 | Splunk SIEM (SYS-09) | CrowdStrike + Tenable feeds (SYS-12) | Security telemetry enrichment, threat intel feeds | Low | Y, TLS 1.3 | HTTPS | Y (CrowdStrike + Tenable subprocessors) |
| FLOW-10 | Regulatory reporting (SecureBorder CISO → SOC → regulator) | National CSIRT + Government Authority (per country) | Incident reports (NIS 2 Art. 23(4) 24h early warning; CRA Art. 14(1); AI_Act Art. 73) | Very low (event-driven) | Y, TLS 1.3 + signed PDF or structured JSON | HTTPS + email + secure government portal (per jurisdiction) | N (statutory reporting — no processor relationship) |
| FLOW-11 | Kiosk biometric enrolment (system-initiated, controller-supplied) | SYS-04 firmware (transient cache) | Encrypted biometric template from controller for verification only | Low (per session) | Y, mTLS + TLS 1.3 internal | mTLS | Y (controller-supplied enrolment data; subprocessor relationship per government DPA) |
| FLOW-12 | EU staff HR record maintenance | SYS-10 SAP | Employment contract data, performance records, tax-relevant identifiers | Low | Y, TLS 1.3 internal VPC + encrypted field-level PII | HTTPS (over corporate VPC) | N (self-managed SAP on SYS-01) |

### 2.3 Personal Data Categories

| Category | Legal Basis (Art. 6 GDPR + Art. 9 if applicable) | Systems Processing | Retention | Erasure Mechanism |
|---|---|---|---|---|
| **Facial biometric templates (Art. 9)** | Art. 9(2)(g) — substantial public interest (government contract for border control) | SYS-04 + SYS-06 (transient cache only; deleted seconds after match) | Seconds to minutes (per match window); no cross-session persistence | Automatic immediate purge after match (Art. 5(1)(c) data minimisation by design) |
| **Passport MRZ data (Art. 6/9 if biometric data extracted)** | Art. 6(1)(c) — legal obligation; Art. 9(2)(g) for biometric components | SYS-04 + SYS-02 (controller-side); syslog to STORE-04 audit | Per government authority policy (varies by country; typically deleted post-match) | Controller-side deletion via SYS-02 API; SecureBorder-side cache purged per minimisation policy |
| **Watchlist data (Art. 6 — government-supplied)** | Art. 6(1)(c) and (e) — legal obligation + public interest | SYS-03 (controller-supplied) + STORE-03 (cache) | Per government policy; cached for performance only | Controller-side deletion via SYS-03 feed; SecureBorder cache deleted per SLA |
| **Match decision audit events (no biometric content)** | Art. 6(1)(c) — legal obligation; Art. 9(2)(g) for special-category metadata | SYS-04 + SYS-09 (STORE-04 immutable WORM) | 10 years (legal + NIS 2 + national archival) | Not erased during retention period; thereafter destroyed via WORM bucket lifecycle |
| **EU staff employment records (Art. 6 + Art. 9 if health data)** | Art. 6(1)(b) contract performance; Art. 9(2)(b) for health where relevant | SYS-10 SAP + STORE-07 | 7 years (employment + tax) per NL law; 10 years where tax-relevant | HR-led deletion per retention schedule; DPO oversight |
| **EU staff credentials (Art. 6 — legitimate interest + contract)** | Art. 6(1)(b) — contract performance | SYS-08 + STORE-06 | Active employment + 90 days post-termination | Okta admin workflow + audit log entry |
| **Investigator/alleged subject access requests (Art. 15-22)** | Art. 6(1)(c) — legal obligation | SYS-09 audit + SYS-08 SSO for DPO workflow | Per Art. 12 GDPR — 30 days standard; complex 60 days | DPO + CISO coordinated deletion; audit of deletion itself |
| **Endpoint telemetry / SOC signals** | Art. 6(1)(f) — legitimate interest (security) | SYS-12 + CrowdStrike + Splunk | 13 months (Splunk retention policy); 10 years for security-relevant audit entries | Splunk lifecycle policy; SIEM retention controls |

### 2.4 Data Subject Categories

| Subject Type | Data Categories | Access Mechanism | Erasure Mechanism |
|---|---|---|---|
| **Schengen travellers (data subjects; controller = government)** | Passport MRZ, facial biometric template (transient), match decision audit metadata | Subject exercises rights via the controlling government authority (e.g., border police agency); SecureBorder responds to controller instructions only | Controller-driven; SecureBorder deletes from transient cache automatically per minimisation |
| **EU employees** | Employment records, performance, salaries, benefits, training records | Employee self-service portal (subset) + HR workflow + DPO escalation | HR-driven per retention schedule; DPO oversight for special-category data |
| **Job applicants** | CV, interview notes, references | HR workflow + DPO workflow | Auto-purge 4 weeks after close (if rejected); longer if consented |
| **External contractors / vendors** | Contract details, access logs (building + system), payment metadata | Procurement + admin workflow | Per contract terms + 7-year tax retention |
| **Visitors (site visits to HQ / lab)** | Name, ID document copy, sign-in timestamp | Reception + security desk | Auto-purge after 30 days (per visitor policy) |
| **Whistleblowers / ethics channel users** | Identity (may be confidential), report content | Confidential ethics portal; DPO + Legal access only | Per investigation closure + 7-year retention of investigation record (anonymised if identity disclosed) |

## 3. Compliance Mapping (Regulatory Baseline)

This mapping uses SecureBorder's `applicable_regs = [GDPR, CRA, NIS 2, AI_Act]`. The Regulatory Baseline source of truth is `00_METHODOLOGY/PREPROCESSING/SubDomains/`. All 38 sub-domains are ACTIVE because 4 regulations apply (no sub-domain has zero intersection with the participating regulations). The 3 sub-domains that appear in DORA only (D-07.2, D-07.4, D-09.3) are ACTIVE via ISO 27001 best-practice coverage and CIS Critical Security Controls inheritance — they are flagged in this document as "DORA-exclusive, ISO 27001-derived".

| Sub-domain | Relevant Systems | Relevant Data Stores | Relevant Data Flows | Regulatory Baseline Requirement IDs | SubDomains file | Corpus Manifest Path | NIST CSF Anchors |
|---|---|---|---|---|---|---|---|
|  D-01.1 Data at Rest Encryption  |  SYS-01, SYS-04, SYS-06, SYS-07, SYS-09, SYS-10  |  STORE-01, STORE-02, STORE-03, STORE-04, STORE-05, STORE-07  |  FLOW-01, FLOW-11, FLOW-12  |  1.1; 1.1.1, 1.1.2, 1.1.3, 1.1.4  |  [D-01.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.1.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.manifest.json | PR.DS-01, PR.DS-10, GV.RM-04, PR.DS-02 |
|  D-01.2 Data in Transit Encryption  |  SYS-01, SYS-02, SYS-03, SYS-04, SYS-08, SYS-09, SYS-11  |  (n/a — encryption in transit refers to FLOW-)  |  FLOW-01, FLOW-02, FLOW-03, FLOW-04, FLOW-05, FLOW-06, FLOW-07, FLOW-08, FLOW-11, FLOW-12  |  1.2; 1.2.1, 1.2.2, 1.2.3  |  [D-01.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.2.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.2/D-01.2.manifest.json | PR.DS-02, PR.IR-01 |
|  D-01.3 Key Management  |  SYS-07 HSM, SYS-01 KMS  |  STORE-01, STORE-02, STORE-04  |  FLOW-04, FLOW-07, FLOW-11  |  1.3; 1.3.1, 1.3.2, 1.3.3  |  [D-01.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.3.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.3/D-01.3.manifest.json | PR.DS-01, PR.IR-03, GV.OV-01, PR.AA-05 |
|  D-01.4 Data Integrity Mechanisms  |  SYS-04, SYS-09 (STORE-04 hash-chained), SYS-11 (signed artefacts)  |  STORE-04, STORE-02  |  FLOW-04, FLOW-07  |  1.4; 1.4.1, 1.4.2, 1.4.3, 1.4.4  |  [D-01.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.4.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.4/D-01.4.manifest.json | PR.DS-01, PR.DS-10, PR.DS-12, PR.PS-04, PR.DS-11, PR.IR-03, PR.IR-04 |
|  D-02.1 Vulnerability Identification  |  SYS-04, SYS-11, SYS-12 (Tenable Nessus)  |  STORE-02  |  FLOW-09  |  2.1; 2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5  |  [D-02.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.1.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.1/D-02.1.manifest.json | ID.IM-02, ID.RA-01, ID.RA-05, PR.PS-02, PR.PS-02; ID.RA-05, ID.AM-02, GV.SC-04, GV.RM-01, GV.RM-06, ID.RA-03, ID.RA-04, ID.RA-06, ID.RA-06; PR.PS-06; RS.MI-01, PR.PS-06, RS.MA-03, RS.MI-01 |
|  D-02.2 Patch Management  |  SYS-04 firmware, SYS-11 OTA pipeline  |  STORE-02  |  FLOW-04  |  2.2; 2.2.1, 2.2.2  |  [D-02.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.2.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.2/D-02.2.manifest.json | GV.OV-02, ID.RA-01, ID.RA-06, PR.IR-03, PR.IR-03; ID.RA-01; PR.PS-01, PR.PS-01, PR.PS-02 |
|  D-02.3 Coordinated Vulnerability Disclosure  |  SYS-01 corporate website, ENISA CVD hub  |  (n/a — policy artifact)  |  (n/a — inbound disclosure channel)  |  2.3; 2.3.1, 2.3.2  |  [D-02.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.3.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.3/D-02.3.manifest.json | GV.PO-01, GV.SC-04, RS.CO-03, ID.RA-01 |
|  D-02.4 Threat-Led Penetration Testing  |  SYS-04, SYS-06, SYS-01 cloud production  |  STORE-04  |  FLOW-01, FLOW-03  |  2.4; 2.4.1, 2.4.2, 2.4.3  |  [D-02.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.4.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.4/D-02.4.manifest.json | DE.CM-09, ID.RA-01, PR.PS-06, GV.SC-04, ID.RA-04 |
|  D-03.1 Identity Lifecycle Management  |  SYS-08 Okta, SYS-07 HSM, SYS-04 firmware TPM  |  STORE-06  |  FLOW-08  |  3.1; 3.1.1, 3.1.2, 3.1.3, 3.1.4  |  [D-03.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.1.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.1/D-03.1.manifest.json | PR.AA-02, PR.AA-03, PR.DS-12, DE.CM-09, ID.AM-01, PR.AA-01, PR.AA-05, PR.AA-06, PR.AT-02 |
|  D-03.2 Multi-Factor Authentication  |  SYS-08, SYS-07, SYS-04 TPM  |  STORE-06  |  FLOW-08  |  3.2; 3.2.1, 3.2.2, 3.2.3, 3.2.4  |  [D-03.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.2.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.2/D-03.2.manifest.json | PR.AA-05, PR.AA-06, PR.AT-02, DE.CM-09, ID.AM-01, PR.AA-01, PR.AA-03, PR.DS-02, PR.IR-03 |
|  D-03.3 Authorisation & Least Privilege  |  SYS-08 RBAC, SYS-01 IAM, SYS-12 SOC roles  |  STORE-01, STORE-04, STORE-06  |  FLOW-03, FLOW-08, FLOW-09  |  3.3; 3.3.1, 3.3.2, 3.3.3, 3.3.4  |  [D-03.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.3.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.3/D-03.3.manifest.json | PR.AA-05, PR.AA-06, PR.AT-02, DE.CM-09, ID.AM-01, PR.AA-01, PR.PS-04, ID.AM-02 |
|  D-03.4 Secure System Defaults  |  SYS-04 (hardware secure boot), SYS-01 (cloud baselines)  |  STORE-04  |  FLOW-03  |  3.4; 3.4.1, 3.4.2  |  [D-03.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.4.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.4/D-03.4.manifest.json | GV.PO-01, PR.DS-12, PR.PS-01, GV.SC-03 |
|  D-04.1 Incident Detection & Triage  |  SYS-12 (SIEM + EDR + IDS), SYS-09 correlation rules  |  STORE-04  |  FLOW-03, FLOW-05, FLOW-09  |  4.1; 4.1.1, 4.1.2, 4.1.3, 4.1.4  |  [D-04.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.1.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.1/D-04.1.manifest.json | DE.AE-02, DE.CM-01, DE.CM-09, PR.PS-04, RS.MA-02, RS.MA-01 |
|  D-04.2 Containment & Mitigation  |  SYS-12 IR playbooks, SYS-04 firmware quarantine  |  STORE-04  |  FLOW-03, FLOW-09  |  4.2; 4.2.1, 4.2.2, 4.2.3, 4.2.4  |  [D-04.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.2.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.2/D-04.2.manifest.json | PR.DS-01, PR.DS-12, PR.IR-04, RC.RP-04, RS.MI-01, RS.MI-02, DE.CM-09, PR.IR-03, RC.RP-01 |
|  D-04.3 Regulatory Notification  |  SOC + CISO + DPO + AI Governance Lead  |  STORE-04  |  FLOW-10  |  4.3; 4.3.1, 4.3.2, 4.3.3, 4.3.4, 4.3.5  |  [D-04.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.3.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/D-04.3.manifest.json | RS.CO-02, RS.CO-04, RS.MA-03, RS.AN-03, RS.AN-07, RS.MA-02, RS.MA-01 |
|  D-04.4 Data Restoration & Recovery  |  SYS-01 backups, SYS-09 immutable, SYS-02 contract continuity  |  STORE-01, STORE-02, STORE-04  |  (restoration flows, internal to SYS-01)  |  4.4; 4.4.1, 4.4.2, 4.4.3, 4.4.4  |  [D-04.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.4.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.4/D-04.4.manifest.json | PR.DS-11, PR.IR-04, RC.RP-04, PR.DS-12, PR.IR-03 |
|  D-05.1 Data Minimisation  |  SYS-04 firmware (transient cache purge), SYS-06 (hardware-locked TTL)  |  STORE-05 (transient)  |  FLOW-01, FLOW-11  |  5.1; 5.1.1, 5.1.2, 5.1.3  |  [D-05.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.1.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.1/D-05.1.manifest.json | GV.OC-03, GV.PO-01, ID.AM-03, PR.DS-12, PR.DS-01, PR.PS-06 |
|  D-05.2 Retention & Archiving  |  SYS-09 WORM bucket, SYS-10 retention engine  |  STORE-04, STORE-07  |  FLOW-12  |  5.2; 5.2.1, 5.2.2, 5.2.3  |  [D-05.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.2.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.2/D-05.2.manifest.json | ID.AM-03, PR.DS-12, GV.OC-04, GV.OV-02, PR.PS-02, GV.PO-02, PR.PS-04 |
|  D-05.3 Right to Erasure  |  DPO workflow, SYS-10 HR deletion, SYS-09 audit redaction policy  |  STORE-04, STORE-06, STORE-07  |  (deletion flows, internal)  |  5.3; 5.3.1, 5.3.2  |  [D-05.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.3.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.3/D-05.3.manifest.json | GV.SC-04, PR.DS-10, PR.DS-12, PR.DS-12 (+ PR.DS-02 for the second limb) |
|  D-05.4 Data Portability  |  (n/a — SecureBorder is processor for traveller data)  |  (controller-side, not within SecureBorder scope)  |  (n/a for data subject portability — traveller requests go to government)  |  5.4; 5.4.1  |  [D-05.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.4.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.4/D-05.4.manifest.json | PR.DS-10, PR.DS-12 |
|  D-06.1 Vendor Risk Assessment  |  All SYS with subprocessors; SYS-11 SBOM  |  (n/a)  |  FLOW-04, FLOW-05, FLOW-09  |  6.1; 6.1.1, 6.1.2, 6.1.3, 6.1.4  |  [D-06.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.1.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/D-06.1.manifest.json | GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, GV.SC-01, ID.RA-02, GV.OC-03, ID.RA-01 |
|  D-06.2 Software Bill of Materials  |  SYS-11 (CycloneDX per release)  |  STORE-02  |  FLOW-04, FLOW-07  |  6.2; 6.2.1  |  [D-06.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.2.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.2/D-06.2.manifest.json | GV.SC-02, GV.SC-03, ID.AM-02 |
|  D-06.3 Contractual Security Obligations  |  All vendor contracts; Art. 28 DPA; CRA Annex I Part I (2)(h) clauses; NIS 2 supply chain clauses  |  (n/a — paper artefacts)  |  (n/a — contractual)  |  6.3; 6.3.1, 6.3.2, 6.3.3, 6.3.4  |  [D-06.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.3.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/D-06.3.manifest.json | GV.OC-03, GV.SC-02, GV.SC-03, GV.SC-04, PR.DS-12, RS.CO-04, RS.MI-01, ID.AM-04, ID.RA-01, ID.RA-02, PR.PS-06 |
|  D-06.4 Third-Party Boundary Management  |  SYS-01, SYS-04, SYS-08, SYS-09, SYS-12  |  STORE-01, STORE-04  |  FLOW-04, FLOW-05, FLOW-06, FLOW-07, FLOW-09  |  6.4; 6.4.1, 6.4.2, 6.4.3, 6.6.4  |  [D-06.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.4.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.4/D-06.4.manifest.json | GV.OC-02, GV.RR-02, GV.OC-03, GV.SC-02, GV.SC-03, GV.SC-04, GV.SC-05, ID.AM-04, ID.RA-02, RS.CO-04 |
|  D-07.1 Secure-by-Design Principles  |  SYS-04 firmware dev, SYS-11 pipeline, SYS-05 ML pipeline  |  (n/a)  |  (n/a — design-time artefact)  |  7.1; 7.1.1, 7.1.2, 7.1.3, 7.1.4, 7.1.5  |  [D-07.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.1.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/D-07.1.manifest.json | PR.DS-12, PR.PS-06, PR.PS-01, PR.PS-02, ID.RA-01 |
|  D-07.2 Secure Coding Practices **DORA-exclusive; ISO 27001-derived**  |  SYS-04, SYS-11, SYS-05  |  (n/a)  |  (n/a — code-review artefact)  |  7.2; 7.2.1, 7.2.2, 7.2.3  |  [D-07.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.2.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.2/D-07.2.manifest.json (NOT_ADDRESSED) | PR.PS-02, PR.PS-06, ID.RA-01 |
|  D-07.3 CI/CD Pipeline Security  |  SYS-11 (Jenkins + JFrog + cosign)  |  STORE-02  |  FLOW-07  |  7.3; 7.3.1, 7.3.2  |  [D-07.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.3.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.3/D-07.3.manifest.json | PR.PS-02, PR.PS-06, ID.RA-01 |
|  D-07.4 Change Management **DORA-exclusive; ISO 27001-derived**  |  SYS-11 release pipeline, SYS-04 firmware update  |  STORE-02  |  FLOW-04, FLOW-07  |  7.4; 7.4.1, 7.4.2  |  [D-07.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.4.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.4/D-07.4.manifest.json (NOT_ADDRESSED) | GV.OV-01, GV.OV-02, GV.PO-02, GV.SC-04, ID.IM-04, PR.PS-02 |
|  D-08.1 General Security Awareness  |  All staff (450) — security awareness programme  |  (n/a — LMS)  |  (n/a)  |  8.1; 8.1.1, 8.1.2, 8.1.3, 8.1.4  |  [D-08.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.1.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.1/D-08.1.manifest.json | PR.AT-01, PR.AT-02, PR.PS-01 |
|  D-08.2 Role-Specific Competence  |  All staff + developers + SOC + AI team — role-specific training  |  (n/a — LMS)  |  (n/a)  |  8.2; 8.2.1, 8.2.2, 8.2.3, 8.2.4, 8.2.5  |  [D-08.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.2.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.2/D-08.2.manifest.json | PR.AT-01, PR.AT-02, GV.SC-03, PR.AT-04, GV.RR-01, GV.RR-02, GV.RR-04, PR.AT-03 |
|  D-08.3 Management Board Training **NIS 2-applicable; ACTIVE for SecureBorder**  |  Management Board (CEO + CTO + CISO + Non-Exec Directors)  |  (n/a — governance artefact)  |  (n/a)  |  8.3; 8.3.1, 8.3.2  |  [D-08.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.3.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.3/D-08.3.manifest.json | GV.RR-01, PR.AT-03 |
|  D-09.1 Information Security Policies  |  All production systems (ISO 27001 policy set v4.7)  |  (n/a — paper artefact)  |  (n/a)  |  9.1; 9.1.1, 9.1.2, 9.1.3, 9.1.4, 9.1.5  |  [D-09.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.1.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/D-09.1.manifest.json | GV.OV-03, GV.PO-01, GV.PO-01 (primary), GV.PO-02, GV.RM-04, GV.RR-01, GV.RR-02, GV.RR-03, GV.OC-03, GV.SC-01, GV.SC-04, GV.OV-01, GV.RM-05, GV.OC-04, GV.RM-01 |
|  D-09.2 Impact & Risk Assessments  |  DPIA + FRIA + NIS 2 risk assessment + AI_Act risk management  |  (n/a — paper artefact)  |  (n/a)  |  9.2; 9.2.1, 9.2.2, 9.2.3, 9.2.4, 9.2.5  |  [D-09.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.2.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/D-09.2.manifest.json | ID.RA-04, ID.RA-05, ID.RA-05 (primary), ID.SC-04, GV.OV-01, GV.RM-04 |
|  D-09.3 Asset Inventories **DORA-exclusive; ISO 27001-derived**  |  SYS-01..SYS-13 inventory maintained in CMDB  |  (n/a — paper artefact)  |  (n/a)  |  9.3; 9.3.1, 9.3.2, 9.3.3  |  [D-09.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.3.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/D-09.3.manifest.json (NOT_ADDRESSED) | ID.AM-01, ID.AM-02, PR.PS-01, PR.PS-01 (primary) |
|  D-09.4 Records of Processing  |  DPIA register, FRIA register, RoPA, Annex VII documentation  |  (n/a — paper + tooling artefact)  |  (n/a)  |  9.4; 9.4.1, 9.4.2, 9.4.3, 9.4.4, 9.4.5  |  [D-09.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.4.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/D-09.4.manifest.json | GV.PO-02, ID.AM-08, ID.AM-08 (primary), PR.DS-12, ID.RA-05, GV.PO-01 |
|  D-10.1 Continuous Security Monitoring  |  SYS-12 SIEM, SYS-04 EDR, SYS-11 build pipeline monitoring  |  STORE-04  |  FLOW-03, FLOW-05, FLOW-09  |  10.1; 10.1.1, 10.1.2, 10.1.3, 10.1.4, 10.1.5  |  [D-10.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.1.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/D-10.1.manifest.json | DE.AE-02, DE.CM-01, DE.CM-01 (primary), DE.CM-09, ID.IM-04, DE.CM-09 (primary), GV.OV-03 |
|  D-10.2 Audit Logging & Traceability  |  SYS-09 (STORE-04), SYS-08 Okta audit, SYS-12 SOC logs  |  STORE-04  |  FLOW-03, FLOW-09  |  10.2; 10.2.1, 10.2.2, 10.2.3, 10.2.4  |  [D-10.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.2.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/D-10.2.manifest.json | DE.CM-01, GV.PO-02, PR.DS-11, PR.DS-11 (primary), PR.PT-01, ID.RA-04, PR.IP-06, DE.AE-03, DE.CM-09, PR.PS-04, PR.PS-04 (primary), RC.RP-03 |
|  D-10.3 Compliance Testing  |  Internal audit team, external auditor  |  (n/a — paper artefact)  |  (n/a)  |  10.3; 10.3.1, 10.3.2, 10.3.3, 10.3.4, 10.3.5  |  [D-10.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.3.md)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/D-10.3.manifest.json | DE.AE-02, GV.OV-03, ID.RA-05, PR.IP-07, PR.IP-07 (primary), PR.PS-04 |

## 4. Corpus Provenance

Every active sub-domain row in §3 is enriched with two corpus linkage columns. The **Corpus Manifest Path** column links to the per-sub-domain manifest JSON (`applicable_articles_by_regulation`, `applicable_clauses_by_regulation`, `applicable_nist_controls_by_regulation`, `sub_requirements_by_regulation`); the **NIST CSF Anchors** column lists the unique NIST CSF 2.0 subcategories aggregated across Case_02's four applicable regulations (GDPR + CRA + NIS 2 + AI_Act), filtered out of any DORA-exclusive anchors.

### 4.1 Per-sub-domain manifest path index

| Sub-domain | Sub-domain name | Status | Manifest path | Articles folder |
|---|---|---|---|---|
| D-01.1 | Data at Rest Encryption | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/articles` (22 files) |
| D-01.2 | Data in Transit Encryption | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.2/D-01.2.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.2/articles` (12 files) |
| D-01.3 | Cryptographic Key Management | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.3/D-01.3.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.3/articles` (13 files) |
| D-01.4 | Data Integrity Mechanisms | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.4/D-01.4.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.4/articles` (19 files) |
| D-02.1 | Vulnerability Identification | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.1/D-02.1.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.1/articles` (26 files) |
| D-02.2 | Patch Management & Updates | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.2/D-02.2.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.2/articles` (17 files) |
| D-02.3 | Coordinated Vulnerability Disclosure | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.3/D-02.3.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.3/articles` (6 files) |
| D-02.4 | Threat-Led Penetration Testing | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.4/D-02.4.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.4/articles` (8 files) |
| D-03.1 | Identity Lifecycle Management | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.1/D-03.1.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.1/articles` (21 files) |
| D-03.2 | Multi-Factor Authentication | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.2/D-03.2.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.2/articles` (6 files) |
| D-03.3 | Authorisation & Least Privilege | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.3/D-03.3.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.3/articles` (11 files) |
| D-03.4 | Secure System Defaults | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.4/D-03.4.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.4/articles` (9 files) |
| D-04.1 | Incident Detection & Triage | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.1/D-04.1.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.1/articles` (19 files) |
| D-04.2 | Incident Containment & Response | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.2/D-04.2.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.2/articles` (19 files) |
| D-04.3 | Incident Notification & Reporting | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/D-04.3.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/articles` (56 files) |
| D-04.4 | Incident Recovery & Lessons Learned | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.4/D-04.4.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.4/articles` (14 files) |
| D-05.1 | Data Minimisation | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.1/D-05.1.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.1/articles` (16 files) |
| D-05.2 | Retention & Archiving | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.2/D-05.2.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.2/articles` (9 files) |
| D-05.3 | Right to Erasure | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.3/D-05.3.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.3/articles` (10 files) |
| D-05.4 | Data Portability | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.4/D-05.4.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.4/articles` (3 files) |
| D-06.1 | Vendor Risk Assessment | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/D-06.1.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/articles` (10 files) |
| D-06.2 | Software Bill of Materials (SBOM) | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.2/D-06.2.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.2/articles` (2 files) |
| D-06.3 | Contractual Security Obligations | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/D-06.3.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/articles` (28 files) |
| D-06.4 | Third-Party Boundary Management | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.4/D-06.4.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.4/articles` (15 files) |
| D-07.1 | Secure-by-Design Principles | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/D-07.1.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/articles` (21 files) |
| D-07.2 | Secure Coding Practices | NOT_ADDRESSED | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.2/D-07.2.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.2/articles` (4 files) |
| D-07.3 | CI/CD Pipeline Security | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.3/D-07.3.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.3/articles` (6 files) |
| D-07.4 | Change Management | NOT_ADDRESSED | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.4/D-07.4.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.4/articles` (7 files) |
| D-08.1 | General Security Awareness | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.1/D-08.1.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.1/articles` (16 files) |
| D-08.2 | Role-Specific Competence | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.2/D-08.2.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.2/articles` (14 files) |
| D-08.3 | Management Board Training | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.3/D-08.3.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.3/articles` (4 files) |
| D-09.1 | Information Security Policies | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/D-09.1.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/articles` (57 files) |
| D-09.2 | Impact & Risk Assessments | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/D-09.2.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/articles` (25 files) |
| D-09.3 | Asset Inventories | NOT_ADDRESSED | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/D-09.3.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/articles` (11 files) |
| D-09.4 | Records of Processing | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/D-09.4.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/articles` (27 files) |
| D-10.1 | Continuous Security Monitoring | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/D-10.1.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/articles` (25 files) |
| D-10.2 | Audit Logging & Traceability | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/D-10.2.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/articles` (18 files) |
| D-10.3 | Compliance Testing | ACTIVE | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/D-10.3.manifest.json` | `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/articles` (17 files) |

### 4.2 Aggregate counts (Case_02 applicable regs only)

| Macro-domain | Active sub-domains | NIST CSF anchors (Case_02) |
|---|---:|---|
| D-01 (D-01 Data Protection & Encryption) | 4 | PR.DS-01, PR.DS-10, GV.RM-04, PR.DS-02, PR.IR-01, PR.IR-03, GV.OV-01, PR.AA-05, PR.DS-12, PR.PS-04, PR.DS-11, PR.IR-04 |
| D-02 (D-02 Vulnerability Management) | 4 | ID.IM-02, ID.RA-01, ID.RA-05, PR.PS-02, PR.PS-02; ID.RA-05, ID.AM-02, GV.SC-04, GV.RM-01, GV.RM-06, ID.RA-03, ID.RA-04, ID.RA-06, ID.RA-06; PR.PS-06; RS.MI-01, PR.PS-06, RS.MA-03, RS.MI-01, GV.OV-02, PR.IR-03, PR.IR-03; ID.RA-01; PR.PS-01, PR.PS-01, GV.PO-01, RS.CO-03, DE.CM-09 |
| D-03 (D-03 Access Control) | 4 | PR.AA-02, PR.AA-03, PR.DS-12, DE.CM-09, ID.AM-01, PR.AA-01, PR.AA-05, PR.AA-06, PR.AT-02, PR.DS-02, PR.IR-03, PR.PS-04, ID.AM-02, GV.PO-01, PR.PS-01, GV.SC-03 |
| D-04 (D-04 Incident Response) | 4 | DE.AE-02, DE.CM-01, DE.CM-09, PR.PS-04, RS.MA-02, RS.MA-01, PR.DS-01, PR.DS-12, PR.IR-04, RC.RP-04, RS.MI-01, RS.MI-02, PR.IR-03, RC.RP-01, RS.CO-02, RS.CO-04, RS.MA-03, RS.AN-03, RS.AN-07, PR.DS-11 |
| D-05 (D-05 Data Lifecycle) | 4 | GV.OC-03, GV.PO-01, ID.AM-03, PR.DS-12, PR.DS-01, PR.PS-06, GV.OC-04, GV.OV-02, PR.PS-02, GV.PO-02, PR.PS-04, GV.SC-04, PR.DS-10, PR.DS-12 (+ PR.DS-02 for the second limb) |
| D-06 (D-06 Supply Chain) | 4 | GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, GV.SC-01, ID.RA-02, GV.OC-03, ID.RA-01, ID.AM-02, PR.DS-12, RS.CO-04, RS.MI-01, PR.PS-06, GV.OC-02, GV.RR-02, GV.SC-05 |
| D-07 (D-07 Secure Development) | 2 | PR.DS-12, PR.PS-06, PR.PS-01, PR.PS-02, ID.RA-01, GV.OV-01, GV.OV-02, GV.PO-02, GV.SC-04, ID.IM-04 |
| D-08 (D-08 Human Factors) | 3 | PR.AT-01, PR.AT-02, PR.PS-01, GV.SC-03, PR.AT-04, GV.RR-01, GV.RR-02, GV.RR-04, PR.AT-03 |
| D-09 (D-09 Governance & Documentation) | 3 | GV.OV-03, GV.PO-01, GV.PO-01 (primary), GV.PO-02, GV.RM-04, GV.RR-01, GV.RR-02, GV.RR-03, GV.OC-03, GV.SC-01, GV.SC-04, GV.OV-01, GV.RM-05, GV.OC-04, GV.RM-01, ID.RA-04, ID.RA-05, ID.RA-05 (primary), ID.SC-04, ID.AM-01, ID.AM-02, PR.PS-01, PR.PS-01 (primary), ID.AM-08, ID.AM-08 (primary), PR.DS-12 |
| D-10 (D-10 Monitoring Audit) | 3 | DE.AE-02, DE.CM-01, DE.CM-01 (primary), DE.CM-09, ID.IM-04, DE.CM-09 (primary), GV.OV-03, GV.PO-02, PR.DS-11, PR.DS-11 (primary), PR.PT-01, ID.RA-04, PR.IP-06, DE.AE-03, PR.PS-04, PR.PS-04 (primary), RC.RP-03, ID.RA-05, PR.IP-07, PR.IP-07 (primary) |

### 4.3 NOT_ADDRESSED sub-domains

Per Sprint 1 reconciliation, three sub-domains are flagged NOT_ADDRESSED because their regulatory participants are DORA-exclusive (DORA does not apply to SecureBorder). They are retained in the corpus cross-reference for ISO 27001 inheritance traceability, and they remain in §3 above so the compliance mapping surface is complete.

| Sub-domain | Reason NOT_ADDRESSED | Corpus retention |
|---|---|---|
| D-07.2 Secure Coding Practices | DORA-exclusive; ISO 27001 A.14 + IEC 62443-4-1 inheritance | Manifest preserved for cross-case reference |
| D-07.4 Change Management | DORA-exclusive; ISO 27001 A.12.1 + AI_Act Art. 16 inheritance | Manifest preserved for cross-case reference |
| D-09.3 Asset Inventories | DORA-exclusive; ISO 27001 A.5.9 inheritance | Manifest preserved for cross-case reference |

Source: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` (Sprint 2 corpus root).

---
## 5. Gate

| Gate Criterion | Status | Evidence |
|---|---|---|
| All production systems are inventoried | PASS | 13 systems documented in Section 1.1 |
| All data stores documented with encryption status | PASS | 7 stores documented in Section 2.1 |
| All data flows documented with encryption status | PASS | 12 flows documented in Section 2.2 |
| Personal data categories enumerated with legal basis | PASS | 8 categories documented in Section 2.3 (incl. Art. 9 biometric, employee, witness, audit) |
| Compliance mapping table populated for all 38 active sub-domains | PASS | 38 rows in Section 3; all marked ACTIVE |
| Proportionality maintained for HIGH-complexity 4-regulation company | PASS | No over-engineering claimed (HSM is justified by Critical Class + Art. 9; SIEM is justified by 24/7 NIS 2 SOC commitment) |

## N. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-07-11 | Executor | Created SecureBorder populated architecture and data inventory from the 04a template; 13 systems / 7 stores / 12 flows proportional to HIGH complexity (4 regulations, 450 staff, hardware+software Critical Class product with Edge AI). |
| 1.1 | 2026-08-06 | Executor | Sprint 1 reconciliation: frontmatter → AEGIS-P2-RICH-*, status: DRAFT → RECONCILED, active_subdomains 38 → 35, applicable_regs aligned. Body preserved verbatim. |
| 1.2 | 2026-08-06 | Executor | Sprint 2 corpus enrichment: §3 Compliance Mapping gains 2 columns (Corpus Manifest Path + NIST CSF Anchors) per sub-domain (38 rows); new §4 Corpus Provenance with per-sub-domain manifest index + aggregate counts + NOT_ADDRESSED explanation. Source: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`. |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-07-11 |
| Technical Review | CTO |  |  |
| Security Review | CISO |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Data backbone:** `Case_02_Phase1.xlsx` (13 sheets: COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, MATURITY, SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES)
- **Operational architecture:** the kiosk-to-cloud flow is detailed in §1.2; for full mTLS endpoint inventory see `04c_ThirdParty_Landscape.md` §2.
- **AI_Act specifically:** the Edge AI inference engine on SYS-04 falls under Annex III — see `05_Regulatory_Applicability.md §3.5` for AI_Act overlay on D-09.2 (FRIA), D-09.4 (technical documentation), D-10.1 (post-market monitoring).
- **High-tier proportionality note (P2):** the HSM cluster (SYS-07) and immutable WORM store (STORE-04) are **not** over-engineering for a HIGH-tier Critical Class + Annex III AI company. They are the minimum proportionate baseline to satisfy GDPR Art. 32 + CRA Annex I Part I (2)(c) + NIS 2 Art. 21 + AI_Act Art. 9.
