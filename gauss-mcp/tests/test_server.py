import asyncio

from gauss_mcp.server import list_tools_impl


def test_server_lists_all_tools(tmp_state_dir):
    tools = asyncio.run(list_tools_impl())
    names = {t.name for t in tools}
    assert "gauss_prove" in names
    assert "gauss_formalize" in names
    assert "gauss_status" in names
    assert "gauss_job_status" in names
    assert "gauss_new_session" not in names  # path-B: removed
    # 8 workflow + 5 control = 13 total
    assert len(names) == 13
