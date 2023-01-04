"""
    1. my_max() 함수 만들기
        : 매개변수 5개
            그 중 가장 큰 수를 출력
            (max(리스트) 참고)

    2. print_stars()
        : 매겨변수 1개
            해당 숫자만틈의 '*'을 출력
            ex) print_stars(3) '***'
            ex) print_stars(4) '****'

    3. print_random_name()
        : 매개변수 0개
            '피카츄', '라이츄', '파이리' 중 1개의 이름을
            랜덤하게 출력
            (random.choice() 활용)
"""
#################################################################

def my_max(a,b,c,d,e):
    x = [a, b, c, d, e]
    print(f'{max(x)}')

my_max(5, 120, 15, 20, 25)

#################################################################

def print_stars(a):
    print('*' * a)

print_stars(5)

# def print_stars(a):
#     for i in range(a):
#         print('*', end = '')
#     print("")

#################################################################

import random

def print_random_name():
    a = ['피카츄', '라이츄', '파이리']
    print(random.choice(a))

print_random_name()