---
document_id: AEGIS-P3-ANNEX-A
title: Use Case Diagrams Annex (Case_03)
phase: 3
version: 1.0
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
---

# Annex A — Use Case Diagrams

> **Render note:** diagrams use `useCaseDiagram` — requires Mermaid ≥ v11.6.
> Syntax follows the known-good reference: Case_02 `Doc21_Use_Cases_Catalog.md` §5.1.

**Source of truth:** `03_PHASE3_DECOMPOSITION/Doc22_Use_Cases_Catalog.md` §6B (product functional use cases UC-63+, PKG-A..F). Actors are taken from each fully-dressed card (primary actor per §6B.x table; supporting actors from "Actor Brief Descriptions" §2.x). Include (`..>`) / extend (`.>`) edges are drawn **only** where a card's `**Constrained by:**` field or extensions explicitly indicate a dependency between two use cases **of the same package**; cross-package constraints (e.g. UC-73 → UC-63, UC-90 → UC-77/78/83) are intentionally omitted here and remain traceable in Doc22/Doc23. Note: PROC-39 and PROC-40 are pre-existing compliance use cases (§6) reused inside the PKG-C/PKG-F flows per Doc22 §6B.1 and §6B.6 tables; they are shown as package members.

---

## §1 — System-wide

Six product packages and the top actors from Doc22 §6B.0.

```mermaid
useCaseDiagram
    actor "Customer (Retail)" as CUST
    actor "Customer (Corporate)" as CORP
    actor "TPP (Third-Party Provider)" as TPP
    actor "Underwriter" as UND
    actor "SYS-03 (OmniScore AI Platform)" as SYS03
    actor "SYS-11 (Fraud & AML Platform)" as SYS11

    package "PKG-A — Onboarding & KYC" {
        usecase "PKG-A\nOnboarding & KYC" as PKGA
    }
    package "PKG-B — Digital Banking Core" {
        usecase "PKG-B\nDigital Banking Core" as PKGB
    }
    package "PKG-C — Lending & OmniScore" {
        usecase "PKG-C\nLending & OmniScore" as PKGC
    }
    package "PKG-D — Payments & Open Banking" {
        usecase "PKG-D\nPayments & Open Banking" as PKGD
    }
    package "PKG-E — Corporate & Treasury" {
        usecase "PKG-E\nCorporate & Treasury" as PKGE
    }
    package "PKG-F — Fraud & Customer Service" {
        usecase "PKG-F\nFraud & Customer Service" as PKGF
    }

    CUST --> PKGA
    CUST --> PKGB
    CUST --> PKGC
    CUST --> PKGD
    CUST --> PKGF
    CORP --> PKGE
    TPP --> PKGD
    UND --> PKGC
    SYS03 --> PKGC
    SYS11 --> PKGA
    SYS11 --> PKGD
    SYS11 --> PKGF
```

---

## §2 — PKG-A: Onboarding & KYC (UC-69..74)

Actors from cards UC-69..74. Includes: UC-69 brief description enumerates UC-70/71/72/73 as in-line steps; UC-74 `**Constrained by:**` UC-71 (vault filing).

```mermaid
useCaseDiagram
    actor "Customer (Retail)" as CUST
    actor "SYS-02 (Mobile app channel)" as SYS02
    actor "SYS-11 (Fraud & AML Platform)" as SYS11
    actor "SYS-16 (Document vault)" as SYS16
    actor "Sanctions screening provider" as SSP

    package "PKG-A — Onboarding & KYC" {
        usecase "UC-69\nOpen Account via\nMobile App" as UC69
        usecase "UC-70\neIDAS Identity Verification" as UC70
        usecase "UC-71\nKYC Document Upload &\nVault Filing (SYS-16)" as UC71
        usecase "UC-72\nSanctions & PEP Screening" as UC72
        usecase "UC-73\nOmniScore Consent &\nData-Use Acknowledgement" as UC73
        usecase "UC-74\nTax Residency Self-Certification\n(FATCA/CRS)" as UC74
    }

    CUST --> UC69
    CUST --> UC70
    CUST --> UC71
    CUST --> UC73
    CUST --> UC74
    SYS11 --> UC72
    SYS02 --> UC69
    SYS16 --> UC71
    SYS16 --> UC74
    SSP --> UC72

    UC69 ..> UC70 : include
    UC69 ..> UC71 : include
    UC69 ..> UC72 : include
    UC69 ..> UC73 : include
    UC74 ..> UC71 : include
```

