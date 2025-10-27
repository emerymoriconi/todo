from http import HTTPStatus
from datetime import datetime
from fastapi import FastAPI

from todo_api.schemas import TaskCreate, TaskPublic

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/tasks/{task_id}", response_model=TaskPublic)
def read_task(task_id: int):
    ...


@app.post("/tasks/", status_code=HTTPStatus.CREATED, response_model=TaskPublic)
def create_task(task: TaskCreate):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return TaskPublic(
        id=1,  # Por enquanto um ID fixo, depois implementaremos com banco de dados
        title=task.title,
        description=task.description,
        is_done=False,
        created_at=current_time,
        updated_at=current_time
    )


@app.get("/tasks/", response_model=list[TaskPublic])
def read_tasks():
    ...


@app.put("/tasks/{task_id}", response_model=TaskPublic)
def update_task(task_id: int, task: TaskCreate):
    ...


@app.delete("/tasks/{task_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_task(task_id: int):
    ...