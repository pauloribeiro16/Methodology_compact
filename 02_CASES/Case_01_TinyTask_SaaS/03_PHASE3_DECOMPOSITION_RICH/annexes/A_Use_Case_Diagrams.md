---
document_id: AEGIS-P3-RICH-ANNEX-A
title: Annex A — Use Case Diagrams (Phase 3 RICH)
phase: 3
version: 0.6
created: 2026-08-24
updated: 2026-09-05
author: Fase de Especificação 4 Executor (paulo@methodology.pt)
status: ADJUSTED_FIELDS
case: Case_01_TinyTask_SaaS
tier: MICRO
sibling_of: ../03_PHASE2_RULES_RICH/
branch: feature/aegis-p3-case01-rich
sibling_doc: ../03_PHASE3_DECOMPOSITION/annexes/A_Use_Case_Diagrams.md
inputs: [../Doc20_Use_Cases_Catalog.md]
outputs: []
related_documents: [../Doc20_Use_Cases_Catalog.md, ../Doc32_Process_Capability_Cards.md, ../RULE_FREEZE.md, ../KG_CHAINS.md]
expected_documents: annex-a
reconciliation_note: "v0.5 rewrite (2026-09-05): legacy `graph`-style package/actor diagrams replaced by 12 Mermaid `useCaseDiagram` (beta) diagrams — 1 system-wide + 11 per package. Source of truth is Doc20_Use_Cases_Catalog.md (§1 actors, §2 functional U.C.7-11, §3 security/compliance U.C.1-6). Post LANE NAMING, compliance cards are PROC-01..17 / CAP-01 (legacy U.C.x.y.z ids preserved where cards kept them). Include/extend edges drawn ONLY where a card explicitly invokes/extends another UC in the same package; cross-package relationships are listed as notes. Legacy Level 0/Level 1 diagrams preserved in git history." # v0.6 (2026-09-05, UC SEPARATION): UC-ovals-only cleanup per rubric v1.8 §5C.5 — PROC-*/CAP-* ovals removed from §7-§12 (lane diagrams are the §5C.4 flowcharts in Doc32), §1 security package ovals relabelled to UC ids only, PKG-TRN (0 UCs) becomes note-only (§12), system-wide omits it. 11 useCaseDiagram blocks remain.
---

# Annex A — Use Case Diagrams (Phase 3 RICH)

> **Render note:** Mermaid `useCaseDiagram` — requires Mermaid ≥ v11.6 (GitHub renders; older VS Code may not; the source is readable as fallback).
>
> **Source of truth:** `../Doc20_Use_Cases_Catalog.md` — §1 actors, §2 functional packages (PKG-7…PKG-11, U.C.7–11), §3 security & compliance packages (PKG-DP/SEC/IAM/DEV/GOV, U.C.1–6 UCs; lane cards PROC-01..17 / CAP-01 live in `../Doc32_Process_Capability_Cards.md` and are NOT drawn here — UC ovals only, rubric v1.8 §5C.5). Ovals carry the card ID + title; actors are the real actor names from Doc20 §1. Syntax mimics the known-good `useCaseDiagram` in `Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md` §5.1.
>
> **Edge convention:** solid `-->` = actor association (Primary Actor / Stakeholders). Dashed `..>` = include/extend, drawn **only** where the card text explicitly invokes or extends another use case.

---

## §1 — System-wide

One oval per package; actors per Doc20 §1. Packages with UC-lane content only (PKG-7…11, PKG-DP/SEC/IAM/DEV/GOV). PKG-TRN Training & Awareness holds no UC cards (its three cards are PROC lane cards in Doc32) — omitted per the UC-ovals-only rule (§5C.5).

