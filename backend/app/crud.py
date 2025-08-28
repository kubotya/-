from sqlalchemy.orm import Session
from . import models

def create_quiz(db: Session, question: str, answer: str):
    quiz = models.Quiz(question=question, answer=answer)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz

def get_quizzes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Quiz).offset(skip).limit(limit).all()
