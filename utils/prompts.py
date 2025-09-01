from langchain_core.prompts import PromptTemplate

"""classifier_tools.py"""
classifier_template = """Ты классифицируешь ввод пользователя на такие группы(Math, History, English).Вывод должен быть одним из этих слов.
Ввод ученика: {question}
Твой вывод:"""
classifier = PromptTemplate(
    template=classifier_template,
    input_variables=["question"]
)



"""english_tools.py"""
english_template = """Ты учитель Английского языка.
Объясняй простыми словами и будь креативным.
Вопрос ученика: {question}
Твой ответ:"""
english = PromptTemplate(
    template=english_template,
    input_variables=["question"]
)



"""history_tools.py"""
history_template = """Ты учитель истории Казахстана.
Объясняй простыми словами и будь креативным.
Вопрос ученика: {question}
Твой ответ:"""
history = PromptTemplate(
    template=history_template,
    input_variables=["question"]
)



"""memory.py"""
memory_template = "Ты обычный агент для помощт человеку.Используешь чат истории: {chat_history}, отвечай на вопрос: {question}"
memory_prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template=memory_template
)