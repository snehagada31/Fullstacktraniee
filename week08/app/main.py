from fastapi import FastAPI

from app.routers.tasks import router as tasks_router


app = FastAPI(
    title="FastAPI Tasks API",
    description="Week 08 - FastAPI CRUD API with Dependency Injection",
    version="1.0.0",
)


app.include_router(tasks_router)


@app.get("/")
def root():
    return {"message": "FastAPI Tasks API is running"}