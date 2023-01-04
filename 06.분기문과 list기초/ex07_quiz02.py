"""

    사용자에게 년,월,일을 입력 받고
    1월 1일부터 해당 날짜까지 며칠이 소요되는 지 출력하세요.
    윤년을 포함하세요.
        => 윤년 : year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
    2020 1 30  ==> 29일 소요!
    2020 12 31 ==> 365일 소요! (윤년)

"""
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = int(input("year(년도)를 입력해주세요 : "))
month = int(input("month(월)을(를) 입력해주세요 : "))
date = int(input("date(날짜)를 입력해주세요 : "))
total = 0

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    day[1] = 29

for i in range(month):
    if month-1 == i:
        total += (date-1)
    else:
        total += day[i]

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print(f"{total}일 소요! (윤년)")
else:
    print(f"{total}일 소요!")

print("-------------------------------- 디데이 계산기 --------------------------------")
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

s_day = int(input("시작일을 입력하세요 ex)19970327 : "))
o_day = int(input("목표일을 입력하세요 ex)19980102 : "))

s_year = s_day // 10000
s_month = (s_day - s_year * 10000) // 100
s_date = (s_day - s_year * 10000 - s_month * 100)
o_year = o_day // 10000
o_month = (o_day - o_year * 10000) // 100
o_date = (o_day - o_year * 10000 - o_month * 100)

year = o_year - s_year
month = o_month - s_month
date = o_date - s_date

d_day = 0

while o_day >= s_day:
    if o_day < s_day:
        print('시작일이 목표일보다 큽니다!, 다시 입력해주세요!')
        s_day = int(input("시작일을 입력하세요 ex)19970327 : "))
        o_day = int(input("목표일을 입력하세요 ex)19980102 : "))

if year >= 2:
    for i in range(year-1):
        d_day += 365

if s_month < 12:
    for i in range(12 - s_month):
        d_day += day[s_month + i]

d_day += day[s_month-1] - s_date

if o_month >= 2:
    for i in range(o_month-1):
        d_day += day[i]

d_day += o_date

print(d_day)




"""

    위 계산을 활용하여 디데이 계산기를 만드세요.
    시작일 : YYYYMMDD 형태의 문자열로 입력 받습니다.
    목표일 : YYYYMMDD 형태의 문자열로 입력 받습니다.
    시작일로부터 목표일까지 며칠이 소요되는 지 출력하세요.
    목표일은 시작일보다 미래입니다.

"""





