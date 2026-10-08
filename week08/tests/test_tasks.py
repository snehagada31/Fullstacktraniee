from fastapi.testclient import TestClient

from app.main import app
from app.dependencies import get_tasks_service
from app.schemas.task import TaskResponse


class FakeTasksService:
    def __init__(self):
        self.tasks = [
            TaskResponse(
                id=100,
                title="Fake Task",
                description="Created by fake service",
                completed=False,
            )
        ]

    def get_tasks(self):
        return self.tasks

    def get_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                return task

        return None

    def create_task(self, task):
        new_task = TaskResponse(
            id=101,
            title=task.title,
            description=task.description,
            completed=task.completed,
        )

        self.tasks.append(new_task)
        return new_task

    def update_task(self, task_id: int, task_data):
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

    def delete_task(self, task_id: int):
        task = self.get_task(task_id)

        if task is None:
            return False

        self.tasks.remove(task)
        return True


def get_fake_tasks_service():
    return FakeTasksService()


app.dependency_overrides[get_tasks_service] = get_fake_tasks_service

client = TestClient(app)


def test_get_tasks_with_fake_service():
    response = client.get("/tasks/")

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 100,
            "title": "Fake Task",
            "description": "Created by fake service",
            "completed": False,
        }
    ]


def test_get_task_from_fake_service():
    response = client.get("/tasks/100")

    assert response.status_code == 200
    assert response.json()["title"] == "Fake Task"


def test_get_missing_task():
    response = client.get("/tasks/999")

    assert response.status_code == 404


def test_create_task():
    response = client.post(
        "/tasks/",
        json={
            "title": "New Task",
            "description": "Test task",
            "completed": False,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "New Task"
    assert data["description"] == "Test task"
    assert data["completed"] is False


def test_update_task():
    response = client.put(
        "/tasks/100",
        json={
            "title": "Updated Task",
            "description": "Updated description",
            "completed": True,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated Task"
    assert data["description"] == "Updated description"
    assert data["completed"] is True


def test_delete_task():
    response = client.delete("/tasks/100")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Task deleted successfully"
    }