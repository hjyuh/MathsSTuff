# Gauss MCP Server Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a Python MCP server (`gauss-mcp`) that exposes OpenGauss workflows as fire-and-forget tools for Claude Desktop, with file-based async results.

**Architecture:** Stdio MCP server runs inside WSL, launched by Claude Desktop via `wsl -e`. Each workflow tool spawns a detached worker subprocess that runs `gauss chat -q "/<command>" -Q --resume <session>`, writes results atomically to a JSON file in `!math/gauss-mcp-results/`. State (sticky session, sticky project) lives in `~/.gauss-mcp/state.json`. See [the design doc](2026-04-12-gauss-mcp-server-design.md) for full rationale.

**Tech Stack:** Python 3.11 (from OpenGauss venv), `mcp` SDK (stdio transport), `pytest`, stdlib `subprocess`/`fcntl`/`json`/`os.replace`. No other deps.

**Critical early validation:** Task 2 verifies that `gauss chat -q "/prove ..."` actually invokes the slash command. If it doesn't, the entire approach changes — do NOT skip Task 2.

---

## Task 1: Project scaffolding

**Files:**
- Create: `gauss-mcp/pyproject.toml`
- Create: `gauss-mcp/README.md`
- Create: `gauss-mcp/src/gauss_mcp/__init__.py` (empty)
- Create: `gauss-mcp/tests/__init__.py` (empty)
- Create: `gauss-mcp/tests/conftest.py`

All paths are relative to `C:\Users\z20ma\OneDrive\Documents\!math\` (Windows view) which is `/mnt/c/Users/z20ma/OneDrive/Documents/!math/` from WSL.

**Step 1: Write `pyproject.toml`**

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "gauss-mcp"
version = "0.1.0"
description = "MCP server wrapping math.inc OpenGauss workflows for Claude Desktop"
requires-python = ">=3.11"
dependencies = [
    "mcp>=1.0",
]

[project.optional-dependencies]
dev = ["pytest>=8", "pytest-asyncio>=0.23"]

[project.scripts]
gauss-mcp = "gauss_mcp.__main__:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
markers = [
    "integration: requires gauss CLI on PATH (deselect with -m 'not integration')",
]
```

**Step 2: Write minimal `README.md`** — just one paragraph describing what the package is and pointing at the design doc.

**Step 3: Write `tests/conftest.py`**

```python
import os
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def tmp_state_dir(monkeypatch):
    """Isolate ~/.gauss-mcp/ for each test."""
    with tempfile.TemporaryDirectory() as d:
        monkeypatch.setenv("GAUSS_MCP_HOME", d)
        yield Path(d)


@pytest.fixture
def tmp_output_dir(tmp_path):
    out = tmp_path / "results"
    out.mkdir()
    return out
```

**Step 4: Install editable into the OpenGauss venv**

Run in WSL (use the same `bash -lc` + sudo trick from earlier session if needed):
```
source ~/OpenGauss/venv/bin/activate
cd /mnt/c/Users/z20ma/OneDrive/Documents/!math/gauss-mcp
pip install -e ".[dev]"
```
Expected: succeeds, `pytest` and `mcp` import cleanly.

**Step 5: Run pytest to confirm zero tests pass**

Run: `pytest -q`
Expected: `no tests ran`

**Step 6: Commit**

```bash
git add gauss-mcp/
git commit -m "feat(gauss-mcp): scaffold package"
```

---

## Task 2: Validate slash-command-via-`-q` assumption (CRITICAL)

**Why first:** the entire wrapper assumes `gauss chat -q "/prove ..." -Q` invokes the `/prove` slash command. If Gauss treats `-q` text as a literal user message and doesn't dispatch slash commands, we need a different approach (PTY transcript, or import Gauss internals). Find out NOW before building anything else.

**Files:**
- Create: `gauss-mcp/scripts/smoke_slash_command.sh`

**Step 1: Write the smoke script**

```bash
#!/usr/bin/env bash
# Validates that `gauss chat -q "/<slash> ..."` dispatches the slash command.
# Usage: ./scripts/smoke_slash_command.sh
set -euo pipefail

GAUSS=$(command -v gauss || echo "$HOME/.local/bin/gauss")
[ -x "$GAUSS" ] || { echo "gauss not found"; exit 2; }

echo "=== Test 1: literal hello ==="
"$GAUSS" chat -q "say the word PONG and nothing else" -Q 2>&1 | tail -20

echo
echo "=== Test 2: /status slash command (should show status, not echo) ==="
"$GAUSS" chat -q "/status" -Q 2>&1 | tail -30
```

**Step 2: Make it executable and run it from WSL**

```
chmod +x gauss-mcp/scripts/smoke_slash_command.sh
./gauss-mcp/scripts/smoke_slash_command.sh
```

**Step 3: Inspect output and decide**

- If Test 2 shows status info (workflow output) → assumption holds, proceed to Task 3.
- If Test 2 just echoes "/status" or treats it as a question → **STOP.** Update the design doc, then either:
  - (a) drive Gauss via expect/pexpect against an interactive `gauss chat` session, or
  - (b) import Gauss's chat module directly from the same Python venv and call its slash dispatcher.
  - Do not proceed past Task 2 until this is resolved.

