import numpy as np

# a = np.array([1,2,3,4,5])

# print(a)

# b = np.array([[1,2,3],[4,5,6]])
# print(b)

c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)

d = np.array([1,2,3], dtype = bool)
print(d)

print(np.array([1,2,3], dtype = complex))

e = np.arange(1,11,2)
print(e)

print(np.arange(1,13).reshape(4,3))

print(np.ones((2,3)))
print(np.zeros((3,4)))
print(np.random.random((3,4)))


print(np.linspace(-10,10,10,dtype = int))

print(np.identity(3))