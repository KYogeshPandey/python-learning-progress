# number greater than 5

l = [1,2,3,4,5,6,7,8,]
print(list(filter(lambda x : x>5,l)))


# fetch fruits starting with a 

fruits = ['apple', 'guava' 'cherry']
print(list(filter(lambda x : x.startswith('a'), fruits)))


# Reduce

# sum of all items

import functools

print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5]))


# find min

print(functools.reduce(lambda x,y: x if x<y else y, [23,22,11,45,34]))