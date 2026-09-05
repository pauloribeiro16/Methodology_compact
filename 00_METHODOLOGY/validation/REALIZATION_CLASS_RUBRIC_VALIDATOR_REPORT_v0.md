---
document_id: AEGIS-METH-RC-RUBRIC-VALIDATOR-REPORT-V0
title: Validator Report — Independent Review and Classification Dry-Run of REALIZATION_CLASS_RUBRIC v1.0
phase: Cross-phase
version: 0.1
created: 2026-09-05
updated: 2026-09-05
author: Validator
status: ACTIVE
---

# Validator Report — REALIZATION_CLASS_RUBRIC v1.0 (2026-09-05)

> **Verdict: `APPROVED_WITH_AMENDMENTS`** (amendments listed in §6).
> Independent dry-run: 46/46 rules classified (30 CR + 16 BPR — recount confirms), 0 undecidable, distribution **TECHNOLOGY 20 / PROCESS 20 / CAPABILITY 6**. All 9 rubric exemplars (§8) independently reproduced (9/9 primary agreement; 1 optional-secondary difference).
> Independence statement: the Executor report was read **only** for §4 Open Questions and the 9 exemplars (§A.6 comparison). No pre-existing classification was consulted; none exists yet in any case artifact.

---

## 1. Findings — §A.1 Testability of §2 class definitions and §3 decision tree

**Overall: testable in structure, weak at two seams.** The closed enum, ordered tree (first-YES-wins), STOP provision, and secondary-class constraint (0..1, ≠ primary) are all decidable. The dry-run reached a class for 46/46 rules with 0 STOPs — strong evidence the tree terminates. However:

1. **T-disqualifier vs "periodic re-verification" is not operationalized.** §2 (rubric L31) disqualifies TECHNOLOGY when "sustaining it requires recurring human triage, approval, notification or escalation decisions", but the positive test (L31) explicitly permits "only periodic re-verification". Most Doc18 cards contain a quarterly review (≈2/3 of cards), several with explicit sign-off — e.g. CR-D-03.1-001 criterion "A quarterly orphan-account and role-claim review has CTO sign-off" (`Doc18_Rules_Catalog.md` L728); CR-D-03.3-001 L917. Is a CTO sign-off a "recurring approval decision" (→ not TECHNOLOGY) or "re-verification" (→ TECHNOLOGY)? Two readers can diverge. Validator resolution used in §4 below: a recurring step is **constitutive** (Q1 = NO) only if its outcome *changes what the control accepts or permits* (exception approval, risk acceptance, containment decision); a recurring step that only *re-checks built state* is re-verification (Q1 = YES). This test is not in the rubric — proposed as Amendment A3.

2. **The P/C seam is the least decidable boundary.** The tie-break "Run the procedure again → PROCESS. Keep the ability alive → CAPABILITY" (rubric L68) is a metaphor, not a test. 8 of my 46 calls were genuinely hard P/C cases (CR-D-06.1, 06.3, 07.1, 08.1, 09.4, 10.3, BPR-D-04.3-001, BPR-D-07.1-001). Concrete instability demonstrated by the rubric itself: **CR-D-08.1-001 (Annual Security Awareness) and CR-D-08.2-001 (Role-Specific Competence) have near-identical card structure** (owner trio CTO+HR+DPO, artefact [programme/matrix], completion records, quarterly content review, method INSPECT — Doc18 L2218-2226 vs L2313-2321), yet the rubric exemplifies 08.2 as CAPABILITY and never states where 08.1 falls. A rater applying the tie-break literally ("run the training again" vs "keep competence alive") can land either rule in either class. See Amendment A4.

3. **Q1-first ordering biases toward TECHNOLOGY, correctly but silently.** Because most cards contain *some* recurring human element, the classification effectively turns on whether that element is constitutive. The rubric works because its tie-break sentence "If the automated path alone satisfies all verification criteria → TECHNOLOGY" (L67) is actually the sharpest instrument in the document — it should be promoted from tie-break guidance to a primary test step (Amendment A3).

---

## 2. Findings — §A.2 Tie-breaks

