#!/usr/bin/env python3
"""Port Fase 4 part 3: Doc19 V4 heatmap rows -> status rows; text patches."""
import re

P = "02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/Doc19_Framework_Mapping_Matrix.md"
lines = open(P, encoding="utf-8").read().split("\n")

def status(cur, tgt):
    cur, tgt = cur.strip(), tgt.strip()
    if cur == "N/A" or tgt == "N/A":
        return "N/A"
    c, t = int(cur), int(tgt)
    return "IMPLEMENTED" if c >= t else ("NOT IMPLEMENTED" if c == 0 else "PARTIAL")

out, in_v4, rows = [], False, 0
for ln in lines:
    if ln.startswith("### V4 —"):
        out.append("### V4 — Implementation Status overview per sub-domain (replaces the legacy numerical heatmap)")
        in_v4 = True
        continue
    if in_v4 and ln.startswith("| sub_domain | cur_csf |"):
        out.append("| sub_domain | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) | Note |")
        out.append("|------------|------|---------|---------|------|")
        continue
    if in_v4 and re.match(r"^\| D-\d\d\.\d \|", ln):
        c = [x.strip() for x in ln.split("|")[1:-1]]
        # | sub | cc | tc | cp | tp | ca | ta | gaps... | colour |
        s1, s2, s3 = status(c[1], c[2]), status(c[3], c[4]), status(c[5], c[6])
        rows += 1
        note = f"backfilled from legacy {c[1]}→{c[2]} / {c[3]}→{c[4]} / {c[5]}→{c[6]} (was {c[-1]})"
        out.append(f"| {c[0]} | {s1} | {s2} | {s3} | {note} |")
        continue
    if in_v4 and ln.startswith("**Heatmap summary"):
        out.append("**Status overview.** Per-axis status counts derive from §5.1 (IMPLEMENTED 54 · PARTIAL 67 · N/A 35 · NOT IMPLEMENTED 0 across 156 axis-cells). No sub-domain is NOT IMPLEMENTED; the ORANGE legacy band (D-04.3, D-05.3, D-07.1, D-07.3, D-10.1) corresponds to PARTIAL controls with active remediation documented in §4.5/§5.2.")
        continue
    if in_v4 and (ln.startswith("## Validation") or ln.startswith("## Version History")):
        in_v4 = False
    out.append(ln)

src = "\n".join(out)
src = src.replace(
 "## §4 — Modelo de Maturidade Tripla (CSF 0-4 + Privacy 0-4 + AI RMF 0-4)",
 "## §4 — Implementation Posture (adopted 2026-08-28, port Fase 4; supersedes the legacy triple-maturity model)")
src = src.replace(
 "> Mirrors Case_01 SPEC §7 (Modelo de Maturidade Dupla) but extended to 3 frameworks. Tiers 1-4 at program/Function level (CSF native; adopted for the other two); 0-4 per-subcategory at the control level.",
 "> Previously mirrored the Case_01 SPEC §7 double-maturity model extended to 3 frameworks. Superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0 — see §4.1.")
src = src.replace(
 "> `cur_tier` from Doc 11 column 13 (Maturity Score) aggregated per Function;",
 "> Legacy note (pre-port): cur_tier derived from Doc 11 column 13 aggregated per Function; now backfilled —")
src = src.replace(
 "> `cur_csf` = Doc 11 column 13 (Maturity Score);",
 "> Legacy note (pre-port): cur_csf was Doc 11 column 13 (Maturity Score); §5.1 statuses below are the deterministic backfill —")
src = src.replace(
 "> Aggregation rule: per Function, take MAX(cur across the cards in that Function — the lowest maturity card anchors the Function's cur).",
 "> Legacy aggregation note (pre-port): MAX(cur across cards) anchored each Function's cur; the qualitative contexts below quote the legacy scale for traceability.")
src = src.replace(
 "### §6.4 — Sub-domains with low target maturity (tgt < 3)",
 "### §6.4 — Sub-domains at the STANDARD target profile (legacy tgt = 3)")
src = src.replace(
 "**No active sub-domain has tgt < 3** in Case_02 (Track B floor enforced).",
 "**No active sub-domain falls below the STANDARD target profile** (legacy tgt 3; Track B floor enforced — posture equivalent: every active sub-domain has at least PARTIAL-with-defined-target controls).")
src = src.replace(
 "FN-02 — CR-D-07.1-001 has airmf = N/A (no AI-C* i",
 "FN-02 (updated, port Fase 3) — CR-D-07.1-001 airmf anchored to MEASURE-2.7 (previously N/A; no AI-C* i")
src = src.replace(
 "total_cells_triple_maturity: 165",
 "implementation_posture_decision: Implementation Posture Model v2.0 (IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md): 3 states + N/A categories; legacy triple-maturity (165 cells) superseded via deterministic backfill — port Fase 4")
src = src.replace(
 "`02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/Doc05_Security_Posture.md` — current maturity per macro-domain (3.0 overall).",
 "`02_CASES/Case_02_SecureBorder_Solutions/01_PHASE1_CONTEXT_RICH/Doc05_Security_Posture.md` — qualitative posture input per macro-domain (DEPRECATED_FOR_POSTURE; superseded as scoring source).")

open(P, "w", encoding="utf-8").write("\n".join(src.split("\n")))
print("V4 rows:", rows)
