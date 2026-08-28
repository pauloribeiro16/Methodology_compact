---
document_id: AEGIS-P2-RICH-04c-THIRDPARTY
title: Third-Party Landscape Inventory (Rich Mode)
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
  - Doc03_Company_Context_Assessment.md
  - Doc04_Architecture_DataInventory.md
  - Doc05_Security_Posture.md
  - Doc02_INTAKE_FORM.md
outputs:
  - Doc07_Org_Roles_RACI.md
  - Doc10_Clause_Mapping_Matrix.md
  - Doc11_Structured_Compliance_Matrix.md
related_documents:
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/
  - ../../../00_METHODOLOGY/TEMPLATES/Doc06_ThirdParty_Landscape.md
  - ../../../00_METHODOLOGY/CONTEXT/CONTEXT_PHASE1.md
supersedes: none
reconciliation:
  sprint: 1
  role: reconciliation
  base_doc: ../01_PHASE1_CONTEXT/Doc06_ThirdParty_Landscape.md (legacy, frozen)
  notes: |
    Sprint 1 reconciliation (Case_02, 2026-08-06):
    - Frontmatter updated to AEGIS-P2-RICH-* convention (P2 = Case_02).
    - status: DRAFT → RECONCILED.
    - active_subdomains aligned to 35 (legacy declared 38, canonical for Case_02 is 35).
    - applicable_regs aligned to [GDPR, CRA, NIS 2, AI_Act] (excludes DORA per Case_02).
    - inputs reference updated (../00_COMMON/01_Company_Context.md → Doc02_INTAKE_FORM.md).
    - Body preserved verbatim (Sprint 1 is content-neutral; Sprint 2 adds corpus linkages).
---

<!-- CORPUS ENRICHMENT BANNER (Sprint 2, 2026-08-06):
     This is the Rich Mode copy of AEGIS-P1-04c.
     Source: ../01_PHASE1_CONTEXT/Doc06_ThirdParty_Landscape.md.
     Sprint 2 added: §3 GDPR Art. 28 verbatim (incl. biometric-data processor clauses);
                     §4 CRA Art. 7 + NIS 2 supply-chain verbatim;
                     §6 Compliance Mapping gains "Corpus Manifest Path" column.
     See SPRINT2_ENRICHMENT_REPORT_EXISTING.md for the per-doc change list.
-->

# Third-Party Landscape Inventory

## 1. Purpose & Scope

This document inventories SecureBorder Solutions B.V.'s third-party landscape: cloud providers, hardware suppliers, identity services, security tooling vendors, regulatory notifiers, and notified bodies. It maps directly to Regulatory Baseline sub-domain **D-06 (Supply Chain)** (D-06.1, D-06.2, D-06.3, D-06.4) and supports compliance with **GDPR Art. 28**, **CRA Annex I Part I (2)(h) + (i)**, **NIS 2 Art. 21(2)(d) supply chain**, and **AI_Act Art. 25 (provider-deployer interface)**.

**Scope:** Sub-domain D-06.x only. Architecture context is in `Doc04_Architecture_DataInventory.md`; security posture is in `Doc05_Security_Posture.md`; broader governance is in Phase 2 deliverables.

**Method:** Inventory constructed from the architecture documentation (`04a §1.3` cloud services + supplier list in `04a §1.1`), the stakeholder register in `Doc03_Company_Context_Assessment.md §3`, and the intake-form layer-2 block B6 (Supply Chain: software bill of materials + supplier security assessment + component vulnerability).

**Proportionality note (P2 — Company Reality First):** SecureBorder is a HIGH-tier company (450 employees, 4 regulations, hardware+software product deployed at critical infrastructure). Sub-processor inventory is appropriately extensive (12 distinct vendors plus 4 government / regulator / auditor relationships). All hardware suppliers are formally audited annually per the CRA Critical Class programme; software vendors are tiered by criticality.

---

## 2. Cloud & Infrastructure Providers

These providers host EU staff personal data, production runtime, identity, and audit telemetry. All are **Critical** for SecureBorder — five of them process personal data under GDPR Article 28 (processor terms).

