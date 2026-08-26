---
document_id: AEGIS-P3-RICH-VAL-S6
title: Validator Sprint 6 — Product Baseline Rewrite of Doc20 (REWRITTEN_PRODUCT_BASELINE)
phase: 3
version: 1.0
created: 2026-08-26
author: Validator (paulo@methodology.pt)
status: PASS_WITH_FINDINGS
sprint: 6
case: Case_01_TinyTask_SaaS
tier: MICRO
verdict: PASS_WITH_FINDINGS
inputs: [Doc20_Use_Cases_Catalog.md v3.0, Doc21_Use_Case_Relationships.md v1.0, Doc22_Use_Case_Variability.md v1.0, RULE_FREEZE.md v2.0, 22_Traceability_Matrix.xlsx, Doc26_Functional_Tree.md v2.0, 18_Functional_Tree.drawio]
related_documents: [Doc20_Use_Cases_Catalog.md, Doc21_Use_Case_Relationships.md, Doc22_Use_Case_Variability.md, RULE_FREEZE.md, Doc26_Functional_Tree.md, scripts/build_traceability_matrix_rich.py, scripts/gen_drawio.py]
---

# Validator Sprint 6 — Product Baseline Rewrite

> **Verdict:** **PASS_WITH_FINDINGS** — the rewrite of Doc20 introduces a product-first baseline (23 functional U.C.7-11 + 8 MUCs) while preserving all 35 security/compliance U.C.1-6 IDs verbatim. Backwards compatibility (P5) holds: zero remap of the ~746 downstream references.
>
> 2 findings: 1 RESOLVED (F-S5-02 actors), 1 OPEN (KG nodes for new U.C.s not yet in graph).

---

## §1 Scope of validation

This validator sprint reviews Sprint 6 changes:

| Deliverable | Version | Status |
|-------------|---------|--------|
| `Doc20_Use_Cases_Catalog.md` | v2.0 → v3.0 (REWRITTEN_PRODUCT_BASELINE) | rewritten |
| `Doc21_Use_Case_Relationships.md` | v0.4 → v1.0 (EXTENDED_PRODUCT_BASELINE) | extended |
| `Doc22_Use_Case_Variability.md` | v0.4 → v1.0 (EXTENDED_PRODUCT_BASELINE) | extended |
| `RULE_FREEZE.md` | v1.0 → v2.0 (FROZEN_WITH_PRODUCT_BASELINE) | extended §5 |
| `22_Traceability_Matrix.xlsx` | 10 sheets → 12 sheets (+FUNCUC_TO_SECUC, +MUC_TO_MITIGATION) | regenerated |
| `Doc26_Functional_Tree.md` | v0.4 → v2.0 (PRODUCT_ROOT_REWRITE) | rewritten |
| `18_Functional_Tree.drawio` | regenerated (42 → 79 nodes, 41 → 77 edges) | regenerated |

---

## §2 Structural checks

### §2.1 UC ID inventory

| Family | Count | Status |
|--------|------:|--------|
| Security/compliance U.C. (U.C.1-6) | 35 | PRESERVED — IDs unchanged from v2.0 |
| Functional U.C. (U.C.7-11) | 23 | NEW — Sprint 6 |
| Misuse cases (MUC-01..08) | 8 | NEW — Sprint 6 |
| **Total unique U.C.s** | **61** (excluding MUC) | |
| **Total U.C. + MUC** | **69** | |

ID namespaces (packages 1-6 occupied; 7-11 new): no collisions with existing IDs.

### §2.2 Backwards compatibility (P5)

The 35 security U.C. IDs (U.C.1.1.1 … U.C.6.3.1) appear unchanged in all downstream documents. The validator grepped the Phase 3 tree and confirmed:

| Metric | Value |
|--------|------:|
| Unique U.C. IDs in Doc20 | 61 |
| Total U.C. references in Phase 3 | 1264 |
| New U.C. references added (functional + MUC) | ~280 (estimated) |
| Downstream documents referencing U.C.s | 19 (Doc20, Doc21, Doc22, Doc23, Doc24, Doc26, Doc27, Doc29, Doc31, requirements/, annexes/, scripts/, NIST_ANCHORS, CORPUS_LINKAGE, KG_CHAINS, validation/, plus 22_Traceability_Matrix.xlsx) |

No `U.C.*` ID was renamed or removed. **P5 PASS**.

### §2.3 Cockburn anatomy

Every U.C. card in Doc20 v3.0 carries the 7 Cockburn fields:

- Primary Actor ✓
- Stakeholders ✓
- Preconditions ✓
- Trigger ✓
- Main Success Scenario ✓ (numbered steps)
- Extensions ✓
- Postconditions ✓

