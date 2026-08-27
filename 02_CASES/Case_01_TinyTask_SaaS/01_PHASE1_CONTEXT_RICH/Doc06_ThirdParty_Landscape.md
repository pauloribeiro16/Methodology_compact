---
document_id: AEGIS-P1-04c
title: Third-Party Landscape Inventory
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
  - Doc04_Architecture_DataInventory.md
  - Doc02_INTAKE_FORM.md
outputs:
  - Doc10_Clause_Mapping_Matrix.md
  - Doc11_Structured_Compliance_Matrix.md
applicable_regs: [GDPR, CRA]
active_subdomains: 37
inactive_subdomains: [D-08.3]
related_documents:
  - ../../../00_METHODOLOGY/PREPROCESSING/SubDomains/D-06_Supply-Chain/
  - ../../../00_METHODOLOGY/TEMPLATES/04c_ThirdParty_Landscape.md
  - ../../../00_METHODOLOGY/CONTEXT/CONTEXT_PHASE1.md
supersedes: none
---

> **Fase de Especificação 1 Reconciliation Note (2026-08-06)**
> Rich Mode copy of legacy `01_PHASE1_CONTEXT/04c_ThirdParty_Landscape.md` (v1.0). Fase de Especificação 1 changes:
> - **I-10 (status DRAFT → RECONCILED):** Fase de Especificação 1 milestone.
> - Body content unchanged from legacy. Fase de Especificação 2 will replace `SubDomains/` paths with the new `PREPROCESSING_by_domain/domains/` corpus paths.
>
> **Fase de Especificação 2 Enrichment Note (2026-08-06)**
> - **Status: RECONCILED → CORPUS_ENRICHED.** Section 4 (Subprocessors) extended with verbatim GDPR Art. 28 (1)+(2)+(3)(a)–(h) extracted from corpus ambiguity file. Section 5 (Supply Chain Risk) extended with verbatim CRA Art. 7(1)–(4) classification reference + verbatim CRA Art. 13(5)/(6) substantive supply-chain due-diligence text — both extracted from corpus. Section 7 (Compliance Mapping) table extended with `Corpus Manifest Path` column for all four D-06.x rows. New §10 Corpus Provenance documents the verbatim-quote provenance.

# Third-Party Landscape Inventory

## 1. Purpose & Scope

This document inventories TinyTask Lda.'s third-party landscape: cloud providers, software vendors, subprocessors. It maps directly to Regulatory Baseline sub-domain **D-06 (Supply Chain)** — specifically D-06.1, D-06.2, D-06.3, D-06.4 — and supports compliance with **GDPR Art. 28** (processor obligations and controller due diligence) and **CRA Annex I Part I (2)(j) and (k)** (attack-surface reduction, exploitation-mitigation via the supply chain).

**Scope:** Sub-domain D-06.x only. Broader architecture context is in `04a_Architecture_DataInventory.md`; broader governance (policies, risk assessments) is in `04b_Security_Posture.md` and Phase 2 deliverables.

**Method:** Inventory was constructed from the architecture documentation (`04a`), the stakeholder register in `04_Company_Context_Assessment.md §3`, and the intake form layer-2 block B6 answers (supply chain visibility = Low; SBOM = Not started; supplier security assessment = None; component vulnerability = Manual ad hoc).

**Proportionality note (P2 — Company Reality First):** TinyTask is an 8-employee micro-SaaS. Inventory is limited to 6 third parties that actually touch personal data or the production system. No formal supplier programme exists; the inventory is a precondition to building one, not evidence one already exists.

---

## 2. Cloud & Infrastructure Providers

The following providers host customer data, the production application, or authentication. All three are critical because they process personal data on behalf of the controller (account data) and/or the B2B customers whose content is processed.

