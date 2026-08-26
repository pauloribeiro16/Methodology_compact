# EXECUTION BRIEF — Domain Parser Pilot (D-01.1)

> **Instruções para um modelo executor.** Implementar exatamente o que está aqui descrito. Não inventar, não adicionar features, não mudar a stack. Ler as secções "Pré-requisitos" e "Fontes canónicas" ANTES de escrever código.

---

## 1. OBJETIVO

Construir um **parser determinístico** que converte `D-01.1.md` (3006 linhas, 4 Parts, estrutura irregular) num **JSON sidecar estruturado e filtrável** (`D-01.1.json`), mais um **CLI de filtragem** que resolve o caso de uso "quero toda a informação aplicável a CRA + GDPR só".

Piloto para **um domínio** (D-01.1). Se correr bem, escala para os 38 domínios sem reescrita — por isso o código tem de ser **reutilizável**, não hard-coded para D-01.1.

---

## 2. PRÉ-REQUISITOS — LER ANTES DE COMEÇAR

### 2.1 Ficheiros a ler obrigatoriamente (contexto)

1. **Alvo do parsing** (ler completo antes de tocar no parser):
   ```
   00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.md
   ```

2. **Enum canónico a validar contra** (NÃO hardcodar):
   ```
   00_METHODOLOGY/SCHEMA/obligated_party.yaml
   ```

3. **Parser de tabelas existente a reutilizar como referência de estilo**:
   ```
   01_IMPLEMENTATION_TOOLS/evals_draft/markdown_parser.py
   ```
   → Seguir o estilo (regex puro + `yaml.safe_load`, typing `List[Dict[str,str]]`).

4. **Linter estrutural existente (padrão de frontmatter parsing a seguir)**:
   ```
   01_IMPLEMENTATION_TOOLS/lints/structural/lint_document_structure.py
   ```
   → Seguir o padrão `re.search(r'^---\n(.*?)\n---', content, re.DOTALL)` + `yaml.safe_load`.

> ⚠️ **Contexto do compact repo (2026-08-26).** Itens 2, 3 e 4 residem no **repo principal AEGIS**, **não no compacto**. Antes de os consultar, sincronize do repositório principal ou peça-os ao Orchestrator. Se for implementar o parser só com base neste corpus, declare explicitamente a limitação ao Orchestrator antes de escrever código.

### 2.2 Stack tecnológica — OBRIGATÓRIA

- **Python 3.9+** (não assumir 3.10+ — usar `from typing import List, Dict, Optional` em vez de `list[str]`)
- **Apenas stdlib + PyYAML**. Importar: `re`, `json`, `yaml`, `pathlib`, `argparse`, `sys`, `datetime`, `typing`.
- **PROIBIDO introduzir**: `markdown-it-py`, `python-frontmatter`, `mistletoe`, `mistune`, `pydantic`, `dataclasses`. O repo não as usa; o parser deve ser standalone com stdlib + PyYAML.
- **Shebang**: `#!/usr/bin/env python3`
- **UTF-8**: todos os ficheiros Markdown têm Unicode (`↔`, `—`, `§`, `<mark>`). Ler sempre com `encoding="utf-8"`.

### 2.3 Restrições de repo (MUITO IMPORTANTE)

- **NUNCA modificar os `.md` originais.** O parser é **read-only**. O JSON é sidecar.
- **Seguir branch workflow** do repo: criar branch `feature/domain-parser-pilot` antes de commitar (ver secção 9).
- **Linguagem do código**: comentários e docstrings em **inglês** (convenção do repo). User-facing strings (erros, help do CLI) em **inglês**.

---

## 3. FONTE DE VERDADE — ESTRUTURA DE D-01.1.md

O ficheiro tem **5 H1 headings** (1 título + 4 Parts). Cada Part começa com `# Part N — <descrição>`. Os níveis H são **não-monotónicos** (Part 2 salta de H1 para H4) — **não usar níveis H como delimitador**. Usar os 4 `# Part N` como delimitadores top-level.

### 3.1 Esqueleto (100% consistente em todos os 38 domínios)

```
# D-01.1 — <title>                    (L1, título)
# Part 1 — Sub-domain definition      (L8)
# Part 2 — Domain Analysis (cross-regulation)
# Part 3 — Deep Analysis (per-pair)
# Part 4 — Relevant Ambiguity (by regulation)
```

