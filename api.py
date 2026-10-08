from fastapi import FastAPI
from pydantic import BaseModel

from tools import (
    add_task,
    list_tasks,
    remove_task,
    complete_task,
    update_priority,
    search_tasks,
    delete_all_tasks
)

app = FastAPI(
    title="Personal Productivity Assistant",
    description="Task Management Agent API",
    version="1.0"
)


class TaskRequest(BaseModel):
    task: str


class PriorityRequest(BaseModel):
    task: str
    priority: str


class SearchRequest(BaseModel):
    keyword: str


@app.get("/")
def root():
    return {
        "message": "Productivity Assistant Running"
    }


@app.get("/tasks")
def get_tasks():
    return {
        "tasks": list_tasks()
    }


@app.post("/add-task")
def create_task(request: TaskRequest):

    return {
        "result": add_task(request.task)
    }


@app.post("/remove-task")
def delete_task(request: TaskRequest):

    return {
        "result": remove_task(request.task)
    }


@app.post("/complete-task")
def complete(request: TaskRequest):

    return {
        "result": complete_task(request.task)
    }


@app.post("/set-priority")
def priority(request: PriorityRequest):

    return {
        "result": update_priority(
            request.task,
            request.priority
        )
    }


@app.post("/search")
def search(request: SearchRequest):

    return {
        "results": search_tasks(
            request.keyword
        )
    }


@app.delete("/delete-all")
def delete_all():

    return {
        "result": delete_all_tasks()
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }