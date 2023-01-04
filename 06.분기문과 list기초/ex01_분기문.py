print('---- break test ----')
for i in range(10, 0, -1):
    if i % 4 == 0:
        break
    print(i)

print('---- continue test----')
for i in range(10, 0, -1):
    if i % 4 == 0:
        continue
    print(i)