"""

    미완성 일떄 pass 씀
    ex) 밑에 if n < 2 안에 조건식을 넣어야 하는데 아직
        써야할 조건식이 미완성일때 pass를 임시로 사용하면
        error가 나지 않는다.
"""



import random

n = random.randint(1, 10)
print(n)

if n < 2:
    pass
elif n < 8:
    print(f'{n}(은)는 2 이상 8 미만이다~')
else:
    pass