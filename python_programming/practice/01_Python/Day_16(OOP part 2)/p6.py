class Person :

    def __init__(self,name,gender):
        self.name = 'nitish' 
        self.gender = 'male'


# Outside the class function
def greet(person):
    person.name = 'ankit'
    return person

p = Person('nitish','male')
print(id(p))
p1 = greet(p)
print(id(p))