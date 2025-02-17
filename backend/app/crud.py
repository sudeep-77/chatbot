from sqlalchemy.orm import Session
from . import models, schemas

def get_faq_by_question(db: Session, question: str):
    result = db.query(models.FAQ).filter(models.FAQ.question == question)
    return result.first()

def get_faq_list(db: Session):
    result = db.query(models.FAQ)
    return result.all()

def create_faq(db: Session, faq: schemas.FAQCreate):
    new_faq = models.FAQ(**faq.dict())
    db.add(new_faq)
    db.commit()
    db.refresh(new_faq)
    return new_faq
