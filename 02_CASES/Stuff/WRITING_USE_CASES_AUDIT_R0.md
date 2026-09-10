---
document_id: AEGIS-AUDIT-WRITING-USE-CASES-R0
title: writing-use-cases skill audit R0 — Case_01/02/03
phase: 3
version: 1.0
created: 2026-09-09
updated: 2026-09-09
author: Executor
status: GENERATED
case: All cases
---

# writing-use-cases skill audit R0 — Case_01/02/03

Read-only audit. Authoritative source: `skills/writing-use-cases/SKILL.md`
(delivered 2026-09-09, commit b3cf204 — Cockburn + RMAC + AEGIS Bike4All
RUP 10-section + §10 Security & Compliance Annex + rubric §5B/§5C).

**Bottom line.** No prior campaign audited the **card-content quality
dimension** (anti-pattern catalogue, §10 schema per card, RUP 10-section
completeness, actor-intention MSS, primary-actor discipline). Those are the
concerns of the `writing-use-cases` skill, and this R0 catalogues the gaps
across **Case_01, Case_02, Case_03**. Severity uses P0–P3 (P0 = card missing
required section; P1 = required field missing in a populated card;
P2 = anti-pattern affecting naming or diagram; P3 = cosmetic / stale).
**No edits were made** — see §6 priority queue.

---

## §1 Scope and prior-campaign coverage

### §1.1 Artefacts audited (read-only)

| Case | Catalogue | Relationships | Variability | Annex A | Annex B | Lane cards |
|---|---|---|---|---|---|---|
| Case_01 | `02_CASES/Case_01_TinyTask_SaaS/03_PHASE3_DECOMPOSITION_RICH/Doc20_Use_Cases_Catalog.md` (3109 L) | `Doc21_Use_Case_Relationships.md` (210 L) | `Doc22_Use_Case_Variability.md` (105 L) | `annexes/A_Use_Case_Diagrams.md` (392 L, 22 PlantUML blocks, 11 SVGs) | `annexes/B_Sequence_Diagrams.md` (304 L, 23 sequenceDiagrams) | `Doc32_Process_Capability_Cards.md` (556 L) |
| Case_02 | `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md` (3206 L) | `Doc22_Use_Case_Relationships.md` (186 L) | `Doc23_Use_Case_Variability.md` (96 L) | `annexes/A_Use_Case_Diagrams.md` (364 L, 6 PlantUML blocks, 7 SVGs) | `annexes/B_Sequence_Diagrams.md` (271 L, 19 sequenceDiagrams) | `Doc31_Process_Capability_Cards.md` (1275 L) |
| Case_03 | `02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/Doc22_Use_Cases_Catalog.md` (4209 L) | `Doc23_Use_Case_Relationships.md` (562 L) | `Doc24_Use_Case_Variability.md` (402 L) | `annexes/A_Use_Case_Diagrams.md` (354 L, 8 PlantUML blocks, 8 SVGs) | `annexes/B_Sequence_Diagrams.md` (531 L, 33 sequenceDiagrams) | `Doc32_Process_Capability_Cards.md` (1480 L) |

### §1.2 Prior campaigns that already covered Phase 3 (do NOT re-flag)

| Campaign | Closed concerns |
|---|---|
| UC SEPARATION (5 commits, 2026-09-05) | Catalogues lane-pure (UCs only in Doc20/21/22); PROC/CAP in Doc31/32; 6 borderline titles → P7. |
| RENUMBER (5 commits, 2026-09-05) | Flat `UC-NN` numbering per case (C1 01..40, C2 01..36, C3 01..33); `U.C.X.Y.Z` extinct in active ids. |
| LANE CARDS / REALIZATION CLASS | 102/102 PROC/CAP cards with §5C schemas and §5C.4 flowcharts; UC/CAP/PROC classification rule. |
| UML DIAGRAMS (MERMAID_RENDER_FIX) | `useCaseDiagram` → PlantUML + committed SVG (26 files in `annexes/svg/`); gotchas `;`, `OFF`, `OFFR` codified in rubric v1.9; 77 sequenceDiagrams render-validated. |
| ALT-ANCHOR | UNMAPPED_* retired; 5 frozen referentials (800-53r5, SSDF, ASVS, SAMM, CSF 2.0) + 800-53r5 column generator; 3 gates v0.4 PASS. |

