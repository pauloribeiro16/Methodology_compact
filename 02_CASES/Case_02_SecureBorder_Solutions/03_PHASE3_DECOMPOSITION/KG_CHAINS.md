---
document_id: AEGIS-C02-P3-KG-CHAINS
title: KG Derivation Chains v0 (Case_02 Phase 3)
phase: 3
version: 0.0
created: 2026-09-04
updated: 2026-09-04
author: PORT-PARITY-2 Executor (generated)
status: GENERATED
case: Case_02_SecureBorder_Solutions
kg_build: case-local P1+P2 graph JSONs (F4 port)
---

> **GENERATED v0 (PORT-PARITY-2) — pending human review.** Mechanically derived from ../01_PHASE1_CONTEXT_RICH/data/phase1_graph.json, ../02_PHASE2_RULES_RICH/data/phase2_graph.json, ../02_PHASE2_RULES_RICH/control_set.yaml@traceability; verify before relying on it.

# KG Derivation Chains v0 — Case_02 SecureBorder Solutions

**Graphs used (case-local, ported F4):** `../01_PHASE1_CONTEXT_RICH/data/phase1_graph.json` — 521 nodes / 1205 links; `../02_PHASE2_RULES_RICH/data/phase2_graph.json` — 278 nodes / 356 links. Node ids below are cited **verbatim** from those files; hops that exist as graph edges are labelled with their relation; hops that exist only by id convention are labelled `ID-join (control_set.yaml@traceability)` — they are **not** graph edges.

## §1 Graph inventory (verbatim counts)

| Graph | Nodes | Links | Node types |
|---|---:|---:|---|
| P1 phase1_graph.json | 521 | 1205 | RegulatoryClause 111, AdjustedGoal 70, RaciActivity 63, EvidenceItem 59, NistControl 45, SecurityControlDomain 38, ThirdParty 22, Stakeholder 13, RaciRole 13, System 13, CoverageGap 12, DataFlow 12, Domain 10, DataSubjectCategory 10, Tension 9, PersonalDataCategory 8, DataStore 7, Regulation 5, CompanyContext 1 |
| P2 phase2_graph.json | 278 | 356 | NistSubcategory 78, SecurityOperationalObjective 55, Obligation 38, ComplianceRule 38, PrivacyOperationalObjective 34, BestPracticeRule 25, Tension 9, CompanyContext 1 |

P1 relations: {'RACI': 631, 'MAPS_TO': 111, 'ALIGNS_TO': 109, 'YIELDS': 70, 'APPLIES_TO': 70, 'HAS_EVIDENCE': 59, 'BELONGS_TO': 38, 'CITES_CLAUSE': 34, 'CITES_OUTCOME': 25, 'CAPTURES': 15, 'HOSTS': 11, 'FLOWS_BETWEEN': 10, 'HAS_TENSION_WITH': 9, 'OVERLAPS_WITH': 6, 'ASSESSES': 4, 'FLAGS': 3}
P2 relations: {'MAPS_TO': 193, 'YIELDS': 89, 'MITIGATES': 64, 'GENERATES': 10}

## §2 Representative derivation chains (one per regulation)

Pattern: CompanyContext → Regulation → Clause → Evidence → Sub-domain → AG → OBL → CR → NIST anchor. Selection rule (mechanical): first control in `control_set.yaml` whose `source` field cites the regulation.

### CH-01 (GDPR): CR-D-01.1-001

1. **CompanyContext** — `CC-SECUREBORDER-2026-001` (P2 node; no outgoing edges — anchor node)
2. **Regulation→Clause** — `GDPR-C04` (P1 RegulatoryClause; label “REG-GDPR — Art. 5(1)(d)”)
3. **Clause←Evidence** — `EV-D-01.1-001` P1 `CITES_CLAUSE` edge
4. **Sub-domain→AG** — `AG-D-01.1-001`, `AG-D-01.1-002` P1 `YIELDS` edges from `D-01.1`
5. **AG→OBL** — `OBL-D-01.1-001` (P2 Obligation node) — ID-join (control_set.yaml@traceability)
6. **OBL→CR** — `CR-D-01.1-001` — ID-join (control_set.yaml@traceability “GDPR-C04, GDPR-C14, CRA-C07, NIS2-C18, AI-C17 → AG-D-01.1-001/-002 → O…”)
7. **CR→Goal** — `PO-D-01.1-001` P2 `MITIGATES` edges
8. **CR→NIST** — `NIST-CSF-PR.DS-01`, `NIST-PF-PR.DS-P1`, `NIST-PF-CT.DP-P2` P2 `MAPS_TO` edges

### CH-02 (CRA): CR-D-01.1-001

