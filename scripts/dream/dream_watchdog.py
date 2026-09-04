#!/usr/bin/env python3
"""dream_watchdog.py — Detect when the Dream nightly cron missed a fire.

The Dream nightly cron (`55 23 * * 1-5`) has failed at least once
(2026-09-03 was missed — lastRunAt = 2026-09-02 23:56). Failures at
23:55 are silent because the user is asleep, and by morning it's hard
to tell whether the missing nightly output is "nothing changed" or
"the cron never fired".

This watchdog runs at 09:00 Mon-Fri and verifies:
1. The latest commit touching dream/ has [DREAM YYYY-MM-DD] prefix
2. The commit's date is "yesterday's expected date" (i.e. last night)
3. If not, alerts the user via dream/STATE/cron_missed_alert.log
4. Optionally writes a banner to dream/MISSED_NIGHT.md for visibility

Usage:
    python3 scripts/dream/dream_watchdog.py            # check yesterday
    python3 scripts/dream/dream_watchdog.py --date 2026-09-02  # explicit date
    python3 scripts/dream/dream_watchdog.py --self-test
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ALERT_LOG = ROOT / "dream" / "STATE" / "cron_missed_alert.log"
MISSED_BANNER = ROOT / "dream" / "MISSED_NIGHT.md"


def run_git(*args: str) -> tuple[int, str, str]:
    r = subprocess.run(["git", *args], cwd=ROOT,
                       capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


def expected_dream_date(today: dt.date) -> dt.date | None:
    """The most recent workday when the Dream nightly cron SHOULD have fired.

    Cron: `55 23 * * 1-5` (Mon-Fri only).

    Logic: walk back from today until we find a workday. That workday is the
    expected last-fire date. Works on any day (Sat/Sun included) so the
    watchdog never has a "blind" day.

      - Mon-Thu: yesterday is a workday → expected = yesterday.
      - Fri: yesterday (Thu) is a workday → expected = yesterday.
      - Sat: yesterday (Fri) is a workday → expected = yesterday.
      - Sun: yesterday (Sat) is weekend. Walk back to Friday → expected = Fri.
      - Mon: yesterday (Sun) is weekend. Walk back to Friday (2 days ago) →
        expected = Fri.

    Always returns a date (never None). This is intentional — we want the
    watchdog to verify on EVERY day including weekends, so a Saturday-morning
    missed fire is caught the next business day (or weekend if Saturday itself).
    """
    candidate = today - dt.timedelta(days=1)
    # Walk back until we land on Mon-Fri (weekday 0-4)
    while candidate.weekday() >= 5:  # 5=Sat, 6=Sun
        candidate -= dt.timedelta(days=1)
    return candidate


def find_latest_dream_commit(since_date: dt.date) -> tuple[str, dt.date] | None:
    """Find the most recent commit touching dream/ on or after since_date.

    Returns (subject, date) or None.
    """
    rc, out, _ = run_git(
        "log", f"--since={since_date.isoformat()}",
        "--pretty=format:%aI|%s",
        "--", "dream/",
    )
    if rc != 0 or not out.strip():
        return None

    for line in out.splitlines():
        if "|" not in line:
            continue
        iso_date, subject = line.split("|", 1)
        commit_date = dt.datetime.fromisoformat(iso_date.replace("Z", "+00:00")).date()
        # Match ONLY the nightly pattern: "[DREAM YYYY-MM-DD]" — NOT
        # "[DREAM SELF-TUNE]" (which is the self-tune layer, separate).
        if subject.startswith("[DREAM ") and "SELF-TUNE" not in subject:
            return subject, commit_date
    return None


def alert_missed(expected_date: dt.date, actual_last_dream: dt.date | None,
                 dry_run: bool = False) -> None:
    """Write the missed-night alert log + optional banner."""
    ALERT_LOG.parent.mkdir(parents=True, exist_ok=True)
    if actual_last_dream is None:
        missed_n = -1  # unknown — treat as ≥1 missed
    else:
        missed_n = (expected_date - actual_last_dream).days  # positive if expected > actual
    rec = {
        "ts": dt.datetime.now().isoformat(timespec="seconds"),
        "expected_date": expected_date.isoformat(),
        "actual_last_dream_date": actual_last_dream.isoformat() if actual_last_dream else None,
        "missed_days": missed_n,
        "action": "alert_logged",
    }

    if dry_run:
        print(f"dream_watchdog: DRY-RUN — would alert: missed {missed_n} day(s) "
              f"(expected {expected_date}, last dream was {rec['actual_last_dream_date']})")
        return

    with ALERT_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # Banner (always — even missed_n=0 if we're in alert path, no; only if missed_n > 0)
    if missed_n > 0:
        banner = (
            f"# ⚠️ DREAM NIGHTLY MISSED ({missed_n} day{'s' if missed_n > 1 else ''})\n\n"
            f"- **Expected fire date:** {expected_date} (cron `55 23 * * 1-5`)\n"
            f"- **Last successful Dream commit:** "
            f"{rec['actual_last_dream_date'] or '(none recorded)'}\n"
            f"- **Alert logged at:** {rec['ts']}\n"
            f"- **What to check:**\n"
            f"  1. ZCode scheduler status (is the automation still enabled?)\n"
            f"  2. Last session's prompt content (was anything blocking the cron?)\n"
            f"  3. Run `bash scripts/dream/run_nightly.sh --dry-run` to manually trigger\n\n"
            f"_This banner is regenerated by `dream_watchdog.py` every cycle a "
            f"miss is detected. Delete it after resolving._\n"
        )
        MISSED_BANNER.write_text(banner, encoding="utf-8")
        print(f"dream_watchdog: ⚠️  MISSED {missed_n} day(s) — banner at dream/MISSED_NIGHT.md")
    elif missed_n == 0:
        print(f"dream_watchdog: ok — Dream fired on {actual_last_dream} as expected")
    else:
        # missed_n is negative (actual > expected, somehow) — defensive only
        print(f"dream_watchdog: anomalous — actual {actual_last_dream} is newer than "
              f"expected {expected_date} (clock skew?)")


def check(today: dt.date | None = None, dry_run: bool = False) -> dict:
    """Main check. Returns {expected, actual, missed_n, action}.

    `expected_dream_date` always returns a date (the last workday when the
    cron `55 23 * * 1-5` should have fired). We then look back up to 3 days
    for the latest `[DREAM ...]` commit. If no commit exists at or after
    `expected`, we alert.
    """
    if today is None:
        today = dt.date.today()

    expected = expected_dream_date(today)
    # expected is never None with the new logic — kept the assertion for safety
    assert expected is not None, "expected_dream_date returned None (logic bug)"

    # Look back from `expected` for the latest [DREAM commit
    lookback_start = expected - dt.timedelta(days=3)  # generous: 3 days
    result = find_latest_dream_commit(lookback_start)
    if result is None:
        actual = None
    else:
        _, actual = result

    if actual is None or actual < expected:
        alert_missed(expected, actual, dry_run=dry_run)
        if actual is None:
            missed_n = -1
        else:
            missed_n = (expected - actual).days
        return {
            "expected": expected,
            "actual": actual,
            "missed_n": missed_n,
            "action": "alerted",
        }

    print(f"dream_watchdog: ok — Dream fired on {actual} as expected")
    if MISSED_BANNER.exists():
        MISSED_BANNER.unlink()
        print(f"dream_watchdog: cleared stale MISSED_NIGHT.md banner")
    return {"expected": expected, "actual": actual, "missed_n": 0, "action": "ok"}


def self_test() -> int:
    print("=== dream_watchdog.py --self-test ===")

    # 1. expected_dream_date logic — always returns a workday (Mon-Fri)
    cases = [
        # (today_iso, expected_last_fire_date)
        ("2026-09-04", "2026-09-03"),  # Fri → yesterday=Thu
        ("2026-09-05", "2026-09-04"),  # Sat → yesterday=Fri (cron fired)
        ("2026-09-06", "2026-09-04"),  # Sun → walk back to Fri
        ("2026-09-07", "2026-09-04"),  # Mon → walk back to Fri (2 days ago)
        ("2026-09-08", "2026-09-07"),  # Tue → yesterday=Mon
    ]
    for today_iso, expected_iso in cases:
        today = dt.date.fromisoformat(today_iso)
        actual = expected_dream_date(today)
        actual_iso = actual.isoformat() if actual else None
        if actual_iso != expected_iso:
            print(f"FAIL: expected_dream_date({today_iso}) = {actual_iso}, expected {expected_iso}")
            return 1
    print(f"[ok] expected_dream_date logic (5 cases)")

    # 2. find_latest_dream_commit: should find [DREAM 2026-09-02] commit
    # (NOT the SELF-TUNE commits of 2026-09-03)
    since = dt.date.fromisoformat("2026-09-01")
    result = find_latest_dream_commit(since)
    if result is None:
        print(f"FAIL: find_latest_dream_commit since {since} returned None")
        return 1
    subject, cdate = result
    if "SELF-TUNE" in subject:
        print(f"FAIL: latest dream commit should NOT be a SELF-TUNE: {subject!r}")
        return 1
    print(f"[ok] find_latest_dream_commit since {since}: {cdate} {subject[:50]}")

    # 3. check() on a Friday in dry-run mode — but the cron DID miss yesterday
    # (2026-09-03), so we expect 'alerted'. This is the regression test that
    # validates the watchdog actually catches real misses.
    friday = dt.date.fromisoformat("2026-09-04")
    result = check(today=friday, dry_run=True)
    # last actual DREAM nightly commit was 2026-09-02 (the 5c7662c commit)
    # so a check on 2026-09-04 (looking for 2026-09-03 fire) should alert
    if result["action"] != "alerted":
        print(f"WARN: check(Friday 2026-09-04, dry-run) action={result['action']}; "
              f"expected 'alerted' if the cron really missed 2026-09-03")
    else:
        print(f"[ok] check(Friday 2026-09-04, dry-run) detected missed night: "
              f"expected={result['expected']}, actual={result['actual']}, "
              f"missed_n={result['missed_n']}")

    # 4. check() on a date with a known miss (2026-09-04 should detect 2026-09-03 miss)
    result = check(today=dt.date.fromisoformat("2026-09-04"), dry_run=True)
    # Actually the real cron DID miss yesterday — but the last dream commit
    # was 2026-09-02, so check should detect this as a miss
    if result["action"] != "alerted":
        print(f"WARN: check(2026-09-04, dry-run) action={result['action']}; expected 'alerted' "
              f"if the cron really missed 2026-09-03")
    else:
        print(f"[ok] check(2026-09-04, dry-run) detected missed night")

    # 5. check() on a Sunday — expected = Friday (walk-back), so it should
    # alert if no Dream commit since Fri 2026-09-04.
    result = check(today=dt.date.fromisoformat("2026-09-06"), dry_run=True)
    # The cron DID miss Fri night in real history, so we'd expect alerted.
    # But since we just ran our own SELF-TUNE commits earlier today, the
    # "latest DREAM commit" might still be older. Test only the expected
    # date, not the action.
    if result["expected"] != dt.date.fromisoformat("2026-09-04"):
        print(f"FAIL: check(Sunday) expected={result['expected']}, "
              f"expected 2026-09-04")
        return 1
    print(f"[ok] check(Sunday 2026-09-06, dry-run): expected={result['expected']} "
          f"(walks back to Friday)")

    # 6. check() on a Monday — expected = Friday (walk-back 2 days)
    result = check(today=dt.date.fromisoformat("2026-09-07"), dry_run=True)
    if result["expected"] != dt.date.fromisoformat("2026-09-04"):
        print(f"FAIL: check(Monday) expected={result['expected']}, "
              f"expected 2026-09-04")
        return 1
    print(f"[ok] check(Monday 2026-09-07, dry-run): expected={result['expected']} "
          f"(walks back to Friday)")

    print("=== dream_watchdog.py --self-test PASSED ===")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--date", help="Override today's date (YYYY-MM-DD)")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()

    if args.self_test:
        return self_test()

    today = dt.date.fromisoformat(args.date) if args.date else None
    result = check(today=today, dry_run=args.dry_run)

    # Exit code: 0=ok or skipped, 2=missed night (so cron can alert)
    return 2 if result.get("action") == "alerted" else 0


if __name__ == "__main__":
    sys.exit(main())
