from tools import (
    add_task,
    list_tasks,
    remove_task
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
        "(add/list/remove/exit)\n> "
    ).strip()

    if command.lower() == "exit":

        print("Goodbye")

        break

    decision = approval_node()

    if decision.lower() != "yes":

        print("Action rejected")

        continue

    result = ""

    command_lower = command.lower()

    try:

        if command_lower.startswith("add"):

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

        elif "list" in command_lower:

            result = list_tasks()

        else:

            result = (
                "Unknown command. "
                "Use add, list, remove or exit."
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