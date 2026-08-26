---
document_id: AEGIS-P2-RICH-SPEC-01-CASE03
title: "Specification — Phase 2 Case_03: Unified NIST Matrix (CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0; DORA via CSF)"
type: SPECIFICATION
status: ACTIVE
scope: Case_03_OmniBank_Financial
audience: Executor (sub-agent or operator)
branch_target: feature/aegis-p2-case03-csf-pf-airmf
created: 2026-08-07
updated: 2026-08-08
author: Orchestrator (Case_03 specification consolidation session)
decisions_count: 17
purpose: >
  Auto-contido. O Executor lê este ficheiro + os ficheiros do repo que ele
  referencia e executa todo o trabalho sem reabrir decisões nem re-explorar o
  repo. Única fonte de verdade para este contracto.
anti_pattern_note: >
  Este documento é uma SPECIFICAÇÃO, não um artefacto metodológico. Não conta
  para os docs-oficiais da fase. O Executor NÃO deve tratá-lo como Doc 13 —
  Doc 13 é um OUTPUT desta especificação (ver §5.2).
---

# Specification — Phase 2 Case_03: Unified NIST Matrix

> **Lê-me primeiro.** Este documento fecha 17 decisões tomadas em sessão de
> orquestração para o caso Case_03. Está escrito para que um Executor execute do
> início ao fim sem perguntas. Se algo parecer ambíguo, o problema é desta spec —
> sinaliza no commit message e decide a interpretação mais alinhada com o §3
> (princípio arquitectural). Não reinventes decisões já fechadas em §2.

> **Diferença chave vs Case_01/02 SPEC:** Case_03 é o caso **MAX complexity**
> (5 regulations applicable: GDPR + CRA + NIS 2 + **DORA** + AI Act). DORA não
> tem mapeamento 1:1 para um framework NIST específico; é coberto via CSF
> subcats (per §4.4). Os 3 frameworks NIST mapeáveis (CSF + PF + AI RMF) são
> todos ACTIVE. A maturity model é TRIPLE (3 scores independentes por controlo).

---

## Como ler este documento

1. **Lê §1** (contexto) e **§2** (decisões) — 5 minutos.
2. **Lê §3** (princípio arquitectural) — é o teste de coerência para cada decisão.
3. **Antes de executar qualquer bloco: lê §4** (vocabulário dos frameworks) e
   **§5** (artefactos) — são a especificação detalhada do *quê*.
4. **Lê §6 e §7** — são a especificação do *como* (regras NI e maturidade).
5. **Segue §8** (blocos) em ordem estrita. Não saltes blocos.
6. **Valida com §9** antes de declarar pronto.
7. **Cumpre §11** (checklists) e §13 (branch).

**Convenções tipográficas:**
- `caminho/relativo.md` — caminho relativo à raiz do repo, salvo indicação.
- `DEVE` / `NÃO DEVE` — imperativo normativo (RFC 2119-style).
- `Bloco X` — unidade de trabalho atómica (§8).
- `CR` / `BPR` — Compliance Rule / Best Practice Rule (ver Apêndice A).

> ✅ **UPDATE 2026-08-07 — Baseline NIST mappings concluídos (branch `feature/aegis-baseline-nist-mappings`).**
> Os mapeamentos fundacionais que este spec assumia como pré-requisitos **já existem**:
> - Frozen lists: `00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md` (138 subcats) e `00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md` (72 subcats).
> - GDPR→Privacy FW: `00_METHODOLOGY/PREPROCESSING/Regulation/GDPR/02b_SecurityRules_NISTPF.md` (68 SR, 100% cobertura).
> - AI Act→AI RMF: `00_METHODOLOGY/PREPROCESSING/Regulation/AI_Act/02b_SecurityRules_NISTAIRMF.md` (24 SR, 41/72 subcats AI RMF).
>
> **Nota DORA:** DORA não tem mapeamento NIST directo. É coberto via CSF subcats (PR.DS-*, PR.AA-*, DE.CM-*, RS.MA-*, RC.RP-*) e documentado no `06b_DORA_ICT_Risk_Framework.md` (Phase 1).
>
> **Nota de localização:** as frozen lists vivem em `00_METHODOLOGY/PREPROCESSING/` (ao lado do `NIST_CSF_2.0_subcategories.md` canónico), NÃO em `03_REFERENCE_MATERIAL/Framework_Mappings/NIST_Privacy_Framework/`.
>
> O Bloco 0 deste spec (criar vocabulário Privacy FW) **está portanto dispensado** — passa-se directamente ao Bloco A.

---

## Índice

- §1 Contexto & motivação
- §2 Decisões consolidadas (17)
- §3 Princípio arquitectural
- §4 Especificação dos frameworks (vocabulário)
- §5 Artefactos a produzir
- §6 Regra MUST/SHOULD/COULD (semântica operacional)
- §7 Modelo de maturidade tripla
- §8 Blocos de trabalho (plano de execução)
- §9 Critério "pronto" (validação)
- §10 Riscos & decisões diferidas
- §11 Checklists do Executor
- §12 Apêndices (glossário, caminhos, exemplos)
- §13 Branch & execução

---

## §1 — Contexto & motivação

### 1.1 O que é a AEGIS (resumo de 1 parágrafo)

