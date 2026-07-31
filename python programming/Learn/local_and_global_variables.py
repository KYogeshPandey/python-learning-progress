x=4
print(x)

def hello():
    global x     # to modify the global variable x inside the function hello() we can use the global keyword followed by the name of the variable, which tells Python that we want to use the global variable x instead of creating a new local variable with the same name.
    x=5
    print(f"the local x is 5")
    print("hello Yogesh")
    
print(f"the global x is {x}")
hello()
print(f"the global x is {x}")