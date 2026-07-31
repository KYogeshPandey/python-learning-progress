class Employee():
    def __init__(self):
        self.__name="Yogesh"

a=Employee()
# print(a.__name)     #cannot be accessed directly because it is private variable
print(a._Employee__name)    #can be accessed using name mangling syntax
print(a.__dir__())    #to see the list of all the attributes of the class