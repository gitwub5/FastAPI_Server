from selenium import webdriver
from selenium.webdriver.common.by import By

async def fetch_esg_rating(company_name):
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)

    ESG_URL = 'https://www.cgs.or.kr/business/esg_tab04.jsp'
    driver.get(ESG_URL)

    search_box = driver.find_element(By.CSS_SELECTOR, "#svalue")
    search_box.send_keys(company_name)

    search_button = driver.find_element(By.CSS_SELECTOR, "#searchform > button")
    search_button.click()
    contents = driver.find_element(By.TAG_NAME, "tbody")
    rows = contents.find_elements(By.TAG_NAME, "tr")

    results = []

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) > 7:  # 셀이 7개 이상인지 확인하여 유효한 데이터인지 검사
            company = cells[1].text
            esg_rating = cells[3].text
            environmental_rating = cells[4].text
            social_rating = cells[5].text
            governance_rating = cells[6].text
            evaluation_year = cells[7].text
            
            results.append([company, esg_rating, environmental_rating, social_rating, governance_rating, evaluation_year])

    driver.quit()
    return results