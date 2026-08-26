---
document_id: AEGIS-P2-RICH-14-NIST-INPUTS
title: NIST Framework Inputs — Cross-Reference & Provenance
phase: 2
version: 1.1
created: 2026-08-11
updated: 2026-08-13
author: Mavis (auto-generated cross-reference doc)
status: ACTIVE
case: Case_02_SecureBorder_Solutions
applicable_regs: [GDPR, CRA, NIS_2, AI_Act]
inputs:
  - 13_Framework_Mapping_Matrix.md
  - 00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAY_AI_Act_v2024.md
  - 00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAY_NIST_CSF_2.0.md
  - 00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAY_NIST_PF_1.1.md
  - 00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAY_NIST_AI_RMF_1.0.md
  - 00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/VERSION_CHANGELOG.md
outputs:
  - (none — this is a cross-reference doc, not a derivation source)
related_documents:
  - 13_Framework_Mapping_Matrix.md
  - 08_Obligation_Derivation.md
  - 10b_Privacy_Security_Goals_NIST_Implications.md
  - 11_Rules_Catalog.md
  - 05_Regulatory_Applicability.md
supersedes: none
---

# NIST Framework Inputs — Cross-Reference & Provenance

> **Purpose of this document:** Explain how the NIST frameworks (CSF 2.0, PF 1.0, AI RMF 1.0) are integrated into the AEGIS Case_02 corpus — **without duplicating content** that already exists in `13_Framework_Mapping_Matrix.md` and elsewhere.
>
> **Note (2026-08-13, R9 of remediation contract):** Doc 14 now aligns with the canonical PF 1.0 (`NIST_PF_1.0_subcategories.md` — 100 subcats, ACTIVE). The historical PF 1.0→1.1 delta is preserved only as a note (see §3 raw materials and §7 exclusions); `OVERLAY_NIST_PF_1.1.md` exists for future migration reference but is NOT the canonical frozen list used by the Case_02 corpus.
>
> This document is **read-after** the others. It is a navigation map.

## 1. Architecture (the "why" of the structure)

The AEGIS methodology uses a **3-layer model** for external frameworks:

```
┌──────────────────────────────────────────────────────────┐
│ Layer 1 — AEGIS 10×38 (CORE, imutável)                   │
│ Taxonomia canónica dos sub-domínios funcionais.         │
│ Não menciona NIST. Não menciona regulamentos.            │
└──────────────────────────────────────────────────────────┘
                          ▲
                          │ indexa por D-XX.Y
                          │
┌──────────────────────────────────────────────────────────┐
│ Layer 2 — Regulations Overlay (legal, obrigatório)       │
│ Para cada D-XX.Y, lista que regulamentos obrigam.         │
│ AI Act, GDPR, CRA, NIS 2, DORA.                          │
│ ESTE DOCUMENTO referencia esta camada.                   │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ Layer 3 — NIST Frameworks Overlay (best practice, opt)   │
│ Para cada D-XX.Y, lista que subcats NIST ajudam a         │
│ implementar. CSF 2.0, PF 1.0 (canónico, ACTIVE), AI RMF 1.0. │
│ PF 1.0→1.1 delta preservado em `OVERLAY_NIST_PF_1.1.md` para │
│ referência de migração futura. Versionado em VERSION_CHANGELOG.md. │
└──────────────────────────────────────────────────────────┘
```

**Why layered?** A taxonomia AEGIS (Layer 1) nunca muda quando NIST ou regulamentos evoluem. Os overlays (Layers 2 e 3) são atualizados independentemente. Esta separação é o que permite manter 3 casos (TinyTask, SecureBorder, OmniBank) sem refazer tudo.

## 2. What is where (the navigation map)

