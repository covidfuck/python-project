"""
    requests : 서버가 제공하는 데이터를 요청할 때 사용
        한계 - 서버가 제공하지 않는 데이터(화면으로만 제공하는 데이터)
                는 사용 불가

    Selenium : 가상 브라우저
                (브라우저를 통한 요청만 응답해주는 사이트에 사용한다.)

    크롬 driver 설치 주소 : https://chromedriver.chromium.org/downloads
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 엔터

url = "http://www.naver.com"

driver_path = "chromedriver.exe"

driver = webdriver.Chrome(driver_path)

driver.get(url)

"""
#query
"""
# 검색창 elelment 에 접근 (검색창 : #query)
search_input = driver.find_element_by_css_selector("#query")

search_input.send_keys('아이유')
search_input.send_keys(Keys.RETURN)

# 1초 단위로 스크롤 내리기 3번
import time
body = driver.find_element_by_css_selector("body") # <body> 엘레먼트 가져오기
for i in range(3):
    time.sleep(0.5) # 0.5초 일시정지
    body.send_keys(Keys.PAGE_DOWN) # 스크롤 내리기

# 뒤로가기 : driver.back()
# 화면 닫기 : driver.quit()
