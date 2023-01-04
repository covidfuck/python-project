a = {
    'a' : 10,
    'b' : [10, 20, 30],
    'c' : [ {'name' : '홍길동', 'age' : 10}, {'name' : '피카츄', 'age' : 12}],
    'd' : {'x':[True, False]}
}

print(a['a']) # 10
print(a['b'][2]) # 30
print(a['c'][0]['age']) # 10
print(a['d']['x'][0]) # True