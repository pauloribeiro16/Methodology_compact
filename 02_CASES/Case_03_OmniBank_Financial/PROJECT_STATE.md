# Project State — Case 03: OmniBank Financial Systems (High Complexity)

**Last Updated:** 2026-08-28
**Status:** 🟢 Phase 1 ✅ COMPLETE (Rich) | Phase 2 ✅ COMPLETE (Rich) | Phase 3 ✅ COMPLETE (Doc22–31) | 🔄 PORT CAMPAIGN Case_01→Case_03 IN PROGRESS (Fases 0–2, Bloco A)
**Next Phase:** Port Fases 3–7 (UNMAPPED adjudication, posture, Control Set, gates, PRODUCTION_FLOW)
**Complexity:** Maximum (5/5 regulations, 38/38 sub-domains)
**Restructured:** 2026-04-02 (v2.0)

> **⚠️ 2026-08-28 (port Fase 0).** The April sections below (§2–§5) are a historical baseline keyed to legacy doc names and April volumes. Current reality on disk: Rich P1 = Doc01–**Doc14** (Doc11_DORA inserted; Doc14_Adjusted_Goals, 76 AG goals), P2 = **Doc16–Doc21** (78 rules = 38 CR + 40 BPR; **5 tensions** T-001..T-005), P3 = Doc22–Doc31 (complete). Canonical narrative layers: the Aug-6/8 Rich campaign, the Aug-13/14 corr-010 wave (renames + AG- migration) and the port campaign started 2026-08-28.

---

## 1. CASE OVERVIEW

### 1.1 Company Profile

| Attribute | Value |
|-----------|-------|
| **Name** | OmniBank Financial Systems S.A. |
| **Location** | Germany (EU), Frankfurt-registered, ECB-supervised |
| **Size** | Large enterprise (5,000+ employees, >€1.5B revenue) |
| **Sector** | Banking & Financial Services (Consumer Credit + Risk Management) |
| **Product** | Mobile banking app + web platform; OmniScore AI (High-Risk credit scoring) |
| **Data Types** | Customer PII, financial transactions, credit scores, behavioral data |
| **Special Category Data** | No (financial data, not Art. 9) |
| **AI/ML Systems** | Yes — OmniScore AI Platform (AI Act Annex III: credit scoring) |

### 1.2 Regulatory Applicability

| Regulation | Applicable? | Role | Clause Count | Sub-Domains Covered |
|------------|-------------|------|--------------|---------------------|
| **GDPR** | ✅ APPLICABLE | Controller | 28 | 19/38 (50.0%) |
| **CRA** | ✅ APPLICABLE | Manufacturer (Standard) | 26 | 22/38 (57.9%) |
| **NIS 2** | ✅ APPLICABLE | Essential Entity | 29 | 24/38 (63.2%) |
| **DORA** | ✅ APPLICABLE | Financial Entity | 38 | 29/38 (76.3%) |
| **AI Act** | ✅ APPLICABLE | Provider (High-Risk) | 29 | 13/38 (34.2%) |
| **TOTAL** | **5/5** | **—** | **150** | **38/38 (100%)** |

### 1.3 Key Characteristics

- **Maximum Complexity:** All 5 regulations apply with zero exclusions
- **Essential Entity:** NIS 2 financial infrastructure with systemic importance
- **High-Risk AI:** Credit scoring per AI Act Annex III
- **DORA Financial Entity:** Credit institution under ECB/BaFin supervision
- **Hybrid Architecture:** On-premise mainframe + EU cloud for AI/analytics
- **Very High Security Maturity:** ISO 27001 certified, dedicated security org 100+ *(legacy design text — superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0, port Fase 4)*

---

## 2. PHASE COMPLETION STATUS

### 2.1 Phase 1 — Contextual Definition (✅ COMPLETE)

