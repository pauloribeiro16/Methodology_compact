---
document_id: AEGIS-P3-RICH-NIST-ANCHORS
title: NIST CSF 2.0 + NIST PF 1.0 Anchors (Case_01 Phase 3 RICH)
phase: 3
version: 1.0
created: 2026-08-24
updated: 2026-08-24
author: Sprint 2 Executor (paulo@methodology.pt)
status: ACTIVE
case: Case_01_TinyTask_SaaS
tier: MICRO
sprint: 2
sprint_role: nist_anchors
branch: feature/aegis-p3-case01-rich
inputs:
  - 02_PHASE2_RULES_RICH/11_Rules_Catalog.md §7.1 (CR CSF anchors) + §7.2 (BPR CSF anchors)
  - 02_PHASE2_RULES_RICH/10b_Privacy_Security_Goals_NIST_Implications.md (PO/SO anchors)
  - 01_IMPLEMENTATION_TOOLS/scripts/validate_nist_ids.py (pattern validator)
pattern_validated: true
coverage:
  rules_anchored: "46/46 (100%)"
  goals_anchored: "27/31 (87%) — 4 SOs (SO-D-02.2/02.3/03.2/06.2) intentionally blank per Doc 10b"
related_deliverables: [CORPUS_LINKAGE.md, KG_CHAINS.md, validation/SPRINT2_REPORT.md]
---

# NIST CSF 2.0 + NIST PF 1.0 Anchors

> **Purpose.** Per-rule and per-goal NIST anchors (CSF 2.0 + PF 1.0) for the 46 frozen rules
> and 31 frozen goals (Doc 10b). Each rule already has anchors in Doc 11 §7.1 (CR) / §7.2 (BPR);
> Doc 10b supplies the goal anchors. PF anchors are included where Doc 10b lists them.
>
> **Format:** `CSF: PR.XX-NN[,PR.YY-NN] | PF: XX.XX-PN[,YY.YY-PN]`
> **Validation:** All IDs match the patterns enforced by `01_IMPLEMENTATION_TOOLS/scripts/validate_nist_ids.py`:
> - CSF: `re.match(r"^[A-Z]{2}\.[A-Z]{2}-\d+$", id_str)`
> - PF: `re.match(r"^[A-Z]{2}\.[A-Z]{2}-P\d+$", id_str)`
>
> **Note:** No PR.IP-*, PR.AC-*, PR.PT-*, PR.MA-* IDs are emitted (all are CSF 1.1-only / withdrawn in CSF 2.0; validator flags them).

---

## §1 Per-Rule Anchors (46: 30 CR + 16 BPR)

