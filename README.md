# LangGraph AI Tutor Agent 

Интеллектуальный агент, созданный с использованием LangGraph и LangChain, который классифицирует вопросы пользователя и отвечает на них по математике, истории или английскому языку.  
Проект включает в себя:

-  LLM-интеграцию (Together AI)
-  Ветвление с помощью LangGraph
-  Кастомные инструменты (`Tool`)
-  Память диалога (`RunnableWithMessageHistory`)
-  Расширяемую архитектуру под новые предметы и навыки

## Запуск
```bash
pip install -r requirements.txt
python agent.py
