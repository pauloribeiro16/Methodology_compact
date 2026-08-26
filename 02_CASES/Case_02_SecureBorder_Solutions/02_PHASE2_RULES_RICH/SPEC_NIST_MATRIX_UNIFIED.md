---
document_id: AEGIS-P2-RICH-SPEC-01-CASE02
title: "Specification — Phase 2 Case_02: Unified NIST Matrix (CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0)"
type: SPECIFICATION
status: ACTIVE
scope: Case_02_SecureBorder_Solutions
audience: Executor (sub-agent or operator)
branch_target: feature/aegis-p2-case02-csf-pf-airmf
created: 2026-08-07
updated: 2026-08-08
author: Orchestrator (Case_02 specification consolidation session)
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

# Specification — Phase 2 Case_02: Unified NIST Matrix

> **Lê-me primeiro.** Este documento fecha 17 decisões tomadas em sessão de
> orquestração para o caso Case_02. Está escrito para que um Executor execute do
> início ao fim sem perguntas. Se algo parecer ambíguo, o problema é desta spec —
> sinaliza no commit message e decide a interpretação mais alinhada com o §3
> (princípio arquitectural). Não reinventes decisões já fechadas em §2.

> **Diferença chave vs Case_01 SPEC:** Case_02 tem **3 frameworks ACTIVE**
> (CSF + Privacy FW + AI RMF). NÃO existe coluna placeholder no Doc 13 — todas
> as 3 colunas (CSF / Privacy FW / AI RMF) são populated com mapeamentos reais.
> A maturity model é TRIPLE (3 scores independentes por controlo).

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
> - AI_Act→AI RMF: `00_METHODOLOGY/PREPROCESSING/Regulation/AI_Act/02b_SecurityRules_NISTAIRMF.md` (24 SR, 41/72 subcats AI RMF).
>
> **Nota de localização:** as frozen lists vivem em `00_METHODOLOGY/PREPROCESSING/` (ao lado do `NIST_CSF_2.0_subcategories.md` canónico), NÃO em `03_REFERENCE_MATERIAL/Framework_Mappings/NIST_Privacy_Framework/` como o §5.1 abaixo originalmente planeava. Sempre que o §5.1, §5.2 e o Apêndice B referenciam `03_REFERENCE_MATERIAL/.../NIST_PF_1.0_subcategories.md`, ler como `00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md`.
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
EU (GDPR, CRA, NIS 2, DORA, AI_Act) a 38 sub-domínios de segurança, em 3 fases:
**UNDERSTAND** (Phase 1) → **DERIVE** (Phase 2) → **DECOMPOSE** (Phase 3). O
"software" é tooling de validação/linting sobre documentos Markdown estruturados,
não software tradicional. O MANIFESTO declara: *"Regulations are inputs, not
checklists. We derive controls from obligations, not from compliance frameworks."*

### 1.2 O problema actual no Case_02 (4 lacunas, escopo ampliado vs Case_01)

Após a exploração do Phase 1 (`01_PHASE1_CONTEXT_RICH/`) e Phase 2 legacy
(`02_PHASE2_RULES/`) do Case_02, identificámos quatro lacunas que este contracto
resolve:

| # | Lacuna | Sintoma observado | Onde |
|---|---|---|---|
| L1 | **MUST/SHOULD informal** | BPR = P3 uniforme, sem `normative_intensity` formal; semântica SHOULD sem consequência operacional. Caso_02 tem `AVG_with_AI_MUST_override`: AVG preserva SHOULD mas AI-C* presence forces MUST (NI=3) para preservar sinal AI_Act. Contradição `DR-002` resolvida. | Doc 11 §4/§5 |
| L2 | **Maturidade deslocada** | Modelo 0-4 vive no Doc 04b com `phase: 1`, mas `PHASE1_STRATEGY.md §7` diz *"Phase 1 does NOT assess control maturity (Phase 2)."* Maturidade é escalar por cartão, não ancorada a escala comparável. | Doc 04b |
| L3 | **Diferenciação não demonstrável** | MANIFESTO tem retórica forte (*"We are not a compliance checklist tool"*) mas sem demonstração operacional ponto-a-ponto vs. análise compliance+maturidade convencional. | — |
| L4 | **AI RMF sem coluna activa** (Case_01) | Case_01 SPEC original tratava AI RMF como placeholder. Case_02 **tem IA** (biometric border-control system, AI_Act applicable), portanto AI RMF DEVE ser ACTIVE — não placeholder. | Doc 13 §1 |

### 1.3 O que JÁ existe e NÃO DEVE ser recriado

O Executor **NÃO DEVE** reconstruir o seguinte — está feito e é input:

| Artefacto | Caminho | Estado | Reutilização |
|---|---|---|---|
| Lista frozen CSF 2.0 (106 subcats) | `00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md` | ACTIVE | Vocabulário controlado — só de aqui se tiram IDs CSF |
| Lista frozen Privacy FW 1.0 (138 subcats) | `00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md` | ACTIVE | Vocabulário controlado |
| Lista frozen AI RMF 1.0 (72 subcats) | `00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md` | ACTIVE | **ACTIVA em Case_02** (não placeholder) |
| Crosswalk AEGIS↔frameworks (38/38) | `03_REFERENCE_MATERIAL/Framework_Mappings/Framework_Crosswalk_ARM.md` | DRAFT v0.1, corpo populado | Promover a ACTIVE (§5.5). Coluna CSF 38/38, ISO 38/38, secure-development standards 23/38, AI secure-development standards 16/38, 800-53 VAZIA |
| Doc 11 — 55 cartões (38 CR + 17 BPR) | `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES/11_Rules_Catalog.md` | DEEP_ENRICHED | Estender (§5.3). Cada cartão já tem 17 campos. |
| Doc 12 — Excel | `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES/12_Rules_Catalog.xlsx` | — | Estender com novas folhas (§5.6) |
| Doc 04b — Security Posture | `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/04b_Security_Posture.md` | ACTIVE, `phase: 1` | Deprecar para input-only (§5.4) |
| Taxonomia 10×38 | `00_METHODOLOGY/TEMPLATES/00_Taxonomy_Reference.md` | ACTIVE | Read-only |
| Phase 1 ontology (112 cláusulas) | `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` | ACTIVE | Read-only — fonte de cláusulas/NI |

