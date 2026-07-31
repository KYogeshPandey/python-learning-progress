#Pass by refernece

class Person :

    def __init__(self,name,gender):
        self.name = 'nitish' 
        self.gender = 'male'


# Outside the class function
def greet(person):
    print(id(person))
    person.name = 'ankit'
    print('Hi my name is ', person.name ,'and i am a ', person.gender)

p = Person('nitish','male')
print(id(p))
greet(p)
print(p)
