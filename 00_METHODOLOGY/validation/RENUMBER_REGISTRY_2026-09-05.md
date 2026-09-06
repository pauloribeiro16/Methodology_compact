---
document_id: AEGIS-VALID-RENUMBER-REGISTRY
title: RENUMBER Registry — Flat 1..N Lane Ids (old→new per case)
phase: 3
version: 1.0
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
---

# RENUMBER Registry — old→new lane id mapping (3 cases)

Rubric: `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` v1.10 §5B rule 7 (compact
renumbering — flat 1..N per lane per case, no gaps, no retired numbers, dotted
`U.C.x.y.z` flattened). Campaign plan: `02_CASES/RENUMBER_CAMPAIGN_2026-09-05.md`.

Rules:
- Renames applied in **two phases** (old → `TMP-<new>` → new), word-boundary exact.
- Historical "formerly" provenance values (`> Formerly UC-NN —` lines, Doc32 "Formerly"
  column, version-history prose describing past numbering) are **not** renamed — they
  keep the ids they named at the time.
- This file is the authoritative old→new traceability record.

---

## Case_03_OmniBank_Financial — F1 (2026-09-05, DONE)

### UC lane (33): flat UC-01..UC-33

| Old | New |
|---|---|
| UC-33 | UC-01 |
| UC-34 | UC-02 |
| UC-63 | UC-03 |
| UC-64 | UC-04 |
| UC-65 | UC-05 |
| UC-66 | UC-06 |
| UC-67 | UC-07 |
| UC-68 | UC-08 |
| UC-69 | UC-09 |
| UC-70 | UC-10 |
| UC-71 | UC-11 |
| UC-72 | UC-12 |
| UC-73 | UC-13 |
| UC-74 | UC-14 |
| UC-75 | UC-15 |
| UC-76 | UC-16 |
| UC-77 | UC-17 |
| UC-78 | UC-18 |
| UC-79 | UC-19 |
| UC-80 | UC-20 |
| UC-81 | UC-21 |
| UC-82 | UC-22 |
| UC-83 | UC-23 |
| UC-84 | UC-24 |
| UC-85 | UC-25 |
| UC-86 | UC-26 |
| UC-87 | UC-27 |
| UC-88 | UC-28 |
| UC-89 | UC-29 |
| UC-90 | UC-30 |
| UC-91 | UC-31 |
| UC-92 | UC-32 |
| UC-93 | UC-33 |

Dotted child variants found in census: `UC-33.1`, `UC-34.1` → renamed consistently to
`UC-01.1`, `UC-02.1`. No other dotted variants exist in Case_03.

### PROC lane (12): PROC-39..50 freed and filled

| Old | New |
|---|---|
| PROC-41 | PROC-39 |
| PROC-42 | PROC-40 |
| PROC-43 | PROC-41 |
| PROC-44 | PROC-42 |
| PROC-45 | PROC-43 |
| PROC-46 | PROC-44 |
| PROC-47 | PROC-45 |
| PROC-48 | PROC-46 |
| PROC-49 | PROC-47 |
| PROC-50 | PROC-48 |
| PROC-51 | PROC-49 |
| PROC-52 | PROC-50 |

Unchanged lanes: `PROC-01..38`, `CAP-01..10`.

---

## Case_01_TinyTask_SaaS — F2 (2026-09-05, DONE)

Census: 40 live dotted ids (Doc20 `####`/`#### Use-Case` headings + subtree grep, md+py).
Sort: ascending natural (dotted components compared numerically). Compliance lane first
(U.C.1..6 → UC-01..17), then product lane (U.C.7..11 → UC-18..40).

### UC lane (40): flat UC-01..UC-40

