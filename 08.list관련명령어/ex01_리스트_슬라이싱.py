"""

    < 인덱싱 vs 슬라이싱 >
     indexing  slicing

     indexing : '번호(index)'로 칸에 접근

     slicing : 부분 리스트 추출

"""
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
b = a[4:7] # a 리스트의 index 번호 4이상 7미만 --> b = [50, 60, 70]
print(f'a : {b}')
print(f'b : {b}')

print(f'a[3:] : {a[3:]}') # index 번호 4이상 부터 끝까지
print(f'a[:3] : {a[:3]}') # index 번호 처음부터 3미만 까지

print(f'a[3:8:2] : {a[3:8:2]}') # index 번호 4이상 8미만 간격은 2
print(f'a[::2] : {a[::2]}') # 처음부터 끝까지 간격은 2
print(f'a[::-1] : {a[::-1]}') # 거꾸로 출력

# 문자열(str)형 데이터도 인덱싱, 슬라이싱 가능하다!
n = 1346248938239

# 숫자 n의 모든 자릿수의 합을 구해보자!
# step1. 숫자를 문자열형으로 변환
s = str(n) # '1346248938239' n을 str형으로 변경

# step2.
total = 0
for x in range(len(s)):
    total += int(s[x])

print(total)