A AEGIS é uma metodologia de investigação (doutoramento) que mapeia 5 regulamentos
EU (GDPR, CRA, NIS 2, DORA, AI Act) a 38 sub-domínios de segurança, em 3 fases:
**UNDERSTAND** (Phase 1) → **DERIVE** (Phase 2) → **DECOMPOSE** (Phase 3). O
"software" é tooling de validação/linting sobre documentos Markdown estruturados,
não software tradicional. O MANIFESTO declara: *"Regulations are inputs, not
checklists. We derive controls from obligations, not from compliance frameworks."*

### 1.2 O problema actual no Case_03 (4 lacunas, MAX complexity)

Após a exploração do Phase 1 e Phase 2 legacy do Case_03, identificámos quatro lacunas:

| # | Lacuna | Sintoma observado | Onde |
|---|---|---|---|
| L1 | **MUST/SHOULD informal** | BPR = P3 uniforme, sem `normative_intensity` formal. Case_03 tem `AVG_with_AI_MUST + DORA uniformly MUST` — 38 DORA cláusulas todas NI=3, 29 AI Act cláusulas todas NI=3. | Doc 11 §4/§5 |
| L2 | **Maturidade deslocada** | Modelo 0-4 vive no Doc 04b com `phase: 1`, mas `PHASE1_STRATEGY.md §7` diz *"Phase 1 does NOT assess control maturity (Phase 2)."* | Doc 04b |
| L3 | **Diferenciação não demonstrável** | MANIFESTO tem retórica forte mas sem demonstração operacional vs. análise compliance+maturidade convencional. | — |
| L4 | **DORA sem framework específico** | DORA não tem 1:1 NIST mapping; é coberto via CSF subcats. Sem documento a explicar essa cobertura, gera confusão. | Doc 13 §1 |

### 1.3 O que JÁ existe e NÃO DEVE ser recriado

O Executor **NÃO DEVE** reconstruir o seguinte — está feito e é input:

| Artefacto | Caminho | Estado | Reutilização |
|---|---|---|---|
| Lista frozen CSF 2.0 (106 subcats) | `00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md` | ACTIVE | Vocabulário controlado |
| Lista frozen Privacy FW 1.0 (138 subcats) | `00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md` | ACTIVE | Vocabulário controlado |
| Lista frozen AI RMF 1.0 (72 subcats) | `00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md` | ACTIVE | **ACTIVA em Case_03** |
| Crosswalk AEGIS↔frameworks (38/38) | `03_REFERENCE_MATERIAL/Framework_Mappings/Framework_Crosswalk_ARM.md` | **ACTIVE v1.0** (from Case_02) | Reutilizar promoção (D17) |
| Doc 11 — 78 cartões (38 CR + 40 BPR) | `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES/11_Rules_Catalog.md` | DEEP_ENRICHED | Estender (§5.3) |
| Doc 12 — Excel | `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES/12_Rules_Catalog.xlsx` | — | Estender com novas folhas (§5.6) |
| Doc 04b — Security Posture | `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/04b_Security_Posture.md` | ACTIVE, `phase: 1` | Deprecar para input-only (§5.4) |
| DORA ICT Risk Framework | `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/06b_DORA_ICT_Risk_Framework.md` | ACTIVE | Read-only — DORA-specific framework |
| Phase 1 ontology (150 cláusulas) | `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` | ACTIVE | Read-only |

### 1.4 O que falta (4 itens)

1. **Matriz unificada + Govern consolidada (3 frameworks)** — Doc 13 novo (§5.2).
2. **Maturidade tripla por-controlo** — modelo novo (§7).
3. **NI formal AVG + AI/DORA MUST override nos cartões** — campos novos no Doc 11 (§5.3).
4. **Sub-domínios activos mapeados explicitamente** — 38/38 active (todos RIGOROUS/STANDARD; sem DEFERRED per Track B).

---

## §2 — Decisões consolidadas (17 respostas)

