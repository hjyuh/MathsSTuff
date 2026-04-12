import json
import os
import time
from pathlib import Path

import pytest

from gauss_mcp.jobs import (
    make_job_id, init_job_file, write_done, write_error,
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


def test_atomic_write_and_read(tmp_path):
    f = tmp_path / "x.json"
    atomic_write_json(f, {"a": 1})
    assert json.loads(f.read_text()) == {"a": 1}
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
    data["last_heartbeat_at"] = time.time() - 120
    data["worker_pid"] = 999999
    atomic_write_json(f, data)
    assert is_stalled(f) is True