- **TECHNOLOGY vs PROCESS (rubric L67): decidable.** "Where does the assurance live" + "automated path satisfies all verification criteria" resolved every T/P case I encountered, including both §8 borderlines. Verified against the cards: CR-D-02.2-001's human-review mandate is verbatim in the card ("must still retain human review for failed patches, compatibility issues, and exceptions affecting customer availability", Doc18 L517-518) and the exception approval appears **in the verification criteria** (L541 "recorded remediation or approved exception within 72 hours") — constitutive. CR-D-03.2-001's exception clause appears only in the Description (L799-800), not in the criteria (L815-821) — exception-path. The rubric's borderline 1 resolution is reproducible.
- **PROCESS vs CAPABILITY (rubric L68): not fully decidable** — see §1 item 2. It hides no *new* ambiguity but leaves the pre-existing one open.
- **Multi-class provision (L69): clear and decidable** (secondary ≠ primary, max 1). No rule in my dry-run needed more than one secondary.

---

## 3. Findings — §A.3 §4 attribute spec vs actual Case_01 Phase 2 artifacts

| Claim in §4 (rubric L80-87) | Verified against reality | Result |
|---|---|---|
| "One column in the catalog index/summary table" of Doc18 | Doc18 §2 "CONTROL SET SUMMARY & STATISTICS" (Doc18 L39-71) is a per-sub-domain count table (**no per-control column exists**). Per-control indexes are Anexo A/B/C (L4300+). Also: adding a card field collides with frontmatter `fields_per_card: 24` / `expected_fields_per_card: 24` (Doc18 L21-23) and the 24-field schema table (L75-102) — neither §4 nor the rubric mentions bumping these counters. Doc18 also has 92 duplicated "14. Implementation Priority" lines and 0 fields numbered 13 — the "authoritative" catalog's own numbering is defective. | **Imprecise** — needs Amendment A1 |
| `12_Rules_Catalog.xlsx` "one column per field in the rules sheet" | Sheet `Rules_Catalog` exists, 46 data rows (30 CR + 16 BPR, counted via openpyxl, IDs in col B), header at row 5 with **17 legacy columns** and its own note "11 legacy fields"; values are stale vs Doc18 v4.0 (e.g. CR-D-01.1-001 NI 2.667/P1 in xlsx vs NI 3.0/MUST in Doc18; criteria cells are "(Sprint 4 stub)"). | **Misleading as-is** — the "kept in sync" invariant (rubric L80, L89) is unverifiable against a stale mirror. Amendment A2 |
| `control_set.yaml` per-control entry | Exists; each of the 46 entries carries `id/register/domain/title/ni/legal/trace/anchors/status/verification`. A `realization_class:` key per entry fits cleanly. | **Consistent** |
| `phase2_ontology.yaml` enum + attrs on `ComplianceRule`/`BestPracticeRule` | `kg_ontology.enums` block exists (phase2_ontology.yaml L174-180, currently 6 enums, no `RealizationClass` — correct pre-campaign state); classes `ComplianceRule` (L104) and `BestPracticeRule` (L128) exist; the proposed enum style matches the existing `Priority: [MUST, SHOULD, COULD]` style. | **Consistent** |

---

## 4. Findings — §A.4 §6 CAPABILITY anchor to Phase 1 ontology

**Verified — the anchor is correct.** `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml`:

- `kg_ontology.maturity_model` block starts L1635; `scales.capability` at **L1644** with comment `# Scale A`, `name: "Capability (CSF 2.0 native)"`, `scope: ["Organisation", "Function"]` (L1644-1648). Rubric's cited range "~lines 1644–1713" is accurate (covers capability at 1644 through the evidence relations ending ~1721; `CITES_OUTCOME` itself sits at L1709-1711, inside the range).
- `CITES_OUTCOME` cardinality "N:1 when scale=capability; 0 when scale=coverage" at L1709-1711; `CITES_CLAUSE` "N:1 when scale=coverage; 0 when scale=capability" at L1712-1714 — the rubric's parenthetical "(scale=capability ⇒ CITES_CLAUSE absent)" matches.
- `EvidenceItem` class at L1669 with `scale: enum(ScaleRef)`, `ScaleRef: [capability, coverage]` — the rubric's "CapabilityEvidence item" construction is consistent with the schema.
- Vocabulary note verified: v1.6 block authority is `MATURITY_MODEL_CSF_STRICT.md v1.0` (L1636); `00_METHODOLOGY/IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md` frontmatter reads `version: "2.0"`, `supersedes: "MATURITY_MODEL_CSF_STRICT.md v1.0"`. The rubric's decision to anchor on structural elements while deferring tier vocabulary is the correct call.
- Visualisation: `00_METHODOLOGY/00_VISUALISATIONS/Case_01/Case_01_P1_Dashboard.html` exists and contains the "Folio VIII" label. Nit: the rubric cites the path without the `00_METHODOLOGY/` prefix (Amendment A7, trivial).

