---
document_id: AEGIS-P3-RICH-ANNEX-D
title: Annex D — KG Inference Examples (Phase 3 RICH)
phase: 3
version: 0.4
created: 2026-08-24
updated: 2026-08-24
author: Sprint 4 Executor (paulo@methodology.pt)
status: ADJUSTED_FIELDS
sprint: 4
sprint_role: schema_adjustment
case: Case_01_TinyTask_SaaS
tier: MICRO
sibling_of: ../03_PHASE2_RULES_RICH/
branch: feature/aegis-p3-case01-rich
sibling_doc: ../03_PHASE3_DECOMPOSITION/annexes/D_KG_Inference_Examples.md
inputs: [13_Use_Cases_Catalog.md, 22_Traceability_Matrix.xlsx, KG_CHAINS.md]
outputs: []
related_documents: [25_Risk_Analysis.md, KG_CHAINS.md]
expected_documents: annex-d
expected_card_columns: 17
expected_compact_columns: 12
schema_columns: 6
schema_columns_list: [Owner, Verification Criteria, Maturity, Priority, Stakeholders, Reporting]
reconciliation_note: "10 SPARQL examples from legacy preserved; 3 Sprint 2 KG chains prepended in §A; F-S1-09 (14 contamination nodes) catalogued; Sprint 4 schema addendum §E added (no markdown tables in this annex; chains presented as code blocks)."
sprint4_note: "Sprint 4: no markdown index tables in this annex; schema addendum §E references the 6 columns inherited from KG_CHAINS.md / Doc 16."
---

# Annex D — KG Inference Examples (Phase 3 RICH)

> **RICH context:** Examples trace through P2-RICH + P3-RICH paths. Source KG: `/home/epmq-cyber/Área de Trabalho/projects/Deucalion/results/graphify/E3_2026-08-23/graphify-out/graph.json` (3882 nodes, 11232 links).

---

## §A KG Chain Examples (Sprint 2)

> 3 examples reproduced from `KG_CHAINS.md` §1. Format: `Start → hop [relation] → ... → End | EXTRACTED/INFERRED`

### §A.1 CH-05: BPR-D-07.1-001 → CR-D-02.1-001 → CRA

```
START: 02_phase2_rules_rich_11_rules_catalog_bpr_d_07_1_001
  →[references, EXTRACTED, §7.2 BPR-D-07.1-001 field 10 Dependencies]→
HOP 1: 02_phase2_rules_rich_11_rules_catalog_cr_d_02_1_001
  →[references, EXTRACTED, §7.1 CR-D-02.1-001 field 4]→
END:   cra
EXTRACTED=2 / INFERRED=0
```

### §A.2 CH-06: BPR-D-01.1-001 → CR-D-01.1-001 → GDPR (cross-domain)

```
START: 02_phase2_rules_rich_11_rules_catalog_bpr_d_01_1_001
  →[references, EXTRACTED, §7.2 BPR-D-01.1-001 field 10 Dependencies]→
HOP 1: 02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001
  →[references, EXTRACTED, §7.1 CR-D-01.1-001 field 4]→
END:   gdpr
EXTRACTED=2 / INFERRED=0
```

### §A.3 CH-12: NODE-PROC-001 → CR-D-04.3-001 (INFERRED, cross-doc)

```
START: node_proc_001_unified_incident_response
  →[references, INFERRED, Doc 14 §8 NODE-PROC-001]→
END:   02_phase2_rules_rich_11_rules_catalog_cr_d_04_3_001
EXTRACTED=0 / INFERRED=1
NOTE: KG-inferred; Sprint 5 verifies by reading Doc 14 §8 NODE-PROC-001.
```

---

## §B KG Schema Overview (legacy preserved)

The TinyTask Knowledge Graph encodes the complete traceability chain from regulations through to compliance gates:

```
┌─────────────────────────────────────────────────────────────────┐
│              TINYTASK KNOWLEDGE GRAPH SCHEMA                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Regulation ──→ Clause ──→ Rule ──→ NFR ──→ FR ──→ UC ──→ Gate│
│       │            │          │         │        │        │     │
│       │            │          │         │        │        │     │
│       ▼            ▼          ▼         ▼        ▼        ▼     │
│    GDPR         Art.32    CR-D-    NFR-    FR-SEC   CG-SEC   │
│    CRA          Annex I   BPR-D-   NFR-    FR-DP    CG-DP    │
│                              │         │        │        │     │
│                              │         │         ▼        │     │
│                              │         │      Threat    Gate   │
│                              │         │         │        │     │
│                              │         │         ▼        │     │
│                              │         │    Mitigation◄──┘     │
│                              │         │         │              │
│                              ▼         ▼         ▼              │
└─────────────────────────────────────────────────────────────────┘
```

---

## §B.1 Example 1: Regulation → Rule chain

```sparql
MATCH (r:Regulation {id: 'gdpr'})-[:has_clause]->(c:Clause {article: 'Art.32'})
      -[:crystallizes]->(cr:ComplianceRule {id: 'CR-D-01.1-001'})
RETURN r.id, c.article, cr.id, cr.title
```

**Expected result (TinyTask freeze):**
- gdpr → Art.32 → CR-D-01.1-001 (Data at Rest Encryption)

---

## §B.2 Example 2: Rule → Use Case chain

```sparql
MATCH (cr:ComplianceRule {id: 'CR-D-03.1-001'})-[:satisfied_by]->(fr:FunctionalReq)
      -[:implemented_by]->(uc:UseCase)
RETURN cr.id, fr.id, uc.id, uc.title
```