**Step 4: Commit the smoke script**

```bash
git add gauss-mcp/scripts/
git commit -m "test(gauss-mcp): smoke-test slash command dispatch"
```

---

## Task 3: `parse.py` — extract Lean code blocks from Gauss output (TDD)

**Files:**
- Create: `gauss-mcp/src/gauss_mcp/parse.py`
- Create: `gauss-mcp/tests/test_parse.py`

**Step 1: Write the failing test**

```python
from gauss_mcp.parse import extract_lean_blocks


def test_extract_single_block():
    text = "Here is the proof:\n```lean\ntheorem t : 1 = 1 := rfl\n```\nDone."
    assert extract_lean_blocks(text) == ["theorem t : 1 = 1 := rfl"]


def test_extract_multiple_blocks():
    text = "```lean\nA\n```\nmiddle\n```lean4\nB\n```"
    assert extract_lean_blocks(text) == ["A", "B"]


def test_no_blocks_returns_empty():
    assert extract_lean_blocks("just prose") == []


def test_ignores_other_languages():
    text = "```python\nprint('hi')\n```"
    assert extract_lean_blocks(text) == []
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_parse.py -v`
Expected: ImportError on `gauss_mcp.parse`.

**Step 3: Write minimal implementation**

```python
"""Extract Lean code blocks from Gauss output."""
import re

_LEAN_FENCE = re.compile(
    r"```(?:lean|lean4)\s*\n(.*?)\n```",
    re.DOTALL,
)


def extract_lean_blocks(text: str) -> list[str]:
    return [m.group(1).rstrip() for m in _LEAN_FENCE.finditer(text)]
```

**Step 4: Run tests**

Run: `pytest tests/test_parse.py -v`
Expected: 4 passed.

**Step 5: Commit**

```bash
git add gauss-mcp/src/gauss_mcp/parse.py gauss-mcp/tests/test_parse.py
git commit -m "feat(gauss-mcp): extract lean code blocks from output"
```

---

## Task 4: `state.py` — sticky session/project state (TDD)

**Files:**
- Create: `gauss-mcp/src/gauss_mcp/state.py`
- Create: `gauss-mcp/tests/test_state.py`

**Step 1: Write the failing test**

```python
from gauss_mcp.state import State


def test_load_empty_state(tmp_state_dir):
    s = State.load()
    assert s.session_id is None
    assert s.project_path is None


def test_save_and_reload(tmp_state_dir):
    s = State.load()
    s.session_id = "abc123"
    s.project_path = "/home/user/proj"
    s.save()
    s2 = State.load()
    assert s2.session_id == "abc123"
    assert s2.project_path == "/home/user/proj"


def test_state_file_in_gauss_mcp_home(tmp_state_dir):
    s = State.load()
    s.session_id = "xyz"
    s.save()
    assert (tmp_state_dir / "state.json").exists()
```

**Step 2: Run to verify it fails**

Run: `pytest tests/test_state.py -v`
Expected: ImportError.

**Step 3: Write `state.py`**

```python
"""Sticky session + project state for the MCP server."""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional


def gauss_mcp_home() -> Path:
    """Resolve ~/.gauss-mcp/, honoring GAUSS_MCP_HOME for tests."""
    env = os.environ.get("GAUSS_MCP_HOME")
    if env:
        p = Path(env)
    else:
        p = Path.home() / ".gauss-mcp"
    p.mkdir(parents=True, exist_ok=True)
    return p


@dataclass
class State:
    session_id: Optional[str] = None
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

**Step 4: Run tests**

Run: `pytest tests/test_state.py -v`
Expected: 3 passed.

**Step 5: Commit**

```bash
git add gauss-mcp/src/gauss_mcp/state.py gauss-mcp/tests/test_state.py
git commit -m "feat(gauss-mcp): sticky session/project state"
```

---

## Task 5: `jobs.py` — job ids, file layout, atomic writes, heartbeat (TDD)

**Files:**
- Create: `gauss-mcp/src/gauss_mcp/jobs.py`
- Create: `gauss-mcp/tests/test_jobs.py`

This is the largest task; break it into sub-steps.

**Step 1: Write tests for `make_job_id`**

```python
import json
import os
import time
from pathlib import Path

import pytest

from gauss_mcp.jobs import (
    make_job_id, init_job_file, write_running, write_done, write_error,
    read_job, atomic_write_json, is_stalled, JOB_FILENAME_RE,
)


def test_job_id_format():
    jid = make_job_id("prove")
    assert JOB_FILENAME_RE.match(jid + ".json")
    assert "-prove-" in jid


def test_job_id_with_label():
    jid = make_job_id("formalize", label="amc")
    assert "-formalize-" in jid
    assert jid.endswith("-amc")
```

**Step 2: Write tests for atomic write + read**

```python
def test_atomic_write_and_read(tmp_path):
    f = tmp_path / "x.json"
    atomic_write_json(f, {"a": 1})
    assert json.loads(f.read_text()) == {"a": 1}
    # No tmp file left behind:
    assert not (tmp_path / "x.json.tmp").exists()


