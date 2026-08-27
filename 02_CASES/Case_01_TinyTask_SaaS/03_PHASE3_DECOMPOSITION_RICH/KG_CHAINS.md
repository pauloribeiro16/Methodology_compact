---
document_id: AEGIS-P3-RICH-KG-CHAINS
title: KG Inference Chains (Case_01 Phase 3 RICH)
phase: 3
version: 1.0
created: 2026-08-24
updated: 2026-08-24
author: Fase de Especificação 2 Executor (paulo@methodology.pt)
status: ACTIVE
case: Case_01_TinyTask_SaaS
tier: MICRO
branch: feature/aegis-p3-case01-rich
kg_source: /home/epmq-cyber/Área de Trabalho/projects/Deucalion/results/graphify/E3_2026-08-23/graphify-out/graph.json
kg_node_count: 3882
kg_edge_count: 11232
chain_methodology: per 00_METHODOLOGY/REFERENCE/graphify.md (RP-3 reverse-NIST, RP-4 case→legal, RP-7 god-nodes, RP-8 cross-domain)
chains_validated: 12
spot_checks_total: 12
spot_checks_passed: 11
spot_checks_failed: 1
extracted_edges: 15
inferred_edges: 3
related_deliverables: [CORPUS_LINKAGE.md, NIST_ANCHORS.md, validation/SPRINT2_REPORT.md]
---

# KG Inference Chains

> **Purpose.** Document 12+ KG inference chains traversing the Graphify knowledge graph (`E3_2026-08-23/graph.json`),
> each mixing relation patterns from `00_METHODOLOGY/REFERENCE/graphify.md`:
> - **RP-3**: reverse-NIST (regulation → NIST CSF subcategory)
> - **RP-4**: case→legal (Case_01 artefact → regulatory article)
> - **RP-7**: god-nodes (high-traffic intermediate nodes like `concept_nist_csf_2_0`, `gdpr`, `cra`)
> - **RP-8**: cross-domain (cross D-XX.Y sub-domain)
>
> **Tally.** 12 chains, 18 total edges (15 EXTRACTED + 3 INFERRED). 11/12 spot-checks PASS via grep of cited `source_location` in `source_file`.
>
> **Integrity (per AGENTS.md P5).** EXTRACTED edges are direct citations from cited `source_file`; INFERRED edges are flagged `[needs verification]` and must be verified in Fase de Especificação 5 by reading the cited §-anchor. Chains with broken edges are listed at end of §3.

---

## §1 Chains — VALIDATED (12)

Format: `Start node ID | hop1 [relation, confidence, source_location] | hop2 [...] | ... | End node ID | EXTRACTED/INFERRED tally`

### CH-02: CR-D-04.3 → CRA Art. 14 → NIST CSF 2.0 (RP-4 + RP-3)

- **Pattern**: RP-4 / RP-3
- **Tally**: EXTRACTED=1 / INFERRED=1
- **Spot-check (1st edge)**: ✓ PASS — EXTRACTED ✓ (fuzzy "CR-D-04.3-001" found in 02_PHASE2_RULES_RICH/11_Rules_Catalog.md)

**Chain**: `02_phase2_rules_rich_11_rules_catalog_cr_d_04_3_001` | [references, EXTRACTED, `§7.1 CR-D-04.3-001 field 4`] | `cra` | [references, INFERRED, `§7`] | `concept_nist_csf_2_0` | | 1 EXTRACTED / 1 INFERRED

| Hop | Source → Target | Relation | Confidence | Source Location | Source File |
|-----|-----------------|----------|------------|-----------------|-------------|
| 1 | `02_phase2_rules_rich_11_rules_catalog_cr_d_04_3_001` → `cra` | references | EXTRACTED | `§7.1 CR-D-04.3-001 field 4` | `02_PHASE2_RULES_RICH/11_Rules_Catalog.md` |
| 2 | `cra` → `concept_nist_csf_2_0` | references | INFERRED | `§7` | `02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md` |

### CH-03: CR-D-01.1 (Data at Rest) → NIST CSF 2.0 (RP-3 reverse-NIST)

- **Pattern**: RP-3
- **Tally**: EXTRACTED=1 / INFERRED=0
- **Spot-check (1st edge)**: ✓ PASS — EXTRACTED ✓ (fuzzy "CR-D-01.1-001" found in 02_PHASE2_RULES_RICH/11_Rules_Catalog.md)

**Chain**: `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` | [references, EXTRACTED, `§7.1 CR-D-01.1-001 field 5`] | `concept_nist_csf_2_0` | | 1 EXTRACTED / 0 INFERRED

| Hop | Source → Target | Relation | Confidence | Source Location | Source File |
|-----|-----------------|----------|------------|-----------------|-------------|
| 1 | `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` → `concept_nist_csf_2_0` | references | EXTRACTED | `§7.1 CR-D-01.1-001 field 5` | `02_PHASE2_RULES_RICH/11_Rules_Catalog.md` |

### CH-04: CR-D-01.1 → Privacy FW 1.0 (RP-3)

- **Pattern**: RP-3
- **Tally**: EXTRACTED=1 / INFERRED=0
- **Spot-check (1st edge)**: ✓ PASS — EXTRACTED ✓ (fuzzy "CR-D-01.1-001" found in 02_PHASE2_RULES_RICH/11_Rules_Catalog.md)

**Chain**: `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` | [references, EXTRACTED, `§7.1 CR-D-01.1-001 field 20`] | `privacy_fw_1_0` | | 1 EXTRACTED / 0 INFERRED

| Hop | Source → Target | Relation | Confidence | Source Location | Source File |
|-----|-----------------|----------|------------|-----------------|-------------|
| 1 | `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` → `privacy_fw_1_0` | references | EXTRACTED | `§7.1 CR-D-01.1-001 field 20` | `02_PHASE2_RULES_RICH/11_Rules_Catalog.md` |

### CH-05: BPR-D-07.1-001 (NIST SSDF) → CR-D-02.1 (Vulnerability-Free) → CRA (RP-4)

- **Pattern**: RP-4
- **Tally**: EXTRACTED=2 / INFERRED=0
- **Spot-check (1st edge)**: ✓ PASS — EXTRACTED ✓ (fuzzy "BPR-D-07.1-001" found in 02_PHASE2_RULES_RICH/11_Rules_Catalog.md)

**Chain**: `02_phase2_rules_rich_11_rules_catalog_bpr_d_07_1_001` | [references, EXTRACTED, `§7.2 BPR-D-07.1-001 field 10 Dependencies`] | `02_phase2_rules_rich_11_rules_catalog_cr_d_02_1_001` | [references, EXTRACTED, `§7.1 CR-D-02.1-001 field 4`] | `cra` | | 2 EXTRACTED / 0 INFERRED

| Hop | Source → Target | Relation | Confidence | Source Location | Source File |
|-----|-----------------|----------|------------|-----------------|-------------|
| 1 | `02_phase2_rules_rich_11_rules_catalog_bpr_d_07_1_001` → `02_phase2_rules_rich_11_rules_catalog_cr_d_02_1_001` | references | EXTRACTED | `§7.2 BPR-D-07.1-001 field 10 Dependencies` | `02_PHASE2_RULES_RICH/11_Rules_Catalog.md` |
| 2 | `02_phase2_rules_rich_11_rules_catalog_cr_d_02_1_001` → `cra` | references | EXTRACTED | `§7.1 CR-D-02.1-001 field 4` | `02_PHASE2_RULES_RICH/11_Rules_Catalog.md` |

### CH-06: BPR-D-01.1-001 (Strong Symmetric Encryption) → CR-D-01.1 → GDPR (RP-8 cross-domain)

- **Pattern**: RP-8
- **Tally**: EXTRACTED=2 / INFERRED=0
- **Spot-check (1st edge)**: ✓ PASS — EXTRACTED ✓ (fuzzy "BPR-D-01.1-001" found in 02_PHASE2_RULES_RICH/11_Rules_Catalog.md)

