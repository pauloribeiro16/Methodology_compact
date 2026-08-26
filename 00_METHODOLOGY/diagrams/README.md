# AEGIS Diagrams

This is where all the visual diagrams for the AEGIS methodology live.

We have two kinds of diagrams that complement each other:

- **Class diagrams** (`Class_Models/`) answer "what entities exist and how do they relate?" Think of them as a map of the territory.
- **Flow diagrams** (`fluxdiagram/`) answer "what happens, step by step, when you run a phase?" Think of them as the driving directions.

Both are organised by phase (Phase 1, 2, 3), and both use the [Mermaid](https://mermaid.js.org/) format so they render directly on GitHub, GitLab, and VS Code without any extra tooling.

---

## Folder Layout

```
diagrams/
├── Class_Models/                # Static structure — what exists
│   ├── phase1_contextual_definition.md
│   ├── phase2_elaboration_secure_design.md
│   ├── phase3_decomposition.md
│   └── phase3_risk_analysis.md
└── fluxdiagram/                 # Dynamic behaviour — what happens
    ├── phase1_contextual_definition.md        # Phase 1 overview
    ├── phase1/                                # Phase 1 detailed sub-phase flows (12 files: phase1a/1b/1c + filter1/2 + lanes + proportionality + state machines)
    │   └── phase1a_context_capture.md         # 1A — full decision trees + blocks
    ├── phase2/                                # Phase 2 detailed flows (9 files)
    └── phase3/                                # Phase 3 detailed flows (8 files)
```

---

## Why Two Families?

We initially only had class diagrams. They were great for understanding the data model — which entities exist, what attributes they have, how they connect. But when we tried to use them to explain the *process* of running a phase, they fell short. A class diagram shows you that `CompanyContext` feeds into `ComplianceContext`, but it doesn't show you the decision logic, the branching, or the conditional steps that happen along the way.

So we created flow diagrams as a companion. They live side-by-side with the class diagrams, organised by the same phases, but they capture a completely different perspective.

**Phase 1 architecture (v1.1, 2026-07-13).** Phase 1 uses the 3-filter pruning model ([`./fluxdiagram/phase1/phase1_contextual_definition.md`](./fluxdiagram/phase1/phase1_contextual_definition.md)): Filter 1 (applicability), Filter 2 (domain relevance), Filter 3 (conditional extensions). The 38 sub-domains are independent generation lanes ([`./fluxdiagram/phase1/subdomain_lanes.md`](./fluxdiagram/phase1/subdomain_lanes.md)) that converge at Doc 07 + Doc 07b (Track B proportionality, validated by GATE-P — [`./fluxdiagram/phase1/phase1c_proportionality_synthesis.md`](./fluxdiagram/phase1/phase1c_proportionality_synthesis.md)).

---

## How We Got Here

On 15 June 2026, we restructured this directory. Previously, the class diagrams lived directly under `00_METHODOLOGY/Class_Models/`. We moved them into this new `diagrams/` folder and added `fluxdiagram/` as a sibling. The key decisions we made:

1. **Class diagrams and flow diagrams are at different abstraction levels** — a flow diagram doesn't have to mirror the class diagram structure. It captures the *process*, which is something the class diagram can't express well.

2. **Decision trees for the 5 EU regulations are shown as a single block** in the main flow diagram, with an optional sub-diagram for detail. Five parallel branches in one diagram would be unreadable.

3. **The 8 conditional question blocks (B1-B8) are a matrix lookup**, not 8 individual decision diamonds. The triggers are simple enough that a lookup table is clearer.

4. **Confidence checks (Section 6.1 of the intake form) happen in the background** — they're a quality gate, not something that changes the flow path.

5. **Progressive disclosure** — the overview flow diagram collapses dynamic elements into summary nodes. Detailed diagrams in `fluxdiagram/phase1/` expand them to full granularity (every decision point, every block trigger).

6. **Doc 07 is the convergence point** — it pulls from Docs 04, 05, 06 and generates 4+ new analyses (overlap calculation, complementarity opportunities, conflict classification, compound event scenarios). No iterative loops between documents.

7. **The same flow works for all 3 cases** (Case 01, 02, 03). The structure is identical; only the volume scales (1-5 regulations, 0-10 overlap pairs).

The full technical decision log is in [`fluxdiagram/README.md`](./fluxdiagram/README.md).

---

## Viewing the Diagrams

The easiest ways to view Mermaid diagrams:

- **GitHub / GitLab:** they render automatically when you open the `.md` file
- **VS Code:** install the "Markdown Preview Mermaid Support" extension
- **Browser:** paste the Mermaid code block into [mermaid.live](https://mermaid.live/)

---

## Adding a New Diagram

1. Figure out if it's a class diagram (structure) or a flow diagram (process)
2. Put it in the right folder, named `phase{N}_{purpose}.md`
3. Add it to the folder layout above
4. If there's a companion diagram in the other family, cross-reference it

---

**Questions?** Check the scoped [`../AGENTS.md`](../AGENTS.md) for agent-specific rules, or the root [`../../AGENTS.md`](../../AGENTS.md) for the full methodology orchestration protocol.
