#!/usr/bin/env python3
"""build_master_dashboard_data.py — AEGIS Master Dashboard data layer.

Parses the corpus (Phase 1/2/3 artefacts of the 3 cases) into a single JSON
document that powers UNIFIED/AEGIS_Master_Dashboard.html. The JSON is a
DERIVED VIEW: generated from the documents, never hand-maintained.

Usage:
  python3 scripts/build_master_dashboard_data.py                 # write data/aegis_master_data.json
  python3 scripts/build_master_dashboard_data.py --dry-run       # validate parsing, no write
  python3 scripts/build_master_dashboard_data.py --inject PATH   # also inject into an HTML template
                                                                 # (replaces the literal `/*__MASTER_DATA__*/null`)

stdlib-only. Deterministic ordering. Missing sources -> null + warnings[].
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DEFAULT = REPO / "00_METHODOLOGY" / "00_VISUALISATIONS" / "data" / "aegis_master_data.json"
AUDIT_REPORT = REPO / "00_METHODOLOGY" / "validation" / "TRACEABILITY_AUDIT_2026-09-05.md"

CASES = {
    "Case_01_TinyTask_SaaS": {
        "root": "02_CASES/Case_01_TinyTask_SaaS",
        "p3_dir": "03_PHASE3_DECOMPOSITION_RICH",
        "catalog": "03_PHASE3_DECOMPOSITION_RICH/Doc20_Use_Cases_Catalog.md",
        "lane_cards": "03_PHASE3_DECOMPOSITION_RICH/Doc32_Process_Capability_Cards.md",
        "regs": ["GDPR", "CRA"],
        "tier": "Low",
        "product_section": r"## §2 Functional",
        "compliance_section": r"## §3 Security",
    },
    "Case_02_SecureBorder_Solutions": {
        "root": "02_CASES/Case_02_SecureBorder_Solutions",
        "p3_dir": "03_PHASE3_DECOMPOSITION",
        "catalog": "03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md",
        "lane_cards": "03_PHASE3_DECOMPOSITION/Doc31_Process_Capability_Cards.md",
        "regs": ["GDPR", "CRA", "NIS 2", "AI Act"],
        "tier": "High",
        "product_section": r"## 6\. PRODUCT",
        "compliance_section": r"## 7\. DOMAIN DECOMPOSITION",
    },
    "Case_03_OmniBank_Financial": {
        "root": "02_CASES/Case_03_OmniBank_Financial",
        "p3_dir": "03_PHASE3_DECOMPOSITION",
        "catalog": "03_PHASE3_DECOMPOSITION/Doc22_Use_Cases_Catalog.md",
        "lane_cards": "03_PHASE3_DECOMPOSITION/Doc32_Process_Capability_Cards.md",
        "regs": ["GDPR", "CRA", "NIS 2", "DORA", "AI Act"],
        "tier": "Maximum",
        "product_section": r"## 4\. PRODUCT",
        "compliance_section": r"## 3\. COMPLIANCE",
    },
}

# NIST CSF 2.0 functions (case-insensitive lookup; canonical order)
CSF_FUNCTIONS = ["Govern", "Identify", "Protect", "Detect", "Respond", "Recover"]
CSF_FUNCTION_KEYS = {
    "govern": "Govern", "gv": "Govern",
    "identify": "Identify", "id": "Identify",
    "protect": "Protect", "pr": "Protect",
    "detect": "Detect", "de": "Detect",
    "respond": "Respond", "rs": "Respond",
    "recover": "Recover", "rc": "Recover",
}

# AEGIS sub-domain -> NIST CSF 2.0 function (deterministic crosswalk
# anchored to 00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/NIST_AI_RMF
# + 00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md §3 and the 38 sub-domain
# mapping table in 00_METHODOLOGY/PREPROCESSING_by_domain/domains/index.md).
SUBDOMAIN_TO_CSF = {
    # D-01 Data Protection & Encryption -> Protect (PR.DS family)
    "D-01.1": "Protect", "D-01.2": "Protect", "D-01.3": "Protect", "D-01.4": "Protect",
    # D-02 Vulnerability & Patch Management -> Identify (ID.RA family)
    "D-02.1": "Identify", "D-02.2": "Identify", "D-02.3": "Identify", "D-02.4": "Identify",
    # D-03 IAM -> Protect (PR.AA family)
    "D-03.1": "Protect", "D-03.2": "Protect", "D-03.3": "Protect", "D-03.4": "Protect",
    # D-04 Incident Response / Detection / Recovery
    "D-04.1": "Detect", "D-04.2": "Respond", "D-04.3": "Respond", "D-04.4": "Recover",
    # D-05 Data Lifecycle -> Govern (data governance family)
    "D-05.1": "Govern", "D-05.2": "Govern", "D-05.3": "Govern", "D-05.4": "Govern",
    # D-06 Supply Chain / Third-Party -> Govern
    "D-06.1": "Govern", "D-06.2": "Govern", "D-06.3": "Govern", "D-06.4": "Govern",
    # D-07 Secure Development -> Protect (PR.PS family)
    "D-07.1": "Protect", "D-07.2": "Protect", "D-07.3": "Protect", "D-07.4": "Protect",
    # D-08 Training & Awareness -> Govern (GV.OC family)
    "D-08.1": "Govern", "D-08.2": "Govern", "D-08.3": "Govern", "D-08.4": "Govern",
    # D-09 Governance & Risk -> Govern
    "D-09.1": "Govern", "D-09.2": "Identify", "D-09.3": "Govern",
    "D-09.4": "Govern", "D-09.5": "Govern",
    # D-10 Audit Logging / Monitoring -> Detect (DE.CM / DE.AE family)
    "D-10.1": "Detect", "D-10.2": "Detect", "D-10.3": "Detect", "D-10.4": "Detect",
}

# Hardcoded referential framework list (NOT invented content; these are
# versioned external standards referenced by AEGIS cases).
FRAMEWORKS_REF = [
    {"name": "NIST CSF 2.0", "version": "2.0 (2024-02-26)", "path": "00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAYS/OVERLAY_NIST_CSF_2.0.md"},
    {"name": "NIST SP 800-53r5", "version": "Rev 5 (2020-09-23)", "path": "00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/NIST_800-53r5/"},
    {"name": "OWASP ASVS", "version": "4.0.3", "path": "00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAYS/"},
    {"name": "OWASP SAMM", "version": "2.0", "path": "00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAYS/"},
    {"name": "ISO 27002", "version": "2022", "path": "00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAYS/"},
    {"name": "QNRCS Reg 756/2026", "version": "2026-01-01", "path": "00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAYS/OVERLAY_QNRCS_756_2026.md"},
]

# QNRCS / AEGIS dashboard references (stable referentials, not invented content)
QNRCS_RESOURCES = [
    {"id": "QNRCS-756-2026", "title": "Quadro Nacional de Referência para a Cibersegurança (Reg. 756/2026)", "url": "00_METHODOLOGY/PREPROCESSING_by_domain/MAPPINGS/OVERLAYS/OVERLAY_QNRCS_756_2026.md"},
    {"id": "AEGIS-MASTER", "title": "AEGIS Master Dashboard", "url": "00_METHODOLOGY/00_VISUALISATIONS/UNIFIED/AEGIS_Master_Dashboard.html"},
    {"id": "AEGIS-KG-E3", "title": "AEGIS Knowledge Graph (Build E3)", "url": "kg/E3_2026-08-23/graphify-out/graph.html"},
    {"id": "CSF-STRICT", "title": "Maturity Model (CSF Strict v1.0)", "url": "00_METHODOLOGY/MATURITY_MODEL_CSF_STRICT.md"},
]

# Per-case doc-naming conventions for P2 (objectives/obligations/tensions) and P3.
DOC_P2_OBJECTIVES = {
    "Case_01_TinyTask_SaaS": "Doc16_Privacy_Security_Objectives.md",
    "Case_02_SecureBorder_Solutions": "Doc16_Privacy_Security_Goals.md",
    "Case_03_OmniBank_Financial": "Doc17_Privacy_Security_Objectives.md",
}
DOC_P2_OBLIGATIONS = {
    "Case_01_TinyTask_SaaS": "Doc14_Obligation_Derivation.md",
    "Case_02_SecureBorder_Solutions": "Doc14_Obligation_Derivation.md",
    "Case_03_OmniBank_Financial": "Doc15_Obligation_Derivation.md",
}
DOC_P2_TENSIONS = {
    "Case_01_TinyTask_SaaS": "Doc15_Strategic_Tensions_Report.md",
    "Case_02_SecureBorder_Solutions": "Doc15_Strategic_Tensions_Report.md",
    "Case_03_OmniBank_Financial": "Doc16_Strategic_Tensions_Report.md",
}
DOC_P1_AMBIGUITY = "Doc09_Ambiguity_Register.md"

# Per-case P3 doc-naming (filenames differ between C1 RICH and C2/C3)
def doc_p3_paths(case, cfg):
    p3 = cfg["p3_dir"]
    root = cfg["root"]
    if case == "Case_01_TinyTask_SaaS":
        return {
            "gates": f"{root}/{p3}/Doc25_Compliance_Gates_Report.md",
            "risks": f"{root}/{p3}/Doc27_Risk_Analysis.md",
            "alloc": f"{root}/{p3}/Doc24_Requirements_Allocation.md",
            "ftree": f"{root}/{p3}/Doc26_Functional_Tree.md",
            "fr":    f"{root}/{p3}/requirements/Doc29_Functional_Requirements.md",
            "nfr":   f"{root}/{p3}/requirements/Doc31_Non_Functional_Requirements.md",
        }
    if case == "Case_02_SecureBorder_Solutions":
        return {
            "gates": f"{root}/{p3}/Doc26_Compliance_Gates_Report.md",
            "risks": f"{root}/{p3}/Doc28_Risk_Analysis.md",
            "alloc": f"{root}/{p3}/Doc25_Requirements_Allocation.md",
            "ftree": f"{root}/{p3}/Doc27_Functional_Tree.md",
            "fr":    f"{root}/{p3}/requirements/Doc29_Functional_Requirements.md",
            "nfr":   f"{root}/{p3}/requirements/Doc30_Non_Functional_Requirements.md",
        }
    # Case_03
    return {
        "gates": f"{root}/{p3}/Doc27_Compliance_Gates_Report.md",
        "risks": f"{root}/{p3}/Doc29_Risk_Analysis.md",
        "alloc": f"{root}/{p3}/Doc26_Requirements_Allocation.md",
        "ftree": f"{root}/{p3}/Doc28_Functional_Tree.md",
        "fr":    f"{root}/{p3}/requirements/Doc30_Functional_Requirements.md",
        "nfr":   f"{root}/{p3}/requirements/Doc31_Non_Functional_Requirements.md",
    }


def read(rel):
    p = REPO / rel
    if not p.exists():
        return None
    return p.read_text(encoding="utf-8")


def glob_first(root_rel, pattern):
    hits = sorted((REPO / root_rel).rglob(pattern))
    return str(hits[0].relative_to(REPO)) if hits else None


def frontmatter(text):
    if not text:
        return {}
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    out = {}
    if m:
        for line in m.group(1).split("\n"):
            if ":" in line:
                k, _, v = line.partition(":")
                out[k.strip()] = v.strip().strip('"')
    return out


def cut_sections(text):
    """Split a document into (heading, body) chunks at ## level."""
    chunks, cur_h, cur = [], None, []
    for line in (text or "").split("\n"):
        if re.match(r"^## ", line):
            chunks.append((cur_h, "\n".join(cur)))
            cur_h, cur = line, []
        else:
            cur.append(line)
    chunks.append((cur_h, "\n".join(cur)))
    return chunks