### 3.2 Conteúdo por Part

**Part 1 — Sub-domain definition:**
- Frontmatter YAML (linhas 11–32, delimitado por `---`, **não** em code fence)
- `### 1. Cross-Regulation Analysis` → `#### D-01.1 ...` → HTML comment `<!-- participants: GDPR, NIS2, CRA, DORA; AI_Act absent -->` → 6 × `##### Pair: REGA ↔ REGB`
- `### 2. Hierarchical Security Objective` → YAML fences para HSO (HL) + 4 Sub-SOs (GDPR/NIS2/CRA/DORA) sob `#### D-01.1.N — Sub-SO for REG`
- `### 3. Security Requirements` → `### High-level requirement` (1 YAML fence) + `### Sub-requirements` (4 × `#### N.M — title` com YAML fence cada)

**Part 2 — Domain Analysis:**
- Frontmatter YAML (linhas 905–922)
- `##### Participants` → tabela 5 colunas (Regulation | SO ID | summary | Scope/angle)
- `##### Pairwise matrix` → 6 mini-tabelas delimitadas por `<!-- pair: REGA,REGB -->` … `<!-- /pair -->`
- `##### Emergent tensions (3+ regulations)` → delimitado por `<!-- emergent: GDPR,NIS2,CRA,DORA -->` … `<!-- /emergent -->`

**Part 3 — Deep Analysis:**
- Frontmatter YAML (linhas 1027–1044)
- 6 × `##### Pair: REGA ↔ REGB` → **VERBATIM DUPLICATE** do Part 1 (dedup por par)

**Part 4 — Relevant Ambiguity (by regulation):**
- `## GDPR`, `## CRA`, `## NIS2`, `## DORA`, `## AI_Act` (H2 por regulamento)
- Variantes extra: `## CRA v0.2 — ...`, `## DORA v0.2 — ...`, `## NIS 2 v0.2 — ...`
- Cards com **3 variantes estruturais** (ver secção 5.4)

---

## 4. SCHEMA DE SAÍDA — D-01.1.json

Exatamente esta estrutura (não adicionar campos, não remover). Ordem dos campos matters para determinismo.

