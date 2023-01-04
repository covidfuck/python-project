total = 0
while True:
    s = int(input("정수를 입력해주세요(종료는 0을 입력) : "))
    if s == 0:
        print("반복 종료")
        break
    total += s

print(f'종합 : {total}')