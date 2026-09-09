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
# R8 — 12 new P1 parsers (consume Doc01..Doc14, Citation_Index, phase1_graph,
# phase1_ontology). Each parser is robust to missing files: returns None and
# appends to `warn` when the source is absent. All parsers are stdlib-only.
# ---------------------------------------------------------------------------

# Per-case P1 doc filenames (filenames differ across C1/C2/C3 for Doc12/13/14).
DOC_P1_REGULATORY = "Doc08_Regulatory_Applicability.md"        # C1/C2/C3
DOC_P1_STRUCTURED_COMPLIANCE = {                                  # renamed Doc11 (C3=Doc12)
    "Case_01_TinyTask_SaaS": "Doc11_Structured_Compliance_Matrix.md",
    "Case_02_SecureBorder_Solutions": "Doc11_Structured_Compliance_Matrix.md",
    "Case_03_OmniBank_Financial": "Doc12_Structured_Compliance_Matrix.md",
}
DOC_P1_CLAUSE_MAPPING = "Doc10_Clause_Mapping_Matrix.md"          # all cases
DOC_P1_DORA = {                                                   # only C3 has it
    "Case_03_OmniBank_Financial": "Doc11_DORA_ICT_Risk_Framework.md",
}
DOC_P1_PROPORTIONALITY = {                                        # C1/C2=Doc12, C3=Doc13
    "Case_01_TinyTask_SaaS": "Doc12_Proportionality_Profile.md",
    "Case_02_SecureBorder_Solutions": "Doc12_Proportionality_Profile.md",
    "Case_03_OmniBank_Financial": "Doc13_Proportionality_Profile.md",
}
DOC_P1_ADJUSTED_GOALS = {                                         # C1/C2=Doc13, C3=Doc14
    "Case_01_TinyTask_SaaS": "Doc13_Adjusted_Goals.md",
    "Case_02_SecureBorder_Solutions": "Doc13_Adjusted_Goals.md",
    "Case_03_OmniBank_Financial": "Doc14_Adjusted_Goals.md",
}
DOC_P1_ORG_RACI = "Doc07_Org_Roles_RACI.md"
DOC_P1_COMPANY_CONTEXT = "Doc03_Company_Context_Assessment.md"
DOC_P1_THIRD_PARTY = "Doc06_ThirdParty_Landscape.md"
DOC_P1_ARCHITECTURE = "Doc04_Architecture_DataInventory.md"
DOC_P1_TENSIONS = {                                               # C1/C2=Doc15, C3=Doc16
    "Case_01_TinyTask_SaaS": "Doc15_Strategic_Tensions_Report.md",
    "Case_02_SecureBorder_Solutions": "Doc15_Strategic_Tensions_Report.md",
    "Case_03_OmniBank_Financial": "Doc16_Strategic_Tensions_Report.md",
}
DOC_P1_CITATION_INDEX = "Citation_Index.md"


