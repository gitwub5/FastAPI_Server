from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    Text,
    Boolean,
)  # func는 mysql의 함수를 쓸 수 있게 해주는 녀석임
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from .database import Base


class Result(Base):
    __tablename__="result"
    id = Column(Integer, primary_key=True)
    mark = Column(Boolean, nullable=True)
    grade = Column(String, nullable=True)
    environment = Column(String, nullable=True)
    social = Column(String, nullable=True)
    governce = Column(String, nullable=True)
    result = Column(String)

class Article(Base):
    __tablename__="article"
    id = Column(Integer, primary_key=True)
    url = Column(Text)
    result_id = Column(Integer, ForeignKey("result.id"))