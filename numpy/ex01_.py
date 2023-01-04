import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
print(a1)
print(type(a1))
print(a1.shape)
print(a1[0], a1[1], a1[2], a1[3], a1[4])
a1[0] = 4
a1[1] = 5
a1[2] = 6
print(a1)

a2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a2)
print(a2.shape)
print(a2[0,0], a2[1,0], a2[2,0])

a3 = np.array([[[1,2,3], [4,5,6], [7,8,9]],
              [[1,2,3], [4,5,6], [7,8,9]],
              [[1,2,3], [4,5,6], [7,8,9]]])
print(a3)
print(a3.shape)

a4 = np.zeros(10)
print(a4)
a4 = np.ones(5)
print(a4)
a4 = np.full((3,3), 1.23)
print(a4)
a4 = np.empty(10)
print(a4)

print(a1)
a4 = np.full_like(a1, 15)
print(a4)

a5 = np.arange(0, 30, 2)
print(a5)

a5 = np.linspace(0, 5, 20)
print(a5)

a5 = np.random.randint(0,10 ,(3,3))
print(a5)

print(np.random.normal(0, 1 ,(3,3)))

date = np.array("2022-09-07", dtype=np.datetime64)
print(date)
date1 = date + np.arange(12)
print(date1)

def array_info(array):
    print(array)
    print("ndim:", array.ndim)
    print("shape:", array.shape)
    print("dtype:", array.dtype)
    print("size:", array.size)
    print("itemsize:", array.itemsize)
    print("nbytes:", array.nbytes)
    print("strides:", array.strides)

array_info(a1)

print(a1)
print(a1[0:2])

print(a1)
bi = [False, True, True, False, True]
print(a1[bi])

print(a2)
b2 = np.insert(a2, 1, 10, axis = 0)
print(b2)
c2 = np.insert(a2, 2, 15, axis=1)
print(c2)