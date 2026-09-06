---
document_id: AEGIS-P3-RICH-ANNEX-A
title: Annex A — Use Case Diagrams (Phase 3 RICH)
phase: 3
version: 0.8
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
reconciliation_note: "v0.5 rewrite (2026-09-05): legacy `graph`-style package/actor diagrams replaced by 12 Mermaid `useCaseDiagram` (beta) diagrams — 1 system-wide + 11 per package. Source of truth is Doc20_Use_Cases_Catalog.md (§1 actors, §2 functional U.C.7-11, §3 security/compliance U.C.1-6). Post LANE NAMING, compliance cards are PROC-01..17 / CAP-01 (legacy U.C.x.y.z ids preserved where cards kept them). Include/extend edges drawn ONLY where a card explicitly invokes/extends another UC in the same package; cross-package relationships are listed as notes. Legacy Level 0/Level 1 diagrams preserved in git history." # v0.6 (2026-09-05, UC SEPARATION): UC-ovals-only cleanup per rubric v1.8 §5C.5 — PROC-*/CAP-* ovals removed from §7-§12 (lane diagrams are the §5C.4 flowcharts in Doc32), §1 security package ovals relabelled to UC ids only, PKG-TRN (0 UCs) becomes note-only (§12), system-wide omits it. 11 useCaseDiagram blocks remain." # v0.7 (2026-09-05, MERMAID RENDER FIX): the 11 use-case diagrams converted from Mermaid `useCaseDiagram` to native PlantUML source blocks + committed SVGs in svg/ (embedded as markdown images) — Mermaid has no useCaseDiagram type (mermaid-js/mermaid#4628; rubric v1.9 §5C.5).
---

# Annex A — Use Case Diagrams (Phase 3 RICH)

