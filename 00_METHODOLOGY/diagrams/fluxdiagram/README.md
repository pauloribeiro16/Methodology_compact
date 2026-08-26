# Fluxdiagram — Process Flow Diagrams

This folder contains the flow diagrams for the AEGIS methodology. Each diagram shows the step-by-step process of running a phase — what happens first, what decisions get made, what branches exist, and what documents come out at the end.

The companion class diagrams live in [`../Class_Models/`](../Class_Models/). If you're looking at a flow diagram and wondering "what are the attributes of this entity?" or "what's the type of this relationship?", check the class diagram. If you're looking at a class diagram and wondering "in what order do these entities get created?" or "when does this branch activate?", check the flow diagram.

---

## Directory Structure

```
fluxdiagram/
├── phase1/
│   ├── phase1_contextual_definition.md      Phase 1 overview (all 3 sub-phases)
│   ├── phase1a_context_capture.md           Phase 1A — full decision trees + blocks
│   ├── phase1b_regulatory_mapping.md        Phase 1B — per-reg analysis + clause mapping (2 diagrams)
│   ├── phase1b_nuances_and_reasoning.md     Phase 1B — nuances catalog + LLM spec (reference companion)
│   ├── filter2_domain_relevance.md                Phase 1 — Filter 2 detail (Regulatory Baseline lookup + clause mapping → Doc 06) (NEW v1.1)
│   ├── subdomain_lanes.md                         Phase 1 — per-sub-domain lanes architecture (38 lanes from Regulatory Baseline to GATE-P) (NEW v1.1)
│   ├── phase1c_proportionality_synthesis.md       Phase 1C — Track B proportionality + GATE-P criteria (Doc 07b) (NEW v1.1)
│   ├── phase1c_consolidation.md             Phase 1C — coverage consolidation + synthesis engine (2 diagrams)
│   └── phase1c_synthesis_reference.md       Phase 1C — conflict framework + compound events (reference companion)
├── phase2/
│   ├── phase2_elaboration_secure_design.md       Phase 2 overview (fork-join: obligations → tensions + goals → rules)
│   ├── phase2a_obligation_derivation.md          Phase 2A — clause-to-obligation pipeline + 8 derivation rules
│   ├── phase2b_strategic_tensions.md             Phase 2B — tension detection + classification + resolution
│   ├── phase2b_tension_reference.md              Phase 2B — 7-type catalog + 7 resolution patterns (reference)
│   ├── phase2c_goals_and_rules.md                Phase 2C — goal derivation + rule consolidation + Excel
│   └── phase2c_framework_reference.md            Phase 2C — framework mapping + traceability (reference)
├── phase3/
│   ├── phase3_overview.md                  Phase 3 global overview (entry point — decomposition + threat modeling loop)
│   ├── phase3_decomposition.md              Phase 3A/B overview (iterative cycle + downstream)
│   ├── phase3a_iterative_cycle.md           Phase 3A — iterative UC derivation + 7 convergence criteria
│   ├── phase3b_requirements.md              Phase 3B — architecture mapping + FR/NFR + allocation + gates
│   ├── phase3_risk_analysis.md              Phase 3C overview (parallel frameworks + feedback loop)
│   ├── phase3c_threat_modeling.md           Phase 3C — STRIDE/LINDDUN + risk assessment + mitigation + feedback loop
│   └── phase3c_risk_reference.md            Phase 3C — STRIDE/LINDDUN catalogs + risk matrix + D3FEND mapping
└── README.md                                ← this file
```

**Root level** = phase overviews (one diagram per phase, high-level).
**Subfolders** = detailed sub-phase breakdowns (granular flows for individual stages).

---

## Conventions

All diagrams use Mermaid's `flowchart TD` (top-down) format. Here's what the shapes mean:

| Shape | Meaning |
|-------|---------|
| Rectangle `[...]` | A process step or action |
| Rounded `( ... )` | An input or output document |
| Diamond `{ ... }` | A decision point where the flow branches |
| Cylinder `[( ... )]` | A file or persistent data store |
| Parallelogram `[/ ... /]` | Something a human does manually |
| Double brackets `[[ ... ]]` | A sub-process that expands in another diagram |

---

## Design Decisions

These are the specific choices we made for the flow diagrams. They build on the general decisions in [`../README.md`](../README.md).

**Decision trees as a single block.** Each phase evaluates up to 5 EU regulations (GDPR, CRA, NIS 2, DORA, AI Act). Each one has its own decision tree, but they're all independent — GDPR applicability doesn't depend on CRA applicability. Showing all 5 in parallel on one diagram would be unreadable, so we collapse them into one "Regulatory Applicability Assessment" block. The full branching logic for each tree is available in [`phase1/phase1a_context_capture.md`](phase1/phase1a_context_capture.md).

**Conditional blocks as a matrix lookup.** The intake form has 8 conditional question blocks (B1-B8), each triggered by a simple condition like "AI Act applicable" or "company size >= 50". Rather than drawing 8 decision diamonds, we treat the activation as a single matrix lookup step. The full per-block trigger evaluation with question ranges is detailed in [`phase1/phase1a_context_capture.md`](phase1/phase1a_context_capture.md).

