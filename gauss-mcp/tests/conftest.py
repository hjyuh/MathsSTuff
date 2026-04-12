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
