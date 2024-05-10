from fastapi import APIRouter, HTTPException, File, UploadFile
from pydantic import BaseModel
from fastapi.responses import FileResponse
from pytesseract import image_to_string
from PIL import Image
from ..service.esg import fetch_esg_rating
from ..service.coupang import crawl_coupang
from ...core import models, schemas
from ..service import service
from ...core.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/process_text/")
async def process_text(text: str):
    # 여기서 텍스트 처리 및 분석 로직을 구현합니다.
    # 예를 들어, 받은 텍스트를 그대로 반환하거나 다른 처리를 수행할 수 있습니다.
    processed_text = text.upper()  # 예시로 받은 텍스트를 대문자로 변경합니다.

    # 처리된 텍스트를 반환합니다.
    return {"processed_text": processed_text}

@router.post("/upload_image/")
async def process_image(image: UploadFile = File(...)):
    # 이미지 파일을 서버에 저장
    with Image.open(image.file) as img:
        # OCR로 텍스트 추출
        text = image_to_string(img)
    # 이미지 처리 (예: 이미지를 그대로 반환)
    return {"text": text}

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
    print(itemName)
    results = await crawl_coupang(itemName)
    print(results)

