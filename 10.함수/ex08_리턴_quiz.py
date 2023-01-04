"""
    1. get_random_name()
        : 매개변수 0개
            '피카츄', '라이츄', '파이리' 중 1개의 이름을
            랜덤하게 return
            (random.choice() 활용)

   2. get_circle_info()
        : 매개변수 1개 (반지름)
          반지름을 가지고 원의 넓이 계산하여 return
"""
#################################################################

import random

def get_random_name():
    return random.choice(['피카츄', '라이츄', '파이리'])

random_name = get_random_name()

print(random_name)

#################################################################

r = int(input("반지름을 입력하세요 : "))

def get_circle_info():
    return r**2 * 3.14

a = get_circle_info()

print(f'반지름이 {r}인 원의 넓이는 {a}!')


