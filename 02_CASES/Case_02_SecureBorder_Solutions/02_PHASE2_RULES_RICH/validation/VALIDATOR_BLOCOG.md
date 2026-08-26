# VALIDATION REPORT — Block G

## Header

- Date: 2026-08-07
- Validator: fresh sub-agent
- Branch: `feature/aegis-p2-case02-csf-pf-airmf`
- Contract: AEGIS Phase 2 — Case_02 SecureBorder Solutions — CSF + Privacy FW + AI RMF
- Review mode: cold review; Executor artifacts unchanged
- Commit chain reviewed: `git log --oneline -10`; latest Executor commit `504a7f0 [EXECUTOR] Bloco F — 4 visualizações + 6 folhas Excel (3 frameworks)`
- Working tree before report: clean

## §A Tier 1 — Completeness & Consistency

### Supplied acceptance script output (verbatim)

```text
FAIL: TIER 1 CHECKS
  [OK] Doc 11 CR row count (should be 38 unique + duplicates, total ~62): actual=38, expected=38
  [OK] Doc 11 BPR row count (should be 17 unique): actual=17, expected=17
  [OK] Doc 13 sub-section IDs: actual=['1', '2', '3', '4', '5', '6', '7', '8'], expected=['1','2','3','4','5','6','7','8']
  [FAIL] Doc 13 §3 CR YAML blocks (expected 38 unique or 55 with duplicates): actual=38, expected='38 or 55'
  [OK] Doc 13 §3 BPR YAML blocks (expected 17): actual=17, expected=17
  [FAIL] Doc 13 AI RMF distinct (expected >0, prove ACTIVE): actual=65, expected='>0'
  [OK] Doc 13 placeholder count (should be 0): actual=0, expected=0
  [OK] Crosswalk status ACTIVE: actual='ACTIVE', expected='ACTIVE'
  [FAIL] Crosswalk version 1.0: actual=1.0, expected='1.0'
  [OK] 04b status DEPRECATED_FOR_MATURITY: actual='DEPRECATED_FOR_MATURITY', expected='DEPRECATED_FOR_MATURITY'
  [OK] 04b maturity_owner Doc 13: actual='13_Framework_Mapping_Matrix.md', expected='13_Framework_Mapping_Matrix.md'
  [OK] Doc 11 frontmatter has normative_intensity_rule: actual=True, expected=True
  [OK] Doc 11 frontmatter has dr_002_resolution: actual=True, expected=True
  [OK] Doc 11 frontmatter has frameworks_mapped: actual=True, expected=True
  [OK] Doc 11 frontmatter has maturity_dual_mode: actual=True, expected=True
  [OK] frameworks_mapped includes NIST_AI_RMF_1.0: actual=True, expected=True
  [OK] maturity_dual_mode = triple: actual='triple', expected='triple'
  [OK] Excel total sheets (10): actual=10, expected=10
  [OK] Excel has sheet Unified_Matrix: actual=True, expected=True
  [OK] Excel has sheet Govern_Consolidated: actual=True, expected=True
  [OK] Excel has sheet Mapping_nm: actual=True, expected=True
  [OK] Excel has sheet Maturity_Triple: actual=True, expected=True
  [OK] Excel has sheet Cov_Function: actual=True, expected=True
  [OK] Excel has sheet Heatmap_Maturity: actual=True, expected=True
  [FAIL] Doc 13 CSF IDs not in frozen (must be 0 or explicit UNMAPPED): actual=['DE.CM-04', 'DE.CM-05', 'GV.SC-06', 'GV.SC-07', 'GV.SC-08', 'GV.SC-09', 'ID.RA-07', 'ID.RA-08', 'ID.RA-10', 'RC.CO-01', 'RS.AN-01', 'RS.MI-03'], expected=[]
  [FAIL] Doc 13 PF IDs not in frozen (must be 0): actual=['CT.DP-P6'], expected=[]
  [FAIL] Doc 13 PF IDs using v1.0 redirects (must be 0): actual=['PR.PO-P4'], expected=[]
  [OK] Doc 13 AI RMF IDs not in frozen (must be 0): actual=[], expected=[]
  [OK] Doc 13 §1 column bleed (CSF/PF/AI RMF must be separate): actual=0, expected=0
  [FAIL] CR with AI-C MUST override marker (expected ~17): actual=0, expected='>=15'
```