1. **CompanyContext** — `CC-SECUREBORDER-2026-001` (P2 node; no outgoing edges — anchor node)
2. **Regulation→Clause** — `CRA-C07` (P1 RegulatoryClause; label “REG-CRA — Art. 13(9)”)
3. **Clause←Evidence** — `EV-D-06.2-001` P1 `CITES_CLAUSE` edge
4. **Sub-domain→AG** — `AG-D-01.1-001`, `AG-D-01.1-002` P1 `YIELDS` edges from `D-01.1`
5. **AG→OBL** — `OBL-D-01.1-001` (P2 Obligation node) — ID-join (control_set.yaml@traceability)
6. **OBL→CR** — `CR-D-01.1-001` — ID-join (control_set.yaml@traceability “GDPR-C04, GDPR-C14, CRA-C07, NIS2-C18, AI-C17 → AG-D-01.1-001/-002 → O…”)
7. **CR→Goal** — `PO-D-01.1-001` P2 `MITIGATES` edges
8. **CR→NIST** — `NIST-CSF-PR.DS-01`, `NIST-PF-PR.DS-P1`, `NIST-PF-CT.DP-P2` P2 `MAPS_TO` edges

### CH-03 (NIS2): CR-D-01.1-001

1. **CompanyContext** — `CC-SECUREBORDER-2026-001` (P2 node; no outgoing edges — anchor node)
2. **Regulation→Clause** — `NIS2-C18` (P1 RegulatoryClause; label “REG-NIS2 — Art. 21(2)(o)”)
3. **Sub-domain→AG** — `AG-D-01.1-001`, `AG-D-01.1-002` P1 `YIELDS` edges from `D-01.1`
4. **AG→OBL** — `OBL-D-01.1-001` (P2 Obligation node) — ID-join (control_set.yaml@traceability)
5. **OBL→CR** — `CR-D-01.1-001` — ID-join (control_set.yaml@traceability “GDPR-C04, GDPR-C14, CRA-C07, NIS2-C18, AI-C17 → AG-D-01.1-001/-002 → O…”)
6. **CR→Goal** — `PO-D-01.1-001` P2 `MITIGATES` edges
7. **CR→NIST** — `NIST-CSF-PR.DS-01`, `NIST-PF-PR.DS-P1`, `NIST-PF-CT.DP-P2` P2 `MAPS_TO` edges

### CH-04 (AIAct): CR-D-01.1-001

1. **CompanyContext** — `CC-SECUREBORDER-2026-001` (P2 node; no outgoing edges — anchor node)
2. **Regulation→Clause** — `AI-C17` (P1 RegulatoryClause; label “REG-AIAct — Art. 15(1)”)
3. **Sub-domain→AG** — `AG-D-01.1-001`, `AG-D-01.1-002` P1 `YIELDS` edges from `D-01.1`
4. **AG→OBL** — `OBL-D-01.1-001` (P2 Obligation node) — ID-join (control_set.yaml@traceability)
5. **OBL→CR** — `CR-D-01.1-001` — ID-join (control_set.yaml@traceability “GDPR-C04, GDPR-C14, CRA-C07, NIS2-C18, AI-C17 → AG-D-01.1-001/-002 → O…”)
6. **CR→Goal** — `PO-D-01.1-001` P2 `MITIGATES` edges
7. **CR→NIST** — `NIST-CSF-PR.DS-01`, `NIST-PF-PR.DS-P1`, `NIST-PF-CT.DP-P2` P2 `MAPS_TO` edges

## §3 Chain summary

| Chain | Regulation | Rule | Clause (P1) | AG (P1) | OBL (P2) | NIST anchors (P2) |
|---|---|---|---|---|---|---|
| CH-01 | GDPR | CR-D-01.1-001 | GDPR-C04 | AG-D-01.1-001 | OBL-D-01.1-001 ✓ | PR.DS-01 / PR.DS-P1;CT.DP-P2 |
| CH-02 | CRA | CR-D-01.1-001 | CRA-C07 | AG-D-01.1-001 | OBL-D-01.1-001 ✓ | PR.DS-01 / PR.DS-P1;CT.DP-P2 |
| CH-03 | NIS2 | CR-D-01.1-001 | NIS2-C18 | AG-D-01.1-001 | OBL-D-01.1-001 ✓ | PR.DS-01 / PR.DS-P1;CT.DP-P2 |
| CH-04 | AIAct | CR-D-01.1-001 | AI-C17 | AG-D-01.1-001 | OBL-D-01.1-001 ✓ | PR.DS-01 / PR.DS-P1;CT.DP-P2 |

## §4 Verification commands

```bash
python3 - <<'PY'
import json
g1 = json.load(open('02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json'))
g2 = json.load(open('02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/data/phase2_graph.json'))
print(sum(1 for l in g1['links'] if l['rel']=='CITES_CLAUSE'), 'CITES_CLAUSE edges')
print(sum(1 for l in g2['links'] if l['rel']=='MAPS_TO'), 'MAPS_TO edges')
PY
```

All node ids in this document were read mechanically from the two graph JSONs and `control_set.yaml` on 2026-09-04 by `scripts/gen_narrative_docs_v0.py`.
