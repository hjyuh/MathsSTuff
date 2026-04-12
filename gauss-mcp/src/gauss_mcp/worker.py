"""Worker process: resolves one workflow and runs the spawned child to completion."""
from __future__ import annotations

import os
import subprocess
import sys
import threading
from pathlib import Path

from . import jobs, parse
from .gauss_resolver import resolve_workflow


_file_lock = threading.Lock()


def _heartbeat_loop(result_file: Path, pid: int, stop: threading.Event) -> None:
    while not stop.is_set():
        try:
            with _file_lock:
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
            stop.set()
            hb.join(timeout=1)
            with _file_lock:
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
            stop.set()
            hb.join(timeout=1)
            with _file_lock:
                jobs.write_error(
                    result_file,
                    error_type="spawn_failure",
                    message=f"{type(e).__name__}: {e}",
                )
            return

        log_text = log_file.read_text(errors="replace")

        stop.set()
        hb.join(timeout=1)

        if proc.returncode != 0:
            with _file_lock:
                jobs.write_error(
                    result_file,
                    error_type="gauss_exit",
                    message=f"child exited with code {proc.returncode}",
                    log_tail="\n".join(log_text.splitlines()[-50:]),
                )
            return

        lean_blocks = parse.extract_lean_blocks(log_text)
        with _file_lock:
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
