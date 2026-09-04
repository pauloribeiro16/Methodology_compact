# Andar 1 — Orquestração qwen3.8:27b sobre corpus AEGIS (reutilizando aegis-phase1)

> **Decisão de reutilização**: manter `Phase1Orchestrator`, `Phase1GraphState`, todos os modelos Pydantic e a state machine LangGraph v2. **Adaptar apenas os prompts** (catálogo `prompts_v2/catalog.py`) e a função `assemble_inputs` (camada de contexto) para operar sobre o corpus AEGIS (38 sub-domínios + 3 cases) em vez de um intake de empresa.

---

## O que muda vs Andar A original do roadmap

| Componente | Roadmap original (KG) | Este Andar 1 (orquestração) |
|---|---|---|
| Modelo | `qwen3:8b` (95%, 4s/Q) | **`qwen3.8:27b`** (27B, 256K ctx, o mesmo do E3 KG) |
| State machine | (Graphify extrai, sem orquestração) | **LangGraph v2 do aegis-phase1** — reutilizado |
| Input | `.md` dos protótipos | **Corpus AEGIS**: `00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX.Y/**` (38 subdomínios) + `02_CASES/Case_0{1,2,3}/**` |
| Output | `graph.json` (KG extraído) | **Doc 04-07-like**: Company Context Assessment, Regulatory Applicability, Clause Mapping Matrix, Structured Compliance Matrix — mas agora sobre os AEGIS docs, não sobre uma empresa |
| Job | `graphify extract .` | `run_phase1_graph(orch, case_path=corpus_aegis)` |
| sbatch | `graphify_E1_qwen38.sbatch` (já escrito) | **Mesmo template, 2-3 linhas a alterar** |

---

## Passos concretos

### 1. Setup local (read-only agora; execução após aprovação)

1. **Reactivar skill** `hpc-deucalion`: `mv ~/.zcode/skills.disabled/hpc-deucalion ~/.zcode/skills/`
2. **Clonar/copiar** `aegis-phase1` para `~/aegis-kg/aegis-orchestrator/` (NFS, 22 TB; sítio onde já correu o E3)
3. **Verificar dependências**: `pip install -e ".[all]"` (já feito pelo user no clone principal; venv dentro do clone)
4. **Confirmar Ollama em Deucalion** via scout: `ssh … login.deucalion.macc.fccn.pt` → `ollama list | grep qwen3.8`

### 2. Adaptações ao código (todas dentro de `aegis-orchestrator/`, branch isolada)

**Ficheiros a tocar** (mínimo, cirúrgico):

| Ficheiro | Acção | Risco |
|---|---|---|
| `src/aegis_phase1/prompts_v2/catalog.py` | **Adaptar** os templates P1C-LLM-01/02/03 + P1B-LLM-01/02 para o novo domínio (corpus AEGIS, não intake de empresa) | Baixo — substituições literais nos prompts |
| `src/aegis_phase1/v2/orchestrator.py` | **Patch** em `_load_v2_catalog` (~50 linhas) para o novo `case_profile_loader` ler o corpus AEGIS em vez de `case.yaml` | Médio — pode precisar de classes adaptadoras |
| `src/aegis_phase1/v2/state.py` | **Patch** em `V2State` para campos específicos do corpus AEGIS (sub_domain refs em vez de company facts) | Baixo |
| `src/aegis_phase1/v2/loader/` | **Novo** `corpus_aegis_loader.py` (substitui `case_profile_loader.py`) — carrega `00_METHODOLOGY/PREPROCESSING_by_domain/domains/*.md` + `02_CASES/*/00_COMMON/*.yaml` | Médio |
| **NÃO tocar**: `graph.py`, `models.py`, `subphases/`, `nodes/`, `prompts/invoker.py`, `llm/` | Estrutura reutilizada tal-qual | Zero |

**Lógica das adaptações**:
- O `case_profile_loader` actual lê uma empresa (TinyTask). O novo `corpus_aegis_loader` lê o **estado actual do corpus AEGIS** (38 sub-domínios, 282 SRs, 328 SOs, 196 pairs, 3 cases) como se fosse "uma empresa" — mas a empresa é "o repositório AEGIS".
- Os prompts passam de "intake this company's profile + produce Doc 04-07" para "audit this corpus of N sub-domains + produce a re-derivation matrix that cross-references the canonical Phase 1/2/3 docs against the corpus ground truth".