def infer_regulation_from_clause_id(clause_id):
    """Best-effort regulation inference from corpus clause ID prefix.

    Mapping is deterministic and anchored to AEGIS ID conventions:
    GDPR_/GDPR-*  -> GDPR,  CRA_/CRA-*  -> CRA,  NIS2_/NIS-*  -> NIS 2,
    DORA_/DORA-*  -> DORA,  AI_ACT_/AI-Act/AI_ACT -> AI Act,
    QNRCS_*       -> QNRCS,  CR_/OBL_/AG_/PO_/SO_/QNRCS_ need Doc09 fallback.
    """
    if not clause_id:
        return None
    cid = clause_id.upper()
    if cid.startswith("GDPR"):
        return "GDPR"
    if cid.startswith("CRA"):
        return "CRA"
    if cid.startswith("NIS2") or cid.startswith("NIS"):
        return "NIS 2"
    if cid.startswith("DORA"):
        return "DORA"
    if cid.startswith("AI-ACT") or cid.startswith("AI_ACT"):
        return "AI Act"
    if cid.startswith("QNRCS"):
        return "QNRCS"
    return None


def _norm_csf_function(value):
    """Map a string (from ontology/CSV/JSON) onto the canonical CSF function name."""
    if not value:
        return None
    v = str(value).strip()
    v_clean = re.sub(r"[-_]+", "", v).lower()
    # Direct canonical
    for canon in CSF_FUNCTIONS:
        if v_clean == canon.lower():
            return canon
    # Short codes & punctuation variants
    return CSF_FUNCTION_KEYS.get(v_clean, None)


# ---------------------------------------------------------------------------
# Realization-class heuristic (deterministic, fallback only).
#
# The REALIZATION-CLASS campaign (rubric 00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md
# §2 closed enum {TECHNOLOGY, PROCESS, CAPABILITY}; campaign commits 762c095,
# 599a8ba, 113ba05 on 2026-09-05) tags rules explicitly in Case_01 control_set.yaml.
# For Case_02/Case_03 the YAMLs are generated and the field is parked per ledger
# §2 (phase2_ontology.yaml application is on the P7 queue, frozen). The dashboard
# needs honest numbers NOW without authoring new content, so we apply a
# deterministic derivation anchored to the campaign decisions and rubric §8
# worked examples (CR-D-08.1-001 / CR-D-08.2-001 CAPABILITY; CR-D-01.1-001 /
# CR-D-03.2-001 TECHNOLOGY; CR-D-04.3-001 PROCESS).
#
# Existing YAML tags (when present) ALWAYS take precedence; the heuristic is the
# fallback only — the rule-level "_heuristic" flag and the case-level "rc_source"
# string expose the provenance so the dashboard can render it.
# ---------------------------------------------------------------------------
RC_HEURISTIC_GOVERNANCE = {"D-09.1", "D-09.2", "D-09.3", "D-09.4", "D-09.5"}
RC_HEURISTIC_DATA_PROT_TECH = {"D-01.1", "D-01.2", "D-01.3"}
RC_HEURISTIC_VULN_DEV = "D-02."      # CR-D-02.* -> PROCESS (patching pipelines with
                                     # constitutive human triage; rubric §8 borderline 1)
RC_HEURISTIC_IAM = "D-03."          # CR-D-03.* -> TECHNOLOGY (enforced at IdP)
RC_HEURISTIC_SECDEV_GATES = "D-07." # CR-D-07.* -> PROCESS
RC_HEURISTIC_INCIDENT_NOTIFY = "D-04.3"  # CR-D-04.3 -> PROCESS (workflow with SLA clocks)


def derive_realization_class(rule_entry):
    """Derive (class, heuristic_flag) for a control_set entry lacking realization_class.

    Returns (class_string, True) when the heuristic decides; returns (existing_class, False)
    when the YAML already carries the field (caller should not normally call this in that
    case, but the check is defensive). class_string is one of TECHNOLOGY|PROCESS|CAPABILITY.

    Heuristic precedence (first match wins):
      1. D-08.*                       -> CAPABILITY  (training/competence = standing ability)
      2. D-09.1..D-09.5               -> CAPABILITY  (governance rules)
      3. D-01.1 / D-01.2 / D-01.3     -> TECHNOLOGY  (data protection via artefact property)
      4. D-04.3                       -> PROCESS     (incident notification SLA workflow)
      5. BPR-* prefix                 -> PROCESS     (best practice = coordinated activity)
      6. CR-D-02.* (vuln/secdev)      -> PROCESS     (patching pipelines + human triage)
      7. CR-D-03.* (IAM)              -> TECHNOLOGY  (enforced at the IdP)
      8. CR-D-07.* (secdev gates)     -> PROCESS
      9. else                         -> PROCESS     (safe default; _heuristic flag set)

    Anchored to REALIZATION-CLASS campaign commits 762c095 / 599a8ba / 113ba05 (2026-09-05)
    and rubric §8 worked examples. See 00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md §2.
    """
    rid = (rule_entry.get("id") or "").strip()
    sub = (rule_entry.get("sub_domain") or "").strip()
    # 1. Training / competence — standing ability (rubric §8: CR-D-08.1/08.2-001)
    if sub.startswith("D-08."):
        return ("CAPABILITY", True)
    # 2. Governance rules (rubric §8: CR-D-09.1-001 / CR-D-09.2-001)
    if sub in RC_HEURISTIC_GOVERNANCE:
        return ("CAPABILITY", True)
    # 3. Data protection built into the artefact (rubric §8: CR-D-01.1-001)
    if sub in RC_HEURISTIC_DATA_PROT_TECH:
        return ("TECHNOLOGY", True)
    # 4. Incident notification workflow with SLA clocks (rubric §8: CR-D-04.3-001)
    if sub == RC_HEURISTIC_INCIDENT_NOTIFY:
        return ("PROCESS", True)
    # 5. Best-practice rules are coordinated activities by definition
    if rid.startswith("BPR-"):
        return ("PROCESS", True)
    # 6. Vulnerability / secure development pipelines (rubric §8 borderline 1: CR-D-02.2-001)
    if rid.startswith("CR-") and sub.startswith(RC_HEURISTIC_VULN_DEV):
        return ("PROCESS", True)
    # 7. IAM enforced at the IdP, automated tests (rubric §8: CR-D-03.2-001)
    if rid.startswith("CR-") and sub.startswith(RC_HEURISTIC_IAM):
        return ("TECHNOLOGY", True)
    # 8. Secure-development gates are coordinated workflows
    if rid.startswith("CR-") and sub.startswith(RC_HEURISTIC_SECDEV_GATES):
        return ("PROCESS", True)
    # 9. Safe default
    return ("PROCESS", True)


