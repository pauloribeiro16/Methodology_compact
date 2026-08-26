# Graphify Knowledge Graph — Navigation Reference

> **Status**: knowledge graph is built and audited (build E3, 2026-08-23).
> 3,882 concepts (after NIST-id dedup, 2026-08-24) · 11,232 edges · 1,025 hyperedges · 0 dangling refs · 90.2% EXTRACTED.

---

## What this graph is

A traversable semantic map of the methodology core: the **38 security sub-domains** (D-01..D-10) plus the **3 case studies** (Case_01..Case_03). Built by Graphify using `ollama qwen3.8:27b` on Deucalion (A100-80GB), with deterministic post-processing (2-pass label dedup + canonical-ID dedup + phantom-node materialization).

It is **complementary**, never a substitute, for:
- `00_METHODOLOGY/dependency_graph.yaml` (template-level requirements) — gates
- The lint scripts under `01_IMPLEMENTATION_TOOLS/lints/` *(lives in Methodology-main, not here)*

> ⚠️ **Compact-repo note.** This graph was built against the corpus of **Methodology-main** on 2026-08-23. The compact corpus may have drifted (fewer files, less context). Use `scripts/kg.sh audit` to confirm integrity; if `source_file` lookups miss, the affected sub-domain corpus has been trimmed — rebuild on Deucalion (see procedure below) or fall back to `dependency_graph.yaml` + `grep` per AGENTS.md P5.

| Where to find it (in this repo) | |
|---|---|
| **Wrapper** | `scripts/kg.sh` (auto-discovers `./kg/*/graphify-out/graph.json`; `--graph <path>` overrides; `GRAPHIFY_BIN` overrides the external CLI) |
| **Data (E3 build)** | `kg/E3_2026-08-23/graphify-out/graph.json` (5.95 MB) |
| **Viewer** | `kg/E3_2026-08-23/graphify-out/graph.html` (6.22 MB, open in a browser — no server needed) |
| **Protocol** | this file (`kg/GRAPHIFY.md`) |
| **Original build (external)** | `/home/epmq-cyber/Área de Trabalho/projects/Deucalion/results/graphify/E3_2026-08-23/graphify-out/` |
| **Cluster (read-only)** | `/projects/F202512235CPCAA1/graphify-methodology/results/E3_merged/dedup/graphify-out/graph.json` |
| **Cluster per-shard** | `/projects/F202512235CPCAA1/graphify-methodology/results/E3_shards/*/work/graphify-out/graph.json` |
| **Job scripts** | `~/Área de Trabalho/projects/Deucalion/aegis_jobs/graphify_E3_array.sbatch`, `track_E3.sh`, `graphify_E1_*.sbatch`, `graphify_download_qwen38.sbatch` |
| **Consolidation scripts** | `/projects/F202512235CPCAA1/graphify-methodology/consolidate_E3.py`, `materialize_phantoms.py` |

---

## Cheat sheet — agent navigation (no LLM needed, all read `graph.json`)

Graphify navigation commands take a label string (substring, fuzzy) or a full node id; for batch/script use pass `--json`.

| Intent | Command |
|---|---|
| Find a node and its direct context (validator-friendly) | `graphify explain "<label>" --graph <graph.json>` |
| Shortest path between two concepts (regulation → control) | `graphify path "<A>" "<B>" --graph <graph.json>` (add `--undirected` if no path) |
| Discover hubs (most connected) | `graphify god-nodes --top 10 --graph <graph.json>` |
| Search by question (BFS, up to budget tokens) | `graphify query "<natural-language>" --graph <graph.json> --budget 2000` |
| Reverse-impact from a node | `graphify affected "<label>" --graph <graph.json> --depth 2` *(see notes)* |
| Saved outcome for learning loop | `graphify save-result --question Q --answer A --outcome useful` |

The local install lives at `~/.venvs/graphify/bin/graphify` (no `openai` key required for navigation).

**Wrapper (preferred in this repo):** `scripts/kg.sh <subcommand> ...` — same CLI surface, no `--graph` flag needed (auto-discovers the latest `graph.json` under `kg/`); 6 of 10 subcommands (`where`, `domain`, `map`, `nist`, `hyper`, `audit`) are pure-stdlib Python and work without the external CLI. Override the CLI binary with `GRAPHIFY_BIN=/path/to/graphify` if it isn't on the default location.

