# built in scope

import builtins
print(dir(builtins))

# renaiming built in function

# l =[1,2,3]
# max(l)

# def max():
#     print('hello')

# max(l)

# Enclosing scope

def Outer():
    # a = 3
    def inner():
        # a = 4
        print(a)
    inner()
    print('outer function')
a = 1
Outer()
print('main program')

# nonlocal keyword

def Outer():
    a = 3
    def inner():
        nonlocal a
        a+=1
        print('inner',a)
    inner()
    print('outer',a)

Outer()
print('main program')
print('done')