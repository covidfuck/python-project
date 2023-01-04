""" 자료형(type)
    - 데이터의 형태
    - 파이썬 자료형

        1) 숫자형
            정수형 : int
            실수형 : float
                    ** 1.0 / -101.0 <-- 실수형 (소숫점 o)

        2) 문자형 : str
            - 외따옴표 혹은 쌍따옴표로 감싼 데이터
            - string (문자열)

        3) 논리형 : bool
            - 참 혹은 거짓
            - True / False (대소문자 구분)
            - boolean

        4) 객체형
"""



a = int(10 + 3.14)
b = 'abc'
c = '10'
d = 'True'
e = False
print(a ,b, c, d, e)
print(b+c)

# 각 데이터의 자료형을 알려주는 명령어 : type
print(type(a)) # <class 'int'>
print(type(b)) # <class 'str'>
print(type(c)) # <class 'str'>
print(type(d)) # <class 'str'>
print(type(e)) # <class 'bool'>
print(type(b+c+d)) # <class 'str'>

