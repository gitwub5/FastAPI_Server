from fastapi import APIRouter, HTTPException, File, UploadFile, Depends
from pydantic import BaseModel
from fastapi.responses import FileResponse
from pytesseract import image_to_string
from PIL import Image
from ..service.esg import fetch_esg_rating
from ..service.coupang import crawl_coupang
from ...core import models, schemas
from ..service import service
from ...core.database import SessionLocal, engine
from sqlalchemy.orm import Session, joinedload
from typing import List
import time
from ..service.crawling_news import get_keywords
import re

models.Base.metadata.create_all(bind=engine)

router = APIRouter()
db = SessionLocal()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/esg/{company}")
async def process_esg(company):
    print(company)
    results = await fetch_esg_rating(company)
    # 처리된 텍스트를 반환합니다.
    if results:
        first_result = results[0]
        print(first_result[0])
        if first_result[0] != company:
            raise HTTPException(status_code=404, detail="Company does not match with ESG rating information.")
        return {
            "company": first_result[0],
            "grade": first_result[1],
            "environment": first_result[2],
            "social": first_result[3],
            "governance": first_result[4],
            "year": first_result[5]  # 문자열 그대로 반환
        }
    else:
        raise HTTPException(status_code=404, detail="ESG rating information not found.")



@router.get("/item/{itemName}")
async def getItemInfo(itemName):
    product_results = await crawl_coupang(itemName)
    certified_info, esg_info = extract_info(product_results)
    print(certified_info)




def extract_info(product_results):
    # 결과를 줄바꿈으로 분리하여 리스트로 만듭니다.
    lines = product_results.split('\n')

    # 정보를 저장할 두 개의 빈 리스트를 생성합니다.
    certified_info = []
    esg_info = []

    # 현재 어떤 섹션을 분석 중인지 추적합니다.
    current_section = None

    for line in lines:
        # 섹션의 시작을 확인합니다.
        if line.startswith('Certified:'):
            current_section = 'certified'
            continue  # 섹션 제목은 저장하지 않습니다.
        elif line.startswith('ESG:'):
            current_section = 'esg'
            continue

        # 현재 섹션에 따라 해당 정보를 적절한 리스트에 추가합니다.
        if current_section == 'certified' and line.strip():
            certified_info.append(re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", line.strip()))
        elif current_section == 'esg' and line.strip():
            esg_info.append(re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", line.strip()))
        # '```' 제거하기
    if certified_info and certified_info[-1] == '```':
        certified_info.pop()
    if esg_info and esg_info[-1] == '```':
        esg_info.pop()

    return certified_info, esg_info

@router.post("/")
async def postItem(item:schemas.requestItem):
    company = item.company
    product = item.product
    # check = await service.get_result_by_product(db=db,product=product)
    # if check: 
    #     return check
    esg_results = await fetch_esg_rating(company)
    esg_dict={}
    if esg_results:
        first_result = esg_results[0]
        if first_result[0] != company:
            raise HTTPException(status_code=404, detail="Company does not match with ESG rating information.")
        esg_dict = {
            "grade": first_result[1],
            "environment": first_result[2],
            "social": first_result[3],
            "governce": first_result[4],
            "year": first_result[5]  # 문자열 그대로 반환
        }
    
    data = await get_keywords(company)
    product_results = await crawl_coupang(product)
    certified_info, esg_info = extract_info(product_results)
    certified = False
    if certified_info == ['- Yes']:
        certified = True
        
    post_result = schemas.PostResultSchema(
        company=company,
        product=product,
        certified=certified,
        result="결과 처리를 위한 로직 추가 필요",  # 결과 필드는 비즈니스 로직에 따라 적절히 설정해야 합니다.
        **esg_dict
    )

    print(post_result)
    post = await service.create_result(db=db, result=post_result)

    print(type(data["keyword"]), type(data["url"]), type(data["title"]))

    keyword_get = await service.create_keyword(db=db, result_id=post.id, key_info=data["keyword"])
    print(keyword_get)

    article = await service.create_article(db=db, result_id=post.id, urls=data["url"], titles=data["title"])
    print(article)


    await service.create_esg_info(db=db, result_id=post.id,esg_info=esg_info)
    print(esg_info)

    return db.query(models.Result).options(joinedload(models.Result.articles), joinedload(models.Result.esgs), joinedload(models.Result.keywords)).filter(models.Result.id == post.id).first()
    

@router.get("/results", response_model=List[schemas.ResultSchema])
def read_results(db: Session = Depends(get_db)):
    results = db.query(models.Result).options(joinedload(models.Result.articles), joinedload(models.Result.esgs)).all()
    return results

@router.get("/results/{result_id}", response_model=schemas.ResultSchema)
def read_result(result_id: int, db: Session = Depends(get_db)):
    result = db.query(models.Result).options(joinedload(models.Result.articles), joinedload(models.Result.esgs)).filter(models.Result.id == result_id).first()
    return result