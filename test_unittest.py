import unittest
from todo_logic import TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo = TodoList()

    def test_add_task(self):
        self.todo.add_task("Read book")
        self.assertEqual(self.todo.get_tasks(), ["Read book"])

    def test_delete_task(self):
        self.todo.add_task("Read book")
        self.todo.delete_task(0)
        self.assertEqual(self.todo.get_tasks(), [])

    def test_delete_without_selection(self):
        with self.assertRaises(ValueError):
            self.todo.delete_task(None)

if __name__ == "__main__":
    unittest.main()
