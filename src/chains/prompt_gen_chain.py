from langchain_core.messages import AIMessage, ToolMessage, SystemMessage, AnyMessage

from src.utils import LLMService
from src.graph.state import State
from src.config.prompts import PROMPT_SYSTEM


def get_prompt_messages(messages: list[AnyMessage]) -> list[SystemMessage]:
    tool_call = None
    other_msgs = []

    for message in messages:
        if isinstance(message, AIMessage) and message.tool_calls:
            tool_call = message.tool_calls[0]["args"]
        elif isinstance(message, ToolMessage):
            continue
        elif tool_call is not None:
            other_msgs.append(message)

    return [SystemMessage(content=PROMPT_SYSTEM.format(reqs=tool_call))] + other_msgs


def prompt_gen_chain(state: State) -> dict:
    messages = get_prompt_messages(state["messages"])
    response = LLMService().get_llm().invoke(messages)
    return {"messages": [response]}