### Tier 1 interpretation

- Raw output: **23 OK / 7 FAIL**. Four raw failures are comparison-harness artifacts: `38 or 55`, `>0`, and `>=15` are textual expectations rather than predicates, and YAML parses crosswalk version `1.0` as a numeric value.
- Effective acceptance result after independent checks: **27 PASS / 3 FAIL**. The three substantive failed checks are CSF frozen-list integrity, Privacy FW frozen-list integrity, and Privacy FW v1.0 redirect use. Independent source parsing confirms **17 AI-C source CRs and 17 AI-C MUST markers**, so the AI-MUST raw failure is a harness/parser artifact, not an artifact defect.
- Frozen-list integrity remains failed: Doc 13 contains 12 CSF tokens absent from the local frozen extraction, including six absent IDs used in §1/§3 (`GV.SC-06`, `GV.SC-07`, `GV.SC-09`, `ID.RA-07`, `ID.RA-08`, `ID.RA-10`), and does not mark them `UNMAPPED_CSF`. `CT.DP-P6` is absent from the PF frozen extraction; `PR.PO-P4` is a v1.0 redirect.
- Direct structural lint for Case_02 returned **1/2 passed, 1 failed, 31 document-structure errors, 28 warnings**. Doc 13 itself is reported missing the numbered `DOCUMENT PURPOSE` and `VERSION HISTORY` sections. Mermaid syntax passed (4/4 diagrams). Phase 2 and Phase 3 runners passed their available checks.
- `./scripts/test-quick.sh` printed passes for both cases and both quality gates, but the full lint meta-runner reported `0/0 passed` and `All lints passed` while structural lint failed; this is not reliable evidence of a clean Tier 1 result.
- Test collection could not be verified: `python3 -m pytest --collect-only -q` failed because `pytest` is not installed, and no repository virtual environment with pytest was present. No collection-complete claim is made.

## §B Tier 2 — Realism & Alignment

### 1. Three-framework separation

The separation is clean in the checked matrix columns: §1 has zero CSF/PF/AI RMF cross-column bleed, §3 YAML blocks use distinct lists, and V1 in §8 preserves the three separate mapping columns. §2.1–§2.6 each contain exactly three framework rows, including an AI RMF row. However, §2 uses legacy/non-canonical Privacy FW labels such as `ID-P.BE-P1`, `ID-P.RA-P1..P5`, and `GV-P.*` instead of the frozen canonical `ID.BE-P*`, `ID.RA-P*`, and `GV.*-P*` forms; this is recorded as part of FN-01.

### 2. AI RMF ACTIVE proof

AI RMF is demonstrably active: the document contains 65 distinct AI RMF tokens overall, §4.4 names all four Functions, §7 has five path markers and V3 has seven, and the mapping table has 18 CRs with populated AI RMF lists, exceeding the required 17. The 31/72 unused subcategories are explicitly listed in §6.3 with rationale. The 18th mapped CR is nevertheless inconsistent with Doc 11: `CR-D-07.1-001` has AI RMF mappings in Doc 13 (§1/§3) but its Doc 11 source is GDPR/CRA only and contains no `AI-C*`; this unsupported extra anchor is FN-02.

### 3. Normative-intensity distribution

The distribution is defensible after the documented DR-002 rule: independent parsing finds 17 CRs with `AI-C*` sources and 17 corresponding `AI-C present forces MUST` markers; Doc 13 has 37 CR MUST and one SHOULD (`CR-D-07.4-001`), while all 17 BPR-D cards are SHOULD. The AI_Act override appropriately prevents AVG dilution for AI-Act-sourced rules. The main alignment defect is not the distribution but the extra AI RMF mapping for D-07.1 and the mismatch between Doc 13's claim of 17 AI-anchored CRs and its actual 18.

### 4. Maturidade Track B

