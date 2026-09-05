---
document_id: AEGIS-P3-ANNEX-B
title: Sequence Diagrams Annex (Case_02)
phase: 3
version: 1.1
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
case: Case_02_SecureBorder_Solutions
source: Doc21_Use_Cases_Catalog.md (§6 product UC cards)
---

# Annex B — Sequence Diagrams

> **v1.1 (UC SEPARATION, 2026-09-05).** One section per product UC card (§5C.5), ordered by
> the catalogue's §6 card order — 21 sections, 1:1 with the 21 `**Sequence diagram:**`
> pointers in Doc21. The 5 former PROC sections (PROC-23, PROC-24, PROC-25, PROC-26,
> PROC-27) were removed: lane cards do not carry sequence diagrams (§5C.5); their diagrams
> are the §5C.4 flowcharts in `Doc31_Process_Capability_Cards.md`. The stale "B.1 Critical
> Path Sequences" PLACEHOLDER block and the `[CASE_NAME]` header were replaced by proper
> frontmatter (C3 F1 precedent).

---

## §1 — Use-Case — {U.C.8.1.1} Scan Travel Document (MRZ + NFC chip)

```mermaid
sequenceDiagram
    participant TRV as "SH-EXT-002 (Traveler)"
    participant KIOSK as "SYS-06 + SYS-04 (Kiosk)"
    TRV->>KIOSK: Confirm start, place passport on reader
    KIOSK->>KIOSK: Read MRZ, derive BAC/PACE, open NFC chip channel
    KIOSK->>KIOSK: Read chip (portrait + MRZ), validate PA vs CSCA
    KIOSK-->>TRV: Display extracted document data for confirmation
```

## §2 — Use-Case — {U.C.8.2.1} Capture Facial Biometric Sample

```mermaid
sequenceDiagram
    participant TRV as "SH-EXT-002 (Traveler)"
    participant KIOSK as "SYS-06 + SYS-04 (Kiosk)"
    KIOSK->>TRV: Prompt to look at camera
    TRV->>KIOSK: Align with positioning guide
    KIOSK->>KIOSK: Capture burst (3D depth + RGB), run quality checks
    KIOSK->>KIOSK: Compute template in-kiosk, purge raw frames (STORE-05)
```

## §3 — Use-Case — {U.C.8.2.2} Liveness Detection (Presentation Attack Detection)

```mermaid
sequenceDiagram
    participant TRV as "SH-EXT-002 (Traveler)"
    participant KIOSK as "SYS-04 (Edge AI PAD)"
    participant SOC as "SH-INT-008 (SOC)"
    TRV->>KIOSK: Present to sensor
    KIOSK->>KIOSK: Passive+active challenge, CNN liveness score in-kiosk
    KIOSK->>KIOSK: Score >= threshold -> sample certified live
    KIOSK-->>SOC: On failure: spoof security event (kiosk ID + timestamp)
```

## §4 — Use-Case — {U.C.8.2.3} Face Match 1:1 Against Chip Portrait

```mermaid
sequenceDiagram
    participant KIOSK as "SYS-04 (Edge AI)"
    participant AUTH as "SYS-02 (Border authority)"
    KIOSK->>KIOSK: 1:1 live template vs chip portrait, similarity score (<= 2 s)
    KIOSK->>KIOSK: Threshold decision, purge template + frames, keep decision record
    KIOSK-->>AUTH: Match decision shared with national border control
```

## §5 — Use-Case — {U.C.8.3.1} Gate Decision & Release

```mermaid
sequenceDiagram
    participant KIOSK as "SYS-06 + SYS-04 (Kiosk)"
    participant AUTH as "SYS-02 (Border authority)"
    KIOSK->>KIOSK: Combine inputs (PA, liveness, match, watchlist)
    KIOSK->>KIOSK: RELEASE -> door opens
    KIOSK->>AUTH: Crossing event (outbound-only mTLS/QUIC channel)
    KIOSK->>KIOSK: Decision record -> immutable log (no biometric payload)
```

## §6 — Use-Case — {U.C.8.3.2} Referral to Operator Desk

```mermaid
sequenceDiagram
    participant OFFR as "SH-EXT-001 (Border Officer)"
    participant CON as "SYS-08 (Console, SSO+FIDO2)"
    participant LOG as "Immutable audit chain"
    OFFR->>CON: Authenticate (FIDO2), open work item
    CON-->>OFFR: Reason class, chip data, live camera view
    OFFR->>CON: Record decision (approve/deny) + reason code
    CON->>LOG: Append decision (officer ID, timestamps)
```

