from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
class content(BaseModel):
    title:str
    description:str
    duration:datetime

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
db=[]

@app.get("/")
def root():
    return "Homepage it is!"

@app.post("/info",response_model=content)
def create_info(inp:content):
    db.append(inp)
    return inp

@app.get("/tasks")
def show():
    return db

    
@app.delete("/tasks/{task_index}")
def delete_task(task_index: int):
    if 0 <= task_index < len(db):
        removed = db.pop(task_index)
        return {"message": "Task deleted", "task": removed}
    else:
        raise HTTPException(status_code=404, detail="Task not found")
