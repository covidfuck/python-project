"""
    재귀호출 (recursive call)
        함수가 자기자신을 실행하는 것


"""
# 5! => 5 * 4 * 3 * 2 * 1
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

a = fact(5)
print(a)