---

## When to use it (per agent role)

### Executor — pre-change impact (principle P5)

Before propagating any change to a regulatory mapping or sub-domain definition, trace what depends on the affected concept:
```
graphify explain "SR-DORA-029" --graph <graph.json>     # who references me?
graphify god-nodes --top 20 --graph <graph.json>        # am I touching a hub?
```
A node with degree > 50 means the change will affect 50+ cross-references in the methodology corpus — escalate to the human before writing.

### Validator — traceability verification (principle P4)

For traceability spot-checks (regulation → requirement → control → NIST CSF):
```
graphify path "<reg_article>" "<nist_control>" --graph <graph.json> --undirected
graphify explain "<requirement_id>" --graph <graph.json> | head -20
```
A green `EXTRACTED` confidence does NOT prove correctness — it only means the relation was grounded in the source text. Always grep the file at the cited `source_location` before citing the relation downstream.

---

## Integrity rules (must follow, regardless of confidence label)

1. **EXTRACTED ≠ truth**. Spot-check 10/10 in E3 was grounded, but the spot-check is per-sample. The Validator MUST verify any EXTRACTED edge cited in deliverables by grepping the cited `source_location`. Graphify surfaces the location; the agent confirms.
2. **INFERRED = hypothesis**. Inferred edges are valuable as discovery hints (cross-regulation convergences, paraphrases) but **must not be cited as audit evidence**. Always mark them in deliverables with `[INFERRED — needs verification]`.
3. **The deterministic YAML/lints still rule.** When Graphify disagrees with `00_METHODOLOGY/dependency_graph.yaml` or the lint scripts (in Methodology-main) — the deterministic tools win (principle P1). Graphify is the exploration layer, not the gate.
4. **Nó órfão `d_07_1`** (synthetic, source_file=None, label `"d 07 1"`) is a malformed extraction artifact; ignore in queries or rename to a meaningful label before citing.
5. **Phantom nodes** (`"synthetic": true`, source_file=None) are concept-level anchors — they have no source text. Acceptable as targets, never as evidence for a requirement.

---

## Known limitations (do not paper over)

| Limitation | Mitigation |
|---|---|
| `query` is BFS, not semantic — surfaces many weakly-related nodes | pass `--context <relation>` to filter; use `explain` for focused lookups |
| `affected` (reverse-traversal) requires the source node to be a strict target in the graph; regulatory articles (`Art. X`) rarely are | use `path` or `explain` instead; `affected` works only on requirement IDs like `SR-*` |
| Top relation is `references` (83% of edges); `implements`, `cites`, `inherits` are sparse | documentation limitation; model output bias. Would need prompt redesign to rebalance |
| Coverage: 4 large files (`D-07.3.md`, `D-07.4.md`, `D-09.3.md`, `D-09.4.md` ≈ 1.1MB total) generated no nodes despite re-run | those are composite "deep analysis" docs; expect them to need a dedicated `graphify label --mode deep` rebuild if their absence becomes material |
| 79 isolated nodes (1.6%) | mostly singleton concepts; expected; not actionable |

### Query workarounds (validated 2026-08-26)

Findings from a 10-query navigability test run against the compact repo (9/10 queries returned useful results):

1. **NIST sub-controls in `nist` depend on file-derived labels.** `nist PR.DS-01` resolves (file-derived nodes carry that label), but `PR.AC-01` / `PR.AC` return "no node labelled" — after the 2026-08-24 NIST-id dedup, canonical nodes are synthetic `nist_*` and only some sub-controls have file-derived label counterparts. **Workaround:** run `where "<ID-prefix>"` (e.g. `where "PR.AC"`) to find the canonical/file-derived nodes that do exist, then `doc "<full label>"` for context.
2. **`trace` with ambiguous labels proceeds silently on the best score.** The CLI prints `warning: source match was ambiguous (top score X, runner-up Y)` and continues with the top candidate — the chosen node is not restated in the path output. **Mitigation:** use full unambiguous labels; target specific article clauses (`GDPR Art. 32(1)(c): Timely Restoration of Availability`, not `GDPR Art. 32`), consistent with the RP-4 critical lesson. If the warning appears, re-run with a more specific label before citing the chain.
3. **Read (relation, confidence) as a pair.** Conceptual relations (`conceptually_related_to`) can carry `EXTRACTED` confidence — EXTRACTED means "grounded in source text at the cited location", not "deterministically true". Hop counts like RP-8's "4 of 5 hops EXTRACTED" count the confidence field, not the relation type. When citing a chain downstream, always quote relation + confidence together (e.g. `[conceptually_related_to — EXTRACTED]`).