| # | Decisão | Escolha | Justificação | Implicações |
|---|---|---|---|---|
| D1 | Âmbito de execução | **Só Case_03** | Piloto MAX complexity; Case_01/02 são outros contractos | Não tocar Case_01/02 |
| D2 | Abordagem ao catálogo | **Híbrido: derivação AEGIS + CSF 2.0 como pivô** | Mantém identidade AEGIS; CSF dá esqueleto comparável | Frameworks = alvo de mapeamento, não fonte |
| D3 | Maturidade | **Mover p/ Phase 2 + expandir tripla** | Resolve contradição PHASE1_STRATEGY §7 | Doc 04b deprecado; Doc 13 assume tripla maturidade |
| D4 | Argumento "AEGIS vs. convencional" | **Documento académico separado (tese)** | Repo fica neutro | Não escrever argumentação no repo |
| D5 | Frameworks NIST a usar | **CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0** (TODOS 3 ACTIVE; DORA via CSF) | Case_03 MAX: 5 regulations, AI Act + DORA applicable | Doc 13 §1 = matriz com colunas dos 3 frameworks + DORA coverage nota |
| D6 | Articulação estrutural | **Matriz unificada** | Vista única evita triplicação | Doc 13 §1 = matriz com colunas de cada framework |
| D7 | Função Govern sobreposta | **Vista Govern consolidada (3 frameworks)** | Os 3 frameworks têm Govern | Doc 13 §2 = Govern fundida (GV ∥ Govern-P ∥ GOVERN) |
| D8 | Papel dos frameworks | **Só alvo de mapeamento** | MANIFESTO intacto; AEGIS deriva da lei | CR/BPR não se derivam de frameworks |
| D9 | AI RMF no Case_03 | **ACTIVE (não placeholder)** | Case_03 tem IA (credit scoring); AI Act applicable | Schema com 3 colunas populated |
| D10 | Escala de maturidade | **Tiers 1-4 + 0-4 nos 3 frameworks** | Comparabilidade directa CSF ↔ Privacy ↔ AI RMF | Definir 0-4 por-subcat para cada framework |
| D11 | Score por controlo multi-framework | **TRÊS scores (csf + privacy + ai_rmf)** | Preserva dessincronia segurança/privacidade/IA | 6 campos de maturidade por cartão |
| D12 | Govern no Case_03 (3 frameworks) | **3 colunas populated** | Método completo | Coluna AI RMF = mapeamento real |
| D13 | Estrutura do mapeamento | **n:m flexível** | Captura multi-mapping realista | Cada CR/BPR → lista de subcats por framework |
| D14 | Vocabulário Privacy FW | **Lista frozen completa** | Consistência com tratamento CSF | Lista já existe |
| D15 | Onde vive a matriz | **Doc 13 novo consolidado** | Centralização | Doc 13 = 6 sub-secções + 2 viz (§5.2) |
| D16 | Critério "pronto" | **100% CR + coerência BPR** | MUST tem de mapear; SHOULD pode não mapear | Validação em §9 |
| D17 | Branch | **`feature/aegis-p2-case03-csf-pf-airmf`** | Política 1-branch-per-contract | Bloco A REUSED from Case_02 (Crosswalk já ACTIVE) |

---

## §3 — Princípio arquitectural

### 3.1 Frase-mestra

> AEGIS deriva obrigações da lei → traduz em **CR (MUST, NI=3)** e **BPR (SHOULD,
> NI=1-2)** → ancora cada regra aos 38 sub-domínios → mapeia cada sub-domínio em
> paralelo ao **CSF 2.0** (eixo segurança), **Privacy FW 1.0** (eixo privacidade)
> e **AI RMF 1.0** (eixo IA), com **DORA coberto via CSF** subcats → mede
> **maturidade tripla por-controlo** (Tiers 1-4 no programa/Function; 0-4
> por-subcategoria no controlo) → liga tudo a ISO/secure-development standards via crosswalk já existente.

### 3.2 Diagrama de fluxo

```
         REGULAÇÃO (GDPR + CRA + NIS 2 + DORA + AI Act aplicáveis ao Case_03)
              │
              ▼  (derivação AEGIS — intacta, MANIFESTO)
        OBRIGAÇÕES (Doc 08) → CR (MUST, NI=3) + BPR (SHOULD, NI=1-2)
              │                          │
              │   Tensões (Doc 09) ◄─────┤
              │                          │
              ▼                          ▼
        PG/SG (Doc 10) ◄──────────  78 CARTÕES (Doc 11)
              │                          │
              │   38 sub-domínios (Taxonomia D-01.1 … D-10.3)
              │   38/38 active (sem DEFERRED per Track B)
              │                          │
              │           MATRIZ UNIFICADA (Doc 13) ◄── NESTE CONTRACTO
              │                          │
              │           ┌──────────────┼──────────────┐
              │           ▼              ▼              ▼
              │        CSF 2.0      PRIVACY FW 1.1   AI RMF 1.0
              │     GV ID PR DE RS RC  ID-P GV-P CT-P CM-P PR-P   GOVERN MAP MEASURE MANAGE
              │           │              │              │
              │     ┌─────┴──────┐       │              │
              │     │ DORA via   │       │              │
              │     │ CSF subcats│       │              │
              │     └───────────┘       │              │
              │           └──────┬───────┴──────┬───────┘
              │                  ▼             ▼
              │       MATURIDADE TRIPLA por-controlo
              │         Programa: T1-T4 (CSF Tiers) por Function
              │         Controlo: 0-4 por-subcategoria (3 frameworks)
              │                  │
              ▼                  ▼
        CROSSWALK (Framework_Crosswalk_ARM.md, ACTIVE — from Case_02)
              │
              ▼
        ISO 27001 / secure-development standards / AI secure-development standards
```

### 3.3 Invariante metodológica (NÃO violar)

> **Frameworks NIST são ALVO de mapeamento, nunca FONTE de controlos.**
> A AEGIS deriva da lei. CR vêm de obrigações; BPR podem apoiar-se em frameworks
> mas a derivação primária é legal. Se o Executor se encontrar a *inventar* um
> CR só porque uma subcategoria CSF "existe", PARAR — está a violar o MANIFESTO.

---

## §4 — Especificação dos frameworks (vocabulário)

> O Executor DEVE usar apenas IDs das listas frozen. **NÃO inventar IDs.** Se um
> mapeamento não encaixar em nenhuma subcategoria, usar `UNMAPPED_CSF` /
> `UNMAPPED_PRIVACY` / `UNMAPPED_AIRMF`.

