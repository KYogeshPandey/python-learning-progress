 #Map

l=[1,2,4,5,3,6,4]
# def cube(x):
#     return x*x*x

newl= list(map(lambda x: x*x*x, l))
print(newl)

#Filter

def filter_function(a):
    return a>4

newnewl=list(filter(filter_function, newl))
print(newnewl)

#reduce
    
from functools import reduce

numbers = [1,2,3,4,5]

sum = reduce(lambda x,y: x+y, numbers)

print(sum)