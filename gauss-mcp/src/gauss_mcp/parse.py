"""Extract Lean code blocks from Gauss output."""
import re

_LEAN_FENCE = re.compile(
    r"```(?:lean|lean4)\s*\n(.*?)\n```",
    re.DOTALL,
)


def extract_lean_blocks(text: str) -> list[str]:
    return [m.group(1).rstrip() for m in _LEAN_FENCE.finditer(text)]