## §7 — Use-Case — {U.C.8.4.1} Traveller Privacy Notice & Consent Capture

```mermaid
sequenceDiagram
    participant TRV as "SH-EXT-002 (Traveler)"
    participant KIOSK as "SYS-06 (Kiosk)"
    KIOSK->>TRV: Privacy notice (purposes, biometrics, retention, rights)
    TRV->>KIOSK: Acknowledge, consent token where consent-based
    KIOSK->>KIOSK: Link acknowledgement reference to the journey record
```

## §8 — Use-Case — {U.C.9.1.1} Operator Console Session (SSO/FIDO2, Fail-Closed)

```mermaid
sequenceDiagram
    participant OFFR as "SH-EXT-001 (Border Officer)"
    participant SSO as "SYS-08 (Okta + ADFS)"
    participant CON as "Console client"
    OFFR->>SSO: Open console, present FIDO2 assertion
    SSO->>SSO: Verify FIDO2 (mandatory) + risk check
    SSO-->>CON: Role-scoped session token
    CON-->>OFFR: Referral work surface (actions bound to officer ID)
```

## §9 — Use-Case — {U.C.9.2.1} Referral Queue Handling & Triage

```mermaid
sequenceDiagram
    participant KIOSK as "SYS-04/SYS-06 (Kiosk)"
    participant CON as "Console queue (SYS-08)"
    participant OFFR as "SH-EXT-001 (Border Officer)"
    KIOSK->>CON: Referral + reason class + queue token
    CON-->>OFFR: Ordered queue, officer claims item
    OFFR->>CON: Triage reason class, open work item
    CON->>CON: Record state + queue telemetry (U.C.12.3.1)
```

## §10 — Use-Case — {U.C.9.3.1} Manual Identity Verification & Override (Reason Codes)

```mermaid
sequenceDiagram
    participant OFFR as "SH-EXT-001 (Border Officer)"
    participant CON as "Console (SYS-08)"
    participant LOG as "Immutable audit chain (STORE-04)"
    CON-->>OFFR: Evidence bundle (reason class, chip data, live view)
    OFFR->>CON: Outcome (approve/deny/override) + mandatory reason code
    CON->>LOG: Append decision (officer ID, timestamps)
    CON-->>OFFR: Lane dispatch confirmed
```

## §11 — Use-Case — {U.C.9.4.1} Incident Flag & Gate Lock

```mermaid
sequenceDiagram
    participant OFFR as "SH-EXT-001 (Border Officer)"
    participant SOC as "SH-INT-008 (SOC, SYS-12)"
    participant KIOSK as "SYS-06/SYS-04 (Kiosk)"
    OFFR->>SOC: Flag case (incident class + evidence refs)
    SOC->>KIOSK: Lock gate, halt intake
    KIOSK-->>SOC: Lock state confirmed
    SOC-->>KIOSK: On clearance: release lock (logged)
```

## §12 — Use-Case — {U.C.10.2.1} Fleet Health Monitoring

```mermaid
sequenceDiagram
    participant KIOSK as "SYS-06 (Kiosk fleet)"
    participant SIEM as "SYS-09/SYS-12 (Aggregation)"
    participant OPS as "SH-INT-007 (Ops Lead)"
    participant SOC as "SH-INT-008 (SOC)"
    KIOSK->>SIEM: Heartbeat + sensor state + versions
    SIEM->>OPS: Maintenance-class anomaly -> work order
    SIEM->>SOC: Security-class anomaly (e.g. tamper)
    SIEM->>SIEM: Correlate per unit/lane (CAP-02)
```

## §13 — Use-Case — {U.C.10.3.1} Signed OTA Firmware Update (Cosign, Staged)

```mermaid
sequenceDiagram
    participant OPS as "SH-INT-007 (Ops Lead)"
    participant PIPE as "SYS-11 (OTA pipeline)"
    participant KIOSK as "SYS-06/SYS-04 (Kiosk)"
    OPS->>PIPE: Schedule staged rollout (canary -> rings)
    PIPE->>KIOSK: Signed package + CycloneDX SBOM (mTLS)
    KIOSK->>KIOSK: Verify cosign signature in TPM, atomic apply
    KIOSK-->>OPS: New version reported, ring gate on health
```

## §14 — Use-Case — {U.C.10.4.1} Tamper Alert Response

