from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

from app.ai.prediction import predict_sentiment

#예제 ai 모델
class SentimentRequest(BaseModel):
    text: str

@router.post("/")
def predict_sentiment_api(request: SentimentRequest):
    sentiment = predict_sentiment(request.text)
    return {"sentiment": sentiment}

@router.post("/1")
def returndata():
    return "GOOD"