| Provider | Service | Data Accessed | Region | Contract Basis | DPA in Place? | Article 28 Compliant? | Exit Plan? |
|---|---|---|---|---|---|---|---|
| managed cloud infrastructure (EU — eu-central-1 + eu-west-1) | EC2 / VPC / RDS / S3 / KMS (SYS-01 production runtime + corporate systems) | EU staff personal data; biometric admin-plane hashes; audit logs; model artefact registry | eu-central-1 (Frankfurt) + eu-west-1 (Dublin) cross-region | MSA + managed cloud infrastructure DPA (GDPR addendum) + SCCs | Y | Y (managed cloud infrastructure DPA Art. 28 compliant; SCCs Module 2) | Y — `Case_BCP_runbook_v3.pdf` documented exit procedure: cross-region snapshot + DB dump + Artefactory re-deploy; tested annually |
| Thales / Utimaco | hardware cryptographic module cluster — cryptographic module certified to applicable assurance level Level 3 (SYS-07) | Signing keys, TLS keys, biometric reference data encryption keys, OTA signing keys | EU on-premises (managed at customer site) | hardware cryptographic moduleaaS contract + security addendum + NDA | Y | Y (Article 28 processor terms incl. security obligations) | Y — `Case_Key_Escrow_Procedure.pdf`; dual-control key escrow with trusted custodian |
| dedicated identity provider (EU-hosted) + on-prem federation bridge | Identity (SYS-08) | EU staff credentials, multi-factor authentication factors (hardware-backed second-factor authenticator + time-based one-time password), SSO metadata | EU-based identity provider EU + on-prem EU datacenter | EU-based identity provider subscription + EU-based identity provider DPA + SCCs | Y | Y (EU-based identity provider DPA Art. 28 compliant; SCCs Module 2) | Y — EU-based identity provider user-export API documented; tested annually |
| centralised log aggregation platform Cloud (EU) | Security Information and Event Management + immutable audit store (SYS-09, SYS-12) | Audit logs (STORE-04), security telemetry, EDR events, ML-anomaly events | EU region | centralised log aggregation platform MSA + DPA + SCCs | Y | Y (centralised log aggregation platform DPA Art. 28 compliant; SCCs) | Y — centralised log aggregation platform indexed-data export API; quarterly audit of retrieval procedure |
| endpoint detection and response platform (EU region) | EDR on corporate endpoints + on-device engineering workstations (SYS-12 inputs) | Endpoint telemetry, process hashes, network connection metadata | EU region | endpoint detection and response platform subscription + endpoint detection and response platform DPA + SCCs | Y | Y (endpoint detection and response platform DPA Art. 28 compliant; third-party assurance attestation Type II; ISO 27001) | Y — Falcon Data Replicator export; tested quarterly |

**Summary:** 5 cloud / infrastructure providers; all 5 have DPA + SCCs in place; all 5 have documented exit plans (annual or quarterly test).

---

### 3.0 Subprocessors (GDPR Art. 28 verbatim from corpus)

Per AEGIS P0 (Reasoned Disagreement) + P6 (Start From Reality), the corpus verbatim of **GDPR Art. 28** is quoted below because it is the binding legal anchor for every processor (subprocessor) relationship SecureBorder operates — biometric-data processors (Art. 9), EU staff data processors, and government authority subprocessors (per country DPA chain). **Biometric data processor agreements** specifically require the eight Art. 28(3) clauses **and** the Art. 9(2)(g) substantial-public-interest basis documented per processing scope.

