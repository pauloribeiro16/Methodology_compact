---
document_id: AEGIS-P3-ANNEX-B
title: Sequence Diagrams Annex (Case_03)
phase: 3
version: 2.0
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
---

# Annex B — Sequence Diagrams

**Case:** OmniBank Financial Systems
**Phase:** 3 — Decomposition
**Status:** ACTIVE — 33 sequences, one per Doc22 catalog use case, ordered by id (rubric v1.8 §5C.5).

> **v2.0 (UC SEPARATION, 2026-09-05):** sections re-ordered by id (UC-33, UC-34, then UC-63..UC-93);
> UC-66 and UC-92 restored in place (re-adjudicated from PROC-39/40, rubric v1.8 §5B rule 6);
> §1/§2 sequences added for the PKG-DS use cases (UC-33/UC-34, fully-dressed in Doc22 §4.8);
> empty "B.1 Critical Path Sequences" placeholder removed.
>
> **v2.1 (RENUMBER, 2026-09-05, rubric v1.10 §5B rule 7):** ids renumbered UC-01..33; §N order preserved (old→new mapping is ascending), Doc22 pointers remain 1:1.

> **2026-09-10:** Catalogue cards now embed derived copies of these diagrams inline; this annex remains the editable source (rubric §5C.5 v1.11).

## §1 — Use-Case — {UC-01} Data Protection Officer Executes Data Erasure Request

```mermaid
sequenceDiagram
    participant DS as Data Subject
    participant DPO as DPO (erasure owner)
    participant PLAT as OmniBank platform (sharding erasure)
    participant ITO as IT Operations (backups)
    participant TP as Third parties (processors / AI providers)
    DS->>DPO: Erasure request (GDPR Art. 17(1)), identity verified
    DPO->>PLAT: Determine scope: PII, AI training data, inference records (CR-D-05.3-001)
    DPO->>DPO: Legal-hold / retention conflict screen (PROC-21 schedule)
    PLAT->>PLAT: Per-subject key destruction — ciphertext unrecoverable (BPR-D-05.3-001)
    PLAT->>ITO: Propagate erasure to copies / backups (GDPR Art. 17(2))
    PLAT->>TP: Notification ≤ 72h (GDPR Art. 17(2)), verification ≤ 60d (PROC-23)
    PLAT-->>DPO: Completion record on sanitization audit trail
    DPO-->>DS: Erasure confirmation (≤ 30 days)
```

## §2 — Use-Case — {UC-02} Data Subject Requests Data Export

```mermaid
sequenceDiagram
    participant DS as Data Subject
    participant DPO as DPO (scope approval)
    participant PLAT as OmniBank platform (export assembly)
    DS->>DPO: Export request (GDPR Art. 15(3) / Art. 20), identity verified
    DPO->>PLAT: Scope: personal data, AI decisions, training-data lineage, scoring factors (CR-D-05.4-001)
    PLAT->>PLAT: Assemble standardized JSON/CSV, exclude third-party personal data
    PLAT-->>DS: Machine-readable export ≤ 30 days (GDPR Art. 20)
    PLAT->>PLAT: Request/dispatch logged against data-subject record
```

## §3 — Use-Case — {UC-03} Apply for Consumer Credit


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (App, SCA)
    participant LO as SYS-14 (Loan Origination)
    participant F as SYS-11 (Fraud/AML)
    C->>APP: Select product/amount/term, SECCI, consent + declarations
    APP->>LO: Submit application record
    LO->>F: Fraud screening
    LO->>LO: Invoke OmniScore decisioning (UC-04)
```

## §4 — Use-Case — {UC-04} OmniScore Computes Credit Score


```mermaid
sequenceDiagram
    participant LO as SYS-14 (Loan Origination)
    participant AI as SYS-03 (OmniScore)
    participant UW as Underwriter (UC-06)
    LO->>AI: Decisioning request (application features)
    AI->>AI: Run approved model version, score + confidence band
    AI->>AI: Generate reason codes, write decision-context record
    AI-->>LO: Score + reasons + model version id
    LO->>UW: Borderline band -> queue human review
```

## §5 — Use-Case — {UC-05} Customer Receives Score Explanation


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (App)
    participant AI as SYS-03 (Explainability layer)
    C->>APP: Open decision screen
    APP->>AI: Request outcome view / explanation package
    AI-->>APP: Principal reason codes / package (CR-D-05.4-001 format)
    APP-->>C: Plain-language outcome, dispatch logged
```