The maturity model is directionally realistic for a HIGH-complexity company: most current values are 3, RIGOROUS areas target 4, STANDARD areas target 3–4, and AI RMF MEASURE is the largest gap at current 2 to target 4. §4.5 provides 15 Function rows and explicit justifications. It is not internally aligned with the Track B input, however: 07b declares 35 active sub-domains, with D-07.4, D-08.3, and D-09.3 excluded, while Doc 13's V4 presents 37 rows, excludes only D-08.3, includes D-07.4 as GREY, and includes D-09.3 as GREEN. The unresolved MEDIUM-versus-LARGE classification in 07b also makes the 8 RIGOROUS/27 STANDARD distribution provisional.

### 5. Heatmap formula

§4.6 and §8 explicitly document `gap_display = MIN(gap_csf, gap_priv, gap_airmf)` with N/A exclusion, and every V4 row is arithmetically consistent with that MIN calculation; the reported color counts are exactly 28 GREEN, 8 YELLOW, 1 GREY. The counts are not defensible as a worst-axis risk heatmap: MIN selects the smallest applicable gap, so a control with a CSF gap of 1 and PF gap of 0 is rendered GREEN, while the prose calls the display the “worst axis.” A MAX-based worst-gap view, or separate axis statuses, is needed to avoid masking a material maturity deficit; this is FN-03.

### 6. Gap analysis

The requested gap evidence is present: §6.5 explicitly cross-references T-001 through T-004, §6.3 lists 31/72 unused AI RMF subcategories with reasons, and §6.4 gives proportionality rationale for target-3 entries. The CSF gap list itself contains absent frozen-list IDs without `UNMAPPED_CSF` handling, and the §6.4 heading says `tgt < 3` while listing target `3`; both reduce mechanical clarity. The low-target and active-scope claims also inherit the 35-versus-37 inconsistency noted in FN-04.

### 7. AI_Act signals

The AI_Act signal is strong: §7 has separate GDPR, CRA, NIS 2, AI_Act, and multi-regulation path markers; V3 expands this to seven paths; and each §2 Govern concept has a populated AI RMF row, including `GOVERN-1.1`. The labels “CRA-only” and “AI_Act-only” are not strictly accurate for the selected CRs: `CR-D-02.1-001` carries CRA/NIS2/AI_Act and `CR-D-05.1-001` carries GDPR/CRA/AI_Act. The source-to-rule paths are present, but the “only” labels should be corrected or the paths should use genuinely sole-authority rules; this is FN-05.

### 8. DR-002 resolution and AI override

Doc 11 frontmatter contains `dr_002_resolution`, `normative_intensity_rule`, `frameworks_mapped`, `maturity_dual_mode: triple`, and the AI override rule; Doc 13 repeats both the resolution and `ni_avg_rule_note`. Independent parsing confirms the AI-C override is applied to 17 CR rows. The supplied acceptance script's zero count is a regex-column bug, not an artifact failure. The remaining issue is the unsupported D-07.1 AI RMF anchor, which should not be justified as AI-C-derived until its regulatory source is corrected.

## §C Findings

### FN-01 — Frozen framework identifiers are not integrity-safe

**Severity: HIGH**

Doc 13 uses six absent CSF IDs in the core §1/§3 mapping (`GV.SC-06`, `GV.SC-07`, `GV.SC-09`, `ID.RA-07`, `ID.RA-08`, `ID.RA-10`) and lists additional absent CSF/PF IDs in §6 (`DE.CM-04`, `DE.CM-05`, `GV.SC-08`, `RC.CO-01`, `RS.AN-01`, `RS.MI-03`, `CT.DP-P6`). The supplied integrity check therefore fails, and the known absent IDs are not consistently represented as `UNMAPPED_CSF`; §6 also uses non-canonical legacy PF labels (`ID-P.*`, `GV-P.*`). Recommendation: reconcile the frozen source/list declaration first, then replace every unsupported core mapping with a frozen ID or an explicit `UNMAPPED_*` token; normalize §2 PF notation and remove redirected `PR.PO-P4` usage.

### FN-02 — Unsupported AI RMF anchor for CR-D-07.1-001

**Severity: HIGH**

