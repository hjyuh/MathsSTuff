# Gauss MCP Server — Design

**Date:** 2026-04-12
**Status:** Approved, ready for implementation plan
**Goal:** Expose math.inc OpenGauss workflows as MCP tools so Claude Desktop can call Gauss as a Lean verification / formalization backend.

## Motivation

OpenGauss is installed and authenticated in WSL with Claude Code as the inference backend. We want Claude Desktop (Windows) to be able to say "let me send this to Gauss for verification" mid-conversation, hand off the work, and pick up the result later. Gauss is an MCP *client*, not a server, so we build a thin wrapper.

All Gauss calls are **fire-and-forget**: tools return immediately with a job handle, Gauss runs in a detached background process, and results land as JSON files Claude can read on the next turn (or whenever the user asks). No timeouts, no blocking the Claude Desktop UI.

## Architecture

```
Claude Desktop (Windows)
   │  stdio over wsl.exe
   ▼
gauss-mcp  (Python, WSL, stdio MCP server)
   │  detached subprocess (setsid)
   ▼
gauss chat -q "/<command>\n\n<input>" -Q --resume <session_id>
   │
   ▼
~/.gauss/  (existing SQLite session store, OAuth creds, config)
```

**State owned by the MCP server** lives in `~/.gauss-mcp/`:

- `state.json` — sticky session ID + sticky project path
- `server.log` — MCP server log, rotated 5×1MB
- `jobs/<job_id>.log` — per-job worker stdout/stderr (kept inside WSL for speed)

**Result files** live in `/mnt/c/Users/z20ma/OneDrive/Documents/!math/gauss-mcp-results/` by default (browseable from Windows). Per-call `output_dir` arg overrides.

**Code location:** `/mnt/c/Users/z20ma/OneDrive/Documents/!math/gauss-mcp/`, installed editable into the existing OpenGauss venv.

## Tool surface (13 tools)

### 8 workflow tools (async, one per Gauss slash command)

`gauss_prove`, `gauss_formalize`, `gauss_autoformalize`, `gauss_draft`, `gauss_review`, `gauss_autoprove`, `gauss_refactor`, `gauss_golf`

**Input schema (all identical):**
```json
{
  "input": "string — theorem, lean code, or natural-language prompt",
  "project_path": "string? — override sticky project",
  "session_id":   "string? — override sticky session",
  "output_dir":   "string? — override default result dir",
  "job_name":     "string? — human label appended to job_id"
}
```

**Return (immediate):**
```json
{
  "job_id":      "2026-04-12T15-22-08-prove-a1b2",
  "status":      "running",
  "output_file": "<output_dir>/<job_id>.json",
  "log_file":    "~/.gauss-mcp/jobs/<job_id>.log",
  "session_id":  "...",
  "started_at":  "2026-04-12T15:22:08Z"
}
```

**Result file (written atomically when worker finishes):**
```json
{
  "job_id": "...",
  "status": "done | error | stalled",
  "session_id": "...",
  "command": "/prove",
  "input": "...",
  "started_at": "...",
  "finished_at": "...",
  "duration_s": 42.1,
  "result_text": "Gauss's final response",
  "lean_code_blocks": ["..."],
  "error": null
}
```

### 5 control tools (synchronous, cheap)

| Tool | Purpose |
|---|---|
| `gauss_job_status(job_id)` | Read result file, return current state. Detects stalled jobs via heartbeat + PID check. |
| `gauss_job_result(job_id)` | Return parsed result JSON if `done`; error if still running. |
| `gauss_list_jobs(limit?, status?)` | List recent jobs from the result dir. |
| `gauss_new_session(project_path?)` | Start a fresh Gauss session, make it sticky, return new ID. |
| `gauss_set_project(path)` | Set the sticky project dir. |
| `gauss_status()` | (extra) Report `gauss --version`, active backend/provider from `~/.gauss/config.yaml`, sticky session/project, default output dir. |

