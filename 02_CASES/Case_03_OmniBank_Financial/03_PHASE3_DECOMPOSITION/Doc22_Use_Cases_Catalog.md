---
document_id: AEGIS-P3-13
title: Use Cases Catalog
phase: 3
version: 3.1
created: 2026-04-28
updated: 2026-09-05
author: Compliance Lead
status: DRAFT
inputs: [11_Rules_Catalog.md, 10_Privacy_Security_Objectives.md, 09_Strategic_Tensions_Report.md, 04_Company_Context_Assessment.md]
outputs: [Doc23_Use_Case_Relationships.md, Doc24_Use_Case_Variability.md, Doc25_Architectural_Nodes.md, Doc26_Requirements_Allocation.md, Doc32_Process_Capability_Cards.md]
traceability: AEGIS Class Model → UseCase, UseCasePackage, Actor, UseCaseRelationship classes
related_documents: 00_COMMON/Taxonomy_Reference.md
regulations: GDPR, CRA, NIS 2, DORA, AI Act (5/5)
case_id: CASE-03-OMNIBANK
case: Case_03_OmniBank_Financial
complexity: Maximum (5 regulations, 38 sub-domains, 63 rules)
---

# Use Cases Catalog

**Case:** Case 03 — OmniBank Financial Systems (Maximum Complexity)
**Phase:** 3 — Decomposition & Risk Integration
**Step:** 1 — Define Packages + Use Cases

> **UML diagrams:** `annexes/A_Use_Case_Diagrams.md` (use case diagrams) ·
> `annexes/B_Sequence_Diagrams.md` (sequence diagrams, one per use case).

---

## 1. DOCUMENT PURPOSE

This document is the primary output of Phase 3 Step 1 for Case 03 — OmniBank Financial Systems (Maximum Complexity). It defines the use cases of the UC (technology) lane. Since v3.0 (UC SEPARATION, rubric `REALIZATION_CLASS_RUBRIC.md` v1.8 §5B rule 6) the catalog is **lane-pure**: it holds use-case cards only; the 10 compliance domains (PKG-D-01..D-10) are indexed in §3 and realised by process/capability lane cards in `Doc32_Process_Capability_Cards.md`.

Each Use Case follows the Actor + Verb + Object pattern and maps to one or more compliance rules. UCs are organized into product packages (PKG-A..F, §4) plus a dedicated privacy & data-subject package (PKG-DS, §4.8). Relationships and Variability are defined in Doc23_Use_Case_Relationships.md and Doc24_Use_Case_Variability.md.

**Scope:** 7 use-case packages (PKG-A..F product + PKG-DS privacy), 33 use cases; 10 compliance domains indexed in §3 with realisation in `Doc32_Process_Capability_Cards.md`, across all 5 applicable regulations.

---

## 2. USE CASES CATALOG METADATA

| Field | Value |
|-------|-------|
| **caseId** | CASE-03-OMNIBANK |
| **caseName** | OmniBank Financial Systems S.A. |
| **complexity** | Maximum |
| **regulationsCovered** | GDPR, CRA, NIS 2, DORA, AI Act (5/5) |
| **totalPackages** | 7 (PKG-A..F product + PKG-DS) |
| **totalUseCases** | 33 (31 product + 2 PKG-DS) |
| **totalComplianceRulesMapped** | 38/38 (100%) |
| **totalBestPracticeRulesMapped** | 25/25 (100%) |
| **complianceDomains** | 10 (PKG-D-01..D-10) — indexed in §3, **not** use-case packages |
| **phase3Status** | v3.1 — lane-pure use-case catalog (UC SEPARATION + RENUMBER, ids UC-01..33) |
| **relationshipsDefined** | Doc23_Use_Case_Relationships.md |
| **variabilityDefined** | Doc24_Use_Case_Variability.md |

---

## 3. COMPLIANCE DOMAIN INDEX (PKG-D-01..D-10)

> **v3.0 (UC SEPARATION, rubric v1.8 §5B rule 6 — human decision 2026-09-05):** this catalog is
> lane-pure — it holds use-case cards only. The former §6 summary compliance cards were removed:
> the 38 PROC-01..38 and 7 CAP-01..07 full cards already live in `Doc32_Process_Capability_Cards.md`;
> the 15 non-genuine `UC-*` cards were re-laned to PROC-41..52 / CAP-08..10 (full cards authored in Doc32);
> UC-33/UC-34 stayed in the UC lane and moved to PKG-DS (§4.8). This index preserves the
> domain → realisation → rules traceability without card duplication.
> **Full process/capability cards: `Doc32_Process_Capability_Cards.md`.**

### 3.1 Domain overview (scope, actors, goals — from the former package sections)

| Domain | Name | Scope (Purpose) | Primary Actors | Business Goals | Primary Regulations | Lane cards (Doc32) | Priority distribution |
|---|---|---|---|---|---|---|---|
| PKG-D-01 | Data Protection & Encryption | Encrypt data at rest and in transit; manage cryptographic keys; ensure data integrity and AI system resilience. | Data Protection Officer, Security Architect, AI System Administrator, Data Subject | AG-D-01.1-001, AG-D-01.2-001, AG-D-01.3-001, AG-D-01.4-001 | All 5 | 8 | CRITICAL: 4, HIGH: 3, MEDIUM: 1 |
| PKG-D-02 | Vulnerability Management | Maintain zero known exploitable vulnerabilities; operate automated patch management; coordinate vulnerability disclosure; execute TLPT. | Security Operations Manager, Vulnerability Assessment Team, Penetration Tester, AI Security Analyst | AG-D-02.1-002, AG-D-02.2-002, AG-D-02.3-002, AG-D-02.4-002 | CRA, NIS 2, DORA, AI Act | 7 | CRITICAL: 4, HIGH: 2, MEDIUM: 1 |
| PKG-D-03 | Access Control | Implement unified identity management with MFA; enforce least privilege; maintain secure default configurations. | Identity and Access Manager, Security Administrator, AI Platform Administrator, Human Resources Manager | AG-D-03.1-002, AG-D-03.2-002, AG-D-03.3-002, AG-D-03.4-002 | CRA, NIS 2, DORA, AI Act | 7 | CRITICAL: 4, HIGH: 3, MEDIUM: 0 |
| PKG-D-04 | Incident Response | Operate 24/7 SOC; maintain business continuity; execute universal incident notification; maintain redundant backups. | Security Operations Center Analyst, Business Continuity Manager, Compliance Officer, AI Operations Manager | AG-D-04.1-002, AG-D-04.2-002, AG-D-04.3-002, AG-D-04.4-002 | All 5 | 8 | CRITICAL: 5, HIGH: 2, MEDIUM: 1 |
| PKG-D-05 | Data Lifecycle | Enforce data minimization; implement tiered retention; execute cryptographic erasure; enable data portability. | Data Protection Officer, AI Data Engineer, Data Subject, Compliance Officer | AG-D-05.1-001, AG-D-05.2-001, AG-D-05.3-001, AG-D-05.4-001 | GDPR, CRA, AI Act | 4 (+2 UCs in PKG-DS) | CRITICAL: 4, HIGH: 1, MEDIUM: 1 |
| PKG-D-06 | Supply Chain | Operate vendor risk management; maintain SBOM; enforce contractual security; manage concentration risk. | Vendor Risk Manager, Procurement Manager, Security Architect, Legal Counsel | AG-D-06.1-002, AG-D-06.2-002, AG-D-06.3-002, AG-D-06.4-002 | GDPR, NIS 2, DORA | 5 | CRITICAL: 3, HIGH: 2, MEDIUM: 0 |
| PKG-D-07 | Secure Development | Implement privacy/security by design; enforce secure coding; secure CI/CD pipeline; operate formal change management. | Software Development Manager, Security Engineer, Release Manager, AI ML Engineer | AG-D-07.1-001, AG-D-07.2-002, AG-D-07.3-002, AG-D-07.4-002 | NIS 2, DORA | 6 | CRITICAL: 3, HIGH: 3, MEDIUM: 0 |
| PKG-D-08 | Human Factors | Deliver security awareness training; maintain role-specific competence; ensure board-level oversight. | Training Manager, Security Awareness Officer, HR Manager, Board Secretary | AG-D-08.1-002, AG-D-08.2-002, AG-D-08.3-002 | GDPR, NIS 2, AI Act | 4 | CRITICAL: 2, HIGH: 1, MEDIUM: 1 |
| PKG-D-09 | Governance & Documentation | Maintain unified ISMS; conduct IPSARA assessments; manage asset inventory; maintain compliance documentation. | Chief Information Security Officer, Compliance Manager, Data Protection Officer, AI Governance Lead | AG-D-09.1-001, AG-D-09.2-001, AG-D-09.4-001, AG-D-09.3-002 | All 5 | 5 | CRITICAL: 3, HIGH: 2, MEDIUM: 0 |
| PKG-D-10 | Monitoring & Audit | Deploy 24/7 monitoring with AI threat detection; maintain immutable audit logs; execute penetration testing and AI evaluation. | SOC Manager, Security Analyst, Audit Manager, AI Security Analyst | AG-D-10.1-002, AG-D-10.2-002, AG-D-10.3-002 | CRA, NIS 2, DORA, AI Act | 6 | CRITICAL: 4, HIGH: 2, MEDIUM: 0 |

### 3.2 Realisation index

| Domain | Realised by (lane cards in Doc32) | UCs in this catalog | Rules covered (the ids the former package cards held) |
|---|---|---|---|
| PKG-D-01 Data Protection & Encryption | PROC-01, PROC-39, PROC-40, PROC-02, PROC-03, PROC-41, PROC-04, CAP-08 | — | CR-D-01.1-001, CR-D-01.2-001, CR-D-01.3-001, CR-D-01.4-001, BPR-D-12.4-001 |
| PKG-D-02 Vulnerability Management | PROC-05, PROC-06, PROC-07, PROC-08, PROC-09, CAP-01, PROC-42 | — | CR-D-02.1-001, CR-D-02.2-001, CR-D-02.3-001, CR-D-02.4-001, BPR-D-02.4-001, BPR-D-12.1-001, BPR-D-12.4-001, BPR-D-02.1-001, BPR-D-02.3-001, BPR-D-02.2-001, CR-D-06.2-001 |
| PKG-D-03 Access Control | PROC-10, PROC-43, PROC-11, PROC-12, PROC-13, PROC-44, PROC-45 | — | CR-D-03.1-001, BPR-D-03.1-001, CR-D-03.2-001, BPR-D-03.2-001, CR-D-03.3-001, BPR-D-03.3-001, CR-D-03.4-001, BPR-D-03.4-001 |
| PKG-D-04 Incident Response | CAP-02, PROC-14, PROC-15, CAP-09, PROC-16, PROC-17, PROC-18, PROC-19 | — | CR-D-04.1-001, BPR-D-04.1-001, CR-D-04.2-001, BPR-D-04.2-001, CR-D-04.3-001, BPR-D-04.3-001, CR-D-04.4-001, BPR-D-04.4-001, CR-D-10.1-001, BPR-D-12.2-001, AI-C26, AI-C29 |
| PKG-D-05 Data Lifecycle | PROC-20, PROC-21, UC-01, UC-02, PROC-22, PROC-23 | UC-01, UC-02 (PKG-DS, §4.8) | CR-D-05.1-001, BPR-D-05.1-001, CR-D-05.2-001, CR-D-05.3-001, BPR-D-05.3-001, CR-D-05.4-001, BPR-D-05.4-001, GDPR-C12 |
| PKG-D-06 Supply Chain | PROC-24, CAP-03, PROC-25, PROC-26, PROC-27 | — | CR-D-06.1-001, BPR-D-06.1-001, CR-D-06.2-001, BPR-D-02.2-001, CR-D-06.3-001, BPR-D-06.3-001, CR-D-06.4-001, BPR-D-06.4-001, BPR-D-12.3-001 |
| PKG-D-07 Secure Development | PROC-28, PROC-29, PROC-46, PROC-30, PROC-47, PROC-48 | — | CR-D-07.1-001, BPR-D-07.1-001, CR-D-07.2-001, BPR-D-07.2-001, CR-D-07.3-001, BPR-D-07.3-001, CR-D-07.4-001, BPR-D-07.4-001 |
| PKG-D-08 Human Factors | PROC-31, CAP-04, PROC-32, PROC-33 | — | CR-D-08.1-001, BPR-D-08.1-001, CR-D-08.2-001, BPR-D-08.2-001, BPR-D-12.3-001, CR-D-08.3-001, BPR-D-08.3-001 |
| PKG-D-09 Governance & Documentation | CAP-05, PROC-34, CAP-06, CAP-07, PROC-35 | — | CR-D-09.1-001, BPR-D-09.1-001, BPR-D-09.4-001, CR-D-09.2-001, BPR-D-09.2-001, BPR-D-09.3-001, CR-D-09.3-001, CR-D-09.4-001, DORA-C38 |
| PKG-D-10 Monitoring & Audit | PROC-49, CAP-10, PROC-36, PROC-37, PROC-50, PROC-38 | — | CR-D-10.1-001, BPR-D-10.1-001, BPR-D-12.2-001, CR-D-10.2-001, BPR-D-10.2-001, CR-D-10.3-001, BPR-D-10.3-001, BPR-D-12.4-001, CR-D-02.4-001, AI-C09, AI-C10 |

> Rule ids above are carried verbatim from the former §6 package cards (v2.3); the full cards in
> `Doc32_Process_Capability_Cards.md` carry them in their **Realises** field. Traceability chain:
> RULE → CAP → PROC → UC (rubric v1.8 §5C).

---
## 4. PRODUCT FUNCTIONAL USE CASES (UC-03+, PKG-A..F, PKG-DS) — OmniBank platform product (formerly §6B)

> **v2.1 (PORT-PARITY-2 Phase 3 restructure pilot, 2026-09-04).** This section models the
> **OmniBank product itself** (digital channels, OmniScore, lending) as a normal software
> product: actor-goal use cases in fully-dressed form (Cockburn), with security/compliance
> layered on as a per-UC annex. **Nomenclature unchanged**: the pre-existing compliance use
> cases PROC-01..UC-62 (§6) keep IDs and content verbatim; new product use cases continue the
> flat numbering at **UC-63+** and never reuse existing IDs. This pilot delivers PKG-C
> (Lending & OmniScore, §4.2, formerly §6B.1); the massification pass (v2.2) delivered PKG-A/B/D/E/F (§4.3–§4.7, formerly §6B.2–§6B.6).
>
> **Template (2026-09-04):** the PKG-C and PKG-A/B/D/E/F use cases are written fully-dressed in the RUP-style
> per-UC template of `03_REFERENCE_MATERIAL/P3_E2_Requirement_Analysis_Bike4All_Maintenance_platform_v1r2.md`
> (sections 1–10, one Mermaid sequence diagram per UC), adjusted to AEGIS: section 10 is the
> **Security & Compliance Annex (AEGIS)** carrying provenance, constrained-by, rules, threats
> and NIST anchors; MUC linkage is preserved.

### 4.1 Product actors (reuse of existing stakeholder/system IDs)

| Actor | Role in the product | Drives |
|-------|---------------------|--------|
| Customer (Retail) | Primary product user: onboards, banks, borrows via SYS-02 app. | UC-03, UC-05, UC-07–21, UC-24–25, UC-30–33 |
| OmniScore AI Platform (SYS-03) | The scoring system itself — acts, never decides alone. | UC-04 |
| Underwriter (Consumer Lending) | Human oversight on borderline/high-risk credit decisions. | UC-06 |
| Head of AI Governance (stakeholder) | Owns bias/drift monitoring and model governance. | Annex targets |
| Fraud & AML Platform (SYS-11) | Consumes journey telemetry; sanctions/fraud/AML screening. | UC-12, UC-30, Annex targets |
| Customer (Corporate) | Corporate self-service (SME + large corporate) via SYS-21. | UC-26–29 |
| TPP (Third-Party Provider) | PSD2 third party consuming AIS/PIS via SYS-18. | UC-22, UC-23 (counterparty of UC-21) |
| Document vault (SYS-16) | KYC/KYB document filing with 10-year retention. | UC-11, UC-14 (supporting: UC-26, UC-33) |

### 4.2 PKG-C — Lending & OmniScore (6)

| UC ID | Title | Primary Actor | Prio |
|-------|-------|---------------|------|
| UC-03 | Apply for Consumer Credit | Customer (Retail) | CRITICAL |
| UC-04 | OmniScore Computes Credit Score | SYS-03 (AI Platform) | CRITICAL |
| UC-05 | Customer Receives Score Explanation | Customer (Retail) | HIGH |
| UC-06 | Underwriter Reviews Borderline Application | Underwriter | CRITICAL |
| UC-07 | Customer Accepts Offer & Contract Signed | Customer (Retail) | CRITICAL |
| UC-08 | Customer Manages Repayment & Arrears View | Customer (Retail) | HIGH |

#### Use-Case: {UC-03} Apply for Consumer Credit

##### 1 Brief Description

The customer applies for consumer credit through the mobile app: product selection,
pre-contractual information (SECCI), credit-bureau consent and income/expense
declarations. It is triggered when the customer opens the credit product and submits the
application form. The submitted application then enters the OmniScore decisioning flow
(UC-04) or — without consent — the manual path (UC-06).

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Selects the product, grants consents, submits declarations and receives the application
status.

###### 2.2 SYS-02 (Mobile app channel):

PSD2 SCA-protected session; captures the application, consents and declarations.

###### 2.3 SYS-14 (Loan Origination):

Creates the application record; invokes the OmniScore decisioning flow (UC-04).

###### 2.4 SYS-11 (Fraud & AML Platform):

Screens the application for fraud patterns.

###### 2.5 DPO:

Owner of the consent records.

##### 3 Preconditions

- Customer onboarded (PKG-A, pending) with verified identity.
- App session under PSD2 SCA.

##### 4 Basic Flow of Events

1. Customer selects product, amount and term; app shows the pre-contractual information sheet (SECCI).
2. Customer grants the credit-bureau check consent; consent recorded with timestamp.
3. Customer submits income/expense declarations; app validates completeness.
4. SYS-14 creates the application record; SYS-11 screens for fraud patterns (no hit → continue).
5. SYS-14 invokes the OmniScore decisioning flow (UC-04) and awaits the outcome.

> **Sequence diagram:** → Annex B §3 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Consent declined>

Trigger: step 2. The application cannot proceed under automated scoring; the customer is
offered the manual-review path (UC-06 without score, Art. 22(3) right not to be subject
to solely automated decisions).

###### 5.2 <Alternate flow: Fraud screening hit>

Trigger: step 4. Application frozen; sent to the financial-crime queue (no decision until
cleared).

###### 5.3 <Alternate flow: Data incomplete>

Trigger: step 3. Guided correction (max 3 attempts), then save-as-draft.

##### 6 Subflows

###### 6.1 <Subflow: Bureau consent capture>

1. Present the consent purpose (credit-bureau check) before any bureau data is touched.
2. Record the consent with timestamp against the application record (evidence for UC-05 and audits).

###### 6.2 <Subflow: Fraud screening>

1. SYS-11 screens the declared data and the session for fraud patterns.
2. Hit → freeze the application into the financial-crime queue; no hit → continue to decisioning.

##### 7 Key Scenarios

###### 7.1 <Scenario: Application submitted>

1. Application exists with status SUBMITTED; consent + screening evidence on record; score flow invoked (UC-04).

###### 7.2 <Scenario: Fraud hit>

1. Application frozen, financial-crime queue, no decision until cleared.

##### 8 Post-conditions

###### 8.1

Application exists with status SUBMITTED.

###### 8.2

Consent + screening evidence on record.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Product/amount/term selection, SECCI presentation, bureau consent,
declaration validation, application record creation, decisioning invocation.

**Usability (U):** Guided correction of incomplete data (max 3 attempts) before
save-as-draft.

**Reliability (R):** Fraud screening gates every application; PSD2 SCA session resists
takeover (MUC-01-analogue); journey monitoring (CR-D-10.1-001).

**Performance (P):** N/A — no attested timing constraint for the application step.

**Supportability (S):** Scoring factors exportable by design (CR-D-05.4-001) keeps the
application data model stable for audit and data-subject requests.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-14 (consumer credit origination + decision engine, integrates OmniScore), SYS-02 (SCA app channel); Doc19 CR-D-05.4-001 (credit scoring factors exportable).
- **Constrained by:** PROC-10/PROC-43 (identity, MFA), PROC-41 (field-level encryption of declarations), PROC-44 (AI platform access).
- **Rules / NFR:** CR-D-05.4-001 (data export incl. scoring factors), CR-D-10.1-001 (journey monitoring).
- **Threats addressed:** MUC-C3-05 (application data crafted to game scoring), MUC-01-analogue (session takeover).
- **NIST anchors:** PR.AA-01, PR.DS-01.

#### Use-Case: {UC-04} OmniScore Computes Credit Score

##### 1 Brief Description

The OmniScore AI platform (SYS-03) computes the credit score for a submitted application
using the approved model version, with reason codes generated inside the model runtime. It
is triggered when the SYS-14 decisioning request arrives (UC-03 step 5). Score bands route
the application — auto-approve, auto-decline or borderline — and borderline cases always
reach a human (UC-06): never a silent auto-decline without a human path.

