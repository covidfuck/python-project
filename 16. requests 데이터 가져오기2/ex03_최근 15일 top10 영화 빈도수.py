"""
    15일간 영화 top10 증
    가장 오랜 기간동안 TOP10 안에 들었던 영화의 이름을 출력
"""
import requests
from datetime import datetime, timedelta

dic = {}
cnt = 0
a = datetime.now() - timedelta(days=15)
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
for i in range(15):
    b = a + timedelta(days=i)
    date = b.strftime("%Y%m%d")
    prameter = {
        'key': '24d843c3be4aa7f2334ed1fece9098d1',
        'targetDt': date
    }
    resp = requests.get(url, prameter)

    json = resp.json()

    for j in range(10):
        movieNm = json['boxOfficeResult']['dailyBoxOfficeList'][j]['movieNm']
        if movieNm in dic:
            dic[f'{movieNm}'] += 1
        else:
            dic[f'{movieNm}'] = 1

max_movieNm, max_count = None, 0
for k, v in dic.items():
    if max_count < v:
        max_movieNm = k
        max_count = v
print(dic)
print(f'최장 기간 : {max_movieNm} {max_count}회')


