# Orphan Inventory v0 — Case_02 / Case_03

**Sources:** `data/phase2_graph.json` audits (AUD-P2-004 / AUD-P2-005 / AUD-P2-005b).
**Methodology:** AUD-P2-005b (Case_03) = obligation without a CR addressing it (via the AG chain).
AUD-P2-004/005 (Case_02) = PO/SO without a CR/BPR addressing it. (Case_01 AUD-P2-005
carries 4 orphan obligations; deferred per `02_CASES/CHANGE_LOG_CENTRAL.md` §0.5.)

**Verdict scheme:**
- **MITIGADO** — orphan obligation is addressed by a BPR sibling (the audit looks for CR
  only by spec; BPR coverage is the deliberate mirror mechanism).
- **GAP** — no CR and no BPR addresses it; real coverage gap → P7 human queue.
- **LEGIT** — orphan is an intentional structural artifact (e.g. derived AG objective that
  is informational, not implementation-mandatory).

---

## Case_03 — 10 orphan obligations (AUD-P2-005b)

| Orphan OBL | BPR sibling present? | Verdict | Notes |
|---|---|---|---|
| OBL-D-02.2-001 | BPR-D-02.2-001 ✓ | MITIGADO | BPR covers; audit only scans CR |
| OBL-D-02.3-001 | BPR-D-02.3-001 ✓ | MITIGADO | BPR covers |
| OBL-D-03.2-001 | BPR-D-03.2-001 ✓ | MITIGADO | BPR covers |
| OBL-D-04.3-001 | BPR-D-04.3-001 ✓ | MITIGADO | BPR covers |
| OBL-D-06.2-001 | — | **GAP** | SBOM/PS.3; no CR, no BPR. P7: add CR or BPR, or formally waive with rationale |
| OBL-D-06.3-001 | BPR-D-06.3-001 ✓ | MITIGADO | BPR covers |
| OBL-D-07.4-001 | BPR-D-07.4-001 ✓ | MITIGADO | BPR covers |
| OBL-D-08.3-001 | BPR-D-08.3-001 ✓ | MITIGADO | BPR covers |
| OBL-D-10.2-001 | BPR-D-10.2-001 ✓ | MITIGADO | BPR covers |
| OBL-D-10.3-001 | BPR-D-10.3-001 ✓ | MITIGADO | BPR covers |

**C3 verdict:** 9 MITIGADO + 1 GAP (`OBL-D-06.2-001`). GAP → P7.

## Case_02 — 14 PO + 40 SO without CR/BPR addressing (AUD-P2-004 / AUD-P2-005)

These are SECONDARY coverage flags (objectives → CR/BPR is the legal coverage path).
The 14 PO items (`PO-D-XX.Y-002` family, mostly duplicates of the PO-D-XX.Y-001 that
DO have CR coverage) are inherent to the bilingual PO/AG structure: each sub-domain
carries one PO aligned with the AG and one informational PO. The 40 SO duplicates
follow the same pattern.

**C2 verdict:** LEGIT (informational duplicates of objectives that already have CR
coverage; the audit counts them because it does not dedup on the primary PO/SO per
sub-domain). **No P7 items** — the audit threshold can be improved (filter on the
_primary_ PO/SO per sub-domain, drop the secondary) without touching the case.

## Resolution path

- **C3 OBL-D-06.2-001** → P7 human queue (see PENDING_CAMPAIGNS_LEDGER.md §5).
- **C2 audit threshold** → out-of-scope improvement (post-campaign, the audit script
  in `scripts/build_p2_graph.py` could dedup PO/SO on the primary per sub-domain).
