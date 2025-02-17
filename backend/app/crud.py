from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

async def get_faq_by_question(db: AsyncSession, question: str):
    result = await db.execute(select(models.FAQ).filter(models.FAQ.question == question))
    return result.scalars().first()

async def get_faq_list(db: AsyncSession):
    result = await db.execute(select(models.FAQ))
    return result.scalars().all()

async def create_faq(db: AsyncSession, faq: schemas.FAQCreate):
    new_faq = models.FAQ(**faq.dict())
    db.add(new_faq)
    await db.commit()
    await db.refresh(new_faq)
    return new_faq