```json
{
  "schema_version": "1.0.0",
  "source_file": "D-01.1.md",
  "source_path": "00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.md",
  "parsed_at": "<ISO 8601 UTC timestamp>",
  "parser_version": "1.0.0",
  "metadata": {
    "<todos os campos dos 3 frontmatter blocks fundidos; chaves Part-1优先>"
  },
  "subdomain": {
    "id": "D-01.1",
    "name": "Data at Rest Encryption",
    "participants": ["GDPR", "NIS2", "CRA", "DORA"],
    "ai_act": "absent"
  },
  "security_objectives": {
    "high_level": {
      "id": "SO-D-01.1.HL",
      "yaml": { "<conteúdo do YAML fence bruto, parsed>" },
      "objective": "Data held at rest in storage is protected...",
      "considerations": ["<bullet 1>", "<bullet 2>", "..."]
    },
    "sub_objectives": [
      {
        "id": "SO-D-01.1.GDPR",
        "regulation": "GDPR",
        "yaml": { "<parsed>" },
        "objective": "...",
        "considerations": ["..."],
        "csf_anchors": ["PR.DS-01", "..."]
      }
    ]
  },
  "requirements": {
    "high_level": {
      "req_id": "1.1",
      "title": "...",
      "yaml": { "<parsed>" },
      "nist_csf": ["PR.DS-01"],
      "applicable_if": { "regs": ["GDPR", "NIS2", "CRA", "DORA"], "scope_overlap": "conditional" }
    },
    "sub_requirements": [
      {
        "req_id": "1.1.1",
        "regulation": "GDPR",
        "title": "...",
        "yaml": { "<parsed>" },
        "nist_csf": ["PR.DS-01", "PR.DS-10"],
        "applicable_if": { "regs": ["GDPR"], "scope_overlap": "Y" }
      }
    ]
  },
  "pairs": [
    {
      "pair": ["GDPR", "NIS2"],
      "source_part": "Part1",          // "Part1" ou "Part3" (dedup mantém Part1)
      "classification": "COMPLEMENTARY",
      "verified_relationship": "SAME (CORRECTED — wording only)",
      "scope_disjoint": "Y",
      "fields": {
        "<todos os bold-label pseudo-fields extraídos: scope_comparison, trigger_comparison, threshold_timeline_comparison, recipient_comparison, content_template_comparison, reasoning, downstream_implication, etc.>"
      },
      "raw_text": "<texto bruto do bloco do par, para auditoria>"
    }
  ],
  "pairwise_matrix": [
    {
      "pair": ["GDPR", "NIS2"],
      "classification": "Complementary",
      "rows": [
        { "regulation": "GDPR", "summary": "...", "anchor": "Art. 5(1)(f) CIA; Art. 32 risk-based; ..." }
      ],
      "why": "GDPR anchors at-rest encryption to..."
    }
  ],
  "emergent_tensions": [
    { "regulations": ["GDPR", "NIS2", "CRA", "DORA"], "text": "All four regulations impose..." }
  ],
  "ambiguity_cards": [
    {
      "regulation": "GDPR",
      "clause_id": "GDPR-CL01",
      "article_ref": "Art. 5(1)(a)",
      "title": "Lawfulness, fairness, transparency",
      "card_variant": "GDPR-light",     // "GDPR-light" | "GDPR-verbatim" | "source-locus"
      "type": "principle",
      "obligated_party": "CONTROLLER",
      "obligation_type": "CONTINUOUS",
      "berry_anchor": "§3.3.5 (vagueness), §5.1 (lists lawful, fair)",
      "source_locus": null,             // só preenchido em source-locus variant
      "instances": [
        {
          "n": 1,
          "type": "VAG",
          "severity": "S3",
          "phrase": "lawful, fair, transparent",
          "analysis_text": "Three conjunctive vague adjectives. Each is inquiry-resistant...",
          "variant_readings": [
            { "id": "R1", "reading": "fair = no deception about purpose or use...", "source": "Recital 47 (non-binding); ICO fairness guidance." }
          ]
        }
      ],
      "verbatim": null                  // só preenchido em GDPR-verbatim variant
    }
  ],
  "nist_controls": [
    {
      "id": "PR.DS-01",
      "sources": [
        { "from": "requirement", "ref": "1.1.1", "regulation": "GDPR" },
        { "from": "security_objective", "ref": "SO-D-01.1.GDPR", "regulation": "GDPR" }
      ]
    }
  ],
  "parse_warnings": [
    "<warnings não-fatais: obligated_party fora do enum, YAML fence inválido, etc.>"
  ],
  "counts": {
    "pairs": 6,
    "pairwise_matrix": 6,
    "requirements_high_level": 1,
    "requirements_sub": 4,
    "security_objectives_high_level": 1,
    "security_objectives_sub": 4,
    "ambiguity_cards_by_regulation": { "GDPR": 11, "CRA": 2, "NIS2": 11, "DORA": 11, "AI_Act": 0 },
    "nist_controls_unique": 4,
    "warnings": 0
  }
}
```

---

## 5. REGAS DE PARSING — DETALHE POR SECÇÃO

### 5.1 Divisão em Parts (topo do parser)

```python
# Delimitar Parts pelo H1 único:
part_pattern = re.compile(r'^# Part (\d) — .+$', re.MULTILINE)
# Capturar as posições dos 4 matches; slice do texto entre eles.
# Part 1 = do match 1 até match 2; Part 2 = match 2 até match 3; etc.
# Part 4 = match 4 até EOF.
```

### 5.2 Frontmatter (3 blocos)

```python
# Cada Part pode começar com um bloco --- YAML ---.
# Regex:
fm_pattern = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
# Aplicar dentro de cada Part slice.
# yaml.safe_load() em cada bloco.
# Fundir os 3 dicts num único "metadata": Part 1先 (tem document_id/title/derivation),
# Part 2/3 adicionam parent/macro_domain/sub_domain se não existirem.
```

### 5.3 YAML fences (Volere reqs, Sub-SOs, HSO)

```python
# Regex (multiline, DOTALL):
yaml_fence = re.compile(r'```yaml\n(.*?)\n```', re.DOTALL)
# Para cada match: yaml.safe_load(). Atenção: alguns blocos são uma LISTA YAML
# (reqs começam com "- req_id:"), outros são dict (HSO: "id: ...").
# Lidar com ambos: isinstance(parsed, list) → usar [0].
```

