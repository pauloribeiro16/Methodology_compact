---
document_id: AEGIS-C03-P3-KG-CHAINS
title: KG Derivation Chains v0 (Case_03 Phase 3)
phase: 3
version: 0.0
created: 2026-09-04
updated: 2026-09-04
author: PORT-PARITY-2 Executor (generated)
status: GENERATED
case: Case_03_OmniBank_Financial
kg_build: case-local P1+P2 graph JSONs (F4 port)
---

> **GENERATED v0 (PORT-PARITY-2) — pending human review.** Mechanically derived from ../01_PHASE1_CONTEXT_RICH/data/phase1_graph.json, ../02_PHASE2_RULES_RICH/data/phase2_graph.json, ../02_PHASE2_RULES_RICH/control_set.yaml@traceability; verify before relying on it.

# KG Derivation Chains v0 — Case_03 OmniBank Financial

**Graphs used (case-local, ported F4):** `../01_PHASE1_CONTEXT_RICH/data/phase1_graph.json` — 749 nodes / 2054 links; `../02_PHASE2_RULES_RICH/data/phase2_graph.json` — 242 nodes / 340 links. Node ids are cited **verbatim**; hops that exist as graph edges carry their relation; hops that exist only by id convention are labelled `ID-join (control_set.yaml@traceability)` — they are **not** graph edges. Case_03's 5-regulation scope adds **DORA**; P2 objective nodes live on the AG-D- id space (corr-010).

## §1 Graph inventory (verbatim counts)

| Graph | Nodes | Links | Node types |
|---|---:|---:|---|
| P1 phase1_graph.json | 749 | 2054 | RegulatoryClause 150, NistControl 121, EvidenceItem 119, AdjustedGoal 76, RaciActivity 65, SecurityControlDomain 38, ThirdParty 33, System 25, DataFlow 25, Stakeholder 15, RaciRole 15, PersonalDataCategory 13, CoverageGap 12, DataStore 12, Domain 10, DataSubjectCategory 9, Regulation 5, Tension 5, CompanyContext 1 |
| P2 phase2_graph.json | 242 | 340 | NistSubcategory 82, BestPracticeRule 40, Obligation 38, ComplianceRule 38, SecurityOperationalObjective 26, PrivacyOperationalObjective 12, Tension 5, CompanyContext 1 |

P1 relations: {'RACI': 804, 'ALIGNS_TO': 577, 'MAPS_TO': 150, 'HAS_EVIDENCE': 119, 'CITES_OUTCOME': 82, 'YIELDS': 76, 'APPLIES_TO': 74, 'BELONGS_TO': 38, 'CITES_CLAUSE': 37, 'CAPTURES': 35, 'FLOWS_BETWEEN': 25, 'HOSTS': 14, 'OVERLAPS_WITH': 10, 'ASSESSES': 5, 'HAS_TENSION_WITH': 4, 'FLAGS': 4}
P2 relations: {'MAPS_TO': 196, 'MITIGATES': 99, 'YIELDS': 38, 'GENERATES': 7}

## §2 Representative derivation chains (one per regulation)

Pattern: CompanyContext → Regulation → Clause → Evidence → Sub-domain → AG → OBL → CR → NIST anchor. Selection rule (mechanical): first control in `control_set.yaml` whose `source` field cites the regulation.

### CH-01 (GDPR): CR-D-01.1-001

1. **CompanyContext** — `CC-OMNIBANK-2026-001` (P2 node; no outgoing edges — anchor node)
2. **Regulation→Clause** — `GDPR-C04` (P1 RegulatoryClause; label “REG-GDPR — Art. 5(1)(f)”)
3. **Clause←Evidence** — `EV-D-01.1-001` P1 `CITES_CLAUSE` edge
4. **Sub-domain→AG** — `AG-D-01.1-001`, `AG-D-01.1-002` P1 `YIELDS` edges from `D-01.1`
5. **AG→OBL** — `OBL-D-01.1-001` (P2 Obligation node) — ID-join (control_set.yaml@traceability)
6. **OBL→CR** — `CR-D-01.1-001` — ID-join (control_set.yaml@traceability “GDPR-C04, C14; CRA-C07; NIS2-C18; DORA-C09; AI-C17 → AG-D-01.1-001/-00…”)
7. **CR→Goal** — `AG-D-01.1-001`, `AG-D-01.4-001`, `AG-D-05.2-001` P2 `MITIGATES` edges (AG-D- space)
8. **CR→NIST** — `NIST-CSF-PR.DS-01`, `NIST-PF-PR.DS-P1`, `NIST-PF-CT.DP-P2` P2 `MAPS_TO` edges

### CH-02 (CRA): CR-D-01.1-001

1. **CompanyContext** — `CC-OMNIBANK-2026-001` (P2 node; no outgoing edges — anchor node)
2. **Regulation→Clause** — `CRA-C07` (P1 RegulatoryClause; label “REG-CRA — Annex I Part I §2(e)”)
3. **Sub-domain→AG** — `AG-D-01.1-001`, `AG-D-01.1-002` P1 `YIELDS` edges from `D-01.1`
4. **AG→OBL** — `OBL-D-01.1-001` (P2 Obligation node) — ID-join (control_set.yaml@traceability)
5. **OBL→CR** — `CR-D-01.1-001` — ID-join (control_set.yaml@traceability “GDPR-C04, C14; CRA-C07; NIS2-C18; DORA-C09; AI-C17 → AG-D-01.1-001/-00…”)
6. **CR→Goal** — `AG-D-01.1-001`, `AG-D-01.4-001`, `AG-D-05.2-001` P2 `MITIGATES` edges (AG-D- space)
7. **CR→NIST** — `NIST-CSF-PR.DS-01`, `NIST-PF-PR.DS-P1`, `NIST-PF-CT.DP-P2` P2 `MAPS_TO` edges

