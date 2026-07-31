# Advanced Indexing

# Fancy Indexing

import numpy as np

a1 = np.arange(24).reshape(6,4)
 
print(a1[[0,2,3,5]])
print(a1[:,[0,2,3]])

# Boolean Indexing

a2 = np.random.randint(1,100,24).reshape(6,4)

# find aall numbers greater than 50
print(a2[a2>50])

# Even numbers

print(a2[a2%2==0])

# greter than 50 and even numbers

print(a2[(a2>50)&(a2%2==0)]) 

# Find all numbers not divisible by 7

print(a2[a2%7!=0])
print(a2[~(a2%7 == 0)])