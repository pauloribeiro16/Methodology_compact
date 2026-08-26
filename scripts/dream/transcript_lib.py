"""Parser for ZCode rollout JSONL files.

Each line of `~/.zcode/cli/rollout/model-io-sess_*.jsonl` is one model_io
exchange: a single full conversation snapshot (`request.body.messages`) plus
the new user message, the assistant's reply, tool calls and tool results.

Exchanges have cumulative history: record N's `messages` already contain every
prior user/assistant turn. We de-duplicate to produce one (turn, role, content,
tool_calls) row per logical turn.

Functions:
- iter_exchanges(rollout_path) -> Iterator[Exchange]
- exchanges_for_project(rollout_dir, project_markers) -> Iterator[Exchange]
"""
from __future__ import annotations

import json
import os
import re
import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Iterable, Iterator, Optional


@dataclass
class ToolCall:
    name: str
    input_summary: str  # truncated to ~120 chars


@dataclass
class Turn:
    role: str  # 'user' | 'assistant' | 'tool'
    text: str
    tool_calls: list[ToolCall] = field(default_factory=list)
    tool_call_id: Optional[str] = None  # for tool results
    tool_name: Optional[str] = None     # for tool results


@dataclass
class Exchange:
    completed_at: str
    session_id: str
    request_id: str
    duration_ms: int
    is_project: bool   # was this exchange in the project (vs title-gen / subagent)?
    new_user_text: str         # the user message that triggered this exchange
    turns: list[Turn]          # full conversation snapshot from this record


# --------------------- helpers ---------------------

