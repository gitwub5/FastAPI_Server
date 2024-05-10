from sqlalchemy.orm import Session, joinedload
from ...core import models, schemas
from typing import List
async def get_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Result).offset(skip).limit(limit).all()

async def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).offset(skip).limit(limit).all()

async def get_article(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()

async def get_result_by_product(db: Session, product: str):
    return db.query(models.Result).options(joinedload(models.Result.articles), joinedload(models.Result.esgs)).filter(models.Result.product == product).first()


async def create_result(db: Session, result: schemas.PostResultSchema):

    # SQLAlchemy 모델 인스턴스 만들기
    db_result = models.Result(
        grade = result.grade,
        environment = result.environment,
        social = result.social,
        governce = result.governce,
        certified = result.certified,
        product = result.product,
        company = result.company
    )
    db.add(db_result)  # DB에 해당 인스턴스 추가하기
    db.commit()  # DB의 변경 사항 저장하기
    db.refresh(db_result)  # 생성된 ID와 같은 DB의 새 데이터를 포함하도록 새로고침
    return db_result

    

# async def create_esg_info(db: Session, info: schemas.EsgSchema):
#     db_result = models.Esg(
#         result_id = info.result_id,
#         keyword = info.keyword
#     )
#     db.add(db_result)
#     db.commit()
#     db.refresh(db_result)
#     return db_result

async def create_esg_info(db: Session, result_id: int, esg_info: List[str]):
    db_results = []
    for keyword in esg_info:
        db_result = models.Esg(
            result_id=result_id,
            keyword=keyword
        )
        db.add(db_result)
        db.commit()
        db.refresh(db_result)
        db_results.append(db_result)
    return db_results
