# P7 Briefing Pack — 2026-09-05

**Purpose.** The 4 items below are **human-decision territory (P7)**. This pack
distils the fact-pack evidence (see `validation/REALIZATION_CLASS_RUBRIC_VALIDATOR_REPORT_v0.md`
for the campaign context, and `02_CASES/PORT_PARITY2_VERIFICATION_REPORT.md` for the
prior verification work). Each item is presented as a brief, three options, and
the Orchestrator's recommendation based on what the data actually shows.

**Decision contract.** Pick A/B/C per item (or propose alternative). Decisions are
recorded by the human into `02_CASES/PENDING_CAMPAIGNS_LEDGER.md` §5; implementation
campaigns are planned and approved separately. This pack is informational — it does
**not** modify any case doc.

---

## Item 1 — OBL-D-06.2-001 (Case_03, SBOM / PS.3 orphan)

### Context
- Domain D-06.2 in Case_03 has **only two rules**: `CR-D-06.2-001` (CRA sole authority)
  and `BPR-D-02.2-001` (originally D-02.2, EO 14028 supply-chain).
- `BPR-D-06.2-001` does **not exist** (grep returns 0 hits anywhere).
- Chain: `AG-D-06.2-002` (sole PG) → `OBL-D-06.2-001` → `CR-D-06.2-001`. The
  `AG-D-06.2-001` is intentionally absent (Doc 10 §3, sole sub-domain).
- Regulation: **CRA Annex I §18** (CRA-C18) — SBOM is the "sole authority" obligation
  of D-06. Doc20 §1 shows `PS.3 = 1` for D-06.2 — only one PS.3-tagged rule for the
  entire SBOM sub-domain.
- Files: `02_CASES/Case_03_OmniBank_Financial/02_PHASE2_RULES_RICH/Doc19_Rules_Catalog.md:383,430`,
  `TRACEABILITY_AUDIT.md:92`, `Doc17_Privacy_Security_Objectives.md:140`,
  `Doc15_Obligation_Derivation.md:156`, `Doc20_Framework_Mapping_Matrix.md:94`.

### Options
| | Approach | What changes | Risk |
|---|---|---|---|
| **A** | **Accept BPR-D-02.2-001 dual-duty** (recommended) | Update Doc19/Doc20 narrative to document the overlap explicitly. Add a Doc20 §X note: "D-06.2 PS.3 anchor lives in BPR-D-02.2-001 (cross-domain reuse, deliberate per PORT-PARITY-2 verification)". No new rule. | LOW — minimal disruption |
| B | Create `BPR-D-06.2-001` focused on SBOM | Adds 1 rule to Doc11, Doc14, Doc19, Doc20, Doc26, Doc27, control_set.yaml. Aligns naming, improves PS.3 coverage. | MEDIUM — adds new content that must trace through all 7 docs |
| C | P7 ratifies GAP as LEGIT, adds Doc19/Doc20 note | Like A but states explicitly that the orphan remains; ratifies as P7 decision. | LOW — same as A but with explicit ratification |

### Orchestrator recommendation
**A.** The fact-pack shows the overlap is already working operationally (BPR-D-02.2-001
double-duties on PS.3). Option B creates more work than it solves; C is essentially A
with extra process. A keeps everything traceable and adds one explicit note.

---

## Item 2 — verify_rich FAILs (Case_02 + Case_03)

### Context
11 FAILs documented across the two cases. Source:
`02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/validation/RICH_LINT_BASELINE.md`
and `Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/validation/RICH_LINT_BASELINE.md`.

| FAIL | Sev | What | Pattern |
|---|---|---|---|
| F5-C2-01 | HIGH | FR traceability sparse: 25/84 FRs carry `Source Rule = —`; only 10 distinct rules cited at FR level | Real content drift (April FR cards pre-date corr-008) |
| F5-C2-02 | MEDIUM | Stale count claims ("53 rules", "44 UCs") in Doc25 + catalog | Known-pattern (P2 renumber to 63 controls) |
| F5-C2-03 | LOW | Doc29 FR-71 and FR-72 duplicated rows (86 rows / 84 unique) | Real content drift |
| F5-C2-04 | LOW | 0/8 P3 docs carry `case:` frontmatter field | Known-pattern (corr-008 8-field completeness) |
| F5-C3-01 | MEDIUM | "63 rules" stale on Doc26; complexity frontmatter says 63 vs frozen 78 | Known-pattern |
| **F5-C3-02** | **HIGH** | **Doc31 NFR inconsistency: summary says 56 NFRs (per-category sum 12+10+12+10+6+6) but only 12 cards (NFR-01..12) defined** | Real content drift (suspected truncation) |
| F5-C3-03 | LOW | BPR-D-12.1-001 absent from Doc26 §3 allocation (present in Doc27 + control_set) | Real content drift |
| F5-C3-04 | LOW | Doc23 references dangling UC-99 (Doc22 ends at UC-62) | Real content drift |
| F5-C3-05 | LOW | Same as F5-C2-04 (`case:` field) | Known-pattern |
| F5-C3-06 | MEDIUM | 5 FR cards cite raw article citations (FR-59 AI-C09/10; FR-62 DORA-C38; FR-63 GDPR Art. 35; FR-64 AI Act Art. 28; AI Act Art. 14) instead of catalog rule ids | Real content drift (corr-008 requires rule-layer IDs) |
| F5-C3-07 | INFO | CR-D-05.4-001 + 34 N/A AI-RMF placeholders + 6 `status_csf: —` | Known-pattern (deliberate gap) |

