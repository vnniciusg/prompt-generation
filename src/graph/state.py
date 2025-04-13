from dataclasses import dataclass
from typing import Annotated, TypedDict, Literal, Union

from langchain_core.messages import AnyMessage, AIMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.graph import END


@dataclass(kw_only=True)
class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]


def get_state(state: State) -> Union[Literal["add_tool_message", "info", END], str]:
    last_message = state["messages"][-1]

    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "add_tool_message"

    if not isinstance(last_message, HumanMessage):
        return END

    return "info"
