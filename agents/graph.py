from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from agents.state import AgentState
from agents.nodes import assistant
from agents.tools import add_medication
from agents.tools import list_medications
from agents.tools import log_health_metric

builder = StateGraph(AgentState)

builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(
    [
        add_medication,
        list_medications,
        log_health_metric,
    ]
)
)

builder.add_edge(START, "assistant")

builder.add_conditional_edges(
    "assistant",
    tools_condition,
)

builder.add_edge("tools", "assistant")
builder.add_edge("assistant", END)

graph = builder.compile()