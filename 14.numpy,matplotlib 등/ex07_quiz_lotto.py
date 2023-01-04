"""
    Quiz1. 6개의 당첨 숫자를 출력

    Quiz2. 901 ~ 905회의 모든 6개의 당첨 번호를 출력

"""
import requests

# url = 'https://www.dhlottery.co.kr/common.do'
#
# parameter = {
#     'method' : 'getLottoNumber',
#     'drwNo' : 900 # 900 회차
# }
#
# resp = requests.get(url, parameter)
#
#
# print(resp.text)
#
# d = resp.json()
#
# print(d['drwtNo1'], d['drwtNo2'], d['drwtNo3'], d['drwtNo4'], d['drwtNo5'], d['drwtNo6'])

url = 'https://www.dhlottery.co.kr/common.do'

for i in range(901, 906):
    lst = []
    parameter = {
        'method' : 'getLottoNumber',
        'drwNo' : i
    }
    resp = requests.get(url, parameter)

    d = resp.json()

    for j in range(1, 7):
        lst.append(d[f'drwtNo{j}'])
    print(f'{i}회 당첨 번호 : {lst}')