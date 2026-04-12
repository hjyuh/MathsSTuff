# Gauss MCP Server — Path B Amendment

**Date:** 2026-04-12
**Supersedes:** parts of `2026-04-12-gauss-mcp-server.md` and `2026-04-12-gauss-mcp-server-design.md`
**Status:** Approved

## What changed

Task 2 of the original plan smoke-tested the assumption that `gauss chat -q "/<slash> ..." -Q` would dispatch slash commands. **The assumption was untestable as written:** `gauss chat -q` has a hard provider gate at `gauss_cli/main.py:429` that exits with `Gauss query mode needs a configured provider` before any slash parsing happens. Claude Code OAuth does not satisfy that gate; only API-key-style providers (OPENROUTER_API_KEY, ANTHROPIC_API_KEY, etc.) do.

Investigation found a clean alternative: `gauss_cli.autoformalize.resolve_autoformalize_request()`, a pure Python function at `gauss_cli/autoformalize.py:386`. The interactive Gauss TUI itself uses this resolver to dispatch `/prove`, `/draft`, `/review`, `/checkpoint`, `/refactor`, `/golf`, `/autoprove`, `/formalize`, `/autoformalize`. It returns a `HandoffRequest(argv, cwd, env)` describing exactly the subprocess to spawn the configured "managed backend" (Claude Code in our setup), and **bypasses the provider gate entirely**. Verified via source read at `gauss_cli/main.py:71-119, 425-452` and `gauss_cli/autoformalize.py:386-465`.

A separate smoke test confirmed `claude --print --output-format text` works with piped stdin/stdout — no TTY needed.

## Architectural impact

**The MCP server's external behavior is unchanged.** Still 14 tools, still async fire-and-forget, still file-based results in `!math/gauss-mcp-results/`. What changes is *how the worker process talks to Gauss*.

**Old worker flow (path A, abandoned):**
```
worker → subprocess.run(["gauss", "chat", "-q", "/prove ...", "-Q", "--resume", session_id])
                        ↑ blocked by provider gate
```

**New worker flow (path B):**
```
worker → from gauss_cli.autoformalize import resolve_autoformalize_request
       → from gauss_cli.config import load_config
       → plan = resolve_autoformalize_request("/prove ...", load_config(), active_cwd=project_path)
       → subprocess.run(plan.handoff_request.argv, cwd=plan.handoff_request.cwd,
                        env=plan.handoff_request.env, stdout=PIPE, stderr=PIPE)
                        ↑ this is a Claude Code invocation; uses ~/.claude/ OAuth
```

**Session continuity is dropped.** Each call spawns a fresh Claude Code child process with its own history. Claude Desktop already maintains conversation memory at a higher layer and can re-supply context naturally when calling tools again. The "sticky session" abstraction was solving a problem Claude Desktop already solves.

## Task changes

