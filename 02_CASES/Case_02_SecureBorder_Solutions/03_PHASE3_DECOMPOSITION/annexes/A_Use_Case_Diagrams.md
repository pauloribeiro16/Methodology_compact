---
document_id: AEGIS-P3-ANNEX-A
title: Use Case Diagrams Annex (Case_02)
phase: 3
version: 1.1
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
case: Case_02_SecureBorder_Solutions
source: Doc21_Use_Cases_Catalog.md (§5.1, §6)
reconciliation_note: v1.1 (UC SEPARATION, 2026-09-05) — PROC ovals/edges removed per rubric v1.8 §5C.5 (UC ovals only); package UC counts updated (PKG-9 4, PKG-10 4, PKG-11 3, PKG-12 3); orphan actors removed; lane diagrams are the Doc31 §5C.4 flowcharts.
---

# Annex A — Use Case Diagrams

> **v1.1 (UC SEPARATION, 2026-09-05).** Use case diagrams carry **UC ovals only** (rubric
> `REALIZATION_CLASS_RUBRIC.md` v1.8 §5C.5): the PROC-23/24/25/26/27 ovals, their actor
> edges and their per-oval notes were removed — those lane cards are diagrammed only as
> §5C.4 flowcharts in `Doc31_Process_Capability_Cards.md`. Prose may still reference lane
> ids where a sequencing/dependency note needs them.

