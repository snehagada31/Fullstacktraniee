from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_tasks_service
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services.tasks_service import TasksService


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    service: TasksService = Depends(get_tasks_service)
):
    return service.create_task(task)


@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    completed: bool | None = None,
    service: TasksService = Depends(get_tasks_service)
):
    tasks = service.get_tasks()

    if completed is None:
        return tasks

    return [
        task for task in tasks
        if task.completed == completed
    ]


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    service: TasksService = Depends(get_tasks_service)
):
    task = service.get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    service: TasksService = Depends(get_tasks_service)
):
    task = service.update_task(task_id, task_data)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    service: TasksService = Depends(get_tasks_service)
):
    deleted = service.delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {"message": "Task deleted successfully"}