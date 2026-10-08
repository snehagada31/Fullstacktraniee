from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse


class TasksService:
    def __init__(self):
        self.tasks: list[TaskResponse] = []
        self.next_id = 1

    def create_task(self, task: TaskCreate) -> TaskResponse:
        new_task = TaskResponse(
            id=self.next_id,
            title=task.title,
            description=task.description,
            completed=task.completed,
        )

        self.tasks.append(new_task)
        self.next_id += 1

        return new_task

    def get_tasks(self) -> list[TaskResponse]:
        return self.tasks

    def get_task(self, task_id: int) -> TaskResponse | None:
        for task in self.tasks:
            if task.id == task_id:
                return task

        return None

    def update_task(
        self,
        task_id: int,
        task_data: TaskUpdate
    ) -> TaskResponse | None:

        task = self.get_task(task_id)

        if task is None:
            return None

        if task_data.title is not None:
            task.title = task_data.title

        if task_data.description is not None:
            task.description = task_data.description

        if task_data.completed is not None:
            task.completed = task_data.completed

        return task

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)

        if task is None:
            return False

        self.tasks.remove(task)
        return True