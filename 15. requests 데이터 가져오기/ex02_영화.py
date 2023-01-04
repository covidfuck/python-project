import requests

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
prameter = {
    'key' : '24d843c3be4aa7f2334ed1fece9098d1',
    'targetDt' : '20210314'
}

resp = requests.get(url, prameter)
print(resp.text)
