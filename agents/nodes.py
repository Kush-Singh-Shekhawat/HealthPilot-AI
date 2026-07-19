from langchain_core.messages import SystemMessage

from config.llm import llm

from agents.prompts import SYSTEM_PROMPT

from agents.tools import (
    add_medication,
    list_medications,
    log_health_metric,
)

llm_with_tools = llm.bind_tools(
    [
        add_medication,
        list_medications,
        log_health_metric,
    ]
)


def assistant(state):
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"],
    ]

    response = llm_with_tools.invoke(messages)

    return {
        "messages": [response]
    }