# Stacking

import numpy as np

a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

print(np.hstack((a4,a5,a5,a4)))
print(np.vstack((a4,a5,a4)))

# splitting

print(np.hsplit(a4,2))
print(np.vsplit(a5,3))