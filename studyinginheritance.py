class Employee:
    def __init__(self,name,id):
        self._name= name
        self._id = id

    def showdetails(self):
        print(f"the name of the employee {self._id } is :{self._name}")

class Programmer(Employee):
    def showlanguage(self):
        print("the default language is python")


e1 =Programmer("mohit kumar", 123) 
e1.showdetails()
e1.showlanguage()