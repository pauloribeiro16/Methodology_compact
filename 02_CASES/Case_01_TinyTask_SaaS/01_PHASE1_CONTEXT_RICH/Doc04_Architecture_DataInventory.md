---
document_id: AEGIS-P1-04a
title: Architecture & Data Inventory
phase: 1
version: 1.1
created: 2026-07-11
updated: 2026-08-06
author: Executor (Fase de Especificação 1 reconciliation; Fase de Especificação 2 corpus enrichment)
status: CORPUS_ENRICHED
case_study: TinyTask Lda.
sprint_role: reconciled_from_legacy
inputs:
  - Doc03_Company_Context_Assessment.md
  - Doc02_INTAKE_FORM.md
  - Doc08_Regulatory_Applicability.md
outputs:
  - Doc11_Structured_Compliance_Matrix.md
applicable_regs: [GDPR, CRA]
active_subdomains: 37
inactive_subdomains: [D-08.3]
related_documents:
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/index.md
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.4.md
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.manifest.json
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/D-09.4.manifest.json
---

> **Fase de Especificação 1 Reconciliation Note (2026-08-06)**
> Rich Mode copy of legacy `01_PHASE1_CONTEXT/04a_Architecture_DataInventory.md` (v1.0). Fase de Especificação 1 changes:
> - **I-10 (status DRAFT → RECONCILED):** Fase de Especificação 1 milestone.
> - **I-13 (02_Regulatory_Mapping_Master.md deprecation):** Not referenced. N/A.
> - Body content unchanged from legacy. Fase de Especificação 2 will replace `SubDomains/` paths with the new `PREPROCESSING_by_domain/domains/` corpus paths (L1/L2/L3/L4).
>
> **Fase de Especificação 2 Enrichment Note (2026-08-06)**
> - **Status: RECONCILED → CORPUS_ENRICHED.** Section 3 (Compliance Mapping) table extended with two corpus-derived columns: `Corpus Manifest Path` (path to per-sub-domain `D-XX.Y.manifest.json`) and `NIST CSF Anchors` (GDPR + CRA unique NIST controls). New §4 Corpus Provenance documents the extraction pattern and sources. 37 rows enriched (one per active sub-domain; D-08.3 inactive). Legacy `SubDomains/` paths preserved in column 6 for backwards compatibility — both corpora now point to the same sub-domains.

# Architecture & Data Inventory

## 1. Technical Architecture

TinyTask Lda. is a micro SaaS provider in Portugal with 8 employees, operating a productivity web application for EU customers. The company is a GDPR Controller for account and billing data, a GDPR Processor for B2B customer project content, and a CRA Manufacturer for the Team Organizer SaaS product. Operational posture is low-tier; regulatory complexity remains medium because GDPR and CRA both apply.

### 1.1 System Inventory

| System ID | Name | Type | Tech Stack | Owner | Criticality | Hosts Personal Data? |
|---|---|---|---|---|---|---|
| SYS-01 | Main SaaS Application | Cloud SaaS application | Node.js API, React web client, PostgreSQL driver | CTO and development team | Important | Y |
| SYS-02 | Auth Service | Managed identity service | Auth0 using OAuth 2.0 and OIDC | CTO | Important | Y |
| SYS-03 | Customer Data Store | Managed relational database | PostgreSQL on EU cloud region | CTO and lead developer | Critical | Y |
| SYS-04 | Cloud KMS | Managed key management | Cloud KMS with provider-managed key storage | CTO | Supporting | N |
| SYS-05 | Backup Store | Managed object storage | S3-compatible encrypted bucket | CTO | Important | Y |

### 1.2 Network Topology

Users access the React web client over HTTPS. The web client calls SYS-01 through the public application endpoint protected by TLS 1.3. SYS-01 runs in a cloud application environment and connects to SYS-03 over the provider internal network with encrypted database transport. SYS-01 sends authentication requests to SYS-02 using OAuth 2.0 and OIDC over HTTPS, emits pseudonymised operational logs to STORE-03, and sends billing metadata to Stripe for payment processing. SYS-05 receives scheduled encrypted backup exports from SYS-03. Administrative access is limited to the CTO and developers through Auth0 administrator accounts; MFA is enforced for administrators only.