```mermaid
useCaseDiagram
    actor "User (Free-tier)" as USER
    actor "Workspace Admin/Owner" as ADM
    actor "DPO / Compliance Manager" as DPO
    actor "CTO / CISO" as CTO
    actor "Lead Developer" as DEV
    actor "Operations Lead" as OPS
    actor "Risk Owner" as RO

    package "PKG-7 Account & Access" {
        usecase "U.C.7\nAccount & Access" as P7
    }
    package "PKG-8 Team & Task Core" {
        usecase "U.C.8\nTeam & Task Core" as P8
    }
    package "PKG-9 Collaboration" {
        usecase "U.C.9\nCollaboration" as P9
    }
    package "PKG-10 Platform" {
        usecase "U.C.10\nPlatform" as P10
    }
    package "PKG-11 Self-Service" {
        usecase "U.C.11\nSelf-Service" as P11
    }
    package "PKG-DP Data Protection" {
        usecase "U.C.1.*\nData Protection" as PDP
    }
    package "PKG-SEC Security Operations" {
        usecase "U.C.2.*\nSecurity Operations" as PSEC
    }
    package "PKG-IAM Identity & Access" {
        usecase "U.C.3.*\nIdentity & Access" as PIAM
    }
    package "PKG-DEV Secure Development" {
        usecase "U.C.4.*\nSecure Development" as PDEV
    }
    package "PKG-GOV Governance & Compliance" {
        usecase "U.C.5.6.1\nGovernance & Compliance" as PGOV
    }

    USER --> P7
    USER --> P8
    USER --> P9
    USER --> P11
    ADM --> P10
    DPO --> PDP
    CTO --> PIAM
    CTO --> PGOV
    DEV --> PDEV
    OPS --> PSEC
    RO --> PGOV
```

---

## §2 — PKG-7 Account & Access (U.C.7)

Doc20 §2.1. Cross-package: quota/upgrade flows route to U.C.10.2.1 (PKG-10).

```mermaid
useCaseDiagram
    actor "Free-tier User" as FU
    actor "Member" as MEM
    actor "Workspace Admin/Owner" as ADM

    package "PKG-7 Account & Access" {
        usecase "U.C.7.1.1\nSign Up & Account Creation" as UC711
        usecase "U.C.7.1.2\nLogin (email/password + optional SSO)" as UC712
        usecase "U.C.7.1.3\nPassword Reset & Recovery" as UC713
        usecase "U.C.7.2.1\nSession Management (timeout, logout-everywhere)" as UC721
        usecase "U.C.7.5.1\nInvite Member & Assign Role" as UC751
    }

    FU --> UC711
    MEM --> UC712
    MEM --> UC713
    MEM --> UC721
    ADM --> UC751
    UC751 ..> UC711
```

> U.C.7.1.2/7.1.3/7.2.1 Primary Actor is "Member **or** Free-tier User" (Doc20 cards §2 Actor Brief Descriptions). `UC751 ..> UC711` = invite invokes sign-up for account-less invitees (card flow step 4 / subflow 6.1).

---

## §3 — PKG-8 Team & Task Core (U.C.8)

Doc20 §2.2. Cross-package: assignee notification via U.C.9.2.1 (PKG-9); free-tier quota routes to U.C.10.2.1 (PKG-10).

```mermaid
useCaseDiagram
    actor "Free-tier User" as FU
    actor "Workspace Admin/Owner" as ADM
    actor "Member" as MEM

    package "PKG-8 Team & Task Core" {
        usecase "U.C.8.1.1\nCreate Workspace" as UC811
        usecase "U.C.8.1.2\nCreate Project" as UC812
        usecase "U.C.8.2.1\nCreate Task" as UC821
        usecase "U.C.8.2.2\nAssign Task" as UC822
        usecase "U.C.8.2.3\nChange Task Status & Due Date" as UC823
        usecase "U.C.8.3.1\nView Project Board (Kanban)" as UC831
    }

    ADM --> UC811
    FU --> UC811
    MEM --> UC812
    MEM --> UC821
    MEM --> UC822
    MEM --> UC823
    MEM --> UC831
```

> U.C.8.1.1 Primary Actor is "Free-tier User **or** Workspace Admin/Owner" (workspace creation on sign-up).

---

## §4 — PKG-9 Collaboration (U.C.9)

Doc20 §2.3. Cross-package: malicious-attachment handling at U.C.9.3.1 anchors MUC-08 fail-safe (U.C.2.4.1, PKG-SEC).

```mermaid
useCaseDiagram
    actor "Member" as MEM

    package "PKG-9 Collaboration" {
        usecase "U.C.9.1.1\nComment on Task" as UC911
        usecase "U.C.9.2.1\n@Mention & In-App Notification" as UC921
        usecase "U.C.9.3.1\nAttach File to Task" as UC931
        usecase "U.C.9.4.1\nSearch & Filter Tasks" as UC941
        usecase "U.C.9.5.1\nActivity Feed (recent events)" as UC951
    }

    MEM --> UC911
    MEM --> UC921
    MEM --> UC931
    MEM --> UC941
    MEM --> UC951
    UC911 ..> UC921
```

