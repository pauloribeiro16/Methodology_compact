# Path-completo hover-highlight + tooltip informativo (UNIFIED Dashboard)

## Problema
- `emphasis.focus: 'adjacency'` actual **só ilumina 1 hop** (vizinhos directos). Quando o utilizador faz hover em `Art. 5(1)`, só Art + Clauses directos ficam highlighted — não o path completo até às subcategorias CSF.
- Tooltip default só mostra `name`. Sem info de regulatory/security rationale.
- Click handlers existem mas o utilizador reporta "as tuas alterações não fizeram nada" — provavelmente porque o highlight de 1-hop é fraco demais para perceber.

## Diagnóstico
- **3 Sankey** charts (linhas ~23881, 24033, 24135) já têm `emphasis` + `blur` + `select` injetados. **Insuficiente para path-completo**.
- **Click handlers OK** em todos os 3 (linhas 23890, 24045, 24150) → abrem `sankeyDetalhe` / `csfSankeyDetalhe` / `secondarySankeyDetalhe`.
- **Tooltips default** sem formatter custom — info limitada.
- **ECharts 5.4.3 edge highlight**: `chart.dispatchAction({type:'highlight', seriesIndex:0, dataType:'edge', dataIndex:i})`.

## Solução: JS custom BFS + custom tooltip

### 1. Helper único `setupPathHighlight(chart, links)` reutilizável

```js
function setupPathHighlight(chart, links) {
  // Build adjacency: nodeName → Set<linkIndex>
  const nameToLinkIdxs = new Map();
  links.forEach((l, i) => {
    if (!nameToLinkIdxs.has(l.source)) nameToLinkIdxs.set(l.source, new Set());
    if (!nameToLinkIdxs.has(l.target)) nameToLinkIdxs.set(l.target, new Set());
    nameToLinkIdxs.get(l.source).add(i);
    nameToLinkIdxs.get(l.target).add(i);
  });
  // Build neighbours: nodeName → Set<nodeName>
  const neighbours = new Map();
  links.forEach(l => {
    if (!neighbours.has(l.source)) neighbours.set(l.source, new Set());
    if (!neighbours.has(l.target)) neighbours.set(l.target, new Set());
    neighbours.get(l.source).add(l.target);
    neighbours.get(l.target).add(l.source);
  });
  function bfsPath(startName) {
    const visitedNodes = new Set([startName]);
    const visitedLinks = new Set();
    const queue = [startName];
    while (queue.length) {
      const n = queue.shift();
      const linksHere = nameToLinkIdxs.get(n) || new Set();
      const nsHere = neighbours.get(n) || new Set();
      for (const idx of linksHere) visitedLinks.add(idx);
      for (const adj of nsHere) {
        if (!visitedNodes.has(adj)) { visitedNodes.add(adj); queue.push(adj); }
      }
    }
    return { nodes: visitedNodes, links: visitedLinks };
  }
  chart.on('mouseover', { dataType: 'node' }, (p) => {
    const path = bfsPath(p.name);
    path.nodes.forEach(name => chart.dispatchAction({ type: 'highlight', seriesIndex: 0, name }));
    path.links.forEach(idx => chart.dispatchAction({ type: 'highlight', seriesIndex: 0, dataType: 'edge', dataIndex: idx }));
  });
  chart.on('mouseout', { dataType: 'node' }, () => {
    chart.dispatchAction({ type: 'downplay', seriesIndex: 0 });
  });
}
```

Chamar 3× após cada `setOption`:
```js
setupPathHighlight(chart, links);
```

### 2. Custom tooltip com info rico

Adicionar ao `setOption`:
```js
tooltip: {
  trigger: 'item',
  formatter: (params) => {
    if (params.dataType === 'edge') {
      return `<b>${params.data.source}</b> → <b>${params.data.target}</b>`;
    }
    // Node — show rationale excerpt (use lookup if available)
    const node = params.data;
    const subDomain = node.name && node.name.startsWith('D-') ? node.name : '';
    const rationale = window._getNodeTooltip ? window._getNodeTooltip(node) : null;
    if (rationale) {
      return `<div style="max-width:340px;font-family:var(--sans);font-size:12px;line-height:1.5">
        <div style="font-weight:700;color:#0d1b2a">${params.name}</div>
        ${rationale}
      </div>`;
    }
    return `<b>${params.name}</b>`;
  },
  backgroundColor: '#fbf9f5',
  borderColor: '#b8893a',
  borderWidth: 1,
  textStyle: { color: '#0d1b2a', fontFamily: 'Inter, sans-serif' }
}
```