def test_init_job_file_writes_running(tmp_output_dir):
    f = init_job_file(
        tmp_output_dir,
        job_id="2026-04-12T00-00-00-prove-aaaa",
        command="/prove",
        input_text="t : 1=1",
        session_id="sess1",
    )
    data = read_job(f)
    assert data["status"] == "running"
    assert data["command"] == "/prove"
    assert data["session_id"] == "sess1"
    assert data["input"] == "t : 1=1"
    assert "started_at" in data
```

**Step 3: Write tests for done/error transitions and stall detection**

```python
def test_write_done(tmp_output_dir):
    f = init_job_file(tmp_output_dir, "jid1", "/prove", "x", "s")
    write_done(f, result_text="proof complete", lean_blocks=["theorem t := rfl"])
    data = read_job(f)
    assert data["status"] == "done"
    assert data["result_text"] == "proof complete"
    assert data["lean_code_blocks"] == ["theorem t := rfl"]
    assert data["finished_at"]
    assert data["duration_s"] >= 0


def test_write_error(tmp_output_dir):
    f = init_job_file(tmp_output_dir, "jid2", "/prove", "x", "s")
    write_error(f, error_type="gauss_exit", message="boom", log_tail="line1\nline2")
    data = read_job(f)
    assert data["status"] == "error"
    assert data["error"]["type"] == "gauss_exit"
    assert data["error"]["message"] == "boom"
    assert "line1" in data["error"]["log_tail"]


def test_stalled_detection(tmp_output_dir, monkeypatch):
    f = init_job_file(tmp_output_dir, "jid3", "/prove", "x", "s")
    data = read_job(f)
    # Heartbeat 120s ago, no live PID:
    data["last_heartbeat_at"] = time.time() - 120
    data["worker_pid"] = 999999  # almost certainly dead
    atomic_write_json(f, data)
    assert is_stalled(f) is True
```

**Step 4: Run tests to verify they fail**

Run: `pytest tests/test_jobs.py -v`
Expected: ImportError.

**Step 5: Implement `jobs.py`**

```python
"""Job lifecycle: ids, file layout, atomic writes, heartbeat, stall detection."""
from __future__ import annotations

import json
import os
import re
import secrets
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

JOB_FILENAME_RE = re.compile(
    r"\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}-[a-z]+-[a-z0-9]{4}(?:-[\w-]+)?\.json$"
)

STALL_THRESHOLD_S = 60


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _now_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")


def make_job_id(command: str, label: Optional[str] = None) -> str:
    rand = secrets.token_hex(2)
    base = f"{_now_compact()}-{command}-{rand}"
    return f"{base}-{label}" if label else base


def atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2))
    os.replace(tmp, path)