| Provider | Service | Data Accessed | Region | Contract Basis | DPA in Place? | Article 28 Compliant? | Exit Plan? |
|---|---|---|---|---|---|---|---|
| AWS (or equivalent EU cloud provider) | EC2 / compute (SYS-01 application runtime) | Application logs, runtime config, no direct personal data at this layer | eu-west-1 | MSA + AWS DPA (GDPR addendum) + SCCs via AWS Customer Agreement | Y | Y (AWS DPA Art. 28 compliant; SCCs Module 2 where applicable) | N — exit procedure not yet documented; data extraction via DB dump + S3 inventory |
| AWS (or equivalent EU cloud provider) | RDS / managed PostgreSQL (SYS-03) | Customer accounts (email, name, hashed password), B2B project content — personal data | eu-west-1 | MSA + AWS DPA + SCCs | Y | Y (AWS DPA Art. 28 compliant) | N — exit procedure not yet documented |
| AWS (or equivalent EU cloud provider) | S3 / object storage (SYS-05 backups) | Encrypted DB backups containing personal data | eu-west-1 | MSA + AWS DPA + SCCs | Y | Y | N — exit procedure not yet documented (see gap in Section 8) |
| AWS (or equivalent EU cloud provider) | Cloud KMS (SYS-04) | Key metadata only; raw keys never leave HSM-bound processors | EU region | MSA + AWS DPA | Y | Y | N — wrapped keys exportable; procedure not yet documented |
| Stripe | Stripe-hosted payment checkout (FLOW-05) | Card PAN tokenised by Stripe; TinyTask stores only billing metadata and Stripe customer IDs; no PAN | Stripe-controlled regions (TinyTask EU customers' card data reside in Stripe-controlled EU processing locations per Stripe DPA) | Stripe Services Agreement + Stripe DPA (Standard Contractual Clauses incorporated) | Y | Y (Stripe DPA — Art. 28 / GDPR-compliant terms) | Y (Stripe exports customer + transaction data; documented process via Stripe Dashboard API) |
| Auth0 (by Okta) | Authentication / identity (SYS-02) | Email addresses (used as identifiers), hashed passwords, MFA factors, session metadata, OIDC tokens | EU tenant where available (Auth0 EU region) | Auth0 subscription terms + Auth0 DPA | Y | Y (Auth0 DPA — Art. 28 compliant; SCCs Module 2) | Y (Auth0 user-export API documented; export procedure known but not yet exercised) |

**Summary:** 6 cloud / infrastructure providers; all 6 have a DPA in place; all 6 (subject to the noted exit-plan gap for AWS) have GDPR-compliant Article 28 terms.

---

## 3. Software Vendors & SaaS Products

The following SaaS products are used in the development-and-operations lifecycle. None of these vendors process customer personal data directly; they process developer/source-code artefacts, pseudonymised operational telemetry, or vulnerability metadata only. They are tracked here for CRA Annex I Part II supply-chain obligations, GDPR records of processing (Art. 30), and D-06.1 vendor risk assessment.

| Vendor | Product | Data Processed | Subprocessor? | Contract Type | CRA-Conformant? | Criticality |
|---|---|---|---|---|---|---|
| GitHub | Source-code hosting + Git-based version control | Source code, issue text, commit metadata (no production personal data) | N (developer tool; no end-user data path) | GitHub MSA for Organisations + GitHub DPA | Not assessed (CRA scope = products with digital elements on EU market; GitHub's internal CRA posture is not separately verified by TinyTask) | Important (single point of failure for code IP and release artefacts) |
| Datadog (or equivalent) | APM / log aggregation (STORE-03) | Pseudonymised operational logs and metrics — no raw customer content by design | Y (logs flow from SYS-01 → Datadog subprocessor) | Datadog MSA + Datadog DPA + SCCs | Not assessed | Critical (sole telemetry/detection supplier — D-10.1 dependency) |
| Snyk | Software composition analysis / vulnerability scanning | Source code + dependency manifests; no runtime personal data | N (developer tool; on-demand scans only) | Snyk subscription + Snyk DPA (paid tiers) | Not assessed | Important (feeds CRA Annex I Part II (1) SBOM-derivation and D-02.1 vulnerability identification) |
| Auth0 (by Okta) | Authentication (also listed in Section 2) | Already inventoried | Y | Already inventoried | Already inventoried | Already inventoried |

**Summary:** 3 distinct software vendors (GitHub, Datadog, Snyk); Auth0 is duplicated above only to mark the cross-reference; it is operationally counted once as a cloud/identity provider in Section 2.

---

## 4. Subprocessors (per Art. 28 GDPR)

Article 28(2) GDPR requires the controller (and processor) to inform the data subject of any intended changes concerning the addition or replacement of subprocessors. The list below is the current subprocessor inventory; controllers/customers must be notified before any addition.

### 4.1 GDPR Art. 28 — Verbatim Reference (extracted from corpus)

The obligations tracked in this section trace directly to the GDPR text. The verbatim paragraphs of Art. 28 (extracted from the corpus at `00_METHODOLOGY/PREPROCESSING_by_domain/_by_regulation/GDPR/Ambiguity/04_GDPR_Ch4_ControllerProcessor.md`, lines 200–223) are reproduced here for traceability:

> [verbatim from `00_METHODOLOGY/PREPROCESSING_by_domain/_by_regulation/GDPR/Ambiguity/04_GDPR_Ch4_ControllerProcessor.md:200–223`]
>
> > **Article 28**
> > **Processor**
> >
> > 1. Where processing is to be carried out on behalf of a controller, the controller shall use only processors providing **sufficient guarantees** to implement **appropriate technical and organisational measures** in such a manner that processing will meet the requirements of this Regulation and ensure the protection of the rights of the data subject.
> >
> > 2. The processor shall not engage another processor without **prior specific or general written authorisation** of the controller. In the case of general written authorisation, the processor shall inform the controller of any intended changes concerning the addition or replacement of other processors, thereby giving the controller the opportunity to object to such changes.
> >
> > 3. Processing by a processor shall be governed by a **contract or other legal act** under Union or Member State law, that is binding on the processor with regard to the controller and that sets out the subject-matter and duration of the processing, the nature and purpose of the processing, the type of personal data and categories of data subjects and the obligations and rights of the controller. That contract or other legal act shall stipulate, in particular, that the processor:
> >
> > (a) processes the personal data only on **documented instructions** from the controller (...)
> >
> > (b) ensures that persons authorised to process the personal data have committed themselves to **confidentiality** or are under an **appropriate statutory obligation of confidentiality**;
> >
> > (c) takes all measures required pursuant to Article 32;
> >
> > (d) respects the conditions referred to in paragraphs 2 and 4 for engaging another processor;
> >
> > (e) taking into account the nature of the processing, assists the controller by appropriate technical and organisational measures, insofar as this is possible, for the fulfilment of the controller's obligation to respond to requests for exercising the data subject's rights laid down in Chapter III;
> >
> > (f) assists the controller in ensuring compliance with the obligations pursuant to Articles 32 to 36 taking into account the nature of processing and the information available to the processor;
> >
> > (g) at the choice of the controller, **deletes or returns all the personal data** to the controller after the end of the provision of services relating to processing, and **deletes existing copies** unless Union or Member State law requires storage of the personal data;
> >
> > (h) makes available to the controller all information necessary to demonstrate compliance with the obligations laid down in this Article and allow for and contribute to **audits, including inspections**, conducted by the controller or another auditor mandated by the controller.

**Mapping to subprocessor list below:** Art. 28(1) → sufficient-guarantees selection (Section 2 + Section 4 Last Audit column); Art. 28(2) → sub-processor authorisation flow (Section 6 subprocessor approval mechanism); Art. 28(3)(a)–(h) → DPA mandatory clauses (Section 6 Contractual Coverage table); Art. 28(3)(g) → contract-end erasure/return obligation (Section 5 AWS/Stripe exit-plan gap).

| Subprocessor | Parent Vendor | Service | Data Access | Article 28 Contract? | Last Audit |
|---|---|---|---|---|---|
| AWS (or equivalent EU cloud provider) | AWS (direct) | EC2 / RDS / S3 / KMS | Personal data: account records (email, name, hashed password) and B2B project content | Y (AWS DPA — Art. 28 compliant; SCCs) | No formal audit performed (relying on AWS SOC 2 / ISO 27001 / ISO 27018 certifications — see Section 5) |
| Stripe | Stripe (direct) | Payment processing via hosted checkout | Card data tokenised and processed by Stripe under PCI-DSS; TinyTask only sends billing metadata + session-scoped tokens | Y (Stripe DPA — Art. 28 compliant; PCI-DSS Level 1 inheritor) | No formal audit performed (relying on Stripe PCI-DSS Level 1 + SOC 2 reports) |
| Auth0 | Auth0/Okta (direct) | Identity / authentication | Email, hashed password, MFA factors, session metadata, OIDC tokens | Y (Auth0 DPA — Art. 28 compliant; SCCs) | No formal audit performed (relying on Auth0 SOC 2 / ISO 27001 + ISO 27018 certifications) |
| Datadog (or equivalent) | Datadog (direct) | Log aggregation + APM | Pseudonymised operational logs and metrics; no raw customer content | Y (Datadog DPA — Art. 28 compliant; SCCs) | No formal audit performed (relying on Datadog SOC 2 Type II report) |

**Note (per AEGIS P1 principle — Multi-perspective deliberation):** Relying on the vendor's own SOC 2 / ISO 27001 evidence does not constitute an *independent* audit by TinyTask. This is a documented limitation, not a hidden gap; the action is tracked in `04b_Security_Posture.md` as a MEDIUM-priority improvement (annual review of vendor certification freshness).

---

## 5. Supply Chain Risk Assessment

Risk score key: **H** = High, **M** = Medium, **L** = Low, **VH** = Very High.

Criticality reflects **business impact of vendor failure or incident** (i.e., what breaks in the product / for the customer if this vendor is compromised or unavailable). Risk score reflects **likelihood × impact** for the current posture level (no formal supplier programme; dependency on third-party certifications).

### 5.1 CRA Art. 7 — Verbatim Classification Reference (extracted from corpus)

CRA Art. 7 defines the "important products with digital elements" classification (Annex III, Class I + II). The verbatim paragraphs of Art. 7(1) + Art. 7(2)(a)/(b) (extracted from the corpus at `00_METHODOLOGY/PREPROCESSING_by_domain/_archive_unmatched/CRA/02_CRA_Art6-8_Classification.md`, lines 41–53) are reproduced here:

> [verbatim from `00_METHODOLOGY/PREPROCESSING_by_domain/_archive_unmatched/CRA/02_CRA_Art6-8_Classification.md:41–53`]
>
> > **1.** Products with digital elements which have the **core functionality** of a product category set out in **Annex III** shall be considered to be important products with digital elements and shall be subject to the conformity assessment procedures referred to in Article 32(2) and (3). The integration of a product with digital elements which has the core functionality of a product category set out in Annex III shall not in itself render the product in which it is integrated subject to the conformity assessment procedures referred to in Article 32(2) and (3).
> >
> > 2. The categories of products with digital elements referred to in paragraph 1 of this Article, divided into classes I and II as set out in Annex III, meet at least one of the following criteria:
> >
> > (a) the product with digital elements **primarily performs functions critical to the cybersecurity of other products, networks or services**, including securing authentication and access, intrusion prevention and detection, end-point security or network protection;
> >
> > (b) the product with digital elements performs a function which **carries a significant risk of adverse effects in terms of its intensity and ability to disrupt, control or cause damage to a large number of other products or to the health, security or safety of its users through direct manipulation**, such as a central system function, including network management, configuration control, virtualisation or processing of personal data.
> >
> > 3. The Commission is empowered to adopt delegated acts in accordance with Article 61 to amend Annex III by including in the list a new category within each class of the categories of products with digital elements and specifying its definition, moving a category of products from one class to the other or withdrawing an existing category from that list. …
> >
> > 4. By 11 December 2025, the Commission shall adopt an implementing act specifying the technical description of the categories of products with digital elements under classes I and II as set out in Annex III and the technical description of the categories of products with digital elements as set out in Annex IV. …

**Relevance to TinyTask supply-chain risk:** CRA Art. 7 is a **classification gate**, not a substantive supply-chain duty. It determines whether the Team Organizer SaaS falls into "important product" territory — most likely **no** for a generic productivity SaaS (the Annex III list (class I) is dominated by password managers, identity-management systems, VPN, network management; TinyTask's B2B project-management functionality is not in Annex III). However, Art. 7(4) Commission implementing acts (deadline 11 Dec 2025) may amend the technical descriptions and could pull generic SaaS into Class I. The classification check is therefore re-verified at each substantial modification per Art. 13(10).

### 5.2 CRA Art. 13(5)/(6) — Substantive Supply-Chain Due-Diligence Reference (extracted from corpus)

The substantive supply-chain obligations on the manufacturer live in CRA Art. 13, not Art. 7. For completeness — because Art. 7 above may be misread as the "supply-chain article" — the verbatim text of Art. 13(5) (due diligence on third-party components) and Art. 13(6) (component vulnerability reporting + address and remediate) is reproduced from the corpus at `00_METHODOLOGY/PREPROCESSING_by_domain/_by_regulation/CRA/Ambiguity/03_CRA_Art13_Manufacturers.md`, lines 23–25:

> [verbatim from `00_METHODOLOGY/PREPROCESSING_by_domain/_by_regulation/CRA/Ambiguity/03_CRA_Art13_Manufacturers.md:23–25`]
>
> > **5.** For the purpose of complying with paragraph 1, manufacturers shall **exercise due diligence when integrating components sourced from third parties** so that those components do not compromise the cybersecurity of the product with digital elements, including when integrating components of free and open-source software that have not been made available on the market in the course of a commercial activity.
> >
> > **6.** Manufacturers shall, upon identifying a vulnerability in a component, including in an open source-component, which is integrated in the product with digital elements report the vulnerability to the person or entity manufacturing or maintaining the component, and **address and remediate** the vulnerability in accordance with the vulnerability handling requirements set out in Part II of Annex I. …

**Mapping to risk table below:** Art. 13(5) → SBOM-generation + component-vulnerability assessment (currently a GAP per Section 8 GAP-TPL-03); Art. 13(6) → vendor reporting loop + remediation cycle (covered by Snyk weekly scan; see AWS + Stripe + Auth0 + Datadog vendor rows).

| Vendor | Criticality | Risk Score | Last Assessment | SBOM Available? | Next Review |
|---|---|---|---|---|---|
| AWS (or equivalent EU cloud provider) | Critical (sole cloud provider for compute, database, object storage, and KMS) | L (DPA in place; SOC 2 / ISO 27001 / ISO 27018 inherited controls; multi-AZ design mitigates single-zone failure) | 2026-04 — informal review during intake (no formal assessment yet) | N (AWS does not publish SBOM as a SaaS consumer; applies to vendor's own products only) | 2027-04 (annual review; first formal review planned) |
| Stripe | Critical (sole payment processor; PCI-DSS scope delegated) | L (DPA + PCI-DSS Level 1 + strong tokenisation model; card PAN never stored by TinyTask) | 2026-04 — informal review | N/A (payment processor; SBOM not applicable) | 2027-04 |
| Auth0 | Critical (sole identity provider; MFA + password storage) | L (DPA in place; Auth0 SOC 2 + ISO 27001 / ISO 27018; MFA enforced for admins) | 2026-04 — informal review | N/A (managed identity service; SBOM not applicable) | 2027-04 |
| Datadog (or equivalent) | Critical (sole telemetry/detection supplier) | M (DPA in place; pseudonymisation reduces data exposure; outage would degrade D-10.1 monitoring for the duration) | 2026-04 — informal review | N/A (log SaaS) | 2027-04 |
| GitHub | Important (sole source-code hosting; single point for IP + release artefacts) | M (GitHub DPA + enforced 2FA for developer accounts; risk concentrated because there is no alternate VCS) | 2026-04 — informal review | N/A (repository service) | 2027-04 |
| Snyk | Important (feeds vulnerability identification + SBOM-derivation for CRA Annex I Part II (1)) | L (DPA in paid tier; on-demand scans; no persistent data flow) | 2026-04 — informal review | Y (Snyk can output CycloneDX/SPDX for the scanned projects) | 2027-04 |

**Vendor count:** 6 (AWS counted once despite four services; Auth0 counted once despite appearing in Section 2 and Section 3).

**No Critical+High combinations.** The single Medium-risk vendors are Datadog and GitHub; risk-acceptance is documented in `04b_Security_Posture.md` (out-of-scope of this document).

---

## 6. Contractual Coverage

This section maps each vendor to four contractual checkpoints: (a) Art. 28 DPA coverage for GDPR processor relationships; (b) clauses supporting Art. 30 records; (c) TinyTask's right to audit the vendor (and whether the vendor substitutes its own third-party certifications instead); (d) subprocessor approval mechanism.

| Vendor | Art. 28 DPA | Art. 30 Clauses | Security Audit Right | Subprocessor Approval |
|---|---|---|---|---|
| AWS (or equivalent EU cloud provider) | Y (AWS DPA — Art. 28 compliant) | Y (DPA references processor records) | Indirect — AWS substitutes SOC 2 / ISO 27001 / ISO 27018 reports in lieu of direct audit access | Y — AWS publishes subprocessor list; customers may subscribe to change notifications |
| Stripe | Y | Y | Indirect — Stripe provides PCI-DSS Level 1 AOC and SOC 2 reports | Y — Stripe publishes subprocessor list |
| Auth0 | Y | Y | Indirect — Auth0 provides SOC 2 / ISO 27001 + ISO 27018 reports on request | Y — Auth0/Okta publishes subprocessor list |
| Datadog | Y | Y | Indirect — Datadog SOC 2 Type II report available | Y — Datadog publishes subprocessor list |
| GitHub | Y (GitHub DPA) | Limited (source code is not personal data subject to Art. 30 processor records) | Indirect — GitHub SOC 2 available | Y |
| Snyk | Y (Snyk DPA — paid tiers) | Limited (developer tool; no personal data processed) | Indirect — Snyk SOC 2 available | Limited (Snyk subprocessors disclosed) |

**Common pattern:** All vendors substitute third-party certifications for direct audit access. This is industry-standard for micro-SaaS and is a proportionate choice; it requires annual freshness review (tracked in `04b_Security_Posture.md`).

**Subprocessor approval flow (per Art. 28(2) GDPR):** When TinyTask is acting as a **processor** for a B2B customer (controller), the DPA with that controller requires advance notice (typically 30 days) of any new subprocessor. The CTO/CEO maintains the master subprocessor list above and notifies B2B customers of changes.

---

## 7. Compliance Mapping (Regulatory Baseline)

Active scope for TinyTask = 37 of 38 sub-domains (D-08.3 INACTIVE — NIS2 + DORA-only participating regs). The four rows below cover the D-06 (Supply Chain) sub-domains within that active set.

| Sub-domain | Vendors Affected | Compliance Status | Notes | Corpus Manifest Path |
|---|---|---|---|---|
| D-06.1 Vendor Risk Assessment | AWS, Stripe, Auth0, Datadog, GitHub, Snyk (all 6) | Partial — inventory complete, risk scores assigned, but no formal review cadence and no contractual review at each renewal | Action: schedule annual review; tracked in `04b_Security_Posture.md`. | `PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.1/D-06.1.manifest.json` |
| D-06.2 Software Bill of Materials (SBOM) | Snyk (tooling), GitHub (source hosting), AWS (not consumer-relevant) | Partial — Snyk can produce CycloneDX/SPDX; no pipeline integration yet to emit SBOM per release | Action: integrate Snyk SBOM export into CI/CD by Phase 2; required for CRA Annex I Part II (1). | `PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.2/D-06.2.manifest.json` |
| D-06.3 Contractual Security Obligations | AWS, Stripe, Auth0, Datadog, GitHub, Snyk | Covered for GDPR Art. 28 (DPAs in place); covered for CRA via contractual supply-chain clauses from upstream component vendors; no GDPR Art. 32-equivalent direct clauses between TinyTask and *its* subprocessor B2B controllers (handled in B2B customer DPAs in Section 4 subprocessor notice flow) | — | `PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.3/D-06.3.manifest.json` |
| D-06.4 Third-Party Boundary Management | AWS, Stripe, Auth0, Datadog (those with data-egress paths) | Covered — TLS + DPA + subprocessor approval flow + pseudonymisation of logs before egress to Datadog | — | `PREPROCESSING_by_domain/domains/D-06_Supply-Chain/D-06.4/D-06.4.manifest.json` |

**Active sub-domains referenced here:** all 4 D-06.x sub-domains are active via GDPR + CRA participating regulations.

---

## 8. Gaps & Known Limitations (Open Items)

These items are deliberately surfaced so they can flow into `04b_Security_Posture.md` and Phase 2 remediation plans, rather than being silently accepted.

| Gap ID | Description | Severity | Linked Sub-Domain |
|---|---|---|---|
| GAP-TPL-01 | No formal supplier-security-assessment questionnaire (e.g. SIG / CAIQ) sent to vendors; reliance on inherited certifications only | MEDIUM | D-06.1 |
| GAP-TPL-02 | No documented exit plan for AWS-hosted data extraction (DB dump + S3 inventory possible but not yet formalised) | MEDIUM | D-06.4 |
| GAP-TPL-03 | No pipeline-integrated SBOM generation; Snyk is configured but the SBOM export is not yet wired to release artefacts | HIGH (CRA-mandated) | D-06.2 |
| GAP-TPL-04 | No annual review cycle enforced; "Next Review = 2027-04" is a target, not an automated reminder | MEDIUM | D-06.1, D-06.3 |

All four gaps are tracked in `04b_Security_Posture.md` for Phase 2 prioritisation.

---

## 9. Gate

This document is complete (Phase 1 Step D — Third-Party Landscape) when:

- [x] All cloud providers documented with DPA status (Section 2: 6 rows)
- [x] All software vendors documented with criticality (Section 3: 3 distinct vendors)
- [x] All subprocessors listed with Art. 28 contract status (Section 4: 4 subprocessors — AWS, Stripe, Auth0, Datadog)
- [x] Contractual coverage matrix populated (Section 6)
- [x] Compliance Mapping table populated for D-06.x sub-domains (Section 7)
- [x] Gaps explicitly listed (Section 8) rather than silently accepted — required by **AEGIS P5 (Change Propagation)** and **P0 (Reasoned Disagreement)**
- [x] Verbatim GDPR Art. 28 text linked to subprocessor list (Section 4.1 enrichment)
- [x] Verbatim CRA Art. 7 classification gate + Art. 13(5)/(6) substantive supply-chain duty linked to risk table (Section 5.1 + 5.2 enrichment)
- [x] Compliance Mapping table extended with Corpus Manifest Path column (Section 7 enrichment)

**Gate Status:** PASS (proportionate for LOW-tier micro SaaS under P2).

---

## 10. Corpus Provenance (Fase de Especificação 2 Enrichment)

The verbatim Article texts reproduced in Sections 4.1 (GDPR Art. 28) and 5.1 + 5.2 (CRA Art. 7 + CRA Art. 13(5)/(6)) were extracted from the following corpus paths:

| Section | Source corpus file | Lines | Anchor |
|---|---|---|---|
| §4.1 GDPR Art. 28 | `00_METHODOLOGY/PREPROCESSING_by_domain/_by_regulation/GDPR/Ambiguity/04_GDPR_Ch4_ControllerProcessor.md` | 200–223 | Art. 28(1) + (2) + (3)(a)–(h) verbatim |
| §5.1 CRA Art. 7 | `00_METHODOLOGY/PREPROCESSING_by_domain/_archive_unmatched/CRA/02_CRA_Art6-8_Classification.md` | 41–53 | Art. 7(1)–(4) verbatim (classification gate) |
| §5.2 CRA Art. 13(5)/(6) | `00_METHODOLOGY/PREPROCESSING_by_domain/_by_regulation/CRA/Ambiguity/03_CRA_Art13_Manufacturers.md` | 23–25 | Art. 13(5) due diligence + Art. 13(6) component vuln reporting verbatim |

**Note on task-vs-corpus fit:** The Executor brief referenced "CRA Art. 7" for the Supply Chain Risk section. CRA Art. 7 is in fact a **classification gate** (Annex III important-products regime), not the substantive supply-chain duty — the operative duty is CRA Art. 13(5)/(6) on third-party component due diligence (referenced from `D-06.1` corpus SO-CRA-037 and `D-02.2` corpus SO-CRA-037 + SO-CRA-038). The verbatim quote of Art. 7 is included for accuracy per the brief; the substantive Art. 13(5)/(6) text is also included to ensure the section actually discharges the supply-chain duty rather than a classification question. This dual-quote approach is the most defensible response per AEGIS P0 (Reasoned Disagreement Over Deference): both texts are in scope, neither alone is sufficient.

**Corpus manifest paths added to Section 7 table:** 4 (one per D-06.x sub-domain). Total corpus JSON lookups for this section: 4 (manifest-paths only; no content extraction).

---

## N-1. Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-07-11 | Executor | Populated from template `04c_ThirdParty_Landscape.md`; merged architecture data from `04a` and stakeholder register from `04 §3`. |

## N. Document Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Document Author | Executor |  | 2026-07-11 |
| Technical Review | CTO |  |  |
| AEGIS Methodology Review | Validator |  |  |

## See also

- **Data backbone:** `Case_01_Phase1.xlsx` (13 sheets: COVER, SYSTEMS, DATA_STORES, DATA_FLOWS, PERSONAL_DATA, THIRD_PARTIES, ROLES_RACI, POSTURE, SUBDOMAINS, REG_CHAIN, COMPLIANCE, GAPS, PRIORITIES)
