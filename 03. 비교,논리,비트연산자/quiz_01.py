"""
    사용자에게
    국, 영, 수 점수를 각각 입력 받고
    평균 점수가 85점 이상이고
    세 과목 점수 모두 70점 이상이면 '합격'을 출력
    아니면 '불합격' 을 출력
"""
k = int(input('국어 점수를 입력하세요 : '))
e = int(input('영어 점수를 입력하세요 : '))
m = int(input('수학 점수를 입력하세요 : '))
aver = (k + e + m) / 3 # 평균

if (k >= 70 and m >= 70 and e >= 70 and aver >= 85):
    print('합격')
else:
    print('불합격')