def _text_of(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for c in content:
            t = c.get("type", "?")
            if t == "text":
                parts.append(c.get("text", ""))
            elif t == "tool_use":
                # placeholder; tool calls handled at block level elsewhere
                pass
            elif t == "tool_result":
                rc = c.get("content", "")
                if isinstance(rc, list):
                    rc = " ".join((x.get("text", "") if isinstance(x, dict) else str(x)) for x in rc)
                parts.append(f"[tool_result {c.get('tool_use_id','?')[:8]}] {str(rc)[:300]}")
        return "\n".join(parts).strip()
    return str(content)


def _tool_calls_of(content) -> list[ToolCall]:
    if not isinstance(content, list):
        return []
    out = []
    for c in content:
        if isinstance(c, dict) and c.get("type") == "tool_use":
            name = c.get("name", "?")
            inp = c.get("input", {})
            # compact summary: first string values or keys
            try:
                if isinstance(inp, dict):
                    bits = []
                    for k, v in list(inp.items())[:3]:
                        sv = str(v)
                        bits.append(f"{k}={sv[:60]}")
                    summary = ", ".join(bits)
                else:
                    summary = str(inp)[:120]
            except Exception:
                summary = "<unprintable>"
            out.append(ToolCall(name=name, input_summary=summary))
    return out


def _tool_result_of(content) -> tuple[Optional[str], Optional[str], str]:
    """Return (tool_call_id, tool_name_guess, text) for a tool_result message."""
    if not isinstance(content, list):
        return None, None, _text_of(content)
    text_parts, tool_use_id = [], None
    for c in content:
        if isinstance(c, dict):
            if c.get("type") == "tool_result":
                tool_use_id = c.get("tool_use_id", tool_use_id)
                rc = c.get("content", "")
                if isinstance(rc, list):
                    rc = " ".join((x.get("text", "") if isinstance(x, dict) else str(x)) for x in rc)
                text_parts.append(str(rc))
    return tool_use_id, None, "\n".join(text_parts).strip()


# --------------------- core iterator ---------------------

def _extract_workspace_marker(messages: list[dict]) -> Optional[str]:
    """Decide if an exchange belongs to Methodology_compact / Methodology-main.

    Heuristic: any tool_use referencing a path inside the repo, or any user
    message whose system-reminder brings in the project's AGENTS.md (which
    always names the repo as "Methodology_compact" or "Methodology-main").
    """
    for m in messages:
        c = m.get("content")
        if isinstance(c, list):
            for blk in c:
                if isinstance(blk, dict) and blk.get("type") == "tool_use":
                    inp = blk.get("input", {})
                    if isinstance(inp, dict):
                        for v in inp.values():
                            sv = str(v)
                            if ("Methodology_compact" in sv or "/00_METHODOLOGY/" in sv
                                or "/02_CASES/" in sv or "scripts/kg.sh" in sv
                                or "skills/SKILLNET" in sv or "/skills/" in sv):
                                return "compact"
                            if ("Methodology-main" in sv or "scripts/create-feature.sh" in sv):
                                return "main"
        elif isinstance(c, str):
            if ("Methodology_compact" in c or "/00_METHODOLOGY/" in c or "/02_CASES/" in c
                or "scripts/kg.sh" in c or "skills/SKILLNET" in c or "/skills/case-context-loader" in c):
                return "compact"
            if "Methodology-main" in c or "scripts/create-feature.sh" in c:
                return "main"
    return None


def iter_exchanges(rollout_path: str) -> Iterator[Exchange]:
    """Yield one Exchange per JSONL line (cumulative history not deduped yet)."""
    with open(rollout_path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            req = r.get("request") or {}
            body = req.get("body") or {}
            messages = body.get("messages") or []
            if not messages:
                continue
            completed_at = r.get("completedAt") or r.get("startedAt") or ""
            session_id = r.get("sessionId") or (req.get("headers") or {}).get("x-session-id", "?")
            request_id = r.get("requestId", "?")
            duration_ms = int(r.get("durationMs") or 0)
            ws = _extract_workspace_marker(messages)
            is_project = ws is not None

            turns: list[Turn] = []
            new_user_text = ""
            for m in messages:
                role = m.get("role", "?")
                content = m.get("content")
                if role == "user":
                    txt = _text_of(content)
                    turns.append(Turn(role="user", text=txt))
                elif role == "assistant":
                    tcs = _tool_calls_of(content)
                    txt = _text_of(content)
                    turns.append(Turn(role="assistant", text=txt, tool_calls=tcs))
                elif role == "tool":
                    tcid, tname, txt = _tool_result_of(content)
                    turns.append(Turn(role="tool", text=txt, tool_call_id=tcid, tool_name=tname))

            # The "new" user message is the last user turn in this record
            for m in reversed(messages):
                if m.get("role") == "user":
                    new_user_text = _text_of(m.get("content"))[:600]
                    break

            yield Exchange(
                completed_at=completed_at,
                session_id=session_id,
                request_id=request_id,
                duration_ms=duration_ms,
                is_project=is_project,
                new_user_text=new_user_text,
                turns=turns,
            )


def exchanges_for_project(rollout_dir: str, scope: str = "compact") -> Iterator[Exchange]:
    """Yield exchanges scoped to `scope` (= 'compact' or 'main')."""
    for fname in sorted(os.listdir(rollout_dir)):
        if not fname.endswith(".jsonl"):
            continue
        for ex in iter_exchanges(os.path.join(rollout_dir, fname)):
            if ex.is_project:
                yield ex


# --------------------- lightweight analysis primitives ---------------------

_TOOL_KG = re.compile(r"\bkg\.sh\b")
_TOOL_KG_SUBCMD = re.compile(r"kg\.sh\s+(impact|where|trace|doc|domain|map|hub|nist|hyper|audit|help)")
_TOOL_SKILL = re.compile(r"Skill[\(\{]?\s*name\s*=\s*['\"]?(case-context-loader|doc-conventions|skill)", re.I)
_P5_FLAG = re.compile(r"\b(SR|SO|RULE|REQ)-[A-Z0-9]+(?:-[A-Z0-9.]+)?")
_ID_EDIT = re.compile(r"\bEdit\s*\(", re.I)
_ID_WRITE = re.compile(r"\bWrite\s*\(")


def project_metrics(exchanges: Iterable[Exchange]) -> dict:
    """Compute simple adoption metrics from the per-exchange tool_calls."""
    kg_total = 0
    kg_subcmd: dict[str, int] = {}
    skill_calls: dict[str, int] = {}
    edits_without_impact: list[str] = []
    user_msgs = 0
    exchanges_with_kg = 0
    exchanges_with_skill = 0
    last_impact_per_session: dict[str, str] = {}

    for ex in exchanges:
        saw_kg = False
        saw_skill = False
        user_msgs += sum(1 for t in ex.turns if t.role == "user")
        for t in ex.turns:
            if t.role != "assistant":
                continue
            joined = "\n".join(t.tool_calls[i].name + " " + t.tool_calls[i].input_summary
                               for i in range(len(t.tool_calls)))
            # kg.sh usage
            for m in _TOOL_KG_SUBCMD.finditer(joined + " " + t.text):
                kg_subcmd[m.group(1)] = kg_subcmd.get(m.group(1), 0) + 1
                kg_total += 1
                saw_kg = True
                if m.group(1) == "impact":
                    # try to capture the id
                    mm = re.search(r"impact\s+([\w.-]+)", joined)
                    if mm:
                        last_impact_per_session[ex.session_id] = mm.group(1)
            # explicit Bash calls with kg.sh
            for tc in t.tool_calls:
                if _TOOL_KG.search(tc.input_summary) or tc.name.lower() == "bash":
                    pass  # already caught above
            # skill invocations
            for m in _TOOL_SKILL.finditer(t.text or ""):
                nm = m.group(1)
                skill_calls[nm] = skill_calls.get(nm, 0) + 1
                saw_skill = True
            # P5 check: edits to docs containing IDs without a prior impact this session
            if any(_ID_EDIT.search(tc.input_summary) or _ID_WRITE.search(tc.input_summary)
                   for tc in t.tool_calls):
                pass  # too noisy to act on in MVP; left as a hook
        if saw_kg:
            exchanges_with_kg += 1
        if saw_skill:
            exchanges_with_skill += 1

    return {
        "kg_total": kg_total,
        "kg_subcmd": dict(sorted(kg_subcmd.items(), key=lambda x: -x[1])),
        "skill_calls": dict(sorted(skill_calls.items(), key=lambda x: -x[1])),
        "user_messages": user_msgs,
        "exchanges_with_kg": exchanges_with_kg,
        "exchanges_with_skill": exchanges_with_skill,
        "last_impact_ids": last_impact_per_session,
    }


if __name__ == "__main__":
    import sys
    rd = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/.zcode/cli/rollout")
    n = 0
    for ex in exchanges_for_project(rd):
        n += 1
        if n <= 3:
            print(f"[{ex.completed_at[:19]}] session={ex.session_id[:8]} dur={ex.duration_ms}ms")
            print(f"  new_user: {ex.new_user_text[:120]!r}")
    print(f"\nTotal project-scoped exchanges: {n}")
