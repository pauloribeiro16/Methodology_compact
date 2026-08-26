# Validation Report — Case_03 OmniBank — Block G (Tier 1 + Tier 2)

**Date:** 2026-08-07
**Validator:** Fresh sub-agent (no prior exposure to the build)
**Contract branch:** `feature/aegis-p2-case03-csf-pf-airmf`
**Commit chain under review:**
```
c7fb6d2 [EXECUTOR] Bloco F — 4 visualizações + 6 folhas Excel (3 frameworks, MAX complexity)
05be17a [EXECUTOR] Bloco D — Doc 11 estendido (campos 19-24, tri-maturidade CSF+PF+AI RMF)
4d0f41a [EXECUTOR] Bloco E — 04b deprecated for maturity (moved to Doc 13)
082d185 [EXECUTOR] Bloco C — Doc 13 unified matrix (3 frameworks) + triple maturity (MAX complexity)
ffa86b8 [EXECUTOR] Bloco B — NI formal (AVG+AI MUST) em 78 cartões, DR-002 resolvido
3f5606e [EXECUTOR] Baseline prerequisites — NIST mappings and unified matrix SPEC
```

> **Note (P5 — Change propagation):** The chain has 5 EXECUTOR commits covering Blocks B/C/D/E/F but is **missing Bloco A** (crosswalk DRAFT → ACTIVE promotion) that Case_02 branch included (commit `b203b93` on Case_02). The Crosswalk is therefore still DRAFT/0.1 in the working tree (see FN-01).

---

## §A — Tier 1: Completeness & Consistency

### A.1 — Raw Python output (verbatim)

```
FAIL: TIER 1 CHECKS
  [OK] Doc 11 CR row count (should be 38 unique + duplicates, total ~44): actual=38, expected=38
  [OK] Doc 11 BPR row count (should be 40 unique): actual=40, expected=40
  [OK] Doc 13 sub-section IDs: actual=['1', '2', '3', '4', '5', '6', '7', '8'], expected=['1', '2', '3', '4', '5', '6', '7', '8']
  [OK] Doc 13 §3 CR YAML blocks (expected 38 unique): actual=38, expected=38
  [OK] Doc 13 §3 BPR YAML blocks (expected 40 unique): actual=40, expected=40
  [OK] Doc 13 AI RMF distinct (expected >0, prove ACTIVE): actual=60, expected='>0'
  [OK] Doc 13 placeholder count (should be 0): actual=0, expected=0
  [FAIL] Crosswalk status ACTIVE: actual='DRAFT', expected='ACTIVE'
  [FAIL] Crosswalk version 1.0: actual='0.1 (Template)', expected='1.0'
  [OK] 04b status DEPRECATED_FOR_MATURITY: actual='DEPRECATED_FOR_MATURITY', expected='DEPRECATED_FOR_MATURITY'
  [FAIL] 04b maturity_owner Doc 13: actual='02_PHASE2_RULES_RICH/13_Framework_Mapping_Matrix.md', expected='13_Framework_Mapping_Matrix.md'
  [OK] Doc 11 frontmatter has normative_intensity_rule: actual=True, expected=True
  [OK] Doc 11 frontmatter has dr_002_resolution: actual=True, expected=True
  [OK] Doc 11 frontmatter has frameworks_mapped: actual=True, expected=True
  [OK] Doc 11 frontmatter has maturity_dual_mode: actual=True, expected=True
  [OK] frameworks_mapped includes NIST_AI_RMF_1.0: actual=True, expected=True
  [OK] maturity_dual_mode = triple: actual='triple', expected='triple'
  [OK] Excel total sheets (13): actual=13, expected=13
  [OK] Excel has sheet Unified_Matrix: actual=True, expected=True
  [OK] Excel has sheet Govern_Consolidated: actual=True, expected=True
  [OK] Excel has sheet Mapping_nm: actual=True, expected=True
  [OK] Excel has sheet Maturity_Triple: actual=True, expected=True
  [OK] Excel has sheet Cov_Function: actual=True, expected=True
  [OK] Excel has sheet Heatmap_Maturity: actual=True, expected=True
  [FAIL] Doc 13 CSF IDs not in frozen: actual=['DE.CM-04', 'DE.CM-05', 'GV.SC-06', 'GV.SC-07', 'GV.SC-08', 'GV.SC-09', 'ID.AM-08', 'ID.RA-07', 'ID.RA-08', 'ID.RA-10', 'RC.CO-01', 'RS.AN-01', 'RS.MI-03', 'RS.RP-01'], expected=[]
  [FAIL] Doc 13 PF IDs not in frozen: actual=['CT.DP-P6'], expected=[]
  [FAIL] Doc 13 PF IDs using v1.0 redirects: actual=['PR.PO-P4'], expected=[]
  [OK] Doc 13 AI RMF IDs not in frozen: actual=[], expected=[]
  [OK] Doc 13 §1 column bleed (CSF/PF/AI RMF must be separate): actual=0, expected=0
  [FAIL] CR with AI-C MUST override (expected ~15): actual=0, expected='>=12'
  [FAIL] NI distribution MUST count (expected 30-36): actual=0, expected='30-36'
  [FAIL] NI distribution SHOULD count (expected 2-8): actual=0, expected='2-8'
```

### A.2 — Script-bug triage (manual re-check)

Three of the FAIL lines are **Tier-1-script bugs**, not real failures. I verified by re-reading the source columns directly:

| Check | Script read | Reality (correct column) | Real status |
|-------|-------------|--------------------------|-------------|
| CR AI-C MUST override | regex matched nothing | `15` CR rows contain `AI-C present forces MUST` in column 9 | **PASS** (15 ≥ 12) |
| NI MUST count | regex matched nothing | column 9 (`NI (recomputed DR-002 AVG+AI)`): 33 MUST + 5 SHOULD | **PASS** (33 ∈ [30,36]; 5 ∈ [2,8]) |
| NI SHOULD count | regex matched nothing | same as above | **PASS** |
| 04b maturity_owner | full path vs basename | full path is **more** precise, content points to Doc 13 | **PASS** (false negative) |

The NI distribution by DR-002 recomputed column (the column the methodology treats as authoritative — see Doc 11 frontmatter `dr_002_resolution`):

| Tier | Count | Notes |
|------|------:|-------|
| MUST (NI ≥ 2.5 or AI-C forces) | 33 | All 38 DORA clauses are NI=3 → MUST; 15 AI-C source CRs → MUST |
| SHOULD (2.0 ≤ NI < 2.5, no AI-C) | 5 | CR-D-01.2-001, CR-D-03.2-001, CR-D-04.2-001, CR-D-04.4-001, CR-D-07.1-001 |
| MAY (NI < 2.0) | 0 | — |

This matches the Block B spec exactly ("33 MUST + 5 SHOULD with 12 GDPR/CRA NI=2 clauses").

### A.3 — True Tier 1 failures

After triage, the following are **real** Tier 1 failures:

1. **Crosswalk status `DRAFT` / version `0.1 (Template)`** — was not promoted to ACTIVE/1.0 on this branch (see FN-01).
2. **14 CSF IDs used in Doc 13 that are not in the frozen list** (see FN-02).
3. **`CT.DP-P6` does not exist in frozen PF list** (max is `CT.DP-P5`) — see FN-02.
4. **`PR.PO-P4` is a v1.0 redirect** (MOVED to `PR.IR-P2`) — see FN-02.

### A.4 — Pass/Fail summary

| Category | Pass | Fail | Total |
|----------|-----:|-----:|------:|
| Card counts (CR/BPR) | 2 | 0 | 2 |
| Doc 13 structure | 4 | 0 | 4 |
| Crosswalk status | 0 | 2 | 2 |
| Doc 04b status | 2 | 0 | 2 |
| Doc 11 frontmatter | 5 | 0 | 5 |
| Excel sheets | 7 | 0 | 7 |
| ID integrity | 1 | 3 | 4 |
| NI/AI-C semantics (after script fix) | 3 | 0 | 3 |
| Cross-leak §1 | 1 | 0 | 1 |
| **Total** | **25** | **5** | **30** |

After excluding the 3 script bugs and the 1 false-positive (04b maturity_owner), the real Tier 1 score is **25 pass / 4 fail**.

### A.5 — Lint summary (`run_all_lints.py --case Case_03`)

- Phase 1: 6/6 PASSED (Company Context, Regulatory Mapping, Anti-Hallucination, Ground Truth, Cross-Document, Template)
- Phase 2: 1/1 PASSED (Doc 11 Rules Catalog)
- Phase 3: 7/7 PASSED (Use Cases, Relationships, Variability, Arch Nodes, Req Allocation, Compliance Gates, Functional Tree)
- Structural: Document Structure reports 41 "errors" (cross-cutting template-section warnings — pre-existing case-level issue affecting 04a/04b/04c/04d/07b/07c/13 and historical sprint reports; not a blocker for this contract); Mermaid Syntax 5/5 PASSED.