def read_job(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def init_job_file(
    output_dir: Path,
    job_id: str,
    command: str,
    input_text: str,
    session_id: str,
    log_file: Optional[Path] = None,
) -> Path:
    f = output_dir / f"{job_id}.json"
    data = {
        "job_id": job_id,
        "status": "running",
        "session_id": session_id,
        "command": command,
        "input": input_text,
        "started_at": _now_iso(),
        "finished_at": None,
        "duration_s": None,
        "result_text": None,
        "lean_code_blocks": [],
        "error": None,
        "log_file": str(log_file) if log_file else None,
        "worker_pid": None,
        "last_heartbeat_at": time.time(),
        "_started_monotonic": time.time(),
    }
    atomic_write_json(f, data)
    return f


def write_heartbeat(path: Path, pid: int) -> None:
    data = read_job(path)
    data["last_heartbeat_at"] = time.time()
    data["worker_pid"] = pid
    atomic_write_json(path, data)


def write_done(path: Path, result_text: str, lean_blocks: list[str]) -> None:
    data = read_job(path)
    started = data.get("_started_monotonic", time.time())
    data["status"] = "done"
    data["result_text"] = result_text
    data["lean_code_blocks"] = lean_blocks
    data["finished_at"] = _now_iso()
    data["duration_s"] = round(time.time() - started, 2)
    atomic_write_json(path, data)


def write_error(
    path: Path, error_type: str, message: str, log_tail: str = ""
) -> None:
    data = read_job(path)
    started = data.get("_started_monotonic", time.time())
    data["status"] = "error"
    data["finished_at"] = _now_iso()
    data["duration_s"] = round(time.time() - started, 2)
    data["error"] = {
        "type": error_type,
        "message": message,
        "log_tail": log_tail,
    }
    atomic_write_json(path, data)


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except (OSError, ProcessLookupError):
        return False


def is_stalled(path: Path) -> bool:
    data = read_job(path)
    if data["status"] != "running":
        return False
    hb = data.get("last_heartbeat_at") or 0
    pid = data.get("worker_pid")
    if time.time() - hb < STALL_THRESHOLD_S:
        return False
    if pid and _pid_alive(pid):
        return False
    return True
```

**Step 6: Run tests**

Run: `pytest tests/test_jobs.py -v`
Expected: 6 passed.

**Step 7: Commit**

```bash
git add gauss-mcp/src/gauss_mcp/jobs.py gauss-mcp/tests/test_jobs.py
git commit -m "feat(gauss-mcp): job lifecycle (ids, atomic writes, heartbeat)"
```

---

## Task 6: `gauss_cli.py` — slash-command builder + subprocess args (TDD)

**Files:**
- Create: `gauss-mcp/src/gauss_mcp/gauss_cli.py`
- Create: `gauss-mcp/tests/test_gauss_cli.py`

**Step 1: Write the failing test**

```python
from gauss_mcp.gauss_cli import build_query, build_argv, find_gauss_binary


def test_build_query_combines_command_and_input():
    q = build_query("prove", "theorem t : 1 = 1 := rfl")
    assert q.startswith("/prove\n\n")
    assert "theorem t : 1 = 1 := rfl" in q


def test_build_argv_includes_quiet_and_resume():
    argv = build_argv("/path/to/gauss", query="hi", session_id="sess1")
    assert argv == [
        "/path/to/gauss", "chat",
        "-q", "hi",
        "-Q",
        "--resume", "sess1",
    ]


def test_build_argv_without_session_omits_resume():
    argv = build_argv("/path/to/gauss", query="hi", session_id=None)
    assert "--resume" not in argv


def test_find_gauss_binary_returns_path(monkeypatch, tmp_path):
    fake = tmp_path / "gauss"
    fake.write_text("#!/bin/sh\n")
    fake.chmod(0o755)
    monkeypatch.setenv("PATH", str(tmp_path))
    assert find_gauss_binary() == str(fake)


def test_find_gauss_binary_raises_when_missing(monkeypatch):
    monkeypatch.setenv("PATH", "/nonexistent")
    monkeypatch.setattr("pathlib.Path.exists", lambda self: False)
    import pytest
    with pytest.raises(FileNotFoundError):
        find_gauss_binary()
```

**Step 2: Run to verify it fails**

Run: `pytest tests/test_gauss_cli.py -v`
Expected: ImportError.

**Step 3: Implement `gauss_cli.py`**

```python
"""Gauss CLI invocation helpers."""
from __future__ import annotations

import shutil
from pathlib import Path
from typing import Optional

VALID_COMMANDS = {
    "prove", "formalize", "autoformalize", "draft",
    "review", "autoprove", "refactor", "golf",
}


def build_query(command: str, input_text: str) -> str:
    if command not in VALID_COMMANDS:
        raise ValueError(f"unknown gauss command: {command}")
    return f"/{command}\n\n{input_text}"


def build_argv(
    gauss_bin: str, query: str, session_id: Optional[str]
) -> list[str]:
    argv = [gauss_bin, "chat", "-q", query, "-Q"]
    if session_id:
        argv += ["--resume", session_id]
    return argv


def find_gauss_binary() -> str:
    found = shutil.which("gauss")
    if found:
        return found
    fallback = Path.home() / ".local" / "bin" / "gauss"
    if fallback.exists():
        return str(fallback)
    raise FileNotFoundError(
        "gauss CLI not found on PATH or at ~/.local/bin/gauss"
    )
```

**Step 4: Run tests**

Run: `pytest tests/test_gauss_cli.py -v`
Expected: 5 passed.

**Step 5: Commit**

```bash
git add gauss-mcp/src/gauss_mcp/gauss_cli.py gauss-mcp/tests/test_gauss_cli.py
git commit -m "feat(gauss-mcp): gauss CLI argv + slash query builder"
```

---

## Task 7: `worker.py` — runs one job in a detached process

**Files:**
- Create: `gauss-mcp/src/gauss_mcp/worker.py`
- Create: `gauss-mcp/tests/test_worker.py`

**Step 1: Write the test using a fake gauss script**

```python
import os
import subprocess
import sys
from pathlib import Path

import pytest

from gauss_mcp import jobs
from gauss_mcp.worker import run_job


@pytest.fixture
def fake_gauss(tmp_path, monkeypatch):
    """Drop a fake gauss into PATH that echoes a canned response."""
    fake = tmp_path / "gauss"
    fake.write_text(
        "#!/usr/bin/env bash\n"
        "echo 'Result from fake gauss'\n"
        "echo '```lean'\n"
        "echo 'theorem t : 1 = 1 := rfl'\n"
        "echo '```'\n"
    )
    fake.chmod(0o755)
    monkeypatch.setenv("PATH", f"{tmp_path}:{os.environ['PATH']}")
    return str(fake)


def test_run_job_writes_done_with_lean_blocks(
    fake_gauss, tmp_output_dir, tmp_state_dir, tmp_path
):
    log_dir = tmp_path / "logs"
    log_dir.mkdir()
    job_id = jobs.make_job_id("prove")
    log_file = log_dir / f"{job_id}.log"
    result_file = jobs.init_job_file(
        tmp_output_dir, job_id,
        command="/prove",
        input_text="theorem t : 1 = 1",
        session_id="sess1",
        log_file=log_file,
    )

    run_job(
        result_file=result_file,
        log_file=log_file,
        gauss_bin=fake_gauss,
        command="prove",
        input_text="theorem t : 1 = 1",
        session_id="sess1",
    )

    data = jobs.read_job(result_file)
    assert data["status"] == "done"
    assert "Result from fake gauss" in data["result_text"]
    assert data["lean_code_blocks"] == ["theorem t : 1 = 1 := rfl"]


def test_run_job_writes_error_on_nonzero_exit(
    tmp_path, tmp_output_dir, tmp_state_dir, monkeypatch
):
    fake = tmp_path / "gauss"
    fake.write_text("#!/usr/bin/env bash\necho boom >&2\nexit 3\n")
    fake.chmod(0o755)
    log_file = tmp_path / "out.log"
    job_id = jobs.make_job_id("prove")
    result_file = jobs.init_job_file(
        tmp_output_dir, job_id, "/prove", "x", "s", log_file=log_file
    )

    run_job(
        result_file=result_file, log_file=log_file, gauss_bin=str(fake),
        command="prove", input_text="x", session_id="s",
    )

    data = jobs.read_job(result_file)
    assert data["status"] == "error"
    assert data["error"]["type"] == "gauss_exit"
    assert "boom" in data["error"]["log_tail"]
```

**Step 2: Run to verify it fails**

Run: `pytest tests/test_worker.py -v`
Expected: ImportError.

**Step 3: Implement `worker.py`**

```python
"""Worker process: runs one Gauss job and writes the result file."""
from __future__ import annotations

import os
import subprocess
import sys
import threading
import time
from pathlib import Path

from . import jobs, parse
from .gauss_cli import build_argv, build_query


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
    gauss_bin: str,
    command: str,
    input_text: str,
    session_id: str,
) -> None:
    query = build_query(command, input_text)
    argv = build_argv(gauss_bin, query=query, session_id=session_id)

    stop = threading.Event()
    hb = threading.Thread(
        target=_heartbeat_loop,
        args=(result_file, os.getpid(), stop),
        daemon=True,
    )
    hb.start()

    try:
        with open(log_file, "wb") as logf:
            proc = subprocess.run(argv, stdout=logf, stderr=logf, check=False)
    finally:
        stop.set()
        hb.join(timeout=1)

    log_text = log_file.read_text(errors="replace")

    if proc.returncode != 0:
        jobs.write_error(
            result_file,
            error_type="gauss_exit",
            message=f"gauss exited with code {proc.returncode}",
            log_tail="\n".join(log_text.splitlines()[-50:]),
        )
        return

    lean_blocks = parse.extract_lean_blocks(log_text)
    jobs.write_done(result_file, result_text=log_text, lean_blocks=lean_blocks)


