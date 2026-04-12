from gauss_mcp.parse import extract_lean_blocks


def test_extract_single_block():
    text = "Here is the proof:\n```lean\ntheorem t : 1 = 1 := rfl\n```\nDone."
    assert extract_lean_blocks(text) == ["theorem t : 1 = 1 := rfl"]


def test_extract_multiple_blocks():
    text = "```lean\nA\n```\nmiddle\n```lean4\nB\n```"
    assert extract_lean_blocks(text) == ["A", "B"]


def test_no_blocks_returns_empty():
    assert extract_lean_blocks("just prose") == []


def test_ignores_other_languages():
    text = "```python\nprint('hi')\n```"
    assert extract_lean_blocks(text) == []