TinyTask does not operate separate enterprise network zones, private SOC infrastructure, or a dedicated SIEM. Boundary controls are cloud-native security groups, managed identity controls, TLS, and least-privilege cloud IAM.

### 1.3 Cloud Services

| Provider | Service | Data Stored | Region | Contract Basis | DPA in Place? |
|---|---|---|---|---|---|
| AWS or equivalent EU cloud provider | PostgreSQL managed database | Customer accounts, project metadata, B2B project content | eu-west-1 or equivalent EU region | Cloud services agreement and DPA | Y |
| AWS or equivalent EU cloud provider | S3-compatible object storage | Encrypted database backups | eu-west-1 or equivalent EU region | Cloud services agreement and DPA | Y |
| AWS or equivalent EU cloud provider | Cloud KMS | Encryption keys and key metadata | EU region | Cloud services agreement and DPA | Y |
| Auth0 | Authentication and identity | Email identifiers, authentication metadata, session metadata | EU tenant where available | Auth0 subscription terms and DPA | Y |
| Stripe | Payment processing | Card/payment data, billing contact metadata | Stripe controlled processing locations | Stripe services agreement and DPA | Y |
| Datadog or equivalent | Logs and analytics | Pseudonymised event logs and operational metrics | EU site where available | Monitoring service agreement and DPA | Y |

### 1.4 Authentication & Identity Systems

| System | Purpose | MFA? | SSO? | Password Policy |
|---|---|---|---|---|
| SYS-02 Auth0 | Customer and administrator authentication | Admins only; optional for customers | OIDC for SYS-01 | Auth0 default password policy with minimum length and breached-password checks |
| Cloud provider IAM | Infrastructure administration | Y for CTO and developers | No enterprise SSO | Individual accounts with least-privilege roles; quarterly review not yet formalised |
| GitHub organisation | Source-code repository and pull requests | Y for developers | No enterprise SSO | GitHub enforced 2FA; branch protection limited to main branch |

## 2. Data Inventory

### 2.1 Data Stores

| Store ID | Type | Location | System | Encryption at Rest? | Owner | Retention Period | Backup? |
|---|---|---|---|---|---|---|---|
| STORE-01 | PostgreSQL database | EU cloud region | SYS-03 | Y, AES-256 provider-managed encryption using SYS-04 keys | CTO and lead developer | Active account lifetime plus 30 days after deletion request where legally permissible | Y |
| STORE-02 | Object storage backups | EU cloud region | SYS-05 | Y, SSE-KMS/AES-256 using SYS-04 keys | CTO | Daily backups for 30 days; monthly backups for 12 months | Y |
| STORE-03 | Logs and analytics | EU monitoring region where available | SYS-01 and monitoring provider | Y, provider-managed encryption; no raw task content intentionally logged | CTO | 30 days | N |

### 2.2 Data Flows

| Flow ID | Source | Destination | Data Type | Volume | Encryption in Transit? | Protocol | Subprocessor? |
|---|---|---|---|---|---|---|---|
| FLOW-01 | Web client | SYS-01 Main SaaS Application | Account data and project data | Low to medium | Y, TLS 1.3 | HTTPS REST | N |
| FLOW-02 | SYS-01 Main SaaS Application | STORE-01 Main PostgreSQL | Customer accounts, project data, audit metadata | Low to medium | Y, encrypted internal database transport | PostgreSQL TLS | N |
| FLOW-03 | SYS-01 Main SaaS Application | STORE-03 Logs and analytics | Pseudonymised events, request metadata, error traces | Low | Y, TLS 1.2 or higher | HTTPS agent/API | Y, Datadog or equivalent |
| FLOW-04 | Web client | SYS-02 Auth Service | Authentication credentials, email identifier, OIDC tokens | Low | Y, TLS 1.3 | OAuth 2.0/OIDC over HTTPS | Y, Auth0 |
| FLOW-05 | SYS-01 Main SaaS Application | Stripe | Billing metadata and hosted-checkout redirect; no card PAN stored by TinyTask | Low | Y, TLS 1.2 or higher | HTTPS API | Y, Stripe |

### 2.3 Personal Data Categories