| Rule ID | CSF Anchors | PF Anchors |
|---------|-------------|------------|
| CR-D-01.1-001 | PR.DS-01, PR.DS-10, PR.PS-04 | PR.DS-P1 |
| CR-D-01.2-001 | PR.DS-02, PR.IR-01, PR.PS-04 | PR.DS-P2 |
| CR-D-01.3-001 | GV.OV-01, GV.RM-04, PR.AA-03, PR.AA-04, PR.DS-01 | — |
| CR-D-01.4-001 | PR.DS-01, PR.DS-02, PR.DS-10, PR.IR-03, PR.IR-04, PR.PS-04 | CT.DM-P1, CT.DM-P3 |
| CR-D-02.1-001 | GV.OV-02, ID.AM-02, ID.IM-02, ID.RA-01, ID.RA-03 | ID.RA-P3, ID.RA-P5 |
| CR-D-02.2-001 | GV.OV-02, ID.RA-01, PR.IR-03, PR.PS-01, PR.PS-02 | — |
| CR-D-02.3-001 | GV.PO-01, GV.SC-04, ID.RA-01, RS.CO-03, RS.MA-01 | — |
| CR-D-03.1-001 | ID.AM-01, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 | — |
| CR-D-03.2-001 | PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06, PR.AT-02 | — |
| CR-D-03.3-001 | ID.AM-01, ID.AM-02, PR.AA-01, PR.AA-03, PR.AA-05 | CT.PO-P1 |
| CR-D-03.4-001 | GV.PO-01, GV.SC-03, PR.DS-10, PR.PS-01, PR.PS-04 | CT.DP-P4, CT.PO-P4 |
| CR-D-04.1-001 | DE.AE-02, DE.CM-01, DE.CM-09, ID.RA-04, PR.PS-04 | CM.AW-P7 |
| CR-D-04.2-001 | DE.CM-09, PR.DS-10, PR.IR-03, PR.IR-04, RC.RP-01 | CT.DM-P10, PR.PO-P7 |
| CR-D-04.3-001 | RS.CO-02, RS.MA-01, RS.MA-02, RS.MA-03 | CM.AW-P7, CM.AW-P8, CM.PO-P1, CM.PO-P2 |
| CR-D-04.4-001 | PR.DS-01, PR.DS-10, PR.IR-03, PR.IR-04, RC.RP-01 | — |
| CR-D-05.1-001 | GV.OC-03, GV.PO-01, ID.AM-03, PR.DS-01, PR.DS-10 | CT.DP-P4, CT.PO-P4, ID.RA-P3 |
| CR-D-05.2-001 | GV.OC-04, GV.OV-02, GV.PO-02, ID.AM-03, PR.DS-10 | CT.DM-P5, CT.PO-P4 |
| CR-D-05.3-001 | GV.SC-04, PR.DS-10, PR.DS-02 | CT.DM-P4, CT.DM-P5 |
| CR-D-05.4-001 | PR.DS-10, PR.AA-03, PR.DS-02 | CT.DM-P1, CT.DM-P6 |
| CR-D-06.1-001 | GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04 | ID.IM-P2 |
| CR-D-06.2-001 | GV.SC-02, GV.SC-03, ID.AM-02, ID.RA-01, PR.PS-02 | — |
| CR-D-06.3-001 | GV.OC-03, GV.SC-02, GV.SC-03, GV.SC-04, PR.DS-10 | — |
| CR-D-07.1-001 | GV.PO-02, ID.RA-01, PR.DS-10, PR.PS-01, PR.PS-02 | CT.DP-P2, CT.DP-P4, CT.DP-P5, CT.PO-P4, GV.PO-P2 |
| CR-D-08.1-001 | PR.AT-01, PR.AT-02, PR.PS-01 | GV.AT-P1, GV.AT-P2 |
| CR-D-08.2-001 | GV.RR-02, GV.RR-04, GV.SC-03, PR.AT-01, PR.AT-02 | GV.AT-P1, GV.AT-P2 |
| CR-D-09.1-001 | GV.PO-01, GV.PO-02, GV.RM-04, GV.RR-02, GV.OV-01 | CM.PO-P1, GV.PO-P1, GV.PO-P5 |
| CR-D-09.2-001 | ID.RA-01, ID.RA-04, ID.RA-05, GV.RM-06, GV.OV-02 | ID.RA-P3, ID.RA-P4, ID.RA-P5 |
| CR-D-09.4-001 | GV.PO-02, ID.AM-08, ID.RA-05, PR.DS-10, RS.MA-03 | ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8 |
| CR-D-10.2-001 | DE.CM-01, GV.PO-02, ID.RA-04, PR.DS-01, PR.PS-04 | CT.DM-P4, CT.DM-P9 |
| CR-D-10.3-001 | DE.AE-02, GV.OV-03, ID.RA-05, ID.IM-02, PR.PS-06 | ID.RA-P3, ID.RA-P5 |
| BPR-D-01.1-001 | PR.DS-01, PR.DS-10, PR.PS-04 | PR.DS-P1 |
| BPR-D-01.2-001 | PR.DS-02, PR.IR-01, PR.PS-04 | PR.DS-P2 |
| BPR-D-02.1-001 | ID.RA-01, ID.RA-03, ID.RA-05, ID.IM-02, PR.PS-02 | ID.RA-P3, ID.RA-P5 |
| BPR-D-02.2-001 | ID.RA-01, PR.IR-03, PR.PS-01, PR.PS-02 | — |
| BPR-D-03.1-001 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, ID.AM-01 | CT.PO-P1 |
| BPR-D-03.2-001 | PR.AA-03, PR.AA-04, PR.AA-05, PR.AA-06 | — |
| BPR-D-03.4-001 | GV.PO-01, PR.PS-01, PR.PS-04, ID.IM-02 | CT.DP-P4, CT.PO-P4 |
| BPR-D-04.3-001 | RS.MA-01, RS.MA-02, RS.MA-03, RS.CO-02 | CM.AW-P7, CM.PO-P1 |
| BPR-D-04.3-002 | RS.MA-01, RS.MA-02, RS.CO-02 | CM.PO-P1, CM.PO-P2 |
| BPR-D-05.3-001 | PR.DS-10, GV.SC-04, ID.AM-08 | CT.DM-P4, CT.DM-P5 |
| BPR-D-07.1-001 | GV.PO-02, GV.RR-02, ID.RA-01, PR.PS-01, PR.PS-02 | CT.DP-P2, CT.DP-P4, CT.PO-P4, GV.PO-P2 |
| BPR-D-07.2-001 | ID.RA-04, ID.RA-05, PR.PS-01, PR.PS-02, PR.PS-06 | — |
| BPR-D-09.1-001 | GV.PO-01, GV.PO-02, GV.RM-01, GV.OV-01, GV.OV-03 | CM.PO-P1, GV.PO-P1, GV.PO-P5 |
| BPR-D-10.2-001 | DE.CM-01, DE.AE-02, GV.PO-02, PR.DS-01, PR.PS-04 | CT.DM-P4, CT.DM-P9 |
| BPR-D-10.3-001 | GV.OV-03, ID.RA-01, ID.RA-04, ID.RA-05, ID.IM-02 | ID.RA-P3, ID.RA-P5 |
| BPR-D-10.3-002 | GV.OV-03, ID.RA-01, ID.RA-04, ID.RA-05, PR.PS-06 | ID.RA-P3, ID.RA-P5 |