### 3. Job SLURM (template `graphify_E1_qwen38.sbatch`, 2-3 linhas alteradas)

```diff
- # Graphify E1 smoke with qwen3.8:27b (same scope as the gemma4:26b E1 run:
- # D-01.1 Data at Rest Encryption, 25 files). Uses the NEW ollama 0.32.13 in
- # graphify-methodology/{bin,lib} — the pre-installed 0.31.1 cannot run qwen3.8.
+ # AEGIS orchestration E1 smoke with qwen3.8:27b — LangGraph state machine on
+ # corpus AEGIS (38 sub-domains × 1 case). Adapt input dir to aegis-orchestrator/work/.
```

```diff
- SCOPE="E1_qwen38_D-01.1"
+ SCOPE="orch_E1_qwen38_aegis_corpus"
```

```diff
- cp -r input/E1/* "$RUN_DIR/work"
- cd "$RUN_DIR/work"
- $GRAPHIFY extract . --backend ollama
+ cd "$RUN_DIR/work/aegis-orchestrator"
+ python -m aegis_phase1.v2.runner \
+     --case-path /projects/F202512235CPCAA1/aegis-orchestrator/work/corpus \
+     --output-dir "$RUN_DIR/output" \
+     --model "$MODEL"
```

Resto do sbatch fica igual (env vars, ollama serve, warm-up, kill).

### 4. Verificação (quando o job voltar)

1. **8-10 ficheiros em `output/`** — correspondem aos Doc 04-07 do aegis-phase1 mas aplicados ao corpus.
2. **Comparar** os Doc 04a-d com os **originais Case_01** (em `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/Doc04*.md`) — divergências esperadas (input é o corpus inteiro, não uma empresa) são **bons sinais**, não bugs.
3. **Logs do LangGraph** (trace `AEGIS Phase 1` → 4 subgraphs × N nós) confirmam que **7-9 chamadas LLM** foram feitas em sequência, não em paralelo.

### 5. O que NÃO entra neste Andar (defer)

- Sub-domínios múltiplos em paralelo (E2 com 10 shards) — fica para Andar 2.
- Multi-modal (imagens dos casos) — Andar 3.
- Neo4j + KG web viewer interactivo — Andar 3.
- Rever o `subphases/subphase_*.py` (placeholders vazios) — o v2 já está completo, os v1 não são usados.
- Langfuse tracing (cluster-side) — o código já tem o gancho mas requer Postgres+Clickhouse+Redis+MinIO no cluster, fora do escopo.

---

## Custos

| Item | Estimativa |
|---|---|
| Fila `dev-a100-80` | ~10-30 min espera |
| Walltime | ~1-2h (7-9 chamadas × 5-15min cada; 27B + 256K ctx é pesado) |
| Storage Lustre | ~50-200 MB temporário (output + work/) |
| Comparação E3 KG (mesmo modelo) | 14h × 13 shards — **este Andar 1 é 1 shard com state machine estruturada →10× mais barato** |

---

## 4 P7 fechadas

- **Nº protótipos**: N/A — corpus AEGIS inteiro (38 subdomínios × 3 cases). **Controle**: limitar o Andar 1 a 1 case (Case_01, 13 docs da Fase 1) para não escalar já.
- **3 modelos Ollama**: N/A — **só `qwen3.8:27b`** conforme instrução.
- **Dataset MCQ**: N/A — substituído por "Doc 04-07 against corpus AEGIS" (output estruturado).
- **Janela de fila**: `dev-a100-80` (≤4h, fila curta) para o Andar 1.

---

## O que NÃO entra no plano (intencionalmente, P7 + escopo)

- **Não instalo nada** no Deucalion sem aprovação P7 nos 4 pontos acima (todos fechados por defeito seguro: 1 case, 1 modelo, output estruturado, fila curta).
- **Não corro `sbatch`** sem o scout voltar a confirmar que `qwen3.8:27b` está no cache.
- **Não mexo em `Methodology_compact`** — toda a orquestração corre no cluster, isolada.
- **Não escrevo código de orquestração novo** — só adaptações ao aegis-phase1.