### 1.4 O que falta (4 itens)

1. **Matriz unificada + Govern consolidada (3 frameworks)** — não existe; Doc 13 novo (§5.2).
2. **Maturidade tripla por-controlo em escala comparável** — não existe; modelo novo (§7).
3. **NI formal AVG + AI MUST override nos cartões** — campos novos no Doc 11 (§5.3).
4. **Sub-domínios activos mapeados explicitamente** — 35/38 active, 3 DEFERRED (per `07b_Proportionality_Profile.md` §3).

---

## §2 — Decisões consolidadas (17 respostas)

> Cada decisão tem Justificação (o PORQUÊ) e Implicações práticas (o QUE muda no
> artefacto). O Executor não reabre nenhuma destas.

| # | Decisão | Escolha | Justificação | Implicações |
|---|---|---|---|---|
| D1 | Âmbito de execução | **Só Case_02** | Piloto focado; Case_01 + Case_03 são outros contractos | Não tocar Case_01/03 |
| D2 | Abordagem ao catálogo | **Híbrido: derivação AEGIS + CSF 2.0 como pivô** | Mantém identidade AEGIS; CSF dá esqueleto comparável | Frameworks = alvo de mapeamento, não fonte |
| D3 | Maturidade | **Mover p/ Phase 2 + expandir tripla** | Resolve contradição PHASE1_STRATEGY §7 | Doc 04b deprecado; Doc 13 assume tripla maturidade |
| D4 | Argumento "AEGIS vs. convencional" | **Documento académico separado (tese)** | Repo fica neutro; argumentação vive na escrita | Não escrever argumentação no repo |
| D5 | Frameworks NIST a usar | **CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0** (TODOS 3 ACTIVE) | Case_02 tem IA (biometric system); AI_Act applicable | Doc 13 §1 = matriz com colunas de todos 3 frameworks |
| D6 | Articulação estrutural | **Matriz unificada** | Vista única evita triplicação de camadas | Doc 13 §1 = matriz com colunas de cada framework |
| D7 | Função Govern sobreposta | **Vista Govern consolidada (3 frameworks)** | Os 3 frameworks têm Govern; fundir evita redundância | Doc 13 §2 = Govern fundida (GV ∥ Govern-P ∥ GOVERN) |
| D8 | Papel dos frameworks | **Só alvo de mapeamento** | MANIFESTO intacto; AEGIS deriva da lei | CR/BPR não se derivam de frameworks |
| D9 | AI RMF no Case_02 | **ACTIVE (não placeholder)** | Case_02 tem IA (biometric border-control); AI_Act applicable | Schema com 3 colunas populated (CSF + PF + AI RMF) |
| D10 | Escala de maturidade | **Tiers 1-4 + 0-4 nos 3 frameworks** | Comparabilidade directa CSF ↔ Privacy ↔ AI RMF | Definir 0-4 por-subcat para cada framework |
| D11 | Score por controlo multi-framework | **TRÊS scores (csf + privacy + ai_rmf)** | Preserva dessincronia segurança/privacidade/IA | 6 campos de maturidade por cartão |
| D12 | Govern no Case_02 (3 frameworks) | **3 colunas populated** | Método completo; AI RMF é parte integral | Coluna AI RMF = mapeamento real, não `pending` |
| D13 | Estrutura do mapeamento | **n:m flexível** | Captura multi-mapping realista | Cada CR/BPR → lista de subcats por framework |
| D14 | Vocabulário Privacy FW | **Lista frozen completa** | Consistência com tratamento CSF | Lista já existe (`00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md`) |
| D15 | Onde vive a matriz | **Doc 13 novo consolidado** | Centralização; não fragmenta Doc 11 | Doc 13 = 6 sub-secções (§5.2) |
| D16 | Critério "pronto" | **100% CR + coerência BPR** | MUST tem de mapear; SHOULD pode não mapear | Validação em §9 |
| D17 | Branch | **`feature/aegis-p2-case02-csf-pf-airmf`** | Política 1-branch-per-contract (AGENTS.md) | Branch actual é main; Case_01 também merged |

---

## §3 — Princípio arquitectural

### 3.1 Frase-mestra

> AEGIS deriva obrigações da lei → traduz em **CR (MUST, NI=3)** e **BPR (SHOULD,
> NI=1-2)** → ancora cada regra aos 38 sub-domínios → mapeia cada sub-domínio em
> paralelo ao **CSF 2.0** (eixo segurança), **Privacy FW 1.0** (eixo privacidade)
> e **AI RMF 1.0** (eixo IA), numa **matriz unificada** → mede **maturidade tripla
> por-controlo** (Tiers 1-4 no programa/Function; 0-4 por-subcategoria no controlo)
> → liga tudo a ISO/secure-development standards via crosswalk já existente.

### 3.2 Diagrama de fluxo

