"""
    1. 컴퓨터는 1 ~ 1000 사이 중 랜덤한 수를 1개 고른다.
            (random.randint())
            import random은 맨 윗줄에 한 번만 사용한다.
            < 랜덤 수 생성 >
            ex) a = random.randint(1, 100) # 1 <= a <= 100 중 랜덤한 정수 1개를 선택함
    2. 사용자가 답을 입력한다.
        컴퓨터가 고른 수 > 사용자가 입력한 수  ---> Up 을 출력
        컴퓨터가 고른 수 < 사용자가 입력한 수  ---> Down 을 출력
    3. 사용자가 정답을 입력할 때까지 (2)과정을 반복한다.
    4. 사용자가 정답을 맞춘 후 시도횟수 출력
        시도한 횟수가 10회 이하 WIN을 , 아니면 LOSE를 출력한다.

"""
import random
cnt = 0
a = random.randint(1, 1000)
b = 0

while a != b:
    b = int(input("1 ~ 1000 사이의 정수를 입력해 주세요 : "))
    cnt += 1
    if (a > b):
        print("UP!")
    elif (a < b):
        print("DOWN!")

if cnt <= 10:
    print("WIN!")
elif cnt > 10:
    print("lOSE!")

print(f"{cnt}회에 성공하셨습니다.")



