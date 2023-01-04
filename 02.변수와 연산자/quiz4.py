"""
4자리 정수를 입력 받고 각 자릿수의 총합을 출력하세요
힌트)

    6432 = 2 + 3 + 4 + 6 = 15
    6432 % 10 --> 2
    6432 // 10 --> 643

    643 % 10 --> 3
    643 // 10 --> 64

"""
"""
value = int(input('4자리의 정수값을 입력해 주세요 : '))
a = value % 10
value2 = value // 10
b = value2 % 10
value3 = value2 // 10
c = value3 % 10
value4 = value3 // 10
d = value4
print(f'4자리 정수값의 각 자릿수의 총합은 : {a+b+c+d}입니다!')

"""

nums = int(input('4자리 정수를 입력하시오 : '))
a = nums % 10
    
nums //= 10
b = nums % 10
    
nums //= 10
c = nums % 10
    
nums //= 10
d = nums % 10
    
print(f'4자리 정수값의 각 자릿수의 총합은 : {a+b+c+d}입니다!')