def main() -> None:
    """Entry point: `python -m gauss_mcp.worker <result_file> <log_file>
    <gauss_bin> <command> <session_id>` — input_text is read from stdin."""
    result_file = Path(sys.argv[1])
    log_file = Path(sys.argv[2])
    gauss_bin = sys.argv[3]
    command = sys.argv[4]
    session_id = sys.argv[5]
    input_text = sys.stdin.read()
    try:
        run_job(result_file, log_file, gauss_bin, command, input_text, session_id)
    except Exception as e:
        jobs.write_error(
            result_file,
            error_type="worker_crash",
            message=f"{type(e).__name__}: {e}",
        )
        raise


if __name__ == "__main__":
    main()
```

**Step 4: Run tests**

Run: `pytest tests/test_worker.py -v`
Expected: 2 passed.

**Step 5: Commit**

```bash
git add gauss-mcp/src/gauss_mcp/worker.py gauss-mcp/tests/test_worker.py
git commit -m "feat(gauss-mcp): worker process runs one job"
```

---

## Task 8: Session collision lock (TDD)

**Files:**
- Modify: `gauss-mcp/src/gauss_mcp/jobs.py` (add `acquire_session_lock`)
- Modify: `gauss-mcp/src/gauss_mcp/worker.py` (acquire lock around the gauss call)
- Modify: `gauss-mcp/tests/test_jobs.py` (add lock test)

**Step 1: Write the lock test**

```python
import multiprocessing
import time

from gauss_mcp.jobs import acquire_session_lock


def _hold_lock(session_id, ready, release_after):
    with acquire_session_lock(session_id):
        ready.set()
        time.sleep(release_after)


def test_session_lock_serializes(tmp_state_dir):
    ready = multiprocessing.Event()
    p = multiprocessing.Process(
        target=_hold_lock, args=("sess-x", ready, 0.5)
    )
    p.start()
    ready.wait(2)
    t0 = time.time()
    with acquire_session_lock("sess-x"):
        elapsed = time.time() - t0
    p.join()
    assert elapsed >= 0.4  # second acquirer waited
```

**Step 2: Run to verify it fails**

Run: `pytest tests/test_jobs.py::test_session_lock_serializes -v`
Expected: ImportError on `acquire_session_lock`.

**Step 3: Implement the lock in `jobs.py`**

Add at the bottom of `jobs.py`:

```python
import contextlib
import fcntl


@contextlib.contextmanager
def acquire_session_lock(session_id: str):
    """Per-session file lock so two workers don't hit the same Gauss session."""
    locks_dir = Path(os.environ.get("GAUSS_MCP_HOME", str(Path.home() / ".gauss-mcp"))) / "locks"
    locks_dir.mkdir(parents=True, exist_ok=True)
    lock_path = locks_dir / f"{session_id}.lock"
    f = open(lock_path, "w")
    try:
        fcntl.flock(f, fcntl.LOCK_EX)
        yield
    finally:
        try:
            fcntl.flock(f, fcntl.LOCK_UN)
        finally:
            f.close()