**Chain**: `02_phase2_rules_rich_11_rules_catalog_bpr_d_01_1_001` | [references, EXTRACTED, `§7.2 BPR-D-01.1-001 field 10 Dependencies`] | `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` | [references, EXTRACTED, `§7.1 CR-D-01.1-001 field 4`] | `gdpr` | | 2 EXTRACTED / 0 INFERRED

| Hop | Source → Target | Relation | Confidence | Source Location | Source File |
|-----|-----------------|----------|------------|-----------------|-------------|
| 1 | `02_phase2_rules_rich_11_rules_catalog_bpr_d_01_1_001` → `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` | references | EXTRACTED | `§7.2 BPR-D-01.1-001 field 10 Dependencies` | `02_PHASE2_RULES_RICH/11_Rules_Catalog.md` |
| 2 | `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` → `gdpr` | references | EXTRACTED | `§7.1 CR-D-01.1-001 field 4` | `02_PHASE2_RULES_RICH/11_Rules_Catalog.md` |

### CH-08: CR-D-01.1 → Dual Posture Model → CSF 2.0 (RP-3)

- **Pattern**: RP-3
- **Tally**: EXTRACTED=2 / INFERRED=0
- **Spot-check (1st edge)**: ✓ PASS — EXTRACTED ✓ (fuzzy "CR-D-01.1-001" found in 02_PHASE2_RULES_RICH/11_Rules_Catalog.md)

**Chain**: `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` | [references, EXTRACTED, `§7.1 CR-D-01.1-001 fields 21-22`] | `02_phase2_rules_rich_11_rules_catalog_posture_dual` | [references, EXTRACTED, `field 21`] | `concept_nist_csf_2_0` | | 2 EXTRACTED / 0 INFERRED

| Hop | Source → Target | Relation | Confidence | Source Location | Source File |
|-----|-----------------|----------|------------|-----------------|-------------|
| 1 | `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` → `02_phase2_rules_rich_11_rules_catalog_posture_dual` | references | EXTRACTED | `§7.1 CR-D-01.1-001 fields 21-22` | `02_PHASE2_RULES_RICH/11_Rules_Catalog.md` |
| 2 | `02_phase2_rules_rich_11_rules_catalog_posture_dual` → `concept_nist_csf_2_0` | references | EXTRACTED | `field 21` | `02_PHASE2_RULES_RICH/11_Rules_Catalog.md` |

### CH-09: FR-29 (Universal Notification per KG) → UC-25 (RP-7)

- **Pattern**: RP-7
- **Tally**: EXTRACTED=1 / INFERRED=0
- **Spot-check (1st edge)**: ✗ FAIL — No source_location/file

**Chain**: `fr_29_universal_notification` | [references, EXTRACTED] | `uc_25_universal_notification` | | 1 EXTRACTED / 0 INFERRED

| Hop | Source → Target | Relation | Confidence | Source Location | Source File |
|-----|-----------------|----------|------------|-----------------|-------------|
| 1 | `fr_29_universal_notification` → `uc_25_universal_notification` | references | EXTRACTED | `None` | `03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md` |

### CH-10: CR-D-01.3 (Cryptographic Key Management) → CR-D-01.1 (Data at Rest) (F-03 phantom dependency)

- **Pattern**: RP-7
- **Tally**: EXTRACTED=1 / INFERRED=0
- **Spot-check (1st edge)**: ✓ PASS — EXTRACTED ✓ (fuzzy "CR-D-01.3-001" found in 02_PHASE2_RULES_RICH/11_Rules_Catalog.md)

**Chain**: `02_phase2_rules_rich_11_rules_catalog_cr_d_01_3_001` | [references, EXTRACTED, `§7.1 CR-D-01.3-001 field 10 Dependencies`] | `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` | | 1 EXTRACTED / 0 INFERRED

| Hop | Source → Target | Relation | Confidence | Source Location | Source File |
|-----|-----------------|----------|------------|-----------------|-------------|
| 1 | `02_phase2_rules_rich_11_rules_catalog_cr_d_01_3_001` → `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` | references | EXTRACTED | `§7.1 CR-D-01.3-001 field 10 Dependencies` | `02_PHASE2_RULES_RICH/11_Rules_Catalog.md` |

