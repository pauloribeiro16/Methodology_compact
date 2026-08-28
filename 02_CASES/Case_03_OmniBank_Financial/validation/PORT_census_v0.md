---
document_id: AEGIS-CASE03-PORT-CENSUS
title: "Port Census v0 — Case_01→Case_03 upgrade campaign baseline"
phase: META
version: 0.1
created: 2026-08-28
updated: 2026-08-28
author: Orchestrator (port campaign, Fase 0)
status: ACTIVE
---

# Port Census v0 — baseline before the Case_01-campaign port (Case_03)

Meta report (not a deliverable). Counts taken 2026-08-28 on the post-corr-010
tree (Aug 13–14 wave already applied: DocNN renames incl. Doc11_DORA insert;
AG- goal migration in P1 done). Recipe and counting basis: same as Case_02
`PORT_census_v0.md` — `grep -o` token occurrences, basis stated.

## 1. UNMAPPED token census (deliverables)

| Variant | Occurrences | Files (lines) |
|---|---|---|
| UNMAPPED_AIRMF | 140 | Doc21 (concentrated), Doc20 |
| UNMAPPED_PF | 91 | Doc21, Doc20 |
| UNMAPPED_CSF | 20 | Doc21 |
| UNMAPPED_PRIVACY | 8 | Doc21 |
| `UNMAPPED_` bare | 3 | Doc20/Doc21 |
| **Total** | **262** | Doc21=176 lines, Doc20=34, Doc14=1, Doc19=1 |

Header claims "justification inline" but only ~2 justification strings exist.
Pseudo-ranges: 0 (verified).

## 2. Sprint frontmatter keys (deliverables)

Doc11 (`sprint: 0.6`, `sprint_role`), Doc13 (`sprint: 0.5`, `sprint_role`,
`sprint_3_*` ×3), Doc14 (`sprint_5_author`, `sprint_6_author`, `sprint_role`),
Doc19 (`sprint: 8`), Doc21 (`sprint: 6`), SPEC (`sprint: 6` L326),
P1 README (`sprints_complete: [0,0.5,0.6,1,2,3]`, `sprint_status`),
P2 README (`sprint: 8` + 3 keys), both PROJECT_STATEs (several).

## 3. Legacy maturity vocabulary

Scales `cur N/4 → tgt N/4`: Doc08=158, Doc13=76, Doc20=78, Doc21=2.
`/maturi/i` lines: Doc05=37, Doc21=12, Doc19=10, Doc13=11, Doc20=25,
Doc02=4, Doc07=3, Doc14=3, Doc08=3, Doc04=2, Doc06=1.
Doc05 status: `DEPRECATED_FOR_MATURITY` + `maturity_owner` (Case_02 standard:
DEPRECATED_FOR_POSTURE + posture_owner). Ontology: no posture block.

## 4. Goal/objective IDs

P1 Doc14: **76 unique `AG-D-XX.Y-001/-002`** (corr-010 migration already
applied 2026-08-14 — port Fase 1 AG recipe is verify-only). PG-/SG-: 0 in
live deliverables (validation reports only). P2 objectives (Doc18) also use
AG-D- — PO/SO split deferred to **corr-012** per TRACEABILITY_AUDIT §5a
(P7 decision 2026-08-28: keep AG-, register corr-012 as formal pending item).

## 5. Adjudicated divergences (Fase 0 fixes)

| Divergence | Evidence | Verdict / Action |
|---|---|---|
| Tensions 4 vs 5 vs 7 | Doc17 has T-001..004; ontology v1.1 declares T-001..T-005 (T-005 = D-02.4 DORA TLPT triennial, added Sprint 0.6); P2 PS/README claim 7 | Canonical = **5** (T-005 is real DORA content). Fix Doc17 + state files |
| AI-C19 deployer | Ontology: `obligated_party: ["PROVIDER","DEPLOYER"]` — OmniBank deploys OmniScore internally | **AI-C19 KEEPS** (inverse of Case_02's D1). 150 clauses unchanged; documented as the D1-analog inverse decision |
| `NIST_Privacy_FW_1.1` | P2 PROJECT_STATE frontmatter L21 | → `NIST_Privacy_FW_1.0` (canonical frozen list) |
| "63 rules / 33 goals / Phase 3 pending" in case PS | Actual: 78 rules (38 CR + 40 BPR), 76 AG goals, P3 built (Doc22–31) | State-chain repair |
| Doc20 banner points to deleted `../02_PHASE2_RULES/` | Doc20 L1 | Rewire to `_RICH` tree |
| Ontology copies diverge | 00_COMMON (Jul 7, 1696 ln) vs P1 RICH (Aug 6, 1766 ln, v1.1) | P1 RICH copy declared canonical; 00_COMMON copy = frozen legacy |
| Legacy `../..` links / `00_METHODOLOGY/REFERENCE|SCHEMA` refs | P1/P2 READMEs, frontmatters | Fase 1 repair or mark as upstream-corpus references |

## 6. Verified non-issues (for the record)

- Pseudo-ranges: 0. P1 sprint keys inside `status_history` inline entries: none found beyond those listed in §2.
- DocNN renames complete (P1 Doc01–14 incl. Doc11_DORA, P2 Doc16–21, P3 Doc22–31).
- 8-field frontmatter present on all deliverables (content-freshness gaps in §5).
- Slot map (content-verified): C3 Doc12=C2 Doc11, Doc13=C2 Doc12, Doc14=C2 Doc13,
  Doc16–21=C2 Doc14–19; C2 Doc20_NIST_Framework_Inputs has no C3 counterpart
  (not created — port rule: map by content, not number).

## 7. Gap list vs the Case_02 post-port standard

Census/adjudication UNMAPPED + §4.6 vocabulary; posture model adoption
(P1+P2); Control Set v1 + build script + both gates; PRODUCTION_FLOW.md;
kg_ontology instance (needs **DORA branch** in RegulatoryClause pattern);
frozen AI RMF usage (real anchors kept, 23 CR-without-AI-C* candidates for
`N/A (non-AI scope)`); state-chain freshness; corr-012 registration.
