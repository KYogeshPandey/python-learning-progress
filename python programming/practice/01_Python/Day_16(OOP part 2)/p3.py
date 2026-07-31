class Person :
    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input

    def greet(self):
        if self.country == 'india':
            print('Namaste',self.name)
        else:
            print('Hello',self.name)

# How to access attributes
P = Person('nitish','india')


print(P.country)

# how to access methods
P.greet()

# Attribute creation from outside of the class

P.gender = 'male'

     