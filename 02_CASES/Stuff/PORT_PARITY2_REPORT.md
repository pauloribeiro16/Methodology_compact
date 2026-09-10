# PORT-PARITY-2 — Campaign Report

**Executed:** 2026-09-04 (single-session, orchestrator + 3 verified Executor subagents)
**Scope:** full structural + content propagation of Case_01 waves to Case_02/Case_03 (Phases 1–3, dashboards, scripts, gates)
**Result:** ✅ COMPLETE — 16 commits, all 5 case gates PASS, smoke 16/16, P3 verify_rich honest FAILs queued for human review

---

## 1. What was propagated

| Block | Case_02 | Case_03 |
|---|---|---|
| Baseline (uncommitted Sprint 10/11 work gated + committed) | ✅ 49aa5e4 (link count 505→1205 corrected) | n/a |
| F1 source fixes (Case_01: Folio IV "Maturity EV", NEW-08 v1.6, prose) | ✅ inherits (2f29a7d) | ✅ inherits |
| corr-013 P2 renumber | **not needed** (already Doc14–Doc20) | ✅ Doc16–21 → Doc15–20, 206 refs (6e29834) |
| P1 v1.6 data layer (ontology maturity_model, graph, builder, validator v2.4) | ✅ (was already at parity) | ✅ 749n/2054l/9 audits, 119 EvidenceItems (75bd626) |
| P1 dashboards Folios I–VIII + standalone Maturity | ✅ (parity, 2026-08-31) | ✅ + build_case03_dashboard.py (549d1de) |
| P2 wave (phase2_ontology, build_p2_*, graph, dashboard, control_set at root) | ✅ 278n/356l (468c500) | ✅ 242n/340l (491cf74) |
| P3 rich layer v0 (scripts, 4 narrative docs GENERATED + banner, RICH_LINT, functional tree, TRACEABILITY_AUDIT for C2) | ✅ (e73dfed) | ✅ (637ccc5) |
| Bookkeeping (progress.json, case PS, CHANGE_LOG 6.8, GLOBAL 6.8) | ✅ | ✅ |

**Known deviations (locked with user before execution):** AI-RMF = anchors without radar (all cases); EvidenceItems mechanical + audit flags; P3 docs GENERATED v0 with "pending human review" banner; corr-013 executed; fix-at-source first.

## 2. Verification performed (orchestrator, independent of subagents)

- All 5 gates re-run after every block: `check_unmapped` ×3 + `check_implementation_posture` ×2 — **ALL PASS**.
- Smoke suite full run: **16/16 dashboards** (14 prior + Case_03 P1 ×2, then +P2 ×2).
- Graph JSON deep-checks: 0 dangling links, 0 forbidden maturity scalars on sub-domains, 38/38 active sub-domains with evidence (C3), invariants = counts.
- Screenshots read back as images (force graph, Folio VIII radars CSF+PF on P1+P2, identity strings).
- Diff-scope audit after each subagent: only the allowed paths touched.

## 3. 🔴 Human review queue (P7) — decide these

1. **Case_03 orphan obligations (AUD-P2-005b): 10 obligations unreachable via the AG chain** (root cause AUD-P2-007: 26 `related_goals` AG ids with no Doc17 row). Fix = content edit in Doc17/Doc15 — needs your adjudication (add rows vs. accept gap).
2. **Case_02 objective-coverage orphans: 14 PO / 40 SO without objective link** (audited, not fixed). Catalog-level rule coverage is 63/63.
3. **verify_rich FAILs (honest, not suppressed):**
   - C2: 25/84 FRs carry Source Rule "—"; only 10/63 rules traced at requirement level; stale "53 rules" claims; duplicated FR-71/72 rows.
   - C3: Doc31 claims 56 NFRs but defines 12 cards (**suspected truncation** — check git history of Doc31); 5 FRs cite raw articles instead of rule ids; Doc26 stale "63 rules" vs frozen 78; BPR-D-12.1-001 unallocated; dangling UC-99.
