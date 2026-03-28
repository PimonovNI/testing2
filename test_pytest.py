import pytest
from todo_logic import TodoList

@pytest.fixture
def todo():
    return TodoList()

@pytest.mark.parametrize("task_input, expected", [
    ("Buy milk", ["Buy milk"]),
    ("Read book", ["Read book"]),
    ("  Do homework  ", ["Do homework"])
])
def test_add_task_parametrized(todo, task_input, expected):
    todo.add_task(task_input)
    assert todo.get_tasks() == expected

def test_add_empty_task_raises(todo):
    with pytest.raises(ValueError, match="Task cannot be empty"):
        todo.add_task("")

def test_delete_without_selection_raises(todo):
    with pytest.raises(ValueError, match="Please select a task to delete"):
        todo.delete_task(None)

@pytest.mark.skip(reason="This feature is not implemented yet")
def test_edit_task(todo):
    pass

@pytest.mark.xfail(reason="Sorting functionality is not implemented yet")
def test_tasks_should_be_sorted(todo):
    pass

def test_wrong_expected_task(todo):
    todo.add_task("Buy milk")
    assert todo.get_tasks() == ["Buy bread"]

def test_wrong_delete_result(todo):
    todo.add_task("Task 1")
    todo.delete_task(0)
    assert todo.get_tasks() == ["Task 1"]
