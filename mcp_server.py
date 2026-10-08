from mcp.server.mcpserver import MCPServer

from tools import (
    add_task,
    list_tasks,
    remove_task,
    complete_task,
    update_priority,
    search_tasks
)

server = MCPServer("ProductivityAssistant")


@server.tool()
def add_task_tool(task: str):
    return add_task(task)


@server.tool()
def list_tasks_tool():
    return list_tasks()


@server.tool()
def remove_task_tool(task: str):
    return remove_task(task)


@server.tool()
def complete_task_tool(task: str):
    return complete_task(task)


@server.tool()
def update_priority_tool(
    task: str,
    priority: str
):
    return update_priority(
        task,
        priority
    )


@server.tool()
def search_task_tool(
    keyword: str
):
    return search_tasks(keyword)


print("MCP Server Initialized")


if __name__ == "__main__":
    server.run()