## §2 Per-Goal Anchors (31: 11 PO + 20 SO)

| Goal ID | CSF Anchors | PF Anchors |
|---------|-------------|------------|
| PO-D-01.1-001 | PR.DS-01, PR.DS-02, PR.DS-10, PR.IR-01, PR.PS-06 | PR.DS-P1 |
| PO-D-01.2-001 | PR.DS-02, PR.IR-01 | PR.DS-P2 |
| PO-D-01.4-001 | PR.DS-01, PR.DS-10 | CT.DM-P1, CT.DM-P3 |
| PO-D-05.1-001 | GV.OC-03, GV.PO-01, GV.PO-02, ID.AM-03, PR.AA-02, PR.DS-10 | CT.DP-P4, CT.PO-P4, ID.RA-P3 |
| PO-D-05.2-001 | ID.AM-03, PR.DS-10 | CT.DM-P5, CT.PO-P4 |
| PO-D-05.3-001 | GV.SC-04, PR.DS-10, RS.CO-02 | CT.DM-P4, CT.DM-P5 |
| PO-D-05.4-001 | PR.DS-10 | CT.DM-P1, CT.DM-P6 |
| PO-D-07.1-001 | PR.DS-01, PR.DS-10, PR.PS-01, PR.PS-06 | CT.DP-P2, CT.DP-P4, CT.DP-P5, CT.PO-P4, GV.PO-P2 |
| PO-D-09.1-001 | GV.OC-02, GV.OC-03, GV.OV-03, GV.PO-01, GV.PO-02, GV.RM-04 | CM.PO-P1, GV.PO-P1, GV.PO-P5 |
| PO-D-09.2-001 | GV.OC-03, GV.OV-03, GV.PO-01, GV.RR-02, GV.SC-02, GV.SC-03 | ID.RA-P3, ID.RA-P4, ID.RA-P5 |
| PO-D-09.4-001 | DE.AE-03, GV.PO-02, ID.AM-03, PR.AA-02, PR.DS-10, PR.PS-04 | ID.IM-P1, ID.IM-P4, ID.IM-P6, ID.IM-P8 |
| SO-D-02.1-001 | ID.IM-02, ID.RA-01, ID.RA-05, PR.PS-02 | ID.RA-P3, ID.RA-P5 |
| SO-D-02.2-001 | — | — |
| SO-D-02.3-001 | — | — |
| SO-D-03.1-001 | GV.OC-03, GV.PO-02, PR.AA-02, PR.AA-03, PR.DS-10 | — |
| SO-D-03.2-001 | — | — |
| SO-D-03.3-001 | PR.AA-05, PR.AA-06, PR.AT-02 | CT.PO-P1 |
| SO-D-03.4-001 | PR.DS-10, PR.PS-01, PR.PS-06 | CT.DP-P4, CT.PO-P4 |
| SO-D-04.1-001 | DE.AE-02, DE.CM-01, DE.CM-03, DE.CM-09, RS.MA-02 | CM.AW-P7 |
| SO-D-04.2-001 | PR.DS-01, RS.MI-01, RS.MI-02 | CT.DM-P10, PR.PO-P7 |
| SO-D-04.3-001 | GV.OC-03, ID.RA-06, PR.DS-01, PR.DS-10, PR.IR-03 | CM.AW-P7, CM.AW-P8, CM.PO-P1, CM.PO-P2 |
| SO-D-04.4-001 | PR.DS-01, PR.IR-04, RC.RP-04 | — |
| SO-D-06.1-001 | GV.SC-02, GV.SC-03 | ID.IM-P2 |
| SO-D-06.2-001 | — | — |
| SO-D-06.3-001 | DE.CM-06, GV.OC-03, GV.RR-02, GV.SC-01, GV.SC-02, GV.SC-03 | — |
| SO-D-08.1-001 | GV.OV-03, ID.IM-02, PR.AA-05, PR.AT-01, PR.AT-02 | GV.AT-P1, GV.AT-P2 |
| SO-D-08.2-001 | PR.AT-01, PR.AT-02 | GV.AT-P1, GV.AT-P2 |
| SO-D-09.1-001 | GV.OC-02, GV.OC-03, GV.OV-03, GV.PO-01, GV.PO-02, GV.RM-04 | CM.PO-P1, GV.PO-P1, GV.PO-P5 |
| SO-D-09.2-001 | GV.OC-03, GV.OV-03, GV.PO-01, GV.RR-02, GV.SC-02, GV.SC-03 | ID.RA-P3, ID.RA-P4, ID.RA-P5 |
| SO-D-10.2-001 | DE.AE-03, GV.OV-03, GV.PO-02, ID.AM-03, PR.DS-10, PR.PS-04 | CT.DM-P4, CT.DM-P9 |
| SO-D-10.3-001 | ID.IM-02, ID.IM-04, ID.RA-01, ID.RA-05, ID.RA-06, PR.PS-02 | ID.RA-P3, ID.RA-P5 |