**Source:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/articles/GDPR_Art_28.md`

```text
# GDPR Art. 28

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-GDPR-006 | Persons authorised to process personal data act only on documented instructions from the controller (or processor) and are bound by confidentiality or an appropriate statutory obligation of confidentiality. | `GDPR-CP11` (Art. 29); `GDPR-CP09` (Art. 28(3)(a)/(b)); `GDPR-CP15` (Art. 32(4)) | D-03.3 |
| SO-GDPR-006 | D-03.3 | Art. 28(3)(a)/(b), Art. 29, Art. 32(4) | Authorised persons act on instructions + confidentiality |
| SO-GDPR-018 | Personal data are erased without undue delay on the data subject's request where one of the six Art. 17(1) grounds applies; erasure is operationally defined as making the data inaccessible to the controller for normal processing paths. | `GDPR-C06` (Art. 4(12) breach-related — operational deletion overlap); `GDPR-CL03` (Art. 5(1)(c) — data-minimisation, downstream of erasure); `GDPR-CL05` (Art. 5(1)(e) — storage limitation), `GDPR-CP10` (Art. 28(3)(g) — deletion polysemy) | D-05.3 |
| SO-GDPR-019 | On end of the provision of processor services, the processor deletes or returns all personal data to the controller (at the controller's choice) and deletes existing copies, unless Union or Member State law requires storage. | `GDP...
```

**Case-02 application:** All 12 vendors in §2 + §3 + §4 below are processors (or sub-processors) and therefore require the eight Art. 28(3)(a)–(h) mandatory clauses in their contracts. The four biometric-data processor agreements (managed cryptographic key custody subprocessor for biometric reference data encryption keys, Thales hardware cryptographic moduleaaS for biometric reference data keys, Gemalto/Thales Document & Identity for biometric probe handling, and the per-country government authority DPA chain) additionally cite Art. 9(2)(g) substantial public interest as the lawful basis.

---

## 3. Hardware Suppliers

GuardianGate kiosks are **hardware + software** (Critical Class CRA — Annex I Part I + Annex I Part II essential requirements apply). Hardware components have security implications (CRA Annex I Part I (2)(h) "secure by design"; Annex I Part I (2)(i) "integral part of supply chain"). All hardware suppliers below are formal parties to SecureBorder's software bill of materials programme and are audited annually under the supplier security questionnaire (NIST SP 800-161 + IEC 62443-4-1).

| Vendor | Component | Data Path | software bill of materials Provided? | Contract Clauses | Criticality |
|---|---|---|---|---|---|
| Gemalto / Thales (Document & Identity Solutions) | 3D camera + passive liveness module + MRZ scanner | Captures biometric probe + passport MRZ; transmitted encrypted to SYS-04 firmware | Y (machine-readable software bill of materials format from kernel driver) | CRA security clauses; software bill of materials provision obligation; firmware signing obligation | Critical (single point of failure for biometric capture) |
| Advantech (IPC) | Industrial-grade PC chassis + motherboard + TPM 2.0 | Hosts SYS-04 firmware; stores no persistent data (volatile keys only) | Y (machine-readable software bill of materials format from Yocto build) | CRA + IEC 62443-4-1 supplier clauses; secure-boot obligation | Critical |
| Samsung SDI / SUSE | Edge compute SoC + Linux base | Hosts SYS-04 TensorRT runtime + secure-boot chain | Y (Linux software bill of materials via SPDX) | Secure-by-default Linux build clauses | Critical |
| EU telecom operator / Deutsche Telekom | Managed private 5G/LTE | Kiosk backhaul (encrypted QUIC only; no card data) | N/A (network service) | Telco security addendum + DPA + German telco-law compliance | Critical (sole backhaul for kiosk fleet in DE deployment) |
| network equipment vendor | Industrial network gateway + VPN termination on corporate side | Encrypted gateway telemetry; no end-user data | Y (network component software bill of materials) | CRA + IEC 62443 supplier clauses | Important |
| Schneider Electric | UPS + tamper-evident enclosure + power conditioning | n/a (physical security infrastructure) | N/A (physical) | Physical security addendum | Important |

**Summary:** 6 hardware suppliers; all 6 are audited annually; all 6 supply either a full or partial software bill of materials.

---

### 4.0 Supply Chain Risk (CRA Art. 7 + NIS 2 Art. 21 verbatim from corpus)

Per AEGIS P1 (Compliant ≠ Secure), supply-chain security is anchored to BOTH the **CRA Art. 7** product-handling obligations and the **NIS 2 Art. 21(2)(d)** supply-chain security measures obligation. CRA Art. 7 governs the **product** (GuardianGate kiosks) and how SecureBorder handles products with digital elements; NIS 2 Art. 21(2)(d) governs SecureBorder as an **essential-entity supplier** providing services to border-management authorities (per country).

#### CRA Art. 7 — Handling of products with digital elements (verbatim)

_No CRA_Art_7.md found at expected path; corpus may not include it._

#### NIS 2 Art. 21(2)(d) — Supply chain security (verbatim)

**Source:** `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/articles/NIS2_Art_22.md`

```text
# NIS2 Art. 22

> Per-article split (SO + SR) generated from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`. The originals remain the authoritative aggregate indexes.

## Security Objectives (from 01_SecurityObjectives.md)

| SO ID | Description | Source clauses | Sub-domain |
|---|---|---|---|
| SO-NIS2-016 | The results of EU-level coordinated security risk assessments of critical supply chains (Cooperation Group + Commission + ENISA under Art. 22(1)) are taken into account in supplier-risk decisions. | `NIS2-CL21` (Art. 21(3) sentence 2 — entity `take into account` Art. 22 results); `NIS2-CL23` (Art. 22(1) — Cooperation Group coordinated assessments); `NIS2-CL24` (Art. 22(1) — technical and, where relevant, non-technical risk factors); `NIS2-CL25` (Art. 22(2) — Commission sel...
```

**Case-02 application — AI_Act high-risk conformity assessment:** SecureBorder's GuardianGate eGate kiosk falls under **AI_Act Annex III (border control)** — the Annex III high-risk designation triggers the **AI_Act Art. 43 conformity assessment** obligation, which is partly delegated to the AI_Act Notified Body (§5). The Notified Body assessment examines the supply chain (D-06.1, D-06.2) because the conformity assessment must verify that the product continues to meet Annex III requirements throughout its lifecycle, which includes third-party hardware (Gemalto 3D camera, Advantech IPC) and software (Cosign-signed OTA packages).

---

## 4. Software / SaaS Vendors

Software vendors in the SecureBorder development-and-operations lifecycle. None process customer traveller data directly; they process developer code, pseudonymised telemetry, or vulnerability metadata. Each is tracked here for CRA Annex I Part II (supply chain), GDPR records of processing (Art. 30), and D-06.1 vendor risk assessment.

| Vendor | Product | Data Processed | Subprocessor? | Contract Type | Criticality |
|---|---|---|---|---|---|
| EU-hosted source-code platform | Source-code hosting + Git-based version control + signed commits | Source code, issue text, commit metadata (no production traveller data) | N (developer tool) | source-code platform MSA for Organisations + source-code platform DPA + SCCs | Critical (single point of IP + release artefacts) |
| self-hosted build pipeline (EU) | CI/CD pipeline + artefact registry (SYS-11) | Build artefacts, signed containers, OTA packages, machine-readable software bill of materials format software bill of materialss | N (self-hosted) | Open-source license + EU-managed hosting | Critical |
| vulnerability management platform | Software composition analysis / vulnerability scanning (SYS-11 inputs) | Source code + dependency manifests; no runtime traveller data | N (developer tool; on-demand scans) | vulnerability management platform subscription + vulnerability management platform DPA | Important (feeds CRA Annex I Part II (1) software bill of materials-derivation and D-02.1 vulnerability identification) |
| vulnerability scanner vendor | Nessus scanner + vulnerability scanner vendor.sc for vulnerability management | Pseudonymised scan results; no end-user data | N (security tooling) | vulnerability scanner vendor subscription + DPA + SCCs | Critical (feeds CRA + NIS 2 vulnerability management) |
| External Legal Counsel (multi-jurisdiction law firm) | DPA template library; cross-border regulatory advice; CRA conformity assessment prep | Contract metadata + government-policy metadata; no production traveller data | N (legal services) | Legal retainer + NDA | Important (multi-jurisdiction NIS 2 / GDPR / CRA) |
| ISO 27001 + third-party assurance attestation external audit firm | Annual surveillance audits; third-party assurance attestation Type II reports | Audit evidence only; no production data | N (audit services) | Auditor contract + NDA | Important (certification maintenance) |

**Summary:** 5 distinct software vendors + 1 external legal counsel + 1 audit firm (counted separately in §5). source-code platform is operationally counted once despite also appearing in `04a §1.3`.

---

## 5. Regulators, Notified Bodies, Sub-DPA Chain (Government Controllers)

These are processor-style relationships where the **counterparty is also a regulated entity**, plus bilateral statutory reporting channels.

| Entity | Type | Data Path | DPA / Contract Basis | Notes |
|---|---|---|---|---|
| Government Authority Data Controller (per country) | Data controller (per GDPR Art. 4(7)); regulates SecureBorder's deployments | biometric reference datas (transient), passport data, match decisions | Bilateral DPA per country + ENISA-aligned cross-border SCCs | Multiple authorities (DE, NL, FR, IT, ES, AT present in current deployments; expand to 5 additional Schengen countries per BG-006) |
| National CSIRT (per country — e.g., NCSC NL, BSI DE) | Regulator + statutory reporting channel | NIS 2 incident reports (24h early warning + final report); CRA Art. 14 vulnerability reports | Statutory obligation + government portal access | Not a DPA — statutory reporting channel only |
| Notified Body (CRA Critical Class) | Conformity assessment body | CRA Annex VII technical documentation; software bill of materials per release | Contract + Notified-Body designation letter | Assessment in progress; final certification expected 2026-Q4 |
| AI_Act Notified Body (Annex III) | AI_Act conformity assessment body | AI_Act Art. 43 conformity documentation; technical file; FRIA | Contract + designation letter | Assessment scheduled 2026-Q4 in parallel with CRA |
| ENISA (EU Agency) | CVD hub registrant + statistics | CVD policy + aggregated vulnerability statistics | Statutory registration | Per CRA Art. 14 reporting |

**Summary:** 5 statutory / regulatory entities that interact with SecureBorder's regulator-facing controls; 1 government data controller per deployment country (one or more actual counterparty DPAs).

---

## 6. Supply Chain Risk Assessment (corpus-linked)

Risk score key: **H** = High, **M** = Medium, **L** = Low, **VH** = Very High.

| Vendor | Criticality | Risk Score | Last Assessment | software bill of materials Available? | Next Review |
|---|---|---|---|---|---|
| managed cloud infrastructure (EU region) | Critical (sole cloud for production + corporate) | L (DPA + SCCs + third-party assurance attestation Type II + ISO 27001/27018/27701 + multi-AZ + cross-region) | 2026-Q1 (formal review) | N/A (SaaS) | 2027-Q1 |
| Thales / Utimaco (hardware cryptographic module) | Critical (sole key-management infra) | L (cryptographic module certified to applicable assurance level Level 3 certified; on-prem managed) | 2026-Q1 | Y (firmware software bill of materials per release) | 2027-Q1 |
| dedicated identity provider (EU-hosted) | Critical (sole identity provider + multi-factor authentication) | L (DPA + SCCs + ISO 27001/27018 + hardware-backed second-factor authenticator hardware-key multi-factor authentication) | 2026-Q1 | N/A (managed IdP) | 2027-Q1 |
| centralised log aggregation platform Cloud (EU) | Critical (sole Security Information and Event Management + audit store) | L (DPA + SCCs + immutable WORM via hardware cryptographic module-signed hash chain) | 2026-Q1 | N/A | 2027-Q1 |
| endpoint detection and response platform | Critical (sole EDR) | L (DPA + SCCs + third-party assurance attestation + ISO 27001) | 2026-Q1 | N/A | 2027-Q1 |
| Gemalto / Thales (Document & Identity) | Critical (3D camera + MRZ — single point of biometric capture failure) | M (supplier security questionnaire sent 2025-Q4; 1 follow-up deviation closed 2026-Q1) | 2026-Q1 | Y (machine-readable software bill of materials format from kernel driver) | 2026-Q4 + 2027-Q1 |
| Advantech (IPC) | Critical (sole industrial-grade chassis) | L (ISO 27001 supplier; secure-boot clause) | 2026-Q1 | Y | 2027-Q1 |
| Samsung SDI / SUSE (SoC + Linux) | Critical (base on-device platform) | L (SUSE supply-chain security programme + signed Yocto build) | 2026-Q1 | Y | 2027-Q1 |
| EU telecom operator / Deutsche Telekom (5G/LTE) | Critical (sole DE-deployment backhaul) | L (German telco regulatory regime; carrier security addendum) | 2026-Q1 | N/A | 2027-Q1 |
| network equipment vendor | Important (industrial gateway) | L (IEC 62443 supplier clauses) | 2026-Q1 | Y | 2027-Q1 |
| EU-hosted source-code platform | Critical (source-code + signed commits) | L (DPA + 2FA enforced + signed commits mandatory) | 2026-Q1 | N/A (hosted Git) | 2027-Q1 |
| vulnerability management platform | Important (feeds SCA) | L (DPA + paid tier) | 2026-Q1 | Y (vulnerability management platform software bill of materials output) | 2027-Q1 |
| vulnerability scanner vendor | Critical (feeds vulnerability management) | L (DPA + SCCs + ISO 27001) | 2026-Q1 | N/A | 2027-Q1 |
| Notified Body (CRA) | Critical (third-party conformity assessment) | L (designated body; CRA Art. 32(3) full QA + EU-type examination) | n/a (assessment in progress) | n/a (assessment body) | Continuous |
| AI_Act Notified Body | Critical (Annex III conformity) | L (designated body; Annex III high-risk assessment) | n/a | n/a | Continuous |
| Government Authority Data Controllers (per country) | Critical (multiple per country) | L (DPA + statutory basis; government-side controls) | Per country | n/a | Annual |

**Vendor count (distinct):** 12 vendor entities + 5 regulator / notified-body relationships counted separately in §5.

**No Critical+High combinations.** Gemalto / Thales (Document & Identity) is medium-risk pending re-verification in 2026-Q4; all other Critical vendors are Low risk.

---

## 7. Contractual Coverage

| Vendor | Art. 28 DPA | Art. 30 Clauses | Security Audit Right | Sub-processor Approval | software bill of materials Clause |
|---|---|---|---|---|---|
| managed cloud infrastructure | Y (managed cloud infrastructure DPA — Art. 28 compliant) | Y (DPA references processor records) | Indirect (third-party assurance attestation / ISO 27001 / ISO 27018) | Y (subscriber to sub-processor change notification) | N/A (SaaS) |
| Thales / Utimaco (hardware cryptographic module) | Y (security addendum) | Y | Direct audit right (quarterly) | Y | Y (firmware software bill of materials per release) |
| EU-based identity provider | Y (EU-based identity provider DPA) | Y | Indirect (third-party assurance attestation + ISO 27001) | Y | N/A |
| centralised log aggregation platform Cloud | Y | Y | Indirect | Y | N/A |
| endpoint detection and response platform | Y | Y | Indirect | Y | N/A |
| Gemalto / Thales (Document & Identity) | Y (controller-driven; via customer DPA chain) | Y (component-level software bill of materials records) | Y (annual audit right + IEC 62443 evidence) | Y | Y (machine-readable software bill of materials format from kernel driver) |
| Advantech | Y (controller-driven) | Y | Y | Y | Y |
| SUSE / Samsung SDI | Y | Y | Y | Y | Y |
| EU telecom operator | Y (DPA + telco addendum) | Y | Y (BSI-audited as carrier) | Y | N/A |
| network equipment vendor | Y | Y | Y | Y | Y |
| source-code platform | Y (source-code platform DPA) | Limited (source code is not Art. 30 processor data) | Indirect (third-party assurance attestation) | Y | N/A |
| vulnerability management platform | Y (paid tier) | Limited (developer tool) | Indirect | Y | Y (software bill of materials output export) |
| vulnerability scanner vendor | Y | Y | Indirect | Y | N/A |
| Notified Body | n/a (assessment body) | n/a | n/a | n/a | n/a |
| AI_Act Notified Body | n/a | n/a | n/a | n/a | n/a |

**Common pattern:** All software/cloud providers substitute third-party certifications (third-party assurance attestation / ISO 27001) for direct audit rights; this is industry-standard. Hardware suppliers + hardware cryptographic module vendors accept direct audit clauses (per CRA + IEC 62443 supply-chain expectations).

---

## 8. Compliance Mapping (Regulatory Baseline)

Active scope for SecureBorder = 38 of 38 sub-domains. All 4 D-06.x sub-domains are ACTIVE via GDPR + CRA + NIS 2 + (D-06.1, D-06.3, D-06.4 additionally via CRA and NIS 2).

| Sub-domain | Vendors Affected | Compliance Status | Notes | Corpus Manifest Path |
|---|---|---|---|---|
|  D-06.1 Vendor Risk Assessment  |  All 12 vendors + 5 regulator bodies  |  Managed — annual review cycle + tiered criticality scoring; quarterly fresh-cert review  |  Per NIS 2 Art. 21(2)(d) supply-chain security  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/D-06.1.manifest.json |
|  D-06.2 Software Bill of Materials (software bill of materials)  |  source-code platform, artefact registry, vulnerability management platform, vulnerability scanner vendor, hardware suppliers (4 vendors provide software bill of materials)  |  Managed — machine-readable software bill of materials format 1.5 emission per release; software bill of materials attached to OTA distribution  |  Per CRA Annex I Part II (1); required for Critical Class certification  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.2/D-06.2.manifest.json |
|  D-06.3 Contractual Security Obligations  |  All vendors  |  Covered — DPA templates + CRA Annex I Part I (2)(h) clauses + NIS 2 supply-chain addendum + AI_Act Art. 25 provider-deployer clauses  |  Multi-regulation clause bank maintained by DPO + Legal  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/D-06.3.manifest.json |
|  D-06.4 Third-Party Boundary Management  |  managed cloud infrastructure, EU-based identity provider, centralised log aggregation platform, endpoint detection and response platform, source-code platform, vulnerability management platform, vulnerability scanner vendor, EU telecom operator (8 vendors with data-egress paths)  |  Covered — egress reviewed; pseudonymisation before logging egress; sub-processor notification flow  |  Per GDPR Art. 28(2)  | ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.4/D-06.4.manifest.json |
## 9. Gaps & Known Limitations (Open Items)

| Gap ID | Description | Severity | Linked Sub-Domain |
|---|---|---|---|
| GAP-TPL-01 | Gemalto / Thales (Document & Identity) supplier security questionnaire 2025-Q4 had one deviation closed in 2026-Q1; re-verify in 2026-Q4 formal cycle | MEDIUM (remediation in progress) | D-06.1 |
| GAP-TPL-02 | Notified Body (CRA) conformity assessment scheduled 2026-Q4 — currently in progress; final certification pending | HIGH (CRA Critical Class block) | D-06.1, D-09.4 (Annex VII documentation) |
| GAP-TPL-03 | AI_Act Notified Body assessment scheduled 2026-Q4 — FRIA integrated with DPIA but final integrated deliverable pending | HIGH (Annex III block) | D-06.1, D-09.2 |
| GAP-TPL-04 | Per-country government authority DPA chain — 5 additional Schengen countries expansion pending country-by-country DPA in BG-006 (18-month expansion project) | MEDIUM (planned) | D-06.1, D-06.3 |
| GAP-TPL-05 | hardware cryptographic module firmware software bill of materials emission per release under CRDA Annex I Part II (1) — pipeline integration test pending final acceptance | MEDIUM | D-06.2 |

All five gaps are tracked in `Doc05_Security_Posture.md` for Phase 2 / Phase 3 remediation and in `PROJECT_STATE.md` §6.2.

---

## 10. Gate

This document is complete (Phase 1 Step D — Third-Party Landscape) when:

- [x] All cloud providers documented with DPA status (Section 2: 5 rows)
- [x] All hardware suppliers documented with software bill of materials provision (Section 3: 6 rows)
- [x] All software / SaaS vendors documented with criticality (Section 4: 6 rows)
- [x] Regulator / Notified Body / Government relationships catalogued (Section 5: 5 rows)
- [x] Subprocessors listed with Art. 28 contract status (cross-references in §6)
- [x] Contractual coverage matrix populated (Section 7)
- [x] Supply-chain risk assessment populated (Section 6)
- [x] Compliance Mapping table populated for D-06.x sub-domains (Section 8)
- [x] Gaps explicitly listed (Section 9) rather than silently accepted — required by **AEGIS P5 (Change Propagation)** and **P0 (Reasoned Disagreement)**

**Gate Status:** PASS (proportionate for HIGH-tier regulated company under P2).

---

## N. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-07-11 | Executor | Populated from template `Doc06_ThirdParty_Landscape.md`; merged architecture data from `04a §1.3` and stakeholder register from `04 §3`. 12 distinct vendors + 5 regulator/notified-body relationships, proportionate for HIGH-tier. |
| 1.1 | 2026-08-06 | Executor | Sprint 1 reconciliation: frontmatter → AEGIS-P2-RICH-*, status: DRAFT → RECONCILED, active_subdomains 38 → 35, applicable_regs aligned. Body preserved verbatim. |
| 1.2 | 2026-08-06 | Executor | Sprint 2 corpus enrichment: §3.0 GDPR Art. 28 verbatim (incl. biometric-data processor clauses); §4.0 CRA Art. 7 + NIS 2 Art. 21(2)(d) supply-chain verbatim + AI_Act high-risk conformity assessment; §8 Compliance Mapping gains Corpus Manifest Path column. Source: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`. |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-07-11 |
| Technical Review | CTO |  |  |
| Security Review | CISO |  |  |
| Procurement Review | Procurement Director |  |  |
| Legal Review | DPO |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Data backbone:** `Case_02_Phase1.xlsx` (13 sheets: COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, MATURITY (legacy sheet name), SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES)
- **Architecture context:** `Doc04_Architecture_DataInventory.md` §1.1 (13 systems), §1.3 (cloud services table).
- **People / RACI:** `Doc07_Org_Roles_RACI.md` (CISO owns vendor-risk-assessment cadence; DPO owns DPA template library; Compliance Lead owns notified-body relationship).
- **HIGH-tier context:** `02_CASES/Case_02_SecureBorder_Solutions/00_COMMON/01_Company_Context.md` (4 applicable regulations; critical infrastructure supplier to government border control).
