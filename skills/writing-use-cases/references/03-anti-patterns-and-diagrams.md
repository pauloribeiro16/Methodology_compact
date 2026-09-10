# 03 — Anti-Patterns, Diagrams, Triage

Two halves: a catalogue of anti-patterns that fail audit, and the AEGIS
diagram rules (PlantUML use case diagrams in annex A, Mermaid sequence
diagrams in annex B) plus a triage checklist for reviewing a UC card
before commit.

## §A Anti-Pattern Catalogue (10 violations)

Each entry: name · what it looks like · why it fails · how to fix.

### A1 — CRUD-as-Use-Case

**Looks like:** `Create Customer`, `Read Customer`, `Update Customer`,
`Delete Customer` modelled as four UCs.
**Why it fails:** Use cases express **user goals**, not database operations.
The CRUD primitives are subfunctions (Fish level), not user-goal UCs.
**Fix:** Name the use case after the goal the actor can articulate —
`Register Customer`, `Correct Customer Address`, `Close Customer Account`.
Let the data operations live inside the scenario steps.

### A2 — Function Decomposition

**Looks like:** `Validate Form`, `Save Record`, `Log Transaction`,
`Send Email` modelled as use cases.
**Why it fails:** This is a procedure manual, not a goal-driven model. Each
step in a Main Success Scenario is one actor intention, not a UI or storage
operation.
**Fix:** Demote to subfunctions (Fish level), reachable via `<<include>>`
from a parent user-goal use case.

### A3 — Missing Primary Actor

**Looks like:** A use case with no actor, or with "the system" or "the
database" listed as the actor.
**Why it fails:** Use cases without actors are orphaned requirements;
"the system" as actor is a contradiction (use cases describe behaviour
toward external observers).
**Fix:** Name exactly one **primary actor** (a role) and zero or more
**supporting actors** (other systems, clocks). If you cannot name the
primary actor, you have a subfunction — demote.

### A4 — Wrong Granularity (Too High or Too Low)

**Looks like:** `Manage Customer Relationship` (Summary, too vague) or
`Validate Email Format` (Subfunction, too small).
**Why it fails:** Too-high UCs cannot scope a feature; too-low UCs become
procedures.
**Fix:** Default to **sea level** (User Goal). Promote to Summary only for
executive overview; demote to Subfunction only when reused across UCs via
`<<include>>`.

### A5 — Bad Naming (Noun-Verb-Noun, Gerunds, Vague Verbs)

**Looks like:** `Customer Management`, `Article Processing`, `Handle
Login`.
**Why it fails:** Titles must name the **goal of the primary actor** in
2–5 words. Vague verbs ("handle", "process", "manage") describe no goal.
**Fix:** Active-verb goal phrase — `Register Customer`, `Edit Article`,
`Log In`. Each word earns its place; drop what does not.

### A6 — UI Contamination

**Looks like:** Steps like *"Click the Submit button"*, *"Type the username
in field U1"*, *"Tab to the password field"*.
**Why it fails:** UI details lock the implementation prematurely, bloat the
text, and couple the requirement to one specific interface.
**Fix:** Capture what the actor **wants to achieve**, not which widget they
touch. UI design lives in a separate artefact (wireframes, mockups).

### A7 — Over-Using `<<extend>>`

**Looks like:** `<<extend>>` used as a substitute for any conditional
behaviour; extensions that change the meaning of the base use case.
**Why it fails:** Cockburn himself flagged `<<extend>>` as "ambiguous and
difficult for stakeholders". The base use case should still stand alone.
**Fix:** Use `<<extend>>` only when (a) the extension is **optional** from
the base's perspective, (b) the base stands alone, (c) the extension has a
named trigger condition. Otherwise use Extensions section or `<<include>>`.

### A8 — Use Case as Diagram Only

**Looks like:** A diagram delivered with no prose; one-line use cases.
**Why it fails:** The diagram is the **table of contents**, not the
content. Larman: "Use cases are not diagrams, they are text."
**Fix:** Every use case has a card — at minimum §1, §2, §3, §4, §8, §10
for AEGIS. Casual template is acceptable for early-phase cards but never
diagram-only.

### A9 — Driving Design Too Literally

**Looks like:** Use cases being treated as a literal blueprint for object
design — every step becoming a class method.
**Why it fails:** Use cases describe **observable behaviour at the system
boundary**, not internal structure. Object design has its own discipline.
**Fix:** Map use cases to C4 components, not classes. Use sequence
diagrams (annex B) to capture object collaboration, not catalogue cards.

### A10 — NFRs in the Main Success Scenario

