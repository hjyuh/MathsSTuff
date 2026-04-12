"""Wrap gauss_cli.autoformalize.resolve_autoformalize_request for the worker."""
from __future__ import annotations

from dataclasses import dataclass

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