| Pergunta | Onde está a resposta | Ficheiro |
|---|---|---|
| Quais regulamentos se aplicam ao SecureBorder? | §3.1–§3.4, §8.5-A..D | `05_Regulatory_Applicability.md` |
| Que obligations derivam dos 4 regulamentos? | §11.1–§11.4 | `08_Obligation_Derivation.md` |
| Que tensões há entre regulamentos? | (T-001..T-004) | `09_Strategic_Tensions_Report.md` |
| **Como é que AI Act Art. X mapeia para AIGIS D-XX.Y?** | (este doc) | **`OVERLAYS/OVERLAY_AI_Act_v2024.md`** |
| **Como é que CSF/PF/AI RMF subcats mapeiam para D-XX.Y?** | (este doc) | **`OVERLAYS/OVERLAY_NIST_*.md` (3 ficheiros: CSF 2.0, PF 1.0/1.1, AI RMF 1.0)** |
| **Que mudou entre PF 1.0 e 1.1?** | §3 (raw materials) | **`VERSION_CHANGELOG.md` (PF 1.1 é delta histórico, NÃO o canónico)** |
| **Que regras concretas (CR/BPR) derivam das obligations?** | §4, §5 | `11_Rules_Catalog.md` |
| **Que maturity tem cada control?** | §4, V4 | `13_Framework_Mapping_Matrix.md` |
| **Que goals NIST-aligned temos para cada PO/SO?** | (todos) | `10b_Privacy_Security_Goals_NIST_Implications.md` |
| **Que gaps NIST-identified temos (CSFs não cobertas)?** | §6 | `13_Framework_Mapping_Matrix.md` |

**Regra de ouro:** se o leitor procura um mapeamento, vai aos `OVERLAYS/*.md`. Se procura regras, vai ao `11_Rules_Catalog.md`. Se procura obligations, vai ao `08_Obligation_Derivation.md`. **Nunca duplicar conteúdo entre eles.**

## 3. NIST Input files (raw materials)

Localizados em `00_METHODOLOGY/PREPROCESSING_by_domain/`:

| `NIST-Privacy-Framework-V1.0-Core.xlsx` | PF 1.0 canónico (N=100 subcats) — ACTIVE FROZEN LIST | Não diretamente — usado como input para o mapping | (via `PF 1.0 and 1.1_Core Mapping.xlsx`) |
| `PF 1.0 and 1.1_Core Mapping.xlsx` | Delta 1.0→1.1 do NIST (N=100→138, +38 novas) | Extraído para `pf_delta.json` (reference apenas) | `VERSION_CHANGELOG.md` §3 (PF 1.1 NÃO é o canónico; consultar `NIST_PF_1.0_subcategories.md`) |
| `nist_ai_rmf_playbook.xlsx` | Playbook AI RMF 1.0 (GOVERN/MANAGE/MEASURE/MAP × about/actions/doc/ref) | Mapeamento para AIGIS D-XX.Y (filtrado) | `OVERLAY_NIST_AI_RMF_1.0.md` |

**Importante:** estes são **inputs**, não outputs. Não devem ser editados, só consultados. Se o NIST publicar nova versão, **adicionar novo ficheiro** (e atualizar `VERSION_CHANGELOG.md`).

## 4. How to navigate the SecureBorder corpus (read order for reviewers)

1. **`00_VISUALISATIONS/Case_02_P1_Dashboard.html`** (se existir) — orient by doc
2. **`01_PHASE1_CONTEXT_RICH/05_Regulatory_Applicability.md`** §3.5 — o que se aplica (AI Act + GDPR + CRA + NIS 2)
3. **`01_PHASE1_CONTEXT_RICH/05_Regulatory_Applicability.md`** §8.5-D — os 29 AI Act articles
4. **`OVERLAYS/OVERLAY_AI_Act_v2024.md`** — AI Act filtrado ao SecureBorder
5. **`02_PHASE2_RULES_RICH/08_Obligation_Derivation.md`** §11.4 — 14 obligations AI Act
6. **`02_PHASE2_RULES_RICH/11_Rules_Catalog.md`** — 38 CR + 15+ BPR (com AI-specific)
7. **`02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md`** — Unified NIST view (CSF + PF + AI RMF)
8. **`OVERLAYS/OVERLAY_NIST_*.md`** (3 ficheiros) — extrações filtradas por relevância
9. **`02_PHASE2_RULES_RICH/10b_Privacy_Security_Goals_NIST_Implications.md`** — PO/SO com NIST implications
10. **`02_PHASE2_RULES_RICH/09_Strategic_Tensions_Report.md`** — T-001..T-004 (T-001=incident, T-002=retention, T-003=DPIA+FRIA, T-004=jurisdição)