##### 2 Actor Brief Descriptions

###### 2.1 SYS-03 (OmniScore AI Platform) — Primary Actor (acts on behalf of SYS-14):

Runs the approved model version, computes score + confidence band and generates reason
codes (managed ML runtime + explainability layer + bias monitoring pipeline).

###### 2.2 SYS-14 (Loan Origination):

Issues the decisioning request; consumes the score band; routes borderline cases.

###### 2.3 Head of AI Governance:

Model governance: approved versions, bias/drift monitoring.

###### 2.4 Underwriter:

Consumer of the score at UC-06.

###### 2.5 DPO:

Owner of the automated-decision records.

##### 3 Preconditions

- Application SUBMITTED (UC-03).
- Model version approved and deployed per change control.

##### 4 Basic Flow of Events

1. SYS-03 fetches application features (declared data + internal account data where consented).
2. SYS-03 runs the approved model version; computes the score + confidence band.
3. SYS-03 generates the reason-code set (top contributing factors, GDPR-compliant granularity).
4. SYS-03 returns score + reasons + model version id to SYS-14; decision-context record written (who/what/when/version).
5. Score band routes the application: auto-approve / auto-decline / **borderline → UC-06** (never silent auto-decline without a human path).

> **Sequence diagram:** → Annex B §4 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Model service unavailable>

Trigger: step 2. SYS-14 queues to the manual underwriting path; NO fallback to an
unapproved model version.

###### 5.2 <Alternate flow: Reason-code generation fails>

Trigger: step 3. Decision blocked — explainability is a release condition, not a
nice-to-have.

###### 5.3 <Alternate flow: Input features out of expected distribution>

Trigger: step 1. Flag possible data-quality/manipulation issue (MUC-C3-01) + route to
UC-06.

##### 6 Subflows

###### 6.1 <Subflow: Decision-context record write>

1. Record who/what/when plus model version and the feature snapshot used.
2. Append immutably to the decision records (immutable decision records, CR-D-10.2-001 discipline).

###### 6.2 <Subflow: Reason-code generation>

1. Extract the top contributing factors inside the model runtime (never hand-written).
2. Emit at GDPR-compliant granularity, log-anchored to the model version (anti MUC-C3-05).

##### 7 Key Scenarios

###### 7.1 <Scenario: Score computed>

1. Score + reasons + model version immutably recorded; the band routes the application.

###### 7.2 <Scenario: Unexplainable or manipulated input>

1. Borderline/blocked outcome queued to a human (UC-06) — no silent auto-decline.

##### 8 Post-conditions

###### 8.1

Score + reasons + model version immutably recorded.

###### 8.2

Borderline cases queued to a human.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Feature fetch, scoring with confidence band, in-runtime reason codes,
decision-context record, band routing with a human path.

**Usability (U):** N/A — backend step; the customer-facing explainability surface is
UC-05.

**Reliability (R):** No fallback to unapproved models; decision blocked if reason codes
cannot be generated (fail-closed on explainability).

**Performance (P):** N/A — no attested latency target for scoring.

**Supportability (S):** Approved-model-version pinning plus the bias/drift monitoring
pipeline (PROC-50, SYS-03) keep the service maintainable under AI Act governance
documentation (CR-D-09.1-001).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-03 (managed ML runtime + explainability layer + bias monitoring pipeline); Doc19 BPR-D-12.3-001 (AI Act Art. 14 human oversight thresholds/overrides for credit scoring).
- **Constrained by:** PROC-03 (model integrity validation), CAP-08 (model tampering detection), PROC-50 (AI model performance drift monitoring), PROC-44 (AI model access control).
- **Rules / NFR:** BPR-D-12.3-001 (Art. 14 human oversight), CR-D-05.4-001 (scoring-factor transparency feeds UC-05), CR-D-09.1-001 (governance documentation).
- **Threats addressed:** MUC-C3-01 (input manipulation), MUC-C3-02 (training-data poisoning — detected via drift/bias pipeline), MUC-C3-04 (discriminatory outcomes — bias monitoring pipeline).
- **NIST anchors:** GV.MT-01, MEASURE-2.7.

#### Use-Case: {UC-05} Customer Receives Score Explanation

##### 1 Brief Description

The customer receives the credit decision with plain-language reason codes and can request
the machine-readable explanation package. It is triggered when the customer opens the
decision screen in the app, after a UC-04 or UC-06 outcome. Explanations are generated,
log-anchored evidence — never hand-written — so they cannot drift from actual model
behaviour.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Reads the outcome and reason codes; may request the explanation package or dispute a
reason.

###### 2.2 SYS-02 (Mobile app channel):

Presents the outcome screen; dispatches explanation requests.

###### 2.3 SYS-03 (OmniScore explainability layer):

Source of the principal reason codes and the machine-readable package.

###### 2.4 DPO:

Owner of Art. 22 transparency.

###### 2.5 Head of AI Governance:

Owns XAI quality.

##### 3 Preconditions

- A decision (or borderline outcome) exists from UC-04/UC-06.

##### 4 Basic Flow of Events

1. App presents the outcome with the principal reason codes, in plain language.
2. Customer can request the machine-readable explanation package (CR-D-05.4-001 format).
3. Request/dispatch is logged against the decision record.

> **Sequence diagram:** → Annex B §5 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Disputed reason code>

Trigger: step 1, customer disputes a reason (factually wrong data) → opens a
data-correction flow (GDPR Art. 16 path) linked to the decision; re-scoring after
correction.

###### 5.2 <Alternate flow: Explanation package generation fails>

Trigger: step 2. Human contact channel offered within SLA; never silent.

##### 6 Subflows

###### 6.1 <Subflow: Explanation package dispatch>

1. Generate the package in the CR-D-05.4-001 format from the explainability layer (generated, not hand-written).
2. Log the request/dispatch against the decision record (log-anchored, anti MUC-C3-05).

##### 7 Key Scenarios

###### 7.1 <Scenario: Explanation delivered>

1. Explanation evidence stored with the decision (audit complete).

###### 7.2 <Scenario: Wrong data disputed>

1. Art. 16 correction flow linked to the decision; re-scoring after correction.

##### 8 Post-conditions

###### 8.1

Explanation evidence stored with the decision (audit complete).

###### 8.2

Any dispute is tracked as a linked data-correction flow until resolved.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Plain-language reasons, machine-readable package in the CR-D-05.4-001
format, dispatch logging.

**Usability (U):** Plain language, customer-facing; in-app dispute entry point.

**Reliability (R):** Never silent on generation failure (human contact channel within
SLA); reason codes log-anchored and generated in the model runtime (anti MUC-C3-05).

**Performance (P):** N/A — no attested timing constraint.

**Supportability (S):** The explanation format stays stable for audits and data-subject
requests (PROC-01 linkage).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc19 CR-D-05.4-001 verbatim ("Include AI model decisions, training data lineage, and credit scoring factors"); Doc04 §1.1 SYS-03 explainability layer.
- **Constrained by:** PROC-01 (data subject requests), UC-03 consent record.
- **Rules / NFR:** CR-D-05.4-001, CR-D-09.2-001 (governance reporting).
- **Threats addressed:** MUC-C3-05 (explainability spoofing — reason codes are generated, not hand-written, and log-anchored).
- **NIST anchors:** GV.PO-P1.

#### Use-Case: {UC-06} Underwriter Reviews Borderline Application

> Re-adjudicated from PROC-39 to the UC lane per rubric v1.8 §5B rule 6 (human decision 2026-09-05).

##### 1 Brief Description

The underwriter performs the independent human review of borderline or blocked credit
applications and is the decision-maker here (AI Act Art. 14) — the model only recommends.
It is triggered when a work item lands in the underwriting queue, either from the UC-04
borderline band or from the manual path of UC-03 (ext. 5.1). Decisions carry mandatory
reason codes, and the override-vs-score delta feeds AI-governance metrics.

##### 2 Actor Brief Descriptions

###### 2.1 Underwriter (Consumer Lending) — Primary Actor:

Reviews the work item independently and records the decision with justification.

###### 2.2 SYS-14 (Loan Origination):

Record owner; provides the work-item queue and business-rules engine.

###### 2.3 SYS-03 (OmniScore):

Supplies score, reason codes, model version and confidence band for the review.

###### 2.4 Head of AI Governance:

Consumes the oversight metrics (override deltas).

###### 2.5 Customer:

Subject of the decision.

##### 3 Preconditions

- UC-04 returned a borderline/blocked outcome (or customer invoked the manual path per UC-03 ext. 5.1).

##### 4 Basic Flow of Events

1. Underwriter opens the work item: full application, score + reason codes, model version, confidence band.
2. Underwriter performs independent review (documents, bureau data, overrides only with recorded justification).
3. Underwriter records the decision (approve/decline + mandatory reason code) — the human, not the model, is the decision-maker here (Art. 14).
4. Decision flows to UC-07; the override-vs-score delta is logged for AI-governance metrics.

> **Sequence diagram:** → Annex B §6 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Incomplete decision context>

Trigger: step 1, record missing model version / reasons → work item is BLOCKED; the
underwriter cannot decide on an unexplainable recommendation (fail-closed).

###### 5.2 <Alternate flow: Manipulation indicators>

Trigger: step 2, suspected manipulation flags (MUC-C3-01 from UC-04 ext. 5.3) → escalate
to financial crime before deciding.

###### 5.3 <Alternate flow: Override rate anomaly>

Trigger: step 3, per-underwriter anomaly → governance review trigger (anti-rubber-stamp,
mirrors MUC-C2-05 discipline).

##### 6 Subflows

###### 6.1 <Subflow: Override justification logging>

1. Any override of the model recommendation is recorded with a mandatory justification.
2. The override-vs-score delta is appended to the immutable record and feeds AI-governance metrics.

###### 6.2 <Subflow: Fail-closed context validation>

1. On open, the work item is validated for model version + reason codes.
2. Missing context → BLOCKED (no decision possible on an unexplainable recommendation).

##### 7 Key Scenarios

###### 7.1 <Scenario: Human decision recorded>

1. Human decision with justification on the immutable record; AI-governance metrics updated; decision flows to UC-07.

###### 7.2 <Scenario: Unexplainable recommendation>

1. Work item blocked — the underwriter cannot decide (fail-closed).

##### 8 Post-conditions

###### 8.1

Human decision with justification on the immutable record.

###### 8.2

AI-governance metrics updated.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Work-item review, independent verification, override recording,
metrics feed to governance.

**Usability (U):** Full decision context in one view (application, score, reasons, model
version, confidence band).

**Reliability (R):** Fail-closed on incomplete context; quarterly access review of
underwriter permissions (PROC-11); audit sampling discipline against rubber-stamping.

**Performance (P):** N/A — no attested SLA for review turnaround.

**Supportability (S):** Competence training for underwriters (CR-D-08.2-001); oversight
thresholds and escalation paths maintained per BPR-D-12.3-001.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc19 BPR-D-12.3-001 (human intervention thresholds, override mechanisms, escalation paths); Doc04 §1.1 SYS-14 (business-rules engine + underwriter flow).
- **Constrained by:** PROC-43 (MFA privileged), PROC-11 (quarterly access review), UC-06-audit chain.
- **Rules / NFR:** BPR-D-12.3-001, CR-D-08.2-001 (competence training), CR-D-10.1-001.
- **Threats addressed:** MUC-C3-05, insider rubber-stamping (audit sampling discipline).
- **NIST anchors:** PR.AA-05, DE.CM-09.

#### Use-Case: {UC-07} Customer Accepts Offer & Contract Signed

##### 1 Brief Description

The customer reviews the final offer and signs the credit contract with PSD2 SCA-grade,
hardware-backed signing. It is triggered when the customer reviews the offer in the app
after approval (UC-04 auto-band or UC-06). SYS-14 issues the contract, SYS-16 archives it
in the KYC vault (10-year retention), and disbursement starts under AML monitoring.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Reviews the offer and signs the contract.

###### 2.2 SYS-02 (Mobile app channel):

Presents the final offer; hosts the SCA-grade signing ceremony.

###### 2.3 SYS-14 (Loan Origination):

Issues the contract and initiates the disbursement.

###### 2.4 SYS-16 (KYC/document vault):

Files the contract with 10-year retention (per BaFin/GoBD).

###### 2.5 SYS-11 (Fraud & AML Platform):

Tags the new credit exposure; post-acceptance monitoring.

##### 3 Preconditions

- Approved decision (UC-04 auto-band or UC-06).

##### 4 Basic Flow of Events

1. App presents the final offer (rate, term, SECCI deltas already shown at UC-03).
2. Customer signs with PSD2 SCA-grade signing (hardware-backed).
3. SYS-14 issues the contract; SYS-16 files it in the KYC vault (10-year retention).
4. Disbursement initiated to the customer account; AML monitoring tags the new credit exposure.

> **Sequence diagram:** → Annex B §7 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Signing certificate/SCA failure>

Trigger: step 2. Offer held; retry with step-up; no SMS-fallback signing
(phishing-resistant policy).

###### 5.2 <Alternate flow: AML hit post-acceptance>

Trigger: step 4. Freeze disbursement, financial-crime queue (incident flow).

##### 6 Subflows

###### 6.1 <Subflow: KYC vault filing>

1. Contract document + metadata filed in SYS-16.
2. 10-year retention applied per BaFin/GoBD.

###### 6.2 <Subflow: Step-up signing>

1. On SCA failure, hold the offer (no silent retry loop).
2. Retry with step-up authentication; SMS fallback is prohibited.

##### 7 Key Scenarios

###### 7.1 <Scenario: Contract signed>

1. Contract signed and archived; credit line live.

###### 7.2 <Scenario: Account takeover attempt at signing>

1. SCA required — phishing-resistant signing blocks the takeover (MUC-01-analogue); an AML hit freezes the disbursement.

##### 8 Post-conditions

###### 8.1

Contract signed and archived.

###### 8.2

Credit line live.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Offer presentation, SCA signing ceremony, contract issuance, vault
archiving, disbursement initiation.

**Usability (U):** SECCI deltas already shown at UC-03 — the customer does not re-read
pre-contractual information.

**Reliability (R):** AML monitoring on the new exposure; reportable-event workflows
(CR-D-04.3-001); audit trail (CR-D-10.2-001).

**Performance (P):** N/A — no attested timing constraint for the signing step.

**Supportability (S):** 10-year retention in SYS-16 per BaFin/GoBD; FIDO2-grade signing
hardware (PROC-45).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-14, SYS-16 (10-year retention per BaFin/GoBD), SYS-11.
- **Constrained by:** PROC-45 (FIDO2), PROC-01 (records).
- **Rules / NFR:** CR-D-04.3-001 (reportable events), CR-D-10.2-001 (audit trail).
- **Threats addressed:** MUC-01-analogue (account takeover at signing step — SCA required).
- **NIST anchors:** PR.AA-01, AU.A-06.

#### Use-Case: {UC-08} Customer Manages Repayment & Arrears View

##### 1 Brief Description

The customer manages the live credit in the app: repayment schedule, early repayment and
the arrears view with self-service cure options. It is triggered when the customer opens
the credit management screen. Every action executes against SYS-15 (Loan Servicing) and
never operates on stale figures.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Views the schedule, makes early repayments and uses the arrears self-service options.

###### 2.2 SYS-02 (Mobile app channel):

Presents the servicing state; guards against stale data.

###### 2.3 SYS-15 (Loan Servicing):

Owns repayment schedules, early-repayment settlement, arrears management and collections.

###### 2.4 SYS-11 (Fraud & AML Platform):

Watches arrears fraud patterns.

##### 3 Preconditions

- Live credit (UC-07).

##### 4 Basic Flow of Events

1. App shows the repayment schedule, next instalment, remaining capital.
2. Customer can make an early repayment (partial/full) — app computes settlement figure.
3. Arrears view: if instalments missed, shows the arrears position and self-service cure options.
4. All actions hit SYS-15 and return updated state.

> **Sequence diagram:** → Annex B §8 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Settlement quote expired>

Trigger: step 2. Recompute before accepting.

###### 5.2 <Alternate flow: Arrears beyond policy threshold>

Trigger: step 3. Self-service cure disabled; routed to servicing ops (human contact) with
vulnerability handling.

###### 5.3 <Alternate flow: Data desync SYS-15 ↔ app>

Trigger: step 1. Stale-data banner, no actions allowed on stale figures (fail-safe).

##### 6 Subflows

###### 6.1 <Subflow: Stale-data guard>

1. Compare the app's view timestamp against the SYS-15 state on every action.
2. Desync → stale-data banner; action endpoints disabled (fail-safe).

###### 6.2 <Subflow: Early-repayment settlement>

1. App computes the settlement figure (partial or full).
2. Expired quote → recompute before acceptance.
3. Action hits SYS-15; updated state returned to the app.

##### 7 Key Scenarios

###### 7.1 <Scenario: Servicing action completed>

1. Servicing records consistent; customer actions logged.

###### 7.2 <Scenario: Stale figures>

1. Actions blocked with a stale-data banner — no operations on desynced data.

##### 8 Post-conditions

###### 8.1

Servicing records consistent.

###### 8.2

Customer actions logged.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Schedule view, early repayment (partial/full) with settlement figure,
arrears view with self-service cure options.

**Usability (U):** Self-service cure where policy allows; clear arrears position display
with a human-contact route when disabled.

**Reliability (R):** Fail-safe stale-data guard; sensitive financial PII encrypted
(PROC-41); audit trail (CR-D-10.2-001).

**Performance (P):** N/A — no attested timing constraint for servicing actions.

**Supportability (S):** The full payment-fraud control set lands with PKG-D (noted in the
annex) — the servicing surface is designed to extend.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-15 (repayment schedules, arrears management, collections).
- **Constrained by:** PROC-43 (MFA), PROC-41 (sensitive financial PII encryption).
- **Rules / NFR:** CR-D-10.2-001, CR-D-09.1-001 (records).
- **Threats addressed:** MUC-01-analogue (session takeover → fraudulent early repayments), payment-fraud class (full set with PKG-D).
- **NIST anchors:** PR.DS-01, AU.A-06.

*MUC-C3 detail cards (referenced above):*

#### MUC-C3-01 — Application Data Crafted to Game OmniScore

**Misactor:** Fraudulent applicant (or organised broker).
**Threatens:** UC-03 (declarations), UC-04 (scoring).
**Preconditions:** Knowledge (or probing) of the model's feature sensitivities.
**Attack Flow:**
1. Applicant inflates/stabilises declared income features or times account movements to maximise score.
2. Organised variant: many applications probing decision boundaries.
**Impact:** Bad debt booked on manipulated inputs; model drift masked as market change.
**Mitigated by:** UC-04 ext. 1a (out-of-distribution flags → human path), SYS-11 fraud screening (UC-03 step 4), bias/drift monitoring pipeline (SYS-03), bureau cross-checks at UC-06.
**NIST anchors:** DE.AE-02, GV.MT-01.

#### MUC-C3-04 — Discriminatory Bias Exploitation / Harm

**Misactor:** None (emergent model behaviour) or adversarial probing by researchers/regulators.
**Threatens:** UC-04 (score), UC-05 (explanation), bank's AI Act/GDPR posture.
**Preconditions:** Training data with historical bias slipping past validation.
**Attack Flow:**
1. Protected-class proxies correlate with score; adverse impact concentrated in a group.
2. Explanations (UC-05) surface the pattern publicly.
**Impact:** Regulatory enforcement (AI Act Art. 26/GDPR Art. 22), reputational damage, remediation cost.
**Mitigated by:** SYS-03 bias monitoring pipeline (Doc04 §1.1 attested), PROC-50 (drift monitoring), UC-04 reason codes + UC-05 transparency, governance review (CR-D-09.x), BPR-D-12.3-001 oversight thresholds.
**NIST anchors:** MEASURE-2.7, GV.PO-P1.

#### MUC-C3-05 — Explainability Gaming (spoofed reason codes)

**Misactor:** Malicious insider (ML engineering) or compromised pipeline.
**Threatens:** UC-04 step 3, UC-05.
**Preconditions:** Write access to the reason-code generation or decision records.
**Attack Flow:**
1. Reason codes decoupled from actual model behaviour (cosmetic explanations hiding discriminatory factors).
2. Audit trail shows plausible explanations inconsistent with model versions.
**Impact:** Systemic compliance fraud — explanations exist but are false; worst-case discovery by a regulator.
**Mitigated by:** UC-04 (reason codes generated in the model runtime, log-anchored to model version), UC-06 ext. 1a (fail-closed on incomplete context), CAP-08 (model tampering detection), immutable decision records (CR-D-10.2-001), quarterly access reviews (PROC-11).
**NIST anchors:** PR.DS-01, AU.A-06, DE.CM-09.

### 4.3 PKG-A — Onboarding & KYC (6)

| UC ID | Title | Primary Actor | Prio |
|-------|-------|---------------|------|
| UC-09 | Open Account via Mobile App | Customer (Retail) | CRITICAL |
| UC-10 | eIDAS Identity Verification | Customer (Retail) | CRITICAL |
| UC-11 | KYC Document Upload & Vault Filing (SYS-16, 10y retention) | Customer (Retail) | CRITICAL |
| UC-12 | Sanctions & PEP Screening | SYS-11 (Fraud & AML Platform) | CRITICAL |
| UC-13 | OmniScore Consent & Data-Use Acknowledgement | Customer (Retail) | HIGH |
| UC-14 | Tax Residency Self-Certification (FATCA/CRS) | Customer (Retail) | HIGH |