```
         REGULAÇÃO (GDPR + CRA + NIS 2 + AI_Act aplicáveis ao Case_02)
              │
              ▼  (derivação AEGIS — intacta, MANIFESTO)
        OBRIGAÇÕES (Doc 08) → CR (MUST, NI=3) + BPR (SHOULD, NI=1-2)
              │                          │
              │   Tensões (Doc 09) ◄─────┤
              │                          │
              ▼                          ▼
        PG/SG (Doc 10) ◄──────────  55 CARTÕES (Doc 11)
              │                          │
              │   38 sub-domínios (Taxonomia D-01.1 … D-10.3)
              │   35/38 active (3 DEFERRED per Track B)
              │                          │
              │           MATRIZ UNIFICADA (Doc 13) ◄── NESTE CONTRACTO
              │                          │
              │           ┌──────────────┼──────────────┐
              │           ▼              ▼              ▼
              │        CSF 2.0      PRIVACY FW 1.1   AI RMF 1.0
              │     GV ID PR DE RS RC  ID-P GV-P CT-P CM-P PR-P   GOVERN MAP MEASURE MANAGE
              │           │              │              │
              │           └──────┬───────┴──────┬───────┘
              │                  ▼             ▼
              │       MATURIDADE TRIPLA por-controlo
              │         Programa: T1-T4 (CSF Tiers) por Function
              │         Controlo: 0-4 por-subcategoria (3 frameworks)
              │                  │
              ▼                  ▼
        CROSSWALK (Framework_Crosswalk_ARM.md, ACTIVE)
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
> `UNMAPPED_PRIVACY` / `UNMAPPED_AIRMF` (espelhando a convenção do CSF).

### 4.1 NIST CSF 2.0 (segurança — eixo principal)

- **Fonte autoritativa:** `00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md` (frozen, ACTIVE).
- **Publicação de origem:** NIST CSWP 29 (26 Fevereiro 2024).
- **Estrutura:** 6 Functions, 22 Categories, 106 Subcategories.

| Function | Nome | Categorias | Subcats |
|---|---|---:|---:|
| **GV** | Govern | 6 | 19 |
| **ID** | Identify | 3 | 13 |
| **PR** | Protect | 5 | 22 |
| **DE** | Detect | 3 | 10 |
| **RS** | Respond | 4 | 13 |
| **RC** | Recover | 1 | 6 |

- **Formato do ID:** `XX.YY-NN` (ex: `PR.DS-01`, `GV.OC-03`, `ID.AM-02`).

### 4.2 NIST Privacy Framework 1.0 (privacidade — eixo complementar)

- **Fonte autoritativa:** `00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md` (138 subcats, 5 Functions, 24 Categories).
- **Estrutura:** 5 Functions, 24 Categories, 138 Subcategories (104 activas + 34 redirects).

| Function | Nome (sufixo `-P`) | Função no contexto | Subcats |
|---|---|---|---:|
| **Identify-P** (ID-P) | Identify | Compreender o ecossistema de dados pessoal | 25 |
| **Govern-P** (GV-P) | Govern | Política, responsabilidades, risco de privacidade | 37 |
| **Control-P** (CT-P) | Control | Implementar protecção de dados | 20 |
| **Communicate-P** (CM-P) | Communicate | Comunicação com stakeholders/sujeitos | 10 |
| **Protect-P** (PR-P) | Protect | Salvaguardas técnicas | 46 |

- **Formato do ID:** `XX.YY-PN` (ex: `ID.IM-P1`, `GV.PO-P1`, `PR.DS-P1`, `CT.DM-P3`).

### 4.3 NIST AI RMF 1.0 (IA — eixo IA, **ACTIVO em Case_02**)

- **Fonte autoritativa:** `00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md` (72 subcats, 4 Functions, 19 Categories).
- **Mapeamento AI_Act→AI RMF:** `00_METHODOLOGY/PREPROCESSING/Regulation/AI_Act/02b_SecurityRules_NISTAIRMF.md` (24 SR mapeados a 41/72 subcats AI RMF).
- **Estado em Case_02:** **ACTIVO** (não placeholder). Case_02 tem IA (biometric border-control system) — AI_Act applicable. Todas as 29 cláusulas AI_Act (AI-C*) são NI=3 (MUST) — alinhamento baseline AI_Act.
- **Estrutura:** 4 Functions.

| Function | Nome |
|---|---|
| **GOVERN** | Cultivar cultura de gestão de risco de IA |
| **MAP** | Contextualizar uso de IA |
| **MEASURE** | Analisar/avaliar/medir risco de IA |
| **MANAGE** | Priorizar/acrescentar riscos de IA |

- **Formato do ID:** `GOVERN-1.1`, `MAP-1.1`, etc.
- **O que o Executor faz agora:** Mapear todas as CR com AI-C* nas source clauses para subcats AI RMF relevantes. Sem `pending`.

### 4.4 Correspondência Govern (base da Govern consolidada — 3 frameworks)

Esta tabela é a base do Doc 13 §2 (Vista Govern consolidada para Case_02 com 3 frameworks).

| Conceito de governação | CSF 2.0 | Privacy FW 1.0 | AI RMF 1.0 |
|---|---|---|---|
| Missão/objectivos organizacionais | `GV.OC-*` | `ID-P.BE:*` | `GOVERN-1.*` |
| Requisitos legais/regulatórios | `GV.OC-03`, `GV.LR-*` | `GV-P.PO:*` | `GOVERN-2.*` |
| Política de segurança/privacidade | `GV.PO-*` | `GV-P.PO:1` | `GOVERN-3.*` |
| Papéis e responsabilidades | `GV.RR-*` | `GV-P.PO:2` | `GOVERN-4.*` |
| Gestão de risco | `GV.RM-*` | `ID-P.RA:*`, `GV-P.RM-P:*` | `GOVERN-5.*` |
| Estratégia e melhoria contínua | `GV.STR-*`, `GV.OV-*` | `GV-P.IM:*` | `GOVERN-6.*` |

### 4.5 Regras de sourcing (imperativas)

1. O Executor **DEVE** tirar IDs CSF 2.0 de `NIST_CSF_2.0_subcategories.md`.
2. O Executor **DEVE** tirar IDs Privacy FW de `NIST_PF_1.0_subcategories.md`.
3. O Executor **DEVE** tirar IDs AI RMF de `NIST_AI_RMF_1.0_subcategories.md` — em Case_02, AI RMF é **ACTIVO**.
4. O Executor **NÃO DEVE** inventar IDs. Se não há correspondência, usar `UNMAPPED_CSF`, `UNMAPPED_PRIVACY` ou `UNMAPPED_AIRMF`.

---

## §5 — Artefactos a produzir

> 7 artefactos. Cada um com caminho, acção, schema, exemplo, critério de
> aceitação.

### 5.1 ✅ JÁ EXISTE — `NIST_PF_1.0_subcategories.md` e `NIST_AI_RMF_1.0_subcategories.md`

> **Concluído no contracto baseline** (`feature/aegis-baseline-nist-mappings`).

| Campo | Valor |
|---|---|
| Caminho Privacy FW | `00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md` |
| Caminho AI RMF | `00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md` |
| Acção | ✅ **EXISTENTE** (não recriar) |
| Bloco | 0 (concluído) |

### 5.2 NOVO — `13_Framework_Mapping_Matrix.md`

| Campo | Valor |
|---|---|
| Caminho | `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md` |
| Acção | **NOVO** |
| Bloco | C |

**Frontmatter:**

```yaml
---
document_id: AEGIS-P2-RICH-13-CASE02
title: Framework Mapping Matrix — Unified NIST (CSF 2.0 + Privacy FW 1.0 + AI RMF 1.0)
phase: 2
version: 1.0
created: <data>
updated: <data>
author: Executor (Bloco C)
status: ACTIVE
sprint: 6
case: Case_02_SecureBorder_Solutions
tier: HIGH
applicable_regulations: [GDPR, CRA, NIS_2, AI_Act]
frameworks_in_scope: [NIST_CSF_2.0, NIST_Privacy_FW_1.0, NIST_AI_RMF_1.0]   # all 3 active
frameworks_placeholder: []   # no placeholder in this case
normative_intensity_rule: AVG_with_AI_MUST_override
inputs:
  - 11_Rules_Catalog.md
  - ../../../03_REFERENCE_MATERIAL/Framework_Mappings/Framework_Crosswalk_ARM.md
  - ../../../00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md
  - ../../../00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md
  - ../../../00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md
