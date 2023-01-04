import datetime

a = datetime.datetime.now()

print(a.year)
print(a.month)
print(a.day)
print(a.weekday())
print(a.hour)
print(a.minute)
print(a.second)
print(a.date())

# 8일 뒤의 요일 찾기
b = a + datetime.timedelta(days=8)
print(b.day)

# 150일 뒤의 월 찾기
b = a + datetime.timedelta(days=150)
print(b.month)

# 1년 뒤 오늘의 요일 찾기
b = a + datetime.timedelta(days=365)
print(b)
print(b.weekday())
