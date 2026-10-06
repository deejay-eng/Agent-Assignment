from fastapi import FastAPI
from tools import add_task, list_tasks

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Agent Running"
    }


@app.post("/add-task")
def create_task(task: str):

    result = add_task(task)

    return {
        "result": result
    }


@app.get("/tasks")
def get_tasks():

    return {
        "tasks": list_tasks()
    }