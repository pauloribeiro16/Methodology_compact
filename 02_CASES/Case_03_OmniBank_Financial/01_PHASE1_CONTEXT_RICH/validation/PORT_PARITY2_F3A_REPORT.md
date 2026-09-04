# PORT-PARITY-2 · Block F3a — Case_03 Data-Layer Propagation Report

> **Campaign:** PORT-PARITY-2, block F3a
> **Task:** propagate the Case_01/Case_02 "Phase 1 rich + maturity v1.6/v2.3" DATA LAYER to Case_03_OmniBank_Financial
> **Executor:** Executor agent · **Date:** 2026-09-04
> **Templates:** Case_02 ontology v2.3 / builder v2.4 / validator v2.4 (+ Case_01 ontology v1.6 class defs)
> **Result:** ALL GATES PASS (exit 0). Working tree left uncommitted for orchestrator verification.

---

## 1. Files created/changed (all inside `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/`)

| File | Action | Content |
|---|---|---|
| `phase1_ontology.yaml` | **modified** v2.0-port → **v2.1-port** (additive only) | `kg_ontology.maturity_model` block (EvidenceItem/TierDecision classes, 5 relations HAS_EVIDENCE/CITES_OUTCOME/CITES_CLAUSE/DECIDED_AT/USED_IN, scales capability/coverage, invariants, case_overrides dora=true/ai_act=true); 7 architecture+NIST id_patterns promoted to full class definitions (System/DataStore/DataFlow/PersonalDataCategory/DataSubjectCategory/ThirdParty/NistControl — Case_01 v1.6 shape, sources retargeted to Doc04 §1.1–§2.4/Doc06/Doc14 §5); `NistFramework` enum; `ALIGNS_TO` relation; `EvidenceItem`/`TierDecision` id_patterns (EV-/TD-); `meta.build_note`. DORA branch `^(GDPR\|CRA\|NIS2\|DORA\|AI)-C\d{2}$` KEPT. Nothing deleted. |
| `data/phase1_ontology.compact.json` | **created** (schema 1.1) | Compact sibling of `kg_ontology` (Case_02 shape): 22 classes, 31 relations, 17 enums, invariants.counts (150 clauses, 76 AGs, …), id_patterns incl. EV-/TD-, `maturity_model` block, provenance_rules. |
| `data/phase1_graph.json` | **created** (builder output) | 749 nodes / 2054 links / 9 audits / invariants / ambiguity block. |
| `scripts/build_p1_graph.py` | **created** (v2.1-port) | Graph builder ported from Case_02 v2.4; every source pointer retargeted to Case_03 docs/xlsx (verified against actual file layouts). |
| `scripts/build_p1_dashboard.py` | **created** (v2.1-port) | Validator ported from Case_02 v2.4 verbatim (9 checks + `--strict`), ROOT/paths retargeted, EXPECTED pinned to builder invariants. |
| Existing `scripts/regenerate_ontology.py`, `filter_ambiguity_cards.py`, `generate_corpus_links.py` | untouched | Kept as required. |

## 2. Final counts

### 2.1 Nodes — 749 total

| Type | Count | Source |
|---|---:|---|
| CompanyContext | 1 | ontology@company (CC-OMNIBANK-2026-001) |
| Regulation | 5 | ontology@regulations — **ALL 5 applicable** (GDPR, CRA, NIS2, DORA, AI Act) |
| Domain | 10 | ontology@domains |
| SecurityControlDomain | 38 | **38/38 ACTIVE, zero NOT_ADDRESSED** (only AEGIS case) |
| RegulatoryClause | 150 | ontology@clause_mappings (28 GDPR + 26 CRA + 29 NIS2 + **38 DORA** + 29 AI) |
| Tension | 5 | ontology@tensions (T-001..T-005) |
| Stakeholder / RaciRole | 15 / 15 | xlsx ROLES_RACI header (CEO…Board; CRO, DORA-Risk, Fraud, Board are Case_03-only roles) |
| RaciActivity | 65 | xlsx ROLES_RACI rows |
| CoverageGap | 12 | xlsx GAPS (GAP-01..GAP-12, 2-digit id style) |
| AdjustedGoal | 76 | Doc14 §2 (38 PG slot-001 + 38 SG slot-002) + archived detail cards |
| DataSubjectCategory | 9 | Doc04 §2.4 |
| System / DataStore / DataFlow | 25 / 12 / 25 | xlsx SYSTEMS / DATA_STORES / DATA_FLOWS |
| ThirdParty | 33 | xlsx THIRD_PARTIES (incl. `dora_art30_contract` attr — Case_03-specific column) |
| PersonalDataCategory | 13 | Doc04 §2.3 / xlsx PERSONAL_DATA |
| NistControl | **121** | Doc14 §5: **79 CSF + 38 PF + 4 AI-RMF** (distinct, deduped) |
| EvidenceItem | **119** | mechanical derivation (§2.3 below) |

