"""
    class : 내가 만드는 자료형

"""

class person:
    name = '' # field, 멤버변수
    age = 0

p1 = person()
p2 = person()

p1.name = '홍길동' #  . 의 의미 : ~의
p1.age = 10

p2.name = '이순신'
p2.age = 50

print(f'이름 : {p1.name}, {p1.age}세')
print(f'이름 : {p2.name}, {p2.age}세')