| Category | Legal Basis (Art. 6 GDPR) | Systems Processing | Retention | Erasure Mechanism |
|---|---|---|---|---|
| Email addresses | Contract | SYS-01, SYS-02, SYS-03, STORE-01 | Account lifetime plus 30 days after deletion request where legally permissible | Manual admin deletion through support workflow; Auth0 deletion required separately |
| Names | Contract | SYS-01, SYS-03, STORE-01 | Account lifetime plus 30 days after deletion request where legally permissible | Manual admin deletion through support workflow |
| Project data uploaded by users | Contract | SYS-01, SYS-03, STORE-01, STORE-02 | Account or workspace lifetime; backups retained up to 12 months | Workspace deletion removes active records; backups expire by retention schedule |
| Payment and billing data | Contract | SYS-01 billing metadata, Stripe hosted checkout | Stripe retention under its processor/controller terms; TinyTask stores limited billing references | Deletion or anonymisation by support request; Stripe customer record deletion where legally permissible |

### 2.4 Data Subject Categories

| Subject Type | Data Categories | Access Mechanism | Erasure Mechanism |
|---|---|---|---|
| EU customers (B2B and B2C) | Email, name, account metadata, project data, billing metadata | In-app account view and support request | Manual support workflow; active records deleted and backup expiry relied on for residual copies |
| Free-tier users | Email, name where provided, project data, usage events | In-app account view and support request | Manual support workflow; inactive accounts reviewed ad hoc |
| Enterprise customer end users | Email, name, project data controlled by enterprise customer | Enterprise administrator export and support-assisted DSAR | Processor-assisted deletion on controller instruction under DPA |

## 3. Compliance Mapping (Regulatory Baseline)

This mapping uses the active TinyTask scope from `applicable_regs = [GDPR, CRA]`. The Regulatory Baseline source of truth is `../../../00_METHODOLOGY/PREPROCESSING/SubDomains/`. D-08.3 is excluded because it is inactive for TinyTask; its participating regulations are NIS2 and DORA only.

