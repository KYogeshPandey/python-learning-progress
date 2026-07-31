# Types of arguments

# default argument
# positional argument
# keyword argument

# default argument
def power(a=1,b=1):
    return a**b

print(power(2))

# positional argument

print(power(2,3))    


# Keyword argument

print(power(b=3,a=2))


# *args and **kwargs

"""
* args

allow us to pass a variable number of non keyword argument to a function
"""

def multiply(*args):
    product = 1

    for i in args:
        product = product * i

    
    print(args)
    return product


"""
**kwargs

it allows us to pass any number of keyword arguments .
"""

def display(**kwargs):

    for (key,value) in kwargs.items():
        print(key,'->',value)

display(india= 'delhi', srilanka = 'colombo', nepal = 'kathmandu', pakistan = 'islamabad')

