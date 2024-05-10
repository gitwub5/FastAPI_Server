import numpy as np
import pytesseract
import requests
from PIL import Image
import io

def imageurl2img(image):
    response = requests.get(image)
    image_data = response.content
    img = np.array(Image.open(io.BytesIO(image_data)))
    return img