| Old | New | Title (Doc20) |
|---|---|---|
| U.C.1.2.1 | UC-01 | Data Subject Erasure |
| U.C.1.3.1 | UC-02 | Data Subject Data Export (portability) |
| U.C.1.4.1 | UC-03 | Consent Management |
| U.C.1.5.1 | UC-04 | Structured Data Portability |
| U.C.2.2.1 | UC-05 | Automated Patch Deployment |
| U.C.2.4.1 | UC-06 | Exploit Severity Limitation |
| U.C.2.4.2 | UC-07 | DoS Resilience |
| U.C.2.6.1 | UC-08 | Data Restoration & Recovery |
| U.C.3.1.1 | UC-09 | User Authentication |
| U.C.3.1.2 | UC-10 | MFA for Privileged Accounts |
| U.C.3.2.1 | UC-11 | Authorisation / Least Privilege |
| U.C.3.3.1 | UC-12 | Secure System Defaults |
| U.C.3.5.1 | UC-13 | Audit Logging |
| U.C.4.2.1 | UC-14 | SAST/DAST in CI/CD |
| U.C.4.3.1 | UC-15 | Security Patch Deployment |
| U.C.4.4.1 | UC-16 | Fail-Safe Design |
| U.C.5.6.1 | UC-17 | SBOM Publication |
| U.C.7.1.1 | UC-18 | Sign Up & Account Creation |
| U.C.7.1.2 | UC-19 | Login (email/password + optional SSO) |
| U.C.7.1.3 | UC-20 | Password Reset & Recovery |
| U.C.7.2.1 | UC-21 | Session Management (timeout, logout-everywhere) |
| U.C.7.5.1 | UC-22 | Invite Member & Assign Role |
| U.C.8.1.1 | UC-23 | Create Workspace |
| U.C.8.1.2 | UC-24 | Create Project |
| U.C.8.2.1 | UC-25 | Create Task |
| U.C.8.2.2 | UC-26 | Assign Task |
| U.C.8.2.3 | UC-27 | Change Task Status & Due Date |
| U.C.8.3.1 | UC-28 | View Project Board (Kanban) |
| U.C.9.1.1 | UC-29 | Comment on Task |
| U.C.9.2.1 | UC-30 | @Mention & In-App Notification |
| U.C.9.3.1 | UC-31 | Attach File to Task |
| U.C.9.4.1 | UC-32 | Search & Filter Tasks |
| U.C.9.5.1 | UC-33 | Activity Feed (recent events) |
| U.C.10.1.1 | UC-34 | Kiosk Admin Configuration (TPM-Bound, Dual Control) |
| U.C.10.2.1 | UC-35 | Stripe Checkout (Upgrade Plan) |
| U.C.10.3.1 | UC-36 | Workspace Admin Console |
| U.C.10.3.2 | UC-37 | Enterprise SSO |
| U.C.11.1.1 | UC-38 | View My Account (data held) |
| U.C.11.2.1 | UC-39 | Export My Data (GDPR portability) |
| U.C.11.3.1 | UC-40 | Delete My Account / Workspace |

Unchanged lanes: `PROC-01..17`, `CAP-01` (already contiguous).

### Group/parent grammars (live references) — deterministic remapping

| Old grammar | New | Note |
|---|---|---|
| `U.C.1-6` / `U.C.1–6` | `UC-01..UC-17` | live range refs |
| `U.C.7-11` / `U.C.7–11` | `UC-18..UC-40` | live range refs |
| `U.C.1.*`…`U.C.5.*` | package member ranges (e.g. `U.C.3.*` → `UC-09..UC-13`) | |
| `U.C.7.*` / `U.C.8.*` / `U.C.9.*` / `U.C.10.*` / `U.C.11.*` | `UC-18..UC-22` / `UC-23..UC-28` / `UC-29..UC-33` / `UC-34..UC-37` / `UC-38..UC-40` | |
| `U.C.7.1.*`, `U.C.7.5.*`, `U.C.8.1.*`, `U.C.2.4.*`, `U.C.10.2.*`, `U.C.10.3.*`, `U.C.11.3.*` | sub-package member ranges (`U.C.7.1.*` → `UC-18..UC-20`, etc.) | |
| `U.C.8.x`, `U.C.11.x`, `U.C.8.2.x` | package/sub-package member ranges | |
| `U.C.5.1.*` | `PROC-10` | legacy lane-card group (only U.C.5.1.1 existed → PROC-10) |
| `U.C.6.*` | `PROC-15..17` | package 6 has no live UCs — its three cards are PROC lane cards |
| bare `U.C.7`-style package refs (Annex A ovals) | package member ranges | |

