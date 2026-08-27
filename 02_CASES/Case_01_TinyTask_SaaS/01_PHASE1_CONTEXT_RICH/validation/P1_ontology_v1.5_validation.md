# VALIDATION — `phase1_ontology.yaml` v1.5 (Phase D · Doc13 §7)

| Field | Value |
|---|---|
| Validator | VALIDATOR (this session) |
| Date | 2026-08-27 |
| File validated | `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` |
| v1.5 commit | `0a6a533 [EXECUTOR] v1.5: kg_ontology NistControl + NistFramework enum + ALIGNS_TO relation (Phase D - Doc13 §7 NIST CSF/PF/AI-RMF) — Case_01` |
| Prior commit | `c86a082 [EXECUTOR] v1.4 ...` |
| Source-of-truth | `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/Doc13_Adjusted_Goals.md` §7 (lines 411–1442) |
| Reference (no precedent) | `00_METHODOLOGY/diagrams/Class_Models/phase1_contextual_definition.md` |

---

## Block A — Additive diff

`git diff --shortstat HEAD~1 -- .../phase1_ontology.yaml`:

```
1 file changed, 32 insertions(+), 1 deletion(-)
```

### A.1 Expected-vs-found table

| Item | Expected | Found | Pass? |
|---|---|---|---|
| File count changed | 1 | 1 | yes |
| Insertions | 32 | 32 | yes |
| Deletions | 1 (version line) | 1 | yes |
| Removed body lines | 0 | 0 | yes |
| Modified (non-deletion) lines | 0 (additive only) | 0 (only `-` lines are the version bump and 5 added `#` comment-block lines + 7 added `+#` lines; everything else is new `+` line) | yes |
| Version bump | 1.4 → 1.5 | 1.4 → 1.5 | yes |

The diff is purely additive: every changed line is either `+` (new content) or the single `-`/`+` version-line bump. No body value of any prior field was removed, renamed, or rewritten. The diff also adds a v1.5 history block to the file-header preamble, which is consistent with the v1.3 / v1.4 history blocks above it.

### A.2 Schema counts (Python `yaml.safe_load`)

| Bucket | Expected | Found | Pass? |
|---|---|---|---|
| `kg_ontology.classes` | 19 (12 + 6 v1.4 + NistControl) | 19 | yes |
| `kg_ontology.relations` | 27 (14 + 11 v1.4 + 2 v1.5) | 27 | yes |
| `kg_ontology.enums` | 12 (10 + RaciLetter + RiskScore + NistFramework) | 12 | yes |
| `kg_ontology.invariants.counts` | 30 (20 + 7 v1.4 + 3 v1.5) | 30 | yes |
| `kg_ontology.invariants.id_patterns` | 18 (12 + 2 v1.3 + 2 v1.4 + 2 v1.5) | 18 | yes |
| `header.version` | "1.5" | "1.5" | yes |
| `NistControl` in classes | True | True | yes |
| `NistFramework` in enums | True | True | yes |
| `ALIGNS_TO` verb present | True | True | yes |
| `SOURCED_FROM` verb present | True | True | yes |
| `SOURCED_FROM` status `deferred` | True | True | yes |

Every v1.4 / v1.3 / v1.2 / v1.0 entry verified unchanged (Python dict-key membership test plus the diff confirms no removed keys).

### A.3 Reference-doc check (P5)

`grep -l 'NistControl' 00_METHODOLOGY/diagrams/Class_Models/phase1_contextual_definition.md` → not found. Confirmed: the NistControl class does NOT belong in the methodology-level Class_Models — it is correctly classified as case-level, with `source` annotated `Class_Models has no precedent — case-level`. Honors P5 (no upward bleeding of case artefacts).

---

## Block B — Citation verification

### B.1 `NistControl` attrs vs Doc13 §7 table headers

Doc13 §7 sub-section header for the first table (§7.1.1, line 423):

```
| Function | Control ID | Description (1-liner) | Path |
```

Ontology `NistControl.attrs` (line ~1426 of yaml):

```yaml
attrs: { id: NIST-*, control_id, framework, function,
         description, path }
```

| Doc13 column | Ontology attr | Match? |
|---|---|---|
| `Control ID` | `control_id` | yes |
| `Function` | `function` | yes |
| `Description (1-liner)` | `description` | yes |
| `Path` | `path` | yes |
| — (extra) | `id` (NIST-*) | introduces the internal prefixed form (see §7.2 below) |
| — (extra) | `framework` | implicit in Doc13 (subsection heading `§7.X.1 NIST CSF 2.0` / `§7.X.2 NIST PF 1.0` / `§7.X.3 NIST AI RMF`); making it an explicit column is an honest schema upgrade, not a fabrication |

**Honest citation.**

### B.2 `NistControl.data_source` cites `Doc13 §7 (lines 411–1442)`

