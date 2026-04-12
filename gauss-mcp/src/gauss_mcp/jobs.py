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