> **Render note:** use-case diagrams are native **PlantUML** — each diagram is a
> `plantuml` source block (source of truth, editable) plus a committed SVG
> (`svg/*.svg`, rendered via the PlantUML server) embedded as a markdown image, so it
> renders in GitHub / VS Code / `file://`. Reason: Mermaid has no `useCaseDiagram`
> type (mermaid-js/mermaid#4628; rubric v1.9 §5C.5). Mermaid remains in use for
> sequence diagrams.

## 0. Scope and conventions

Source of truth: `Doc21_Use_Cases_Catalog.md` — system-wide Level 0 diagram in
§5.1, product functional use cases (U.C.8+, PKG-8..12) in §6. This annex adds one
diagram per product package (§2–§6) plus a compact system-wide view (§1).

Conventions (mirroring Doc21 §5.1 syntax):
- `actor "N" as X` — actors use the stakeholder/actor names of Doc21 §3 and §6.0 (SH- IDs in prose).
- `usecase "ID\nTitle" as Y` — one oval per use case, title from the §6.x package tables.
- `-->` — actor association (Primary Actor or Stakeholder per each card's §2 Actor Brief Descriptions).
- `..>` with label `extend` — drawn **only** where a card's Alternative Flows (§5, the
  fully-dressed extension mechanism — the cards carry no separate "Extensions" field)
  explicitly cross-reference another use case. Extension → base direction.
- Precondition/trigger chains between use cases (e.g. U.C.8.1.1 → U.C.8.2.1 → U.C.8.2.2 →
  U.C.8.2.3 → U.C.8.3.1; U.C.9.1.1 → U.C.9.2.1 → U.C.9.3.1) are noted in prose, not drawn
  as `include` — they are sequencing, not decomposition.

---

## §1 — System-wide

See Doc21 §5.1 — system-wide diagram (Level 0: 7 packages, 13 actors). The compact copy
below keeps the 5 product packages (PKG-8..12) and their top actors (Doc21 §6.0), with no
per-UC detail.

```plantuml
@startuml
left to right direction
actor "Traveler" as TRV
actor "Border Control Officer" as BCO
actor "Operations Lead" as OPS
actor "AI Governance Lead" as AIG
actor "SOC Manager" as SOC
actor "National Border Authority" as NBA
rectangle "PKG-8 Traveller eGate Journey" {
usecase "Traveller eGate Journey\n(7 use cases)" as UC8
}
rectangle "PKG-9 Operator Referral Desk" {
usecase "Operator Referral Desk\n(4 use cases)" as UC9
}
rectangle "PKG-10 Kiosk Fleet Operations" {
usecase "Kiosk Fleet Operations\n(4 use cases)" as UC10
}
rectangle "PKG-11 AI Model Lifecycle" {
usecase "AI Model Lifecycle\n(3 use cases)" as UC11
}
rectangle "PKG-12 Administration & Reporting" {
usecase "Administration & Reporting\n(3 use cases)" as UC12
}
TRV -- UC8
BCO -- UC8
BCO -- UC9
OPS -- UC10
OPS -- UC11
OPS -- UC12
AIG -- UC11
SOC -- UC9
SOC -- UC10
SOC -- UC12
NBA -- UC12
@enduml
```

![PKG-8 Traveller eGate Journey use case diagram](svg/A_s1_system_wide.svg)

---

## §2 — PKG-8: Traveller eGate Journey (7 use cases)

Primary actor: **Traveler** (SH-EXT-002) on U.C.8.1.1–8.3.1 and 8.4.1; **Border Control
Officer** (SH-EXT-001) on U.C.8.3.2. Stakeholders from the cards: SOC Manager (spoof/PA
events, U.C.8.2.2), DPO (notice content owner, U.C.8.4.1), National Border Authority
(data controller via SYS-02, U.C.8.1.1/8.4.1). Every failure path extends into the
referral use case (Alternative Flows of U.C.8.1.1 §5.1–5.3, U.C.8.2.1 §5.1, U.C.8.2.2
§5.1, U.C.8.2.3 §5.1, U.C.8.3.1 §5.1).

```plantuml
@startuml
left to right direction
actor "Traveler" as TRV
actor "Border Control Officer" as BCO
actor "SOC Manager" as SOC
actor "DPO" as DPO
actor "National Border Authority" as NBA
rectangle "PKG-8 Traveller eGate Journey" {
usecase "U.C.8.1.1\nScan Travel Document (MRZ + NFC)" as UC811
usecase "U.C.8.2.1\nCapture Facial Biometric Sample" as UC821
usecase "U.C.8.2.2\nLiveness Detection (PAD)" as UC822
usecase "U.C.8.2.3\nFace Match 1:1 vs Chip Portrait" as UC823
usecase "U.C.8.3.1\nGate Decision & Release" as UC831
usecase "U.C.8.3.2\nReferral to Operator Desk" as UC832
usecase "U.C.8.4.1\nPrivacy Notice & Consent Capture" as UC841
}
TRV -- UC811
TRV -- UC821
TRV -- UC822
TRV -- UC823
TRV -- UC831
TRV -- UC841
BCO -- UC832
SOC -- UC822
DPO -- UC841
NBA -- UC811
NBA -- UC841
UC832 .> UC811 : <<extend>>
UC832 .> UC821 : <<extend>>
UC832 .> UC822 : <<extend>>
UC832 .> UC823 : <<extend>>
UC832 .> UC831 : <<extend>>
@enduml
```

![PKG-8 Traveller eGate Journey use case diagram](svg/A_s2_pkg_8_traveller_egate_journey_7_use_case.svg)

Journey sequencing (preconditions, not drawn): 8.4.1/8.1.1 → 8.2.1 → 8.2.2 → 8.2.3 → 8.3.1.

#### U.C.8.1.1 — Scan Travel Document (MRZ + NFC chip)
Primary: Traveler. Stakeholders: Border Officer (referral receiver), National Border Authority (via SYS-02). Extensions: MRZ unreadable / PA invalid / MRZ-chip mismatch → U.C.8.3.2.

#### U.C.8.2.1 — Capture Facial Biometric Sample
Primary: Traveler. Stakeholders: Border Officer, AI Governance Lead (quality thresholds). Extensions: quality below threshold / multi-face / template failure → U.C.8.3.2.

#### U.C.8.2.2 — Liveness Detection (Presentation Attack Detection)
Primary: Traveler. Stakeholders: SOC Manager (spoof events), Border Officer. Extensions: score below threshold / sensor anomaly → U.C.8.3.2.

#### U.C.8.2.3 — Face Match 1:1 Against Chip Portrait
Primary: Traveler. Stakeholders: Border Officer (below-threshold/grey-band), National Border Authority (SYS-02). Extensions: below threshold / grey band → U.C.8.3.2 (never auto-reject).

#### U.C.8.3.1 — Gate Decision & Release
Primary: Traveler. Stakeholders: Border Officer (watchlist/door-failure). Extensions: watchlist hit (quiet referral) / door failure → U.C.8.3.2.

#### U.C.8.3.2 — Referral to Operator Desk
Primary: Border Control Officer. Stakeholders: Traveler, SOC Manager (impostor escalation), DPO (override audit). Extension target of all PKG-8 failure paths.

#### U.C.8.4.1 — Traveller Privacy Notice & Consent Capture
Primary: Traveler. Stakeholders: DPO (notice owner), National Border Authority (controller). Extensions: consent declined → manual officer lane (no UC reference — not drawn).

---

## §3 — PKG-9: Operator Referral Desk (4 use cases)

Primary actor: **Border Control Officer** (SH-EXT-001) on all four. Stakeholders from the
cards: Traveler (presents at desk, U.C.9.3.1), SOC Manager (escalation/clearance, U.C.9.2.1/
9.3.1/9.4.1), DPO (override audit, U.C.9.3.1). One explicit extension: high-risk step-up
re-authentication (U.C.9.1.1 §6.2) on override actions (U.C.9.3.1 §5.1). (The shift-handover
lane card PROC-23 — Doc31 — is no longer drawn here: §5C.5 UC ovals only.)

```plantuml
@startuml
left to right direction
actor "Border Control Officer" as BCO
actor "Traveler" as TRV
actor "SOC Manager" as SOC
actor "DPO" as DPO
rectangle "PKG-9 Operator Referral Desk" {
usecase "U.C.9.1.1\nOperator Console Session (SSO/FIDO2)" as UC911
usecase "U.C.9.2.1\nReferral Queue Handling & Triage" as UC921
usecase "U.C.9.3.1\nManual Verification & Override (Reason Codes)" as UC931
usecase "U.C.9.4.1\nIncident Flag & Gate Lock" as UC941
}
BCO -- UC911
BCO -- UC921
BCO -- UC931
BCO -- UC941
TRV -- UC931
SOC -- UC921
SOC -- UC941
DPO -- UC931
UC911 .> UC931 : <<extend>>
@enduml
```

![PKG-9 Operator Referral Desk use case diagram](svg/A_s3_pkg_9_operator_referral_desk_4_use_cases.svg)

Session chain (preconditions, not drawn): U.C.9.1.1 → U.C.9.2.1 (claimed item) → U.C.9.3.1.

#### U.C.9.1.1 — Operator Console Session (SSO/FIDO2, Fail-Closed)
Primary: Border Officer. Stakeholders: Ops Lead (role admin via PROC-27), SOC Manager (auth anomalies). Extensions: FIDO2 failure → fail-closed, no UC reference (not drawn).

#### U.C.9.2.1 — Referral Queue Handling & Triage
Primary: Border Officer. Stakeholders: SOC Manager (overflow, correlation). Extensions: overflow → intake throttle (U.C.8.3.2 §5.3 behaviour — cross-package, not drawn).

#### U.C.9.3.1 — Manual Identity Verification & Override (Reason Codes)
Primary: Border Officer. Stakeholders: Traveler, SOC Manager, DPO. Extension: step-up re-auth per U.C.9.1.1 §6.2 (drawn).

#### U.C.9.4.1 — Incident Flag & Gate Lock
Primary: Border Officer. Stakeholders: SOC Manager (owns triage/clearance). No cross-UC references in Alternative Flows.

---

## §4 — PKG-10: Kiosk Fleet Operations (4 use cases)

Primary actor: **Operations Lead** (SH-INT-007) on U.C.10.2.1/10.3.1/10.5.1;
**SOC Manager** (SH-INT-008) primaries U.C.10.4.1. Stakeholders from the cards: Dev Lead
(SH-INT-006, OTA co-signing), Airport Operator (SH-EXT-004, physical access). Explicit
extension: heartbeat loss → offline/failover assessment (U.C.10.2.1 §5.1). (The
provisioning lane card PROC-24 — Doc31 — is no longer drawn here: §5C.5 UC ovals only; its
boot-chain-failure extension into U.C.10.4.1 is recorded in Doc31 §PROC-24.)

```plantuml
@startuml
left to right direction
actor "Operations Lead" as OPS
actor "SOC Manager" as SOC
actor "Lead Developer" as DEV
actor "Airport Operator" as APT
rectangle "PKG-10 Kiosk Fleet Operations" {
usecase "U.C.10.2.1\nFleet Health Monitoring" as UC1021
usecase "U.C.10.3.1\nSigned OTA Firmware Update (Cosign, Staged)" as UC1031
usecase "U.C.10.4.1\nTamper Alert Response" as UC1041
usecase "U.C.10.5.1\nOffline/Failover Mode (Store-and-Forward)" as UC1051
}
OPS -- UC1021
OPS -- UC1031
OPS -- UC1051
SOC -- UC1021
SOC -- UC1041
DEV -- UC1031
APT -- UC1041
UC1051 .> UC1021 : <<extend>>
@enduml
```

![PKG-10 Kiosk Fleet Operations use case diagram](svg/A_s4_pkg_10_kiosk_fleet_operations_4_use_case.svg)

#### U.C.10.2.1 — Fleet Health Monitoring
Primary: Ops Lead. Stakeholders: SOC Manager (security-class anomalies). Extension: heartbeat loss → U.C.10.5.1 assessment (drawn); tamper indicators → U.C.10.4.1 appears in basic flow step 4, not an extension (not drawn).

#### U.C.10.3.1 — Signed OTA Firmware Update (Cosign, Staged)
Primary: Ops Lead. Stakeholders: Dev Lead, SOC Manager. No cross-UC references in Alternative Flows.

#### U.C.10.4.1 — Tamper Alert Response
Primary: SOC Manager. Stakeholders: Ops Lead, Airport Operator. Trigger sources U.C.10.2.1 / U.C.9.4.1 appear in the trigger/precondition text (not drawn).

#### U.C.10.5.1 — Offline/Failover Mode (Store-and-Forward Crossing Events)
Primary: Ops Lead. Stakeholders: SOC Manager (backhaul-loss detection). No cross-UC references in Alternative Flows.

---

## §5 — PKG-11: AI Model Lifecycle (3 use cases)

Primary actor: **AI Governance Lead** (SH-INT-005) on U.C.11.2.1/11.3.1;
**Operations Lead** (SH-INT-007) primaries U.C.11.5.1. Stakeholders from the cards: SOC
Manager (rollback incident link, U.C.11.3.1), National Border Authority (SH-EXT-003,
watchlist sync, U.C.11.5.1). **No Alternative Flows block in PKG-11 cross-references
another U.C.** — no dotted arrows. (The training/release lane card PROC-25 and the
drift/bias review lane card PROC-26 — Doc31 — are no longer drawn here: §5C.5 UC ovals
only; their stakeholder sets (Dev Lead, DPO, AI Market Surveillance Authority) belong to
those cards.)

```plantuml
@startuml
left to right direction
actor "AI Governance Lead" as AIG
actor "Operations Lead" as OPS
actor "SOC Manager" as SOC
actor "National Border Authority" as NBA
rectangle "PKG-11 AI Model Lifecycle" {
usecase "U.C.11.2.1\nSigned Model Rollout to Fleet (Staged)" as UC1121
usecase "U.C.11.3.1\nModel Rollback" as UC1131
usecase "U.C.11.5.1\nWatchlist Cache Sync (SYS-03 sFTP, HSM-Bound)" as UC1151
}
AIG -- UC1121
AIG -- UC1131
OPS -- UC1151
SOC -- UC1131
NBA -- UC1151
@enduml
```

![PKG-11 AI Model Lifecycle use case diagram](svg/A_s5_pkg_11_ai_model_lifecycle_3_use_cases.svg)

Lifecycle sequencing (preconditions/basic flow, not drawn): training/release packaging gate (PROC-25, Doc31) → U.C.11.2.1 (rollout eligibility) → U.C.11.3.1 (rollback arming); drift/bias review dispositions (PROC-26, Doc31) → retrain (PROC-25) or rollback (U.C.11.3.1).

#### U.C.11.2.1 — Signed Model Rollout to Fleet (Staged)
Primary: AI Governance Lead. Stakeholders: Ops Lead, SOC Manager. No cross-UC references in Alternative Flows.

#### U.C.11.3.1 — Model Rollback
Primary: AI Governance Lead. Stakeholders: SOC Manager, Dev Lead. Extensions reference U.C.10.4.1 path (cross-package, not drawn).

#### U.C.11.5.1 — Watchlist Cache Sync (SYS-03 sFTP, HSM-Bound)
Primary: Ops Lead. Stakeholders: National Border Authority. No cross-UC references in Alternative Flows.

---

## §6 — PKG-12: Administration & Reporting (3 use cases)

Primary actor: **Operations Lead** (SH-INT-007) on U.C.12.1.1, U.C.12.3.1;
**National Border Authority** (SH-EXT-003) primaries U.C.12.2.1. Stakeholders from the
cards: second approver (CISO delegate or Security Engineer, U.C.12.1.1 dual control),
SOC Manager (config-drift alerts, audit export), Compliance Analyst and DPO (audit
export), CISO and Airport Operator (dashboard). (The role-administration lane card
PROC-27 — Doc31 — is no longer drawn here: §5C.5 UC ovals only.)
**No Alternative Flows block in PKG-12 cross-references another U.C.** — no dotted arrows.

```plantuml
@startuml
left to right direction
actor "Operations Lead" as OPS
actor "Second Approver (CISO del. / Sec. Eng.)" as APPR
actor "National Border Authority" as NBA
actor "Compliance Analyst" as COMP
actor "DPO" as DPO
actor "SOC Manager" as SOC
actor "CISO" as CISO
actor "Airport Operator" as APT
rectangle "PKG-12 Administration & Reporting" {
usecase "U.C.12.1.1\nKiosk Admin Configuration (Dual Control)" as UC1211
usecase "U.C.12.2.1\nAudit Export for Authorities (WORM STORE-04)" as UC1221
usecase "U.C.12.3.1\nSLA & Fleet Status Dashboard" as UC1231
}
OPS -- UC1211
OPS -- UC1231
APPR -- UC1211
NBA -- UC1221
COMP -- UC1221
DPO -- UC1221
SOC -- UC1211
SOC -- UC1221
CISO -- UC1231
APT -- UC1231
@enduml
```

![PKG-12 Administration & Reporting use case diagram](svg/A_s6_pkg_12_administration_reporting_3_use_ca.svg)

#### U.C.12.1.1 — Kiosk Admin Configuration (TPM-Bound, Dual Control)
Primary: Ops Lead. Stakeholders: Second Approver, SOC Manager. No cross-UC references in Alternative Flows.

#### U.C.12.2.1 — Audit Export for Authorities (WORM STORE-04)
Primary: National Border Authority. Stakeholders: Compliance Analyst, SOC Manager, DPO. No cross-UC references in Alternative Flows.

#### U.C.12.3.1 — SLA & Fleet Status Dashboard
Primary: Ops Lead. Stakeholders: CISO, Airport Operator. Fed by U.C.10.2.1/U.C.10.5.1 telemetry (basic-flow/trigger text, not drawn).

---

**Element budget check:** each diagram ≤ 20 elements (actors + ovals): §1 = 11, §2 = 12,
§3 = 8, §4 = 8, §5 = 7, §6 = 11. All aliases defined within their diagram; braces balanced.
Lane cards (PROC-23..27) are diagrammed only in Doc31 §5C.4 flowcharts (UC SEPARATION,
2026-09-05); §3–§6 titles carry the true UC counts (4/4/3/3).