```

**Step 4: Use the lock in `worker.run_job`**

Wrap the `subprocess.run` call:

```python
from .jobs import acquire_session_lock
...
    try:
        with acquire_session_lock(session_id):
            with open(log_file, "wb") as logf:
                proc = subprocess.run(argv, stdout=logf, stderr=logf, check=False)
    finally:
        ...
```

**Step 5: Run all tests**

Run: `pytest -v`
Expected: all green.

**Step 6: Commit**

```bash
git add gauss-mcp/src/gauss_mcp/jobs.py gauss-mcp/src/gauss_mcp/worker.py gauss-mcp/tests/test_jobs.py
git commit -m "feat(gauss-mcp): per-session file lock to serialize concurrent jobs"
```

---

## Task 9: `server.py` — MCP tool registration

**Files:**
- Create: `gauss-mcp/src/gauss_mcp/server.py`
- Create: `gauss-mcp/src/gauss_mcp/__main__.py`
- Create: `gauss-mcp/tests/test_server.py`

This task is bigger; do steps in order without rushing.

**Step 1: Read the `mcp` Python SDK quickstart**

Run in WSL:
```
python -c "import mcp; print(mcp.__version__)"
python -c "from mcp.server import Server; help(Server)" | head -60
```
Pattern is: instantiate `Server("gauss")`, register tools via decorators, run `stdio_server()` in `asyncio.run`. The exact API may have changed since this plan was written — check the version installed and adjust the imports below if needed.

**Step 2: Write `server.py`**

```python
"""MCP server exposing Gauss workflow tools."""
from __future__ import annotations

import asyncio
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from . import jobs, state
from .gauss_cli import VALID_COMMANDS, find_gauss_binary

DEFAULT_OUTPUT_DIR = Path(
    "/mnt/c/Users/z20ma/OneDrive/Documents/!math/gauss-mcp-results"
)

server = Server("gauss")


def _resolve_session(explicit: str | None) -> str:
    if explicit:
        return explicit
    s = state.State.load()
    if s.session_id:
        return s.session_id
    new_id = _create_new_gauss_session()
    s.session_id = new_id
    s.save()
    return new_id


def _create_new_gauss_session() -> str:
    """Run a noop gauss query to mint a fresh session id, return it."""
    gauss = find_gauss_binary()
    proc = subprocess.run(
        [gauss, "chat", "-q", "ready", "-Q"],
        capture_output=True, text=True, check=False,
    )
    # Gauss prints session id at end; the format may need adjustment
    # after seeing real output during Task 2 smoke test.
    for line in proc.stderr.splitlines() + proc.stdout.splitlines():
        if "session" in line.lower() and ":" in line:
            return line.split(":")[-1].strip()
    raise RuntimeError(
        f"Could not extract session id from gauss output:\n"
        f"stdout={proc.stdout}\nstderr={proc.stderr}"
    )


def _resolve_output_dir(explicit: str | None) -> Path:
    p = Path(explicit) if explicit else DEFAULT_OUTPUT_DIR
    p.mkdir(parents=True, exist_ok=True)
    return p


