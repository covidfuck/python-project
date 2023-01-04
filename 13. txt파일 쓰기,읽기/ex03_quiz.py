"""

    구구단 2단.txt, 3단.txt ~~~ 9단.txt 생성
"""

for i in range(2, 10):
    filename = f'{i}단.txt'
    f = open(filename, "w")
    for j in range(1, 10):
        f.write(f'{i} x {j} = {i * j}\n')  # write
    f.close()


