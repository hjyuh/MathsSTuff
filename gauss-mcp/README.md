# gauss-mcp

A Python MCP server that wraps math.inc OpenGauss workflows for Claude Desktop.
It exposes each Gauss workflow (`/prove`, `/formalize`, etc.) as a fire-and-forget
MCP tool: the server dispatches a detached worker, returns immediately with a job
id, and writes the final result to a JSON file you can read back with a separate
tool call.

## Architecture

Claude Desktop spawns this server inside WSL over stdio. Each workflow tool call
uses `gauss_cli.autoformalize.resolve_autoformalize_request` (in-process) to
build the Claude Code subprocess argv for the requested workflow, then detaches
a worker that runs that subprocess, captures stdout/stderr, and writes a result
JSON to a configurable output directory. The control tools (`gauss_job_status`,
`gauss_job_result`, `gauss_list_jobs`) are thin readers over that directory and
the per-job log files. See the design docs for the full rationale:

- `../docs/plans/2026-04-12-gauss-mcp-server-design.md`
- `../docs/plans/2026-04-12-gauss-mcp-server-amendment.md`

## Tools

### Workflow tools (8)

Each takes `input: str` plus optional `project_path`, `output_dir`, `job_name`,
and returns `{job_id, status: "running", output_file, log_file, started_at}`.

- `gauss_prove` — run the Gauss `/prove` workflow on a problem statement.
- `gauss_formalize` — run `/formalize` to turn an informal statement into Lean.
- `gauss_autoformalize` — run `/autoformalize` (formalize + sanity check loop).
- `gauss_draft` — run `/draft` to produce an informal proof sketch.
- `gauss_review` — run `/review` over an existing proof or draft.
- `gauss_autoprove` — run `/autoprove` (draft + prove pipeline).
- `gauss_refactor` — run `/refactor` on an existing Lean artifact.
- `gauss_golf` — run `/golf` to shorten an existing Lean proof.

### Control tools (5)

- `gauss_job_status(job_id)` — returns `running`, `done`, `error`, or `stalled`.
- `gauss_job_result(job_id)` — returns the parsed result JSON once the job is done.
- `gauss_list_jobs(limit?, status?, output_dir?)` — list recent jobs in the output dir.
- `gauss_set_project(path)` — set the sticky project path used by subsequent calls.
- `gauss_status()` — server info: sticky project, default output dir, version.

## Install

Inside WSL, in the OpenGauss venv:

```bash
~/OpenGauss/venv/bin/python -m pip install -e ".[dev]"
```

Then add the server to `%APPDATA%\Claude\claude_desktop_config.json` under
`mcpServers`:

```json
"gauss": {
  "command": "wsl",
  "args": [
    "-e", "bash", "-lc",
    "cd /mnt/c/Users/z20ma/OneDrive/Documents/!math/gauss-mcp && ~/OpenGauss/venv/bin/python -m gauss_mcp"
  ]
}
```

Restart Claude Desktop. The `gauss` server should appear in the MCP panel and
all 13 tools should be listed.

## Usage

Set a sticky project once per session, then call workflow tools without having
to pass `project_path` each time:

```python
gauss_set_project("/home/you/OpenGauss/projects/imo-2024-p1")
gauss_prove(input="Prove that ...")
# -> {"job_id": "j_20260412_...", "status": "running", ...}

gauss_job_status("j_20260412_...")
# -> {"status": "done"}

gauss_job_result("j_20260412_...")
# -> {...parsed result JSON...}
```

## Where results land

- **Results (Windows-visible):** `/mnt/c/Users/z20ma/OneDrive/Documents/!math/gauss-mcp-results/<job_id>.json`
- **Per-job logs (WSL):** `~/.gauss-mcp/jobs/<job_id>.log`

Both paths can be overridden per-call via `output_dir`, or globally via the
server's default output dir.

## Sticky project

`gauss_set_project(path)` must point at a real Gauss project, i.e. a directory
containing `.gauss/project.yaml`. The resolver rejects anything else with a
`resolver_failure` error. To create a project, run `gauss /project init`
interactively inside the target directory before calling `gauss_set_project`.

## Troubleshooting

- **`gauss` server fails to start in Claude Desktop:** check
  `%APPDATA%\Claude\logs\mcp*.log` for the stderr from the WSL command. Usually
  a bad path or a venv that no longer exists.
- **Tool call returns `resolver_failure`:** the project path isn't a Gauss
  project. Run `gauss /project init` (interactive) inside the directory, then
  call `gauss_set_project` again.
- **Tool call returns `gauss_exit`:** the spawned Claude Code child returned
  non-zero. Read `<output_dir>/<job_id>.log` for the actual stderr from Gauss.
- **Job stays in `running` forever:** call `gauss_job_status(job_id)`. If it
  returns `stalled`, the worker process died; the per-job log usually has the
  reason.
- **Editable install regenerates `egg-info` after `pip install`:** harmless,
  covered by `.gitignore`.

## Pinned versions

This server depends on an OpenGauss internal symbol,
`gauss_cli.autoformalize.resolve_autoformalize_request`, which is **not a public
API**. If you upgrade OpenGauss and the wrapper breaks with an `ImportError`,
the resolver function has probably moved. Verify with:

```bash
python -c "from gauss_cli.autoformalize import resolve_autoformalize_request"
```

and update `gauss_mcp/resolver.py` accordingly. Last tested against Gauss
v0.2.2 (2026-04-05).

## Design docs

- `../docs/plans/2026-04-12-gauss-mcp-server-design.md` — original design.
- `../docs/plans/2026-04-12-gauss-mcp-server-amendment.md` — amendment (path-B,
  in-process resolver, fire-and-forget workers).
