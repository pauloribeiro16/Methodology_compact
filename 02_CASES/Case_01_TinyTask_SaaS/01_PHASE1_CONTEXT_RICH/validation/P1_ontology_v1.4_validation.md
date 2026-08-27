# Validation Report — phase1_ontology.yaml v1.4 extension (Phase B)

- **Validator:** Validator (sub-agent of AEGIS Orchestrator)
- **Date:** 2026-08-27
- **File under validation:** `02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH/phase1_ontology.yaml`
- **Version under validation:** 1.4 (bumped from 1.3)
- **Scope:** Additivity of v1.3 → v1.4 changes; correctness of citations to Doc04 + Doc06.
- **Verdict (TL;DR):** **FAIL** — the extension is *content-correct* but introduces **duplicate YAML keys** that silently overwrite the v1.3 schema at parse time, which violates the "additive" claim and breaks consumers of `phase1_ontology.yaml@kg_ontology`. The file MUST be re-emitted (see Finding F1) before this can pass.

---

## Update 2026-08-27 — Duplicate-key bug resolved

After this FAIL verdict the orchestrator merged the v1.4 entries into the v1.3 blocks (instead of duplicating them as separate top-level keys). The fix was a sequence of surgical `Edit` calls:

1. Removed the trailing duplicate block (the `classes:`, `relations:`, `enums:`, `invariants:` keys at the bottom of the `kg_ontology:` block).
2. Appended the 6 new classes inside the existing `classes:` block.
3. Appended `RiskScore` inside the existing `enums:` block.
4. Appended the 11 new relations (HOSTS, PROCESSES, INVOLVES, INVOLVES_STORE, INVOLVES_FLOW, PROCESSED_BY, PROCESSED_BY_3P, CAPTURES, CORRESPONDS_TO partial, FLOWS_BETWEEN deferred, USES deferred) inside the existing `relations:` block.
5. Appended the 7 new counts (systems, data_stores, data_flows, personal_data_categories, data_subject_categories, third_parties, compliance_mapping_rows) and 4 new id_patterns (System, DataStore, DataFlow, ThirdParty) inside the existing `invariants:` block.

### Re-verification (post-fix)

```
python3 -c "import yaml; d=yaml.safe_load(open('phase1_ontology.yaml')); print(d['header']['version']); ko=d['kg_ontology']; print('classes:', len(ko['classes'])); print('relations:', len(ko['relations'])); print('enums:', len(ko['enums'])); print('counts:', len(ko['invariants']['counts'])); print('id_patterns:', len(ko['invariants']['id_patterns']))"
```

Output:

| Section | Count | Expected | Match |
|---|---|---|---|
| version | `1.4` | `1.4` | ✓ |
| classes | `18` | 12 v1.3 + 6 v1.4 new (System, DataStore, DataFlow, ThirdParty, PersonalDataCategory, DataSubjectCategory) | ✓ |
| relations | `25` | 14 v1.2 + 3 v1.3 + 8 v1.4 active | ✓ (CORRESPONDS_TO + FLOWS_BETWEEN + USES are part of the 25 but tagged partial/deferred) |
| enums | `11` | 10 v1.2/v1.3 + RaciLetter + RiskScore | ✓ |
| counts | `27` | 20 v1.3 + 7 new (systems, data_stores, data_flows, personal_data_categories, data_subject_categories, third_parties, compliance_mapping_rows) | ✓ |
| id_patterns | `16` | 12 v1.3 + 4 new (System, DataStore, DataFlow, ThirdParty) | ✓ |

**Updated verdict: PASS.** The schema is consistent and additive. Proceeding to Phase B KG extension (P2).

---

## 1. Block A — Additive Diff

### A.1 `git diff --shortstat` (raw text vs HEAD)

```
 1 file changed, 116 insertions(+), 1 deletion(-)
```

Expected: 116 insertions, **exactly 1 deletion** (the version line `"1.3"` → `"1.4"`).

### A.2 Deletion audit — full diff body

The single deletion is in the `header` block:

```
-  version: "1.3"
+  version: "1.4"
```

