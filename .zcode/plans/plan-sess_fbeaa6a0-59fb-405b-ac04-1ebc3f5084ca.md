# Campanha Paridade Estrutural — Case_02 ao nível do Case_01 (grafo completo + validator completo + dashboard P1 I–VIII)

## Problema
O Case_02 tem só o Folio VIII standalone. O Case_01 tem: grafo rico (AdjustedGoals, DataSubjectCategories, ambiguidade, auditorias, alinhamentos NIST), validator com 8 famílias de checks + `--strict`, e um dashboard P1 com 8 Folios. O utilizador quer **estrutura idêntica** e **mais conteúdo no Case_02**.

## Descobertas do censo (fundamentação)
- **AdjustedGoals**: Doc13 §8 tem 70 cards parseáveis (`AG-D-XX.Y-001` privacy / `-002` security); §2/§3 em tabelas
- **DataSubjectCategory**: Doc04 §2.4 tem 6 categorias (Schengen travellers, EU employees, Job applicants, Contractors, Visitors, Whistleblowers)
- **Ambiguidade**: Doc09 declara **1071 cards**, top-20 documentadas, com severidade S1/S2/S3 e por sub-domínio (§2)
- **NIST alignments**: xlsx `REG_CHAIN` tem coluna "NIST CSF" por requisito — fonte machine-readable para NistControl CSF + ALIGNS_TO (hoje o grafo não tem nenhum)
- **Dashboard Case_01**: Folios IV/V/VI/VII são data-driven do JSON (port direto possível); hardcoded só no Folio I (strap, applicability, tier/cov bars, ambiguity, audits prose, invariants) + PIPELINE legend + arch pills
- **Erro a corrigir**: o meu builder usou tiers LIGHTWEIGHT/MINIMAL mas o Doc12 Case_02 (canónico) diz **8 RIGOROUS + 27 STANDARD**

## Fases (sequenciais, gate em cada uma; paro se falhar)

**Fase 0 — Pre-flight**
case-context-loader + cadeia PROJECT_STATE + `kg.sh impact` nos IDs novos (AG-D-*, DSC); confirmar superfícies de parse (Doc13 §2/§3/§8, Doc09 §1-§3, Doc04 §2.4, REG_CHAIN).
*Gate: mapa fonte→nó confirmado.*

**Fase 1 — Grafo v2.4: paridade de conteúdo** (`build_p1_graph.py`)
- **1a** 70 `AdjustedGoal` nodes (parse Doc13; track privacy `-001` / security `-002`) + 70 edges `YIELDS`
- **1b** 6 `DataSubjectCategory` nodes (Doc04 §2.4) + edges `CAPTURES` → PersonalDataCategory
- **1c** Ambiguidade: parse Doc09 (top-20 cards + stats por severidade/regulação + counts por sub-domínio §2) → `graph.ambiguity` + `invariants.ambiguity_cards_in_scope=1071`
- **1d** NIST: parse REG_CHAIN col "NIST CSF" → `NistControl` nodes CSF + edges `ALIGNS_TO` + `nist_alignment_count` por sub-domínio (para a coluna NIST do Folio IV)
- **1e** Correcção tiers: `proportionality_tier` alinhado com Doc12 (8 RIGOROUS + 27 STANDARD; 4 NOT_ADDRESSED sem tier)
- **1f** Auditorias reais: port dos geradores (tier drift vs Doc12, coverage gaps do sheet GAPS, checks NIST) → audits múltiplas
- **1g** `invariants` completos (goals_total=70, ambiguity, nist_controls, nist_alignments)
*Gate: builder corre; counts = case_invariants da ontologia; 0 dangling; validator PASS.*

**Fase 2 — Validator v2.4: paridade de checks** (`build_p1_dashboard.py`)
Port de Case_01: `check_invariants`, `check_audit_node_ids`, `check_phase_c` (maturity gates integradas), `check_phase_d` (NIST), `check_ontology_types`, `check_relation_verbs`, `check_id_patterns`, `check_provenance`, `check_stale_invariant_counts`, flag `--strict`, `--summary`.
*Gate: `--check` PASS **e** `--strict` PASS.*

**Fase 3 — Dashboard P1 completo** (`00_VISUALISATIONS/Case_02/Case_02_P1_Dashboard.html`)
- Base: `Case_01_P1_Dashboard.html` adaptado — **8 Folios**: I Executive (dados Case_02: 4 aplicáveis GDPR/CRA/NIS2/AIAct, DORA não; tier bar 8 RIG/27 STD; AG card 70=35+35; ambiguity 1071; audits), II Knowledge Graph, III Audit Panel, IV Sub-Domain Deep-Dive (com coluna NIST alignments preenchida), V Phase 1 Story (pipeline Case_02: 5 regs→4 aplicáveis→111 cláusulas→70 AGs), VI RACI (13 roles × 63 activities), VII Architecture (13 SYS/7 STORE/12 FLOW/22 vendors), VIII Maturity (port do `initMaturity` — o standalone `Case_02_P1_Maturity.html` mantém-se)
- De-hardcode do que for possível (números do Folio I lidos de `graph.invariants`); inline JSON via `build_case02_dashboard.py` estendido
*Gate: smoke 11/11 PASS; screenshots frescos dos 8 Folios; 0 pageerrors; verificação visual (radares, grid, RACI, arch com dados Case_02).*

**Fase 4 — Bookkeeping + regressão**
PROJECT_STATE v1.2 + CHANGE_LOG_CENTRAL v6.5 + GLOBAL_PROJECT_STATE; regressão final: builders+validators dos 2 casos, smoke 11 dashboards, grep órfãs, screenshots de não-regressão do Case_01 (Folios I–VIII intactos).
*Gate final: tudo verde → diff mostrado; commit só quando autorizares.*

## Case_03 (fora desta campanha — playbook seguinte)
Mesma sequência (grafo de raiz a partir da ontologia+xlsx Case_03, validator, dashboard, seed Evidence com DORA incluído, 150 cláusulas, 78 regras) numa campanha própria, reutilizando o builder Case_02 como template.

## Dívida / notas
- Story Folio V precisa de narrativa Case_02 (pipeline data-driven já existe; legend counts re-pointed)
- Tiers no meu seed actual estão errados vs Doc12 — corrigido na Fase 1e (Doc12 é canónico)
- progress.json nunca é editado directamente

## Permissões (Bash)
python3 (builders/validators/smoke), playwright screenshots, greps. Sem commits automáticos.