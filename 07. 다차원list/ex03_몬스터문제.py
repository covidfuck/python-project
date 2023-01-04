"""

10 X 10 짜리 이차원 리스트 map이 있다.
map = [[0] * 10] * 10

# 1. 랜덤한 위치에 30마리의 몬스터를 배치해보자.
#	몬스터는 1로 표시한다.
#    (중복 위치 허용)

# 2. 사용자에게 행, 열 순서로 2개의 정수를 입력 받고
#    해당 칸에 위치를 표시한 결과를 출력해보자. (유저는 2로 표시한다.)

# 3. 사용자에게 원하는 공격 범위를 정수형으로 입력 받고
#    사용자의 위치에서 공격 가능한 몬스터의 개수를 출력해보자.

"""
import random
mon = 0 # 몬스터 수

map = [ [0 for n in range(10)] for m in range(10)]

while mon < 30:
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    # if map[a][b] == 1: # 몬스터 위치 중복 x
        # continue
    map[a][b] = 1
    mon += 1

for i in range(10):
    for j in range(10):
        print(f'{map[i][j]}', end = '\t')
    print()

row = int(input("행(row)을 입력해 주세요 : "))
col = int(input("열(column)을 입력해 주세요 : "))

map[row][col] = 2

for i in range(10):
    for j in range(10):
        print(f'{map[i][j]}', end = '\t')
    print()

rag = int(input("공격 사거리를 입력해주세요 : "))

total = 0

행_시작 = row - rag
if 행_시작 < 0:
    행_시작 = 0

행_끝 = row + rag
if 행_끝 >= 10:
    행_끝 = 9

열_시작 = col - rag
if 열_시작 < 0:
    열_시작 = 0

열_끝 = col + rag
if 열_끝 >= 10:
    열_끝 = 9

for 행 in range(행_시작, 행_끝+1):
    for 열 in range(열_시작, 열_끝+1):
        if map[행][열] == 1:
            total += 1

print(f'공격사거리가 {rag}일때 사용자의 위치에서 공격가능한 몬스터의 수는 {total}마리 입니다.')

#
# for i in range(rag+1):
#     if i != rag:
#         for j in range(rag+1):
#             if row >= rag - i and col >= rag - j and j != rag:
#                 total += map[row - rag + i][col - rag + j] # 3 3 3 4, 4 3 4 4
#                 total += map[row - rag + i][col + rag - j] # 3 7 3 6, 4 7 4 6
#                 total += map[row + rag - i][col - rag + j] # 7 3 7 4, 6 3 6 4
#                 total += map[row + rag - i][col + rag - j] # 7 7 7 6, 6 7 6 6
#             if row < rag - i and col >= rag - j and j != rag:
#                 total += map[row + rag - i][col - rag + j]  # 7 3 7 4, 6 3 6 4
#                 total += map[row + rag - i][col + rag - j]  # 7 7 7 6, 6 7 6 6
#             if row >= rag - i and col < rag - j and j != rag:
#                 total += map[row - rag + i][col + rag - j]
#                 total += map[row + rag - i][col + rag - j]
#             if row < rag - i and col < rag - j and j != rag:
#                 total += map[row + rag - i][col + rag - j]
#             if row >= rag - i and j == rag:
#                 total += map[row - rag + i][col - rag + j]
#                 total += map[row + rag - i][col - rag + j]
#             if row < rag - i and j == rag:
#                 total += map[row + rag - i][col - rag + j]
#     if i == rag:
#         for j in range(rag):
#             if col >= rag - j:
#                 total += map[row - rag + i][col - rag + j]
#                 total += map[row + rag - i][col + rag - j]
#             if col < rag - j:
#                 total += map[row + rag - i][col + rag - j]
#
# for i in range(10):
#     for j in range(10):
#         print(f'{map[i][j]}', end = '\t')
#     print()
#
# print(f'공격사거리가 {rag}일때 사용자의 위치에서 공격가능한 몬스터의 수는 {total}마리 입니다.')













