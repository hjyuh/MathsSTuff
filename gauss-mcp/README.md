# gauss-mcp

A Python MCP server that wraps the math.inc OpenGauss CLI so Claude Desktop can invoke Gauss workflows (`/prove`, `/formalize`, etc.) as fire-and-forget tools backed by detached worker subprocesses. See the design doc at `docs/plans/2026-04-12-gauss-mcp-server-design.md` for architecture and rationale.
