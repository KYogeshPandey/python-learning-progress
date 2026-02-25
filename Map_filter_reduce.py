l=[1,2,4,5,3,6,4]
def cube(x):
    return x*x*x

newl= list(map(cube, l))
print(newl)