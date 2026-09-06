---
document_id: AEGIS-P3-ANNEX-B
title: Sequence Diagrams Annex
phase: 3
version: 1.1
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
---

# Annex B — Sequence Diagrams

> Extracted from the catalogue cards per rubric v1.7 §5C.5 (sequence diagrams are annex-only). One section per product UC card.
> **Render note:** Mermaid ≥ v11 recommended.
> **RENUMBER note (2026-09-05):** section ids flattened to `UC-01..UC-36` (rubric v1.10 §5B rule 7); the 23 product sections map monotonically to UC-14..UC-36, so §1..§23 ordering and the Doc20 pointers are unchanged (registry `00_METHODOLOGY/validation/RENUMBER_REGISTRY_2026-09-05.md`).

## §1 — Use-Case — {UC-14} Sign Up & Account Creation

```mermaid
sequenceDiagram
    participant U as A-FREE-01 (Free-tier User)
    participant SYS as A-SYS-01 (TinyTask API)
    participant IdP as A-EXT-02 (Auth0 IdP)
    U->>SYS: Submit sign-up form (email + password, or OAuth)
    SYS->>SYS: Validate email format + password strength (NFR-01)
    SYS->>SYS: Create account record, record consent state (UC-03)
    SYS-->>U: Send verification email
    U->>SYS: Confirm — account status flips to active
```

## §2 — Use-Case — {UC-15} Login (email/password + optional SSO)

```mermaid
sequenceDiagram
    participant U as A-MEMBER-01 / A-FREE-01
    participant SYS as A-SYS-01 (TinyTask API)
    participant IdP as A-EXT-02 (Auth0 IdP)
    U->>SYS: Submit credentials at /login, or click "Login with SSO"
    SYS->>IdP: Validate password, or validate OIDC token
    IdP-->>SYS: Validation result
    SYS->>SYS: Issue session token (30-min idle timeout), log auth event
    SYS-->>U: Session established
```

## §3 — Use-Case — {UC-16} Password Reset & Recovery

```mermaid
sequenceDiagram
    participant U as A-MEMBER-01 / A-FREE-01
    participant SYS as A-SYS-01 (TinyTask API)
    U->>SYS: Submit email via "Forgot password"
    SYS->>SYS: Generate single-use reset token (1-hour expiry), send link
    U->>SYS: Open link, submit new password
    SYS->>SYS: Validate strength, hash, replace — invalidate all sessions
    SYS-->>U: Reset confirmed — user must log in again
```

## §4 — Use-Case — {UC-17} Session Management (timeout, logout-everywhere)

```mermaid
sequenceDiagram
    participant U as A-MEMBER-01 / A-FREE-01
    participant SYS as A-SYS-01 (TinyTask API)
    SYS->>SYS: Detect trigger (30-min idle / logout / forced)
    SYS->>SYS: Invalidate session token server-side
    SYS-->>U: Redirect to login (or forced-logout confirmation)
    SYS->>SYS: Log the event
```

## §5 — Use-Case — {UC-18} Invite Member & Assign Role

```mermaid
sequenceDiagram
    participant ADM as A-WSADM-01 (Workspace Admin)
    participant SYS as A-SYS-01 (TinyTask API)
    participant INV as A-MEMBER-01 (Invitee)
    ADM->>SYS: Enter email + role, click "Invite"
    SYS->>SYS: Validate email + role, create pending membership
    SYS-->>INV: Send invite email (single-use acceptance link)
    INV->>SYS: Accept link (sign-up UC-14 if no account)
    SYS->>SYS: Grant role, log membership grant event
```

## §6 — Use-Case — {UC-19} Create Workspace

```mermaid
sequenceDiagram
    participant U as A-FREE-01 / A-WSADM-01
    participant SYS as A-SYS-01 (TinyTask API)
    U->>SYS: Click "New Workspace", enter name + optional description
    SYS->>SYS: Validate uniqueness within account, create workspace record
    SYS->>SYS: Grant Owner role to creator, log event
    SYS-->>U: Workspace active
```

## §7 — Use-Case — {UC-20} Create Project