### 4.1 NIST CSF 2.0 (segurança — eixo principal)

- **Fonte autoritativa:** `00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md` (106 subcats, 6 Functions, 22 Categories).
- **Cobertura DORA:** DORA (38 clauses) é coberta via CSF subcats em `PR.DS-*`, `PR.AA-*`, `DE.CM-*`, `RS.MA-*`, `RC.RP-*`.

| Function | Nome | Categorias | Subcats |
|---|---|---:|---:|
| **GV** | Govern | 6 | 19 |
| **ID** | Identify | 3 | 13 |
| **PR** | Protect | 5 | 22 |
| **DE** | Detect | 3 | 10 |
| **RS** | Respond | 4 | 13 |
| **RC** | Recover | 1 | 6 |

### 4.2 NIST Privacy Framework 1.0 (privacidade — eixo complementar)

- **Fonte autoritativa:** `00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md` (138 subcats, 5 Functions, 24 Categories).

| Function | Nome (sufixo `-P`) | Função no contexto | Subcats |
|---|---|---|---:|
| **Identify-P** (ID-P) | Identify | Compreender o ecossistema de dados pessoal | 25 |
| **Govern-P** (GV-P) | Govern | Política, responsabilidades, risco de privacidade | 37 |
| **Control-P** (CT-P) | Control | Implementar protecção de dados | 20 |
| **Communicate-P** (CM-P) | Communicate | Comunicação com stakeholders/sujeitos | 10 |
| **Protect-P** (PR-P) | Protect | Salvaguardas técnicas | 46 |

### 4.3 NIST AI RMF 1.0 (IA — eixo IA, ACTIVO em Case_03)

- **Fonte autoritativa:** `00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md` (72 subcats, 4 Functions, 19 Categories).
- **Estado em Case_03:** **ACTIVO** (não placeholder). Case_03 tem IA (credit scoring + fraud detection) — AI Act applicable.

| Function | Nome |
|---|---|
| **GOVERN** | Cultivar cultura de gestão de risco de IA |
| **MAP** | Contextualizar uso de IA |
| **MEASURE** | Analisar/avaliar/medir risco de IA |
| **MANAGE** | Priorizar/acrescentar riscos de IA |

### 4.4 DORA — cobertura via CSF

DORA (Digital Operational Resilience Act) é o regulamento EU específico para o sector financeiro. Não tem mapeamento 1:1 para um framework NIST específico. A AEGIS opta por cobrir DORA via **CSF 2.0 subcats** porque:

1. DORA Art. 9 (ICT risk management) ≈ CSF GV.RM-* + ID.RA-*
2. DORA Art. 10 (ICT incident reporting) ≈ CSF RS.AN-* + RS.MA-*
3. DORA Art. 11 (ICT operational resilience testing) ≈ CSF ID.RA-* + DE.CM-*
4. DORA Art. 12 (ICT third-party risk) ≈ CSF ID.SC-* + GV.SC-*
5. DORA Art. 17 (ICT-related incident logging) ≈ CSF PR.DS-* (integrity)

Ver `06b_DORA_ICT_Risk_Framework.md` para o mapeamento detalhado DORA → CSF.

### 4.5 Correspondência Govern (3 frameworks)

| Conceito de governação | CSF 2.0 | Privacy FW 1.0 | AI RMF 1.0 |
|---|---|---|---|
| Missão/objectivos organizacionais | `GV.OC-*` | `ID-P.BE:*` | `GOVERN-1.*` |
| Requisitos legais/regulatórios | `GV.OC-03`, `GV.LR-*` | `GV-P.PO:*` | `GOVERN-2.*` |
| Política de segurança/privacidade | `GV.PO-*` | `GV-P.PO:1` | `GOVERN-3.*` |
| Papéis e responsabilidades | `GV.RR-*` | `GV-P.PO:2` | `GOVERN-4.*` |
| Gestão de risco | `GV.RM-*` | `ID-P.RA:*`, `GV-P.RM-P:*` | `GOVERN-5.*` |
| Estratégia e melhoria contínua | `GV.STR-*`, `GV.OV-*` | `GV-P.IM:*` | `GOVERN-6.*` |

### 4.6 Regras de sourcing (imperativas)

1. O Executor **DEVE** tirar IDs CSF 2.0 de `NIST_CSF_2.0_subcategories.md`.
2. O Executor **DEVE** tirar IDs Privacy FW de `NIST_PF_1.0_subcategories.md`.
3. O Executor **DEVE** tirar IDs AI RMF de `NIST_AI_RMF_1.0_subcategories.md` — em Case_03, AI RMF é **ACTIVO**.
4. O Executor **DEVE** referenciar DORA → CSF em `06b_DORA_ICT_Risk_Framework.md`.
5. O Executor **NÃO DEVE** inventar IDs. Se não há correspondência, usar `UNMAPPED_CSF`, `UNMAPPED_PRIVACY` ou `UNMAPPED_AIRMF`.

---

## §5 — Artefactos a produzir

### 5.1 ✅ JÁ EXISTE — `NIST_PF_1.0_subcategories.md` e `NIST_AI_RMF_1.0_subcategories.md`

