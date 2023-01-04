"""

    '네이버 쇼핑'에 접속 후
        '그래픽 카드' 를 검색시켜보자!
"""
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
search_input = driver.find_element_by_css_selector("#NM_FAVORITE > div.group_nav > ul.list_nav.type_fix > li:nth-child(5) > a")

search_input.send_keys(Keys.RETURN)
search_input = driver.find_element_by_css_selector("#autocompleteWrapper > input.co_srh_input._input.N\=a\:SNB\.search")
search_input.send_keys('그래픽카드')
search_input.send_keys(Keys.RETURN)


