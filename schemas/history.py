from pydantic import BaseModel,Field,ConfigDict
from datetime import datetime
from schemas.base import NewsItemBase

class HistoryAddRequest(BaseModel):
    news_id:int=Field(...,alias="newsId")


class HistoryNewsItemResponse(NewsItemBase) :
    history_id:int=Field(alias="historyId")
    history_time:datetime=Field(alias="historyTime")

    model_config=ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )

class HistoryListResponse(BaseModel):
    list: list[HistoryNewsItemResponse]
    total: int
    has_more: bool = Field(alias="hasMore")

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )
