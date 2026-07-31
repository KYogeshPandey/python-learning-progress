# Example for Decorator

# execution time of a function

import time

def timer(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        print('Execution time is', func.__name__,time.time()-start_time,'secs')
    return wrapper

@timer
def hello():
    print('Hello World')
    time.sleep(2)

# @timer
# def display():
#     print('Displaying something') 
#     time.sleep(4)

hello()
# display()

@timer
def square(num):
    time.sleep(1)
    print(num**2)

@timer
def power(a,b):
    time.sleep(2)
    print(a**b)

square(5)
power(2,3)