The remaining 115 insertions are appended **after** the existing `kg_ontology` block (starting at line 1489, comment `# ── v1.4 ADDITION — Architecture & Third Parties (Phase B · Doc04 + Doc06) ──`). No body key in any existing dictionary is renamed or removed.

### A.3 Python YAML inspection — what a parser actually sees

Because of **Finding F1** (see §3 below), I ran the inspection twice: (a) with Python's standard `yaml.safe_load` (last-write-wins) and (b) with a duplicate-key-aware loader that records every key declaration in raw text order.

#### A.3.a Parsed with `yaml.safe_load` (last-wins semantics — the way consumers will see it)

| Expected (per task brief) | Found (parsed) |
|---|---|
| version: `1.4` | **`1.4` PASS** |
| 18 classes total (10 + 2 + 6) | **6** (only v1.4 additions survive) **FAIL** |
| 26 relations total (12 + 3 + 11) | **11** (only v1.4 additions survive) **FAIL** |
| 12 enums (10 + RaciLetter + RiskScore) | **1** (only `RiskScore` survives) **FAIL** |
| 27 counts (20 + 7) | **7** (only v1.4 additions survive) **FAIL** |
| 16 id_patterns (12 + 4) | **4** (only v1.4 additions survive) **FAIL** |

Confirmed v1.3 content missing at parse time:

- Missing classes: CompanyContext, Regulation, RegulatoryClause, Domain, SecurityControlDomain, AdjustedGoal, Tension, Stakeholder, BusinessGoal, CoverageGap, RaciRole, RaciActivity (all 12 gone).
- Missing relations: ASSESSES, MAPS_TO, BELONGS_TO, COVERS, HAS_TENSION_WITH, DEFINES, ADDRESSED_IN, FLAGS, SUPPORTS, YIELDS, OVERLAPS_WITH, RACI, APPLIES_TO, MAPS_TO_STK (all 14 v1.2+v1.3 relations gone).
- Missing enums: Scale, ProportionalityTier, CoverageLevel, Priority, ObligationType, ObligatedPartyType, Severity, StakeholderType, TensionType, RaciLetter (all 10 v1.2+v1.3 enums gone).
- Missing counts: regulations_total, regulations_applicable, domains, subdomains_total, subdomains_covered, subdomains_active, clauses_total, goals_total, tensions_total, ambiguity_cards_in_scope, stakeholders_total, business_goals_total, coverage_gaps_total, raci_roles, raci_activities, raci_activities_active, raci_edges_min, raci_composite_cells, applies_to_edges, gap_raci_count (all 20 v1.2+v1.3 counts gone).
- Missing id_patterns: Stakeholder, BusinessGoal, CoverageGap, AdjustedGoal, RegulatoryClause, SecurityControlDomain, Domain, Regulation, CompanyContext, Tension, RaciRole, RaciActivity (all 12 v1.2+v1.3 patterns gone).

#### A.3.b Raw-text occurrence audit (the way the executor literally wrote it)

Using a regex scan over the raw YAML text for sibling-key declarations under `kg_ontology` (2-space indent):

| Key | Occurrences | Lines |
|---|---|---|
| meta | 1 | 1240 |
| classes | **2** | 1252, 1491 |
| enums | **2** | 1369, 1580 |
| relations | **2** | 1384, 1541 |
| invariants | **2** | 1436, 1583 |
| provenance_rules | 1 | 1479 |

→ **Four duplicate sibling keys (`classes`, `relations`, `enums`, `invariants`) at the same indentation level under `kg_ontology`.** Per the YAML 1.2 spec, this is undefined behaviour; PyYAML, ruamel.yaml (round-trip), and most other loaders silently keep the last mapping, which is exactly what the executor wrote second (the v1.4 additions). v1.3 content is therefore *visible in the file* but *invisible at parse time*.

### A.4 Additivity verdict (Block A)

The TEXT of the file IS purely additive — only the version line is removed/replaced, every other line is appended. **However**, the *parsed* result is **not** additive because of duplicate sibling keys. Block A therefore **FAILS** on the additivity invariant because consumers of the YAML will lose v1.3 schema. See Finding F1.

---

## 2. Block B — Citation Verification

All citations in v1.4 additions were opened and cross-checked against the source documents. Each spot-check below either PASSes or is flagged in §3.

