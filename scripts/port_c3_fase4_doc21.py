#!/usr/bin/env python3
"""Port Fase 4 (Case_03): Doc21 §4/§5.1/§5.2/§6.4/V4 posture migration."""
import re

P = "02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/Doc21_Framework_Mapping_Matrix.md"
lines = open(P, encoding="utf-8").read().split("\n")

def status(cur, tgt):
    cur, tgt = cur.strip(), tgt.strip()
    if cur == "N/A" or tgt == "N/A":
        return "N/A"
    c, t = int(cur), int(tgt)
    if c >= t:
        return "IMPLEMENTED"
    if c == 0:
        return "NOT IMPLEMENTED"
    return "PARTIAL"

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
counts = {"IMPLEMENTED": 0, "PARTIAL": 0, "NOT IMPLEMENTED": 0, "N/A": 0}
n51 = 0
id_re = re.compile(r"^\| (CR-D-\d\d\.\d-\d{3}|BPR-D-\d\d\.\d-\d{3}) \|")
in45 = in52 = in_v4 = False
v4rows = 0
i = 0
n = len(lines)
while i < n:
    ln = lines[i]
    if ln.startswith("### §4.1 — CSF Implementation Tiers"):
        while i < n and not lines[i].startswith("### §4.5"):
            i += 1
        out.append(SUPERSEDED)
        continue
    if ln.startswith("### §4.5 — Tabela de avaliação"):
        out.append("### §4.5 — Function-level qualitative implementation context (15 rows: 6 CSF + 5 Privacy + 4 AI RMF)")
        out.append("")
        out.append("> Qualitative Implementation Context per Posture Model §5. Derived from the legacy")
        out.append("> cur/tier numbers via the deterministic backfill (Model §4); legacy values quoted for")
        out.append("> traceability.")
        in45 = True
        i += 1
        continue
    if in45 and re.match(r"^\| \d+ \| ", ln) and "cur_tier" not in ln and "---" not in ln:
        c = [x.strip() for x in ln.split("|")[1:-1]]
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
    if ln.startswith("### §4.6 — Heatmap formula"):
        out.append("### §4.6 — Status distribution (replaces the legacy numerical heatmap)")
        out.append("")
        out.append("> The legacy heatmap formula (numerical cur/tgt gaps per axis, GREEN..RED bands)")
        out.append("> is retired — numerical maturity heatmaps are prohibited (Posture Model §9).")
        out.append("> Per-axis status distribution of the §5.1 per-control table (234 axis-cells over")
        out.append("> 78 in-scope controls): see the counts printed at migration time, recorded in")
        out.append("> `validation/VALIDATOR_UNMAPPED_AUDIT_v0.md` addendum and the case PROJECT_STATE.")
        out.append("> Non-uniformity is intentional and gate-checked.")
        i += 1
        while i < n and not lines[i].startswith("## §5"):
            i += 1
        continue
    if ln.startswith("### §5.1 —"):
        out.append(ln)
        i += 1
        continue
    if id_re.match(ln):
        cells = [c.strip() for c in ln.split("|")[1:-1]]
        if len(cells) == 12 and re.fullmatch(r"\d+|N/A", cells[2]):
            s = [status(cells[2], cells[3]), status(cells[4], cells[5]), status(cells[6], cells[7])]
            for x in s:
                counts[x] += 1
            n51 += 1
            out.append(f"| {cells[0]} | {cells[1]} | {s[0]} | {s[1]} | {s[2]} |")
            i += 1
            continue
    if ln.startswith("| rule_id | sub_domain | cur_csf |"):
        out.append("| rule_id | sub_domain | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) |")
        out.append("|---------|-----------|------|---------|---------|")
        i += 1
        continue
    if ln.startswith("### §5.2 — Per-Function aggregated tiers"):
        out.append("### §5.2 — Per-Function aggregated implementation context (15 rows)")
        in52 = True
        i += 1
        continue
    if in52 and re.match(r"^\| \d+ \| ", ln) and "---" not in ln:
        c = [x.strip() for x in ln.split("|")[1:-1]]
        if len(c) == 8:
            out.append(f"| {c[0]} | {c[1]} | {c[2]} | {c[6]} | {qual(c[3], c[4], c[7])} |")
            i += 1
            continue
    if in52 and ln.startswith("| # | Framework | Function | cur_tier |"):
        out.append("| # | Framework | Function | Aggregated from cards | Implementation Context (qualitative) |")
        out.append("|---|-----------|----------|-----------------------|------------------------------------------|")
        i += 1
        continue
    if in52 and ln.startswith("## §6"):
        in52 = False
    if ln.startswith("### V4 —"):
        out.append("### V4 — Implementation Status overview per sub-domain (replaces the legacy numerical heatmap)")
        in_v4 = True
        i += 1
        continue
    if in_v4 and ln.startswith("| sub_domain | cur_csf |"):
        out.append("| sub_domain | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Note |")
        out.append("|------------|------|---------|---------|------|")
        i += 1
        continue
    if in_v4 and re.match(r"^\| D-\d\d\.\d \|", ln):
        c = [x.strip() for x in ln.split("|")[1:-1]]
        if len(c) >= 12:
            s1, s2, s3 = status(c[1], c[2]), status(c[3], c[4]), status(c[5], c[6])
            v4rows += 1
            note = f"backfilled from legacy {c[1]}→{c[2]} / {c[3]}→{c[4]} / {c[5]}→{c[6]} (was {c[-1]})"
            out.append(f"| {c[0]} | {s1} | {s2} | {s3} | {note} |")
            i += 1
            continue
    if in_v4 and ln.startswith("## Validation") or ln.startswith("## Version History"):
        in_v4 = False
    out.append(ln)
    i += 1

src = "\n".join(out)
src = src.replace(
 "## §4 — Modelo de Maturidade Tripla (CSF 0-4 + Privacy 0-4 + AI RMF 0-4)",
 "## §4 — Implementation Posture (adopted 2026-08-28, port Fase 4; supersedes the legacy triple-maturity model)")
src = src.replace(
 "### §6.4 — Sub-domains with low target maturity (tgt < 3)",
 "### §6.4 — Sub-domains at the STANDARD target profile (legacy tgt = 3)")
src = src.replace(
 "**No active sub-domain has tgt < 3**",
 "**No active sub-domain falls below the STANDARD target profile** (legacy tgt 3; Track B floor enforced — posture equivalent: every active sub-domain has at least PARTIAL-with-defined-target controls).")
open(P, "w", encoding="utf-8").write(src)
print("§5.1 rows:", n51, "distribution:", counts, "V4 rows:", v4rows)
