"""
    사용자에게 소괄호만으로 구성된 문자열을 입력 받습니다.
        이때, 괄호의 짝꿍이 올바른지 True/False 를 출력하세요.
        예) )))()()((( => False
            ()()()()()) => False
            ()(())()()  => True
            ))(())(( => False
            ()(()))( => False
            ((())()) => True
        (위 6개의 테스트를 모두 통과해야합니다.)

"""
a = input("소괄호만으로 구성된 문자열을 입력하세요 : ")
b = a.count("(")
c = a.count(")")

if b == c:
    print(True)
else:
    print(False)