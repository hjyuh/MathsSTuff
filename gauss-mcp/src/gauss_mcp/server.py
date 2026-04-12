"""MCP server exposing Gauss workflow tools."""
from __future__ import annotations

import asyncio
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from . import jobs, state

DEFAULT_OUTPUT_DIR = Path(
    "/mnt/c/Users/z20ma/OneDrive/Documents/!math/gauss-mcp-results"
)

# 8 workflow commands exposed as tools. `checkpoint` is a Gauss-internal command
# recognized by the resolver but not a workflow Claude Desktop should call.
WORKFLOW_COMMANDS = (
    "prove", "formalize", "autoformalize", "draft",
    "review", "autoprove", "refactor", "golf",
)

server = Server("gauss")


def _resolve_output_dir(explicit: str | None) -> Path:
    p = Path(explicit) if explicit else DEFAULT_OUTPUT_DIR
    p.mkdir(parents=True, exist_ok=True)
    return p


def _resolve_project(explicit: str | None) -> str:
    if explicit:
        return explicit
    s = state.State.load()
    if s.project_path:
        return s.project_path
    cwd = os.getcwd()
    if not cwd:
        raise RuntimeError(
            "No project_path provided, no sticky project set, and cwd unavailable."
        )
    return cwd


def _spawn_worker(
    command: str,
    input_text: str,
    project_path: str | None,
    output_dir: str | None,
    job_name: str | None,
) -> dict[str, Any]:
    project = _resolve_project(project_path)
    out_dir = _resolve_output_dir(output_dir)
    log_dir = state.gauss_mcp_home() / "jobs"
    log_dir.mkdir(parents=True, exist_ok=True)

    job_id = jobs.make_job_id(command, label=job_name)
    log_file = log_dir / f"{job_id}.log"
    result_file = jobs.init_job_file(
        out_dir, job_id, f"/{command}", input_text, "", log_file=log_file
    )

    proc = subprocess.Popen(
        [
            sys.executable, "-m", "gauss_mcp.worker",
            str(result_file), str(log_file), command, project,
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    assert proc.stdin is not None
    proc.stdin.write(input_text.encode())
    proc.stdin.close()

    return {
        "job_id": job_id,
        "status": "running",
        "output_file": str(result_file),
        "log_file": str(log_file),
        "started_at": jobs.read_job(result_file)["started_at"],
    }


def _tool_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "required": ["input"],
        "properties": {
            "input": {"type": "string"},
            "project_path": {"type": "string"},
            "output_dir":   {"type": "string"},
            "job_name":     {"type": "string"},
        },
    }


_DESCRIPTIONS = {
    "prove":          "Send a Lean theorem to Gauss /prove and get back a proof attempt. Async — returns a job id; result file appears when ready.",
    "formalize":      "Convert natural-language math into Lean 4 via Gauss /formalize. Async.",
    "autoformalize":  "Aggressively autoformalize a longer math passage via Gauss /autoformalize. Async, can take minutes.",
    "draft":          "Ask Gauss to draft a Lean proof skeleton via /draft. Async.",
    "review":         "Ask Gauss to review existing Lean code via /review. Async.",
    "autoprove":      "Hand a goal to Gauss's autoprover via /autoprove. Async, can take minutes.",
    "refactor":       "Ask Gauss to refactor Lean code via /refactor. Async.",
    "golf":           "Ask Gauss to golf (shorten) a proof via /golf. Async.",
}


async def list_tools_impl() -> list[Tool]:
    tools: list[Tool] = [
        Tool(
            name=f"gauss_{cmd}",
            description=_DESCRIPTIONS[cmd],
            inputSchema=_tool_schema(),
        )
        for cmd in WORKFLOW_COMMANDS
    ]
    tools += [
        Tool(
            name="gauss_job_status",
            description="Read the current status of a job (running, done, error, stalled).",
            inputSchema={
                "type": "object",
                "required": ["job_id"],
                "properties": {"job_id": {"type": "string"}},
            },
        ),
        Tool(
            name="gauss_job_result",
            description="Return the parsed result JSON for a finished job. Errors if still running.",
            inputSchema={
                "type": "object",
                "required": ["job_id"],
                "properties": {"job_id": {"type": "string"}},
            },
        ),
        Tool(
            name="gauss_list_jobs",
            description="List recent jobs in the default or given output dir.",
            inputSchema={
                "type": "object",
                "properties": {
                    "limit":      {"type": "integer", "default": 20},
                    "status":     {"type": "string"},
                    "output_dir": {"type": "string"},
                },
            },
        ),
        Tool(
            name="gauss_set_project",
            description="Set the sticky project directory used for future Gauss calls.",
            inputSchema={
                "type": "object",
                "required": ["path"],
                "properties": {"path": {"type": "string"}},
            },
        ),
        Tool(
            name="gauss_status",
            description="Report sticky project, default output dir, and resolver readiness.",
            inputSchema={"type": "object", "properties": {}},
        ),
    ]
    return tools


def _find_job_file(job_id: str) -> Path:
    p = DEFAULT_OUTPUT_DIR / f"{job_id}.json"
    if p.exists():
        return p
    raise FileNotFoundError(f"job not found: {job_id}")


async def call_tool_impl(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    def text(obj: Any) -> list[TextContent]:
        return [TextContent(type="text", text=json.dumps(obj, indent=2))]

    if name.startswith("gauss_") and name[6:] in WORKFLOW_COMMANDS:
        cmd = name[6:]
        result = _spawn_worker(
            command=cmd,
            input_text=arguments["input"],
            project_path=arguments.get("project_path"),
            output_dir=arguments.get("output_dir"),
            job_name=arguments.get("job_name"),
        )
        return text(result)

    if name == "gauss_job_status":
        f = _find_job_file(arguments["job_id"])
        data = jobs.read_job(f)
        if jobs.is_stalled(f):
            data["status"] = "stalled"
        return text(data)

    if name == "gauss_job_result":
        f = _find_job_file(arguments["job_id"])
        data = jobs.read_job(f)
        if data["status"] == "running":
            raise RuntimeError(f"job {arguments['job_id']} still running")
        return text(data)

    if name == "gauss_list_jobs":
        out_dir = _resolve_output_dir(arguments.get("output_dir"))
        files = sorted(out_dir.glob("*.json"), reverse=True)
        limit = arguments.get("limit", 20)
        wanted = arguments.get("status")
        out: list[dict[str, Any]] = []
        for f in files:
            d = jobs.read_job(f)
            if wanted and d["status"] != wanted:
                continue
            out.append({"job_id": d["job_id"], "status": d["status"], "command": d["command"]})
            if len(out) >= limit:
                break
        return text(out)

    if name == "gauss_set_project":
        s = state.State.load()
        s.project_path = arguments["path"]
        s.save()
        return text({"project_path": s.project_path})

    if name == "gauss_status":
        s = state.State.load()
        return text({
            "sticky_project": s.project_path,
            "default_output_dir": str(DEFAULT_OUTPUT_DIR),
            "valid_commands": sorted(WORKFLOW_COMMANDS),
        })

    raise ValueError(f"unknown tool: {name}")


# Register the handlers with the MCP Server via its decorator API.
# mcp 1.27 decorators return a wrapper; we keep the original impls as
# module-level names so tests can call them directly without routing through
# the JSON-RPC request dispatcher.
server.list_tools()(list_tools_impl)
server.call_tool()(call_tool_impl)


async def main_async() -> None:
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())


def main() -> None:
    asyncio.run(main_async())