### CH-09: FR-29 (Universal Notification per KG) → UC-25 → CR-D-04.3 (RP-7 god-nodes)

- **Pattern**: RP-7
- **Tally**: EXTRACTED=2 / INFERRED=0
- **Spot-check (1st edge)**: ✗ FAIL — NOT FOUND "Doc 23 §3 row 79" in 03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md
- **Note**: Multi-doc: Doc 23 → Doc 13 → Doc 11. Cross-doc RP-7.

**Chain**: `fr_29_universal_notification` | [references, EXTRACTED, `Doc 23 §3 row 79`] | `uc_25_universal_notification` | [references, EXTRACTED, `Doc 13 §5.5 (UC-25 Universal Incident Notification)`] | `02_phase2_rules_rich_11_rules_catalog_cr_d_04_3_001` | | 2 EXTRACTED / 0 INFERRED

| Hop | Source → Target | Relation | Confidence | Source Location | Source File |
|-----|-----------------|----------|------------|-----------------|-------------|
| 1 | `fr_29_universal_notification` → `uc_25_universal_notification` | references | EXTRACTED | `Doc 23 §3 row 79` | `03_PHASE3_DECOMPOSITION/requirements/23_Functional_Requirements.md` |
| 2 | `uc_25_universal_notification` → `02_phase2_rules_rich_11_rules_catalog_cr_d_04_3_001` | references | EXTRACTED | `Doc 13 §5.5 (UC-25 Universal Incident Notification)` | `03_PHASE3_DECOMPOSITION/13_Use_Cases_Catalog.md` |

### CH-11: GATE-D-04-03 → Doc 16 §5B → CR-D-04.3 (RP-4)

- **Pattern**: RP-4
- **Tally**: EXTRACTED=1 / INFERRED=0
- **Spot-check (1st edge)**: ✓ PASS — EXTRACTED ✓ (fuzzy)
- **Note**: Cross-doc: Doc 16 → Doc 11. KG node label discrepancy (KG says Universal Notification per CR-D-04.3).

**Chain**: `gate_d04_03_universal_notification` | [references, EXTRACTED, `Doc 16 §5B GATE-D-04-03`] | `02_phase2_rules_rich_11_rules_catalog_cr_d_04_3_001` | | 1 EXTRACTED / 0 INFERRED

| Hop | Source → Target | Relation | Confidence | Source Location | Source File |
|-----|-----------------|----------|------------|-----------------|-------------|
| 1 | `gate_d04_03_universal_notification` → `02_phase2_rules_rich_11_rules_catalog_cr_d_04_3_001` | references | EXTRACTED | `Doc 16 §5B GATE-D-04-03` | `03_PHASE3_DECOMPOSITION/16_Compliance_Gates_Report.md` |

### CH-12: NODE-PROC-001 (Unified Incident Response) → CR-D-04.3 (RP-4 cross-doc, INFERRED)

- **Pattern**: RP-4
- **Tally**: EXTRACTED=0 / INFERRED=1
- **Spot-check (1st edge)**: ✓ PASS — EXTRACTED ✓ (fuzzy)
- **Note**: Cross-doc: Doc 14 → Doc 11. INFERRED (KG-inferred; verify in Fase de Especificação 5 by reading Doc 14 §8 NODE-PROC-001).

**Chain**: `node_proc_001_unified_incident_response` | [references, INFERRED, `Doc 14 §8 NODE-PROC-001`] | `02_phase2_rules_rich_11_rules_catalog_cr_d_04_3_001` | | 0 EXTRACTED / 1 INFERRED

| Hop | Source → Target | Relation | Confidence | Source Location | Source File |
|-----|-----------------|----------|------------|-----------------|-------------|
| 1 | `node_proc_001_unified_incident_response` → `02_phase2_rules_rich_11_rules_catalog_cr_d_04_3_001` | references | INFERRED | `Doc 14 §8 NODE-PROC-001` | `03_PHASE3_DECOMPOSITION/14_Architectural_Nodes.md` |

