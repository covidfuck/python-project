# 학생 n명의 이름을 모두 input()으로 입력 받고 이들을 print로 출력
n = 5
names = [""] * n
print(names)

for i in range(n):
    names[i] = input(f'{i} 번째 학생 이름 : ')

print(names)