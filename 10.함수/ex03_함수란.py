"""
    함수 (function)
        - 기능 (=기계)
        - 코드를 미리 작성하고 필요할 때 마다 실행시킬 목적
        - 형식 : 단어()
            예 ) print(), input(), int() 등 ...

    함수 정의 (definition)
        - 함수 만들어두기
        - 형식)
            def 함수명(매개변수) : <-- 매개변수 생략 가능
            함수 코드
            return 리턴값 : <-- 리턴값 생략 가능

    함수 호출(calling)
        - 함수 실행하기
        - 형식)
            함수명(인자값)
"""
def fun01(a):
    print(f'a : {a}')

def fun02(a, b):
    print(f'a : {a}')
    print(f'b : {b}')

print('----------')
fun01(10)
print('----------')
fun02(10, 20)