#### Use-Case: {UC-09} Open Account via Mobile App

##### 1 Brief Description

The customer opens a new account end-to-end in the mobile app: product selection, personal
data capture, identity verification (UC-10), KYC document filing (UC-11), screening (UC-12)
and data-use acknowledgements (UC-13, UC-14). It is triggered when a prospective customer
starts onboarding. Success produces an active account with SCA-bound credentials — the entry
gate for every PKG-B journey.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Provides personal data, identity evidence, documents and acknowledgements; receives the
activated account.

###### 2.2 SYS-02 (Mobile app channel):

PSD2 SCA-protected session; captures the onboarding data and orchestrates the verification
steps.

###### 2.3 SYS-17 (CRM):

Holds the customer 360 record created during onboarding (FLOW-11 onboarding path:
SYS-14 + SYS-17 CRM).

###### 2.4 SYS-11 (Fraud & AML Platform):

Runs the KYC/AML screening step of onboarding (FLOW-11: identity documents + screening).

###### 2.5 SYS-16 (Document vault):

Files the KYC document set (STORE-08; 10-year retention per BaFin/GoBD).

##### 3 Preconditions

- Customer holds a valid government ID document.
- App installed on a device capable of hardware-backed signing (SYS-02 attested capability).

##### 4 Basic Flow of Events

1. Customer selects account type and product conditions; app shows the key information document.
2. Customer enters personal data (identification data, tax ID); app validates completeness.
3. Identity verification runs (UC-10); result recorded against the onboarding record.
4. Customer files the KYC document set in the vault (UC-11).
5. SYS-11 runs sanctions/PEP screening (UC-12); customer acknowledges OmniScore data use (UC-13) and files the tax self-certification (UC-14).
6. Onboarding record completed; account activated; credentials issued under PSD2 SCA (SYS-02).

> **Sequence diagram:** → Annex B §9 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Identity verification cannot be completed>

Trigger: step 3 (UC-10 remediation exhausted). Onboarding paused; branch/remediation queue
offered. No account activation without a verified identity result (fail-closed).

###### 5.2 <Alternate flow: Screening hit>

Trigger: step 5 (UC-12 true match or open alert). Onboarding blocked pre-activation; routed
to the financial-crime queue. No activation until cleared.

###### 5.3 <Alternate flow: Abandoned onboarding>

Trigger: any step, session abandoned. Draft retained with expiry; personal data captured in
the draft erased after expiry (CR-D-05.3-001 erasure discipline).

##### 6 Subflows

###### 6.1 <Subflow: Onboarding record assembly>

1. Single onboarding record feeds UC-10..UC-14; fields minimised to the declared purpose
   (CR-D-05.1-001 data minimization).
2. Every step appends its evidence (verification, documents, screening, consents) to the same
   record — one auditable chain.

###### 6.2 <Subflow: Credential issuance>

1. Initial credentials bound at first PSD2 SCA login (UC-15); hardware-backed signing key
   enrolled on the customer device.
2. No active account exists before SCA binding succeeds.

##### 7 Key Scenarios

###### 7.1 <Scenario: Account opened>

1. Active account with SCA-bound credentials; complete KYC evidence chain from UC-10..UC-14
   anchored to the onboarding record.

###### 7.2 <Scenario: Blocked onboarding>

1. Screening hit or failed verification; onboarding paused in the correct queue; no activation.

##### 8 Post-conditions

###### 8.1

Account active with SCA-bound credentials on a bound device.

###### 8.2

Complete KYC evidence chain (identity, documents, screening, consents) on record.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Product selection, data capture, verification/document/screening/consent
orchestration (UC-10..UC-14), activation and credential issuance.

**Usability (U):** Guided flow with resumable drafts; explicit status of the onboarding chain.

**Reliability (R):** Every account passes verification and screening before activation
(fail-closed); PSD2 SCA session resists takeover (MUC-01-analogue).

**Performance (P):** N/A — no attested timing constraint for onboarding.

**Supportability (S):** Minimised data model (CR-D-05.1-001) and 10-year KYC retention
(CR-D-05.2-001) keep the onboarding chain auditable and stable for regulator review.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-02 (mobile channel; PSD2 SCA via open-standard identity delegation; hardware-backed signing), SYS-16 (KYC document vault; 10-year retention per BaFin/GoBD), SYS-11 (fraud detection & AML/KYC), SYS-17 (customer 360); FLOW-11 (onboarding SYS-14 + SYS-17 → KYC/AML SYS-11: identity documents + screening); Doc19 CR-D-05.2-001 (10-year financial record retention).
- **Constrained by:** PROC-10 (identity provisioning), PROC-39 (encryption at rest), PROC-20 (data minimization review), PROC-21 (tiered retention).
- **Rules / NFR:** CR-D-05.2-001 (retention), CR-D-05.1-001 (minimization), CR-D-03.1-001 (unified identity + MFA), CR-D-01.1-001 (encryption at rest).
- **Threats addressed:** MUC-01-analogue (session takeover during onboarding), MUC-C3-01 (manipulated declared data — the same data feeds OmniScore downstream, UC-04).
- **NIST anchors:** PR.AA-01, PR.DS-01.

#### Use-Case: {UC-10} eIDAS Identity Verification

##### 1 Brief Description

The customer's identity is verified as the identity anchor of the KYC record: document data
captured in the app, proofing executed, and the trust exchange carried by the open-standard
identity delegation with eIDAS-qualified certificate infrastructure attested for OmniBank
channels. It is triggered inside UC-09 (step 3) and is reusable for re-identification after
credential loss.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Presents the identity document and completes the proofing challenge.

###### 2.2 SYS-02 (Mobile app channel):

Captures the document evidence; performs hardware-backed signing; delegates identity per the
attested open-standard identity delegation.

###### 2.3 SYS-18 (Open Banking / PSD2 API Gateway):

Trust anchor: open banking APIs terminate in a DMZ with PSD2-compliant eIDAS-qualified
certificates (Doc04 §2.2).

###### 2.4 SYS-11 (Fraud & AML Platform):

Consumes the verification result into the KYC file (FLOW-11).

###### 2.5 Head of Compliance Operations:

Owns KYC quality (SYS-16 owner); consumes remediation-queue metrics.

##### 3 Preconditions

- UC-09 draft onboarding record exists.
- Valid ID document; device capable of secure capture and hardware-backed signing.

##### 4 Basic Flow of Events

1. App captures the document data and confirmation evidence (photo of document + holder).
2. Proofing is performed against the captured evidence.
3. Trust exchange uses the eIDAS-qualified certificate infrastructure (SYS-18 DMZ attestation) — the counterparty certificate chain is validated before any personal data crosses the boundary.
4. Result (verified/failed + method) recorded immutably against the onboarding record (CR-D-10.2-001 discipline).
5. A verified identity result unlocks the UC-11/UC-12 continuation.

> **Sequence diagram:** → Annex B §10 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Document invalid or expired>

Trigger: step 1. Guided re-capture (max 3 attempts), then the branch/remediation path.

###### 5.2 <Alternate flow: Proofing service unavailable>

Trigger: step 2. Onboarding paused fail-closed — there is NO manual override that skips
proofing.

###### 5.3 <Alternate flow: Evidence mismatch>

Trigger: step 2. Remediation queue with human review; no automatic retry beyond the attempt
budget.

##### 6 Subflows

###### 6.1 <Subflow: Certificate-based trust validation>

1. Validate the counterparty certificate chain (eIDAS-qualified, PSD2-compliant) before data
   exchange (CR-D-01.2-001 transport discipline).
2. Invalid/revoked chain → fail-closed; no fallback to unauthenticated exchange.

###### 6.2 <Subflow: Verification evidence logging>

1. Log method, timestamp and outcome to the KYC record (append-only).
2. Evidence is anti-repudiation-grade for later audits (CR-D-10.2-001).

##### 7 Key Scenarios

###### 7.1 <Scenario: Identity verified>

1. Identity anchor on the KYC record; UC-11/UC-12 unlocked; activation possible.

###### 7.2 <Scenario: Unresolvable proofing>

1. Remediation queue; no account; customer guided to the branch path.

##### 8 Post-conditions

###### 8.1

Verified identity result (method + outcome) recorded on the KYC record.

###### 8.2

Fail-closed invariant holds: no account activation without a verified identity result.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Evidence capture, proofing orchestration, certificate trust validation,
result logging.

**Usability (U):** Guided capture with an attempt budget (3) before human remediation.

**Reliability (R):** Fail-closed on proofing or certificate failure; evidence append-only.

**Performance (P):** N/A — no attested verification latency.

**Supportability (S):** The method field keeps the proofing schema open for future eIDAS
wallet integration (open-standard identity delegation attested for SYS-02).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-02 (PSD2 SCA via open-standard identity delegation; hardware-backed signing); Doc04 §2.2 (SYS-18 open banking APIs terminate in a DMZ with PSD2-compliant eIDAS-qualified certificates); FLOW-11 (identity documents into KYC/AML).
- **Constrained by:** PROC-10 (identity provisioning), PROC-45 (FIDO2 authentication), PROC-40 (transport security).
- **Rules / NFR:** CR-D-01.2-001 (transport + certificate validation), CR-D-03.1-001 (unified identity), CR-D-10.2-001 (immutable records).
- **Threats addressed:** MUC-01-analogue (proofing-session hijack — SCA-bound, certificate-validated channel); synthetic identity is backstopped by screening (UC-12).
- **NIST anchors:** PR.AA-01, PR.DS-02.

#### Use-Case: {UC-11} KYC Document Upload & Vault Filing (SYS-16, 10y retention)

##### 1 Brief Description

The customer's KYC document set is captured in the app and filed in the document vault
(SYS-16) with encryption, integrity hashing and retention metadata (account lifetime + 10
years per BaFin/GoBD). It is triggered inside UC-09 (step 4); the filed set feeds screening
(FLOW-11) and remains the KYC evidence of record.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Captures/uploads the required document set.

###### 2.2 SYS-02 (Mobile app channel):

Validates document class/legibility client-side; uploads over the SCA session.

###### 2.3 SYS-16 (Document vault):

Files documents with encryption (HSM-bound CMK) and integrity hashing; enforces the 10-year
retention metadata (STORE-08 attested).

###### 2.4 SYS-11 (Fraud & AML Platform):

Consumes the filed document set for screening (FLOW-11).

###### 2.5 Head of Compliance Operations:

Owner of the vault (SYS-16); owns the document-class catalogue.

##### 3 Preconditions

- Identity verified (UC-10).
- Required document set defined for the account type.

##### 4 Basic Flow of Events

1. App prompts for the required document set (per account type) with capture guidance.
2. Customer captures/uploads each document; app validates class and legibility.
3. Upload over the authenticated channel; SYS-16 applies encryption with HSM-bound CMK and integrity hashing (STORE-08 attested).
4. Documents filed with retention metadata: account lifetime + 10 years (BaFin/GoBD — CR-D-05.2-001).
5. Filing receipt logged against the onboarding record; SYS-11 screening consumes the set (FLOW-11).

> **Sequence diagram:** → Annex B §11 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Unsupported or illegible document>

Trigger: step 2. Guided correction per document class (max 3 attempts), then agent assist
queue.

###### 5.2 <Alternate flow: Vault unavailable>

Trigger: step 3. Upload queued client-side with retry; onboarding paused fail-closed —
onboarding never reaches "verified" with unfilled documents.

###### 5.3 <Alternate flow: Wrong document class>

Trigger: step 2. Routed to the compliance queue for classification instead of silent
acceptance.

##### 6 Subflows

###### 6.1 <Subflow: Integrity stamping>

1. Hash computed at ingest (STORE-08 integrity hashing attested).
2. Any later tamper attempt is detectable against the ingest hash — evidence grade for audits.

###### 6.2 <Subflow: Retention metadata stamping>

1. Documents classified under the legal-obligation retention (account lifetime + 10 years,
   BaFin/GoBD exemption — CR-D-05.2-001).
2. Erasure requests on other personal data are honoured per UC-01 without touching the
   retention-exempt KYC set.

##### 7 Key Scenarios

###### 7.1 <Scenario: Documents filed>

1. Encrypted, hashed, retention-stamped set in SYS-16; screening fed (FLOW-11); onboarding
   continues.

###### 7.2 <Scenario: Incomplete set>

1. Onboarding cannot complete; missing-class checklist drives the customer; compliance queue
   if unresolvable.

##### 8 Post-conditions

###### 8.1

Document set filed in SYS-16 with integrity hash + retention metadata.

###### 8.2

Onboarding cannot reach "active" without a complete filed set.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Upload, class/legibility validation, encryption, integrity hashing,
retention stamping, screening handoff.

**Usability (U):** Guided capture per document class with a progress checklist.

**Reliability (R):** Fail-closed on vault outage; integrity hashing detects any tampering.

**Performance (P):** N/A — no attested upload timing constraint.

**Supportability (S):** Document classes configurable per product without vault schema
change.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-16 (KYC document vault; 10-year retention per BaFin/GoBD); Doc04 §2 STORE-08 (encryption with HSM-bound CMK; integrity hashing; account lifetime + 10 years); FLOW-11 (documents into KYC/AML screening).
- **Constrained by:** PROC-39 (encryption at rest), PROC-02 (HSM key lifecycle), PROC-21 (tiered retention), UC-01 (erasure interplay).
- **Rules / NFR:** CR-D-05.2-001 (retention), CR-D-01.1-001 (encryption at rest), CR-D-01.3-001 (key custody), CR-D-05.3-001 (erasure discipline).
- **Threats addressed:** MUC-01-analogue (hijacked session uploading malicious content — class validation at ingest + integrity hashing).
- **NIST anchors:** PR.DS-01, PR.DS-P1.

#### Use-Case: {UC-12} Sanctions & PEP Screening

##### 1 Brief Description

SYS-11 screens the onboarding customer against sanctions and PEP lists (attested capability)
via the attested screening provider, and the result gates account activation. It is
triggered when identity verification and document filing are complete (UC-09 steps 3–4);
true matches block activation and feed STR/CTR generation.

##### 2 Actor Brief Descriptions

###### 2.1 SYS-11 (Fraud & AML Platform) — Primary Actor:

Executes sanctions/PEP screening and STR/CTR generation (attested capabilities); raises
match alerts.

###### 2.2 Sanctions screening provider (third party):

List provider behind SYS-11 (FLOW-11 attested subprocessor).

###### 2.3 Head of Financial Crime:

Owns match dispositions and the financial-crime queue (SYS-11 owner).

###### 2.4 SYS-16 (Document vault):

Files screening evidence alongside the KYC set.

###### 2.5 Customer (Retail):

Subject of the screening; informed of onboarding status.

##### 3 Preconditions

- Identity verified (UC-10) and document set filed (UC-11).
- Onboarding record carries the customer identification data (name, DOB, identifiers).

##### 4 Basic Flow of Events

1. Onboarding record triggers screening (FLOW-11 path).
2. SYS-11 screens the customer data against sanctions/PEP lists via the screening provider.
3. No hit → result recorded; onboarding continues.
4. Potential match → alert with matched-list evidence into the financial-crime queue.
5. Disposition: true match → activation blocked + STR/CTR generation; false positive → documented disposition.
6. Outcome filed to SYS-16 and anchored immutably to the onboarding record (CR-D-10.2-001).

> **Sequence diagram:** → Annex B §12 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Screening provider outage>

Trigger: step 2. Screening unavailable = onboarding paused (fail-closed); screening is a
gate and is never skipped.

###### 5.2 <Alternate flow: List update after account opening>

Trigger: post-activation list change. Retro-screening of the affected population; hits enter
the queue with the same disposition flow.

###### 5.3 <Alternate flow: Analyst disagreement>

Trigger: step 5. Four-eyes escalation (second reviewer) before the disposition is final.

##### 6 Subflows

###### 6.1 <Subflow: Match disposition>

1. Record the match/no-match rationale immutably with the evidence snapshot.
2. Disposition quality (false-positive rate) feeds provider-tuning reviews.

###### 6.2 <Subflow: STR/CTR handoff>

1. True match → STR/CTR generation (attested SYS-11 capability) on the regulatory-reporting
   path.
2. Report events forwarded to the audit sink (CR-D-10.2-001 records discipline).

##### 7 Key Scenarios

###### 7.1 <Scenario: Clean screening>

1. Screening result anchored to the onboarding record; activation proceeds.

###### 7.2 <Scenario: True match>

1. Account blocked pre-activation; STR generated; financial-crime case on record.

##### 8 Post-conditions

###### 8.1

Screening result immutably anchored to the onboarding/KYC record.

###### 8.2

No account activation with an open or true-match screening result.

##### 9 Special Requirements (FURPS+)

**Functional (F):** List screening, match alerting, disposition, STR/CTR generation,
retro-screening.

**Usability (U):** Analyst queue with side-by-side match evidence; guided disposition forms.

**Reliability (R):** Fail-closed on provider outage; every onboarding screened exactly once
per trigger.

**Performance (P):** N/A — no attested screening latency.

**Supportability (S):** Provider abstraction behind SYS-11 allows list-provider change
without flow change (CR-D-06.4-001 exit-strategy discipline).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-11 (fraud detection & AML/KYC; sanctions screening; STR/CTR generation); FLOW-11 (Sanctions screening provider as subprocessor); Doc04 §1.1 SYS-16 (evidence vault).
- **Constrained by:** PROC-23 (third-party processor audits), PROC-24 (vendor risk assessment), CAP-02 (SOC monitoring), CAP-10 (immutable logs).
- **Rules / NFR:** CR-D-06.1-001 (third-party risk incl. TPPs/providers), CR-D-06.3-001 (contractual security obligations), CR-D-06.4-001 (concentration + exit), CR-D-10.2-001 (immutable records).
- **Threats addressed:** MUC-01-analogue (screening-result tampering — immutable anchoring), MUC-C3-01 (manipulated identity data degrading screening quality — document/bureau cross-checks at UC-10).
- **NIST anchors:** DE.AE-02, AU.A-06.

#### Use-Case: {UC-13} OmniScore Consent & Data-Use Acknowledgement

##### 1 Brief Description

Before any scoring-relevant data is processed, the customer receives the OmniScore data-use
notice — what data, for what purpose, the model-in-the-loop and the Art. 22 human path — and
acknowledges or declines it. It is triggered during onboarding (UC-09 step 5) and before
UC-03 scoring; the acknowledgement is recorded with timestamp and notice version as evidence.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Reads the notice; acknowledges or declines; may withdraw at any time.

###### 2.2 SYS-02 (Mobile app channel):

Presents the notice; captures the acknowledgement.

###### 2.3 DPO:

Owner of the consent records (consent pattern per UC-03 §2.5).

###### 2.4 SYS-14 (Loan Origination):

Consumes the acknowledgement as a precondition of the decisioning flow (UC-04).

###### 2.5 Head of AI Governance:

Owns the transparency of the AI use described in the notice.

##### 3 Preconditions

- Onboarding record exists (UC-09); the customer has reached a scoring-relevant processing
  step.

##### 4 Basic Flow of Events

1. App presents the OmniScore data-use notice (data categories, purpose, automated scoring, Art. 22 rights incl. the human path).
2. Customer acknowledges or declines.
3. Acknowledgement recorded with timestamp + notice version against the customer/application record.
4. Declined → manual path only (UC-03 ext. 5.1, Art. 22(3)).
5. Withdrawal at any time → recorded; downstream automated scoring stops; documented retention exemptions still apply to kept records (CR-D-05.2-001 interplay).

> **Sequence diagram:** → Annex B §13 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Declined>

Trigger: step 2. Application proceeds on the manual path without automated scoring
(Art. 22(3) right not to be subject to solely automated decisions).

###### 5.2 <Alternate flow: Withdrawal mid-application>

Trigger: post-acknowledgement withdrawal. Application rerouted to manual underwriting
(UC-06); no further automated scoring.

###### 5.3 <Alternate flow: Notice version update>

Trigger: regulatory/model change. Re-acknowledgement requested at the next scoring-relevant
event; old evidence remains on record.

##### 6 Subflows

###### 6.1 <Subflow: Consent record write>

1. Timestamp + notice version + scope recorded at GDPR-compliant granularity.
2. Evidence audit-ready and linked to the application record (feeds UC-03/UC-04 preconditions).

###### 6.2 <Subflow: Withdrawal propagation>

1. Withdrawal flag visible to SYS-14/SYS-03 decisioning; automated scoring blocked.
2. Already-made decisions remain on the documented retention basis (CR-D-05.2-001).

##### 7 Key Scenarios

###### 7.1 <Scenario: Acknowledged>

1. Consent evidence on record before any scoring; UC-04 precondition satisfied.

###### 7.2 <Scenario: Withdrawn>

1. Manual path enforced; withdrawal evidence recorded.

##### 8 Post-conditions

###### 8.1

Consent evidence (timestamp + notice version) on record before any scoring.

###### 8.2

Withdrawal blocks automated scoring within the same application immediately.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Notice presentation, acknowledgement capture, withdrawal propagation.