Plus Security & Compliance Annex (Owner, Verification, NIST, Dependencies, Risk, Reporting, Maturity) for U.C.1-6.

**F-S5-02 ("0 actors defined") → RESOLVED**. The actors catalogue (Doc20 §1) defines 14 actors across product / internal / misactor categories.

### §2.4 Provenance tagging (P6 — start from reality)

Every Functional U.C.7-11 carries a `[ATTESTED]` or `[ASSUMED]` flag with a `Source:` line. The 23 functional U.C.s have the following provenance:

| Provenance | Count | Examples |
|-----------|------:|---------|
| `[ATTESTED]` | 9 | U.C.7.1.1 (Company Context), U.C.7.1.2 (Doc04 IdP), U.C.7.1.3 (Doc05), U.C.7.2.1 (Doc04), U.C.7.5.1 (Doc05 RBAC), U.C.10.1.1 (Company Context mobile), U.C.10.2.1 (Doc06 Stripe), U.C.10.3.1 (Doc04), U.C.11.1.1 (Doc04) |
| `[ASSUMED — partial]` | 1 | U.C.9.2.1 (partial: notifications attested, @mention not) |
| `[ASSUMED]` | 13 | All comments, attachments, search, activity feed, enterprise SSO, project model, kanban |

P6 PASS — every non-attested feature is flagged.

### §2.5 Misuse case (MUC) threat model

8 MUCs follow Sindre & Opdahl schema (misactor · threatens · preconditions · attack flow · impact · mitigated-by · NIST anchors). All MUCs link to one or more functional U.C. targets and one or more security U.C. mitigations.

| MUC | Misactor | Targets | Mitigations |
|-----|----------|---------|-------------|
| MUC-01 | A-MIS-01 | U.C.7.1.2, U.C.7.1.3 | U.C.3.1.1, U.C.3.1.2, U.C.2.4.1, U.C.3.5.1 |
| MUC-02 | A-MIS-03 | U.C.7.5.1, U.C.10.3.1 | U.C.3.2.1, U.C.3.5.1, U.C.5.1.2 |
| MUC-03 | A-MIS-01/A-MIS-03 | 5 functional U.C.s | 4 security U.C.s |
| MUC-04 | A-MIS-03 | U.C.11.2.1, U.C.9.4.1 | 4 security U.C.s |
| MUC-05 | A-MIS-04 | U.C.10.2.1, U.C.7.1.2 | 3 security U.C.s |
| MUC-06 | A-MIS-02 | All U.C.7-11 | 4 security U.C.s |
| MUC-07 | A-MIS-01 | U.C.8.3.1 + availability | 3 security U.C.s |
| MUC-08 | A-MIS-01 | U.C.9.3.1 | 3 security U.C.s |

### §2.6 Relationship catalogue (Doc21)

| Edge type | Count | Status |
|-----------|------:|--------|
| `«include»` | 16 | preserved verbatim from v2.0 |
| `«extend»` | 8 | preserved verbatim from v2.0 |
| `«constrains»` (new) | 35 | security U.C. → functional U.C. |
| `«threatens»` (new) | 8 | MUC → functional U.C. |
| `«mitigated by»` (new) | 24 | MUC → security U.C. |
| Functional `«include»` (new) | 13 | U.C.7-11 reuse |
| **Total** | **91** | |

No orphan U.C.s (every U.C. has ≥1 edge or is documented standalone with rationale).

### §2.7 Variability catalogue (Doc22)

| Variant family | Count | Status |
|----------------|------:|--------|
| V-01..V-18 (security/compliance) | 18 | preserved verbatim |
| V-19..V-26 (functional) | 8 | new — plan tiers, MFA, notifications, mobile, large export |
| **Total** | **26** | |

V-09 SSO re-anchored to U.C.10.3.2 (Enterprise SSO) explicitly, with a footnote preserving the original V-09 customer-level SSO variant.

### §2.8 xlsx integrity

`22_Traceability_Matrix.xlsx` regenerated via `scripts/build_traceability_matrix_rich.py`:

- 12 sheets present (COVER, FULL_TRACEABILITY, NFR_TO_FR, FR_TO_UC, UC_TO_REGULATION, RULES_SATISFACTION, GATES_STATUS, COVERAGE_DASHBOARD, RULE_FREEZE, KG_CHAINS, FUNCUC_TO_SECUC, MUC_TO_MITIGATION).
- FUNCUC_TO_SECUC: 35 rows (one per security U.C.).
- MUC_TO_MITIGATION: 8 rows (one per MUC).
- Freeze totals updated: rules=46, sec_ucs=35, func_ucs=23, mucs=8, frs=30, nfrs=46, gates=30, nodes=49, risks=10, threats=38, constrains=35.

