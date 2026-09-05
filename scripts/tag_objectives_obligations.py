#!/usr/bin/env python3
"""
tag_objectives_obligations.py — annotate PO/SO/AG/OBL- ids with derived realization_class.

Method (majority-vote over realizing controls):
  1. For each obj/obl id in the targets doc, find the control ids whose `related_goals`
     or `traceability` field mentions it (single-pass over the control_set.yaml block stream).
  2. Majority-vote over their `realization_class` (TECHNOLOGY / PROCESS / CAPABILITY).
  3. Append the derived class to a `realization_class_derived` metadata block at the
     end of the obj/obl doc.

Usage: python3 scripts/tag_objectives_obligations.py <Case_02|Case_03|all>
"""
import re
import sys
from pathlib import Path
from collections import Counter

TARGETS = {
    "Case_02_SecureBorder_Solutions": [
        ("02_PHASE2_RULES_RICH/Doc15_Obligation_Derivation.md", "OBL-"),
        ("02_PHASE2_RULES_RICH/Doc16_Privacy_Security_Goals.md", "PO-/SO-"),
    ],
    "Case_03_OmniBank_Financial": [
        ("02_PHASE2_RULES_RICH/Doc15_Obligation_Derivation.md", "OBL-"),
        ("02_PHASE2_RULES_RICH/Doc17_Privacy_Security_Objectives.md", "AG-"),
    ],
}

ID_RE = re.compile(r"\b(?:PO|SO|AG|OBL)-D-\d+\.\d+(?:-\d+)?\b")
RULE_ID_RE = re.compile(r"\b(?:CR|BPR)-D-\d+\.\d+-\d+\b")
RULE_CLASS_RE = re.compile(r'realization_class:\s*"([^"]+)"')
BLOCK_START_RE = re.compile(r'^(\s*)-\s*id:\s*"((?:CR|BPR)-D-[\d.]+-\d+)"')


def parse_control_blocks(cs_text):
    """Yield (rule_id, related_goals, traceability, realization_class).

    State machine: a block starts at `- id: "..."` and continues while the next line's
    indent is strictly greater than the `- id` line's indent.
    """
    lines = cs_text.split("\n")
    i = 0
    while i < len(lines):
        m = BLOCK_START_RE.match(lines[i])
        if not m:
            i += 1; continue
        rule_id = m.group(2)
        base_indent = len(m.group(1))
        block_lines = [lines[i]]
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if nxt == "":
                block_lines.append(nxt); j += 1; continue
            stripped = nxt.lstrip()
            if not stripped:
                block_lines.append(nxt); j += 1; continue
            leading = len(nxt) - len(stripped)
            if leading > base_indent:
                block_lines.append(nxt); j += 1
            else:
                break
        block = "\n".join(block_lines)
        rg = re.search(r'related_goals:\s*"([^"]*)"', block)
        tr = re.search(r'traceability:\s*"([^"]*)"', block)
        rc = RULE_CLASS_RE.search(block)
        yield rule_id, (rg.group(1) if rg else ""), (tr.group(1) if tr else ""), (rc.group(1) if rc else None)
        i = j


def build_rule_index(cs_text):
    """{oid: set(rule_id)} and {rule_id: realization_class}."""
    obj2rules = {}
    rule_class = {}
    for rule_id, rg, tr, rc in parse_control_blocks(cs_text):
        rule_class[rule_id] = rc
        for oid in set(ID_RE.findall(rg)) | set(ID_RE.findall(tr)):
            obj2rules.setdefault(oid, set()).add(rule_id)
    return obj2rules, rule_class


def majority_class(rule_ids, rule_class):
    classes = [rule_class[r] for r in rule_ids if r in rule_class and rule_class[r]]
    if not classes: return None, Counter()
    c = Counter(classes)
    return c.most_common(1)[0][0], c


def annotate(doc_text, obj_ids, obj2rules, rule_class):
    lines = doc_text.split("\n")
    per_id_class = {}
    per_id_count = {}
    for oid in sorted(obj_ids):
        rules = obj2rules.get(oid, set())
        cls, dist = majority_class(rules, rule_class)
        per_id_class[oid] = cls
        per_id_count[oid] = (len(rules), dist)
    # Append a metadata section listing each obj/obl with its derived class.
    annotation = ["", "## realisation_class_derived (auto, majority-vote of realizing controls)", "",
                  "| Objective / Obligation | Realising CR/BPR | Majority |",
                  "|---|---|---|"]
    for oid in sorted(obj_ids):
        cls, _ = majority_class(obj2rules.get(oid, set()), rule_class)
        rules = sorted(obj2rules.get(oid, set()))
        rule_str = ", ".join(rules[:5]) + (" …" if len(rules) > 5 else "")
        annotation.append(f"| {oid} | {rule_str or '—'} | {cls or 'no-rule'} |")
    lines.extend(annotation)
    return "\n".join(lines), per_id_class


def process_case(case_name, paths):
    case_root = Path("02_CASES") / case_name
    cs_path = case_root / "02_PHASE2_RULES_RICH" / "control_set.yaml"
    cs_text = cs_path.read_text(encoding="utf-8")
    obj2rules, rule_class = build_rule_index(cs_text)
    print(f"  {case_name}: index built ({len(obj2rules)} obj/obl ids, {sum(len(v) for v in obj2rules.values())} rule-links)")
    summary = {}
    for rel, _ in paths:
        p = case_root / rel
        if not p.exists(): continue
        text = p.read_text(encoding="utf-8")
        ids = sorted(set(ID_RE.findall(text)))
        new_text, per_id_class = annotate(text, ids, obj2rules, rule_class)
        p.write_text(new_text, encoding="utf-8")
        c = Counter(filter(None, per_id_class.values()))
        summary[rel] = c
        print(f"    {rel}: {len(ids)} objs → {dict(c)}")
    return summary


def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: tag_objectives_obligations.py <Case_02|Case_03|all>")
    target = sys.argv[1]
    selected = list(TARGETS.items()) if target == "all" else [(target, TARGETS[target])]
    for case_name, paths in selected:
        process_case(case_name, paths)


if __name__ == "__main__":
    main()