**Implementação progressiva**: para já, o tooltip mostra o nome do nó + (se for Article/Clause/SR/Subcategory) um excerto da `regrational` (campo `regulatory_rationale`) da SRS object correspondente. Para artigos e clauses, mostrar `regulatory_rationale` (primeiros 200 chars); para SR, mostrar `title + rationale`; para NistSubcategory, mostrar `description` se disponível.

Adicionar helper de lookup:
```js
window._getNodeTooltip = function(node) {
  const n = node.name;
  // Art. 5(1) etc. → match in srs[].regulatory_rationale where sr.sr_id's source_clause references
  // SR-XXX → match srs[].title + srs[].regulatory_rationale
  // D-XX.Y → srs[].sub_domain
  // CSF subcats (PR.DS-01 etc.) → lookup from external metadata if available
  if (/^SR-/.test(n)) {
    const sr = window._srs.find(s => s.sr_id === n);
    if (sr) {
      const r = (sr.regulatory_rationale || '').slice(0, 240) + ((sr.regulatory_rationale || '').length > 240 ? '…' : '');
      return `<div style="color:#5a5345;font-size:11px;margin-top:4px"><b>Regulatory:</b> ${r}</div>`;
    }
  }
  if (/^Art\./.test(n)) {
    // Find SRs that cite this article
    const srs = window._srs.filter(s => s.source_article === n || (s.regulatory_rationale || '').includes(n));
    if (srs.length) {
      return `<div style="color:#5a5345;font-size:11px;margin-top:4px">${srs.length} security rule(s) derive from this article: ${srs.slice(0,3).map(s => '<code>' + escapeHtml(s.sr_id) + '</code>').join(', ')}</div>`;
    }
  }
  return null;
};
```

### 3. Garantir `window._srs` acessível

Procurar no código onde `srs` é definido (linhas ~400-500 provavelmente). Se já é global, OK. Se não, expor.

## Fases

**Fase 1 — Inject `setupPathHighlight` helper + 3 chamadas**
- Read linha ~23890 (Chart #1) — ver onde acaba `chart.on('click', ...)` para inserir `setupPathHighlight(chart, links);` após.
- Inserir helper function definition antes do primeiro Sankey init (linha ~23840).
- 3 Edit calls (um por chart) para invocar `setupPathHighlight(chart, links);`.

**Fase 2 — Custom tooltip com rationale lookup**
- Adicionar helper `window._getNodeTooltip` antes dos charts.
- Modificar 3 setOption blocks para usar tooltip com formatter (substituir `tooltip: { trigger: 'item' }` pelo formatter).
- Expor `srs` array como `window._srs` (se ainda não estiver).

**Fase 3 — Smoke + screenshots antes/depois**
- `python3 00_METHODOLOGY/00_VISUALISATIONS/tests/test_dashboards.py --only "AEGIS_Dashboard" --timeout 30`.
- Capturar 3 screenshots (um por Sankey) com hover via `chart.dispatchAction` programaticamente para mostrar path-completo iluminado.
- Verificar visualmente que:
  - Hover Art. 5(1) → ilumina TODO o caminho até CSF subcategories (5 níveis)
  - Tooltip mostra rationale excerpt
- Regressão 12/12.

## Riscos
- **Performance**: BFS num grafo com ~200 nodes × 300 links é trivial (<5ms). OK.
- **Re-entry bugs**: mouseover/mouseout devem ser rápidos; se ECharts firing events muito rápido pode haver flicker. Mitigação: usar `_isHighlighting` flag.
- **Tooltip empty content**: se rationale excerpt não existir, fallback para nome simples.
- **Click handlers existentes**: NÃO devem ser alterados.

## Sequência
1. Fase 1 (BFS highlight helper + 3 invokes) → gate
2. Fase 2 (tooltip com rationale) → gate
3. Fase 3 (smoke + 3 screenshots + regressão 12/12) → diff final

**Próximo passo** (fora do plan): começar Fase 1 — Read linha 23890 + injetar helper antes do primeiro Sankey + 3 invokes.