> **Render note:** use-case diagrams are native **PlantUML** — each diagram is a
> `plantuml` source block (source of truth, editable) plus a committed SVG
> (`svg/*.svg`, rendered via the PlantUML server) embedded as a markdown image, so it
> renders in GitHub / VS Code / `file://`. Reason: Mermaid has no `useCaseDiagram`
> type (mermaid-js/mermaid#4628; rubric v1.9 §5C.5). Mermaid remains in use for
> sequence diagrams and lane-card flowcharts.
>
> **Source of truth:** `../Doc20_Use_Cases_Catalog.md` — §1 actors, §2 functional packages (PKG-7…PKG-11, UC-14..UC-36), §3 security & compliance packages (PKG-DP/SEC/IAM/DEV/GOV, UC-01..UC-13 UCs; lane cards PROC-01..17 / CAP-01 live in `../Doc32_Process_Capability_Cards.md` and are NOT drawn here — UC ovals only, rubric v1.8 §5C.5). Ovals carry the card ID + title; actors are the real actor names from Doc20 §1. Diagrams are native PlantUML (see render note above); the former `useCaseDiagram` reference was `Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md` §5.1.
>
> **RENUMBER note (2026-09-05):** oval ids flattened to `UC-01..UC-36` (rubric v1.10 §5B rule 7; registry `00_METHODOLOGY/validation/RENUMBER_REGISTRY_2026-09-05.md`); PlantUML aliases kept as internal slugs; SVGs re-rendered, filenames unchanged.
>
> **Edge convention:** solid `-->` = actor association (Primary Actor / Stakeholders). Dashed `..>` = include/extend, drawn **only** where the card text explicitly invokes or extends another use case.

---

## §1 — System-wide

One oval per package; actors per Doc20 §1. Packages with UC-lane content only (PKG-7…11, PKG-DP/SEC/IAM/DEV/GOV). PKG-TRN Training & Awareness holds no UC cards (its three cards are PROC lane cards in Doc32) — omitted per the UC-ovals-only rule (§5C.5).

```plantuml
@startuml
left to right direction
actor "User (Free-tier)" as USER
actor "Workspace Admin/Owner" as ADM
actor "DPO / Compliance Manager" as DPO
actor "CTO / CISO" as CTO
actor "Lead Developer" as DEV
actor "Operations Lead" as OPS
actor "Risk Owner" as RO
rectangle "PKG-7 Account & Access" {
usecase "UC-14, UC-15, UC-16, UC-17, UC-18\nAccount & Access" as P7
}
rectangle "PKG-8 Team & Task Core" {
usecase "UC-19, UC-20, UC-21, UC-22, UC-23, UC-24\nTeam & Task Core" as P8
}
rectangle "PKG-9 Collaboration" {
usecase "UC-25, UC-26, UC-27, UC-28, UC-29\nCollaboration" as P9
}
rectangle "PKG-10 Platform" {
usecase "UC-30, UC-31, UC-32, UC-33\nPlatform" as P10
}
rectangle "PKG-11 Self-Service" {
usecase "UC-34, UC-35, UC-36\nSelf-Service" as P11
}
rectangle "PKG-DP Data Protection" {
usecase "UC-01, UC-02, UC-03, UC-04\nData Protection" as PDP
}
rectangle "PKG-SEC Security Operations" {
usecase "UC-05, UC-06, UC-07\nSecurity Operations" as PSEC
}
rectangle "PKG-IAM Identity & Access" {
usecase "UC-08, UC-09, UC-10\nIdentity & Access" as PIAM
}
rectangle "PKG-DEV Secure Development" {
usecase "UC-11, UC-12\nSecure Development" as PDEV
}
rectangle "PKG-GOV Governance & Compliance" {
usecase "UC-13\nGovernance & Compliance" as PGOV
}
USER -- P7
USER -- P8
USER -- P9
USER -- P11
ADM -- P10
DPO -- PDP
CTO -- PIAM
CTO -- PGOV
DEV -- PDEV
OPS -- PSEC
RO -- PGOV
@enduml
```

![PKG-7 Account & Access use case diagram](svg/A_s1_system_wide.svg)

---

## §2 — PKG-7 Account & Access (UC-14, UC-15, UC-16, UC-17, UC-18)

Doc20 §2.1. Cross-package: quota/upgrade flows route to UC-31 (PKG-10).

```plantuml
@startuml
left to right direction
actor "Free-tier User" as FU
actor "Member" as MEM
actor "Workspace Admin/Owner" as ADM
rectangle "PKG-7 Account & Access" {
usecase "UC-14\nSign Up & Account Creation" as UC711
usecase "UC-15\nLogin (email/password + optional SSO)" as UC712
usecase "UC-16\nPassword Reset & Recovery" as UC713
usecase "UC-17\nSession Management (timeout, logout-everywhere)" as UC721
usecase "UC-18\nInvite Member & Assign Role" as UC751
}
FU -- UC711
MEM -- UC712
MEM -- UC713
MEM -- UC721
ADM -- UC751
UC751 .> UC711 : <<include>>
@enduml
```

![PKG-7 Account & Access use case diagram](svg/A_s2_pkg_7_account_access_u_c_7.svg)

> UC-15/7.1.3/7.2.1 Primary Actor is "Member **or** Free-tier User" (Doc20 cards §2 Actor Brief Descriptions). `UC751 ..> UC711` = invite invokes sign-up for account-less invitees (card flow step 4 / subflow 6.1).

---

## §3 — PKG-8 Team & Task Core (UC-19, UC-20, UC-21, UC-22, UC-23, UC-24)

Doc20 §2.2. Cross-package: assignee notification via UC-26 (PKG-9); free-tier quota routes to UC-31 (PKG-10).

```plantuml
@startuml
left to right direction
actor "Free-tier User" as FU
actor "Workspace Admin/Owner" as ADM
actor "Member" as MEM
rectangle "PKG-8 Team & Task Core" {
usecase "UC-19\nCreate Workspace" as UC811
usecase "UC-20\nCreate Project" as UC812
usecase "UC-21\nCreate Task" as UC821
usecase "UC-22\nAssign Task" as UC822
usecase "UC-23\nChange Task Status & Due Date" as UC823
usecase "UC-24\nView Project Board (Kanban)" as UC831
}
ADM -- UC811
FU -- UC811
MEM -- UC812
MEM -- UC821
MEM -- UC822
MEM -- UC823
MEM -- UC831
@enduml
```

![PKG-8 Team & Task Core use case diagram](svg/A_s3_pkg_8_team_task_core_u_c_8.svg)

> UC-19 Primary Actor is "Free-tier User **or** Workspace Admin/Owner" (workspace creation on sign-up).

---

## §4 — PKG-9 Collaboration (UC-25, UC-26, UC-27, UC-28, UC-29)

Doc20 §2.3. Cross-package: malicious-attachment handling at UC-27 anchors MUC-08 fail-safe (UC-06, PKG-SEC).

```plantuml
@startuml
left to right direction
actor "Member" as MEM
rectangle "PKG-9 Collaboration" {
usecase "UC-25\nComment on Task" as UC911
usecase "UC-26\n@Mention & In-App Notification" as UC921
usecase "UC-27\nAttach File to Task" as UC931
usecase "UC-28\nSearch & Filter Tasks" as UC941
usecase "UC-29\nActivity Feed (recent events)" as UC951
}
MEM -- UC911
MEM -- UC921
MEM -- UC931
MEM -- UC941
MEM -- UC951
UC911 .> UC921 : <<include>>
@enduml
```

![PKG-9 Collaboration use case diagram](svg/A_s4_pkg_9_collaboration_u_c_9.svg)

> `UC911 ..> UC921` = comment posts notify watchers via UC-26 (card flow step 4).

---

## §5 — PKG-10 Platform (UC-30, UC-31, UC-32, UC-33)

Doc20 §2.4. Cross-package: UC-33 Enterprise SSO is a "UC-15 extension" (PKG-7); UC-32 console invites via UC-18 (PKG-7).

```plantuml
@startuml
left to right direction
actor "Mobile Client" as MOB
actor "Free-tier User" as FU
actor "Workspace Admin/Owner" as ADM
actor "Enterprise Administrator" as ENT
rectangle "PKG-10 Platform" {
usecase "UC-30\nMobile Sync (offline-first)" as UC1011
usecase "UC-31\nStripe Checkout (Upgrade Plan)" as UC1021
usecase "UC-32\nWorkspace Admin Console" as UC1031
usecase "UC-33\nEnterprise SSO" as UC1032
}
MOB -- UC1011
FU -- UC1021
ADM -- UC1021
ADM -- UC1031
ENT -- UC1032
@enduml
```

![PKG-10 Platform use case diagram](svg/A_s5_pkg_10_platform_u_c_10.svg)

> UC-31 Primary Actor is "Free-tier User **or** Workspace Admin/Owner". A-EXT-01 (Stripe Checkout) is the external system actor inside UC-31's flow.

---

## §6 — PKG-11 Self-Service (UC-34, UC-35, UC-36)

Doc20 §2.5. Cross-package: UC-36 erasure cascades to UC-01 (PKG-DP); exports constrained by UC-02 / UC-10.

```plantuml
@startuml
left to right direction
actor "Member" as MEM
actor "Free-tier User" as FU
actor "Workspace Owner" as OWN
rectangle "PKG-11 Self-Service" {
usecase "UC-34\nView My Account (data held)" as UC1111
usecase "UC-35\nExport My Data (GDPR portability)" as UC1121
usecase "UC-36\nDelete My Account / Workspace" as UC1131
}
MEM -- UC1111
MEM -- UC1121
FU -- UC1131
OWN -- UC1131
@enduml
```

![PKG-11 Self-Service use case diagram](svg/A_s6_pkg_11_self_service_u_c_11.svg)

> UC-36 Primary Actor is "Free-tier User **or** Workspace Owner (for workspace deletion)".

---

## §7 — PKG-DP Data Protection (UC-01, UC-02, UC-03, UC-04)

Doc20 §3.1 (4 UC cards; the package's PROC-01..02 lane cards live in Doc32 and are not drawn — §5C.5). No explicit include/extend declared in card bodies.

```plantuml
@startuml
left to right direction
actor "DPO / Compliance Manager" as DPO
actor "Member" as MEM
actor "Free-tier User" as FU
rectangle "PKG-DP Data Protection" {
usecase "UC-01\nData Subject Erasure" as UC121
usecase "UC-02\nData Subject Data Export (portability)" as UC131
usecase "UC-03\nConsent Management" as UC141
usecase "UC-04\nStructured Data Portability" as UC151
}
DPO -- UC121
DPO -- UC131
DPO -- UC151
MEM -- UC141
FU -- UC141
@enduml
```

![PKG-DP Data Protection use case diagram](svg/A_s7_pkg_dp_data_protection_u_c_1.svg)

---

## §8 — PKG-SEC Security Operations (UC-05, UC-06, UC-07)

Doc20 §3.2 (3 UC cards; PROC-03..05 + PROC-18 lane cards in Doc32, not drawn — §5C.5; PROC-18 = formerly UC-07, LEDGER-ZERO F3). No explicit include/extend declared in card bodies.

```plantuml
@startuml
left to right direction
actor "Lead Developer" as DEV
actor "Operations Lead" as OPS
rectangle "PKG-SEC Security Operations" {
usecase "UC-05\nAutomated Patch Deployment" as UC221
usecase "UC-06\nExploit Severity Limitation" as UC241
usecase "UC-07\nData Restoration & Recovery" as UC261
}
DEV -- UC221
OPS -- UC241
OPS -- UC261
@enduml
```

![PKG-SEC Security Operations use case diagram](svg/A_s8_pkg_sec_security_operations_u_c_2.svg)

---

## §9 — PKG-IAM Identity & Access (UC-08, UC-09, UC-10)

Doc20 §3.3 (3 UC cards; PROC-06..07 + PROC-19/20 lane cards in Doc32, not drawn — §5C.5; PROC-19/20 = formerly UC-11/12, LEDGER-ZERO F3). No explicit include/extend declared in card bodies.

```plantuml
@startuml
left to right direction
actor "CTO / CISO" as CTO
actor "Operations Lead" as OPS
actor "Member" as MEM
rectangle "PKG-IAM Identity & Access" {
usecase "UC-08\nUser Authentication" as UC311
usecase "UC-09\nMFA for Privileged Accounts" as UC312
usecase "UC-10\nAudit Logging" as UC351
}
MEM -- UC311
CTO -- UC311
CTO -- UC312
CTO -- UC351
@enduml
```

![PKG-IAM Identity & Access use case diagram](svg/A_s9_pkg_iam_identity_access_u_c_3.svg)

---

## §10 — PKG-DEV Secure Development (UC-11, UC-12)

Doc20 §3.4 (2 UC cards; PROC-08..09 + PROC-21 lane cards in Doc32, not drawn — §5C.5; PROC-21 = formerly UC-16, LEDGER-ZERO F3). No explicit include/extend declared in card bodies.

```plantuml
@startuml
left to right direction
actor "Lead Developer" as DEV
actor "CTO / CISO" as CTO
rectangle "PKG-DEV Secure Development" {
usecase "UC-11\nSAST/DAST in CI/CD" as UC421
usecase "UC-12\nSecurity Patch Deployment" as UC431
}
DEV -- UC421
DEV -- UC431
@enduml
```

![PKG-DEV Secure Development use case diagram](svg/A_s10_pkg_dev_secure_development_u_c_4.svg)

---

## §11 — PKG-GOV Governance & Compliance (UC-13)

Doc20 §3.5 (1 UC card; PROC-10..14 / CAP-01 lane cards in Doc32, not drawn — §5C.5). Substance note: the package's governance/compliance lane (policies, DPIA, RoPA, processor due diligence, DPAs) has no UC ovals here — see Doc32 flowcharts/graph. No explicit include/extend declared in card bodies.

```plantuml
@startuml
left to right direction
actor "Lead Developer" as DEV
rectangle "PKG-GOV Governance & Compliance" {
usecase "UC-13\nSBOM Publication" as UC561
}
DEV -- UC561
@enduml
```

![PKG-GOV Governance & Compliance use case diagram](svg/A_s11_pkg_gov_governance_compliance_u_c_5_6_1.svg)

---

## §12 — PKG-TRN Training & Awareness (no UC cards)

PKG-TRN holds no UC-lane cards: its three cards (Annual Awareness Training, Role-Specific Training, Phishing Simulation) are PROCESS lane cards **PROC-15..17**, living in `../Doc32_Process_Capability_Cards.md` with their §5C.4 flowcharts. A use-case diagram would carry UC ovals only (rubric v1.8 §5C.5) — with zero UCs there is nothing to draw, so the former diagram is removed and this note stands in its place (the Doc20 §3.6 section was likewise folded into the §3.0 Compliance Domain Index).

---

## §13 — Cross-references

- `../Doc20_Use_Cases_Catalog.md` §1 — actor catalogue (A-FREE-01, A-MEMBER-01, A-WSADM-01, A-ENTADM-01, A-MOB-01, A-CEO-01, A-CTO-01, A-DEV-01, A-OPS-01, A-DPO-01, A-RO-01)
- `../Doc20_Use_Cases_Catalog.md` §2 — functional packages PKG-7..11 (23 UC-14..UC-36 cards, Cockburn fully-dressed)
- `../Doc20_Use_Cases_Catalog.md` §3 — security & compliance UC packages PKG-DP/SEC/IAM/DEV/GOV (17 UC-01..UC-13 cards) + §3.0 Compliance Domain Index → the 18 PROC/CAP lane cards in `../Doc32_Process_Capability_Cards.md`
- `../RULE_FREEZE.md` §5 — UC enumeration; `../KG_CHAINS.md` §1 — CH-09 (FR-29 → UC-21 → CR-D-04.3)
- Legacy Level 0/Level 1 `graph` diagrams (v0.4 of this annex) — preserved in git history
- Known-good syntax reference: `Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md` §5.1

---

**End of Annex A — Use Case Diagrams (Phase 3 RICH, v0.6, UC-ovals-only per rubric v1.8 §5C.5)**
