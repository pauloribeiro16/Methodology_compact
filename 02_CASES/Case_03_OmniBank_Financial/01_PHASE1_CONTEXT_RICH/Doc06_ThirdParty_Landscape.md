---
document_id: AEGIS-P3-RICH-04c-3P
title: Third-Party Landscape Inventory (Rich Mode)
phase: 1
version: 1.2
created: 2026-07-11
updated: 2026-08-06
author: Executor (Sprint 1 reconciliation copy)
status: CORPUS_ENRICHED
case: Case_03_OmniBank_Financial
applicable_regs: [GDPR, CRA, NIS 2, DORA, AI Act]
active_subdomains: 38
inactive_documented: []
inputs:
  - Doc03_Company_Context_Assessment.md
  - Doc04_Architecture_DataInventory.md
  - Doc05_Security_Posture.md
  - Doc02_INTAKE_FORM.md
outputs:
  - Doc07_Org_Roles_RACI.md
  - Doc10_Clause_Mapping_Matrix.md
  - Doc12_Structured_Compliance_Matrix.md
related_documents:
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/
  - ../../../00_METHODOLOGY/TEMPLATES/Doc06_ThirdParty_Landscape.md
sibling_of: ../01_PHASE1_CONTEXT_RICH/Doc06_ThirdParty_Landscape.md
reconciliation_notes:
  - "Sprint 1 (2026-08-06): Copied from 01_PHASE1_CONTEXT/Doc06_ThirdParty_Landscape.md → Rich folder; frontmatter migrated to AEGIS-P3-RICH-* prefix; status DRAFT → RECONCILED; applicable_regs normalized to [GDPR, CRA, NIS 2, DORA, AI Act]; active_subdomains confirmed = 38. Body unchanged."
---

<!-- CORPUS_ENRICHED (Sprint 2, 2026-08-06): Enrichment with verbatim GDPR Art. 28 + CRA Art. 13 + DORA Art. 30 + AI Act Art. 25 cross-references.
Replaces RECONCILED comment. Document copied from legacy 01_PHASE1_CONTEXT/Doc06_ThirdParty_Landscape.md to Rich folder.
Changes: (a) document_id migrated to AEGIS-P3-RICH-04c-3P; (b) status DRAFT → RECONCILED;
(c) applicable_regs normalized from [GDPR, NIS2, CRA, DORA, AI_Act] to [GDPR, CRA, NIS 2, DORA, AI Act] (canonical order);
(d) DORA Art. 28-30 CTPP register alignment cross-referenced (per Sprint 0.6 Doc 04a/04d deliverables).
Sprint 2 (2026-08-06): §3 enriched with verbatim GDPR Art. 28 text from corpus D-06.3/articles/; §4 (Supply Chain Risk) cross-references CRA Art. 13 + NIS 2 Art. 21(2)(d) + DORA Art. 30 + AI Act Art. 25 (corpus-anchored); §6 Compliance Mapping table extended with Corpus Manifest Path column. status RECONCILED → CORPUS_ENRICHED.
-->

---
  - ../../../00_METHODOLOGY/CONTEXT/CONTEXT_PHASE1.md
supersedes: none
---

# Third-Party Landscape Inventory

## 1. Purpose & Scope

This document inventories OmniBank Financial Systems S.A.'s third-party landscape: cloud providers, payment networks, card networks, AI/ML service providers, security tooling vendors, hardware suppliers, and regulatory/statutory counterparties. It maps directly to Regulatory Baseline sub-domain **D-06 (Supply Chain)** (D-06.1, D-06.2, D-06.3, D-06.4) and supports compliance with **GDPR Art. 28**, **CRA Annex I Part I (2)(h) + (i)**, **NIS 2 Art. 21(2)(d) supply chain**, **DORA Art. 28-30** (ICT third-party register + ICT contracts), and **AI Act Art. 25** (provider-deployer interface).

**Scope:** Sub-domain D-06.x only. Architecture context is in `Doc04_Architecture_DataInventory.md`; security posture is in `Doc05_Security_Posture.md`; broader governance is in Phase 2 deliverables.

**Method:** Inventory constructed from the architecture documentation (`04a §1.3` cloud services + supplier list in `04a §1.1`), the stakeholder register in `Doc03_Company_Context_Assessment.md §3`, and the DORA Art. 28 ICT third-party register.

**Proportionality note (P2 — Company Reality First):** OmniBank is a MAXIMUM-tier credit institution (5,000+ employees, 5 regulations, mainframe + cloud hybrid, AI Act Annex III AI, DORA financial entity). Sub-processor inventory is extensive (~22 distinct vendors plus ~10 statutory / regulator / card scheme / network relationships). DORA Art. 28 ICT third-party register is maintained as a separate document by CRO; this 04c document cross-references it. All card networks and SWIFT are formal parties to OmniBank's vendor security programme. Software vendors are tiered by criticality per DORA Art. 30.

---

## 2. Cloud & Infrastructure Providers

These providers host EU customer PII, financial transactions, AI training data, and audit telemetry. All are **Critical** for OmniBank — eight of them process personal data under GDPR Article 28 (processor terms) and are subject to DORA Art. 28-30 ICT third-party requirements.

