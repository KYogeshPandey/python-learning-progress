class Employee:
    companyName = "Apple"
    n0_of_employees = 0      #class variable
    def __init__(self, name):
        self.name = name     #instance variable
        self.increment = 5
        Employee.n0_of_employees +=1
    def showdetails(self):
        print(f"the name of the employee is {self.name} in the company {self.companyName} size and the increment of {self.n0_of_employees} is {self.increment}")

emp1 = Employee("mohit")
emp1.increment = 10
emp1.showdetails()
Employee.companyName = "Google"
emp2 =Employee("Yogesh")
emp2.increment = 50
emp2.showdetails()