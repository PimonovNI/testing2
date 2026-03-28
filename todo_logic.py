class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, text):
        if text is None or text.strip() == "":
            raise ValueError("Task cannot be empty")
        self.tasks.append(text.strip())

    def delete_task(self, index):
        if index is None:
            raise ValueError("Please select a task to delete")
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index is out of range")
        del self.tasks[index]

    def get_tasks(self):
        return self.tasks
