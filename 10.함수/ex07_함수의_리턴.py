"""

    a = input('입력 : ') # input()은 리턴값 x
    print('aaa') # print()는 리턴값 o

    a = random.randint(1, 10) # randint()는 리턴값 o
    a = list() # list()는 리턴값 o
    a.append(10) # append()는 리턴값 x

    리턴값이 있는 함수는 '변수 =' 와 함께 사용한다!!

    < 리턴값 >
    - 함수 실행의 결과물
    - 'return' 과 함께 사용한다.
    - 함수가 실행(=호출)되었던 자리에 반환된다.

    < return >
    - 리턴값을 반환하라!
    - 함수를 끝내라!
    - 호출된 자리로 돌아가라!

"""
def str_stars(n):
    print(f'n : {n}개')
    return '*' * n

a = str_stars(10)
b = str_stars(20)

print(f'a : {a}')
print(f'b : {b}')