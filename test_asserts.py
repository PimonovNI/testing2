from todo_logic import TodoList

def test_add_task():
    todo = TodoList()
    todo.add_task("Buy milk")
    assert todo.get_tasks() == ["Buy milk"]

def test_delete_task():
    todo = TodoList()
    todo.add_task("Buy milk")
    todo.delete_task(0)
    assert todo.get_tasks() == []

def test_add_empty_task():
    todo = TodoList()
    try:
        todo.add_task("")
        assert False
    except ValueError:
        assert True
