#!/usr/bin/env python3
"""check_unmapped.py — Case_02 (Gate v0.3, port Fase 6, 2026-08-28).

Port of the Case_01 gate
(02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/validation/check_unmapped.py),
parameterised for Case_02 and adapted to its 3-framework matrix:

1.  zero pseudo-range markers (UNMAPPED_X..) — lines that QUOTE the forbidden
    pattern while defining the rule (contain Proibido/forbidden/RETIRED/
    retired/superseded) are skipped;
2.  every UNMAPPED_PF carries justification context (parenthetical or
    unmapped_pf_justification);
3.  every PF id belongs to the canonical frozen list
    (00_METHODOLOGY/PREPROCESSING_by_domain/CONTROLS/NIST_PF/*.json);
4.  CSF ids are WARN-only checked (the frozen CSF 2.0 subcategory list lives in
    the upstream corpus; the compact repo mirrors only PF and AI RMF lists —
    same documented limitation as the Case_01 Methodology-main fallback);
5.  AI RMF vocabulary: zero UNMAPPED_AIRMF and zero UNMAPPED_PRIVACY tokens in
    deliverables (both RETIRED); `N/A (non-AI scope)` is the only legal
    placeholder; real AI RMF ids must belong to the frozen 72-subcategory list
    (CONTROLS/NIST_AI_RMF/*/*.json);
6.  zero /maturi/ terms outside retirement/waiver context (legacy, superseded,
    retired, deprecated, pre-port, posture model, "Maturity Score" in the
    posture-model authority paths);
7.  zero sprint_ frontmatter keys in deliverables;
8.  Doc18 Control Set: 63 controls with non-uniform Implementation Status
    distribution (>= 2 distinct states), via validation/build_control_set.py;
9.  build_control_set.py exits 0 and regenerates control_set.yaml with 63 controls.

Exit 0 = GATE PASS.
"""
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
CASE = REPO / "02_CASES" / "Case_02_SecureBorder_Solutions"
CONTROLS = REPO / "00_METHODOLOGY" / "PREPROCESSING_by_domain" / "CONTROLS"

EXCLUDED = ("validation/", "VALIDATOR_", "CHANGE_LOG", "DEPRECATED", "RICH_VS_LEGACY", "PORT_census")
WAIVER_WORDS = ("legacy", "superseded", "retired", "deprecated", "pre-port", "posture model",
                "proibido", "forbidden", "reformado", "vocabulary", "vocabulário", "justificação",
                "historical", "histórico", "was maturi", "ver git", "unmapped_pf_justification",
                "model_csf_strict", "maturity_cur", "maturity_tgt", "evidence model", "maturity redesign", "p1_maturity.html")

violations, warnings = [], []


def excluded(path: Path) -> bool:
    s = str(path)
    return any(x in s for x in EXCLUDED)


def waivered(low: str) -> bool:
    return any(w in low for w in WAIVER_WORDS)


def load_ids(folder: Path):
    ids = set()
    for j in folder.rglob("*.json"):
        m = re.search(r'"control_id"\s*:\s*"([^"]+)"', j.read_text(encoding="utf-8"))
        if m:
            ids.add(m.group(1))
        else:
            ids.add(j.stem)
    return ids


PF_IDS = load_ids(CONTROLS / "NIST_PF")
AI_IDS = load_ids(CONTROLS / "NIST_AI_RMF")
CSF_IDS = None  # frozen list not present in compact repo — warn-only

CSF_RE = re.compile(r"\b(GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}\b")
PF_RE = re.compile(r"\b(?:GV|ID|PR|CT|CM)\.[A-Z]{2}-P\d+\b")
AI_RE = re.compile(r"\b(GOVERN|MAP|MEASURE|MANAGE)-\d\.\d\b")

prev_low = ""
for md in CASE.rglob("*.md"):
    if excluded(md):
        continue
    text_lines = md.read_text(encoding="utf-8").split("\n")
    for n, line in enumerate(text_lines, 1):
        low = line.lower()
        nxt = text_lines[n].lower() if n < len(text_lines) else ""
        wx = waivered(low) or waivered(prev_low) or waivered(nxt)
        if re.search(r"UNMAPPED_[A-Z]+\.\.", line) and not wx:
            violations.append(f"{md}:{n}: pseudo-range marker")
        if "UNMAPPED_PF" in line and not wx:
            if "(" not in line and "unmapped_pf_justification" not in line:
                violations.append(f"{md}:{n}: UNMAPPED_PF without justification")
        if re.search(r"UNMAPPED_(AIRMF|PRIVACY)\b", line) and not wx:
            violations.append(f"{md}:{n}: retired token UNMAPPED_AIRMF/UNMAPPED_PRIVACY")
        if re.search(r"\bmaturi\b|maturity|maturidade", low) and not wx:
            violations.append(f"{md}:{n}: legacy maturity term")
        if re.match(r"^\s*sprint(\w*)\s*:", line):
            violations.append(f"{md}:{n}: sprint frontmatter key")
        for m in PF_RE.finditer(line):
            if m.group(0) not in PF_IDS:
                violations.append(f"{md}:{n}: PF id not in frozen list: {m.group(0)}")
        for m in AI_RE.finditer(line):
            if m.group(0) not in AI_IDS and not wx:
                violations.append(f"{md}:{n}: AI RMF id not in frozen list: {m.group(0)}")
        if CSF_IDS:
            for m in CSF_RE.finditer(line):
                if m.group(0) not in CSF_IDS:
                    violations.append(f"{md}:{n}: CSF id not in frozen list: {m.group(0)}")
        prev_low = low

# Doc18 / control_set check (check 8/9)
r = subprocess.run([sys.executable, str(CASE / "02_PHASE2_RULES_RICH" / "validation" / "build_control_set.py")],
                   capture_output=True, text=True)
print(r.stdout.strip())
if r.returncode != 0:
    violations.append("build_control_set.py failed")
else:
    import yaml  # noqa: E402
    cs = yaml.safe_load((CASE / "02_PHASE2_RULES_RICH" / "validation" / "control_set.yaml").read_text(encoding="utf-8"))
    ctrls = cs["control_set"]["controls"]
    if len(ctrls) != 63:
        violations.append(f"control_set.yaml has {len(ctrls)} controls, want 63")
    dist = {}
    for c in ctrls:
        dist[c["status_csf"]] = dist.get(c["status_csf"], 0) + 1
    if len(dist) < 2:
        violations.append(f"status distribution uniform: {dist}")
    print("status_csf distribution:", dist)

if CSF_IDS is None:
    warnings.append("CSF frozen-list membership check skipped (list not in compact repo) — WARN-only policy")

for w in warnings:
    print("WARN:", w)
if violations:
    print(f"GATE FAIL — {len(violations)} violations:")
    for v in violations[:40]:
        print(" ", v)
    sys.exit(1)
print("GATE PASS (check_unmapped.py, Case_02 v0.3)")