Verified: Doc13 line 411 is the `## §7 NIST Controls Mapping` heading; line 1442 is the last line before `## §8 Cross-References` (line 1443). Range is exact. **Honest citation.**

### B.3 `ALIGNS_TO` direction and citation

```yaml
- { verb: ALIGNS_TO, from: SecurityControlDomain, to: NistControl,
    cardinality: "N:N ...",
    source: "Doc13 §7 per-sub-domain NIST tables; Class_Models has no precedent" }
```

- **Direction**: `SecurityControlDomain → NistControl`. Verified semantically: Doc13 §7 organises NIST tables PER sub-domain (e.g. `§7.13 D-04.2 — Incident Containment & Response` heading on line 777; `§7.13.1 NIST CSF 2.0 controls`, `§7.13.2 NIST PF 1.0 controls`, `§7.13.3 NIST AI RMF controls` on lines 781/797/811). Each sub-domain's table is the data source. The sub-domain is the "host" of the alignment rows, so `from: SecurityControlDomain, to: NistControl` is the correct reading.
- **Cardinality N:N**: well-formed (one sub-domain lists many controls, one control is cited in many sub-domains — e.g. `PR.DS-01` recurs 6× across §7.1, §7.2, §7.3, §7.4, §7.13, etc.).
- **`SecurityControlDomain` exists as a class**: confirmed in `kg_ontology.classes.SecurityControlDomain` (attrs include `id: String /* D-XX.Y */`, matches `id_patterns: ^D-\d{2}\.\d{1}$`). No dangling reference.
- **`NistControl` exists**: confirmed.
- **Honest citation.**

### B.4 `SOURCED_FROM` marked `status: deferred`

```yaml
- { verb: SOURCED_FROM, from: NistControl, to: NistControl,
    cardinality: "N:0..1 (only when a control is in both CSF and PF — same id reused)",
    status: "deferred" }
```

`status: deferred` is present. The relation is internal (`from: NistControl, to: NistControl`) — it is a placeholder for when a control ID would need to link two framework-specific instances. No PF/CSF ID collisions exist today in Doc13 §7 (PF IDs end in `-P<n>`; CSF IDs use bare `-<n>`), so the deferred flag is appropriate. **Honest (and properly scoped).**

### B.5 `NistFramework` enum

```yaml
NistFramework: [CSF, PF, AI-RMF]
```

Verified: Doc13 §7 contains exactly three framework headings, repeated per sub-domain:
- `#### §7.X.1 NIST CSF 2.0 controls` — 35 sub-domains
- `#### §7.X.2 NIST PF 1.0 controls` — 35 sub-domains
- `#### §7.X.3 NIST AI RMF controls` — 1 sub-domain (only §7.13.3, line 811)

No other framework appears in §7. Enum is complete and minimal. **Honest citation.**

### B.6 `id_patterns.NistControl` regex

```yaml
NistControl: "^(NIST-)?[A-Z\\.\\-]+$"
```

Tested against all 110 distinct control IDs harvested from Doc13 §7:

| Sample | `NistControl` match | `NistControlSafe` match (prefixed) |
|---|---|---|
| `PR.DS-01` | **False** | `NIST-PR.DS-01` → True |
| `PR.DS-P2` | **False** | `NIST-PR.DS-P2` → True |
| `MANAGE-2.1` | **False** | `NIST-MANAGE-2.1` → True |
| `GV.RM-04` | **False** | `NIST-GV.RM-04` → True |
| `CT.DP-P4` | **False** | `NIST-CT.DP-P4` → True |
| 110/110 distinct IDs harvested from Doc13 | **0/110 match** | **110/110 match** |

**FINDING (Block B.6 — TYPO)**: `NistControl` is missing the digit class. The character class `[A-Z\.\-]+` excludes `0-9`, but every NIST control ID in Doc13 §7 contains a digit (`PR.DS-01`, `MANAGE-2.1`, `PR.DS-P2`, etc.). The Executor's own illustrative example `NIST-PR.DS-01` would also fail the unprefixed form because of `0` in `01`. The companion `NistControlSafe` pattern (which uses `[A-Za-z0-9._-]`) is correct. This is a regex typo — should be `^(NIST-)?[A-Z0-9\.\-]+$` (add `0-9` to the character class). It does NOT break schema parsing (the YAML is valid) and the regex is not currently executed against live data (it is a validator constraint, not a runtime check), so the typo is latent. **Recommendation: patch before any enforcement code consumes this pattern.**

### B.7 `id_patterns.NistControlSafe` regex

```yaml
NistControlSafe: "^NIST-[A-Za-z0-9._-]{1,80}$"
```

