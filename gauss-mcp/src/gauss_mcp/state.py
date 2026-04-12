"""Sticky project state for the MCP server."""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional


def gauss_mcp_home() -> Path:
    env = os.environ.get("GAUSS_MCP_HOME")
    p = Path(env) if env else Path.home() / ".gauss-mcp"
    p.mkdir(parents=True, exist_ok=True)
    return p


@dataclass
class State:
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
