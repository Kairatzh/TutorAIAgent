"""
    memory.py
"""

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain_together import Together

from configs.settings import load_configs
from utils.prompts import memory_prompt

config = load_configs()

llm = Together(
    model=config["agent"]["model"],
    temperature=config["agent"]["temperature"],
    max_tokens=config["agent"]["max_tokens"],
    together_api_key=config["agent"]["together_api_key"]
)


prompt = memory_prompt

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