---

## 5. Findings — §A.5 §7 ISO crosswalk and §A.6 worked examples

**§A.5 — §7 crosswalk: internally consistent and correctly labelled non-normative.** The theme counts are correct (ISO/IEC 27002:2022: 93 controls = 37 organizational + 8 people + 14 physical + 34 technological). The "indicative, non-normative" label is present and prominent. The divergence example is real: CR-D-05.3-001's card carries `ISO 27001: A.8.10` (Doc18 L1715) and the rubric legitimately PROCESS-classes it. **One internal inconsistency:** §7 folds physical controls into TECHNOLOGY ("insofar as the realization is an artefact property"), but §2's TECHNOLOGY definition ("system/hardware/software build or configuration", rubric L31) does not cover physical artefact measures. Amendment A5.

**§A.6 — 9 worked examples: faithful.** Spot-check of the 4 borderlines/secondaries plus the other 5:

| Rule | Rubric claim | Card evidence | Faithful? |
|---|---|---|---|
| CR-D-02.2-001 (P+T) | Human-review mandate quote; severity SLA; exception owner | Quote verbatim (Doc18 L517-518); criteria L537-543 include 72h remediation-or-approved-exception; quarterly reconciliation | Yes |
| CR-D-09.2-001 (C+P) | "route unresolved scope or risk acceptance to the human decision-maker"; owners, competence, refresh | Quote verbatim (Doc18 L2486); criteria L2501-2507 include human approval/escalation | Yes |
| CR-D-05.3-001 (P) | intake→identity verification→cascade→tombstone→log, 7-day SLA | Matches scope/implementation/criteria (Doc18 L1642-1665) | Yes |
| CR-D-09.1-001 (C) | owners, approvals, review records, reconciliation to operating evidence, 10-year retention | Matches (Doc18 L2379-2413) | Yes |
| CR-D-01.1-001 (T) | "verification criteria are configuration reports" | 2 of 3 criteria are reports; 3rd is periodic review (T-compatible). Slight overstatement, not a defect | Yes |
| CR-D-03.2-001 (T) | automated test rejects sessions without second factor | Criterion verbatim (Doc18 L817) | Yes — note card header anomaly "MUST, NI=2 (SHOULD)" (L784), already flagged by Executor |
| CR-D-10.2-001 (T) | trail, Object Lock, log-failure alerting, retention | Matches (Doc18 L2670-2694) | Yes |
| CR-D-04.3-001 (P) | decision tree, 24h clock, per-recipient submissions, tabletop | Matches (Doc18 L1266-1291) | Yes |
| CR-D-08.2-001 (C) | matrix + named roles + quarterly review, INSPECT | Matches (Doc18 L2313-2321) | Yes |

Titles match Doc18 headings (03.2 abbreviated — acceptable). **All 9 primary classes independently reproduced by this Validator** (see §7 table); the only difference is optional-secondary on CR-D-05.3-001 (I add TECHNOLOGY secondary; the rubric omits it — permitted, not a conflict).

**Additional factual defect found outside §A.6 scope (preamble, rubric L14):** the claim that the triad is "already used as node tracks in Phase 3 architectural nodes (**Doc14/23/25 across cases**)" is **wrong on all three counts**. Corpus-wide grep for `track=` returns exactly one file: `Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/Doc23_Architectural_Nodes.md`. Doc14 (Case_01) is Phase 2 Obligation Derivation — no tracks; Doc25 has none. Doc23's actual values are **not** the clean triad: `TECH`(22) + `TECHNOLOGY`(12), `PROC`(34) + `PROCESS`(6), `CAPABILITY_SUBREQ`(6), `ROLE`(18). The spirit of the claim survives (a TECH/PROCESS/CAPABILITY-family track vocabulary does pre-exist in Phase 3), but a normative instrument must cite evidence accurately — Amendment A6. Note the future lane campaign will also have to reconcile Doc23's abbreviations and extra tracks.

---

## 6. Independent classification dry-run (§B)

Method: rubric §3 tree walked in order per rule, using ONLY each card's Description/Scope/Verification Criteria/Method. Secondary assigned only where the card genuinely requires both. Borderline flags: **H** = hard (a second reader could reasonably land elsewhere), **s** = soft (resolved with modest judgment).

