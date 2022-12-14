"""
1. 구구단 2단 출력
"""
"""
for n in range(2, 10):  # 2 <= n < 10
    print(f'2 X {n} = {2 * n}')
"""
"""
2. 2단 ~ 9단 모두 출력
"""
print("================================================ 구구단 ================================================")
for a in range(2,10):
    for b in range(1,10):
        print(f"{a} x {b} = {a*b}", end = "  ")
    print("\n")
"""
3. 1 ~ 1000 사이의 11과 13의 공배수를 출력
  (그 개수도 출력)
"""
n = 0
for a in range(1, 1001):
    if (a % 11 == 0 and a % 13 == 0):
        print(a)
        n += 1
print(f"1 ~ 1000 사이에 있는 11과 13의 공배수의 갯수는\n{n}개 입니다.")
"""

4. 1 ~ 1000 까지의 홀수를 모두 더하면?
"""
n = 0
for a in range(1, 501):
    n += 2*a-1
print(f"1 ~ 1000 사이에 있는 모든 홀수의 합은\n{n} 입니다.")