outputs: [Phase 3 inputs, 12_Rules_Catalog.xlsx]
traceability: AEGIS Framework Mapping Layer (CSF + PF + AI RMF)
related_documents: 11_Rules_Catalog.md, 12_Rules_Catalog.xlsx, 04b_Security_Posture.md
---
```

**Corpo — 6 sub-secções obrigatórias:**

#### §1 — Matriz Unificada (3 frameworks)

Tabela principal: linhas = 38 sub-domínios (ou controlos CR/BPR agrupados por sub-domínio), colunas = Functions de cada framework.

```
| Sub-domínio | CSF 2.0 (subcats) | Privacy FW 1.0 (subcats) | AI RMF 1.0 (subcats) | ISO 27001 |
|-------------|-------------------|---------------------------|----------------------|-----------|
| D-01.1      | PR.DS-01          | CT-P.DS-P:1               | MAP-2.1, MANAGE-2.1  | A.8.24    |
| D-01.2      | PR.DS-02          | CT-P.DM-P:1               | MAP-2.1              | A.8.24    |
| ...         | ...               | ...                       | ...                  | ...       |
```

- A coluna AI RMF é **populated** com mapeamentos reais (sem `pending`).
- Para sub-domínios com CR e BPR, listar todos os IDs únicos mapeados.

#### §2 — Vista Govern Consolidada (3 frameworks)

Aplica a tabela do §4.4 desta spec. Para cada *conceito de governação* (missão, legal, política, papéis, risco, melhoria), mostra as subcategorias dos 3 frameworks.

#### §3 — Mapeamento n:m CR/BPR ↔ Subcategorias

Para cada um dos 55 cartões (38 CR + 17 BPR), uma linha com:

```yaml
rule_id: CR-D-01.1-001
subdomain: D-01.1
normative_intensity: 3          # MUST (ver §6)
priority_label: MUST
csf_subcategories: [PR.DS-01, PR.DS-10]
privacy_subcategories: [CT-P.DS-P:1]   # populated
ai_rmf_subcategories: [MAP-2.1, MANAGE-2.1]   # populated, not pending
mapping_rationale: >
  PR.DS-01 cobre confidencialidade/integridade de dados em repouso;
  CT-P.DS-P:1 cobre data-action management (biometric data é pessoal);
  MAP-2.1 + MANAGE-2.1 contextualizam o sistema IA de reconhecimento biométrico.
