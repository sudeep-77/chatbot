from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .database import SessionLocal
from . import crud, schemas, gpt_service

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/faq/", response_model=schemas.FAQResponse)
async def add_faq(faq: schemas.FAQCreate, db: AsyncSession = Depends(get_db)):
    print(faq,'faq')
    return await crud.create_faq(db, faq)

@router.get("/get_faq/", response_model=list[dict])
async def get_faq(db: AsyncSession = Depends(get_db)):
    faq_list = await crud.get_faq_list(db)
    return [{"id":faq.id,"question":faq.question} for faq in faq_list]

@router.get("/ask/")
async def ask_chatbot(question: str, db: AsyncSession = Depends(get_db)):
    existing_faq = await crud.get_faq_by_question(db, question)
    if existing_faq:
        return {"answer": existing_faq.answer}
    else:
        ai_answer = await gpt_service.get_ai_response(question)
        return {"answer": ai_answer}