### PARTE I — Obligation Controls (30 CR)

| # | Rule | Title (abridged) | Primary | Secondary | Justification (card-anchored) | Flag |
|---|---|---|---|---|---|---|
| 1 | CR-D-01.1-001 | Data at Rest Encryption | TECHNOLOGY | — | Criteria are configuration/material reports + periodic review; automated-path satisfiable; storage state is the assurance (L123-131) | |
| 2 | CR-D-01.2-001 | Data in Transit Encryption | TECHNOLOGY | — | Channel config reports + annual review; TLS state satisfies criteria (L199-207) | |
| 3 | CR-D-01.3-001 | Cryptographic Key Management | PROCESS | TECHNOLOGY | "Documented lifecycle covering generation, rotation, revocation, destruction" (L264) — realization is executing lifecycle events with triggers/outcomes; criteria only inspect documents | **H** (T/P) |
| 4 | CR-D-01.4-001 | Data Integrity Mechanisms | TECHNOLOGY | — | Integrity controls active + periodic integrity test = re-verification of built state (L353-361) | |
| 5 | CR-D-02.1-001 | Vulnerability-Free Release | TECHNOLOGY | — | CI gate blocks CRITICAL; automated path satisfies all 3 criteria; exception approval is exception-path (L445-453) | s |
| 6 | CR-D-02.2-001 | Automated Security Updates and Patch Remediation | PROCESS | TECHNOLOGY | Card mandates recurring human review (L517-518); Q1 NO; severity-SLA sequence with triggers/outcomes | |
| 7 | CR-D-02.3-001 | Coordinated Vulnerability Disclosure | PROCESS | — | Triage register, acknowledgement within 5 days, escalation to 24h ENISA/CSIRT submission — per-report workflow (L628-634) | |
| 8 | CR-D-03.1-001 | Authentication and Access Control | TECHNOLOGY | — | IdP config + negative tests; quarterly orphan review = re-verification of state, not state-changing judgement (L722-730) | s |
| 9 | CR-D-03.2-001 | Administrative MFA | TECHNOLOGY | — | Automated test rejects missing second factor (L817); enrolment is a state; quarterly log review = re-verification; exception approval only in Description | |
| 10 | CR-D-03.3-001 | Authorisation and Least Privilege | TECHNOLOGY | — | RBAC enforcement + negative tests; quarterly review removes stale grants (correction/exception-fixing) (L911-919) | s |
| 11 | CR-D-03.4-001 | Secure System Defaults | TECHNOLOGY | — | Deny-by-default config, config tests, opaque errors (L1004-1012) | |
| 12 | CR-D-04.1-001 | Exploit Severity Limitation and Fail-Safe | PROCESS | — | Findings need named owner, triage record, containment decision (L1103) — recurring triage/containment; Q1 NO, Q2 YES | |
| 13 | CR-D-04.2-001 | Availability Restoration and DoS Resilience | PROCESS | TECHNOLOGY | Containment playbook + defined authority + drills made constitutive ("rather than an unverified availability statement", L1165) | s |
| 14 | CR-D-04.3-001 | Dual Regulatory Incident Notification | PROCESS | — | Notification workflow: trigger tree, 24h clock, submissions, tabletop (L1266-1291) | |
| 15 | CR-D-04.4-001 | Data Restoration and Recovery | PROCESS | TECHNOLOGY | Realization is the executed recovery sequence (runbook, restore exercise, failed-restore escalation, L1356-1364); DEMONSTRATE method | **H** (T/P) |
| 16 | CR-D-05.1-001 | Data Minimisation | TECHNOLOGY | — | Schema constraints, API allow-lists, redaction tests (L1474-1482); new-field review is a gate check | s |
| 17 | CR-D-05.2-001 | Storage Limitation and Retention | TECHNOLOGY | PROCESS | Lifecycle rules/TTL jobs satisfy criteria; schedule is standing artefact; exception approval exception-path (L1567-1575) | s |
| 18 | CR-D-05.3-001 | Complete and Secure Data Erasure | PROCESS | TECHNOLOGY | 7-day SLA clock, identity verification, request register — per-request workflow; cascade automation secondary (L1642-1665) | s |
| 19 | CR-D-05.4-001 | Structured Data Portability | TECHNOLOGY | — | Automated export pipeline; 48h objective delivered by automation; criteria are tests (L1750-1758) | s |
| 20 | CR-D-06.1-001 | Processor Due Diligence | PROCESS | — | Assessment activity with trigger (new processor/change) and outcome (dossier, approval before transfer, L1843-1851); success = executing the procedure | **H** (P/C) |
| 21 | CR-D-06.2-001 | Software Bill of Materials | TECHNOLOGY | — | SBOM generation/validation/archival in CI; fully automated path (L1936-1944) | |
| 22 | CR-D-06.3-001 | Contractual Processor Security | PROCESS | — | DPA execution, reconciliation, escalation-on-conflict before production use (L2030-2038); "run the procedure again" | **H** (P/C) |
| 23 | CR-D-07.1-001 | Security and Privacy by Design | PROCESS | — | Per-feature sequence: design checks before merge → release evidence (L2125-2133); procedure re-run per trigger | **H** (P/C) |
| 24 | CR-D-08.1-001 | Annual Security Awareness | CAPABILITY | — | Standing workforce awareness owned by CTO+HR+DPO with review-after-incidents cadence (L2201-2226); annual course is the refresh, not the assurance | **H** (P/C) |
| 25 | CR-D-08.2-001 | Role-Specific Security Competence | CAPABILITY | — | Competency matrix, per-role competence, quarterly review of duties/risks (L2294-2321); INSPECT of standing ability | |
| 26 | CR-D-09.1-001 | Security Governance and Technical Documentation | CAPABILITY | — | Policy architecture with owners/approvals/review reconciled to operating evidence (L2379-2415); governance authority | |
| 27 | CR-D-09.2-001 | Unified Privacy and Cybersecurity Risk Assessment | CAPABILITY | PROCESS | Human risk-acceptance authority (L2486) + trigger screen + refresh cadence = standing ability; assessment sequence secondary | |
| 28 | CR-D-09.4-001 | Processing and Breach Records | PROCESS | — | Update-on-processing-change sequence + breach decision per incident (L2595-2601); success = executing updates | **H** (P/C) |
| 29 | CR-D-10.2-001 | Audit Logging and Traceability | TECHNOLOGY | — | Trail, Object Lock, retention config; retrieval test (L2688-2696) | |
| 30 | CR-D-10.3-001 | Control Effectiveness Testing | PROCESS | — | Recurring test cycle: checklist → findings → retest → sign-off (L2763-2787); success = executing the cycle | **H** (P/C) |

