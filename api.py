from fastapi import FastAPI
from pydantic import BaseModel

from tools import (
    add_task,
    list_tasks,
    remove_task
)

app = FastAPI(
    title="AI Task Manager Agent",
    description="Task Management Agent API",
    version="1.0"
)


class TaskRequest(BaseModel):
    task: str


@app.get("/")
def root():

    return {
        "message": "Agent Running"
    }


@app.get("/tasks")
def get_tasks():

    return {
        "tasks": list_tasks()
    }


@app.post("/add-task")
def create_task(request: TaskRequest):

    result = add_task(
        request.task
    )

    return {
        "result": result
    }


@app.post("/remove-task")
def delete_task(request: TaskRequest):

    result = remove_task(
        request.task
    )

    return {
        "result": result
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }