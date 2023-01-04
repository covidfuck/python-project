"""

    로또 생성기
    1. 1 ~ 45 숫자 중 6개를 랜덤하게 선택한다.
        - 중복 숫자 X
    2. 사용자도 6개 숫자를 입력한다.


"""
import random

lotto = set()

while len(lotto) != 6:
    a = random.randrange(1, 45)
    lotto.add(a)

user = set()

while len(user) != 6:
    a = int(input('1 ~ 45 사이 6개의 숫자를 입력해주세요! : '))
    if a in user:
        print('중복 번호 입니다. 다시 입력해주세요!')
        print(f'현재 선택하신 번호 : {user}')
    elif a > 45:
        print("1 ~ 45 사이의 숫자를 입력해주세요!")
    else:
        user.add(a)

print(f' 이번주 로또 번호 : {sorted(lotto)}')
print(f' 입력한 로또 번호 : {sorted(user)}')

user &= lotto

print(user)
print(f'총 {len(user)}개 맞추셨습니다!')