```mermaid
sequenceDiagram
    participant M as A-MEMBER-01 (Member)
    participant SYS as A-SYS-01 (TinyTask API)
    M->>SYS: Click "New Project", enter name + optional description/template
    SYS->>SYS: Validate name uniqueness within workspace
    SYS->>SYS: Create project record (workspace_id scoped), log event
    SYS-->>M: Project created
```

## §8 — Use-Case — {UC-21} Create Task

```mermaid
sequenceDiagram
    participant M as A-MEMBER-01 (Member)
    participant SYS as A-SYS-01 (TinyTask API)
    M->>SYS: Click "New Task", enter title/description/due date/assignee
    SYS->>SYS: Validate title length + due-date format
    SYS->>SYS: Persist task (project_id scoped, workspace_id tenant boundary)
    SYS-->>M: Notify assignee in-app + email (UC-26), log event
```

## §9 — Use-Case — {UC-22} Assign Task

```mermaid
sequenceDiagram
    participant M as A-MEMBER-01 (Member)
    participant SYS as A-SYS-01 (TinyTask API)
    M->>SYS: Select assignee from project-member picker, click "Assign"
    SYS->>SYS: Validate assignee is member of the task's project
    SYS->>SYS: Update task.assignee_id, notify assignee (UC-26)
    SYS-->>M: Assignment recorded, event logged
```

## §10 — Use-Case — {UC-23} Change Task Status & Due Date

```mermaid
sequenceDiagram
    participant M as A-MEMBER-01 (Member)
    participant SYS as A-SYS-01 (TinyTask API)
    M->>SYS: Move card on board, or edit due date
    SYS->>SYS: Validate transition + due-date rule
    SYS->>SYS: Persist change, emit activity event, log
    SYS-->>M: Task reflects new state
```

## §11 — Use-Case — {UC-24} View Project Board (Kanban)

```mermaid
sequenceDiagram
    participant M as A-MEMBER-01 (Member)
    participant SYS as A-SYS-01 (TinyTask API)
    M->>SYS: Open project
    SYS->>SYS: Query tasks filtered by workspace_id + project_id
    SYS-->>M: Render columns by status
    M->>SYS: Optional real-time sync via websockets (Mobile + Web)
```

## §12 — Use-Case — {UC-25} Comment on Task

```mermaid
sequenceDiagram
    participant M as A-MEMBER-01 (Member)
    participant SYS as A-SYS-01 (TinyTask API)
    M->>SYS: Submit comment (Markdown subset)
    SYS->>SYS: Validate length (<= 10 000 chars), sanitise HTML
    SYS->>SYS: Persist comment (task_id scoped)
    SYS-->>M: Notify watchers (UC-26), log event
```

## §13 — Use-Case — {UC-26} @Mention & In-App Notification

```mermaid
sequenceDiagram
    participant M as A-MEMBER-01 (Author)
    participant SYS as A-SYS-01 (TinyTask API)
    participant T as Mentioned member
    M->>SYS: Save comment/description containing @username
    SYS->>SYS: Parse mentions, validate project membership
    SYS->>T: Create in-app notification rows per mention
    SYS->>T: Send email digest (batched <= 5 min) per preferences
```

## §14 — Use-Case — {UC-27} Attach File to Task

```mermaid
sequenceDiagram
    participant M as A-MEMBER-01 (Member)
    participant SYS as A-SYS-01 (TinyTask API)
    M->>SYS: Drag file into task
    SYS->>SYS: Validate size (<= 25 MB) + MIME allowlist, AV scan (ClamAV)
    SYS->>SYS: Upload to object storage (workspace-scoped prefix, SSE via KMS)
    SYS-->>M: Attachment record created (task_id + storage key), event logged
```

## §15 — Use-Case — {UC-28} Search & Filter Tasks

```mermaid
sequenceDiagram
    participant M as A-MEMBER-01 (Member)
    participant SYS as A-SYS-01 (TinyTask API)
    M->>SYS: Enter query / apply filter (assignee, status, due date, tag)
    SYS->>SYS: Build query scoped to user's workspaces + projects, full-text match
    SYS-->>M: Paginated results ordered by relevance
    SYS->>SYS: Log query metadata only (no body content)
```