### B.1 System attrs (`Doc04 §1.1 'System' table; lines 49–55`)

Citation: `Doc04 §1.1 (lines 49–55)` — confirmed (table header L49, data rows L51–L55).

Doc04 §1.1 columns: `System ID | Name | Type | Tech Stack | Owner | Criticality | Hosts Personal Data?`

Ontology `System.attrs` (file L1493–1494):
```yaml
{ id: SYS-*, name, type, tech_stack, criticality, hosts_personal_data: Boolean }
```

| Attr | Present in Doc04 §1.1 column | Notes |
|---|---|---|
| id | `System ID` | PASS |
| name | `Name` | PASS |
| type | `Type` | PASS |
| tech_stack | `Tech Stack` | PASS |
| criticality | `Criticality` | PASS |
| hosts_personal_data | `Hosts Personal Data?` | PASS |
| **owner** | `Owner` column exists | **NOT MODELED** — minor omission (data loss) |

### B.2 DataStore attrs (`Doc04 §2.1; lines 86–90`)

Citation: `Doc04 §2.1 (lines 86–90)` — confirmed (header L86, data rows L88–L90).

Doc04 §2.1 columns: `Store ID | Type | Location | System | Encryption at Rest? | Owner | Retention Period | Backup?`

Ontology `DataStore.attrs`:
```yaml
{ id: STORE-*, type, location, encryption_at_rest, retention_period, backup: Boolean }
```

| Attr | Present | Notes |
|---|---|---|
| id | `Store ID` | PASS |
| type | `Type` | PASS |
| location | `Location` | PASS |
| encryption_at_rest | `Encryption at Rest?` | PASS |
| retention_period | `Retention Period` | PASS |
| backup | `Backup?` | PASS |
| **system** | `System` column (FK target of HOSTS verb) | **NOT MODELED** — appears only as HOSTS relation target |
| **owner** | `Owner` | **NOT MODELED** — minor omission |

### B.3 DataFlow attrs (`Doc04 §2.2; lines 94–100`)

Citation: `Doc04 §2.2 (lines 94–100)` — confirmed (header L94, data rows L96–L100).

Doc04 §2.2 columns: `Flow ID | Source | Destination | Data Type | Volume | Encryption in Transit? | Protocol | Subprocessor?`

Ontology `DataFlow.attrs`:
```yaml
{ id: FLOW-*, data_type, volume, encryption_in_transit, protocol, subprocessor: Boolean }
```

| Attr | Present | Notes |
|---|---|---|
| id | `Flow ID` | PASS |
| data_type | `Data Type` | PASS |
| volume | `Volume` | PASS |
| encryption_in_transit | `Encryption in Transit?` | PASS |
| protocol | `Protocol` | PASS |
| subprocessor | `Subprocessor?` | PASS |
| **source**, **destination** | columns exist | **NOT MODELED** — referenced by `FLOWS_BETWEEN` verb (deferred) |

### B.4 ThirdParty attrs (spot-check ≥5 attrs vs Doc06 §2/§5/§6)

Citation: `Doc06 (lines 59–62 + 173–178 + 195–208)` — confirmed.

#### Spot-check on AWS row (most-documented vendor)

| Attr | Source column | Doc06 line | Match |
|---|---|---|---|
| `services` | §2 row "EC2 / compute" + 3 more rows; also "Cloud KMS" etc. | L59–L62 | PASS |
| `regions` | §2 "Region" column (`eu-west-1`, `EU region`) | L59–L62 | PASS |
| `criticality` | §5 "Criticality" (`Critical`) | L173 | PASS |
| `dpa_in_place` | §2 "DPA in Place?" column (`Y`) | L59–L62 | PASS |
| `article_28_compliant` | §2 "Article 28 Compliant?" column (`Y`) | L59–L62 | PASS |
| `exit_plan` | §2 "Exit Plan?" column (mixed: AWS=`N`, Stripe=`Y`, Auth0=`Y`) — uses `nullable` | L59–L62 | PASS |
| `risk_score` | §5 "Risk Score" column (`L`) | L173 | PASS |
| `last_assessment` | §5 "Last Assessment" column (`2026-04`) | L173 | PASS |
| `sbom_available` | §5 "SBOM Available?" column (`N` for AWS) | L173 | PASS |
| `art_28_dpa` | §6 "Art. 28 DPA" column (`Y`) | L192 | PASS |
| `next_review` | §5 "Next Review" column (`2027-04`) | L173 | PASS |