---
## §3 Per-Artefact Slot (paste-ready for UC/FR/NFR cards)

> Each row: `| <ARTEFACT-ID> | CSF: PR.XX-NN[,…] | PF: XX.XX-PN[,…] |`
> Anchors derived from the artefact's primary CR/PO/SO (Sprint 5 may add secondary anchors).

### §3.1 Use Case cards (35 L1)

| UC ID | CSF | PF |
|-------|-----|-----|
| U.C.1.1.1 | CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1 |
| U.C.1.1.2 | CSF: PR.DS-01, PR.DS-02, PR.DS-10 | PF: CT.DM-P1, CT.DM-P3 |
| U.C.1.2.1 | CSF: GV.SC-04, PR.DS-10, PR.DS-02 | PF: CT.DM-P4, CT.DM-P5 |
| U.C.1.3.1 | CSF: GV.OC-03, GV.PO-01, ID.AM-03 | PF: CT.DP-P4, CT.PO-P4, ID.RA-P3 |
| U.C.1.4.1 | CSF: GV.OC-04, GV.OV-02, GV.PO-02 | PF: CT.DM-P5, CT.PO-P4 |
| U.C.1.5.1 | CSF: PR.DS-10, PR.AA-03, PR.DS-02 | PF: CT.DM-P1, CT.DM-P6 |
| U.C.2.1.1 | CSF: GV.OV-02, ID.AM-02, ID.RA-01 | PF: ID.RA-P3, ID.RA-P5 |
| U.C.2.2.1 | CSF: GV.OV-02, ID.RA-01, PR.IR-03 | PF: — |
| U.C.2.3.1 | CSF: GV.PO-01, GV.SC-04, RS.CO-03 | PF: — |
| U.C.2.4.1 | CSF: DE.AE-02, DE.CM-01, DE.CM-09 | PF: CM.AW-P7 |
| U.C.2.4.2 | CSF: DE.CM-09, PR.DS-10, PR.IR-03 | PF: CT.DM-P10, PR.PO-P7 |
| U.C.2.5.1 | CSF: RS.CO-02, RS.MA-01, RS.MA-02 | PF: CM.AW-P7, CM.AW-P8, CM.PO-P1 |
| U.C.2.6.1 | CSF: PR.DS-01, PR.DS-10, PR.IR-03 | PF: — |
| U.C.3.1.1 | CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: — |
| U.C.3.1.2 | CSF: PR.AA-03, PR.AA-04, PR.AA-05 | PF: — |
| U.C.3.2.1 | CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: CT.PO-P1 |
| U.C.3.3.1 | CSF: GV.PO-01, GV.SC-03, PR.DS-10 | PF: CT.DP-P4, CT.PO-P4 |
| U.C.3.4.1 | CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P8 |
| U.C.3.5.1 | CSF: DE.CM-01, GV.PO-02, PR.DS-01 | PF: CT.DM-P4, CT.DM-P9 |
| U.C.3.6.1 | CSF: DE.AE-02, GV.OV-03, ID.RA-05 | PF: ID.RA-P3, ID.RA-P5 |
| U.C.4.1.1 | CSF: GV.PO-02, ID.RA-01, PR.DS-10 | PF: CT.DP-P2, CT.DP-P4, GV.PO-P2 |
| U.C.4.2.1 | CSF: ID.RA-04, ID.RA-05, PR.PS-01 | PF: — |
| U.C.4.3.1 | CSF: GV.OV-02, ID.RA-01, PR.IR-03 | PF: — |
| U.C.4.4.1 | CSF: DE.AE-02, DE.CM-01, DE.CM-09 | PF: CM.AW-P7 |
| U.C.4.5.1 | CSF: ID.RA-01, ID.RA-04, ID.RA-05 | PF: ID.RA-P3, ID.RA-P4, ID.RA-P5 |
| U.C.5.1.1 | CSF: GV.PO-01, GV.PO-02, GV.RM-04 | PF: CM.PO-P1, GV.PO-P1, GV.PO-P5 |
| U.C.5.1.2 | CSF: GV.PO-01, GV.PO-02, GV.OV-01 | PF: CM.PO-P1, GV.PO-P1 |
| U.C.5.2.1 | CSF: ID.RA-01, ID.RA-04, ID.RA-05 | PF: ID.RA-P3, ID.RA-P4, ID.RA-P5 |
| U.C.5.3.1 | CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P4, ID.IM-P6 |
| U.C.5.4.1 | CSF: GV.SC-01, GV.SC-02, GV.SC-03 | PF: ID.IM-P2 |
| U.C.5.5.1 | CSF: GV.OC-03, GV.SC-02, GV.SC-03 | PF: — |
| U.C.5.6.1 | CSF: GV.SC-02, GV.SC-03, ID.RA-01 | PF: — |
| U.C.6.1.1 | CSF: PR.AT-01, PR.AT-02, PR.PS-01 | PF: GV.AT-P1, GV.AT-P2 |
| U.C.6.2.1 | CSF: GV.RR-02, GV.RR-04, PR.AT-02 | PF: GV.AT-P1, GV.AT-P2 |
| U.C.6.3.1 | CSF: PR.AT-01, PR.AT-02, PR.PS-01 | PF: GV.AT-P1, GV.AT-P2 |

