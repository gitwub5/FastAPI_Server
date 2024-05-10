from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
from . import OCR
from . import imageurl2img
from . import scrolling_pages_down
from openai import OpenAI
from dotenv import load_dotenv
import urllib.parse
import urllib
import os
# import UserAgent
load_dotenv()

async def crawl_coupang(item_name):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("prefs", {"prfile.managed_default_content_setting.images": 2})

    url = "https://www.coupang.com/np/search?component=&q="+urllib.parse.quote(item_name)+"&channel=user"

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # 브라우저를 표시하지 않고 실행
    options.add_argument("--disable-gpu")  # GPU 사용 안 함
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})
    driver.implicitly_wait(2)
    driver.get(url)
    time.sleep(2)

    first_product = driver.find_element(By.XPATH, '//ul[@id="productList"]/li[2]').find_element(By.TAG_NAME, "a")

    driver.get(first_product.get_attribute("href"))
    time.sleep(2)

    ## 전체적으로 스크롤을 하는 페이지이다
    scrolling_pages_down.scroll_page(driver)
    ## 바로 실행하면 로딩이 안된경우도 있기 때문에 2초정도 기다려준다
    time.sleep(2)

    ## 이미지를 찾아온다
    images = driver.find_elements(By.TAG_NAME, "img")

    image_data = []
    for image in images:
        ## 이미지의 주소를 뽑아온다
        src = image.get_attribute("src")
        ## 이미지가 없는 경우 예외처리
        if(src != None):
            ## 이미지의 확장자가 jpeg, png, jpg인경우만 가져온다
            if(src.split(".")[-1] == "jpg" or src.split(".")[-1] == "png" or src.split(".")[-1] == "jpeg"):
                image_data.append(src)

    texts = ""
    ## 이미지를 돌려가며 OCR하며 데이터 뽑아오기
    for image in image_data:
        ## 특정한 경우, 아래의 경우는 테스트하는 것이다.
        if("q89" in image):
            ## 이미지url을 이미지로 변경후 OCR을 돌려본다
            texts += OCR.ocr(imageurl2img.imageurl2img(image)) + "\n"
    return await analyze_sentiment(texts)


async def analyze_sentiment(text):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    eco_keywords = ['친환경인증', '환경인증', '환경표지인증', '녹색건축', '친환경 농산물 인증', '무농약인증']

    """
    주어진 텍스트에서 키워드들의 연관관계와 긍정/부정 정도를 분석합니다.
    """
    message = f"GOAL: read the PRODUCT_INFO and figure out if the product is environmentally certified and related to ESG\n\nPRODUCT_INFO: ```{text}```. \n Find as much evidence as possible for environment. \n1. Make all words in PRODUCT_INFO flow naturally while understanding the overall context of the text.\n2. Check all the words that is related to environment, society, and governance.\n3. Check if there are words which is in list of [```{eco_keywords}```] Return Yes the if the word is in the list and No if not.\n4. Return the ESG evidence that you found in the PRODUCT_INFO\n\nRETURN FORMAT:\n5. You must return text in korean\nCertified:\n- Yes or No\n\n```\n\nESG:\n\n- Evidence 1 \n\n- Evidence 2\n\n- Evidence 3```"
    # OpenAI Sentiment Analysis 수행
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
        # 분석 결과 추출
    )
    sentiment_analysis = response.choices[0].message.content
    return sentiment_analysis

# with open("ocr_result.txt", 'w') as f:
#     f.write(texts)

# with open("langchain_result.txt", 'w') as f:
#     f.write(langchain_result)