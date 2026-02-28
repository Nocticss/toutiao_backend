from fastapi import APIRouter, HTTPException,Query,Depends
from sqlalchemy.ext.asyncio import AsyncSession

from starlette import status
from config.db_conf import get_db
from models.users import User
from utils.auth import get_current_user
from utils.response import success_response
from crud import history
from schemas.history import HistoryAddRequest


router=APIRouter(prefix="/api/history",tags=["history"])

@router.post("/add")
async def add_history(
    data:HistoryAddRequest,
    user:User=Depends(get_current_user),
    db:AsyncSession=Depends(get_db)
):
    result=await history.add_news_history(db,user.id,data.news_id)
    return success_response(message="添加浏览历史记录成功",data=result)

    