## 5. Validation against `13_Framework_Mapping_Matrix.md`

The 38 CR rows in `13_Framework_Mapping_Matrix.md` §1 already contain the full mapping:
- AIGIS D-XX.Y
- Source regulations
- CSF 2.0 subcats
- Privacy FW 1.0 subcats
- AI RMF 1.0 subcats
- Normative intensity (csf_norm, priv_norm, airmf_norm)

The **3 OVERLAY_NIST_*.md** files I generated are **filtered extractions** of the same data, scoped to:
- **OVERLAY_NIST_AI_RMF_1.0.md** → only CR with AI-C* source (14 of 38)
- **OVERLAY_NIST_PF_1.1.md** → only CR with GDPR source (19 of 38); PF 1.0 é o canónico (`NIST_PF_1.0_subcategories.md`), este overlay é delta histórico (1.1) para migração futura
- **OVERLAY_NIST_CSF_2.0.md** → all 38 CR

**No new mapping is introduced** by the OVERLAY files. They are a different **view** of the same data, organised by NIST framework instead of by AIGIS sub-domain. This is by design — the reader picks the lens that matches their question.

**Validation result:** the 3 OVERLAY_NIST_*.md files **are consistent** with `13_Framework_Mapping_Matrix.md` §1, §3.1, §3.2. Spot-checks on 5 random rows show identical CSF/PF/AI RMF subcat strings.

## 6. Gaps & future work

### 6.1 Known gaps (not in this iteration)

- **NIST GenAI Profile (Jul 2024)** — not extracted. If SecureBorder adds GenAI components, this profile becomes relevant. Suggested next input file.
- **NIST SP 800-53 Rev. 5** — referenced in `13_Framework_Mapping_Matrix.md` but not extracted as overlay (already integrated via `10b_Privacy_Security_Goals_NIST_Implications.md` references).
- **ISO/IEC 42001 (AIMS)** — AEGIS 10×38 is designed to accommodate it (D-09.1 + D-09.2 + D-10.x), but no formal mapping yet.

### 6.2 Recommended next steps

1. **Migrate this doc into the Case_01 corpus** (TinyTask) once Phase 1 dashboard is approved.
2. **Add the GenAI Profile** when SecureBorder or any case introduces GenAI.
3. **Add ISO/IEC 42001 overlay** if/when the Case 03 (OmniBank) is processed (financial sector with AI risk management certification potential).
4. **Validate Case_03 mappings** (OmniBank) when it reaches Phase 2.

## 7. What is intentionally NOT in this document

- ❌ Per-article AI Act analysis (already in `05_Regulatory_Applicability.md` §8.5-D)
- ❌ Per-CR NIST mapping (already in `13_Framework_Mapping_Matrix.md` §1)
- ❌ Per-rule implementation guidance (already in `11_Rules_Catalog.md` §8)
- ❌ PF 1.0→1.1 raw delta table (extracted to `pf_delta.json`; summary in `VERSION_CHANGELOG.md` §3; PF 1.0 é canónico, PF 1.1 é delta apenas)
- ❌ Re-derivation of the AIGIS 10×38 taxonomy (out of scope; the taxonomy is the AEGIS core, not Case_02 specific)

## 8. Version history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-08-11 | Mavis (cross-reference generator) | Initial — links the 3 OVERLAY files, VERSION_CHANGELOG, and Case 02 corpus docs into a single navigation map |
| 1.1 | 2026-08-13 | Executor (R9 of remediation contract) | C2-MED-1: aligned Doc 14 to canonical PF 1.0 (was declaring PF 1.1). PF 1.1 retained only as historical delta note (`OVERLAY_NIST_PF_1.1.md`, `pf_delta.json`); canonical frozen list is `NIST_PF_1.0_subcategories.md` (100 subcats, ACTIVE). |
