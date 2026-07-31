# As a dict

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
        return{'name':person.fname + ' ' + person.lname, 'age':person.age, 'gender': person.gender}
    
with open('demo.json','w') as f :
    json.dump(person,f,default=show_object,indent=4)

# deserializing

import json

with open('demo.json', 'r') as f:
    print(json.load(f))