# ---------------------------------------------------------------------------
# R0.1 — Ambiguity, citations, ambiguity_rows
# ---------------------------------------------------------------------------
def parse_ambiguity(case, cfg, warn):
    """Derive ambiguity, citations, ambiguity_rows for a case.

    Sources (in priority order):
      1. phase1_graph.json:ambiguity (richer: by_severity, by_regulation, top_cards)
      2. Doc09_Ambiguity_Register.md (markdown fallback / cross-check)
    """
    out = {"ambiguity": None, "citations": None, "ambiguity_rows": []}
    cards_in_scope_graph = None
    # --- graph.json ---
    g = glob_first(cfg["root"], "phase1_graph.json")
    if g:
        try:
            gd = json.loads(read(g))
            amb = gd.get("ambiguity", {}) or {}
            stats_total = amb.get("stats_total", {}) or {}
            by_sev = stats_total.get("by_severity") or amb.get("by_severity") or {}
            by_reg = stats_total.get("by_regulation") or amb.get("by_regulation") or {}
            cards_in_scope_graph = stats_total.get("cards_in_scope") or amb.get("cards_in_scope")
            s1 = int(by_sev.get("S1", 0) or 0)
            s2 = int(by_sev.get("S2", 0) or 0)
            s3 = int(by_sev.get("S3", 0) or 0)
            # Prefer `cards_in_scope` as the authoritative open count (the
            # corpus caps ambiguity cards at in-scope subdomains; the severity
            # breakdown may double-count). Fall back to sev_sum when absent.
            sev_sum = s1 + s2 + s3
            if cards_in_scope_graph is not None:
                open_total = int(cards_in_scope_graph)
            elif sev_sum > 0:
                open_total = sev_sum
            else:
                open_total = 0
            high = s1  # S1 = high (per AEGIS S1/S2/S3 convention: S1 high, S2 medium, S3 low)
            if open_total or by_reg or sev_sum:
                out["ambiguity"] = {
                    "open": open_total,
                    "high": high,
                    "by_regulation": by_reg,
                    "by_severity": by_sev,
                }
            # top_cards -> ambiguity_rows
            for tc in (amb.get("top_cards") or [])[:50]:
                cid = tc.get("corpus_clause_id") or tc.get("clause_id") or ""
                row = {
                    "id": cid,
                    "regulation": infer_regulation_from_clause_id(cid) or tc.get("regulation") or "",
                    "provision": tc.get("article") or "",
                    "ambiguity": tc.get("type") or "",
                    "severity": tc.get("severity") or "",
                    "status": tc.get("status") or "OPEN",
                    "citation": tc.get("source") or "",
                }
                out["ambiguity_rows"].append(row)
        except json.JSONDecodeError:
            warn.append(f"{case}: {g} unparsable")
    else:
        warn.append(f"{case}: phase1_graph.json not found")

    # --- Doc09 fallback (counts, citation index) ---
    doc09_rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{DOC_P1_AMBIGUITY}"
    t = read(doc09_rel)
    if t:
        # Severity rows in Doc09 (markdown table with | S1 | etc.)
        sev_rows = re.findall(r"^\|\s*(S[123])\s*\|", t, re.M)
        if not out["ambiguity"] and sev_rows:
            s1 = sum(1 for s in sev_rows if s == "S1")
            s2 = sum(1 for s in sev_rows if s == "S2")
            s3 = sum(1 for s in sev_rows if s == "S3")
            by_reg = {}
            for key in ("gdpr", "cra", "dora", "nis2", "ai_act", "ai-act"):
                mm = re.search(rf"ambiguity_cards_{re.escape(key)}\s*:\s*(\d+)", t, re.I)
                if mm:
                    reg_name = {"gdpr": "GDPR", "cra": "CRA", "dora": "DORA",
                                "nis2": "NIS 2", "ai_act": "AI Act", "ai-act": "AI Act"}.get(key, key)
                    by_reg[reg_name] = int(mm.group(1))
            out["ambiguity"] = {
                "open": s1 + s2 + s3,
                "high": s1,
                "by_regulation": by_reg,
                "by_severity": {"S1": s1, "S2": s2, "S3": s3},
            }
        # Citations: count article refs and bullet entries in Doc09 itself
        arts = set(re.findall(r"Art\.\s*\d+[a-z]?(?:\([0-9a-z]+\))?", t))
        # Count detail cards (## Card #N headings or §3 entries)
        card_count = (len(re.findall(r"^### Card\s*#?\d+", t, re.M))
                      + len(re.findall(r"^####\s+Card\s*#?\d+", t, re.M))
                      + len(re.findall(r"^\s*\| Card #\d+", t, re.M)))
        if card_count == 0:
            # Fallback: count §3 sections (one per in-scope subdomain × top cards)
            card_count = len(out["ambiguity_rows"]) or 1
        out["citations"] = {"count": card_count, "unique_articles": len(arts)}
    else:
        warn.append(f"{case}: Doc09_Ambiguity_Register.md missing")
    if out["ambiguity"] is None and cards_in_scope_graph is not None:
        out["ambiguity"] = {"open": int(cards_in_scope_graph), "high": 0,
                            "by_regulation": {}, "by_severity": {}}
    if out["citations"] is None:
        out["citations"] = {"count": 0, "unique_articles": 0}
    return out