### PARTE II — Best-Practice Controls (16 BPR)

| # | Rule | Title (abridged) | Primary | Secondary | Justification (card-anchored) | Flag |
|---|---|---|---|---|---|---|
| 31 | BPR-D-01.1-001 | Strong symmetric encryption at rest | TECHNOLOGY | — | IaC settings, negative test, annual review record (L2875-2883) | |
| 32 | BPR-D-01.2-001 | Current transport crypto standard | TECHNOLOGY | — | Endpoint scans, cert validation; exceptions have owner+review (L2963-2971) | |
| 33 | BPR-D-02.1-001 | Quarterly Vulnerability Scans | PROCESS | — | The rule IS the recurring run + reconciliation + finding disposition (L3026-3060) | |
| 34 | BPR-D-02.2-001 | Apply Critical Patches Within 72 Hours | PROCESS | — | 72h clock with escalation to CTO; applicability→deploy→validate→closure sequence (L3126-3151) | |
| 35 | BPR-D-03.1-001 | Implement RBAC | TECHNOLOGY | — | Server-side enforcement + matrix + quarterly review (L3233-3241); mirrors CR-D-03.3 | s |
| 36 | BPR-D-03.2-001 | Enable FIDO2 for MFA | TECHNOLOGY | — | Enrolment state + auth/recovery tests (L3324-3332) | |
| 37 | BPR-D-03.4-001 | Harden Systems Using CIS Baselines | TECHNOLOGY | — | IaC baseline + drift scan; failed checks → remediation or exception (L3415-3423) | s |
| 38 | BPR-D-04.3-001 | Maintain an Incident Response Playbook | CAPABILITY | — | Q2 NO — realization is a standing maintained artefact (approved, offline-accessible, updated after triggers, L3506-3514); readiness/authority sustained between events | **H** (P/C) |
| 39 | BPR-D-04.3-002 | Conduct Tabletop Exercises Quarterly | PROCESS | — | Realization = running the exercise with records and corrective actions (L3599-3607) | |
| 40 | BPR-D-05.3-001 | Media Sanitisation (Clear/Purge/Destroy) | PROCESS | — | Per-decommissioning procedure: classify → decide → verify → retain evidence (L3691-3699) | |
| 41 | BPR-D-07.1-001 | Follow NIST SSDF Secure Development | PROCESS | — | Practice map realized through the per-feature SDLC; map review-on-change (L3783-3791) | **H** (P/C) |
| 42 | BPR-D-07.2-001 | Conduct SAST and DAST in CI/CD | TECHNOLOGY | — | Fully automated per-PR/release gates; FP triage is exception-path (L3874-3882); contrast with quarterly BPR-D-02.1-001 | s |
| 43 | BPR-D-09.1-001 | Establish an ISMS per ISO 27001 | CAPABILITY | — | Management cycle: scope, registers, internal audit, corrective action, management decisions (L3966-3974) | |
| 44 | BPR-D-10.2-001 | Retain Logs ≥12 Months | TECHNOLOGY | — | Lifecycle config, archive protection, retrieval tests (L4057-4065) | |
| 45 | BPR-D-10.3-001 | Conduct Annual Penetration Testing | PROCESS | — | Recurring assessment: scope → test → findings → owner → retest (L4148-4156) | |
| 46 | BPR-D-10.3-002 | Use OWASP Testing Guide | PROCESS | — | Assessment methodology execution: matrix, coverage, exclusions with rationale (L4239-4247) | |