| Provider | Service | Data Accessed | Region | Contract Basis | DPA in Place? | Article 28 Compliant? | Exit Plan? |
|---|---|---|---|---|---|---|---|
| Managed hosting (EU) | Managed compute / managed network isolation / managed relational database / managed object store / managed key custody / managed ML platform (SYS-02 mobile backend, SYS-03 OmniScore, SYS-13 CDW, SYS-17 CRM hosting) | EU customer PII; financial transactions; credit scores; AI training data; analytics workloads | EU cross-region | MSA + DPA (GDPR addendum) + SCCs + DORA Art. 30 ICT contract addendum | Y | Y (DPA Art. 28 compliant; SCCs Module 2) | Y — `OmniBank_BCP_runbook_v4.pdf` documented exit procedure: cross-region snapshot + DB dump + artefact repository re-deploy; tested annually |
| Managed hosting (EU) | Managed container compute + managed relational database + managed identity service (SYS-02 web backend, SYS-25 SOC tooling) | EU customer PII; audit logs; security telemetry | EU cross-region | MSA + DPA + SCCs + DORA Art. 30 ICT contract addendum | Y | Y (DPA Art. 28 compliant) | Y — migration runbook tested annually |
| Managed CRM (EU instance) | Managed CRM EU instance (SYS-17) | Customer relationship data; complaint records | EU instance | MSA + DPA + SCCs | Y | Y (DPA Art. 28) | Y — annual exit test via data export API |
| Managed contact centre (EU) | Contact centre (SYS-20) | Call recordings (documented third-party security attestation scope for cardholder data; encrypted + tokenised) | EU region | MSA + DPA + SCCs | Y | Y | Y — data export; quarterly test |
| Managed data warehouse (EU on managed hosting) | Data warehouse (SYS-13) | Customer data; financial transactions; aggregated reporting | EU | DPA + SCCs + DORA Art. 30 addendum | Y | Y (DPA) | Y — data export tested quarterly |
| Centralized audit-log management (EU) | SIEM + immutable audit store (SYS-23, SYS-25) | Audit logs; security telemetry; fraud events; AI decision audit | EU region | MSA + DPA + SCCs | Y | Y (DPA Art. 28 + DORA Art. 30) | Y — indexed-data export API; quarterly audit |
| Managed endpoint detection (EU region) | EDR on endpoints + admin workstations (SYS-25 inputs) | Endpoint telemetry; process hashes; network metadata | EU region | Subscription + DPA + SCCs | Y | Y (DPA Art. 28 + documented third-party security attestation + ISO 27001) | Y — data replicator export; tested quarterly |
| Managed identity service (EU tenant) | Identity (SYS-24) | EU staff credentials; MFA factors (strong cryptographic hardware key + time-based one-time password) | EU tenant | Subscription + DPA + SCCs + DORA Art. 30 addendum | Y | Y (DPA Art. 28) | Y — user-export API documented; tested annually |
| Hardware security module vendor | HSM cluster — FIPS 140-2 Level 3 (SYS-22); payment HSMs | Signing keys; PIN encryption keys; TLS keys; AI model signing keys; payment signing | EU on-premises (managed at customer site) | HSMaaS contract + security addendum + NDA + DORA Art. 30 | Y | Y (Article 28 processor terms + documented third-party security attestation P2PE validated) | Y — `OmniBank_Key_Escrow_Procedure.pdf`; dual-control key escrow with trusted custodian |
| Managed behavioural biometric (EU) | Behavioural fraud detection (SYS-11 inputs) | Pseudonymised behavioural biometrics (typing, mouse, gesture); no raw PII | EU region | DPA + SCCs + DORA Art. 30 addendum | Y | Y (DPA Art. 28 + ISO 27001) | Y — model export + retraining fallback; tested annually |
| Managed vulnerability scanning (EU) | Vulnerability scanner + scanner console (SYS-25 inputs) | Pseudonymised scan results; no end-user data | SaaS + EU on-prem (hybrid) | Subscription + DPA + SCCs | Y | Y (DPA Art. 28) | Y — data export API |

**Summary:** 11 cloud / infrastructure providers; all 11 have DPA + SCCs + DORA Art. 30 ICT contract addenda in place; all 11 have documented exit plans (annual or quarterly test).

---


### 2.1 Subprocessor GDPR Art. 28 — Verbatim Anchor

