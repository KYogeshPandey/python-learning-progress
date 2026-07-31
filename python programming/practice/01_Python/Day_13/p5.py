# Nested function

def f():
    def g():
        print('inside function g')
        # f()    # infinite loop
    g()
    print('inside function f')
f()