| Document ID | Document Name | Status | Last Modified | Version |
|-------------|---------------|--------|---------------|---------|
| **00_COMMON** | | | | |
| 00 | Taxonomy_Reference.md | ✅ COMPLETE | 2026-04-01 | 1.0 |
| 01 | Company_Context.md | ✅ COMPLETE | 2026-04-01 | 1.0 |
| 02 | Regulatory_Mapping_Master.md | ✅ COMPLETE | 2026-04-01 | 1.0 |
| 03 | Design_Decisions_Log.md | ✅ COMPLETE | 2026-04-01 | 1.0 |
| **01_PHASE1_CONTEXT** | | | | |
| 04 | Company_Context_Assessment.md | ✅ COMPLETE | 2026-04-01 | 1.0 |
| 05 | Regulatory_Applicability.md | ✅ COMPLETE | 2026-04-01 | 1.0 |
| 06 | Clause_Mapping_Matrix.xlsx | ✅ COMPLETE | 2026-04-01 | 3.0 |
| 07 | Structured_Compliance_Matrix.md | ✅ COMPLETE | 2026-04-01 | 1.0 |

**Phase 1 Gate:** ✅ **PASS** — 8/8 documents complete, 150 clauses mapped, 38/38 sub-domains covered

### 2.2 Phase 2 — Elaboration & Secure Design (✅ COMPLETE)

| Document ID | Document Name | Status | Last Modified | Version |
|-------------|---------------|--------|---------------|---------|
| **02_PHASE2_RULES** | | | | |
| 08 | Obligation_Derivation.md | ✅ COMPLETE | 2026-04-03 | 1.0 |
| 09 | Strategic_Tensions_Report.md | ✅ COMPLETE | 2026-04-03 | 1.0 |
| 10 | Privacy_Security_Goals.md | ✅ COMPLETE | 2026-04-03 | 1.0 |
| 11 | Rules_Catalog.md | ✅ COMPLETE | 2026-04-03 | 1.0 |
| 12 | Rules_Catalog.xlsx | ✅ COMPLETE | 2026-04-03 | 1.0 |

**Phase 2 Gate:** ✅ **PASS** — 5/5 documents complete, 38 obligations derived, 4 tensions resolved, 63 rules catalogued

### 2.3 Phase 3 — Decomposition & Risk Integration (⏳ PENDING)

| Document ID | Document Name | Status |
|-------------|---------------|--------|
| **03_PHASE3_DECOMPOSITION** | | |
| 13 | Use_Cases_Catalog.md | ⏳ PENDING |
| 14 | Architectural_Nodes.md | ⏳ PENDING |
| 15 | Functional_Tree.md | ⏳ PENDING |
| 16 | Compliance_Gates.md | ⏳ PENDING |
| 17 | NFR_FR_Specification.md | ⏳ PENDING |
| 18 | Risk_Analysis.md | ⏳ PENDING |
| 19 | Traceability_Matrix.md | ⏳ PENDING |
| 20+ | Annexes (Diagrams, KG) | ⏳ PENDING |

**Phase 3 Gate:** ⏳ NOT STARTED

---

## 3. KEY METRICS

### 3.1 Phase 1 Metrics

| Metric | Value |
|--------|-------|
| Total Regulatory Clauses | 150 |
| Sub-Domains Covered | 38/38 (100%) |
| Mean Normative Intensity | 2.858 |
| % Mandatory Clauses | 88.0% |
| Strategic Tensions Identified | 4 |
| Sole Authority Gaps | 0 (all covered) |
| Design Decisions Logged | 13 |

### 3.2 Phase 2 Metrics

| Metric | Value |
|--------|-------|
| Obligations Derived | 38 |
| Mean Obligation NI | 2.934 |
| Strategic Tensions Resolved | 4/4 (100%) |
| Privacy Goals | 11 |
| Security Goals | 22 |
| Total Rules | 63 (38 compliance + 25 best practice) |
| Rules by Priority | P1: 37, P2: 1, P3: 25 |
| Implementation Mode | NATIVE: 28 (73%), HYBRID: 10 (27%) |
| Sole Authority Rules | 3 (D-03.4 CRA, D-05.4 GDPR, D-06.2 CRA) |

