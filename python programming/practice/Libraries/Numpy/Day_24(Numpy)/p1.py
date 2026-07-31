# Indexing and slicing

import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

print(a1)
print(a2)
print(a3)

print(a1[-1])
print(a1[0])
print(a2[1,2])
print(a3[1,0,1])
print(a3[0,0,0])
print(a1[2:5])
print(a1[2:5:2])
print(a2[0,:])
print(a2[:,2])


# slicing

print(a3[1])
print(a3[::2])