(That's actually 6 control tools — `gauss_status` was added in Section 4 for introspection. Total: 14.)

## Execution model

**On a workflow tool call:**

1. Generate `job_id = YYYY-MM-DDTHH-MM-SS-<command>-<rand4>` (plus `-<job_name>` if given).
2. Resolve session: explicit arg → sticky → create-and-stick.
3. Resolve project: explicit arg → sticky → cwd.
4. Write `<output_dir>/<job_id>.json` with `status: "running"` so status calls work immediately.
5. Spawn detached worker: `setsid python -m gauss_mcp.worker <job_file>` with `start_new_session=True`. Worker is **not** a child of the MCP server — survives MCP/Claude Desktop restart.
6. Return job handle.

**Worker process:**

- Runs `gauss chat -q "/<command>\n\n<input>" -Q --resume <session_id>` with stdio piped to `<job_id>.log`.
- Writes `last_heartbeat_at` into the result file every 5s.
- On clean exit: parses output, extracts ` ```lean ` fences, builds result JSON, atomic write via `tmp + os.replace`.
- On crash: writes `status: "error"`, `error.type: "worker_crash"`, last 50 log lines.

**Crash recovery:**

- MCP server restart → no impact, worker is detached.
- Worker crash without writing → `gauss_job_status` detects: heartbeat >60s old AND PID gone → marks `status: "stalled"`.

**Concurrency / session collisions:**

If two workflow calls target the **same** session simultaneously, the second worker **auto-queues** behind the first via a per-session file lock (`~/.gauss-mcp/locks/<session_id>.lock`, `fcntl.flock`). Fire-and-forget from Claude's perspective; it just takes longer. Fresh sessions don't contend.

## Error handling

| Class | Surfaces as | Example |
|---|---|---|
| Gauss exited non-zero | Result file `status: "error"`, `error.type: "gauss_exit"` | bad slash command, model API down |
| Lean compilation failure | Result file `status: "done"`, `error.type: "lean_error"`, full diagnostic in `result_text` | proof has a hole; Claude reads and reacts |
| Worker crashed | Result file `status: "error"`, `error.type: "worker_crash"`, log tail attached | Python exception |
| Stalled (no heartbeat) | `gauss_job_status` returns `status: "stalled"` | machine sleep, OOM kill |
| Session not found | MCP protocol error from the failing tool call | bad explicit `session_id` |
| `gauss` not on PATH | MCP protocol error at server startup | install broken |
| Output dir not writable | MCP protocol error from the failing call | permissions |

**Principle:** anything Claude can usefully react to → result file. Anything that means "the wrapper is broken" → MCP protocol error so Claude Desktop shows it red.

## Config & discovery

Zero-config. No `~/.gauss-mcp/config.toml`.

On startup the server:

1. Locates `gauss` via `shutil.which`, falls back to `~/.local/bin/gauss`. Fails loudly if neither exists.
2. Reads `~/.gauss/config.yaml` for backend/provider info — surfaced via `gauss_status()`, never modified.
3. Reads/creates `~/.gauss-mcp/state.json`.
4. Reads/creates the default Windows-side output dir.

Per-call args (`output_dir`, `project_path`, `session_id`) are the only knobs.

## Project layout

```
!math/gauss-mcp/
├── pyproject.toml
├── README.md
├── src/gauss_mcp/
│   ├── __init__.py
│   ├── __main__.py        # python -m gauss_mcp → starts MCP server
│   ├── server.py          # MCP tool registration, stdio loop
│   ├── jobs.py            # job_id, file layout, atomic writes, heartbeat, locks
│   ├── worker.py          # python -m gauss_mcp.worker runs one job
│   ├── gauss_cli.py       # subprocess wrapper, slash-command builder
│   ├── state.py           # sticky session/project file
│   └── parse.py           # extract lean fences, build result JSON
└── tests/
    ├── test_jobs.py
    ├── test_parse.py
    ├── test_state.py
    └── test_integration.py  # @pytest.mark.integration
```

## Testing strategy

**Unit (pytest, no Gauss):** job-id generation, atomic writes, stale-heartbeat detection, slash-command builder, state file load/save, result parsing from canned Gauss output samples.

**Integration (one test, marked slow):** real `gauss chat -q "hello" -Q` against a throwaway session. Verifies job file appears, transitions `running → done`, result text non-empty. Skipped if `gauss` not on PATH.

**Manual smoke in Claude Desktop:** add to `claude_desktop_config.json`, restart, verify `gauss_status()` works, formalize a one-liner, check result file appears in `!math/gauss-mcp-results/`, follow-up call reuses sticky session.

No full TDD. Tests written alongside code, with test-first only for slash-command dispatch and result parsing (highest silent-failure risk).

## Install & wiring

**Inside WSL:**
```bash
cd /mnt/c/Users/z20ma/OneDrive/Documents/!math/gauss-mcp
source ~/OpenGauss/venv/bin/activate
pip install -e .
pip install mcp
```

**`%APPDATA%\Claude\claude_desktop_config.json`:**
```json
{
  "mcpServers": {
    "gauss": {
      "command": "wsl",
      "args": ["-e", "bash", "-lc",
               "source ~/OpenGauss/venv/bin/activate && python -m gauss_mcp"]
    }
  }
}
```

The `bash -lc` form is necessary to avoid the broken Windows-path entries in the default WSL `$PATH`.

## Open questions / risks

- **Slash-command-via-`-q` assumption:** untested. Need an early smoke test that `gauss chat -q "/prove ..."` actually invokes the slash command, vs. treating it as literal text. If it doesn't work, we fall back to driving Gauss via a tiny PTY transcript or by importing Gauss internals from the same venv.
- **Default output dir on `/mnt/c`:** writes are slow. Result JSONs are tiny so this is fine; logs stay inside WSL.
- **Single sticky session across multiple Claude Desktop conversations:** if the user runs two Claude Desktop chats at once, they'll share state. Acceptable per design; explicit `session_id` overrides exist.
- **`mcp` Python SDK compatibility:** pin a known version in `pyproject.toml`.

## Decisions log (for future-me)

- Q1 → Tool-style wrapping with hidden session continuity (Claude as driver, Gauss as backend).
- Q2 → 1:1 mapping of slash commands to tools (option C).
- Q3 → Persistent shared session (option A).
- Q4 → Sticky default + explicit override (option D).
- Q5 → Python MCP server in WSL, stdio (option A).
- Q6 → All calls fire-and-forget with file-based results (variant of B, no polling tool needed beyond `gauss_job_status`).
- Q7 → Structured JSON returns (option B).
- Q8 → Sticky project + per-call override (option C).
- Q9 → Code in `!math/gauss-mcp/` (option A).
- Q10 → Zero-config (option A).
- Q11 → Mixed errors: result-file vs MCP protocol (option C).
- Q12 → Light tests + integration smoke (option A).
- Default output dir → `!math/gauss-mcp-results/` (option B for browseability).
- Logs dir → `~/.gauss-mcp/jobs/` inside WSL (option B for speed).
- Concurrency → auto-queue same-session calls via file lock (option A).
