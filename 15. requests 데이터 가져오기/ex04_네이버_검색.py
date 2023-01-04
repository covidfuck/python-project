import requests

url = 'https://openapi.naver.com/v1/search/book.json'
prameter = {'query' : '해리포터'}
header = {
    'X-Naver-Client-Id' : 'fg7KGDFU7h3aeuuoRNzY',
    'X-Naver-Client-Secret' : 'kvSlrmfKYR'
}

resp = requests.get(url, prameter, headers = header)
print(resp.text)

# # harry.json 에 저장
# with open('harry.json', 'w', encoding = 'utf-8') as f:
#     f.write(resp.text)