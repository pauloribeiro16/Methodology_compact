# phase2_ontology.yaml — History (Case_03)

**Purpose:** document the timeline of this file so future campaigns understand why
realization_class is NOT present here even though the Realization Class rubric
(`00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` v1.2) is in force.

## Timeline

| Date | Commit | Event |
|---|---|---|
| 2026-09-04 | `491cf74` (PORT-PARITY-2 F4) | File **created** as part of the C3 P2 wave (control_set canonical at P2 root, build_p2_graph 242n/340l, AUD-P2-005b 10 orphan OBL — 9 MITIGADO, 1 GAP → P7). |
| 2026-09-05 | `2948fb8` (Realization Class) | Rubric v1.2 published + Case_01 tag wave committed. **Freeze on ontology modifications begins here for Case_01**; the same date is the convention start for C2/C3. |
| 2026-09-05 | `b5ec03a` / `387695d` | ALT-ANCHOR methodology + Case_03 (Doc14/19/20, control_set, check_unmapped.py). **phase2_ontology.yaml untouched.** |
| 2026-09-05 | `66d0373` | ALT-ANCHOR Case_02 — independent; **C3 ontology untouched**. |

## Proof — no realization_class in this file

```
$ grep -c "realization_class\\|RealizationClass" phase2_ontology.yaml
0
```

The C3 ontology predates the Realization Class rubric by one day. The freeze started
at `2948fb8` and has been respected retroactively: the file was created for a
different purpose (C3 P2 wave migration to ontology graph, AUD-P2-005b orphan audit)
and was never updated to carry the rubric's enum. Adding `RealizationClass` to it is
deferred until a future campaign reopens the ontology modification freeze (P7).

## What this means

- The **freeze on phase2_ontology.yaml modifications is intact** post-`2948fb8`.
- No retroactive action is required: the C3 ontology does not claim any
  `realization_class` mapping that would conflict with the rubric.
- The C3 tag wave (78 rules pending the future Realization Class propagation) will
  land elsewhere (likely in `control_set.yaml` mirroring Case_01).
