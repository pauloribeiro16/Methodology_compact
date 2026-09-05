#!/usr/bin/env python3
"""
apply_realization_class.py — derived realization_class on control_set.yaml.

Usage: python3 scripts/apply_realization_class.py <Case_02|Case_03|all>

Heuristic (derived from existing fields, not invented):
  * TECHNOLOGY — airmf stream from {IDENTIFY-*, DETECT-*} (measurement streams);
                  OR csf maps in PR/DE/SC/SI and verification is TEST;
                  OR pf map in PR/AC/PR/DS and field is clearly a system feature.
  * PROCESS    — airmf stream from {INCIDENT RESPONSE, POLICY & COMPLIANCE,
                  OPERATIONS MGMT, RISK MANAGEMENT};
                  OR verification is INSPECT/DEMONSTRATE with sequenced human steps;
                  OR pf map in CT/CM/ID/GV (privacy programme operations).
  * CAPABILITY  — airmf stream from {GOVERN-*, EDUCATION & GUIDANCE};
                  OR role is board/CISO-level (per Source UC and Owner);
                  OR pf map in GV (governance standing ability).

Idempotent. Tolerant of pre-existing realization_class (does not overwrite unless
the existing value disagrees and the heuristic gives a stronger signal).
"""
import re
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
CASES = {
    "Case_02": _REPO / "02_CASES" / "Case_02_SecureBorder_Solutions" / "02_PHASE2_RULES_RICH" / "control_set.yaml",
    "Case_03": _REPO / "02_CASES" / "Case_03_OmniBank_Financial" / "02_PHASE2_RULES_RICH" / "control_set.yaml",
}

# SAMM stream -> preferred class
TECH_STREAMS = {"IDENTIFY", "DETECT"}  # measurement
PROCESS_STREAMS = {"INCIDENT", "POLICY", "OPERATIONS", "RISK", "DESIGN"}
CAPABILITY_STREAMS = {"GOVERN", "EDUCATION", "STRATEGY"}


def derive(c):
    airmf = c.get("airmf", "").upper()
    csf = c.get("csf", "").upper()
    pf = c.get("pf", "").upper()
    verification = c.get("verification", "").upper()
    role = c.get("role", "").upper()

    # Priority 1: AIRMF stream hint
    for tok in TECH_STREAMS:
        if tok in airmf: return "TECHNOLOGY"
    for tok in CAPABILITY_STREAMS:
        if tok in airmf: return "CAPABILITY"
    for tok in PROCESS_STREAMS:
        if tok in airmf: return "PROCESS"

    # Priority 2: verification shape
    if verification in {"INSPECT", "DEMONSTRATE"} and "GV" in csf:
        return "PROCESS"
    if verification == "TEST" and "PR" in csf:
        return "TECHNOLOGY"

    # Priority 3: PF map
    if "GV" in pf: return "CAPABILITY"
    if any(tag in pf for tag in ("CT", "CM")): return "PROCESS"
    if any(tag in pf for tag in ("PR", "DE", "SC", "SI")): return "TECHNOLOGY"

    # Priority 4: role-based
    if "BOARD" in role or "CISO" in role: return "CAPABILITY"

    return "PROCESS"  # safe default (per rubric: rules that can't be classified as TECHNOLOGY tend to be workflow)


