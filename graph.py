from tools import (
    add_task,
    list_tasks,
    remove_task,
    complete_task,
    update_priority,
    search_tasks,
    delete_all_tasks
)

from hooks import (
    pre_tool_hook,
    post_tool_hook
)

from summarize import save_checkpoint

from dotenv import load_dotenv
from langfuse import Langfuse

import os

load_dotenv()

langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)


def approval_node():
    return input(
        "Approve action? (yes/no): "
    )


while True:

    command = input(
        "\nWhat would you like to do?\n"
        "(add/list/remove/complete/priority/search/delete all/exit)\n> "
    ).strip()

    command_lower = command.lower()

    if command_lower == "exit":

        print("Goodbye")

        break

    try:

        result = ""

        if command_lower == "delete all":

            decision = approval_node()

            if decision.lower() != "yes":

                print("Action rejected")

                continue

            result = delete_all_tasks()

        elif command_lower.startswith("add"):

            tasks_text = command[3:].strip()

            if not tasks_text:

                result = "Please provide task name"

            else:

                tasks = [
                    task.strip()
                    for task in tasks_text.split(",")
                    if task.strip()
                ]

                outputs = []

                for task in tasks:

                    pre_tool_hook(task)

                    task_result = add_task(task)

                    task_result = post_tool_hook(
                        task_result
                    )

                    outputs.append(task_result)

                result = "\n".join(outputs)

        elif command_lower.startswith("remove"):

            tasks_text = command[6:].strip()

            if not tasks_text:

                result = "Please provide task name"

            else:

                tasks = [
                    task.strip()
                    for task in tasks_text.split(",")
                    if task.strip()
                ]

                outputs = []

                for task in tasks:

                    pre_tool_hook(task)

                    task_result = remove_task(task)

                    task_result = post_tool_hook(
                        task_result
                    )

                    outputs.append(task_result)

                result = "\n".join(outputs)

        elif command_lower.startswith("complete"):

            task = command[8:].strip()

            pre_tool_hook(task)

            result = complete_task(task)

            result = post_tool_hook(result)

        elif command_lower.startswith("priority"):

            parts = command.split()

            if len(parts) < 3:

                result = (
                    "Usage: priority <task> <High/Medium/Low>"
                )

            else:

                priority = parts[-1]

                task = " ".join(parts[1:-1])

                result = update_priority(
                    task,
                    priority
                )

                result = post_tool_hook(result)

        elif command_lower.startswith("search"):

            keyword = command[6:].strip()

            result = search_tasks(keyword)

        elif "list" in command_lower:

            result = list_tasks()

        else:

            result = (
                "Unknown command. "
                "Use add, list, remove, complete, "
                "priority, search, delete all or exit."
            )

        save_checkpoint(
            {
                "last_action": command,
                "result": str(result)
            }
        )

        langfuse.create_event(
            name="agent-action"
        )

        langfuse.flush()

        print("\nResult:")
        print(result)

    except Exception as e:

        print(
            f"Error: {str(e)}"
        )