---

## §3 — PKG-B: Digital Banking Core (UC-75..80)

Actors from cards UC-75..80. Includes per `**Constrained by:**`: UC-76→UC-75, UC-77→UC-75, UC-78→UC-75/UC-77, UC-79→UC-77, UC-80→UC-75 (cross-package UC-85/UC-90/UC-34 constraints omitted).

```mermaid
useCaseDiagram
    actor "Customer (Retail)" as CUST
    actor "SYS-02 (Mobile app channel)" as SYS02
    actor "SYS-01 (CBS / payments core)" as SYS01
    actor "SYS-05 (Card management)" as SYS05
    actor "SYS-13 (Customer Data Warehouse)" as SYS13
    actor "SYS-16 (Document vault)" as SYS16

    package "PKG-B — Digital Banking Core" {
        usecase "UC-75\nLogin with PSD2 SCA" as UC75
        usecase "UC-76\nView Balances & Transactions" as UC76
        usecase "UC-77\nSEPA Transfer\n(incl. Instant)" as UC77
        usecase "UC-78\nManage Cards\n(block/limits)" as UC78
        usecase "UC-79\nStanding Orders" as UC79
        usecase "UC-80\nStatements & Export" as UC80
    }

    CUST --> UC75
    CUST --> UC76
    CUST --> UC77
    CUST --> UC78
    CUST --> UC79
    CUST --> UC80
    SYS02 --> UC75
    SYS01 --> UC77
    SYS01 --> UC79
    SYS05 --> UC78
    SYS13 --> UC76
    SYS13 --> UC80
    SYS16 --> UC80

    UC76 ..> UC75 : include
    UC77 ..> UC75 : include
    UC78 ..> UC75 : include
    UC78 ..> UC77 : include
    UC79 ..> UC77 : include
    UC80 ..> UC75 : include
```

---

## §4 — PKG-C: Lending & OmniScore (UC-63..68, PROC-39)

Actors from cards UC-63/64/65/67/68/PROC-39. Edges: UC-65 `**Constrained by:**` UC-63 (consent record) → include; PROC-39 is the manual/borderline path of UC-63 per UC-63 brief description → extend.

```mermaid
useCaseDiagram
    actor "Customer (Retail)" as CUST
    actor "SYS-02 (Mobile app channel)" as SYS02
    actor "SYS-03 (OmniScore AI Platform)" as SYS03
    actor "SYS-14 (Loan Origination)" as SYS14
    actor "Underwriter (Consumer Lending)" as UND

    package "PKG-C — Lending & OmniScore" {
        usecase "UC-63\nApply for Consumer Credit" as UC63
        usecase "UC-64\nOmniScore Computes\nCredit Score" as UC64
        usecase "UC-65\nCustomer Receives\nScore Explanation" as UC65
        usecase "PROC-39\nUnderwriter Reviews\nBorderline Application" as PROC39
        usecase "UC-67\nCustomer Accepts Offer\n& Contract Signed" as UC67
        usecase "UC-68\nCustomer Manages Repayment\n& Arrears View" as UC68
    }

    CUST --> UC63
    CUST --> UC65
    CUST --> UC67
    CUST --> UC68
    SYS03 --> UC64
    SYS14 --> UC64
    SYS02 --> UC63
    UND --> PROC39

    UC65 ..> UC63 : include
    PROC39 .> UC63 : extend
```

---

## §5 — PKG-D: Payments & Open Banking (UC-81..85)

Actors from cards UC-81..85. Includes per `**Constrained by:**`: UC-81↔UC-82 (mutual constraint recorded on both cards), UC-83→UC-81/UC-82, UC-85→UC-83 (cross-package UC-75/UC-77/UC-58 omitted).

