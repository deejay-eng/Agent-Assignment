from mcp.server.mcpserver import MCPServer

server = MCPServer("TaskAgent")


@server.tool()
def add_task(task: str):
    return f"Added task: {task}"


@server.tool()
def list_tasks():
    return ["Buy Milk"]


print("MCP Server Initialized")


if __name__ == "__main__":
    server.run()