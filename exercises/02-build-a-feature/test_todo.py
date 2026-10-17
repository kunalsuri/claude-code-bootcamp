import pytest

import todo


@pytest.fixture(autouse=True)
def temp_data_file(tmp_path, monkeypatch):
    monkeypatch.setattr(todo, "DATA_FILE", str(tmp_path / "todo.json"))


def test_add_and_load():
    todo.add_task("buy milk")
    assert todo.load_tasks() == [{"title": "buy milk", "done": False}]


def test_format_tasks():
    todo.add_task("buy milk")
    assert todo.format_tasks(todo.load_tasks()) == "1. [ ] buy milk"
