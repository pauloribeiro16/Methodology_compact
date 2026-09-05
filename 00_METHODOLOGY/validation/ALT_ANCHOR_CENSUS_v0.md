# ALT-ANCHOR Census v0 — element-level dedup (Fase 0)

**Rule:** one row per canonical gap-element (a missing PF/CSF subcategory concept), with all
occurrence sites listed. Anchor proposals respect realization_class routing
(TECHNOLOGY: 800-53r5→SSDF→ASVS · PROCESS: 800-53r5→SAMM · CAPABILITY: SAMM→800-53→ISO 27002).
**Status:** C1 element table COMPLETE (from matrix §1 rows + card lines; justification texts read).
C2 / C3 tables PENDING (next step).

---

## Case_01 — canonical gap elements (12) + occurrence sites

| # | Element (missing concept) | Lacks | realization_class → route | Occurrence sites (file:line) | Proposed anchor (working) | Conf. |
|---|---|---|---|---|---|---|
| E1 | PR.PS-04 log records / secure-development logging | PF | TECHNOLOGY → 800-53r5 | Doc19:77, Doc18:179, Doc16 card SO-D-03.1 context; Doc18:994 (03.3), Doc19:91 (03.3) | 800-53r5 AU-2/AU-3 (event logging); SSDF PW.8/PW.9 | HIGH |
| E2 | PR.DS-10 risk-strategy data management | PF | PROCESS → 800-53r5 | Doc19:77 (01.1), Doc18:799 (03.1), Doc18:1479 (04.4), Doc16 L1224 | 800-53r5 PM-4/PM-6 (risk mgmt plan) or RA family | MED |
| E3 | ID.AM-01 asset inventory (privacy side) | PF | TECHNOLOGY → 800-53r5/SSDF | Doc19:84 (03.1), Doc18:799, Doc18:994 (03.3), Doc19:88 (03.3) | 800-53r5 CM-8 (system component inventory); SSDF PO.5 | HIGH |
| E4 | Identity assertions protected/verified | PF | TECHNOLOGY → ASVS/800-53r5 | Doc19:85 (03.2), Doc18:898, Doc18:3470 (BPR-03.2 FIDO2), Doc19:1285 (BPR-10.3, GAP-flagged), Doc16 L1289 | ASVS V3.5 (token/assertion binding); 800-53r5 IA-4 | HIGH — BPR-10.3 instance already GAP-flagged at MICRO, keep NO-ANALOGUE candidate for that occurrence |
| E5 | RS.MA-03 incident-authority reporting | PF | PROCESS → 800-53r5 | Doc19:88 (04.1), Doc19:90 (04.3), Doc18 mirrors | 800-53r5 IR-6 (incident reporting) | HIGH |
| E6 | RC.RP recover-execution (PF 1.0 has no Recover axis) | PF | TECHNOLOGY → 800-53r5/SSDF | Doc19:91 (04.4, 3 cells), Doc18:1479, Doc16 L1679 | 800-53r5 CP-10 (recovery/reconstitution); SSDF PW.9 | HIGH |
| E7 | Ecosystem risk → enterprise risk integration | PF | PROCESS → 800-53r5/SAMM | Doc19:98 (06.3), Doc18:2150, Doc16 L1874 | 800-53r5 SR-6/PM-30? (supply-chain risk integration); SAMM ORG-B? | MED |
| E8 | GV.RM-04 positive-risk / strategic opportunities | PF | CAPABILITY → SAMM/800-53 | Doc19:102 (09.1), Doc18:2539, Doc19:1255 (BPR-10.3), Doc16 L1224? | 800-53r5 PM-8/RA family; SAMM GRC? — likely NO-ANALOGUE (positive risk is not a security control) | LOW |
| E9 | Stakeholder expectations register (ID.BE-P5 draft only) | PF | CAPABILITY | Doc19:1242 (BPR-10.3) | NO-ANALOGUE candidate (out-of-MICRO scope by design) | HIGH |
| E10 | Outcomes organisation depends on (ID.BE-P6 draft only) | PF | CAPABILITY | Doc19:1243 (BPR-10.3) | NO-ANALOGUE candidate (same) | HIGH |
| E11 | Identity assertions + stakeholder cluster (BPR-10.3 §6.2) | PF | — | Doc19:1242-1285 | split per E4/E9/E10 | — |
| E12 | Data portability (GDPR Art. 20) — no CSF 2.0 subcategory | CSF | PROCESS → 800-53r5/ISO | Doc16:1873 (DPA card, beside GV.SC-04) | 800-53r5 PT-2?/AC-… — likely NO-ANALOGUE in NIST set; ISO 27002 A.5.34 (privacy/PII) candidate | MED |

