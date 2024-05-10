from PIL import Image
import numpy as np
import pytesseract

def ocr(img):
    pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.3.4_1/bin/tesseract'
    text = pytesseract.image_to_string(img, lang='kor')
    return text
