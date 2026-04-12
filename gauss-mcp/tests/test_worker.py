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
