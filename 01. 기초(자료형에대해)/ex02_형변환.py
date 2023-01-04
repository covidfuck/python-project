"""
name = input('이름 : ')
age = int(input('나이 : '))

print(f'당신의 이름은 {name}이고,')
print(f'나이는 {age}살 이군요!')
print(f'내년엔 {age + 1}살 입니다!')

# 10 + 1 = 11
# '10' + 1 = 에러!
# '10' + '1' = '101'


    정수형으로 : int(변환할 값)
    실수형으로 : float(값)
    논리형으로 : bool(값)
    문자형으로 : str(값)
"""

a = int(3.999999999)
b = float(100)
c = bool(3)
d = str(100)
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))