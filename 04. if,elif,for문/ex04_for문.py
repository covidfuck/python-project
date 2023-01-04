"""
    < for 문 >
    - 반복문
    for 번수 in range():
        반복할 문장..

    range() 자리에는
        문자열, 리스트, 딕셔너리 등 나열형 데이터가 들어간다.

"""

for i in range(2, 10):
    print(i)

print("============")

for a in "Hello, Python!":
    print(f"문자 : {a}")

print("============")

s = input('문장 : ')
cnt = 0
for ch in s:
    if 65 <= ord(ch) <= 90:
        cnt += 1
print(f'대문자는 {cnt}개')