**Mapeamento:**
- HSO HL: fence dentro de `#### D-01.1.0 — High-level SecurityObjective`
- Sub-SOs: fence dentro de `#### D-01.1.N — Sub-SO for REG` (N=1 GDPR, 2 NIS2, 3 CRA, 4 DORA)
- HL req: fence dentro de `### High-level requirement`
- Sub-reqs: fence dentro de `#### N.M — <title>` sob `### Sub-requirements`

**Objective/Considerations** (texto fora do YAML fence, após a fence):
- `**Objective.**` → parágrafo seguinte (uma linha concatenada)
- `**Considerations.**` → bullets `- ` seguintes até próximo heading

### 5.4 Pairs (Part 1 e Part 3) — bold-label pseudo-fields

Delimitador: `##### Pair: REGA ↔ REGB`

```python
pair_heading = re.compile(r'^##### Pair: (\w+)\s*↔\s*(\w+)\s*$', re.MULTILINE)
```

Conteúdo entre dois `##### Pair:` (ou próximo heading de nível menor) = corpo do par.

Dentro do corpo, extrair **bold-label pseudo-fields**:

```python
# Padrão: **Label:** ou **Label (optional parens):** seguido de valor.
# Valor pode ser: inline, blockquote (> ...), bullets (- subkey: val), parágrafo.
field_pattern = re.compile(r'^\*\*([^*]+?):\*\*\s*(.*?)$', re.MULTILINE)
# Depois, para cada field, extrair sub-estrutura (blockquote, bullets) que se segue
# até ao próximo **Label:**.
```

**Campos esperados (nomes normalizados):**
- `gdpr_article`, `nis2_article`, `cra_article`, `dora_article`, `ai_act_article` → `<REG> article (verbatim from ...)`
- `scope_comparison` → bullets `- GDPR scope:`, `- NIS 2 scope:`, `- Scope overlap:`
- `trigger_comparison`, `threshold_timeline_comparison`, `recipient_comparison`, `content_template_comparison`
- `classified_relationship` → valor inline (e.g. `COMPLEMENTARY.`)
- `verified_relationship` → valor inline
- `reasoning` → parágrafo
- `scope_disjoint_test` → valor inline (`Y`/`Conditional`) + bullet `- If Y:`
- `p0_note` (opcional)
- `downstream_implication` → parágrafo

**DEDDUP**: Part 3 é verbatim duplicate de Part 1. Manter **só Part 1** no output. Adicionar `source_part: "Part1"` a cada par.

### 5.5 Pairwise matrix (Part 2) — HTML comment markers

```python
# Delimitadores HTML:
pair_block = re.compile(
    r'<!-- pair: (\w+),(\w+) -->\n(.*?)\n<!-- /pair -->',
    re.DOTALL
)
# Dentro: uma tabela markdown com header-dados (NÃO header-nomes):
#   | GDPR ↔ NIS2 | **Complementary** | Tension/difference |
#   |---|---|---|
#   | **GDPR** (SR-..., Art. ...) | summary | anchor |
#   | **NIS2** (SR-..., Art. ...) | summary | anchor |
# Extrair: classification da 1ª linha (bold), 2 data rows (reg, summary, anchor).
# "Why" paragraph a seguir à tabela (antes de <!-- /pair -->).
```

### 5.6 Participants

```python
participants_pat = re.compile(
    r'<!-- participants: ([^>]+?)-->',
)
# Parsear: split por vírgula, trim, identificar "AI_Act absent" se presente.
```

### 5.7 Emergent tensions (Part 2)

```python
emergent_pat = re.compile(
    r'<!-- emergent: ([\w,]+) -->\n(.*?)\n<!-- /emergent -->',
    re.DOTALL
)
# regulations = lista do atributo; text = bullets concatenados.
```

### 5.8 Ambiguity cards (Part 4) — 3 variantes

**Part 4 começa em `# Part 4 — Relevant Ambiguity (by regulation)`.** Estrutura: `## REGULAÇÃO` (H2) contém cards. Cada H2 pode ser:
- `## GDPR`, `## CRA`, `## NIS2`, `## DORA`, `## AI_Act` (básico)
- `## CRA v0.2 — Article 13 ...`, `## DORA v0.2 — ...`, `## NIS 2 v0.2 — ...` (extensões)
- `## Ambiguity Analysis — NIS 2 ... v0.1 (SUPERSEDED)` (legacy)

