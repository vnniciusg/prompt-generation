from typing import Any

from langgraph.graph import StateGraph
from langchain_core.messages import ToolMessage

from src.graph.state import State


def add_tool_message(state: State) -> dict[str, Any]:
    return {
        "messages": [
            ToolMessage(
                content="Prompt generated!",
                tool_call_id=state["messages"][-1].tool_calls[0]["id"],
            )
        ]
    }


def setup_workflow_nodes(workflow: StateGraph) -> None:
    workflow.add_node("add_tool_message", add_tool_message)
