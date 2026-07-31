l = [1,2,3,4]
l.append(5)
print(l)



# Variable Scope

def g(y):
    print(x)
    print(x+1)

x = 5
g(x)
print(x)


def g(y):
    x = 1
    x += 1
    print(x)
x = 5
g(x)
print(x)


def h(y):
    global x       # global keyword not a good practice
    x = x+ 1
    print(x)
x = 5
h(x)
print(x)

