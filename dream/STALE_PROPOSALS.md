# STALE_PROPOSALS — amendment proposals awaiting human verdict

> Amendments that have appeared in `dream/ADOPTION_REPORT.md` for **5 or more
> consecutive nightly cycles** without being applied, rejected, or marked
> resolved are moved here by the Dream nightly (self-tune pass) to break the
> stagnation loop. The original proposal lives in ADOPTION_REPORT.md history
> (`git log -p -- dream/ADOPTION_REPORT.md | grep -A8 "<title>"`).
>
> **Lifecycle**:
> - **AWAITING-HUMAN-VERDICT**: moved here from the live proposals list. The
>   human reviews and either applies, rejects (with reason), or refines.
> - **RESOLVED**: human applied or rejected. Move to the bottom under
>   "Resolved" with a one-line outcome.
>
> **Why archive instead of delete**: the heuristic that generated the
> amendment may re-appear later (e.g. KG counts drift back below the
> threshold). Keeping the history allows diffing current vs past states
> without re-deriving from scratch.
>
> **Format**: one block per stale proposal.

## AWAITING-HUMAN-VERDICT

### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


### Skills are pre-flight but never invoked

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** Zero `case-context-loader` or `doc-conventions` invocations recorded across the audited window — the pre-flight line 'Skills: case-context-loader / doc-conventions' is text only. Either remove from AGENTS.md or make them actions a subagent/hook can detect.

**Proposed patch:**

```
Either:
  (a) Wire the SessionStart hook to invoke `skills/case-context-loader/scripts/load_case_context.sh`
      so it runs by default; or
  (b) Drop the mandatory items from pre-flight if the human prefers to invoke manually.
```

### Invoke case-context-loader at the start of any case session

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** 3 case(s) tracked in 02_CASES/. case-context-loader is the only skill that bootstraps a session with the actual current state. Use it before planning case work.

**Proposed patch:**

```
Add to the 'Where to start' section: 'Always start by running case-context-loader — the in-line read of GLOBAL+case+progress.json+phases below is the manual fallback, not the default.'
```

### Log hook firings for the dream to consume

- **First seen:** 2026-08-28
- **Last seen:** 2026-09-03 (archived 2026-09-03)
- **Consecutive cycles:** 20


**Rationale:** The kg-reminder hook fires once per session and the script writes nothing. For adoption measurement we need a side-effect log line per fire (e.g. `echo "$(date -Iseconds) kg-reminder" >> dream/STATE/hook.log`).

**Proposed patch:**

```
In `kg-reminder.sh`, after `touch "$SENTINEL"`, append the same ts to a line in `dream/STATE/hook.log` so the audit can correlate prompts that triggered the reminder.
```


_empty — first stale proposal will be archived here on next nightly cycle_

## RESOLVED

_empty — no proposals resolved yet_
