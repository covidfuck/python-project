"""

    salesAmt, salesAcc
"""


import requests

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
prameter = {
    'key' : '24d843c3be4aa7f2334ed1fece9098d1',
    'targetDt' : '20221216'
}

resp = requests.get(url, prameter)

a = resp.json()

print("-------------------------- 20210316 일일 박스오피스 순위별 매출액 --------------------------")
for i in range(10):
    print(f"{i+1}위 :",a['boxOfficeResult']['dailyBoxOfficeList'][i]['movieNm'])
    print("일 매출액 :",a['boxOfficeResult']['dailyBoxOfficeList'][i]['salesAmt'], "총 매출액 :",a['boxOfficeResult']['dailyBoxOfficeList'][i]['salesAcc'])