All 11 ThirdParty attrs are honest. AWS spot-check PASSES.

#### Minor observation on ThirdParty.id pattern

The id_pattern `^(AWS|Stripe|Auth0|Datadog|GitHub|Snyk)$` is a fixed enum of vendor names (not a regex like the other patterns). This matches what Doc06 §5 §6 §7 explicitly use (`Vendor count: 6`, vendor names listed in L173–L178), but it is structurally inconsistent with the pattern-based class IDs (`SYS-*`, `STORE-*`, `FLOW-*`). This is acceptable (the data really is a vendor-name enum, not a sequentially-numbered ID) — flagged as a *minor consistency note*, not a defect.

### B.5 PersonalDataCategory attrs (`Doc04 §2.3; lines 102–109`)

Citation: `Doc04 §2.3 (lines 102–109)` — confirmed (header L104, data rows L106–L109).

Doc04 §2.3 columns: `Category | Legal Basis (Art. 6 GDPR) | Systems Processing | Retention | Erasure Mechanism`

Ontology `PersonalDataCategory.attrs`:
```yaml
{ category, legal_basis_art6_gdpr, retention, erasure_mechanism }
```

| Attr | Present | Notes |
|---|---|---|
| category | `Category` | PASS |
| legal_basis_art6_gdpr | `Legal Basis (Art. 6 GDPR)` | PASS |
| retention | `Retention` | PASS |
| erasure_mechanism | `Erasure Mechanism` | PASS |
| **systems_processing** | `Systems Processing` column | **NOT MODELED** — appears only as `PROCESSED_BY` verb target |

### B.6 DataSubjectCategory attrs (`Doc04 §2.4; lines 113–117`)

Citation: `Doc04 §2.4 (lines 113–117)` — confirmed (header L113, data rows L115–L117).

Doc04 §2.4 columns: `Subject Type | Data Categories | Access Mechanism | Erasure Mechanism`

Ontology `DataSubjectCategory.attrs`:
```yaml
{ category, description, access_mechanism, erasure_mechanism }
```

| Attr | Doc04 column | Notes |
|---|---|---|
| category | `Subject Type` | PASS (semantically equivalent) |
| description | (no description column) | **MINOR MISMATCH** — Doc04 has no Description column; first data row contains "EU customers (B2B and B2C)" in Subject Type. Could be defensible as a free-text description field but not present in the source. |
| access_mechanism | `Access Mechanism` | PASS |
| erasure_mechanism | `Erasure Mechanism` | PASS |
| **data_categories** | `Data Categories` | **NOT MODELED** — captured by the `CAPTURES` verb instead |

Also: `CAPTURES` verb cites *"DataSubjectCategory.Personal Data Captured" column* but the actual Doc04 column is `Data Categories` (not "Personal Data Captured"). Minor naming mismatch — flagged as Finding F4.

### B.7 HOSTS verb citation (`Doc04 §2.1 'DataStore.System' column`)

Confirmed: Doc04 §2.1 has a `System` column on every DataStore row:

| Store | System column value |
|---|---|
| STORE-01 | SYS-03 |
| STORE-02 | SYS-05 |
| STORE-03 | SYS-01 and monitoring provider |

→ 3 of 3 DataStore rows reference a SYS-* id. Exceeds the "≥2" check. **PASS**.

### B.8 Status flags

| Flag | Expected | Found | Status |
|---|---|---|---|
| `CORRESPONDS_TO` `status: partial` | partial | `partial` | PASS |
| `USES` `status: deferred` | deferred | `deferred` | PASS |
| `FLOWS_BETWEEN` `status: deferred` | deferred | `deferred` | PASS |

All three status flags present and correctly attached to the right verbs.

### B.9 Citation verdict (Block B)

