import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def tmp_state_dir(monkeypatch):
    """Override GAUSS_MCP_HOME to a temp dir so state writes don't touch the real ~/.gauss-mcp."""
    with tempfile.TemporaryDirectory() as d:
        monkeypatch.setenv("GAUSS_MCP_HOME", d)
        yield Path(d)


@pytest.fixture
def tmp_output_dir(tmp_path):
    out = tmp_path / "results"
    out.mkdir()
    return out