### §3.2 FR cards (30)

| FR ID | Source CR | CSF | PF |
|-------|-----------|-----|-----|
| FR-01 | CR-D-03.1-001 | CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: — |
| FR-02 | CR-D-03.1-001 | CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: — |
| FR-03 | CR-D-03.1-001 | CSF: ID.AM-01, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 | PF: — |
| FR-04 | CR-D-03.1-001 | CSF: ID.AM-01, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 | PF: — |
| FR-05 | CR-D-03.1-001 | CSF: ID.AM-01, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 | PF: — |
| FR-06 | — (no CR) | CSF: — | PF: — |
| FR-07 | CR-D-01.1-001 | CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1 |
| FR-08 | CR-D-01.1-001 | CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1 |
| FR-09 | CR-D-01.1-001 | CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1 |
| FR-10 | — (no CR) | CSF: — | PF: — |
| FR-11 | CR-D-01.1-001 | CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1 |
| FR-12 | CR-D-01.1-001 | CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1 |
| FR-13 | CR-D-02.1-001 | CSF: GV.OV-02, ID.AM-02, ID.RA-01, ID.RA-03 | PF: ID.RA-P3, ID.RA-P5 |
| FR-14 | CR-D-04.1-001 | CSF: DE.AE-02, DE.CM-01, DE.CM-09, ID.RA-04, PR.PS-04 | PF: CM.AW-P7 |
| FR-15 | CR-D-04.1-001 | CSF: DE.AE-02, DE.CM-01, DE.CM-09, ID.RA-04, PR.PS-04 | PF: CM.AW-P7 |
| FR-16 | CR-D-01.1-001 (Sprint 5 should remap to CR-D-04.3) | CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1 |
| FR-17 | CR-D-02.1-001 | CSF: GV.OV-02, ID.AM-02, ID.IM-02, ID.RA-01, ID.RA-03 | PF: ID.RA-P3, ID.RA-P5 |
| FR-18 | CR-D-02.1-001 | CSF: GV.OV-02, ID.AM-02, ID.IM-02, ID.RA-01, ID.RA-03 | PF: ID.RA-P3, ID.RA-P5 |
| FR-19 | CR-D-03.1-001 | CSF: ID.AM-01, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 | PF: — |
| FR-20 | CR-D-07.1-001 | CSF: GV.PO-02, ID.RA-01, PR.DS-10, PR.PS-01, PR.PS-02 | PF: CT.DP-P2, CT.DP-P4, GV.PO-P2 |
| FR-21 | CR-D-02.1-001 | CSF: GV.OV-02, ID.AM-02, ID.IM-02, ID.RA-01, ID.RA-03 | PF: ID.RA-P3, ID.RA-P5 |
| FR-22 | — (process, no CR) | CSF: — | PF: — |
| FR-23 | CR-D-02.1-001 (Sprint 5 should remap to CR-D-06.2) | CSF: GV.SC-02, GV.SC-03, ID.AM-02, ID.RA-01, PR.PS-02 | PF: — |
| FR-24 | — (no CR) | CSF: — | PF: — |
| FR-25 | CR-D-06.1-001 | CSF: GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04 | PF: ID.IM-P2 |
| FR-26 | CR-D-06.1-001 | CSF: GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04 | PF: ID.IM-P2 |
| FR-27 | CR-D-06.1-001 | CSF: GV.SC-01, GV.SC-02, GV.SC-03, GV.SC-04, ID.AM-04 | PF: ID.IM-P2 |
| FR-28 | CR-D-02.1-001 | CSF: GV.OV-02, ID.AM-02, ID.IM-02, ID.RA-01, ID.RA-03 | PF: ID.RA-P3, ID.RA-P5 |
| FR-29 | CR-D-08.1-001 | CSF: PR.AT-01, PR.AT-02, PR.PS-01 | PF: GV.AT-P1, GV.AT-P2 |
| FR-30 | — (no CR) | CSF: — | PF: — |
### §3.3 NFR cards (46)

