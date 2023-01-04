"""
    참고) 리스트도 객체다
        깊은 복사와 얕은 복사가 있다.
"""
class Person:
    name = ''

a = Person()
b = Person()
a.name = '홍길동'
print(a.name)  # '홍길동'
print(b.name)  # ''
############################
# 얕은 복사
a = Person()
b = a
a.name = "홍길동"
print(a.name)  # '홍길동'
print(b.name)  # '홍길동'
print(a)
print(b)
############################
# 깊은 복사
import copy
a = Person()
b = copy.copy(a)  # a의 복사본 생성
a.name = '홍길동'
print(a.name)  # '홍길동'
print(b.name)  # ''