---

## Reasoning patterns (validated 2026-08-24)

Eight agent-use patterns, each validated against the E3 build. Use them as the **starting toolkit** for any new analysis; expand from here.

### RP-1 — Impact analysis (principle P5, propagation cost)
```
graphify affected "SR-GDPR-014" --graph <graph.json> --depth 2
```
Reverse-traversal of the requirement graph. Works on requirement IDs (`SR-*`, `SO-*`), not on shard or article labels.
**Validated**: SR-GDPR-014 → **65 impacted nodes** at depth 2, including case-derived requirements (`Req 4.1.1`, `Req 4.3.1`, `Req 4.4.1`). Quantifies the ripple cost *before* writing.
**Rule**: if `affected --depth 2` returns >50 nodes, escalate the change to the human.

### RP-2 — Cross-regulation convergence (the thesis gold)
Python recipe — iterate INFERRED links with relation in `semantically_similar_to`/`conceptually_related_to`, classify endpoints by `SR-<REG>-` prefix:
```python
pairs = Counter()
for l in g["links"]:
    if l["confidence"] != "INFERRED": continue
    if l["relation"] not in ("semantically_similar_to","conceptually_related_to"): continue
    rs, rt = reg_of(l["source"]), reg_of(l["target"])
    if rs and rt and rs != rt:
        pairs[tuple(sorted([rs, rt]))] += 1
```
**Validated in E3**: 170 cross-regulation endpoint-pairs across 10 regulation pairs. Top: DORA↔GDPR=52, CRA↔DORA=41, GDPR↔NIS2=34, AIACT↔CRA=14.
**Always** label the output `[INFERRED — needs verification]`. These are candidate unified controls, never evidence.

### RP-3 — Reverse NIST index (operationalisation check)
For any NIST CSF control, find all security requirements that operationalise it:
```python
tgt = [n for n in g["nodes"] if n["label"].upper().startswith("NIST CSF PR.DS-01")]
for l in g["links"]:
    if l["target"] == tgt[0]["id"]:
        print(nodes[l["source"]]["label"], l["relation"], l["confidence"])
```
**Validated**: `PR.DS-01 (Data-at-Rest)` receives **55 inbound references**, mostly from CRA/DORA/GDPR confidentiality/encryption requirements. This is what "operationalised in NIST CSF 2.0" looks like from the requirement side.
**Note**: after the 2026-08-24 NIST-id dedup, canonical ids are `nist_*` (synthetic), with file-prefixed duplicates merged.

### RP-4 — Case → base-legal traceability
```
graphify path "Rules Catalog (Case 03 OmniBank)" "GDPR Art. 32(1)(c): Timely Restoration of Availability" --undirected --graph <graph.json>
```
**Validated** (5 hops): Rules Catalog → Doc 08 → NIS2 → SR-DORA-015 → SR-GDPR-024 → **GDPR Art. 32(1)(c)**. Each hop carries the relation + confidence.
**Critical lesson from testing**: target must be an unambiguous article clause (e.g. `Art. 32(1)(c)`), not a generic `GDPR Art. 32` (which triggers the ambiguity warning and resolves fuzzily).

### RP-5 — Thematic communities (reading map)
```
graphify cluster-only <graph-dir> --no-label --graph <graph.json>
```
**Validated in E3**: 6 largest communities, each 200-275 nodes. Hubs reveal the community theme — e.g. Community 1 centres on DORA risk-management SRs (`SR-DORA-004/029/008`); Community 10 on cross-state CIA+A cryptography SRs.
**Use**: as a reading map when navigating the corpus for the first time, or when an Executive asks "what's in scope?".

