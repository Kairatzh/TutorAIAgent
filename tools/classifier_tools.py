"""
    classifier_tools.py
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
