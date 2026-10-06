import json
import os

FILE_NAME = "tasks.json"


def load_tasks():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_tasks(tasks):

    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(task):

    tasks = load_tasks()

    tasks.append(task)

    save_tasks(tasks)

    return f"Added task: {task}"

def remove_task(task):

    tasks = load_tasks()

    if task in tasks:

        tasks.remove(task)

        save_tasks(tasks)

        return f"Removed task: {task}"

    return f"Task not found: {task}"

def list_tasks():

    return load_tasks()