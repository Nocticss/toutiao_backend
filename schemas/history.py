from pydantic import BaseModel,Field,ConfigDict
from datetime import datetime
from schemas.base import NewsItemBase

class HistoryAddRequest(BaseModel):
    news_id:int=Field(...,alias="newsId")