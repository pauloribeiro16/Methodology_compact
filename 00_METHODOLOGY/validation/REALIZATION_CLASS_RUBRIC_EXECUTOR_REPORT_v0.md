---
document_id: AEGIS-METH-RC-RUBRIC-REPORT-V0
title: Executor Report — Realization Class Rubric v1.0
phase: Cross-phase
version: 0.1
created: 2026-09-05
updated: 2026-09-05
author: Executor
status: ACTIVE
---

# Executor Report — REALIZATION_CLASS_RUBRIC v1.0 (2026-09-05)

## 1. Files created / changed

| File | Action | Notes |
|---|---|---|
| `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` | **CREATED** | 166 lines (target ≤220). Frontmatter 8 fields, `document_id: AEGIS-METHODOLOGY-REALIZATION-CLASS-RUBRIC`, phase Cross-phase, status ACTIVE, author Executor, dates 2026-09-05. §-numbered style matches `IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md`. Contains §1 Purpose, §2 Classes, §3 Decision tree (normative, simple mermaid flowchart), §4 Attribute spec, §5 Class→Lane identity mapping, §6 CAPABILITY anchor, §7 ISO 27002:2022 crosswalk (1 table), §8 Worked examples, §9 Governance + version history. |
| `00_METHODOLOGY/AGENTS.md` | **EDITED** (additive only) | See diff summary §3 below. |
| `00_METHODOLOGY/validation/REALIZATION_CLASS_RUBRIC_EXECUTOR_REPORT_v0.md` | **CREATED** | This report (`validation/` dir newly created). |
| `02_CASES/**` | NOT touched | Constraint respected — Doc18 read-only, exemplar selection only. No tagging performed. |

## 2. Exemplars chosen (9 real Case_01 rules from Doc18, 3 per class)

Quoted as-is (Case_01 uses legacy `CR-`/`BPR-` prefixes, deprecated corr-007; no new deprecated-prefixed IDs introduced).

| Class | Rule | Title | Why it illustrates the class |
|---|---|---|---|
| TECHNOLOGY | `CR-D-01.1-001` | Data at Rest Encryption | Built store encryption + segregated KMS; verification criteria are configuration reports; no recurring judgement. |
| TECHNOLOGY | `CR-D-03.2-001` | Administrative MFA | Enforced at managed-identity privileged routes; automated test rejects missing second factor. |
| TECHNOLOGY | `CR-D-10.2-001` | Audit Logging and Traceability | Built pipeline: multi-region trail, Object Lock, retention config, log-failure alerting. |
| PROCESS | `CR-D-04.3-001` | Dual Regulatory Incident Notification | One notification workflow: trigger decision tree, 24h internal clock, per-recipient submissions, tabletop-tested. |
| PROCESS | `CR-D-05.3-001` | Complete and Secure Data Erasure | Request-to-verified-erasure workflow with 7-day SLA; identity verification + completion register are coordinated activities. |
| PROCESS | `CR-D-02.2-001` | Automated Security Updates and Patch Remediation | **Borderline shown resolved:** automation present but card mandates recurring human review (failed patches, exceptions) → Q1 NO; defined severity-SLA sequence → PROCESS, secondary TECHNOLOGY. |
| CAPABILITY | `CR-D-08.2-001` | Role-Specific Security Competence | Competency matrix + named owners + quarterly review; verified by INSPECT of the standing ability. |
| CAPABILITY | `CR-D-09.1-001` | Security Governance and Technical Documentation | Standing policy architecture: owners, approvals, policies reconciled to operating evidence, 10y retention. |
| CAPABILITY | `CR-D-09.2-001` | Unified Privacy and Cybersecurity Risk Assessment | **Borderline shown resolved:** Q2 looks YES (trigger→analyse→approve sequence) but tie-break applies — human risk-acceptance authority + periodic refresh = standing ability → CAPABILITY primary, PROCESS secondary. |

## 3. corr-008 diff summary (`00_METHODOLOGY/AGENTS.md`)

