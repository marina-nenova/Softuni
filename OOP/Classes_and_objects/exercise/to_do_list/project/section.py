from Classes_and_objects.exercise.to_do_list.project.task import Task


class Section:
    def __init__(self, name:str):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        if any([existing_task.name == task.name for existing_task in self.tasks]):
            return f"Task is already in the section {self.name}"
        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = [task for task in self.tasks if task.completed]
        self.tasks = [task for task in self.tasks if not task.completed]
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        output = f"Section {self.name}:"
        for task in self.tasks:
            output += f"\n{task.details()}"
        return output