The structural lint "Document Structure" lists Doc 13 as missing standard sections `1. DOCUMENT PURPOSE` / `VERSION HISTORY`. This is **by design** for Case_02/Case_03 which use the `## §1..§8` semantic sections per the methodology SPEC. No blocker.

---

## §B — Tier 2: Realism & Alignment

### B.1 — 3-framework separation (CSF / Privacy FW / AI RMF)

**PASS — clean separation throughout.** Cross-leak check performed for all four major framework-mapping sections (§1 tabular, §3 YAML, §5 tabular, §8 tabular) with the strictest pattern (CSF column checked for PF-P\d+ and AI RMF GOVERN|MAP|MEASURE|MANAGE patterns, etc.). Result: **0 cross-leak rows in any section**. The §2 Govern view (6 subsections §2.1–§2.6) also has exactly 3 framework rows per concept (CSF 2.0 / Privacy FW / AI RMF), totalling 18 framework rows. The discipline of keeping CSF subcats in CSF column only, PF subcats in PF column only, and AI RMF subcats in AI RMF column only is consistently applied.

### B.2 — AI RMF ACTIVE proof

**PASS — AI RMF is genuinely active, not a placeholder.** Evidence:
- 60 distinct AI RMF IDs appear in Doc 13 (all from the frozen 72 — zero invention).
- §3 CR YAML: all 38 CR cards carry an `airmf_subcategories` field; 35 of 38 use real IDs, 3 use `UNMAPPED_AIRMF` (CR-D-02.3-001, CR-D-02.3-001 mappability, CR-D-08.3-001) — this is the prescribed escape valve for CR with no AI Act duty.
- §4.4 defines the 0–4 maturity scale anchored to AI RMF statement language (mentions MEASURE-2.*, MANAGE-1.*, GOVERN-5.1 explicitly).
- §6.3 documents 31/72 AI RMF subcategories as defensibly unused (no AI Act Title III §5 cybersecurity counterpart) — explicit gap analysis, not a silent placeholder.
- §7 mermaid paths include AI Act–specific path (e) anchored on `AI-C05 → CR-D-05.1-001`.

### B.3 — NI distribution defensibility

**PASS.** Distribution of 33 MUST + 5 SHOULD is the spec-defined Block B outcome for Case_03 (5 regulations including AI Act with all 29 AI clauses at NI=3 and DORA with all 38 clauses at NI=3, plus AI-C MUST override applied to 15 CR). The 5 SHOULD rows (CR-D-01.2-001, 03.2-001, 04.2-001, 04.4-001, 07.1-001) are precisely the GDPR/CRA NI=2 cases that escaped both the DORA override (no DORA in source) and the AI-C override (no AI-C in source) — consistent with the methodology design.

### B.4 — Maturidade Track B for MAX tier

**PASS — proportional and documented.** Per `07b_Proportionality_Profile.md` §3 referenced by Doc 13 §5.1:
- 31 RIGOROUS sub-domains → tgt 4/4 across all 3 frameworks (CSF + PF + AI RMF)
- 5 STANDARD sub-domains → tgt 3/4 (D-02.3, D-03.4, D-05.1, D-05.4, D-06.2)
- 2 STANDARD with operational tgt 4/4 (D-05.2, D-05.3) — justified by 10y BaFin retention + T-002 cryptographic sharding
- §6.4 explicitly confirms "zero sub-domains have tgt < 3" (Track B floor enforced; MAX scale excludes DEFERRED)
The `07b` proportionality was cross-validated against Doc 11 column 13 (Maturity Score) for `cur_csf`, with the same mapping for `cur_priv` and `cur_airmf`. Consistent.

### B.5 — Heatmap MAX formula defensibility

**PASS.** §4.6 documents `gap_worst = MAX(gap_csf, gap_priv, gap_airmf)` with the **N/A exclusion rule** (FN-03 from Case_02 explicitly applied): when a framework is N/A for a control, it is excluded from the MAX, not treated as gap 0. Four worked examples demonstrate the rule's application (CR-D-06.4-001, CR-D-09.1-001, CR-D-10.1-001, CR-D-05.4-001). The 38-row heatmap in §5.2 ends with: **1 RED (D-02.4 TLPT), 6 ORANGE, 31 YELLOW, 0 GREEN, 0 GREY** — matches the expected 1/6/31 distribution for Case_03 MAX tier. The single RED row (D-02.4) is justified: current 1/4 → target 4/4 across all three frameworks, driven by TLPT adversarial robustness + AI bias testing (DORA Art. 26 + AI Act Art. 43 + Annex III §5).

### B.6 — Gap analysis (§6) coverage

**PASS with caveats.** §6 has 7 subsections:
- §6.1: 14 CSF subcategories gap-acceptable or covered-by (with explicit FN-03 carry-over check) — defensible
- §6.2: 45 PF subcategories unused (104 - 59 = 45) — defensible for GDPR-touched scope
- §6.3: 31/72 AI RMF unused — defensibly characterised as internal-practice or outside AI Act T5 cybersecurity scope
- §6.4: zero sub-domains at tgt < 3 (Track B floor) — clean
- §6.5: **Frozen-list integrity findings DEFERRED (DF1)** with an explicit claim "No ID.AM-08 / RS.RP-01 / similar carry-overs in §1 or §3. All identifiers used are from the active frozen lists." — **THIS CLAIM IS FACTUALLY FALSE** (see FN-02). 14 CSF IDs and 2 PF IDs used in §3 do not exist in frozen or use v1.0 redirects.
- §6.6: NI distribution analysis — references 33 MUST + 5 SHOULD (matches Tier 1 reality)
- §6.7: T-001..T-004 + T-005 cross-reference table — complete with Doc 13 anchors (sub-domain + §2.5 risk view + §3 CR + §5.1 + §5.2)

The §6.5 false claim is the most significant Tier 2 finding — the Executive self-reported an integrity check as PASS while the check fails (see FN-02).

### B.7 — 5-regulation coverage in §7 mermaid

**PASS.** §7 has 6 Mermaid sub-paths covering all 5 regulations individually + 1 multi-regulation path:
- (a) GDPR-only — CR-D-05.4-001 (data portability, SOLE AUTHORITY GDPR)
- (b) CRA-only — CR-D-02.1-001 (vulnerability identification)
- (c) NIS 2-only — CR-D-07.4-001 (change management)
- (d) DORA-only — CR-D-02.4-001 (TLPT, DORA Art. 26 + RTS)
- (e) AI Act-only — CR-D-05.1-001 (data governance, AI Act Art. 10)
- (f) Multi-regulation — CR-D-04.3-001 (5-reg, T-001 RESOLVED) — references GDPR Art. 33, CRA Art. 14(3-5), NIS 2 Art. 23, DORA-C35 Art. 19 + RTS, AI-C26 Art. 73

DORA Art. references in §2.5: DORA Art. 5(2), Art. 5 ICT risk governance, Art. 9 ICT risk management framework — all present. §6.7 additionally references DORA Art. 11 (immutable logs), Art. 19 + RTS 2025/301 Art. 6 (4h initial report), Art. 26 (TLPT). §7 path (d) references DORA Art. 26 + RTS explicitly.

### B.8 — DR-002 resolution + AI/DORA override

**PASS.** Doc 11 frontmatter contains:
- `dr_002_resolution` (multi-line block, full text): "DR-002 definido como AVG (não MAX)... qualquer CR com AI-C* nas source clauses é forçado MUST (NI=3)... DORA também é MUST uniforme (todas as 38 DORA cláusulas são NI=3)"
- `normative_intensity_rule: AVG_with_AI_MUST_override`
- The field expected by the validator (`ni_avg_rule_note`) is **not** present under that exact name — Doc 11 uses `normative_intensity_rule` instead. Same semantic content (see FN-03, LOW).

Application:
- AI-C MUST override: **15 CR rows** contain the marker `AI-C present forces MUST` in the DR-002 recomputed column (≥12 expected) — PASS
- DORA override: **27 CR** have DORA in source; of these, **19 have NI=3.000 AVG** and all 27 are recomputed to MUST via either AVG ≥ 2.5 or AI-C presence. The "all 38 DORA clauses are NI=3" statement in frontmatter refers to the source-clause level, not the CR level (38 unique DORA clauses spread across 27 CRs) — semantically correct.

---

## §C — Findings

### FN-01 — Crosswalk still DRAFT/0.1 (Template) [HIGH]

**Location:** `03_REFERENCE_MATERIAL/Framework_Mappings/Framework_Crosswalk_ARM.md` lines 4 + 8