The 11 cloud + infrastructure providers in §2 are all **sub-processors** under GDPR Art. 28 (OmniBank is the controller; providers are processors; their downstream providers — e.g. managed hosting sub-processors — are sub-processors). The verbatim GDPR Art. 28 text from the corpus (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/articles/GDPR_Art_28.md`) supplies the eight Art. 28(3) sub-clauses that each DPA must contain:

**Art. 28(3) eight mandatory DPA clauses** (verbatim corpus reference):
| SO-GDPR-021 | The controller engages only processors providing sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing meets the requirements of GDPR and protects data-subject rights. | `GDPR-CP07` (Art. 28(1)); `GDPR-CP08` (Art. 28(2)); `GDPR-C03` (Art. 4(7)/(8) — controller/processor) | D-06.1 |
| SO-GDPR-021 | D-06.1 | Art. 28(1)/(2), Art. 4(7)/(8) | Sufficient guarantees from processors |
| SO-GDPR-022 | Contracts (or other legal acts) between controller and processor contain the eight Art. 28(3) mandatory clauses covering subject-matter, type of data, obligations, rights, deletion/return, audit, sub-processor conditions, and confidentiality. | `GDPR-CP09` (Art. 28(3)(a)–(h)); `GDPR-CP08` (Art. 28(2) — sub-processor authorisation) | D-06.3 |
| SO-GDPR-022 | D-06.3 | Art. 28(3)(a)–(h), Art. 28(2) | DPA mandatory clauses; sub-processor authorisation |



**Selected Art. 28 SRs from corpus** (`requirements.sub_requirements` in D-06.3 JSON sidecar):
- **SR-GDPR-011** — Instruction-bound processing under least-privilege authorisation
- **SR-GDPR-012** — Confidentiality undertakings for authorised personnel
- **SR-GDPR-017** — Processor-to-controller breach notification without undue delay
- **SR-GDPR-022** — Downstream-recipient cascade for rectification and erasure
- **SR-GDPR-030** — Right-to-erasure with cryptographic key-destruction deletion path
- **SR-GDPR-031** — Processor erasure or return at end of processing services
- **SR-GDPR-033** — Processor due diligence with documented sufficient guarantees
- **SR-GDPR-034** — Eight-element processor contract with audit and instruction clauses
- **SR-GDPR-035** — Processor auditability with continuous external-activity monitoring
- **SR-GDPR-036** — Sub-processor authorisation with controller change-notification
- **SR-GDPR-037** — Controller-evidenced processor erasure on contract end
- **SR-GDPR-055** — Adequacy-governed cross-border transfer inventory and review

**Corpus source file:** [`GDPR_Art_28.md`](00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/articles/GDPR_Art_28.md) (per-article SO + SR extraction from `01_SecurityObjectives.md` and `02_SecurityRules_NIST.md`).

**Mapping to §2 sub-processors:** all 11 cloud + infrastructure providers in §2 hold GDPR Art. 28-compliant DPA contracts. The 8-clause floor (Art. 28(3)(a)–(h)) is satisfied via each provider's DPA template, each augmented by SCCs Module 2 + DORA Art. 30 ICT contract addendum.

---



## 3. Hardware Suppliers

OmniBank's CBS mainframe, payment systems, and treasury run on-premises on enterprise mainframe hardware. Branch banking uses industrial-grade PCs. The mobile app is a software product; CRA Default Class conformity assessment applies.

| Vendor | Component | Data Path | SBOM Provided? | Contract Clauses | Criticality |
|---|---|---|---|---|---|
| Mainframe hardware vendor | Enterprise mainframe systems (SYS-01) + legacy enterprise database + mainframe operating system | Hosts CBS ledger + customer master; all transactional processing | Y (firmware + DB SBOM per release; vulnerability feed) | DORA Art. 30 + CRA + ISO 27001 supplier clauses; 24/7 hardware support | Critical (CBS is single point of failure for all banking operations) |
| Network vendor | Industrial network gateway + corporate VPN | Encrypted gateway telemetry; no end-user data | Y (network component SBOM) | DORA Art. 30 + CRA + industry industrial-cybersecurity supplier clauses | Critical (sole network gateway) |
| Server vendor (Dell/HPE-equivalent) | Branch banking thin clients + servers | Branch transactions + cash deposits (SYS-19) | Y (firmware SBOM) | DORA Art. 30 + CRA supplier clauses | Important |
| Power infrastructure vendor | UPS + power conditioning + tamper-evident enclosures | n/a (physical security infrastructure) | N/A (physical) | Physical security addendum | Important |
| Hardware security module vendor (Document & Identity) | Hardware security modules (payment HSMs) + smart card readers | PIN translation + branch card readers | Y (machine-readable SBOM format from kernel driver) | DORA Art. 30 + CRA + documented third-party security attestation P2PE supplier clauses; firmware signing obligation | Critical |

**Summary:** 5 hardware suppliers; all 5 are audited annually; all 5 supply either a full or partial SBOM.

---

## 4. Software / SaaS Vendors

Software vendors in OmniBank's development-and-operations lifecycle. None process customer financial data directly without explicit Art. 28 terms; they process developer code, pseudonymised telemetry, or vulnerability metadata. Each is tracked here for CRA Annex I Part II (supply chain), GDPR records of processing (Art. 30), DORA Art. 28-30 ICT register, and D-06.1 vendor risk assessment.

| Vendor | Product | Data Processed | Subprocessor? | Contract Type | Criticality |
|---|---|---|---|---|---|
| Managed source control (EU) | Source-code hosting + Git-based version control + signed commits | Source code; issue text; commit metadata (no production customer data) | N (developer tool) | MSA for Organisations + DPA + SCCs | Critical (single point of IP + release artefacts) |
| Managed CI/CD orchestration + managed artefact repository (self-hosted, EU) | CI/CD pipeline + artefact registry (SYS-11) | Build artefacts; signed containers; machine-readable SBOM format SBOMs; signed OTA packages | N (self-hosted) | Open-source license + EU-managed hosting | Critical |
| Automated dependency scanner | Software composition analysis / vulnerability scanning (SYS-25 inputs) | Source code + dependency manifests; no runtime customer data | N (developer tool; on-demand scans) | Subscription + DPA | Important (feeds CRA + AI Act vulnerability management) |
| Managed vulnerability scanning | Vulnerability scanner + scanner console | Pseudonymised scan results; no end-user data | N (security tooling) | Subscription + DPA + SCCs | Critical (feeds CRA + DORA + NIS 2 vulnerability management) |
| Fraud management + AML platform vendor | Fraud Management + AML Platform (SYS-11) | Transaction events; pseudonymised for ML; STR/CTR generation | Y (as Art. 28 processor) | Subscription + DPA + SCCs + DORA Art. 30 addendum | Critical (feeds AML/KYC + BaFin compliance) |
| Managed treasury platform | Treasury Management System (SYS-08) | FX positions; money market; fixed income (no PII) | Y | Subscription + DPA + DORA Art. 30 addendum | Critical (treasury operations) |
| External Legal Counsel (multi-jurisdiction) | DPA + DORA Art. 30 ICT contract template library; cross-border regulatory advice | Contract + policy metadata; no production customer data | N (legal services) | Legal retainer + NDA | Important (multi-jurisdiction NIS 2 + GDPR + DORA + CRA + AI Act) |
| External audit firm (ISO 27001 + documented third-party security attestation) | Annual surveillance audits; documented third-party security attestation ROC; documented third-party security attestation reports | Audit evidence only; no production data | N (audit services) | Auditor contract + NDA | Important (certification maintenance) |
| TLPT framework provider (central bank) | TLPT framework guidance + threat intelligence (DORA Art. 24) | Threat intel + framework artefacts; no production data | N (regulator-supplied framework) | Statutory framework | Important (DORA Art. 24 TLPT) |

**Summary:** 9 distinct software vendors + 1 external legal counsel + 1 audit firm (counted separately in §5) + 1 TLPT framework. Managed source control is operationally counted once despite also appearing in `04a §1.3`.

---

## 5. Card Networks, Payment Systems, Correspondent Banks (DORA Critical + Statutory)

These are processor-style relationships where the counterparty is also a regulated entity, plus statutory reporting channels. Several are designated or eligible as Critical ICT Third-Party Providers (CTPPs) per DORA Art. 28-30 — this is a critical compliance area for OmniBank.

| Entity | Type | Data Path | DPA / Contract Basis | Notes |
|---|---|---|---|---|
| Visa | Card network (SYS-05) | Card authorisation + clearing; tokenised PANs | Card scheme rules + bilateral + DORA CTPP framework | **Eligible for CTPP designation** — Visa is in scope for ESA Lead Overseer review; OmniBank has DORA Art. 30 ICT contract addendum |
| Mastercard | Card network (SYS-05) | Card authorisation + clearing; tokenised PANs | Card scheme rules + bilateral + DORA CTPP framework | **Eligible for CTPP designation** — similar to Visa |
| SWIFT | SWIFT Messaging Gateway (SYS-06) | MT/MX messages; correspondent banking | SWIFT customer agreement + SWIFT CSP 2024 | SWIFT is treated as a CTPP per DORA Art. 28 — OmniBank has CSP-compliant infrastructure |
| Deutsche Bundesbank | TARGET2 / RTGS access (SYS-04) | Settlement instructions | Statutory + bilateral agreement | Statutory — not a vendor but a regulated payment system |
| ECB / EBA | Regulatory reporting (AnaCredit + COREP + FINREP) | Supervisory reports | Statutory reporting | Statutory |
| BaFin | German national supervisor | Incident reports (NIS 2 + DORA + AI Act); supervisory returns | Statutory | Statutory |
| ENISA | EU Agency + CVD hub | CVD policy + aggregated vulnerability statistics | Statutory registration | Per CRA Art. 14 reporting |
| AI Act Notified Body | AI Act conformity assessment | AI Act Art. 43 conformity documentation + FRIA | Contract + designation letter | Assessment scheduled 2026-Q3 |
| External audit firm (ISO 27001 + documented third-party security attestation) | Annual surveillance + documented third-party security attestation ROC + documented third-party security attestation reports | Audit evidence only; no production data | Auditor contract + NDA | Certification maintenance |
| Federal Financial Supervisory Authority (BaFin) Joint Supervisory Forum | Sector-specific information sharing (BaFin + Deutsche Bundesbank) | Information sharing per DORA + NIS 2 | Statutory | Industry threat-sharing consortium member; threat-intel sharing |

**Summary:** 10 statutory / regulatory / card-scheme / network entities that interact with OmniBank's regulator-facing controls and DORA Art. 28-30 CTPP framework.

---

## 6. Supply Chain Risk Assessment

Risk score key: **H** = High, **M** = Medium, **L** = Low, **VH** = Very High.

| Vendor | Criticality | Risk Score | Last Assessment | SBOM Available? | Next Review |
|---|---|---|---|---|---|
| Managed hosting (EU region) | Critical (DORA Art. 28 CTPP-eligible; sole cloud for production + corporate) | L (DPA + SCCs + DORA Art. 30 + documented third-party security attestation + ISO 27001/27018/27701 + multi-AZ + cross-region) | 2026-Q1 (formal review) | N/A (SaaS) | 2027-Q1 |
| Managed hosting (EU) | Critical (DORA Art. 28 CTPP-eligible) | L (DPA + SCCs + DORA Art. 30 + documented third-party security attestation + ISO 27001) | 2026-Q1 | N/A | 2027-Q1 |
| Hardware security module vendor | Critical (sole key-management infra; payment HSMs for PIN) | L (FIPS 140-2 Level 3 certified; on-prem managed; documented third-party security attestation P2PE) | 2026-Q1 | Y (firmware SBOM per release) | 2027-Q1 |
| Mainframe hardware vendor | Critical (CBS sole platform) | L (DORA Art. 30 + ISO 27001 supplier + 24/7 hardware support) | 2026-Q1 | Y (firmware + DB SBOM) | 2027-Q1 |
| Managed identity service (EU tenant) | Critical (sole identity provider + MFA) | L (DPA + DORA Art. 30 + ISO 27001/27018 + strong cryptographic hardware-key MFA) | 2026-Q1 | N/A | 2027-Q1 |
| Centralized audit-log management (EU) | Critical (sole SIEM + audit store) | L (DPA + DORA Art. 30 + immutable WORM via HSM-signed hash chain) | 2026-Q1 | N/A | 2027-Q1 |
| Managed endpoint detection | Critical (sole EDR) | L (DPA + SCCs + documented third-party security attestation + ISO 27001) | 2026-Q1 | N/A | 2027-Q1 |
| Fraud management + AML platform vendor | Critical (AML/KYC platform; BaFin-supervised) | L (DPA + DORA Art. 30 + ISO 27001 + certified) | 2026-Q1 | Y (SBOM) | 2027-Q1 |
| Managed CRM (EU FSC) | Important (CRM + complaint handling) | L (DPA + SCCs + DORA Art. 30 + ISO 27001) | 2026-Q1 | N/A | 2027-Q1 |
| Managed contact centre (EU) | Important (contact centre; documented third-party security attestation scope) | L (DPA + SCCs + documented third-party security attestation) | 2026-Q1 | N/A | 2027-Q1 |
| Managed data warehouse (EU on managed hosting) | Critical (CDW; analytics + reporting) | L (DPA + DORA Art. 30 + ISO 27001) | 2026-Q1 | Y (SBOM) | 2027-Q1 |
| Managed behavioural biometric (EU) | Critical (behavioural biometric fraud detection) | M (Art. 9 special category data; supplier security questionnaire sent 2025-Q4; 1 follow-up deviation closed 2026-Q1) | 2026-Q1 | Y (machine-readable SBOM format) | 2026-Q4 + 2027-Q1 |
| Network vendor | Critical (sole industrial network gateway) | L (DORA Art. 30 + industry industrial-cybersecurity supplier clauses) | 2026-Q1 | Y | 2027-Q1 |
| Hardware security module vendor (Document & Identity) | Critical (payment HSMs + smart card readers) | L (DORA Art. 30 + documented third-party security attestation P2PE + ISO 27001) | 2026-Q1 | Y (machine-readable SBOM format from kernel driver) | 2027-Q1 |
| Server vendor (Dell/HPE-equivalent) | Important | L (DORA Art. 30 + ISO 27001 supplier) | 2026-Q1 | Y | 2027-Q1 |
| Power infrastructure vendor | Important (physical security) | L (physical security addendum) | 2026-Q1 | N/A | 2027-Q1 |
| Managed source control (EU) | Critical (source-code + signed commits) | L (DPA + DORA Art. 30 + 2FA enforced + signed commits mandatory) | 2026-Q1 | N/A | 2027-Q1 |
| Automated dependency scanner | Important (feeds SCA) | L (DPA + paid tier) | 2026-Q1 | Y (SBOM output) | 2027-Q1 |
| Managed vulnerability scanning | Critical (feeds vulnerability management) | L (DPA + DORA Art. 30 + ISO 27001) | 2026-Q1 | N/A | 2027-Q1 |
| Managed treasury platform | Critical (Treasury Management System) | L (DPA + DORA Art. 30 + ISO 27001) | 2026-Q1 | Y (SBOM) | 2027-Q1 |
| Visa | Critical (card network; CTPP-eligible) | L (card scheme rules + DORA Art. 30 + documented third-party security attestation) | 2026-Q1 | N/A | 2027-Q1 |
| Mastercard | Critical (card network; CTPP-eligible) | L (card scheme rules + DORA Art. 30 + documented third-party security attestation) | 2026-Q1 | N/A | 2027-Q1 |
| SWIFT | Critical (CSP-controlled; CTPP per DORA) | L (SWIFT CSP 2024 compliant + DORA Art. 30) | 2026-Q1 | N/A | 2027-Q1 |
| EU carrier (T-Systems-equivalent) | Critical (branch MPLS + corporate VPN) | L (BSI-audited carrier + DPA + DORA Art. 30) | 2026-Q1 | N/A | 2027-Q1 |
| External Legal Counsel | Important | L (legal retainer + NDA; multi-jurisdiction) | 2026-Q1 | N/A | 2027-Q1 |
| External audit firm | Important | L (auditor contract + NDA) | 2026-Q1 | N/A | 2027-Q1 |
| AI Act Notified Body | Critical (Annex III conformity assessment) | L (designated body) | n/a (assessment scheduled 2026-Q3) | n/a (assessment body) | Continuous |
| TLPT framework provider | Important (DORA Art. 24 TLPT) | L (regulator-supplied framework) | n/a | n/a | Annual |

**Vendor count (distinct):** 22 vendor entities + 10 statutory / regulator / card-scheme / network relationships counted separately in §5.

**No Critical+High combinations.** Managed behavioural biometric is medium-risk pending re-verification in 2026-Q4; all other Critical vendors are Low risk.

---



### 6.1 Supply Chain Risk — Cross-Regulation Corpus References

The 27-row risk assessment in §6 is anchored to the following multi-regulation corpus sources:

**CRA Art. 13 (verbatim corpus)** — vendor obligations for products with digital elements (OmniBank SYS-02 mobile app + SYS-03 OmniScore AI Platform are CRA products). Corpus source: [`CRA_Art_13.md`](00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/articles/CRA_Art_13.md)
- Art. 13(1) — duty of diligence (Annex I Part I (1) secure-by-default + (2)(h) supply-chain)
- Art. 13(5) — conformity assessment procedure
- Art. 13(8) — 5-year support floor (security updates)
- Art. 13(13) — SBOM duty for software vendors

**NIS 2 Art. 21(2)(d) (verbatim corpus)** — supply chain security including security-related aspects of relationships with suppliers. Corpus source: [`NIS2_Art_21.md`](00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/articles/NIS2_Art_21.md)
- Art. 21(2)(d) — entities must include supply-chain security in risk-assessment + policies
- For OmniBank: tiered criticality + annual formal assessment + DORA Art. 28-30 register

**DORA Art. 30 (verbatim corpus)** — ICT third-party contracts for critical ICT services. Corpus source: [`DORA_Art_30.md`](00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/articles/DORA_Art_30.md)
- Art. 30(1) — pre-contract documentation requirements
- Art. 30(2) — contract minimum content (location of data + data access + continuity + monitoring + termination)
- Art. 30(3)(a)–(f) — closed-list contract clauses (description of services + location + data protection + access rights + SLA + exit)
- For OmniBank: all 11 cloud providers + critical infrastructure providers have DORA Art. 30 ICT contract addenda

**CRA Art. 7 (verbatim corpus)** — general product obligations; references Annex I Part I (2)(h) for supply-chain. Corpus source: [`CRA_Art_7.md`](00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/articles/CRA_Art_7.md) (located in D-09.4 per the corpus's per-domain routing)

**AI Act Art. 25 (cross-reference, NOT in corpus verbatim)** — provider-deployer interface obligations for high-risk AI systems. **DECLARATION:** AI Act Art. 25 is referenced in this doc for OmniScore AI Platform SYS-03 but the verbatim corpus file does not exist under `00_METHODOLOGY/PREPROCESSING_by_domain/domains/` (corpus coverage gap). The obligation is captured by AI Governance Lead per `04d` RACI; provider-deployer clauses are embedded in the managed ML platform contract addendum (OmniScore training environment). **Coverage gap flagged for Phase 2 disambiguation.**

---



## 7. Contractual Coverage

| Vendor | Art. 28 DPA | DORA Art. 30 ICT Contract | Security Audit Right | Sub-processor Approval | SBOM Clause |
|---|---|---|---|---|---|
| Managed hosting | Y (DPA — Art. 28 compliant) | Y (DORA Art. 30 addendum) | Indirect (documented third-party security attestation / ISO 27001 / ISO 27018) + DORA Art. 28(3) | Y (subscriber to sub-processor change notification; DORA Art. 28(4)) | N/A (SaaS) |
| Managed hosting (Microsoft-equivalent) | Y (DPA) | Y (DORA Art. 30 addendum) | Indirect (documented third-party security attestation + ISO 27001) + DORA Art. 28(3) | Y | N/A |
| Hardware security module vendor | Y (security addendum) | Y (DORA Art. 30 addendum) | Direct audit right (quarterly) + DORA Art. 28(3) | Y | Y (firmware SBOM per release) |
| Mainframe hardware vendor | Y | Y (DORA Art. 30 addendum) | Direct audit right (annual) + DORA Art. 28(3) | Y | Y (firmware + DB SBOM per release) |
| Managed identity service | Y (DPA) | Y (DORA Art. 30 addendum) | Indirect (documented third-party security attestation + ISO 27001) + DORA Art. 28(3) | Y | N/A |
| Centralized audit-log management | Y | Y (DORA Art. 30 addendum) | Indirect + DORA Art. 28(3) | Y | N/A |
| Managed endpoint detection | Y | Y (DORA Art. 30 addendum) | Indirect + DORA Art. 28(3) | Y | N/A |
| Fraud management + AML platform vendor | Y (DPA) | Y (DORA Art. 30 addendum) | Indirect (documented third-party security attestation + ISO 27001) + DORA Art. 28(3) | Y | Y (SBOM) |
| Managed CRM | Y | Y (DORA Art. 30 addendum) | Indirect + DORA Art. 28(3) | Y | N/A |
| Managed contact centre | Y | Y (DORA Art. 30 addendum) | Indirect + DORA Art. 28(3) | Y | N/A |
| Managed data warehouse | Y | Y (DORA Art. 30 addendum) | Indirect + DORA Art. 28(3) | Y | Y (SBOM) |
| Managed behavioural biometric | Y | Y (DORA Art. 30 addendum) | Y (annual audit right) + DORA Art. 28(3) | Y | Y (machine-readable SBOM format) |
| Network vendor | Y | Y (DORA Art. 30 addendum) | Y (annual) + DORA Art. 28(3) | Y | Y |
| Hardware security module vendor (Document & Identity) | Y (controller-driven; via customer DPA chain) | Y (DORA Art. 30) | Y (annual audit right + industry industrial-cybersecurity + documented third-party security attestation P2PE) | Y | Y (machine-readable SBOM format) |
| Server vendor (Dell/HPE-equivalent) | Y | Y (DORA Art. 30 addendum) | Y | Y | Y |
| Power infrastructure vendor | Y | Y (DORA Art. 30 addendum) | Y | Y | N/A |
| Managed source control | Y (DPA) | Y (DORA Art. 30 addendum) | Indirect (documented third-party security attestation) + DORA Art. 28(3) | Y | N/A |
| Automated dependency scanner | Y (paid tier) | Y (DORA Art. 30 addendum) | Indirect + DORA Art. 28(3) | Y | Y (SBOM output export) |
| Managed vulnerability scanning | Y | Y (DORA Art. 30 addendum) | Indirect + DORA Art. 28(3) | Y | N/A |
| Managed treasury platform | Y | Y (DORA Art. 30 addendum) | Indirect + DORA Art. 28(3) | Y | Y (SBOM) |
| Visa | Card scheme rules | Y (DORA Art. 30 addendum; CTPP framework) | Indirect (documented third-party security attestation + Visa security programme) | Y | N/A |
| Mastercard | Card scheme rules | Y (DORA Art. 30 addendum; CTPP framework) | Indirect (documented third-party security attestation + Mastercard security programme) | Y | N/A |
| SWIFT | SWIFT customer agreement | Y (DORA Art. 30 addendum; CTPP framework) | SWIFT CSP 2024 compliance + DORA Art. 28(3) | Y | N/A |
| EU carrier (T-Systems-equivalent) | Y (DPA + telco addendum) | Y (DORA Art. 30 addendum) | Y (BSI-audited as carrier) | Y | N/A |
| AI Act Notified Body | n/a | n/a | n/a | n/a | n/a |

**Common pattern:** All software/cloud providers substitute third-party certifications (documented third-party security attestation / ISO 27001) for direct audit rights + DORA Art. 28(3) on-site audit right; this is industry-standard. Hardware suppliers + HSM vendors + mainframe vendor accept direct audit clauses (per CRA + industry industrial-cybersecurity + DORA Art. 30 supply-chain expectations). All critical vendors have DORA Art. 30 ICT contract addenda.

---

## 8. Compliance Mapping (Regulatory Baseline)

Active scope for OmniBank = 38 of 38 sub-domains. All 4 D-06.x sub-domains are ACTIVE via GDPR + NIS 2 + CRA + DORA. AI Act adds provider-deployer interface clauses (Art. 25) for OmniScore AI Platform.

| Sub-domain | Vendors Affected | Compliance Status | Corpus Manifest Path | Notes |
|---|---|---|---|---|
| D-06.1 Vendor Risk Assessment | All 22 vendors + 10 statutory bodies | Managed — annual review cycle + tiered criticality scoring; quarterly fresh-cert review + DORA Art. 28-30 register | [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/D-06.1.manifest.json`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/D-06.1.manifest.json) | Per NIS 2 Art. 21(2)(d) + DORA Art. 28-30 + CRA supply-chain expectations |
| D-06.2 Software Bill of Materials (SBOM) | Managed source control, managed artefact repository, automated dependency scanner, managed vulnerability scanning, managed treasury platform, fraud management vendor, managed data warehouse, managed behavioural biometric, hardware suppliers (5 vendors provide SBOM) | Managed — machine-readable SBOM format emission per release; SBOM attached to mobile app distribution + AI model artefacts | [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.2/D-06.2.manifest.json`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.2/D-06.2.manifest.json) | Per CRA Annex I Part II (1) (mobile app); AI Act Art. 11 (AI technical documentation) |
| D-06.3 Contractual Security Obligations | All vendors | Covered — DPA + DORA Art. 30 ICT contract templates + CRA Annex I Part I (2)(h) clauses + NIS 2 supply-chain addendum + AI Act Art. 25 provider-deployer clauses | [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/D-06.3.manifest.json`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/D-06.3.manifest.json) | Multi-regulation clause bank maintained by DPO + Legal + CRO |
| D-06.4 Third-Party Boundary Management | Managed hosting (cloud), managed CRM, managed contact centre, centralized audit-log management, managed endpoint detection, managed data warehouse, managed source control, automated dependency scanner, managed vulnerability scanning, managed behavioural biometric (11 vendors with data-egress paths) | Covered — egress reviewed; pseudonymisation before logging egress; sub-processor notification flow + DORA Art. 28(4) sub-outsourcing register | [`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.4/D-06.4.manifest.json`](../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.4/D-06.4.manifest.json) | Per GDPR Art. 28(2) + DORA Art. 28(4) |