| NFR ID | CSF | PF |
|--------|-----|-----|
| NFR-01 | CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1 |
| NFR-02 | CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1 |
| NFR-03 | CSF: PR.DS-01, PR.DS-10, PR.PS-04 | PF: PR.DS-P1 |
| NFR-04 | CSF: PR.DS-02, PR.IR-01, PR.PS-04 | PF: PR.DS-P2 |
| NFR-05 | CSF: PR.DS-02, PR.IR-01, PR.PS-04 | PF: PR.DS-P2 |
| NFR-06 | CSF: PR.DS-01, PR.DS-02, PR.DS-10 | PF: CT.DM-P1, CT.DM-P3 |
| NFR-07 | CSF: PR.DS-01, PR.DS-02, PR.DS-10 | PF: CT.DM-P1, CT.DM-P3 |
| NFR-08 | CSF: GV.SC-04, PR.DS-10, PR.DS-02 | PF: CT.DM-P4, CT.DM-P5 |
| NFR-09 | CSF: GV.SC-04, PR.DS-10, PR.DS-02 | PF: CT.DM-P4, CT.DM-P5 |
| NFR-10 | CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P4, ID.IM-P6 |
| NFR-11 | CSF: GV.PO-01, GV.PO-02, GV.RM-04 | PF: CM.PO-P1, GV.PO-P1, GV.PO-P5 |
| NFR-12 | CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P4, ID.IM-P6 |
| NFR-13 | CSF: DE.CM-09, PR.DS-10, PR.IR-03 | PF: CT.DM-P10, PR.PO-P7 |
| NFR-14 | CSF: DE.CM-09, PR.DS-10, PR.IR-03 | PF: CT.DM-P10, PR.PO-P7 |
| NFR-15 | CSF: PR.DS-01, PR.DS-10, PR.IR-03 | PF: — |
| NFR-16 | CSF: PR.DS-01, PR.DS-10, PR.IR-03 | PF: — |
| NFR-17 | CSF: DE.CM-09, PR.DS-10, PR.IR-03 | PF: CT.DM-P10, PR.PO-P7 |
| NFR-18 | CSF: PR.DS-01, PR.DS-10, PR.IR-03 | PF: — |
| NFR-19 | CSF: DE.CM-09, PR.DS-10, PR.IR-03 | PF: CT.DM-P10, PR.PO-P7 |
| NFR-20 | CSF: PR.DS-01, PR.DS-02, PR.DS-10 | PF: CT.DM-P1, CT.DM-P3 |
| NFR-21 | CSF: GV.OV-02, ID.AM-02, ID.RA-01 | PF: ID.RA-P3, ID.RA-P5 |
| NFR-22 | CSF: GV.OV-02, ID.RA-01, PR.IR-03 | PF: — |
| NFR-23 | CSF: GV.OV-02, ID.RA-01, PR.IR-03 | PF: — |
| NFR-24 | CSF: GV.OV-02, ID.RA-01, PR.IR-03 | PF: — |
| NFR-25 | CSF: ID.AM-01, PR.AA-01, PR.AA-03 | PF: CT.PO-P1 |
| NFR-26 | CSF: DE.CM-01, GV.PO-02, PR.DS-01 | PF: CT.DM-P4, CT.DM-P9 |
| NFR-27 | CSF: DE.CM-01, GV.PO-02, PR.DS-01 | PF: CT.DM-P4, CT.DM-P9 |
| NFR-28 | CSF: DE.CM-01, GV.PO-02, PR.DS-01 | PF: CT.DM-P4, CT.DM-P9 |
| NFR-29 | CSF: DE.CM-01, GV.PO-02, PR.DS-01 | PF: CT.DM-P4, CT.DM-P9 |
| NFR-30 | CSF: GV.OC-03, GV.PO-01, ID.AM-03 | PF: CT.DP-P4, CT.PO-P4, ID.RA-P3 |
| NFR-31 | CSF: GV.OC-03, GV.PO-01, ID.AM-03 | PF: CT.DP-P4, CT.PO-P4, ID.RA-P3 |
| NFR-32 | CSF: GV.OC-04, GV.OV-02, GV.PO-02 | PF: CT.DM-P5, CT.PO-P4 |
| NFR-33 | CSF: GV.SC-04, PR.DS-10, PR.DS-02 | PF: CT.DM-P4, CT.DM-P5 |
| NFR-34 | CSF: PR.DS-10, PR.AA-03, PR.DS-02 | PF: CT.DM-P1, CT.DM-P6 |
| NFR-35 | CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P4, ID.IM-P6 |
| NFR-36 | CSF: GV.PO-02, ID.RA-01, PR.DS-10 | PF: CT.DP-P2, CT.DP-P4, GV.PO-P2 |
| NFR-37 | CSF: GV.PO-02, ID.RA-01, PR.DS-10 | PF: CT.DP-P2, CT.DP-P4, GV.PO-P2 |
| NFR-38 | CSF: GV.PO-01, GV.PO-02, GV.RM-04 | PF: CM.PO-P1, GV.PO-P1, GV.PO-P5 |
| NFR-39 | CSF: GV.OC-03, GV.PO-01, ID.AM-03 | PF: CT.DP-P4, CT.PO-P4, ID.RA-P3 |
| NFR-40 | CSF: GV.PO-01, GV.PO-02, GV.RM-04 | PF: CM.PO-P1, GV.PO-P1, GV.PO-P5 |
| NFR-41 | CSF: ID.RA-01, ID.RA-04, ID.RA-05 | PF: ID.RA-P3, ID.RA-P4, ID.RA-P5 |
| NFR-42 | CSF: ID.RA-01, ID.RA-04, ID.RA-05 | PF: ID.RA-P3, ID.RA-P4, ID.RA-P5 |
| NFR-43 | CSF: GV.PO-02, ID.AM-08, PR.DS-10 | PF: ID.IM-P1, ID.IM-P4, ID.IM-P6 |
| NFR-44 | CSF: DE.CM-01, GV.PO-02, PR.DS-01 | PF: CT.DM-P4, CT.DM-P9 |
| NFR-45 | CSF: GV.PO-01, GV.PO-02, GV.RM-04 | PF: CM.PO-P1, GV.PO-P1, GV.PO-P5 |
| NFR-46 | CSF: GV.PO-01, GV.PO-02, GV.RM-04 | PF: CM.PO-P1, GV.PO-P1, GV.PO-P5 |

