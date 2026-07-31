# _dir__

x=(1,2,3)
print(dir(x))
print(x.__add__)
print(x.__add__(x))

#__dict__

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1


p1=person("yogesh",22)
print(p1.__dict__)
# print(help(str))
print(help(person))