| Sub-domain | Relevant Systems | Relevant Data Stores | Relevant Data Flows | Regulatory Baseline Requirement IDs | SubDomains file | Corpus Manifest Path | NIST CSF Anchors |
|---|---|---|---|---|---|---|---|
| D-01.1 Data at Rest Encryption | SYS-03, SYS-04, SYS-05 | STORE-01, STORE-02, STORE-03 | FLOW-02 | 1.1; 1.1.1, 1.1.2, 1.1.3, 1.1.4 | [D-01.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.1.md) | `PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.manifest.json` | PR.DS-01, PR.DS-10 |
| D-01.2 Data in Transit Encryption | SYS-01, SYS-02, SYS-03 | STORE-01 | FLOW-01, FLOW-02, FLOW-03, FLOW-04, FLOW-05 | 1.2; 1.2.1, 1.2.2, 1.2.3 | [D-01.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.2.md) | `PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.2/D-01.2.manifest.json` | PR.DS-02, PR.IR-01 |
| D-01.3 Key Management | SYS-04 | STORE-01, STORE-02 | FLOW-02 | 1.3; 1.3.1, 1.3.2, 1.3.3 | [D-01.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.3.md) | `PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.3/D-01.3.manifest.json` | GV.OV-01, PR.AA-05, PR.DS-01, PR.IR-03 |
| D-01.4 Data Integrity Mechanisms | SYS-01, SYS-03, SYS-05 | STORE-01, STORE-02 | FLOW-02 | 1.4; 1.4.1, 1.4.2, 1.4.3, 1.4.4 | [D-01.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-01_Data-Protection/D-01.4.md) | `PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.4/D-01.4.manifest.json` | PR.DS-01, PR.DS-10, PR.DS-12, PR.PS-04 |
| D-02.1 Vulnerability Identification | SYS-01, SYS-02, SYS-03 | STORE-03 | FLOW-03 | 2.1; 2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5 | [D-02.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.1.md) | `PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.1/D-02.1.manifest.json` | ID.AM-02, ID.IM-02, ID.RA-01, ID.RA-05, PR.PS-02 |
| D-02.2 Patch Management | SYS-01, SYS-03 | STORE-03 | FLOW-03 | 2.2; 2.2.1, 2.2.2 | [D-02.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.2.md) | `PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.2/D-02.2.manifest.json` | GV.OV-02, ID.RA-01, ID.RA-06, PR.IR-03, PR.PS-01, PR.PS-02 |
| D-02.3 Coordinated Vulnerability Disclosure | SYS-01 | STORE-03 | FLOW-03 | 2.3; 2.3.1, 2.3.2 | [D-02.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.3.md) | `PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.3/D-02.3.manifest.json` | GV.PO-01, GV.SC-04, RS.CO-03 |
| D-02.4 Threat-Led Penetration Testing | SYS-01, SYS-02, SYS-03 | STORE-01 | FLOW-01, FLOW-04 | 2.4; 2.4.1, 2.4.2, 2.4.3 | [D-02.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-02_Vulnerability-Management/D-02.4.md) | `PREPROCESSING_by_domain/domains/D-02_Vulnerability-Management/D-02.4/D-02.4.manifest.json` | DE.CM-09, ID.RA-01, PR.PS-06 |
| D-03.1 Identity Lifecycle Management | SYS-02, cloud IAM, GitHub organisation | STORE-01 | FLOW-04 | 3.1; 3.1.1, 3.1.2, 3.1.3, 3.1.4 | [D-03.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.1.md) | `PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.1/D-03.1.manifest.json` | DE.CM-09, ID.AM-01, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06, PR.DS-12 |
| D-03.2 Multi-Factor Authentication | SYS-02, cloud IAM, GitHub organisation | STORE-01 | FLOW-04 | 3.2; 3.2.1, 3.2.2, 3.2.3, 3.2.4 | [D-03.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.2.md) | `PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.2/D-03.2.manifest.json` | DE.CM-09, ID.AM-01, PR.AA-01, PR.AA-05, PR.AA-06, PR.AT-02 |
| D-03.3 Authorisation & Least Privilege | SYS-01, SYS-02, SYS-03, SYS-04 | STORE-01, STORE-02 | FLOW-02, FLOW-04 | 3.3; 3.3.1, 3.3.2, 3.3.3, 3.3.4 | [D-03.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.3.md) | `PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.3/D-03.3.manifest.json` | DE.CM-09, ID.AM-01, PR.AA-01, PR.AA-05, PR.AA-06, PR.AT-02, PR.PS-04 |
| D-03.4 Secure System Defaults | SYS-01, SYS-02, SYS-03 | STORE-01 | FLOW-01, FLOW-04 | 3.4; 3.4.1, 3.4.2 | [D-03.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-03_Access-Control/D-03.4.md) | `PREPROCESSING_by_domain/domains/D-03_Access-Control/D-03.4/D-03.4.manifest.json` | GV.PO-01, GV.SC-03, PR.DS-12, PR.PS-01 |
| D-04.1 Incident Detection & Triage | SYS-01, SYS-03, STORE-03 monitoring | STORE-03 | FLOW-03 | 4.1; 4.1.1, 4.1.2, 4.1.3, 4.1.4 | [D-04.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.1.md) | `PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.1/D-04.1.manifest.json` | DE.AE-02, DE.CM-01, DE.CM-09, PR.PS-04, RS.MA-02 |
| D-04.2 Containment & Mitigation | SYS-01, SYS-02, SYS-03 | STORE-01, STORE-03 | FLOW-01, FLOW-03, FLOW-04 | 4.2; 4.2.1, 4.2.2, 4.2.3, 4.2.4 | [D-04.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.2.md) | `PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.2/D-04.2.manifest.json` | DE.CM-09, PR.DS-01, PR.DS-12, PR.IR-03, PR.IR-04, RC.RP-04, RS.MI-01, RS.MI-02 |
| D-04.3 Regulatory Notification | SYS-01, SYS-02, STORE-03 monitoring | STORE-03 | FLOW-03 | 4.3; 4.3.1, 4.3.2, 4.3.3, 4.3.4, 4.3.5 | [D-04.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.3.md) | `PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.3/D-04.3.manifest.json` | RS.AN-03, RS.AN-07, RS.CO-02, RS.CO-04, RS.MA-02, RS.MA-03 |
| D-04.4 Data Restoration & Recovery | SYS-03, SYS-05 | STORE-01, STORE-02 | FLOW-02 | 4.4; 4.4.1, 4.4.2, 4.4.3, 4.4.4 | [D-04.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-04_Incident-Response/D-04.4.md) | `PREPROCESSING_by_domain/domains/D-04_Incident-Response/D-04.4/D-04.4.manifest.json` | PR.DS-11, PR.DS-12, PR.IR-03, PR.IR-04, RC.RP-04 |
| D-05.1 Data Minimisation | SYS-01, SYS-03 | STORE-01, STORE-03 | FLOW-01, FLOW-03, FLOW-05 | 5.1; 5.1.1, 5.1.2, 5.1.3 | [D-05.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.1.md) | `PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.1/D-05.1.manifest.json` | GV.OC-03, GV.PO-01, ID.AM-03, PR.DS-12 |
| D-05.2 Retention & Archiving | SYS-03, SYS-05, STORE-03 monitoring | STORE-01, STORE-02, STORE-03 | FLOW-02, FLOW-03 | 5.2; 5.2.1, 5.2.2, 5.2.3 | [D-05.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.2.md) | `PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.2/D-05.2.manifest.json` | GV.OC-04, GV.OV-02, ID.AM-03, PR.DS-12, PR.PS-02 |
| D-05.3 Right to Erasure | SYS-01, SYS-02, SYS-03, SYS-05 | STORE-01, STORE-02 | FLOW-01, FLOW-04, FLOW-05 | 5.3; 5.3.1, 5.3.2 | [D-05.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.3.md) | `PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.3/D-05.3.manifest.json` | GV.SC-04, PR.DS-10, PR.DS-12 |
| D-05.4 Data Portability | SYS-01, SYS-03 | STORE-01 | FLOW-01 | 5.4; 5.4.1 | [D-05.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-05_Data-Lifecycle/D-05.4.md) | `PREPROCESSING_by_domain/domains/D-05_Data-Lifecycle/D-05.4/D-05.4.manifest.json` | PR.DS-10, PR.DS-12 |
| D-06.1 Vendor Risk Assessment | SYS-02, SYS-03, SYS-04, SYS-05, Stripe | STORE-01, STORE-02, STORE-03 | FLOW-03, FLOW-04, FLOW-05 | 6.1; 6.1.1, 6.1.2, 6.1.3, 6.1.4 | [D-06.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.1.md) | `PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/D-06.1.manifest.json` | GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04, ID.RA-02 |
| D-06.2 Software Bill of Materials | SYS-01 release pipeline | STORE-03 | FLOW-03 | 6.2; 6.2.1 | [D-06.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.2.md) | `PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.2/D-06.2.manifest.json` | GV.SC-02, GV.SC-03, ID.AM-02 |
| D-06.3 Contractual Security Obligations | SYS-02, SYS-03, SYS-05, Stripe, Datadog | STORE-01, STORE-02, STORE-03 | FLOW-03, FLOW-04, FLOW-05 | 6.3; 6.3.1, 6.3.2, 6.3.3, 6.3.4 | [D-06.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.3.md) | `PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/D-06.3.manifest.json` | GV.OC-03, GV.SC-02, GV.SC-03, GV.SC-04, PR.DS-12, RS.CO-04, RS.MI-01 |
| D-06.4 Third-Party Boundary Management | SYS-01, SYS-02, SYS-03, SYS-05 | STORE-01, STORE-02, STORE-03 | FLOW-03, FLOW-04, FLOW-05 | 6.4; 6.4.1, 6.4.2, 6.4.3, 6.4.4 | [D-06.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/D-06.4.md) | `PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.4/D-06.4.manifest.json` | GV.OC-02, GV.OC-03, GV.RR-02, GV.SC-02, GV.SC-03, GV.SC-04 |
| D-07.1 Secure-by-Design Principles | SYS-01, SYS-02, SYS-03 | STORE-01 | FLOW-01, FLOW-02, FLOW-04 | 7.1; 7.1.1, 7.1.2, 7.1.3, 7.1.4, 7.1.5 | [D-07.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.1.md) | `PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.1/D-07.1.manifest.json` | PR.DS-12, PR.PS-01, PR.PS-06 |
| D-07.2 Secure Coding Practices | SYS-01 release pipeline | STORE-03 | FLOW-03 | 7.2; 7.2.1, 7.2.2, 7.2.3 | [D-07.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.2.md) | `PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.2/D-07.2.manifest.json` | PR.PS-02, PR.PS-06 |
| D-07.3 CI/CD Pipeline Security | SYS-01 release pipeline | STORE-03 | FLOW-03 | 7.3; 7.3.1, 7.3.2 | [D-07.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.3.md) | `PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.3/D-07.3.manifest.json` | PR.PS-02, PR.PS-06 |
| D-07.4 Change Management | SYS-01, SYS-03 | STORE-01, STORE-03 | FLOW-03 | 7.4; 7.4.1, 7.4.2 | [D-07.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-07_Secure-Development/D-07.4.md) | `PREPROCESSING_by_domain/domains/D-07_Secure-Development/D-07.4/D-07.4.manifest.json` | GV.OV-01, GV.OV-02, GV.PO-02, GV.SC-04, ID.IM-04, PR.PS-02 |
| D-08.1 General Security Awareness | All production systems | STORE-01, STORE-02, STORE-03 | All production flows | 8.1; 8.1.1, 8.1.2, 8.1.3, 8.1.4 | [D-08.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.1.md) | `PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.1/D-08.1.manifest.json` | PR.AT-01, PR.AT-02 |
| D-08.2 Role-Specific Competence | SYS-01, SYS-02, SYS-03, SYS-04 | STORE-01, STORE-02 | FLOW-01, FLOW-02, FLOW-04 | 8.2; 8.2.1, 8.2.2, 8.2.3, 8.2.4, 8.2.5 | [D-08.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-08_Human-Factors/D-08.2.md) | `PREPROCESSING_by_domain/domains/D-08_Human-Factors/D-08.2/D-08.2.manifest.json` | GV.SC-03, PR.AT-01, PR.AT-02, PR.AT-04 |
| D-09.1 Information Security Policies | All production systems | STORE-01, STORE-02, STORE-03 | All production flows | 9.1; 9.1.1, 9.1.2, 9.1.3, 9.1.4, 9.1.5 | [D-09.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.1.md) | `PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.1/D-09.1.manifest.json` | GV.OC-03, GV.OV-03, GV.PO-01, GV.PO-02, GV.RM-04, GV.RR-01, GV.RR-02, GV.RR-03, GV.SC-01, GV.SC-04 |
| D-09.2 Impact & Risk Assessments | SYS-01, SYS-02, SYS-03, SYS-05 | STORE-01, STORE-02, STORE-03 | FLOW-01, FLOW-02, FLOW-03, FLOW-04, FLOW-05 | 9.2; 9.2.1, 9.2.2, 9.2.3, 9.2.4, 9.2.5 | [D-09.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.2.md) | `PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.2/D-09.2.manifest.json` | ID.RA-04, ID.RA-05, ID.SC-04 |
| D-09.3 Asset Inventories | SYS-01, SYS-02, SYS-03, SYS-04, SYS-05 | STORE-01, STORE-02, STORE-03 | FLOW-01, FLOW-02, FLOW-03, FLOW-04, FLOW-05 | 9.3; 9.3.1, 9.3.2, 9.3.3 | [D-09.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.3.md) | `PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.3/D-09.3.manifest.json` | ID.AM-01, ID.AM-02 |
| D-09.4 Records of Processing | SYS-01, SYS-02, SYS-03, SYS-05, Stripe | STORE-01, STORE-02, STORE-03 | FLOW-01, FLOW-02, FLOW-03, FLOW-04, FLOW-05 | 9.4; 9.4.1, 9.4.2, 9.4.3, 9.4.4, 9.4.5 | [D-09.4.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-09_Governance-Documentation/D-09.4.md) | `PREPROCESSING_by_domain/domains/D-09_Governance-Documentation/D-09.4/D-09.4.manifest.json` | GV.PO-02, ID.AM-08, ID.RA-05, PR.DS-12 |
| D-10.1 Continuous Security Monitoring | SYS-01, SYS-03, STORE-03 monitoring | STORE-03 | FLOW-03 | 10.1; 10.1.1, 10.1.2, 10.1.3, 10.1.4, 10.1.5 | [D-10.1.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.1.md) | `PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.1/D-10.1.manifest.json` | DE.AE-02, DE.CM-01, DE.CM-09, ID.IM-04 |
| D-10.2 Audit Logging & Traceability | SYS-01, SYS-02, SYS-03 | STORE-03 | FLOW-03, FLOW-04 | 10.2; 10.2.1, 10.2.2, 10.2.3, 10.2.4 | [D-10.2.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.2.md) | `PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.2/D-10.2.manifest.json` | DE.CM-01, GV.PO-02, ID.RA-04, PR.DS-11, PR.IP-06, PR.PT-01 |
| D-10.3 Compliance Testing | SYS-01, SYS-02, SYS-03, SYS-05 | STORE-01, STORE-02, STORE-03 | All production flows | 10.3; 10.3.1, 10.3.2, 10.3.3, 10.3.4, 10.3.5 | [D-10.3.md](../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-10_Monitoring-Audit/D-10.3.md) | `PREPROCESSING_by_domain/domains/D-10_Monitoring-Audit/D-10.3/D-10.3.manifest.json` | DE.AE-02, GV.OV-03, ID.RA-05, PR.IP-07 |

