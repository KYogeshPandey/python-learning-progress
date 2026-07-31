# Inheritance

class User:

    def __init__(self):
        self.name = 'ankit'
        self.gender = 'male'

    def login(self):
        print('login')


class Student(User):

    # def __init__(self):
    #     self.rollno = 116

    def enroll(self):
        print('enroll into the course')

s = Student()
u = User()

print(u.name)
print(s.name)
s.login()
s.enroll()
