from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define a Pydantic model for Task
class Task(BaseModel):
    id: int
    description: str
    completed: bool

# Sample data for tasks
tasks = [
    {"id": 1, "description": "Task 1", "completed": False},
    {"id": 2, "description": "Task 2", "completed": False},
]

# Create a task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks.append(task.dict())
    return task

# Get a task by id
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Get a task by description
@app.get("/tasks/description/{description}", response_model=Task)
def read_task_by_description(description: str):
    for task in tasks:
        if task["description"] == description:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Delete a task by id
@app.delete("/tasks/{task_id}")
def delete_task_by_id(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

# Delete a task by description
@app.delete("/tasks/description/{description}")
def delete_task_by_description(description: str):
    for i, task in enumerate(tasks):
        if task["description"] == description:
            del tasks[i]
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

# Update a task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks[i] = task.dict()
            return task
    raise HTTPException(status_code=404, detail="Task not found")