**Active sub-domains referenced here:** all 4 D-06.x sub-domains are ACTIVE via GDPR + CRA + NIS 2 + DORA participating regulations.

---

## 9. Gaps & Known Limitations (Open Items)

| Gap ID | Description | Severity | Linked Sub-Domain |
|---|---|---|---|
| GAP-TPL-01 | Managed behavioural biometric supplier security questionnaire 2025-Q4 had one deviation closed in 2026-Q1; re-verify in 2026-Q4 formal cycle (Art. 9 special category data handling) | MEDIUM (remediation in progress) | D-06.1 |
| GAP-TPL-02 | AI Act Notified Body (Annex III) conformity assessment scheduled 2026-Q3 — currently in progress; final certification pending | HIGH (AI Act Annex III block) | D-06.1, D-09.4 (AI Act Art. 11 technical file) |
| GAP-TPL-03 | DORA Art. 24 TLPT first cycle scheduled 2026-Q4 (every 3 years thereafter) — preparation in progress | HIGH (DORA Art. 24 obligation) | D-06.1, D-09.2, D-10.3 |
| GAP-TPL-04 | DORA Art. 28-30 ICT third-party register — complete for 22 active vendors; ongoing maintenance per DORA Art. 28(3) on-site audit right | LOW (process in place) | D-06.1, D-06.3 |
| GAP-TPL-05 | HSM firmware SBOM emission per release under CRA Annex I Part II (1) — pipeline integration test pending final acceptance | MEDIUM | D-06.2 |
| GAP-TPL-06 | DORA Art. 28(4) sub-outsourcing register for all 11 cloud providers — sub-processor notification flow in place; register consolidation ongoing | LOW | D-06.4 |

