from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, gpt_service,database

router = APIRouter()



@router.post("/faq/", response_model=schemas.FAQResponse)
def add_faq(faq: schemas.FAQCreate, db: Session = Depends(database.get_db)):
    print(faq,'faq')
    return crud.create_faq(db, faq)

@router.get("/get_faq/", response_model=list[dict])
def get_faq(db: Session = Depends(database.get_db)):
    faq_list = crud.get_faq_list(db)
    return [{"id":faq.id,"question":faq.question} for faq in faq_list]

@router.get("/ask/")
async def ask_chatbot(question: str, db: Session = Depends(database.get_db)):
    existing_faq = crud.get_faq_by_question(db, question)
    if existing_faq:
        return {"answer": existing_faq.answer}
    else:
        ai_answer = await gpt_service.get_ai_response(question)
        return {"answer": ai_answer}