- **Added** one 5-line paragraph directly after the DEPRECATED-IDs paragraph in "## ID Hierarchy (corr-008)": registers that Phase 2 rules (canonical `RULE-*`; legacy `CR-`/`BPR-` in Case_01) carry mandatory `realization_class` {TECHNOLOGY, PROCESS, CAPABILITY} + optional `realization_class_secondary` (≠ primary), normatively defined in `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md`; states the invariance guarantee (IDs, D-XX.Y spine, catalog structure unchanged).
- **Version block:** frontmatter `version: 2.0 → 2.2`, `updated: 2026-08-26 → 2026-09-05`; footer `Version: 2.1 → 2.2 (registered Phase 2 realization_class attribute, 2026-09-05)`. This also resolves the pre-existing frontmatter(2.0)/footer(2.1) drift. Nothing else touched; no renumbering.

## 4. Open questions (for Validator / Orchestrator)

1. **Maturity-model vocabulary drift:** `phase1_ontology.yaml` v1.6 `maturity_model` block still cites `MATURITY_MODEL_CSF_STRICT.md v1.0`, superseded by `IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0` (whose §9 deprecates tier vocabulary that v1.6 still uses: `T1..T4`, tier_names). The rubric anchors §6 on the structural elements (Scale A + EvidenceItem `CITES_OUTCOME` "N:1 when scale=capability") and carries a vocabulary note; a future ontology bump may want to align the authority pointer. Out of scope here (case file untouched).
2. **Pre-existing Doc18 artifacts noticed while reading (not fixed, `02_CASES/` read-only):** duplicated "14. Implementation Priority" fields in most cards; mangled heading `CR-D-06.1-001 — Procefederated single sign-onr Due Diligence`; `CR-D-03.2-001` card header says "MUST, NI=2 (SHOULD)" (header vs bucket mismatch). Flag for the next case campaign.
3. **Tagging campaign scope:** rubric §4 names 4 storage locations (catalog column+card, `12_Rules_Catalog.xlsx`, `control_set.yaml`, `phase2_ontology.yaml` enum + attrs). The actual enum/attr insertion and per-rule tagging is the separate later Phase 2 task — not started, per constraints.
4. **Physical controls in §7 crosswalk:** folded into TECHNOLOGY ("realized by artefact properties") per the locked decision; if a future case contains facility-security-heavy domains (D-XX physical), a fourth class debate could resurface — enum stays closed, P7 applies.

---

## 5. Addendum (v1.1 rework, 2026-09-05) — Validator amendments A1–A7 applied

Verdict `APPROVED_WITH_AMENDMENTS`; amendments file `00_METHODOLOGY/validation/RC_RUBRIC_AMENDMENTS_A1-A8.md` (the only file consulted — the Validator report `REALIZATION_CLASS_RUBRIC_VALIDATOR_REPORT_v0.md` was NOT opened, per the blind-baseline constraint).

**Applied (A1–A7, all `APPLY-NOW`):**

- **A1** — Constitutive-step test: replaced §2 TECHNOLOGY Disqualifier cell and §3 tie-break bullet 1 (verbatim).
- **A2** — P/C structural indicators + Doc18 standing note (`CR-D-08.1-001`/`CR-D-08.2-001`): replaced §3 tie-break bullet 2 (verbatim).
- **A3** — §4 storage row rewritten to Anexo A + card fields 25/26 (verbatim) and the "Doc18 counter adjustment (campaign step)" paragraph inserted after the §4 storage table (verbatim).
- **A4** — "Sync rule" paragraph added at the end of §4 (verbatim, after the Invariance guarantees paragraph).
- **A5** — §2 TECHNOLOGY Definition cell rewritten to cover physical artefact measures + "constitutive" wording (verbatim).
- **A6** — Preamble final clause replaced with the per-case Phase 3 facts (verbatim) + the optional §5 Forward-pointer companion sentence appended (applied — it reinforces the same correction).
- **A7** — §6 dashboard path prefixed with `00_METHODOLOGY/` (verbatim).

**Deferred:** A8 (`DEFER` — two further §8 borderlines; not applied).

