"""

    < 논리연산자 >
    and or not

    항1 and 항2 : 양 항이 모두 True 여야 최종 결과 True
    항1 or 항2 : 한쪽 항만 True 여도 최정 결과 True
    not 항1 : 항이 True이면 False,
                  False면 True
                  'a == False' 는 'not a' 와 같다.
"""

# Quiz 사용자에게 월, 일을 입력 받고
# 월 : 1 이상 12 이하
# 일 : 1 이상 31 이하
# 두 조건을 모두 만족하면 : True
# 두 조건을 모두 만족하지 못하면 : False
# 예) 2월 30일도 True라고 가정

month = int(input('월을 입력해 주세요 : '))
date = int(input('일을 입력해 주세요 : '))

print(1 <= month <= 12 and 1 <= date <= 31)