# ---------------------------------------------------------------------------
# R0.2 — Maturity (NIST CSF 2.0 radar)
# ---------------------------------------------------------------------------
def parse_maturity(case, cfg, warn):
    """Compute NIST CSF 2.0 maturity radar from phase1_ontology.compact.json.

    Scoring formula (deterministic, documented here per R0.2):
        evidence_count = number of EvidenceItem nodes with csf_function F
        if evidence_count == 0: score = 0
        else: score = min(4, round(sqrt(evidence_count) * 2))
    Scale A: T1=Initial, T2=Repeatable, T3=Adaptive (defined), T4=Adaptive (managed).
    Cap at 4.
    """
    labels = list(CSF_FUNCTIONS)
    target = [4] * 6
    current = [0] * 6
    function_coverage = {f: 0 for f in labels}
    evidence_cells = []

    ont_rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/data/phase1_ontology.compact.json"
    ont = None
    ont_p = REPO / ont_rel
    if ont_p.exists():
        try:
            ont = json.loads(ont_p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            warn.append(f"{case}: phase1_ontology.compact.json unparsable")
            ont = None
    else:
        # Not all cases ship the compact sibling (yaml only)
        ont = None

    # Pull evidence from graph nodes (most reliable: EvidenceItem nodes
    # have csf_function in attrs; the graph also has NistControl/TierDecision
    # nodes which we cross-check).
    g = glob_first(cfg["root"], "phase1_graph.json")
    ev_items = []
    if g:
        try:
            gd = json.loads(read(g))
            for n in gd.get("nodes", []):
                if n.get("type") == "EvidenceItem":
                    ev_items.append(n)
        except json.JSONDecodeError:
            pass

    for ev in ev_items:
        attrs = ev.get("attrs", {}) or {}
        fn_raw = (attrs.get("csf_function")
                  or attrs.get("function")
                  or "")
        fn = _norm_csf_function(fn_raw)
        scale = attrs.get("scale") or ""
        ev_id = attrs.get("ev_id") or ev.get("id") or ""
        # Subdomain -> CSF function crosswalk (deterministic fallback;
        # the csf_function attr is often absent on the EvidenceItem node).
        sub = attrs.get("subdomain_id") or ""
        if not fn and sub in SUBDOMAIN_TO_CSF:
            fn = SUBDOMAIN_TO_CSF[sub]
        if fn and fn in function_coverage:
            function_coverage[fn] += 1
        evidence_cells.append({
            "id": ev_id,
            "function": fn or "",
            "type": (ev.get("type") or "EvidenceItem"),
            "scale": scale,
            "status": "OBSERVED" if attrs.get("observed") else "PENDING",
        })

    # Compute scores with documented formula
    import math
    for i, fn in enumerate(labels):
        c = function_coverage.get(fn, 0)
        if c == 0:
            current[i] = 0
        else:
            current[i] = min(4, round(math.sqrt(c) * 2))

    return {
        "labels": labels,
        "current": current,
        "target": target,
        "evidence_cells": evidence_cells[:10],
        "function_coverage": function_coverage,
    }


# ---------------------------------------------------------------------------
# R0.3 — Full graph nodes/links
# ---------------------------------------------------------------------------
def parse_graph_full(case, cfg, warn):
    """Return full nodes/links arrays from phase1_graph.json (truncated at 5000 links)."""
    g = glob_first(cfg["root"], "phase1_graph.json")
    if not g:
        warn.append(f"{case}: phase1_graph.json not found")
        return {"nodes": [], "links": []}
    try:
        gd = json.loads(read(g))
    except json.JSONDecodeError:
        warn.append(f"{case}: {g} unparsable")
        return {"nodes": [], "links": []}
    nodes = []
    for n in gd.get("nodes", []) or []:
        nodes.append({
            "id": n.get("id"),
            "type": n.get("type"),
            "label": n.get("label"),
            "lane": n.get("lane"),
            "attrs": n.get("attrs", {}) or {},
        })
    links = []
    raw_links = gd.get("links", []) or []
    for l in raw_links[:5000]:
        links.append({
            "from": l.get("from"),
            "to": l.get("to"),
            "rel": l.get("rel"),
            "attrs": l.get("attrs", {}) or {},
        })
    return {"nodes": nodes, "links": links}


def parse_p2_graph(case, cfg, warn):
    """Derive p2.graph from control_set.yaml.

    nodes: each control (controls[].id) -> a node.
    links: trace.dependencies / trace.phase1 / trace.objectives / trace.obligations
           -> one link per reference, rel = field name.
    Cap nodes at 200, links at 500.
    """
    nodes = []
    links = []
    cs = glob_first(cfg["root"], "control_set.yaml")
    if not cs:
        warn.append(f"{case}: control_set.yaml not found (p2.graph)")
        return {"nodes": nodes, "links": links}
    t = read(cs)
    # Each control block: parse id, domain, trace.{phase1,obligations,objectives,dependencies}
    # We use a coarse but robust block parser anchored on "- id:".
    # Strategy: split on lines beginning with "  - id:" (control entries);
    # 4-space indent + quoted ids also accepted (C2/C3 generated YAMLs).
    blocks = re.split(r"(?m)^(?=\s*-?\s*id:\s*\"?[A-Z])", t)
    for b in blocks:
        m_id = re.search(r"^\s*-?\s*id:\s*\"?([A-Z]{2,}-D-[\d.]+-\d+|BPR-[\w.-]+)\"?", b, re.M)
        if not m_id:
            continue
        if len(nodes) >= 200:
            break
        cid = m_id.group(1)
        m_dom = re.search(r"^\s*-?\s*(?:sub_)?domain:\s*\"?([D]-[\d.]+)\"?", b, re.M)
        m_title = re.search(r"^\s*-?\s*title:\s*\"?([^\"\n]+)\"?", b, re.M)
        if not m_title:
            m_title = re.search(r"^\s*-?\s*description:\s*\"?([^\"\n]+)\"?", b, re.M)
        nodes.append({
            "id": cid,
            "type": "RULE",
            "label": m_title.group(1).strip() if m_title else cid,
            "attrs": {"sub_domain": m_dom.group(1) if m_dom else ""},
        })
        # trace relations (C1: nested trace.{phase1,obligations,objectives,dependencies})
        for rel_name in ("phase1", "obligations", "objectives", "dependencies"):
            m = re.search(rf"^\s*{rel_name}:\s*\n((?:\s*-\s*[^\n]+\n?)+)", b, re.M)
            if m:
                for tgt in re.findall(r"-\s*\"?([A-Za-z0-9][\w.-]*)\"?", m.group(1)):
                    if len(links) < 500:
                        links.append({"from": cid, "to": tgt, "rel": rel_name, "attrs": {}})
        # C2/C3 fallback: single string fields (related_goals / traceability)
        for rel_name in ("related_goals", "traceability"):
            m = re.search(rf"^\s*{rel_name}:\s*\"?([^\"\n]+)\"?", b, re.M)
            if m:
                for tgt in re.findall(r"\b(?:PO|SO|OBL|AG|CR|BPR)-D-[\d.]+(?:-[\w.-]+)?\b", m.group(1)):
                    if len(links) < 500:
                        links.append({"from": cid, "to": tgt, "rel": rel_name, "attrs": {}})
    return {"nodes": nodes, "links": links}


def parse_p3_graph(case, cfg, warn, catalog, lane):
    """Derive p3.graph from use_cases + lane_cards.

    nodes: each UC, PROC, CAP -> a node.
    links: cross-references (PROC/CAP -> UC where "Related Rules" mentions the
           UC, etc). Here we emit a thin set: PROC/CAP -> use_case mentioned
           in the catalog text body, plus UC -> package parent.
    """
    nodes = []
    links = []
    # UC nodes
    for u in catalog.get("ucs", []) or []:
        nodes.append({
            "id": u.get("id"),
            "type": "UC",
            "label": u.get("title") or u.get("id"),
            "attrs": {"package": u.get("package") or ""},
        })
    # PROC / CAP nodes
    for p in lane.get("proc", []) or []:
        nodes.append({
            "id": p.get("id"),
            "type": "PROC",
            "label": p.get("title") or p.get("id"),
            "attrs": {"fields": {k: p.get(k) for k in ("Owner", "Maturity", "Realises", "Anchors") if p.get(k)}},
        })
    for c in lane.get("cap", []) or []:
        nodes.append({
            "id": c.get("id"),
            "type": "CAP",
            "label": c.get("title") or c.get("id"),
            "attrs": {"fields": {k: c.get(k) for k in ("Owner", "Maturity", "Realises", "Anchors") if c.get(k)}},
        })
    # Edges: PROC/CAP Realises / Anchors -> related CR/UC IDs in attributes
    for kind in ("proc", "cap"):
        for c in lane.get(kind, []) or []:
            for field in ("Realises", "Anchors"):
                v = c.get(field) or ""
                for tgt in re.findall(r"\b(?:UC-\d+|CR-D-[\d.]+-\d+|BPR-[\w.-]+|PROC-\d+|CAP-\d+)\b", v):
                    links.append({"from": c.get("id"), "to": tgt, "rel": field.upper(),
                                  "attrs": {}})
    # Edges: UC -> package parent
    for u in catalog.get("ucs", []) or []:
        if u.get("package"):
            links.append({"from": u.get("id"), "to": u["package"], "rel": "IN_PACKAGE",
                          "attrs": {}})
    # Cap at 500 edges
    if len(links) > 500:
        links = links[:500]
    return {"nodes": nodes, "links": links}


# ---------------------------------------------------------------------------
# P1 parser (extended)
# ---------------------------------------------------------------------------
def parse_p1(case, cfg, warn):
    status = {}
    pj = read(f"{cfg['root']}/progress.json")
    if pj:
        try:
            data = json.loads(pj)
            for k, v in (data.get("phases") or {}).items():
                status[k] = {x: v.get(x) for x in ("status", "gate", "completed_at")}
        except json.JSONDecodeError:
            warn.append(f"{case}: progress.json unparsable")
    else:
        warn.append(f"{case}: progress.json missing")
    # Graph counts (existing) + full nodes/links (R0.3)
    g = glob_first(cfg["root"], "phase1_graph.json")
    nodes_count = links_count = None
    if g:
        try:
            gd = json.loads(read(g))
            nodes_count, links_count = len(gd.get("nodes", [])), len(gd.get("links", []))
        except json.JSONDecodeError:
            warn.append(f"{case}: {g} unparsable")
    else:
        warn.append(f"{case}: phase1_graph.json not found")
    graph_full = parse_graph_full(case, cfg, warn)
    # Ontology counts
    o = glob_first(cfg["root"], "phase1_ontology.yaml")
    ev_total = ev_cap = None
    if o:
        ot = read(o)
        ev_total = len(re.findall(r"^\s*-?\s*id:\s*EV-", ot, re.M))
        ev_cap = len(re.findall(r"scale:\s*capability", ot))
    # R0.1 — ambiguity / citations / rows
    amb_data = parse_ambiguity(case, cfg, warn)
    # R0.2 — maturity
    maturity = parse_maturity(case, cfg, warn)
    # R0 fix: expose the case knowledge graph under p1.graph as
    #   {nodes: [array], links: [array], counts: {nodes:int, links:int}}
    # so the dashboard shell can render both the vis-network view and the
    # count tiles from a single consistent shape.
    graph_payload = {
        "nodes": graph_full.get("nodes", []) or [],
        "links": graph_full.get("links", []) or [],
        "counts": {
            "nodes": nodes_count if nodes_count is not None else len(graph_full.get("nodes", []) or []),
            "links": links_count if links_count is not None else len(graph_full.get("links", []) or []),
        },
    }
    return {
        "status": status.get("phase_1", status.get("phase_1_rich")),
        "graph": graph_payload,
        # Back-compat alias kept for any consumer reading graph_full by name.
        "graph_full": graph_payload,
        "evidence_items": ev_total,
        "evidence_capability_scale": ev_cap,
        "ontology_file": o,
        "ambiguity": amb_data["ambiguity"],
        "citations": amb_data["citations"],
        "ambiguity_rows": amb_data["ambiguity_rows"],
        "maturity": maturity,
    }


# ---------------------------------------------------------------------------
# P2 parsers (extended)
# ---------------------------------------------------------------------------
def _parse_rules_table(case, cfg, warn, rules):
    """Build a rules_table (top 100) from control_set.yaml controls.

    Schema per row: {id, sub_domain, title, realization_class, source, ni}.
    """
    cs = glob_first(cfg["root"], "control_set.yaml")
    if not cs:
        return []
    t = read(cs)
    # Block-split tolerant to 2-, 3-, 4-, 6-space indents and quoted ids
    blocks = re.split(r"(?m)^(?=\s*-?\s*id:\s*\"?[A-Z])", t)
    table = []
    for b in blocks:
        m_id = re.search(r"^\s*-?\s*id:\s*\"?([A-Z]{2,}-D-[\d.]+-\d+|BPR-[\w.-]+)\"?", b, re.M)
        if not m_id:
            continue
        rid = m_id.group(1)
        m_dom = re.search(r"^\s*-?\s*(?:sub_)?domain:\s*\"?([D]-[\d.]+)\"?", b, re.M)
        # title can be 'title:' (C1) or 'description:' (C2/C3 generated YAML)
        m_title = re.search(r"^\s*-?\s*title:\s*\"?([^\"\n]+)\"?", b, re.M)
        if not m_title:
            m_title = re.search(r"^\s*-?\s*description:\s*\"?([^\"\n]+)\"?", b, re.M)
        m_rc = re.search(r"^\s*realization_class:\s*\"?(\w+)\"?", b, re.M)
        m_ni = re.search(r"^\s*ni:\s*\"?([0-9.]+)\"?", b, re.M)
        if not m_ni:
            m_ni = re.search(r"^\s*ni:\s*\n\s*value:\s*([0-9.]+)", b, re.M)
        # legal can be a list (C1) or comma-separated source: (C2/C3)
        m_legal = re.search(r"^\s*legal:\s*\n((?:\s*-\s*[^\n]+\n?)+)", b, re.M)
        legal = ""
        if m_legal:
            legal = " | ".join(
                re.sub(r"^\s*-\s*['\"]?", "", l).rstrip()
                for l in m_legal.group(1).splitlines()
                if l.strip().startswith("-")
            )
        else:
            m_source = re.search(r"^\s*source:\s*\"?([^\"\n]+)\"?", b, re.M)
            if m_source:
                legal = m_source.group(1)
        table.append({
            "id": rid,
            "sub_domain": m_dom.group(1) if m_dom else "",
            "title": (m_title.group(1).strip() if m_title else ""),
            "realization_class": m_rc.group(1) if m_rc else "",
            "source": legal,
            "ni": m_ni.group(1) if m_ni and m_ni.group(1) else "",
        })
        if len(table) >= 100:
            break
    return table


def _parse_obligations_objectives_mappings(case, cfg, warn):
    """Parse Doc14 (obligations), Doc16 (objectives), Doc19 (mappings) per case.

    Schemas:
      obligations: [{id, rule_id, derived_from, priority}]
      objectives:  [{id, rule_id, derived_from, priority}]
      mappings:    [{framework, control, anchor}]
    """
    obligations = []
    objectives = []
    mappings = []

    ob_rel = DOC_P2_OBLIGATIONS.get(case)
    if ob_rel:
        t = read(f"{cfg['root']}/02_PHASE2_RULES_RICH/{ob_rel}")
        if t:
            # OBL-D-XX.X-NNN ids
            for m in re.finditer(r"\b(OBL-D-\d{2}\.\d{1}-\d{3})\b", t):
                obligations.append({
                    "id": m.group(1),
                    "rule_id": None,
                    "derived_from": None,
                    "priority": None,
                })
            # Deduplicate while preserving order
            seen, dedup = set(), []
            for o in obligations:
                if o["id"] in seen:
                    continue
                seen.add(o["id"])
                dedup.append(o)
            obligations = dedup
            # Priority field: derived from a "Priority" table column near the ID
            for o in obligations:
                m = re.search(rf"{re.escape(o['id'])}.*?Priority[^|]*\|\s*(\w+)", t, re.S)
                if m:
                    o["priority"] = m.group(1)
        else:
            warn.append(f"{case}: obligation doc missing ({ob_rel})")

    ob_doc_rel = DOC_P2_OBJECTIVES.get(case)
    if ob_doc_rel:
        t = read(f"{cfg['root']}/02_PHASE2_RULES_RICH/{ob_doc_rel}")
        if t:
            for prefix in (r"PO-D-\d{2}\.\d{1}-\d{3}", r"SO-D-\d{2}\.\d{1}-\d{3}",
                           r"AG-D-\d{2}\.\d{1}-\d{3}"):
                for m in re.finditer(rf"\b({prefix})\b", t):
                    objectives.append({
                        "id": m.group(1),
                        "rule_id": None,
                        "derived_from": None,
                        "priority": None,
                    })
            seen, dedup = set(), []
            for o in objectives:
                if o["id"] in seen:
                    continue
                seen.add(o["id"])
                dedup.append(o)
            objectives = dedup
        else:
            warn.append(f"{case}: objectives doc missing ({ob_doc_rel})")

    # Mappings: parse Doc19_Framework_Mapping_Matrix (or C3 Doc20)
    map_rel = None
    for cand in (
        "02_PHASE2_RULES_RICH/Doc19_Framework_Mapping_Matrix.md",
        "02_PHASE2_RULES_RICH/Doc20_Framework_Mapping_Matrix.md",
    ):
        p = REPO / cfg["root"] / cand
        if p.exists():
            map_rel = f"{cfg['root']}/{cand}"
            break
    if map_rel:
        t = read(map_rel)
        if t:
            # Look for table rows of the form: | CR-... | ... | NIST-... |
            for m in re.finditer(r"^\|\s*((?:CR|BPR)-D-[\d.]+-\d+)\s*\|([^|]*)\|([^|]*)\|",
                                 t, re.M):
                mappings.append({
                    "framework": m.group(3).strip(),
                    "control": m.group(1),
                    "anchor": m.group(2).strip(),
                })
                if len(mappings) >= 200:
                    break
    return obligations, objectives, mappings


def _parse_tensions(case, cfg, warn):
    """Parse tensions from Doc15 (or per-case equivalent).

    Schema per row: {id, name, severity, related_objectives, recommended_disposition}.
    """
    out = []
    t_rel = DOC_P2_TENSIONS.get(case)
    if not t_rel:
        return out
    t = read(f"{cfg['root']}/02_PHASE2_RULES_RICH/{t_rel}")
    if not t:
        warn.append(f"{case}: tension doc missing ({t_rel})")
        return out
    # Headings: ## T-001 ... , ## T-M-001 ..., ## T-L-001 ...
    # We split on headings of that form and parse the body for severity + disposition
    chunks = re.split(r"(?m)^##\s+(T-[A-Z0-9-]+)\b\s*[—:-]?\s*([^\n]*)", t)
    # chunks: [pre, id1, name1, body1, id2, name2, body2, ...]
    i = 1
    while i < len(chunks):
        tid = chunks[i]
        name = chunks[i + 1].strip() if i + 1 < len(chunks) else ""
        body = chunks[i + 2] if i + 2 < len(chunks) else ""
        # Severity
        sev_m = re.search(r"\*\*Severity\*\*\s*\|\s*([A-Za-z_]+)", body)
        if not sev_m:
            sev_m = re.search(r"severity[:\s]*\**\s*([A-Z]+)", body, re.I)
        sev = (sev_m.group(1) if sev_m else "").upper()
        # Recommended disposition
        disp_m = re.search(r"recommended_disposition[:\s]*([^\n|]+)", body, re.I)
        if not disp_m:
            disp_m = re.search(r"\*\*Disposition\*\*\s*\|\s*([^\n|]+)", body)
        disp = (disp_m.group(1).strip() if disp_m else "")
        # Related objectives (PO/SO refs)
        objs = sorted(set(re.findall(r"\b(?:PO|SO)-D-\d{2}\.\d{1}-\d{3}\b", body)))
        out.append({
            "id": tid.strip(),
            "name": name,
            "severity": sev,
            "related_objectives": objs,
            "recommended_disposition": disp,
        })
        i += 3
    return out


def _parse_posture(case, cfg, warn):
    """Compute posture.maturity_band from CAP maturity distribution.

    Bands (qualitative, per AEGIS posture model v2.0):
      OPTIMIZING:                all CAP T4
      QUANTITATIVELY_MANAGED:    all CAP T3+
      MANAGED:                   average T >= 2.5
      DEFINED:                   average T >= 1.5
      PLANNED:                   else

    Falls back to scanning the lane-cards markdown directly for CAP card
    `| Maturity |` lines when the rich-mode parser does not extract the field.
    """
    cap = []
    try:
        lane = parse_lane_cards(case, cfg, warn)
        cap = lane.get("cap", []) or []
    except Exception:
        cap = []
    # Build a list of (id, title, maturity) tuples
    cards = []
    for c in cap:
        cards.append((c.get("id"), c.get("title"), (c.get("Maturity") or "").upper()))
    # Fallback: scan the lane-cards doc directly
    if not any(m for _, _, m in cards):
        lc_rel = f"{cfg['root']}/{cfg['lane_cards']}"
        t = read(lc_rel)
        if t:
            cur_id = cur_title = None
            for line in t.splitlines():
                m_h = re.match(r"^##\s+(CAP-\d+)\s*[—:-]\s*(.*)$", line)
                if m_h:
                    cur_id = m_h.group(1)
                    cur_title = m_h.group(2).strip()
                    continue
                mm = re.match(r"^\|\s*Maturity\s*\|\s*([^|]+?)\s*\|", line, re.I)
                if mm and cur_id:
                    cards.append((cur_id, cur_title, mm.group(1).strip().upper()))
    if not cards:
        return None
    tiers = []
    for _, _, m in cards:
        if "PLANNED" in m:
            tiers.append(1)
        else:
            tm = re.search(r"\bT([1-4])\b", m)
            if tm:
                tiers.append(int(tm.group(1)))
            else:
                pm = re.search(r"\(([1-4])\)", m)
                if pm:
                    tiers.append(int(pm.group(1)))
                else:
                    nm = re.search(r"\b([1-4])\b", m)
                    if nm:
                        tiers.append(int(nm.group(1)))
    if not tiers:
        return None
    avg = sum(tiers) / len(tiers)
    if avg >= 3.5 and all(t >= 3 for t in tiers):
        band = "QUANTITATIVELY_MANAGED"
    elif avg >= 2.5:
        band = "MANAGED"
    elif avg >= 1.5:
        band = "DEFINED"
    else:
        band = "PLANNED"
    gaps = []
    for cid, title, m in cards:
        low = "PLANNED" in m or re.search(r"\(1\)|\bT1\b|\b1\b", m) is not None
        if low:
            label = (title or cid or "?").split(" ")[0]
            gaps.append({"function": label[:24],
                         "description": (title or cid or "")[:120]})
    return {
        "maturity_band": band,
        "target_band": "QUANTITATIVELY_MANAGED",
        "gaps": gaps[:20],
    }


def parse_p2(case, cfg, warn):
    """Parse Phase 2 control_set.yaml + extended widgets."""
    cs = glob_first(cfg["root"], "control_set.yaml")
    rules, rc_counts = [], {"TECHNOLOGY": 0, "PROCESS": 0, "CAPABILITY": 0, "other": 0}
    explicit_count = heuristic_count = 0
    if cs:
        t = read(cs)
        ids = re.findall(r'^\s*-?\s*(?:rule_)?id:\s*"?([A-Z]{2,}-D-[\d.]+-\d+)"?', t, re.M)
        classes = re.findall(r'realization_class:\s*"?(\w+)"?', t)
        domains = re.findall(r'^\s*-?\s*(?:sub_)?domain:\s*"?([D]-[\d.]+)"?', t, re.M)
        for i, rid in enumerate(ids):
            sub = domains[i] if i < len(domains) else ""
            entry = {"id": rid, "sub_domain": sub}
            rc_raw = classes[i] if i < len(classes) else None
            if rc_raw and rc_raw in rc_counts:
                rc = rc_raw
                heuristic = False
                explicit_count += 1
            else:
                rc, heuristic = derive_realization_class(entry)
                heuristic_count += 1
            key = rc if rc in rc_counts else "other"
            rc_counts[key] += 1
            rules.append({"id": rid, "realization_class": rc, "_heuristic": heuristic,
                          "sub_domain": sub})
    else:
        warn.append(f"{case}: control_set.yaml not found")
    if explicit_count and heuristic_count:
        rc_source = "mixed"
    elif heuristic_count:
        rc_source = "heuristic"
    elif explicit_count:
        rc_source = "yaml"
    else:
        rc_source = "none"
    # Tensions: use rich per-doc parser (full objects), fall back to id-set
    rich_tensions = _parse_tensions(case, cfg, warn)
    if not rich_tensions:
        tensions_ids = set()
        for cand in sorted((REPO / cfg["root"]).rglob("*Tension*")):
            tt = cand.read_text(encoding="utf-8", errors="ignore")
            tensions_ids |= set(re.findall(r"\bT-\d{3}\b", tt))
        rich_tensions = [{"id": t, "name": "", "severity": "",
                          "related_objectives": [], "recommended_disposition": ""}
                         for t in sorted(tensions_ids)]

    # R0.4 — rules_table, obligations/objectives/mappings, posture, frameworks, qnrcs, graph
    rules_table = _parse_rules_table(case, cfg, warn, rules)
    obligations, objectives, mappings = _parse_obligations_objectives_mappings(case, cfg, warn)
    posture = _parse_posture(case, cfg, warn)
    p2_graph = parse_p2_graph(case, cfg, warn)

    return {
        "rules_total": len(rules),
        "realization_class": rc_counts,
        "rc_source": rc_source,
        "rc_explicit": explicit_count,
        "rc_heuristic": heuristic_count,
        "rules_sample": rules[:5],
        "rules_file": cs,
        "tensions": [t["id"] for t in rich_tensions],   # back-compat: list[str]
        "tension_objects": rich_tensions,               # new: list[dict]
        "rules_table": rules_table,
        "obligations": obligations,
        "objectives": objectives,
        "mappings": mappings,
        "posture": posture,
        "frameworks": list(FRAMEWORKS_REF),
        "qnrcs_resources": list(QNRCS_RESOURCES),
        "graph": p2_graph,
        "last_updated": dt.datetime.now().isoformat(timespec="seconds"),
    }


# ---------------------------------------------------------------------------
# P3 parsers (extended)
# ---------------------------------------------------------------------------
def parse_p3_gates(case, cfg, warn):
    gates = {}
    vr = REPO / cfg["root"] / cfg["p3_dir"] / "scripts" / "verify_rich.py"
    if vr.exists():
        r = subprocess.run([sys.executable, str(vr)], capture_output=True, text=True, timeout=120)
        m = re.search(r"summary: (.+)", r.stdout + r.stderr)
        gates["verify_rich"] = {"summary": m.group(1) if m else f"exit {r.returncode}",
                                "pass": r.returncode == 0}
    else:
        warn.append(f"{case}: verify_rich.py missing")
    return gates


def parse_annexes(case, cfg):
    ann = REPO / cfg["root"] / cfg["p3_dir"] / "annexes"
    out = {"use_case_diagrams_plantuml": None, "svg_files": None,
           "sequence_diagrams": None}
    a = ann / "A_Use_Case_Diagrams.md"
    b = ann / "B_Sequence_Diagrams.md"
    sv = ann / "svg"
    if a.exists():
        out["use_case_diagrams_plantuml"] = len(re.findall(r"```plantuml", a.read_text(encoding="utf-8")))
    if b.exists():
        out["sequence_diagrams"] = len(re.findall(r"```mermaid\nsequenceDiagram", b.read_text(encoding="utf-8")))
    if sv.exists():
        out["svg_files"] = len(list(sv.glob("*.svg")))
    return out


# ---------------------------------------------------------------------------
# R0.5 — FR / NFR / Allocations / Threats / Gates tables
# ---------------------------------------------------------------------------
def _parse_card_heading_table(t, heading_re, max_rows=50):
    """Parse a doc with #### {heading} ... card sections.

    Returns a list of dicts: {id, title, description, source, priority, status, ...}
    where the second-line table fields are captured when present.
    """
    rows = []
    if not t:
        return rows
    blocks = re.split(r"(?m)^####\s+(" + heading_re + r")\s*[—:-]?\s*([^\n]*)", t)
    i = 1
    while i < len(blocks):
        rid = blocks[i].strip()
        title = blocks[i + 1].strip() if i + 1 < len(blocks) else ""
        body = blocks[i + 2] if i + 2 < len(blocks) else ""
        row = {"id": rid, "title": title, "description": "", "source": "",
               "priority": "", "status": ""}
        # First table row (| **Field** | value |)
        for line in body.splitlines()[:60]:
            mm = re.match(r"^\|\s*\*\*([^*]+?)\*\*\s*\|\s*([^|]+?)\s*\|", line)
            if mm:
                k = mm.group(1).strip()
                v = mm.group(2).strip()
                kl = k.lower()
                if "description" in kl or "requirement" in kl or "nfr" in kl or "fr " in kl:
                    row["description"] = v
                elif "source" in kl or "linked" in kl or "rule" in kl:
                    row["source"] = v
                elif "priority" in kl:
                    row["priority"] = v
                elif "status" in kl:
                    row["status"] = v
        if not row["description"]:
            # Fallback: first non-empty line of body
            for line in body.splitlines():
                line = line.strip()
                if line and not line.startswith("|") and not line.startswith("#"):
                    row["description"] = line[:200]
                    break
        rows.append(row)
        if len(rows) >= max_rows:
            break
        i += 3
    return rows


def parse_requirements_full(case, cfg, warn):
    """Extended FR / NFR / allocations parser for P3 widgets.

    Supports two layouts:
      (a) `#### FR-NN ...` heading + per-card table (C3)
      (b) tabular `| FR-NN | description | ...` rows (C1/C2)
    """
    paths = doc_p3_paths(case, cfg)
    out = {"fr_table": [], "nfr_table": [], "allocations": []}

    # FR
    t = read(paths["fr"])
    if t:
        out["fr_table"] = _parse_card_heading_table(t, r"FR-\d{1,3}", max_rows=50)
        if not out["fr_table"]:
            # Tabular fallback: | FR-NN | description | source | linked FRs | CR | method | priority
            for m in re.finditer(
                r"^\|\s*(FR-\d{1,3})\s*\|([^|]+?)\|([^|]*?)\|([^|]*?)\|([^|]*?)\|([^|]*?)\|([^|]*?)\|",
                t, re.M):
                out["fr_table"].append({
                    "id": m.group(1).strip(),
                    "title": m.group(2).strip()[:120],
                    "description": m.group(2).strip(),
                    "source": m.group(5).strip(),
                    "priority": m.group(7).strip(),
                    "status": "",
                })
                if len(out["fr_table"]) >= 50:
                    break
    else:
        warn.append(f"{case}: FR doc missing ({paths['fr']})")

    # NFR
    t = read(paths["nfr"])
    if t:
        out["nfr_table"] = _parse_card_heading_table(
            t, r"NFR-(?:\d{1,3}|[A-Z]{2,5}-\d{1,3})", max_rows=50)
        if not out["nfr_table"]:
            for m in re.finditer(
                r"^\|\s*(NFR-(?:\d{1,3}|[A-Z]{2,5}-\d{1,3}))\s*\|([^|]+?)\|([^|]*?)\|([^|]*?)\|([^|]*?)\|([^|]*?)\|",
                t, re.M):
                out["nfr_table"].append({
                    "id": m.group(1).strip(),
                    "title": m.group(2).strip()[:120],
                    "description": m.group(2).strip(),
                    "source": m.group(5).strip(),
                    "priority": "",
                    "status": "",
                })
                if len(out["nfr_table"]) >= 50:
                    break
    else:
        warn.append(f"{case}: NFR doc missing ({paths['nfr']})")

    # Allocations: pull from Doc24 / Doc25 / Doc26 depending on case
    t = read(paths["alloc"])
    if t:
        for row in _parse_card_heading_table(t, r"(?:DN-\d{1,3}|DN-D-[\d.]+-\d{3})", max_rows=100):
            out["allocations"].append(row)
        if not out["allocations"]:
            # Tabular fallback: | CR-... | ... | node
            for m in re.finditer(
                r"\|\s*((?:CR|BPR)-D-[\d.]+-\d+)\s*\|([^|]*?)\|([^|]*?)\|", t):
                out["allocations"].append({
                    "id": m.group(1).strip(),
                    "title": m.group(3).strip()[:80],
                    "description": m.group(2).strip()[:120],
                    "source": "control_set",
                    "priority": "", "status": "",
                })
                if len(out["allocations"]) >= 200:
                    break
    else:
        warn.append(f"{case}: alloc doc missing ({paths['alloc']})")

    seen, dedup = set(), []
    for a in out["allocations"]:
        if a["id"] in seen:
            continue
        seen.add(a["id"])
        dedup.append(a)
    out["allocations"] = dedup
    return out


def parse_threat_table(case, cfg, warn):
    """Parse Doc27 (or per-case) Risk Analysis for RISK-NN / THR-NN rows.

    Handles two layouts:
      (a) `#### RISK-NN ...` heading + per-card body table
      (b) tabular `| RISK-NN | threat | ... |` rows (C1/C2 RICH)
    """
    paths = doc_p3_paths(case, cfg)
    t = read(paths["risks"])
    if not t:
        warn.append(f"{case}: risk doc missing ({paths['risks']})")
        return []
    rows = []
    # (a) heading layout
    blocks = re.split(r"(?m)^####\s+((?:RISK|THR)-\d{1,3})\s*[—:-]?\s*([^\n]*)", t)
    i = 1
    while i < len(blocks):
        rid = blocks[i].strip()
        title = blocks[i + 1].strip() if i + 1 < len(blocks) else ""
        body = blocks[i + 2] if i + 2 < len(blocks) else ""
        row = {"id": rid, "title": title, "threat": "", "stride": "",
               "likelihood": "", "impact": "", "mitigation_uc": "",
               "mitigation_gate": ""}
        for line in body.splitlines()[:50]:
            mm = re.match(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
            if mm:
                k = mm.group(1).strip().lower()
                v = mm.group(2).strip()
                if "risk" in k and "id" not in k:
                    row["threat"] = v
                elif "likelihood" in k:
                    row["likelihood"] = v
                elif "impact" in k:
                    row["impact"] = v
                elif "mitigation uc" in k or "uc " in k:
                    row["mitigation_uc"] = v
                elif "mitigation gate" in k or "gate" in k:
                    row["mitigation_gate"] = v
                elif "stride" in k:
                    row["stride"] = v
        if not row["threat"]:
            row["threat"] = title
        rows.append(row)
        if len(rows) >= 100:
            break
        i += 3
    if rows:
        return rows
    # (b) tabular fallback (multiple flavours):
    #     - C1/C2: | RISK-NN | description | D-sub | likelihood | impact | ...
    #     - C3:   | THR-DP-NN × Actor | name | flow | stride | anchors | CR | impact | ...
    # Use a permissive row scan that captures up to 7 columns and heuristically
    # maps the impact / likelihood / mitigation fields.
    for line in t.splitlines():
        if not line.startswith("|"):
            continue
        m = re.match(r"^\|\s*((?:RISK|THR)-[A-Z0-9-]+)\b[^|]*\|(.+)\|\s*$", line)
        if not m:
            continue
        rid = m.group(1).strip()
        rest = [c.strip() for c in m.group(2).split("|")]
        # Heuristic column mapping (best-effort across the two layouts):
        #   rest[0] = name/description  rest[-1] = impact  rest[-3] = stride?
        name = rest[0] if rest else rid
        stride = ""
        impact = ""
        gate = ""
        likelihood = ""
        if len(rest) >= 7:  # C3 layout: name, flow, stride, anchors, CR, impact
            stride = rest[2] if len(rest) > 2 else ""
            gate = rest[4] if len(rest) > 4 else ""
            impact = rest[5] if len(rest) > 5 else ""
        elif len(rest) >= 5:  # C1/C2: desc, D-sub, likelihood, impact, mitigation, ...
            likelihood = rest[2] if len(rest) > 2 else ""
            impact = rest[3] if len(rest) > 3 else ""
            gate = rest[4] if len(rest) > 4 else ""
        rows.append({
            "id": rid,
            "title": name[:120],
            "threat": name,
            "stride": stride,
            "likelihood": likelihood,
            "impact": impact,
            "mitigation_uc": "",
            "mitigation_gate": gate,
        })
        if len(rows) >= 100:
            break
    return rows


def parse_gates_table(case, cfg, warn):
    """Parse Doc25/26/27 (per-case) for GATE-D-XX-NN / GATE-CR-... rows.

    Handles two layouts:
      (a) `#### GATE-...` heading + per-card body (C3)
      (b) tabular `| GATE-CR-D-... | rule | ... | status | ...` rows (C1/C2)
    """
    paths = doc_p3_paths(case, cfg)
    t = read(paths["gates"])
    if not t:
        warn.append(f"{case}: gates doc missing ({paths['gates']})")
        return []
    rows = []
    # (a) heading layout
    blocks = re.split(r"(?m)^####\s+(GATE-(?:D-[\d.]+-\d+|CR-D-[\d.]+-\d+|D-\d{2}-\d{2}|IM-\d+))\s*[—:-]?\s*([^\n]*)", t)
    i = 1
    while i < len(blocks):
        gid = blocks[i].strip()
        name = blocks[i + 1].strip() if i + 1 < len(blocks) else ""
        body = blocks[i + 2] if i + 2 < len(blocks) else ""
        row = {"id": gid, "name": name, "status": "", "rules_checked": 0,
               "passed": 0, "failed": 0}
        for line in body.splitlines()[:60]:
            mm = re.match(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
            if mm:
                k = mm.group(1).strip().lower()
                v = mm.group(2).strip()
                if "status" in k or k == "gate status":
                    row["status"] = v
                elif "rule" in k and "verified" in k:
                    row["rules_checked"] = len(re.findall(r"(?:CR|BPR)-D-[\d.]+-\d+", v))
                elif "method" in k and row["status"] == "":
                    row["status"] = v
        rows.append(row)
        if len(rows) >= 100:
            break
        i += 3
    if rows:
        return rows
    # (b) tabular fallback: | GATE-CR-D-XX.X-NNN | CR-D-XX.X-NNN | D-XX.X | ... | STATUS | ...
    for m in re.finditer(
        r"^\|\s*(GATE-(?:CR-D-[\d.]+-\d+|D-[\d.]+-\d+|D-\d{2}-\d{2}|IM-\d+))\s*\|"
        r"([^|]*?)\|([^|]*?)\|([^|]*?)\|([^|]*?)\|([^|]*?)\|",
        t, re.M):
        gid = m.group(1).strip()
        rule = m.group(2).strip()
        status = m.group(5).strip() or m.group(4).strip()
        rows.append({
            "id": gid,
            "name": rule,
            "status": status,
            "rules_checked": 1 if rule else 0,
            "passed": 0,
            "failed": 0,
        })
        if len(rows) >= 100:
            break
    return rows


def parse_threat_flow(case, cfg, warn, muc_ids, ucs, lane):
    """Cross-reference muc_ids x UCs x PROC/CAP to build threat_flow entries."""
    flow = []
    if not muc_ids:
        return flow
    uc_index = {u.get("id"): u for u in (ucs or [])}
    proc_index = {p.get("id"): p for p in (lane.get("proc", []) or [])}
    cap_index = {c.get("id"): c for c in (lane.get("cap", []) or [])}
    for muc in muc_ids[:30]:
        # Pick a UC whose title contains the MUC or fall back to the first UC
        uc = next((u for u in (ucs or []) if muc in (u.get("title") or "")),
                  (ucs or [None])[0] if ucs else None)
        if not uc:
            continue
        # Find a PROC/CAP that realises this UC
        target = None
        for p in (lane.get("proc", []) or []):
            if (uc.get("id") in (p.get("Realises") or "")):
                target = p; break
        if not target:
            for c in (lane.get("cap", []) or []):
                if (uc.get("id") in (c.get("Realises") or "")):
                    target = c; break
        flow.append({
            "muc": muc,
            "flow": uc.get("title") or uc.get("id"),
            "lane_card": target.get("id") if target else "",
            "strength": "MEDIUM",
        })
    return flow


def parse_maturity_distribution(lane):
    """Count from PROC/CAP fields.Maturity strings.

    Accepts: 'PLANNED (1)', 'T1', 'T2 ...', 'T3', 'T4', 'PLANNED', 'IMPLEMENTED'.
    Falls back to scanning the lane-cards markdown directly for `| Maturity |`
    lines, because the rich-mode card parser does not always capture fields
    (e.g. C1 uses plain `| Field | value |` without `**Field**`).
    """
    dist = {"PLANNED": 0, "1": 0, "2": 0, "3": 0, "4": 0}
    for kind in ("proc", "cap"):
        for c in lane.get(kind, []) or []:
            m = (c.get("Maturity") or "").upper()
            if m:
                _count_maturity_token(m, dist)
    # Fallback: parse the lane-cards markdown directly when nothing was
    # captured (rich-mode cards without `**Field**` markers).
    if sum(dist.values()) == 0:
        cfg = lane.get("_cfg") or {}
        if cfg:
            lc_rel = f"{cfg['root']}/{cfg['lane_cards']}"
            t = read(lc_rel)
            if t:
                for line in t.splitlines():
                    mm = re.match(r"^\|\s*Maturity\s*\|\s*([^|]+?)\s*\|", line, re.I)
                    if mm:
                        _count_maturity_token(mm.group(1).upper(), dist)
    return dist


def _count_maturity_token(m, dist):
    """Increment the maturity_distribution bucket for one Maturity string."""
    if "PLANNED" in m:
        dist["PLANNED"] += 1
    else:
        tm = re.search(r"\bT([1-4])\b", m)
        if tm:
            dist[tm.group(1)] += 1
        else:
            pm = re.search(r"\(([1-4])\)", m)
            if pm:
                dist[pm.group(1)] += 1
            else:
                nm = re.search(r"\b([1-4])\b", m)
                if nm:
                    dist[nm.group(1)] += 1


def parse_risks(case, cfg, warn):
    muc = set()
    for cand in sorted(x for x in (REPO / cfg["root"]).rglob("*.md") if x.is_file()):
        muc |= set(re.findall(r"\bMUC-[A-Z0-9-]+\b", cand.read_text(encoding="utf-8", errors="ignore")))
    return {"muc_ids": sorted(muc), "muc_count": len(muc)}


# ---------------------------------------------------------------------------
# Legacy FR/NFR summary (kept for back-compat)
# ---------------------------------------------------------------------------
def parse_fr_nfr(case, cfg):
    req = REPO / cfg["root"] / cfg["p3_dir"] / "requirements"
    fr = nfr = None
    if req.exists():
        for f in sorted(req.glob("*Functional_Requirements.md")):
            ft = f.read_text(encoding="utf-8")
            fr = max(fr or 0, len(set(re.findall(r"\bFR-\d+\b", ft))), len(re.findall(r"^#### FR-", ft, re.M)))
        for f in sorted(req.glob("*Non_Functional_Requirements.md")):
            ft = f.read_text(encoding="utf-8")
            nfr = max(nfr or 0, len(set(re.findall(r"\bNFR-\d+\b", ft))), len(re.findall(r"^#### NFR-", ft, re.M)))
    return {"fr_ids": fr, "nfr_ids": nfr}


def parse_audit(warn):
    res = {}
    t = read(str(AUDIT_REPORT.relative_to(REPO))) if AUDIT_REPORT.exists() else None
    if not t:
        warn.append("traceability audit report missing")
        return res
    for case, row in re.findall(r"^\| (Case_\d\d)[^|]*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|", t, re.M):
        res[case] = {"obj_to_ctrl": row0(row), "ctrl_to_obj": row0(row, 1), "uc_to_obj": row0(row, 2)}
    return res


def row0(cell, idx=0):
    m = re.search(r"(\d+)/(\d+) = ([\d.]+)%", cell if isinstance(cell, str) else "")
    return None


def audit_row(t, case):
    m = re.search(rf"^\| {case} \|([^|]*)\|([^|]*)\|([^|]*)\|", t, re.M)
    if not m:
        return None
    vals = []
    for c in m.groups():
        mm = re.search(r"(\d+)/(\d+) = ([\d.]+)%", c)
        vals.append({"covered": int(mm.group(1)), "total": int(mm.group(2)), "pct": float(mm.group(3))} if mm else None)
    keys = ["obj_to_ctrl", "ctrl_to_obj", "uc_to_obj"]
    return dict(zip(keys, vals))


# ---------------------------------------------------------------------------
# Catalog & Lane parsers (kept verbatim from prior version)
# ---------------------------------------------------------------------------
def parse_catalog(case, cfg, warn):
    """UC inventory + packages from the case catalog. Grammar-tolerant."""
    text = read(f"{cfg['root']}/{cfg['catalog']}")
    if not text:
        warn.append(f"{case}: catalog missing ({cfg['catalog']})")
        return {"packages": [], "ucs": []}
    fm = frontmatter(text)
    chunks = cut_sections(text)

    def in_family(head, family):
        if head is None:
            return False
        pat = cfg[family]
        return re.search(pat, head, re.I) is not None

    packages, ucs, cur_pkg = [], [], None
    pkg_re = re.compile(r"^###\s+(?:§?\d+\.\d+\s+)?(?:\d+\.\d+\s+)?((?:PKG|PKG-)[-\w]*(?:\s*[—:-]\s*[^(\n]+)?[^(\n]*)")
    pkg_name_re = re.compile(r"^###\s+(?:§?\d+\.\d+\s+)?(?:\d+\.\d+\s+)?(PKG-[\w-]+)")
    for head, body in chunks:
        family = None
        if in_family(head, "product_section"):
            family = "product"
        elif in_family(head, "compliance_section"):
            family = "compliance"
        for line in body.split("\n"):
            m_pkg = pkg_re.match(line) if line.startswith("### ") else None
            if m_pkg:
                cur_pkg = m_pkg.group(1).strip()
                continue
            m = re.match(r"^#### (?:Use-Case: \{([^}]+)\}|(UC-\d+))\s*[—-]?\s*(.*)$", line)
            if m:
                uid = (m.group(1) or m.group(2)).strip()
                title = (m.group(3) or "").strip()
                ucs.append({"id": uid, "title": title, "package": cur_pkg, "lane": "UC"})
                continue
            m2 = re.match(r"^#### (UC-\d+)\s+—\s+(.*)$", line)
            if m2:
                ucs.append({"id": m2.group(1), "title": m2.group(2).strip(), "package": cur_pkg, "lane": "UC"})
                continue
            if family == "compliance":
                m3 = re.match(r"^\|\s*(UC-\d+)\s*\|\s*([^|]+?)\s*\|", line)
                if m3:
                    ucs.append({"id": m3.group(1), "title": m3.group(2).strip(), "package": cur_pkg, "lane": "UC"})
    seen, dedup = set(), []
    for u in ucs:
        if u["id"] in seen:
            continue
        seen.add(u["id"])
        u["lane"] = "UC" if u["id"].startswith("UC") else u["id"].split("-")[0]
        dedup.append(u)
    pk_seen, pkgs = set(), []
    for _, body in chunks:
        for line in body.split("\n"):
            if not line.startswith("### "):
                continue
            mn = pkg_name_re.match(line)
            if not mn:
                continue
            name = mn.group(1)
            if name and name not in pk_seen:
                pk_seen.add(name)
                pkgs.append(name)
    return {"packages": pkgs, "ucs": dedup, "frontmatter_version": fm.get("version")}


def parse_lane_cards(case, cfg, warn):
    """PROC/CAP cards from the per-case lane-cards doc (§5C.1/§5C.2 fields)."""
    text = read(f"{cfg['root']}/{cfg['lane_cards']}")
    if not text:
        warn.append(f"{case}: lane cards doc missing ({cfg['lane_cards']})")
        return {"proc": [], "cap": []}
    out = {"proc": [], "cap": []}
    cur = None
    for line in text.split("\n"):
        m = re.match(r"^## (PROC-\d+)\s+—\s+(.*)$", line)
        if m:
            cur = {"id": m.group(1), "title": m.group(2).strip(), "fields": {}}
            out["proc"].append(cur)
            continue
        m = re.match(r"^## (CAP-\d+)\s+—\s+(.*)$", line)
        if m:
            cur = {"id": m.group(1), "title": m.group(2).strip(), "fields": {}}
            out["cap"].append(cur)
            continue
        if cur:
            fm_ = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|$", line)
            if fm_ and fm_.group(1) != "Field":
                cur["fields"][fm_.group(1)] = fm_.group(2)
    for kind in ("proc", "cap"):
        for c in out[kind]:
            f = c.pop("fields")
            keep = ["Owner", "Trigger", "Activities", "Roles", "SLA / Timing", "Span",
                    "Maturity", "Realises", "Anchors", "Evidence"]
            c.update({k: f.get(k) for k in keep})
    return out


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def build(warn):
    data = {"meta": {}, "cases": {}, "crosscase": {}}
    try:
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True,
                                text=True, cwd=REPO).stdout.strip()
    except Exception:
        commit = None
    data["meta"] = {"generated_at": dt.datetime.now().isoformat(timespec="seconds"),
                    "git_commit": commit, "warnings": warn}
    audit_t = read(str(AUDIT_REPORT.relative_to(REPO)))
    for case, cfg in CASES.items():
        c = {"profile": {"tier": cfg["tier"], "regulations": cfg["regs"]}}
        # P1 + P2
        p1 = parse_p1(case, cfg, warn)
        p2 = parse_p2(case, cfg, warn)
        # P3 components
        cat = parse_catalog(case, cfg, warn)
        lane = parse_lane_cards(case, cfg, warn)
        lane["_cfg"] = cfg  # used by maturity_distribution fallback
        risks = parse_risks(case, cfg, warn)
        req_full = parse_requirements_full(case, cfg, warn)
        threat_table = parse_threat_table(case, cfg, warn)
        gates_table = parse_gates_table(case, cfg, warn)
        threat_flow = parse_threat_flow(case, cfg, warn, risks["muc_ids"],
                                        cat["ucs"], lane)
        maturity_dist = parse_maturity_distribution(lane)
        p3_graph = parse_p3_graph(case, cfg, warn, cat, lane)
        # Back-compat FR/NFR summary
        fr_nfr_legacy = parse_fr_nfr(case, cfg)
        p3 = {
            "catalog": cat,
            "lane_cards": lane,
            "annexes": parse_annexes(case, cfg),
            "fr_nfr": fr_nfr_legacy,
            "risks": risks,
            "gates": parse_p3_gates(case, cfg, warn),
            # Flat aliases expected by AEGIS_Master_Dashboard.html:
            "use_cases": cat["ucs"],
            "uc_table": cat["ucs"],                # R0.7 — alias for Folio 9
            "proc_cards": lane["proc"],
            "cap_cards":  lane["cap"],
            "requirements": {
                "fr_ids": fr_nfr_legacy.get("fr_ids"),
                "nfr_ids": fr_nfr_legacy.get("nfr_ids"),
                "fr_table": req_full["fr_table"],
                "nfr_table": req_full["nfr_table"],
                "allocations": req_full["allocations"],
            },
            "threats": risks.get("muc_ids") or [],
            "threat_table": threat_table,
            "gate_table": gates_table,
            "gates_table": gates_table,
            "threat_flow": threat_flow,
            "maturity_distribution": maturity_dist,
            "drill_available": False,
            "graph": p3_graph,
        }
        # Explicit phase dicts (R0.6 — predictable shape)
        c["phases"] = {
            "P1": p1,
            "P2": p2,
            "P3": p3,
        }
        c["audit"] = audit_row(audit_t, case.replace("Case_0", "Case_0").replace("Case_01", "Case_01")) if audit_t else None
        if audit_t:
            m = re.search(rf"^\| Case_\d\d \|", audit_t, re.M)
        data["cases"][case] = c
    # crosscase
    data["crosscase"] = {
        "uc_totals": {c: len(data["cases"][c]["phases"]["P3"]["catalog"]["ucs"]) for c in CASES},
        "proc_totals": {c: len(data["cases"][c]["phases"]["P3"]["lane_cards"]["proc"]) for c in CASES},
        "cap_totals": {c: len(data["cases"][c]["phases"]["P3"]["lane_cards"]["cap"]) for c in CASES},
        "audit": {c: data["cases"][c].get("audit") for c in CASES},
    }
    # gates_matrix (top-level): per-case gate category summaries for Folio 13.
    # Use the most-common status from p3.gates_table per case, split into the
    # four AEGIS categories (Context/Compliance/Realisation/Operation) by
    # matching the gate name prefix (GATE-CR- -> Compliance, GATE-PROC- ->
    # Operation, GATE-CAP- -> Realisation, else Context).
    def _categorise(g):
        n = g.get("name", "")
        if "CR-" in n or n.startswith("GATE-CR-"):
            return "Compliance"
        if n.startswith("GATE-PROC-") or "PROC" in n:
            return "Operation"
        if n.startswith("GATE-CAP-") or "CAP-" in n:
            return "Realisation"
        return "Context"
    gm = {}
    for case in CASES:
        tbl = data["cases"][case]["phases"]["P3"].get("gates_table", [])
        cats = {"Context": [], "Compliance": [], "Realisation": [], "Operation": []}
        for g in tbl:
            cats[_categorise(g)].append(g)
        short = case.split("_")[0].lower() + "_" + case.split("_")[1]  # case_01
        gm[short] = {}
        for cat_name, rows in cats.items():
            if not rows:
                gm[short][cat_name] = "--"
                continue
            # Pick most-common status; PASS takes precedence if any.
            statuses = [r.get("status", "--") for r in rows]
            from collections import Counter
            counts = Counter(statuses)
            top = counts.most_common(1)[0][0]
            gm[short][cat_name] = top
    # Map category names to G1..G4 in the shell
    data["gates_matrix"] = {
        short: {
            "G1": vals.get("Context", "--"),
            "G2": vals.get("Compliance", "--"),
            "G3": vals.get("Realisation", "--"),
            "G4": vals.get("Operation", "--"),
        }
        for short, vals in gm.items()
    }
    # audit rows properly per case key used in the report (Case_01 style)
    if audit_t:
        for case in CASES:
            data["cases"][case]["audit"] = audit_row(audit_t, case.replace("_TinyTask_SaaS", "").replace("_SecureBorder_Solutions", "").replace("_OmniBank_Financial", ""))
    return data


def inject(html_path, data):
    p = Path(html_path)
    t = p.read_text(encoding="utf-8")
    blob = json.dumps(data, ensure_ascii=False, indent=1)
    placeholder = "/*__MASTER_DATA__*/null"
    if placeholder in t:
        t = t.replace(placeholder, blob, 1)
    else:
        # Already-injected state: replace the existing `const MASTER_DATA = {...};`
        # block. Find the line "const MASTER_DATA = {" at top level (not inside a comment).
        import re
        m = re.search(r"^const MASTER_DATA = \{", t, re.M)
        if not m:
            raise SystemExit(f"placeholder {placeholder} and const MASTER_DATA block both missing in {p}")
        start = m.start()
        # Find the matching close: track brace depth starting at the opening brace.
        depth = 0
        i = start + len("const MASTER_DATA = ")
        while i < len(t):
            ch = t[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
            i += 1
        else:
            raise SystemExit(f"could not find end of MASTER_DATA const block in {p}")
        # Consume optional trailing semicolon or newline
        while end < len(t) and t[end] in ";\n":
            end += 1
        t = t[:start] + "const MASTER_DATA = " + blob + ";" + t[end:]
    p.write_text(t, encoding="utf-8")
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(OUT_DEFAULT))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--inject", default=None, help="HTML template to inject the JSON into")
    args = ap.parse_args()

    warn = []
    data = build(warn)
    data["meta"]["warnings"] = sorted(set(warn))

    # light validation
    errs = []
    for case, c in data["cases"].items():
        ids = [u["id"] for u in c["phases"]["P3"]["catalog"]["ucs"]]
        if len(ids) != len(set(ids)):
            errs.append(f"{case}: duplicate UC ids")
        if not ids:
            errs.append(f"{case}: 0 UCs parsed — grammar mismatch?")
        # R0.6 explicit validations
        m = c["phases"]["P1"]["maturity"]
        if len(m["labels"]) != 6:
            errs.append(f"{case}: maturity.labels != 6")
        if len(m["current"]) != 6:
            errs.append(f"{case}: maturity.current != 6")
        if len(m["target"]) != 6:
            errs.append(f"{case}: maturity.target != 6")
        if not isinstance(c["phases"]["P1"]["graph_full"]["nodes"], list):
            errs.append(f"{case}: graph_full.nodes not a list")
        if c["phases"]["P2"]["rules_table"] is None:
            errs.append(f"{case}: rules_table is None")
    if errs:
        print("VALIDATION ERRORS:", *errs, sep="\n  ")
        sys.exit(2)

    blob = json.dumps(data, ensure_ascii=False, indent=1)
    print(f"parsed: {sum(data['crosscase']['uc_totals'].values())} UCs, "
          f"{sum(data['crosscase']['proc_totals'].values())} PROC, "
          f"{sum(data['crosscase']['cap_totals'].values())} CAP, "
          f"warnings={len(data['meta']['warnings'])}")
    if args.dry_run:
        print("dry-run: no write")
        return
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(blob, encoding="utf-8")
    print(f"wrote {out} ({len(blob)} bytes)")
    if args.inject:
        inject(args.inject, data)
        print(f"injected into {args.inject}")


if __name__ == "__main__":
    main()