```

O Executor DEVE preencher `csf_subcategories`, `privacy_subcategories` E `ai_rmf_subcategories` para os 38 CR (D16: 100% CR). Para os 17 BPR, mapear onde fizer sentido.

#### §4 — Modelo de Maturidade Tripla

Especifica o modelo (ver §7 desta spec para conteúdo). Tabelas:
- 4.1 Implementation Tiers CSF (T1-T4) aplicados ao programa/Function.
- 4.2 Escala 0-4 por-subcategoria para CSF 2.0.
- 4.3 Escala 0-4 por-subcategoria para Privacy FW 1.0.
- 4.4 Escala 0-4 por-subcategoria para AI RMF 1.0.
- 4.5 Tabela de avaliação por-Function para o Case_02 (3 frameworks × 6+5+4 = 15 Functions).

#### §5 — Aplicação ao Case_02

- 5.1 Avaliação por-controlo: tabela com `rule_id`, `cur_csf`, `tgt_csf`, `cur_priv`, `tgt_priv`, `cur_ai`, `tgt_ai`, `gap`.
- 5.2 Avaliação por-Function: T1-T4 actual vs target para cada uma das 6 CSF Functions + 5 Privacy Functions + 4 AI RMF Functions.

#### §6 — Gap Analysis

- 6.1 Subcategorias CSF **não cobertas** por nenhum CR/BPR do Case_02.
- 6.2 Subcategorias Privacy FW **não cobertas**.
- 6.3 Subcategorias AI RMF **não cobertas**.
- 6.4 Sub-domínios com baixa maturidade-alvo (tgt < 3) — justificar com proporção HIGH.

**Critério de aceitação (Doc 13):**
- 6 sub-secções presentes e populadas.
- 100% dos CR com mapeamento n:m (D16).
- AI RMF coluna populated (D9, D12) — **NÃO placeholder**.
- Modelo de maturidade §4 definido para os 3 frameworks (D10).
- Gap analysis identifica pelo menos as subcats não cobertas.

### 5.3 ESTENDER — `11_Rules_Catalog.md`

| Campo | Valor |
|---|---|
| Caminho | `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES/11_Rules_Catalog.md` (canonical) |
| Acção | **ESTENDER** (55 cartões existentes) |
| Bloco | D |

**Campos NOVOS a adicionar a cada cartão (CR e BPR):**

Substituir o campo "5. NIST CSF Anchors" e "13. Maturity Score" por uma estrutura expandida. Manter a numeração 1-18 e adicionar 19-24:

```
18. Normative Intensity: 3 (MUST)                       # ver §6
19. CSF Subcategories: [PR.DS-01, PR.DS-10]              # n:m
20. Privacy FW Subcategories: [CT-P.DS-P:1]              # n:m
21. AI RMF Subcategories: [MAP-2.1, MANAGE-2.1]          # n:m — populated
22. Maturity (CSF): cur 1/4 → tgt 3/4                    # substitui "Maturity Score" antigo
23. Maturity (Privacy): cur 1/4 → tgt 3/4
24. Maturity (AI RMF): cur 1/4 → tgt 3/4
```

> **Decisão de estrutura:** Manter o campo "13. Maturity Score" legado marcado como
> `(legacy — ver 22/23/24)` para não quebrar lints existentes.

**Atualização do frontmatter do Doc 11:**

```yaml
expected_fields_per_card: 24     # era 17 → +1 (Bloco B NI) + 6 (Bloco D tri-maturidade)
fields_per_card: 24              # era 17
normative_intensity_rule: AVG_with_AI_MUST_override
frameworks_mapped: [NIST_CSF_2.0, NIST_Privacy_FW_1.0, NIST_AI_RMF_1.0]
maturity_dual: false
maturity_dual_mode: triple   # CSF + Privacy + AI RMF (D11 Case_02)
```

**Critério de aceitação (Doc 11):**
- 100% dos 38 CR têm campos 18-24 preenchidos.
- 100% dos 17 BPR têm campo 18 com NI 1-2 (SHOULD/COULD).
- `normative_intensity_rule: AVG_with_AI_MUST_override` no frontmatter.
- Lint passa.

### 5.4 DEPRECAR — `04b_Security_Posture.md`

| Campo | Valor |
|---|---|
| Caminho | `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/04b_Security_Posture.md` |
| Acção | **DEPRECAR para input-only** |
| Bloco | E |

**O que muda:**
- O Doc 04b deixa de ser o dono do modelo de maturidade.
- O modelo de maturidade (avaliação tripla, target, gap) vive no Doc 13 §4-5.

**Critério de aceitação (Doc 04b):**
- `status: DEPRECATED_FOR_MATURITY` no frontmatter.
- `status_history` com entrada datada.
- Banner de deprecated no topo do corpo.
- `maturity_owner` aponta para Doc 13.

### 5.5 PROMOVER — `Framework_Crosswalk_ARM.md`

| Campo | Valor |
|---|---|
| Caminho | `03_REFERENCE_MATERIAL/Framework_Mappings/Framework_Crosswalk_ARM.md` |
| Acção | **PROMOVER DRAFT → ACTIVE** |
| Bloco | A |

**Critério de aceitação:**
- `status: ACTIVE`, `version: 1.0`.
- `status_history` presente.
- Nota de 800-53 fora-de-âmbito.
- Referência ao Privacy FW + AI RMF (que vive no Doc 13).

### 5.6 ESTENDER — `12_Rules_Catalog.xlsx`

| Campo | Valor |
|---|---|
| Caminho | `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES/12_Rules_Catalog.xlsx` |
| Acção | **ESTENDER** (adicionar folhas) |
| Bloco | F |

**Novas folhas a adicionar:**

| Folha | Conteúdo |
|---|---|
| `Unified_Matrix` | Réplica do Doc 13 §1 (matriz sub-domínio × 3 frameworks) |
| `Govern_Consolidated` | Réplica do Doc 13 §2 |
| `Mapping_nm` | 55 linhas × `{rule_id, subdomain, NI, csf_subcats, priv_subcats, ai_rmf_subcats}` |
| `Maturity_Triple` | 55 linhas × `{rule_id, cur_csf, tgt_csf, cur_priv, tgt_priv, cur_ai, tgt_ai, gap}` |
| `Cov_Function` | Visualização por Function (6 CSF + 5 Privacy + 4 AI RMF = 15) |
| `Heatmap_Maturity` | Sub-domínio × gap (cor = MAX gap entre 3 frameworks) |

**Critério de aceitação:**
- 6 novas folhas presentes.
- `Mapping_nm` tem 55 linhas (1 por regra).
- `Heatmap_Maturity` com formatação condicional (cor por MAX gap entre 3 frameworks).

### 5.7 NOVO — 4 Visualizações

Bloco F. Formato de cada uma (a renderizar em markdown no Doc 13 e/ou Excel):

#### V1 — Matriz de Cobertura (CR/BPR × CSF + Privacy + AI RMF)
- Tabela 55 linhas × colunas `[rule_id, type(CR/BPR), NI, subdomain, csf_subcats, priv_subcats, ai_rmf_subcats]`.

#### V2 — Mapa de Cobertura por Function
- Para cada uma das 15 Functions (6 CSF + 5 Privacy + 4 AI RMF), contar subcats cobertas por CR vs BPR vs GAP.

#### V3 — Grafo de Rastreabilidade
- **Figura central da tese.** Nodos: Regulação → Cláusula → Obrigação → CR/BPR → sub-domínio → CSF/Privacy/AI RMF → ISO/secure-development standards.

#### V4 — Heatmap de Maturidade (TRIPLA)
- Linhas: 38 sub-domínios (ou 55 controlos).
- Cor: `gap = MAX(gap_csf, gap_priv, gap_ai_rmf)` (pior caso entre os 3 frameworks).
- Cores: Verde (gap 0) / Amarelo (gap 1) / Laranja (gap 2) / Vermelho (gap 3-4).

---

## §6 — Regra MUST/SHOULD/COULD (semântica operacional)

### 6.1 NI → consequência operacional

| NI | Label | Origem típica | Consequência operacional |
|---|---|---|---|
| **3** | **MUST** | Cláusula SHALL; obrigação incondicional | **Bloqueia gate de conformidade.** Falhar = não-conformidade. |
| **2** | **SHOULD** | Cláusula SHOULD; recomendado; BPR com base em framework | **Não bloqueia conformidade.** Alimenta gap de maturidade. |
| **1** | **COULD** | Cláusula MAY; aspiracional | Aspiracional. |

### 6.2 Regra de derivação DR-002 — RESOLVER com AVG + AI MUST override

**Resolução deste contracto:** **Adoptar `AVG` com override para AI-C* (todas NI=3).**

**Fórmula:**

```
IF any source_clause(rule) starts with "AI-C" THEN NI(rule) = 3
ELSE NI(rule) = AVG( NI(clause) for clause in source_clauses(rule) )
```

**Justificação da escolha AVG + AI MUST override:**
- AVG preserva diferenciação SHOULD (P0: MAX mata o sinal, ver AP-P2-09).
- AI-C* presence forces MUST (NI=3) preserva AI_Act signal (baseline) — todas as 29 cláusulas AI_Act são NI=3 → MUST.
- DORA NOT APPLICABLE em Case_02 (não financeiro); só GDPR + CRA + NIS 2 + AI_Act.

**Bucketing:**

| Bucket | Intervalo NI | Label operacional |
|---|---|---|
| P1 | NI ≥ 2.5 | MUST (implementar) |
| P2 | 2.0 ≤ NI < 2.5 | SHOULD (implementar se proporcional) |
| P3 | NI < 2.0 | COULD (aspiracional) |

**Documentação obrigatória no Doc 11 frontmatter:**

```yaml
normative_intensity_rule: AVG_with_AI_MUST_override
dr_002_resolution: >
  DR-002 definido como AVG (não MAX). MAX mata diferenciação (AP-P2-09).
  AVG preserva SHOULD. Adicionalmente, qualquer CR com AI-C* nas source
  clauses é forçado MUST (NI=3) — alinhamento com a baseline AI_Act.
