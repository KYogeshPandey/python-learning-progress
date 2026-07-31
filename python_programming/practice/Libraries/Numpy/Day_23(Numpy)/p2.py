# Array Attributes/Changing Datatype/Array operations/Array Functions

import numpy as np

a1 = np.arange(10,)
a2 = np.arange(12,dtype = float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

# #ndim

# print(a3.ndim)
# print(a2.ndim)
# print(a1.ndim)


# # shape

# print(a3.shape)
# print(a2.shape)
# print(a1.shape)

# # size

# print(a1.size)
# print(a2.size)
# print(a3.size)

# # itemsize

# print(a3.itemsize)
# print(a2.size)
# print(a1.size)

# # dtype

# print(a1.dtype)
# print(a2.dtype)
# print(a3.dtype)

# # Changing Datatype

# # asdatatype

# print(a3.astype(np.int32))

# # array operations

# a4 = np.arange(1,13,dtype = int).reshape(3,4)
# a5 = np.arange(12,24,dtype=int).reshape(3,4)

# # scalar operations

# print(a4)
# print(a4*2)
# print(a4+2)

# print(a4>7)
# print(a5>=15)
# print(a5 == 20)

# # vector operstions

# print(a4 + a5)
# print(a4-a5)
# print(a4/a5)
# print(a4%a5)

# Array Functions

a1 = np.arange(12).reshape(3,4)
# a1 = np.round(a1 * 100)

# print(np.max(a1))
# print(np.min(a1))
# print(np.sum(a1))
# print(np.min(a1,axis=0))
# print(np.prod(a1, axis = 0))

print(a1)

print(np.mean(a1))
print(np.median(a1))
print(np.std(a1,axis =0))
print(np.var(a1,axis = 1))

print(np.sin(a1))

a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)

print(np.dot(a2,a3))

print(np.log(a1))
print(np.exp(a1))

print(np.round(np.random.random((3,4))*100))
print(np.floor(np.random.random((3,4))*100))
print(np.ceil(a2))