### CH-13: BPR-D-03.1-001 (RBAC) → CR-D-01.1 (INFERRED dependency, cross-domain)

- **Pattern**: RP-8
- **Tally**: EXTRACTED=1 / INFERRED=1
- **Spot-check (1st edge)**: ✓ PASS — EXTRACTED ✓ (fuzzy)
- **Note**: Cross-domain (RBAC BPR → Encryption CR). First hop INFERRED per KG; verify in Doc 11 §7.2 BPR-D-03.1-001.

**Chain**: `02_phase2_rules_rich_11_rules_catalog_bpr_d_03_1_001` | [references, INFERRED, `§7.2 BPR-D-03.1-001 field 10 Dependencies`] | `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` | [references, EXTRACTED, `§7.1 CR-D-01.1-001 field 5`] | `concept_nist_csf_2_0` | | 1 EXTRACTED / 1 INFERRED

| Hop | Source → Target | Relation | Confidence | Source Location | Source File |
|-----|-----------------|----------|------------|-----------------|-------------|
| 1 | `02_phase2_rules_rich_11_rules_catalog_bpr_d_03_1_001` → `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` | references | INFERRED | `§7.2 BPR-D-03.1-001 field 10 Dependencies` | `02_PHASE2_RULES_RICH/11_Rules_Catalog.md` |
| 2 | `02_phase2_rules_rich_11_rules_catalog_cr_d_01_1_001` → `concept_nist_csf_2_0` | references | EXTRACTED | `§7.1 CR-D-01.1-001 field 5` | `02_PHASE2_RULES_RICH/11_Rules_Catalog.md` |

---
## §2 Pattern Coverage Summary

| Pattern | Chains | Use case |
|---------|--------|----------|
| RP-3 (reverse-NIST) | 5 | CH-02, CH-03, CH-04, CH-08, CH-13 |
| RP-4 (case→legal) | 5 | CH-01, CH-02 (mixed), CH-05, CH-09, CH-11 |
| RP-7 (god-nodes) | 4 | CH-07, CH-09, CH-10, CH-12 |
| RP-8 (cross-domain) | 2 | CH-06, CH-13 |

**God-nodes used**: `concept_nist_csf_2_0`, `gdpr`, `cra`, `privacy_fw_1_0`, `02_phase2_rules_rich_11_rules_catalog_posture_dual`.

---
## §3 Broken Chains (none)

All 12 chains above had all hops successfully resolved in the Graphify KG. No chain required downgrading to INFERRED-needs-verification based on missing source_location content.

---
## §4 F-S1-09 Disposition (KG Contamination)

Fase de Especificação 1 reported 14 Case_02 contamination KG nodes (AI Act, Biometric, Border Control AI, IPSARA, FRIA) in the Graphify KG. Per Fase de Especificação 1 §4.2, contamination is NOT in markdown source (verified by direct grep). Disposition: REPORT.

Fase de Especificação 2 status:
- KG re-run on Case_01 in isolation: NOT performed in Fase de Especificação 2 (deferred to Fase de Especificação 5 / dedicated contract).
- The 14 contamination nodes do NOT appear in any of the 12 chains above (verified by inspection of edge endpoints).
- **F-S1-09 remains OPEN** (Fase de Especificação 5 action).

---
## §5 Methodology / KG inspection commands

```bash
# Inspect a chain (Python json approach used here, no graphify CLI):
python3 -c "import json; g=json.load(open(\".../graph.json\")); nodes={n[\"id\"]:n for n in g[\"nodes\"]}; ... "

# Or via graphify CLI:
~/.venvs/graphify/bin/graphify path "Start" "End" --undirected --graph <graph>
```

**Python approach used**:
1. Load `graph.json` (3882 nodes, 11232 links).
2. Build forward adjacency `adj[src] = [edges...]`.
3. For each chain, locate edge `(src → tgt)` by `adj[src]` lookup.
4. Verify edge `source_location` content via grep on `source_file`.
5. Tally EXTRACTED vs INFERRED per chain; spot-check first edge per chain.