- Prefix `NIST-` mandatory ✓
- Character class allows uppercase, lowercase, digits, dot, underscore, dash ✓
- Length 1–80 ✓
- Tested: matches all 110 distinct IDs when prefixed (`NIST-PR.DS-01`, `NIST-MANAGE-2.1`, etc.). **Honest and correct.**

---

## Block C — Counts vs Doc13 §7 ground truth

Re-extracted §7 (lines 412–1442) directly:

| Bucket | Executor claim | My re-extraction | Notes |
|---|---|---|---|
| `nist_controls` | 117 = 77 CSF + 38 PF + 2 AI-RMF | **117** (77 CSF incl. malformed + 38 PF + 2 AI-RMF) | matches when malformed `Function=?` rows are included; initial naive parser (well-formed only) gave 70 — the 7 distinct malformed IDs (RS.CO-04, PR.AT-03, PR.AT-04, ID.SC-04, PR.IP-06, PR.PT-01, PR.IP-07) bridge the gap. **Honest.** |
| `nist_alignments` | 513 | **513** (245 CSF + 266 PF + 2 AI-RMF) | matches exactly. |
| `nist_aimrm_subdomains` | 1 | 1 | only `§7.13.3 NIST AI RMF controls` (under `§7.13 D-04.2`) exists. AI-RMF IDs are `MANAGE-2.1`, `MANAGE-2.3` — both in D-04.2. **Honest.** |

### C.1 Malformed rows sanity (ground-truth drift)

Confirmed: 8 rows with `Function | ?` in Doc13 §7 (lines 829, 1038, 1194, 1195, 1256, 1372, 1374, 1409). This matches the ground-truth extraction note. **Not an ontology defect** — they are pre-existing Doc13 drift findings, and the ontology correctly counts them as part of `nist_alignments` and `nist_controls` (otherwise distinct CSF would be 70, not 77).

---

## Top 3 findings

1. **Block B.6 — `id_patterns.NistControl` regex typo (latent bug)**: the character class `[A-Z\.\-]+` excludes digits, so it matches **0 of 110** distinct NIST control IDs harvested from Doc13 §7. Should be `[A-Z0-9\.\-]+`. The sibling pattern `NistControlSafe` is correct. Severity: **low** (does not break YAML parsing; only affects future regex-based validators); recommend Executor patch in a follow-up v1.5.1.

2. **Block A.1 — version-line deletion**: the diff shows the line `-  version: "1.4"` removed and `+  version: "1.5"` added. This is the expected version-bump semantics and is consistent with v1.2 → v1.3 → v1.4 → v1.5 history. Not a defect.

3. **Block C.1 — alignment count depends on including 8 malformed rows**: `nist_alignments: 513` is correct ONLY if the 8 `Function=?` rows in Doc13 §7 are counted. They are real rows in the source doc and the ontology correctly counts them. **No defect in the ontology**, but the methodology should flag the 8 drift rows so the next Doc13 revision does not silently shift this invariant. (This is a doc drift, not an ontology drift.)

---

## Verdict

**CONDITIONAL PASS** — with one actionable follow-up.

The v1.5 extension is **purely additive** (32 insertions, 1 version-line deletion, zero body mutations), schema-consistent (all expected counts hit exactly), semantically aligned with Doc13 §7 (sub-domain as host of per-framework tables; NistFramework enum is minimal and complete), and every count (117 controls / 513 alignments / 1 AI-RMF sub-domain) reconciles against a direct re-extraction of Doc13 §7.

The only defect is a regex typo in `id_patterns.NistControl` that would reject every real control ID in Doc13 §7. This is **latent** (no consumer code reads the pattern today; the YAML is still valid), so the ontology can be accepted as-is, but Executor should patch in v1.5.1:

```yaml
-      NistControl: "^(NIST-)?[A-Z\\.\\-]+$"
+      NistControl: "^(NIST-)?[A-Z0-9\\.\\-]+$"
```

All other blocks are clean.

---

## Update 2026-08-27 — v1.6 (regex fix applied)

The orchestrator applied the v1.5.1 patch inline:

```yaml
-      NistControl: "^(NIST-)?[A-Z\.\-]+$"
+      NistControl: "^(NIST-)?[A-Z0-9\.\-]+$"
```

Bumped the file version to `1.6`. Spot-test (Python `re.match`):

| Test ID | Pattern match |
|---|---|
| `PR.DS-01` | True |
| `NIST-PR.DS-01` | True |
| `MANAGE-2.1` | True |
| `NIST-MANAGE-2.1` | True |
| `ID.AM-08` | True |
| `NIST-ID.AM-08` | True |
| `GV.OV-03` | True |
| `CT.DP-P4` | True |

All 8 representative control-ID formats now match. The DEFECT of the previous round is closed.

**Updated verdict: PASS.**

---

## Files touched

- `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/validation/P1_ontology_v1.5_validation.md` (this report, new file; amended)
- `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml` (regex typo fixed → v1.6)