### Distribution (independent baseline)

| Class | CR | BPR | Total |
|---|---:|---:|---:|
| TECHNOLOGY | 13 | 7 | **20** (43.5%) |
| PROCESS | 13 | 7 | **20** (43.5%) |
| CAPABILITY | 4 | 2 | **6** (13.0%) |
| **Total** | **30** | **16** | **46** |

- Recount vs expectation: **46 confirmed** (30 CR + 16 BPR; matches Doc18 frontmatter `expected_total_controls: 46`, §2 tables, and the xlsx row count).
- **Undecidable (§3 step-4 STOP): none** — 46/46 resolved by the tree.
- Hard borderlines (a second reader could reasonably differ): 8 — CR-D-01.3-001, CR-D-04.4-001, CR-D-06.1-001, CR-D-08.1-001, CR-D-09.4-001, CR-D-10.3-001, BPR-D-04.3-001, BPR-D-07.1-001.
- Soft borderlines: 8 — CR-D-02.1-001, CR-D-03.1-001, CR-D-03.3-001, CR-D-04.2-001, CR-D-05.2-001, CR-D-05.4-001, BPR-D-03.1-001, BPR-D-03.4-001, BPR-D-07.2-001 (9 listed as `s`; CR-D-05.3-001/CR-D-04.2-001 secondary choices also judgment calls).
- Exemplar agreement: 9/9 primary classes match rubric §8; 1 optional-secondary difference (CR-D-05.3-001).

---

## 7. Verdict and proposed amendments

**Verdict: `APPROVED_WITH_AMENDMENTS`.** The rubric is fit for purpose as the normative classifier: closed enum, terminating tree, 0 STOPs across the full corpus, 9/9 exemplar reproduction, correct Phase 1 anchor, faithful examples. The defects below are precision and reliability items, not conceptual failures. A1-A3, A6 should be applied before the tagging campaign starts; A4, A5, A7, A8 at the next rubric revision.