## §16 — Use-Case — {UC-29} Activity Feed (recent events)

```mermaid
sequenceDiagram
    participant M as A-MEMBER-01 (Member)
    participant SYS as A-SYS-01 (TinyTask API)
    M->>SYS: Open dashboard
    SYS->>SYS: Query recent events scoped to accessible projects
    SYS-->>M: Render last 50 events (timestamp + actor + action)
```

## §17 — Use-Case — {UC-30} Mobile Sync (offline-first)

```mermaid
sequenceDiagram
    participant M as A-MOB-01 (Mobile Client)
    participant SYS as A-SYS-01 (TinyTask API)
    M->>SYS: Upload queued mutations
    SYS->>SYS: Validate workspace_id scope, persist
    SYS-->>M: Return canonical state version
    M->>SYS: Pull newer server events via /sync
```

## §18 — Use-Case — {UC-31} Stripe Checkout (Upgrade Plan)

```mermaid
sequenceDiagram
    participant U as A-FREE-01 / A-WSADM-01
    participant SYS as A-SYS-01 (TinyTask API)
    participant STR as A-EXT-01 (Stripe Checkout)
    U->>SYS: Click "Upgrade"
    SYS->>STR: Create Checkout Session (workspace_id metadata)
    STR-->>U: Hosted payment page (no PAN to TinyTask)
    STR->>SYS: Signed webhook posts to /webhooks/stripe
    SYS->>SYS: Verify signature, update workspace.plan = paid, log
```

## §19 — Use-Case — {UC-32} Workspace Admin Console

```mermaid
sequenceDiagram
    participant ADM as A-WSADM-01 (Workspace Admin)
    participant SYS as A-SYS-01 (TinyTask API)
    ADM->>SYS: Open workspace settings
    SYS-->>ADM: Render membership list, roles, billing summary, audit filter
    ADM->>SYS: Perform action (invite UC-18 / role / remove / usage)
    SYS->>SYS: Apply action, log it
```

## §20 — Use-Case — {UC-33} Enterprise SSO

```mermaid
sequenceDiagram
    participant ENT as A-ENTADM-01 (Enterprise Admin)
    participant SYS as A-SYS-01 (TinyTask API)
    participant IdP as A-EXT-02 (Auth0 IdP)
    ENT->>SYS: Upload SAML/OIDC metadata
    SYS->>SYS: Validate signature, store IdP config per enterprise tenant
    ENT->>IdP: Members land on SSO login by default (UC-15 extension)
    SYS-->>ENT: SSO login audit trail visible
```

## §21 — Use-Case — {UC-34} View My Account (data held)

```mermaid
sequenceDiagram
    participant M as A-MEMBER-01 (Member)
    participant SYS as A-SYS-01 (TinyTask API)
    M->>SYS: Open account page
    SYS-->>M: List data categories (profile, account activity, workspace memberships)
    M->>SYS: Read-only view
    SYS->>SYS: Audit log entry
```

## §22 — Use-Case — {UC-35} Export My Data (GDPR portability)

```mermaid
sequenceDiagram
    participant M as A-MEMBER-01 (Member)
    participant SYS as A-SYS-01 (TinyTask API)
    M->>SYS: Click "Export my data"
    SYS->>SYS: Generate JSON archive (profile, workspaces, tasks, comments, attachment metadata)
    SYS->>SYS: Signed download URL (24h expiry), email link, log event
    SYS-->>M: Download archive
```

## §23 — Use-Case — {UC-36} Delete My Account / Workspace

```mermaid
sequenceDiagram
    participant U as A-FREE-01 / A-WSADM-01
    participant SYS as A-SYS-01 (TinyTask API)
    U->>SYS: Click delete, type confirmation phrase
    SYS->>SYS: Schedule deletion (immediate account / 30-day grace workspace)
    SYS-->>U: Confirmation email with cancel link (within grace)
    SYS->>SYS: After grace — cryptographic erasure primary + backup (UC-01)
    SYS->>SYS: Log the event
```

