from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Result 모델에 대한 Pydantic 스키마
class ResultSchema(BaseModel):
    id: Optional[int] = None
    mark: Optional[bool] = None
    grade: Optional[str] = None
    environment: Optional[str] = None
    social: Optional[str] = None
    governce: Optional[str] = None
    result: Optional[str] = None
    certified: Optional[bool] = None
    product: Optional[str] = None
    company: Optional[str] = None
    articles: List['ArticleSchema'] = []  # ArticleSchema 인스턴스의 리스트 추가
    esgs: List['EsgSchema'] = []  # EsgSchema 인스턴스의 리스트 추가
    class Config:
        orm_mode = True

# Article 모델에 대한 Pydantic 스키마
class ArticleSchema(BaseModel):
    url: Optional[str] = None
    title: Optional[str] = None
    result_id: Optional[int] = None

    class Config:
        orm_mode = True



class EsgSchema(BaseModel):
    id: Optional[int] = None
    keyword: Optional[str] = None
    context: Optional[str] = None
    result_id: int

    class Config:
        orm_mode = True

# Result와 Article을 연결하는 스키마가 필요한 경우, ArticleSchema 내에 ResultSchema를 포함시켜 관계를 나타낼 수 있습니다.
class ArticleWithResultSchema(ArticleSchema):
    result: ResultSchema


class requestItem(BaseModel):
    company: str
    product: str


class KeyWordSchema(BaseModel):
    keyword: Optional[str] = None
    result_id: Optional[int] = None
    class Config:
        orm_mode = True


class PostResultSchema(BaseModel):
    id: Optional[int] = None
    mark: Optional[bool] = None
    grade: Optional[str] = None
    environment: Optional[str] = None
    social: Optional[str] = None
    governce: Optional[str] = None
    result: str
    certified: Optional[bool] = None
    product: Optional[str] = None
    company: Optional[str] = None
    class Config:
        orm_mode = True