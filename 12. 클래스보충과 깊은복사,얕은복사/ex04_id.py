"""
    id : 객체의 고유번호 (주민등록번호 같은 번호)
         객체의 메모리 주소를 고유번호로 사용한다.
"""
class Person:
    name = ''

a = Person()
b = Person()
print(a)
print(b)

print(id(a))
print(id(b))