**Usability (U):** Plain language; declination is one tap — no dark patterns.

**Reliability (R):** Consent checked as a UC-04 precondition (fail-closed).

**Performance (P):** N/A — no attested timing constraint.

**Supportability (S):** Notice versioning supports regulatory/model change without schema
break; historical acknowledgements remain retrievable.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §2 credit-scores line (Art. 22 automated decision; "Right to human review (Art. 22)"); Doc04 §1.1 SYS-03 (credit scoring), SYS-02 (app channel); Doc19 CR-D-05.4-001 (transparency incl. scoring factors).
- **Constrained by:** UC-03 (application consent record), PROC-01 (data subject rights), UC-06 (human path).
- **Rules / NFR:** CR-D-05.1-001 (minimization), CR-D-05.4-001 (scoring-factor transparency), CR-D-09.1-001 (governance documentation).
- **Threats addressed:** MUC-C3-04 (bias harm — informed data subjects plus the human path are first-line mitigation), MUC-C3-05 (spoofed transparency — the notice version is log-anchored).
- **NIST anchors:** GV.PO-P1, CT.DP-P2.

#### Use-Case: {UC-14} Tax Residency Self-Certification (FATCA/CRS)

##### 1 Brief Description

The customer files a tax residency self-certification during onboarding, which is anchored
to the KYC record with the same protection envelope as the document vault. It is triggered
inside UC-09 (step 5); certification status gates account activation and change events
re-trigger certification.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Declares residency(ies) and TINs; signs the self-certification.

###### 2.2 SYS-02 (Mobile app channel):

Presents the form; validates field completeness.

###### 2.3 SYS-16 (Document vault):

Files the certification with the KYC record (encryption + retention metadata, STORE-08).

###### 2.4 Head of Compliance Operations:

Owns the tax-reporting obligation and the re-certification process.

##### 3 Preconditions

- Onboarding record exists (UC-09); identity verified (UC-10).

##### 4 Basic Flow of Events

1. App presents the tax residency self-certification form (residency(ies), TINs, explanation fields).
2. Customer completes and signs the certification.
3. Certification filed in SYS-16 with the KYC record (same encryption/retention envelope as UC-11).
4. Profile change events (e.g. address/residency change) open a re-certification task with an SLA.
5. Certification status gates account activation — incomplete/stale blocks activation.

> **Sequence diagram:** → Annex B §14 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Missing TIN>

Trigger: step 2. Guided explanation capture (documented reason per form rules); certification
acceptable with the documented explanation.

###### 5.2 <Alternate flow: Indicia of change>

Trigger: step 4. Re-certification task opened with SLA; reporting process protected while
the task ages.

###### 5.3 <Alternate flow: Refusal to certify>

Trigger: step 5. Account cannot activate — the certification is a legal-obligation gate.

##### 6 Subflows

###### 6.1 <Subflow: Re-certification trigger>

1. Profile-change events enqueue a renewal task with SLA tracking.
2. Aged tasks escalate to Compliance Operations before reporting is impaired.

###### 6.2 <Subflow: Filing evidence>

1. Certification anchored to the KYC record; retrievable for audits and regulatory reporting.
2. Prior certification versions retained per CR-D-05.2-001.

##### 7 Key Scenarios

###### 7.1 <Scenario: Certified onboarding>

1. Self-certification on file; account activated.

###### 7.2 <Scenario: Stale certification>

1. Renewal task open with SLA; activation/new products gated until refreshed.

##### 8 Post-conditions

###### 8.1

Signed self-certification filed with the KYC record.

###### 8.2

Activation blocked while certification is missing or stale.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Form capture, TIN validation, filing, re-certification triggers.

**Usability (U):** Guided field help; explanation capture for missing TINs.

**Reliability (R):** Certification is a hard activation gate (fail-closed).

**Performance (P):** N/A — no attested timing constraint.

**Supportability (S):** Form schema versioned; prior certifications remain retrievable
(CR-D-05.2-001).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-16 (KYC document vault; 10-year retention per BaFin/GoBD); Doc04 §2 government-identifiers line (Tax ID — Art. 6(1)(c) legal obligation; account lifetime + 10 years, BaFin/GoBD exemption; pseudonymisation after closure).
- **Constrained by:** UC-11 (vault filing), PROC-21 (tiered retention), UC-01 (erasure — documented exemption interplay).
- **Rules / NFR:** CR-D-05.2-001 (retention), CR-D-01.1-001 (encryption at rest), CR-D-05.1-001 (minimal fields).
- **Threats addressed:** MUC-01-analogue (hijacked session altering certifications — SCA session + change logging, CR-D-10.2-001).
- **NIST anchors:** PR.DS-01, AU.A-06.

### 4.4 PKG-B — Digital Banking Core (6)

| UC ID | Title | Primary Actor | Prio |
|-------|-------|---------------|------|
| UC-15 | Login with PSD2 SCA | Customer (Retail) | CRITICAL |
| UC-16 | View Balances & Transactions | Customer (Retail) | HIGH |
| UC-17 | SEPA Transfer (incl. Instant) | Customer (Retail) | CRITICAL |
| UC-18 | Manage Cards (block/limits) | Customer (Retail) | HIGH |
| UC-19 | Standing Orders | Customer (Retail) | MEDIUM |
| UC-20 | Statements & Export | Customer (Retail) | MEDIUM |

#### Use-Case: {UC-15} Login with PSD2 SCA

##### 1 Brief Description

The customer authenticates to the mobile app under mandatory PSD2 SCA: strong cryptographic
key + biometrics, hardware-backed signing and risk-based step-up (all attested SYS-02
capabilities), with behavioural signals feeding fraud detection. It is triggered at every
session start; the resulting SCA session is the trust root for every PKG-B/PKG-D journey.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Presents credentials + SCA factor; completes step-up when asked.

###### 2.2 SYS-02 (Mobile app channel):

Enforces PSD2 SCA (strong cryptographic key + biometrics; hardware-backed signing);
customer-set risk-based step-up (attested).

###### 2.3 SYS-24 (Managed identity service):

Validates the session/identity backend (attested identity service for digital channels).

###### 2.4 SYS-11 (Fraud & AML Platform):

Consumes behavioural biometric signals (EU-processed, explicit consent, attested) for
session-risk evaluation.

##### 3 Preconditions

- Account active with SCA-bound credentials (UC-09/UC-15 device binding).

##### 4 Basic Flow of Events

1. Customer opens the app and presents credentials + SCA factor (biometrics / hardware-backed key).
2. Session validated against the managed identity service (SYS-24).
3. Behavioural signals evaluated; session risk computed.
4. Low risk → session established; elevated risk → step-up challenge (attested risk-based step-up).
5. Session bound to the device (hardware-backed signing key) and handed to the product journeys.

> **Sequence diagram:** → Annex B §15 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Step-up fails repeatedly>

Trigger: step 4. Session denied; security event logged to the monitoring plane (CAP-02 feed,
CR-D-10.1-001).

###### 5.2 <Alternate flow: Credential recovery>

Trigger: failed authentication, lost device. Re-identification via the UC-10 identity anchor
— never a credential-only reset.

###### 5.3 <Alternate flow: Behavioural anomaly>

Trigger: step 3. Session denied + fraud case raised (SYS-11).

##### 6 Subflows

###### 6.1 <Subflow: Risk-based step-up>

1. Session risk score (behavioural biometrics + device posture) selects the challenge level
   (attested "customer-set; risk-based step-up").
2. Step-up failure count feeds the risk score and the fraud plane.

###### 6.2 <Subflow: Device binding>

1. Hardware-backed signing key enrolled at first SCA (UC-09 subflow 6.2).
2. Re-binding to a new device requires re-identification (UC-10).

##### 7 Key Scenarios

###### 7.1 <Scenario: Session established>

1. SCA session on a bound device; behavioural baseline active; journeys unlocked.

###### 7.2 <Scenario: Takeover attempt>

1. Denied at step-up; security event + fraud case (MUC-01-analogue control holds).

##### 8 Post-conditions

###### 8.1

SCA-authenticated session established on a bound device.

###### 8.2

Failed/denied logins logged as security events.

##### 9 Special Requirements (FURPS+)

**Functional (F):** SCA, session validation, risk evaluation, step-up, device binding.

**Usability (U):** Biometrics as the primary factor; customer-set convenience within the
attested risk-based step-up envelope.

**Reliability (R):** SCA mandatory — no single-factor fallback (attested).

**Performance (P):** N/A — no attested login latency target.

**Supportability (S):** Factor set extensible via the attested open-standard identity
delegation on SYS-02.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-02 (PSD2 SCA mandatory: strong cryptographic key + biometrics; transaction signing; customer-set; risk-based step-up); §2 SYS-24 (managed identity service for digital channels); behavioural biometrics into SYS-11 (EU region, explicit consent, withdrawal deletes).
- **Constrained by:** UC-10 (identity anchor for recovery), PROC-43 (MFA discipline), CAP-02 (security event monitoring).
- **Rules / NFR:** CR-D-03.1-001 (unified identity + MFA), CR-D-03.2-001 (step-up for high-risk transactions), CR-D-01.2-001 (transport security), CR-D-10.1-001 (monitoring).
- **Threats addressed:** MUC-01-analogue (credential theft / session takeover — SCA + risk-based step-up are the control).
- **NIST anchors:** PR.AA-01, DE.AE-02.

#### Use-Case: {UC-16} View Balances & Transactions

##### 1 Brief Description

The customer views account balances and transaction history in the app: live figures from
the core banking backend (FLOW-02 path) and deeper history from the data warehouse (FLOW-13
nightly load), each explicitly freshness-labelled. It is triggered when the customer opens
the accounts overview; every non-live figure carries a staleness marker — no silent stale
data.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Views balances and transactions; drills into history; can enter a dispute (UC-24).

###### 2.2 SYS-02 (Mobile app channel):

Renders the overview; fetches account data over the SCA session.

###### 2.3 SYS-01 (CBS mainframe):

Source of live balances and the recent transaction set (FLOW-02 internet banking → CBS).

###### 2.4 SYS-13 (Customer Data Warehouse):

Source of deep history (FLOW-13 nightly load, attested).

##### 3 Preconditions

- SCA session established (UC-15).

##### 4 Basic Flow of Events

1. Customer opens the accounts overview; app fetches live balances via the core banking backend (FLOW-02 path).
2. Customer opens a transaction list (default window, paged).
3. History beyond the hot set is served from the warehouse (FLOW-13) and marked as such.
4. Every view renders freshness markers where data is not live.
5. Customer can select a transaction and start a dispute (UC-24).

> **Sequence diagram:** → Annex B §16 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: CBS unavailable>

Trigger: step 1. Last-known balances shown with an explicit staleness notice; no fabricated
figures.

###### 5.2 <Alternate flow: Warehouse lag>

Trigger: step 3. Recent history from the core, older from the warehouse, stitched with
visible markers.

###### 5.3 <Alternate flow: Disputed transaction>

Trigger: step 5. Dispute entry point (UC-24) with the transaction context pre-linked.

##### 6 Subflows

###### 6.1 <Subflow: Stale-data guard>

1. Every non-live figure labelled with its source and age (same discipline as UC-08).
2. Labels mandatory — the view cannot suppress them.

###### 6.2 <Subflow: Paging/windowing>

1. Default window with explicit deep-history request.
2. Deep-history requests logged in journey telemetry (CR-D-10.1-001).

##### 7 Key Scenarios

###### 7.1 <Scenario: Overview displayed>

1. Balances + transactions rendered with freshness markers.

###### 7.2 <Scenario: Degraded mode>

1. Explicit staleness notices; no silent stale data.

##### 8 Post-conditions

###### 8.1

Balances/transactions displayed with data-freshness markers.

###### 8.2

Views logged in journey telemetry (CR-D-10.1-001).

##### 9 Special Requirements (FURPS+)

**Functional (F):** Balance fetch, history paging, staleness marking, dispute entry.

**Usability (U):** Single overview; search/filter on transactions.

**Reliability (R):** No silent stale data — degraded mode is explicit.

**Performance (P):** N/A — no attested latency target.

**Supportability (S):** View layer independent of core schema changes (backend façade).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-01 (CBS mainframe) via FLOW-02 (internet banking → CBS transaction path); SYS-13 (CDW) via FLOW-13 (customer + transaction data, nightly).
- **Constrained by:** UC-15 (SCA session), PROC-40 (transport security), PROC-41 (field-level encryption of PII at rest).
- **Rules / NFR:** CR-D-01.2-001 (transport), CR-D-01.1-001 (encryption at rest), CR-D-10.1-001 (journey monitoring).
- **Threats addressed:** MUC-01-analogue (hijacked session reading financial data — SCA + step-up on sensitive views).
- **NIST anchors:** PR.DS-02, PR.DS-01.

#### Use-Case: {UC-17} SEPA Transfer (incl. Instant)

##### 1 Brief Description

The customer executes a SEPA credit transfer (standard or instant): instruction created in
the app, authorised with PSD2 SCA transaction signing (hardware-backed, attested), screened
in the real-time fraud stream (FLOW-10, attested) and executed via the payments core. It is
triggered when the customer submits a transfer; held instructions are never silently
executed.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Creates the transfer and authorises it with transaction signing.

###### 2.2 SYS-02 (Mobile app channel):

Capture + confirmation summary + SCA transaction signing (attested).

###### 2.3 SYS-11 (Fraud & AML Platform):

Screens the instruction in the real-time transaction stream (FLOW-10 attested).

###### 2.4 SYS-01 (CBS / payments core):

Executes the payment (payments core on-prem, attested); instant variant via the instant
scheme path.

##### 3 Preconditions

- SCA session (UC-15); beneficiary data available; transfer within limits (UC-25).

##### 4 Basic Flow of Events

1. Customer creates the transfer (beneficiary, amount, reference); app validates the IBAN and shows the confirmation summary.
2. Customer approves with SCA transaction signing (hardware-backed key, attested).
3. SYS-11 screens the instruction in the real-time stream (FLOW-10).
4. No flag → execution via the payments core; instant variant uses the instant scheme path when available, else standard SEPA with clear labelling.
5. Confirmation + entry in history (UC-16); signing + screening evidence on the payment record.

> **Sequence diagram:** → Annex B §17 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Fraud flag>

Trigger: step 3. Instruction held; customer verification via the alert loop (UC-30); no
silent execution.

###### 5.2 <Alternate flow: Limit breach>

Trigger: step 1. Declined with the limit context surfaced (manage at UC-25).

###### 5.3 <Alternate flow: New beneficiary>

Trigger: step 2. Step-up signing enforced (attested risk-based step-up on transactions).

##### 6 Subflows

###### 6.1 <Subflow: Transaction signing>

1. Every transfer authorised with the hardware-backed signing key (attested PSD2 SCA
   transaction signing).
2. Signing evidence bound to the payment record (CR-D-10.2-001).

###### 6.2 <Subflow: Instant path>

1. Scheme availability checked at instruction time.
2. Fallback to standard SEPA is explicit in the confirmation (never a silent downgrade).

##### 7 Key Scenarios

###### 7.1 <Scenario: Transfer executed>

1. Signed, screened, booked; evidence chain complete.

###### 7.2 <Scenario: Held instruction>

1. Fraud queue; customer contacted before release; nothing executes silently.

##### 8 Post-conditions

###### 8.1

Transfer executed or explicitly held — never ambiguous.

###### 8.2

Signing + screening evidence on the payment record (CR-D-10.2-001).

##### 9 Special Requirements (FURPS+)

**Functional (F):** Transfer creation, IBAN validation, SCA signing, screening, execution,
instant variant.

**Usability (U):** Beneficiary management with validation; decline reasons include limit
context.

**Reliability (R):** No execution without SCA + screening (fail-closed); PSD2 SCA session
resists takeover (MUC-01-analogue).

**Performance (P):** N/A — no attested transfer SLA.

**Supportability (S):** Payment rails abstracted; instant adoption config-driven.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-02 (transaction signing), SYS-11 (transaction monitoring; FLOW-10 real-time streaming from CBS + Card Mgmt), SYS-01 (CBS mainframe; payments in production on-prem).
- **Constrained by:** UC-15 (SCA session), UC-25 (limits), UC-30 (fraud alert loop), CAP-10 (immutable logs).
- **Rules / NFR:** CR-D-03.2-001 (step-up on high-risk transactions), CR-D-10.1-001 (24/7 monitoring), CR-D-10.2-001 (immutable records).
- **Threats addressed:** MUC-01-analogue (authorised-push-payment fraud from a hijacked session — signing + behavioural signals), payment-fraud class (full loop lands with PKG-D/PKG-F: UC-24, UC-25, UC-30).
- **NIST anchors:** PR.AA-01, DE.AE-02.

#### Use-Case: {UC-18} Manage Cards (block/limits)

##### 1 Brief Description

The customer manages card state and spend limits in the app: temporary block/unblock,
permanent block with reissue, per-card limits with step-up on increases. It is triggered
when the customer opens a card detail; state changes apply to the card authorisation path
(SYS-05, card-scheme security-attestation scope, firewall-segmented — attested).

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Blocks/unblocks the card; sets limits; requests reissue.

###### 2.2 SYS-02 (Mobile app channel):

SCA-protected management surface.

###### 2.3 SYS-05 (Card management):

Executes state/limit changes on the authorisation path (card-scheme security-attestation
scope, isolated via firewall segmentation — attested).

###### 2.4 SYS-11 (Fraud & AML Platform):

Fraud signals inform default states; card state changes feed fraud cases.

##### 3 Preconditions

- SCA session (UC-15); card exists in the customer's portfolio.

##### 4 Basic Flow of Events

1. Customer opens the card detail.
2. Temporary block/unblock executed immediately (block effective before the confirmation is shown).
3. Permanent block → reissue flow offered; fraud linkage if indicated (SYS-11).
4. Per-card limits view/edit; increases require SCA step-up (attested risk-based step-up).
5. Changes confirmed with the authorisation-path state and logged immutably (CR-D-10.2-001).

> **Sequence diagram:** → Annex B §18 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Stolen card>

Trigger: step 3. Permanent block + reissue + fraud case linkage (SYS-11).

###### 5.2 <Alternate flow: Limit increase above threshold>

Trigger: step 4. Additional risk validation; out-of-policy increases take the human review
path.

###### 5.3 <Alternate flow: Scheme-scope maintenance window>

Trigger: step 2. Change queued with explicit status (SYS-05 isolation attested) — no silent
pending states.

##### 6 Subflows

###### 6.1 <Subflow: Block propagation>

1. Ordering rule: the block is effective on the authorisation path before the confirmation
   is rendered.
2. Unblock uses the same authoritative path.

###### 6.2 <Subflow: Change logging>

1. Card-state and limit changes append immutably (CR-D-10.2-001).
2. Change evidence is retrievable for disputes (UC-24) and investigations.

##### 7 Key Scenarios

###### 7.1 <Scenario: Card blocked>

1. Authorisation stream reflects the blocked state; evidence on record.

###### 7.2 <Scenario: Limit raise>

1. Step-up + risk validation passed; new limits live.

##### 8 Post-conditions

###### 8.1

Card state change live on the authorisation path.

###### 8.2

Change evidence on record (supports UC-24 disputes).

##### 9 Special Requirements (FURPS+)

**Functional (F):** Block/unblock, permanent block + reissue, limit management.

**Usability (U):** Block reachable in at most two taps from card detail.

**Reliability (R):** Block-before-confirm ordering; SCA step-up on increases.

**Performance (P):** N/A — no attested timing constraint.

**Supportability (S):** Card-state model mirrors the scheme-scope constraints (SYS-05
segmentation attested).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §2.2 SYS-05 (card management sits in card-scheme security-attestation scope, isolated via firewall segmentation); Doc04 §1.1 SYS-02 (SCA app channel; risk-based step-up), SYS-11 (fraud platform).
- **Constrained by:** UC-15 (SCA session), UC-17 (payment path), UC-24 (disputes), PROC-12 (hardened configuration baseline).
- **Rules / NFR:** CR-D-03.2-001 (step-up), CR-D-10.2-001 (immutable records), CR-D-01.2-001 (transport).
- **Threats addressed:** MUC-01-analogue (attacker blocking cards or raising limits post-takeover — step-up on increases; blocks are protective and reversible).
- **NIST anchors:** PR.AA-01, AU.A-06.

#### Use-Case: {UC-19} Standing Orders

##### 1 Brief Description

The customer schedules recurring payments as standing orders: mandate created with SCA
signing, stored in the payments core, executed on schedule with the same screening as
on-demand payments, and editable/cancellable with re-signing. It is triggered when the
customer creates a standing order.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Creates, edits and cancels standing orders.

###### 2.2 SYS-02 (Mobile app channel):

Mandate capture + SCA signing (attested transaction signing).

###### 2.3 SYS-01 (CBS / payments core):

Stores the mandate and executes on schedule.

###### 2.4 SYS-11 (Fraud & AML Platform):

Screens executions like any payment (FLOW-10 stream).

##### 3 Preconditions

- SCA session (UC-15); within limits at execution time (UC-25).

##### 4 Basic Flow of Events

