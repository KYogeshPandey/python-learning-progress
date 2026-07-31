# serializing and deseralizing custom objects

class Person:
    def __init__(self,fname,lname,age,gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

person = Person('Nitish','Singh',33,'Male') 


import json

def show_object(person):
    if isinstance(person,Person):
        return "{} {} age -> {} gender ->{}".format(person.fname,person.lname,person.age,person.gender)

with open ('demo.json', 'w') as f :
    json.dump (person,f,default = show_object)

