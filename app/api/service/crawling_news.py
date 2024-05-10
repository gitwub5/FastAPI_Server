from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from openai import OpenAI
import os
import re
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

async def crawling_esgnews_with_keyword(brand):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 브라우저를 표시하지 않고 실행
    options.add_argument("--disable-gpu")  # GPU 사용 안 함
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    url = "https://news.google.com/"
    news_lists = []
    title_lists = []
    
    try:
        driver.get(url)
        time.sleep(1)

        search_box = driver.find_element(By.CLASS_NAME, 'Ax4B8.ZAGvjd')
        search_box.click()
        search_box.clear()
        search_box.send_keys(brand + " ESG")
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

        news_elements = driver.find_elements(By.CLASS_NAME, 'JtKRv')
        for news_element in news_elements:
            news_title = news_element.text
            news_link = news_element.get_attribute("href")

            # 기사 제목에 친환경 관련된 단어가 있는 경우에만 저장
            if check_keyword(news_title):
                news_lists.append(news_link)
                title_lists.append(news_title)

    except Exception as e:
        print("에러 발생:", e)

    finally:
        driver.quit()
        return news_lists, title_lists

def check_keyword(title):
    keywords = ["친환경", "플라스틱제로", "미세플라스틱제로", "플라스틱프리", "천연", "식물성", "생분해",
            "자연분해", "지구", "나무", "숲", "에코", "에코프렌들리", "저자극", "자연", "자연유래성분",
            "제로웨이스트", "착한", "되살림", "순수", "안심", "안전", "재활용", "재사용", "업사이클링",
            "리유저블", "자연소재", "무해", "식물유래성분", "녹색", "녹색제품", "깨끗", "환경호르몬제로",
            "리필", "탄소발자국", "CO2", "환경보호", "그린", "유해물질제로", "동물실험", "재생플라스틱",
            "지속가능", "녹색인증", "자원순환", "PCR", "가치소비", "FCS", "자연추출", "오가닉", "자연친화"
            ,"eco-friendly", "plastic-free", "zero plastic", "natural", "plant-based", "biodegradable",
            "compostable", "earth", "tree", "forest", "eco", "ecofriendly", "low-impact", "nature",
             "naturally derived", "zero waste", "ethical", "upcycling", "pure", "safe", "non-toxic"
            ,"zero", "eco", "Green"]
    
    for word in keywords:
        if word in title:
                return True
        return False

async def get_article_content(url_list, brand):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    content_list = []

    try:
        for url in url_list[:3]:
            driver.get(url)
            time.sleep(2)

            # 기사가 로드될 때까지 대기 (10초)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@itemprop='articleBody' or @class='article_body' or @class='article-body' or @id='news_contents' or @class='news_view']")))

            article_content = driver.find_element(By.XPATH, "//div[@itemprop='articleBody' or @class='article_body' or @class='article-body' or @id='news_contents' or @class='news_view']")
            content_html = article_content.get_attribute("outerHTML")

            soup = BeautifulSoup(content_html, 'html.parser')
            text = soup.get_text()
            text = await analyze_proscons(text, brand)
            content_list.append(text)

    except Exception as e:
        print("에러 발생:", e)

    finally:
        driver.quit()
        return content_list


async def analyze_proscons(text, brand):
    #주어진 텍스트에서 키워드들의 연관관계와 긍정/부정 정도를 분석합니다.
    
    message = f"'''{text}'''을 요약하여 입력하세요. '{brand}' 기업이 끼치는 ESG 영향 중에 환경 분야에서의 긍정적인 측면과 부정적인 측면으로 나누어 각각 키워드 단위로 설명하시오. 출력 형식은 긍정: ,부정: "
    # OpenAI Sentiment Analysis 수행
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
        # 분석 결과 추출
    )
    proscons_analysis = response.choices[0].message.content
    return proscons_analysis

async def get_positive_keywords(reply_list):
    positive_keywords = []
    for text in reply_list:
        positive_start_index = text.find("긍정:") + len("긍정:")
        negative_start_index = text.find("부정:")
    
        # 긍정과 부정 사이의 텍스트를 추출
        content_between = text[positive_start_index:negative_start_index].strip()
    
        # 쉼표로 구분하여 리스트로 변환
        keywords_list = [re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", keyword.strip()) for keyword in content_between.split(',')]
        positive_keywords += keywords_list

    if len(positive_keywords) > 3:
        return positive_keywords[:3]
    
    return positive_keywords

async def get_keywords(brand):
    news_links, news_titles = await crawling_esgnews_with_keyword(brand)
    analyse_list = await get_article_content(news_links, brand)
    good_keywords = await get_positive_keywords(analyse_list)
    return {
        "keyword": good_keywords,
        "title": news_titles,
        "url": news_links
    }