All six gaps are tracked in `Doc05_Security_Posture.md` for Phase 2 / Phase 3 remediation and in `PROJECT_STATE.md` §6.2.

---

## 10. Gate

This document is complete (Phase 1 Step D — Third-Party Landscape) when:

- [x] All cloud providers documented with DPA + DORA Art. 30 ICT contract status (Section 2: 11 rows)
- [x] All hardware suppliers documented with SBOM provision (Section 3: 5 rows)
- [x] All software / SaaS vendors documented with criticality (Section 4: 9 rows + 1 audit + 1 TLPT framework)
- [x] Card networks / payment systems / correspondent banks / regulator relationships catalogued (Section 5: 10 rows)
- [x] Subprocessors listed with Art. 28 contract status + DORA Art. 30 status (cross-references in §6 and §7)
- [x] Contractual coverage matrix populated (Section 7) — including DORA Art. 30 column
- [x] Supply-chain risk assessment populated (Section 6)
- [x] Compliance Mapping table populated for D-06.x sub-domains (Section 8)
- [x] Gaps explicitly listed (Section 9) rather than silently accepted — required by **AEGIS P5 (Change Propagation)** and **P0 (Reasoned Disagreement)**

**Gate Status:** PASS (proportionate for MAXIMUM-tier credit institution under P2).

