"""
문제1.
 국, 영, 수 점수 입력 받고 (input())
 평균을 출력
 평균이
 90 이상 : A
 80 이상 90 미만 : B
 70 이상 80 미만 : C
 60 이상 70 미만 : D
 60 미만 : F
 위 학점을 출력

 문제2.
 정수 1개를 입력 받고
 2, 3, 5의 배수인지 출력
 6 입력
 2의 배수
 3의 배수
 4 입력
 2의 배수
 17 입력
 해당 사항 없음
"""
# Quiz 1


# Quiz 2
a = int(input("정수 1개를 입력해주세요 : "))
if (a % 2 == 0):
    print("2의 배수")
    if (a % 3 == 0):
        print("3의 배수")
    if (a % 5 == 0):
        print("5의 배수")
elif (a % 3 == 0):
    print("3의 배수")
    if (a % 5 == 0):
        print("5의 배수")
elif (a % 5 == 0):
    print("5의 배수")
else:
    print("해당 사항 없음")

