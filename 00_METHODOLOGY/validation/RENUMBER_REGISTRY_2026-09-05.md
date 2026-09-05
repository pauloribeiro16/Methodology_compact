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
| U.C.10.1.1 | UC-34 | Mobile Sync (offline-first) |
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

## Case_02_* — F3 (PENDING)

| Old | New |
|---|---|
| *(to be filled by F3 census — 15 compliance → UC-01..15, U.C.8..12 product → UC-16..36)* | |