Doc 13 maps `CR-D-07.1-001` to AI RMF in §1 and §3 (for example `GOVERN-4.1`, `GOVERN-4.3`, and `MEASURE-2.7` at `13_Framework_Mapping_Matrix.md:81` and `:490`), producing 18 mapped CRs. Doc 11's source for the same card is GDPR-C09/CRA-C02/CRA-C22 at `11_Rules_Catalog.md:173` and has no `AI-C*`; Doc 13 itself claims only 17 AI-C-derived CRs at `13_Framework_Mapping_Matrix.md:51` and `:101`. Recommendation: either add a traceable AI_Act source clause to Doc 11 through the governing process, or set this CR to `UNMAPPED_AIRMF` and remove the unsupported anchor; do not silently derive framework coverage from applicability alone.

### FN-03 — MIN heatmap contradicts the stated worst-axis interpretation

**Severity: MEDIUM**

The formula and N/A rule are documented at `13_Framework_Mapping_Matrix.md:929-938`, and V4 produces the stated 28 GREEN / 8 YELLOW / 1 GREY counts at `:1429-1473`. Because MIN chooses the smallest applicable gap, it suppresses other-axis gaps and cannot represent the “worst axis only” statement at `:1473`; the table's GREEN rows therefore overstate maturity. Recommendation: retain the requested MIN value only as a separate coverage indicator, and add a MAX/worst-axis heatmap or three axis-specific colors before using this visualization for prioritization.

### FN-04 — Track B active scope and maturity visualization are inconsistent

**Severity: HIGH**

The Track B input declares 35 active sub-domains and excludes D-07.4, D-08.3, and D-09.3 at `07b_Proportionality_Profile.md:65` and `:145-149`. Doc 13 says V4 has 37 rows and only D-08.3 is inactive at `13_Framework_Mapping_Matrix.md:1431`, then includes D-07.4 as GREY and D-09.3 as GREEN. The per-control table also includes the excluded domains. Recommendation: establish one authoritative active-domain set, regenerate §4.5/§5/V4 and all totals from it, and explicitly classify excluded cards as out of scope rather than mixing them with active maturity results.

### FN-05 — Traceability graph “only” path labels are inaccurate

**Severity: LOW**

The five path markers at `13_Framework_Mapping_Matrix.md:1144-1200` are present, but the CRA-only path uses a three-regulation CR and the AI_Act-only path uses a three-regulation CR. Recommendation: rename them “CRA-origin” and “AI_Act-origin,” or select sole-authority rules so the labels match the graph semantics.

### FN-06 — Track B scale classification remains unresolved upstream

**Severity: MEDIUM**

The company is recorded as 450 employees and €120M revenue at `07b_Proportionality_Profile.md:50-59`, while the same document records an open MAJOR finding that these values meet the LARGE thresholds at `:296-309`. Doc 13's 8 RIGOROUS/27 STANDARD maturity basis therefore remains provisional. Recommendation: adjudicate the scale input before treating target maturity and evidence-depth conclusions as final; if MEDIUM is retained, document the explicit deviation from the proportionality model.

### FN-07 — Doc 11 rendered field count does not match the stated 24-column input

**Severity: MEDIUM**

Doc 11 declares 18 expected fields per card at `11_Rules_Catalog.md:21-25`; its rendered CR headers contain 17 columns in ordinary domains and 18 where `Activation Condition` is present (`:84-87`, `:126-129`), while the requested contract input describes 24 columns. Recommendation: reconcile the contract schema, frontmatter, headers, Excel schema, and validator expectations, then add a mechanical field-count check that distinguishes optional activation fields from mandatory framework and maturity fields.

### FN-08 — Collection verification was unavailable

**Severity: INFO**

The required collection check could not run because `pytest` is not installed in the system interpreter and no usable repository virtual environment was present. The quick script is lint/quality-gate based and does not verify pytest collection. Recommendation: install the declared test dependencies or document the repository's actual collection command so future validators can satisfy the collection-integrity rule.

## §D Verdict

**FAIL** — the contract has strong three-framework coverage and active AI RMF evidence, but fails frozen-ID integrity and direct structural validation, with unresolved maturity-scope and heatmap-alignment findings.

### Finding counts

- HIGH: 4
- MEDIUM: 3
- LOW: 1
- INFO: 1
- Total: 9

Most important non-blocking issue: **FN-03**, because the MIN heatmap makes controls appear GREEN whenever any applicable framework has zero gap, despite being presented as a worst-axis visualization.
