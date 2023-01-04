"""
    935 ~ 954 회 까지의 당첨 번호를 모두 받고
    각 숫자가 몇 회 등장 했는지 출력

    ex) 1: 5회
        2: 9회
        ~~~
        45 : 4회
"""
import requests

url = 'https://www.dhlottery.co.kr/common.do'

lst = []

for i in range(895, 955):
    parameter = {
        'method' : 'getLottoNumber',
        'drwNo' : i
    }
    resp = requests.get(url, parameter)

    d = resp.json()

    for j in range(1, 7):
        lst.append(d[f'drwtNo{j}'])

for i in range(1, 46):
    b = lst.count(i)
    print(f'{i} : {b}회')

print(f'954회 : {resp.text}')


