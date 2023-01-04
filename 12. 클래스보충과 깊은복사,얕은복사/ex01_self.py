"""

    self : 0번 인자
        - '나'
        - 이 객체의 id
        - 메서드

"""
class Person:

    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age
        # 참고! 필드는 __init__()에 선언하는 것이 좋다.

    def __str__(self):
            return f'{self.name}, {self.age}세'

    def add_age(self):
        self.age += 1

p1 = Person()
p2 = Person('홍길동', 10)

print(p1)
print(p2)

p1.add_age()

print(p1)
print(p2)

