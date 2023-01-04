"""

    clear() 는 원소들만 삭제 (리스트는 유지)
    완적 삭제는 'del' 사용
        del a

"""
a = [1, 2, 3, 4]
a.clear()
print(f'a : {a}')

del a
# print(a) <-- 에러!
# del은 모든것을 지운다!

"""
    'b = a' 와 'b = a.copy()' 의 차이
    
"""
a = [1, 2, 3, 4]
b = a # 얕은 복사
a[0] = 1000
print(f'a : {a}')
print(f'b : {b}')
print(f'a의 ID : {id(a)}')
print(f'b의 ID : {id(b)}')

a = [1, 2, 3, 4]
b = a.copy() # 깊은 복사
a[0] = 1000
print(f'a : {a}')
print(f'b : {b}')
print(f'a의 ID : {id(a)}')
print(f'b의 ID : {id(b)}')