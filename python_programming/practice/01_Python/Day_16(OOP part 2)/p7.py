
# list of objects
class Person:
    
    def __init__(self,name,country):
        self.name = name
        self.country = country

p1 = Person('nitish','India')
p2 = Person('steve','Australia')
p3 = Person('mark','America')

l = [p1,p2,p3]

for i in l :
    print(i.name,i.country)

# Dict of objects

class Person:
    
    def __init__(self,name,country):
        self.name = name
        self.country = country

p1 = Person('nitish','India')
p2 = Person('steve','Australia')
p3 = Person('mark','America')

d = {'p1':p1,'p2':p2,'p3':p3}

for i in d :
    print(d[i].name,d[i].country)