**Evidence:** Frontmatter shows `version: 0.1 (Template)` and `status: DRAFT`. Git log shows the Crosswalk was last touched in the "Rebrand" commit (67eaac5) — no Bloco A promotion on this branch. Case_02 branch added commit `b203b93 [EXECUTOR] Bloco A — crosswalk promoted DRAFT→ACTIVE (Case_02 contract reuse)` but this commit was never ported to Case_03.

**Impact:** The Crosswalk is the shared mapping artifact for the 38 sub-domains. Doc 13 §6.1 explicitly says "the mapping in §1 + §3 covers the CSF subcategories that appear in `Framework_Crosswalk_ARM.md`". A DRAFT Crosswalk is semantically weaker than an ACTIVE one — downstream Phase 3 lints (Requirements Allocation, Compliance Gates) inherit this fragility.

**Recommendation:** Port Case_02's Bloco A commit (or apply a targeted frontmatter promotion) — promote version to `1.0` and status to `ACTIVE`, with a changelog entry referencing the Case_03 contract.

### FN-02 — 16 invented / non-frozen IDs in Doc 13 [HIGH]

**Location:** Doc 13 §3 YAML, §1 table, §8 visualizations, and §6 gap-analysis text.

**Evidence:** The frozen list `00_METHODOLOGY/PREPROCESSING/NIST_CSF_2.0_subcategories.md` declares 106 subcategories but only contains 98 active IDs (the file acknowledges this in §6.5: "declares 106 subcategories but the frozen active IDs are 98 (8 duplicate IDs in freeze)"). The frozen list for `NIST_Privacy_FW_1.1_subcategories.md` has 34 v1.0 redirects.

IDs used in Doc 13 that violate the frozen-list contract:

**CSF — actively used in §3 YAML `csf_subcategories` (6 IDs):**
| ID | Used in cards | Frozen status |
|----|---------------|---------------|
| `GV.SC-06` | CR-D-06.3-001, BPR-D-06.3-001 | NOT in frozen (max is `GV.SC-05`) |
| `GV.SC-07` | CR-D-06.1-001, BPR-D-06.1-001 | NOT in frozen |
| `GV.SC-09` | CR-D-06.2-001, BPR-D-02.2-001 | NOT in frozen |
| `ID.RA-07` | CR-D-07.4-001, BPR-D-07.4-001 | NOT in frozen (max is `ID.RA-06`) |
| `ID.RA-08` | CR-D-02.1-001, CR-D-02.3-001, BPR-D-12.4-001 | NOT in frozen |
| `ID.RA-10` | CR-D-06.1-001 | NOT in frozen |

**CSF — referenced in §6 gap-analysis text (8 IDs, not in active mapping):**
`DE.CM-04`, `DE.CM-05`, `GV.SC-08`, `ID.AM-08`, `RC.CO-01`, `RS.AN-01`, `RS.MI-03`, `RS.RP-01` (plus `RS.RP-01` also appears in one BPR mapping_rationale text at line 55549).

**PF — `CT.DP-P6`** in §6.2 text (frozen max is `CT.DP-P5`).
**PF — `PR.PO-P4`** in §1, §3, §6.2, §8 (frozen marks this as `Moved to PR.IR-P2` — v1.0 redirect).

**Impact:** The frozen-list integrity rule from root AGENTS.md says "Sub-agents MUST pick from this list — no invention of IDs allowed. If a SecurityRule does not map cleanly to any subcategory below, use `UNMAPPED_CSF` per the brief." Doc 13 §6.5 explicitly states "No ID.AM-08 / RS.RP-01 / similar carry-overs in §1 or §3. All identifiers used are from the active frozen lists" — **this self-check is false** for the 6 active YAML IDs above. The §6.5 claim should be corrected, and the 6 active IDs replaced with `UNMAPPED_CSF` (CSF column) or with the closest frozen equivalent.

**Recommendation:**
1. For the 6 active CSF YAML IDs: replace with `UNMAPPED_CSF` token (preserves traceability intent) OR remap to nearest frozen IDs (e.g. `GV.SC-06/07/09` → `GV.SC-04/05` with rationale; `ID.RA-07/08/10` → `ID.RA-04/05/06` with rationale).
2. For `PR.PO-P4`: replace with `PR.IR-P2` (the v1.0 redirect target) — affects 7 occurrences across §1, §3, §6.2, §8.
3. For §6 gap-analysis text mentions of non-frozen IDs (`DE.CM-04`, `GV.SC-08`, etc.): keep them as descriptive references but prefix with "(`non-frozen`) " or move them to a separate "out-of-frozen-set" subsection that does not claim these are valid subcategories.

