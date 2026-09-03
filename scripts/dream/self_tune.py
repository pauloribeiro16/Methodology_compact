#!/usr/bin/env python3
"""self_tune.py — Safe auto-edit helper for the Dream nightly.

The Dream nightly may self-edit its own infrastructure
(`scripts/dream/*`, `.zcode/hooks/*`, `dream/*`) but NEVER P7-protected
methodology / state files. This helper enforces that scope and runs
pre-commit validation.

P7 boundary (DO NOT LOOSEN):
  NEVER edit:
    - AGENTS.md, 00_METHODOLOGY/AGENTS.md
    - 02_CASES/*/PROJECT_STATE.md, 02_CASES/GLOBAL_PROJECT_STATE.md
    - 02_CASES/*/progress.json
    - 00_METHODOLOGY/dependency_graph.yaml
    - 00_METHODOLOGY/PREPROCESSING_by_domain/domains/**
    - any other methodology/state file

  MAY edit:
    - scripts/dream/*.py, scripts/dream/*.sh
    - .zcode/hooks/*.sh
    - dream/LESSONS.md, dream/MEMORY_PATCHES/*.md, dream/STATE/*
    - dream/SELF_TUNE_LOG.md, dream/STALE_PROPOSALS.md, and any
      newly created dream/*.md file

Usage (called by the Dream nightly prompt, not by humans):
    python3 scripts/dream/self_tune.py validate <file>
    python3 scripts/dream/self_tune.py check-scope <file>
    python3 scripts/dream/self_tune.py commit --message "<msg>" <files...>
    python3 scripts/dream/self_tune.py --self-test
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

# --- P7-protected scope (deny-list) ---
P7_DENY_PATTERNS = [
    r"(^|/)AGENTS\.md$",
    r"(^|/)00_METHODOLOGY/AGENTS\.md$",
    r"(^|/)02_CASES/.*/PROJECT_STATE\.md$",
    r"(^|/)02_CASES/GLOBAL_PROJECT_STATE\.md$",
    r"(^|/)02_CASES/.*/progress\.json$",
    r"(^|/)00_METHODOLOGY/dependency_graph\.yaml$",
    r"(^|/)00_METHODOLOGY/PREPROCESSING_by_domain/domains/.*",
]

# --- Auto-edit allowed scope (allow-list; takes priority over deny-list) ---
SELF_TUNE_ALLOW_PATTERNS = [
    r"(^|/)scripts/dream/[^/]+\.(py|sh)$",
    r"(^|/)scripts/dream/transcript_lib\.py$",
    r"(^|/)scripts/dream/tests/[^/]+$",
    r"(^|/)\.zcode/hooks/[^/]+\.sh$",
    r"(^|/)dream/LESSONS\.md$",
    r"(^|/)dream/MEMORY_PATCHES/[^/]+\.md$",
    r"(^|/)dream/STATE/[^/]+$",
    r"(^|/)dream/SELF_TUNE_LOG\.md$",
    r"(^|/)dream/STALE_PROPOSALS\.md$",
    r"(^|/)dream/[A-Z][A-Z0-9_]+\.md$",  # new dream/*.md in CAPS
]


def is_p7_protected(rel_path: str) -> bool:
    """True if the path is on the deny-list (P7-protected methodology content)."""
    return any(re.search(p, rel_path) for p in P7_DENY_PATTERNS)


def is_self_tune_allowed(rel_path: str) -> bool:
    """True if the path is on the allow-list (Dream infrastructure)."""
    return any(re.search(p, rel_path) for p in SELF_TUNE_ALLOW_PATTERNS)


def check_scope(rel_path: str) -> tuple[bool, str]:
    """Return (allowed, reason). P7-protected paths are denied even if they
    accidentally match an allow pattern (deny wins)."""
    if is_p7_protected(rel_path):
        return False, f"P7-protected: {rel_path}"
    if not is_self_tune_allowed(rel_path):
        return False, f"outside self-tune allow-list: {rel_path}"
    return True, "ok"


def validate_python(file_path: Path) -> tuple[bool, str]:
    """Run `python3 -m py_compile`. Returns (ok, detail)."""
    try:
        r = subprocess.run(
            [sys.executable, "-m", "py_compile", str(file_path)],
            capture_output=True, text=True, timeout=30,
        )
        if r.returncode == 0:
            return True, "py_compile ok"
        return False, f"py_compile failed: {r.stderr.strip() or r.stdout.strip()}"
    except subprocess.TimeoutExpired:
        return False, "py_compile timeout (30s)"
    except FileNotFoundError as e:
        return False, f"python3 missing: {e}"


def validate_bash(file_path: Path) -> tuple[bool, str]:
    """Run `bash -n`. Returns (ok, detail)."""
    try:
        r = subprocess.run(
            ["bash", "-n", str(file_path)],
            capture_output=True, text=True, timeout=10,
        )
        if r.returncode == 0:
            return True, "bash -n ok"
        return False, f"bash -n failed: {r.stderr.strip() or r.stdout.strip()}"
    except subprocess.TimeoutExpired:
        return False, "bash -n timeout (10s)"
    except FileNotFoundError as e:
        return False, f"bash missing: {e}"


def validate_dry_run(file_path: Path) -> tuple[bool, str]:
    """For Python: run with `--help`. For Bash: source with empty env.

    This catches argparse typos, missing imports, and syntax errors that
    py_compile / bash -n miss.
    """
    if file_path.suffix == ".py":
        try:
            r = subprocess.run(
                [sys.executable, str(file_path), "--help"],
                capture_output=True, text=True, timeout=15,
            )
            # --help typically exits 0; argparse sometimes exits 2 with usage
            # but still prints description → accept either if no traceback
            if r.returncode in (0, 2) and "Traceback" not in r.stderr:
                return True, f"--help ok (rc={r.returncode})"
            return False, f"--help failed (rc={r.returncode}): {r.stderr.strip()[:200]}"
        except subprocess.TimeoutExpired:
            return False, "--help timeout (15s)"
        except FileNotFoundError as e:
            return False, f"python3 missing: {e}"

    if file_path.suffix == ".sh":
        # Smoke: source the script with no args in a subshell. Most scripts
        # either no-op (good) or fail loudly (bad). Catches runtime-only
        # syntax issues that bash -n misses.
        try:
            r = subprocess.run(
                ["bash", "-c", f"set -e; source '{file_path}'; : ok"],
                capture_output=True, text=True, timeout=10,
            )
            if r.returncode == 0:
                return True, "source smoke ok"
            return False, f"source smoke failed: {r.stderr.strip()[:200]}"
        except subprocess.TimeoutExpired:
            return False, "source smoke timeout (10s)"
        except FileNotFoundError as e:
            return False, f"bash missing: {e}"

    return True, "no dry-run needed (non-script file)"


def validate_file(file_path: Path) -> tuple[bool, list[str]]:
    """Run all applicable validators. Returns (all_ok, [detail_lines])."""
    rel = str(file_path.relative_to(ROOT)) if file_path.is_absolute() else str(file_path)
    in_scope, scope_reason = check_scope(rel)
    details = [f"scope: {scope_reason}"]
    if not in_scope:
        return False, details

    suffix = file_path.suffix
    if suffix == ".py":
        ok, msg = validate_python(file_path)
        details.append(f"py_compile: {msg}")
        if not ok:
            return False, details
        ok, msg = validate_dry_run(file_path)
        details.append(f"dry_run: {msg}")
        if not ok:
            return False, details
    elif suffix == ".sh":
        ok, msg = validate_bash(file_path)
        details.append(f"bash -n: {msg}")
        if not ok:
            return False, details
        ok, msg = validate_dry_run(file_path)
        details.append(f"dry_run: {msg}")
        if not ok:
            return False, details

    return True, details


def git_diff_scope(file_paths: list[str]) -> tuple[bool, str]:
    """Verify each path is within the self-tune allow-list. Returns
    (ok, message). Caller is responsible for actually running `git diff`.
    """
    for fp in file_paths:
        allowed, reason = check_scope(fp)
        if not allowed:
            return False, f"OUT-OF-SCOPE: {fp} — {reason}"
    return True, "all paths in scope"


def commit_self_tune(message: str, file_paths: list[str], dry_run: bool = False) -> int:
    """Stage and commit with `[DREAM SELF-TUNE]` prefix. Returns git exit code."""
    allowed, reason = git_diff_scope(file_paths)
    if not allowed:
        print(f"self_tune.commit: REFUSED — {reason}", file=sys.stderr)
        return 2

    if not message.startswith("[DREAM SELF-TUNE]"):
        print(f"self_tune.commit: REFUSED — message must start with '[DREAM SELF-TUNE]' "
              f"(got: {message[:50]!r})", file=sys.stderr)
        return 2

    if dry_run:
        print(f"self_tune.commit: DRY-RUN — would commit {len(file_paths)} file(s) "
              f"with message: {message[:80]!r}")
        for fp in file_paths:
            print(f"  - {fp}")
        return 0

    try:
        subprocess.run(["git", "add", *file_paths], cwd=ROOT, check=True,
                       capture_output=True, text=True)
        r = subprocess.run(
            ["git", "commit", "-m", message],
            cwd=ROOT, capture_output=True, text=True,
        )
        if r.returncode == 0:
            sha_line = [ln for ln in r.stdout.splitlines() if ln.startswith("[")]
            print(f"self_tune.commit: OK — {sha_line[0] if sha_line else 'committed'}")
            return 0
        print(f"self_tune.commit: git commit failed (rc={r.returncode}): "
              f"{r.stderr.strip()[:300]}", file=sys.stderr)
        return r.returncode
    except subprocess.CalledProcessError as e:
        print(f"self_tune.commit: git add failed: {e.stderr or e}", file=sys.stderr)
        return e.returncode or 1


# --------------------- self-test ---------------------

def self_test() -> int:
    """End-to-end self-test: scope, validators, commit (dry-run)."""
    print("=== self_tune.py --self-test ===")

    # 1. Scope: allow-list matches Dream infra files
    allowed_cases = [
        "scripts/dream/adoption_audit.py",
        "scripts/dream/reconcile.py",
        "scripts/dream/brief.sh",
        ".zcode/hooks/kg-reminder.sh",
        ".zcode/hooks/guard-bash.sh",
        "dream/LESSONS.md",
        "dream/SELF_TUNE_LOG.md",
        "dream/STALE_PROPOSALS.md",
        "dream/MEMORY_PATCHES/2026-08-26.md",
        "dream/STATE/bash_use.log",
        "dream/STATE/hook.log",
        "dream/NEW_DREAM_FILE.md",
    ]
    for p in allowed_cases:
        ok, reason = check_scope(p)
        if not ok:
            print(f"FAIL: {p} should be allowed, got: {reason}")
            return 1
    print(f"[ok] {len(allowed_cases)} allow-list cases")

    # 2. Scope: deny-list matches P7-protected paths
    denied_cases = [
        "AGENTS.md",
        "00_METHODOLOGY/AGENTS.md",
        "02_CASES/Case_01_TinyTask_SaaS/PROJECT_STATE.md",
        "02_CASES/Case_02_SecureBorder_Solutions/PROJECT_STATE.md",
        "02_CASES/Case_03_OmniBank_Financial/PROJECT_STATE.md",
        "02_CASES/GLOBAL_PROJECT_STATE.md",
        "02_CASES/Case_01_TinyTask_SaaS/progress.json",
        "00_METHODOLOGY/dependency_graph.yaml",
        "00_METHODOLOGY/PREPROCESSING_by_domain/domains/D-01.1.md",
    ]
    for p in denied_cases:
        ok, reason = check_scope(p)
        if ok:
            print(f"FAIL: {p} should be denied, got: {reason}")
            return 1
    print(f"[ok] {len(denied_cases)} deny-list cases")

    # 3. Validate this script (Python + dry-run)
    here = Path(__file__).resolve()
    ok, details = validate_file(here)
    print(f"[{'ok' if ok else 'FAIL'}] validate self_tune.py: {details}")
    if not ok:
        return 1

    # 4. Validate adoption_audit.py
    audit = ROOT / "scripts" / "dream" / "adoption_audit.py"
    ok, details = validate_file(audit)
    print(f"[{'ok' if ok else 'FAIL'}] validate adoption_audit.py: {details}")
    if not ok:
        return 1

    # 5. Validate reconcile.py
    recon = ROOT / "scripts" / "dream" / "reconcile.py"
    ok, details = validate_file(recon)
    print(f"[{'ok' if ok else 'FAIL'}] validate reconcile.py: {details}")
    if not ok:
        return 1

    # 6. Validate brief.sh (bash)
    brief = ROOT / "scripts" / "dream" / "brief.sh"
    ok, details = validate_file(brief)
    print(f"[{'ok' if ok else 'FAIL'}] validate brief.sh: {details}")
    if not ok:
        return 1

    # 7. Commit (dry-run): verify prefix + scope guards work
    rc = commit_self_tune(
        "[DREAM SELF-TUNE] self_tune.py: self-test commit (would-apply)",
        ["scripts/dream/self_tune.py"],
        dry_run=True,
    )
    if rc != 0:
        print(f"FAIL: dry-run commit returned {rc}")
        return 1
    print("[ok] commit dry-run")

    # 8. Commit: refuse bad prefix
    rc = commit_self_tune(
        "no prefix here", ["scripts/dream/self_tune.py"], dry_run=True,
    )
    if rc == 0:
        print("FAIL: commit with bad prefix should have been refused")
        return 1
    print("[ok] commit refused bad prefix")

    # 9. Commit: refuse P7-protected path
    rc = commit_self_tune(
        "[DREAM SELF-TUNE] attempt to touch P7 file",
        ["AGENTS.md"], dry_run=True,
    )
    if rc == 0:
        print("FAIL: commit with P7-protected path should have been refused")
        return 1
    print("[ok] commit refused P7-protected path")

    print("=== self_tune.py --self-test PASSED ===")
    return 0


# --------------------- main ---------------------

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=False)

    p_validate = sub.add_parser("validate", help="Validate one file (scope + syntax + dry-run)")
    p_validate.add_argument("file", type=Path)

    p_check = sub.add_parser("check-scope", help="Check if a path is in self-tune scope")
    p_check.add_argument("path")

    p_commit = sub.add_parser("commit", help="Commit with [DREAM SELF-TUNE] prefix")
    p_commit.add_argument("--message", required=True)
    p_commit.add_argument("--dry-run", action="store_true")
    p_commit.add_argument("files", nargs="+")

    p.add_argument("--self-test", action="store_true",
                   help="Run end-to-end self-test")

    args = p.parse_args()

    if args.self_test:
        return self_test()

    if args.cmd == "validate":
        ok, details = validate_file(args.file)
        print("\n".join(details))
        return 0 if ok else 1

    if args.cmd == "check-scope":
        ok, reason = check_scope(args.path)
        print(f"{'ALLOW' if ok else 'DENY'}: {args.path} — {reason}")
        return 0 if ok else 2

    if args.cmd == "commit":
        return commit_self_tune(args.message, args.files, dry_run=args.dry_run)

    p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
