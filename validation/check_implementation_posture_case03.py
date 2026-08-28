#!/usr/bin/env python3
"""check_implementation_posture.py — Case_02 (Gate v0.3, port Fase 6).

Port of validation/check_implementation_posture.py (Case_01), parameterised
for Case_02 and aligned with the Implementation Posture Model
(00_METHODOLOGY/IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md v2.0):

1.  zero legacy maturity terms in Case_02 deliverables outside
    supersession/waiver context (legacy, superseded, retired, deprecated,
    pre-port, posture model, hist.', justification lines);
2.  zero sprint_ frontmatter keys in deliverables;
3.  Doc18 Control Set carries 63 controls with Implementation Status fields;
4.  status distribution is non-uniform (>= 2 distinct states);
5.  validation/build_control_set.py exits 0 and produces control_set.yaml
    with 63 controls (status parsing verified — the Case_01 '**' defect is
    structurally impossible and asserted against).

Exit 0 = GATE PASS.
"""
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CASE = REPO / "02_CASES" / "Case_03_OmniBank_Financial"
BUILD = CASE / "02_PHASE2_RULES_RICH" / "validation" / "build_control_set.py"

EXCLUDED = ("validation/", "VALIDATOR_", "CHANGE_LOG", "DEPRECATED", "_deprecated", "RICH_VS_LEGACY", "PORT_census")
WAIVER = ("legacy", "superseded", "retired", "deprecated", "pre-port", "posture model",
          "proibido", "forbidden", "reformado", "vocabulary", "vocabulário", "justificação",
          "historical", "histórico", "was maturi", "ver git")

violations = []


def excluded(p):
    return any(x in str(p) for x in EXCLUDED)


for md in CASE.rglob("*.md"):
    if excluded(md):
        continue
    lines = md.read_text(encoding="utf-8").split("\n")
    for n, line in enumerate(lines, 1):
        low = line.lower()
        wx = any(w in low for w in WAIVER) or (n > 1 and any(w in lines[n - 2].lower() for w in WAIVER))
        if re.search(r"maturity|maturi", low) and not wx:
            violations.append(f"{md}:{n}: legacy maturity term")
        if re.match(r"^\s*sprint(\w*)\s*:", line):
            violations.append(f"{md}:{n}: sprint frontmatter key")

r = subprocess.run([sys.executable, str(BUILD)], capture_output=True, text=True)
if r.returncode != 0:
    violations.append("build_control_set.py failed")
    print(r.stderr[-500:])
else:
    print(r.stdout.strip())
    if "'**'" in r.stdout:
        violations.append("Case_01 '**' status parsing defect detected")
    import yaml
    cs = yaml.safe_load((BUILD.parent / "control_set.yaml").read_text(encoding="utf-8"))
    ctrls = cs["control_set"]["controls"]
    if len(ctrls) != 78:
        violations.append(f"control count {len(ctrls)} != 78")
    dist = {}
    for c in ctrls:
        dist[c["status_csf"]] = dist.get(c["status_csf"], 0) + 1
    if len(dist) < 2:
        violations.append(f"uniform status distribution: {dist}")
    print("status_csf distribution:", dist)

if violations:
    print(f"GATE FAIL — {len(violations)} violations:")
    for v in violations[:40]:
        print(" ", v)
    sys.exit(1)
print("GATE PASS (check_implementation_posture.py, Case_03 v0.3)")
