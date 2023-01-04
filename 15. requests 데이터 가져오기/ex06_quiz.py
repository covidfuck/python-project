# 사용자에게 검색어 1개를 입력 받는다
# 네이버 도서 검색 실행 query = 사용자가 입련한 단어
# 응답받은 json 에서 image 경로를 모두 받아서
# 책 제목.png 형식으로 파일 생성(이미지 파일)
import requests

url = 'https://openapi.naver.com/v1/search/book.json'
name = input('책 제목을 입력하세요 : ')
prameter = {'query' : name }
header = {
    'X-Naver-Client-Id' : 'fg7KGDFU7h3aeuuoRNzY',
    'X-Naver-Client-Secret' : 'kvSlrmfKYR'
}

resp = requests.get(url, prameter, headers = header)

print(resp.text)

a = resp.json()

for i in range(10):
    b = a['items'][i]['image']
    from PIL import Image
    import io
    img_link = b
    response = requests.get(img_link)
    in_memory_file = io.BytesIO(response.content)
    im = Image.open(in_memory_file)
    im.save(f'{i}.png')

