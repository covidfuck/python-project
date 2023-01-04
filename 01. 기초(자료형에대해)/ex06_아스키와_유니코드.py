"""

    ASCII (American Standard Code for information interchange)
        : 대소문자 26개
        : '0' ~ '9' 10개
        : 특수기호 66개

    UNICODE
        : 비영어권 문자들

    ord(문자) --> 해당 문자의 정수값
    chr(정수) --> 해당 정수에 연결된 문자

    ** 이름 이니셜 3글자의 정수값을(유니코드) 구해보자!
    J = 74 , D = 68, Y= 89
"""

a = chr(65)
b = chr(44032)
c = chr(44033)
d = ord('a')
e = ord('b')
f = chr(67)
print(a, b, c, d, e, f)

Jung = ord('J')
Dong = ord('D')
Yeon = ord('Y')

print(Jung, Dong, Yeon)
