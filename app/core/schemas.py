from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Result 모델에 대한 Pydantic 스키마
class ResultSchema(BaseModel):
    id: Optional[int] = None
    mark: Optional[bool] = None
    grade: Optional[str] = None
    environment: Optional[str] = None
    social: Optional[str] = None
    governce: Optional[str] = None
    result: str

    class Config:
        orm_mode = True

# Article 모델에 대한 Pydantic 스키마
class ArticleSchema(BaseModel):
    id: Optional[int] = None
    url: str
    result_id: int

    class Config:
        orm_mode = True

# Result와 Article을 연결하는 스키마가 필요한 경우, ArticleSchema 내에 ResultSchema를 포함시켜 관계를 나타낼 수 있습니다.
class ArticleWithResultSchema(ArticleSchema):
    result: ResultSchema