1. Customer creates the standing order (beneficiary, amount, frequency, start/end); SCA signing.
2. Mandate stored in the payments core (SYS-01).
3. On each due date the core executes; SYS-11 screens the execution (FLOW-10).
4. Failures (e.g. insufficient funds) follow the retry/notification policy — never silent.
5. Customer views/edits/cancels; edits create a new signed mandate version.

> **Sequence diagram:** → Annex B §19 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Insufficient funds at execution>

Trigger: step 4. Bounded retry per schedule + in-app notification; no silent failure.

###### 5.2 <Alternate flow: Amendment>

Trigger: step 5. Old mandate superseded as a versioned record; new mandate re-signed.

###### 5.3 <Alternate flow: Cancellation race>

Trigger: step 5, cancellation while an execution is in flight. Core arbitrates; outcome
communicated to the customer.

##### 6 Subflows

###### 6.1 <Subflow: Mandate versioning>

1. Edits create a new signed version; history retained (CR-D-05.2-001 financial-record
   retention).
2. Only the latest version executes.

###### 6.2 <Subflow: Execution monitoring>

1. Execution outcomes surface in-app and into SYS-11 telemetry.
2. Repeated failures raise a service case.

##### 7 Key Scenarios

###### 7.1 <Scenario: Mandate active>

1. Signed mandate executing on schedule with screening evidence.

###### 7.2 <Scenario: Execution failure>

1. Retry + notification; customer informed; nothing silently drops.

##### 8 Post-conditions

###### 8.1

Mandate stored (signed) and executing on schedule.

###### 8.2

Mandate history retained per financial-record retention (CR-D-05.2-001).

##### 9 Special Requirements (FURPS+)

**Functional (F):** Create/edit/cancel, scheduling, execution, failure handling.

**Usability (U):** Next-3-executions preview before signing.

**Reliability (R):** Failures always notified; retries bounded.

**Performance (P):** N/A — no attested timing constraint.

**Supportability (S):** Frequency model supports calendar/regulation changes without schema
break.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-02 (transaction signing), SYS-01 (CBS mainframe; payments core on-prem), SYS-11 (transaction monitoring; FLOW-10).
- **Constrained by:** UC-17 (signing/screening pattern), UC-25 (limits at execution time), PROC-21 (retention).
- **Rules / NFR:** CR-D-05.2-001 (retention), CR-D-03.2-001 (step-up on signing), CR-D-10.2-001 (records).
- **Threats addressed:** MUC-01-analogue (attacker creating standing orders post-takeover — signing + step-up on creation/edits).
- **NIST anchors:** PR.AA-01, AU.A-06.

#### Use-Case: {UC-20} Statements & Export

##### 1 Brief Description

The customer requests account statements and data exports: generation from the warehouse
history (FLOW-13, attested nightly load) or the live core for current periods, machine-readable
export in the CR-D-05.4-001 portability format, periodic statements archived in the document
vault. It is triggered by an explicit customer request or the periodic statement schedule.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Requests statements/exports; downloads via the app.

###### 2.2 SYS-02 (Mobile app channel):

Request surface + authenticated download (SCA session).

###### 2.3 SYS-13 (Customer Data Warehouse):

History source (FLOW-13 attested).

###### 2.4 SYS-16 (Document vault):

Archive of periodic statements (retention metadata per CR-D-05.2-001).

##### 3 Preconditions

- SCA session (UC-15).

##### 4 Basic Flow of Events

1. Customer requests a statement (period, account, format) or the periodic statement is scheduled.
2. Generation from CDW history (FLOW-13) or live core for current periods.
3. Machine-readable export produced in the CR-D-05.4-001 portability format (incl. scoring factors where applicable).
4. Periodic statements filed to SYS-16; download through the SCA session.
5. Request/dispatch logged against the customer record (anti-exfiltration evidence).

> **Sequence diagram:** → Annex B §20 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Large period requested>

Trigger: step 2. Async generation with notification; download when ready.

###### 5.2 <Alternate flow: Generation failure>

Trigger: step 2. Human contact channel within SLA (UC-05 pattern) — never silent.

###### 5.3 <Alternate flow: Export on risky session>

Trigger: step 4. Re-authentication (step-up) before the download completes.

##### 6 Subflows

###### 6.1 <Subflow: Portability format export>

1. Export follows the CR-D-05.4-001 standardized format (stable for audits and DSARs,
   UC-02/PROC-01).
2. Scoring-factor inclusion keeps the AI transparency clause satisfied.

###### 6.2 <Subflow: Dispatch logging>

1. Every export logged against the customer record (CR-D-10.2-001).
2. Volume anomalies feed the monitoring plane (step-up + fraud signal).

##### 7 Key Scenarios

###### 7.1 <Scenario: Statement delivered>

1. Document delivered + archived; dispatch logged.

###### 7.2 <Scenario: Abnormal export pattern>

1. Volume anomaly → step-up + monitoring signal before further exports.

##### 8 Post-conditions

###### 8.1

Statement/export delivered and logged.

###### 8.2

Periodic statements archived in SYS-16 per retention rules.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Statement generation, export formats, archiving, dispatch logging.

**Usability (U):** Format choice (PDF/machine-readable); period presets.

**Reliability (R):** Never silent on failure (human channel SLA).

**Performance (P):** N/A — no attested timing constraint.

**Supportability (S):** Export schema follows the CR-D-05.4-001 portability format (stable
for audits and data-subject requests).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-13 (CDW; FLOW-13), SYS-16 (DMS), SYS-02 (app channel); Doc19 CR-D-05.4-001 (automated data export/portability incl. AI scoring factors).
- **Constrained by:** UC-02 (data export compliance flow), UC-15 (SCA session), CAP-10 (log evidence).
- **Rules / NFR:** CR-D-05.4-001 (portability), CR-D-05.2-001 (retention), CR-D-10.2-001 (immutable records).
- **Threats addressed:** MUC-01-analogue (mass export from a hijacked session — volume anomaly detection + step-up).
- **NIST anchors:** PR.DS-01, DE.AE-02.

### 4.5 PKG-D — Payments & Open Banking (5)

| UC ID | Title | Primary Actor | Prio |
|-------|-------|---------------|------|
| UC-21 | PSD2 Consent Grant/Revoke | Customer (Retail) | CRITICAL |
| UC-22 | TPP Onboarding & AIS Access (SYS-18) | TPP (Third-Party Provider) | HIGH |
| UC-23 | PIS Payment Initiation with SCA | TPP (Third-Party Provider) | CRITICAL |
| UC-24 | Payment Dispute & Chargeback | Customer (Retail) | HIGH |
| UC-25 | Payment Limits Management | Customer (Retail) | MEDIUM |

#### Use-Case: {UC-21} PSD2 Consent Grant/Revoke

##### 1 Brief Description

The customer grants or revokes PSD2 consent for a Third-Party Provider (TPP) at the open
banking gateway: TPP validated via eIDAS-qualified certificates (DMZ, attested), customer
authenticates with SCA, scope + duration are explicit, and revocation cuts TPP access
immediately. It is triggered when a TPP redirects the customer with a consent request or the
customer manages consents in the app.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Reviews scope/duration; grants or revokes; sees the active-TPP list.

###### 2.2 SYS-18 (Open Banking / PSD2 API Gateway):

TPP onboarding + consent management (attested); eIDAS-qualified certificates in the DMZ.

###### 2.3 TPP (Third-Party Provider):

Requests and consumes the consented access (inbound and outbound third party — FLOW-03
attested).

###### 2.4 SYS-02 (Mobile app channel):

SCA ceremony for the consent (attested SCA discipline).

##### 3 Preconditions

- Customer active (UC-09); TPP presenting valid eIDAS-qualified credentials (UC-22).

##### 4 Basic Flow of Events

1. TPP redirects the customer to the bank with a consent request (AIS/PIS scope, duration).
2. SYS-18 validates the TPP's eIDAS-qualified certificate (attested DMZ termination).
3. Customer authenticates with SCA and reviews scope + duration; scope can be narrowed to the minimum (CR-D-05.1-001).
4. Grant recorded at SYS-18 consent management; TPP receives the consent token.
5. Revocation at any time in the app → token invalidated; TPP access cut; evidence retained (CR-D-10.2-001).

> **Sequence diagram:** → Annex B §21 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Unknown or invalid TPP certificate>

Trigger: step 2. Deny fail-closed — no consent ceremony without a valid certificate chain.

###### 5.2 <Alternate flow: Scope narrowing>

Trigger: step 3. Customer deselects consent elements; the minimal granted scope is what is
recorded (CR-D-05.1-001).

###### 5.3 <Alternate flow: Revoke during active access>

Trigger: step 5. Token invalidated immediately; the TPP's next call fails closed; access-log
evidence retained.

##### 6 Subflows

###### 6.1 <Subflow: Consent scope validation>

1. Scope syntax + duration caps validated server-side at SYS-18.
2. The recorded scope is authoritative for enforcement — never the TPP's claim.

###### 6.2 <Subflow: Revocation propagation>

1. Consent token revoked; dependent access fails closed.
2. Customer sees the active-TPP list with per-TPP revoke actions.

##### 7 Key Scenarios

###### 7.1 <Scenario: Consent granted>

1. Scoped, time-boxed, revocable consent at SYS-18 with SCA evidence.

###### 7.2 <Scenario: Consent revoked>

1. Access cut immediately; evidence retained.

##### 8 Post-conditions

###### 8.1

Consent record at SYS-18 (scope, duration, SCA evidence).

###### 8.2

Revocation cuts TPP access immediately.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Consent request validation, SCA ceremony, grant/revoke, active-TPP
listing.

**Usability (U):** One screen per TPP with plain-language scope toggles.

**Reliability (R):** No consent without SCA; no access without consent (attested PSD2 model).

**Performance (P):** N/A — no attested timing constraint.

**Supportability (S):** Consent schema versioned for PSD2 RTS evolution.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-18 (PSD2 SCA-compliant APIs; TPP onboarding + consent management), SYS-02 (SCA); FLOW-03 (customer consent + account information; TPPs third parties — both inbound and outbound); Doc04 §2.2 (SYS-18 DMZ, PSD2-compliant eIDAS-qualified certificates).
- **Constrained by:** UC-22 (TPP onboarding), UC-15 (SCA), PROC-23 (third-party audits).
- **Rules / NFR:** CR-D-05.1-001 (minimization), CR-D-06.3-001 (third-party obligations), CR-D-10.2-001 (immutable records).
- **Threats addressed:** MUC-01-analogue (consent phishing — customers tricked into granting access; mitigations: plain-language scopes, active-TPP list, one-tap revocation).
- **NIST anchors:** PR.AA-01, AU.A-06.

#### Use-Case: {UC-22} TPP Onboarding & AIS Access (SYS-18)

##### 1 Brief Description

A TPP is onboarded at the open banking gateway and given account-information access strictly
within customer-granted consents: eIDAS-qualified certificate validation, API credentials,
monitored access, suspension path on deviation. It is triggered by a TPP registration request
or an AIS access attempt.

##### 2 Actor Brief Descriptions

###### 2.1 TPP (Third-Party Provider) — Primary Actor:

Registers; consumes AIS APIs within consented scopes.

###### 2.2 SYS-18 (Open Banking / PSD2 API Gateway):

Certificate validation, credential issuance, scoped enforcement (attested TPP onboarding).

###### 2.3 Head of Digital Channels:

Owns SYS-18 (attested ownership); approves TPP registrations.

###### 2.4 Vendor Risk Manager:

Third-party risk assessment for the TPP relationship (PROC-24 discipline).

###### 2.5 SOC (SYS-25):

Consumes AIS access anomalies (SOC tooling attested).

##### 3 Preconditions

- TPP holds valid eIDAS-qualified credentials (PSD2 DMZ attestation).
- Customer consents exist for any AIS scope served (UC-21).

##### 4 Basic Flow of Events

1. TPP registration request with eIDAS-qualified certificate.
2. SYS-18 validates the certificate chain + registration; Head of Digital Channels approves.
3. API credentials issued to the TPP.
4. AIS access served strictly within customer-granted consents (UC-21); access monitored for rate, scope and anomaly patterns.
5. Deviation → throttle/suspend path with human review.

> **Sequence diagram:** → Annex B §22 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Certificate revoked or expired>

Trigger: any handshake. Access cut fail-closed; no data leaves without a valid chain.

###### 5.2 <Alternate flow: Scope violation or anomalous volume>

Trigger: step 4. Automatic throttle + human review; suspension if unresolved.

###### 5.3 <Alternate flow: Concentration concern>

Trigger: portfolio review. Many TPPs on one provider stack → exit-strategy review
(CR-D-06.4-001).

##### 6 Subflows

###### 6.1 <Subflow: Certificate lifecycle gate>

1. Certificate chain validated on every handshake with revocation checking.
2. Expired/revoked → immediate fail-closed denial.

###### 6.2 <Subflow: AIS anomaly monitoring>

1. Access patterns evaluated against consent scopes and baselines.
2. Anomalies alert the SOC (CR-D-10.1-001 monitoring discipline).

##### 7 Key Scenarios

###### 7.1 <Scenario: TPP productive>

1. Scoped, monitored AIS access within valid certificates + consents.

###### 7.2 <Scenario: Misbehaving TPP>

1. Suspended pending review; evidence on record.

##### 8 Post-conditions

###### 8.1

TPP access exists only with valid certificates + customer consents.

###### 8.2

All AIS access logged immutably (CR-D-10.2-001).

##### 9 Special Requirements (FURPS+)

**Functional (F):** Registration, certificate validation, credential issuance, scoped AIS
enforcement, monitoring.

**Usability (U):** Developer-facing onboarding documentation with predictable error
semantics.

**Reliability (R):** Fail-closed on certificate problems; no consent, no data.

**Performance (P):** N/A — no attested API latency target.

**Supportability (S):** Gateway abstracts API versioning for TPP ecosystem change.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-18 (TPP onboarding + consent management; PSD2 SCA-compliant APIs; Head of Digital Channels ownership), SYS-25 (SOC tooling); Doc04 §2.2 (SYS-18 terminates in a DMZ with PSD2-compliant eIDAS-qualified certificates); FLOW-03 (TPPs third parties — inbound and outbound).
- **Constrained by:** UC-21 (consent source), PROC-24 (vendor risk assessment), PROC-49 (threat detection).
- **Rules / NFR:** CR-D-06.1-001 (third-party risk incl. TPPs), CR-D-06.3-001 (contractual obligations), CR-D-06.4-001 (concentration + exit), CR-D-10.1-001 (monitoring).
- **Threats addressed:** MUC-01-analogue (stolen TPP credentials — certificate binding + anomaly monitoring).
- **NIST anchors:** DE.CM-09, AU.A-06.

#### Use-Case: {UC-23} PIS Payment Initiation with SCA

##### 1 Brief Description

A TPP initiates a payment on the customer's behalf through the open banking gateway: consent
+ certificate validated, customer performs PSD2 SCA (redirect or decoupled challenge), and
only then does the payment commit to the payments core with the same fraud screening as
in-app transfers. It is triggered by a TPP payment-initiation request.

##### 2 Actor Brief Descriptions

###### 2.1 TPP (Third-Party Provider) — Primary Actor:

Submits the payment initiation; consumes status callbacks.

###### 2.2 SYS-18 (Open Banking / PSD2 API Gateway):

Validates consent + TPP credentials; orchestrates the SCA ceremony; idempotency.

###### 2.3 Customer (Retail):

Approves via SCA on the bound device (redirect to app or decoupled challenge).

###### 2.4 SYS-01 (CBS / payments core):

Executes the committed payment (same execution path as UC-17).

###### 2.5 SYS-11 (Fraud & AML Platform):

Screens the initiation in the real-time stream (FLOW-10 attested).

##### 3 Preconditions

- TPP onboarded (UC-22); consent covers PIS for the target account (UC-21).

##### 4 Basic Flow of Events

1. TPP submits the payment initiation at SYS-18 (consent + certificate validated).
2. Customer performs SCA (redirect into the app or decoupled challenge — attested SCA ceremony).
3. On SCA approval the payment commits to the payments core; SYS-11 screens the instruction (FLOW-10).
4. Status callbacks report the outcome to the TPP.
5. Evidence chain (consent, SCA, screening, commit) recorded on the payment record (CR-D-10.2-001).

> **Sequence diagram:** → Annex B §23 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: SCA abandoned or failed>

Trigger: step 2. Initiation cancelled; TPP may retry idempotently; nothing commits.

###### 5.2 <Alternate flow: Insufficient funds>

Trigger: step 3. Rejection with reason to the TPP; no partial commit.

###### 5.3 <Alternate flow: TPP suspended mid-flow>

Trigger: any step. Initiation aborted fail-closed.

##### 6 Subflows

###### 6.1 <Subflow: Decoupled SCA>

1. Approval pushed to the customer's bound device.
2. If the TPP session dies mid-flow, the result is reported to both sides — no orphaned
   commitments.

###### 6.2 <Subflow: Duplicate protection>

1. Idempotency key enforced at SYS-18; identical requests collapse.
2. Anti double-charge invariant: exactly-once commit semantics.

##### 7 Key Scenarios

###### 7.1 <Scenario: Payment initiated>

1. Single commit with the full evidence chain on record.

###### 7.2 <Scenario: Abandoned SCA>

1. No commit; retry is safe and idempotent.

##### 8 Post-conditions

###### 8.1

Payment executed only with SCA + valid consent + screening.

###### 8.2

Full evidence chain (consent, SCA, screening, commit) on the payment record.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Initiation, consent check, SCA, commit, callbacks, idempotency.

**Usability (U):** TPP-facing surface with predictable status codes/errors.

**Reliability (R):** Exactly-once commit; failures explicit.

**Performance (P):** N/A — no attested latency target.

**Supportability (S):** Initiation API versioned (PSD2 RTS evolution).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-18 (PSD2 SCA-compliant APIs; consent management), SYS-02 (transaction signing), SYS-11 (transaction monitoring; FLOW-10 real-time), SYS-01 (payments core).
- **Constrained by:** UC-21 (consent), UC-22 (TPP standing), UC-17 (execution path), CAP-10 (immutable logs).
- **Rules / NFR:** CR-D-03.2-001 (step-up/SCA discipline), CR-D-10.1-001 (monitoring), CR-D-10.2-001 (immutable records).
- **Threats addressed:** MUC-01-analogue (fraudulent initiations — SCA is the PSD2 control; behavioural signals assist), payment-fraud class (detection loop lands with UC-30).
- **NIST anchors:** PR.AA-01, DE.AE-02.

#### Use-Case: {UC-24} Payment Dispute & Chargeback

##### 1 Brief Description

The customer disputes a payment/card transaction; the case is managed in the CRM with
evidence, the scheme chargeback path is assessed via card management, and fraud suspicion
links the case to SYS-11 with protective card actions. It is triggered from a transaction
view (UC-16) or a contact-centre contact (SYS-20).

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Files the dispute; supplies evidence; receives the outcome.

###### 2.2 SYS-17 (CRM):

Case management with SLA tracking (complaint/case handling attested).

###### 2.3 SYS-05 (Card management):

Scheme chargeback path (card-scheme security-attestation scope — attested).

###### 2.4 SYS-20 (Contact centre):

Phone-channel intake with recorded calls (attested).

###### 2.5 SYS-11 (Fraud & AML Platform):

Fraud case linkage and detection input.

##### 3 Preconditions

- Transaction exists in the customer's history (UC-16).

##### 4 Basic Flow of Events

1. Customer selects the transaction and disputes it (in-app from UC-16, or via SYS-20 with a recorded call).
2. Case created in SYS-17 with evidence (receipts, statements, context).
3. Scheme chargeback path assessed via SYS-05 (scheme-scope rules).
4. Fraud suspicion → SYS-11 case linkage + protective card actions (UC-18).
5. Outcome communicated; case + evidence retained (CR-D-10.2-001, CR-D-05.2-001).

> **Sequence diagram:** → Annex B §24 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Dispute declined>

Trigger: step 3. Appeal path with additional evidence; second reviewer for the appeal.

###### 5.2 <Alternate flow: Fraud confirmed>

Trigger: step 4. Card blocked/reissued (UC-18); fraud case owned by SYS-11; dispute follows
the fraud outcome.

###### 5.3 <Alternate flow: Phone-channel dispute>

Trigger: step 1 via SYS-20. Recorded call linked to the same case (single thread).

##### 6 Subflows

###### 6.1 <Subflow: Evidence capture>

1. Structured evidence checklist per dispute category; attachments into the case.
2. Evidence immutably anchored (CR-D-10.2-001).

###### 6.2 <Subflow: Case linkage>

1. Dispute ↔ fraud case ↔ card state share identifiers — one investigative thread.
2. Linkage visible in the customer 360 record (SYS-17 attested).

##### 7 Key Scenarios

###### 7.1 <Scenario: Dispute resolved>

1. Outcome + evidence on record; customer informed.

###### 7.2 <Scenario: Fraud-linked dispute>

1. Card safe (blocked/reissued); single case thread end-to-end.

##### 8 Post-conditions

###### 8.1

Dispute case closed with outcome + evidence on record.

###### 8.2

Fraud-linked disputes leave the card in a safe state.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Dispute intake (channels), evidence, scheme-path assessment, outcome,
linkage.

**Usability (U):** Dispute entry from the transaction itself (UC-16 deep link).