def parse_regulations(case, cfg, warn):
    """Doc08 — extract regs list + clause table.

    Returns {regs, clauses:[{id,regulation,article,title,sub_domain}], total_clauses}
    or None if Doc08 missing. Clauses parsed from
    `| CLAUSE-NN | REG | Article NN | Title | D-XX.Y |` rows OR from the broader
    Doc10 table grammar `| GDPR-C01 | Art. 5(1)(c) | D-05.1 ... |` (Article column).
    When Doc08 has no clause rows, fall back to scanning Doc10_Clause_Mapping_Matrix.md.
    """
    rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{DOC_P1_REGULATORY}"
    t = read(rel)
    if not t:
        warn.append(f"{case}: {DOC_P1_REGULATORY} missing (parse_regulations)")
        return None
    fm = frontmatter(t)
    out = {"regs": [], "clauses": [], "total_clauses": 0}
    # applicable_regs from frontmatter (canonical) OR from H1/H2 list
    regs_raw = fm.get("applicable_regs") or fm.get("regs") or ""
    if isinstance(regs_raw, str) and regs_raw:
        out["regs"] = [r.strip().strip("'\"") for r in re.split(r"[,;\[\]]", regs_raw) if r.strip()]
    elif isinstance(regs_raw, list):
        out["regs"] = regs_raw
    if not out["regs"]:
        # Fallback: scan body for "Applicability Result: ✅ APPLICABLE" or the
        # `## 3. REGULATION-BY-REGULATION ...` H3 headings like "### 3.1 GDPR".
        out["regs"] = sorted(set(m.group(1).strip() for m in re.finditer(
            r"^###\s+\d+\.\d+\s+([A-Z][A-Za-z 0-9]+?)\s*\(", t, re.M)))
    # Pull clauses from any markdown table with a CLAUSE-ID + REG + ARTICLE column.
    seen = set()
    # Shape A
    for m in re.finditer(
        r"^\|\s*(CLAUSE-\d+)\s*\|\s*([A-Z][A-Za-z 0-9]+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([D]-\d{1,2}\.\d)\s*\|",
        t, re.M):
        cid, reg, art, title, sd = (s.strip() for s in m.groups())
        if cid in seen: continue
        seen.add(cid)
        out["clauses"].append({"id": cid, "regulation": reg, "article": art,
                               "title": title, "sub_domain": sd})
    # Shape B (Doc10 / Doc08 mapping tables) — REG-CXX ids (GDPR-C01, CRA-C02, ...)
    for m in re.finditer(
        r"^\|\s*((?:GDPR|CRA|NIS2|DORA|AI[A_-]?ACT|NIS|CRA|NIS_2)[-_]C\d{1,3})\s*\|"
        r"\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|",
        t, re.M):
        cid = m.group(1).strip().replace("NIS_2", "NIS2").replace("AI-ACT", "AIACT").replace("AI_ACT", "AIACT")
        if cid in seen: continue
        seen.add(cid)
        article = m.group(2).strip()
        rest = m.group(3).strip()
        # Try to extract a D-XX.Y from the third column
        sd_m = re.search(r"(D-\d{1,2}\.\d)", rest)
        sub = sd_m.group(1) if sd_m else ""
        # Derive regulation from cid prefix
        reg = infer_regulation_from_clause_id(cid) or (m.group(1).split("-")[0].upper())
        out["clauses"].append({"id": cid, "regulation": reg, "article": article,
                               "title": rest[:120], "sub_domain": sub})
    # Fallback: scan Doc10_Clause_Mapping_Matrix.md when Doc08 has no clause table
    if not out["clauses"]:
        doc10 = read(f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{DOC_P1_CLAUSE_MAPPING}")
        if doc10:
            for m in re.finditer(
                r"^\|\s*((?:GDPR|CRA|NIS2|DORA|AIACT|AI-ACT|AI_ACT|NIS)[-_]C\d{1,3})\s*\|"
                r"\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|",
                doc10, re.M):
                cid = m.group(1).strip()
                article = m.group(2).strip()
                rest = m.group(3).strip()
                if cid in seen: continue
                seen.add(cid)
                sd_m = re.search(r"(D-\d{1,2}\.\d)", rest)
                reg = infer_regulation_from_clause_id(cid) or cid.split("-")[0]
                out["clauses"].append({"id": cid, "regulation": reg, "article": article,
                                       "title": rest[:120],
                                       "sub_domain": sd_m.group(1) if sd_m else ""})
    out["total_clauses"] = len(out["clauses"])
    if not out["clauses"]:
        warn.append(f"{case}: parse_regulations: no clause rows extracted")
    return out


def parse_nist_controls(case, cfg, warn):
    """Doc13/Doc14 §5 NIST Controls Mapping table — 38 sub-domains × 3 frameworks.

    Returns {controls:[{framework,function,sub_domain,control_id,name,coverage}]}.
    Coverage defaults to 1.0 when the corpus marks a control as in scope.
    """
    fname = DOC_P1_ADJUSTED_GOALS.get(case)
    if not fname:
        warn.append(f"{case}: adjusted goals filename unknown for {case}")
        return None
    rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{fname}"
    t = read(rel)
    if not t:
        warn.append(f"{case}: {fname} missing (parse_nist_controls)")
        return None
    out = {"controls": []}
    # The §5 table has columns: Sub-Domain | Sub-Domain Name | Applicable Regs |
    # NIST CSF 2.0 Controls | NIST PF 1.0 Controls | NIST AI RMF Controls
    # Capture groups 1..4: sub, name, regs, csf, pf, ai
    row_re = re.compile(
        r"^\|\s*(D-\d{1,2}\.\d)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"
        r"\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", re.M)
    controls_seen = 0
    for m in row_re.finditer(t):
        sub, name, regs, csf, pf, ai = (s.strip() for s in m.groups())
        # Skip header + separator rows
        if sub.lower() == "sub-domain" or set(sub) <= {"-"}: continue
        controls_seen += 1
        for fw, raw in (("NIST CSF 2.0", csf), ("NIST PF 1.0", pf), ("NIST AI RMF", ai)):
            if not raw or raw == "—": continue
            # Strip duplicates / trailing punctuation and split on commas/semicolons
            tokens = [tok.strip().rstrip(",").rstrip(";") for tok in re.split(r"[,;]", raw)]
            # Some cells contain duplicates like "PR.PS-06; RS.MI-01, PR.PS-02, PR.PS-02"
            tokens = [tok for tok in tokens if tok and tok != "—"]
            seen_tok = set()
            for tok in tokens:
                # Reject semicolons leftover from OCR-style concatenations (e.g. "...; RS.MI-01")
                # by keeping only those that look like NIST control ids (NN.LL-NN...)
                clean = re.sub(r";\s*", "", tok).strip()
                if not clean or clean in seen_tok: continue
                if not re.match(r"^[A-Z]{2}\.[A-Z]{2}-\d", clean): continue
                seen_tok.add(clean)
                # Function code = first 2 letters before the dot
                fn_code = clean.split(".")[0] if "." in clean else ""
                out["controls"].append({
                    "framework": fw,
                    "function": fn_code,
                    "sub_domain": sub,
                    "control_id": clean,
                    "name": name,
                    "coverage": 1.0,
                })
    if not out["controls"]:
        # Fallback: scan any table-like line that has a Sub-Domain column AND a
        # column whose cells contain tokens like GV.RM-04, PR.DS-01, etc. This
        # covers C1/C2 where §5 is not present but NIST anchors still appear
        # in other tables (e.g. the §4 Track B Decision Trail includes NIST anchors
        # in the implementation references column).
        # Match a row that begins with | D-XX.Y ... and ends with |
        for m in re.finditer(r"^\|\s*(D-\d{1,2}\.\d)[^|\n]*\|([^|\n]*(?:\|[^|\n]*)*)\|\s*$",
                              t, re.M):
            sub = m.group(1).strip()
            row_text = m.group(0)
            # Walk every cell looking for NIST control ids
            seen_tok = set()
            for tok in re.findall(r"\b([A-Z]{2}\.[A-Z]{2}-\d+(?:\.\d+)?)\b", row_text):
                if tok in seen_tok: continue
                seen_tok.add(tok)
                fn = tok.split(".")[0]
                # Guess framework from function prefix: GV/ID/PR/DE/RS/RC -> CSF;
                # GV/ID/PR/CT/CM/PA -> PF (overlap with CSF); MANAGE/GOVERN/MEASURE -> AI.
                fw = "NIST AI RMF" if fn in ("MANAGE", "GOVERN", "MEASURE") else "NIST CSF 2.0"
                out["controls"].append({
                    "framework": fw,
                    "function": fn,
                    "sub_domain": sub,
                    "control_id": tok,
                    "name": sub,
                    "coverage": 1.0,
                })
            if seen_tok:
                controls_seen += 1
        if out["controls"]:
            warn.append(f"{case}: parse_nist_controls: §5 absent — fell back to row-scan")
    if not out["controls"]:
        warn.append(f"{case}: parse_nist_controls: 0 controls extracted")
    out["total"] = controls_seen
    return out


def parse_clause_mapping(case, cfg, warn):
    """Doc10 — Clause Mapping Matrix (Markdown companion).

    Returns {clauses:[{control,framework,sub_domain,weight:float}]}. Weight comes
    from the NI (Normative Intensity) column when present.

    The Doc10 grammar differs between C3 (8-column row with explicit NI col 8)
    and C1/C2 (5-column row: Clause ID | Article | D-XX.X | obligated | brief).
    """
    rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{DOC_P1_CLAUSE_MAPPING}"
    t = read(rel)
    if not t:
        warn.append(f"{case}: {DOC_P1_CLAUSE_MAPPING} missing (parse_clause_mapping)")
        return None
    out = {"clauses": []}
    # Per-row grammar (C3): 8 columns with NI at position 8
    for m in re.finditer(
        r"^\|\s*((?:GDPR|CRA|NIS2|DORA|AIACT|AI-ACT|AI_ACT|NIS)[-_]C\d{1,3})\s*\|"
        r"\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|([^|]*?)\|([^|]*?)\|([^|]*?)\|([^|]*?)\|"
        r"\s*([\d.]+)\s*\|",
        t, re.M):
        cid = m.group(1).strip()
        if cid.upper().startswith("NIS_2"):
            cid = "NIS2-" + cid.split("-", 1)[1]
        article = m.group(2).strip()
        sub_raw = m.group(3).strip()
        sd_m = re.search(r"(D-\d{1,2}\.\d)", sub_raw)
        sub = sd_m.group(1) if sd_m else ""
        try:
            ni = float(m.group(8).strip())
            weight = round(min(1.0, ni / 3.0), 3)
        except (ValueError, IndexError):
            weight = 0.0
        reg = infer_regulation_from_clause_id(cid) or cid.split("-")[0]
        out["clauses"].append({
            "control": cid,
            "framework": reg,
            "sub_domain": sub,
            "article": article,
            "weight": weight,
        })
        if len(out["clauses"]) >= 200:
            break
    # Per-row grammar (C1/C2): 5 columns — Clause ID | Article | D-XX.X | obligated | brief
    if not out["clauses"]:
        for m in re.finditer(
            r"^\|\s*((?:GDPR|CRA|NIS2|DORA|AIACT|AI-ACT|AI_ACT|NIS)[-_]C\d{1,3})\s*\|"
            r"\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|",
            t, re.M):
            cid = m.group(1).strip()
            article = m.group(2).strip()
            sub = m.group(3).strip()
            reg = infer_regulation_from_clause_id(cid) or cid.split("-")[0]
            out["clauses"].append({
                "control": cid,
                "framework": reg,
                "sub_domain": sub,
                "article": article,
                "weight": 1.0,  # default when NI is not split into its own column
            })
            if len(out["clauses"]) >= 200:
                break
    if not out["clauses"]:
        warn.append(f"{case}: parse_clause_mapping: no rows extracted")
    return out


def parse_dora(case, cfg, warn):
    """Doc11_DORA_ICT_Risk_Framework.md (only C3).

    Returns {articles:[{article,sub_domain,title,requirement}]}.
    Skips silently (returns None) for C1/C2.
    """
    fname = DOC_P1_DORA.get(case)
    if not fname:
        return None
    rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{fname}"
    t = read(rel)
    if not t:
        warn.append(f"{case}: {fname} missing (parse_dora)")
        return None
    out = {"articles": []}
    # Match #### Art. NN — Title or #### Art. NN — Sub-section title
    for m in re.finditer(r"^####\s+(Art\.\s*\d+(?:\([0-9a-z]+\))*)\s+[—:-]\s+([^\n]+)$", t, re.M):
        article = m.group(1).strip()
        title = m.group(2).strip()
        out["articles"].append({
            "article": article,
            "sub_domain": "",
            "title": title,
            "requirement": title,
        })
    # Pull sub_domain from the first "**Primary sub-domain(s)** | ..." row in this block
    if out["articles"]:
        # Re-scan by block to find first sub-domain mention
        blocks = re.split(r"(?m)^####\s+(Art\.\s*\d+(?:\([0-9a-z]+\))*)\s+[—:-]\s+([^\n]+)$", t)
        i = 1
        idx = 0
        while i < len(blocks) and idx < len(out["articles"]):
            body = blocks[i + 2] if i + 2 < len(blocks) else ""
            sd_m = re.search(r"\*\*Primary sub-domain\(s\)\*\*\s*\|\s*\*\*([D]-\d{1,2}\.\d)\*\*", body)
            if not sd_m:
                sd_m = re.search(r"\|\s*\*\*(D-\d{1,2}\.\d)", body)
            if sd_m:
                out["articles"][idx]["sub_domain"] = sd_m.group(1)
            i += 3
            idx += 1
    if not out["articles"]:
        warn.append(f"{case}: parse_dora: no articles extracted")
    return out


def parse_proportionality(case, cfg, warn):
    """Doc12/Doc13 Proportionality Profile — §4 tier table.

    Returns {tiers:{RIGOROUS:int,STANDARD:int,SIMPLE:int,...}, per_subdomain:{D-XX.Y: tier}}.
    C3 has a 13-column row; C1/C2 have a 5/6-column row with `Tier` col at index 3.
    """
    fname = DOC_P1_PROPORTIONALITY.get(case)
    if not fname:
        warn.append(f"{case}: proportionality filename unknown for {case}")
        return None
    rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{fname}"
    t = read(rel)
    if not t:
        warn.append(f"{case}: {fname} missing (parse_proportionality)")
        return None
    out = {"tiers": {}, "per_subdomain": {}}
    # Row: | D-XX.Y Sub-domain name | I | P | Tier | ...
    for m in re.finditer(
        r"^\|\s*(D-\d{1,2}\.\d)\s+[^|]+\|\s*[A-Z_]+\s*\|\s*[A-Z_]+\s*\|\s*([A-Z]+)\s*\|",
        t, re.M):
        sd, tier = m.group(1), m.group(2).upper()
        out["per_subdomain"][sd] = tier
        out["tiers"][tier] = out["tiers"].get(tier, 0) + 1
    # Fallback to frontmatter tier_distribution if no rows found
    if not out["tiers"]:
        fm = frontmatter(t)
        td = fm.get("tier_distribution", {}) or {}
        for k, v in td.items():
            if isinstance(v, int) and k.upper() in ("RIGOROUS", "STANDARD", "LIGHTWEIGHT",
                                                   "MINIMAL", "DEFERRED", "SIMPLE"):
                out["tiers"][k.upper()] = v
        # Also try the legacy frontmatter "tier_distribution:" flattened form
        if not out["tiers"]:
            for k, v in td.items():
                if isinstance(v, int):
                    out["tiers"][k.upper()] = v
    # Last-ditch: pull from §3 Tier Assignment Summary table — | TIER | Count | Rationale |
    if not out["tiers"]:
        for m in re.finditer(r"^\|\s*\*?\*?(RIGOROUS|STANDARD|LIGHTWEIGHT|MINIMAL|DEFERRED|SIMPLE)\*?\*?\s*\|\s*\*?\*?(\d+)\*?\*?\s*\|",
                              t, re.M):
            tier = m.group(1).upper()
            count = int(m.group(2))
            out["tiers"][tier] = count
        # Also build per_subdomain from §4 per-row "Tier" column (4th col)
        for m in re.finditer(r"^\|\s*(D-\d{1,2}\.\d)[^|]*\|[^|]*\|[^|]*\|[^|]*\|\s*(RIGOROUS|STANDARD|LIGHTWEIGHT|MINIMAL|DEFERRED|SIMPLE)\s*\|",
                              t, re.M):
            sd, tier = m.group(1), m.group(2).upper()
            out["per_subdomain"][sd] = tier
    if not out["tiers"]:
        warn.append(f"{case}: parse_proportionality: 0 tiers extracted")
    return out


def parse_posture_gaps(case, cfg, warn):
    """CoverageGap nodes from phase1_graph.json (preferred) OR fallback to Doc15/Doc16.

    Returns {gaps:[{id,function,sub_domain,severity,description,recommended_disposition}]}.
    """
    out = {"gaps": []}
    g = glob_first(cfg["root"], "phase1_graph.json")
    if g:
        try:
            gd = json.loads(read(g))
            for n in gd.get("nodes", []) or []:
                if (n.get("type") or "") != "CoverageGap": continue
                attrs = n.get("attrs", {}) or {}
                out["gaps"].append({
                    "id": n.get("id") or attrs.get("id") or "",
                    "function": attrs.get("function") or attrs.get("csf_function") or "",
                    "sub_domain": attrs.get("sub_domain") or attrs.get("subdomain_id") or "",
                    "severity": attrs.get("severity") or "MEDIUM",
                    "description": attrs.get("description") or n.get("label") or "",
                    "recommended_disposition": attrs.get("recommended_disposition") or attrs.get("disposition") or "",
                })
        except json.JSONDecodeError:
            warn.append(f"{case}: phase1_graph.json unparsable in parse_posture_gaps")
    if out["gaps"]:
        return out
    # Fallback: Doc15/Doc16 strategic tensions
    fname = DOC_P1_TENSIONS.get(case)
    if fname:
        rel = f"{cfg['root']}/02_PHASE2_RULES_RICH/{fname}"
        if not (REPO / rel).exists():
            rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{fname}"
        t = read(rel)
        if t:
            for m in re.finditer(
                r"^##\s+(T-[A-Z0-9-]+)\b\s*[—:-]?\s*([^\n]*)", t, re.M):
                tid = m.group(1).strip()
                title = m.group(2).strip()
                out["gaps"].append({
                    "id": tid, "function": "Cross-cutting", "sub_domain": "",
                    "severity": "MEDIUM",
                    "description": title,
                    "recommended_disposition": "",
                })
            if out["gaps"]:
                return out
    warn.append(f"{case}: parse_posture_gaps: no gaps extracted")
    return out if out["gaps"] else None


def parse_stakeholders(case, cfg, warn):
    """Doc07 — extract named roles (stakeholders) and their RACI activity assignments.

    Returns {stakeholders:[{id,name,role,raci:{activity:R|A|C|I}}]}.
    """
    rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{DOC_P1_ORG_RACI}"
    t = read(rel)
    if not t:
        warn.append(f"{case}: {DOC_P1_ORG_RACI} missing (parse_stakeholders)")
        return None
    out = {"stakeholders": []}
    # Heuristic 1: Section "## 2. Key Roles" with bullet list of role names.
    # Many RACI docs use a table per role; we capture role names + their CISO/DPO/CRO aliases.
    role_section = re.search(r"^##\s+2\.\s+Key Roles(.*?)(?=^##\s|\Z)", t, re.M | re.S)
    if role_section:
        body = role_section.group(1)
        for m in re.finditer(r"^\s*-\s+\*\*([^*]+?)\*\*\s*[—:-]?\s*([^\n]*)", body, re.M):
            role_name = m.group(1).strip()
            role_desc = m.group(2).strip()
            out["stakeholders"].append({
                "id": f"ROLE-{len(out['stakeholders']) + 1:02d}",
                "name": role_name,
                "role": role_desc or role_name,
                "raci": {},
            })
    # Heuristic 2: scan RACI matrices — | Activity | R1 | R2 | ... | — extract
    # column headers as role names; row key as activity; cell value as RACI code.
    # We pick the first such matrix.
    raci_blocks = re.findall(
        r"(?:RACI\|[^\n]*\n)((?:\|[^\n]*\n)+)", t)
    if raci_blocks:
        # Use the first block to add RACI mappings back to the existing stakeholders
        block = raci_blocks[0]
        lines = [ln for ln in block.strip().split("\n") if ln.strip().startswith("|")]
        if len(lines) >= 3:
            header = [c.strip() for c in lines[0].strip("|").split("|")]
            # Identify role columns (anything containing CISO/DPO/CRO/CEO/etc.)
            role_cols = []
            for i, h in enumerate(header):
                if i == 0:
                    continue  # activity column
                # match against stakeholder names
                for s in out["stakeholders"]:
                    short = s["name"].split("(")[0].strip()
                    if short and (short[:6].lower() in h.lower() or h.lower().startswith(short[:4].lower())):
                        role_cols.append((i, s["id"]))
                        break
            # Map activity rows
            for ln in lines[2:]:
                cells = [c.strip() for c in ln.strip("|").split("|")]
                if not cells: continue
                activity = cells[0]
                if not activity: continue
                for col_idx, stake_id in role_cols:
                    if col_idx >= len(cells): continue
                    code = cells[col_idx].strip().upper()
                    if code in ("R", "A", "C", "I"):
                        for s in out["stakeholders"]:
                            if s["id"] == stake_id:
                                s["raci"][activity] = code
                                break
    if not out["stakeholders"]:
        warn.append(f"{case}: parse_stakeholders: 0 stakeholders extracted")
    return out


def parse_business_goals(case, cfg, warn):
    """Doc03 Company Context — extract BG-NNN business goals.

    Returns {goals:[{id,name,priority}]}.

    C1 BG table: | BG-01 | name | description | HIGH | GDPR | metrics | ...
    C2/C3: | BG-001 | name | priority | ...
    """
    rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{DOC_P1_COMPANY_CONTEXT}"
    t = read(rel)
    if not t:
        warn.append(f"{case}: {DOC_P1_COMPANY_CONTEXT} missing (parse_business_goals)")
        return None
    out = {"goals": []}
    # Try 3-col grammar first (C2/C3): | BG-001 | name | priority |
    for m in re.finditer(r"^\|\s*(BG-\d{2,3})\s*\|\s*([^|]+?)\s*\|\s*([A-Z]+)\s*\|", t, re.M):
        out["goals"].append({
            "id": m.group(1).strip(),
            "name": m.group(2).strip()[:140],
            "priority": m.group(3).strip(),
        })
        if len(out["goals"]) >= 30: break
    # Fallback: capture any | BG-NN | ... | row, take col 2 as name and look for CRITICAL/HIGH/MEDIUM/LOW
    if not out["goals"]:
        for m in re.finditer(r"^\|\s*(BG-\d{2,3})\s*\|\s*([^|]+)", t, re.M):
            name = m.group(2).strip()[:140]
            pri = ""
            for tok in ("CRITICAL", "HIGH", "MEDIUM", "LOW"):
                if tok in name.upper():
                    pri = tok
                    break
            out["goals"].append({
                "id": m.group(1).strip(),
                "name": name,
                "priority": pri or "MEDIUM",
            })
            if len(out["goals"]) >= 30: break
    if not out["goals"]:
        warn.append(f"{case}: parse_business_goals: 0 BG rows extracted")
    return out


def parse_third_party(case, cfg, warn):
    """Doc06 — extract vendor rows (cloud, hardware, SaaS sections).

    Returns {vendors:[{id,name,type,data_processed,sbom_ref}]}.
    """
    rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{DOC_P1_THIRD_PARTY}"
    t = read(rel)
    if not t:
        warn.append(f"{case}: {DOC_P1_THIRD_PARTY} missing (parse_third_party)")
        return None
    out = {"vendors": []}
    # Header pattern (Doc06 cloud section):
    # | Provider | Service | Data Accessed | Region | Contract Basis | DPA | Art 28 | Exit |
    for m in re.finditer(
        r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", t, re.M):
        a, b, c = (s.strip() for s in m.groups())
        # Skip header / separator rows
        if a.lower() in ("provider", "vendor", "---", ""): continue
        if set(a) <= {"-", " "}: continue
        # Heuristic: vendor name column is the first cell of a substantive row
        if len(a) < 2 or len(a) > 200: continue
        out["vendors"].append({
            "id": f"V-{len(out['vendors']) + 1:03d}",
            "name": a,
            "type": b[:80],
            "data_processed": c[:140],
            "sbom_ref": "",
        })
        if len(out["vendors"]) >= 60: break
    if not out["vendors"]:
        warn.append(f"{case}: parse_third_party: 0 vendor rows extracted")
    return out


def parse_adjusted_goals(case, cfg, warn):
    """Doc13/Doc14 Adjusted Goals — §5 NIST controls table OR §2 multi-reg table.

    For sub-domains we synthesise a goal record {id:'AG-D-XX.Y', type:'PG'|'SG',
    name, nist_anchors:[...], source:Doc13|Doc14}. Top 80.
    """
    fname = DOC_P1_ADJUSTED_GOALS.get(case)
    if not fname:
        warn.append(f"{case}: adjusted goals filename unknown for {case}")
        return None
    rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{fname}"
    t = read(rel)
    if not t:
        warn.append(f"{case}: {fname} missing (parse_adjusted_goals)")
        return None
    out = {"goals": []}
    # §5 NIST Controls table (preferred — has explicit anchors)
    for m in re.finditer(
        r"^\|\s*(D-\d{1,2}\.\d)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"
        r"\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|",
        t, re.M):
        sub, name, regs, csf, pf, ai = (s.strip() for s in m.groups())
        if sub.lower() == "sub-domain" or set(sub) <= {"-"}: continue
        anchors = []
        for raw in (csf, pf, ai):
            if not raw or raw == "—": continue
            for tok in re.split(r"[,;]", raw):
                tok = re.sub(r";\s*", "", tok).strip().rstrip(",")
                if tok and re.match(r"^[A-Z]{2}\.[A-Z]{2}-\d", tok):
                    anchors.append(tok)
        out["goals"].append({
            "id": f"AG-{sub}",
            "type": "AG",
            "name": name[:120],
            "sub_domain": sub,
            "nist_anchors": anchors[:12],
            "source": fname.replace("Doc", "Doc").replace(".md", ""),
        })
        if len(out["goals"]) >= 80: break
    # Fallback: §2 multi-reg table if §5 was empty. Match `| D-XX.Y | name |` rows.
    if not out["goals"]:
        for m in re.finditer(r"^\|\s*(D-\d{1,2}\.\d)[^|\n]*\|([^|\n]+)", t, re.M):
            sub = m.group(1).strip()
            name = m.group(2).strip()[:120]
            if sub.lower() == "sub-domain" or set(sub) <= {"-"}: continue
            if name.startswith("—") or "`" in name[:5]:
                # Skip rows whose second column is a SO-D-XX.Y code or em-dash
                continue
            out["goals"].append({
                "id": f"PG-{sub}",
                "type": "PG",
                "name": name,
                "sub_domain": sub,
                "nist_anchors": [],
                "source": fname.replace(".md", ""),
            })
            if len(out["goals"]) >= 80: break
    if not out["goals"]:
        warn.append(f"{case}: parse_adjusted_goals: 0 goals extracted")
    return out


def parse_citations_rows(case, cfg, warn):
    """Citation_Index.md — extract citation rows.

    Returns {citations:[{id,article,source_doc,referenced_by}]}.

    Two layouts supported:
      (a) C1: "## §2 GDPR Citations" + rows of form
          `| Art. NN | N doc(s) | `domains/...` |`
      (b) C2/C3: "## 2. GDPR Citations" + rows of form
          `| GDPR Art. NN | `corpus/file.md` | Title |`
          OR "## GDPR Citations" + same row format.
    When the Citation_Index.md has no per-row tables (C3 MAX case), we fall
    back to extracting Art. NN mentions from Doc09_Ambiguity_Register.md.
    """
    rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{DOC_P1_CITATION_INDEX}"
    t = read(rel)
    if not t:
        warn.append(f"{case}: {DOC_P1_CITATION_INDEX} missing (parse_citations_rows)")
        return None
    out = {"citations": []}
    current_reg = ""
    # Track regulation by walking §N Regulation Citations headings
    lines = t.split("\n")
    for line in lines:
        # Regulation section heading: e.g. "## §2 GDPR Citations" or "## 2. GDPR Citations"
        m_sec = re.match(r"^##\s+(?:§\d+|\d+\.)\s+([A-Za-z][A-Za-z0-9 _]*?)\s+Citations?\s*$", line)
        if m_sec:
            current_reg = m_sec.group(1).strip()
            continue
        m_sec2 = re.match(r"^##\s+([A-Z]{2,}[\w]*)\s+Citations?\s*$", line)
        if m_sec2:
            current_reg = m_sec2.group(1).strip()
            continue
        # Article row (C1 format): | Art. 32 | 5 doc(s) | `domains/...` |
        m_art = re.match(r"^\|\s*(Art\.\s*\d+[a-z]?(?:\([0-9a-z]+\))*|Annex\s+[IVX]+(?:[^|]*?)?|Recital\s+\d+)\s*\|"
                          r"\s*(\d+\s*doc\(s\)|[^|]*?)\s*\|\s*`?([^|`]+?)`?\s*\|",
                          line)
        if m_art:
            article = m_art.group(1).strip()
            count_txt = m_art.group(2).strip()
            corpus_path = m_art.group(3).strip()
            out["citations"].append({
                "id": f"CIT-{len(out['citations']) + 1:03d}",
                "regulation": current_reg or "?",
                "article": article,
                "source_doc": corpus_path[:120],
                "referenced_by": count_txt[:120],
            })
            if len(out["citations"]) >= 200:
                break
            continue
        # Reference row (C2/C3 format): | GDPR Art. 17 | `corpus/file.md` | Title |
        m_ref = re.match(r"^\|\s*((?:GDPR|CRA|NIS\s?2|DORA|AI\s?Act)\s+Art\.\s*\d+[a-z]?(?:\([0-9a-z]+\))*|"
                          r"Annex\s+[IVX]+(?:[^|]*?)?)\s*\|\s*`([^`]+)`\s*\|", line)
        if m_ref:
            article = m_ref.group(1).strip()
            corpus_path = m_ref.group(2).strip()
            # Derive regulation from article prefix
            reg = "GDPR" if article.startswith("GDPR") else (
                "CRA" if article.startswith("CRA") else (
                    "NIS 2" if article.startswith("NIS") else (
                        "DORA" if article.startswith("DORA") else (
                            "AI Act" if article.startswith("AI") else current_reg or "?"))))
            out["citations"].append({
                "id": f"CIT-{len(out['citations']) + 1:03d}",
                "regulation": reg,
                "article": article,
                "source_doc": corpus_path[:120],
                "referenced_by": "",
            })
            if len(out["citations"]) >= 200:
                break
    # Fallback: Doc09_Ambiguity_Register.md (C3 MAX case)
    if not out["citations"]:
        doc09 = read(f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{DOC_P1_AMBIGUITY}")
        if doc09:
            seen = set()
            for m in re.finditer(r"^\s*-\s*\*\*(?:Citation|Article|Provision|Anchor)\*\*\s*:?\s*([^\n]+)",
                                  doc09, re.M):
                txt = m.group(1)
                art = re.search(r"Art\.\s*\d+[a-z]?(?:\([0-9a-z]+\))?", txt)
                if not art: continue
                a = art.group(0)
                if a in seen: continue
                seen.add(a)
                out["citations"].append({
                    "id": f"CIT-{len(out['citations']) + 1:03d}",
                    "regulation": "—",
                    "article": a,
                    "source_doc": "Doc09_Ambiguity_Register",
                    "referenced_by": txt[:120],
                })
                if len(out["citations"]) >= 100:
                    break
    if not out["citations"]:
        warn.append(f"{case}: parse_citations_rows: 0 rows extracted")
    return out


def parse_architecture(case, cfg, warn):
    """Doc04 — System inventory + data assets.

    Returns {systems:[{id,name,trust_boundary,data_assets:[{id,classification}]}]}.
    """
    rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{DOC_P1_ARCHITECTURE}"
    t = read(rel)
    if not t:
        warn.append(f"{case}: {DOC_P1_ARCHITECTURE} missing (parse_architecture)")
        return None
    out = {"systems": []}
    # SYS-NN rows: | SYS-01 | Core Banking System ... | Critical | Y |
    for m in re.finditer(
        r"^\|\s*(SYS-\d{1,3})\s*\|\s*([^|]+?)\s*\|", t, re.M):
        sid = m.group(1).strip()
        name = m.group(2).strip()[:120]
        out["systems"].append({
            "id": sid,
            "name": name,
            "trust_boundary": "Internal (EU)",
            "data_assets": [],
        })
        if len(out["systems"]) >= 80: break
    # Tag data assets: each system's data_assets list is left empty here —
    # the dashboard table renders the system list only. (Doc04 has no clean
    # per-system data-asset table; filling it would require synthesis that
    # crosses the "no invented content" rule.)
    if not out["systems"]:
        warn.append(f"{case}: parse_architecture: 0 systems extracted")
    return out


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
    # R8 — call the 12 new P1 parsers. Each returns its dict OR None when the
    # source file is missing/empty; we record None in the payload and add a
    # warning so the dashboard can render an empty-state placeholder.
    p1_extensions = {
        "regulations":  parse_regulations(case, cfg, warn),
        "nist_controls": parse_nist_controls(case, cfg, warn),
        "clause_mapping": parse_clause_mapping(case, cfg, warn),
        "dora":         parse_dora(case, cfg, warn),
        "proportionality": parse_proportionality(case, cfg, warn),
        "posture_gaps": parse_posture_gaps(case, cfg, warn),
        "stakeholders": parse_stakeholders(case, cfg, warn),
        "business_goals": parse_business_goals(case, cfg, warn),
        "third_party":  parse_third_party(case, cfg, warn),
        "adjusted_goals": parse_adjusted_goals(case, cfg, warn),
        "citations_rows": parse_citations_rows(case, cfg, warn),
        "architecture": parse_architecture(case, cfg, warn),
    }
    none_keys = sorted(k for k, v in p1_extensions.items() if v is None)
    if none_keys:
        warn.append(f"{case}: R8 P1 parsers returned None: {','.join(none_keys)}")
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
        # R8 — 12 new P1 extension dicts (each None when source file missing)
        "regulations": p1_extensions["regulations"],
        "nist_controls": p1_extensions["nist_controls"],
        "clause_mapping": p1_extensions["clause_mapping"],
        "dora": p1_extensions["dora"],
        "proportionality": p1_extensions["proportionality"],
        "posture_gaps": p1_extensions["posture_gaps"],
        "stakeholders": p1_extensions["stakeholders"],
        "business_goals": p1_extensions["business_goals"],
        "third_party": p1_extensions["third_party"],
        "adjusted_goals": p1_extensions["adjusted_goals"],
        "citations_rows": p1_extensions["citations_rows"],
        "architecture": p1_extensions["architecture"],
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
# R6 — Full-card drill-down parsers (per-row "detail" blocks)
# ---------------------------------------------------------------------------
# Each parser reads the source corpus document and returns a dict
# keyed by id -> {sections:[{title, body}], fields:{k:v}, diagram?:str}.
# When a card is missing for an id, the value is None.
# ---------------------------------------------------------------------------

# Per-case P2 rule catalog filenames (used by parse_rule_cards)
DOC_P2_RULES_CATALOG = {
    "Case_01_TinyTask_SaaS": ("02_PHASE2_RULES_RICH", "Doc18_Rules_Catalog.md"),
    "Case_02_SecureBorder_Solutions": ("02_PHASE2_RULES_RICH", "Doc18_Rules_Catalog.md"),
    "Case_03_OmniBank_Financial": ("02_PHASE2_RULES_RICH", "Doc19_Rules_Catalog.md"),
}


def _split_md_sections(body, start_level=5):
    """Split a markdown body at headings `start_level`..6 (#-counts).

    Returns list of (level, heading_title, body_lines_after_heading).
    The list is in document order; headings are kept inline with their content.
    """
    sections = []
    cur_level, cur_title, cur_lines = None, None, []
    for line in (body or "").split("\n"):
        m = re.match(r"^(#{3,6})\s+(.*)$", line)
        if m:
            # Flush (use a snapshot copy to avoid aliasing)
            if cur_level is not None:
                sections.append((cur_level, cur_title, list(cur_lines)))
            cur_level = len(m.group(1))
            cur_title = m.group(2).strip()
            cur_lines = []
        else:
            cur_lines.append(line)
    if cur_level is not None:
        sections.append((cur_level, cur_title, list(cur_lines)))
    return sections


def _strip_sequence_diagram_pointer(lines):
    """Drop the standalone sequence-diagram pointer line that RUP cards carry."""
    out = []
    for ln in lines:
        if re.match(r"^\s*>\s*\*\*Sequence diagram:\*\*", ln):
            continue
        out.append(ln)
    return out


def parse_uc_cards(case, cfg, warn):
    """R6.1 — parse UC cards (fully-dressed RUP + compact §3 forms).

    Returns {id: {sections:[{title, body}], fields:{}, diagram?:str} | None}.
    """
    text = read(f"{cfg['root']}/{cfg['catalog']}")
    if not text:
        warn.append(f"{case}: UC catalog missing for R6 parse ({cfg['catalog']})")
        return {}
    out = {}
    # Split on #### Use-Case or #### UC-NN
    blocks = re.split(r"(?m)^####\s+(.*)$", text)
    # blocks: [pre, head1, body1, head2, body2, ...]
    SECTION_TITLES_RUP = {
        1: "Brief Description",
        2: "Actor Brief Descriptions",
        3: "Preconditions",
        4: "Basic Flow",
        5: "Alternative Flows",
        6: "Subflows",
        7: "Key Scenarios",
        8: "Post-conditions",
        9: "Special Requirements",
        10: "Security & Compliance Annex",
    }
    i = 1
    while i < len(blocks):
        heading = blocks[i].strip()
        body = blocks[i + 1] if i + 1 < len(blocks) else ""
        i += 2
        # Two heading grammars
        m_rup = re.match(r"^Use-Case:\s*\{([^}]+)\}\s*(.+)?$", heading)
        m_cmp = re.match(r"^(UC-\d+)\s+[—-]\s+(.+)$", heading)
        if m_rup:
            uc_id = m_rup.group(1).strip()
            title = (m_rup.group(2) or "").strip()
            body_lines = _strip_sequence_diagram_pointer(body.split("\n"))
            # Drop the front-matter block (the id and title echo lines) if present
            body_lines = [ln for ln in body_lines if not re.match(r"^\s*\*\*(Use-Case Id|Title|Primary Actor)\*\*", ln)]
            # Walk sub-headings ##### N to build sections
            sub = _split_md_sections("\n".join(body_lines), start_level=5)
            sections = []
            for lvl, h, lines in sub:
                if lvl != 5:
                    continue
                # Strip leading "N " or "N.N " tokens
                m_num = re.match(r"^(\d+)\.?\s*(.*)$", h)
                if not m_num:
                    continue
                num = int(m_num.group(1))
                ttl = SECTION_TITLES_RUP.get(num, m_num.group(2).strip() or h)
                body_txt = "\n".join(lines).strip("\n")
                if not body_txt.strip():
                    continue
                sections.append({"title": ttl, "body": body_txt})
            out[uc_id] = {"sections": sections, "fields": {}, "title": title}
        elif m_cmp:
            uc_id = m_cmp.group(1).strip()
            title = m_cmp.group(2).strip()
            # Compact card — extract **Label:** value pairs and put rest in one "Card" section
            fields = {}
            leftover = []
            for ln in body.split("\n"):
                m_f = re.match(r"^\s*-\s+\*\*(.+?):\*\*\s*(.+?)\s*$", ln)
                if m_f:
                    fields[m_f.group(1).strip()] = m_f.group(2).strip()
                else:
                    leftover.append(ln)
            leftover_txt = "\n".join(leftover).strip()
            sections = []
            if leftover_txt:
                sections.append({"title": "Card", "body": leftover_txt})
            out[uc_id] = {"sections": sections, "fields": fields, "title": title}
    return out


def parse_rule_cards(case, cfg, warn):
    """R6.2 — parse Rule cards (1..18 numbered fields). C1/C2 only; C3 returns {}."""
    out = {}
    if case == "Case_03_OmniBank_Financial":
        return out
    rel = DOC_P2_RULES_CATALOG.get(case)
    if not rel:
        return out
    text = read(f"{cfg['root']}/{rel[0]}/{rel[1]}")
    if not text:
        warn.append(f"{case}: rules catalog missing for R6 parse ({rel[0]}/{rel[1]})")
        return out
    # C1/C2 rule headings: ### CR-D-XX.X-NNN — Title  (8.N cards not present as ###)
    blocks = re.split(r"(?m)^###\s+(CR-D-\d{2}\.\d+-\d+)\s+[—-]\s+([^\n]+)$", text)
    i = 1
    while i < len(blocks):
        rid = blocks[i].strip()
        title = blocks[i + 1].strip() if i + 1 < len(blocks) else ""
        body = blocks[i + 2] if i + 2 < len(blocks) else ""
        i += 3
        # Numbered fields are at start-of-line "1. **Description**" etc.
        sections = []
        # Split body by numbered heading lines
        chunks = re.split(r"(?m)^(\d+)\.\s+\*\*([^*]+?)\*\*", body)
        # chunks: [pre, num1, label1, body1, num2, label2, body2, ...]
        j = 1
        while j < len(chunks):
            num = chunks[j]
            label = chunks[j + 1] if j + 1 < len(chunks) else ""
            body_txt = chunks[j + 2] if j + 2 < len(chunks) else ""
            j += 3
            body_clean = body_txt.strip("\n").rstrip()
            if not body_clean:
                continue
            sections.append({"title": f"{num}. {label.strip()}", "body": body_clean})
        out[rid] = {"sections": sections, "fields": {}, "title": title}
    return out


def _detect_fr_doc(case, cfg, kind="fr"):
    """Find the FR or NFR doc path for the case by content sniffing."""
    p3 = cfg["p3_dir"]
    root = cfg["root"]
    req_dir = REPO / root / p3 / "requirements"
    if not req_dir.exists():
        return None
    if kind == "fr":
        pattern = re.compile(r"^####?\s*FR-", re.M)
    else:
        pattern = re.compile(r"^####?\s*NFR-", re.M)
    # Prefer the file whose content matches
    candidates = list(req_dir.glob("*.md"))
    for p in candidates:
        try:
            t = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if pattern.search(t):
            return str(p.relative_to(REPO))
    # Fall back to the conventional filename
    fallback = {
        "Case_01_TinyTask_SaaS": {"fr": f"{p3}/requirements/Doc29_Functional_Requirements.md",
                                  "nfr": f"{p3}/requirements/Doc31_Non_Functional_Requirements.md"},
        "Case_02_SecureBorder_Solutions": {"fr": f"{p3}/requirements/Doc29_Functional_Requirements.md",
                                           "nfr": f"{p3}/requirements/Doc30_Non_Functional_Requirements.md"},
        "Case_03_OmniBank_Financial": {"fr": f"{p3}/requirements/Doc30_Functional_Requirements.md",
                                      "nfr": f"{p3}/requirements/Doc31_Non_Functional_Requirements.md"},
    }
    return fallback.get(case, {}).get(kind)


def parse_req_cards(case, cfg, warn):
    """R6.3 — parse FR / NFR cards. C1 fully dressed, C3 table rows, C2 rows only."""
    out = {"fr": {}, "nfr": {}}
    fr_rel = _detect_fr_doc(case, cfg, "fr")
    nfr_rel = _detect_fr_doc(case, cfg, "nfr")
    # FR
    if fr_rel:
        t = read(fr_rel)
        if t:
            if case == "Case_01_TinyTask_SaaS":
                # Heading: ### FR-NN — Title [priority=..., fields=N]
                # Capture id + the trailing bracket block + everything to next ###
                blocks = re.split(r"(?m)^###\s+(FR-\d{1,3})\s+[—-]\s+(.*)$", t)
                i = 1
                while i < len(blocks):
                    rid = blocks[i].strip()
                    heading_rest = blocks[i + 1] if i + 1 < len(blocks) else ""
                    body = blocks[i + 2] if i + 2 < len(blocks) else ""
                    i += 3
                    # heading_rest = "Title [priority=..., fields=N]" or just "Title"
                    m_head = re.match(r"^([^\[]*?)\s*(\[[^\]]*\])?\s*$", heading_rest.strip())
                    title = (m_head.group(1).strip() if m_head else heading_rest.strip())
                    fields = {}
                    leftover = []
                    for ln in body.split("\n"):
                        m_f = re.match(r"^\s*\*\*([^*]+?):\*\*\s*(.+?)\s*$", ln)
                        if m_f:
                            fields[m_f.group(1).strip()] = m_f.group(2).strip()
                        else:
                            leftover.append(ln)
                    leftover_txt = "\n".join(leftover).strip()
                    sections = []
                    desc = fields.pop("Description", None)
                    if desc:
                        sections.append({"title": "Description", "body": desc})
                    if leftover_txt:
                        sections.append({"title": "Details", "body": leftover_txt})
                    out["fr"][rid] = {"sections": sections, "fields": fields, "title": title}
            elif case == "Case_03_OmniBank_Financial":
                # Heading: #### FR-NN: Title + | Field | Value | table
                blocks = re.split(r"(?m)^####\s+(FR-\d+):\s+([^\n]+)$", t)
                i = 1
                while i < len(blocks):
                    rid = blocks[i].strip()
                    title = blocks[i + 1].strip() if i + 1 < len(blocks) else ""
                    body = blocks[i + 2] if i + 2 < len(blocks) else ""
                    i += 3
                    fields = {}
                    for m in re.finditer(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|\s*$", body, re.M):
                        fields[m.group(1).strip()] = m.group(2).strip()
                    desc = fields.get("FR Description", "")
                    sections = []
                    if desc:
                        sections.append({"title": "FR Description", "body": desc})
                    out["fr"][rid] = {"sections": sections, "fields": fields, "title": title}
            # C2: rows only — leave empty (we still capture any heading-form FR)
            blocks = re.split(r"(?m)^###\s+(FR-\d+)\s+[—-]\s+([^\n]+)$", t)
            i = 1
            while i < len(blocks):
                rid = blocks[i].strip()
                title = blocks[i + 1].strip() if i + 1 < len(blocks) else ""
                body = blocks[i + 2] if i + 2 < len(blocks) else ""
                i += 3
                if rid not in out["fr"]:
                    out["fr"][rid] = {"sections": [], "fields": {}, "title": title}
    # NFR
    if nfr_rel:
        t = read(nfr_rel)
        if t:
            if case == "Case_01_TinyTask_SaaS":
                blocks = re.split(r"(?m)^###\s+(NFR-\d{1,3})\s+[—-]\s+(.*)$", t)
                i = 1
                while i < len(blocks):
                    rid = blocks[i].strip()
                    heading_rest = blocks[i + 1] if i + 1 < len(blocks) else ""
                    body = blocks[i + 2] if i + 2 < len(blocks) else ""
                    i += 3
                    m_head = re.match(r"^([^\[]*?)\s*(\[[^\]]*\])?\s*$", heading_rest.strip())
                    title = (m_head.group(1).strip() if m_head else heading_rest.strip())
                    fields = {}
                    leftover = []
                    for ln in body.split("\n"):
                        m_f = re.match(r"^\s*\*\*([^*]+?):\*\*\s*(.+?)\s*$", ln)
                        if m_f:
                            fields[m_f.group(1).strip()] = m_f.group(2).strip()
                        else:
                            leftover.append(ln)
                    leftover_txt = "\n".join(leftover).strip()
                    sections = []
                    desc = fields.pop("Description", None)
                    if desc:
                        sections.append({"title": "Description", "body": desc})
                    if leftover_txt:
                        sections.append({"title": "Details", "body": leftover_txt})
                    out["nfr"][rid] = {"sections": sections, "fields": fields, "title": title}
            elif case == "Case_03_OmniBank_Financial":
                blocks = re.split(r"(?m)^####\s+(NFR-[\w-]+):\s+([^\n]+)$", t)
                i = 1
                while i < len(blocks):
                    rid = blocks[i].strip()
                    title = blocks[i + 1].strip() if i + 1 < len(blocks) else ""
                    body = blocks[i + 2] if i + 2 < len(blocks) else ""
                    i += 3
                    fields = {}
                    for m in re.finditer(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|\s*$", body, re.M):
                        fields[m.group(1).strip()] = m.group(2).strip()
                    desc = fields.get("NFR Description") or fields.get("Description", "")
                    sections = []
                    if desc:
                        sections.append({"title": "NFR Description", "body": desc})
                    out["nfr"][rid] = {"sections": sections, "fields": fields, "title": title}
    return out


def parse_threat_cards(case, cfg, warn):
    """R6.4 — parse RISK-NN (17 fields) and THR-... (12 fields) cards. C1 only rich."""
    out = {}
    if case != "Case_01_TinyTask_SaaS":
        return out
    paths = doc_p3_paths(case, cfg)
    t = read(paths.get("risks"))
    if not t:
        warn.append(f"{case}: risks doc missing for R6 parse ({paths.get('risks')})")
        return out
    # Match both RISK-NN and THR-XXX-NN at ### level
    blocks = re.split(r"(?m)^###\s+((?:RISK|THR)-[\w-]+)\s+[—-]\s+([^\n]+?)\s*\[", t)
    i = 1
    while i < len(blocks):
        rid = blocks[i].strip()
        title = blocks[i + 1].strip() if i + 1 < len(blocks) else ""
        body = blocks[i + 2] if i + 2 < len(blocks) else ""
        i += 3
        fields = {}
        leftover = []
        for ln in body.split("\n"):
            m_f = re.match(r"^\s*\*\*([^*]+?):\*\*\s*(.+?)\s*$", ln)
            if m_f:
                fields[m_f.group(1).strip()] = m_f.group(2).strip()
            else:
                leftover.append(ln)
        leftover_txt = "\n".join(leftover).strip()
        sections = []
        desc = fields.pop("Description", None) or fields.pop("Threat", None)
        if desc:
            sections.append({"title": "Description", "body": desc})
        if leftover_txt:
            sections.append({"title": "Details", "body": leftover_txt})
        out[rid] = {"sections": sections, "fields": fields, "title": title}
    return out


def parse_ambiguity_cards(case, cfg, warn):
    """R6.5 — parse Doc09 ambiguity Card / Resolution blocks."""
    out = {}
    rel = f"{cfg['root']}/01_PHASE1_CONTEXT_RICH/{DOC_P1_AMBIGUITY}"
    t = read(rel)
    if not t:
        warn.append(f"{case}: Doc09 missing for R6 parse")
        return out
    # Split on #### Card #N: ... and #### Resolution (per card N): ...
    lines = t.split("\n")
    cur_id = None
    cur_id_value = None  # extracted clause id from heading (e.g. GDPR-CL23)
    cur_card_body = []
    cur_resolution = None
    cur_res_body = []
    cur_kind = None  # "card" or "resolution"

    def flush():
        nonlocal cur_id, cur_id_value, cur_card_body, cur_resolution, cur_res_body, cur_kind
        if cur_id is not None:
            card_text = "\n".join(cur_card_body).strip()
            res_text = "\n".join(cur_res_body).strip()
            sections = []
            fields = {}
            if card_text:
                sections.append({"title": "Card", "body": card_text})
            if res_text:
                sections.append({"title": "Resolution", "body": res_text})
            # Pull common bold-label lines into fields
            for ln in (cur_card_body + cur_res_body):
                m_f = re.match(r"^\s*-\s+\*\*(.+?):\*\*\s*(.+?)\s*$", ln)
                if m_f:
                    fields[m_f.group(1).strip()] = m_f.group(2).strip()
            # Key by extracted clause id when present, else by ordinal "Card N"
            key = cur_id_value if cur_id_value else f"Card {cur_id}"
            out[key] = {"sections": sections, "fields": fields, "title": f"Card #{cur_id}: {cur_id_value or ''}".strip()}
        cur_id = None
        cur_id_value = None
        cur_card_body = []
        cur_res_body = []
        cur_kind = None

    card_re = re.compile(r"^####\s+Card\s*#(\d+):\s+(.+?)\s*$")
    res_re = re.compile(r"^####\s+Resolution\s*(?:\(per card (\d+)\))?\s*:?\s*$")
    for ln in lines:
        m_c = card_re.match(ln)
        if m_c:
            flush()
            cur_id = m_c.group(1)
            cur_id_value = m_c.group(2).strip()
            cur_kind = "card"
            continue
        m_r = res_re.match(ln)
        if m_r:
            # Switch to resolution for current card
            cur_kind = "resolution"
            continue
        if cur_kind == "card":
            cur_card_body.append(ln)
        elif cur_kind == "resolution":
            cur_res_body.append(ln)
    flush()
    return out


def parse_lane_diagram(case, cfg, warn):
    """R6.6 — extract mermaid block for each PROC/CAP card from the lane-cards doc."""
    out = {}  # id -> diagram string
    text = read(f"{cfg['root']}/{cfg['lane_cards']}")
    if not text:
        return out
    lines = text.split("\n")
    cur_id = None
    in_mermaid = False
    buf = []
    for ln in lines:
        m_p = re.match(r"^##\s+(PROC-\d+|CAP-\d+)\s+[—-]\s+", ln)
        if m_p:
            if cur_id and buf:
                out[cur_id] = "\n".join(buf).strip("\n")
            cur_id = m_p.group(1)
            in_mermaid = False
            buf = []
            continue
        if cur_id is None:
            continue
        if re.match(r"^```mermaid\s*$", ln):
            in_mermaid = True
            continue
        if in_mermaid:
            if re.match(r"^```\s*$", ln):
                out[cur_id] = "\n".join(buf).strip("\n")
                in_mermaid = False
                buf = []
                continue
            buf.append(ln)
    if cur_id and buf and cur_id not in out:
        out[cur_id] = "\n".join(buf).strip("\n")
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
        # R6 — full-card drill-down details
        uc_cards = parse_uc_cards(case, cfg, warn)
        rule_cards = parse_rule_cards(case, cfg, warn)
        req_cards = parse_req_cards(case, cfg, warn)
        threat_cards = parse_threat_cards(case, cfg, warn)
        ambiguity_cards = parse_ambiguity_cards(case, cfg, warn)
        lane_diagrams = parse_lane_diagram(case, cfg, warn)
        # Attach detail to each row (key by id)
        # UC rows
        for u in cat["ucs"]:
            card = uc_cards.get(u["id"])
            if card is not None:
                u["detail"] = card
            else:
                u["detail"] = None
        # Rule rows
        for r in (req_full or []):  # placeholder, replaced below via p2.rules_table
            pass
        # Lane cards
        LANE_FIELD_KEYS = ("Owner", "Trigger", "Activities", "Roles",
                           "SLA / Timing", "Span", "Maturity", "Realises",
                           "Anchors", "Evidence")
        for kind in ("proc", "cap"):
            for card_obj in lane.get(kind, []) or []:
                card_detail = {
                    "sections": [{"title": k, "body": str(card_obj.get(k) or "")}
                                 for k in LANE_FIELD_KEYS if card_obj.get(k)],
                    "fields": {},
                    "title": card_obj.get("title", ""),
                }
                if card_obj.get("id") in lane_diagrams:
                    card_detail["diagram"] = lane_diagrams[card_obj["id"]]
                card_obj["detail"] = card_detail
        # Ambiguity rows — id match
        amb_keys = list(ambiguity_cards.keys())
        for idx, a in enumerate(p1_amb := p1.get("ambiguity_rows") or []):
            key = a.get("id")
            card = ambiguity_cards.get(key) if key else None
            if card is None and idx < len(amb_keys):
                # Fallback: ordinal position match
                card = ambiguity_cards.get(amb_keys[idx])
            a["detail"] = card
        # R6 — wire detail onto p2.rules_table, p3.fr/nfr/threat rows
        for r in (p2.get("rules_table") or []):
            r["detail"] = rule_cards.get(r.get("id")) if r.get("id") else None
        for r in (req_full.get("fr_table") or []):
            r["detail"] = req_cards["fr"].get(r.get("id")) if r.get("id") else None
        for r in (req_full.get("nfr_table") or []):
            r["detail"] = req_cards["nfr"].get(r.get("id")) if r.get("id") else None
        for r in (threat_table or []):
            r["detail"] = threat_cards.get(r.get("id")) if r.get("id") else None
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
