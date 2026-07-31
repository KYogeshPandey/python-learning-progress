# Functions are 1st class citizen

# type and id
def square(num):
    return num**2

print(type(square))
print(id(square))


# reassign

x = square
id(x)

print(x(3))

# deleting a function

# del square

print(square(3))

# storing

l = [1,2,3,4,square]
print(l[-1](3))

s = {square}
print(s)


# returning  function

def f():
    def x(a,b):
        return a+b
    return x

val = f()(3,4)
print(val)


# function as argument

def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_c')
    return z()

print(func_b(func_a))