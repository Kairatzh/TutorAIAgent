from typing import List, Dict
from pydantic import BaseModel

#Состояние графа
class GraphState(BaseModel):
    text: str = None
    memory: List[Dict[str, str]] = None
    answer: str = None