```

### 6.3 Instruções de execução (Bloco B)

O Executor DEVE, para cada um dos 55 cartões em Doc 11:
1. Ler as source clauses (campo 4 "Source Article" → clause IDs).
2. Consultar `phase1_ontology.yaml` para o `normative_strength` de cada cláusula.
3. Se alguma source clause começa com "AI-C": NI = 3 (override).
4. Caso contrário: NI = AVG(...).
5. Atribuir `normative_intensity` (campo 18): inteiro 1-3 + label MUST/SHOULD/COULD.
6. Para BPR (sem cláusula source legal directa): atribuir NI com base na força do framework de origem.

---

## §7 — Modelo de maturidade tripla

### 7.1 Duas escalas (D10)

| Escala | Nível | Aplicação | Frameworks |
|---|---|---|---|
| **Implementation Tiers (T1-T4)** | Programa / por-Function | Avaliação macro | CSF 2.0 (nativo); Privacy FW e AI RMF adoptam |
| **Maturidade por-subcategoria (0-4)** | Por-controlo / por-subcat | Granularidade operacional | **Todos os 3 frameworks** |

### 7.2 Implementation Tiers (T1-T4) — nível programa/Function

| Tier | Nome | Descrição |
|---|---|---|
| **1** | Partial | Risco não formalizado; práticas ad-hoc |
| **2** | Risk-Informed | Risco gerido informalmente; práticas definidas mas não consistentes |
| **3** | Repeatable | Práticas formais, repetíveis, com monitorização |
| **4** | Adaptive | Práticas adaptativas, melhoria contínua, automatização |

- **Aplicação ao Case_02:** avaliar cada uma das 15 Functions (6 CSF + 5 Privacy + 4 AI RMF).
- **Exemplo esperado para HIGH:** a maioria das Functions em T2-T3 (proporcional a empresa média).

### 7.3 Escala 0-4 por-subcategoria — nível controlo (CONSTRUÍDA)

> **Desacordo P0 registado (D10 + adaptação):** NIST define Implementation Tiers
> explicitamente ao nível da organização, não por-controlo. A resolução adoptada
> é: Tiers no programa/Function, maturidade 0-4 por-subcategoria no controlo.
> A escala 0-4 por-subcategoria **tem de ser construída**.

**Escala 0-4 (adoptada para os 3 frameworks):**

| Nível | Label | Definição operacional |
|---|---|---|
| **0** | None | Sem controlo implementado |
| **1** | Ad-hoc | Informal, inconsistente, sem documentação |
| **2** | Defined | Documentado mas não totalmente implementado |
| **3** | Managed | Implementado, monitorizado, medido |
| **4** | Optimized | Melhoria contínua, automatizado |

### 7.4 TRÊS scores por controlo (D11)

Cada controlo mapeado aos 3 frameworks tem **três scores independentes**:
- `maturity_csf: {cur: X, tgt: Y}`
- `maturity_privacy: {cur: X, tgt: Y}`
- `maturity_ai_rmf: {cur: X, tgt: Y}`

Isto preserva a dessincronia segurança/privacidade/IA. **NÃO agregar** num score único.

### 7.5 Heatmap — decisão técnica

Para o heatmap (V4), usar `gap = MAX(gap_csf, gap_priv, gap_ai_rmf)` para a **cor**
(representa o pior caso entre os 3 frameworks), mas manter os scores individuais visíveis no detalhe.

### 7.6 Ligação maturidade-alvo ↔ proporção

A maturidade-alvo não é livre. Para cada controlo, o `tgt` DEVE ser consistente
com o tier de proporção do sub-domínio (Track B, `07b_Proportionality_Profile.md`):

| Tier proporção (Track B) | Target maturidade esperado |
|---|---|
| LIGHTWEIGHT | 2-3 |
| MINIMAL | 2 |
| STANDARD | 3 |
| RIGOROUS | 3-4 |
| DEFERRED | não avaliado |

**Case_02 Track B:** 7 RIGOROUS + 27 STANDARD + 1 DEFERRED + 3 LIGHTWEIGHT.
**Active sub-domains:** 35/38 (3 DEFERRED excluídos da avaliação).

---

## §8 — Blocos de trabalho (plano de execução)

### 8.1 Diagrama de dependências

```
Bloco 0 [fundação, sem deps]  Vocabulário Privacy FW + AI RMF frozen
   │
   ▼
Bloco A [deps: 0]  Promover crosswalk DRAFT → ACTIVE
   │
   ▼
Bloco B [deps: A]  Formalizar MUST/SHOULD nos 55 cartões (NI, AVG + AI MUST override)
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
Bloco G fix [deps: F]  FN-01..FN-07 closure
          │
          ▼
