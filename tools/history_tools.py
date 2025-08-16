"""
    history_tools.py:
        Тулз для взаимодействие с LLM по английскому.
    TODO:
        1.Убрать промты в отдельный утилиту.
        2.Добавить memory в LLM
        3.Соединить с состояние GraphState(ибо не будет работать только потому что агент наследует состояние при инициализации)
"""


from langchain_core.prompts import PromptTemplate
from langchain_together import Together

from utils.prompts import history
from configs.settings import load_configs
from utils.states import GraphState

config = load_configs()

llm = Together(
    model=config["agent"]["model"],
    temperature=config["agent"]["temperature"],
    max_tokens=config["agent"]["max_tokens"],
    together_api_key=config["agent"]["together_api_key"]
)
prompt = history
chain = prompt | llm

def history(state: GraphState) -> GraphState:
    state.answer = chain.invoke({"question": state.text})
    return state