| Campo | Valor |
|---|---|
| Caminho Privacy FW | `00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md` |
| Caminho AI RMF | `00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md` |
| Acção | ✅ **EXISTENTE** (não recriar) |

### 5.2 NOVO — `13_Framework_Mapping_Matrix.md`

| Campo | Valor |
|---|---|
| Caminho | `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md` |
| Acção | **NOVO** |
| Bloco | C |

**Frontmatter:**

```yaml
---
document_id: AEGIS-P2-RICH-13-CASE03
title: Framework Mapping Matrix — Unified NIST (CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0)
phase: 2
version: 1.0
created: <data>
updated: <data>
author: Executor (Bloco C)
status: ACTIVE
sprint: 6
case: Case_03_OmniBank_Financial
tier: MAX
applicable_regulations: [GDPR, CRA, NIS_2, DORA, AI_Act]
frameworks_in_scope: [NIST_CSF_2.0, NIST_Privacy_FW_1.0, NIST_AI_RMF_1.0]
frameworks_placeholder: []
frameworks_dora_coverage: via_CSF_subcats
normative_intensity_rule: AVG_with_AI_MUST_override
ni_avg_rule_note: |
  AVG(NI) per regulation source clauses. AI-C* and DORA-C* presence forces MUST (NI=3).
  DORA clauses uniformly NI=3 (all 38); NIS2 clauses uniformly NI=3 (all 29);
  GDPR has 10 NI=2 + 18 NI=3; CRA has 2 NI=2 + 24 NI=3. AI + DORA MUST-preserved by source.
inputs:
  - 11_Rules_Catalog.md
  - ../../../03_REFERENCE_MATERIAL/Framework_Mappings/Framework_Crosswalk_ARM.md
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md
  - ../../../00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md
  - ../../../00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md
  - ../../../02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/06b_DORA_ICT_Risk_Framework.md
outputs: [Phase 3 inputs, 12_Rules_Catalog.xlsx]
traceability: AEGIS Framework Mapping Layer (CSF + PF + AI RMF; DORA via CSF coverage)
---
```

**Corpo — 6 sub-secções obrigatórias + 2 viz (V1-V4):**

#### §1 — Matriz Unificada (3 frameworks)
#### §2 — Vista Govern Consolidada (3 frameworks)
#### §3 — Mapeamento n:m CR/BPR ↔ Subcategorias
#### §4 — Modelo de Maturidade Tripla
#### §5 — Aplicação ao Case_03
#### §6 — Gap Analysis (CSF + Privacy + AI RMF)

Plus: §6.5 (sub-domain inventory, added by Bloco G fix), §7 (V1-V4 visualizations), §8 (findings reconciliation).

### 5.3 ESTENDER — `11_Rules_Catalog.md`

| Campo | Valor |
|---|---|
| Caminho | `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES/11_Rules_Catalog.md` (canonical) |
| Acção | **ESTENDER** (78 cartões existentes) |
| Bloco | D |

**Campos NOVOS (18, 19-24):**

```
18. Normative Intensity: 3 (MUST)
19. CSF Subcategories: [PR.DS-01, PR.DS-10]
20. Privacy FW Subcategories: [CT-P.DS-P:1]
21. AI RMF Subcategories: [MAP-2.1, MANAGE-2.1]
22. Maturity (CSF): cur 1/4 → tgt 3/4
23. Maturity (Privacy): cur 1/4 → tgt 3/4
24. Maturity (AI RMF): cur 1/4 → tgt 3/4
```

**Frontmatter updates:**
```yaml
expected_fields_per_card: 24
fields_per_card: 24
normative_intensity_rule: AVG_with_AI_MUST_override
ni_avg_rule_note: |
  AVG(NI) per regulation source clauses. AI-C* and DORA-C* presence forces MUST (NI=3).
frameworks_mapped: [NIST_CSF_2.0, NIST_Privacy_FW_1.0, NIST_AI_RMF_1.0]
maturity_dual_mode: triple   # CSF + Privacy + AI RMF (D11 Case_03)
```

### 5.4 DEPRECAR — `04b_Security_Posture.md`

`04b_Security_Posture.md` → DEPRECATED_FOR_MATURITY; maturity_owner: 13_Framework_Mapping_Matrix.md.

### 5.5 PROMOVER — `Framework_Crosswalk_ARM.md` (REUSED from Case_02)

> **Note:** Bloco A is REUSED from Case_02 contract (commit `c972048`). Crosswalk
> is already ACTIVE v1.0 on `main`. No separate commit needed for Case_03.

### 5.6 ESTENDER — `12_Rules_Catalog.xlsx`

Adicionar 6 folhas: `Unified_Matrix`, `Govern_Consolidated`, `Mapping_nm` (78 linhas), `Maturity_Triple` (78 linhas), `Cov_Function` (15 Functions), `Heatmap_Maturity`.

### 5.7 NOVO — 4 Visualizações

V1 matriz cobertura, V2 mapa por Function, V3 Mermaid traceability, V4 heatmap (gap = MAX entre 3 frameworks).

---

## §6 — Regra MUST/SHOULD/COULD (semântica operacional)

### 6.1 NI → consequência operacional