> `UC911 ..> UC921` = comment posts notify watchers via U.C.9.2.1 (card flow step 4).

---

## §5 — PKG-10 Platform (U.C.10)

Doc20 §2.4. Cross-package: U.C.10.3.2 Enterprise SSO is a "U.C.7.1.2 extension" (PKG-7); U.C.10.3.1 console invites via U.C.7.5.1 (PKG-7).

```mermaid
useCaseDiagram
    actor "Mobile Client" as MOB
    actor "Free-tier User" as FU
    actor "Workspace Admin/Owner" as ADM
    actor "Enterprise Administrator" as ENT

    package "PKG-10 Platform" {
        usecase "U.C.10.1.1\nMobile Sync (offline-first)" as UC1011
        usecase "U.C.10.2.1\nStripe Checkout (Upgrade Plan)" as UC1021
        usecase "U.C.10.3.1\nWorkspace Admin Console" as UC1031
        usecase "U.C.10.3.2\nEnterprise SSO" as UC1032
    }

    MOB --> UC1011
    FU --> UC1021
    ADM --> UC1021
    ADM --> UC1031
    ENT --> UC1032
```

> U.C.10.2.1 Primary Actor is "Free-tier User **or** Workspace Admin/Owner". A-EXT-01 (Stripe Checkout) is the external system actor inside U.C.10.2.1's flow.

---

## §6 — PKG-11 Self-Service (U.C.11)

Doc20 §2.5. Cross-package: U.C.11.3.1 erasure cascades to U.C.1.2.1 (PKG-DP); exports constrained by U.C.1.3.1 / U.C.3.5.1.

```mermaid
useCaseDiagram
    actor "Member" as MEM
    actor "Free-tier User" as FU
    actor "Workspace Owner" as OWN

    package "PKG-11 Self-Service" {
        usecase "U.C.11.1.1\nView My Account (data held)" as UC1111
        usecase "U.C.11.2.1\nExport My Data (GDPR portability)" as UC1121
        usecase "U.C.11.3.1\nDelete My Account / Workspace" as UC1131
    }

    MEM --> UC1111
    MEM --> UC1121
    FU --> UC1131
    OWN --> UC1131
```

> U.C.11.3.1 Primary Actor is "Free-tier User **or** Workspace Owner (for workspace deletion)".

---

## §7 — PKG-DP Data Protection (U.C.1.*)