## 4. Corpus Provenance (Fase de Especificação 2 Enrichment)

The "Corpus Manifest Path" and "NIST CSF Anchors" columns added to the Section 3 table above were extracted from the corpus at `00_METHODOLOGY/PREPROCESSING_by_domain/domains/`. The full extraction pattern was:

```bash
for sd in D-XX.Y; do
  path=$(find . -name "${sd}.manifest.json" -path "*/${sd}/*" 2>/dev/null | head -1)
  nist=$(jq -r '[.applicable_nist_controls_by_regulation.GDPR[]?, .applicable_nist_controls_by_regulation.CRA[]?] | unique | join(", ")' "$path")
  echo "${sd}|${path}|${nist}"
done
```

**Source corpus layer:** Per-sub-domain manifest (`D-XX.Y.manifest.json`) under `PREPROCESSING_by_domain/domains/<D-XX_Domain>/D-XX.Y/`.

**Scope:** 37 active sub-domains. D-08.3 (Management Board Training) is excluded — its participating regulations are NIS2 and DORA only, neither applicable to TinyTask (per `05_Regulatory_Applicability.md §6.3` and Doc 04a §3 narrative).

**NIST CSF Anchors column:** Union of GDPR + CRA applicable NIST controls per sub-domain. Some entries carry parenthetical qualifications preserved verbatim from the corpus (e.g., `PR.DS-12 (+ PR.DS-02 for the second limb)`); these reflect corpus annotation rather than distinct controls. See SPRINT2_ENRICHMENT_REPORT_EXISTING.md §3 for extraction notes.

**Provenance note:** Path values in the table are relative-to-repo-root paths to the per-sub-domain manifest files. Total corpus lookups: 37 (one per active sub-domain).

## 5. Gate

| Gate Criterion | Status | Evidence |
|---|---|---|
| All production systems are inventoried | PASS | 5 systems documented in Section 1.1 |
| All data stores documented with encryption status | PASS | 3 stores documented in Section 2.1 |
| All data flows documented with encryption status | PASS | 5 flows documented in Section 2.2 |
| Personal data categories enumerated with legal basis | PASS | 4 categories documented in Section 2.3 |
| Compliance mapping table populated for all active sub-domains | PASS | 37 active SubDomains rows in Section 3; D-08.3 explicitly inactive |
| Proportionality maintained for low-tier micro SaaS | PASS | Managed services used; no enterprise HSM, SOC, SIEM, or formal CMDB claimed |

## N-1. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-07-11 | Executor | Created TinyTask populated architecture and data inventory from the 04a template |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-07-11 |
| Technical Review | CTO |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Data backbone:** `Case_01_Phase1.xlsx` (13 sheets: COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, POSTURE, SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES)
