#!/usr/bin/env bash
# Validates that `gauss chat -q "/<slash> ..."` dispatches the slash command.
# Usage: ./scripts/smoke_slash_command.sh
set -euo pipefail

GAUSS=$(command -v gauss || echo "$HOME/.local/bin/gauss")
[ -x "$GAUSS" ] || { echo "gauss not found"; exit 2; }

echo "=== Test 1: literal hello ==="
"$GAUSS" chat -q "say the word PONG and nothing else" -Q 2>&1 | tail -20

echo
echo "=== Test 2: /status slash command (should show status, not echo) ==="
"$GAUSS" chat -q "/status" -Q 2>&1 | tail -30
