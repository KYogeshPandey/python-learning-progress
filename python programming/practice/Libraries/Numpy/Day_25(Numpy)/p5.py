# Working with missing values
import numpy as np

a = np.array([1,2,3,4,np.nan,6])
print(a[np.isnan(a)])
print(a[~np.isnan(a)])
# print(np.isnan(a))
# print(a)