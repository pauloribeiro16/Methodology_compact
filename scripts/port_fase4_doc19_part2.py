#!/usr/bin/env python3
"""Port Fase 4: Doc19 §4/§5.2/§6.4/V4 posture migration (part 2)."""
import re

P = "02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/Doc19_Framework_Mapping_Matrix.md"
src = open(P, encoding="utf-8").read()
lines = src.split("\n")

SUPERSEDED = """### §4.1 — Implementation Posture scale (ADOPTED, port Fase 4, 2026-08-28)

> **SUPERSEDED.** The legacy triple-maturity model (CSF Implementation Tiers
> T1–T4 at program/Function level; 0–4 per-subcategory scales on the CSF,
> Privacy FW and AI RMF axes) is superseded by
> `00_METHODOLOGY/IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md` v2.0:
>
> - States: **IMPLEMENTED** (evidence pointer mandatory) / **PARTIAL** /
>   **NOT IMPLEMENTED** ("what's missing" note mandatory), plus special
>   categories `N/A — product-security deliverable (SSDF <ID>)` and
>   `N/A — statutory obligation`.
> - Numerical maturity scores, 0–4 scales and Tier designations are
>   PROHIBITED at control and Function level (Model §9).
> - The §5.1 per-control table and the §4.5/§5.2 Function views use the
>   deterministic legacy backfill (Model §4); the historical scale
>   definitions remain in git history only.
"""

def qual(cur, tgt, just):
    if cur.strip() == tgt.strip():
        return f"**Target profile met** (legacy scale {cur}→{tgt}): {just}"
    return f"**PARTIAL — active gap to target** (legacy scale {cur}→{tgt}): {just}"

out = []
i = 0
n = len(lines)
in45 = in52 = False
while i < n:
    ln = lines[i]
    # §4.1 .. §4.4 replaced wholesale
    if ln.startswith("### §4.1 —"):
        while not lines[i].startswith("### §4.5"):
            i += 1
        out.append(SUPERSEDED)
        continue
    # §4.5 header + preamble + table
    if ln.startswith("### §4.5 —"):
        out.append("### §4.5 — Function-level qualitative implementation context (15 rows: 6 CSF + 5 Privacy + 4 AI RMF)")
        out.append("")
        out.append("> Qualitative Implementation Context per Posture Model §5: operational strengths,")
        out.append("> active remediation for PARTIAL controls, roadmap priorities. Derived from the legacy")
        out.append("> cur/tier numbers via the deterministic backfill (Model §4); legacy values quoted for")
        out.append("> traceability.")
        in45 = True
        i += 1
        continue
    if in45 and re.match(r"^\| \d+ \| ", ln) and "cur_tier" not in ln and "---" not in ln:
        c = [x.strip() for x in ln.split("|")[1:-1]]
        # | # | Framework | Function | cur | tgt | Justification |
        out.append(f"| {c[0]} | {c[1]} | {c[2]} | {qual(c[3], c[4], c[5])} |")
        i += 1
        continue
    if in45 and ln.startswith("| # | Framework | Function | cur_tier |"):
        out.append("| # | Framework | Function | Implementation Context (qualitative) |")
        out.append("|---|-----------|----------|------------------------------------------|")
        i += 1
        continue
    if in45 and ln.startswith("|---|"):
        i += 1
        continue
    if in45 and (ln.startswith("## §5") or ln.startswith("### §4.6")):
        in45 = False
    # §4.6 heatmap formula
    if ln.startswith("### §4.6 — Heatmap formula"):
        out.append("### §4.6 — Status distribution (replaces the legacy numerical heatmap)")
        out.append("")
        out.append("> The legacy heatmap formula (numerical cur/tgt gaps per axis, GREEN..RED bands)")
        out.append("> is retired with the maturity model — numerical maturity heatmaps are prohibited")
        out.append("> (Posture Model §9). The §5.1 per-control statuses distribute as follows")
        out.append("> (156 axis-cells over 52 in-scope controls): **IMPLEMENTED 54 · PARTIAL 67 ·")
        out.append("> N/A (non-AI scope / no privacy axis) 35 · NOT IMPLEMENTED 0**. Non-uniformity")
        out.append("> is intentional and gate-checked.")
        # skip old §4.6 content up to ## §5
        i += 1
        while i < n and not lines[i].startswith("## §5"):
            i += 1
        continue
    # §5.2 aggregated tiers
    if ln.startswith("### §5.2 — Per-Function aggregated tiers"):
        out.append("### §5.2 — Per-Function aggregated implementation context (15 rows)")
        in52 = True
        i += 1
        continue
    if in52 and re.match(r"^\| \d+ \| ", ln) and "---" not in ln:
        c = [x.strip() for x in ln.split("|")[1:-1]]
        # | # | Framework | Function | cur | tgt | gap | Aggregated from cards | Justification |
        if len(c) == 8:
            out.append(f"| {c[0]} | {c[1]} | {c[2]} | {c[6]} | {qual(c[3], c[4], c[7])} |")
            i += 1
            continue
    if in52 and ln.startswith("| # | Framework | Function | cur_tier |"):
        out.append("| # | Framework | Function | Aggregated from cards | Implementation Context (qualitative) |")
        out.append("|---|-----------|----------|-----------------------|------------------------------------------|")
        i += 1
        continue
    if in52 and (ln.startswith("## §6")):
        in52 = False
    out.append(ln)
    i += 1

open(P, "w", encoding="utf-8").write("\n".join(out))
print("done")
