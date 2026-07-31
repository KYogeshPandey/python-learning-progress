# Namespaces and decorators

# Namespaces  AND LEGB rule

# Builtin namespace
# Global Namespace
# Enclosing Namespace
# Local Namespace



# Local and Global

a =2           # Global

def temp():
    b= 3       # Local
    print(b)

temp()
print(a)

# EDITING IN GLOBAL VARIABLE

a =2           # Global

def temp():
    global a
    a+=1       # Local
    print(a)

temp()
print(a)

# creating a global variable inside local scope

def temp():
    # local variable
    global a
    a = 1
    print(a)

temp
print(a)        


# function parameter is local

def temp(z):
    # local variable
    print(z)

a = 5
temp(5)
print(a)