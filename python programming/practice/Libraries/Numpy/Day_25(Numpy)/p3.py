#  Broadcasting

import numpy as np

a = np.arange(12).reshape(4,3)
b = np.arange(3)
print(a+b)

c = np.array([1])
d  = np.arange(4).reshape(2,2)
print(c+d)

e = np.arange(3).reshape(1,3)
f = np.arange(4).reshape(4,1)
print(e+f)