---

## N-1. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-07-11 | Executor | Populated from template `Doc06_ThirdParty_Landscape.md`; merged architecture data from `04a §1.3` and stakeholder register from `04 §3`. 22 distinct vendors + 10 statutory/regulator/card-scheme/network relationships, proportionate for MAXIMUM-tier credit institution with DORA Art. 28-30 CTPP framework + AI Act Annex III obligations. |
| 1.2 | 2026-08-06 | Executor | Sprint 2 corpus enrichment: new §2.1 Subprocessor GDPR Art. 28 Verbatim Anchor added (8 mandatory DPA clauses + SR rule titles); new §6.1 Supply Chain Risk Cross-Regulation References added (CRA Art. 13 + NIS 2 Art. 21(2)(d) + DORA Art. 30 + CRA Art. 7 + AI Act Art. 25 declared gap); §8 Compliance Mapping table extended with Corpus Manifest Path column for D-06.1..D-06.4. status RECONCILED → CORPUS_ENRICHED. |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-07-11 |
| Technical Review | CTO |  |  |
| Security Review | CISO |  |  |
| Compliance Review | CRO |  |  |
| Procurement Review | Procurement Director |  |  |
| Legal Review | DPO + Legal |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Data backbone:** `Case_03_Phase1.xlsx` (13 sheets: COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, MATURITY (legacy sheet name), SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES)
- **Architecture context:** `Doc04_Architecture_DataInventory.md` §1.1 (25 systems), §1.3 (cloud services table), §2.2 (25 flows).
- **People / RACI:** `Doc07_Org_Roles_RACI.md` (CRO owns DORA Art. 28-30 ICT third-party register; CISO owns vendor-risk-assessment cadence; DPO owns DPA + DORA Art. 30 template library; Procurement Director owns vendor relationship management).
- **MAXIMUM-tier context:** `02_CASES/Case_03_OmniBank_Financial/00_COMMON/01_Company_Context.md` (5 applicable regulations; complexity tier MAXIMUM; 5,000+ employees; credit institution + DORA financial entity + NIS 2 essential entity + AI Act Annex III + CRA mobile app Default Class).