### 3.3 Regulatory Contribution (Phase 2)

| Regulation | Clauses | Obligations Involved | % of Obligations |
|------------|---------|---------------------|------------------|
| DORA | 38 | 29/38 | 76.3% |
| NIS 2 | 29 | 24/38 | 63.2% |
| AI Act | 29 | 13/38 | 34.2% |
| CRA | 26 | 18/38 | 47.4% |
| GDPR | 28 | 12/38 | 31.6% |

---

## 4. STRATEGIC TENSIONS RESOLVED

| Tension ID | Type | Severity | Sub-Domain(s) | Resolution | Status |
|------------|------|----------|---------------|------------|--------|
| T-001 | TEMPORAL_CONFLICT | CRITICAL | D-04.3 | Max-SLA Routing (24h universal workflow) | ✅ RESOLVED |
| T-002 | REQUIREMENT_CONFLICT | CRITICAL | D-05.3 vs D-10.2 | Cryptographic Sharding | ✅ RESOLVED |
| T-003 | FREQUENCY_MISMATCH | MEDIUM | D-09.2 | IPSARA Unified Assessment Framework | ✅ RESOLVED |
| T-004 | INTENSITY_GAP | LOW | D-07.1 | Follow CRA secure-by-default standard | ✅ RESOLVED |

---

## 4B. LINTING STATUS

### Lint Restructuring (2026-04-04)

Linting tools restructured from monolithic runner into per-phase runners with auto-discovery of per-document scripts.

**New Commands:**
```bash
# Per-phase (recommended)
python lints/run_structural_lints.py --case "OmniBank Financial Systems"
python lints/run_phase1_lints.py --case "OmniBank Financial Systems"
python lints/run_phase2_lints.py --case "OmniBank Financial Systems"
python lints/run_phase3_lints.py --case "OmniBank Financial Systems"

# Single lint
python lints/run_phase2_lints.py --case "OmniBank Financial Systems" --select rules_catalog

# All phases (backward compatible)
python lints/run_all_lints.py --case "OmniBank Financial Systems"
```

**New Scripts Created:**
- `run_structural_lints.py`, `run_phase1_lints.py`, `run_phase2_lints.py`, `run_phase3_lints.py`
- Phase 2: `lint_08_obligation_derivation.py`, `lint_09_strategic_tensions.py`, `lint_10_goals.py`, `lint_11_rules_catalog.py`
- Phase 3: `lint_13_use_cases.py`, `lint_14_nodes.py`, `lint_15_allocation.py`, `lint_16_gates.py`, `lint_17_functional_tree.py`

**Status:** Phase 1 lints passed; Phase 2 lints pending (new scripts need testing)

---

## 5. CHANGE LOG — CASE 03

### 5.1 Recent Changes

| Date | Document | Change Type | Description | Impact |
|------|----------|-------------|-------------|--------|
| 2026-04-04 | lints/ | TOOLS RESTRUCTURE | Per-phase runners + 9 per-document lint scripts created | High |
| 2026-04-03 | 08_Obligation_Derivation.md | NEW | 38 obligations derived from 150 clauses | High |
| 2026-04-03 | 09_Strategic_Tensions_Report.md | NEW | 4 tensions detected and resolved (2 CRITICAL) | High |
| 2026-04-03 | 10_Privacy_Security_Objectives.md | NEW | 33 goals (11 Privacy + 22 Security) | High |
| 2026-04-03 | 11_Rules_Catalog.md | NEW | 63 rules (38 compliance + 25 best practice) | High |
| 2026-04-03 | outputs/12_Rules_Catalog.xlsx | NEW | Machine-readable rules catalog (4 sheets) | High |
| 2026-04-03 | PROJECT_STATE.md | UPDATE | Phase 1 & 2 marked COMPLETE | Medium |
| 2026-04-02 | All | FOLDER RENAMED | `Caso 3 - High Complexity` → `Case_03_OmniBank_Financial` | Medium |
| 2026-04-02 | PROJECT_STATE.md | RESTRUCTURE v2.0 | Methodology restructured (new directory layout) | High |

