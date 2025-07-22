"""
    memory.py
"""

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain_together import Together
from config import MODEL_NAME, MAX_TOKENS, TEMPERATURE, API_KEY
from langchain_core.prompts import PromptTemplate

llm = Together(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS,
    together_api_key=API_KEY
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