**Reliability (R):** No dispute lost — every case carries an SLA state.

**Performance (P):** N/A — no attested SLA numbers for disputes.

**Supportability (S):** Case model mirrors scheme dispute categories.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-17 (CRM; complaint handling; customer 360), SYS-05 (card management; scheme-scope), SYS-20 (contact centre; call recording), SYS-11 (fraud platform).
- **Constrained by:** UC-16 (transaction context), UC-18 (card state), UC-32 (complaint interplay), CAP-10 (log evidence).
- **Rules / NFR:** CR-D-05.2-001 (retention), CR-D-10.2-001 (immutable records).
- **Threats addressed:** MUC-01-analogue (fraudulent disputes from a hijacked session — SCA session + history checks), first-party misuse (evidence discipline + second reviewer).
- **NIST anchors:** AU.A-06, DE.AE-02.

#### Use-Case: {UC-25} Payment Limits Management

##### 1 Brief Description

The customer views and adjusts payment limits per channel/class: reductions immediate,
increases behind risk-based step-up and thresholds, enforcement authoritative at the payments
core. It is triggered when the customer opens the limits screen or a decline surfaces the
limit context (UC-17).

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Views and adjusts own limits.

###### 2.2 SYS-02 (Mobile app channel):

Limits surface + step-up ceremony (attested risk-based step-up).

###### 2.3 SYS-01 (CBS / payments core):

Authoritative limits enforcement at execution time.

###### 2.4 SYS-11 (Fraud & AML Platform):

Risk signals inform thresholds and flag abusive change patterns.

##### 3 Preconditions

- SCA session (UC-15).

##### 4 Basic Flow of Events

1. Customer views current limits per channel/class.
2. Customer requests a change; step-up authentication required (attested).
3. Risk rules validate: reductions immediate; increases subject to risk thresholds.
4. Approved change becomes effective on the execution path (payments core authoritative).
5. Change signed and logged immutably (CR-D-10.2-001).

> **Sequence diagram:** → Annex B §25 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Increase above risk threshold>

Trigger: step 3. Human review path — out-of-threshold increases are never auto-approved.

###### 5.2 <Alternate flow: Risky session>

Trigger: step 2. Change blocked until the session identity is re-verified.

###### 5.3 <Alternate flow: Bulk/corporate-class limits>

Trigger: step 3. Out of retail scope; routed as guidance to the corporate journey family
(PKG-E).

##### 6 Subflows

###### 6.1 <Subflow: Threshold ladder>

1. Limit classes with distinct risk rules; increases ladder per class.
2. Ladder configuration owned by risk, enforced server-side.

###### 6.2 <Subflow: Change evidence>

1. Every change signed + logged (CR-D-10.2-001).
2. History feeds UC-24/UC-30 investigations.

##### 7 Key Scenarios

###### 7.1 <Scenario: Limits adjusted>

1. Approved state effective at the core.

###### 7.2 <Scenario: Blocked change>

1. Risk signals → denial + monitoring case.

##### 8 Post-conditions

###### 8.1

Limits reflect the approved state on the execution path.

###### 8.2

Limit-change history immutable (evidence grade).

##### 9 Special Requirements (FURPS+)

**Functional (F):** View/change limits, risk validation, enforcement sync.

**Usability (U):** Current limits shown next to every decline reason (UC-17).

**Reliability (R):** Enforcement authoritative at the core; client values are hints only.

**Performance (P):** N/A — no attested timing constraint.

**Supportability (S):** Limit classes config-driven (product evolution without redeploy).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-02 (risk-based step-up attested), SYS-11 (transaction monitoring), SYS-01 (CBS/payments core).
- **Constrained by:** UC-17 (execution path), UC-23 (PIS execution), UC-15 (SCA session).
- **Rules / NFR:** CR-D-03.2-001 (step-up), CR-D-10.1-001 (monitoring), CR-D-10.2-001 (immutable records).
- **Threats addressed:** MUC-01-analogue (attacker raising limits after takeover — step-up + risk thresholds are the control).
- **NIST anchors:** PR.AA-01, DE.AE-02.

### 4.6 PKG-E — Corporate & Treasury (4)

| UC ID | Title | Primary Actor | Prio |
|-------|-------|---------------|------|
| UC-26 | Corporate Onboarding with Delegated Users (SYS-21) | Customer (Corporate) — Corporate Administrator | CRITICAL |
| UC-27 | Cash Management Dashboard | Customer (Corporate) — Treasurer | HIGH |
| UC-28 | FX Deal Execution (SYS-08) | Customer (Corporate) — Treasurer | CRITICAL |
| UC-29 | Trade Finance Letter of Credit (SYS-07, UCP 600) | Customer (Corporate) — Applicant | HIGH |

#### Use-Case: {UC-26} Corporate Onboarding with Delegated Users (SYS-21)

##### 1 Brief Description

A corporate customer (SME + large corporate, attested SYS-21 scope) is onboarded on the
corporate portal: entity verification with sanctions screening of the company and its
beneficial owners, KYB documents in the vault, and a delegated-user model with
separation-of-duties validation. It is triggered when a corporate administrator starts
onboarding; the delegation graph it produces scopes every PKG-E journey.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Corporate) — Corporate Administrator — Primary Actor:

Provides entity data and beneficial-ownership structure; creates delegated users and roles.

###### 2.2 SYS-21 (Corporate Banking Portal):

Corporate self-service surface (cash management, FX deals — attested scope).

###### 2.3 SYS-11 (Fraud & AML Platform):

Screening of the entity and beneficial owners (UC-12 pattern at entity level).

###### 2.4 SYS-16 (Document vault):

KYB document filing (STORE-08 envelope).

###### 2.5 Head of Corporate Banking:

Owns SYS-21 (attested); owns the corporate onboarding policy.

##### 3 Preconditions

- Corporate entity data and registry extract available.
- Administrators identifiable with authority to represent the entity.

##### 4 Basic Flow of Events

1. Corporate administrator starts onboarding at SYS-21: company data, registry extract, beneficial-ownership structure.
2. Entity + beneficial owners screened by SYS-11 (sanctions/PEP — UC-12 pattern, entity level).
3. KYB documents filed in SYS-16 (UC-11 pattern: encryption, integrity hashing, retention metadata).
4. Administrator creates delegated users with role templates (least privilege); each user gets own credentials — no sharing.
5. Segregation-of-duties rules validated across the delegation graph before activation.

> **Sequence diagram:** → Annex B §26 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Beneficial-owner screening hit>

Trigger: step 2. Enhanced-due-diligence queue; onboarding blocked until resolved (UC-12
invariant at entity level).

###### 5.2 <Alternate flow: Delegated user leaves the company>

Trigger: post-activation lifecycle. Immediate deprovisioning (PROC-13 pattern) + session
revocation.

###### 5.3 <Alternate flow: Role request violates separation of duties>

Trigger: step 5. Denied with explanation; a dual-role exception requires a second approver
and is logged.

##### 6 Subflows

###### 6.1 <Subflow: Delegation model>

1. Role templates + separation-of-duties constraints (RBAC per BPR-D-03.1-001).
2. Delegation graph wired to quarterly access reviews (PROC-11, CR-D-03.3-001).

###### 6.2 <Subflow: Delegated-user lifecycle>

1. Joiner/mover/leaver handling for delegated users.
2. Leaver events trigger same-day deprovisioning with audit evidence.

##### 7 Key Scenarios

###### 7.1 <Scenario: Corporate onboarded>

1. Entity verified + delegation graph live on SYS-21; PKG-E journeys unlocked.

###### 7.2 <Scenario: Blocked on UBO hit>

1. EDD queue; no activation; financial-crime case on record.

##### 8 Post-conditions

###### 8.1

Corporate customer live on SYS-21 with verified entity + validated delegation graph.

###### 8.2

No delegated user shares credentials; SoD validated at provisioning time.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Entity onboarding, screening, KYB filing, delegation, SoD validation.

**Usability (U):** Bulk user import for large corporates.

**Reliability (R):** Screening gates entity activation (fail-closed).

**Performance (P):** N/A — no attested timing constraint.

**Supportability (S):** Role templates versioned; delegation graph exportable for audits
(CR-D-03.3-001 quarterly reviews).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-21 (Corporate Banking Portal; corporate customers SME + large corporate; cash management, FX deals; Head of Corporate Banking ownership), SYS-11 (sanctions screening), SYS-16 (KYC document vault).
- **Constrained by:** PROC-10 (identity provisioning), PROC-13 (deprovisioning), UC-12 (screening), PROC-11 (quarterly access review).
- **Rules / NFR:** BPR-D-03.1-001 (RBAC + separation of duties), CR-D-03.3-001 (least privilege + quarterly reviews), CR-D-05.2-001 (retention).
- **Threats addressed:** MUC-01-analogue (dormant delegated credentials — lifecycle + reviews are the control).
- **NIST anchors:** PR.AA-01, AU.A-06.

#### Use-Case: {UC-27} Cash Management Dashboard

##### 1 Brief Description

The corporate treasurer views aggregated balances and positions across accounts and entities
on the SYS-21 cash management surface (attested scope), with drill-down to account level and
scoped exports. It is triggered when the treasurer opens the dashboard; feeder data carries
explicit freshness markers.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Corporate) — Treasurer — Primary Actor:

Views aggregated positions; drills down; exports within own scope.

###### 2.2 SYS-21 (Corporate Banking Portal):

Cash management surface (attested); enforces delegation-scoped views.

###### 2.3 SYS-01 (CBS):

Account-level source data (position data flows to treasury/risk per FLOW-19 attested).

###### 2.4 SYS-08 (TMS):

Treasury positions context (FX, money market, fixed income; real-time risk positions —
attested).

##### 3 Preconditions

- Corporate onboarded with delegation graph (UC-26); SCA session per the PSD2 discipline
  (UC-15).

##### 4 Basic Flow of Events

1. Treasurer opens the dashboard; SYS-21 aggregates balances/positions across the delegated
   entity scope.
2. Dashboard renders per-source freshness markers (live core vs. aggregated feeds).
3. Treasurer drills down to account/transaction level within delegated rights.
4. Payment batches are view-only here; execution follows the UC-17/UC-23-class flows.
5. Export limited to the user's delegation scope; export logged (CR-D-10.2-001).

> **Sequence diagram:** → Annex B §27 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Feeder system lag>

Trigger: step 2. Staleness markers per source; no silent mixing of live and nightly data.

###### 5.2 <Alternate flow: Permission gap on an entity>

Trigger: step 3. Entity views filtered by delegation roles (UC-26); no cross-entity leakage.

###### 5.3 <Alternate flow: Export anomaly>

Trigger: step 5. Volume anomaly → monitoring flag + step-up before further exports.

##### 6 Subflows

###### 6.1 <Subflow: Aggregation freshness>

1. Per-source freshness markers mandatory in the widget model.
2. Stale aggregates degrade visibly, never silently.

###### 6.2 <Subflow: Scoped export>

1. Export bounded by the requester's delegation scope.
2. Every export logged with scope + volume (CR-D-10.2-001).

##### 7 Key Scenarios

###### 7.1 <Scenario: Dashboard rendered>

1. Aggregated, freshness-labelled, scope-filtered view.

###### 7.2 <Scenario: Scope-filtered view>

1. Delegation roles honoured; attempts outside scope denied + logged.

##### 8 Post-conditions

###### 8.1

Aggregated view displayed with explicit freshness.

###### 8.2

All views/exports within delegation scope + logged.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Aggregation, drill-down, scoped export.

**Usability (U):** Entity/account switcher; saved views.

**Reliability (R):** No silent stale data.

**Performance (P):** N/A — no attested latency target.

**Supportability (S):** Widget model extensible to new feeder systems without redesign.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-21 (cash management), SYS-08 (TMS; FX, money market, fixed income; real-time risk positions), SYS-01 (CBS; FLOW-19 position data to ALM/Risk/Treasury).
- **Constrained by:** UC-26 (delegation scope), UC-15 (SCA discipline), CAP-10 (log evidence).
- **Rules / NFR:** CR-D-01.2-001 (transport), CR-D-03.3-001 (least privilege), CR-D-10.2-001 (immutable records).
- **Threats addressed:** MUC-01-analogue (corporate session takeover → financial-structure exposure — SCA + scoped views).
- **NIST anchors:** PR.DS-02, PR.AA-01.

#### Use-Case: {UC-28} FX Deal Execution (SYS-08)

##### 1 Brief Description

The corporate treasurer requests and executes an FX deal: quote with a validity window from
the Treasury Management System (FX + real-time risk positions, attested), acceptance with SCA
inside the window, booking in TMS with position update and immutable deal record. It is
triggered when the treasurer requests a quote; stale quotes are never executable.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Corporate) — Treasurer — Primary Actor:

Requests quotes; accepts deals within delegated authority.

###### 2.2 SYS-21 (Corporate Banking Portal):

Corporate FX deal front-end (attested corporate FX deals on SYS-21).

###### 2.3 SYS-08 (Treasury Management System):

Quote generation, execution, booking, real-time risk positions (attested).

###### 2.4 Head of Treasury:

Owns SYS-08 (attested); owns dealer-limit policy and the human review path.

##### 3 Preconditions

- Delegated FX authority in the delegation graph (UC-26); SCA session (UC-15).

##### 4 Basic Flow of Events

1. Treasurer requests a quote (pair, amount, value date) at SYS-21.
2. SYS-08 returns the quote with an explicit validity window.
3. Treasurer accepts within the window; deal confirmed with SCA.
4. SYS-08 books the deal; risk positions update (real-time, attested).
5. Confirmations to the customer + treasury ops; deal record immutable (CR-D-10.2-001).

> **Sequence diagram:** → Annex B §28 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Quote expired>

Trigger: step 3. Re-quote required — execution on a stale price is impossible (server-side
window arbitration).

###### 5.2 <Alternate flow: Deal above dealer limit>

Trigger: step 3. Human dealer-review path; never auto-accepted.

###### 5.3 <Alternate flow: Settlement failure>

Trigger: step 4. Ops queue; position flagged; customer informed.

##### 6 Subflows

###### 6.1 <Subflow: Quote validity enforcement>

1. Accept/reject arbitrated server-side strictly within the window.
2. Expired quotes rejected with a re-quote action.

###### 6.2 <Subflow: Deal record integrity>

1. Deal + evidence chain append-only (CR-D-10.2-001).
2. Audit-grade record for disputes and regulatory review.

##### 7 Key Scenarios

###### 7.1 <Scenario: Deal executed>

1. Booked in TMS with positions updated and evidence complete.

###### 7.2 <Scenario: Out-of-limit deal>

1. Dealer review path; human decision recorded.

##### 8 Post-conditions

###### 8.1

Deal booked in TMS with full evidence chain.

###### 8.2

No execution outside the quote window or dealer limits.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Quote, accept, execution, booking, position update.

**Usability (U):** Quote state clearly time-boxed in the UI.

**Reliability (R):** Stale quotes never executable (fail-closed); dealer limits enforce the
human path.

**Performance (P):** N/A — no attested latency target.

**Supportability (S):** Instrument set extensible (SYS-08 scope attested: FX, money market,
fixed income — FX first).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-08 (Treasury Management System; FX; real-time risk positions; Head of Treasury ownership), SYS-21 (corporate FX deals).
- **Constrained by:** UC-15 (SCA), UC-26 (delegated authority), CAP-10 (log evidence).
- **Rules / NFR:** CR-D-03.2-001 (step-up on deal confirmation), CR-D-10.2-001 (immutable records), CR-D-10.1-001 (deal-flow monitoring).
- **Threats addressed:** MUC-01-analogue (fraudulent deals via hijacked corporate session — SCA + limits + immutable records).
- **NIST anchors:** PR.AA-01, AU.A-06.

#### Use-Case: {UC-29} Trade Finance Letter of Credit (SYS-07, UCP 600)

##### 1 Brief Description

The corporate applicant requests a letter of credit: bank review with sanctions screening of
the parties, issuance and advice to the beneficiary bank over the SWIFT correspondent channel
(FLOW-24, attested), document examination under ICC UCP 600 (attested SYS-07 compliance
basis), then payment or refusal. It is triggered by an LC issuance request at SYS-07.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Corporate) — Applicant — Primary Actor:

Submits the LC request, amendments and document-related instructions.

###### 2.2 SYS-07 (Trade Finance System):

LC lifecycle: issuance, guarantees, documentary collections; ICC UCP 600 compliance
(attested).

###### 2.3 SYS-06 (SWIFT):

Correspondent-bank messaging (logically/physically segregated per SWIFT CSP 2024 —
attested); FLOW-24 secure channel.

###### 2.4 SYS-11 (Fraud & AML Platform):

Sanctions screening of parties and documents (attested screening capability).

###### 2.5 Head of Trade Finance:

Owns SYS-07 (attested); owns issuance/examination policy.

##### 3 Preconditions

- Corporate authority for trade finance in the delegation graph (UC-26).
- Credit line/collateral arrangements in place per bank policy.

##### 4 Basic Flow of Events

1. Applicant submits the LC issuance request (terms, documents, beneficiary).
2. Bank review (credit line, collateral, terms) + sanctions screening of all parties (SYS-11).
3. LC issued and advised to the beneficiary bank via the SWIFT correspondent channel (FLOW-24: secure correspondent-banking PKI + HSM-bound signing).
4. Documents presented; examined per UCP 600 (attested compliance basis).
5. Payment or refusal per the examination outcome; the full chain is recorded (CR-D-10.2-001).

> **Sequence diagram:** → Annex B §29 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Document discrepancies>

Trigger: step 4. Refusal notice per UCP 600 discipline; applicant amendment cycle.

###### 5.2 <Alternate flow: Sanctions hit on a party>

Trigger: step 2. LC blocked; financial-crime queue (UC-12 pattern); no messages dispatched.

###### 5.3 <Alternate flow: Amendment request>

Trigger: any step before issuance closes. Amended terms re-issued with re-screening.

##### 6 Subflows

###### 6.1 <Subflow: SWIFT dispatch>

1. Correspondent messaging only over the attested secure channel (FLOW-24: PKI +
   HSM-bound signing).
2. No message leaves without completed screening (gate order).

###### 6.2 <Subflow: Document examination record>

1. Per-document findings anchored to the LC case (UCP 600 compliance evidence).
2. Case record immutable (CR-D-10.2-001).

##### 7 Key Scenarios

###### 7.1 <Scenario: LC issued and advised>

1. Screening clear; LC advised over the secure channel; chain on record.

###### 7.2 <Scenario: Discrepant documents>

1. Refusal per UCP 600; amendment path open; evidence anchored.

##### 8 Post-conditions

###### 8.1

LC lifecycle (issuance → examination → settlement/refusal) fully recorded.

###### 8.2

No message leaves without sanctions screening + the secure channel (FLOW-24 attested).

##### 9 Special Requirements (FURPS+)

**Functional (F):** LC issuance, screening, SWIFT advice, examination, settlement/refusal.

**Usability (U):** Applicant sees examination status per document set.

**Reliability (R):** UCP 600 compliance basis is authoritative (attested SYS-07 capability).

**Performance (P):** N/A — no attested SLA for LC processing.

**Supportability (S):** Product family extensible (guarantees, documentary collections —
attested SYS-07 scope).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-07 (Trade Finance System; letters of credit, guarantees, documentary collections; ICC UCP 600 compliance), SYS-06 (SWIFT segregated per SWIFT CSP 2024), SYS-11 (sanctions screening); FLOW-24 (LCs/guarantees to correspondent banks; secure correspondent-banking PKI + HSM-bound signing).
- **Constrained by:** UC-12 (screening), UC-26 (corporate authority), CAP-10 (log evidence).
- **Rules / NFR:** CR-D-06.3-001 (correspondent third-party obligations), CR-D-10.2-001 (immutable records), CR-D-05.2-001 (retention).
- **Threats addressed:** MUC-01-analogue (fraudulent LC instruction from a hijacked corporate session — SCA + delegated authority), documentary-fraud/sanctions-evasion class (SYS-11 screening gate before dispatch).
- **NIST anchors:** PR.DS-02, DE.AE-02.

### 4.7 PKG-F — Fraud & Customer Service (4)

| UC ID | Title | Primary Actor | Prio |
|-------|-------|---------------|------|
| UC-30 | In-App Fraud Alert Confirm/Deny (SYS-11) | Customer (Retail) | CRITICAL |
| UC-31 | Card Block via Contact Centre (SYS-20) | Customer (Retail) | CRITICAL |
| UC-32 | Complaint Filing & Handling (SYS-17) | Customer (Retail) | MEDIUM |
| UC-33 | Secure Messaging | Customer (Retail) | MEDIUM |

#### Use-Case: {UC-30} In-App Fraud Alert Confirm/Deny (SYS-11)

##### 1 Brief Description

When SYS-11 flags a suspicious transaction in the real-time stream (FLOW-10, attested), the
customer confirms or denies it in the app: deny blocks the transaction and triggers protective
actions + a fraud case; no response defaults to deny per risk rule (fail-safe default). It is
triggered by a SYS-11 detection on a customer journey.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Confirms (genuine) or denies (fraud) with one tap.

###### 2.2 SYS-11 (Fraud & AML Platform):

