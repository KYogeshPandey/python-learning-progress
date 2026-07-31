# A Big Problem

def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args) == data_type:
                func(*args)
            else:
                raise TypeError('ye dtabase nhi chalega')
        return inner_wrapper
    return outer_wrapper

@sanity_check(int)
def square(num):
    print(num**2)

@sanity_check(str)
def greet(name):
    print('Hello',name)

greet('yogesh')
square(2)