**Expected result (TinyTask freeze):**
- CR-D-03.1-001 → FR-01..05 → U.C.3.1.1 / U.C.3.2.1 / U.C.3.5.1

---

## §B.3 Example 3: Risk → Mitigation chain

```sparql
MATCH (risk:Risk {id: 'RISK-01'})-[:mitigated_by]->(gate:ComplianceGate)
      -[:verified_by]->(test:Test)
RETURN risk.id, gate.id, test.method, test.result
```

**Expected result (TinyTask freeze):**
- RISK-01 (MFA bypass) → GATE-CR-D-03.2-001 → TEST → PASS

---

## §B.4 Example 4: NIST CSF anchor chain (RP-3 reverse)

```sparql
MATCH (cr:ComplianceRule)-[:anchored_to]->(csf:NISTCSF {function: 'PR.AA'})
RETURN cr.id, csf.subcategory
ORDER BY cr.id
```

**Expected result:** CR-D-03.1-001 → PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05

---

## §B.5 Example 5: Cross-domain chain (RBAC → Encryption)

```sparql
MATCH (bpr:BestPracticeRule {id: 'BPR-D-03.1-001'})-[:references]->(cr:ComplianceRule)
RETURN bpr.id, cr.id, cr.subdomain
```

**Expected result:** BPR-D-03.1-001 (RBAC) → CR-D-01.1-001 (Encryption, D-01.1) — cross-domain (D-03 → D-01).

---

## §B.6 Example 6: Dual PO/SO coverage (F-02)

```sparql
MATCH (po:PrivacyObjective)-[:derived_from]->(cr:ComplianceRule)
      <-[:derived_from]-(so:SecurityObjective)
RETURN po.id, so.id, cr.id
```

**Expected result:** PO-D-09.1-001 + SO-D-09.1-001 → CR-D-09.1-001 (dual coverage).

---

## §B.7 Example 7: Phantom PO reference (F-03)

```sparql
MATCH (cr:ComplianceRule {id: 'CR-D-01.3-001'})-[:derived_from]->(po:PrivacyObjective)
RETURN cr.id, po.id
```

**Expected result:** NULL — PO-D-01.3-001 is a phantom per F-03 (F-01 carried from Phase 2).

---

## §B.8 Example 8: God-node traversal (RP-7)

```sparql
MATCH (a:Artefact)-[:references]->(g:GodNode {id: 'cra'})<-[:references]-(b:Artefact)
WHERE a.id < b.id
RETURN a.id, b.id, count(*) AS shared_refs
ORDER BY shared_refs DESC
LIMIT 5
```

**Expected result:** Top pairs sharing `cra` references.

---

## §B.9 Example 9: Gate → Rule verification (RP-4)

```sparql
MATCH (g:ComplianceGate {id: 'GATE-CR-D-04.3-001'})-[:verifies]->(cr:ComplianceRule)
RETURN g.id, cr.id, cr.subdomain
```

**Expected result:** GATE-CR-D-04.3-001 → CR-D-04.3-001 (D-04.3 — Incident Notification).

---

## §B.10 Example 10: UC → Package mapping

```sparql
MATCH (uc:UseCase)-[:member_of]->(pkg:Package)
RETURN pkg.id, count(uc) AS uc_count
ORDER BY uc_count DESC
```

**Expected result:**
- PKG-SEC: 7, PKG-IAM: 7, PKG-GOV: 7, PKG-DP: 6, PKG-DEV: 5, PKG-TRN: 3 — total = 35.

---

## §C Contamination Register (F-S1-09)

> **Status:** REPORTED (KG-extraction artefacts; NOT in markdown source).

The Graphify KG carries 14 Case_02 contamination nodes (AI Act, Biometric, Border Control AI, IPSARA, FRIA) pointing at Case_01 Phase 3 paths. Verified by direct grep of legacy Phase 3 markdown: contamination is NOT in the source text. Legacy Doc 13a §5 explicitly disconfirms AI Act applicability for TinyTask ("No NIS 2, DORA, or AI Act applies.").

**Action:** Sprint 5 re-runs Graphify on Case_01 in isolation (Case_02 ontology disabled). If contamination persists, escalate to P7 human arbiter for ontology remediation. See `RULE_FREEZE.md` §4 for full inventory.

---

## §D Cross-references

- `KG_CHAINS.md` §1 — 12 chains (source for §A above)
- `RULE_FREEZE.md` §4 — contamination register
- `25_Risk_Analysis.md` §2 — risk catalogue (RISK-01..10)
- `16_Compliance_Gates_Report.md` §2 — gate catalogue

---

## §E Schema addendum (Sprint 4)

This annex contains 12 KG inference chains and 10 SPARQL examples presented as code blocks (no markdown index tables). The chain-summary schema inherited from `KG_CHAINS.md` §1 covers the 6-column Sprint 4 addition. The canonical chain card fields now include:

| Owner | Verification Criteria | Maturity | Priority | Stakeholders | Reporting |
|-------|-----------------------|----------|----------|--------------|-----------|

These 6 columns are present on the per-chain and per-gate tables in `KG_CHAINS.md` and `16_Compliance_Gates_Report.md` §2 (gates) / §3 (SC1-SC5). Card-level values will be populated in Sprint 5.

---

**End of Annex D — KG Inference Examples (Phase 3 RICH, ADJUSTED_FIELDS, Sprint 4)**
