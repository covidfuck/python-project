"""

    비트연산자(bitwise 연산자)
        - 비트 단위로 연산.

    & : 양 비트가 모두 1이면 1 (and)
    | : 한 쪽 비트만 1이여도 1 (or)
    ^ : 한 쪽 비트만 1이면 1 (xor)
    ~ : 1이면 0으로, 0이면 1 (not) , (1의 보수를 구함)


    8bit = 1byte
    python 에서 int형 데이터의 크기 64bit (8바이트)

    음의 정수 표현 : 2의 보수를 구한다
        ex) 4의 2의 보수  -->  -4

"""
a = 11
b = 22
print(a & b)
print(a | b)
print(a ^ b)
print(~b)
print(a >> 2)
print(a << 2)

