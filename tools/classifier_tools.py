"""
    classifier_tools.py
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

prompt_template = """Ты классифицируешь ввод пользователя на такие группы(Math, History, English).Вывод должен быть одним из этих слов.
Ввод ученика: {question}
Твой вывод:"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["question"]
)

chain = prompt | llm

def classifier_tool(text: str):
    result = chain.invoke({"question": text})
    return result.strip().lower()


classification_tool = Tool(
    name="ClassifierTool",
    description="Ты должен классифицировать текст",
    func=classifier_tool
)
