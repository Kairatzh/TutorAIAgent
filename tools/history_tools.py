"""
    history_tools.py
"""


from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_together import Together
from configs.settings import load_configs

config = load_configs()

llm = Together(
    model=config["agent"]["model"],
    temperature=config["agent"]["temperature"],
    max_tokens=config["agent"]["max_tokens"],
    together_api_key=config["agent"]["together_api_key"]
)


prompt_template = """Ты учитель истории Казахстана.
Объясняй простыми словами и будь креативным.
Вопрос ученика: {question}
Твой ответ:"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["question"]
)

chain = prompt | llm

def historic_boy(text: str) -> str:
    return chain.invoke({"question": text})

history_tool = Tool(
    name="KazakhHistoryTool",
    func=historic_boy,
    description="Отвечает на вопросы по истории Казахстана простыми словами"
)