### Options
| | Approach | What changes | Risk |
|---|---|---|---|
| A | Accept all 11 as honest baseline, do nothing | Ledger §5 keeps 11 FAILs as known-pattern | LOW — current state, no work |
| **B** | **Close only the 2 HIGH now** (recommended) | Fix F5-C2-01 (relink 25 FR orphans to CR/BPR — overlaps with Item 7's Volere pilot on PKG-9) + F5-C3-02 (decide: restore 44 NFR cards OR correct summary to 12). The 9 LOW/MEDIUM remain as honest baseline. | MEDIUM — C2-01 fully addressed by Item 7; C3-02 needs your decision on "restore vs recount" |
| C | Close all 11 FAILs in one campaign | ~3 days of work; fixes catalog row counts, dangling UC-99, 5 raw citations, etc. | MEDIUM-HIGH — broad touch across 8 docs |

### Orchestrator recommendation
**B.** Targeted: F5-C2-01 is largely addressed by Item 7 (the Volere pilot on PKG-9
will link 5–8 orphan FRs as part of its work; the remaining 17 are candidates for a
follow-on wave). F5-C3-02 needs the explicit decision "restore 44 NFRs OR correct
summary". The rest of the 9 are honest baseline and don't block anything.

---

## Item 3 — D-07.2 coverage Case_01 (4 orphan obligations)

### Context
- 4 orphan obligations: `OBL-D-07.2-001`, `OBL-D-07.3-001`, `OBL-D-07.4-001`,
  `OBL-D-10.1-001`. All CRA-anchored (CRA-C02, CRA-C22, CRA-C12).
- Source: `02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/TRACEABILITY_AUDIT.md:103-106,162`,
  `Doc14_Obligation_Derivation.md:123`.
- "F-07 cross-doc orphan" — obligations added in Doc08 (Sprint 6+) referencing
  `CR-D-XX.X-001` placeholders that didn't exist in Doc11 §4 at the time.
- Mitigation: `BPR-D-07.2-001` (SAST/DAST in CI/CD, framework = OWASP ASVS V3) covers
  the SAST/DAST intent; N/A marker signals "no dedicated CR exists, BPR framework
  reference suffices". Doc23 architectural nodes already point at the orphan CRs via
  `BPR-D-07.2-001` (lines 70, 88, 93, 94, 125, 126).
- `PROJECT_STATE.md:42` lists "AUD-P2-005 — 4 obligations orphan, mitigated by
  BPR-D-07.2-001 N/A marker".

### Options
| | Approach | What changes | Risk |
|---|---|---|---|
| A | Add 4 new CRs (Doc11 §4 + Doc14 + Doc23 + Doc27) | Adds 4 new rule cards; full coverage parity. | HIGH — adds 4 rules to chase through every doc |
| **B** | **Formal accept the mitigation** (recommended) | Withdraw the `N/A marker` from `BPR-D-07.2-001`; mark Doc23 / Doc27 nodes "BPR-anchored closure"; update Doc14 and PROJECT_STATE audit row to reflect the P7 decision. **No new rules.** | LOW — already operationally covered; just paperwork |

### Orchestrator recommendation
**B.** The fact-pack shows the operational coverage already exists (ASVS V3 reference
in `BPR-D-07.2-001`, architectural nodes pointing at the orphans via the BPR arrow).
Adding 4 new CRs adds no security value — it adds traceability work. B formalises
what is already true.

---

## Item 4 — Phantom refs

### Context
Two distinct lineages of phantoms, all deliberate:
1. **AEGIS F-01 / F-03 lineage**: `PO-D-01.3-001` / `PG-D-01.3-001` referenced by
   `CR-D-01.3-001` while the underlying PO/PG was intentionally deleted (CRA sole
   authority key-management). Carried LOW in Sprint reports across C1/C2/C3.
   Source: `RULE_FREEZE.md:53,102,129` ("Legacy PO-D-01.3-001 references are intentional
   phantoms per F-03").
2. **PORT-PARITY-2 verification cross-case phantoms**: 2 phantom citations confirmed
   PASS in `PORT_PARITY2_VERIFICATION_REPORT.md:19` (one historical, one legitimate
   cross-case note in `PRODUCTION_FLOW.md:42`).
3. **C1 historical cleanup (2026-04-06)**: 10 phantom derivation nodes removed, plus
   UC/node/gate phantoms — all reconciled.
4. **corr-008 reconciliation**: legacy `PG-` / `SG-` suffixed refs mapped to `AG-`
   in Doc13 Appendix A alias tables.

### Options
| | Approach | What changes | Risk |
|---|---|---|---|
| **A** | **Maintain as-is** (recommended) | Already documented in SPRINT_REPORTs + VALIDATOR_SPRINT5. Add explicit ledger row ratifying the maintenance. | LOW |
| B | Add explicit "phantoms by design" note in Doc13/Doc14 of each case | More visible provenance; but adds frontmatter noise. | MEDIUM — touches 6 docs for a metadata-level clarification |

### Orchestrator recommendation
**A.** The phantoms are a design feature, not a defect; the documentation trail is
complete (F-01 / F-03 audit trail). Adding per-doc banner notes would create the
impression that there is a problem to be flagged when there isn't. The ledger will
note that this item is ratified as-is.

---

## Decision template (for the human)

For each item, pick a letter (or write your own variant):

```
Item 1 (OBL-D-06.2-001): [A / B / C / custom]
Item 2 (verify_rich FAILs): [A / B / C / custom]
Item 3 (D-07.2 coverage C1): [A / B / custom]
Item 4 (phantom refs):       [A / B / custom]
```

Record the decisions in `02_CASES/PENDING_CAMPAIGNS_LEDGER.md` §5 and the human will
approve the resulting implementation campaign(s) in a follow-up plan.