def _spawn_worker(
    command: str,
    input_text: str,
    project_path: str | None,
    session_id: str | None,
    output_dir: str | None,
    job_name: str | None,
) -> dict[str, Any]:
    gauss_bin = find_gauss_binary()
    sess = _resolve_session(session_id)
    out_dir = _resolve_output_dir(output_dir)
    log_dir = state.gauss_mcp_home() / "jobs"
    log_dir.mkdir(parents=True, exist_ok=True)

    job_id = jobs.make_job_id(command, label=job_name)
    log_file = log_dir / f"{job_id}.log"
    result_file = jobs.init_job_file(
        out_dir, job_id, f"/{command}", input_text, sess, log_file=log_file
    )

    cwd = project_path or state.State.load().project_path or os.getcwd()

    # Detached worker: setsid + start_new_session
    proc = subprocess.Popen(
        [
            sys.executable, "-m", "gauss_mcp.worker",
            str(result_file), str(log_file), gauss_bin, command, sess,
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
        cwd=cwd,
    )
    proc.stdin.write(input_text.encode())
    proc.stdin.close()

    return {
        "job_id": job_id,
        "status": "running",
        "output_file": str(result_file),
        "log_file": str(log_file),
        "session_id": sess,
        "started_at": jobs.read_job(result_file)["started_at"],
    }


def _tool_schema(extra_required: list[str] = ()) -> dict[str, Any]:
    return {
        "type": "object",
        "required": ["input"] + list(extra_required),
        "properties": {
            "input": {"type": "string"},
            "project_path": {"type": "string"},
            "session_id":   {"type": "string"},
            "output_dir":   {"type": "string"},
            "job_name":     {"type": "string"},
        },
    }


_DESCRIPTIONS = {
    "prove":          "Send a Lean theorem to Gauss /prove and get back a proof attempt. Async — returns a job id; result file appears when ready.",
    "formalize":      "Convert natural-language math into Lean 4 via Gauss /formalize. Async.",
    "autoformalize":  "Aggressively autoformalize a longer math passage via Gauss /autoformalize. Async, can take minutes.",
    "draft":          "Ask Gauss to draft a Lean proof skeleton via /draft. Async.",
    "review":         "Ask Gauss to review existing Lean code via /review. Async.",
    "autoprove":      "Hand a goal to Gauss's autoprover via /autoprove. Async, can take minutes.",
    "refactor":       "Ask Gauss to refactor Lean code via /refactor. Async.",
    "golf":           "Ask Gauss to golf (shorten) a proof via /golf. Async.",
}


@server.list_tools()
async def list_tools() -> list[Tool]:
    tools = [
        Tool(
            name=f"gauss_{cmd}",
            description=desc,
            inputSchema=_tool_schema(),
        )
        for cmd, desc in _DESCRIPTIONS.items()
    ]
    tools += [
        Tool(
            name="gauss_job_status",
            description="Read the current status of a job (running, done, error, stalled).",
            inputSchema={
                "type": "object",
                "required": ["job_id"],
                "properties": {"job_id": {"type": "string"}},
            },
        ),
        Tool(
            name="gauss_job_result",
            description="Return the parsed result JSON for a finished job. Errors if still running.",
            inputSchema={
                "type": "object",
                "required": ["job_id"],
                "properties": {"job_id": {"type": "string"}},
            },
        ),
        Tool(
            name="gauss_list_jobs",
            description="List recent jobs in the default or given output dir.",
            inputSchema={
                "type": "object",
                "properties": {
                    "limit":      {"type": "integer", "default": 20},
                    "status":     {"type": "string"},
                    "output_dir": {"type": "string"},
                },
            },
        ),
        Tool(
            name="gauss_new_session",
            description="Start a fresh Gauss session and make it sticky.",
            inputSchema={
                "type": "object",
                "properties": {"project_path": {"type": "string"}},
            },
        ),
        Tool(
            name="gauss_set_project",
            description="Set the sticky project directory used for future Gauss calls.",
            inputSchema={
                "type": "object",
                "required": ["path"],
                "properties": {"path": {"type": "string"}},
            },
        ),
        Tool(
            name="gauss_status",
            description="Report gauss version, sticky session/project, default output dir.",
            inputSchema={"type": "object", "properties": {}},
        ),
    ]
    return tools


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    def text(obj: Any) -> list[TextContent]:
        return [TextContent(type="text", text=json.dumps(obj, indent=2))]

    if name.startswith("gauss_") and name[6:] in VALID_COMMANDS:
        cmd = name[6:]
        result = _spawn_worker(
            command=cmd,
            input_text=arguments["input"],
            project_path=arguments.get("project_path"),
            session_id=arguments.get("session_id"),
            output_dir=arguments.get("output_dir"),
            job_name=arguments.get("job_name"),
        )
        return text(result)

    if name == "gauss_job_status":
        f = _find_job_file(arguments["job_id"])
        data = jobs.read_job(f)
        if jobs.is_stalled(f):
            data["status"] = "stalled"
        return text(data)

    if name == "gauss_job_result":
        f = _find_job_file(arguments["job_id"])
        data = jobs.read_job(f)
        if data["status"] == "running":
            raise RuntimeError(f"job {arguments['job_id']} still running")
        return text(data)

    if name == "gauss_list_jobs":
        out_dir = _resolve_output_dir(arguments.get("output_dir"))
        files = sorted(out_dir.glob("*.json"), reverse=True)
        limit = arguments.get("limit", 20)
        wanted = arguments.get("status")
        out: list[dict[str, Any]] = []
        for f in files:
            d = jobs.read_job(f)
            if wanted and d["status"] != wanted:
                continue
            out.append({"job_id": d["job_id"], "status": d["status"], "command": d["command"]})
            if len(out) >= limit:
                break
        return text(out)

    if name == "gauss_new_session":
        new_id = _create_new_gauss_session()
        s = state.State.load()
        s.session_id = new_id
        if arguments.get("project_path"):
            s.project_path = arguments["project_path"]
        s.save()
        return text({"session_id": new_id})

    if name == "gauss_set_project":
        s = state.State.load()
        s.project_path = arguments["path"]
        s.save()
        return text({"project_path": s.project_path})

    if name == "gauss_status":
        s = state.State.load()
        return text({
            "gauss_bin": find_gauss_binary(),
            "sticky_session": s.session_id,
            "sticky_project": s.project_path,
            "default_output_dir": str(DEFAULT_OUTPUT_DIR),
        })

    raise ValueError(f"unknown tool: {name}")


def _find_job_file(job_id: str) -> Path:
    candidates = [DEFAULT_OUTPUT_DIR, *map(Path, [])]  # extend if needed
    for c in candidates:
        p = c / f"{job_id}.json"
        if p.exists():
            return p
    raise FileNotFoundError(f"job not found: {job_id}")


async def main_async() -> None:
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())


def main() -> None:
    asyncio.run(main_async())
```

**Step 3: Write `__main__.py`**

```python
from .server import main

if __name__ == "__main__":
    main()
```

**Step 4: Write minimal `test_server.py`** (just import + tool listing)

```python
import asyncio
import pytest

from gauss_mcp.server import server


def test_server_lists_all_tools(tmp_state_dir):
    tools = asyncio.run(server.list_tools())
    names = {t.name for t in tools}
    assert "gauss_prove" in names
    assert "gauss_formalize" in names
    assert "gauss_status" in names
    assert "gauss_job_status" in names
    # 8 workflow + 6 control = 14 total
    assert len(names) == 14
