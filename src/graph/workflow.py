from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import MemorySaver

from src.graph.state import get_state, State
from src.graph.nodes import setup_workflow_nodes
from src.chains.info_chain import info_chain
from src.chains.prompt_gen_chain import prompt_gen_chain


def create_workflow() -> StateGraph:
    workflow = StateGraph(State)
    workflow.add_node("info", info_chain)
    workflow.add_node("prompt", prompt_gen_chain)
    setup_workflow_nodes(workflow)

    workflow.add_conditional_edges("info", get_state, ["add_tool_message", "info", END])
    workflow.add_edge("add_tool_message", "prompt")
    workflow.add_edge("prompt", END)
    workflow.add_edge(START, "info")

    return workflow.compile(checkpointer=MemorySaver())