```mermaid
useCaseDiagram
    actor "Customer (Retail)" as CUST
    actor "TPP (Third-Party Provider)" as TPP
    actor "SYS-18 (Open Banking / PSD2 API Gateway)" as SYS18
    actor "SYS-01 (CBS / payments core)" as SYS01

    package "PKG-D — Payments & Open Banking" {
        usecase "UC-81\nPSD2 Consent Grant/Revoke" as UC81
        usecase "UC-82\nTPP Onboarding &\nAIS Access (SYS-18)" as UC82
        usecase "UC-83\nPIS Payment Initiation with SCA" as UC83
        usecase "UC-84\nPayment Dispute & Chargeback" as UC84
        usecase "UC-85\nPayment Limits Management" as UC85
    }

    CUST --> UC81
    CUST --> UC84
    CUST --> UC85
    TPP --> UC82
    TPP --> UC83
    SYS18 --> UC82
    SYS18 --> UC83
    SYS01 --> UC83

    UC81 ..> UC82 : include
    UC82 ..> UC81 : include
    UC83 ..> UC81 : include
    UC83 ..> UC82 : include
    UC85 ..> UC83 : include
```

---

## §6 — PKG-E: Corporate & Treasury (UC-86..89)

Actors from cards UC-86..89 (Customer (Corporate) personas per card). Includes per `**Constrained by:**`: UC-87/UC-88/UC-89 → UC-86 (delegation scope / delegated authority / corporate authority; cross-package UC-72/UC-75 omitted).

```mermaid
useCaseDiagram
    actor "Customer (Corporate) — Corporate Administrator" as CADM
    actor "Customer (Corporate) — Treasurer" as TRE
    actor "Customer (Corporate) — Applicant" as APP
    actor "SYS-21 (Corporate Banking Portal)" as SYS21
    actor "SYS-08 (Treasury Management System)" as SYS08
    actor "SYS-07 (Trade Finance System)" as SYS07
    actor "SYS-06 (SWIFT)" as SYS06

    package "PKG-E — Corporate & Treasury" {
        usecase "UC-86\nCorporate Onboarding with\nDelegated Users (SYS-21)" as UC86
        usecase "UC-87\nCash Management Dashboard" as UC87
        usecase "UC-88\nFX Deal Execution (SYS-08)" as UC88
        usecase "UC-89\nTrade Finance Letter of Credit\n(SYS-07, UCP 600)" as UC89
    }

    CADM --> UC86
    TRE --> UC87
    TRE --> UC88
    APP --> UC89
    SYS21 --> UC86
    SYS21 --> UC87
    SYS21 --> UC88
    SYS08 --> UC87
    SYS08 --> UC88
    SYS07 --> UC89
    SYS06 --> UC89

    UC87 ..> UC86 : include
    UC88 ..> UC86 : include
    UC89 ..> UC86 : include
```

---

## §7 — PKG-F: Fraud & Customer Service (UC-90, UC-91, PROC-40, UC-93)

Actors from cards UC-90/91/PROC-40/UC-93. Extend: UC-91 `**Constrained by:**` UC-90 (alert-loop fallback) — contact-centre block as fallback of the in-app alert loop. No same-package includes (all other constraints are cross-package).

```mermaid
useCaseDiagram
    actor "Customer (Retail)" as CUST
    actor "SYS-11 (Fraud & AML Platform)" as SYS11
    actor "SYS-20 (Contact Centre Platform)" as SYS20
    actor "SYS-17 (CRM)" as SYS17
    actor "SOC (SYS-25)" as SOC25

    package "PKG-F — Fraud & Customer Service" {
        usecase "UC-90\nIn-App Fraud Alert\nConfirm/Deny (SYS-11)" as UC90
        usecase "UC-91\nCard Block via\nContact Centre (SYS-20)" as UC91
        usecase "PROC-40\nComplaint Filing &\nHandling (SYS-17)" as PROC40
        usecase "UC-93\nSecure Messaging" as UC93
    }

    CUST --> UC90
    CUST --> UC91
    CUST --> PROC40
    CUST --> UC93
    SYS11 --> UC90
    SYS20 --> UC91
    SYS20 --> PROC40
    SYS17 --> PROC40
    SYS17 --> UC93
    SOC25 --> UC90

    UC91 .> UC90 : extend
```

---

**Traceability:** UC IDs ↔ Doc22 §6B fully-dressed cards; actor names ↔ §6B.0 product actor table and per-card §2 "Actor Brief Descriptions"; include/extend edges ↔ per-card §10 `**Constrained by:**` fields (same-package subset only). Cross-package and compliance-plane dependencies (UC-17, UC-22, UC-33, UC-34, UC-57, UC-58, UC-61, UC-06, UC-08, UC-02/03, PROC-01..24, CAP-02) are documented in Doc22 §6B §10 and Doc23_Use_Case_Relationships.md.
