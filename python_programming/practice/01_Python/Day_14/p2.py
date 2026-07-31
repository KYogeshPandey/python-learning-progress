# Lambda function

#it can take any number of argumens , but have only ane expression
# it is used foe HOF(higher order function)

a = lambda x : x**2
print(a(3))

b = lambda x,y : x+y
print(b(3,4))


a = lambda x : 'even' if x %2 == 0 else 'odd'
print(a(7))