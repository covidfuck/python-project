"""

    함수 : add
    인자(들어오는 값) : 정수 2개
    하는 일 : 두 정수를 더한다. 이를 출력
    리턴(나가는 값) : X
"""

def add_1(a, b):
    print(a+b)

add_1(5, 7)

"""

    함수 : add_2()
    인자(들어오는 값) : 정수 2개
    하는 일 : 두 정수를 더한다. 
    리턴(나가는 값) : 더한 값
"""

def add_2(a, b):
    return a+b

print(add_2(5, 6))

"""

    함수 : add_3()
    인자(들어오는 값) : X
    하는 일 : 두 정수를 input()으로 입력 받고
             두 정수를 더한다
    리턴(나가는 값) : 더한 값
"""

def add_3():
    a = int(input("정수 1 : "))
    b = int(input("정수 2 : "))
    return a+b

c = add_3()
print(c)