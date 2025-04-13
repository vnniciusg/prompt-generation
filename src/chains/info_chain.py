from typing import Any

from langchain_core.messages import SystemMessage

from src.utils import LLMService
from src.graph.state import State
from src.config.prompts import TEMPLATE
from src.models.prompt_intructions import PromptInstructions


def get_messages_info(messages: list[SystemMessage]) -> list[SystemMessage]:
    return [SystemMessage(content=TEMPLATE)] + messages


def info_chain(state: State) -> dict[str, Any]:
    messages = get_messages_info(state["messages"])
    response = LLMService().bind_tools([PromptInstructions]).invoke(messages)
    return {"messages": [response]}
