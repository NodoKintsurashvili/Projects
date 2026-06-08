from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import engine, get_db
from models import Task, Base
from typing import Optional

Base.metadata.create_all(bind=engine)
app = FastAPI()

class TaskCreate(BaseModel):
  title: str
  completed: Optional[bool] = False

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
  return db.query(Task).all()


@app.get("/tasks/{id}")
def get_task(id: int, db: Session = Depends(get_db)):
  task = db.query(Task).filter(Task.id == id).first()

  if not task:
    raise HTTPException(status_code=404, detail="Task not found")
  
  return task


@app.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
  new_task = Task(title=task.title, completed=task.completed)
  db.add(new_task)
  db.commit()
  db.refresh(new_task)

  return new_task


@app.put("/tasks/{id}")
def update_task(id: int, task: TaskCreate, db: Session = Depends(get_db)):
  existing = db.query(Task).filter(Task.id == id).first()

  if not existing:
    raise HTTPException(status_code=404, detail= "Task not found")
  
  existing.title  = task.title
  existing.completed = task.completed

  db.commit()
  db.refresh(existing)
  return existing


@app.delete("/tasks/{id}")
def delete_task(id: int, db: Session= Depends(get_db)):
  task = db.query(Task).filter(Task.id == id).first()

  if not task:
    raise HTTPException(status_code=404, detail= "Task not found")
  
  db.delete(task)
  db.commit()

  return {"message": "Task deleted"}