| NI | Label | Origem típica | Consequência operacional |
|---|---|---|---|
| **3** | **MUST** | Cláusula SHALL; obrigação incondicional | **Bloqueia gate de conformidade.** |
| **2** | **SHOULD** | Cláusula SHOULD; recomendado | **Não bloqueia conformidade.** Alimenta gap de maturidade. |
| **1** | **COULD** | Cláusula MAY; aspiracional | Aspiracional. |

### 6.2 Regra de derivação DR-002 — RESOLVER com AVG + AI/DORA MUST override

**Resolução deste contracto:**

```
IF any source_clause(rule) starts with "AI-C" OR "DORA-C" THEN NI(rule) = 3
ELSE NI(rule) = AVG( NI(clause) for clause in source_clauses(rule) )
```

**Justificação:**
- AVG preserva diferenciação SHOULD (P0: MAX mata o sinal, ver AP-P2-09).
- AI-C* e DORA-C* presence forces MUST (NI=3) preserva AI Act + DORA signal — ambas têm NI uniforme = 3.
- GDPR (10 NI=2 + 18 NI=3) e CRA (2 NI=2 + 24 NI=3) preservam SHOULD via AVG.

**Bucketing:**

| Bucket | Intervalo NI | Label |
|---|---|---|
| P1 | NI ≥ 2.5 | MUST (implementar) |
| P2 | 2.0 ≤ NI < 2.5 | SHOULD |
| P3 | NI < 2.0 | COULD |

**Documentação obrigatória no Doc 11 frontmatter:**

```yaml
normative_intensity_rule: AVG_with_AI_MUST_override
ni_avg_rule_note: |
  AVG(NI) per regulation source clauses. AI-C* and DORA-C* presence forces MUST (NI=3).
  DORA clauses uniformly NI=3 (all 38); NIS2 clauses uniformly NI=3 (all 29);
  GDPR has 10 NI=2 + 18 NI=3; CRA has 2 NI=2 + 24 NI=3.
```

### 6.3 Instruções de execução (Bloco B)

Para cada um dos 78 cartões em Doc 11:
1. Ler as source clauses.
2. Se alguma source clause começa com "AI-C" ou "DORA-C": NI = 3.
3. Caso contrário: NI = AVG(...).
4. Atribuir `normative_intensity` (campo 18).

---

## §7 — Modelo de maturidade tripla

### 7.1 Duas escalas (D10)

| Escala | Nível | Aplicação | Frameworks |
|---|---|---|---|
| **Implementation Tiers (T1-T4)** | Programa / por-Function | Avaliação macro | CSF (nativo); Privacy FW e AI RMF adoptam |
| **Maturidade por-subcategoria (0-4)** | Por-controlo / por-subcat | Granularidade operacional | **Todos os 3 frameworks** |

### 7.2 Implementation Tiers (T1-T4)

| Tier | Nome | Descrição |
|---|---|---|
| **1** | Partial | Risco não formalizado |
| **2** | Risk-Informed | Risco gerido informalmente |
| **3** | Repeatable | Práticas formais, repetíveis |
| **4** | Adaptive | Práticas adaptativas, melhoria contínua |

- **Aplicação ao Case_03:** avaliar cada uma das 15 Functions (6 CSF + 5 Privacy + 4 AI RMF).
- **Exemplo esperado para MAX:** a maioria das Functions em T3-T4 (proporcional a banco de grande porte).

### 7.3 Escala 0-4 por-subcategoria

| Nível | Label | Definição operacional |
|---|---|---|
| **0** | None | Sem controlo implementado |
| **1** | Ad-hoc | Informal, inconsistente |
| **2** | Defined | Documentado mas não totalmente implementado |
| **3** | Managed | Implementado, monitorizado |
| **4** | Optimized | Melhoria contínua, automatizado |

### 7.4 TRÊS scores por controlo (D11)

Cada controlo mapeado aos 3 frameworks tem **três scores independentes**:
- `maturity_csf: {cur: X, tgt: Y}`
- `maturity_privacy: {cur: X, tgt: Y}`
- `maturity_ai_rmf: {cur: X, tgt: Y}`

### 7.5 Heatmap — decisão técnica

`gap = MAX(gap_csf, gap_priv, gap_ai_rmf)` para a **cor**.

### 7.6 Ligação maturidade-alvo ↔ proporção

| Tier proporção (Track B) | Target maturidade esperado |
|---|---|
| LIGHTWEIGHT | 2-3 |
| MINIMAL | 2 |
| STANDARD | 3 |
| RIGOROUS | 3-4 |
| DEFERRED | não avaliado |

**Case_03 Track B:** 31 RIGOROUS + 7 STANDARD + 0 DEFERRED. **Active sub-domains:** 38/38 (todos).

---

## §8 — Blocos de trabalho (plano de execução)

### 8.1 Diagrama de dependências

```
Bloco 0 [fundação, sem deps]  ✅ DONE (baseline)
   │
   ▼
Bloco A [deps: 0]  ⚠ REUSED (from Case_02 commit c972048)
   │
   ▼
Bloco B [deps: A]  NI formal (AVG + AI/DORA MUST override) — 78 cartões
   │
   ▼
Bloco C [deps: B, 0]  Doc 13: matriz unificada (3 frameworks) + Govern + maturidade tripla
   │
   ├─────────────┬───────────┐
   ▼             ▼           ▼
Bloco D       Bloco E     (paralelo)
Estender      Deprecar
Doc 11        04b
   │             │
   └──────┬──────┘
          ▼
Bloco F [deps: C, D]  4 visualizações + 6 folhas Excel
          │
          ▼
Bloco G fix [deps: F]  FN-01..FN-05 closure
          │
          ▼
Validator [deps: G]  Tier 1+2 evaluation
```

