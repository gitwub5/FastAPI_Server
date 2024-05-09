from app.ai.model_loader import SentimentAnalyzer

sentiment_analyzer = SentimentAnalyzer()

def predict_sentiment(text):
    return sentiment_analyzer.predict_sentiment(text)