Detection + alerting (transaction monitoring, real-time stream — attested).

###### 2.3 SYS-02 (Mobile app channel):

Push/in-app alert surface over the SCA-bound device.

###### 2.4 SOC (SYS-25):

Escalation path for unresolved/complex fraud cases (SOC tooling attested).

##### 3 Preconditions

- Customer reachable on the bound device (UC-15); detection raised by SYS-11.

##### 4 Basic Flow of Events

1. SYS-11 flags a suspicious transaction in the real-time stream (FLOW-10 attested).
2. In-app alert with transaction context pushed to the customer.
3. Customer confirms (genuine) → transaction proceeds; confirmation is model feedback.
4. Customer denies (fraud) → transaction blocked + protective card/payment actions (UC-18) + fraud case opened.
5. No response within the risk-tiered window → default-deny (fail-safe default).

> **Sequence diagram:** → Annex B §30 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Timeout>

Trigger: step 5. Default-deny; documented reversal path if the customer later confirms.

###### 5.2 <Alternate flow: Repeated false alerts>

Trigger: step 3 pattern. Feedback into detection tuning + alert-fatigue review.

###### 5.3 <Alternate flow: Customer unreachable>

Trigger: no app contact. Contact-centre fallback (UC-31 pattern); default-deny applies in the
meantime.

##### 6 Subflows

###### 6.1 <Subflow: Default-deny window>

1. Risk-tiered timeout — higher-risk detections get shorter windows.
2. Timeout outcomes recorded as model-relevant evidence.

###### 6.2 <Subflow: Case creation>

1. Deny/timeout → fraud case with full journey evidence attached.
2. Case feeds detection-quality metrics (CR-D-10.1-001).

##### 7 Key Scenarios

###### 7.1 <Scenario: Fraud denied>

1. Transaction blocked; protective actions applied; case on record.

###### 7.2 <Scenario: Genuine confirmed>

1. Transaction released; confirmation feeds detection tuning.

##### 8 Post-conditions

###### 8.1

Every alert resolved (confirm/deny/timeout) with evidence.

###### 8.2

Denies leave payment/card in a safe state.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Alerting, confirm/deny, protective actions, case creation.

**Usability (U):** One-glance context; one-tap verdicts.

**Reliability (R):** Default-deny on timeout (fail-safe); never silent release.

**Performance (P):** N/A — no attested alert SLA.

**Supportability (S):** Alert taxonomy versioned (detection model evolution).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-11 (fraud detection; transaction monitoring; FLOW-10 real-time streaming), SYS-02 (app channel), SYS-25 (SOC tooling).
- **Constrained by:** UC-17 (screening path), UC-18 (protective actions), UC-23 (PIS loop), PROC-49 (threat detection plane).
- **Rules / NFR:** CR-D-10.1-001 (24/7 monitoring), BPR-D-04.1-001 (incident playbooks), CR-D-10.2-001 (case records).
- **Threats addressed:** MUC-01-analogue (attacker dismissing their own fraud alerts — default-deny window + out-of-band confirmation).
- **NIST anchors:** DE.AE-02, DE.CM-09.

#### Use-Case: {UC-31} Card Block via Contact Centre (SYS-20)

##### 1 Brief Description

A customer blocks a card through the contact centre: caller verification protocol over the
recorded-call platform (attested SYS-20), block executed on the card authorisation path
(SYS-05), asymmetric assurance — blocking is easy, unblocking is strict. It is triggered by an
inbound contact-centre call requesting card protection.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Requests the block by phone; completes the verification protocol.

###### 2.2 SYS-20 (Contact Centre Platform):

Agent surface + call recording (attested; documented third-party security attestation scope
for cardholder data).

###### 2.3 SYS-05 (Card management):

Executes the block on the authorisation path (scheme-scope attested).

###### 2.4 SYS-11 (Fraud & AML Platform):

Fraud case linkage when misuse is suspected.

##### 3 Preconditions

- Customer identifiable via the verification protocol (knowledge + possession signals).

##### 4 Basic Flow of Events

1. Customer calls the contact centre to block a card.
2. Agent runs the caller verification protocol (recorded call — attested).
3. Agent executes the block on the card authorisation path (SYS-05); when in doubt, the temporary block is applied first (protective, reversible).
4. Confirmation read back; recorded call retained per policy.
5. Fraud suspicion → SYS-11 case + reissue flow (UC-18 pattern).

> **Sequence diagram:** → Annex B §31 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Verification fails>

Trigger: step 2. Fail-safe: temporary block applied anyway (protective + reversible);
unblocking requires full re-verification.

###### 5.2 <Alternate flow: Social-engineering indicators>

Trigger: step 2. Agent fails closed; fraud review with the recorded call as evidence.

###### 5.3 <Alternate flow: Contact-centre unavailable>

Trigger: platform outage. IVR/app self-service block (UC-18) takes over.

##### 6 Subflows

###### 6.1 <Subflow: Caller verification>

1. Protocol steps with an asymmetric rule: block easy, unblock strict.
2. Verification outcomes recorded with the call reference.

###### 6.2 <Subflow: Recorded-call evidence>

1. Calls retained in the encrypted + tokenised cardholder-data scope (attested SYS-20).
2. Retention per policy (CR-D-05.2-001); evidence retrievable for fraud cases.

##### 7 Key Scenarios

###### 7.1 <Scenario: Card blocked via phone>

1. Card safe on the authorisation path; recorded evidence retained.

###### 7.2 <Scenario: Suspected social engineering>

1. Blocked + fraud review; recorded evidence attached.

##### 8 Post-conditions

###### 8.1

Card state safe (blocked) with recorded evidence.

###### 8.2

Unblocking requires strict verification (asymmetric assurance).

##### 9 Special Requirements (FURPS+)

**Functional (F):** Caller verification, block execution, case linkage, call recording.

**Usability (U):** Agent script with a verification checklist.

**Reliability (R):** Fail-safe: block first, verify fully later (reversible).

**Performance (P):** N/A — no attested handling-time target.

**Supportability (S):** Script/protocol versioned; recordings retained per CR-D-05.2-001.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-20 (contact centre; call recording; documented third-party security attestation scope for cardholder data; Head of Customer Service ownership), SYS-05 (card management), SYS-11 (fraud platform).
- **Constrained by:** UC-18 (block path), UC-30 (alert-loop fallback), PROC-23 (third-party attestation-scope audits).
- **Rules / NFR:** CR-D-01.1-001 (encrypted/tokenised recordings), CR-D-05.2-001 (retention), CR-D-06.3-001 (processor obligations).
- **Threats addressed:** MUC-01-analogue (social engineering of the phone channel — verification protocol + recording + asymmetric block/unblock).
- **NIST anchors:** PR.AA-01, AU.A-06.

#### Use-Case: {UC-32} Complaint Filing & Handling (SYS-17)

> Re-adjudicated from PROC-40 to the UC lane per rubric v1.8 §5B rule 6 (human decision 2026-09-05).

##### 1 Brief Description

The customer files a complaint (in-app or via the contact centre); the case is managed in the
CRM (complaint handling attested for SYS-17) with SLA tracking, linked evidence, an outcome
and — where needed — a regulatory escalation path. It is triggered by a customer complaint or
an agent raising one on the customer's behalf.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Files the complaint; supplies evidence; tracks status; receives the outcome.

###### 2.2 SYS-17 (CRM):

Case management (complaint handling attested; customer 360 context).

###### 2.3 SYS-20 (Contact centre):

Phone-channel intake with recorded calls (attested).

###### 2.4 Compliance Officer:

Owns the regulatory-escalation path (PROC-15/PROC-19 discipline).

##### 3 Preconditions

- Customer identifiable (UC-15 session or verified phone contact).

##### 4 Basic Flow of Events

1. Customer files the complaint (category, description, evidence) in-app or via SYS-20.
2. Case created in SYS-17 with category-based SLA tracking.
3. Investigation with access to linked records (decisions, disputes, journeys).
4. Outcome + response to the customer; evidence chain retained (CR-D-10.2-001).
5. Unresolved/out-of-SLA or regulatory-relevant cases escalate to the Compliance Officer.

> **Sequence diagram:** → Annex B §32 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Complaint contests an automated decision>

Trigger: step 3 (Art. 22 contest). Linkage to UC-05/UC-06 evidence + human re-review path.

###### 5.2 <Alternate flow: Complaint reveals a bias pattern>

Trigger: step 3. Pattern flagged to AI governance (bias/drift pipeline — MUC-C3-04
detection value of the channel).

###### 5.3 <Alternate flow: Regulator escalation>

Trigger: step 5. Case handed to Compliance with the full evidence bundle (PROC-19 reporting
discipline).

##### 6 Subflows

###### 6.1 <Subflow: Evidence linkage>

1. Complaint ↔ decision records ↔ dispute cases share identifiers — one thread.
2. Linked evidence immutably anchored (CR-D-10.2-001).

###### 6.2 <Subflow: SLA tracking>

1. Category-based SLAs; breach escalates automatically.
2. SLA metrics feed service governance.

##### 7 Key Scenarios

###### 7.1 <Scenario: Complaint resolved>

1. Outcome + full evidence chain on record; customer informed.

###### 7.2 <Scenario: Systemic-signal complaint>

1. Pattern escalated to the owning governance function (AI governance for model-related
   signals).

##### 8 Post-conditions

###### 8.1

Complaint case closed with outcome + evidence chain.

###### 8.2

Systemic patterns surfaced to their owning governance functions.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Intake (channels), case management, evidence linkage, outcome,
escalation.

**Usability (U):** In-app filing with attachments; status tracking.

**Reliability (R):** No silent case aging — SLA breaches escalate.

**Performance (P):** N/A — no attested SLA numbers.

**Supportability (S):** Category taxonomy versioned; complaint data retained per
CR-D-05.2-001.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-17 (managed CRM EU instance; customer 360 view; complaint handling), SYS-20 (contact centre channel; call recording).
- **Constrained by:** UC-05 (explanation evidence), UC-06 (human-decision records), UC-24 (dispute linkage), PROC-19 (regulator reporting path).
- **Rules / NFR:** CR-D-05.2-001 (retention), CR-D-10.2-001 (immutable records), BPR-D-12.3-001 (human oversight/escalation interplay for AI-related complaints).
- **Threats addressed:** MUC-C3-04 (discriminatory patterns surface first through complaints — the channel is wired to AI governance), MUC-C3-05 (complaint evidence is log-anchored and hard to spoof).
- **NIST anchors:** GV.PO-P1, DE.AE-02.

#### Use-Case: {UC-33} Secure Messaging

##### 1 Brief Description

The customer and the bank exchange secure in-app messages: authenticated-session-only
threads, agent responses from the CRM, sensitive attachments routed to the document vault
instead of raw chat storage, transcripts retained per class. It is triggered when the customer
opens a thread; the bank never asks for credentials or SCA factors in messages.

##### 2 Actor Brief Descriptions

###### 2.1 Customer (Retail) — Primary Actor:

Starts threads; sends messages/attachments; reads replies.

###### 2.2 SYS-02 (Mobile app channel):

SCA-protected messaging surface (authenticated sessions only).

###### 2.3 SYS-17 (CRM):

Agent inbox + customer 360 context (attested); transcript retention.

###### 2.4 SYS-16 (Document vault):

Filing of sensitive attachments (STORE-08 envelope).

##### 3 Preconditions

- SCA session (UC-15).

##### 4 Basic Flow of Events

1. Customer opens a secure thread (authenticated session only).
2. Messages exchanged with bank agents in SYS-17 (customer 360 context).
3. Attachments classified: non-sensitive shown inline; sensitive filed to SYS-16 with a reference (UC-11 pattern).
4. Thread transcript retained in the CRM record per retention class.
5. Channel rule surfaced in-thread: the bank never asks for credentials or SCA factors.

> **Sequence diagram:** → Annex B §33 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Sensitive attachment>

Trigger: step 3. Vault filing with retention metadata; only a reference stays in the thread.

###### 5.2 <Alternate flow: Erasure request on a thread>

Trigger: data-subject request. Crypto-shredding per CR-D-05.3-001 within documented BaFin
retention exemptions (CR-D-05.2-001).

###### 5.3 <Alternate flow: Agent-side mass-view anomaly>

Trigger: monitoring. Access anomaly → flag + review (least-privilege discipline).

##### 6 Subflows

###### 6.1 <Subflow: Attachment routing>

1. Classification decides inline vs. vault (BPR-D-05.1-001 classification discipline).
2. Vault-filed attachments inherit the STORE-08 envelope (encryption + integrity hashing).

###### 6.2 <Subflow: Transcript retention + erasure>

1. Retention class assigned per content classification.
2. Erasure executes via crypto-shredding within the documented constraints (CR-D-05.3-001).

##### 7 Key Scenarios

###### 7.1 <Scenario: Thread resolved>

1. Transcript on record, linked to the customer 360 view.

###### 7.2 <Scenario: Sensitive document exchanged>

1. Vault-anchored reference; nothing sensitive lingers in chat storage.

##### 8 Post-conditions

###### 8.1

Message history retained per class and linked to the customer 360 record.

###### 8.2

No credentials or SCA factors ever exchanged in-thread (channel rule).

##### 9 Special Requirements (FURPS+)

**Functional (F):** Threads, attachments, classification routing, retention/erasure.

**Usability (U):** Threading + search within the customer's own history.

**Reliability (R):** Authenticated-session-only access (no anonymous web mail).

**Performance (P):** N/A — no attested timing constraint.

**Supportability (S):** Message schema versioned; export feeds DSARs (UC-02/PROC-01).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc04 §1.1 SYS-02 (SCA app channel), SYS-17 (CRM EU instance; customer 360), SYS-16 (document vault); Doc04 §2 authentication-data line (crypto-shredding of credentials attested at closure).
- **Constrained by:** UC-15 (session), UC-11 (vault filing), UC-01 (erasure interplay), UC-02 (export).
- **Rules / NFR:** CR-D-01.1-001 (encryption at rest), CR-D-05.3-001 (erasure), BPR-D-05.1-001 (classification), CR-D-05.2-001 (retention).
- **Threats addressed:** MUC-01-analogue (hijacked session reading messages — SCA + step-up on sensitive threads), phishing class (in-thread channel-authenticity statement).
- **NIST anchors:** PR.DS-01, CT.DP-P2.

*MUC-C3 detail cards — massification additions (same structure as MUC-C3-01):*

#### MUC-C3-02 — Training-Data Poisoning of OmniScore

**Misactor:** Malicious insider (ML engineering) or compromised upstream data supplier.
**Threatens:** UC-04 (score), PROC-47 (secure training pipeline).
**Preconditions:** Write/influence access to the training data flowing into STORE-03
(OmniScore AI training data + explainability logs, EU cloud, immutable WORM for AI Act
Art. 12 documentation — attested).
**Attack Flow:**
1. Poisoned/mislabelled records injected into the training corpus (compromised ingestion or
   insider edit), shaping future scoring behaviour.
2. Trigger pattern planted (feature signature → favourable score band) activated after
   deployment.
**Impact:** Systematically skewed scores at scale; bias/drift signals masked as market
change; systematic credit mispricing and AI Act data-governance breach.
**Mitigated by:** SYS-03 bias + drift monitoring pipeline (out-of-family behaviour flags —
PROC-50), PROC-47 secure AI training pipeline (provenance + integrity gates on training data),
CAP-08 model tampering detection, PROC-44 AI model/training-data access control, STORE-03
immutable WORM documentation (attested).
**NIST anchors:** DE.AE-02, MEASURE-2.7.

#### MUC-C3-03 — Model Inversion / Membership Inference

**Misactor:** External adversary/researcher with query access, or malicious insider with
training-artefact access.
**Threatens:** UC-04 (score + confidence), UC-05 (explanation package), training-data
confidentiality.
**Preconditions:** Query access to scoring or explanations (direct or via a TPP-style
integration), or read access to training artefacts.
**Attack Flow:**
1. Confidence/reason-code probing reconstructs feature contributions and approximates the
   model (model extraction/inversion).
2. Membership inference: determine whether a specific person's record was in the training
   set (GDPR-scale privacy harm).
**Impact:** IP loss (model theft); privacy breach on training data (membership); regulatory
exposure (GDPR Art. 5/32, AI Act).
**Mitigated by:** PROC-44 access control (inference API + training data), PROC-41 field-level
encryption of training datasets, GDPR-compliant granularity of reason codes (UC-04/UC-05 —
minimum-necessary explanation surface), PROC-37 adversarial robustness testing, PROC-11
quarterly access reviews.
**NIST anchors:** PR.DS-01, DE.CM-09.

### 4.8 PKG-DS — Privacy & Data-subject UCs (2)

| UC ID | Title | Primary Actor | Prio |
|-------|-------|---------------|------|
| UC-01 | Data Protection Officer Executes Data Erasure Request | Data Protection Officer | CRITICAL |
| UC-02 | Data Subject Requests Data Export | Data Subject | HIGH |

> **v3.0 (UC SEPARATION):** UC-33/UC-34 were the only genuine use cases among the former §6
> compliance cards (PKG-D-05 stubs). Per human decision 2026-09-05 (rubric v1.8 §5B rule 6) they
> stay in the UC lane and are grouped in this dedicated package, elevated from summary stubs to
> fully-dressed form. Their rules (CR-D-05.3-001/BPR-D-05.3-001 erasure; CR-D-05.4-001/
> BPR-D-05.4-001 export) are also indexed in §3 (PKG-D-05) with lane cards in
> `Doc32_Process_Capability_Cards.md` (PROC-20/21/23 discipline, CAP-10 counterpart).

#### Use-Case: {UC-01} Data Protection Officer Executes Data Erasure Request

##### 1 Brief Description

The Data Protection Officer executes cryptographic sharding-based erasure within 30 days of a
GDPR erasure request or retention expiry, covering PII, AI training data contributions and model
inference records (CR-D-05.3-001). It is triggered when a data-subject erasure request arrives
(GDPR Art. 17(1), identity verified) or when the tiered retention schedule expires an item. The
erasure resolves tension T-002: PII keys are destroyed while the DORA-mandated immutable log
structure remains verifiable (CAP-10).

##### 2 Actor Brief Descriptions

###### 2.1 Data Protection Officer — Primary Actor:

Owns the erasure decision and execution: verifies the request, determines the erasure scope and
completes the erasure record.

###### 2.2 OmniBank platform (system):

Executes the cryptographic-sharding erasure (per-subject key destruction), backup/replication
propagation, third-party notification scheduling and the completion log.

###### 2.3 IT Operations Manager (Secondary):

Supports the infrastructure and backup side of the erasure propagation.

###### 2.4 Data Subject:

Requester (GDPR Art. 17(1)); receives the completion confirmation.

##### 3 Preconditions

- Erasure request registered and requester identity verified (or retention expiry reached on the
  policy path).
- In-scope data locatable: PII, AI training data contributions and model inference records.

##### 4 Basic Flow of Events

1. Erasure request received and logged (GDPR Art. 17(1)); identity verified before any erasure action.
2. DPO determines the erasure scope: PII, AI training data contributions and model inference records (CR-D-05.3-001).
3. DPO screens the scope for legal-hold/retention conflicts (tiered retention schedule — PROC-21); non-conflicting items proceed.
4. OmniBank platform executes the cryptographic-sharding erasure: per-subject material keys destroyed, ciphertext rendered unrecoverable (CR-D-05.3-001); cryptographic erase per the media sanitization standard (BPR-D-05.3-001).
5. Erasure propagated to copies, replications and backups (GDPR Art. 17(2)); IT Operations Manager supports the backup side.
6. Third parties (processors, AI model providers) informed of the erasure request within 72 hours (GDPR Art. 17(2)); compliance verified per the third-party audit discipline (PROC-23).
7. Erasure completion record written to the sanitization audit trail (BPR-D-05.3-001); data subject receives confirmation.

> **Sequence diagram:** → Annex B §1 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Identity verification failure>

Trigger: step 1/2. Request suspended — no erasure is executed on an unverified identity; the
requester is asked to complete verification and the 30-day clock resumes on success.

###### 5.2 <Alternate flow: Legal-hold/retention conflict>

Trigger: step 3. Statutory retention obligations (tiered retention policy — PROC-21) prevail for
the conflicting data only; the non-conflicting scope is erased; the conflict and its grounds are
documented in the erasure record and communicated to the data subject.

###### 5.3 <Alternate flow: Data held by third parties>

Trigger: step 6. Third-party notification issued (72-hour SLA per rule); erasure compliance at the
third party verified within 60 days of request (PROC-23 audit discipline).

##### 6 Subflows

###### 6.1 <Subflow: Cryptographic sharding erasure>

1. Per-subject material keys located in designated cryptographic custody.
2. Keys destroyed — the ciphertext becomes unrecoverable while the hash-chained log structure
   remains verifiable (T-002 resolution; CAP-10 discipline).

###### 6.2 <Subflow: Erasure record>

1. Completion record captures scope, method (cryptographic erase), timestamps and third-party
   notifications (BPR-D-05.3-001 audit trail).

##### 7 Key Scenarios

###### 7.1 <Scenario: Erasure completed>

1. Erasure record complete within 30 days; PII unrecoverable; log structure intact; third parties
   notified and verified.

