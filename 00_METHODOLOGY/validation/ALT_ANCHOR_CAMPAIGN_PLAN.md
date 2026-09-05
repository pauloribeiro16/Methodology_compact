# Campaign Plan — ALT-ANCHOR (death of UNMAPPED + multi-referential anchoring)

> **Status ledger.** This file is the durable execution plan for the ALT-ANCHOR campaign,
> kept on disk so no decision is lost between sessions. Update the checklist + status
> block at every phase boundary. Human decisions are FINAL (P7) — never re-litigate.

**Created:** 2026-09-05 · **Orchestrator:** ZCode session · **Branch:** master
**Predecessor campaign:** Realization Class (commit `2948fb8`, same day) — provides the
`realization_class` attribute this campaign routes on.

---

## 1. Locked human decisions (2026-09-05, FINAL)

1. **`UNMAPPED_*` marker family is RETIRED.** Replacement: `ALT-ANCHOR (ref1; ref2; …)` —
   rule element with no PF/CSF subcategory but covered by a sibling referential.
   Terminal state `ALT-ANCHOR (NO-ANALOGUE)` when no referential in the set covers it.
   Never force an anchor. NO-ANALOGUE items go to the P7 human queue.
2. **Anchor referential set (frozen):** NIST SP 800-53r5 · NIST SSDF (SP 800-218) ·
   OWASP ASVS 4.0.3 · OWASP SAMM v2 · ISO 27002:2022 (last resort; crosswalk already in
   `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` §7).
   Class alignment: ASVS→TECHNOLOGY · SAMM→PROCESS/CAPABILITY (SAMM level ties to
   maturity model v1.6 Scale A) · 800-53r5/SSDF→all classes.
3. **Full 800-53 materialisation:** every PF/CSF row in the 3 framework-mapping matrices
   gains a 800-53r5 column with content taken from the existing PF JSON crosswalks
   (`related_refs` / "NIST SP 800-53 Rev. 5: …"). Anti-drift = mechanical: a generator
   script is the only writer; JSONs stay the single source; re-runs are idempotent.
   (User chose "matriz completa" over "só residuais" knowing the drift trade-off.)
4. **Orphans are in scope:** C3 (10 orphan obligations), C2 (14 PO/40 SO without
   objective) — per-ID verdict LEGIT / MITIGADO / GAP; real GAPs → P7 queue.
5. Context (same day): Realization Class campaign = documents-only;
   `phase2_ontology.yaml`, dashboards, `data/` mirrors, KG reflection remain DEFERRED
   (user decision; Executor re-restored the ontology once and was reverted 2× — do not
   touch ontologies in this campaign either).

## 2. Scope of writes

- **Rename** UNMAPPED→ALT-ANCHOR wherever live occurrences exist:
  C1: Doc16 (9: 8 PF + 1 CSF), Doc18 (13), Doc19 (~31 incl. notes/Anexo);
  C2: Doc18 (~9), Doc19 (~22), **03_PHASE3_DECOMPOSITION/NIST_ANCHORS.md (8)**;
  C3: Doc19/Doc20 (~14 cells + adjacents), **03_PHASE3_DECOMPOSITION/NIST_ANCHORS.md**.
  NIST_ANCHORS.md refresh was already a pending item — folded in here.
- **800-53r5 column: matrix docs only** — C1 `Doc19_Framework_Mapping_Matrix.md`,
  C2 `Doc19_Framework_Mapping_Matrix.md`, C3 `Doc20_Framework_Mapping_Matrix.md`.
  Cards, xlsx (stale-bannered), mirrors, dashboards, ontologies: untouched.
- Frozen corpus `domains/**` untouched (guard-protected). No commits without gates.

## 3. Phases

### Fase 0 — Census (dedup to element level) — IN PROGRESS
- [x] C1 raw occurrence extraction (Doc16/18/19 lines mapped)
- [x] C1 element table — 52 raw → 12 canonical elements; written to `ALT_ANCHOR_CENSUS_v0.md`
- [x] C2 element table — 8 canonical elements (7 PF + 1 CSF)
- [x] C3 element table — 9 canonical elements (C2 family + CI/CD pipeline security)
- [x] Census file complete: `00_METHODOLOGY/validation/ALT_ANCHOR_CENSUS_v0.md` (C1 12 + C2 8 + C3 9 elements)
- Anchor proposals per element use rule-card content + PF JSON crosswalks +
  realization_class routing. Expected NO-ANALOGUE candidates: GDPR data portability
  (CR-D-05.4 family), positive-risk (GV.RM-04), identity assertions, stakeholder
  expectations (BPR-D-10.3-002 cluster).

### Fase 1 — Frozen referential sources — PENDING
- [ ] `CONTROLS/NIST_80053R5/` (id+name; minimum = all controls referenced by PF JSON
      crosswalks + base controls of families AC AT AU CA CM CP IA IR MA MP PE PL PM PS
      PT RA SA SC SI SR)
