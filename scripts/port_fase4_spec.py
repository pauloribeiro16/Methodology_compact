#!/usr/bin/env python3
"""Port Fase 4: mark legacy-design lines in Case_02 SPEC; add posture banner."""
P = "02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/SPEC_NIST_MATRIX_UNIFIED.md"
lines = open(P, encoding="utf-8").read().split("\n")
WAIVE = ("legacy", "superseded", "retired", "deprecated", "postura", "posture")
MARK = " *(legacy design text — superseded by IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0, port Fase 4)*"
out, n = [], 0
for ln in lines:
    low = ln.lower()
    if "maturi" in low and not any(w in low for w in WAIVE):
        ln = ln.rstrip() + MARK
        n += 1
    out.append(ln)
src = "\n".join(out)
src = src.replace(
 "## Como ler este documento",
 """## ⚠️ POSTURE MODEL SUPERSESSION (2026-08-28, port Fase 4)

> The triple-maturity scoring designed in this SPEC (Tiers T1–T4, 0–4
> per-subcategory scales, 165 numeric cells, fields 16–18 "Maturity") is
> **SUPERSEDED** by `00_METHODOLOGY/IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md`
> v2.0 (3 states + N/A categories, deterministic backfill). Doc19 §4/§5.1 and
> Doc18 carry the adopted implementation. Sections below that still describe
> the legacy scoring are marked *legacy design text*; they are retained for
> specification history and are not authoritative.

## Como ler este documento""", 1)
open(P, "w", encoding="utf-8").write(src)
print("lines marked:", n)
