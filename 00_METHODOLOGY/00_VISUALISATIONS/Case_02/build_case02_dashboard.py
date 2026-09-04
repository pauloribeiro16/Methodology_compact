#!/usr/bin/env python3
"""Inline the current phase1_graph.json into Case_02_P1_Dashboard.html and
Case_02_P1_Maturity.html for file:// use.

Browsers block `fetch()` on file:// for security. We resolve this by writing
the graph JSON into a `<script type="application/json" id="phase1-graph-data">`
block in the HTML head — same pattern as Case_01_P1_Dashboard.html. The render
script (initMaturity) reads from `window.PHASE1_GRAPH_DATA` (inlined below the
JSON script) instead of doing a fetch.

Usage
-----
    python3 build_case02_dashboard.py
    default: ../../02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json
    into ../Case_02/Case_02_P1_Dashboard.html and Case_02_P1_Maturity.html.

Run this after `python3 build_p1_graph.py` (regenerate phase1_graph.json first).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HTML_PATH = HERE / "Case_02_P1_Dashboard.html"
MATURITY_HTML_PATH = HERE / "Case_02_P1_Maturity.html"
GRAPH_PATH = (HERE.parent.parent.parent /
              "02_CASES" / "Case_02_SecureBorder_Solutions" /
              "01_PHASE1_CONTEXT_RICH" / "data" / "phase1_graph.json")


def build_dashboard(graph: dict, graph_data: str) -> None:
    html = open(HTML_PATH, encoding="utf-8").read()

    # Replace fetch() with window.PHASE1_GRAPH_DATA shortcut if present
    html = html.replace(
        'async function load() {\n'
        '  try {\n'
        '    const r = await fetch(DATA_PATH_C02);',
        'async function load() {\n'
        '  try {\n'
        '    if (window.PHASE1_GRAPH_DATA) { initMaturity(window.PHASE1_GRAPH_DATA); return; }\n'
        '    const r = await fetch(DATA_PATH_C02);'
    )
    if 'initMaturity(DATA);' in html and 'window.PHASE1_GRAPH_DATA' not in html.split('initMaturity(DATA);')[0][-200:]:
        html = html.replace(
            'initMaturity(DATA);', 'initMaturity(window.PHASE1_GRAPH_DATA || DATA);', 1
        )

    # Inlining JSON scripts in head
    json_block = '<script type="application/json" id="phase1-graph-data">' + graph_data + '</script>'
    obj_literal = '<script>window.PHASE1_GRAPH_DATA = ' + graph_data + ';</script>'
    # Step 1: strip any pre-existing JSON block (idempotent reset)
    if 'id="phase1-graph-data"' in html:
        html = re.sub(
            r'<script type="application/json" id="phase1-graph-data">.*?</script>',
            '',
            html, count=1, flags=re.DOTALL)
    # Step 2: strip any pre-existing object literal (idempotent reset)
    if 'window.PHASE1_GRAPH_DATA = {' in html:
        html = re.sub(
            r'<script>window\.PHASE1_GRAPH_DATA = \{.*?\};</script>',
            '',
            html, count=1, flags=re.DOTALL)
    # Step 3: inject both fresh before </head>
    html = html.replace("</head>", json_block + "\n" + obj_literal + "\n</head>", 1)

    # Step 4: Patch renderAuditColumns and titles for Case_02
    new_html = html
    new_html = re.sub(
        r'(AUDITS\.forEach\(a => byKind\[a\.kind\] = \(byKind\[a\.kind\] \|\| \[\]\)\.concat\(a\)\);)',
        r'\1\n  const _have = new Set(AUDITS.map(a => a.kind));\n  const _order = ["structural","cross_doc_conflict","broken_link","coverage_gap","blocking_ambiguity"].filter(k => _have.has(k));',
        new_html,
        count=1,
    )
    new_html = re.sub(
        r'const order = \[[^\]]+\];',
        'const order = _order;',
        new_html,
        count=1,
    )
    # Patch audit titles mapping to include structural and clarify titles
    new_html = new_html.replace(
        '  const titles = {\n'
        '    cross_doc_conflict: "CFL · cross_doc_conflict",\n'
        '    broken_link: "BLN · broken_link",\n'
        '    coverage_gap: "CVG · coverage_gap",\n'
        '    blocking_ambiguity: "BAM · blocking_ambiguity"\n'
        '  };',
        '  const titles = {\n'
        '    structural: "STR · structural / seed",\n'
        '    cross_doc_conflict: "CFL · cross_doc_conflict",\n'
        '    broken_link: "BLN · broken_link",\n'
        '    coverage_gap: "CVG · coverage_gap",\n'
        '    blocking_ambiguity: "BAM · blocking_ambiguity"\n'
        '  };'
    )

    # Patch Folio III header findings count
    new_html = new_html.replace(
        '<span class="aside">29 findings &middot; click for full text</span>',
        f'<span class="aside">{len(graph.get("audits", []))} findings &middot; click for full text</span>'
    )

    # Patch Folio I audit-badges kindLabels
    new_html = new_html.replace(
        '  const kindLabels = {\n'
        '    cross_doc_conflict: "CFL · cross-doc conflict",\n'
        '    broken_link: "BLN · broken link",\n'
        '    coverage_gap: "CVG · coverage gap",\n'
        '    blocking_ambiguity: "BAM · blocking ambiguity"\n'
        '  };',
        '  const kindLabels = {\n'
        '    structural: "STR · structural",\n'
        '    cross_doc_conflict: "CFL · cross-doc conflict",\n'
        '    broken_link: "BLN · broken link",\n'
        '    coverage_gap: "CVG · coverage gap",\n'
        '    blocking_ambiguity: "BAM · blocking ambiguity"\n'
        '  };'
    )

    # Patch Folio II toolbar Tier dropdown
    old_f_tier = (
        '    <label>Tier\n'
        '      <select id="f-tier">\n'
        '        <option value="all">All</option>\n'
        '        <option value="LIGHTWEIGHT">LIGHTWEIGHT</option>\n'
        '        <option value="MINIMAL">MINIMAL</option>\n'
        '        <option value="DEFERRED">DEFERRED</option>\n'
        '      </select>\n'
        '    </label>'
    )
    new_f_tier = (
        '    <label>Tier\n'
        '      <select id="f-tier">\n'
        '        <option value="all">All</option>\n'
        '        <option value="RIGOROUS">RIGOROUS</option>\n'
        '        <option value="STANDARD">STANDARD</option>\n'
        '      </select>\n'
        '    </label>'
    )
    new_html = new_html.replace(old_f_tier, new_f_tier)

    # Patch ECharts force-directed layout parameters for 521 nodes
    new_html = new_html.replace(
        'force: { repulsion: 220, edgeLength: [60, 140], gravity: 0.05 }',
        'force: { repulsion: 350, edgeLength: [80, 180], gravity: 0.08, friction: 0.6 }'
    )

    # Patch typeLabel in renderSideForNode to cover CoverageGap and Stakeholder
    new_html = new_html.replace(
        '    NistControl: "NIST Control"\n'
        '  }[n.type] || n.type;',
        '    NistControl: "NIST Control",\n'
        '    CoverageGap: "Coverage Gap",\n'
        '    Stakeholder: "Stakeholder",\n'
        '    EvidenceItem: "Evidence Item"\n'
        '  }[n.type] || n.type;'
    )

    # Derived counts
    sd_active = sum(1 for n in graph.get("nodes", [])
                    if n["type"] == "SecurityControlDomain" and n.get("attrs", {}).get("active"))
    rigorous = sum(1 for n in graph.get("nodes", [])
                    if n["type"] == "SecurityControlDomain"
                    and n.get("attrs", {}).get("proportionality_tier") == "RIGOROUS")
    standard = sum(1 for n in graph.get("nodes", [])
                    if n["type"] == "SecurityControlDomain"
                    and n.get("attrs", {}).get("proportionality_tier") == "STANDARD")
    not_addressed_count = 4
    substantive = sd_active

    # Folio I tier/cov bars
    new_html = re.sub(
        r'<div class="seg" style="background:#5c7a3a; flex:31">31 LW</div>\s*'
        r'<div class="seg" style="background:#2c7cb0; flex:5">5 MIN</div>\s*'
        r'<div class="seg" style="background:#8a2a2a; flex:1">1 DEF</div>',
        f'<div class="seg" style="background:#5c7a3a; flex:{rigorous}">{rigorous} RIG</div>\n      '
        f'<div class="seg" style="background:#8a2a2a; flex:{standard}">{standard} STD</div>',
        new_html, count=1)
    new_html = re.sub(
        r'<div class="seg" style="background:#5c7a3a; flex:16">16 SUB</div>\s*'
        r'<div class="seg" style="background:#b8893a; flex:19">19 PART</div>\s*'
        r'<div class="seg" style="background:#8a2a2a; flex:3">3 N/A</div>',
        f'<div class="seg" style="background:#5c7a3a; flex:{substantive}">{substantive} SUB</div>\n      '
        f'<div class="seg" style="background:#b8893a; flex:0.0001">0 PART</div>\n      '
        f'<div class="seg" style="background:#8a2a2a; flex:{not_addressed_count}">{not_addressed_count} N/A</div>',
        new_html, count=1)

    # Header strap line
    n_nodes = len(graph.get("nodes", []))
    n_links = len(graph.get("links", []))
    n_audits = len(graph.get("audits", []))
    n_amb = (graph.get("ambiguity") or {}).get("stats_total", {}).get("cards_in_scope", 0)
    new_html = re.sub(
        r'A knowledge-graph atlas of the regulatory landscape:\s*\d+\s*nodes,\s*\d+\s*links,\s*\d+\s*audits,\s*\d+\s*ambiguity cards',
        f'A knowledge-graph atlas for SecureBorder B.V.: {n_nodes} nodes, {n_links} links, {n_audits} audits, {n_amb} ambiguity cards',
        new_html, count=1)

    # Seal and title
    new_html = new_html.replace('<div class="seal">01</div>', '<div class="seal">02</div>')
    new_html = new_html.replace("Case 01 &middot; Phase 1", "Case 02 &middot; Phase 1")
    new_html = new_html.replace("Case 01 · Phase 1", "Case 02 · Phase 1")
    new_html = new_html.replace(
        '<div class="sub">TinyTask Lda. &middot; Lisbon, PT &middot; AEGIS Rich Mode</div>',
        '<div class="sub">SecureBorder B.V. &middot; The Hague, NL &middot; AEGIS Rich Mode</div>'
    )
    new_html = new_html.replace("TINYTASK LDA.", "SECUREBORDER B.V.")
    new_html = new_html.replace("LISBON, PT", "THE HAGUE, NL")

    # Item 1 Checklist replacements:
    # 1. Company card
    old_company_card = (
        '    <div class="card">\n'
        '      <div class="label">Company</div>\n'
        '      <div class="value smaller">TinyTask Lda.</div>\n'
        '      <div class="sub">MICRO scale &middot; 8 FTE &middot; 0.85 sec FTE</div>\n'
        '      <dl class="kv-grid" style="margin-top:10px">\n'
        '        <dt>HQ</dt><dd>Lisbon, PT (EU)</dd>\n'
        '        <dt>Sector</dt><dd>Technology / B2B SaaS</dd>\n'
        '        <dt>Product</dt><dd>Team Organizer</dd>\n'
        '        <dt>Stack</dt><dd>AWS eu-west-1 &middot; Firebase Auth &middot; Stripe &middot; GitHub Actions</dd>\n'
        '      </dl>\n'
        '    </div>'
    )
    new_company_card = (
        '    <div class="card">\n'
        '      <div class="label">Company</div>\n'
        '      <div class="value smaller">SecureBorder Solutions B.V.</div>\n'
        '      <div class="sub">MEDIUM scale &middot; 450 employees &middot; 5–8 sec FTE</div>\n'
        '      <dl class="kv-grid" style="margin-top:10px">\n'
        '        <dt>HQ</dt><dd>The Hague, NL (EU)</dd>\n'
        '        <dt>Sector</dt><dd>Defense / Security / Critical Infrastructure</dd>\n'
        '        <dt>Product</dt><dd>GuardianGate eGate kiosks</dd>\n'
        '        <dt>Stack</dt><dd>Edge AI (on-device) &middot; EU cloud &middot; Signed OTA &middot; PKI / HSM</dd>\n'
        '      </dl>\n'
        '    </div>'
    )
    new_html = new_html.replace(old_company_card, new_company_card)

    # 2. Applicability Verdict
    old_app_card = (
        '    <div class="card gold">\n'
        '      <div class="label">Applicability Verdict</div>\n'
        '      <div class="value">2 / 5</div>\n'
        '      <div class="sub">regulations applicable</div>\n'
        '      <ul class="applicability-list">\n'
        '        <li><span class="yes">YES</span><span><b>GDPR</b> &mdash; controller + processor; personal data</span></li>\n'
        '        <li><span class="yes">YES</span><span><b>CRA</b> &mdash; manufacturer (Default class)</span></li>\n'
        '        <li><span class="no">NO</span><span><b>NIS2</b> &mdash; &lt;50 FTE (Doc08 &sect;4)</span></li>\n'
        '        <li><span class="no">NO</span><span><b>DORA</b> &mdash; not financial entity</span></li>\n'
        '        <li><span class="no">NO</span><span><b>AI Act</b> &mdash; no AI system in product</span></li>\n'
        '      </ul>\n'
        '    </div>'
    )
    new_app_card = (
        '    <div class="card gold">\n'
        '      <div class="label">Applicability Verdict</div>\n'
        '      <div class="value">4 / 5</div>\n'
        '      <div class="sub">regulations applicable</div>\n'
        '      <ul class="applicability-list">\n'
        '        <li><span class="yes">YES</span><span><b>GDPR</b> &mdash; controller + processor; biometric Art. 9</span></li>\n'
        '        <li><span class="yes">YES</span><span><b>CRA</b> &mdash; manufacturer (Critical Class)</span></li>\n'
        '        <li><span class="yes">YES</span><span><b>NIS2</b> &mdash; essential entity supplier (450 FTE)</span></li>\n'
        '        <li><span class="yes">YES</span><span><b>AI Act</b> &mdash; high-risk AI provider (Annex III)</span></li>\n'
        '        <li><span class="no">NO</span><span><b>DORA</b> &mdash; not financial entity</span></li>\n'
        '      </ul>\n'
        '    </div>'
    )
    new_html = new_html.replace(old_app_card, new_app_card)

    # 3. Coverage Tier card (number + legend)
    old_tier_card = (
        '    <div class="card dark">\n'
        '      <div class="label">Coverage Tier (Doc12 &sect;4)</div>\n'
        '      <div class="value">37</div>\n'
        '      <div class="sub">sub-domains with a tier assigned</div>\n'
        '      <div class="tier-bar" id="tier-bar"></div>\n'
        '      <div class="legend">\n'
        '        <span><span class="sw" style="background:#5c7a3a"></span>LIGHTWEIGHT 31</span>\n'
        '        <span><span class="sw" style="background:#2c7cb0"></span>MINIMAL 5</span>\n'
        '        <span><span class="sw" style="background:#8a2a2a"></span>DEFERRED 1</span>\n'
        '      </div>\n'
        '    </div>'
    )
    new_tier_card = (
        '    <div class="card dark">\n'
        '      <div class="label">Coverage Tier (Doc12 &sect;4)</div>\n'
        '      <div class="value">34</div>\n'
        '      <div class="sub">active sub-domains with a tier assigned</div>\n'
        '      <div class="tier-bar" id="tier-bar"></div>\n'
        '      <div class="legend">\n'
        '        <span><span class="sw" style="background:#5c7a3a"></span>RIGOROUS 8</span>\n'
        '        <span><span class="sw" style="background:#8a2a2a"></span>STANDARD 26</span>\n'
        '      </div>\n'
        '    </div>'
    )
    new_html = new_html.replace(old_tier_card, new_tier_card)

    # 4. Coverage Level card
    old_cov_card = (
        '    <div class="card warn">\n'
        '      <div class="label">Coverage Level (Doc11 &sect;3)</div>\n'
        '      <div class="value">38</div>\n'
        '      <div class="sub">sub-domains scored</div>\n'
        '      <div class="cov-bar" id="cov-bar"></div>\n'
        '      <div class="legend">\n'
        '        <span><span class="sw" style="background:#5c7a3a"></span>SUBSTANTIVE 16</span>\n'
        '        <span><span class="sw" style="background:#b8893a"></span>PARTIAL 19</span>\n'
        '        <span><span class="sw" style="background:#8a2a2a"></span>NOT_ADDRESSED 3</span>\n'
        '      </div>\n'
        '    </div>'
    )
    new_cov_card = (
        '    <div class="card warn">\n'
        '      <div class="label">Coverage Level (Doc11 &sect;3)</div>\n'
        '      <div class="value">38</div>\n'
        '      <div class="sub">sub-domains scored</div>\n'
        '      <div class="cov-bar" id="cov-bar"></div>\n'
        '      <div class="legend">\n'
        '        <span><span class="sw" style="background:#5c7a3a"></span>SUBSTANTIVE 34</span>\n'
        '        <span><span class="sw" style="background:#8a2a2a"></span>NOT_ADDRESSED 4</span>\n'
        '      </div>\n'
        '    </div>'
    )
    new_html = new_html.replace(old_cov_card, new_cov_card)

    # 5. Adjusted Goals card
    old_ag_card = (
        '    <div class="card good">\n'
        '      <div class="label">Adjusted Goals</div>\n'
        '      <div class="value">69</div>\n'
        '      <div class="sub">AGs across 3 tracks</div>\n'
        '      <dl class="kv-grid" style="margin-top:10px">\n'
        '        <dt>HL</dt><dd>7 (high-level &mdash; Doc13 &sect;2)</dd>\n'
        '        <dt>GDPR-driven</dt><dd>28 (Doc13 &sect;3)</dd>\n'
        '        <dt>CRA-driven</dt><dd>34 (Doc13 &sect;4)</dd>\n'
        '        <dt>Priority</dt><dd>69 MUST &middot; 0 SHOULD/COULD</dd>\n'
        '      </dl>\n'
        '    </div>'
    )
    new_ag_card = (
        '    <div class="card good">\n'
        '      <div class="label">Adjusted Goals</div>\n'
        '      <div class="value">70</div>\n'
        '      <div class="sub">AGs across 2 tracks (Doc13 &sect;8)</div>\n'
        '      <dl class="kv-grid" style="margin-top:10px">\n'
        '        <dt>Privacy</dt><dd>35 (AG-D-XX.Y-001)</dd>\n'
        '        <dt>Security</dt><dd>35 (AG-D-XX.Y-002)</dd>\n'
        '        <dt>Tensions</dt><dd>3 resolved (T-001..T-003)</dd>\n'
        '        <dt>Priority</dt><dd>70 MUST &middot; 0 SHOULD/COULD</dd>\n'
        '      </dl>\n'
        '    </div>'
    )
    new_html = new_html.replace(old_ag_card, new_ag_card)

    # 6. Ambiguity Register card
    old_amb_card = (
        '    <div class="card">\n'
        '      <div class="label">Ambiguity Register (Doc09)</div>\n'
        '      <div class="value">417</div>\n'
        '      <div class="sub">cards in scope &middot; Doc09 &sect;1</div>\n'
        '      <div class="severity-hist" id="sev-hist"></div>\n'
        '      <div class="legend" style="margin-top:6px">\n'
        '        <span><span class="sw" style="background:#c9bfa7"></span>S1 0</span>\n'
        '        <span><span class="sw" style="background:#2c7cb0"></span>S2 251</span>\n'
        '        <span><span class="sw" style="background:#b8893a"></span>S3 252</span>\n'
        '      </div>\n'
        '      <div class="sub" style="margin-top:6px"><span class="mono">GDPR 276 &middot; CRA 141</span></div>\n'
        '    </div>'
    )
    new_amb_card = (
        '    <div class="card">\n'
        '      <div class="label">Ambiguity Register (Doc09)</div>\n'
        '      <div class="value">1071</div>\n'
        '      <div class="sub">cards in scope &middot; Doc09 &sect;1</div>\n'
        '      <div class="severity-hist" id="sev-hist"></div>\n'
        '      <div class="legend" style="margin-top:6px">\n'
        '        <span><span class="sw" style="background:#c9bfa7"></span>S1 —</span>\n'
        '        <span><span class="sw" style="background:#2c7cb0"></span>S2 —</span>\n'
        '        <span><span class="sw" style="background:#b8893a"></span>S3 (Top-20)</span>\n'
        '      </div>\n'
        '      <div class="sub" style="margin-top:6px"><span class="mono">GDPR &middot; CRA &middot; NIS 2 &middot; AI Act (Doc09 &sect;2)</span></div>\n'
        '    </div>'
    )
    new_html = new_html.replace(old_amb_card, new_amb_card)

    # 7. Caveats / Audits prose card
    old_caveats_prose = (
        '        Of the 29 audits raised by <span class="mono">build_p1_dashboard.py --check</span>, the first 26 cover document-level drift\n'
        '        (CFL-001 Doc10 &sect;3 legacy table, CFL-002 sub-domain count cascade, BLN-002 Doc12/Doc13 tier conflict) and\n'
        '        domain-level findings. The remaining three (NEW-06/07/08) are Phase C additions that surface the\n'
        '        Doc08 &sect;9 &harr; phase1_graph asymmetry on Art. 35/37, non-canonical evidence_type strings, and the uniform 2&rarr;3\n'
        '        maturity distribution across 36 of 37 active sub-domains. See <b>Audit Panel</b> for full text and recommendations.'
    )
    new_caveats_prose = (
        '        Of the 8 audits raised by <span class="mono">build_p1_dashboard.py --check</span>, the structural findings cover\n'
        '        NEW-C02-01 (Maturity redesign v2.3 with 59 EvidenceItems), NEW-C02-02 (70 AdjustedGoals seeded from Doc13 §8),\n'
        '        NEW-C02-03 (1071 ambiguity cards in scope per Doc09 §1), NEW-C02-04 (CSF alignment from REG_CHAIN),\n'
        '        and NEW-C02-05 (Tier distribution per Doc12 §3). Consistency checks CFL-C02-001 (tier verification),\n'
        '        BLN-C02-001 (10 macro-domains baseline), and CVG-C02-001 (coverage gaps ledger) confirm complete case integrity.\n'
        '        See <b>Audit Panel</b> for full text and recommendations.'
    )
    new_html = new_html.replace(old_caveats_prose, new_caveats_prose)

    # 8. Folio V Pipeline legend counts
    old_pipeline_legend = (
        '        <li><span class="sw sh-stk"></span>Stakeholders <span class="mono">7</span></li>\n'
        '        <li><span class="sw sh-bg"></span>Business Goals <span class="mono">5</span></li>\n'
        '        <li><span class="sw sh-cc"></span>Company <span class="mono">1</span></li>\n'
        '        <li><span class="sw sh-reg"></span>Regulations <span class="mono">5</span></li>\n'
        '        <li><span class="sw sh-rc"></span>Clauses <span class="mono">54</span></li>\n'
        '        <li><span class="sw sh-scd"></span>Sub-Domains <span class="mono">38</span></li>\n'
        '        <li><span class="sw sh-ag"></span>Adjusted Goals <span class="mono">69</span></li>'
    )
    new_pipeline_legend = (
        '        <li><span class="sw sh-stk"></span>Stakeholders <span class="mono">10</span></li>\n'
        '        <li><span class="sw sh-bg"></span>Business Goals <span class="mono">7</span></li>\n'
        '        <li><span class="sw sh-cc"></span>Company <span class="mono">1</span></li>\n'
        '        <li><span class="sw sh-reg"></span>Regulations <span class="mono">5</span></li>\n'
        '        <li><span class="sw sh-rc"></span>Clauses <span class="mono">111</span></li>\n'
        '        <li><span class="sw sh-scd"></span>Sub-Domains <span class="mono">38</span></li>\n'
        '        <li><span class="sw sh-ag"></span>Adjusted Goals <span class="mono">70</span></li>'
    )
    new_html = new_html.replace(old_pipeline_legend, new_pipeline_legend)

    # 9. Footer line
    old_footer = (
        '<footer class="foot">\n'
        '  <div>Data: <span class="mono">phase1_graph.json</span> (2026-08-26) &middot; 272 nodes &middot; 785 links &middot; Audits: 29 &middot; See <span class="mono">validation/P1_graph_json_validation.md</span>.</div>\n'
        '  <div class="right">\n'
        '    AEGIS Rich Mode &middot; Case_01 &middot; standalone file://\n'
        '  </div>\n'
        '</footer>'
    )
    new_footer = (
        '<footer class="foot">\n'
        f'  <div>Data: <span class="mono">phase1_graph.json</span> (2026-08-28) &middot; {n_nodes} nodes &middot; {n_links} links &middot; Audits: {n_audits} &middot; See <span class="mono">validation/P1_graph_json_validation.md</span>.</div>\n'
        '  <div class="right">\n'
        '    AEGIS Rich Mode &middot; Case_02 &middot; standalone file://\n'
        '  </div>\n'
        '</footer>'
    )
    new_html = new_html.replace(old_footer, new_footer)

    # 10. JS return "TinyTask" -> "SecureBorder"
    new_html = new_html.replace('if (n.type === "CompanyContext") return "TinyTask";', 'if (n.type === "CompanyContext") return "SecureBorder";')

    # 11. AI-RMF framework pill / outcome in initMaturity
    new_html = new_html.replace(
        'const framework = csfFunction(a.outcome) ? "CSF" : (pfFunction(a.outcome) ? "PF" : "—");',
        'const framework = csfFunction(a.outcome) ? "CSF" : (pfFunction(a.outcome) ? "PF" : (/^(GOVERN-|MAP-|MEASURE-|MANAGE-)/.test(a.outcome) ? "AI-RMF" : "—"));'
    )

    # 12. Folio VI RACI Matrix: 63 activities, 12 roles
    old_raci_header = '<span class="aside">43 activities &middot; 6 roles &middot; colour-coded</span>'
    new_raci_header = '<span class="aside">63 activities &middot; 12 roles &middot; colour-coded</span>'
    new_html = new_html.replace(old_raci_header, new_raci_header)

    old_raci_active_label = '<label class="cb"><input type="checkbox" id="r-active-only"> Active only (41)</label>'
    new_raci_active_label = '<label class="cb"><input type="checkbox" id="r-active-only"> Active only (63)</label>'
    new_html = new_html.replace(old_raci_active_label, new_raci_active_label)

    # Replace thead in tbl-raci
    old_raci_thead = (
        '        <thead>\n'
        '          <tr>\n'
        '            <th data-col="act"     data-order="asc">ACT</th>\n'
        '            <th data-col="name"    data-order="asc">Activity</th>\n'
        '            <th data-col="active"  data-order="asc">Active</th>\n'
        '            <th data-col="domain"  data-order="asc">Domain</th>\n'
        '            <th data-col="sub"     data-order="asc">Sub-domain</th>\n'
        '            <th data-col="dpo"     data-order="asc">DPO</th>\n'
        '            <th data-col="ciso"    data-order="asc">CISO</th>\n'
        '            <th data-col="dev"     data-order="asc">Dev</th>\n'
        '            <th data-col="legal"   data-order="asc">Legal</th>\n'
        '            <th data-col="hr"      data-order="asc">HR</th>\n'
        '            <th data-col="board"   data-order="asc">Board</th>\n'
        '          </tr>\n'
        '        </thead>'
    )
    new_raci_thead = (
        '        <thead>\n'
        '          <tr>\n'
        '            <th data-col="act"     data-order="asc">ACT</th>\n'
        '            <th data-col="name"    data-order="asc">Activity</th>\n'
        '            <th data-col="active"  data-order="asc">Active</th>\n'
        '            <th data-col="domain"  data-order="asc">Domain</th>\n'
        '            <th data-col="sub"     data-order="asc">Sub-domain</th>\n'
        '            <th data-col="ceo"     data-order="asc">CEO</th>\n'
        '            <th data-col="cto"     data-order="asc">CTO</th>\n'
        '            <th data-col="ciso"    data-order="asc">CISO</th>\n'
        '            <th data-col="dpo"     data-order="asc">DPO</th>\n'
        '            <th data-col="aigov"   data-order="asc">AI-Gov</th>\n'
        '            <th data-col="comp"    data-order="asc">Comp</th>\n'
        '            <th data-col="ia"      data-order="asc">IA</th>\n'
        '            <th data-col="soc"     data-order="asc">SOC</th>\n'
        '            <th data-col="legal"   data-order="asc">Legal</th>\n'
        '            <th data-col="hr"      data-order="asc">HR</th>\n'
        '            <th data-col="proc"    data-order="asc">Proc</th>\n'
        '            <th data-col="board"   data-order="asc">Board</th>\n'
        '          </tr>\n'
        '        </thead>'
    )
    new_html = new_html.replace(old_raci_thead, new_raci_thead)

    # Patch RACI JS constants & functions for 12 roles
    old_raci_js = (
        'const ROLES = ["ROLE-DPO","ROLE-CISO","ROLE-DEV","ROLE-LEGAL","ROLE-HR","ROLE-BOARD"];\n'
        'const ROLE_HEADERS = [\n'
        '  { id: "ROLE-DPO",   label: "DPO" },\n'
        '  { id: "ROLE-CISO",  label: "CISO" },\n'
        '  { id: "ROLE-DEV",   label: "Dev" },\n'
        '  { id: "ROLE-LEGAL", label: "Legal" },\n'
        '  { id: "ROLE-HR",    label: "HR" },\n'
        '  { id: "ROLE-BOARD", label: "Board" }\n'
        '];\n'
        '// data-col → cell column index in the rendered row tuple\n'
        'const COL_INDEX = { act: 0, name: 1, active: 2, domain: 3, sub: 4,\n'
        '                    dpo: 5, ciso: 6, dev: 7, legal: 8, hr: 9, board: 10 };'
    )
    new_raci_js = (
        'const ROLES = ["ROLE-CEO","ROLE-CTO","ROLE-CISO","ROLE-DPO","ROLE-AI-Gov","ROLE-Comp","ROLE-IA","ROLE-SOC","ROLE-Legal","ROLE-HR","ROLE-Proc","ROLE-Board"];\n'
        'const ROLE_HEADERS = [\n'
        '  { id: "ROLE-CEO",    col: "ceo",   label: "CEO" },\n'
        '  { id: "ROLE-CTO",    col: "cto",   label: "CTO" },\n'
        '  { id: "ROLE-CISO",   col: "ciso",  label: "CISO" },\n'
        '  { id: "ROLE-DPO",    col: "dpo",   label: "DPO" },\n'
        '  { id: "ROLE-AI-Gov", col: "aigov", label: "AI-Gov" },\n'
        '  { id: "ROLE-Comp",   col: "comp",  label: "Comp" },\n'
        '  { id: "ROLE-IA",     col: "ia",    label: "IA" },\n'
        '  { id: "ROLE-SOC",    col: "soc",   label: "SOC" },\n'
        '  { id: "ROLE-Legal",  col: "legal", label: "Legal" },\n'
        '  { id: "ROLE-HR",     col: "hr",    label: "HR" },\n'
        '  { id: "ROLE-Proc",   col: "proc",  label: "Proc" },\n'
        '  { id: "ROLE-Board",  col: "board", label: "Board" }\n'
        '];\n'
        'const COL_INDEX = { act: 0, name: 1, active: 2, domain: 3, sub: 4,\n'
        '                    ceo: 5, cto: 6, ciso: 7, dpo: 8, aigov: 9, comp: 10,\n'
        '                    ia: 11, soc: 12, legal: 13, hr: 14, proc: 15, board: 16 };'
    )
    new_html = new_html.replace(old_raci_js, new_raci_js)

    # Patch rowToTuple to render all 12 cells
    old_row_to_tuple = (
        'function rowToTuple(r) {\n'
        '  return [\n'
        '    `<span class="mono">${escapeHtml(r.actId)}</span>`,\n'
        '    `<span class="raci-name">${escapeHtml(r.name)}</span>`,\n'
        '    r.active ? `<span class="raci-active-on" title="active">●</span>` : `<span class="raci-active-off" title="inactive">○</span>`,\n'
        '    `<span class="mono">${escapeHtml(r.domain)}</span>`,\n'
        '    `<span class="raci-sub"><a href="#" data-focus-sub="${escapeHtml(r.sub)}" title="${escapeHtml(r.corpus)}">${escapeHtml(r.sub)}</a></span>`,\n'
        '    cellHtml(r.cells["ROLE-DPO"]),\n'
        '    cellHtml(r.cells["ROLE-CISO"]),\n'
        '    cellHtml(r.cells["ROLE-DEV"]),\n'
        '    cellHtml(r.cells["ROLE-LEGAL"]),\n'
        '    cellHtml(r.cells["ROLE-HR"]),\n'
        '    cellHtml(r.cells["ROLE-BOARD"])\n'
        '  ];\n'
        '}'
    )
    new_row_to_tuple = (
        'function rowToTuple(r) {\n'
        '  return [\n'
        '    `<span class="mono">${escapeHtml(r.actId)}</span>`,\n'
        '    `<span class="raci-name">${escapeHtml(r.name)}</span>`,\n'
        '    r.active ? `<span class="raci-active-on" title="active">●</span>` : `<span class="raci-active-off" title="inactive">○</span>`,\n'
        '    `<span class="mono">${escapeHtml(r.domain)}</span>`,\n'
        '    `<span class="raci-sub"><a href="#" data-focus-sub="${escapeHtml(r.sub)}" title="${escapeHtml(r.corpus)}">${escapeHtml(r.sub)}</a></span>`,\n'
        '    ...ROLE_HEADERS.map(rh => cellHtml(r.cells[rh.id]))\n'
        '  ];\n'
        '}'
    )
    new_html = new_html.replace(old_row_to_tuple, new_row_to_tuple)

    # Patch raciCompare to sort on all 12 columns
    old_raci_compare = (
        '  if (col === "act")    { av = a.actId; bv = b.actId; }\n'
        '  else if (col === "name")   { av = a.name.toLowerCase(); bv = b.name.toLowerCase(); }\n'
        '  else if (col === "active") { av = a.active ? 1 : 0; bv = b.active ? 1 : 0; }\n'
        '  else if (col === "domain") { av = a.domain; bv = b.domain; }\n'
        '  else if (col === "sub")    { av = a.sub; bv = b.sub; }\n'
        '  else if (col === "dpo")    { av = a.cells["ROLE-DPO"] || ""; bv = b.cells["ROLE-DPO"] || ""; }\n'
        '  else if (col === "ciso")   { av = a.cells["ROLE-CISO"] || ""; bv = b.cells["ROLE-CISO"] || ""; }\n'
        '  else if (col === "dev")    { av = a.cells["ROLE-DEV"] || ""; bv = b.cells["ROLE-DEV"] || ""; }\n'
        '  else if (col === "legal")  { av = a.cells["ROLE-LEGAL"] || ""; bv = b.cells["ROLE-LEGAL"] || ""; }\n'
        '  else if (col === "hr")     { av = a.cells["ROLE-HR"] || ""; bv = b.cells["ROLE-HR"] || ""; }\n'
        '  else if (col === "board")  { av = a.cells["ROLE-BOARD"] || ""; bv = b.cells["ROLE-BOARD"] || ""; }'
    )
    new_raci_compare = (
        '  if (col === "act")    { av = a.actId; bv = b.actId; }\n'
        '  else if (col === "name")   { av = a.name.toLowerCase(); bv = b.name.toLowerCase(); }\n'
        '  else if (col === "active") { av = a.active ? 1 : 0; bv = b.active ? 1 : 0; }\n'
        '  else if (col === "domain") { av = a.domain; bv = b.domain; }\n'
        '  else if (col === "sub")    { av = a.sub; bv = b.sub; }\n'
        '  else {\n'
        '    const rh = ROLE_HEADERS.find(h => h.col === col);\n'
        '    if (rh) { av = a.cells[rh.id] || ""; bv = b.cells[rh.id] || ""; }\n'
        '  }'
    )
    new_html = new_html.replace(old_raci_compare, new_raci_compare)

    # Patch raci-foot findings title
    new_html = new_html.replace('<h3><span class="pip">CVG &middot; GAP-RACI</span>5 RACI findings', '<h3><span class="pip">CVG &middot; GAP-RACI</span>RACI Findings &amp; Gaps')

    # 13. Folio IV Sub-Domain Deep-Dive: 2 Goal Tracks (Privacy -001 and Security -002)
    old_grid_thead = (
        '        <th data-col-key="hl">HL Goal</th>\n'
        '        <th data-col-key="gdpr">GDPR Goal</th>\n'
        '        <th data-col-key="cra">CRA Goal</th>'
    )
    new_grid_thead = (
        '        <th data-col-key="priv">Privacy Goal</th>\n'
        '        <th data-col-key="sec">Security Goal</th>'
    )
    new_html = new_html.replace(old_grid_thead, new_grid_thead)

    # Patch Folio IV DATA construction to extract privacy and security goals
    old_grid_data_js = (
        '    const slot001 = goals.filter(g => g.attrs && g.attrs.slot === "001").map(g => g.id);\n'
        '    const slot002 = goals.filter(g => g.attrs && g.attrs.slot === "002").map(g => g.id);\n'
        '\n'
        '    out[n.id] = {\n'
        '      label: n.label,\n'
        '      coverage_level: (n.attrs && n.attrs.coverage_level) || "NOT_ADDRESSED",\n'
        '      proportionality_tier: (n.attrs && n.attrs.proportionality_tier) || null,\n'
        '      active: !!((n.attrs && n.attrs.active) === true),\n'
        '      clause_count: clauseLinks.length,\n'
        '      ni_avg,\n'
        '      source_regulations: source_regs.map(r => (r === "REG-GDPR" ? "GDPR" : r === "REG-CRA" ? "CRA" : r)),\n'
        '      amb_in_scope: amb.in_scope || 0,\n'
        '      amb_total: amb.total || 0,\n'
        '      hl:   slot001[0] || null,    // Doc13 §2 HL goal — share id with the GDPR-driven entry\n'
        '      gdpr: slot001[0] || null,   // Doc13 §3 GDPR-driven goal (same AG-D-XX.X-001 node, track=GDPR)\n'
        '      cra:  slot002[0] || null    // Doc13 §4 CRA-driven goal (AG-D-XX.X-002, track=CRA)\n'
        '    };'
    )
    new_grid_data_js = (
        '    const slot001 = goals.filter(g => (g.attrs && g.attrs.slot === "001") || g.id.endsWith("-001")).map(g => g.id);\n'
        '    const slot002 = goals.filter(g => (g.attrs && g.attrs.slot === "002") || g.id.endsWith("-002")).map(g => g.id);\n'
        '\n'
        '    out[n.id] = {\n'
        '      label: n.label,\n'
        '      coverage_level: (n.attrs && n.attrs.coverage_level) || "NOT_ADDRESSED",\n'
        '      proportionality_tier: (n.attrs && n.attrs.proportionality_tier) || null,\n'
        '      active: !!((n.attrs && n.attrs.active) === true),\n'
        '      clause_count: clauseLinks.length,\n'
        '      ni_avg,\n'
        '      source_regulations: source_regs.map(r => r.replace(/^REG-/, "")),\n'
        '      amb_in_scope: amb.in_scope || 0,\n'
        '      amb_total: amb.total || 0,\n'
        '      priv: slot001[0] || null,   // Doc13 §8 Privacy track AG-D-XX.Y-001\n'
        '      sec:  slot002[0] || null    // Doc13 §8 Security track AG-D-XX.Y-002\n'
        '    };'
    )
    new_html = new_html.replace(old_grid_data_js, new_grid_data_js)

    # Patch Folio IV rows construction in initGrid()
    old_init_grid_rows = (
        '      g.hl ? `<span class="goal-id hl" data-focus="${g.hl}">${g.hl}</span>` : `<span style="color:var(--faint)">—</span>`,\n'
        '      g.gdpr ? `<span class="goal-id gdpr" data-focus="${g.gdpr}">${g.gdpr}</span>` : `<span style="color:var(--faint)">—</span>`,\n'
        '      g.cra ? `<span class="goal-id cra" data-focus="${g.cra}">${g.cra}</span>` : `<span style="color:var(--faint)">—</span>`,'
    )
    new_init_grid_rows = (
        '      g.priv ? `<span class="goal-id gdpr" data-focus="${g.priv}">${g.priv}</span>` : `<span style="color:var(--faint)">—</span>`,\n'
        '      g.sec ? `<span class="goal-id cra" data-focus="${g.sec}">${g.sec}</span>` : `<span style="color:var(--faint)">—</span>`,'
    )
    new_html = new_html.replace(old_init_grid_rows, new_init_grid_rows)

    old_init_grid_tds = (
        '      <td data-col-key="hl">${r[6]}</td>\n'
        '      <td data-col-key="gdpr">${r[7]}</td>\n'
        '      <td data-col-key="cra">${r[8]}</td>\n'
        '      <td data-col-key="active">${r[9]}</td>\n'
        '      <td data-col-key="ambig">${r[10]}</td>\n'
        '      ${r.slice(11).map(c => `<td data-col-key="${c.k}" class="cell-${c.k}">${c.v}</td>`).join("")}'
    )
    new_init_grid_tds = (
        '      <td data-col-key="priv">${r[6]}</td>\n'
        '      <td data-col-key="sec">${r[7]}</td>\n'
        '      <td data-col-key="active">${r[8]}</td>\n'
        '      <td data-col-key="ambig">${r[9]}</td>\n'
        '      ${r.slice(10).map(c => `<td data-col-key="${c.k}" class="cell-${c.k}">${c.v}</td>`).join("")}'
    )
    new_html = new_html.replace(old_init_grid_tds, new_init_grid_tds)

    # Adjust DataTables order column index in Folio IV
    new_html = new_html.replace('order: [[18, "asc"]],\n      columnDefs: [{ orderable: false, targets: [19] }]', 'order: [[17, "asc"]],\n      columnDefs: [{ orderable: false, targets: [18] }]')

    # 14. Folio VII Architecture & Third Parties: update counts and attributes
    n_sys = sum(1 for n in graph.get("nodes", []) if n["type"] == "System")
    n_stores = sum(1 for n in graph.get("nodes", []) if n["type"] == "DataStore")
    n_flows = sum(1 for n in graph.get("nodes", []) if n["type"] == "DataFlow")
    n_vendors = sum(1 for n in graph.get("nodes", []) if n["type"] == "ThirdParty")

    old_arch_pills = (
        '      <span class="arch-pill"><b>5</b> systems</span>\n'
        '      <span class="arch-pill"><b>3</b> stores</span>\n'
        '      <span class="arch-pill"><b>5</b> flows</span>\n'
        '      <span class="arch-pill"><b>6</b> vendors</span>'
    )
    new_arch_pills = (
        f'      <span class="arch-pill"><b>{n_sys}</b> systems</span>\n'
        f'      <span class="arch-pill"><b>{n_stores}</b> stores</span>\n'
        f'      <span class="arch-pill"><b>{n_flows}</b> flows</span>\n'
        f'      <span class="arch-pill"><b>{n_vendors}</b> vendors</span>'
    )
    new_html = new_html.replace(old_arch_pills, new_arch_pills)

    # Patch vendorRows attributes mapping for Case_02
    old_vendor_mapping = (
        '    return {\n'
        '      id: n.id,\n'
        '      name: a.name || n.id,\n'
        '      alias: (a.aliases && a.aliases[0]) || "",\n'
        '      services: a.services || [],\n'
        '      data_accessed: a.data_accessed || [],\n'
        '      criticality: a.criticality || "",\n'
        '      risk: a.risk_score || "?",\n'
        '      art_28: a.art_28_dpa === true,\n'
        '      sbom: a.sbom_available === true,\n'
        '      exit: a.exit_plan === true,\n'
        '      last_review: (a.last_assessment || "").slice(0, 10),\n'
        '      regions: a.regions || [],\n'
        '      next_review: a.next_review || "",\n'
        '      security_audit_right: a.security_audit_right || "",\n'
        '      subprocessor_approval: a.subprocessor_approval || "",\n'
        '      art_30: a.art_30_clauses === true,\n'
        '      attrs: a,\n'
        '      source: n.source || []\n'
        '    };'
    )
    new_vendor_mapping = (
        '    const srv = Array.isArray(a.services) ? a.services : (a.services ? [String(a.services)] : []);\n'
        '    const dacc = Array.isArray(a.data_accessed) ? a.data_accessed : (a.data_accessed ? [String(a.data_accessed)] : []);\n'
        '    const regs = Array.isArray(a.regions) ? a.regions : (a.regions ? [String(a.regions)] : []);\n'
        '    return {\n'
        '      id: n.id,\n'
        '      name: a.name || n.id,\n'
        '      alias: (a.aliases && a.aliases[0]) || "",\n'
        '      services: srv,\n'
        '      data_accessed: dacc,\n'
        '      criticality: a.criticality || "medium",\n'
        '      risk: a.risk_score || "M",\n'
        '      art_28: a.dpa_in_place === true || a.article_28_compliant === true || a.art_28_dpa === true,\n'
        '      sbom: a.sbom_available === true,\n'
        '      exit: a.exit_plan === true,\n'
        '      last_review: (a.last_assessment || "").slice(0, 10),\n'
        '      regions: regs,\n'
        '      next_review: a.next_review || "",\n'
        '      security_audit_right: a.security_audit_right || "",\n'
        '      subprocessor_approval: a.subprocessor_approval || "",\n'
        '      art_30: a.art_30_clauses === true,\n'
        '      attrs: a,\n'
        '      source: n.source || []\n'
        '    };'
    )
    new_html = new_html.replace(old_vendor_mapping, new_vendor_mapping)

    # 15. Folio VIII AI-RMF support in initMaturity()
    old_mat_fn_detect = (
        '  const capByFn = new Map();\n'
        '  const capByFnPF = new Map();\n'
        '  for (const n of capability) {\n'
        '    const fn = csfFunction(n.attrs.outcome);\n'
        '    const fnPF = pfFunction(n.attrs.outcome);\n'
        '    if (fn) { if (!capByFn.has(fn)) capByFn.set(fn, []); capByFn.get(fn).push(n); }\n'
        '    if (fnPF) { if (!capByFnPF.has(fnPF)) capByFnPF.set(fnPF, []); capByFnPF.get(fnPF).push(n); }\n'
        '  }'
    )
    new_mat_fn_detect = (
        '  const AIRMF_FN_OF = { "GOVERN-": "GOVERN-AI", "MAP-": "MAP-AI", "MEASURE-": "MEASURE-AI", "MANAGE-": "MANAGE-AI" };\n'
        '  function airmfFunction(outcome) {\n'
        '    for (const p of Object.keys(AIRMF_FN_OF)) if (outcome && outcome.startsWith(p)) return AIRMF_FN_OF[p];\n'
        '    return null;\n'
        '  }\n'
        '  const capByFn = new Map();\n'
        '  const capByFnPF = new Map();\n'
        '  const capByFnAI = new Map();\n'
        '  for (const n of capability) {\n'
        '    const fn = csfFunction(n.attrs.outcome);\n'
        '    const fnPF = pfFunction(n.attrs.outcome);\n'
        '    const fnAI = airmfFunction(n.attrs.outcome);\n'
        '    if (fn) { if (!capByFn.has(fn)) capByFn.set(fn, []); capByFn.get(fn).push(n); }\n'
        '    if (fnPF) { if (!capByFnPF.has(fnPF)) capByFnPF.set(fnPF, []); capByFnPF.get(fnPF).push(n); }\n'
        '    if (fnAI) { if (!capByFnAI.has(fnAI)) capByFnAI.set(fnAI, []); capByFnAI.get(fnAI).push(n); }\n'
        '  }'
    )
    new_html = new_html.replace(old_mat_fn_detect, new_mat_fn_detect)

    open(HTML_PATH, "w", encoding="utf-8").write(new_html)
    print(f"wrote {HTML_PATH} ({len(graph_data)} bytes JSON inlined)", file=sys.stderr)


def build_maturity(graph: dict, graph_data: str) -> None:
    if not MATURITY_HTML_PATH.exists():
        return
    html = open(MATURITY_HTML_PATH, encoding="utf-8").read()

    # Inlining JSON scripts in head
    json_block = '<script type="application/json" id="phase1-graph-data">' + graph_data + '</script>'
    obj_literal = '<script>window.PHASE1_GRAPH_DATA = ' + graph_data + ';</script>'

    if 'id="phase1-graph-data"' in html:
        html = re.sub(
            r'<script type="application/json" id="phase1-graph-data">.*?</script>',
            '',
            html, count=1, flags=re.DOTALL)
    if 'window.PHASE1_GRAPH_DATA = {' in html:
        html = re.sub(
            r'<script>window\.PHASE1_GRAPH_DATA = \{.*?\};</script>',
            '',
            html, count=1, flags=re.DOTALL)
    html = html.replace("</head>", json_block + "\n" + obj_literal + "\n</head>", 1)

    # Replace load() with window.PHASE1_GRAPH_DATA shortcut
    html = html.replace(
        'async function load() {\n'
        '  try {\n'
        '    const r = await fetch(DATA_PATH_C02);',
        'async function load() {\n'
        '  try {\n'
        '    if (window.PHASE1_GRAPH_DATA) { initMaturity(window.PHASE1_GRAPH_DATA); return; }\n'
        '    const r = await fetch(DATA_PATH_C02);'
    )

    open(MATURITY_HTML_PATH, "w", encoding="utf-8").write(html)
    print(f"wrote {MATURITY_HTML_PATH} ({len(graph_data)} bytes JSON inlined)", file=sys.stderr)


def main(argv: list[str]) -> int:
    graph = json.load(open(GRAPH_PATH, encoding="utf-8"))
    graph_data = json.dumps(graph, ensure_ascii=False)

    build_dashboard(graph, graph_data)
    build_maturity(graph, graph_data)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))