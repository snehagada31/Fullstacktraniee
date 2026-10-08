from app.services.tasks_service import TasksService


_tasks_service = TasksService()


def get_tasks_service() -> TasksService:
    return _tasks_service