```

**Step 5: Run tests**

Run: `pytest -v`
Expected: all green (server test passes; older tests still pass).

Note: this task contains the most likely API mismatches with the `mcp` SDK. If the test fails because of signature differences (e.g., decorator returns differ, `Tool` field names differ), adjust to match the installed version — the **shape** of what we're doing is correct.

**Step 6: Commit**

```bash
git add gauss-mcp/src/gauss_mcp/server.py gauss-mcp/src/gauss_mcp/__main__.py gauss-mcp/tests/test_server.py
git commit -m "feat(gauss-mcp): MCP server with 14 tools"
```

---

## Task 10: End-to-end integration test against real gauss

**Files:**
- Create: `gauss-mcp/tests/test_integration.py`

**Step 1: Write the test**

```python
import os
import time
from pathlib import Path

import pytest

from gauss_mcp import jobs
from gauss_mcp.gauss_cli import find_gauss_binary
from gauss_mcp.worker import run_job


pytestmark = pytest.mark.integration


def test_real_gauss_hello(tmp_output_dir, tmp_path):
    try:
        gauss_bin = find_gauss_binary()
    except FileNotFoundError:
        pytest.skip("gauss not installed")

    log_file = tmp_path / "out.log"
    job_id = jobs.make_job_id("prove")
    result_file = jobs.init_job_file(
        tmp_output_dir, job_id,
        command="/prove",
        input_text="say hello and nothing else",
        session_id="",  # let gauss create one
        log_file=log_file,
    )

    run_job(
        result_file=result_file, log_file=log_file, gauss_bin=gauss_bin,
        command="prove", input_text="say hello and nothing else", session_id="",
    )

    data = jobs.read_job(result_file)
    assert data["status"] in ("done", "error")
    assert data["finished_at"]
    assert data["result_text"]
```

**Step 2: Run integration test**

Run: `pytest -v -m integration`
Expected: passes if `gauss` is installed; gives a real result file.

If it fails because session_id is required: change Task 9's `_create_new_gauss_session` based on what real Gauss output looks like, then re-run.

**Step 3: Commit**

```bash
git add gauss-mcp/tests/test_integration.py
git commit -m "test(gauss-mcp): end-to-end integration test against real gauss"
```

---

## Task 11: Wire into Claude Desktop and manual smoke

**Files:**
- Modify: `%APPDATA%\Claude\claude_desktop_config.json`

**Step 1: Edit `claude_desktop_config.json`**

Add (or merge into existing `mcpServers`):

```json
{
  "mcpServers": {
    "gauss": {
      "command": "wsl",
      "args": [
        "-e", "bash", "-lc",
        "source ~/OpenGauss/venv/bin/activate && python -m gauss_mcp"
      ]
    }
  }
}
```

**Step 2: Restart Claude Desktop fully** (quit from system tray, reopen).

**Step 3: Smoke test in Claude Desktop**

Open a new chat. Verify the gauss tools appear. Then walk through:

1. Ask Claude: "call gauss_status and show me the result"
2. Ask Claude: "use gauss to formalize this: 'every prime greater than 2 is odd'"
3. Wait a few seconds. Ask Claude: "check the status of that gauss job"
4. Ask: "show me the final result"
5. Confirm a `.json` file appeared in `C:\Users\z20ma\OneDrive\Documents\!math\gauss-mcp-results\`

**Step 4: If anything fails**, check `~/.gauss-mcp/server.log` and the per-job `.log` files inside `~/.gauss-mcp/jobs/`.

**Step 5: Commit any config tweaks discovered during smoke**

If Task 9 needed adjustment for real session-id format, commit those fixes here as a follow-up.

---

## Task 12: README + final cleanup

**Files:**
- Modify: `gauss-mcp/README.md`

Write a real README covering: what it is, install steps, the Claude Desktop config snippet, the tool list with one-line descriptions, where results land, and a "troubleshooting" section pointing at logs.

**Commit:**
```bash
git add gauss-mcp/README.md
git commit -m "docs(gauss-mcp): README with install + troubleshooting"
```

---

## Done criteria

- [ ] All unit tests pass: `pytest -v -m "not integration"`
- [ ] Integration test passes: `pytest -v -m integration` (when gauss is available)
- [ ] Claude Desktop lists all 14 gauss tools after restart
- [ ] Calling `gauss_formalize` from Claude Desktop produces a result file in `!math/gauss-mcp-results/`
- [ ] Follow-up call in same conversation reuses the sticky session
- [ ] All commits in place; nothing uncommitted

## Risks / things to watch

- **Slash command dispatch (Task 2):** the entire design rests on this. If it doesn't work, stop and re-design.
- **`mcp` SDK API drift:** Task 9 will likely need small tweaks for the installed version.
- **Session id extraction:** `_create_new_gauss_session` uses a heuristic. After Task 2's smoke test you'll know what real Gauss output looks like — fix it then.
- **WSL PATH weirdness:** the Claude Desktop launch uses `bash -lc` to dodge the `/mnt/c/Program Files` issue we hit earlier in installation.
