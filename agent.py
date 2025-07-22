from typing import List, Dict

from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel

from tools.math_tools import plus_tool, minus_tool
from tools.history_tools import history_tool
from tools.english_tools import english_tool
from tools.classifier_tools import classification_tool
from tools.memory import memory_runnable


class GraphState(BaseModel):
    text: str
    memory: List[Dict[str, str]]

def classify_router_math(state: GraphState):
    text = state.text.strip().lower()
    if "+" in text or "plus" in text:
        return "plus_tool"
    elif "-" in text or "minus" in text:
        return "minus_tool"
    return "plus_tool"


def classify_router(state: GraphState):
    return classification_tool.func(state.text).lower()


workflow = StateGraph(GraphState)

workflow.add_node("Main", RunnableLambda(classify_router))
workflow.add_node("Math", RunnableLambda(classify_router_math))
workflow.add_node("History", history_tool)
workflow.add_node("English", english_tool)
workflow.add_node("PlusMath", plus_tool)
workflow.add_node("MinusMath", minus_tool)
workflow.add_node("Memory", memory_runnable)

workflow.add_conditional_edges(
    "Main",
    classify_router,
    {
        "math": "Math",
        "history": "History",
        "english": "English"
    }
)
workflow.add_conditional_edges(
    "Math",
    classify_router_math,
    {
        "plus_tool": "PlusMath",
        "minus_tool": "MinusMath"
    }
)

workflow.add_edge("Memory", "Main")
workflow.add_edge("History", END)
workflow.add_edge("English", END)
workflow.add_edge("PlusMath", END)
workflow.add_edge("MinusMath", END)

agent = workflow.compile()

def agent_gen(text: str):
    result = agent.invoke(
        input={"text": text, "memory": []},
        config={"configurable": {"session_id": "user1"}}
        )
    return result


print(agent_gen("Сколько будет 12 плюс 30?"))
print(agent_gen("Как образуется Present Continuous?"))
print(agent_gen("Когда была Великая Отечественная война?"))