| # | Amendment | Where | Rationale |
|---|---|---|---|
| **A1** | Replace "catalog index/summary table" with the concrete anchor: one `realization_class` / `realization_class_secondary` column in **Anexo A** (per-control index) + one field per card; state that the tagging campaign must bump Doc18 frontmatter `fields_per_card`/`expected_fields_per_card` (24→25 or amend the §3 schema table) and repair the duplicated "field 14" numbering (92 occurrences, 0 fields numbered 13) it will trip over. | §4, rubric L84 | Doc18's §2 table has no per-control column; field-count invariants exist and would fail |
| **A2** | Add a precondition note: `12_Rules_Catalog.xlsx` (`Rules_Catalog` sheet, 17 legacy columns, Sprint-4 stubs, stale NI values) is currently **out of sync** with Doc18 v4.0; either regenerate it before column sync or mark it derived-but-frozen and exclude it from the "kept in sync" invariant. | §4, rubric L80/L89 | "Kept in sync" is unverifiable against a stale mirror |
| **A3** | Operationalize the T-disqualifier (promote to a numbered step or keep as tie-break): a recurring step is **constitutive** (Q1 = NO) only if its outcome *changes what the control accepts or permits* (exception approval, risk acceptance, containment/transfer authorization) — test: the step appears in the card's **Verification Criteria**, not only in the Description's exception clause; steps that only re-check built state (reviews, sign-offs on findings) are periodic re-verification (Q1 = YES). | §2/§3, rubric L31/L67 | Resolves the "CTO sign-off on quarterly review" class of ambiguity; mechanically separates CR-D-02.2-001 (criterion contains "approved exception") from CR-D-03.2-001 |
| **A4** | Strengthen the P/C tie-break with structural indicators, empirically grounded in Doc18: CAPABILITY indicators — named owner of the ability, competence/curriculum maintenance, authority to accept risk or approve policy, review-of-people-or-authority cadence; PROCESS indicators — SLA/clock ("within 24h/72h/7 days"), notification, escalation, per-trigger sequence execution. Add an explicit note that workforce-competence rules (CR-D-08.1-001, CR-D-08.2-001) are CAPABILITY even when evidenced by completion records — without it, 08.1 vs 08.2 is unstable. | §3, rubric L68 | 8/46 hard borderlines were all P/C; the 08.1/08.2 twin-card case demonstrates rater drift |
| **A5** | Extend the §2 TECHNOLOGY definition to "system, hardware, software, **or physical artefact measure**" so §2 matches §7's folding of physical controls. | §2, rubric L31 vs L124 | Internal consistency |
| **A6** | Correct the preamble evidence claim (rubric L14): the triad is pre-figured **only** in `Case_01/03_PHASE3_DECOMPOSITION_RICH/Doc23_Architectural_Nodes.md`, whose actual track values are `TECH`(22)/`TECHNOLOGY`(12)/`PROC`(34)/`PROCESS`(6)/`CAPABILITY_SUBREQ`(6)/`ROLE`(18) — not "Doc14/23/25 across cases". Add: the future lane campaign must reconcile Doc23's abbreviations and out-of-enum tracks. | Preamble + §5 | Normative instrument must cite evidence accurately; corpus-wide `track=` grep returns exactly one file |
| **A7** | Prefix the §6 dashboard path with `00_METHODOLOGY/` (currently resolves only from inside `00_VISUALISATIONS/`). Optionally cite exact lines: `capability` L1644, `CITES_OUTCOME` L1709. | §6, rubric L112 | Trivial precision; anchor otherwise verified correct |
| **A8** | Add 1-2 further borderline exemplars from the dry-run's hard list (recommended: CR-D-01.3-001 for the T/P lifecycle seam; CR-D-06.1-001 or BPR-D-04.3-001 for the P/C seam) at the next revision. | §8 | Reduce rater drift on the two seams identified in §A.1 |

**Agreement-rate computation (for the Orchestrator):** use §6's table as the Validator baseline. Executor tagging does not yet exist; the only Executor positions on record are the 9 §8 exemplars, with which this baseline agrees 9/9 on primary class.

---

## 8. Files referenced (evidence paths)

- Rubric: `00_METHODOLOGY/REALIZATION_CLASS_RUBRIC.md` (all line refs per v1.0)
- `02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/Doc18_Rules_Catalog.md` (rule cards; line refs in tables above)
- `02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/12_Rules_Catalog.xlsx` (openpyxl: 20 sheets; `Rules_Catalog` 46 rows, header row 5, 17 legacy cols)
- `02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/control_set.yaml` (per-control entries, 46)
- `02_CASES/Case_01_TinyTask_SaaS/02_PHASE2_RULES_RICH/phase2_ontology.yaml` (enums L174-180; ComplianceRule L104; BestPracticeRule L128)
- `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` (maturity_model L1635-1735)
- `00_METHODOLOGY/IMPLEMENTATION_POSTURE_MODEL_CSF_STRICT.md` (v2.0, supersedes maturity model v1.0)
- `00_METHODOLOGY/00_VISUALISATIONS/Case_01/Case_01_P1_Dashboard.html` (Folio VIII)
- `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/Doc23_Architectural_Nodes.md` (sole `track=` user; 6 enum variants)

*Validator, 2026-09-05. No files outside this report were modified.*
