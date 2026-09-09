# 01 — Elicitation Process (RMAC p1 slides 16–46)

This reference encodes the **elicitation workflow** that precedes any use case
card. Authoritative source: *Modelação com UML*, Ricardo J. Machado,
Universidade do Minho, slides p1 (IX-2001), slides 16–46. Translated and
adapted for AEGIS — citation, not duplication.

## §A Requirements Elicitation Discipline (slides 16–19)

- **Interactive, not documentary.** Capture requirements by talking to
  stakeholders, not by reading briefs. Use case diagrams are a working
  artefact, not a deliverable handed down from analysis.
- **Problem terminology, not solution terminology.** User requirements are
  expressed in the user's own vocabulary and from an operational viewpoint.
  System requirements are a consequence — they are derived later.
- **Filter the noise.** Reject generic statements ("it has to be easy to use")
  and solution-biased statements ("I want a relational database"). Both are
  evidence the elicitation drifted.
- **Decouple from design decisions.** The use case diagram does not commit to
  any technology, framework, or storage choice. If a stakeholder proposes one,
  capture the *goal*, not the *mechanism*.

## §B The Onion-Skin Analogy (slides 21–26)

Model the environment around the system in four concentric layers, outer →
inner:

| Layer | Contents | In your scope? |
|---|---|---|
| 1 — Users | Human roles interacting with the system | **Outside** the system boundary; become actors |
| 2 — Sensors / Actuators | Devices that supply or receive signals | Outside (unless the device is being designed) |
| 3 — Interfaces | Other systems the system talks to | Outside (unless you're designing the adapter) |
| 4 — System | The thing being built | **Inside** the system boundary |

**Decision rule** — an object belongs to the system-to-be-built unless any of
the following is true:

1. It is already specified by an existing device interface.
2. It already exists in the captured environment and will not be developed.
3. It supplies or receives information from the system rather than being
   supplied by it (i.e. it is upstream/downstream, not part of it).
4. It is a person monitoring outputs or sending inputs (a user, by definition
   outside).

Apply this rule before drawing the context diagram; it stops the model from
absorbing everything the user mentions.

## §C Context Diagram → Use Case Diagram Ordering (slides 27–37)

1. **Context diagram first.** Model every layer except the outermost as a
   single black box. Capture actors (roles) and their relationships to the
   black box — **no message flows yet**. Capturing messages at this stage is
   premature (slide 32).
2. **One use case diagram per actor.** After actors are stable, draw one use
   case diagram per actor group. Actors are unstable during use case capture
   — that is acceptable; the deck is explicit that "actors are a pretext and
   a means to an end" (slide 37).
3. **Iterate.** Go back to the context diagram as new actors surface from the
   use case capture. The two diagrams co-evolve.

## §D Orthogonal Refinement (slides 44–45)

Use cases can be decomposed into sub-use cases. To keep the diagram
manageable, apply **two or more orthogonal views**:

- **By specialisation** (variants) — one parent UC, several children for
  distinct flows (e.g. "Pay by Card" / "Pay by Cash" generalise "Pay").
- **By decomposition** (subfunctions) — break a complex UC into smaller UCs
  shared by `<<include>>`.

Refine **risk-driven**: the most complex or most regulated functionalities get
the deepest decomposition. Stable, well-understood UCs stay at sea level.

## §E Textual Description (slide 46)

Three acceptable forms for the textual body of a use case:

1. Numbered steps with pre- and post-conditions.
2. Pseudo-code.
3. Activity diagram.

**Recommendation:** in the first pass, write **small informal texts in
natural language**. That keeps the client in the loop and the analyst honest
about what is known. Move to numbered steps with pre/post-conditions only
when the client no longer needs to read the text directly.

AEGIS convention (rubric §5C.5): the textual body always ends with a single
pointer line `> **Sequence diagram:** → Annex B §N` — the prose is the
catalogue card; the sequence diagram is the annex-only view.

## §F Worked Micro-Example — Place Order (slide 40)

The deck's canonical example exercises all three UC-to-UC relationships on one
family:

- **«extend»** — `Request Catalog` extends `Place Order` (base = Place Order).
- **«include»** — `Place Order` includes `Supply Customer Data`, `Order
  Product`, `Arrange Payment`.
- **Generalisation** — `Pay Cash` and `Arrange Credit` generalise `Arrange
  Payment` (parent/child).

When teaching include vs extend, **use this family**: it is the cleanest
single diagram that shows all three relationships without competing for
attention.

## §G Anti-Pattern Specific to This Phase

- **Drawing the use case diagram before the context diagram** — you cannot
  know the actors without scoping the environment first.
- **Treating the onion-skin layers as scope** — the system is *one* layer
  (the innermost). Everything else is environment.
- **Capturing message flows in the context diagram** — premature; wait for
  the use case diagrams to be stable (slide 32).
- **Refining every use case uniformly** — refinement should be risk-driven,
  not exhaustive.
