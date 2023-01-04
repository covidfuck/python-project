

a = [10, 20, 30]

a.append(40) # 리스트 a의 맨뒤에 40 추가
print(f'1. {a}')

# 원소 삭제:
#   리스트.remove(원소)
#   리스트.pop(인덱스)
#   리스트.pop() # () 아무것도 쓰지 않으면 맨 마지막 원소 삭제

a.remove(40)
print(f'2. {a}')

# 원소 삽입 : 리스트.insert(인덱스, 원소)
a.insert(2, 100) # a[2]에 100을 삽입
print(f'3. {a}')

# 원소 위치 검색 : 리스트.index(원소)
n = a.index(20) # 없는 원소 검색시 오류 , if문을 사용하세요!
print(f'4. 20은 index {n}번에 위치한다')

# 원소 정렬:
#   리스트.sort() : 오름차순 정렬
#   리스트.sort(reverse=True) : 내림차순 정렬
a.sort(reverse=True)
print(f'5. {a}')

# 원소 역순 배치 : 리스트.reverse()  현재 리스트의 원소들의 순서를 역순으로 바꿈
b = [1, 7, 10, 5]
b.reverse()
print(f'6. {b}')

# 원소 확장 : 리스트.extend(리스트)
# '+=' 로 대체 가능.
a = [1, 2, 3]
b = [10, 20, 30]
a += b # a.extend(b)
print(f'7. a : {a} / b : {b}')

a = [1, 2, 3]
b = [10, 20, 30]
b += a
print(f'8. a : {a} / b : {b}')

# 중복 원소 개수 세기 : 리스트.count(원소)
a = [10, 20, 30, 10, 10, 20]
b = a.count(10)
print(f'9. 리스트 a에 10은 {b}개 있습니다.')

# 리스트 복사 하기 : 리스트.copy()
b = a.copy()
print(f'10. b : {b}')

# 모든 원소 삭제 : 리스트.clear()
b.clear()
print(f'11. b : {b}')