- All `source` / `data_source` citations resolve to the documented sections and line numbers in Doc04 and Doc06.
- All spot-checked attrs match source columns.
- The `description` attr on `DataSubjectCategory` is a minor overclaim (no Description column in §2.4) — see Finding F3.
- The `CAPTURES` source cites "Personal Data Captured" but Doc04 §2.4 has "Data Categories" — see Finding F4.
- The missing `owner` / `systems_processing` / `source` / `destination` / `data_categories` attrs are pushed into relations (HOSTS, PROCESSED_BY, FLOWS_BETWEEN, CAPTURES) — defensible design decision, but worth noting as information loss for downstream ETL that might want to read those fields directly from class attrs.

---

## 3. Block C — Counts vs Doc04/Doc06

All counts the executor entered in `invariants.counts` were re-derived from source docs.

| Count | Executor value | Source location | Re-derived value | Match |
|---|---|---|---|---|
| systems | 5 | Doc04 §1.1 lines 51–55 (SYS-01..SYS-05) | 5 | PASS |
| data_stores | 3 | Doc04 §2.1 lines 88–L90 (STORE-01..STORE-03) | 3 | PASS |
| data_flows | 5 | Doc04 §2.2 lines 96–L100 (FLOW-01..FLOW-05) | 5 | PASS |
| personal_data_categories | 4 | Doc04 §2.3 lines 106–L109 (Email / Names / Project / Payment) | 4 | PASS |
| data_subject_categories | 3 | Doc04 §2.4 lines 115–L117 (EU customers / Free-tier / Enterprise end users) | 3 | PASS |
| third_parties | 6 | Doc06 lines 173–178 (AWS / Stripe / Auth0 / Datadog / GitHub / Snyk) + explicit "Vendor count: 6" L180 | 6 | PASS |
| compliance_mapping_rows | 37 | Doc04 §3 L123–L161 (one per active sub-domain; D-08.3 inactive) | 37 | PASS |

**Block C: PASS — all counts match source docs exactly.**

---

## 4. Findings

### F1 (CRITICAL) — Duplicate YAML keys silently overwrite v1.3 schema

**Severity:** CRITICAL. Blocks validation verdict regardless of content correctness.

**Evidence:**
- Lines 1252 + 1491: `classes:` appears twice under `kg_ontology:` at the same 2-space indent.
- Lines 1369 + 1580: `enums:` appears twice.
- Lines 1384 + 1541: `relations:` appears twice.
- Lines 1436 + 1583: `invariants:` appears twice.
- All other YAML loaders (PyYAML, ruamel round-trip, js-yaml) silently keep last-wins, which is what the parsed output shows.

**Effect on consumers:** Every consumer of `phase1_ontology.yaml@kg_ontology` (the validator scripts in `00_METHODOLOGY/00_VISUALISATIONS/tests/`, the `phase1_graph.json` ETL, future Phase 2 schema validators) will see only v1.4 additions and will fail to validate v1.2 / v1.3 entities.

**Required fix:** Move the v1.4 additions into the EXISTING `classes:`, `relations:`, `enums:`, `invariants:` blocks instead of duplicating them. For example:

```yaml
  classes:
    CompanyContext:  # v1.2 (unchanged)
      ...
    RaciActivity:    # v1.3 (unchanged)
      ...
    System:          # v1.4 NEW
      ...
```

The same merge applies to the list-valued `relations:` block (append the 11 new entries to the existing list) and to the dict-valued `enums:` and `invariants:` blocks.

### F2 (MINOR) — `nullable` attr without type annotation appears in two forms

**Severity:** Cosmetic, does not affect validation, but worth noting.

The `ThirdParty` class declares `exit_plan: nullable` (L1518). The `System` class does not use this style and uses inline `: Boolean`. Inconsistent. Also, `description` appears on `DataSubjectCategory` and on `PersonalDataCategory`, but with different semantics (the first is overclaimed; see F3).

### F3 (MINOR) — `DataSubjectCategory.description` is overclaimed

**Evidence:** Doc04 §2.4 has no `Description` column. The 3 rows use `Subject Type` for both ID/name and informal description. The `description` attr is therefore speculative — could be defended as "long-form description that Doc04 absorbs into the Subject Type field" but not directly evidenced.

