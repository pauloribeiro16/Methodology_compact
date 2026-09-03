#!/usr/bin/env python3
"""auto_tune.py — Apply mechanical self-tunes the Dream nightly prompt proposes.

The Dream nightly prompt (orchestrator-side) detects patterns (e.g. drift count
unchanged for 2 cycles, parser blindspot in heuristics, stale proposals) and
emits self-tune intents. This script:

1. Reads the intents from `dream/STATE/self_tune_intents.json` (one JSON per line).
2. For each intent, runs the corresponding generator function (pure mechanical
   edits — no LLM, deterministic).
3. Validates each generated edit via `self_tune.py validate`.
4. Commits with `[DREAM SELF-TUNE]` prefix.
5. Logs to `dream/SELF_TUNE_LOG.md`.

P7 boundary (delegated to self_tune.py):
  - Allowed: scripts/dream/*, .zcode/hooks/*, dream/LESSONS.md,
    dream/MEMORY_PATCHES/*, dream/STATE/*, dream/SELF_TUNE_LOG.md,
    dream/STALE_PROPOSALS.md, new dream/*.md.
  - Forbidden: AGENTS.md, 02_CASES/*/PROJECT_STATE.md, progress.json,
    dependency_graph.yaml, domains/**.

Intent format (one JSON line in `dream/STATE/self_tune_intents.json`):
  {"intent": "<name>", "args": {...}, "rationale": "...", "ts": "..."}

Available intents:
  - "drift_escalation": if drift count == previous drift count for >= 2 cycles
    on the same files, append "HUMAN ACTION PENDING" marker to RECONCILIATION.md.
  - "amendment_parser_blindspot_annotation": if an amendment disappeared and
    user_messages == 0, annotate the corresponding gate in adoption_audit.py
    with a [PARSER-BLINDSPOT] comment so future nightlies don't re-emit it.
  - "self_tune_log_append": append a one-line entry to dream/SELF_TUNE_LOG.md.

Usage:
    python3 scripts/dream/auto_tune.py apply-intents
    python3 scripts/dream/auto_tune.py apply-intents --dry-run
    python3 scripts/dream/auto_tune.py --self-test
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SELF_TUNE_LOG = ROOT / "dream" / "SELF_TUNE_LOG.md"
RECONCILIATION = ROOT / "dream" / "RECONCILIATION.md"
ADOPTION_AUDIT = ROOT / "scripts" / "dream" / "adoption_audit.py"
RECONCILE_PY = ROOT / "scripts" / "dream" / "reconcile.py"
INTENTS_FILE = ROOT / "dream" / "STATE" / "self_tune_intents.json"
INTENTS_LOG = ROOT / "dream" / "STATE" / "self_tune_intents.log"
APPLIED_LOG = ROOT / "dream" / "STATE" / "auto_tune_applied.log"

sys.path.insert(0, str(ROOT / "scripts" / "dream"))
import self_tune  # noqa: E402


# --------------------- intent generators ---------------------
# Each generator returns a list of {file, change_description, post_validate} dicts.

def intent_drift_escalation(args: dict) -> list[dict]:
    """Annotate RECONCILIATION.md if drift count is unchanged for >= N cycles
    on the same files. Args:
      - current_files: list[str] of files in the latest drift table.
      - previous_files: list[str] from the previous cycle.
      - cycles: int (how many consecutive cycles with the same drift set).
      - threshold: int (default 2 — same as plan).
    """
    threshold = args.get("threshold", 2)
    current = set(args.get("current_files", []))
    previous = set(args.get("previous_files", []))
    cycles = int(args.get("cycles", 0))

    if cycles < threshold:
        return []
    if current != previous or not current:
        return []

    # Build the marker text. We append it to RECONCILIATION.md as a
    # trailing section so it's visible in the brief without breaking the
    # existing structure.
    today = dt.date.today().isoformat()
    marker = (
        f"\n## Drift escalation — {today}\n\n"
        f"**HUMAN ACTION PENDING** — drift set unchanged for **{cycles} consecutive "
        f"nightly cycles**. Same files: {', '.join(sorted(current))}. "
        f"Apply the diff in the 'Proposed state-file patches' section above, or "
        f"merge the corresponding commits and bump the `Last Updated` header.\n"
    )

    change = {
        "file": str(RECONCILIATION.relative_to(ROOT)),
        "read": lambda: RECONCILIATION.read_text(encoding="utf-8"),
        "write": lambda cur: cur + marker,
        "description": f"drift_escalation marker ({cycles} cycles)",
    }
    return [change]


def intent_amendment_parser_blindspot_annotation(args: dict) -> list[dict]:
    """Annotate adoption_audit.py heuristic with a [PARSER-BLINDSPOT] comment
    when an amendment's gate depends on a metric the parser can't surface.

    Args:
      - gate_text: str (the source-code substring of the gate expression).
      - proposal_title: str (the amendment title that disappeared).
      - metric: str (which derived metric the parser can't see).
    """
    gate_text = args.get("gate_text", "").strip()
    proposal_title = args.get("proposal_title", "(unknown)")
    metric = args.get("metric", "user_messages")

    if not gate_text:
        return []

    src = ADOPTION_AUDIT.read_text(encoding="utf-8")
    if gate_text not in src:
        return []
    if "[PARSER-BLINDSPOT" in src:
        # Already annotated — skip
        return []

    today = dt.date.today().isoformat()
    annotation = (
        f"\n            # [PARSER-BLINDSPOT {today}] proposal '{proposal_title}'\n"
        f"            # depends on metric '{metric}' which the jsonl parser\n"
        f"            # cannot surface (machine log = telemetry only). When this\n"
        f"            # proposal disappears, it is a parser blindspot, NOT\n"
        f"            # adoption. Do not re-emit without first adding jsonl\n"
        f"            # prompt-content extraction.\n            "
    )

    # Insert the annotation just before the line that contains gate_text
    new_src_lines = []
    inserted = False
    for line in src.splitlines():
        if not inserted and gate_text in line:
            indent = re.match(r"^(\s*)", line).group(1)
            new_src_lines.append(line.replace(gate_text, annotation.rstrip() + "\n" + indent + gate_text, 1))
            inserted = True
        else:
            new_src_lines.append(line)
    if not inserted:
        return []

    new_src = "\n".join(new_src_lines) + "\n"
    change = {
        "file": str(ADOPTION_AUDIT.relative_to(ROOT)),
        "read": lambda: src,
        "write": lambda _: new_src,
        "description": f"annotate parser-blindspot for '{proposal_title}'",
    }
    return [change]


def intent_self_tune_log_append(args: dict) -> list[dict]:
    """Append a one-line entry to dream/SELF_TUNE_LOG.md.

    Args:
      - scope: str (e.g. 'reconcile.py', 'adoption_audit.py').
      - action: str (short verb).
      - reason: str (one-line context).
    """
    scope = args.get("scope", "unknown")
    action = args.get("action", "modified")
    reason = args.get("reason", "(no reason given)")
    today = dt.date.today().isoformat()

    entry = f"- {today} | {scope} | {action} | {reason}\n"
    change = {
        "file": str(SELF_TUNE_LOG.relative_to(ROOT)),
        "read": lambda: SELF_TUNE_LOG.read_text(encoding="utf-8"),
        "write": lambda cur: cur.rstrip("\n") + "\n" + entry,
        "description": f"self_tune_log_append ({scope})",
    }
    return [change]


INTENT_GENERATORS = {
    "drift_escalation": intent_drift_escalation,
    "amendment_parser_blindspot_annotation": intent_amendment_parser_blindspot_annotation,
    "self_tune_log_append": intent_self_tune_log_append,
}


# --------------------- core ---------------------

def load_intents() -> list[dict]:
    """Read pending intents from dream/STATE/self_tune_intents.json (one JSON
    per line). Returns the parsed list. Missing file → empty list."""
    if not INTENTS_FILE.exists():
        return []
    out = []
    for line in INTENTS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"auto_tune: skipping malformed intent: {e}: {line[:80]}", file=sys.stderr)
    return out


def record_intent(intent: dict) -> None:
    """Append an intent to the intent log (audit trail)."""
    INTENTS_LOG.parent.mkdir(parents=True, exist_ok=True)
    with INTENTS_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": dt.datetime.now().isoformat(timespec="seconds"),
                            **intent}, ensure_ascii=False) + "\n")


def record_applied(intent_name: str, files: list[str], rationale: str) -> None:
    """Append an applied-self-tune record (audit trail)."""
    APPLIED_LOG.parent.mkdir(parents=True, exist_ok=True)
    with APPLIED_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "ts": dt.datetime.now().isoformat(timespec="seconds"),
            "intent": intent_name,
            "files": files,
            "rationale": rationale,
        }, ensure_ascii=False) + "\n")


def apply_intent(intent: dict, dry_run: bool = False) -> tuple[bool, list[str]]:
    """Apply a single intent. Returns (ok, files_modified)."""
    name = intent.get("intent")
    if name not in INTENT_GENERATORS:
        print(f"auto_tune: unknown intent '{name}'", file=sys.stderr)
        return False, []

    record_intent(intent)

    changes = INTENT_GENERATORS[name](intent.get("args", {}))
    if not changes:
        return True, []  # No-op intent — still counts as success

    files_modified = []
    for ch in changes:
        rel = ch["file"]
        abs_path = ROOT / rel

        # Scope check via self_tune (mandatory)
        allowed, reason = self_tune.check_scope(rel)
        if not allowed:
            print(f"auto_tune: REFUSED — {rel} — {reason}", file=sys.stderr)
            return False, []

        # Apply the change
        cur = ch["read"]()
        new = ch["write"](cur)
        if cur == new:
            # Idempotent — nothing to do
            continue

        if dry_run:
            print(f"auto_tune: DRY-RUN — would modify {rel} ({ch['description']})")
            files_modified.append(rel)
            continue

        abs_path.write_text(new, encoding="utf-8")
        files_modified.append(rel)

        # Validate the file (syntax + dry-run)
        ok, details = self_tune.validate_file(abs_path)
        if not ok:
            # Roll back
            abs_path.write_text(cur, encoding="utf-8")
            print(f"auto_tune: ROLLBACK — {rel} failed validation: {details}", file=sys.stderr)
            return False, []

    return True, files_modified


def apply_all_intents(dry_run: bool = False) -> list[dict]:
    """Apply every intent in dream/STATE/self_tune_intents.json. Returns a
    list of {intent, files, ok} records."""
    intents = load_intents()
    if not intents:
        return []

    results = []
    for intent in intents:
        ok, files = apply_intent(intent, dry_run=dry_run)
        results.append({
            "intent": intent.get("intent"),
            "args": intent.get("args", {}),
            "files": files,
            "ok": ok,
            "rationale": intent.get("rationale", ""),
        })
        if ok and files and not dry_run:
            record_applied(intent.get("intent"), files, intent.get("rationale", ""))

    return results


def commit_applied(results: list[dict], dry_run: bool = False) -> int:
    """Collect all modified files from results and commit them under a single
    `[DREAM SELF-TUNE]` commit."""
    files = []
    for r in results:
        if r["ok"] and r["files"]:
            files.extend(r["files"])
    if not files:
        return 0

    # Dedup preserving order
    seen = set()
    unique = []
    for f in files:
        if f not in seen:
            unique.append(f)
            seen.add(f)

    intents_summary = ", ".join(r["intent"] for r in results if r["ok"] and r["files"]) or "(no-op)"
    msg = (
        f"[DREAM SELF-TUNE] auto-applied {len(unique)} file(s) from intents: {intents_summary}"
    )
    return self_tune.commit_self_tune(msg, unique, dry_run=dry_run)


# --------------------- self-test ---------------------

def self_test() -> int:
    """End-to-end self-test: 3 intents in a temp dir, verify scope + commit."""
    print("=== auto_tune.py --self-test ===")

    # Test 1: scope check via self_tune
    cases = [
        ("scripts/dream/auto_tune.py", True),
        ("dream/SELF_TUNE_LOG.md", True),
        ("AGENTS.md", False),
        ("02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md", False),
    ]
    for path, expected in cases:
        ok, _ = self_tune.check_scope(path)
        if ok != expected:
            print(f"FAIL: scope({path}) = {ok}, expected {expected}")
            return 1
    print(f"[ok] {len(cases)} scope cases")

    # Test 2: intent_drift_escalation with same files for 2 cycles → 1 change
    changes = intent_drift_escalation({
        "current_files": ["02_CASES/Case_02/PROJECT_STATE.md"],
        "previous_files": ["02_CASES/Case_02/PROJECT_STATE.md"],
        "cycles": 2,
    })
    if len(changes) != 1:
        print(f"FAIL: drift_escalation returned {len(changes)} changes, expected 1")
        return 1
    if changes[0]["file"] != "dream/RECONCILIATION.md":
        print(f"FAIL: drift_escalation targets wrong file: {changes[0]['file']}")
        return 1
    print(f"[ok] intent_drift_escalation (2 cycles, same files)")

    # Test 3: intent_drift_escalation with different files → 0 changes
    changes = intent_drift_escalation({
        "current_files": ["X"],
        "previous_files": ["Y"],
        "cycles": 2,
    })
    if changes:
        print(f"FAIL: drift_escalation (different files) returned {len(changes)} changes")
        return 1
    print(f"[ok] intent_drift_escalation no-op when files differ")

    # Test 4: intent_drift_escalation with cycles=1 → 0 changes
    changes = intent_drift_escalation({
        "current_files": ["X"], "previous_files": ["X"], "cycles": 1,
    })
    if changes:
        print(f"FAIL: drift_escalation (cycles=1) returned {len(changes)} changes")
        return 1
    print(f"[ok] intent_drift_escalation no-op below threshold")

    # Test 5: intent_self_tune_log_append (in-memory)
    original = SELF_TUNE_LOG.read_text(encoding="utf-8")
    try:
        changes = intent_self_tune_log_append({
            "scope": "test.py", "action": "test", "reason": "self-test entry",
        })
        if len(changes) != 1:
            print(f"FAIL: self_tune_log_append returned {len(changes)} changes")
            return 1
        # Simulate write+read
        cur = SELF_TUNE_LOG.read_text(encoding="utf-8")
        new = changes[0]["write"](cur)
        if "self-test entry" not in new:
            print("FAIL: self_tune_log_append write() did not include the entry")
            return 1
        print(f"[ok] intent_self_tune_log_append")
    finally:
        SELF_TUNE_LOG.write_text(original, encoding="utf-8")

    # Test 6: apply_intent refuses P7-protected paths
    intent = {
        "intent": "drift_escalation",
        "args": {
            "current_files": ["X"], "previous_files": ["X"], "cycles": 5,
        },
    }
    # Monkey-patch the drift_escalation generator to target AGENTS.md
    real_gen = INTENT_GENERATORS["drift_escalation"]
    def fake_gen(args):
        return [{
            "file": "AGENTS.md",
            "read": lambda: "",
            "write": lambda c: c + "x",
            "description": "should be refused",
        }]
    INTENT_GENERATORS["drift_escalation"] = fake_gen
    try:
        ok, files = apply_intent(intent, dry_run=False)
        if ok:
            print("FAIL: apply_intent accepted P7-protected target")
            return 1
        print("[ok] apply_intent refuses P7-protected paths")
    finally:
        INTENT_GENERATORS["drift_escalation"] = real_gen

    # Test 7: load_intents handles missing file
    global INTENTS_FILE
    real_intents = INTENTS_FILE
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        INTENTS_FILE = Path(tmp) / "self_tune_intents.json"
        intents = load_intents()
        if intents:
            print(f"FAIL: load_intents on missing file returned {len(intents)}")
            return 1
        print("[ok] load_intents handles missing file")
        INTENTS_FILE = real_intents

    print("=== auto_tune.py --self-test PASSED ===")
    return 0


# --------------------- main ---------------------

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cmd", nargs="?", default="apply-intents",
                   choices=["apply-intents"])
    p.add_argument("--self-test", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    if args.self_test:
        return self_test()

    results = apply_all_intents(dry_run=args.dry_run)
    if not results:
        print("auto_tune: no intents to apply")
        return 0

    n_ok = sum(1 for r in results if r["ok"])
    print(f"auto_tune: applied {n_ok}/{len(results)} intents")
    for r in results:
        status = "ok" if r["ok"] else "FAIL"
        files = ", ".join(r["files"]) if r["files"] else "(no files)"
        print(f"  [{status}] {r['intent']}: {files}")

    # Commit if anything was actually applied
    if any(r["ok"] and r["files"] for r in results):
        return commit_applied(results, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