### §1.3 Genuine delta — what this R0 surfaces

1. **§10 Security & Compliance Annex completeness** card-by-card (Provenance tag + Constrained by + Rules/NFR + Threats + NIST anchors) — never validated per card.
2. **Anti-pattern catalogue sweep** (10 violations from `references/03-anti-patterns-and-diagrams.md §A`) — never applied to existing titles.
3. **Bike4All RUP 10-section template compliance per card** — prior audits checked *existence* of catalogues, not §1–§10 per card.
4. **Granularity sea-level audit** — intra-UC Cockburn levels not enforced; classification rule covered UC-vs-PROC-vs-CAP but not intra-UC.
5. **Primary-actor discipline** — exactly one Primary actor by role; non-human actors with stereotypes per RMAC p1 slides 30–31.
6. **`<<include>>` / `<<extend>>` semantic correctness** — relationships docs last audited at id level (RENUMBER), not at semantics.
7. **MSS actor-intention discipline** — no UI contamination ("Click Submit" etc.) on §4 Basic Flow — no precedent in any prior campaign.

---

## §2 Methodology

### §2.1 Skill under audit

Eight hard rules from `skills/writing-use-cases/SKILL.md`:

1. Sea level by default (Cockburn summary/user-goal/subfunction levels).
2. Title is active-verb goal phrase (reject noun-verb-noun, gerunds, CRUD primitives).
3. One primary actor by role; non-human actors carry stereotypes (`«worker»`, `«internal worker»`, `«case worker»`, `«entity»`).
4. `«include»` for mandatory shared; `«extend»` only when base stands alone.
5. AEGIS Bike4All RUP 10-section template (canonical upstream); §10 **non-negotiable**.
6. MSS steps are actor intentions, not UI actions.
7. Use case diagrams = PlantUML + committed SVG (annex A); sequence diagrams = Mermaid (annex B); UC ovals only; gotchas `;` and `OFF`.
8. Process before diagram (RMAC p1 slides 16–37).

Ten anti-patterns from `references/03-anti-patterns-and-diagrams.md §A`:
A1 CRUD-as-UC; A2 Function Decomposition; A3 Missing Primary Actor;
A4 Wrong Granularity; A5 Bad Naming; A6 UI Contamination;
A7 `<<extend»` Overuse; A8 Diagram-Only UC; A9 Driving Design Literally;
A10 NFRs in MSS.

§10 schema (`references/02-card-template.md §C`): Provenance (`[ATTESTED]`
Source: DocNN §N or `[ASSUMED]`); Constrained by; Rules / NFR;
Threats addressed; NIST anchors.

### §2.2 Severity rubric