## §6 — Use-Case — {UC-06} Underwriter Reviews Borderline Application


```mermaid
sequenceDiagram
    participant UW as Underwriter
    participant LO as SYS-14 (Work item)
    participant GOV as Head of AI Governance
    LO->>UW: Work item (application, score, reasons, model version)
    UW->>UW: Independent review, overrides only with justification
    UW->>LO: Decision (approve/decline) + reason code
    LO-->>GOV: Override-vs-score delta for metrics
```

## §7 — Use-Case — {UC-07} Customer Accepts Offer & Contract Signed


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant LO as SYS-14 (Origination)
    participant KV as SYS-16 (KYC vault)
    participant AML as SYS-11 (AML)
    C->>LO: Accept offer, sign (PSD2 SCA, hardware-backed)
    LO->>KV: File contract (10-year retention)
    LO->>AML: New credit exposure tagged
    LO-->>C: Disbursement initiated
```

## §8 — Use-Case — {UC-08} Customer Manages Repayment & Arrears View


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (App)
    participant SVC as SYS-15 (Loan Servicing)
    C->>APP: Open credit management
    APP->>SVC: Fetch schedule / arrears state
    SVC-->>APP: Current figures
    C->>SVC: Early repayment / cure action (via app)
```

## §9 — Use-Case — {UC-09} Open Account via Mobile App


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (App, SCA)
    participant CRM as SYS-17 (Customer 360)
    participant F as SYS-11 (KYC/AML)
    C->>APP: Start onboarding, data + product selection
    APP->>CRM: Create onboarding/customer record
    APP->>F: Identity + document + screening steps (UC-10..12)
    F-->>CRM: Screening result anchored to record
    CRM-->>C: Account activated, SCA credentials issued
```

## §10 — Use-Case — {UC-10} eIDAS Identity Verification


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (App, SCA)
    participant GW as SYS-18 (eIDAS certs, DMZ)
    participant F as SYS-11 (KYC file)
    C->>APP: Document + confirmation evidence
    APP->>GW: Trust exchange (eIDAS-qualified certificates)
    GW-->>APP: Validated trust chain
    APP->>F: Verification result (immutable KYC record)
```

## §11 — Use-Case — {UC-11} KYC Document Upload & Vault Filing (SYS-16, 10y retention)


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (App, SCA)
    participant DMS as SYS-16 (Vault, STORE-08)
    participant F as SYS-11 (Screening)
    C->>APP: Capture/upload document set
    APP->>DMS: Upload (encrypted, integrity-hashed)
    DMS-->>APP: Filing receipt + retention metadata (10y)
    DMS->>F: Document set for screening (FLOW-11)
```

## §12 — Use-Case — {UC-12} Sanctions & PEP Screening


```mermaid
sequenceDiagram
    participant OB as Onboarding (UC-09)
    participant F as SYS-11 (Fraud/AML)
    participant P as Screening provider
    participant FC as Head of Financial Crime
    OB->>F: Screening trigger (customer data)
    F->>P: List screening query
    P-->>F: Match candidates
    F->>FC: Alert + evidence (queue) / clear result
    FC->>F: Disposition (block + STR/CTR or release)
```

## §13 — Use-Case — {UC-13} OmniScore Consent & Data-Use Acknowledgement


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (App)
    participant DPO as DPO (Consent store)
    participant LO as SYS-14 (Decisioning)
    APP->>C: OmniScore data-use notice (versioned)
    C->>APP: Acknowledge / decline
    APP->>DPO: Consent record (timestamp + notice version)
    LO->>DPO: Precondition check before UC-04
```

## §14 — Use-Case — {UC-14} Tax Residency Self-Certification (FATCA/CRS)


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (App)
    participant DMS as SYS-16 (Vault)
    participant CO as Head of Compliance Ops
    APP->>C: Self-certification form
    C->>APP: Declare residency + TINs, sign
    APP->>DMS: File certification with KYC record
    CO->>DMS: Re-certification tasks on change events
```

## §15 — Use-Case — {UC-15} Login with PSD2 SCA


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (SCA, hardware-backed)
    participant ID as SYS-24 (Identity service)
    participant F as SYS-11 (Behavioural signals)
    C->>APP: Credentials + SCA factor
    APP->>ID: Session validation
    ID-->>APP: Valid, risk-based step-up decision
    APP->>F: Behavioural signal check
    APP-->>C: SCA session established (device-bound)
```

