"""

    Pocketmon 클래스 만들기
        필드 : 이름(name), 레벨(level), 체력(hp)

    1. pocketmon 객체 3개 찍어내기
    2. 이름, 레벨, 체력은 아무거나 넣기
        이름 : input() 으로 입력 받기
        레벨 : 1 ~ 30 중 랜덤하게 (random.randint())
        체력 : 레벨의 100배 (10%의 확률로 150배)
    3. 세 포켓몬의 모든 정보를 출력하기
"""
import random

class Poketmon:
    name = ''
    level = 0
    hp = 0

p1 = Poketmon()
p2 = Poketmon()
p3 = Poketmon()

p1.name = input('이름 : ')
p1.level = random.randint(1, 30)
a = random.randint(1, 100)
if a <= 20:
    p1.hp = p1.level * 100
else:
    p1.hp = p1.level * 150

p2.name = input('이름 : ')
p2.level = random.randint(1, 30)
a = random.randint(1, 100)
if a <= 20:
    p2.hp = p2.level * 100
else:
    p2.hp = p2.level * 150

p3.name = input('이름 : ')
p3.level = random.randint(1, 30)
a = random.randint(1, 100)
if a <= 20:
    p3.hp = p3.level * 100
else:
    p3.hp = p3.level * 150

print(f'이름 : {p1.name}  레벨 : {p1.level}  HP : {p1.hp}')
print(f'이름 : {p2.name}  레벨 : {p2.level}  HP : {p2.hp}')
print(f'이름 : {p3.name}  레벨 : {p3.level}  HP : {p3.hp}')




