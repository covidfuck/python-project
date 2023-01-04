"""

    네이버 쇼핑 best100 으로 접속
    TOP 10 목록을 print()

    + 추출한 인기 키워드 10개를 모두 상세보기 실행
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 엔터
import time

url = "https://search.shopping.naver.com/best100v2/main.nhn"
driver_path = "chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get(url)

for i in range(1, 11):
    sel = driver.find_element_by_css_selector(f"#popular_srch_lst > li:nth-child({i}) > span.txt > a")
    search_input = driver.find_element_by_css_selector("#autocompleteWrapper > input.co_srh_input._input")
    search_input.send_keys(f"{sel.text}")
    search_input.send_keys(Keys.RETURN)
    body = driver.find_element_by_css_selector("body")  # <body> 엘레먼트 가져오기
    for i in range(3):
        time.sleep(0.4)  # 0.5초 일시정지
        body.send_keys(Keys.PAGE_DOWN)  # 스크롤 내리기
    driver.back()
    # print(f"{i}위 : {sel.text}")






