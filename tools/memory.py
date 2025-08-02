"""
    memory.py
"""

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain_together import Together
from configs.settings import load_configs
from langchain_core.prompts import PromptTemplate

config = load_configs()

llm = Together(
    model=config["agent"]["model"],
    temperature=config["agent"]["temperature"],
    max_tokens=config["agent"]["max_tokens"],
    together_api_key=config["agent"]["together_api_key"]
)


prompt_template = "Ты обычный агент для помощт человеку.Используешь чат истории: {chat_history}, отвечай на вопрос: {question}"
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template=prompt_template
)

chain = prompt | llm

# обернуть chain в Runnable с памятью
memory_runnable = RunnableWithMessageHistory(
    chain,
    lambda session_id: ConversationBufferMemory(
        return_messages=True, memory_key="chat_history"
    ),
    input_messages_key="question",
    history_messages_key="chat_history",
)