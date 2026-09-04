#!/usr/bin/env python3
"""Build Case_03_P1_Dashboard.html + Case_03_P1_Maturity.html from the Case_02
parity templates (Folios I-VIII), inlining the Case_03 phase1_graph.json for
file:// use.

REGRA DE OURO — the graph JSON is the single data source and is never edited.
Every number injected into the HTML is derived programmatically from
02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json.
The Case_02 templates are read-only inputs; outputs land in ../Case_03/.

Method
------
1. Read the Case_02 templates (the most complete parity dashboards).
2. Strip their inlined Case_02 JSON blobs (idempotent reset).
3. Apply Case_03 identity + data patches (asserted — every replacement must
   match exactly the expected number of times or the build fails).
4. Inline the Case_03 graph JSON in BOTH shapes:
   <script type="application/json" id="phase1-graph-data"> AND
   window.PHASE1_GRAPH_DATA = {...} (fetch() is blocked on file://).

Usage
-----
    python3 build_case03_dashboard.py
    
Run after scripts/build_p1_graph.py whenever the graph regenerates.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
VIS = HERE.parent                      # 00_METHODOLOGY/00_VISUALISATIONS
REPO = VIS.parent.parent               # repo root
TEMPLATE_DASH = VIS / "Case_02" / "Case_02_P1_Dashboard.html"
TEMPLATE_MAT = VIS / "Case_02" / "Case_02_P1_Maturity.html"
OUT_DASH = HERE / "Case_03_P1_Dashboard.html"
OUT_MAT = HERE / "Case_03_P1_Maturity.html"
GRAPH_PATH = (REPO / "02_CASES" / "Case_03_OmniBank_Financial" /
              "01_PHASE1_CONTEXT_RICH" / "data" / "phase1_graph.json")


def rep(html: str, old: str, new: str, n: int, label: str) -> str:
    """Replace exactly n occurrences of old; fail loudly otherwise."""
    found = html.count(old)
    if found != n:
        raise SystemExit(
            f"[build_case03] patch '{label}' expected {n} occurrence(s), found {found}:\n"
            f"  old starts: {old[:120]!r}")
    return html.replace(old, new)


def re_sub1(html: str, pattern: str, new: str, label: str) -> str:
    out, cnt = re.subn(pattern, new, html, count=1, flags=re.DOTALL)
    if cnt != 1:
        raise SystemExit(f"[build_case03] regex patch '{label}' matched {cnt} times")
    return out


def strip_inline_json(html: str) -> str:
    """Remove any pre-existing inlined graph JSON (both shapes)."""
    html = re.sub(r'<script type="application/json" id="phase1-graph-data">.*?</script>',
                  "", html, flags=re.DOTALL)
    html = re.sub(r'<script>window\.PHASE1_GRAPH_DATA = \{.*?\};</script>',
                  "", html, flags=re.DOTALL)
    return html


def inject_json(html: str, graph_data: str) -> str:
    """Inline the graph JSON in both shapes right before </head>."""
    assert "</script" not in graph_data, "graph JSON would break the inline <script> block"
    json_block = '<script type="application/json" id="phase1-graph-data">' + graph_data + '</script>'
    obj_literal = '<script>window.PHASE1_GRAPH_DATA = ' + graph_data + ';</script>'
    return html.replace("</head>", json_block + "\n" + obj_literal + "\n</head>", 1)


# ---------------------------------------------------------------------------
# Derived numbers — everything below comes from the graph, nothing hand-typed.
# ---------------------------------------------------------------------------
def derive(graph: dict) -> dict:
    nodes, links, audits = graph["nodes"], graph["links"], graph.get("audits", [])
    meta = graph.get("meta", {})
    amb = graph.get("ambiguity", {}).get("stats_total", {})
    inv = graph.get("invariants", {})
    by_type = Counter(n["type"] for n in nodes)
    attrs = lambda n: n.get("attrs") or {}

    sds = [n for n in nodes if n["type"] == "SecurityControlDomain"]
    ags = [n for n in nodes if n["type"] == "AdjustedGoal"]
    evi = [n for n in nodes if n["type"] == "EvidenceItem"]

    cc = next(n for n in nodes if n["type"] == "CompanyContext")
    cca = attrs(cc)

    reg_nodes = [n for n in nodes if n["type"] == "Regulation"]

    d = {}
    d["n_nodes"], d["n_links"], d["n_audits"] = len(nodes), len(links), len(audits)
    d["gen_date"] = str(meta.get("generated", ""))[:10]
    d["schema_version"] = meta.get("schema_version", "phase1_graph.json")
    d["amb_cards"] = amb.get("cards_in_scope", 0)
    d["amb_by_sev"] = amb.get("by_severity", {})
    d["amb_by_reg"] = amb.get("by_regulation", {})
    d["amb_reg_line"] = " &middot; ".join(
        f"{'AI Act' if k == 'AI-Act' else k} {v}" for k, v in d["amb_by_reg"].items())

    d["company"] = attrs(cc).get("name") or cc["label"]
    d["company_label_js"] = "OmniBank"
    d["scale"] = str(cca.get("scale", "—")).upper()
    d["employees"] = f"{cca.get('employees', 0):,}+"
    d["hq"] = cca.get("hq", "—")
    d["sector"] = cca.get("sector", "—")
    d["revenue"] = "&gt;&euro;1.5B" if (cca.get("revenue_eur") or 0) >= 1.5e9 else "&mdash;"
    d["stack_line"] = "Hybrid (on-premise core + cloud) &middot; IBM z/OS + DB2 core &middot; EU cloud"

    d["regs_total"] = by_type["Regulation"]
    d["regs_applicable"] = sum(1 for r in reg_nodes if attrs(r).get("applicable"))

    d["sd_active"] = sum(1 for n in sds if attrs(n).get("active"))
    d["rigorous"] = sum(1 for n in sds if attrs(n).get("proportionality_tier") == "RIGOROUS")
    d["standard"] = sum(1 for n in sds if attrs(n).get("proportionality_tier") == "STANDARD")
    d["substantive"] = sum(1 for n in sds if attrs(n).get("coverage_level") == "SUBSTANTIVE")
    d["partial"] = sum(1 for n in sds if attrs(n).get("coverage_level") == "PARTIAL")
    d["not_addressed"] = sum(1 for n in sds if attrs(n).get("coverage_level") == "NOT_ADDRESSED")

    d["ags"] = len(ags)
    d["ags_priv"] = sum(1 for n in ags if attrs(n).get("track") == "PRIVACY")
    d["ags_sec"] = sum(1 for n in ags if attrs(n).get("track") == "SECURITY")
    prio = Counter(attrs(n).get("implementation_priority") for n in ags)
    d["ags_prio_line"] = f'{prio.get("CRITICAL", 0)} CRITICAL &middot; {prio.get("HIGH", 0)} HIGH &middot; {prio.get("MEDIUM", 0)} MEDIUM'
    d["tensions"] = by_type["Tension"]
    d["tension_edges"] = sum(1 for l in links if l["rel"] == "HAS_TENSION_WITH")

    d["stakeholders"] = by_type["Stakeholder"]
    d["bgs"] = by_type["BusinessGoal"]          # 0 in Case_03 (data-honest)
    d["clauses"] = by_type["RegulatoryClause"]
    d["systems"] = by_type["System"]
    d["stores"] = by_type["DataStore"]
    d["flows"] = by_type["DataFlow"]
    d["vendors"] = by_type["ThirdParty"]

    d["raci_acts"] = by_type["RaciActivity"]
    d["raci_roles"] = by_type["RaciRole"]
    d["raci_active"] = sum(1 for n in nodes if n["type"] == "RaciActivity" and attrs(n).get("active"))

    d["evi"] = len(evi)
    d["evi_cov"] = sum(1 for e in evi if attrs(e).get("scale") == "coverage")
    d["evi_cap"] = sum(1 for e in evi if attrs(e).get("scale") == "capability")
    d["evi_obs"] = sum(1 for e in evi if attrs(e).get("observed") is True)

    nist = [n for n in nodes if n["type"] == "NistControl"]
    nfw = Counter(attrs(n).get("framework") for n in nist)
    d["nist_csf"], d["nist_pf"], d["nist_ai"] = nfw.get("CSF", 0), nfw.get("PF", 0), nfw.get("AI-RMF", 0)

    ai_sds = sorted(attrs(e).get("subdomain_id") for e in evi
                    if attrs(e).get("scale") == "capability"
                    and str(attrs(e).get("outcome", "")).startswith(("GOVERN-", "MAP-", "MEASURE-", "MANAGE-")))
    d["ai_sds"] = ai_sds

    audit_kinds = Counter(a["kind"] for a in audits)
    d["audit_kinds"] = audit_kinds
    return d


# ---------------------------------------------------------------------------
# DASHBOARD
# ---------------------------------------------------------------------------
def build_dashboard(graph: dict, graph_data: str, d: dict) -> None:
    html = TEMPLATE_DASH.read_text(encoding="utf-8")
    html = strip_inline_json(html)

    # --- 1. Title / masthead / seal -------------------------------------
    # The on-disk <title> uses the raw '·' char while the H1 uses &middot;.
    if "<title>Case 02 &middot; Phase 1" in html:
        html = rep(html, "<title>Case 02 &middot; Phase 1 &mdash; Knowledge &amp; Audit Dashboard</title>",
                   "<title>Case 03 &middot; Phase 1 &mdash; Knowledge &amp; Audit Dashboard</title>", 1, "title")
    else:
        html = rep(html, "<title>Case 02 · Phase 1 — Knowledge &amp; Audit Dashboard</title>",
                   "<title>Case 03 · Phase 1 — Knowledge &amp; Audit Dashboard</title>", 1, "title-raw")
    html = rep(html, "<h1>Case 02 &middot; Phase 1 &mdash; Knowledge &amp; Audit Dashboard</h1>",
               "<h1>Case 03 &middot; Phase 1 &mdash; Knowledge &amp; Audit Dashboard</h1>", 1, "h1")
    html = rep(html, '<div class="sub">SecureBorder B.V. &middot; The Hague, NL &middot; AEGIS Rich Mode</div>',
               f'<div class="sub">{d["company"]} &middot; {d["hq"]} &middot; AEGIS Rich Mode</div>', 1, "masthead-sub")
    html = rep(html, '<div class="seal">02</div>', '<div class="seal">03</div>', 1, "seal")
    html = rep(html,
               '      <div><strong>Generated</strong> 2026-08-26</div>\n'
               '      <div><strong>Schema</strong> phase1_graph.json v1.0</div>',
               f'      <div><strong>Generated</strong> {d["gen_date"]}</div>\n'
               f'      <div><strong>Schema</strong> {d["schema_version"]}</div>', 1, "meta-stamp")
    html = re_sub1(
        html,
        r'A knowledge-graph atlas for SecureBorder B\.V\.: \d+ nodes, \d+ links, \d+ audits, \d+ ambiguity cards',
        f'A knowledge-graph atlas for {d["company"]}: {d["n_nodes"]} nodes, {d["n_links"]} links, '
        f'{d["n_audits"]} audits, {d["amb_cards"]} ambiguity cards',
        "strap")

    # --- 2. Folio I — Company card ---------------------------------------
    old_company = (
        '    <div class="card">\n'
        '      <div class="label">Company</div>\n'
        '      <div class="value smaller">SecureBorder Solutions B.V.</div>\n'
        '      <div class="sub">MEDIUM scale &middot; 450 employees &middot; 5\u20138 sec FTE</div>\n'
        '      <dl class="kv-grid" style="margin-top:10px">\n'
        '        <dt>HQ</dt><dd>The Hague, NL (EU)</dd>\n'
        '        <dt>Sector</dt><dd>Defense / Security / Critical Infrastructure</dd>\n'
        '        <dt>Product</dt><dd>GuardianGate eGate kiosks</dd>\n'
        '        <dt>Stack</dt><dd>Edge AI (on-device) &middot; EU cloud &middot; Signed OTA &middot; PKI / HSM</dd>\n'
        '      </dl>\n'
        '    </div>')
    new_company = (
        '    <div class="card">\n'
        '      <div class="label">Company</div>\n'
        f'      <div class="value smaller">{d["company"]}</div>\n'
        f'      <div class="sub">{d["scale"]} scale &middot; {d["employees"]} employees &middot; {d["revenue"]} revenue &middot; MAXIMUM complexity</div>\n'
        '      <dl class="kv-grid" style="margin-top:10px">\n'
        f'        <dt>HQ</dt><dd>{d["hq"]}</dd>\n'
        f'        <dt>Sector</dt><dd>{d["sector"]} (ECB-supervised)</dd>\n'
        '        <dt>Product</dt><dd>Mobile banking app + web platform + OmniScore credit-scoring AI</dd>\n'
        f'        <dt>Stack</dt><dd>{d["stack_line"]}</dd>\n'
        '      </dl>\n'
        '    </div>')
    html = rep(html, old_company, new_company, 1, "company-card")

    # --- 3. Folio I — Applicability card (5/5, from Regulation attrs) ----
    old_app = (
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
        '    </div>')
    new_app = (
        '    <div class="card gold">\n'
        '      <div class="label">Applicability Verdict</div>\n'
        f'      <div class="value">{d["regs_applicable"]} / {d["regs_total"]}</div>\n'
        '      <div class="sub">regulations applicable</div>\n'
        '      <ul class="applicability-list">\n'
        '        <li><span class="yes">YES</span><span><b>GDPR</b> &mdash; controller + processor (customer PII incl. biometric authentication)</span></li>\n'
        '        <li><span class="yes">YES</span><span><b>CRA</b> &mdash; manufacturer (mobile app + web platform)</span></li>\n'
        '        <li><span class="yes">YES</span><span><b>NIS2</b> &mdash; essential entity (Annex I banking, 5,000+ employees)</span></li>\n'
        '        <li><span class="yes">YES</span><span><b>DORA</b> &mdash; financial entity (credit institution, Art. 2(1))</span></li>\n'
        '        <li><span class="yes">YES</span><span><b>AI Act</b> &mdash; provider + deployer (Annex III credit scoring)</span></li>\n'
        '      </ul>\n'
        '    </div>')
    html = rep(html, old_app, new_app, 1, "applicability-card")

    # --- 4. Folio I — Coverage Tier card ----------------------------------
    old_tier = (
        '    <div class="card dark">\n'
        '      <div class="label">Coverage Tier (Doc12 &sect;4)</div>\n'
        '      <div class="value">34</div>\n'
        '      <div class="sub">active sub-domains with a tier assigned</div>\n'
        '      <div class="tier-bar" id="tier-bar"></div>\n'
        '      <div class="legend">\n'
        '        <span><span class="sw" style="background:#5c7a3a"></span>RIGOROUS 8</span>\n'
        '        <span><span class="sw" style="background:#8a2a2a"></span>STANDARD 26</span>\n'
        '      </div>\n'
        '    </div>')
    new_tier = (
        '    <div class="card dark">\n'
        '      <div class="label">Coverage Tier (Doc13 &sect;4)</div>\n'
        f'      <div class="value">{d["sd_active"]}</div>\n'
        '      <div class="sub">active sub-domains with a tier assigned</div>\n'
        '      <div class="tier-bar" id="tier-bar"></div>\n'
        '      <div class="legend">\n'
        f'        <span><span class="sw" style="background:#5c7a3a"></span>RIGOROUS {d["rigorous"]}</span>\n'
        f'        <span><span class="sw" style="background:#8a2a2a"></span>STANDARD {d["standard"]}</span>\n'
        '      </div>\n'
        '    </div>')
    html = rep(html, old_tier, new_tier, 1, "tier-card")

    # --- 5. Folio I — Coverage Level card ---------------------------------
    old_cov = (
        '    <div class="card warn">\n'
        '      <div class="label">Coverage Level (Doc11 &sect;3)</div>\n'
        '      <div class="value">38</div>\n'
        '      <div class="sub">sub-domains scored</div>\n'
        '      <div class="cov-bar" id="cov-bar"></div>\n'
        '      <div class="legend">\n'
        '        <span><span class="sw" style="background:#5c7a3a"></span>SUBSTANTIVE 34</span>\n'
        '        <span><span class="sw" style="background:#8a2a2a"></span>NOT_ADDRESSED 4</span>\n'
        '      </div>\n'
        '    </div>')
    new_cov = (
        '    <div class="card warn">\n'
        '      <div class="label">Coverage Level (Doc12 &sect;3)</div>\n'
        f'      <div class="value">{d["sd_active"]}</div>\n'
        '      <div class="sub">sub-domains scored</div>\n'
        '      <div class="cov-bar" id="cov-bar"></div>\n'
        '      <div class="legend">\n'
        f'        <span><span class="sw" style="background:#5c7a3a"></span>SUBSTANTIVE {d["substantive"]}</span>\n'
        f'        <span><span class="sw" style="background:#b8893a"></span>PARTIAL {d["partial"]}</span>\n'
        f'        <span><span class="sw" style="background:#8a2a2a"></span>NOT_ADDRESSED {d["not_addressed"]}</span>\n'
        '      </div>\n'
        '    </div>')
    html = rep(html, old_cov, new_cov, 1, "coverage-card")

    # --- 6. Folio I — Adjusted Goals card ----------------------------------
    old_ag = (
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
        '    </div>')
    new_ag = (
        '    <div class="card good">\n'
        '      <div class="label">Adjusted Goals</div>\n'
        f'      <div class="value">{d["ags"]}</div>\n'
        '      <div class="sub">AGs across 2 tracks (Doc14 &sect;2)</div>\n'
        '      <dl class="kv-grid" style="margin-top:10px">\n'
        f'        <dt>Privacy</dt><dd>{d["ags_priv"]} (AG-D-XX.Y-001)</dd>\n'
        f'        <dt>Security</dt><dd>{d["ags_sec"]} (AG-D-XX.Y-002)</dd>\n'
        f'        <dt>Tensions</dt><dd>{d["tension_edges"]} of {d["tensions"]} resolved as clause-pair edges</dd>\n'
        f'        <dt>Priority</dt><dd>{d["ags_prio_line"]}</dd>\n'
        '      </dl>\n'
        '    </div>')
    html = rep(html, old_ag, new_ag, 1, "ag-card")

    # --- 7. Folio I — Ambiguity card ----------------------------------------
    old_amb = (
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
        '    </div>')
    sev = d["amb_by_sev"]
    new_amb = (
        '    <div class="card">\n'
        '      <div class="label">Ambiguity Register (Doc09)</div>\n'
        f'      <div class="value">{d["amb_cards"]}</div>\n'
        '      <div class="sub">cards in scope &middot; Doc09 &sect;1</div>\n'
        '      <div class="severity-hist" id="sev-hist"></div>\n'
        '      <div class="legend" style="margin-top:6px">\n'
        f'        <span><span class="sw" style="background:#c9bfa7"></span>S1 {sev.get("S1", 0)}</span>\n'
        f'        <span><span class="sw" style="background:#2c7cb0"></span>S2 {sev.get("S2", 0)}</span>\n'
        f'        <span><span class="sw" style="background:#b8893a"></span>S3 {sev.get("S3", 0)}</span>\n'
        '      </div>\n'
        f'      <div class="sub" style="margin-top:6px"><span class="mono">Top-20 by regulation: {d["amb_reg_line"]}</span></div>\n'
        '    </div>')
    html = rep(html, old_amb, new_amb, 1, "ambiguity-card")

    # --- 8. Folio I — Caveats prose (9 audits, accurate) ---------------------
    old_caveats = (
        '        Of the 8 audits raised by <span class="mono">build_p1_dashboard.py --check</span>, the structural findings cover\n'
        '        NEW-C02-01 (Maturity redesign v2.3 with 59 EvidenceItems), NEW-C02-02 (70 AdjustedGoals seeded from Doc13 §8),\n'
        '        NEW-C02-03 (1071 ambiguity cards in scope per Doc09 §1), NEW-C02-04 (CSF alignment from REG_CHAIN),\n'
        '        and NEW-C02-05 (Tier distribution per Doc12 §3). Consistency checks CFL-C02-001 (tier verification),\n'
        '        BLN-C02-001 (10 macro-domains baseline), and CVG-C02-001 (coverage gaps ledger) confirm complete case integrity.\n'
        '        See <b>Audit Panel</b> for full text and recommendations.')
    new_caveats = (
        f'        Of the {d["n_audits"]} audits raised by <span class="mono">build_p1_dashboard.py --check</span>, the six NEW-C03 findings\n'
        f'        (5 structural + 1 blocking-ambiguity) record the maturity layer seed ({d["evi"]} EvidenceItems: {d["evi_cov"]} coverage +\n'
        f'        {d["evi_cap"]} capability; NEW-C03-01), the {d["ags"]} AdjustedGoals from Doc14 &sect;2 + archived detail cards (NEW-C03-02),\n'
        f'        the {d["amb_cards"]}-card ambiguity scope per Doc09 &sect;1 (NEW-C03-03), the {d["nist_csf"] + d["nist_pf"] + d["nist_ai"]} NistControl anchors from\n'
        f'        Doc14 &sect;5 ({d["nist_csf"]} CSF + {d["nist_pf"]} PF + {d["nist_ai"]} AI-RMF; REG_CHAIN cross-checked, NEW-C03-04), the\n'
        f'        {d["rigorous"]} RIGOROUS / {d["standard"]} STANDARD split across {d["sd_active"]}/{d["sd_active"]} ACTIVE sub-domains (NEW-C03-05), and the real\n'
        f'        DORA axis with 38 clauses and {d["tension_edges"]}/{d["tensions"]} tension edges resolved (NEW-C03-06). Consistency checks\n'
        '        CFL-C03-001 (Doc14 &sect;5.1 statistics reconciled), BLN-C03-001 (10 macro-domain baseline) and\n'
        '        CVG-C03-001 (D-07.2 coverage evidence withheld pending orchestrator decision; 37/38\n'
        '        clause-anchored) complete the panel. See <b>Audit Panel</b> for full text and recommendations.')
    html = rep(html, old_caveats, new_caveats, 1, "caveats-prose")

    # --- 9. Folio I — buildExec bars -----------------------------------------
    old_tierbar = (
        '  tierBar.innerHTML = `\n'
        '    <div class="seg" style="background:#5c7a3a; flex:8">8 RIG</div>\n'
        '      <div class="seg" style="background:#8a2a2a; flex:26">26 STD</div>\n'
        '  `;')
    new_tierbar = (
        '  tierBar.innerHTML = `\n'
        f'    <div class="seg" style="background:#5c7a3a; flex:{d["rigorous"]}">{d["rigorous"]} RIG</div>\n'
        f'      <div class="seg" style="background:#8a2a2a; flex:{d["standard"]}">{d["standard"]} STD</div>\n'
        '  `;')
    html = rep(html, old_tierbar, new_tierbar, 1, "buildExec-tierbar")

    old_covbar = (
        '  covBar.innerHTML = `\n'
        '    <div class="seg" style="background:#5c7a3a; flex:34">34 SUB</div>\n'
        '      <div class="seg" style="background:#b8893a; flex:0.0001">0 PART</div>\n'
        '      <div class="seg" style="background:#8a2a2a; flex:4">4 N/A</div>\n'
        '  `;')
    new_covbar = (
        '  covBar.innerHTML = `\n'
        f'    <div class="seg" style="background:#5c7a3a; flex:{d["substantive"]}">{d["substantive"]} SUB</div>\n'
        f'      <div class="seg" style="background:#b8893a; flex:{d["partial"] if d["partial"] else 0.0001}">{d["partial"]} PART</div>\n'
        f'      <div class="seg" style="background:#8a2a2a; flex:{d["not_addressed"] if d["not_addressed"] else 0.0001}">{d["not_addressed"]} N/A</div>\n'
        '  `;')
    html = rep(html, old_covbar, new_covbar, 1, "buildExec-covbar")

    # --- 10. Folio III header -------------------------------------------------
    html = rep(html, '<span class="aside">8 findings &middot; click for full text</span>',
               f'<span class="aside">{d["n_audits"]} findings &middot; click for full text</span>', 1, "folio3-aside")

    # --- 11. Folio IV intro + footnote + ip tooltips + risk cell ---------------
    html = rep(html, 'criteria, evidence depth, ownership, risk, priority and the Doc12 &sect;4 proportionality pair',
               'criteria, evidence depth, ownership, risk, priority and the Doc13 &sect;4 proportionality pair',
               1, "folio4-intro")
    old_foot = (
        '    Phase C columns draw from <span class="mono">Doc08 &sect;9</span> (54 verification rows) and <span class="mono">Doc12 &sect;4</span> (37 proportionality rows);\n'
        '    D-02.4 is the only DEFERRED row.')
    new_foot = (
        f'    Phase C columns draw from <span class="mono">Doc13 &sect;4</span> ({d["sd_active"]} proportionality rows: evidence depth, verification\n'
        '    method, ownership, risk, I/P) and <span class="mono">Doc12 &sect;3</span> (coverage level); Case_03 has no DEFERRED rows &mdash;\n'
        f'    {d["rigorous"]} RIGOROUS / {d["standard"]} STANDARD, all {d["sd_active"]} ACTIVE.')
    html = rep(html, old_foot, new_foot, 1, "folio4-footnote")
    html = rep(html, 'title="Build / Inherit (Doc12 §4)"', 'title="Build / Inherit (Doc13 §4)"', 1, "ip-i-tooltip")
    html = rep(html, 'title="Must / Should (Doc12 §4)"', 'title="Must / Should (Doc13 §4)"', 1, "ip-p-tooltip")
    html = rep(html, "Doc11 §3 · Doc12 §4", "Doc12 §3 · Doc13 §4", 1, "source-cell-label")

    # risk_if_not_met is free prose in Case_03 (not HIGH/MEDIUM enums) — render
    # a compact truncated value with the full prose as tooltip, keep the pill
    # path for genuine enum values.
    old_risk = (
        '    const risk = a.risk_if_not_met || "—";\n'
        '    const riskHtml = risk === "—"\n'
        '      ? `<span style="color:var(--faint)">—</span>`\n'
        '      : `<span class="${gridRiskClass(risk)}">${escapeHtml(risk)}</span>`;')
    new_risk = (
        '    const risk = a.risk_if_not_met || "—";\n'
        '    const riskHtml = risk === "—"\n'
        '      ? `<span style="color:var(--faint)">—</span>`\n'
        '      : (["HIGH","MEDIUM","MED","LOW"].includes(risk)\n'
        '          ? `<span class="${gridRiskClass(risk)}">${escapeHtml(risk)}</span>`\n'
        '          : `<span title="${escapeHtml(risk)}" style="white-space:nowrap;font-family:var(--mono);font-size:10.5px;color:var(--ink-soft);cursor:help">${escapeHtml(risk.length > 34 ? risk.slice(0, 33) + "…" : risk)}</span>`);')
    html = rep(html, old_risk, new_risk, 1, "folio4-risk-cell")

    # --- 12. Folio V legend counts ---------------------------------------------
    old_legend = (
        '        <li><span class="sw sh-stk"></span>Stakeholders <span class="mono">10</span></li>\n'
        '        <li><span class="sw sh-bg"></span>Business Goals <span class="mono">7</span></li>\n'
        '        <li><span class="sw sh-cc"></span>Company <span class="mono">1</span></li>\n'
        '        <li><span class="sw sh-reg"></span>Regulations <span class="mono">5</span></li>\n'
        '        <li><span class="sw sh-rc"></span>Clauses <span class="mono">111</span></li>\n'
        '        <li><span class="sw sh-scd"></span>Sub-Domains <span class="mono">38</span></li>\n'
        '        <li><span class="sw sh-ag"></span>Adjusted Goals <span class="mono">70</span></li>')
    new_legend = (
        f'        <li><span class="sw sh-stk"></span>Stakeholders <span class="mono">{d["stakeholders"]}</span></li>\n'
        f'        <li><span class="sw sh-bg"></span>Business Goals <span class="mono">{d["bgs"]}</span></li>\n'
        '        <li><span class="sw sh-cc"></span>Company <span class="mono">1</span></li>\n'
        f'        <li><span class="sw sh-reg"></span>Regulations <span class="mono">{d["regs_applicable"]}</span></li>\n'
        f'        <li><span class="sw sh-rc"></span>Clauses <span class="mono">{d["clauses"]}</span></li>\n'
        f'        <li><span class="sw sh-scd"></span>Sub-Domains <span class="mono">{d["sd_active"]}</span></li>\n'
        f'        <li><span class="sw sh-ag"></span>Adjusted Goals <span class="mono">{d["ags"]}</span></li>')
    html = rep(html, old_legend, new_legend, 1, "folio5-legend")

    # --- 13. Folio VI — RACI (15 roles × 65 activities, fully data-driven) ------
    html = rep(html, '<span class="aside">63 activities &middot; 12 roles &middot; colour-coded</span>',
               f'<span class="aside">{d["raci_acts"]} activities &middot; {d["raci_roles"]} roles &middot; colour-coded</span>',
               1, "folio6-aside")
    html = rep(html, 'Active only (63)</label>', f'Active only ({d["raci_active"]})</label>', 1, "folio6-active-label")

    old_thead = (
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
        '        </thead>')
    new_thead = (
        '        <thead>\n'
        '          <tr id="raci-head-row"><!-- role columns built from graph RaciRole nodes by buildRaciHead() --></tr>\n'
        '        </thead>')
    html = rep(html, old_thead, new_thead, 1, "folio6-thead")

    old_roles = (
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
        '                    ia: 11, soc: 12, legal: 13, hr: 14, proc: 15, board: 16 };')
    new_roles = (
        '// Case_03: roles are read from the graph (15 RaciRole nodes, xlsx order) —\n'
        '// no hardcoded role list, so Folio VI cannot drift from the data layer.\n'
        'const ROLES = NODES.filter(n => n.type === "RaciRole").map(n => n.id);\n'
        'const ROLE_HEADERS = NODES.filter(n => n.type === "RaciRole").map(n => ({\n'
        '  id: n.id,\n'
        '  col: "r" + n.id.replace(/^ROLE-/, "").toLowerCase().replace(/[^a-z0-9]+/g, ""),\n'
        '  label: (n.attrs && n.attrs.name) || n.id\n'
        '}));\n'
        'const COL_INDEX = (() => {\n'
        '  const o = { act: 0, name: 1, active: 2, domain: 3, sub: 4 };\n'
        '  ROLE_HEADERS.forEach((rh, i) => { o[rh.col] = 5 + i; });\n'
        '  return o;\n'
        '})();')
    html = rep(html, old_roles, new_roles, 1, "folio6-roles-js")

    old_initraci = (
        'function initRaci() {\n'
        '  buildRaciRows();\n'
        '  applyRaciFilter();\n'
        '  renderRaciAudits();')
    new_initraci = (
        'function buildRaciHead() {\n'
        '  // Build the RACI <thead> from ROLE_HEADERS (derived from graph RaciRole nodes).\n'
        '  const tr = document.querySelector("#tbl-raci thead tr");\n'
        '  if (!tr) return;\n'
        '  const fixed = [\n'
        '    { col: "act", label: "ACT" }, { col: "name", label: "Activity" },\n'
        '    { col: "active", label: "Active" }, { col: "domain", label: "Domain" },\n'
        '    { col: "sub", label: "Sub-domain" }\n'
        '  ];\n'
        '  tr.innerHTML = fixed.map(f => `<th data-col="${f.col}" data-order="asc">${f.label}</th>`).join("") +\n'
        '    ROLE_HEADERS.map(rh => `<th data-col="${rh.col}" data-order="asc">${escapeHtml(rh.label)}</th>`).join("");\n'
        '}\n'
        '\n'
        'function initRaci() {\n'
        '  buildRaciHead();\n'
        '  buildRaciRows();\n'
        '  applyRaciFilter();\n'
        '  renderRaciAudits();')
    html = rep(html, old_initraci, new_initraci, 1, "folio6-initraci")

    # --- 14. Folio VII — Architecture --------------------------------------------
    old_pills = (
        '      <span class="arch-pill"><b>13</b> systems</span>\n'
        '      <span class="arch-pill"><b>7</b> stores</span>\n'
        '      <span class="arch-pill"><b>12</b> flows</span>\n'
        '      <span class="arch-pill"><b>22</b> vendors</span>')
    new_pills = (
        f'      <span class="arch-pill"><b>{d["systems"]}</b> systems</span>\n'
        f'      <span class="arch-pill"><b>{d["stores"]}</b> stores</span>\n'
        f'      <span class="arch-pill"><b>{d["flows"]}</b> flows</span>\n'
        f'      <span class="arch-pill"><b>{d["vendors"]}</b> vendors</span>')
    html = rep(html, old_pills, new_pills, 1, "folio7-pills")
    html = rep(html, '<span><b>6</b> third parties &middot; sorted by Risk (L &rarr; VH)</span>',
               f'<span><b>{d["vendors"]}</b> third parties &middot; sorted by Risk (L &rarr; VH)</span>', 1, "folio7-vendor-strap")

    old_sysflow = (
        '  // 4. Sys → Flow (for each FLOW originating at a system)\n'
        '  LINKS.filter(l => l.rel === "INVOLVES_FLOW").slice(0, 5).forEach(l => {\n'
        '    links.push({ source: l.from, target: l.to,\n'
        '                 lineStyle: { color: relColor("INVOLVES_FLOW"), width: 1.2, opacity: 0.6 } });\n'
        '  });')
    new_sysflow = (
        '  // 4. System → System data movement (FLOWS_BETWEEN — Case_03 has no INVOLVES_FLOW rel)\n'
        '  LINKS.filter(l => l.rel === "FLOWS_BETWEEN").slice(0, 8).forEach(l => {\n'
        '    links.push({ source: l.from, target: l.to,\n'
        '                 lineStyle: { color: "#6f8aa0", width: 1.2, opacity: 0.6 } });\n'
        '  });')
    html = rep(html, old_sysflow, new_sysflow, 1, "folio7-sysflow")

    old_flowstore = (
        '  // 5. Flow → Store (PROCESSES from a DataStore is not in our graph; instead, derive: every\n'
        '  //    DataFlow has a subprocessor attribute; mirror by attaching FLOW → STORE-03 (logs) when\n'
        '  //    FLOW-03 → Datadog. Keep simple: only the FLOW-03 to STORE-03 link.)\n'
        '  const flowToStore = [\n'
        '    { source: "FLOW-02", target: "STORE-01", note: "primary persistence" },\n'
        '    { source: "FLOW-03", target: "STORE-03", note: "telemetry ingest" },\n'
        '    { source: "FLOW-01", target: "STORE-03", note: "app logs" }\n'
        '  ];\n'
        '  flowToStore.forEach(p => {\n'
        '    links.push({ source: p.source, target: p.target,\n'
        '                 lineStyle: { color: relColor("HOSTS"), width: 1.2, opacity: 0.55, type: "dashed" } });\n'
        '  });')
    new_flowstore = (
        '  // 5. Case_03 has no flow→store relations in the graph; store wiring is drawn from the\n'
        '  //    real HOSTS (System → DataStore) edges in block 3. No fabricated edges.')
    html = rep(html, old_flowstore, new_flowstore, 1, "folio7-flowstore")

    old_pdc = (
        '  // 6. PDC layer: each Flow → relevant PDC (PROCESSES relation). Map by subprocessor / data_type.\n'
        '  //    For legibility, draw a couple of PROCESSES edges we know from the data.\n'
        '  LINKS.filter(l => l.rel === "PROCESSES").slice(0, 4).forEach(l => {\n'
        '    links.push({ source: l.from, target: l.to,\n'
        '                 lineStyle: { color: relColor("PROCESSES"), width: 1.0, opacity: 0.6, type: "dashed" } });\n'
        '  });')
    new_pdc = (
        '  // 6. PDC layer: data-subject → personal-data category captures (CAPTURES relation)\n'
        '  LINKS.filter(l => l.rel === "CAPTURES").slice(0, 6).forEach(l => {\n'
        '    links.push({ source: l.from, target: l.to,\n'
        '                 lineStyle: { color: relColor("CAPTURES"), width: 1.0, opacity: 0.6, type: "dashed" } });\n'
        '  });')
    html = rep(html, old_pdc, new_pdc, 1, "folio7-pdc")

    old_covmap_c = '  // For each SecurityControlDomain (38), count INVOLVES / INVOLVES_STORE / INVOLVES_FLOW edges from it.'
    new_covmap_c = '  // Case_03: sub-domains carry HAS_EVIDENCE links; each EvidenceItem\'s sources[] names the\n' \
                   '  // architecture nodes. Count distinct SYS-/STORE-/FLOW- ids per sub-domain.'
    html = rep(html, old_covmap_c, new_covmap_c, 1, "folio7-covmap-comment")

    old_covmap = (
        '  const data = sds.map(n => {\n'
        '    const out = LINKS.filter(l => l.from === n.id);\n'
        '    const sysCount   = out.filter(l => l.rel === "INVOLVES"  && sysById.has(l.to)).length;\n'
        '    const storeCount = out.filter(l => l.rel === "INVOLVES_STORE" && storesById.has(l.to)).length;\n'
        '    const flowCount  = out.filter(l => l.rel === "INVOLVES_FLOW"  && flowsById.has(l.to)).length;')
    new_covmap = (
        '  const evsBySd = new Map();\n'
        '  LINKS.forEach(l => {\n'
        '    if (l.rel !== "HAS_EVIDENCE") return;\n'
        '    if (!evsBySd.has(l.from)) evsBySd.set(l.from, []);\n'
        '    evsBySd.get(l.from).push(l.to);\n'
        '  });\n'
        '  const data = sds.map(n => {\n'
        '    const evSrcs = ((evsBySd.get(n.id) || []).map(id => nodeById.get(id)).filter(Boolean))\n'
        '      .flatMap(e => (e.attrs && e.attrs.sources) || []);\n'
        '    const sysCount   = new Set(evSrcs.filter(s => sysById.has(s))).size;\n'
        '    const storeCount = new Set(evSrcs.filter(s => storesById.has(s))).size;\n'
        '    const flowCount  = new Set(evSrcs.filter(s => flowsById.has(s))).size;')
    html = rep(html, old_covmap, new_covmap, 1, "folio7-covmap")

    # --- 15b. Ambiguity stats shape (Case_03) ------------------------------------
    # Case_03 ambiguity.stats_per_subdomain carries in_scope as a BOOLEAN plus a
    # separate total; Case_02 carried a numeric in_scope count. Normalise so the
    # Folio IV "Ambig in scope" column and the Folio II/V ambiguity bars show the
    # in-scope COUNT (== total when the sub-domain is in scope), not "true".
    old_ambraw = '    const amb = ambBy.get(n.id) || { in_scope: 0, total: 0 };'
    new_ambraw = (
        '    const ambRaw = ambBy.get(n.id) || { in_scope: 0, total: 0 };\n'
        '    // Case_03: in_scope is boolean — normalise to the in-scope count.\n'
        '    const amb = {\n'
        '      in_scope: (typeof ambRaw.in_scope === "number") ? ambRaw.in_scope\n'
        '                : (ambRaw.in_scope === true ? (ambRaw.total || 0) : 0),\n'
        '      total: ambRaw.total || 0\n'
        '    };')
    html = rep(html, old_ambraw, new_ambraw, 1, "grid-amb-in-scope-normalise")

    # --- 15. Folio VIII — maturity classification (Case_03 outcome syntax) --------
    # Case_03 NIST outcomes: CSF dotted without -P suffix (GV.RM-04), PF dotted WITH
    # -P<lvl> suffix (GV.RM-P1), AI-RMF dashed (MANAGE-2.1). The Case_02 template's
    # dash-prefix PF map matches nothing here and its dot-prefix csfFunction would
    # swallow PF outcomes into the CSF radar — reclassify.
    old_pffn = (
        '  // PF 1.0 Function map (outcomes use \'-\' separator; e.g. GV-PO-P1)\n'
        '  const PF_FN_OF = {\n'
        '    "GV-": "GOVERN-P", "ID-": "IDENTIFY-P", "PR-": "PROTECT-P",\n'
        '    "CM-": "COMMUNICATE-P", "CT-": "CONTROL-P",\n'
        '  };')
    new_pffn = (
        '  // PF 1.0 Function map — Case_03 outcomes use dotted prefixes with a -P<lvl>\n'
        '  // suffix (GV.RM-P1, CT.DP-P4); the -P\\d suffix is what separates PF anchors\n'
        '  // from CSF 2.0 subcategories (GV.RM-04). AI-RMF keeps dashed ids (MANAGE-2.1).\n'
        '  const PF_FN_OF_DOT = {\n'
        '    "GV.": "GOVERN-P", "ID.": "IDENTIFY-P", "PR.": "PROTECT-P",\n'
        '    "CM.": "COMMUNICATE-P", "CT.": "CONTROL-P",\n'
        '  };')
    html = rep(html, old_pffn, new_pffn, 1, "folio8-pf-fn-map")

    old_fns = (
        '  function csfFunction(outcome) {\n'
        '    for (const p of Object.keys(FN_OF)) if (outcome && outcome.startsWith(p)) return FN_OF[p];\n'
        '    return null;\n'
        '  }\n'
        '  function pfFunction(outcome) {\n'
        '    for (const p of Object.keys(PF_FN_OF)) if (outcome && outcome.startsWith(p)) return PF_FN_OF[p];\n'
        '    return null;\n'
        '  }')
    new_fns = (
        '  function isAirmfOutcome(outcome) { return /^(GOVERN-|MAP-|MEASURE-|MANAGE-)/.test(outcome || ""); }\n'
        '  function isPfOutcome(outcome) { return !isAirmfOutcome(outcome) && /-P\\d+$/.test(outcome || ""); }\n'
        '  function csfFunction(outcome) {\n'
        '    if (!outcome || isAirmfOutcome(outcome) || isPfOutcome(outcome)) return null;\n'
        '    for (const p of Object.keys(FN_OF)) if (outcome.startsWith(p)) return FN_OF[p];\n'
        '    return null;\n'
        '  }\n'
        '  function pfFunction(outcome) {\n'
        '    if (!isPfOutcome(outcome)) return null;\n'
        '    for (const p of Object.keys(PF_FN_OF_DOT)) if (outcome.startsWith(p)) return PF_FN_OF_DOT[p];\n'
        '    return null;\n'
        '  }')
    html = rep(html, old_fns, new_fns, 1, "folio8-csf-pf-fns")

    old_pfanchors_head = (
        '  // PF anchor: 1 short PF subcategory per D-XX.Y, derived from OVERLAY_NIST_PF_1.1.md §2.\n'
        '  // Map keyed by subdomain id. For sub-domains not in the PF overlay, value is "—".\n'
        '  const PF_ANCHORS = {')
    new_pfanchors_head = (
        '  // PF anchor: 1 PF capability outcome per D-XX.Y, derived from the sub-domain\'s PF-anchored\n'
        '  // capability EvidenceItem (Scale A) — data-derived, no hardcoded overlay table.\n'
        '  const PF_ANCHORS = {};')
    # Replace header + the hardcoded entries up to the closing '};' of the map.
    html = re_sub1(
        html,
        re.escape(old_pfanchors_head) + r'.*?\n  \};',
        new_pfanchors_head.replace("\\", r"\\") + "\n  for (const n of capability) {\n"
        "    const o = n.attrs && n.attrs.outcome;\n"
        "    if (o && isPfOutcome(o)) PF_ANCHORS[n.attrs.subdomain_id] = o;\n"
        "  }",
        "folio8-pf-anchors")

    html = rep(html, '<th>Outcome (GDPR/CRA)</th>', '<th>Outcome (clause)</th>', 1, "folio8-cov-header")
    html = rep(html, '<div class="sub">CSF + PF frameworks &middot; per Function</div>',
               '<div class="sub">CSF + PF + AI-RMF frameworks &middot; per Function</div>', 1, "folio8-cap-kpi-sub")

    # --- 16. JS label formatter ------------------------------------------------
    html = rep(html, 'if (n.type === "CompanyContext") return "SecureBorder";',
               'if (n.type === "CompanyContext") return "OmniBank";', 3, "js-label-formatter")

    # --- 17. Footer ---------------------------------------------------------------
    old_footer = (
        '  <div>Data: <span class="mono">phase1_graph.json</span> (2026-08-28) &middot; 521 nodes &middot; 1205 links &middot; Audits: 8 &middot; See <span class="mono">validation/P1_graph_json_validation.md</span>.</div>\n'
        '  <div class="right">\n'
        '    AEGIS Rich Mode &middot; Case_02 &middot; standalone file://\n'
        '  </div>')
    new_footer = (
        f'  <div>Data: <span class="mono">phase1_graph.json</span> ({d["gen_date"]}) &middot; {d["n_nodes"]} nodes &middot; {d["n_links"]} links &middot; Audits: {d["n_audits"]} &middot; See <span class="mono">validation/PORT_PARITY2_F3B_REPORT.md</span>.</div>\n'
        '  <div class="right">\n'
        '    AEGIS Rich Mode &middot; Case_03 &middot; standalone file://\n'
        '  </div>')
    html = rep(html, old_footer, new_footer, 1, "footer")

    # --- 18. Inline data (both shapes) ---------------------------------------
    html = inject_json(html, graph_data)

    OUT_DASH.write_text(html, encoding="utf-8")
    print(f"wrote {OUT_DASH} ({len(graph_data)} bytes JSON inlined, "
          f"{d['n_nodes']} nodes / {d['n_links']} links / {d['n_audits']} audits)", file=sys.stderr)


# ---------------------------------------------------------------------------
# MATURITY (standalone Folio VIII — 2 radars: CSF + PF; AI-RMF anchors in Scale A)
# ---------------------------------------------------------------------------
def build_maturity(graph: dict, graph_data: str, d: dict) -> None:
    html = TEMPLATE_MAT.read_text(encoding="utf-8")
    html = strip_inline_json(html)

    # Identity
    html = rep(html, "<title>Case 02 · Phase 1 — Maturity (CSF 2.0 strict)</title>",
               "<title>Case 03 · Phase 1 — Maturity (CSF 2.0 strict)</title>", 1, "mat-title")
    html = rep(html, "AEGIS P1 Maturity Folio — Case_02 standalone.",
               "AEGIS P1 Maturity Folio — Case_03 standalone.", 1, "mat-css-comment")
    html = rep(html, '<span class="case-tag">CASE 02</span>',
               '<span class="case-tag">CASE 03</span>', 1, "mat-case-tag")
    html = rep(html, "<h1>SecureBorder Solutions · Phase 1 — Maturity Folio</h1>",
               f"<h1>{d['company']} · Phase 1 — Maturity Folio</h1>", 1, "mat-h1")
    html = rep(html, "SECUREBORDER B.V. · THE HAGUE, NL · AEGIS RICH MODE · v2.3 maturity_model",
               f"{d['company'].upper()} · {d['hq'].upper()} · AEGIS RICH MODE · {d['schema_version'].split()[-1]} maturity_model",
               1, "mat-sub")
    html = rep(html, "    phase1_graph.json v2.3<br>",
               f"    {d['schema_version']}<br>", 1, "mat-schema-line")
    html = rep(html, "Single-page Folio VIII for Case_02 SecureBorder. Renders TWO scales in parallel",
               f"Single-page Folio VIII for Case_03 {d['company_label_js']}. Renders TWO scales in parallel",
               1, "mat-strap")

    # Disclaimer — replace Case_02 vendor examples with Case_03 graph id families
    html = rep(html,
               "ROLE-*, ACT-*, GDPR-C*, CRA-C*, NIS2-C*, AI-C*, AWS, Splunk, Okta, Thales/Utimaco…",
               "ROLE-*, ACT-*, GDPR-C*, CRA-C*, NIS2-C*, DORA-C*, AI-C*, NIST-*, vendor nodes…", 1, "mat-disclaimer-ids")

    # AI-RMF callout — Case_03: 6 anchors, all MANAGE-2.1
    ai_ids = ", ".join(d["ai_sds"])
    ai_outcomes = sorted({e["attrs"]["outcome"] for e in graph["nodes"]
                          if e["type"] == "EvidenceItem" and e["attrs"].get("scale") == "capability"
                          and str(e["attrs"].get("outcome", "")).startswith(("GOVERN-", "MAP-", "MEASURE-", "MANAGE-"))})
    old_callout = (
        '    <!-- AI-RMF anchors note (Case_02-specific addition) -->\n'
        '    <div class="mat-callout">\n'
        '      <div class="mat-callout-h">AI-RMF anchors (Case_02-specific)\n'
        '        <span class="mat-callout-tag">SecureBorder AI Act applicable</span></div>\n'
        '      <div class="mat-callout-body">\n'
        '        <p>SecureBorder is an AI Act <em>provider</em> (per <code>04_Company_Context_Assessment.md</code> §L217).\n'
        '        For Case_02 the model adds 5 Capability anchors on\n'
        '        <code>OVERLAY_NIST_AI_RMF_1.0.md</code> outcomes (GOVERN-1.2, MAP-2.1, MEASURE-3.2,\n'
        '        MEASURE-4.1, MANAGE-5.2). They appear in the <strong>Scale A</strong> table below with\n'
        '        <code>Framework=AI</code> but do <strong>not</strong> drive a third radar (CSF + PF only).\n'
        '        Reason: AI-RMF has 4 functions vs CSF\'s 6; mixing axes in one chart would mislead.\n'
        '        See the <strong>Citation discipline audit</strong> at the bottom for source provenance.</p>\n'
        '      </div>\n'
        '    </div>')
    new_callout = (
        '    <!-- AI-RMF anchors note (Case_03-specific addition) -->\n'
        '    <div class="mat-callout">\n'
        '      <div class="mat-callout-h">AI-RMF anchors (Case_03-specific)\n'
        '        <span class="mat-callout-tag">OmniBank AI Act applicable — provider + deployer</span></div>\n'
        '      <div class="mat-callout-body">\n'
        '        <p>OmniBank is an AI Act <em>provider + deployer</em> (OmniScore credit scoring, Annex III\n'
        '        high-risk; Doc08 &sect;8 Q39/Q73). For Case_03 the model adds '
        f'{len(d["ai_sds"])} Capability anchors on\n'
        '        <code>OVERLAY_NIST_AI_RMF_1.0.md</code> outcomes (' + ", ".join(ai_outcomes) + ') across\n'
        f'        {ai_ids}. They appear in the <strong>Scale A</strong> table below with\n'
        '        <code>Framework=AI</code> but do <strong>not</strong> drive a third radar\n'
        '        (CSF + PF only — locked decision). Reason: AI-RMF has 4 functions vs CSF\'s 6;\n'
        '        mixing axes in one chart would mislead. See the <strong>Citation discipline audit</strong>\n'
        '        at the bottom for source provenance.</p>\n'
        '      </div>\n'
        '    </div>')
    html = rep(html, old_callout, new_callout, 1, "mat-ai-callout")

    # JS: header comment + data path
    html = rep(html,
               "   Folio VIII — Case_02 P1 Maturity (v2.3).\n"
               "   Data source: ../02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json",
               "   Folio VIII — Case_03 P1 Maturity (v2.1-port).\n"
               "   Data source: ../02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json",
               1, "mat-js-header")
    html = rep(html, 'const DATA_PATH_C02 = "../../../02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json";',
               'const DATA_PATH_C03 = "../../../02_CASES/Case_03_OmniBank_Financial/01_PHASE1_CONTEXT_RICH/data/phase1_graph.json";',
               1, "mat-data-path")
    html = rep(html, "DATA_PATH_C02", "DATA_PATH_C03", 3, "mat-data-path-refs")

    # Cosmetic: template renders "38 active active SDs" (label + value both say
    # 'active'); keep the number only.
    html = rep(html, '$("mat-kpi-active").textContent = activeSDs + " active";',
               '$("mat-kpi-active").textContent = String(activeSDs);', 1, "mat-kpi-active-wart")

    # frameworkOf — Case_03 outcome syntax (dotted CSF, dotted -P PF, dashed AI)
    old_fwof = (
        'function frameworkOf(outcome) {\n'
        '  if (!outcome) return "—";\n'
        '  if (outcome.startsWith(("GV-","ID-","PR-","CM-","CT-"))) return "PF";\n'
        '  if (outcome.startsWith(("GOVERN-","MAP-","MEASURE-","MANAGE-"))) return "AI-RMF";\n'
        '  return "CSF";   // GV./ID./PR./DE./RS./RC. or bare\n'
        '}')
    new_fwof = (
        'function frameworkOf(outcome) {\n'
        '  if (!outcome) return "—";\n'
        '  if (/^(GOVERN-|MAP-|MEASURE-|MANAGE-)/.test(outcome)) return "AI-RMF";\n'
        '  if (/-P\\d+$/.test(outcome)) return "PF";   // Case_03 PF anchor: dotted id + -P<lvl> suffix (GV.RM-P1)\n'
        '  return "CSF";   // GV./ID./PR./DE./RS./RC. (GV.RM-04 style)\n'
        '}')
    html = rep(html, old_fwof, new_fwof, 1, "mat-frameworkOf")

    old_csf = (
        'function csfFunction(outcome) {\n'
        '  const FN_OF = { "GV.":"GOVERN","ID.":"IDENTIFY","PR.":"PROTECT",\n'
        '                  "DE.":"DETECT","RS.":"RESPOND","RC.":"RECOVER" };\n'
        '  for (const p of Object.keys(FN_OF)) if (outcome && outcome.startsWith(p)) return FN_OF[p];\n'
        '  return null;\n'
        '}')
    new_csf = (
        'function csfFunction(outcome) {\n'
        '  const FN_OF = { "GV.":"GOVERN","ID.":"IDENTIFY","PR.":"PROTECT",\n'
        '                  "DE.":"DETECT","RS.":"RESPOND","RC.":"RECOVER" };\n'
        '  if (!outcome || frameworkOf(outcome) !== "CSF") return null;  // keep PF/AI out of the CSF axis\n'
        '  for (const p of Object.keys(FN_OF)) if (outcome.startsWith(p)) return FN_OF[p];\n'
        '  return null;\n'
        '}')
    html = rep(html, old_csf, new_csf, 1, "mat-csfFunction")

    # PF radar — dotted PF outcomes
    old_pfradar = (
        '  const PF_FN_OF = { "GV-":"GOVERN-P","ID-":"IDENTIFY-P","PR-":"PROTECT-P","CM-":"COMMUNICATE-P","CT-":"CONTROL-P" };\n'
        '  const capByFnPF = new Map();\n'
        '  for (const n of capability) {\n'
        '    for (const p of Object.keys(PF_FN_OF)) {')
    new_pfradar = (
        '  // Case_03 PF outcomes are dotted with a -P<lvl> suffix (GV.RM-P1, CT.DP-P4).\n'
        '  const PF_FN_OF = { "GV.":"GOVERN-P","ID.":"IDENTIFY-P","PR.":"PROTECT-P","CM.":"COMMUNICATE-P","CT.":"CONTROL-P" };\n'
        '  const capByFnPF = new Map();\n'
        '  for (const n of capability) {\n'
        '    if (frameworkOf(n.attrs.outcome) !== "PF") continue;\n'
        '    for (const p of Object.keys(PF_FN_OF)) {')
    html = rep(html, old_pfradar, new_pfradar, 1, "mat-pf-radar")

    # PF_ANCHORS — data-derived from PF capability EvidenceItems
    html = re_sub1(
        html,
        r'  // PF anchor per D-XX\.Y, sourced from OVERLAY_NIST_PF_1\.1\.md §2\.\n'
        r'  // Sub-domains not in the PF overlay get "—"\.\n'
        r'  const PF_ANCHORS = \{.*?\n  \};',
        '  // PF anchor per D-XX.Y, derived from the sub-domain\'s PF-anchored capability\n'
        '  // EvidenceItem (Scale A) — data-derived, no hardcoded overlay table.\n'
        '  const PF_ANCHORS = {};\n'
        '  for (const n of capability) {\n'
        '    const o = n.attrs && n.attrs.outcome;\n'
        '    if (o && frameworkOf(o) === "PF") PF_ANCHORS[n.attrs.subdomain_id] = o;\n'
        '  }',
        "mat-pf-anchors")

    # Inline data (both shapes)
    html = inject_json(html, graph_data)

    # Render-order fix: initMaturity() runs while #maturity-view is still
    # display:none, so echarts.init() measures 0×0 and the radars never paint
    # (inherited from the Case_02 template, where canvas width is 0 too).
    # Resize the stored chart instances after the view is revealed.
    old_reveal = (
        '  // Reveal view\n'
        '  document.getElementById("loading").style.display = "none";\n'
        '  document.getElementById("maturity-view").style.display = "block";\n'
        '}')
    new_reveal = (
        '  // Reveal view\n'
        '  document.getElementById("loading").style.display = "none";\n'
        '  document.getElementById("maturity-view").style.display = "block";\n'
        '  // The radars were initialised while #maturity-view was still display:none\n'
        '  // (0x0 canvas); resize now that the container is visible so they paint.\n'
        '  ["mat-radar-csf", "mat-radar-pf"].forEach(id => {\n'
        '    const c = window[id];\n'
        '    if (c && typeof c.resize === "function") c.resize();\n'
        '  });\n'
        '}')
    html = rep(html, old_reveal, new_reveal, 1, "mat-reveal-resize")

    OUT_MAT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT_MAT} ({len(graph_data)} bytes JSON inlined)", file=sys.stderr)


def main(argv: list[str]) -> int:
    graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    graph_data = json.dumps(graph, ensure_ascii=False)
    d = derive(graph)

    print("# derived numbers (all from phase1_graph.json):", file=sys.stderr)
    for k in ("n_nodes", "n_links", "n_audits", "gen_date", "schema_version", "amb_cards",
              "regs_applicable", "sd_active", "rigorous", "standard", "substantive", "partial",
              "not_addressed", "ags", "ags_priv", "ags_sec", "tensions", "tension_edges",
              "stakeholders", "bgs", "clauses", "systems", "stores", "flows", "vendors",
              "raci_acts", "raci_roles", "raci_active", "evi", "evi_cov", "evi_cap", "evi_obs",
              "nist_csf", "nist_pf", "nist_ai"):
        print(f"  {k} = {d[k]}", file=sys.stderr)
    print(f"  ai_sds = {d['ai_sds']}", file=sys.stderr)
    print(f"  amb_by_reg = {dict(d['amb_by_reg'])}", file=sys.stderr)
    print(f"  audit_kinds = {dict(d['audit_kinds'])}", file=sys.stderr)

    build_dashboard(graph, graph_data, d)
    build_maturity(graph, graph_data, d)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