### Legacy dotted ids NOT renamed (historical provenance)

The 18 lane-card ids that left the UC lane in the UC SEPARATION campaign (rubric v1.8
§5B rule 6) keep the ids they are named by in "Formerly"/legacy prose: `U.C.1.1.1`,
`U.C.1.1.2`, `U.C.1.6.1`, `U.C.2.1.1`, `U.C.2.3.1`, `U.C.2.5.1`, `U.C.2.7.1`,
`U.C.3.4.1`, `U.C.3.6.1`, `U.C.4.1.1`, `U.C.4.5.1`, `U.C.5.1.1`, `U.C.5.1.2`,
`U.C.5.2.1`, `U.C.5.3.1`, `U.C.5.4.1`, `U.C.5.5.1`, `U.C.5.7.1`, `U.C.6.1.1`,
`U.C.6.2.1`, `U.C.6.3.1` (incl. the `UC-x.y.z` spelling used in
`Phase_3_Functional_Decomposition_Synthesis.md`). Protected historical lines: Doc20
frontmatter notes + §6.1/§6.2 migration tables (+ new RENUMBER supersede note), Doc32
"Formerly" column, sprint6/reconciliation notes, freeze lines in PROJECT_STATEs,
`validation/` sprint & lint reports (frozen records).

## Case_02_SecureBorder_Solutions — F3 (2026-09-05, DONE)

Census: 36 live dotted ids (Doc21 `#### Use-Case: {U.C.x.y.z}` headings §6 + §7 tables +
subtree grep, md+py+csv). Compliance per-UC ids use the same dotted grammar as product;
`UC-DP..UC-TRN` are domain/package labels (not UC ids) and stay. Sort: ascending natural
(dotted components compared numerically). Compliance lane first (§7, 15 UCs → UC-01..15),
then product lane (§6, U.C.8..12, 21 UCs → UC-16..36).

### UC lane (36): flat UC-01..UC-36