**Looks like:** Performance, security, or reliability requirements woven
into the numbered MSS steps.
**Why it fails:** NFRs don't fit the actor-intention pattern. They apply
across many use cases and need a separate audit trail.
**Fix:** Capture NFRs in §9 Special Requirements (FURPS+) and §10 Security
& Compliance Annex; cross-reference the use cases they constrain.

## §B Use Case Diagram Rules (annex A)

Authoritative source: `REALIZATION_CLASS_RUBRIC.md` §5C.5 (human decision
2026-09-05).

- **Notation: native PlantUML** (`@startuml` source block, kept for
  editability) **plus committed rendered SVG** under `annexes/svg/`,
  embedded as a markdown image. Mermaid has no `useCaseDiagram` type in
  any stable release (mermaid-js/mermaid#4628) — do not rely on it.
- **Scope:** one **system-wide** diagram per case, plus one diagram **per
  package**.
- **Actors** come from the catalogue card's Primary Actor and Stakeholders;
  non-human actors carry stereotypes (`«worker»`, `«internal worker»`,
  `«case worker»`, `«entity»` per Machado/RMAC p1 slide 30).
- **Critical Extensions** become `<<include>>` / `<<extend>>` relationships
  on the diagram (don't just sit in §5 prose).
- **UC ovals only.** `PROC-*` / `CAP-*` **never** appear as ovals or actors
  in annex A — their diagrams are the §5C.4 flowcharts in the lane-cards
  doc. Annex A packages are the catalog's UC packages (product plus any
  dedicated compliance-UC package).
- **Catalogue gallery (rubric §5C.5 v1.11, 2026-09-10).** Each catalogue
  embeds the system-wide + per-package diagrams as markdown images
  referencing the same `annexes/svg/` files (`annexes/svg/...`, relative to
  the catalogue) — derived views; edit the annex, then re-embed.

## §C Sequence Diagram Rules (annex B)

Also from §5C.5:

- **Mermaid `sequenceDiagram` only.** Every sequence diagram is authored in
  `annexes/B_Sequence_Diagrams.md` (one section per product UC, ordered by
  id) — the editable source. Catalogue cards embed a verbatim derived copy
  inline (rubric §5C.5 v1.11, 2026-09-10; supersedes the pointer line
  `> **Sequence diagram:** → Annex B §N`).
- **PROC/CAP cards do NOT carry sequence diagrams.** Their diagrams are the
  §5C.4 flowcharts.
- **Render-validated, not structurally checked.** Every Mermaid block must
  pass a **real-render check** (`mermaid.render` via headless browser) —
  structural validation does not catch unsupported diagram types.
- **Gotcha: `;` inside message text.** `;` is a statement separator in
  Mermaid sequence diagrams. Use `,` instead in message/note text.
- **Gotcha: participant named `OFF`.** Collides with the `autonumber off`
  keyword — render error. Use `OFFR` or similar.
- **Quoted or parenthesised participant aliases** are permitted (e.g.
  `participant "Email Service" as ES`).
- **Both diagrams are derived views** of the catalogue cards: when the card
  changes, the diagrams change with it. The card is the source of truth.

## §D Triage Checklist (8 questions, pre-commit)

Run through this before committing a UC card or UC diagram:

1. **Primary actor** — is exactly one named, by role (not person)?
2. **Title** — is it an active-verb goal phrase (2–5 words, no gerund)?
3. **Granularity** — is it sea level (User Goal), unless intentionally a
   Summary or a Subfunction via `<<include>>`?
4. **MSS** — are steps actor intentions, not UI actions?
5. **Extensions** — are they anchored to specific MSS steps and triggered
   by a named condition?
6. **§10 Security & Compliance Annex** — is Provenance tagged
   (`[ATTESTED]` / `[ASSUMED]`), with Constraints, Rules/NFR, Threats, and
   NIST anchors populated?
7. **Diagram placement** — UC ovals only in annex A; sequence diagram in
   annex B; Mermaid blocks render-validated (no `;` gotcha, no `OFF`
   participant)?
8. **Lane separation** — is the UC lane-pure (UC-* only, no PROC/CAP
   mixing)? Cross-check rubric §5B and the per-case catalog §2.

A "no" on any of the 8 means the card is **not ready to commit**. Fix
before commit; do not defer with TODOs.

## §E Quick Reference — Diagram Decision Tree

```
Need a diagram of system behaviour at the boundary?
├── Yes, scope the system → use case diagram → annex A → PlantUML + SVG
├── Yes, detail one scenario's messages → sequence diagram → annex B → Mermaid
├── Yes, model internal workflow → flowchart TD → §5C.4 lane-card doc
├── Yes, aggregate capabilities → graph LR → §5C.4 lane-card doc
└── No (just structure) → class diagram → separate artefact
```
