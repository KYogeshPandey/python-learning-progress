# Decorators

# A decorator is a function that receives another function as input and adds some functionality to it and returns it.

# there are two types of decorators available in python 
# Built in decorators (@staticmethod, @classmethod, @property)
# user defined decorators that we programmers can create according to our needs

def modify(func,num):
    return func(num)

def square(num):
    return num**2

modify(square,2)



def my_decorator(func):
    def wrapper():
        print('*************************')
        func()
        print('*************************')
    return wrapper

@my_decorator
def hello():
    print('Hello')

@my_decorator  
def display():
    print('Hello World')
                
hello()
display()

