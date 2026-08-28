#!/usr/bin/env python3
"""Port Fase 5 (Case_03): Doc20 → Control Set v1 transform + annexes."""
import re
from collections import defaultdict

P = "02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/Doc20_Rules_Catalog.md"
src = open(P, encoding="utf-8").read()
lines = src.split("\n")

def status(txt):
    m = re.match(r"cur (\d)/4 → tgt (\d)/4", txt.strip())
    if not m:
        return txt.strip()
    c, t = int(m.group(1)), int(m.group(2))
    if c >= t:
        return "IMPLEMENTED"
    if c == 0:
        return "NOT IMPLEMENTED"
    return "PARTIAL"

out = []
section = None
n_cr = n_bpr = 0
for idx, ln in enumerate(lines):
    if ln.startswith("## 4. COMPLIANCE"):
        section = "CR"
    elif ln.startswith("## 5. BEST PRACTICE"):
        section = "BPR"
    elif re.match(r"^## 6\.", ln):
        section = None
    if section == "CR" and ln.startswith("| Rule ID | Rule Description | Source | Sub-Domain |"):
        w = 16
        for j in range(idx + 1, min(idx + 6, len(lines))):
            if re.match(r"^\| CR-D-", lines[j]):
                w = len([x.strip() for x in lines[j].split("|")[1:-1]])
                break
        if w == 16:
            out.append("| Rule ID | Rule Description | Source | Sub-Domain | NI | Priority | Verification | Implementation | Related Goals | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |")
        continue
    if section == "BPR" and ln.startswith("| Rule ID | Rule Description | Framework Reference | Sub-Domain |"):
        out.append("| Rule ID | Rule Description | Framework Reference | Sub-Domain | Priority | Verification | Related Compliance Rules | NI (recomputed DR-002 AVG+AI) | CSF Subcats | PF Subcats | AI RMF Subcats | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Traceability (Field 23) | Framework Anchors (Field 24) |")
        continue
    if section == "CR" and re.match(r"^\| CR-D-\d\d\.\d-\d{3} \|", ln):
        c = [x.strip() for x in ln.split("|")[1:-1]]
        if len(c) == 17:  # tables with an extra Case_03-specific column
            sd = c[3]
            f23 = f"{c[2]} → AG-D-{sd}-001/-002 → {c[8]}".replace("AG-D-D-", "AG-D-")
            out.append("| " + " | ".join(c[:14] + [status(c[14]), status(c[15]), status(c[16]), f23, "CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc21 §1 aggregate view"]) + " |")
            n_cr += 1
            continue
        if len(c) == 16:
            sd = c[3]
            f23 = f"{c[2]} → AG-D-{sd}-001/-002 → {c[8]}".replace("AG-D-D-", "AG-D-")
            out.append("| " + " | ".join(c[:13] + [status(c[13]), status(c[14]), status(c[15]), f23, "CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc21 §1 aggregate view"]) + " |")
            n_cr += 1
            continue
    if section == "BPR" and re.match(r"^\| BPR-D-\d\d\.\d-\d{3} \|", ln):
        c = [x.strip() for x in ln.split("|")[1:-1]]
        if len(c) == 15:
            sd = c[3]
            f23 = f"{c[2]} → AG-D-{sd}-001/-002 → related CRs: {c[6]}"
            out.append("| " + " | ".join(c[:11] + [status(c[11]), status(c[12]), status(c[13]), f23, "CSF/PF/AIRMF inline; ISO 27001 + SSDF → Doc21 §1 aggregate view"]) + " |")
            n_bpr += 1
            continue
    out.append(ln)

src = "\n".join(out)

# rebuild from transformed text for annex indexing
controls = []
for ln in src.split("\n"):
    c = [x.strip() for x in ln.split("|")[1:-1]]
    if c and re.match(r"^(CR|BPR)-D-\d\d\.\d-\d{3}$", c[0]) and len(c) >= 17 and "Implementation Status (CSF)" not in c[0]:
        controls.append(c)

func_idx = defaultdict(set)
for c in controls:
    for cell in c[9:13]:
        for m in re.findall(r"\b(GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b", cell):
            func_idx[m].add(c[0])

annex = ["", "## Annex A — CSF 2.0 Function Index (generated, port Fase 5)", "",
         "| Function | Controls anchoring at least one subcategory of the function |", "|---|---|"]
fname = {"GV": "GOVERN", "ID": "IDENTIFY", "PR": "PROTECT", "DE": "DETECT", "RS": "RESPOND", "RC": "RECOVER"}
for f in ["GV", "ID", "PR", "DE", "RS", "RC"]:
    ids = sorted(func_idx.get(f, []))
    annex.append(f"| {f} ({fname[f]}) | {len(ids)} controls: {', '.join(ids[:8])}{'…' if len(ids) > 8 else ''} |")
annex += ["", "## Annex B — Framework anchors (ISO 27001 / SSDF)", "",
          "Rule-level ISO 27001 and SSDF anchors are aggregated in `Doc21_Framework_Mapping_Matrix.md` §1 (columns `ISO 27001`, `SSDF`). This catalog inlines CSF/PF/AIRMF only (F24).", ""]
reg_count = defaultdict(int)
for c in controls:
    s = c[2]
    for reg, pat in [("GDPR", r"GDPR-C?\d*"), ("CRA", r"CRA-C?\d*"), ("NIS 2", r"NIS2-C?\d*"), ("DORA", r"DORA-C?\d*"), ("AI Act", r"AI-C?\d*")]:
        if re.search(pat, s):
            reg_count[reg] += 1
annex += ["## Annex C — Statutory Source Index", "",
          "Per-regulation touch count across the 78 controls:", ""]
for reg in ["GDPR", "CRA", "NIS 2", "DORA", "AI Act"]:
    annex.append(f"- **{reg}:** {reg_count.get(reg, 0)} controls")
annex.append("")

src = src.replace("## 13. VERSION HISTORY", "\n".join(annex) + "\n## 13. VERSION HISTORY", 1)
src = src.replace(
 "## 13. VERSION HISTORY\n",
 "## 13. VERSION HISTORY\n\n| Version | Date | Author | Changes |\n|---------|------|--------|---------|\n"
 "| 2.0 | 2026-08-28 | Executor (port Fase 5) | **Control Set v1.** Catalog tables carry the corrected 24-field schema mapping: maturity columns → Implementation Status (F21/F22, deterministic backfill per posture model §4), Traceability (F23: Legal → AG-D → related goals/CRs) and Framework Anchors (F24 → Doc21 §1) added; Annexes A–C appended; `validation/build_control_set.py` generates control_set.yaml (78 controls; Case_01 `'**'` status-parsing bug fixed and asserted). |\n", 1)

open(P, "w", encoding="utf-8").write(src)
print("CR:", n_cr, "BPR:", n_bpr, "controls indexed:", len(controls))
