from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    tool_result: str
    approval_required: bool