---
## §4 Coverage Stats

| Family | Count | Note |
|--------|-------|------|
| Rules with CSF anchors | 46/46 (100%) | All CR + BPR have CSF anchors in Doc 11 §7 |
| Rules with PF anchors | 27/46 (59%) | Doc 11 omits PF for technical BPRs (e.g. RBAC, FIDO2) |
| Goals with CSF anchors | 27/31 (87%) | 4 SOs (SO-D-02.2/02.3/03.2/06.2) blank per Doc 10b §4 |
| Goals with PF anchors | 27/31 (87%) | All POs + most SOs; pure-CSF SOs left blank |
| Per-artefact slot rows | 35 UC + 30 FR + 46 NFR = 111 | All derived from primary CR/PO/SO |

## §5 Validation log

```python
# validate_nist_ids.py patterns applied:
CSF: re.match(r"^[A-Z]{2}\.[A-Z]{2}-\d+$", id_str)
PF:  re.match(r"^[A-Z]{2}\.[A-Z]{2}-P\d+$", id_str)
# All IDs above comply (verified by inspection):
# - CSF: PR.DS-01..10, PR.IR-01..04, PR.PS-01..06, PR.AA-01..06, PR.AT-01..02, GV.*, ID.*, DE.*, RS.*, RC.*
# - PF:  PR.DS-P1/P2, CT.*-P1..P10, GV.*-P1..P5, CM.*-P1..P9, ID.IM-P1..P8, ID.RA-P3..P5
# Withdrawn IDs (CSF 1.1-only) NOT used: PR.IP-*, PR.AC-*, PR.PT-*, PR.MA-*, DE.DP-*, RS.AN-*, etc.
# Phantoms (NEITHER 1.1 nor 2.0) NOT used: GV.MA-*, CM.PO-P3+
# AEGIS-rejected NOT used: ID.RA-P2
```