**Regra de atribuição de regulamento:** usar o H2 imediatamente acima do card. Extrair o nome do regulamento do início do H2 (até primeiro espaço ou `v0.2`):
- `## CRA v0.2 — ...` → regulação = `CRA`
- `## NIS 2 v0.2 — ...` → regulação = `NIS2` (normalizar "NIS 2" → "NIS2")
- `## GDPR` → regulação = `GDPR`

**TRÊS variantes de card (detetar por heading):**

#### Variante A — "GDPR-light" (H5)
```
##### Art. 5(1)(a) — Lawfulness, fairness, transparency

**Clause: GDPR-CL01** | type: principle | obligatedParty: CONTROLLER | obligationType: CONTINUOUS

**Berry anchor:** §3.3.5 (vagueness), §5.1 (lists `lawful`, `fair`).

**Instance 1 — VAG / S3 / `lawful`, `fair`, `transparent`**

<narrativa>

**Variant readings:**
| # | Reading | Disambiguation source |
|---|---|---|
| R1 | ... | ... |

<concluding paragraph>
```

#### Variante B — "GDPR-verbatim" (H3 `### Article NN`)
```
### Article 10 — Criminal convictions and offences

#### Verbatim
> <blockquote>

#### Clause breakdown
<vazio ou conteúdo>

##### Art. 21(1) — ...    ← próximo card começa aqui
```

#### Variante C — "source-locus" (H4 `#### N.M REG-CLNN — Art. X`)
```
#### 3.1 NIS2-CL07 — Art. 21(1) sentence 1 — Risk-management core obligation

**Source locus:**
> <blockquote>

**Instance 1 — VAG — S3 — `appropriate and proportionate`**

<narrativa + bullets R1/R2/R3>

| # | Reading | Disambiguation source |
|---|---|---|
| R1 | ... | ... |

*Berry anchor:* §5.1 (`appropriate`, `proportionate`).
```

#### Detecção e extração

```python
# Regex de headings de card:
card_gdpr_light = re.compile(r'^##### Art\. (.+?) — (.+)$', re.MULTILINE)
card_gdpr_verbatim = re.compile(r'^### Article (\d+) — (.+)$', re.MULTILINE)
card_source_locus = re.compile(r'^#### [\d.]+ ([A-Z]+-CL\w+) — Art\. (.+?) — (.+)$', re.MULTILINE)
```

**Para cada card, o "corpo" é do heading até ao próximo heading do mesmo ou superior nível.**

**Extração de campos comuns (3 variantes):**

1. **Metadata inline pipe-delimited** (Variantes A e C têm; B não tem):
   ```python
   # Linha: **Clause: GDPR-CL01** | type: principle | obligatedParty: CONTROLLER | obligationType: CONTINUOUS
   meta_pat = re.compile(
       r'\*\*Clause:\s*([A-Z]+-CL\w+)\*\*\s*\|\s*type:\s*([^|]+?)\s*\|\s*obligatedParty:\s*([^|]+?)\s*\|\s*obligationType:\s*([^|\n]+)'
   )
   ```

2. **Source locus** (Variante C):
   ```python
   # **Source locus:** seguido de blockquote.
   source_locus_pat = re.compile(r'\*\*Source locus:\*\*\s*\n>((?:>.*\n?)+)', re.MULTILINE)
   ```

3. **Berry anchor** (ênfase mista — bold OU italic):
   ```python
   berry_bold = re.compile(r'\*\*Berry anchor:\*\*\s*(.+)')
   berry_italic = re.compile(r'\*Berry anchor:\*\s*(.+)')
   # Tentar bold先; se falhar, italic.
   ```