### 5.2 Pending Changes

| Priority | Document | Change Required | Reason |
|----------|----------|-----------------|--------|
| HIGH | Phase 3 documents | Create 8+ Phase 3 documents | Phase 3 kickoff required |
| MEDIUM | Document approvals | Sign approval tables | All documents have empty approval signatures |
| LOW | QWEN.md update | Update Case 3 status | Global state needs reconciliation |

---

## 6. NEXT STEPS

### 6.1 Phase 3 Kickoff

| Task | Owner | Dependencies |
|------|-------|--------------|
| Create 03_PHASE3_DECOMPOSITION/ directory | Compliance Lead | Phase 2 complete ✅ |
| Define Architectural Nodes (Doc 14) | Security Architect | Rules Catalog ✅ |
| Define Functional Requirements & Allocate Obligations | Security Architect | Obligation Derivation ✅ |
| Create Use Cases Catalog (Doc 13) | Compliance Lead | Rules Catalog ✅ |
| Define Compliance Gates (Doc 16) | CISO | Functional Requirements |
| Create NFR/FR Specification (Doc 17) | CTO | Use Cases + Nodes |
| Conduct Risk Analysis (Doc 18) | CRO | Functional Tree |
| Build Traceability Matrix (Doc 19) | Compliance Lead | All above |
| Create Annexes (Diagrams, KG) | Security Architect | All above |

### 6.2 Known Issues / Blockers

| Issue | Impact | Mitigation | Status |
|-------|--------|------------|--------|
| AI Governance Lead not hired | HIGH | Required for AI Act conformity assessment | 🔴 OPEN |
| DORA conformity assessment not started | HIGH | Required before DORA compliance deadline | 🔴 OPEN |
| Document approvals not signed | LOW | All Phase 1-2 docs have empty approval tables | 🟡 PENDING |

---

## 7. DOCUMENT LOCATIONS

| Document Type | Path |
|---------------|------|
| **00_COMMON** | `02_CASES/Case_03_OmniBank_Financial/00_COMMON/` |
| **01_PHASE1_CONTEXT_RICH** | `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/` |
| **02_PHASE2_RULES_RICH** | `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/` |
| **03_PHASE3_DECOMPOSITION** | `02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/` (not yet created) |
| **Phase 1 Excel** | `01_PHASE1_CONTEXT_RICH/Case_03_Phase1_RICH.xlsx` |
| **Phase 2 Excel** | `02_PHASE2_RULES_RICH/12_Rules_Catalog.xlsx` |
| **PROJECT_STATE.md** | `02_CASES/Case_03_OmniBank_Financial/PROJECT_STATE.md` |

**Full Path:** `02_CASES/Case_03_OmniBank_Financial/`

---

## 8. CONTACTS & OWNERS

| Role | Responsibility | Contact |
|------|----------------|---------|
| Compliance Lead | Phase 1-2 implementation | compliance@methodology.pt |
| CTO | Technical review, security architecture | security-arch@methodology.pt |
| CISO | Security governance, incident response | ciso@omnibankeu.com |
| DPO | GDPR compliance, data subject rights | dpo@omnibankeu.com |
| AI Governance Lead | AI Act conformity | ai-governance@omnibankeu.com |
| CRO | Risk management, DORA ICT risk | cro@omnibankeu.com |
| AEGIS Methodology Review | Methodology compliance | aegis-review@methodology.pt |

---

