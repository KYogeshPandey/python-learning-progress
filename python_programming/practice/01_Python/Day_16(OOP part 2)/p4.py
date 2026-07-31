# reference variable

# object without a reference

class Person :

    def __init__(self,name,gender):
        self.name = 'nitish' 
        self.gender = 'male'


# Outside the class function
def greet(person):
    print('Hi my name is ', person.name ,'and i am a ', person.gender)
    p1 = Person('ankit','male')
    return p1 

p = Person('nitish','male')
x = greet(p)
print(x.name)
print(x.gender)
# q = p

# # Multiple ref

# print(id(p))
# print(id(q))


# # change the attribute value with the help of 2nd object

# print(p.name)
# print(q.name)
# q.name = 'ankit'    
# print(p.name)
# print(q.name)
# print(p.name)