def process_case(name, path):
    if not path.exists():
        raise SystemExit(f"missing: {path}")
    text = path.read_text(encoding="utf-8")
    # Find each control block `- id: "..."` ... up to next `- id:` or end of `controls:`
    # Use a simple state machine: locate blocks, replace `realization_class:` line in-place.
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r'\s*- id:\s*"([^"]+)"', ln)
        if not m:
            i += 1
            continue
        block_id = m.group(1)
        # collect block until next `- id:` or outdent
        j = i + 1
        while j < len(lines) and not re.match(r'\s*- id:\s*"', lines[j]) and not re.match(r"^[^\s]", lines[j]):
            j += 1
        block = lines[i:j]
        # already has realization_class?
        has = any(re.match(r"\s*realization_class:", ln) for ln in block)
        # extract needed fields
        c = {"id": block_id}
        for ln in block:
            m2 = re.match(r'\s*(airmf|csf|pf|verification|role):\s*"?(.*?)"?\s*$', ln)
            if m2 and m2.group(1) in c and not c[m2.group(1)]:
                c[m2.group(1)] = m2.group(2).rstrip('"')
        proposed = derive(c)
        if not has:
            # insert before the next sibling or at end of block
            indent = "      "
            block.append(f'{indent}realization_class: "{proposed}"')
            new_lines = block + lines[j:]
            lines[i:j] = []
            lines.extend(new_lines[: len(block) - (j - i)])
            # rebuild: simpler — rebuild whole file by replacing the block slice
            lines = text.split("\n")
        else:
            # check existing value
            for ln in block:
                m3 = re.match(r'\s*realization_class:\s*"([^"]+)"', ln)
                if m3 and m3.group(1) != proposed:
                    # record a divergence line (do not auto-overwrite)
                    print(f"DIVERGENCE {name} {block_id}: existing={m3.group(1)} heuristic={proposed}")
        i = j
    # rebuild text with insertions
    # Re-do insertion properly (state machine was destructive; instead build a fresh text)
    fresh = []
    in_control = False
    block_buf = []
    inserted_for = set()
    for ln in text.split("\n"):
        m = re.match(r'\s*- id:\s*"([^"]+)"', ln)
        if m and m.group(1) not in inserted_for:
            block_id = m.group(1)
            # collect block
            idx = text.split("\n").index(ln)
            # find end of block
            all_lines = text.split("\n")
            k = idx + 1
            block_lines = [ln]
            while k < len(all_lines) and not re.match(r'\s*- id:\s*"', all_lines[k]) and not re.match(r"^[^\s]", all_lines[k]):
                block_lines.append(all_lines[k])
                k += 1
            # gather fields
            c = {"id": block_id}
            for bl in block_lines:
                m2 = re.match(r'\s*(airmf|csf|pf|verification|role):\s*"?(.*?)"?\s*$', bl)
                if m2 and m2.group(1) in c and not c[m2.group(1)]:
                    c[m2.group(1)] = m2.group(2).rstrip('"')
            has = any(re.match(r"\s*realization_class:", bl) for bl in block_lines)
            proposed = derive(c)
            if not has:
                indent = "      "
                block_lines.insert(0, ln)
                # insert realization_class just before end (after the last property, keep indentation)
                block_lines.append(f'{indent}realization_class: "{proposed}"')
                inserted_for.add(block_id)
                fresh.append("\n".join(block_lines))
                # consume k-idx lines
                # but we iterated line by line — easier: do all-at-once rewrite
                break
            else:
                fresh.append("\n".join(block_lines))
                inserted_for.add(block_id)
                break
        elif m:
            fresh.append(ln)
        else:
            fresh.append(ln)
    # if the per-line loop above broke early, do a simpler full pass
    new_text = apply_pass(text)
    if new_text != text:
        path.write_text(new_text)
        n_added = new_text.count("realization_class:") - text.count("realization_class:")
        print(f"{name}: {n_added} realization_class added")


def extract_fields(block):
    """Extract airmf/csf/pf/verification from a control block (yaml-like)."""
    c = {}
    for bl in block:
        m = re.match(r'^\s*(airmf|csf|pf|verification|role)\s*:\s*(.+?)\s*$', bl)
        if m and m.group(1) not in c:
            val = m.group(2).strip()
            # strip surrounding quotes if present
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            c[m.group(1)] = val
    return c


def apply_pass(text):
    """Single-pass line-aware: find each control block and insert realization_class
    after the block's last property if not already present."""
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r'\s*- id:\s*"([^"]+)"', ln)
        if not m:
            out.append(ln); i += 1; continue
        # find end of block
        j = i + 1
        while j < len(lines):
            if re.match(r'\s*- id:\s*"', lines[j]): break
            if re.match(r"^[^\s]", lines[j]): break
            j += 1
        block = lines[i:j]
        if not any(re.match(r"\s*realization_class:", bl) for bl in block):
            c = extract_fields(block)
            proposed = derive(c)
            block.append(f'      realization_class: "{proposed}"')
        out.extend(block)
        i = j
    return "\n".join(out)


def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: apply_realization_class.py <Case_02|Case_03|all>")
    target = sys.argv[1]
    selected = list(CASES.items()) if target == "all" else [(target, CASES[target])]
    for name, p in selected:
        text = p.read_text(encoding="utf-8")
        new_text = apply_pass(text)
        if new_text != text:
            p.write_text(new_text, encoding="utf-8")
            n_added = new_text.count("realization_class:") - text.count("realization_class:")
            print(f"{name}: {n_added} realization_class added")
        else:
            print(f"{name}: no change")


if __name__ == "__main__":
    main()
