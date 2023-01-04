"""

    두 개의 선을 plot 에 띄우기 (plot 2개)
    선1 - 실선, 빨강
          사용자에게 총 5개의 정수를 입력 받음
    선2 - 점선, 파랑
          1 ~ 100 사이의 랜덤 5개

"""
from matplotlib import pyplot as plt
import random
x = ['1', '2', '3', '4', '5']
lst = [''] * 5
for i in range(5):
    lst[i] = int(input('정수 입력 : '))
y = lst

lst = [''] * 5
for i in range(5):
    a = random.randint(1, 100)
    lst[i] = a
z = lst
plt.plot(x, y, color = 'red', linestyle = 'solid')
plt.plot(x, z, color = 'blue', linestyle = 'dotted')

plt.title('Quiz')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
