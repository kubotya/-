from fastapi import FastAPI, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import models, database, crud
import random

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/quizzes/")
def create_quiz(question: str, answer: str, db: Session = Depends(get_db)):
    return crud.create_quiz(db, question, answer)

@app.get("/quizzes/")
def read_quizzes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_quizzes(db, skip, limit)

@app.get("/quiz/random/")
def get_random_quiz(db: Session = Depends(get_db)):
    quizzes = crud.get_quizzes(db)
    if not quizzes:
        return {"message": "クイズがありません"}
    quiz = random.choice(quizzes)
    return {"id": quiz.id, "question": quiz.question}

@app.post("/quiz/answer/")
def check_answer(quiz_id: int = Body(...), answer: str = Body(...), db: Session = Depends(get_db)):
    quiz = db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()
    if not quiz:
        return {"result": "not found"}
    if quiz.answer.strip().lower() == answer.strip().lower():
        return {"result": "correct"}
    else:
        return {"result": "incorrect", "correct_answer": quiz.answer}
