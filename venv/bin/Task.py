class Task:
    def __init__(self, task_name, task_description, deadline, priority, for_whom):
        self.task_name = task_name
        self.task_description = task_description
        self.deadline = deadline
        self.priority = priority
        self.for_whom = for_whom