| Old | New | Title (Doc21) |
|---|---|---|
| U.C.1.2.1 | UC-01 | Right to Erasure (Cryptographic Sharding) |
| U.C.2.3.1 | UC-02 | Vulnerability Scanning & Management |
| U.C.2.4.1 | UC-03 | Patch Deployment (Signed OTA) |
| U.C.3.2.1 | UC-04 | Multi-Factor Authentication |
| U.C.3.3.1 | UC-05 | Biometric Enrollment |
| U.C.3.4.1 | UC-06 | Least Privilege Access Enforcement |
| U.C.3.5.1 | UC-07 | Secure Default Configuration |
| U.C.3.7.1 | UC-08 | Human-in-the-Loop Override |
| U.C.4.2.1 | UC-09 | Dependency Scanning & SBOM |
| U.C.4.3.1 | UC-10 | CI/CD Security Gate |
| U.C.4.6.1 | UC-11 | AI Model Versioning & Rollback |
| U.C.5.8.1 | UC-12 | Third-Party Boundary Management |
| U.C.6.2.1 | UC-13 | AI Accuracy Monitoring & Drift Detection |
| U.C.6.4.1 | UC-14 | AI Explainability Reporting |
| U.C.6.7.1 | UC-15 | AI Training Data Management |
| U.C.8.1.1 | UC-16 | Scan Travel Document (MRZ + NFC chip) |
| U.C.8.2.1 | UC-17 | Capture Facial Biometric Sample |
| U.C.8.2.2 | UC-18 | Liveness Detection (Presentation Attack Detection) |
| U.C.8.2.3 | UC-19 | Face Match 1:1 Against Chip Portrait |
| U.C.8.3.1 | UC-20 | Gate Decision & Release |
| U.C.8.3.2 | UC-21 | Referral to Operator Desk |
| U.C.8.4.1 | UC-22 | Traveller Privacy Notice & Consent Capture |
| U.C.9.1.1 | UC-23 | Operator Console Session (SSO/FIDO2, Fail-Closed) |
| U.C.9.2.1 | UC-24 | Referral Queue Handling & Triage |
| U.C.9.3.1 | UC-25 | Manual Identity Verification & Override (Reason Codes) |
| U.C.9.4.1 | UC-26 | Incident Flag & Gate Lock |
| U.C.10.2.1 | UC-27 | Fleet Health Monitoring |
| U.C.10.3.1 | UC-28 | Signed OTA Firmware Update (Cosign, Staged) |
| U.C.10.4.1 | UC-29 | Tamper Alert Response |
| U.C.10.5.1 | UC-30 | Offline/Failover Mode (Store-and-Forward Crossing Events) |
| U.C.11.2.1 | UC-31 | Signed Model Rollout to Fleet (Staged) |
| U.C.11.3.1 | UC-32 | Model Rollback |
| U.C.11.5.1 | UC-33 | Watchlist Cache Sync (SYS-03 sFTP, HSM-Bound) |
| U.C.12.1.1 | UC-34 | Kiosk Admin Configuration (TPM-Bound, Dual Control) |
| U.C.12.2.1 | UC-35 | Audit Export for Authorities (WORM STORE-04) |
| U.C.12.3.1 | UC-36 | SLA & Fleet Status Dashboard |

Unchanged lanes: `PROC-01..27`, `CAP-01..10` (already contiguous). Domain/package labels
`UC-DP..UC-TRN` (Doc21 §5.1/§7) and aliases `UC8..UC12`, `UC811`-style (Annex A) unchanged.

### Group/parent grammars (live references) — deterministic remapping

| Old grammar | New | Note |
|---|---|---|
| `U.C.1–U.C.7` / `U.C.1–7` | `UC-01..UC-15` | live compliance-lane range refs |
| `U.C.8–U.C.12` / `U.C.8–12` / `U.C.8+` | `UC-16..UC-36` | live product-lane range refs |
| `U.C.8.x–12.x` / `U.C.8.*–U.C.12.*` | `UC-16..UC-36` | product branch refs (Doc27 §3.1) |
| `U.C.8.x` / `U.C.8.x.y` / `U.C.8.*` | `UC-16..UC-22` | PKG-8 member range |
| `U.C.8.1.*` | `UC-16` | only member is 8.1.1 |
| `U.C.8.2.*` | `UC-17..UC-19` | |
| `U.C.8.1.1–8.3.1` / `U.C.8.1.1–U.C.8.3.1` | `UC-16..UC-20` | Annex A / Doc21 ranges |
| `U.C.10.x` | `UC-27..UC-30` | PKG-10 member range (incl. Doc31 CAP-02 mermaid node) |
| `U.C.11.x` | `UC-31..UC-33` | PKG-11 member range (Doc22, Doc24) |
| `U.C.9.1.1–U.C.9.3.1` / `…–U.C.9.4.1` / `…–9.5.1` | `UC-23..UC-25` / `UC-23..UC-26` / `UC-23..UC-26` | range endpoints; 9.5.1 is a retired lane card (PROC-23), so `–9.5.1` resolves to UC-26 |
| `U.C.10.2.1–U.C.10.5.1` | `UC-27..UC-30` | |
| `U.C.12.1.1–12.4.1` | `UC-34..UC-36` | 12.4.1 retired (PROC-27); range resolves to UC-36 |
| bare dotted tails (`…U.C.9.2.1/9.3.1/9.4.1`, `…U.C.10.2.1/10.3.1/10.5.1`, `U.C.8.1.1/8.4.1`, Annex A chain `8.4.1/8.1.1 → 8.2.1 …`) | `UC-24/UC-25/UC-26`, `UC-27/UC-28/UC-30`, `UC-16/UC-22`, `UC-22/UC-16 → UC-17 → UC-18 → UC-19 → UC-20` | continuation tokens after a full id, and Annex A prose chain |