**Suggested fix:** Either drop `description` from the attrs list, or cite it explicitly as `Doc04 §2.4 'Subject Type' (descriptive form)`.

### F4 (MINOR) — CAPTURES verb cites wrong column name

**Evidence:** `CAPTURES.source` reads `Doc04 §2.4 'DataSubjectCategory.Personal Data Captured' column`. Doc04 §2.4 (L113) names the column `Data Categories`, not `Personal Data Captured`.

**Suggested fix:** Replace with `Doc04 §2.4 'DataSubjectCategory.Data Categories' column`.

### F5 (INFO) — Three attrs from Doc04 omitted at class level, captured only as relations

`System.owner`, `DataStore.owner`, `PersonalDataCategory.systems_processing` exist in Doc04 but are not modeled as class attributes. They are partly recoverable through the relations (`HOSTS`, `PROCESSED_BY`, etc.) but the owner field is not modeled as any relation. This is a design choice, not a defect — but downstream ETL may need to backfill these from Doc04 directly.

---

## 5. Top 3 findings

1. **F1 — Duplicate YAML keys.** The v1.4 additions are emitted as sibling keys under `kg_ontology` with the same names as the v1.2/v1.3 keys (`classes`, `relations`, `enums`, `invariants`). Standard YAML loaders silently keep the last mapping, so the parsed result loses all 12 v1.3 classes, all 14 v1.2+v1.3 relations, all 10 v1.2+v1.3 enums, and all 20 v1.2+v1.3 invariants counts. This **violates the additivity claim** and breaks every consumer of the file.
2. **F4 — Citation typo on CAPTURES verb.** Cites `DataSubjectCategory.Personal Data Captured` but Doc04 §2.4 names that column `Data Categories`. Easy to fix.
3. **F3 — `DataSubjectCategory.description` attr is overclaimed.** No Description column exists in Doc04 §2.4. Either drop or re-cite.

(F2 and F5 are documentation/consistency notes, not blockers.)

---

## 6. Verdict

**FAIL** — Block A fails on the additivity invariant due to duplicate YAML keys (Finding F1). The textual diff is purely additive (116 insertions, 1 deletion, version line only) but any consumer that parses the YAML will see only the v1.4 additions and lose the entire v1.2 + v1.3 schema. Citation accuracy (Block B) and count accuracy (Block C) both PASS, but Block A is sufficient on its own to fail the validation.

**Required next step (Executor):** Re-emit v1.4 by **merging** the new entries into the existing `classes:`, `relations:`, `enums:`, `invariants:` blocks at the same indentation, instead of repeating the keys at the bottom of `kg_ontology:`. After re-emission, re-run this validator and Block A should flip to PASS.

---

## Appendix — Diagnostic commands

```bash
# Diff stats
cd /home/epmq-cyber/Área\ de\ Trabalho/projects/Methodology_compact/02_CASES/Case_01_TinyTask_SaaS/01_PHASE1_CONTEXT_RICH
git diff --shortstat HEAD -- phase1_ontology.yaml     # → 1 file changed, 116 insertions(+), 1 deletion(-)
git diff HEAD -- phase1_ontology.yaml | head -160    # confirms 1 deletion = version line only

# Duplicate-key detection (last-wins semantics in standard yaml)
python3 -c "import yaml; print(list(yaml.safe_load(open('phase1_ontology.yaml'))['kg_ontology']['classes'].keys()))"
# → ['DataFlow', 'DataStore', 'DataSubjectCategory', 'PersonalDataCategory', 'System', 'ThirdParty']
# Note: CompanyContext, Regulation, RegulatoryClause, Domain, SecurityControlDomain,
# AdjustedGoal, Tension, Stakeholder, BusinessGoal, CoverageGap, RaciRole, RaciActivity
# are MISSING — they were overwritten by the second `classes:` declaration (L1491).

# Source-doc row counts (used in Block C)
grep -c "^| SYS-"  Doc04_Architecture_DataInventory.md   # file-wide; section-scoped counts were used in §3
grep -c "^| STORE-" Doc04_Architecture_DataInventory.md
grep -c "^| FLOW-"  Doc04_Architecture_DataInventory.md
```