**Document Version:** 3.1 (Port campaign Bloco A — Fase 0 state-chain repair)
**Last Reviewed:** 2026-08-28
**Next Review:** Phase 3 Kickoff

## Sprint 0.5 — Port Campaign Case_01→Case_03, Fase 0 (2026-08-28)

- `validation/PORT_census_v0.md` — full baseline: UNMAPPED 262 tokens (AIRMF 140 / PF 91 / CSF 20 / PRIVACY 8 / bare 3), sprint keys, legacy maturi scales (Doc08=158, Doc13=76, Doc20=78), goal census (76 AG verified; PG/SG=0 em deliverables)
- **Adjudicações:** tensões canónicas = **5** (T-005 DORA TLPT integrado no Doc17; claim "7" incorrecto); **AI-C19 MANTÉM-SE** (OmniBank é PROVIDER + DEPLOYER do OmniScore — inverso do D1 do Case_02; 150 cláusulas); PF 1.1 → 1.0 no P2 PS; **corr-012 registado** como pendência formal (split PO/SO adiado — decisão P7 2026-08-28, coerente com TRACEABILITY_AUDIT §5a)
- **Cadeia de estado:** PS do caso 3.1 (banner + realidade Rich/corr-010, dirs `_RICH` no §9); progress.json com backfill Rich + corr-010 + evento Fase 0; P1 PS/README (sprints_complete 0–6, tabela deliverables DocNN, Doc14 ✅)
- **Decisões P7 registadas:** manter AG-D- no P2 (corr-012 adiado); DORA mantém `via_CSF` sem coluna própria; cópia canónica da ontologia = P1 RICH
- **Next:** Fase 1 (sprint sweep, refs legacy, Docs 16/18/20 DRAFT→ACTIVE), Fase 2 (postura P1 + kg_ontology com branch DORA) — Bloco A

## Port Bloco A — Fases 1–2 (2026-08-28)

- **Fase 1 (higiene estrutural):** sprint sweep em deliverables (Doc11/13/14/19/21, SPEC, READMEs, PS); mapeamento legacy→DocNN por conteúdo (slot map C3: Doc12=C2·Doc11 … Doc21=C2·Doc19; 377 refs, 19 basenames); refs a dirs apagados (`../02_PHASE2_RULES/` → `_RICH`, xlsx repoint); Docs 16/17/18/20 DRAFT→ACTIVE com frontmatter de 5 regulações + `case:`; Doc17 v1.1 (T-005)
- **Fase 2 (postura P1 + ontologia):** `/maturi/` purge — Doc05 → `DEPRECATED_FOR_POSTURE` + `posture_owner: Doc21`, Doc08 158 células backfilled, Doc13 76, Doc02/04/06/07/14 reescritos; `phase1_ontology.yaml` v2.0-port — kg_ontology aditivo com **branch DORA** no RegulatoryClause, posture block, invariants (150 cláusulas, 38/38, 76 goals, 5 tensões, `dora_coverage: via_CSF`, AI-C19 KEPT); validação PASS em `01_PHASE1_CONTEXT_RICH/validation/P1_ontology_port_validation.md`
- **P5 record:** kg.sh impact AG-D-05.2-001 / AEGIS-P3-RICH-07c → no match (KG E3 sem nós de Case_03 — sem contaminação F-S1-09)
- **Verification (Bloco A exit):** 0 chaves sprint em deliverables; 0 basenames legacy em Doc*/READMEs (fora 00_Taxonomy_Reference ambíguo e RICH_VS_LEGACY histórico); /maturi/ P1 = só waivers legítimos (nomes reais de folhas xlsx + contexto de superssão); 76 AG goals verificados; YAMLs parseiam
- **Next (Bloco B):** Fase 3 (UNMAPPED P2 — 262 tokens), Fase 4 (postura P2 — Doc21 §4 + Doc20 78 escalas), Fase 5 (Control Set v1 — 78 controlos) 