### 8.2 Especificação por bloco

#### Bloco 0 — ✅ CONCLUÍDO
#### Bloco A — ⚠ REUSED from Case_02 (commit `c972048`)
#### Bloco B — NI formalization ✅ COMPLETE
#### Bloco C — Doc 13 (matriz + Govern + maturidade tripla) ✅ COMPLETE
#### Bloco D — Estender Doc 11 (campos 19-24) ✅ COMPLETE
#### Bloco E — Deprecar 04b ✅ COMPLETE
#### Bloco F — Visualizações + Excel ✅ COMPLETE
#### Bloco G fix — FN-01..FN-05 closure ✅ COMPLETE
#### Validator — Tier 1+2 ✅ COMPLETE

---

## §9 — Critério "pronto" (validação)

> **D16: 100% CR + coerência BPR.**

### 9.1 Cobertura

- [ ] **100% dos 38 CR** têm:
  - [ ] campo 18 (`normative_intensity`) — AVG + AI/DORA MUST override.
  - [ ] campo 19 (`csf_subcategories`) com pelo menos 1 subcat.
  - [ ] campo 20 (`privacy_subcategories`) — pode ser `[]` com justificação.
  - [ ] campo 21 (`ai_rmf_subcategories`) — populated.
  - [ ] campos 22-24 (`maturity_csf`, `maturity_privacy`, `maturity_ai_rmf`) com cur/tgt.

- [ ] **40 BPR** têm campo 18 com NI 1-2 (SHOULD/COULD).

### 9.2 Artefactos

- [ ] `13_Framework_Mapping_Matrix.md` criado com 6 sub-secções + 2 viz.
- [ ] `Framework_Crosswalk_ARM.md` ACTIVE v1.0 (REUSED).
- [ ] `04b_Security_Posture.md` DEPRECATED_FOR_MATURITY.
- [ ] `12_Rules_Catalog.xlsx` com 6 folhas novas.

### 9.3 Coerência metodológica

- [ ] DR-002 resolvido com AVG + AI/DORA MUST override.
- [ ] AI RMF populated (D9) — sem placeholder.
- [ ] DORA coverage via CSF documented (D5, §4.4).
- [ ] Maturidade-alvo consistente com proporção Track B (§7.6).
- [ ] `ni_avg_rule_note` present in Doc 11 frontmatter (FN-03).

### 9.4 Lint & Validator

- [ ] `./scripts/test-quick.sh` passa.
- [ ] Validator Tier 1 (completude/consistência): sem findings críticos abertos.
- [ ] Validator Tier 2 (realismo/alinhamento): sem findings críticos.

---

## §10 — Riscos & decisões diferidas

### 10.1 Riscos

| # | Risco | Mitigação |
|---|---|---|
| R1 | **Propagação ~6 artefactos** (acima do limiar P5 de 3) | Confinado ao Case_03; não fragmenta o método global. |
| R2 | **Maturidade tripla = verbosidade** (3 scores × 78 cards = 234 cells) | Justificado pelo princípio D11; mitigado no heatmap via MAX. |
| R3 | **AI RMF subcats limitadas** (41/72 cobertas por AI Act) | Aceitável; usar `UNMAPPED_AIRMF` para o resto. |
| R4 | **DORA sem framework 1:1** | Coberto via CSF subcats + `06b_DORA_ICT_Risk_Framework.md` (Phase 1). |
| R5 | **F-01 legacy Doc 10 goal count** (33 vs 76) | Documented in README §4; canonical = 76. |

### 10.2 Decisões diferidas

| # | Decisão diferida | Porquê |
|---|---|---|
| DF1 | Preenchimento da coluna NIST 800-53 no crosswalk | 800-53 é pesado; CSF 2.0 já cobre. |
| DF2 | Retropropagação do método a Case_01/02 | Fora de âmbito (D1). |
| DF3 | Argumento académico "AEGIS vs. convencional" | Vive na tese, não no repo (D4). |

---

## §11 — Checklists do Executor

### 11.1 Pre-flight

```bash
git checkout main
git checkout -b feature/aegis-p2-case03-csf-pf-airmf
git branch --show-current
# Esperado: feature/aegis-p2-case03-csf-pf-airmf

git status --short

ls 02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES/11_Rules_Catalog.md
ls 02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml
ls 00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md
ls 00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md
ls 00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md
ls 03_REFERENCE_MATERIAL/Framework_Mappings/Framework_Crosswalk_ARM.md   # MUST be ACTIVE
```

### 11.2 Por-bloco

- [ ] Inputs do bloco presentes?
- [ ] Output conforme schema do §5?
- [ ] Lint passa?
- [ ] Commit message no formato `[EXECUTOR] Bloco X — descrição`?

### 11.3 Pós-execução

- [ ] §9 todo verde.
- [ ] `PROJECT_STATE.md` actualizado.
- [ ] Branch pushed; `./scripts/test-quick.sh` passa.
- [ ] Validator Tier 1+2 report gerado.

