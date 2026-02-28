from sqlalchemy import select,delete,func
from sqlalchemy.ext.asyncio import AsyncSession
from models.history import History
from models.news import News

async def add_news_history(
        db:AsyncSession,
        user_id:int,
        news_id:int
):
    history=History(user_id=user_id,news_id=news_id)
    db.add(history)
    await db.commit()
    await db.refresh(history)
    return history


