"""Integration tests against the real gauss_cli resolver.

These do NOT need a real Gauss project. A separate manual smoke test in Task 11
exercises the full Claude Desktop -> MCP -> worker -> Claude Code -> Lean stack.
"""
import shutil
from pathlib import Path

import pytest

from gauss_mcp.gauss_resolver import resolve_workflow

pytestmark = pytest.mark.integration


def test_gauss_cli_imports():
    """Sanity: the resolver target is importable from this Python environment."""
    from gauss_cli.autoformalize import resolve_autoformalize_request  # noqa
    from gauss_cli.config import load_config  # noqa
    config = load_config()
    assert isinstance(config, dict)


def test_resolve_workflow_against_non_project_dir(tmp_path):
    """Calling resolve_workflow on a non-Gauss directory should raise something
    actionable, not return successfully."""
    with pytest.raises(Exception) as excinfo:
        resolve_workflow("prove", "say hello", project_path=str(tmp_path))
    msg = str(excinfo.value).lower()
    # The error should mention either project, gauss, or workspace — not be a
    # cryptic AttributeError or similar.
    assert any(word in msg for word in ("project", "gauss", "workspace", "config"))


def test_claude_binary_present():
    """The path-B design depends on `claude` being available — Gauss returns an
    argv that starts with the Claude Code binary."""
    # We can't easily check via shutil.which because the test process inherits
    # a constrained PATH; check the canonical install location instead.
    candidates = ["/usr/bin/claude", "/usr/local/bin/claude"]
    found = [p for p in candidates if Path(p).exists()]
    assert found, f"claude binary not found in {candidates}"