Validator [deps: G]  Tier 1+2 evaluation
```

### 8.2 Especificação por bloco

#### Bloco 0 — ✅ CONCLUÍDO (contracto baseline)

> O Bloco 0 original (vocabulário Privacy FW + AI RMF) **foi absorvido pelo contracto baseline**
> `feature/aegis-baseline-nist-mappings`. Tanto a frozen list Privacy FW como a AI RMF
> já existem, e os mapeamentos GDPR→PF + AI_Act→AI RMF também. **Saltar directamente para o Bloco A.**

#### Bloco A — Crosswalk promotion

| Campo | Valor |
|---|---|
| Deps | Bloco 0 ✅ (concluído) |
| Outputs | `Framework_Crosswalk_ARM.md` (ACTIVE, §5.5) |
| Commit | `[EXECUTOR] Bloco A — crosswalk promoted DRAFT→ACTIVE (Case_02 contract reuse)` |

#### Bloco B — MUST/SHOULD formalization (NI formal)

| Campo | Valor |
|---|---|
| Outputs | Doc 11 com campo 18 (NI) em todos os 55 cartões |
| Commit | `[EXECUTOR] Bloco B — NI formal (AVG+AI MUST) em 79 cartões, DR-002 resolvido` |
| Validação | 100% dos 55 cartões com campo 18; AVG + AI MUST override aplicado |

#### Bloco C — Doc 13 (matriz + Govern + maturidade tripla)

| Campo | Valor |
|---|---|
| Outputs | `13_Framework_Mapping_Matrix.md` (3 frameworks, §5.2) |
| Commit | `[EXECUTOR] Bloco C — Doc 13 unified matrix (3 frameworks CSF+PF+AI RMF) + triple maturity` |
| Validação | 6 sub-secções; 100% CR mapeados aos 3 frameworks; AI RMF populated (NÃO placeholder) |

#### Bloco D — Estender Doc 11 (campos 19-24, tri-maturidade)

| Campo | Valor |
|---|---|
| Outputs | Doc 11 com campos 19-24 em todos os 55 cartões |
| Commit | `[EXECUTOR] Bloco D — Doc 11 estendido (campos 19-24, tri-maturidade CSF+PF+AI RMF)` |

#### Bloco E — Deprecar 04b

| Campo | Valor |
|---|---|
| Outputs | `04b_Security_Posture.md` (DEPRECATED_FOR_MATURITY, §5.4) |
| Commit | `[EXECUTOR] Bloco E — 04b deprecated for maturity (moved to Doc 13)` |

#### Bloco F — Visualizações + Excel (10 sheets)

| Campo | Valor |
|---|---|
| Outputs | 4 visualizações + 6 folhas Excel (§5.6, §5.7) |
| Commit | `[EXECUTOR] Bloco F — 4 visualizações + 6 folhas Excel (3 frameworks)` |

#### Bloco G fix — FN-01..FN-07 closure

| Campo | Valor |
|---|---|
| Outputs | All 7 Validator findings closed |
| Commit | `[EXECUTOR] Bloco G fix — FN-01 frozen IDs + FN-02 AI RMF anchor + FN-03 heatmap MAX + FN-04 35 active + FN-05 path labels + FN-07 field count` |

#### Validator — Tier 1+2

| Campo | Valor |
|---|---|
| Outputs | Relatório Validator Tier 1+2 |
| Commit | `[VALIDATOR] Tier 1+2 evaluation — Case_02 unified matrix (3 frameworks, Block G)` |

---

## §9 — Critério "pronto" (validação)

> **D16: 100% CR + coerência BPR.**

### 9.1 Cobertura

- [ ] **100% dos 38 CR** têm:
  - [ ] campo 18 (`normative_intensity`) preenchido com NI calculado por AVG + AI MUST override.
  - [ ] campo 19 (`csf_subcategories`) com pelo menos 1 subcat.
  - [ ] campo 20 (`privacy_subcategories`) — pode ser `[]` com justificação.
  - [ ] campo 21 (`ai_rmf_subcategories`) — populated (NÃO placeholder).
  - [ ] campos 22-24 (`maturity_csf`, `maturity_privacy`, `maturity_ai_rmf`) com cur/tgt.

- [ ] **17 BPR** têm:
  - [ ] campo 18 com NI 1-2 (SHOULD/COULD).
  - [ ] campos 19-21 mapeados **onde fizer sentido**.

### 9.2 Artefactos

- [ ] `13_Framework_Mapping_Matrix.md` criado com 6 sub-secções e 3 frameworks populated.
- [ ] `Framework_Crosswalk_ARM.md` ACTIVE v1.0.
- [ ] `04b_Security_Posture.md` DEPRECATED_FOR_MATURITY.
- [ ] `12_Rules_Catalog.xlsx` com 6 folhas novas.

### 9.3 Coerência metodológica

- [ ] DR-002 resolvido com AVG + AI MUST override.
- [ ] Nenhum controlo derivado *de* um framework (invariante §3.3).
- [ ] AI RMF populated (D9) — sem placeholder em Case_02.
- [ ] Maturidade-alvo consistente com proporção Track B (§7.6).

### 9.4 Lint & Validator

- [ ] `./scripts/test-quick.sh` passa.
- [ ] Validator Tier 1 (completude/consistência): sem findings críticos abertos.
- [ ] Validator Tier 2 (realismo/alinhamento): sem findings críticos.

---

## §10 — Riscos & decisões diferidas

### 10.1 Riscos

| # | Risco | Mitigação |
|---|---|---|
| R1 | **Propagação ~6 artefactos** (acima do limiar P5 de 3) | Confinado ao Case_02; não fragmenta o método global. |
| R2 | **Maturidade tripla = verbosidade** (3 scores por cartão) | Justificado pelo princípio D11; mitigado no heatmap via MAX para cor. |
| R3 | **AI RMF subcats limitadas** (41/72 cobertas por AI_Act) | Aceitável; usar `UNMAPPED_AIRMF` para o resto. |
| R4 | **Consistência cross-case** (Case_01/03 dessincronizados) | Aceitável como piloto. Documentar. |
| R5 | **Sub-domínios DEFERRED** (3/38) | Excluídos da avaliação de maturidade; justificação em Doc 13 §6. |

### 10.2 Decisões diferidas

| # | Decisão diferida | Porquê | Onde sinalizar |
|---|---|---|---|
| DF1 | Preenchimento da coluna NIST 800-53 no crosswalk | 800-53 é pesado; CSF 2.0 já cobre a necessidade de pivô. | `Framework_Crosswalk_ARM.md` nota. |
| DF2 | Retropropagação do método a Case_01/03 | Fora de âmbito (D1). | `PROJECT_STATE.md`. |
| DF3 | Argumento académico "AEGIS vs. convencional" | Vive na tese, não no repo (D4). | — |

---

## §11 — Checklists do Executor

### 11.1 Pre-flight (antes do Bloco A)

```bash
# 1. Branch correcta
git checkout main
git checkout -b feature/aegis-p2-case02-csf-pf-airmf
git branch --show-current
# Esperado: feature/aegis-p2-case02-csf-pf-airmf

