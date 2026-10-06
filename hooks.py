def pre_tool_hook(task):

    print("Running pre-tool hook")

    if len(task) < 3:
        raise Exception("Task too short")

    return True


def post_tool_hook(result):

    print("Running post-tool hook")

    return result