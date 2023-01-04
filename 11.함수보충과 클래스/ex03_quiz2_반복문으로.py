"""

    Pocketmon 클래스 만들기
        필드 : 이름(name), 레벨(level), 체력(hp)

    1. pocketmon 객체 3개 찍어내기
    2. 이름, 레벨, 체력은 아무거나 넣기
        이름 : input() 으로 입력 받기
        레벨 : 1 ~ 30 중 랜덤하게 (random.randint())
        체력 : 레벨의 100배 (10%의 확률로 150배)
    3. 세 포켓몬의 모든 정보를 출력하기
    4. 반복문을 사용하자
"""
import random

class Poketmon:
    name = ''
    level = 0
    hp = 0

p = [Poketmon(), Poketmon(), Poketmon()]

for i in range(3):
    p[i].name = input('이름 : ')
    p[i].level = random.randint(1, 30)
    a = random.randint(1, 100)
    if a <= 20:
        p[i].hp = p[i].level * 100
    else:
        p[i].hp = p[i].level * 150

for i in range(3):
    print(f'이름 : {p[i].name}  레벨 : {p[i].level}  HP : {p[i].hp}')