4. **Instances** (padrão com 2 variantes de delimitador):
   ```python
   # Variante 1: **Instance N — TYPE / SX / `phrase`**
   # Variante 2: **Instance N — TYPE — SX — `phrase`**
   instance_pat = re.compile(
       r'\*\*Instance (\d+) — ([A-Z+]+) [—/] ([SN]\d) [—/] `([^`]+)`\*\*'
   )
   ```

5. **Variant readings** (tabela `| # | Reading | Disambiguation source |`):
   ```python
   # Dentro do corpo de cada instance, procurar a tabela.
   readings_pat = re.compile(
       r'\|\s*(R\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|\n]+?)\s*\|'
   )
   # Ignorar a linha de separator (|---|---|---|) e o header (| # | Reading | ... |).
   ```

6. **Verbatim** (Variante B): blockquote sob `#### Verbatim`.

7. **analysis_text**: todo o texto narrativo da instance entre o heading da instance e a tabela de variant readings (excluindo bullets R1/R2/R3 inline se existirem, mas **incluindo** bullets de análise). Preservar como string (limpar markdown residual: strip `**bold**` wrappers preservando o texto dentro, mas manter bullets e estrutura).

**Casos especiais a tratar:**

- **Heading malformado L418** (`#### Scope-overlap principle (operational). The high-level SO...` é um parágrafo, não heading): este heading está em **Part 1 §2**, não em Part 4. O parser de Part 4 não o atingirá. **Ignorar.**

- **CL-ID reuse** (NIS2-CL07 aparece para Art. 21(1) sentence 1 E Art. 21(2)(c) Crisis management): cada card é uma entrada separada no array `ambiguity_cards`. Key = `(clause_id, article_ref)`. **Não colapsar.** Adicionar warning se o mesmo `(clause_id, article_ref)` aparecer duplicado.

- **Empty `#### Clause breakdown`** (Variant B, Articles 10/26/33): o conteúdo é vazio. Adicionar o card mesmo assim, com `instances: []` e `berry_anchor: null`.

- **`_No applicable AI_Act ambiguity._`**: criar card AI_Act com `clause_id: null`, `instances: []`, `title: "No applicable ambiguity"`.

- **Cards source-locus com numbering reusado** (`#### 3.1 ...` aparece 4×): não confiar no numbering. Usar `clause_id + article_ref` como identificador único.

### 5.9 NIST controls (agregação)

Pós-parsing, iterar sobre `requirements.sub_requirements` + `security_objectives.sub_objectives` e agregar todos os `nist_csf` IDs numa lista única `nist_controls`, com `sources` indicando origem. **Dedup por ID.**

### 5.10 Validação de enums

```python
# Carregar 00_METHODOLOGY/SCHEMA/obligated_party.yaml
# Validar cada ambiguity_card.obligated_party contra canonical_enum.
# Se fora do enum: adicionar a parse_warnings (NÃO crashar).
```

---

## 6. CLI DE FILTRAGEM — `filter.py`

### 6.1 Interface

```bash
python filter.py --domain D-01.1 --regs CRA,GDPR [--format json|table|summary]
```

Argumentos:
- `--domain` (obrigatório): sub-domain ID (e.g. `D-01.1`)
- `--regs` (obrigatório): regulamentos aplicáveis, comma-separated (e.g. `CRA,GDPR`)
- `--format` (opcional, default `summary`): `json` (JSON filtrado completo), `table` (ASCII tables por secção), `summary` (contadores + amostra)

### 6.2 Lógica de filtragem

Para `--regs CRA,GDPR`:

| Secção do JSON | Regra |
|---|---|
| `metadata`, `subdomain` | sempre incluído |
| `subdomain.participants` | filtrar para só os que estão em regs |
| `security_objectives.high_level` | sempre incluído (agrega todos) |
| `security_objectives.sub_objectives` | `regulation in regs` |
| `requirements.high_level` | sempre incluído (agrega todos) |
| `requirements.sub_requirements` | `regulation in regs` |
| `pairs` | incluir se **ambos** os elementos do par estão em regs |
| `pairwise_matrix` | incluir se **ambos** os elementos do par estão em regs |
| `emergent_tensions` | incluir se **todos** os elementos estão em regs |
| `ambiguity_cards` | `regulation in regs` |
| `nist_controls` | incluir se **alguma** source tem `regulation in regs` |
| `counts` | recalculado sobre o conjunto filtrado |

### 6.3 Output `--format summary` (default)

Texto legível com contadores por secção + primeiros 200 chars de cada item. Exemplo:

```
Domain: D-01.1 — Data at Rest Encryption
Filters: regulations = [CRA, GDPR]

Participants (filtered): CRA, GDPR

Pairs (1 of 6):
  [1] CRA ↔ GDPR — COMPLEMENTARY (verified: SAME)
      Reasoning: The OJ texts impose...

Sub-requirements (2 of 4):
  [1] 1.1.3 (CRA) — Product-stored data is encrypted using state-of-the-art mechanisms
      NIST: PR.DS-01
  [2] ...

Sub-SOs (2 of 4):
  ...

Ambiguity cards (N of M):
  [1] CRA / CRA-CL01 / Art. 6 chapeau + (a) — Essential-requirements gate (Part I)
      instances: 4
  ...

NIST controls (aggregated): PR.DS-01, PR.DS-02, ...
```

### 6.4 Output `--format table`

ASCII tables (usar `tabulate` SE disponível; senão, hand-rolled com `|` separators). Uma tabela por secção.

### 6.5 Output `--format json`

JSON completo filtrado (mesmo schema que o sidecar, mas com arrays filtrados). Útil para pipe para `jq`.

---

## 7. FICHEIROS A CRIAR (3)

### 7.1 `00_METHODOLOGY/PREPROCESSING_by_domain/parse_domain.py`

Parser CLI:

```bash
python parse_domain.py <path-to-D-XX.Y.md> [--output <path>] [--pretty]
# Default: escreve <dirname>/<basename>.json
# --pretty: indent=2 (default true)
```

Estrutura do ficheiro:
- Shebang + docstring
- Imports (stdlib + yaml)
- Constantes (regex patterns, paths relativos a SCHEMA)
- Funções de parsing (uma por secção: `_parse_frontmatter`, `_parse_parts`, `_parse_pairs`, `_parse_pairwise_matrix`, `_parse_security_objectives`, `_parse_requirements`, `_parse_ambiguity_cards`, `_parse_participants`, `_parse_emergent_tensions`, `_aggregate_nist_controls`, `_validate_enums`)
- Função `parse_domain_file(md_path: Path) -> dict` (entry point)
- Função `_emit_json(data: dict, output: Path)` (com `parsed_at` timestamp UTC ISO 8601)
- `if __name__ == "__main__":` com argparse

### 7.2 `00_METHODOLOGY/PREPROCESSING_by_domain/filter.py`

Filtros CLI. Carrega `<domain-id>.json` sidecar. Estrutura:
- Imports
- Funções de filtro (uma por secção)
- Funções de output (`_render_summary`, `_render_table`, `_render_json`)
- `if __name__ == "__main__":` com argparse

### 7.3 `00_METHODOLOGY/PREPROCESSING_by_domain/SCHEMA_domain_json.md`

Documentação do schema de saída. Estrutura:
- Overview + versionamento (`schema_version`, `parser_version`)
- Tabela de campos top-level (nome, tipo, descrição, obrigatório?)
- Sub-schema por secção (com exemplos)
- Enum: `obligated_party` (link para `obligated_party.yaml`)
- Regras de dedup e normalização (NIS 2 → NIS2, etc.)
- Changelog

---

## 8. CRITÉRIOS DE ACEITE (testar antes de entregar)

1. **`python parse_domain.py domains/D-01_Data-Protection/D-01.1/D-01.1.md`** gera `D-01.1.json` sem erros (warnings OK).
2. **Round-trip determinismo**: correr 2× e fazer `diff` dos JSONs (excluindo a linha `parsed_at`) → têm de ser **byte-idênticos**.
3. **Cobertura estrutural** (assert no `counts`):
   - `pairs == 6` (não 12 — dedup Part1/3)
   - `pairwise_matrix == 6`
   - `requirements_high_level == 1`, `requirements_sub == 4`
   - `security_objectives_high_level == 1`, `security_objectives_sub == 4`
   - `ambiguity_cards_by_regulation` reportado (GDPR/CRA/NIS2/DORA/AI_Act) — número exato a confirmar no run, não assumir
   - `warnings == 0` (idealmente)
4. **CLI filtragem**: `python filter.py --domain D-01.1 --regs CRA,GDPR --format summary` corre sem erro e mostra:
   - Participants: CRA, GDPR (2)
   - Pairs: 1 (CRA↔GDPR)
   - Sub-requirements: 2 (1.1.3 CRA + ... )

   wait — D-01.1 tem sub-reqs 1.1.1 GDPR / 1.1.2 NIS2 / 1.1.3 CRA / 1.1.4 DORA. Filtrar CRA,GDPR → 2 sub-reqs.
   - Sub-SOs: 2 (CRA + GDPR)
   - Ambiguity cards: apenas CRA + GDPR
   - NIST controls: agregados de CRA + GDPR sources
5. **Schema válido**: `D-01.1.json` faz parse com `json.load()` sem erro.
6. **Enum**: nenhum `obligated_party` fora de `obligated_party.yaml canonical_enum` (se houver, aparece em `parse_warnings`).

---

## 9. BRANCH WORKFLOW (MUITO IMPORTANTE)

O repo **PROÍBE commits diretos em `main`** (ver `AGENTS.md`). Seguir:

```bash
cd /home/epmq-cyber/Área\ de\ Trabalho/projects/Methodology-main

# 1. Criar branch feature
git checkout main
git pull origin main
git checkout -b feature/domain-parser-pilot

# 2. Implementar (3 ficheiros novos — não há ficheiros modified)

# 3. Validar localmente
python 00_METHODOLOGY/PREPROCESSING_by_domain/parse_domain.py \
    00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.md
python 00_METHODOLOGY/PREPROCESSING_by_domain/filter.py \
    --domain D-01.1 --regs CRA,GDPR --format summary

# 4. Commit (NÃO push sem confirmação)
git add 00_METHODOLOGY/PREPROCESSING_by_domain/parse_domain.py \
        00_METHODOLOGY/PREPROCESSING_by_domain/filter.py \
        00_METHODOLOGY/PREPROCESSING_by_domain/SCHEMA_domain_json.md \
        00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.json
git commit -m "feat: domain parser pilot D-01.1 (parse_domain.py + filter.py + schema doc)"
```

**Não fazer `git push` sem confirmação explícita do utilizador.**

---

## 10. NOTAS DE ESCALABILIDADE (para validação de design)

O piloto deve ser escrito de forma a escalar aos 38 domínios. Verificações de design:

- O 4-Part H1 skeleton é **100% consistente** em todos os 38 ficheiros (`# Part 1 — Sub-domain definition`, `# Part 2 — Domain Analysis (cross-regulation)`, `# Part 3 — Deep Analysis (per-pair)`, `# Part 4 — Relevant Ambiguity (by regulation)`).
- **Não hardcodar** "D-01.1", "GDPR/NIS2/CRA/DORA", ou counts específicos. Tudo deve ser derivado do conteúdo.
- Part 4 pode ter H2 extra (`## CRA v0.2 — Article 13 ...`, `## DORA v0.2 — ...`). O parser de ambiguity cards trata-as como cards source-locus sob a regulação extraída do H2.
- D-08 e D-10 têm **3 sub-domínios** em vez de 4 (sem impacto no parser).
- **Paths relativos**: o parser deve funcionar com path absoluto OU relativo. O `source_path` no JSON deve ser relativo à raiz do repo.
- **Idempotência**: `parsed_at` é o único campo não-determinístico. Tudo o resto deve ser determinístico.

---

## 11. O QUE NÃO FAZER

- ❌ Modificar `.md` originais (read-only).
- ❌ Gerar JSON para os outros 37 domínios (só D-01.1 neste piloto).
- ❌ Adicionar lints ao pre-push hook (follow-up).
- ❌ Introduzir Pydantic, dataclasses, markdown-it-py, python-frontmatter, ou qualquer lib nova.
- ❌ Hardcodar counts esperados como assertions que crashe o parser (devem ir para `counts` no output, não para `assert`).
- ❌ Fazer `git push` sem confirmação do utilizador.
- ❌ Commitar em `main` (sempre feature branch).

---

## 12. ENTREGÁVEL

No final, o utilizador deve ter:

1. `00_METHODOLOGY/PREPROCESSING_by_domain/parse_domain.py` — parser funcional
2. `00_METHODOLOGY/PREPROCESSING_by_domain/filter.py` — CLI de filtragem funcional
3. `00_METHODOLOGY/PREPROCESSING_by_domain/SCHEMA_domain_json.md` — schema documentado
4. `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01_Data-Protection/D-01.1/D-01.1.json` — output gerado
5. Branch `feature/domain-parser-pilot` com commit (não pushed)
6. Relatório de validação (output dos comandos de teste da secção 8) partilhado com o utilizador.

---

**FIM DO BRIEF**
