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

    tasks.append(
        {
            "task": task,
            "completed": False,
            "priority": "Medium"
        }
    )

    save_tasks(tasks)

    return f"Added task: {task}"


def list_tasks():
    return load_tasks()


def remove_task(task):

    tasks = load_tasks()

    filtered = [
        t for t in tasks
        if t["task"].lower() != task.lower()
    ]

    save_tasks(filtered)

    return f"Removed task: {task}"


def complete_task(task):

    tasks = load_tasks()

    for t in tasks:
        if t["task"].lower() == task.lower():
            t["completed"] = True
            save_tasks(tasks)
            return f"Completed task: {task}"

    return f"Task not found: {task}"


def update_priority(task, priority):

    tasks = load_tasks()

    for t in tasks:
        if t["task"].lower() == task.lower():
            t["priority"] = priority
            save_tasks(tasks)
            return f"Priority updated to {priority}"

    return f"Task not found: {task}"


def search_tasks(keyword):

    tasks = load_tasks()

    return [
        t for t in tasks
        if keyword.lower()
        in t["task"].lower()
    ]


def delete_all_tasks():

    save_tasks([])

    return "All tasks deleted"