## §16 — Use-Case — {UC-16} View Balances & Transactions


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (App)
    participant CBS as SYS-01 (CBS)
    participant CDW as SYS-13 (Warehouse)
    C->>APP: Open accounts overview
    APP->>CBS: Live balances (FLOW-02 path)
    APP->>CDW: Deep history (FLOW-13, nightly)
    APP-->>C: View with freshness markers
```

## §17 — Use-Case — {UC-17} SEPA Transfer (incl. Instant)


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (Transaction signing)
    participant F as SYS-11 (Real-time screening)
    participant CBS as SYS-01 (Payments core)
    C->>APP: Transfer + SCA signing
    APP->>F: Instruction into transaction stream
    F-->>CBS: Clear → execute (instant or standard)
    CBS-->>C: Confirmation + history entry
```

## §18 — Use-Case — {UC-18} Manage Cards (block/limits)


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (App, step-up)
    participant CARDS as SYS-05 (Card mgmt, scheme scope)
    participant F as SYS-11 (Fraud linkage)
    C->>APP: Block / limits change
    APP->>CARDS: State change (block-before-confirm)
    CARDS-->>APP: Authorisation path updated
    APP->>F: State-change evidence for fraud cases
```

## §19 — Use-Case — {UC-19} Standing Orders


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (Signing)
    participant CBS as SYS-01 (Payments core)
    participant F as SYS-11 (Screening)
    C->>APP: Create standing order + sign
    APP->>CBS: Store mandate
    CBS->>F: Execute on due date → screening
    CBS-->>C: Execution confirmation / failure notice
```

## §20 — Use-Case — {UC-20} Statements & Export


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (App, SCA)
    participant CDW as SYS-13 (Warehouse)
    participant DMS as SYS-16 (Vault)
    C->>APP: Statement/export request
    APP->>CDW: Generate (FLOW-13 history / live core)
    CDW-->>APP: Document + CR-D-05.4-001 export format
    APP->>DMS: Periodic statement archived, download logged
```

## §21 — Use-Case — {UC-21} PSD2 Consent Grant/Revoke


```mermaid
sequenceDiagram
    participant TPP as TPP (Third Party)
    participant GW as SYS-18 (Consent mgmt, eIDAS certs)
    participant APP as SYS-02 (SCA)
    participant C as Customer (Retail)
    TPP->>GW: Consent request (scope, duration)
    GW->>APP: SCA ceremony + consent screen
    C->>APP: Grant (possibly narrowed scope)
    APP->>GW: Consent recorded, token to TPP
    C->>GW: Revoke anytime → access cut
```

## §22 — Use-Case — {UC-22} TPP Onboarding & AIS Access (SYS-18)


```mermaid
sequenceDiagram
    participant TPP as TPP (Third Party)
    participant GW as SYS-18 (Gateway, eIDAS certs)
    participant DC as Head of Digital Channels
    participant SOC as SOC (SYS-25)
    TPP->>GW: Registration + certificate
    GW->>DC: Validation result for approval
    DC->>GW: Approve → API credentials
    TPP->>GW: AIS calls (consent-scoped)
    GW->>SOC: Access telemetry + anomalies
```

## §23 — Use-Case — {UC-23} PIS Payment Initiation with SCA


```mermaid
sequenceDiagram
    participant TPP as TPP (Third Party)
    participant GW as SYS-18 (Gateway)
    participant APP as SYS-02 (SCA)
    participant CBS as SYS-01 (Payments core)
    TPP->>GW: Payment initiation (consent + cert validated)
    GW->>APP: SCA challenge (redirect/decoupled)
    APP-->>GW: SCA approval
    GW->>CBS: Commit (screened via FLOW-10)
    GW-->>TPP: Status callback
```

## §24 — Use-Case — {UC-24} Payment Dispute & Chargeback


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant CRM as SYS-17 (Case)
    participant CARDS as SYS-05 (Scheme path)
    participant F as SYS-11 (Fraud linkage)
    C->>CRM: Dispute + evidence (app or SYS-20)
    CRM->>CARDS: Chargeback assessment
    CARDS-->>CRM: Scheme outcome
    CRM->>F: Fraud linkage if suspected
    CRM-->>C: Outcome communicated
```

## §25 — Use-Case — {UC-25} Payment Limits Management


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (Step-up)
    participant CBS as SYS-01 (Enforcement)
    participant F as SYS-11 (Risk rules)
    C->>APP: Limit change request
    APP->>F: Risk validation (thresholds)
    F-->>APP: Approve / human-review path
    APP->>CBS: Effective change + immutable log
```

## §26 — Use-Case — {UC-26} Corporate Onboarding with Delegated Users (SYS-21)


```mermaid
sequenceDiagram
    participant CA as Corp Administrator
    participant PORTAL as SYS-21 (Corporate portal)
    participant F as SYS-11 (Entity/UBO screening)
    participant CO as Head of Corporate Banking
    CA->>PORTAL: Entity data + UBO structure
    PORTAL->>F: Screening (entity + UBOs)
    F-->>PORTAL: Clear / hit
    PORTAL->>CO: KYB complete → activation approval
    PORTAL->>CA: Delegated users + roles provisioned (SoD validated)
```

## §27 — Use-Case — {UC-27} Cash Management Dashboard


```mermaid
sequenceDiagram
    participant T as Treasurer (Corporate)
    participant PORTAL as SYS-21 (Cash mgmt)
    participant CBS as SYS-01 (Accounts)
    participant TMS as SYS-08 (Positions)
    T->>PORTAL: Open dashboard
    PORTAL->>CBS: Account balances
    PORTAL->>TMS: Position context
    PORTAL-->>T: Aggregated view (freshness-marked, scope-filtered)
```

## §28 — Use-Case — {UC-28} FX Deal Execution (SYS-08)


```mermaid
sequenceDiagram
    participant T as Treasurer (Corporate)
    participant PORTAL as SYS-21 (Corporate FX)
    participant TMS as SYS-08 (TMS)
    participant TO as Treasury Ops
    T->>PORTAL: Quote request (pair, amount, date)
    PORTAL->>TMS: Quote (validity window)
    T->>TMS: Accept in window (SCA)
    TMS->>TO: Booked deal + position update
```

## §29 — Use-Case — {UC-29} Trade Finance Letter of Credit (SYS-07, UCP 600)


```mermaid
sequenceDiagram
    participant AP as Applicant (Corporate)
    participant TF as SYS-07 (Trade Finance, UCP 600)
    participant SW as SYS-06 (SWIFT correspondents)
    participant BB as Beneficiary bank
    AP->>TF: LC issuance request
    TF->>TF: Review + sanctions screening (SYS-11)
    TF->>SW: Issue + advise (FLOW-24 secure channel)
    BB->>TF: Present documents
    TF->>AP: Examination outcome (pay / refuse per UCP 600)
```

## §30 — Use-Case — {UC-30} In-App Fraud Alert Confirm/Deny (SYS-11)


```mermaid
sequenceDiagram
    participant F as SYS-11 (Detection)
    participant APP as SYS-02 (Alert surface)
    participant C as Customer (Retail)
    participant SOC as SOC (SYS-25)
    F->>APP: Suspicious transaction flagged
    APP->>C: Fraud alert (context)
    C->>APP: Confirm / Deny
    APP->>F: Release / block + case
    F->>SOC: Escalation if unresolved
```

## §31 — Use-Case — {UC-31} Card Block via Contact Centre (SYS-20)


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant CC as SYS-20 (Agent, recorded call)
    participant CARDS as SYS-05 (Card mgmt)
    participant F as SYS-11 (Fraud case)
    C->>CC: Block request (phone)
    CC->>CC: Verification protocol
    CC->>CARDS: Block (temporary-first when in doubt)
    CARDS-->>CC: Authorisation path updated
    CC->>F: Case linkage if misuse suspected
```

## §32 — Use-Case — {UC-32} Complaint Filing & Handling (SYS-17)


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant CRM as SYS-17 (Case mgmt)
    participant CC as SYS-20 (Phone intake)
    participant CO as Compliance Officer
    C->>CRM: Complaint + evidence (app)
    C->>CC: Alternative intake (recorded call)
    CC->>CRM: Case created
    CRM->>CRM: Investigation + SLA tracking
    CRM->>CO: Escalation (regulatory path) if needed
    CRM-->>C: Outcome + response
```

## §33 — Use-Case — {UC-33} Secure Messaging


```mermaid
sequenceDiagram
    participant C as Customer (Retail)
    participant APP as SYS-02 (App, SCA)
    participant CRM as SYS-17 (Agent inbox)
    participant DMS as SYS-16 (Vault)
    C->>APP: Message (+ attachment)
    APP->>CRM: Thread message
    APP->>DMS: Sensitive attachment → vault reference
    CRM-->>C: Agent reply + transcript retained
```