### 2.2 Links — 2054 total

| Rel | Count | Rel | Count |
|---|---:|---|---:|
| RACI | 804 | MAPS_TO | 150 |
| ALIGNS_TO | 577 (264 CSF + 307 PF + 6 AI-RMF, deduped per sd) | BELONGS_TO | 38 |
| HAS_EVIDENCE | 119 | YIELDS | 76 |
| CITES_OUTCOME | 82 | FLOWS_BETWEEN | 25 |
| CITES_CLAUSE | 37 | APPLIES_TO | 74 |
| CAPTURES | 35 (Doc04 §2.4↔§2.3 heuristic, same as Case_02) | OVERLAPS_WITH | 10 (5 regs, all applicable) |
| HOSTS | 14 | ASSESSES | 5 |
| FLAGS | 4 | HAS_TENSION_WITH | 4 (mechanically resolved, see §3.2) |

**0 dangling links** (verified over all 2054). **0 dangling CITES/HAS_EVIDENCE targets. 100% EvidenceItem `sources[]` resolvable** (graph node ids or canonical doc-section strings).

### 2.3 EvidenceItems — 119 (mechanical derivation, no invented content)

| Framework / scale | Count | Derivation rule |
|---|---:|---|
| Coverage (Scale B, CITES_CLAUSE) | **37** | 1 per active sub-domain **with a clause anchor** in ontology@clause_mappings (first clause per sd, deterministic). `observed=true` — Scale-B SUBSTANTIVE anchors met (documented control Doc13 §4 + RACI activity Doc07 §4 + coverage level Doc12 §3). |
| Capability CSF (Scale A) | **38** | 1 per sub-domain (all 38 have CSF in Doc14 §5), anchored on FIRST listed CSF control. |
| Capability PF (Scale A) | **38** | 1 per sub-domain (all 38 have PF in Doc14 §5), first listed PF control. |
| Capability AI-RMF (Scale A) | **6** | The 6 sub-domains with real AI-RMF anchors per Doc14 §5 (D-02.1, D-07.1, D-07.2, D-07.3, D-09.2, D-10.1) — REAL for OmniBank (AI Act PROVIDER + DEPLOYER, OmniScore Annex III). |
| Total | **119** | 37 + 38 + 38 + 6. EV id slots: -001 coverage, -002 CSF, -003 PF, -004 AI-RMF. |

Capability items carry **`observed=false`** (Doc13 §4 "Impl. Status (backfilled)" = PARTIAL for all 38 rows) — capability tiers are NOT asserted; **no TierDecision nodes emitted** (parity: Case_01/Case_02 graphs also contain zero TierDecisions). All 38 sub-domains have non-empty `evidence_ids` (coverage + capability; `coverage_evidence_ids` kept separately — 37/38 non-empty).

### 2.4 Audits — 9

| id | kind | severity | subject |
|---|---|---|---|
| NEW-C03-01 | structural | info | Maturity layer seeded (119 EV; gates; xlsx MATURITY sheet deliberately not ingested — Gate 1) |
| NEW-C03-02 | structural | info | 76 AdjustedGoals from Doc14 §2 + `_deprecated/Doc15_Appendix_A_OLD.md` archive; 76 YIELDS |
| NEW-C03-03 | blocking_ambiguity | info | Ambiguity Register: 1490 cards, per-sd counts, top-20 (GDPR 5 + CRA 4 + NIS 2 4 + DORA 4 + AI Act 3) |
| NEW-C03-04 | structural | info | 121 NistControl from Doc14 §5 + REG_CHAIN cross-check (30 CSF / 142 raw — strict subset) |
| NEW-C03-05 | structural | info | Proportionality: **31 RIGOROUS + 7 STANDARD** (Doc13 §3/§4), 38/38 ACTIVE |
| NEW-C03-06 | structural | info | DORA axis real (38 clauses, Doc11); 4/5 tension edges mechanically resolved |
| CFL-C03-001 | cross_doc_conflict | low | Doc14 §5.1 raw-mention stats vs deduped graph counts — reconciled, no conflict |
| BLN-C03-001 | broken_link | low | 10 macro-domain baseline (matches Case_01/02) |
| CVG-C03-001 | coverage_gap | **low** | **D-07.2 has no clause anchor → Coverage EV withheld for human review; 37/38 clause-anchored** |