| Task | Status | Change |
|---|---|---|
| 1 | ✅ Done | No change |
| 2 | ✅ Done (failed → resolved) | Smoke script committed at `9da467a` documents the failure; this amendment documents the resolution. Mark task complete. |
| 3 | unchanged | `parse.py` works on text output regardless of source |
| **4** | **CHANGED** | `state.py` drops `session_id` field. Keeps only `project_path`. Rename class from `State` to `State` (same name, narrower contract). |
| 5 | unchanged | `jobs.py` works the same; the result file just no longer tracks `session_id` semantically (we keep the field but it'll be `None` or a synthetic per-job id) |
| **6** | **REPLACED** | `gauss_cli.py` is now `gauss_resolver.py`. New API surface below. |
| **7** | **CHANGED** | `worker.py` calls the resolver, then spawns the resolved argv. Heartbeat/result-write logic unchanged. |
| **8** | **DELETED** | Session collision lock no longer needed (no shared sessions). |
| **9** | **CHANGED** | `server.py` drops `gauss_new_session` and `session_id` args from all tools. Renumbered tool count: 12 instead of 14 (8 workflow + 4 control: `gauss_job_status`, `gauss_job_result`, `gauss_list_jobs`, `gauss_set_project`, `gauss_status`). |
| 10 | unchanged | Integration test still hits the worker; just adjust the call signature |
| 11 | unchanged | Wiring stays the same |
| 12 | unchanged | README |

## Replacement Task 4: `state.py` — sticky project (TDD)

**Files:**
- Create: `gauss-mcp/src/gauss_mcp/state.py`
- Create: `gauss-mcp/tests/test_state.py`

**Step 1: Failing test**

```python
from gauss_mcp.state import State


def test_load_empty_state(tmp_state_dir):
    s = State.load()
    assert s.project_path is None


def test_save_and_reload(tmp_state_dir):
    s = State.load()
    s.project_path = "/home/user/proj"
    s.save()
    s2 = State.load()
    assert s2.project_path == "/home/user/proj"


def test_state_file_in_gauss_mcp_home(tmp_state_dir):
    s = State.load()
    s.project_path = "/x"
    s.save()
    assert (tmp_state_dir / "state.json").exists()
```

**Step 2: Implementation**

```python
"""Sticky project state for the MCP server."""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional


def gauss_mcp_home() -> Path:
    env = os.environ.get("GAUSS_MCP_HOME")
    p = Path(env) if env else Path.home() / ".gauss-mcp"
    p.mkdir(parents=True, exist_ok=True)
    return p


@dataclass
class State:
    project_path: Optional[str] = None

    @classmethod
    def load(cls) -> "State":
        f = gauss_mcp_home() / "state.json"
        if not f.exists():
            return cls()
        return cls(**json.loads(f.read_text()))

    def save(self) -> None:
        f = gauss_mcp_home() / "state.json"
        tmp = f.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(asdict(self), indent=2))
        os.replace(tmp, f)
```

Commit: `feat(gauss-mcp): sticky project state`

## Replacement Task 6: `gauss_resolver.py` — wrap the in-process resolver (TDD)

**Files:**
- Create: `gauss-mcp/src/gauss_mcp/gauss_resolver.py`
- Create: `gauss-mcp/tests/test_gauss_resolver.py`

**The valid commands set** (validated against `_WORKFLOW_ALIAS_MAP` in `gauss_cli/autoformalize.py`):
```
prove, formalize, autoformalize, draft, review, autoprove, refactor, golf, checkpoint
```

**Step 1: Failing tests**

```python
import pytest

from gauss_mcp.gauss_resolver import (
    VALID_COMMANDS, build_slash_input, ResolvedJob, resolve_workflow,
)


def test_valid_commands_includes_all_eight():
    for cmd in ("prove", "formalize", "autoformalize", "draft",
                "review", "autoprove", "refactor", "golf"):
        assert cmd in VALID_COMMANDS


def test_build_slash_input_format():
    s = build_slash_input("prove", "theorem t : 1 = 1 := rfl")
    assert s.startswith("/prove ")
    assert "theorem t : 1 = 1 := rfl" in s


def test_build_slash_input_rejects_unknown_command():
    with pytest.raises(ValueError):
        build_slash_input("nonsense", "x")


def test_resolve_workflow_returns_argv_cwd_env(monkeypatch, tmp_path):
    """resolve_workflow wraps gauss_cli.autoformalize.resolve_autoformalize_request.
    Mock the upstream call so the test doesn't need a real Gauss project."""

    fake_request = type("HR", (), {
        "argv": ["claude", "--print", "stub"],
        "cwd": str(tmp_path),
        "env": {"FAKE": "1"},
    })()
    fake_plan = type("Plan", (), {"handoff_request": fake_request})()

    def fake_resolver(slash_input, config, active_cwd):
        assert slash_input.startswith("/prove ")
        assert active_cwd == str(tmp_path)
        return fake_plan

    monkeypatch.setattr(
        "gauss_cli.autoformalize.resolve_autoformalize_request", fake_resolver
    )
    monkeypatch.setattr("gauss_cli.config.load_config", lambda: {})

    job = resolve_workflow("prove", "theorem t : 1 = 1", project_path=str(tmp_path))
    assert isinstance(job, ResolvedJob)
    assert job.argv == ["claude", "--print", "stub"]
    assert job.cwd == str(tmp_path)
    assert job.env["FAKE"] == "1"
```

**Step 2: Implementation**

```python
"""Wrap gauss_cli.autoformalize.resolve_autoformalize_request for the worker."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

VALID_COMMANDS = {
    "prove", "formalize", "autoformalize", "draft",
    "review", "autoprove", "refactor", "golf", "checkpoint",
}


def build_slash_input(command: str, input_text: str) -> str:
    if command not in VALID_COMMANDS:
        raise ValueError(f"unknown gauss command: {command}")
    return f"/{command} {input_text}"


@dataclass
class ResolvedJob:
    argv: list[str]
    cwd: str
    env: dict[str, str]


def resolve_workflow(command: str, input_text: str, project_path: str) -> ResolvedJob:
    """Call Gauss's in-process resolver and return a spawnable job."""
    # Imports are inside the function so unit tests can monkeypatch them
    # without forcing the test process to load all of gauss_cli.
    from gauss_cli.autoformalize import resolve_autoformalize_request
    from gauss_cli.config import load_config

    slash_input = build_slash_input(command, input_text)
    config = load_config()
    plan = resolve_autoformalize_request(slash_input, config, active_cwd=project_path)
    hr = plan.handoff_request
    return ResolvedJob(argv=list(hr.argv), cwd=str(hr.cwd), env=dict(hr.env))
```

**Important notes for the implementer:**

1. **The mocked attribute paths in the test are dotted** (`gauss_cli.autoformalize.resolve_autoformalize_request`), but the implementation imports inside the function. Use `monkeypatch.setattr("gauss_cli.autoformalize.resolve_autoformalize_request", ...)` — this works because `monkeypatch.setattr` patches the attribute on the module object itself, so the deferred `from ... import` inside `resolve_workflow` picks up the patched version. Verify this works in the test.

2. **`load_config()` may take args** in the real implementation. Read its actual signature in `gauss_cli/config.py` and adjust the test mock accordingly. If it requires a path, pass it as a kwarg from `resolve_workflow`.

3. **`resolve_autoformalize_request` may raise `AutoformalizeError`** for missing project, invalid command, etc. Let it propagate from `resolve_workflow`. The worker will catch it.

4. **The argv returned will likely contain a tempfile path** that Gauss creates as part of the handoff bundle. Don't try to clean it up — Gauss owns its lifecycle.

Commit: `feat(gauss-mcp): in-process workflow resolver`

## Replacement Task 7: `worker.py` — runs one resolved job

**Files:**
- Create: `gauss-mcp/src/gauss_mcp/worker.py`
- Create: `gauss-mcp/tests/test_worker.py`

**Step 1: Failing tests**

```python
import os
from pathlib import Path

import pytest

from gauss_mcp import jobs
from gauss_mcp.worker import run_job


def test_run_job_writes_done_with_lean_blocks(
    monkeypatch, tmp_output_dir, tmp_state_dir, tmp_path
):
    """Mock resolve_workflow so we don't need a real Gauss project. Use a fake
    'claude' that emits a lean block."""
    fake_claude = tmp_path / "fake_claude"
    fake_claude.write_text(
        "#!/usr/bin/env bash\n"
        "echo 'Result from fake claude'\n"
        "echo '```lean'\n"
        "echo 'theorem t : 1 = 1 := rfl'\n"
        "echo '```'\n"
    )
    fake_claude.chmod(0o755)

    from gauss_mcp.gauss_resolver import ResolvedJob
    monkeypatch.setattr(
        "gauss_mcp.worker.resolve_workflow",
        lambda command, input_text, project_path: ResolvedJob(
            argv=[str(fake_claude)], cwd=str(tmp_path), env=dict(os.environ),
        ),
    )

    log_dir = tmp_path / "logs"
    log_dir.mkdir()
    job_id = jobs.make_job_id("prove")
    log_file = log_dir / f"{job_id}.log"
    result_file = jobs.init_job_file(
        tmp_output_dir, job_id, command="/prove",
        input_text="theorem t : 1 = 1", session_id="", log_file=log_file,
    )

    run_job(
        result_file=result_file, log_file=log_file,
        command="prove", input_text="theorem t : 1 = 1",
        project_path=str(tmp_path),
    )

    data = jobs.read_job(result_file)
    assert data["status"] == "done"
    assert "Result from fake claude" in data["result_text"]
    assert data["lean_code_blocks"] == ["theorem t : 1 = 1 := rfl"]