### RP-6 — Coverage matrix (methodology QA, free)
Python recipe — for each `D-XX.Y` subdomain, which regulations are represented?
```python
cov = defaultdict(set)
for n in g["nodes"]:
    r = reg_of(n["id"])
    sd = re.match(r"(D-\d+\.\d+)", n["source_file"] or "").group(1) if n["source_file"] else None
    if r and sd: cov[sd].add(r)
```
**Validated in E3**: 23 of 34 `D-XX.Y` subdomains have SR nodes. **Zero** subdomains have all 5 regulations. `D-02.2/D-02.3` are CRA-only; `D-02.4` is DORA-only; AI Act is absent from every D-01 sub-domain.
**Caveat**: 4 large deep-analysis files (D-07.3/7.4/9.3/9.4) generated no nodes; their absence may understate coverage. Treat the matrix as a *lower bound* for AI Act and possibly CRA.

### RP-7 — Hub watchdog (architectural risk)
```
graphify god-nodes --top 10 --graph <graph.json>
```
**Validated**: top 10 hubs are 8× DORA + 2× GDPR. `SR-DORA-001 (CIA+A Protection Matrix)` has 101 edges — the single most connected requirement in the corpus.
**Rule**: any change to a top-10 hub affects >85 cross-references → always escalate.

### RP-8 — Cross-domain reasoning chain (the kill-shot)
```
graphify path "SR-DORA-003: Classification-Driven Cryptographic-Key Protection with Policy Linkage" "AI Act Art. 15(3) — Resilience against errors/faults/drift (SR-AIACT-015)" --undirected --graph <graph.json>
```
**Validated** (5 hops): DORA-003 ↔ SR-CRA-001 [INFERRED] → `concept nist csf 2 0` ← SR-AIACT-021 ← AI Act 15(1) ↔ AI Act 15(3). **4 of 5 hops are EXTRACTED**. This is the kind of multi-regulation reasoning chain no individual document states — and exactly the type of "discovery" the methodology claims to enable.
**Use**: for thesis argumentation, cross-domain audit narratives, and to surface emergent structures that inform research questions.

---

## Rebuild / update procedure

1. **Cluster pull** (only if you have the AEGIS-Phase 1 repo clone on Deucalion):
   `cd /projects/F202512235CPCAA1/graphify-methodology && git pull` (NB: this repo lives in your local cluster workspace, not in `Methodology-main`)
2. **Stage new corpus** at `input/E3/<SHARD>/` (only `.md`, exclude `*.json`, `*.manifest.json`, `review/`, `Legacy/`). The compact corpus here (`00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-XX.Y/**` + `02_CASES/Case_0{1,2,3}/**`) is a valid input set — stage it directly from this repo if working from the compact.
3. **Re-extract incrementally** (cache reuses previous work):
   `sbatch --array=0-12%4 graphify_E3_array.sbatch` — only the affected shards
4. **Re-consolidate** on the cluster:
   `python3 consolidate_E3.py && python3 materialize_phantoms.py`
5. **Audit** (run this script before any commit/copy):
   - Re-check `dangling=0`, `relation="INFERRED"`=0, hyperedge broken refs=0
   - Spot-check ≥ 10 EXTRACTED edges with `--undirected` path query
   - Coverage: 0 critical files missing in your scope
6. **Copy** the new `graph.json` (and optionally `graph.html`) into `kg/<BUILD>/graphify-out/` and commit
7. **Commit** the updated `kg/GRAPHIFY.md` footer with the new build date

---

## Provenance & reproducibility

| Build | Date | Model | Walltime | Nodes / Links / Hyper | Failures |
|---|---|---|---|---|---|
| E1 gemma | 2026-08-15 | gemma4:26b (Ollama) | 34 min | 446 / 667 / 30 | 0 |
| E1 qwen | 2026-08-15 | qwen3.8:27b (Ollama) | 57 min | 446 / 667 / 30 (same scope) | 0 |
| **E3** | **2026-08-23** | **qwen3.8:27b** | **~14h (4-GPU array, 13 shards) + 36min incremental re-run** | **3,882 / 11,232 / 1,025** (after 2026-08-24 NIST dedup) | **0** |

Cluster notes:
- Jobs used `normal-a100-80` partition, 1× A100-80GB per task, `--gres=gpu:a100:1`
- `NUM_CTX=262144`, `OLLAMA_NUM_PARALLEL=2` (only safe at this context size)
- `GRAPHIFY_API_TIMEOUT=1800000` (30 min) was the critical fix; default timeouts fail the largest chunks
- `--token-budget 12000` was the second critical fix; default 60000 truncates the largest shards
- Array limit `%4` (max 4 concurrent) keeps queue fair; all 13 fit in ~14h