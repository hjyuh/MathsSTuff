from gauss_mcp.state import State


def test_load_empty_state(tmp_state_dir):
    s = State.load()
    assert s.project_path is None


def test_save_and_reload(tmp_state_dir):
    s = State.load()
    s.project_path = "/home/user/proj"
    s.save()
    s2 = State.load()
    assert s2.project_path == "/home/user/proj"


def test_state_file_in_gauss_mcp_home(tmp_state_dir):
    s = State.load()
    s.project_path = "/x"
    s.save()
    assert (tmp_state_dir / "state.json").exists()
