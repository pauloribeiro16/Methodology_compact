# 02 — Card Template (Cockburn + AEGIS Bike4All RUP 10 + §10 Annex)

Two templates matter for AEGIS Phase 3 use case cards. The Cockburn
fully-dressed template is the **industry reference**; the AEGIS Bike4All
RUP 10-section template is the **house convention** that adds the
Security & Compliance Annex (§10) — non-negotiable in AEGIS.

## §A Cockburn Fully-Dressed Template (Wikipedia *Use case*)

Use this when authoring a generic use case (no AEGIS context) or when
comparing AEGIS cards against industry expectations:

| Field | Content |
|---|---|
| **Title** | Active-verb goal phrase of the primary actor. |
| **Primary Actor** | The role that initiates the use case. |
| **Goal in Context** | Where this use case fits in the bigger picture. |
| **Scope** | What is being designed — Organization, System, or Component. |
| **Level** | Goal level — Summary (+), User Goal (default), Subfunction (−). |
| **Stakeholders and Interests** | Every party that cares and *what* each cares about. |
| **Precondition** | What must be true before the use case starts. |
| **Minimal Guarantees** | What the system guarantees even if the goal is not achieved. |
| **Success Guarantees** | State of the system once the goal is achieved (postcondition on success). |
| **Trigger** | The event that starts the use case. |
| **Main Success Scenario** | Numbered list; one actor intention per step. |
| **Extensions** | Numbered alternative/exceptional paths anchored to specific MSS steps. |
| **Technology & Data Variations List** | Optional; e.g. "1a. System may authenticate via LDAP or local DB." |

Cockburn's **casual** template is acceptable for early-phase or lightweight
artefacts: Title + Primary Actor + Scope + Level + Story (a paragraph).

## §B AEGIS Bike4All RUP 10-Section Template (canonical)

Authoritative source: `Methodology-main/03_REFERENCE_MATERIAL/P3_E2_Requirement_Analysis_Bike4All_Maintenance_platform_v1r2.md`
(does not live in the compact repo; link upstream). The 10 sections:

| § | Section | What goes in |
|---|---|---|
| 1 | Brief Description | One-paragraph summary of the goal and its value to the primary actor. |
| 2 | Actors | Numbered sub-items — `2.1 Primary`, `2.2 System`, `2.3 Stakeholder`, … |
| 3 | Preconditions | State the system must be in before the use case starts. |
| 4 | Basic Flow of Events | Numbered steps; followed by the card's embedded sequence diagram (derived verbatim copy; editable source: `annexes/B_Sequence_Diagrams.md` §N). |
| 5 | Alternative Flows | Subitems `5.1 <Alternate flow: …>`, `5.2 …`; each opens with `Trigger:`. |
| 6 | Subflows | Subitems `6.1 <Subflow: …>`, `6.2 …` — reusable fragments shared via `<<include>>`. |
| 7 | Key Scenarios | Subitems `7.1 <Scenario: …>` — concrete instances that justify the card. |
| 8 | Post-conditions | Numbered — state the system is in after the goal is achieved (or after each alternative). |
| 9 | Special Requirements | FURPS+ — Functional / Usability / Reliability / Performance / Supportability. |
| 10 | **Security & Compliance Annex (AEGIS)** | See §C below — non-negotiable. |

A card that drops a section without justification is incomplete. If a section
genuinely does not apply (e.g. an integration adapter has no UX concerns),
document the deviation in §10 instead of leaving the section blank.

## §C §10 Security & Compliance Annex (AEGIS) — Schema

Fixed fields. Any UC card missing one of these is **incomplete**:

| Field | Format | Example |
|---|---|---|
| **Provenance** | `[ATTESTED] Source: <DocNN §N>` or `[ASSUMED]` | `[ATTESTED] Source: Doc12 §4` |
| **Constrained by** | comma-separated `UC-*` / `PROC-*` ids | `UC-12, PROC-04` |
| **Rules / NFR** | comma-separated `RULE-*` / `NFR-*` ids | `NFR-D-04.1-012` |
| **Threats addressed** | comma-separated `MUC-*` ids | `MUC-07` |
| **NIST anchors** | `PR.AA-NN` style ids (NIST CSF 2.0 / PF / AI RMF) | `PR.AA-01, PR.AA-03` |

**Provenance tagging is the AEGIS audit hinge.** `[ATTESTED]` cards carry a
real citation in the methodology corpus; `[ASSUMED]` cards are flagged for
later review. A card with no Provenance marker fails audit (rubric §5C +
Doc20 §2).

## §D Worked Example — UC-14 Register Account (Case_01 Doc20 §2.1)

Excerpt from the canonical exemplar:

```markdown
### UC-14 — Register Account

**§1 Brief Description**
The customer registers a new account on the TinyTask platform.

**§2 Actors**
- 2.1 Primary: Customer (unauthenticated visitor).
- 2.2 Supporting: Email-verification service («external worker»).

**§3 Preconditions**
Customer has a valid email address; not currently logged in.

**§4 Basic Flow of Events**
1. Customer opens the registration page.
2. Customer submits email and chosen password.
3. System validates the input (format, uniqueness).
4. System creates the account and dispatches a verification email.
5. Customer clicks the verification link.
6. System marks the account as active.
**Sequence diagram** (derived copy — editable source: Annex B §14).

**§5 Alternative Flows**
- 5.1 *Email already in use.* Trigger: System detects duplicate. Step 3a:
  System displays an inline error and asks the customer to recover the
  existing account instead.

**§8 Post-conditions**
- The customer account exists and is active.
- A `customer.registered` audit event is recorded.

**§9 Special Requirements (FURPS+)**
- Performance: account creation completes in <2 s at p95.
- Reliability: verification email is dispatched within 30 s; retries on
  transient SMTP failure up to 3 times.

**§10 Security & Compliance Annex (AEGIS)**
- **Provenance:** [ATTESTED] Source: Doc12 §4.
- **Constrained by:** UC-12 (authentication session).
- **Rules / NFR:** NFR-D-04.1-012 (password complexity), NFR-D-04.1-013
  (verification email).
- **Threats addressed:** MUC-07 (account enumeration via /register).
- **NIST anchors:** PR.AA-01, PR.AA-03.
```

Note: §6 (Subflows) and §7 (Key Scenarios) are omitted in this excerpt
because the card genuinely does not use them — but the omission is *visible*
in the document, not silent. A complete card that uses subflows would render
them as `6.1 <Subflow: …>` blocks.

## §E When to Use Cockburn vs Bike4All

| Situation | Template |
|---|---|
| AEGIS Phase 3 deliverable (Doc20/21/22, Doc31/32) | **Bike4All RUP 10** — §10 is required. |
| Standalone use case for a stakeholder briefing | Cockburn casual or fully-dressed — adapt §10 if compliance attaches. |
| Industry / academic write-up | Cockburn fully-dressed — AEGIS §10 is optional. |
| Cross-methodology comparison | Render **both** side by side; flag deltas in §10. |

Never mix sections from the two templates inside the same card — the result
is unreadable and fails audit.
