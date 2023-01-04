"""

    파이썬의 자료구조 자료형
    1. list : [원소, 원소, 원소, ....]
    2. tuple : (원소, 원소, 원소, ....)
    3. set : {원소, 원소, 원소, ....}
    4. dictionary : {키:값, 키:값, 키:값, ....}
"""

a = 10, 20, 30
print(f'a : {a}, {type(a)}')

a, *b, c = 10, 20, 30, 40, 50
print(type(a))
print(type(b))
print(f'a : {a}, b : {b}, c : {c}')
