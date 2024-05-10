def scroll_page(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # 스크롤을 끝까지 내림
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 새로 로드된 콘텐츠의 높이 확인
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height