# 2. Working tree limpa (ou só ficheiros novos deste contracto)
git status --short

# 3. Artefactos de input presentes
ls 02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES/11_Rules_Catalog.md
ls 02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml
ls 00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md
ls 00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md
ls 00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md
ls 03_REFERENCE_MATERIAL/Framework_Mappings/Framework_Crosswalk_ARM.md
```

### 11.2 Por-bloco (antes de commit)

- [ ] Inputs do bloco presentes?
- [ ] Output conforme schema do §5?
- [ ] Lint passa?
- [ ] Commit message no formato `[EXECUTOR] Bloco X — descrição`?

### 11.3 Pós-execução (antes de PR)

- [ ] §9 todo verde.
- [ ] `PROJECT_STATE.md` actualizado.
- [ ] Branch pushed; `./scripts/test-quick.sh` passa.
- [ ] Validator Tier 1+2 report gerado.

### 11.4 Anti-patterns a EVITAR

| Anti-pattern | Porquê evitar |
|---|---|
| ❌ Tocar Case_01/03 | D1 — só Case_02 |
| ❌ Inventar IDs CSF/Privacy/AI RMF | §4.5 — só das listas frozen |
| ❌ Derivar CR de frameworks (não da lei) | §3.3 — invariante metodológica |
| ❌ Usar AI RMF como placeholder | D9 — em Case_02, AI RMF é ACTIVE |
| ❌ Escrever argumento académico no repo | D4 — vive na tese |
| ❌ MAX(NI) em vez de AVG | §6.2 — mata SHOULD (AP-P2-09) |
| ❌ Agregar maturidade num score único | D11 — preservar dessincronia tripla |
| ❌ Preencher coluna 800-53 | DF1 — fora de âmbito |
| ❌ Apagar conteúdo do 04b | §5.4 — só deprecar, manter input |
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
| **DR-002** | Regra de derivação NI: `AVG_with_AI_MUST_override` para Case_02 |
| **AI-C\*** | Source clauses da AI_Act (NI uniforme = 3) |
| **Function** | Topo da hierarquia NIST (CSF: 6; Privacy: 5; AI RMF: 4) |
| **Subcategory** | Unidade atómica mapeável (CSF: 106; Privacy: 138; AI RMF: 72) |
| **Tier (CSF)** | Implementation Tier 1-4 (Partial/Risk-Informed/Repeatable/Adaptive) |
| **Maturity 0-4** | None/Ad-hoc/Defined/Managed/Optimized — por-subcat, por framework |
| **Govern consolidada** | Vista que funde GV (CSF) + Govern-P (Privacy) + GOVERN (AI RMF) |
| **Matriz unificada** | Vista única com colunas de cada framework — Doc 13 §1 |
| **Track B** | Camada de proporção (LIGHTWEIGHT/STANDARD/RIGOROUS/DEFERRED) |
| **UNMAPPED_CSF/PRIVACY/AIRMF** | Marcador para quando não há correspondência numa subcategoria |
| **AVG_with_AI_MUST_override** | Regra NI: AVG normal, mas presença de AI-C* força MUST (NI=3) |

### Apêndice B — Caminhos completos referenciados

**Inputs (read-only):**
- `00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md` — CSF frozen
- `00_METHODOLOGY/PREPROCESSING_by_domain/_global/NIST_PF_1.0_subcategories.md` — PF frozen
- `00_METHODOLOGY/PREPROCESSING/NIST_AI_RMF_1.0_subcategories.md` — AI RMF frozen
- `00_METHODOLOGY/PREPROCESSING/Regulation/GDPR/02b_SecurityRules_NISTPF.md`
- `00_METHODOLOGY/PREPROCESSING/Regulation/AI_Act/02b_SecurityRules_NISTAIRMF.md`
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml`
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/04b_Security_Posture.md`
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/07b_Proportionality_Profile.md`

**Outputs (a produzir/estender):**
- `03_REFERENCE_MATERIAL/Framework_Mappings/Framework_Crosswalk_ARM.md` — PROMOVER
- `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md` — NOVO
- `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES/11_Rules_Catalog.md` — ESTENDER (canonical)
- `02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES/12_Rules_Catalog.xlsx` — ESTENDER
- `02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/04b_Security_Posture.md` — DEPRECAR

### Apêndice C — Notas sobre o caso

- **Tier:** HIGH (250-500 FTE; €50-100M ARR)
- **Domínio:** Biometric border-control technology
- **Regulations aplicáveis:** GDPR + CRA + NIS 2 + AI_Act (4/5; DORA NOT APPLICABLE)
- **Sub-domínios:** 38 totais; 35 active (3 DEFERRED per Track B)
- **Source clauses:** 112 (GDPR 28 + CRA 26 + NIS 2 29 + AI_Act 29)
- **Frameworks:** 3 ACTIVE (CSF + PF + AI RMF) — **sem placeholder**

---

## §13 — Branch & execução

### 13.1 Branch

```bash
git checkout main
git checkout -b feature/aegis-p2-case02-csf-pf-airmf
```

**Política:** 1 branch per contract (AGENTS.md).

### 13.2 Commit por bloco

Cada bloco = 1 commit. Formato: `[EXECUTOR] Bloco X — descrição`.

### 13.3 Finalização

```bash
./scripts/test-quick.sh                          # validar
git push -u origin feature/aegis-p2-case02-csf-pf-airmf
./scripts/finish-feature.sh                      # preparar PR
# Validator Tier 1+2 → relatório
# PR para main
```

---

**Fim da especificação.**

> Este documento fecha 17 decisões e especifica 7 artefactos em 8 blocos.
> O Executor lê isto + os ficheiros referenciados e executa sem perguntas.
> Se algo parecer ambíguo: alinha com §3 (princípio), §6 (NI), §7 (maturidade tripla).
> Não reinventes decisões fechadas em §2.