Doc20 §3.1 (4 UC cards; the package's PROC-01..02 lane cards live in Doc32 and are not drawn — §5C.5). No explicit include/extend declared in card bodies.

```mermaid
useCaseDiagram
    actor "DPO / Compliance Manager" as DPO
    actor "Member" as MEM
    actor "Free-tier User" as FU

    package "PKG-DP Data Protection" {
        usecase "U.C.1.2.1\nData Subject Erasure" as UC121
        usecase "U.C.1.3.1\nData Subject Data Export (portability)" as UC131
        usecase "U.C.1.4.1\nConsent Management" as UC141
        usecase "U.C.1.5.1\nStructured Data Portability" as UC151
    }

    DPO --> UC121
    DPO --> UC131
    DPO --> UC151
    MEM --> UC141
    FU --> UC141
```

---

## §8 — PKG-SEC Security Operations (U.C.2.*)

Doc20 §3.2 (4 UC cards; PROC-03..05 lane cards in Doc32, not drawn — §5C.5). No explicit include/extend declared in card bodies.

```mermaid
useCaseDiagram
    actor "Lead Developer" as DEV
    actor "Operations Lead" as OPS

    package "PKG-SEC Security Operations" {
        usecase "U.C.2.2.1\nAutomated Patch Deployment" as UC221
        usecase "U.C.2.4.1\nExploit Severity Limitation" as UC241
        usecase "U.C.2.4.2\nDoS Resilience" as UC242
        usecase "U.C.2.6.1\nData Restoration & Recovery" as UC261
    }

    DEV --> UC221
    OPS --> UC241
    OPS --> UC242
    OPS --> UC261
```

---

## §9 — PKG-IAM Identity & Access (U.C.3.*)

Doc20 §3.3 (5 UC cards; PROC-06..07 lane cards in Doc32, not drawn — §5C.5). No explicit include/extend declared in card bodies.

```mermaid
useCaseDiagram
    actor "CTO / CISO" as CTO
    actor "Operations Lead" as OPS
    actor "Member" as MEM

    package "PKG-IAM Identity & Access" {
        usecase "U.C.3.1.1\nUser Authentication" as UC311
        usecase "U.C.3.1.2\nMFA for Privileged Accounts" as UC312
        usecase "U.C.3.2.1\nAuthorisation / Least Privilege" as UC321
        usecase "U.C.3.3.1\nSecure System Defaults" as UC331
        usecase "U.C.3.5.1\nAudit Logging" as UC351
    }

    MEM --> UC311
    CTO --> UC311
    CTO --> UC312
    CTO --> UC321
    CTO --> UC351
    OPS --> UC331
```

---

## §10 — PKG-DEV Secure Development (U.C.4.*)

Doc20 §3.4 (3 UC cards; PROC-08..09 lane cards in Doc32, not drawn — §5C.5). No explicit include/extend declared in card bodies.

```mermaid
useCaseDiagram
    actor "Lead Developer" as DEV
    actor "CTO / CISO" as CTO

    package "PKG-DEV Secure Development" {
        usecase "U.C.4.2.1\nSAST/DAST in CI/CD" as UC421
        usecase "U.C.4.3.1\nSecurity Patch Deployment" as UC431
        usecase "U.C.4.4.1\nFail-Safe Design" as UC441
    }

    DEV --> UC421
    DEV --> UC431
    CTO --> UC441
```

---

## §11 — PKG-GOV Governance & Compliance (U.C.5.6.1)

Doc20 §3.5 (1 UC card; PROC-10..14 / CAP-01 lane cards in Doc32, not drawn — §5C.5). Substance note: the package's governance/compliance lane (policies, DPIA, RoPA, processor due diligence, DPAs) has no UC ovals here — see Doc32 flowcharts/graph. No explicit include/extend declared in card bodies.

```mermaid
useCaseDiagram
    actor "Lead Developer" as DEV

    package "PKG-GOV Governance & Compliance" {
        usecase "U.C.5.6.1\nSBOM Publication" as UC561
    }

    DEV --> UC561
```

---

## §12 — PKG-TRN Training & Awareness (no UC cards)

PKG-TRN holds no UC-lane cards: its three cards (Annual Awareness Training, Role-Specific Training, Phishing Simulation) are PROCESS lane cards **PROC-15..17**, living in `../Doc32_Process_Capability_Cards.md` with their §5C.4 flowcharts. A use-case diagram would carry UC ovals only (rubric v1.8 §5C.5) — with zero UCs there is nothing to draw, so the former diagram is removed and this note stands in its place (the Doc20 §3.6 section was likewise folded into the §3.0 Compliance Domain Index).

---

## §13 — Cross-references

- `../Doc20_Use_Cases_Catalog.md` §1 — actor catalogue (A-FREE-01, A-MEMBER-01, A-WSADM-01, A-ENTADM-01, A-MOB-01, A-CEO-01, A-CTO-01, A-DEV-01, A-OPS-01, A-DPO-01, A-RO-01)
- `../Doc20_Use_Cases_Catalog.md` §2 — functional packages PKG-7..11 (23 U.C.7–11 cards, Cockburn fully-dressed)
- `../Doc20_Use_Cases_Catalog.md` §3 — security & compliance UC packages PKG-DP/SEC/IAM/DEV/GOV (17 U.C.1–6 cards) + §3.0 Compliance Domain Index → the 18 PROC/CAP lane cards in `../Doc32_Process_Capability_Cards.md`
- `../RULE_FREEZE.md` §5 — UC enumeration; `../KG_CHAINS.md` §1 — CH-09 (FR-29 → UC-25 → CR-D-04.3)
- Legacy Level 0/Level 1 `graph` diagrams (v0.4 of this annex) — preserved in git history
- Known-good syntax reference: `Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md` §5.1

---

**End of Annex A — Use Case Diagrams (Phase 3 RICH, v0.6, UC-ovals-only per rubric v1.8 §5C.5)**