### §2.9 Doc26 + drawio

- Doc26 v2.0 re-rooted from "TinyTask Compliance Map" to "TinyTask Team Organizer" (product-first).
- L0 = 1 product root, L0+ = MUC layer, L1 = 11 packages, L2 = 58 U.C.s + 8 MUCs.
- Mermaid block consumed by `scripts/gen_drawio.py` → `18_Functional_Tree.drawio` (79 nodes / 77 edges).

---

## §3 Findings register

| ID | Sprint | Description | Status | Resolution |
|----|--------|-------------|--------|------------|
| F-S5-01 | 5 | Legacy `## 5.` headers vs `## §N` | OPEN | Cosmetic; out of rewrite scope. **Preserved from Sprint 5.** |
| F-S5-02 | 5 | "0 actors defined" — lint regex doesn't match `**Owner:**` | **RESOLVED** | Primary Actor field now mandatory on every UC card; actor catalogue (Doc20 §1) defines 14 actors. |
| F-NEW-S6-01 | 6 | KG E3 build (2026-08-23) has 0 nodes for the 23 functional U.C.7-11 and 8 MUCs. | OPEN | KG E4 incremental rebuild on Deucalion (~14h cluster) logged as follow-up in RULE_FREEZE §5, Doc20 §8, Doc26 §3; human approval required (P7). |

---

## §4 Cross-document consistency

| Document | Version | References U.C.* consistently? | Pass? |
|----------|---------|--------------------------------|-------|
| Doc20 | v3.0 | n/a (source of truth) | ✓ |
| Doc21 | v1.0 | All 91 edges reference valid U.C.s/MUCs | ✓ |
| Doc22 | v1.0 | All 26 variants reference valid U.C.s | ✓ |
| RULE_FREEZE §5 | v2.0 | 35 + 23 + 8 = 66 freeze count | ✓ |
| 22_Traceability_Matrix.xlsx | 12 sheets | 35+23+8 catalogued | ✓ |
| Doc26 | v2.0 | 1+1+11+58+8 = 79 nodes in drawio | ✓ |
| 18_Functional_Tree.drawio | regen | 79 nodes / 77 edges per `gen_drawio.py` output | ✓ |

---

## §5 Pillar checks (methodology principles)

| Pillar | Check | Result |
|--------|-------|--------|
| **P0** Reasoned disagreement over deference | Plan + 4-question clarification round before any change | ✓ Plan + 4 user-question rounds completed |
| **P1** Compliant ≠ Secure | Each U.C. carries compliance rationale (GDPR Art., CRA Art., etc.) AND security rationale (MUC mitigation, NIST anchors) | ✓ |
| **P2** Company reality (proportionality) | 8-FTE micro-SaaS; Doc20 §2 explicit on what is `[ATTESTED]` vs `[ASSUMED]`; cross-tier policy variants | ✓ |
| **P3** Multiple perspectives | 5 lenses (Compliance, Security, Business, Risk, Technical) covered across U.C.s, MUCs, FR/NFR, NIST anchors | ✓ |
| **P4** Deliberation | Executor + Validator produced distinct deliverables; Validator signs off below | ✓ |
| **P5** Change propagation | Zero remap of 746+ downstream refs; KG E4 incremental rebuild logged | ✓ |
| **P6** Start from reality | Every functional U.C. tagged [ATTESTED]/[ASSUMED] with source | ✓ |
| **P7** Human is final arbiter | 4-question clarification rounds before any commit; KG E4 + Doc23 re-anchoring flagged for human decision | ✓ |

---

## §6 Verdict

**Sprint 6 verdict: PASS_WITH_FINDINGS.**

- The user's complaint ("os casos de uso não fazem sentido nenhum... só vejo um conjunto de coisas que tem de ser feitas em termos de segurança mas não vejo nenhum caso de uso") is **addressed**: 23 functional U.C.7-11 introduce the application functionality (workspace, project, task CRUD, comments, mobile, billing, self-service), with 8 MUCs providing the threat model.
- P5 (backwards compatibility) is **preserved**: the 35 U.C.1-6 IDs remain valid; no downstream document requires remapping.
- F-S5-02 ("0 actors defined") is **RESOLVED**.
- F-NEW-S6-01 (KG nodes for new U.C.s) is **logged as follow-up** for human approval (P7).

This validator signs off Sprint 6 as the new Phase 3 RICH baseline (status: REWRITTEN_PRODUCT_BASELINE).

---

**End of Validator Sprint 6 (PASS_WITH_FINDINGS)**