## 3. Divergences from the Case_02 template (adaptations, honestly recorded)

1. **NIST primary source = Doc14 §5, not REG_CHAIN.** Case_02's builder took CSF controls from the xlsx REG_CHAIN column. Case_03's REG_CHAIN exists (same layout) but only carries 30 distinct CSF controls; Doc14 §5 is Case_03's canonical NIST table (38 rows × CSF/PF/AI-RMF, corpus-derived per its §5 header + validation table). The builder parses Doc14 §5 for all three frameworks and keeps REG_CHAIN as a cross-check (audit CFL-C03-001 + `regchain_*` invariants). Case_03's Doc13 has no §7 NIST crosswalk (Case_02's equivalent section lives in Doc14 §5 here) — the task brief's "Doc13 §7 or Doc12 NIST columns" resolved to Doc14 §5.
2. **D-07.2 has no RegulatoryClause anchor** — absent from ontology@clause_mappings (150 clauses map to 37 sub-domains) AND from Doc10 (zero mentions); REG_CHAIN anchors it only via Sub-SO ids (SO-D-07.2.CRA/DORA/AI_Act). Per the no-invention rule the Coverage EvidenceItem was withheld; D-07.2 still carries capability evidence (evidence_ids non-empty). **Orchestrator decision needed:** add a D-07.2 clause to ontology+Doc10, or ratify Sub-SO-only coverage.
3. **HAS_TENSION_WITH resolution.** Case_03's ontology tensions reference regulation articles ("GDPR-Art.33"), not clause ids (Case_02 had clause_1/clause_2 fields). The builder resolves article refs → clause ids mechanically via the clause_mappings article index and emits at most one edge per tension: **4/5 resolved** (T-001, T-002, T-003, T-004); T-005 resolves to a single clause (DORA-C28) + non-clause regimes (ISO 27001) → no edge. Skipped refs are listed in the audit.
4. **AdjustedGoal source.** Case_02 parsed AG cards from Doc13 §8 in the same file. Case_03's Doc14 §2 is a decision-summary table (corr-010 shrink); the 76 detail cards (18 fields) were archived verbatim to `_deprecated/Doc15_Appendix_A_OLD.md`. The builder parses §2 for canonical ids/titles and the archive for objective prose, source articles, NIST anchors, verification criteria, owner, status — with an id cross-check between the two (0 mismatches). AG id convention confirmed: `AG-D-XX.Y-001` privacy / `-002` security (same as Case_02).
5. **Proportionality parsed, not hardcoded.** Case_02 hardcoded a 35-row SUBDOMAIN_PROPORTIONALITY table. Case_03's builder parses Doc13 §4 (13 columns × 38 rows) mechanically — 31 RIGOROUS + 7 STANDARD, satisfaction_pattern BUILD_FULL/INHERIT, impl status PARTIAL — so the graph cannot drift from Doc13.
6. **Capability `observed=false` policy.** Case_02 hand-authored capability claims with per-tier commentary (T2/T3 borderline). Case_03 derives mechanically and marks all 82 capability items unobserved because Doc13 §4 marks implementation PARTIAL across the board; the decision is recorded in NEW-C03-01.
7. **CoverageGap pattern widened** to `^GAP-\d{2,3}$` (Case_03 canonical GAP-01..GAP-12, Doc07 §7 + GAPS xlsx). Case_02 kept `^GAP-\d{3}$` and warned on 12 ids; Case_03 therefore has no CoverageGap warnings.
8. **GAPS sub-domain refs are macro-level** ("D-04 Incident Response"); FLAGS edges are emitted only for exact `D-XX.Y` tokens found in gap descriptions (4 edges; 12 gap nodes retained).
9. **xlsx MATURITY sheet not ingested** — macro-domain 0–4 legacy scale; loading it into sub-domain attrs would violate maturity Gate 1 (forbidden scalars). Recorded in NEW-C03-01; superseded by MATURITY_MODEL_CSF_STRICT.md.
10. **AG `tier` attr** is filled from Doc13 §4 per sub-domain (RIGOROUS/STANDARD) instead of Case_02's "LIGHTWEIGHT placeholder".
11. **ThirdParty `dora_art30_contract` attr** added from the Case_03-specific xlsx column; DPA/Art.28 columns parsed with startswith("Y") because Case_03 cell values are "Y (…)" strings (Case_02 used bare "Y").

## 4. Gate outputs (run 2026-09-04)

```
=== GATE 1: python3 scripts/build_p1_graph.py ===
wrote …/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json
  {'CompanyContext': 1, 'Regulation': 5, 'Domain': 10, 'SecurityControlDomain': 38,
   'RegulatoryClause': 150, 'Tension': 5, 'Stakeholder': 15, 'RaciRole': 15,
   'RaciActivity': 65, 'CoverageGap': 12, 'AdjustedGoal': 76, 'DataSubjectCategory': 9,
   'System': 25, 'DataStore': 12, 'DataFlow': 25, 'ThirdParty': 33,
   'PersonalDataCategory': 13, 'NistControl': 121, 'EvidenceItem': 119}
  link count: 2054
  audits count: 9
EXIT=0

=== GATE 2: python3 scripts/build_p1_dashboard.py --check --strict ===
# 3 warning(s):
  [warn] ID pattern mismatch for type 'Stakeholder': 7 violations; sample: ['STK-AI-Gov-01', 'STK-Comp-01', …]
  [warn] ID pattern mismatch for type 'RaciRole': 7 violations; sample: ['ROLE-AI-Gov', 'ROLE-Comp', …]
  [warn] ID pattern mismatch for type 'ThirdParty': 6 violations; sample: ['AWS__EU___eu-central-1___eu-west-1_', …]
OK — invariants pass, audit node_ids resolve, ontology types/relations valid. (warnings: 3)
EXIT=0
```
The 3 warnings are the same classes Case_02's validator also warns on (STK-/ROLE-/ThirdParty esc_id style with hyphens/lowercase from xlsx role+vendor names — Case_02: 5-6 violations each on the same patterns). Non-fatal by design in both cases (Case_02 `--check --strict` likewise exits 0 with 5 warnings).

```
=== GATE 3: json load ===
749 2054 9        EXIT=0

=== GATE 4: python3 scripts/regenerate_ontology.py ===
EXIT=0   (Sprint-1 TODO stub — prints a plan, validates nothing; unchanged behaviour)

=== Extra integrity checks ===
- dangling links (all 16 relation types): 0
- unresolvable EvidenceItem sources[]: 0 (Gate 4 citation discipline: 0 hits)
- sub-domains with empty evidence_ids: none (38/38 carry evidence)
- CITES_CLAUSE/CITES_OUTCOME targets: all resolve (37 → RegulatoryClause, 82 → NistControl)
- builder determinism: two runs identical modulo `meta.generated` timestamp
- ontology YAML re-parse after edit: kg_ontology = meta/id_patterns/classes/enums/relations/
  forbidden_subdomain_attrs/implementation_posture/case_invariants/maturity_model; clause (150),
  subdomain (38), regulation (5) counts unchanged (additive edit only)
- git scope: only 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/** modified/added
```

## 5. Orchestrator decisions requested

1. **D-07.2 clause anchor (CVG-C03-001):** add a clause to ontology+Doc10 vs ratify Sub-SO-only coverage. Until then 37/38 coverage-anchored (invariant `subdomains_with_coverage_evidence: 37`).
2. **T-005 edge:** accept "no clause pair" (current) or extend ontology tensions with explicit clause refs (Sprint 2+ candidate, mirrors T-001..T-004 registration note).
3. **Capability observed=false:** confirm the conservative posture (recommended; Doc13 §4 PARTIAL) or commission a Validator pass to hand-author tier commentary like Case_02's.
4. **Warning budget:** 3 residual warnings are id-style only (same family as Case_02's accepted warnings); tightening would require renaming STK/ROLE/vendor ids in the graph away from the xlsx header strings.
