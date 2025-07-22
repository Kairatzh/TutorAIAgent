"""
    history_tools.py
"""


from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_together import Together
from config import API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS

llm = Together(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS,
    together_api_key=API_KEY
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
