"""

    2. 영화진흥원 Top10의 영화제목, 당일 매출액을
        날짜별로 저장
"""
import requests
import openpyxl

wb = openpyxl.Workbook()

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'

while True:
    date = input("날짜를 입력해주세요(YYYYMMDD) : ")
    if date == 'exit':
        break
    else:
        ws = wb.create_sheet(f'{date}') # 기본 시트 생성
        parameter = {
        'key': '24d843c3be4aa7f2334ed1fece9098d1',
        'targetDt': date
        }

        resp = requests.get(url, parameter)

        a = resp.json()

        for i in range(10):
            movieNm = a['boxOfficeResult']['dailyBoxOfficeList'][i]['movieNm']
            salesAmt = a['boxOfficeResult']['dailyBoxOfficeList'][i]['salesAmt']

            ws.append([f'{movieNm}', f'{salesAmt}원'])

wb.save('movie.xlsx')