def test_run_job_writes_error_on_nonzero_exit(
    monkeypatch, tmp_output_dir, tmp_state_dir, tmp_path
):
    fake_claude = tmp_path / "fake_claude"
    fake_claude.write_text("#!/usr/bin/env bash\necho boom >&2\nexit 3\n")
    fake_claude.chmod(0o755)

    from gauss_mcp.gauss_resolver import ResolvedJob
    monkeypatch.setattr(
        "gauss_mcp.worker.resolve_workflow",
        lambda command, input_text, project_path: ResolvedJob(
            argv=[str(fake_claude)], cwd=str(tmp_path), env=dict(os.environ),
        ),
    )

    log_file = tmp_path / "out.log"
    job_id = jobs.make_job_id("prove")
    result_file = jobs.init_job_file(
        tmp_output_dir, job_id, "/prove", "x", "", log_file=log_file
    )

    run_job(
        result_file=result_file, log_file=log_file,
        command="prove", input_text="x", project_path=str(tmp_path),
    )

    data = jobs.read_job(result_file)
    assert data["status"] == "error"
    assert data["error"]["type"] == "gauss_exit"
    assert "boom" in data["error"]["log_tail"]


def test_run_job_writes_error_on_resolver_failure(
    monkeypatch, tmp_output_dir, tmp_state_dir, tmp_path
):
    def boom(**kwargs):
        raise RuntimeError("no project here")
    monkeypatch.setattr("gauss_mcp.worker.resolve_workflow", boom)

    log_file = tmp_path / "out.log"
    job_id = jobs.make_job_id("prove")
    result_file = jobs.init_job_file(
        tmp_output_dir, job_id, "/prove", "x", "", log_file=log_file
    )

    run_job(
        result_file=result_file, log_file=log_file,
        command="prove", input_text="x", project_path=str(tmp_path),
    )

    data = jobs.read_job(result_file)
    assert data["status"] == "error"
    assert data["error"]["type"] == "resolver_failure"
    assert "no project here" in data["error"]["message"]