**Adjusted wording (2 deviations, both within A4's scope):**

1. A4 lists two targets (§4 header line + the "Mass re-tagging…" sentence) but supplies one replacement block. The Sync rule paragraph was placed at the end of §4; the replaced §9 sentence was retained as a minimal pointer: "Mass re-tagging of a case is a campaign; cross-location consistency is governed by the Sync rule (§4)." — preserving §9 context without duplicating the rule.
2. A4's §4 header line was harmonized to "**Storage locations** (Markdown catalog authoritative; sync governed by the Sync rule below):" — the former "kept in sync" phrasing would contradict the banner-noted-stale xlsx approach the amendment codifies.

All other amendment wording is verbatim. Frontmatter bumped to `version: 1.1` (updated 2026-09-05); version-history row added as instructed. A8 not applied.

**AGENTS.md re-check (step 5):** the corr-008 paragraph added in v1.0 makes no Phase 3 node-track claim, so A6's correction contradicts nothing there — unchanged. Minor observation (no action, out of A6 scope): its class gloss "(technical control / coordinated activity sequence / standing organizational ability)" predates A5's physical-artefact extension; it is a shorthand pointer to the rubric, not a normative definition, so it was left as-is.

---

## 6. Tag wave v1 — Case_01 Phase 2 (2026-09-05)

Applied `realization_class` (+ optional secondary) to all 46 Doc18 rules per RUBRIC v1.1 §3/§4, under the mid-flight SCOPE CHANGE (documents only — data mirrors and dashboards out). Blind constraint respected throughout: `REALIZATION_CLASS_RUBRIC_VALIDATOR_REPORT_v0.md` was never opened.

### 6.1 Final distribution (46 rules)

| Class | CR | BPR | Total | IDs |
|---|--:|--:|--:|---|
| TECHNOLOGY | 13 | 5 | **18** | CR-D-01.1/01.2/01.3/01.4/03.1/03.2/03.3/03.4/05.1/05.2/05.4/06.2/10.2; BPR-D-01.1/03.1/03.2/03.4/10.2 |
| PROCESS | 13 | 10 | **23** | CR-D-02.1/02.2/02.3/04.1/04.2/04.3/04.4/05.3/06.1/06.3/07.1/09.4/10.3; BPR-D-01.2/02.1/02.2/04.3-001/04.3-002/05.3/07.1/07.2/10.3-001/10.3-002 |
| CAPABILITY | 4 | 1 | **5** | CR-D-08.1/08.2/09.1/09.2; BPR-D-09.1 |

Secondaries (8): TECHNOLOGY→ CR-D-02.1, CR-D-02.2, CR-D-04.1, CR-D-04.2, CR-D-04.4, BPR-D-01.2, BPR-D-07.2 (7); PROCESS→ CR-D-09.2 (1). Decision criterion for secondaries: VC gates on BOTH a built automated safeguard AND a constitutive human-coordinated step (A1 test). Agreement with the rubric's own 9 exemplars (§8 v1.1): **9/9**, including both secondaries (02.2→TECHNOLOGY, 09.2→PROCESS) and both non-secondary PROCESS exemplars (04.3, 05.3).

### 6.2 Gates — before/after

| Gate | BEFORE | AFTER |
|---|---|---|
| `validation/check_unmapped.py` | GATE PASS (v0.3); UNMAPPED_PF occurrences 52; 5 waived pre-existing CSF ids | GATE PASS (v0.3); 52; identical warnings. **Note:** this gate regenerates control_set.yaml (see 6.3.1); the AFTER run is the last regeneration, attribute re-applied post-gate |
| ID census Doc18 | 46 unique (30 CR + 16 BPR), 560 occurrences | identical (diff vs saved baseline: empty) |
| ID census control_set.yaml | 30 + 16 | identical |
| ID census 12_Rules_Catalog.xlsx (Rules_Catalog sheet) | 46 unique | identical |
| Doc18 field-25 count | — | 46 (mandatory field on every card) |
| Doc18 field-26 count | — | 46 (8 with a class, 38 rendered `—`) |
| 3-way agreement Doc18 × control_set.yaml × xlsx | — | 0 mismatches on primary and secondary for all 46 IDs |
| `scripts/build_p2_graph.py` + `git diff data/phase2_graph.json` | — | no diff (builder ignores the new field; nothing to revert) |
| Dashboard smoke | 16/16 PASS (baseline) | skipped per scope change (no dashboard-input files among changes by construction; last recorded runs before/after doc edits were 16/16) |
| `git status --short` proof | — | modified: Doc18_Rules_Catalog.md, control_set.yaml, phase2_ontology.yaml, 12_Rules_Catalog.xlsx (the 4 in-scope files) + `00_METHODOLOGY/AGENTS.md` and `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` + `00_METHODOLOGY/validation/` from the *previous* rubric tasks. No `data/`, no `00_VISUALISATIONS/`, no scripts |

### 6.3 Edits applied

1. **Doc18**: frontmatter `expected_fields_per_card`/`fields_per_card` 24→26, version 4.0→4.1, updated 2026-09-05; §3 schema "(24 Fields)"→"(26 Fields)" + rows 25/26 (§1 prose "24-field detail card" → "26-field" for coherence); all 46 cards gained fields 25/26 after the SSDF anchor line (regex-verified 46 insertions); Anexo A gained the `Realization Class` column (secondary rendered `PRIMARY (+SECONDARY)`); new **Anexo D — Realization Class Distribution (derived view, generated-on-tag, regenerate-if-changed)**; **DOCUMENT HISTORY** section with the required row.
2. **control_set.yaml**: `realization_class:` (46) + `realization_class_secondary:` (8) appended to each control entry after `verification.owner`.
3. **phase2_ontology.yaml**: `enums.RealizationClass: [TECHNOLOGY, PROCESS, CAPABILITY]`; `realization_class: enum(RealizationClass)` + `realization_class_secondary: enum(RealizationClass)` on ComplianceRule and BestPracticeRule (mirroring existing enum-attr style).
4. **12_Rules_Catalog.xlsx**: `Rules_Catalog` sheet — header cells R5/S5, 46 rule rows (6–51) filled from the Doc18-derived map, values `—` where unused; A4 banner placed in cell A2 (verbatim Sync-rule semantics: stale until regenerated, 46 rows match Doc18, NI/stub columns untouched). Nothing else changed.

### 6.4 Scope-change handling and deviations

1. **control_set.yaml is a generated file** — repo-root `validation/build_control_set.py` regenerates it from Doc18 on every `check_unmapped.py` run (fixed 24-field schema), which silently wiped my first in-place edit during the AFTER gate. Re-applied post-gate and verified by YAML parse + census. **Follow-up required:** the generator must emit fields 25/26 for the attribute to survive future gate runs (out of documents-only scope — flagging for the next tooling pass; until then, re-run the tag insert after any regeneration).
2. **`data/phase2_ontology.compact.json`**: edited pre-scope-change (attrs + enum), REVERTED via `git checkout --` per coordinator instruction; file is back to HEAD.
3. **`data/phase2_graph.json`**: builder executed once pre-scope-change, produced **zero diff**; no revert needed, file untouched.
4. **Card numbering defects left as-is** (per gates-first rule): duplicated `14. Implementation Priority` lines (~2 per card) and missing field 13 remain; the A3 "may reconcile" option was not exercised because a 46-card renumber cannot be proven identical-PASS without disproportionate risk. Doc18's pre-existing NI header/bucket mismatch on `CR-D-03.2-001` ("MUST, NI=2 (SHOULD)") also untouched.
5. **Version bump**: 4.0 → 4.1 ("+1" interpreted as minor increment; the change is additive).
6. No new deprecated-prefixed IDs introduced; all CR-/BPR- IDs quoted are pre-existing Doc18 IDs (deprecated corr-007 prefixes tolerated only as legacy aliases per corr-008).

---

## 7. Fix wave v1 — audit adjudication applied (2026-09-05)

Validator audit (`REALIZATION_CLASS_TAGWAVE_AUDIT_v0.md`, verdict `FIX_WAVE_NEEDED`): 41/46 primary agreement vs the Validator's blind baseline; 5 divergences adjudicated — 4 in the Executor's favour, 2 fixes required. Blind constraint lifted for this wave; the audit file was read.

### 7.1 Fixes applied (2 rules × 3 document locations)

| Rule | Change | Locations |
|---|---|---|
| `BPR-D-03.4-001` | TECHNOLOGY → **PROCESS**, secondary **TECHNOLOGY** (exception disposition in criterion 2, audit §4.6) | Doc18 card fields 25/26, 4 Anexo A rows, Anexo D; control_set.yaml entry (+ new secondary key); xlsx cols 18/19 |
| `BPR-D-04.3-001` | PROCESS → **CAPABILITY**, secondary `—` (standing-artefact rule, audit §4.4) | Doc18 card fields 25/26, 6 Anexo A rows, Anexo D; control_set.yaml entry (secondary key removed); xlsx cols 18/19 |

### 7.2 Final adjudicated distribution (confirmed by recount after edits)

| Class | Count | Secondaries |
|---|--:|---|
| TECHNOLOGY | **17** | 8 rules carry secondary TECHNOLOGY (CR-D-02.1/02.2/04.1/04.2/04.4, BPR-D-01.2/**03.4**/07.2) |
| PROCESS | **23** | CR-D-09.2-001 → secondary PROCESS |
| CAPABILITY | **6** | — |
| **Total** | **46** | **9 secondaries** (8 TECHNOLOGY + 1 PROCESS) |

### 7.3 Generator extension (`validation/build_control_set.py` v1.0 → v1.1)

Added parsing of Doc18 card fields 25/26 and emission of `realization_class:` (mandatory; generator aborts with `ValueError` if a card lacks it) and `realization_class_secondary:` (key omitted when the card renders `—`) into each control entry, after `verification`. Verification: snapshot → run → **diff empty** (regenerated output byte-identical to the fixed working state; all 46+9 keys preserved); `git diff control_set.yaml` vs HEAD = 55 insertions, 0 deletions. **The tag-wave defect flagged in §6.3.1 is closed**: control_set.yaml now survives `check_unmapped.py` regeneration with the attribute intact (proven by running the gate after the generator change — post-gate file still identical to snapshot).

### 7.4 Gates (after fixes)

| Gate | Result |
|---|---|
| `validation/check_unmapped.py` | GATE PASS (v0.3); UNMAPPED_PF 52; identical warnings; regeneration stable |
| ID census Doc18 / control_set.yaml / xlsx | identical to tag-wave baseline (46 unique; 30 CR + 16 BPR each) |
| Doc18 field counts | f25=46, f26=46 (9 used, 37 `—`) |
| control_set.yaml keys | 46 `realization_class`, 9 `realization_class_secondary` |
| 3-way agreement Doc18 × control_set.yaml × xlsx | NONE — 46/46 agree on primary AND secondary; fixes confirmed in all three |
| Anexo A faithfulness | 4/4 rows for BPR-D-03.4-001 → `PROCESS (+TECHNOLOGY)`; 6/6 rows for BPR-D-04.3-001 → `CAPABILITY` |
| `git status --short` | **final in-scope set:** Doc18_Rules_Catalog.md, control_set.yaml, 12_Rules_Catalog.xlsx, `validation/build_control_set.py` (+ prior-task methodology artefacts: `00_METHODOLOGY/AGENTS.md`, `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md`, `00_METHODOLOGY/validation/` reports). `phase2_ontology.yaml` at HEAD (ontology DEFERRED, human decision). No `data/`, no `00_VISUALISATIONS/` |

### 7.5 Deviations / incidents

1. **`phase2_ontology.yaml` — CORRECTED (Orchestrator adjudication):** the revert I detected at wave start was **intentional** — a human decision ("não tocar na ontologia"; documents-only scope) executed by the Orchestrator, making the ontology location DEFERRED per rubric v1.2 §4. My re-restoration was itself the out-of-scope change and has been reverted again by the Orchestrator; the file is at HEAD. **Ontology is out of scope for this campaign — do not touch.** The generator change is unaffected (it reads Doc18 only). Final in-scope set: Doc18_Rules_Catalog.md, control_set.yaml, 12_Rules_Catalog.xlsx, validation/build_control_set.py, + methodology artefacts (REALIZATION_CLASS_RUBRIC.md, AGENTS.md, validation/ reports).
2. **Generator `** ` quirk not propagated:** the generator's legacy fields keep a `** ` prefix from naive colon-splitting (e.g. `method: '** TEST'`). The new fields use a strict regex and emit clean enum values — deliberate; the legacy quirk was left untouched (out of scope).
3. Audit §1 reports the xlsx secondary column as "cols 17/18"; the actual sheet columns are 18/19 (Q ends at 17). Values matched on the audit's own spot-check; no action.
4. Agreements noted for the record: all 8 tag-wave secondaries confirmed (audit §5); audit §4.1–4.5 adjudicated 4 baseline flips onto the Executor's applied values.
