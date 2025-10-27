# arquivo que contém os schemas Pydantic para a API de tarefas
# esses schemas definem a estrutura dos dados que serão enviados e recebidos pela API

from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskPublic(BaseModel):
    id: int
    title: str
    description: str 
    is_done: bool = False
    created_at: str
    updated_at: str