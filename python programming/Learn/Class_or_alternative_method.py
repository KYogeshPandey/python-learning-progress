class Employee:
    def __init__(self, name , id):
        self.name = name 
        self.id = id

    @classmethod
    def from_str(cls, string):
        return cls (string.split("-")[0], int(string.split("-")[1]))
        
e1 = Employee("yogesh", 101)
print(e1.name)
print(e1.id)

string = "aman- 102"
e2 = Employee.from_str(string)
print(e2.name)
print(e2.id)
