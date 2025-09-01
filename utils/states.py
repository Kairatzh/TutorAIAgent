from typing import List, Dict, Optional
from pydantic import BaseModel

#Состояние графа
class GraphState(BaseModel):
    text: Optional[str] = None
    memory: Optional[List[Dict[str, str]]] = None
    answer: Optional[str] = None
    