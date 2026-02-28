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





"""

@router.get("/list")
async def get_favorite_list(
    page:int=Query(1,ge=1),
    page_size:int=Query(10,ge=1,le=100,alias="pageSize"),
    user:User=Depends(get_current_user),
    db:AsyncSession=Depends(get_db)
):
    rows,total=await favorite.get_favorite_list(db,user.id,page,page_size)
    favorite_list = [{
        **news.__dict__,
        "favorite_time": favorite_time,
        "favorite_id": favorite_id
    } for news, favorite_time, favorite_id in rows]
    has_more = total > page * page_size

    data = FavoriteListResponse(list=favorite_list, total=total, hasMore=has_more)
    return success_response(message="获取收藏列表成功", data=data)
"""