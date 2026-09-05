# phase2_ontology.yaml — History (Case_02)

**Purpose:** document the timeline of this file so future campaigns understand why
realization_class is NOT present here even though the Realization Class rubric
(`00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` v1.2) is in force.

## Timeline

| Date | Commit | Event |
|---|---|---|
| 2026-09-04 | `468c500` (PORT-PARITY-2 F4) | File **created** as part of the C2 P2 wave (28 controls → phase2_ontology v1.0, build_p2_graph 278n/356l, 0 orphan OBL). |
| 2026-09-05 | `2948fb8` (Realization Class) | Rubric v1.2 published + Case_01 tag wave committed. **Freeze on ontology modifications begins here for Case_01** (no new commits touching Case_01 phase2_ontology.yaml). |
| 2026-09-05 | `b5ec03a` / `5a681c9` | ALT-ANCHOR methodology + Case_01. **No ontology modifications in C2.** |
| 2026-09-05 | `66d0373` | ALT-ANCHOR Case_02: Doc19 / control_set / check_unmapped.py touched; **phase2_ontology.yaml untouched**. |
| 2026-09-05 | `387695d` | ALT-ANCHOR Case_03 — same posture for C3. |

## Proof — no realization_class in this file

```
$ grep -c "realization_class\\|RealizationClass" phase2_ontology.yaml
0
```

The C2 ontology predates the Realization Class rubric by one day. The freeze started
at `2948fb8` and has been respected retroactively: the file was created for a
different purpose (C2 P2 wave migration to ontology graph, AUD-P2-005 0 orphan OBL)
and was never updated to carry the rubric's enum. Adding `RealizationClass` to it is
deferred until a future campaign reopens the ontology modification freeze (P7).

## What this means

- The **freeze on phase2_ontology.yaml modifications is intact** post-`2948fb8`.
- No retroactive action is required: the C2 ontology does not claim any
  `realization_class` mapping that would conflict with the rubric.
- The C2 tag wave (55 rules pending the future Realization Class propagation) will
  land elsewhere (likely in `control_set.yaml` mirroring Case_01).
