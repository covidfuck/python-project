"""

    1. 주민번호 입력 받기
        (YYMMDD-GXXXXXX) # G = 1,2 <-- 1900년대생 G = 3,4 <-- 2000년대생
    2. 나이. (2021로 계산)
        성별. ('여성' 혹은 '남성')
        생일 . (M월 D일)


"""
a = input(' 주민번호를 입력해주세요 : ')

ag = a[0:2] # 태어난 년도
mon = a[2:4] # 월
day = a[4:6] # 일
gen = a[7] # 성별 (1 3 = 남자, 2 4 = 여자)

age = 122 - int(ag)

if int(gen) == 3 or int(gen) == 4:
    age -= 100

if gen == "2" or gen == "4":
    print(f'나이 : {age} \n성별 : 여자 \n생일 : {mon}월 {day}일')
else:
    print(f'나이 : {age} \n성별 : 남자 \n생일 : {mon}월 {day}일')