Additional C1 occurrence sites to migrate with the same elements: Doc16 L133/134/145/153
(objective cards mirroring CR-D-03.1/03.2/04.4/06.3), Doc18 cards fields 20 (L785, L884,
L1465, L2136, L3376), Doc19 note L147/108 (audit context lines — vocabulary, may need
wording update but not anchors).

**C1 totals:** 52 raw occurrences → 12 canonical elements (8 likely anchorable HIGH/MED,
3 NO-ANALOGUE candidates, 1 LOW needing adjudication).

## Case_02 — canonical gap elements (8: 7 PF + 1 CSF) — COMPLETE

| # | Element | Lacks | class → route | Occurrence sites | Proposed anchor (working) | Conf. |
|---|---|---|---|---|---|---|
| G1 | Product patch/OTA update management | PF | TECHNOLOGY → SSDF/800-53 | Doc19:76,1268; Doc18 mirror | SSDF PS.1+PW.4; 800-53r5 SI-2/SI-7 | HIGH |
| G2 | MFA (no PF-specific subcategory) | PF | TECHNOLOGY → 800-53/ASVS | Doc19:80,1272; Doc18 mirror | 800-53r5 IA-2(1) (same control the PF PR.AC-P6 JSON crosswalks to); ASVS V3.3 | HIGH |
| G3 | Backup/DR recovery | PF | TECHNOLOGY → 800-53 | Doc19:86,1278; Doc18 mirror | 800-53r5 CP-9+CP-10 | HIGH |
| G4 | Data portability (GDPR Art. 20) | CSF | PROCESS → ISO last resort | Doc19:90,1282; Doc18 mirror | NO-ANALOGUE in NIST set → ISO 27002:2022 A.5.34 | MED (adjudicate) |
| G5 | Physical third-party boundary isolation | PF | TECHNOLOGY → 800-53 | Doc19:94,1286; Doc18 mirror | 800-53r5 PE-3(+PE-6) | HIGH |
| G6 | Secure-SDLC | PF | PROCESS → SSDF/800-53 | Doc19:96,1288; Doc18 mirror | SSDF PW group (PW.1, PW.4-8); 800-53r5 SA-8 | HIGH |
| G7 | Board-level training | PF | CAPABILITY → SAMM/800-53 | Doc19:101; (Doc18: none) | SAMM EG (Education & Guidance) L1-2; 800-53r5 AT-2/AT-3 | MED |
| G8 | Compliance-testing | PF | CAPABILITY/PROCESS → 800-53/SAMM | Doc19:108,1297 | 800-53r5 CA-2/CA-7; SAMM VR-B | HIGH |

C2 NIST_ANCHORS.md (8 lines, 03_PHASE3_DECOMPOSITION) mirrors the same elements — map during write-back.

## Case_03 — canonical gap elements (9: 8 PF + 1 CSF) — COMPLETE

Same canonical family as C2 plus one new element:
| # | Element | Lacks | class → route | Occurrence sites | Proposed anchor (working) | Conf. |
|---|---|---|---|---|---|---|
| G1–G8 | same elements as C2 (patch/OTA, MFA, backup/DR, portability, third-party boundary, secure-SDLC, board-training, compliance-testing) | PF/CSF | as C2 | Doc20 §1 rows L78-110 + §6.2 mirrors L1639-1707 (CR+BPR pairs); Doc19 14 card lines; NIST_ANCHORS.md 15 lines; Doc14:1 (P1 doc) | as C2 | — |
| G9 | CI/CD pipeline security controls | PF | TECHNOLOGY → SSDF/ASVS/800-53 | Doc20:99,1660,1696 (CR-D-07.3-001 + BPR pair) | SSDF PW.7+PW.8; ASVS V14; 800-53r5 SA-15/SI-7 | HIGH |

Note: C3 BPR rows (L1678-1707) are secondary-policy mirrors of the CR gap elements — same
canonical elements, dedup keeps them as occurrences, not new decisions.
C3 has one live occurrence in `_deprecated/Doc15_Appendix_A_OLD.md` — OUT of scope (deprecated dir,
gate-excluded).

---

*Source evidence: conversation extraction 2026-09-05 (Doc19 §1 rows L77-108; Doc18 card
grep; Doc16 objective rows). BPR-10.3 justifications quoted in full above.*
