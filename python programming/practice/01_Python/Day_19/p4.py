# PICKLING

# pickling is the process in which python object are converted into byte streams and
# unpickling is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print('Hi my name is ',self.name, 'and I am ', self.age,'years old')

p = Person('Nitish',33)

# pickle dump
import pickle
from pprint import pp
with open('person.pkl','wb') as f:
    pickle.dump(p,f)


# pickle load
import pickle
with open('person.pkl','rb') as f :
    p = pickle.load(f)

p.display_info


# Pickle Vs Json

#pickle lets the user to store data in binary format . JSON lets the user store data in a human readable text format