```

**Step 2: Implementation**

```python
"""Worker process: resolves one workflow and runs the spawned child to completion."""
from __future__ import annotations

import os
import subprocess
import sys
import threading
from pathlib import Path

from . import jobs, parse
from .gauss_resolver import resolve_workflow


def _heartbeat_loop(result_file: Path, pid: int, stop: threading.Event) -> None:
    while not stop.is_set():
        try:
            jobs.write_heartbeat(result_file, pid)
        except Exception:
            pass
        stop.wait(5)


def run_job(
    result_file: Path,
    log_file: Path,
    command: str,
    input_text: str,
    project_path: str,
) -> None:
    stop = threading.Event()
    hb = threading.Thread(
        target=_heartbeat_loop,
        args=(result_file, os.getpid(), stop),
        daemon=True,
    )
    hb.start()

    try:
        try:
            resolved = resolve_workflow(
                command=command, input_text=input_text, project_path=project_path,
            )
        except Exception as e:
            jobs.write_error(
                result_file,
                error_type="resolver_failure",
                message=f"{type(e).__name__}: {e}",
            )
            return

        try:
            with open(log_file, "wb") as logf:
                proc = subprocess.run(
                    resolved.argv,
                    stdout=logf, stderr=logf,
                    cwd=resolved.cwd, env=resolved.env,
                    check=False,
                )
        except Exception as e:
            jobs.write_error(
                result_file,
                error_type="spawn_failure",
                message=f"{type(e).__name__}: {e}",
            )
            return

        log_text = log_file.read_text(errors="replace")

        if proc.returncode != 0:
            jobs.write_error(
                result_file,
                error_type="gauss_exit",
                message=f"child exited with code {proc.returncode}",
                log_tail="\n".join(log_text.splitlines()[-50:]),
            )
            return

        lean_blocks = parse.extract_lean_blocks(log_text)
        jobs.write_done(result_file, result_text=log_text, lean_blocks=lean_blocks)
    finally:
        stop.set()
        hb.join(timeout=1)


def main() -> None:
    """python -m gauss_mcp.worker <result_file> <log_file> <command> <project_path>
    — input_text on stdin."""
    result_file = Path(sys.argv[1])
    log_file = Path(sys.argv[2])
    command = sys.argv[3]
    project_path = sys.argv[4]
    input_text = sys.stdin.read()
    try:
        run_job(result_file, log_file, command, input_text, project_path)
    except Exception as e:
        jobs.write_error(
            result_file, error_type="worker_crash",
            message=f"{type(e).__name__}: {e}",
        )
        raise


if __name__ == "__main__":
    main()
```

Commit: `feat(gauss-mcp): worker process runs one resolved workflow`

## Task 8: deleted

The session collision lock is no longer needed because there are no shared sessions. Each worker spawns an independent Claude Code child. Skip Task 8 entirely.

## Replacement Task 9: `server.py` — MCP tools (12, not 14)

Same structure as the original Task 9, but:

- **Drop these tools:** `gauss_new_session`
- **Drop these arguments from every workflow tool:** `session_id`
- **`gauss_status` no longer reports** `sticky_session`
- **Project resolution** in `_spawn_worker`: explicit `project_path` arg → sticky → cwd → error if none of those exist (the resolver requires a project).
- **Worker spawn argv** is now: `[python, "-m", "gauss_mcp.worker", str(result_file), str(log_file), command, project_path]`. Input passed via stdin as before.

The other tools (`gauss_job_status`, `gauss_job_result`, `gauss_list_jobs`, `gauss_set_project`, `gauss_status`, plus 8 workflow tools) are unchanged in shape.

**Final tool count: 13** (8 workflow + `gauss_job_status` + `gauss_job_result` + `gauss_list_jobs` + `gauss_set_project` + `gauss_status`).

Update the test in Task 9 Step 4:
```python
assert len(names) == 13
```

## Risks closed

- ~~Slash command dispatch via `-q`~~ — abandoned; using in-process resolver instead.
- ~~Session id extraction~~ — no sessions.

## New risks

- **Coupling to `gauss_cli` internals.** `resolve_autoformalize_request` is not a documented public API. A future Gauss release could rename or restructure it. Mitigation: pin the OpenGauss commit we tested against in the README troubleshooting section, and write the resolver wrapper such that an `ImportError` on either symbol gives a clear actionable error message.
- **The spawned Claude Code child is itself an interactive agent** that may run for many turns under `--print` mode. We have no per-turn visibility — only the final stdout. That's fine for the fire-and-forget MCP shape but means jobs can take quite a while. No timeout (per design). The heartbeat keeps the result file fresh.
