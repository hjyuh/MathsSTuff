# MCP Server Setup — Aristotle (Harmonic) + Axle (AxiomMath)
# Windows Setup Guide for Mahmoud
# March 14, 2026

---

## Prerequisites

### Install uv (Python package manager — needed for both)
Open PowerShell and run:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Restart your terminal after installing.

### Install axle CLI
```powershell
pip install axiom-axle --break-system-packages
```
Verify: `axle --version`

---

## 1. Aristotle (Harmonic) — Cloud Theorem Prover

### What it does
- `prove`: Fill in `sorry` statements in Lean code
- `prove_file`: Prove all sorries in a Lean file with Mathlib support
- `formalize`: Convert natural language math → Lean 4 code
- Supports async mode for long-running proofs (minutes to hours)

### Step 1: Get API key
1. Go to https://aristotle.harmonic.fun/
2. Sign up and copy your API key
3. ALSO CHECK: Harmonic has a $1M research sponsorship program for students

### Step 2: Set environment variable
In PowerShell:
```powershell
[System.Environment]::SetEnvironmentVariable("ARISTOTLE_API_KEY", "your-key-here", "User")
```
Restart your terminal.

### Step 3a: Add to Claude Code
```powershell
claude mcp add aristotle -e ARISTOTLE_API_KEY=%ARISTOTLE_API_KEY% -- uvx --from git+https://github.com/septract/lean-aristotle-mcp aristotle-mcp
```

### Step 3b: Add to Claude Desktop
Edit `%APPDATA%\Claude\claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "aristotle": {
      "command": "uvx",
      "args": [
        "--from", "git+https://github.com/septract/lean-aristotle-mcp",
        "aristotle-mcp"
      ],
      "env": {
        "ARISTOTLE_API_KEY": "your-key-here"
      }
    }
  }
}
```
Restart Claude Desktop.

### Usage tips
- Simple proofs: 1-5 minutes
- Complex proofs: can take HOURS
- Use async mode (wait=False) for anything non-trivial
- Lean 4 only (not Lean 3)
- Mathlib dependencies resolved automatically for file-based proving

---

## 2. Axle (AxiomMath) — Lean Verification Engine

### What it does
- `check`: Evaluate Lean code and report all messages
- `verify_proof`: Validate a proof against a formal statement
- `repair_proofs`: Repair broken theorem proofs
- `simplify_theorems`: Simplify proofs
- `extract_theorems`: Split file into separate theorems
- `sorry2lemma`: Extract sorries to standalone lemmas
- `have2sorry`: Replace have statements with sorry
- `merge`: Combine multiple Lean files
- `normalize`: Standardize formatting
- `rename`: Rename declarations
- `disprove`: Attempt to disprove theorems by proving the negation

### Step 1: Get API key (optional but recommended for higher limits)
1. Go to https://axle.axiommath.ai/
2. Sign up if needed
3. Generate API key
4. Note: anonymous users get 10 concurrent requests, API key users get 20

### Step 2: Set environment variable (if using API key)
```powershell
[System.Environment]::SetEnvironmentVariable("AXLE_API_KEY", "your-key-here", "User")
```

### Step 3: Install the MCP wrapper
The Axle MCP server is a community wrapper by Vilin97:
```powershell
git clone https://github.com/Vilin97/axle-mcp.git C:\Users\z20ma\axle-mcp
```

### Step 4a: Add to Claude Code
```powershell
claude mcp add axle -s user -e AXLE_DEFAULT_ENVIRONMENT=lean-4.28.0 -- cmd /c python C:\Users\z20ma\axle-mcp\server.py
```

Note the `cmd /c` wrapper — Windows requires this for Python-based MCP servers.

### Step 4b: Add to Claude Desktop
Edit `%APPDATA%\Claude\claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "axle": {
      "command": "python",
      "args": ["C:\\Users\\z20ma\\axle-mcp\\server.py"],
      "env": {
        "AXLE_DEFAULT_ENVIRONMENT": "lean-4.28.0",
        "AXLE_API_KEY": "your-key-here"
      }
    }
  }
}
```

### OR: Use the axle repo you already cloned
You have the official repo at `C:\Users\z20ma\Documents\MathsSTuff\axiom-lean-engine`.
You can also use axle directly as a Python library in scripts without MCP:
```python
from axle import AxleClient
client = AxleClient()
result = client.check("theorem foo : 1 + 1 = 2 := by norm_num")
```

---

## 3. Verify Both Are Working

### Test Aristotle
In Claude Code or Claude Desktop, ask:
```
Use the aristotle tool to formalize: "For all natural numbers n, n + 0 = n"
```

### Test Axle
In Claude Code or Claude Desktop, ask:
```
Use the axle tool to check this Lean code:
theorem test : 1 + 1 = 2 := by norm_num
```

---

## 4. Combined Config (Claude Desktop)

If you want both in one config file:
```json
{
  "mcpServers": {
    "aristotle": {
      "command": "uvx",
      "args": [
        "--from", "git+https://github.com/septract/lean-aristotle-mcp",
        "aristotle-mcp"
      ],
      "env": {
        "ARISTOTLE_API_KEY": "your-aristotle-key"
      }
    },
    "axle": {
      "command": "python",
      "args": ["C:\\Users\\z20ma\\axle-mcp\\server.py"],
      "env": {
        "AXLE_DEFAULT_ENVIRONMENT": "lean-4.28.0",
        "AXLE_API_KEY": "your-axle-key"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y", "@anthropic/mcp-server-filesystem",
        "C:\\Users\\z20ma\\Documents\\MathsSTuff"
      ]
    }
  }
}
```

---

## Why Both?

**Aristotle** is for PROVING — it fills in sorries, generates proofs from scratch, 
and formalizes natural language. It's the creative engine.

**Axle** is for ENGINEERING — it checks, validates, repairs, simplifies, extracts, 
and transforms existing Lean code. It's the quality control engine.

For the 686 pipeline: you'd use Aristotle to formalize claims into Lean, 
then Axle to verify, simplify, and ensure correctness. They complement each other 
exactly like your multi-model research pipeline.