**Confidence check in the background.** Section 6.1 of the intake form compares what the client believes applies versus what the decision trees calculate. This is a useful quality gate, but it doesn't change the flow path — it just flags items for human review. So it stays as a background annotation, not a visible flow element.

**Progressive disclosure.** We don't show all 5 decision trees, all 8 blocks at once. The overview diagram collapses these into summary nodes. The detailed diagrams in `phase1/` expand them fully. A company with 2 applicable regulations sees a simpler diagram than one with 5.

**Doc 07 as the convergence point.** Documents 04, 05, and 06 each have their own purpose — they're not iterative versions of the same thing. Doc 07 is where everything converges and where genuinely new cross-regulation analyses happen (overlap calculation, complementarity, conflict classification, compound events). There are no refinement loops between the documents.

**Excel as an explicit output.** Doc 06 (Clause Mapping Matrix) is generated as an Excel file. It appears as a visible file output node in the flow, not just as a document reference.

**LLM reasoning as explicit nodes.** Phase 1B introduces LLM-assisted reasoning at four specific points (interpretation/derogation identification, rationale generation, strategic implications, gap analysis). These are NOT generic "ask AI" steps — each has a defined purpose, input contract, instruction set, KB requirement, output format, and quality criteria. They appear as amber-coloured nodes with `[LLM-X]` badges referencing spec tables in [`phase1/phase1b_regulatory_mapping.md`](phase1/phase1b_regulatory_mapping.md). The remaining Phase 1B steps (criteria evaluation, classification, NI assignment, clause mapping) are deterministic.

**Nuances as a distinct concern.** Regulatory nuances (classification, interpretation, derogation, threshold) are shown as purple-coloured steps in Phase 1B. They modify how articles apply but do not change the static clause-to-subdomain mapping. The full catalog with all examples from 3 cases is in [`phase1/phase1b_nuances_and_reasoning.md`](phase1/phase1b_nuances_and_reasoning.md).

**Conflict classification as a 3-type taxonomy.** Phase 1C introduces the Synergistic / Structural Tension / Contextual Tension classification for regulatory overlaps. This determines whether an overlap is an efficiency opportunity (implement once), a design decision (unified framework), or a per-event challenge (compound event analysis). The full framework with criteria and resolution patterns is in [`phase1/phase1c_synthesis_reference.md`](phase1/phase1c_synthesis_reference.md).

**Compound events as positive + negative identification.** Phase 1C's LLM-F identifies events that trigger multiple regulations (positive) AND events that look compound but are not (negative). The negative examples demonstrate discrimination ability. The methodology and scaling analysis are in [`phase1/phase1c_synthesis_reference.md`](phase1/phase1c_synthesis_reference.md).

**Internal ontology.** The `phase1_ontology.yaml` file is a machine-readable representation of the entire phase. It's useful for tooling and downstream automation, but it's internal infrastructure — it doesn't appear in the user-facing flow diagram.

**One flow for all cases.** The same diagram works for Case 01 (2 regulations, 8 employees), Case 02 (4 regulations, 450 employees), and Case 03 (5 regulations, 5000+ employees). The structure is identical; only the volume of analysis scales.

**Phase 1 v1.1 architecture (2026-07-13).** Phase 1 was restructured around the 3-filter pruning model defined in [`../../../PHASE1_STRATEGY.md`](../../../PHASE1_STRATEGY.md). The 3 filters are:
- **Filter 1 — Applicability** (was Phase 1A + 1B): 5 decision trees + per-regulation analysis loop. Detail in `phase1/phase1a_context_capture.md` + `phase1/phase1b_regulatory_mapping.md`.
- **Filter 2 — Domain Relevance** (NEW): Regulatory Baseline lookup + scope_overlap computation + clause mapping. Detail in `phase1/filter2_domain_relevance.md`.
- **Filter 3 — Conditional Extensions** (was Phase 1A Diagram 2): 8 block triggers + conditional questions. Embedded in `phase1/phase1a_context_capture.md`.

The 38 sub-domains are now independent **lanes** (detail in `phase1/subdomain_lanes.md`) that converge at Doc 07 + Doc 07b (Track B Proportionality, validated by GATE-P — detail in `phase1/phase1c_proportionality_synthesis.md`).

---

## What to Avoid

- Five decision trees shown in parallel on the main diagram (use the detail diagram instead)
- Eight diamonds for the eight conditional blocks (use the detail diagram instead)
- Iterative loops between Docs 05/06/07 (they are distinct documents, not refinement stages)
- Confidence check as a flow-changing decision point
- Mirroring the class diagram structure (different abstraction level)
- Showing every possible element in one flat diagram

---

**See also:** [`../README.md`](../README.md) for the general diagram directory overview, and [`../Class_Models/README.md`](../Class_Models/README.md) for the companion class diagrams.