### FN-03 — Doc 11 missing `ni_avg_rule_note` field [LOW]

**Location:** Doc 11 frontmatter (lines 14–22).

**Evidence:** Validator spec expected both `dr_002_resolution` AND `ni_avg_rule_note` fields. Doc 11 has `dr_002_resolution` (correct) and `normative_intensity_rule: AVG_with_AI_MUST_override` (semantically equivalent — describes the AVG+AI MUST rule), but does not use the exact key `ni_avg_rule_note`.

**Impact:** Cosmetic naming difference. The semantic content (AVG with AI-C MUST override) is fully documented in `dr_002_resolution` and `normative_intensity_rule`.

**Recommendation:** Add `ni_avg_rule_note` as an alias or rename `normative_intensity_rule` for consistency with Case_02.

### FN-04 — Structural lint flags Doc 13 missing standard sections [INFO]

**Location:** Doc 13 lacks `## 1. DOCUMENT PURPOSE` and `## N. VERSION HISTORY` headings.

**Evidence:** `run_all_lints.py` structural phase reports 41 "errors" across the case, 2 of which target Doc 13. The lint output shows `13_Framework_Mapping_Matrix.md: Missing required section matching '^#{1,2}\s+\d+\.\s+(DOCUMENT PURPOSE|PROPÓSITO|OBJECTIVO)'` and the equivalent for VERSION HISTORY.

**Impact:** None — the methodology SPEC for Case_02/Case_03 explicitly uses the `## §1..§8` semantic section model. This is consistent with prior cases (Case_02 Doc 13 has the same structure). The structural lint pattern is overly strict for Case_02+ docs.

**Recommendation:** Either (a) update the lint pattern to accept `## §N — Title` as a valid Document Purpose section, or (b) add the two required sections to Doc 13 as 2-line stubs (no functional change). Case_01's standard template uses the `## N.` form; Case_02+ has migrated to `## §N`.

### FN-05 — §6.5 self-check contradicts reality [MED]

**Location:** Doc 13 §6.5 line 1434.

**Evidence:** §6.5 states "Carry-over check (FN-03 from Case_02): No `ID.AM-08` / `RS.RP-01` / similar carry-overs in §1 or §3. All identifiers used are from the active frozen lists." The mention of `ID.AM-08` and `RS.RP-01` is incidental (they appear in this sentence only), but the **broader claim** about "all identifiers used" is false — 6 CSF IDs + 1 PF ID (CT.DP-P6 + PR.PO-P4) are used in §3 that are not in the frozen list.

**Impact:** A validator or auditor relying on §6.5 as the integrity check would be misled. This finding is structurally subsumed by FN-02 but worth flagging separately because it concerns the **self-audit statement**, not just the underlying IDs.

**Recommendation:** Either (a) correct §6.5 with a true inventory of non-frozen IDs and rationale, or (b) remove the overconfident carry-over claim.

---

## §D — Verdict

**PASS_WITH_FINDINGS** — Contract is structurally and semantically sound, but two HIGH-severity ID-integrity findings (FN-01 Crosswalk DRAFT, FN-02 16 non-frozen IDs) require executor follow-up before Block H (Phase 3 trigger). The methodology's intent (tri-maturidade CSF+PF+AI RMF, MAX tier, 5 regulations, T-001..T-004 resolution, heatmap aggregation) is correctly implemented; the gaps are in crosswalk promotion discipline and frozen-list boundary enforcement.

| Severity | Count | Findings |
|----------|------:|----------|
| HIGH | 2 | FN-01, FN-02 |
| MED | 1 | FN-05 |
| LOW | 1 | FN-03 |
| INFO | 1 | FN-04 |
| **Total** | **5** | — |

**Most important non-blocking issue:** **FN-02** — 16 invented / non-frozen IDs in Doc 13 (6 active in §3 YAML `csf_subcategories`, plus 10 in §6 gap-analysis text). The §6.5 self-audit claim that "all identifiers used are from the active frozen lists" is factually false and undermines the integrity check. Fix: replace 6 active YAML IDs with `UNMAPPED_CSF` or remap to nearest frozen equivalents; replace `PR.PO-P4` (v1.0 redirect) with `PR.IR-P2` across §1/§3/§6.2/§8 (7 occurrences).