###### 7.2 <Scenario: Partial erasure (conflict)>

1. Non-conflicting scope erased; conflicting data retained per the statutory schedule; refusal
   grounds documented and communicated.

##### 8 Post-conditions

###### 8.1

Personal data in scope cryptographically erased (keys destroyed) within 30 days of the request.

###### 8.2

Erasure completion record on the audit trail; third-party notifications dispatched and verified.

##### 9 Special Requirements (FURPS+)

**Functional (F):** Request intake with identity verification, scope determination, key-destruction
erasure, backup/replication propagation, third-party notification, completion record.

**Usability (U):** Erasure confirmation returned to the data subject on completion.

**Reliability (R):** Fail-closed — completion only when in-scope stores, copies and backups are
covered; T-002 invariant holds (log integrity preserved while PII is unrecoverable).

**Performance (P):** Erasure completed within 30 days; third parties notified within 72 hours (per
rule CR-D-05.3-001).

**Supportability (S):** Works across PII, AI training data contributions and inference records;
interfaces with the tiered retention schedule (PROC-21) and third-party audits (PROC-23).

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc19 CR-D-05.3-001 verbatim ("Enable cryptographic sharding-based erasure within 30 days of request or retention expiry. Applies to PII, AI training data contributions, and model inference records. Resolves tension T-002"); BPR-D-05.3-001 (media sanitization standard — Clear, Purge, Destroy; cryptographic erase; sanitization documented for audit trail). Elevated from the Doc22 v2.3 §6 stub per UC SEPARATION (rubric v1.8 §5B rule 6, human decision 2026-09-05).
- **Constrained by:** PROC-21 (tiered retention schedule), PROC-23 (third-party erasure audits), CAP-10 (immutable audit logs — T-002 counterpart).
- **Rules / NFR:** CR-D-05.3-001, BPR-D-05.3-001.
- **Objectives:** AG-D-05.3-001.
- **Regulatory citations:** GDPR Art. 17(1) (right to erasure); GDPR Art. 17(2) (informing other controllers/processors — propagation to copies, replications and backups).
- **Tension resolution:** T-002 — cryptographic sharding enables DORA immutable log retention while satisfying GDPR erasure. PII keys destroyed; log structure preserved.
- **NIST anchors:** PR.DS-10 (CSF 2.0); CT.DM-P4, CT.DM-P5 (Privacy Framework) — per Doc20/NIST_ANCHORS.

#### Use-Case: {UC-02} Data Subject Requests Data Export

##### 1 Brief Description

The data subject requests an export of their personal data in machine-readable format. The export
covers personal data, AI model decisions, training data lineage and credit scoring factors
(CR-D-05.4-001). It is triggered when the data subject submits an export request; the package is
delivered within 30 days (per rule; GDPR Art. 20 data portability, with the Art. 15(3) copy right
covering items outside Art. 20's portability scope).

##### 2 Actor Brief Descriptions

###### 2.1 Data Subject — Primary Actor:

Submits the export request; receives the machine-readable package.

###### 2.2 OmniBank platform (system):

Assembles the export from live records, AI decision records, training-data lineage and scoring
factors; generates standardized formats (JSON/CSV per BPR-D-05.4-001).

###### 2.3 Data Protection Officer (Secondary):

Verifies the request and approves the response package; ensures third-party data exclusion and
scope correctness.

##### 3 Preconditions

- Requester identity verified.
- The subject's records locatable: personal data, AI model decisions, training data lineage and
  credit scoring factors.

##### 4 Basic Flow of Events

1. Data subject submits the export request (GDPR Art. 15(3) copy / Art. 20 data portability); request logged with timestamp.
2. DPO verifies identity and determines the export scope: personal data, AI model decisions, training data lineage and credit scoring factors (CR-D-05.4-001).
3. OmniBank platform assembles the export in standardized machine-readable formats (JSON/CSV, per BPR-D-05.4-001); third-party personal data is excluded from the package.
4. Export delivered to the data subject within 30 days (per rule CR-D-05.4-001; GDPR Art. 20).
5. Request/dispatch logged against the data-subject record.

> **Sequence diagram:** → Annex B §2 (B_Sequence_Diagrams.md)

##### 5 Alternative Flows

###### 5.1 <Alternate flow: Identity verification failure>

Trigger: step 2. Request suspended — no export is issued on an unverified identity; verification
must complete before the package is assembled.

###### 5.2 <Alternate flow: Third-party data in scope>

Trigger: step 3. Records containing other data subjects' personal data are excluded or redacted;
the remainder is delivered and the exclusions are noted to the requester.

###### 5.3 <Alternate flow: Items outside portability scope>

Trigger: step 4. Where items fall outside Art. 20's portability scope (e.g. derived scores or
lineage not provided by the data subject), they are supplied under the Art. 15(3) copy right in
the same machine-readable format.

##### 6 Subflows

###### 6.1 <Subflow: Scoring-factor package>

1. Credit scoring factors drawn from the generated explanation/reason-code records (CR-D-05.4-001
   scope: "Include AI model decisions, training data lineage, and credit scoring factors").
2. Format matches the machine-readable requirement (JSON/CSV — BPR-D-05.4-001).

###### 6.2 <Subflow: Third-party exclusion>

1. Records scanned for third-party personal data before assembly.
2. Excluded/redacted items recorded with the dispatch log.

##### 7 Key Scenarios

###### 7.1 <Scenario: Export delivered>

1. Machine-readable package delivered within 30 days; dispatch logged against the data-subject
   record.

###### 7.2 <Scenario: Third-party exclusion>

1. Package delivered with third-party data excluded; exclusions noted to the requester.

##### 8 Post-conditions

###### 8.1

Export delivered in standardized machine-readable format within 30 days.

###### 8.2

Dispatch logged against the data-subject record (auditable).

##### 9 Special Requirements (FURPS+)

**Functional (F):** Export assembly across personal data, AI model decisions, training data lineage
and credit scoring factors; JSON/CSV standardized formats; dispatch logging.

**Usability (U):** Single request surface for the data subject; machine-readable output.

**Reliability (R):** Complete scope per CR-D-05.4-001 — no silent omissions; third-party exclusion
enforced before delivery.

**Performance (P):** Export completed within 30 days (per rule CR-D-05.4-001).

**Supportability (S):** Export model stays stable for audits and data-subject requests; feeds the
UC-05 explanation package and the PROC-23 third-party audit discipline.

##### 10 Security & Compliance Annex (AEGIS)

- **Provenance:** [ATTESTED] Doc19 CR-D-05.4-001 verbatim ("Enable data export in machine-readable formats within regulatory SLAs (GDPR: 30 days). Include AI model decisions, training data lineage, and credit scoring factors."); BPR-D-05.4-001 (automated data lifecycle management; GDPR-compliant portability with standardized export formats JSON, CSV). Elevated from the Doc22 v2.3 §6 stub per UC SEPARATION (rubric v1.8 §5B rule 6, human decision 2026-09-05).
- **Constrained by:** UC-03 (consent/declaration data), UC-05 (scoring-factor explanation records), PROC-22 (training-data lineage documentation), PROC-23 (third-party data audits).
- **Rules / NFR:** CR-D-05.4-001, BPR-D-05.4-001.
- **Objectives:** AG-D-05.4-001.
- **Regulatory citations:** GDPR Art. 15(3) (copy of personal data undergoing processing); GDPR Art. 20 (data portability — structured, commonly used, machine-readable format).
- **NIST anchors:** ALT-ANCHOR — no direct CSF 2.0 subcategory for portability (Doc20 §D-05.4); CT.DM-P1, CT.DM-P6 (Privacy Framework); ISO 27002:2022 A.5.34 (per Doc20 ALT-ANCHOR note).

### 4.9 MUC-C3 inventory (OmniScore AI threat model)

| MUC ID | Threat | Target UCs | Mitigations |
|--------|--------|------------|-------------|
| MUC-C3-01 | Application data crafted to game OmniScore | UC-03, UC-04, UC-06 | Out-of-distribution flags → human path (UC-04 ext. 5.3); SYS-11 fraud screening (UC-03 step 4); bureau cross-checks (UC-06); bias/drift pipeline |
| MUC-C3-02 | Training-data poisoning of OmniScore | UC-04, PROC-47 | SYS-03 bias+drift pipeline (PROC-50); PROC-47 secure training pipeline; CAP-08 tampering detection; PROC-44 access control; STORE-03 WORM |
| MUC-C3-03 | Model inversion / membership inference | UC-04, UC-05 | PROC-44 access control; PROC-41 field-level encryption; reason-code granularity (UC-04/05); PROC-37 adversarial testing; PROC-11 access reviews |
| MUC-C3-04 | Discriminatory bias exploitation / harm | UC-04, UC-05, UC-32 | SYS-03 bias monitoring; PROC-50 drift monitoring; BPR-D-12.1-001 bias testing; human path (UC-06); complaint channel wired to governance (UC-32) |
| MUC-C3-05 | Explainability gaming (spoofed reason codes) | UC-04, UC-05, UC-06 | In-runtime reason codes log-anchored to model version; CAP-08; UC-06 fail-closed on incomplete context; CR-D-10.2-001 immutable records; PROC-11 |
| MUC-C3-06 | Model & training-data exfiltration (IP/customer-data theft) | UC-04, PROC-47, PROC-22 | PROC-44 access control + PROC-11 reviews; PROC-41 encryption (STORE-03/STORE-10 HSM-bound CMK — attested); export-anomaly monitoring (PROC-49); egress minimisation (CR-D-05.1-001) |

> **Note (MUC-C3-06):** no canonical definition of MUC-C3-06 exists elsewhere in the corpus
> (the MUC-C3 family was introduced in this document's §6B pilot); the row above records the
> sixth threat class implied by the 01–05 set (model/data exfiltration). If the ambiguity
> register later defines MUC-C3-06 differently, this row must be reconciled (P7 — human
> arbiter).

## 5. USE CASE METRICS SUMMARY

### 5.1 Distribution by Priority

| Priority | Count | Percentage | Example UCs |
|----------|-------|------------|-------------|
| CRITICAL | 17 | 51.5% | UC-03, UC-04, UC-06, UC-07 |
| HIGH | 11 | 33.3% | UC-05, UC-08, UC-13, UC-14 |
| MEDIUM | 5 | 15.2% | UC-19, UC-20, UC-25, UC-32 |
| **TOTAL** | **33** | **100%** | — |

### 5.2 Distribution by Package

| Package | UCs | CRITICAL | HIGH | MEDIUM | LOW |
|--------|-----|----------|------|--------|-----|
| PKG-C: Lending & OmniScore | 6 | 4 | 2 | 0 | 0 |
| PKG-A: Onboarding & KYC | 6 | 4 | 2 | 0 | 0 |
| PKG-B: Digital Banking Core | 6 | 2 | 2 | 2 | 0 |
| PKG-D: Payments & Open Banking | 5 | 2 | 2 | 1 | 0 |
| PKG-E: Corporate & Treasury | 4 | 2 | 2 | 0 | 0 |
| PKG-F: Fraud & Customer Service | 4 | 2 | 0 | 2 | 0 |
| PKG-DS: Privacy & Data-subject | 2 | 1 | 1 | 0 | 0 |
| **TOTAL** | **33** | **17** | **11** | **5** | **0** |

> The former "Distribution by Domain" (D-01..D-10) described the compliance-card population
> removed in v3.0; that population is now indexed in §3 (Compliance Domain Index) with lane
> cards in `Doc32_Process_Capability_Cards.md`.

### 5.3 Rules Coverage Matrix

| Domain | Compliance Rules | Best Practice Rules | Realised by |
|--------|------------------|---------------------|-------------|
| D-01 | 4 | 1 | Doc32 lane cards (§3.2) |
| D-02 | 5 | 6 | Doc32 lane cards (§3.2) |
| D-03 | 4 | 4 | Doc32 lane cards (§3.2) |
| D-04 | 5 | 5 | Doc32 lane cards (§3.2) |
| D-05 | 4 | 3 | Doc32 lane cards (§3.2) + UC-01/UC-02 (PKG-DS §4.8) |
| D-06 | 4 | 5 | Doc32 lane cards (§3.2) |
| D-07 | 4 | 4 | Doc32 lane cards (§3.2) |
| D-08 | 3 | 4 | Doc32 lane cards (§3.2) |
| D-09 | 4 | 4 | Doc32 lane cards (§3.2) |
| D-10 | 4 | 5 | Doc32 lane cards (§3.2) |

> Counts are distinct rule ids carried by the former §6 package cards (v2.3 ground truth);
> BPR-D-12.x (AI-specific) are counted in their host domains. Per-rule realisation lives in the
> §3.2 index and in the Doc32 cards' **Realises** field. Total distinct mentions across domains:
> 41 CR / 41 BPR (rules shared across domains counted once per domain).

---

## 6. TRACEABILITY CHAIN

### 6.1 Regulation → Rule → UC Mapping

> v3.0: rule lists unchanged; UC counts recomputed over the 33 catalog use cases
> (§4 card annexes + PKG-DS). Compliance-rule realisation is indexed in §3 / Doc32.

| Regulation | Rules | UCs |
|------------|-------|-----|
GDPR12 (CR-D-01.1, CR-D-03.3, CR-D-04.2, CR-D-04.3, CR-D-04.4, CR-D-05.1, CR-D-05.2, CR-D-05.3, CR-D-05.4, CR-D-06.1, CR-D-06.3, CR-D-08.1, CR-D-08.2, CR-D-09.1, CR-D-09.2, CR-D-09.4, CR-D-10.3) | 25 |
CRA18 (CR-D-01.1, CR-D-01.2, CR-D-01.3, CR-D-01.4, CR-D-02.1, CR-D-02.2, CR-D-02.3, CR-D-02.4, CR-D-03.1, CR-D-03.2, CR-D-03.4, CR-D-04.1, CR-D-04.2, CR-D-04.3, CR-D-05.1, CR-D-05.3, CR-D-06.2, CR-D-07.1, CR-D-10.1, CR-D-10.2, CR-D-10.3) | 29 |
NIS 224 (CR-D-01.1, CR-D-02.1, CR-D-02.2, CR-D-03.1, CR-D-03.2, CR-D-03.3, CR-D-04.1, CR-D-04.2, CR-D-04.3, CR-D-04.4, CR-D-06.1, CR-D-06.3, CR-D-06.4, CR-D-07.2, CR-D-07.3, CR-D-07.4, CR-D-08.1, CR-D-08.2, CR-D-08.3, CR-D-09.1, CR-D-09.2, CR-D-09.3, CR-D-10.1, CR-D-10.2, CR-D-10.3) | 31 |
DORA29 (CR-D-01.1, CR-D-01.2, CR-D-01.3, CR-D-02.1, CR-D-02.2, CR-D-02.4, CR-D-03.1, CR-D-03.2, CR-D-03.3, CR-D-04.1, CR-D-04.2, CR-D-04.3, CR-D-04.4, CR-D-06.1, CR-D-06.3, CR-D-06.4, CR-D-07.2, CR-D-07.3, CR-D-07.4, CR-D-08.3, CR-D-09.1, CR-D-09.2, CR-D-09.3, CR-D-10.1, CR-D-10.2, CR-D-10.3) | 31 |
AI Act13 (CR-D-01.1, CR-D-01.4, CR-D-02.1, CR-D-02.4, CR-D-03.1, CR-D-04.3, CR-D-05.1, CR-D-05.2, CR-D-07.1, CR-D-08.2, CR-D-09.1, CR-D-09.2, CR-D-10.1, CR-D-10.2, CR-D-10.3) | 31 |

---

## 7. STRATEGIC TENSION TRACEABILITY

| Tension ID | Type | Resolved By | UCs |
|------------|------|-------------|-----|
| T-001 | Temporal Conflict (24h notification) | PROC-15: Universal Incident Notification | PROC-15 |
| T-002 | Requirement Conflict (Erasure vs Logs) | UC-01, CAP-10: Cryptographic Sharding | UC-01, CAP-10 |
| T-003 | Frequency Mismatch (Assessment overlap) | PROC-34: IPSARA Unified Assessment | PROC-34 |
| T-004 | Intensity Gap (Secure-by-default) | PROC-28: Secure-by-Design | PROC-28 |

---

## 8. NEXT STEPS

1. **Define Use Case Relationships (Doc 13a)** — Establish «include» and «extend» relationships between UCs
2. **Define Use Case Variability (Doc 13b)** — Document specialization and alternative scenarios per regulation
3. **Compliance Analysis Gate** — Verify all rules mapped to UCs
4. **Derive Functional Requirements** — Extract FRs from UCs for Doc 23
5. **Derive Non-Functional Requirements** — Extract NFRs from UCs for Doc 24

---

## 9. VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 3.1 | 2026-09-05 | Executor (RENUMBER F1) | Compact renumbering per rubric v1.10 §5B rule 7: lane ids flattened to UC-01..33 / PROC-39..50 (two-phase word-boundary rename; registry `00_METHODOLOGY/validation/RENUMBER_REGISTRY_2026-09-05.md`); Annex A 8 PlantUML sources updated + 8 SVGs re-rendered; Annex B §1..§33 headings re-anchored (order preserved — mapping is ascending); §4 actor table Drives ranges updated. Historical provenance (Formerly / version rows ≤3.0) keeps the ids it named | High |
| 3.0 | 2026-09-05 | Executor (UC SEPARATION F1) | Lane-pure catalog per rubric v1.8 §5B rule 6: §6 replaced by the Compliance Domain Index (§3); 15 non-genuine UC cards re-laned to PROC-41..52/CAP-08..10 (full cards in Doc32); PROC-39/40 re-adjudicated to UC-66/92; PKG-DS added with UC-33/34 fully-dressed (§4.8); numbering, metadata and metrics corrected (33 UCs / 7 packages); Annex A/B pointers regenerated | High |
| 2.1 | 2026-09-04 | PORT-PARITY-2 Executor (Phase 3 product-first pilot) | Added §6B Product Functional Use Cases (PKG-C Lending & OmniScore, 6 fully-dressed UCs UC-63..68) + MUC-C3-01/04/05 cards; compliance UCs PROC-01..62 (§6) preserved verbatim | High |
| 2.2 | 2026-09-04 | PORT-PARITY-2 Executor (Phase 3 massification C3) | Added §6B.2–§6B.6 product packages PKG-A/B/D/E/F (25 fully-dressed UCs UC-69..93) + MUC-C3-02/03 detail cards + §6B.7 MUC-C3 inventory table; §6B.0 actor Drives updated; compliance UCs PROC-01..62 (§6) preserved verbatim | High |
| 1.0 | 2026-04-28 | Compliance Lead | Initial creation — 62 UCs across 10 packages derived from 63 rules |

---

## 10. DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Compliance Lead | [TBD] | | |
| CISO | [TBD] | | |
| Data Protection Officer | [TBD] | | |
| Chief Risk Officer | [TBD] | | |
| AI Governance Lead | [TBD] | | |

---

**Next Step:** Proceed to 13a_Use_Case_Relationships.md to define UC relationships.
---

## Lane Naming (2026-09-05)

v2.2 → v2.3: non-technology UCs re-laned to PROC-*/CAP-* per human decision 2026-09-05 (rubric REALIZATION_CLASS_RUBRIC v1.3 §5B; registry `00_METHODOLOGY/validation/LANE_NAMING_CENSUS_v0.md`). Applied via `scripts/rename_lane_ids.py`.

v3.0 → v3.1 (RENUMBER, 2026-09-05, rubric v1.10 §5B rule 7): lane ids renumbered flat 1..N — UC-33/34/63..93 → UC-01..33, PROC-41..52 → PROC-39..50 (PROC-01..38 and CAP-01..10 untouched); two-phase word-boundary rename; registry `00_METHODOLOGY/validation/RENUMBER_REGISTRY_2026-09-05.md`.

v2.3 → v3.0 (UC SEPARATION, 2026-09-05): 15 remaining non-genuine §6 `UC-*` cards re-laned in a single word-boundary pass — UC-02→PROC-41, UC-03→PROC-42, UC-06→PROC-43, UC-15→PROC-44, UC-17→PROC-45, UC-21→PROC-46, UC-22→PROC-47, UC-44→PROC-48, UC-46→PROC-49, UC-47→PROC-50, UC-57→PROC-51, UC-61→PROC-52, UC-08→CAP-08, UC-26→CAP-09, UC-58→CAP-10; PROC-39→UC-66 and PROC-40→UC-92 re-adjudicated back to the UC lane (rubric v1.8 §5B rule 6; numbers 39/40 retired, PROC numbering continues at 41). The PROC/CAP summary stubs no longer live in this catalog: §6 became the Compliance Domain Index (§3) and all full lane cards live in `Doc32_Process_Capability_Cards.md`.

---

## Lane Cards cross-reference

All PROCESS and CAPABILITY lane cards (50 PROC + 10 CAP, one card + one Mermaid diagram each, with an articulation table binding every card to this catalog and to the downstream documents) live in `Doc32_Process_Capability_Cards.md` (per `REALIZATION_CLASS_RUBRIC.md` v1.8 §5B rule 6 / §5C.3). This catalog holds use cases only: PKG-A..F (§4.2–§4.7) and PKG-DS (§4.8); the compliance domains PKG-D-01..D-10 are indexed in §3.
