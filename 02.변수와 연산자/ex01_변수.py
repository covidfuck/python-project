"""
    변수(Variable)
        - 데이터 1개를 저장(보관)하는 '칸'의 역할
            - 데이터 1개를 저장하는 메모리
        - ' or " <-- 따음표 치지 않은 단어는 변수로 인식한다.

        'aa' : 문자열 데이터
        aa : 변수 aa
        aa() : 함수 aa
        - 변수의 목적
            : 값 보관의 목적
            : 값의 별명 붙이기
        - 변수의 사용방법
            1) 변수 생성
                변수명 = 초기값  ex) a = 10
                ( 변수는 최초 대입이 이루어지는 시점에 생성됨)
            2) 변수에 값 넣기
                변수명 = 값
                ( 생성된 이후의 대입의 경우 값은 변경된다.)
            3) 변수의 값 보기 (=변수호출)

"""

a = 10  # 변수 a에 10을 보관하겠다1 (대입하겠다)

pi = 3.14
r = 10
area = r ** 2 * pi
print(f'반지름 : {r}, 원의 넓이 : {area}')
r = 20
area = r ** 2 * pi
print(f'반지름 : {r}, 원의 넓이 : {area}')
