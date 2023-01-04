import numpy as np

lst1 = [10, 20, 30, 40, 50]
lst2 = [2, 4, 6, 8, 10]

arr1 = np.array(lst1)
arr2 = np.array(lst1)

print(lst1, type(lst1))
print(arr1, type(arr1))

print(arr1.shape) # (5,)

lst3 = [[1,2,3], [4,5,6]]
arr3 = np.array(lst3)
print(arr3.shape)
print(arr3.dtype)

arr4 = np.array([1.1, 2.2, 3.3])
print(arr4.shape)
print(arr4.dtype)

arr = np.zeros(5)
print(arr) # [0. 0. 0. 0. 0.]

arr = np.ones(5)
print(arr) # [1. 1. 1. 1. 1.]

arr = np.ones((2, 3))
print(arr) # [[1. 1. 1.] [1. 1. 1.]]

# 연산
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.arange(5)

print(arr1) # [10 20 30 40 50]
print(arr2) # [0 1 2 3 4]
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
# print(arr1 / arr2) # 0으로는 못나눔

arr6 = np.array([1, 2, 3, 4, 5])
print(arr6[arr6 % 2 == 0])

arr7 = np.random.rand(2, 3)
print(arr7)