- [ ] `CONTROLS/NIST_SSDF/` (SP 800-218 v1.1, PO/PS/PW/RV ~42 tasks)
- [ ] `CONTROLS/OWASP_ASVS/` (ASVS 4.0.3, V1–V14 at V*.x.y, ~285)
- [ ] `CONTROLS/OWASP_SAMM/` (v2: 6 functions, 15 practices, 30 streams FF-SL, levels 1-3)
- [ ] `CONTROLS/NIST_CSF_2.0/` (106 subcategories — un-WARNs the C2/C3 gates)
- [ ] `_MANIFEST.json` per dir (source URLs, version, date, count, UNVERIFIED flags)
- Every entry web-verified; anything unverifiable flagged UNVERIFIED, never omitted silently.

### Fase 2 — Central spec + generator — PENDING
- [ ] `00_METHODOLOGY/ALT_ANCHOR_CRITERION.md`: vocabulary (ALT-ANCHOR / NO-ANALOGUE),
      per-class anchor hierarchy (TECHNOLOGY: 800-53→SSDF→ASVS; PROCESS: 800-53→SAMM;
      CAPABILITY: SAMM→800-53 PL/GOVERN→ISO 27002 last resort), dedup rule
      (1 decision per rule-element), generator contract, marker migration table
      (UNMAPPED_PF→ALT-ANCHOR etc.). 3 case SPECs point here.
- [ ] `scripts/build_alt_anchor_columns.py` (repo root): injects/updates the 800-53r5
      column in the 3 matrices from PF JSONs; idempotent; aborts on unknown id.

### Fase 3 — Write-back per case (one at a time, gate between) — PENDING
- [ ] C1 (Doc16/18/19 + matrix column) → gate v0.4 PASS
- [ ] C2 (Doc18/19 + NIST_ANCHORS.md + matrix column) → gate v0.4 PASS
- [ ] C3 (Doc19/20 + NIST_ANCHORS.md + matrix column) → gate v0.4 PASS
- Gate changes (all 3): `UNMAPPED_` forbidden in live docs; every ALT-ANCHOR must carry
  anchors validated against frozen lists; CSF hard-check via NIST_CSF_2.0.
- Validator: independent re-adjudication of ≥25% of residual anchors; divergences by
  deliberation (P4); report in `validation/`.

### Fase 4 — Orphans inventory — PENDING
- [ ] C3: 10 orphan obligations — verdict per ID: LEGIT / MITIGADO (BPR covers) / GAP
- [ ] C2: 14 PO + 40 SO without objective — same verdicts
- Real GAPs → P7 queue in PROJECT_STATE + GLOBAL.

### Fase 5 — Gates + bookkeeping + commits — PENDING
- [ ] 3× gates PASS · PROJECT_STATE ×3 + GLOBAL + CHANGE_LOG_CENTRAL
- [ ] Commits per unit: (a) methodology + frozen sources; (b) C1; (c) C2; (d) C3; (e) orphans

## 4. Acceptance criteria

- `grep -r "UNMAPPED_"` over the 3 cases = 0 in live docs (historical reports exempt).
- 100% of ALT-ANCHOR occurrences carry anchors validated against frozen lists.
- 800-53r5 column present on 100% of PF/CSF rows of the 3 matrices; generator re-run = zero diff.
- 4 new referential dirs + CSF 2.0, all web-verified with manifests.
- 3× gates PASS · orphans inventory complete with per-ID verdicts.

## 5. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Drift JSON↔docs (user accepted the trade-off of full materialisation) | generator is single writer; idempotent re-run promoted to gate check |
| False anchors | web-verified lists; Validator re-adjudication of ≥25%; NO-ANALOGUE as honest terminal |
| Volume (~900+ cells) | script does the bulk; human/agent decisions only on ~40 residual elements |
| Concurrency limits on subagents | execute in-conversation, agent-by-agent when possible; this file is the memory |

## 6. Execution log

- 2026-09-05: campaign approved (plan v3). Fase 0 started in-conversation: C1 raw census
  extracted (Doc19 cells L77–108, L1242–1285; Doc16 L133–1874; Doc18 L179–3470).
  Subagent dispatch blocked by model concurrency limits — work continues in-conversation.
- 2026-09-05 (2): durable ledgers created at user request — this plan file +
  `02_CASES/PENDING_CAMPAIGNS_LEDGER.md` (ALL open campaigns: ALT-ANCHOR in execution,
  Realization-Class deferred items, Phase 3 product-first remainder, PORT-PARITY-2 parked
  fix wave, P7 queue, dormant items).
- 2026-09-05 (3): Fase 0 COMPLETE — all 3 cases deduplicated in-conversation →
  `ALT_ANCHOR_CENSUS_v0.md`: C1 52→12 elements; C2 →8 elements; C3 →9 elements (+CI/CD).
  Shared gap family confirmed across cases (patch/OTA, MFA, backup/DR, portability,
  boundary, secure-SDLC, board-training, compliance-testing). Next: Fase 1 frozen sources.
