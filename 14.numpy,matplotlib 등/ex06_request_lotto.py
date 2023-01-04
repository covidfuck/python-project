"""


    요청 URL 구조
        ex) https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=861
        ? 앞의 주소는 서버의 주소
        ? 뒤의 주소는 파라미터(parameter) <== 서버에게 전달해줄 값 = 요청변수
"""
import requests

# 요청 URL
url = 'https://www.dhlottery.co.kr/common.do'

# 요청 변수 (파라미터)
parameter = {
    'method' : 'getLottoNumber',
    'drwNo' : 900 # 900 회차
}

# 요청 보내기 및 응답 받기
resp = requests.get(url, parameter)

# 응답 패킷의 '내용' 보기
# print(resp.text)

# 응답 패킷의 '내용'(JSON)을 딕셔너리로 인식하기
d = resp.json()
print(d['bnusNo'])

# Quiz1. 6개의 당첨 숫자를 출력

# Quiz2. 901 ~ 905회의 모든 6개의 당첨 번호를 출력

