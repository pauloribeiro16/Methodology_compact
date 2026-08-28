#!/usr/bin/env python3
"""Port Fase 4: migrate Doc19 §5.1 numeric cur/tgt cells to Implementation Status."""
import re

P = "02_CASES/Case_02_SecureBorder_Solutions/02_PHASE2_RULES_RICH/Doc19_Framework_Mapping_Matrix.md"
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

out = []
counts = {"IMPLEMENTED": 0, "PARTIAL": 0, "NOT IMPLEMENTED": 0, "N/A": 0}
migrated = 0
id_re = re.compile(r"^\| (CR-D-\d\d\.\d-\d{3}|BPR-D-\d\d\.\d-\d{3}) \|")
for ln in lines:
    if id_re.match(ln):
        cells = [c.strip() for c in ln.split("|")[1:-1]]
        if len(cells) == 13 and re.fullmatch(r"\d+|N/A", cells[2]) :
            rid, sd = cells[0], cells[1]
            s = [status(cells[2], cells[3]), status(cells[4], cells[5]), status(cells[6], cells[7])]
            for x in s:
                counts[x] += 1
            migrated += 1
            out.append(f"| {rid} | {sd} | {s[0]} | {s[1]} | {s[2]} |")
            continue
    if ln.startswith("| rule_id | sub_domain | cur_csf |"):
        out.append("| rule_id | sub_domain | Implementation Status (CSF) | Implementation Status (Privacy) | Implementation Status (AI RMF) |")
        out.append("|---------|-----------|------|---------|---------|")
        continue
    out.append(ln)

open(P, "w", encoding="utf-8").write("\n".join(out))
print("rows migrated:", migrated)
print("distribution:", counts)
