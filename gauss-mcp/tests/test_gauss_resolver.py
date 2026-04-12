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
    # Force modules into sys.modules so monkeypatch.setattr can find attributes
    # on the deferred imports inside resolve_workflow.
    import gauss_cli.autoformalize  # noqa: F401
    import gauss_cli.config  # noqa: F401

    fake_request = type("HR", (), {
        "argv": ("claude", "--print", "stub"),
        "cwd": str(tmp_path),
        "env": {"FAKE": "1"},
    })()
    fake_plan = type("Plan", (), {"handoff_request": fake_request})()

    def fake_resolver(command, config, *, active_cwd=None, base_env=None):
        assert command.startswith("/prove ")
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