### CH-03 (NIS2): CR-D-01.1-001

1. **CompanyContext** — `CC-OMNIBANK-2026-001` (P2 node; no outgoing edges — anchor node)
2. **Regulation→Clause** — `NIS2-C18` (P1 RegulatoryClause; label “REG-NIS2 — Art. 21(3)”)
3. **Sub-domain→AG** — `AG-D-01.1-001`, `AG-D-01.1-002` P1 `YIELDS` edges from `D-01.1`
4. **AG→OBL** — `OBL-D-01.1-001` (P2 Obligation node) — ID-join (control_set.yaml@traceability)
5. **OBL→CR** — `CR-D-01.1-001` — ID-join (control_set.yaml@traceability “GDPR-C04, C14; CRA-C07; NIS2-C18; DORA-C09; AI-C17 → AG-D-01.1-001/-00…”)
6. **CR→Goal** — `AG-D-01.1-001`, `AG-D-01.4-001`, `AG-D-05.2-001` P2 `MITIGATES` edges (AG-D- space)
7. **CR→NIST** — `NIST-CSF-PR.DS-01`, `NIST-PF-PR.DS-P1`, `NIST-PF-CT.DP-P2` P2 `MAPS_TO` edges

### CH-04 (DORA): CR-D-01.1-001

1. **CompanyContext** — `CC-OMNIBANK-2026-001` (P2 node; no outgoing edges — anchor node)
2. **Regulation→Clause** — `DORA-C09` (P1 RegulatoryClause; label “REG-DORA — Art. 10(2)”)
3. **Sub-domain→AG** — `AG-D-01.1-001`, `AG-D-01.1-002` P1 `YIELDS` edges from `D-01.1`
4. **AG→OBL** — `OBL-D-01.1-001` (P2 Obligation node) — ID-join (control_set.yaml@traceability)
5. **OBL→CR** — `CR-D-01.1-001` — ID-join (control_set.yaml@traceability “GDPR-C04, C14; CRA-C07; NIS2-C18; DORA-C09; AI-C17 → AG-D-01.1-001/-00…”)
6. **CR→Goal** — `AG-D-01.1-001`, `AG-D-01.4-001`, `AG-D-05.2-001` P2 `MITIGATES` edges (AG-D- space)
7. **CR→NIST** — `NIST-CSF-PR.DS-01`, `NIST-PF-PR.DS-P1`, `NIST-PF-CT.DP-P2` P2 `MAPS_TO` edges

### CH-05 (AIAct): CR-D-01.1-001

1. **CompanyContext** — `CC-OMNIBANK-2026-001` (P2 node; no outgoing edges — anchor node)
2. **Regulation→Clause** — `AI-C17` (P1 RegulatoryClause; label “REG-AIACT — Art. 15(2)”)
3. **Sub-domain→AG** — `AG-D-01.1-001`, `AG-D-01.1-002` P1 `YIELDS` edges from `D-01.1`
4. **AG→OBL** — `OBL-D-01.1-001` (P2 Obligation node) — ID-join (control_set.yaml@traceability)
5. **OBL→CR** — `CR-D-01.1-001` — ID-join (control_set.yaml@traceability “GDPR-C04, C14; CRA-C07; NIS2-C18; DORA-C09; AI-C17 → AG-D-01.1-001/-00…”)
6. **CR→Goal** — `AG-D-01.1-001`, `AG-D-01.4-001`, `AG-D-05.2-001` P2 `MITIGATES` edges (AG-D- space)
7. **CR→NIST** — `NIST-CSF-PR.DS-01`, `NIST-PF-PR.DS-P1`, `NIST-PF-CT.DP-P2` P2 `MAPS_TO` edges

## §3 Chain summary

| Chain | Regulation | Rule | Clause (P1) | AG (P2) | OBL (P2) | NIST anchors |
|---|---|---|---|---|---|---|
| CH-01 | GDPR | CR-D-01.1-001 | GDPR-C04 | AG-D-01.1-001, AG-D-01.4-001 | OBL-D-01.1-001 ✓ | PR.DS-01 / PR.DS-P1; CT.DP-P2 |
| CH-02 | CRA | CR-D-01.1-001 | CRA-C07 | AG-D-01.1-001, AG-D-01.4-001 | OBL-D-01.1-001 ✓ | PR.DS-01 / PR.DS-P1; CT.DP-P2 |
| CH-03 | NIS2 | CR-D-01.1-001 | NIS2-C18 | AG-D-01.1-001, AG-D-01.4-001 | OBL-D-01.1-001 ✓ | PR.DS-01 / PR.DS-P1; CT.DP-P2 |
| CH-04 | DORA | CR-D-01.1-001 | DORA-C09 | AG-D-01.1-001, AG-D-01.4-001 | OBL-D-01.1-001 ✓ | PR.DS-01 / PR.DS-P1; CT.DP-P2 |
| CH-05 | AIAct | CR-D-01.1-001 | AI-C17 | AG-D-01.1-001, AG-D-01.4-001 | OBL-D-01.1-001 ✓ | PR.DS-01 / PR.DS-P1; CT.DP-P2 |

## §4 Verification commands

```bash
python3 - <<'PY'
import json
g1 = json.load(open('02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json'))
g2 = json.load(open('02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/data/phase2_graph.json'))
print(sum(1 for l in g1['links'] if l['rel']=='CITES_CLAUSE'), 'CITES_CLAUSE edges')
print(sum(1 for l in g2['links'] if l['rel']=='MAPS_TO'), 'MAPS_TO edges')
PY
```

All node ids in this document were read mechanically from the two graph JSONs and `control_set.yaml` on 2026-09-04 by `scripts/gen_narrative_docs_v0.py`.