```mermaid
sequenceDiagram
    participant MON as "SYS-09/SYS-12 (Telemetry)"
    participant SOC as "SH-INT-008 (SOC)"
    participant OPS as "SH-INT-007 (Ops Lead)"
    MON->>SOC: Tamper alert (unit ID + class)
    SOC->>OPS: Contain: lock unit (U.C.9.4.1), revoke cert
    OPS-->>SOC: Inspection result (false / confirmed)
    SOC->>SOC: Re-image from signed baseline or retire, log
```

## §15 — Use-Case — {U.C.10.5.1} Offline/Failover Mode (Store-and-Forward Crossing Events)

```mermaid
sequenceDiagram
    participant KIOSK as "SYS-06/SYS-04 (Kiosk)"
    participant SINK as "SYS-09 (Audit sink)"
    participant OPS as "SH-INT-007 (Ops Lead)"
    KIOSK->>KIOSK: Heartbeat loss -> failover -> restricted mode
    KIOSK->>KIOSK: Queue events (encrypted, sequenced)
    KIOSK->>SINK: On reconnect: ordered store-and-forward flush
    SINK-->>OPS: Completeness reconciled, offline window logged
```

## §16 — Use-Case — {U.C.11.2.1} Signed Model Rollout to Fleet (Staged)

```mermaid
sequenceDiagram
    participant AIG as "SH-INT-005 (AI Governance)"
    participant PIPE as "SYS-11 (Distribution)"
    participant KIOSK as "SYS-04 (Edge AI runtime)"
    AIG->>PIPE: Approve staged rollout (canary -> rings)
    PIPE->>KIOSK: Signed model artefact (cosign + SBOM)
    KIOSK->>KIOSK: Verify signature in TPM, pin version
    KIOSK-->>AIG: Canary metrics -> ring gate (vs governed bounds)
```

## §17 — Use-Case — {U.C.11.3.1} Model Rollback

```mermaid
sequenceDiagram
    participant AIG as "SH-INT-005 (AI Governance)"
    participant KIOSK as "SYS-04 (Edge AI runtime)"
    participant SOC as "SH-INT-008 (SOC)"
    AIG->>KIOSK: Rollback to previous signed version (scope)
    KIOSK->>KIOSK: Revert, update version pins
    KIOSK-->>AIG: Health + drift metrics confirm revert
    AIG->>SOC: Link rollback to incident record
```

## §18 — Use-Case — {U.C.11.5.1} Watchlist Cache Sync (SYS-03 sFTP, HSM-Bound)

```mermaid
sequenceDiagram
    participant SYS3 as "SYS-03 (Gov feed)"
    participant CACHE as "STORE-03 (Isolated cache)"
    participant KIOSK as "SYS-04 (Read endpoints)"
    SYS3->>CACHE: sFTP batch to DMZ, HSM-bound decryption
    CACHE->>CACHE: 1:1 mirror update (encrypted, HSM CMK)
    KIOSK->>CACHE: Read via subservice endpoints only
    CACHE-->>SYS3: Sync version logged, deletions propagated
```

## §19 — Use-Case — {U.C.12.1.1} Kiosk Admin Configuration (TPM-Bound, Dual Control)

```mermaid
sequenceDiagram
    participant OPS as "SH-INT-007 (Ops Lead)"
    participant APP as "Second approver (dual control)"
    participant KIOSK as "SYS-06/SYS-04 (Unit)"
    OPS->>APP: Config version (diff vs baseline)
    APP->>OPS: Approve (sensitive classes)
    OPS->>KIOSK: Dispatch over mTLS management channel
    KIOSK-->>OPS: Applied, version recorded, drift watched
```

## §20 — Use-Case — {U.C.12.2.1} Audit Export for Authorities (WORM STORE-04)

```mermaid
sequenceDiagram
    participant AUTH as "SH-EXT-003 (Authority)"
    participant COMP as "SH-INT-010 + DPO (Scope check)"
    participant WORM as "SYS-09 STORE-04 (WORM)"
    AUTH->>COMP: Evidence request (case/period scope)
    COMP->>WORM: Approved scoped extraction
    WORM-->>AUTH: Signed bundle (signature chain + integrity proof)
    COMP->>COMP: Export recorded in audit chain
```

## §21 — Use-Case — {U.C.12.3.1} SLA & Fleet Status Dashboard

```mermaid
sequenceDiagram
    participant TEL as "SYS-09 (Telemetry)"
    participant DASH as "SLA & Fleet dashboard"
    participant OPS as "SH-INT-007 (Ops Lead)"
    TEL->>DASH: Unit status + SLA counters
    DASH->>DASH: Uptime vs 99.99%, breach windows annotated
    DASH-->>OPS: Live view + threshold alerts
    DASH->>DASH: Periodic SLA report archived
```