4. **D-07.2 (Case_03) coverage**: no clause anchor → Coverage EvidenceItem withheld + CVG-C03-001 audit. Decide: clause anchor vs. Sub-SO-only coverage.
5. **F3a minor adjudications accepted by orchestrator** (veto if wrong): T-005 no HAS_TENSION_WITH edge (single-clause tension); capability `observed=false` everywhere (Doc13 §4 = PARTIAL; consistent with port Fase 4 backfill); 3 id-style warnings (STK-/ROLE-/ThirdParty hyphen styles — same family Case_02 already warns).
6. **Phantom refs left untouched** (pre-existing, not made worse): C3 `Doc20_NIST_Framework_Inputs` (2 hits — doc doesn't exist in C3); C1 Doc05 legacy basename refs already fixed this campaign.
7. **corr-013b (registered debt):** C3 P3 renumber Doc22–31 → Doc21–30 — recommend it rides the future P3 RICH campaign, not overnight work.
8. **Naming parity (optional):** C2 Doc16 is `Privacy_Security_Goals` vs C1/C3 `Objectives`. Renaming is a corr-010-class change — deferred.

## 4. Registered debt / nits (non-blocking)

- C3 `phase1_ontology.compact.json` has `schema_version: null` (content complete; validator passes — cosmetic).
- C3 P2 after corr-013 ends at Doc20 while P3 starts at Doc22 (Doc21 gap) — accepted cosmetic until corr-013b.
- Historical reports (PORT_census_v0, VALIDATOR_UNMAPPED_AUDIT_v0, SPRINT*) intentionally keep old doc numbers — point-in-time records.
- KG E3 `graph.json` predates all renames — rebuild is a main-repo activity (per protocol).
- Gate waiver lists were extended with provenance tokens (`model_csf_strict`, `maturity_cur/tgt`, `maturity redesign`, `P1_Maturity.html`) — the /maturi/ ban now correctly allows rule-defining and provenance text; strictness otherwise unchanged.

## 5. Commit index

| Commit | Block |
|---|---|
| 49aa5e4 | F0 Case_02 P1 parity baseline |
| 7be0b3b | F0 Case_01 P2 wave baseline |
| 5888cf7 / 3eddf3c / de6928e | F0 dream / harness / UNIFIED |
| 2f29a7d | F1 source fixes Case_01+02 |
| 6e29834 / bf811e2 | F2 corr-013 C3 / gate waiver harmonisation |
| 75bd626 | F3a C3 P1 data layer |
| 549d1de | F3b C3 P1 dashboards |
| 468c500 / 491cf74 | F4 P2 wave C2 / C3 |
| e73dfed / 637ccc5 | F5 P3 rich v0 C2 / C3 |
| (this commit) | F6 bookkeeping + report |

---

## TEMPLATE CONVERSION 2026-09-04

**Follow-up campaign (Executor, single session).** Converted the two product-UC pilot
sections from compact Cockburn cards to the **Bike4All RUP-style fully-dressed template**
(`Methodology-main/03_REFERENCE_MATERIAL/P3_E2_Requirement_Analysis_Bike4All_Maintenance_platform_v1r2.md`),
adjusted to AEGIS: per-UC section 10 = **Security & Compliance Annex (AEGIS)** (provenance,
constrained-by, rules/NFR, threats, NIST anchors — carried over verbatim), MUC linkage
preserved. Format upgrade + enrichment only; **no UC/rule/MUC/NIST ID changed or dropped**
(31 checked IDs in Doc21, 26 in Doc22 — all present).

**Files (only these two edited; no commit):**
- `Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md` — §6 intro + §6.1 PKG-8: 7 UCs (`U.C.8.1.1`…`U.C.8.4.1`) rewritten as `#### Use-Case: {…}` blocks; PKG-9..12 pending note updated ("will be written in this template").
- `Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/Doc22_Use_Cases_Catalog.md` — §6B intro + §6B.1 PKG-C: 6 UCs (UC-63…UC-68); MUC-C3-01/04/05 cards left verbatim; pending note updated.

**Per-UC structure:** `##### 1 Brief Description` … `##### 10 Security & Compliance Annex (AEGIS)`, with `######` subsections; Mermaid `sequenceDiagram` (4–8 lines, participants = actor/SYS ids) placed right after §4 in every UC.

**Enrichments added (derived from existing card facts + attested Doc03/Doc04 only; no new compliance claims):**
- **Subflows (24 headings; 21 distinct reusable fragments + 3 explicit cross-references):** C2 — chip authentication BAC/PACE+PA, security-event raise, biometric template purge, guided re-capture, presentation-attack challenge, decision-log write, offline store-and-forward, officer console session, consent token capture. C3 — bureau consent capture, fraud screening, decision-context record write, reason-code generation, explanation package dispatch, override justification logging, fail-closed context validation, KYC vault filing, step-up signing, stale-data guard, early-repayment settlement.
- **Key Scenarios (26):** success + main failure outcome per UC.
- **FURPS+ (13 UCs × 5 labels):** anchors from attested facts (≤2 s match → P; WORM/immutable decision log + audit trail → R; in-kiosk purge/consent-gating → F; plain-language UI/guided capture → U; model-version pinning/governed thresholds → S). Slots with no attested fact filled honestly with "N/A".
- **Alternative Flows (35):** every card extension became a named `#### 5.n <Alternate flow: …>`.
- Intro notes (v1.3/v2.1) extended with template-adoption sentence.

**Known cosmetic drift (registered):** MUC cards keep old extension labels ("UC-64 ext. 1a", "UC-66 ext. 1a") which now map to §5.3 / §5.1 of the converted UCs — MUC cards were out of scope by instruction.

**Gates (all unchanged from baseline):**
```
C2 check_unmapped → GATE PASS (Case_02 v0.3)
C3 check_unmapped → GATE PASS (Case_03 v0.3)
C2 verify_rich → summary: 8 checks, 2 FAIL, 6 PASS   (FAILs pre-existing: CHK-1 frontmatter, CHK-2 FR census)
C3 verify_rich → summary: 8 checks, 3 FAIL, 5 PASS   (FAILs pre-existing: CHK-1, CHK-3 NFR census, CHK-6 cross-refs)
```

**Sanity (python):** Doc21 UC blocks = 7/7, Doc22 = 6/6; all 13 UC blocks have 10/10 numbered sections + exactly 1 mermaid; sequenceDiagram total = 13 (Doc21 keeps its pre-existing §5.1 useCaseDiagram); `git diff` hunks confined to the §6 / §6B ranges (old lines 215–400 and 998–1196).

## TEMPLATE CONVERSION — CASE_01 (2026-09-04)

**Scope:** `Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/Doc20_Use_Cases_Catalog.md` §2 only — the 23 functional product UCs (U.C.7.1.1…U.C.11.3.1; PKG-7: 5, PKG-8: 6, PKG-9: 5, PKG-10: 4, PKG-11: 3) converted from compact Cockburn cards to the Bike4All RUP-style 10-section template (same reference + AEGIS adjustments as C2/C3: §10 Security & Compliance Annex, [ATTESTED]/[ASSUMED] provenance bullet, MUC linkage). §1 Actors, §3 (U.C.1-6, locked), §4 MUCs, §5–§8, frontmatter: untouched. Package summary tables kept as-is. §2 intro gained the template-adoption sentence. No commit made.

**Per-UC structure:** `#### Use-Case: {U.C.x.y.z} …` with `##### 1`…`##### 10`; mermaid `sequenceDiagram` (4–8 lines, participants = actor/SYS ids) directly after §4 in all 23 UCs.

**Enrichments (derived from the cards + attested Doc03/Doc04 facts only; no new compliance claims):**
- **Alternative Flows (50):** every card extension bullet (2a/3a/…, incl. inline Extensions lines) became one named `###### 5.n <Alternate flow: …>` — 1:1, verified per-UC.
- **Subflows (32):** reusable fragments extracted from existing flow facts (account provisioning, consent capture, SSO/OIDC dance, session invalidation sweep, reset-token lifecycle, pending-membership lifecycle, task field validation, tenant-scoped persistence, board query, comment sanitisation, mention parsing, notification delivery, upload validation + AV scan, signed-webhook intake, admin action application, IdP metadata onboarding, archive assembly, signed-URL delivery, grace-period handling, cryptographic erasure, …).
- **Key Scenarios (46):** success + main failure per UC.
- **Post-condition blocks (46):** card Postconditions split into `###### 8.n` statements (content verbatim per clause).
- **FURPS+ (23 UCs × 5 labels = 115 slots):** 80 filled from attested facts only (NFR-01/02, 30-min idle timeout, 5-failure lockout, 1-hour reset token, 7-day purge, 25 MB + MIME allowlist, ClamAV quarantine, ≤5 min digest, 24h URL, 100 MB async, 30-day grace, ≤200-char title, ≤10 000 chars, last-writer-wins, no-PAN, workspace_id scoping…); 35 slots honestly **N/A** (P: 19, U: 12, R: 4; F/S: 0).

**Preservation (python diff vs git HEAD §2):** Main Success Scenario steps 83/83 verbatim; precondition fragments and postcondition clauses all present; annex bullet lines 0 missing (Provenance 23/23 verbatim, Constrained by 23/23, Rules/NFR 23/23, NIST anchors 23/23, Threats 18/23 — 5 cards never had one); CR-/PO-/FR-/NFR-/MUC ID sets equal; whole-file U.C. ID set (59 unique) unchanged; [ATTESTED]/[ASSUMED] counts preserved (+1 each from the new intro sentence quoting the convention).

**Gates:**
```
check_unmapped (Case_01) → GATE PASS (v0.3 real: UNMAPPED, Posture, Frontmatter, Control Set YAML verified)  [baseline and after]
Sanity: 23 UC blocks × 10/10 numbered sections (in order) · 23 mermaid sequenceDiagrams · 0 ##### orphans outside §2 · fences balanced · mermaid structural check clean (0 issues)
git diff: Doc20 = +2162/−283 — only file touched by this session (Doc21/Doc22/report hunks belong to the parallel C2/C3 conversion session)
```

**Notes:** zero "maturi" tokens; U.C.10.2.1 MSS keeps the card's original step numbering (1,2,4,5,6) verbatim; package header "U.C.10.3.2 … Enterprise SSO [ASSUMED]" table title unchanged (card heading "Enterprise SSO").
