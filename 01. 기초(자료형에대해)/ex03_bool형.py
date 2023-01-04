print(bool(0)) # False
print(bool(-1.234567))  # True
# 숫자 : 0 만 False
# 나머지는 모두 True

print(bool("ABC"))  # True
print(bool("")) # False
# 문자 : 글자가 0갸면 False (공백)
# 글자가 1개라도 있으면 True

print(bool([10,20,30])) # True
print(bool([])) # False
# 데이터가 없으면 False
# 기타 : 데이터가 있으면 True

