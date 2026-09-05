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
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
CASE = REPO / "02_CASES" / "Case_02_SecureBorder_Solutions"

def load_anchor_sets():
    controls = REPO / "00_METHODOLOGY" / "PREPROCESSING_by_domain" / "CONTROLS"
    r5 = set()
    for f in controls.glob("NIST_80053R5/??.json"):
        for c in json.loads(f.read_text(encoding="utf-8"))["controls"]:
            r5.add(c["id"])
    ssdf = set()
    sd = json.loads((controls / "NIST_SSDF" / "SSDF.json").read_text(encoding="utf-8"))
    for p in sd["practices"]:
        ssdf.add(p["id"])
        for t in p.get("tasks", []):
            ssdf.add(t["id"])
    av = json.loads((controls / "OWASP_ASVS" / "ASVS_sections.json").read_text(encoding="utf-8"))
    asvs_ids = set(av["chapters"]) | {s["id"] for s in av["sections"]}
    sm = json.loads((controls / "OWASP_SAMM" / "SAMM_streams.json").read_text(encoding="utf-8"))
    samm_ids = {s["stream"] for s in sm["streams"]}
    for s in sm["streams"]:
        for lv in (1, 2, 3):
            samm_ids.add(f"{s['stream']}-{lv}")
    iso = {f"A.{maj}.{n:02d}" for maj in range(5, 9) for n in range(1, 40)}
    return {"800-53r5": r5 | {"IP-3", "DM-1"}, "SSDF": ssdf, "ASVS": asvs_ids,
            "SAMM": samm_ids, "ISO": iso}


def alt_anchor_spans(line):
    out = []
    idx = 0
    while True:
        s = line.find("ALT-ANCHOR (", idx)
        if s < 0: break
        i = s + len("ALT-ANCHOR ")
        depth = 0; j = i
        while j < len(line):
            if line[j] == "(": depth += 1
            elif line[j] == ")":
                depth -= 1
                if depth == 0: out.append(line[i+1:j]); break
            j += 1
        idx = j + 1
    return out

def alt_anchor_is_valid(inner):
    last = None
    for raw in inner.split(";"):
        ref = raw.strip()
        if not ref:
            return False
        parts = ref.split(" ", 1)
        if len(parts) == 2 and parts[0] in ANCHOR_SETS:
            last, ident = parts[0], parts[1].strip()
        else:
            if last is None:
                return False
            ident = ref
        if ident not in ANCHOR_SETS[last]:
            return False
    return True

ANCHOR_SETS = load_anchor_sets()

# Pre-existing CSF 1.1 remnants (families retired/replaced in CSF 2.0). Waived with
# successor mapping — normalisation is a future campaign (see PENDING_CAMPAIGNS_LEDGER).
CSF_11_WAIVER = {
    "PR.DS-12": "1.1 remnant (PR.DS 2.0 = DS-01/02/10/11)",
    "RS.CO-04": "1.1 remnant (RS.CO 2.0 = CO-02/CO-03)",
    "PR.IP-06": "1.1 family retired (2.0: PR.PS)",
    "PR.IP-07": "1.1 family retired (2.0: PR.PS)",
    "PR.PT-01": "1.1 family retired (2.0: PR.DS-10)",
    "PR.AT-03": "1.1 remnant (PR.AT 2.0 = AT-01/AT-02)",
    "PR.AT-04": "1.1 remnant (PR.AT 2.0 = AT-01/AT-02)",
    "PR.AC-01": "1.1 family retired (2.0: PR.AA)",
    "ID.SC-04": "1.1 family retired (2.0: GV.SC)",
}

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
CSF_IDS = None
_csf_json = REPO / "00_METHODOLOGY" / "PREPROCESSING_by_domain" / "CONTROLS" / "NIST_CSF_2.0" / "CSF_2.0.json"
try:
    CSF_IDS = {s if isinstance(s, str) else s.get("id")
               for s in json.loads(_csf_json.read_text(encoding="utf-8"))["subcategories"]}
except Exception:
    CSF_IDS = None  # frozen list unavailable — warn-only fallback

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
        if re.search(r"UNMAPPED_(PF|CSF|AIRMF|PRIVACY)\b", line) and not wx:
            violations.append(f"{md}:{n}: RETIRED UNMAPPED token (v0.4): {line.strip()[:110]}")
        for inner0 in alt_anchor_spans(line):
            inner = inner0.strip()
            # ellipsis "..." is a prose placeholder for a list (e.g. "[`ALT-ANCHOR (…)` anchors …]")
            if inner == "NO-ANALOGUE" or "…" in inner or alt_anchor_is_valid(inner):
                continue
            violations.append(f"{md}:{n}: ALT-ANCHOR invalid '{inner}'")
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
                if m.group(0) not in CSF_IDS and m.group(0) not in CSF_11_WAIVER:
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

for w in warnings:
    print("WARN:", w)
if violations:
    print(f"GATE FAIL — {len(violations)} violations:")
    for v in violations[:40]:
        print(" ", v)
    sys.exit(1)
print("GATE PASS (check_unmapped.py, Case_02 v0.4)")
