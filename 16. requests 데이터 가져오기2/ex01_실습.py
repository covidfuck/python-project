# 사용자에게 검색어 1개를 입력 받는다.
# 네이버 도서 검색 실행 query=사용자가 입력한 단어
# 응답받은 json에서 image 경로를 모두 받아서
# 책제목.png 형식으로 파일 생성(이미지 파일)
import requests
from PIL import Image
import io  # 입출력(Input, Output) 스트림
import os  # mkdir 이라는 시스템 명령을 사용하고 싶어서..

keyword = input('검색어 : ')



# 사전 준비
url = 'https://openapi.naver.com/v1/search/book.json'
param = {'query' : keyword}
header = {
    'X-Naver-Client-Id' : 'VIDuHUvMzioOGfvUhKpw',
    'X-Naver-Client-Secret' : 'f25KIjCLKc'
}

# 요청 보내기 및 응답 받기
resp = requests.get(url=url, params=param, headers=header)

# 응답 내용을 json -> dictionary로
di = resp.json()

# 빈 딕셔너리 (이미지 URL들을 담을) (키:책 제목, 값: 이미지 URL)
image_di = {}

# image URL 만 10개 추출
for i in range(10):
    title = str(di['items'][i]['title'])
    title = title.replace("<b>", "")
    title = title.replace("</b>", "")
    title = title.replace("/", "_")
    image_di[title] = di['items'][i]['image']

# 사용자가 입력한 '검색어'로 새 디텍토리 생성
os.mkdir(keyword)

for k, v in image_di.items():
    response = requests.get(v)
    in_memory_file = io.BytesIO(response.content)
    im = Image.open(in_memory_file)
    im.save(f'{keyword}/{k}.png')
