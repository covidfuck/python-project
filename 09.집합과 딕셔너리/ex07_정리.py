# 리스트 생성 : list()
a = list('abc') # str -> list
print(a)

a = list((1,2,3,4,5)) # tuple -> list
print(a)

a = list( {'a' : 10, 'b' : 20, 'c' : 30}) # dictionary -> list
print(a)

# set 생성 : set()
a = set("Hello, Python!!!!!")
print(a)

a = set({'a' : 10, 'b' : 20, 'c' : 30})
print(a)

a = set([10,20,30,40,50])
print(a)

# tuple 생성 : tuple()
a = tuple([10,20,30,40,50])
print(a)

a = tuple('PYTHON!!')
print(a)

a = tuple({'a' : 10, 'b' : 20, 'c' : 30})
print(a)

# 딕셔너리 생성 : dict()
a = dict([('a', 1), ('b', 2), ('c', 3)])
print(a)

a = list() # a = []
b = set() # b = set() (주의! b = {}는 안됨) why? 빈 딕셔너리가 생성되기 때문
c = tuple() # c = ()
d = dict() # d = {}

# 원소 1개짜리 tuple 만들기
a = (10,)
print(a, type(a))