### Legacy dotted ids NOT renamed (historical provenance)

The 32 §7 lane-card ids + 5 product PROC stub ids that left the UC lane in LANE NAMING /
UC SEPARATION (rubric v1.3/v1.8 §5B rule 6) keep the ids they are named by: `U.C.1.1.1`,
`U.C.1.3.1`(→PROC-02 Formerly), `U.C.1.4.1`, `U.C.1.5.1`, `U.C.1.6.1`, `U.C.2.1.1`,
`U.C.2.2.1`, `U.C.2.5.1`, `U.C.2.6.1`, `U.C.2.7.1`, `U.C.2.8.1`, `U.C.3.1.1`, `U.C.3.6.1`,
`U.C.4.1.1`, `U.C.4.4.1`, `U.C.4.5.1`, `U.C.5.1.1`, `U.C.5.2.1`, `U.C.5.3.1`, `U.C.5.4.1`,
`U.C.5.5.1`, `U.C.5.6.1`, `U.C.5.7.1`, `U.C.6.1.1`, `U.C.6.3.1`, `U.C.6.5.1`, `U.C.6.6.1`,
`U.C.7.1.1`, `U.C.7.2.1`, `U.C.7.3.1`, `U.C.7.4.1`, `U.C.7.5.1`, `U.C.9.5.1`, `U.C.10.1.1`,
`U.C.11.1.1`, `U.C.11.4.1`, `U.C.12.4.1`. Protected historical lines: Doc31 "Formerly"
column (37 rows), Doc27 "(formerly U.C.x.y.z)" tree annotations, Doc21 §6.6 "Formerly"
blockquote + Lane Naming section, Doc21 §6 v1.3 nomenclature blockquote, version-history
rows, Doc23 v1.1 row pairing "U.C.10.1.1/PROC-24", Doc21 v1.0 release row "(44 UCs: …)"
(the row CHK-5 claim-parses — historical, informational), and frozen records under
`**/validation/` + `02_PHASE2_RULES_RICH/TRACEABILITY_AUDIT.md`.

### Stale live references re-anchored (not renumbered)

- `PROJECT_STATE.md` §7.1 next-steps table: `U.C.2.7.1`→`PROC-08`, `U.C.6.3.1`→`PROC-20`,
  `U.C.2.8.1`→`PROC-09` (ids retired by LANE NAMING; re-anchored to the owning lane cards).
- `Doc21` MUC-07 row references `U.C.2.4.2` (id never existed in C2's live catalog —
  Case_01-family reference); left verbatim, informational.

## LEDGER-ZERO F3 append (2026-09-06) — Case_01 re-lane + compact renumber

P7 decision 2026-09-06: 4 borderline compliance UCs re-laned (rubric v1.8 §5B rule 6):
| Old UC | Title | New lane id |
|---|---|---|
| UC-07 | DoS Resilience | PROC-18 |
| UC-11 | Authorisation / Least Privilege | PROC-19 |
| UC-12 | Secure System Defaults | PROC-20 |
| UC-16 | Fail-Safe Design | PROC-21 |

Compact renumber (rubric v1.10 §5B rule 7, ascending, relative order preserved):
| Old | New | Family |
|---|---|---|
| UC-01..06 | UC-01..06 (unchanged) | compliance |
| UC-08, UC-09, UC-10, UC-13, UC-14, UC-15, UC-17 | UC-07, UC-08, UC-09, UC-10, UC-11, UC-12, UC-13 | compliance |
| UC-18..40 | UC-14..36 (shift −4) | product |
End state Case_01: 36 live UCs (13 compliance + 23 product) · PROC-01..21 · CAP-01.