- **P0** — card missing a required RUP 10-section (rule #5 fail).
- **P1** — required §10 field missing in a populated card.
- **P2** — anti-pattern visible at naming or diagram level (A1/A2/A3/A5/A7), or Mermaid gotcha (`;`/`OFF`) on rendered annex.
- **P3** — cosmetic / stale (legacy `U.C.X.Y.Z` ref, draft-vs-baseline frontmatter, sequence alias `OFFR` near keyword).

### §2.3 Verification approach

Counts via `grep -c` over the field pattern; per-card identification
via Python split on `^#### Use-Case: ` (heading boundary); Relationships
edges recognised with **French quotes** `«include»` (Unicode U+00AB/U+00BB)
not the ASCII `<<` form that prior reports used. UI-contamination sweep
via per-case regex matching UI verbs (`clicks?`, `types?`, `enters?`,
`taps?`, `fills?`, `selects?`) inside §4 Basic Flow steps. No edits,
no renders, no commits outside `02_CASES/WRITING_USE_CASES_AUDIT_R0.md`.

---

## §3 Per-case findings

### §3.1 Case_01 — TinyTask SaaS (Doc20, STATUS=REWRITTEN_PRODUCT_BASELINE v3.4)

**Structure count.** 23 product UC `#### Use-Case:` blocks (UC-14..UC-36);
13 §3 security/compliance abbreviated cards; §10 headings = 23 (one per
product UC).

| §10 field | Count | Required (per skill) | Status |
|---|---|---|---|
| Provenance | 23 | 23 | OK |
| Constrained by | 23 | 23 | OK |
| Rules / NFR | 23 | 23 | OK |
| Threats addressed | **18** | 23 | **MISSING 5** |
| NIST anchors | 23 | 23 | OK |

**Missing Threats addressed (per-card, computed via Python split):**
UC-17, UC-23, UC-26, UC-29, UC-34.

| ID | Severity | Hard rule / anti-pattern | What | Why it fails | Suggested fix |
|---|---|---|---|---|---|
| C1-FIND-01 | **P1** | rule #5 / §10 schema | UC-17, UC-23, UC-26, UC-29, UC-34 §10 blocks lack `**Threats addressed:**` field. | The §10 schema is non-negotiable; Threats is one of the 5 required fields. | For each, populate with the applicable MUC ids from `Doc20 §4` (MUC-01..08) and re-derive Threats-to-UC mapping from the existing `«threatens»` edges in `Doc21_Use_Case_Relationships.md §4`. |
| C1-FIND-02 | **P2** | A1 CRUD-as-UC | UC-19 *Create Workspace* (line 638), UC-20 *Create Project* (730), UC-21 *Create Task* (818), UC-36 *Delete My Account / Workspace* (2228). | Use case titles are CRUD primitives, not user goals. | Rename to actor-goal form per Cockburn rule #2: e.g. *Stand Up a New Workspace*, *Spin Up a Project*, *Capture a Task*, *Close My Account / Tear Down a Workspace*. Catalog frontmatter counters (`23 product + 17 security`) must update. |
| C1-FIND-03 | **P3** | A6 UI Contamination (mild) | MSS steps at lines 146, 285, 362, 664, 757, 845, 1043, 1064, 1227, 1900 use UI verbs (clicks/enters/selects/types). | Steps describe UI actions, not actor intentions. | Rewrite steps as actor-intention per AEGIS pattern — present in C3 catalogue as model (e.g. C3 uses "Customer selects account type" but the verb itself is goal-level, which is borderline-acceptable for product UC). Decide policy: this R0 flags it but does not enforce — judgment call. |
| C1-FIND-04 | **P3** | cosmetic | 11 legacy `U.C.X.Y.Z` references survive at lines 47, 3040–3057 (version history, lane registry, package index). | All in historical/version-history prose — not active ids. | Optional: append `(formerly U.C.X.Y.Z)` annotation if the user prefers full traceability; or leave as registry residue. Lowest priority. |
| C1-FIND-05 | **P2** | rule #5 (consistency) | §3 security/compliance cards (13 of them, after UC-01..UC-13) are *abbreviated* — no `#### Use-Case:` block, no §1..§9 anatomy, only Annex bullets. | Inconsistent with §2 product cards which carry full RUP anatomy. The skill's rule #5 says §1..§10 should be present in every UC card. | Decide policy: either (a) promote §3 cards to full RUP anatomy; or (b) document an AEGIS exception in the skill — "compliance UC stubs are acceptable when the Use Case is fully expressed by the underlying PROC/CAP lane cards". Option (b) is the lighter edit and matches `feedback-use-cases-product-realism` (UCs should look like product UCs, not compliance checklists). |

### §3.2 Case_02 — SecureBorder Solutions (Doc21, STATUS=DRAFT v1.7)

**Structure count.** 19 product UC `#### Use-Case:` blocks (UC-16..UC-34, all
in §6); 15 compliance UCs (UC-01..UC-15) live as summary-table rows in §7.x
(UC-DP/SEC/IAM/DEV/GOV/AI), indexed by `Doc31_Process_Capability_Cards.md`.
§10 headings = 19 (one per §6 product UC; §7 compliance UCs have **no**
`##### 10 Security & Compliance Annex` — see Findings).

**§10 field counts (product UCs only, the 19 that have blocks):**

| §10 field | Count | Required | Status |
|---|---|---|---|
| Provenance | 19 | 19 | OK |
| Constrained by | 19 | 19 | OK |
| Rules / NFR | 19 | 19 | OK |
| Threats addressed | 19 | 19 | OK |
| NIST anchors | 19 | 19 | OK |

(The earlier count of 24 Provenance shown in §10 totals was inflated by §6
zero-shot radar Annex and §7/§9 reference tables; **C2 §10 fields for
the 19 fully-dressed product UCs are 100% complete.**)

| ID | Severity | Hard rule / anti-pattern | What | Why it fails | Suggested fix |
|---|---|---|---|---|---|
| C2-FIND-01 | **P0** | rule #5 / RUP 10-section | UC-01..UC-15 (15 compliance UCs) in §7.x summary tables **lack `#### Use-Case:` blocks AND lack the §10 Security & Compliance Annex**. They have only compact columns: Use Case Name / Description / Primary Actor / Related Rules / Related Goals / Related PSOs / Priority / Regulation / SLA. | Skill rule #5 says §1..§10 are mandatory per UC. Compliance UCs are legitimate UCs (lane-pure catalog per UC SEPARATION); they need the same anatomy as product UCs. | Promote each compliance UC row to a full `#### Use-Case: {UC-NN}` block: copy compact columns into §1 (Description), §2 (Actors via Primary Actor + implicit stakeholders), §3 (Preconditions inferred from Regulation/SLA columns), §4 (Basic Flow placeholder or link to the Doc31 lane card), §9 (Special Requirements from Priority/SLA), §10 (Provenance from DocNN refs; Constraints from Related UC/PROC; Threats derived from MUC catalogue). Heavy work — likely a dedicated sprint. |
| C2-FIND-02 | **P2** | rule #5 / heading collision | `## 10. UC TO BUSINESS GOALS` at line 2896 (top-level) **collides** with the per-UC `##### 10 Security & Compliance Annex (AEGIS)`. A reader sees two different "§10" sections. | Same as C3-FIND-01 — the heading naming convention reserves §10 for the Security & Compliance Annex. | Rename top-level to `## A. UC TO BUSINESS GOALS` (or renumber all top-level sections §A..§F). Localised edit, low risk. |
| C2-FIND-03 | **P2** | rule #7 / Mermaid alias | `participant OFFR as "SH-EXT-001 (Border Officer)"` appears at 5 lines (95, 119, 134, 145, 158) of `annexes/B_Sequence_Diagrams.md`. | Alias begins with `OFF`; the rubric §5C.5 explicitly notes that `OFF` collides with the `autonumber off` keyword in some Mermaid parsers. `OFFR` itself is fine for stable Mermaid, but the prefix trip-wire is preserved. | Rename alias to `BOFR` or `BORDER_OFFICER` (no `OFF*` prefix) in all 5 occurrences. Localised edit; verify render stays green. |
| C2-FIND-04 | **P3** | cosmetic | 8 legacy `U.C.X.Y.Z` refs at lines 2461–2463, 2634, 3164, 3167–3168, 3196 — all in version history / package index. | Not active ids. | Optional `formerly` annotation or leave as registry residue. |
| C2-FIND-05 | **P3** | documentation hygiene | Doc21 STATUS=DRAFT v1.7. §7.6 notes "NEW Category for SecureBorder" — content stable, body fully dressed but frontmatter says DRAFT. | Stale draft status; the §7 reorganisation by UC SEPARATION was substantive. | Either bump to a v1.8 + BASELINE status, or document why DRAFT is correct (perhaps awaiting a planned v1.9 law-clause sweep). |
| C2-FIND-06 | (INFO) | rule #4 / edges | Relationships doc (Doc22) shows 15 `«include»` + 14 `«extend»` edges. The `«extend»` count is high (14) — within rule #7 limits, but borderline for §3.3 A7 (`<<extend»` overuse). | RMAC p1 slide 43 names three legitimate uses (UCBase / UCExt / UCVar1,2); 14 extensions across a 19-UC base is dense but defensible. | No action — info only. Future audit could check each extension's "base stands alone" property. |

### §3.3 Case_03 — OmniBank Financial (Doc22, STATUS=DRAFT v3.1)

**Structure count.** 33 fully-dressed UC cards (UC-01..UC-33) all in
§4.2..§4.8 (31 product + 2 PKG-DS privacy/data-subject). §10 headings = 33.

| §10 field | Count | Required | Status |
|---|---|---|---|
| Provenance | 33 | 33 | OK |
| Constrained by | 33 | 33 | OK |
| Rules / NFR | 33 | 33 | OK |
| Threats addressed | **31** | 33 | **MISSING 2** |
| NIST anchors | 33 | 33 | OK |

**Missing Threats addressed (per-card):** UC-01 (DPO Data Erasure, line 258),
UC-02 (Data Subject Data Export, line 380). Both are PKG-DS privacy UCs.

| ID | Severity | Hard rule / anti-pattern | What | Why it fails | Suggested fix |
|---|---|---|---|---|---|
| C3-FIND-01 | **P1** | rule #5 / §10 schema | UC-01 (DPO Data Erasure) and UC-02 (Data Subject Export) §10 blocks lack `**Threats addressed:**`. | Schema is mandatory; even privacy/Data Subject UCs must enumerate which MUCs they mitigate. | Populate from PKG-DS threat catalogue: typically MUC-C3-12 (data export over-disclosure), MUC-C3-13 (erasure audit gap), etc. Cross-check `Doc24_Use_Case_Variability.md` and the `«mitigated by»` edges in `Doc23_Use_Case_Relationships.md`. |
| C3-FIND-02 | **P2** | rule #5 / heading collision | `## 10. DOCUMENT APPROVAL` at line 4182 (top-level) **collides** with the per-UC `##### 10 Security & Compliance Annex (AEGIS)`. | Heading-numbering collision — same root cause as C2-FIND-02. | Rename top-level to `## A. DOCUMENT APPROVAL` (or renumber all top-level sections §A..§F). Localised edit. |
| C3-FIND-03 | **P3** | documentation hygiene | Doc22 STATUS=DRAFT v3.1. UC-01..UC-33 are 100% fully-dressed and §10 is near-100% complete. | Stale draft status — the body has surpassed baseline. | Bump to v3.2 + BASELINE (or document why DRAFT is correct). |
| C3-FIND-04 | (INFO) | rule #4 / edges | Relationships doc (Doc23) shows 35 `«include»` + 15 `«extend»` edges. Dense but documented. | Higher density than C2 (same family of families). | No action — info only; 35 includes are plausible for 33 UCs given banking-context shared flows. |

### §3.4 Cross-case observations

| Check | C1 | C2 | C3 |
|---|---|---|---|
| Total UCs (incl. abbreviated §7/§3) | 23 product + 13 §3 sec (≈ 36 cards referenced) | 19 product + 15 §7 compliance (34 total) | 33 fully-dressed (incl. 2 PKG-DS) |
| Fully-dressed `#### Use-Case:` blocks | 23 | 19 | 33 |
| §10 fields full (5/5) per blocked card | 18/23 (5 missing Threats) | 19/19 | 31/33 (2 missing Threats) |
| Annex A PlantUML blocks | 22 | 6 (+1 in Doc21 §5.1) | 8 |
| Annex B sequenceDiagram blocks | 23 | 19 | 33 |
| `;` gotcha in Mermaid | 0 | 0 | 0 |
| `participant OFF*` gotcha | 0 | 5 (lines 95, 119, 134, 145, 158) | 0 |
| `autonumber off` gotcha | 0 | 0 | 0 |
| Top-level `## 10.*` collision with per-UC §10 | none | YES (line 2896) | YES (line 4182) |
| Legacy `U.C.X.Y.Z` refs (historical) | 11 | 8 | 0 |
| A1 CRUD-as-UC titles | 4 (UC-19/20/21/36) | 0 | 0 |
| A5 Vague-verb UC titles ("Handle/Process/Manage") | 0 | 0 | 0 |
| `<RelationshipDoc>` «include» / «extend» | 6 / 6 (+ «constrains» 4, «threatens» 4, «mitigated by» 3) | 15 / 14 | 35 / 15 |
| Lane separation (UCs only in catalogue) | OK | OK | OK |
| PROC/CAP as ovals/actors in Annex A | 0 (rule §5C.5 satisfied) | 0 | 0 |

**Reading the table.** The §10 schema gap is **3 cases × 2-5 cards** = 7
missing Threats fields total (5+0+2). Two cases (C2, C3) share the same
`## 10.*` heading-collision pattern, fixable in one pass per case. C2 has
the densest compliance-UC gap (15 §7 abbreviated cards). C1 is unique in
its 4 CRUD-as-UC titles. C3 is the cleanest overall.

---

## §4 Known closed (do NOT re-flag)

These were closed by 2026-09-05 campaigns and remain green at R0 time:

- **Lane-purity** of Doc20/21/22 (UCs only; PROC/CAP in Doc31/32).
- **Flat UC-NN numbering** per case (C1 01..40, C2 01..36, C3 01..33).
- **PlantUML + committed SVG** in Annex A (no Mermaid useCaseDiagram).
- **Lane separation** (PROC/CAP never appear as ovals/actors in Annex A).
- **`<<extend»`/`<<include»` edges enumerated** in Relationships docs.
- **6 borderline titles** (U.C.2.4.2/3.2.1/3.3.1/4.4.1 / U.C.10.5.1/11.5.1) — already in P7 ledger.
- **Realization Class tagging** (UC/CAP/PROC) — closed.
- **Evidence items / maturity items** — separate concerns, not in scope.
- **Master-Dashboard integration** (case-aware crosslinks, drilldown, modal) — outside this audit.

---

## §5 Severity-rubric recap (for the priority queue)

- **P0** — card missing a required RUP 10-section (rule #5 fail).
- **P1** — required §10 field missing in a populated card.
- **P2** — anti-pattern visible at naming or diagram level; Mermaid gotcha on rendered annex.
- **P3** — cosmetic / stale / heading-collision (low-risk rename).

---

## §6 Priority queue (proposed, NOT applied)

Sequenced from cheapest fix-per-impact to most expensive:

| Priority | Item | Files affected | Locus | Estimated effort |
|---|---|---|---|---|
| **P3 / fast** | C2-FIND-02 + C3-FIND-02 — rename top-level `## 10.*` to `## A.*` (or renumber) | `Doc21_Use_Cases_Catalog.md` line 2896; `Doc22_Use_Cases_Catalog.md` line 4182 | per-case catalogue | 5 min per file |
| **P3 / fast** | C1-FIND-04 + C2-FIND-04 — append `(formerly U.C.X.Y.Z)` to legacy refs (optional) | Doc20 lines 47, 3040–3057; Doc21 lines 2461–3196 | historical prose | 5 min each |
| **P2 / fast** | C2-FIND-03 — rename `participant OFFR` → `BOFR` in 5 lines of Annex B | `Doc21/annexes/B_Sequence_Diagrams.md` lines 95, 119, 134, 145, 158 | Mermaid aliases | 10 min, must verify render |
| **P3 / fast** | C1-FIND-03 — decide policy on A6 UI-contamination in MSS steps (accept-vs-rewrite) | Doc20 §2 product UC §4 Basic Flows | body text | policy decision |
| **P1 / medium** | C1-FIND-01 — populate `**Threats addressed:**` for UC-17, UC-23, UC-26, UC-29, UC-34 | Doc20 §10 blocks at lines for those 5 cards | §10 fields | 30 min, requires MUC-01..08 mapping |
| **P1 / medium** | C3-FIND-01 — populate `**Threats addressed:**` for UC-01, UC-02 (PKG-DS) | Doc22 §10 blocks at lines 258, 380 | §10 fields | 15 min, requires PKG-DS threat cat. |
| **P3 / medium** | C2-FIND-05 + C3-FIND-03 — STATUS frontmatter hygiene (DRAFT → BASELINE) | Doc21 v1.7→v1.8 BASELINE; Doc22 v3.1→v3.2 BASELINE | frontmatter | 5 min each, requires smoke test |
| **P2 / heavy** | C2-FIND-01 — promote 15 §7 compliance UCs from summary-table rows to full `#### Use-Case:` blocks with §1..§10 anatomy | Doc21 §7.x — 15 cards | entire §7 | half-day sprint |
| **P2 / heavy** | C1-FIND-02 — rename 4 CRUD-as-UC titles to user-goal form (e.g. *Stand Up a Workspace*) + update cross-refs (Catalogue §2, Counts frontmatter, MUC mapping, dashboard widgets) | Doc20 §2 + Master-Dashboard JSON if any UC-19/20/21/36 referenced | titles + side-effects | 1-2 hours, regression risk |
| **P2 / policy** | C1-FIND-05 — decide whether §3 security/compliance abbreviated cards comply with rule #5 or warrant full RUP anatomy | Doc20 §3 | policy + body | review-level |

**Total estimated effort**, top-to-bottom: ~1 working day for all P1+P2 fixes
(assuming C2 §7 promotion and C1 CRUD renames are accepted). If the user
prefers a strict reading of rule #5 ("every UC must be §1..§10 complete"),
then C2-FIND-01 alone is a sprint of its own.

---

## §7 Decision points for the user (P7)

The following are policy-level (not implementation) and should be ratifed
before any of the priority-queue edits above proceed:

1. **A6 UI-contamination policy.** "Member clicks Save" in a product-UC
   MSS — is that an actor-intention (the actor intends to save) or a
   UI-level verb (rule #6 violation)? Skill says no UI verbs, but the AEGIS
   product-realism feedback says UCs should look like product UCs.
   *Recommendation:* treat `Member clicks X` as acceptable when X is a
   navigation step (Save, Submit), reject only `Member types X in field Y`.

2. **Compliance-UC abbreviated form.** Should `#### Use-Case:` blocks exist
   for §3/§7 compliance UCs (Case_01 §3, Case_02 §7), or is the
   summary-table + lane-card pointer (Doc31/32) sufficient?
   *Recommendation:* summarise in catalogue but always expand to §1..§10
   anatomy for **P0** UCs only (those with HIGH/CRITICAL priority or
   that are referenced by MUCs). For the rest, summary + lane card is OK.

3. **Heading-collision fix path.** Rename top-level `## 10.*` → `## A.*`,
   OR renumber all top-level sections §A..§F? 
   *Recommendation:* rename top-level only (one file each, 2 lines each),
   document convention in skill `references/02-card-template.md §D`.

4. **CRUD-as-UC renames scope.** If C1-FIND-02 is approved, do the
   renames cascade into Doc22/21, Master-Dashboard JSON, and the
   CSV/script that the master dashboard uses? Or are they case-local?
   *Recommendation:* case-local in Doc20; verify Master-Dashboard
   references by grep before commit.

---

## §8 Reproducibility

| Tool | Where |
|---|---|
| Count `«include»` / `«extend»` edges | Python `re.findall(r"«include»", text)` over Relationships docs |
| Per-card identification | Python split on `^#### Use-Case: ` boundary |
| §10 field count | `grep -c "Threats addressed\|Provenance:\|Rules / NFR\|NIST anchors\|Constrained by"` |
| CRUD/Handle/Process/Manage sweep | `grep -iE "\b(Create\|Read\|Update\|Delete\|Modify\|Add\|Remove)\b"` against `#### Use-Case:` titles + summary-table rows |
| `OFF*` / `autonumber off` gotcha | `grep -nE "participant\s+OFF[^R]\|participant OFFR\|autonumber off"` over annex B |
| Legacy `U.C.X.Y.Z` refs | `grep -nE "U\.C\.[0-9]" over catalogues + version histories |

All counts in this report were computed at audit time and frozen at the
document_id header (`updated: 2026-09-09`). The audit is read-only — no
file outside `02_CASES/WRITING_USE_CASES_AUDIT_R0.md` was modified.

---

## Appendix A — 8 hard rules (verbatim from SKILL.md)

1. Sea level by default.
2. Title is active-verb goal phrase.
3. One primary actor, named by role, not by person.
4. `<<include>>` for mandatory shared; `<<extend>>` only when the base stands alone.
5. AEGIS Bike4All RUP 10-section template; §10 non-negotiable.
6. MSS steps are actor intentions, not UI actions.
7. UC diagrams = PlantUML + SVG (annex A); sequence = Mermaid (annex B); UC ovals only; gotchas `;` and `OFF`.
8. Process before diagram (RMAC p1 slides 16–37).

## Appendix B — 10 anti-patterns (verbatim from references/03-... §A)

A1 CRUD-as-UC; A2 Function Decomposition; A3 Missing Primary Actor;
A4 Wrong Granularity; A5 Bad Naming; A6 UI Contamination;
A7 `<<extend»` Overuse; A8 Diagram-Only UC; A9 Driving Design Literally;
A10 NFRs in MSS.

## Appendix C — §10 schema (verbatim from references/02-... §C)

| Field | Format | Example |
|---|---|---|
| Provenance | `[ATTESTED] Source: <DocNN §N>` or `[ASSUMED]` | `[ATTESTED] Source: Doc12 §4` |
| Constrained by | comma-separated `UC-*` / `PROC-*` ids | `UC-12, PROC-04` |
| Rules / NFR | comma-separated `RULE-*` / `NFR-*` ids | `NFR-D-04.1-012` |
| Threats addressed | comma-separated `MUC-*` ids | `MUC-07` |
| NIST anchors | `PR.AA-NN` style | `PR.AA-01, PR.AA-03` |