### 11.4 Anti-patterns a EVITAR

| Anti-pattern | Porquê evitar |
|---|---|
| ❌ Tocar Case_01/02 | D1 — só Case_03 |
| ❌ Inventar IDs CSF/Privacy/AI RMF | §4.6 — só das listas frozen |
| ❌ Derivar CR de frameworks (não da lei) | §3.3 — invariante metodológica |
| ❌ Usar AI RMF como placeholder | D9 — em Case_03, AI RMF é ACTIVE |
| ❌ Escrever argumento académico no repo | D4 — vive na tese |
| ❌ MAX(NI) em vez de AVG | §6.2 — mata SHOULD |
| ❌ Agregar maturidade num score único | D11 — preservar dessincronia tripla |
| ❌ Tratar DORA como framework separado | §4.4 — DORA via CSF subcats |
| ❌ Apagar conteúdo do 04b | §5.4 — só deprecar |
| ❌ Commit directo em main | AGENTS.md — 1 branch per contract |

---

## §12 — Apêndices

### Apêndice A — Glossário

| Termo | Definição |
|---|---|
| **AEGIS** | Metodologia de mapeamento 5 regulamentos EU × 38 sub-domínios × 3 fases |
| **CR** | Compliance Rule — derivada de obrigação legal, NI tipicamente 3 (MUST) |
| **BPR** | Best Practice Rule — derivada de framework, NI tipicamente 1-2 |
| **NI** | Normative Intensity — 1 (May/COULD), 2 (Should/SHOULD), 3 (Shall/MUST) |
| **DR-002** | Regra de derivação NI: `AVG_with_AI_MUST_override` para Case_03 |
| **AI-C\*** | Source clauses da AI Act (NI uniforme = 3) |
| **DORA-C\*** | Source clauses da DORA (NI uniforme = 3) |
| **DORA via CSF** | DORA não tem framework 1:1 NIST; é coberta via CSF subcats |
| **Function** | Topo da hierarquia NIST |
| **Maturity 0-4** | None/Ad-hoc/Defined/Managed/Optimized — por-subcat, por framework |
| **Track B** | Camada de proporção (LIGHTWEIGHT/STANDARD/RIGOROUS/DEFERRED) |
| **UNMAPPED_CSF/PRIVACY/AIRMF** | Marcador para quando não há correspondência numa subcategoria |
| **AVG_with_AI_MUST_override** | Regra NI: AVG normal, mas presença de AI-C*/DORA-C* força MUST (NI=3) |

### Apêndice B — Caminhos completos referenciados

**Inputs (read-only):**
- `00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md`
- `00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md`
- `00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md`
- `00_METHODOLOGY/PREPROCESSING/Regulation/GDPR/02b_SecurityRules_NISTPF.md`
- `00_METHODOLOGY/PREPROCESSING/Regulation/AI_Act/02b_SecurityRules_NISTAIRMF.md`
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml`
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/04b_Security_Posture.md`
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/06b_DORA_ICT_Risk_Framework.md`
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/07b_Proportionality_Profile.md`

**Outputs (a produzir/estender):**
- `03_REFERENCE_MATERIAL/Framework_Mappings/Framework_Crosswalk_ARM.md` — PROMOVIDO (REUSED from Case_02)
- `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md` — NOVO
- `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES/11_Rules_Catalog.md` — ESTENDER (canonical)
- `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES/12_Rules_Catalog.xlsx` — ESTENDER
- `02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/04b_Security_Posture.md` — DEPRECAR

### Apêndice C — Notas sobre o caso

- **Tier:** MAX (5000+ FTE; multi-billion ARR)
- **Domínio:** Banking / Financial Services
- **Regulations aplicáveis:** GDPR + CRA + NIS 2 + **DORA** + AI Act (5/5; all applicable)
- **Sub-domínios:** 38 totais; 38/38 active (todos RIGOROUS/STANDARD; sem DEFERRED)
- **Source clauses:** 150 (GDPR 28 + CRA 26 + NIS 2 29 + DORA 38 + AI Act 29)
- **Frameworks:** 3 ACTIVE (CSF + PF + AI RMF); DORA via CSF subcats
- **Bloco A:** REUSED from Case_02 (commit `c972048`)

---

## §13 — Branch & execução

### 13.1 Branch

```bash
git checkout main
git checkout -b feature/aegis-p2-case03-csf-pf-airmf
```

**Política:** 1 branch per contract (AGENTS.md).

### 13.2 Commit por bloco

Cada bloco = 1 commit. Formato: `[EXECUTOR] Bloco X — descrição`.

### 13.3 Finalização

```bash
./scripts/test-quick.sh
git push -u origin feature/aegis-p2-case03-csf-pf-airmf
./scripts/finish-feature.sh
# Validator Tier 1+2 → relatório
# PR para main
```

---

**Fim da especificação.**

> Este documento fecha 17 decisões e especifica 7 artefactos em 8 blocos.
> O Executor lê isto + os ficheiros referenciados e executa sem perguntas.
> Se algo parecer ambíguo: alinha com §3 (princípio), §6 (NI), §7 (maturidade tripla).
> Não reinventes decisões fechadas em §2.