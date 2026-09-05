---
document_id: AEGIS-P3-ANNEX-A
title: Use Case Diagrams Annex (Case_03)
phase: 3
version: 1.2
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
---

# Annex A — Use Case Diagrams

> **Render note:** use-case diagrams are native **PlantUML** — each diagram is a
> `plantuml` source block (source of truth, editable) plus a committed SVG
> (`svg/*.svg`, rendered via the PlantUML server) embedded as a markdown image, so it
> renders in GitHub / VS Code / `file://`. Reason: Mermaid has no `useCaseDiagram`
> type (mermaid-js/mermaid#4628; rubric v1.9 §5C.5). Mermaid remains in use for
> sequence diagrams.
> Syntax follows the former reference: Case_02 `Doc21_Use_Cases_Catalog.md` §5.1.

**Source of truth:** `03_PHASE3_DECOMPOSITION/Doc22_Use_Cases_Catalog.md` §4 (product functional use cases, formerly §6B; UC-03..33 plus PKG-DS). Actors are taken from each fully-dressed card (primary actor per §4.x table; supporting actors from "Actor Brief Descriptions" §2.x). Include (`..>`) / extend (`.>`) edges are drawn **only** where a card's `**Constrained by:**` field or extensions explicitly indicate a dependency between two use cases **of the same package**; cross-package constraints are intentionally omitted here and remain traceable in Doc22/Doc23. Note: UC-66 and UC-92 (now UC-06 and UC-32 after the 2026-09-05 RENUMBER, rubric v1.10 §5B rule 7) were re-adjudicated from PROC-39/40 to the UC lane per rubric v1.8 §5B rule 6 (human decision 2026-09-05); they are genuine actor→system use cases shown as PKG-C/PKG-F members per Doc22 §4.2 and §4.7 tables. Diagrams carry UC ovals only (§5C.5): PROC-*/CAP-* live in the Doc32 lane cards.

---

## §1 — System-wide

Seven product packages (PKG-A..F + PKG-DS) and the top actors from Doc22 §4.1 (formerly §6B.0).

```plantuml
@startuml
left to right direction
actor "Customer (Retail)" as CUST
actor "Customer (Corporate)" as CORP
actor "TPP (Third-Party Provider)" as TPP
actor "Underwriter" as UND
actor "SYS-03 (OmniScore AI Platform)" as SYS03
actor "SYS-11 (Fraud & AML Platform)" as SYS11
actor "Data Protection Officer" as DPO
actor "Data Subject" as DSUB
rectangle "PKG-A — Onboarding & KYC" {
usecase "PKG-A\nOnboarding & KYC" as PKGA
}
rectangle "PKG-B — Digital Banking Core" {
usecase "PKG-B\nDigital Banking Core" as PKGB
}
rectangle "PKG-C — Lending & OmniScore" {
usecase "PKG-C\nLending & OmniScore" as PKGC
}
rectangle "PKG-D — Payments & Open Banking" {
usecase "PKG-D\nPayments & Open Banking" as PKGD
}
rectangle "PKG-E — Corporate & Treasury" {
usecase "PKG-E\nCorporate & Treasury" as PKGE
}
rectangle "PKG-F — Fraud & Customer Service" {
usecase "PKG-F\nFraud & Customer Service" as PKGF
}
rectangle "PKG-DS — Privacy & Data-subject UCs" {
usecase "UC-01\nDPO Executes\nData Erasure Request" as UC33
usecase "UC-02\nData Subject Requests\nData Export" as UC34
}
CUST -- PKGA
CUST -- PKGB
CUST -- PKGC
CUST -- PKGD
CUST -- PKGF
CORP -- PKGE
TPP -- PKGD
UND -- PKGC
SYS03 -- PKGC
SYS11 -- PKGA
SYS11 -- PKGD
SYS11 -- PKGF
DSUB -- UC34
DSUB -- UC33
DPO -- UC33
@enduml
```

![System-wide use case diagram](svg/A_s1_system_wide.svg)

---

## §2 — PKG-A: Onboarding & KYC (UC-09..14)

Actors from cards UC-09..14. Includes: UC-09 brief description enumerates UC-10/11/12/13 as in-line steps; UC-14 `**Constrained by:**` UC-11 (vault filing).

```plantuml
@startuml
left to right direction
actor "Customer (Retail)" as CUST
actor "SYS-02 (Mobile app channel)" as SYS02
actor "SYS-11 (Fraud & AML Platform)" as SYS11
actor "SYS-16 (Document vault)" as SYS16
actor "Sanctions screening provider" as SSP
rectangle "PKG-A — Onboarding & KYC" {
usecase "UC-09\nOpen Account via\nMobile App" as UC69
usecase "UC-10\neIDAS Identity Verification" as UC70
usecase "UC-11\nKYC Document Upload &\nVault Filing (SYS-16)" as UC71
usecase "UC-12\nSanctions & PEP Screening" as UC72
usecase "UC-13\nOmniScore Consent &\nData-Use Acknowledgement" as UC73
usecase "UC-14\nTax Residency Self-Certification\n(FATCA/CRS)" as UC74
}
CUST -- UC69
CUST -- UC70
CUST -- UC71
CUST -- UC73
CUST -- UC74
SYS11 -- UC72
SYS02 -- UC69
SYS16 -- UC71
SYS16 -- UC74
SSP -- UC72
UC69 .> UC70 : <<include>>
UC69 .> UC71 : <<include>>
UC69 .> UC72 : <<include>>
UC69 .> UC73 : <<include>>
UC74 .> UC71 : <<include>>
@enduml
```

![PKG-A — Onboarding & KYC use case diagram](svg/A_s2_pkg_a_onboarding_kyc_uc_69_74.svg)

---

## §3 — PKG-B: Digital Banking Core (UC-15..20)

Actors from cards UC-15..20. Includes per `**Constrained by:**`: UC-16→UC-15, UC-17→UC-15, UC-18→UC-15/UC-17, UC-19→UC-17, UC-20→UC-15 (cross-package UC-25/UC-30/UC-02 constraints omitted).

```plantuml
@startuml
left to right direction
actor "Customer (Retail)" as CUST
actor "SYS-02 (Mobile app channel)" as SYS02
actor "SYS-01 (CBS / payments core)" as SYS01
actor "SYS-05 (Card management)" as SYS05
actor "SYS-13 (Customer Data Warehouse)" as SYS13
actor "SYS-16 (Document vault)" as SYS16
rectangle "PKG-B — Digital Banking Core" {
usecase "UC-15\nLogin with PSD2 SCA" as UC75
usecase "UC-16\nView Balances & Transactions" as UC76
usecase "UC-17\nSEPA Transfer\n(incl. Instant)" as UC77
usecase "UC-18\nManage Cards\n(block/limits)" as UC78
usecase "UC-19\nStanding Orders" as UC79
usecase "UC-20\nStatements & Export" as UC80
}
CUST -- UC75
CUST -- UC76
CUST -- UC77
CUST -- UC78
CUST -- UC79
CUST -- UC80
SYS02 -- UC75
SYS01 -- UC77
SYS01 -- UC79
SYS05 -- UC78
SYS13 -- UC76
SYS13 -- UC80
SYS16 -- UC80
UC76 .> UC75 : <<include>>
UC77 .> UC75 : <<include>>
UC78 .> UC75 : <<include>>
UC78 .> UC77 : <<include>>
UC79 .> UC77 : <<include>>
UC80 .> UC75 : <<include>>
@enduml
```

![PKG-B — Digital Banking Core use case diagram](svg/A_s3_pkg_b_digital_banking_core_uc_75_80.svg)

---

## §4 — PKG-C: Lending & OmniScore (UC-03..08)

Actors from cards UC-03/04/05/06/07/08. Edges: UC-05 `**Constrained by:**` UC-03 (consent record) → include; UC-06 (re-adjudicated from PROC-39) is the manual/borderline path of UC-03 per UC-03 brief description → extend.

```plantuml
@startuml
left to right direction
actor "Customer (Retail)" as CUST
actor "SYS-02 (Mobile app channel)" as SYS02
actor "SYS-03 (OmniScore AI Platform)" as SYS03
actor "SYS-14 (Loan Origination)" as SYS14
actor "Underwriter (Consumer Lending)" as UND
rectangle "PKG-C — Lending & OmniScore" {
usecase "UC-03\nApply for Consumer Credit" as UC63
usecase "UC-04\nOmniScore Computes\nCredit Score" as UC64
usecase "UC-05\nCustomer Receives\nScore Explanation" as UC65
usecase "UC-06\nUnderwriter Reviews\nBorderline Application" as UC66
usecase "UC-07\nCustomer Accepts Offer\n& Contract Signed" as UC67
usecase "UC-08\nCustomer Manages Repayment\n& Arrears View" as UC68
}
CUST -- UC63
CUST -- UC65
CUST -- UC67
CUST -- UC68
SYS03 -- UC64
SYS14 -- UC64
SYS02 -- UC63
UND -- UC66
UC65 .> UC63 : <<include>>
UC66 .> UC63 : <<extend>>
@enduml
```

![PKG-C — Lending & OmniScore use case diagram](svg/A_s4_pkg_c_lending_omniscore_uc_63_68.svg)

---

## §5 — PKG-D: Payments & Open Banking (UC-21..25)

Actors from cards UC-21..25. Includes per `**Constrained by:**`: UC-21↔UC-22 (mutual constraint recorded on both cards), UC-23→UC-21/UC-22, UC-25→UC-23 (cross-package UC-15/UC-17/CAP-10 omitted).

```plantuml
@startuml
left to right direction
actor "Customer (Retail)" as CUST
actor "TPP (Third-Party Provider)" as TPP
actor "SYS-18 (Open Banking / PSD2 API Gateway)" as SYS18
actor "SYS-01 (CBS / payments core)" as SYS01
rectangle "PKG-D — Payments & Open Banking" {
usecase "UC-21\nPSD2 Consent Grant/Revoke" as UC81
usecase "UC-22\nTPP Onboarding &\nAIS Access (SYS-18)" as UC82
usecase "UC-23\nPIS Payment Initiation with SCA" as UC83
usecase "UC-24\nPayment Dispute & Chargeback" as UC84
usecase "UC-25\nPayment Limits Management" as UC85
}
CUST -- UC81
CUST -- UC84
CUST -- UC85
TPP -- UC82
TPP -- UC83
SYS18 -- UC82
SYS18 -- UC83
SYS01 -- UC83
UC81 .> UC82 : <<include>>
UC82 .> UC81 : <<include>>
UC83 .> UC81 : <<include>>
UC83 .> UC82 : <<include>>
UC85 .> UC83 : <<include>>
@enduml
```

![PKG-D — Payments & Open Banking use case diagram](svg/A_s5_pkg_d_payments_open_banking_uc_81_85.svg)

---

## §6 — PKG-E: Corporate & Treasury (UC-26..29)

Actors from cards UC-26..29 (Customer (Corporate) personas per card). Includes per `**Constrained by:**`: UC-27/UC-28/UC-29 → UC-26 (delegation scope / delegated authority / corporate authority; cross-package UC-12/UC-15 omitted).

```plantuml
@startuml
left to right direction
actor "Customer (Corporate) — Corporate Administrator" as CADM
actor "Customer (Corporate) — Treasurer" as TRE
actor "Customer (Corporate) — Applicant" as APP
actor "SYS-21 (Corporate Banking Portal)" as SYS21
actor "SYS-08 (Treasury Management System)" as SYS08
actor "SYS-07 (Trade Finance System)" as SYS07
actor "SYS-06 (SWIFT)" as SYS06
rectangle "PKG-E — Corporate & Treasury" {
usecase "UC-26\nCorporate Onboarding with\nDelegated Users (SYS-21)" as UC86
usecase "UC-27\nCash Management Dashboard" as UC87
usecase "UC-28\nFX Deal Execution (SYS-08)" as UC88
usecase "UC-29\nTrade Finance Letter of Credit\n(SYS-07, UCP 600)" as UC89
}
CADM -- UC86
TRE -- UC87
TRE -- UC88
APP -- UC89
SYS21 -- UC86
SYS21 -- UC87
SYS21 -- UC88
SYS08 -- UC87
SYS08 -- UC88
SYS07 -- UC89
SYS06 -- UC89
UC87 .> UC86 : <<include>>
UC88 .> UC86 : <<include>>
UC89 .> UC86 : <<include>>
@enduml
```

![PKG-E — Corporate & Treasury use case diagram](svg/A_s6_pkg_e_corporate_treasury_uc_86_89.svg)

---

## §7 — PKG-F: Fraud & Customer Service (UC-30, UC-31, UC-32, UC-33)

Actors from cards UC-30/31/32/33 (UC-32 re-adjudicated from PROC-40 per rubric v1.8 §5B rule 6). Extend: UC-31 `**Constrained by:**` UC-30 (alert-loop fallback) — contact-centre block as fallback of the in-app alert loop. No same-package includes (all other constraints are cross-package).

```plantuml
@startuml
left to right direction
actor "Customer (Retail)" as CUST
actor "SYS-11 (Fraud & AML Platform)" as SYS11
actor "SYS-20 (Contact Centre Platform)" as SYS20
actor "SYS-17 (CRM)" as SYS17
actor "SOC (SYS-25)" as SOC25
rectangle "PKG-F — Fraud & Customer Service" {
usecase "UC-30\nIn-App Fraud Alert\nConfirm/Deny (SYS-11)" as UC90
usecase "UC-31\nCard Block via\nContact Centre (SYS-20)" as UC91
usecase "UC-32\nComplaint Filing &\nHandling (SYS-17)" as UC92
usecase "UC-33\nSecure Messaging" as UC93
}
CUST -- UC90
CUST -- UC91
CUST -- UC92
CUST -- UC93
SYS11 -- UC90
SYS20 -- UC91
SYS20 -- UC92
SYS17 -- UC92
SYS17 -- UC93
SOC25 -- UC90
UC91 .> UC90 : <<extend>>
@enduml
```

![PKG-F — Fraud & Customer Service use case diagram](svg/A_s7_pkg_f_fraud_customer_service_uc_90_uc_91.svg)
---

## §8 — PKG-DS: Privacy & Data-subject UCs (UC-01, UC-02)

New package in Doc22 v3.0 (UC SEPARATION): UC-33/UC-34 elevated to fully-dressed form (§4.8).
Actors from the cards: Data Protection Officer (primary on UC-01, secondary on UC-02), Data
Subject (requester; primary on UC-02). No same-package includes/extends (the erasure/export
constraints — PROC-21/PROC-23/CAP-10 and UC-03/UC-05/PROC-22 — are compliance-plane or
cross-package and stay traceable in Doc22 §4.8 §10 / §3.2).

```plantuml
@startuml
left to right direction
actor "Data Protection Officer" as DPO
actor "Data Subject" as DSUB
rectangle "PKG-DS — Privacy & Data-subject UCs" {
usecase "UC-01\nDPO Executes\nData Erasure Request" as UC33
usecase "UC-02\nData Subject Requests\nData Export" as UC34
}
DPO -- UC33
DSUB -- UC33
DSUB -- UC34
@enduml
```

![PKG-DS — Privacy & Data-subject UCs use case diagram](svg/A_s8_pkg_ds_privacy_data_subject_ucs_uc_33_uc.svg)

---

> **v1.2 (RENUMBER, 2026-09-05, rubric v1.10 §5B rule 7):** UC ovals renumbered UC-01..33; aliases kept; all 8 SVGs re-rendered from the updated sources.

**Traceability:** UC IDs ↔ Doc22 §4 fully-dressed cards; actor names ↔ §4.1 product actor table and per-card §2 "Actor Brief Descriptions"; include/extend edges ↔ per-card §10 `**Constrained by:**` fields (same-package subset only). Cross-package and compliance-plane dependencies (PROC-43, PROC-45, PROC-49, CAP-10, PROC-50, PROC-41, CAP-08, PROC-39/40, PROC-01..24, CAP-02) are documented in Doc22 §3.2/§4 §10 and Doc23_Use_Case_Relationships.md. UC-01/UC-02 are catalog UCs (PKG-DS, §8 above).
