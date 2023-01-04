"""
    if 조건식:
        `조건식`이 True일 때 실행할 문장들
        (if문의 종속문장)

    if 의 옵션
    1. else
    if 조건식:
        `조건식`이 True일 때 실행할 문장들
    else:
        위의 `조건식`이 False일 때 실행할 문장들
        (그렇지 않으면..이라는 뜻)

    2. elif

"""
import random
n = random.randint(1,10)
print("1 ~ 10 사이의 랜덤한 숫자를 뽑습니다!")
print(f'뽑힌 수 : {n}')

if n % 2 == 0:
    print('짝수입니다~')
else:
    print("홀수입니다~")
