# DICTIONARY

# it is also know as maps or key arrays, assocaitive array

#1 Mutable
#2 Indexing has no meaning
#3 key's can't be duplicate
#4 key's can't be mutable items

# create Dictionary

d = {}

# 1D dictionary

d1 = {'name': 'John', 'age': 30, 'city': 'New York'}

# with mixed keys 

d2 = {(1,2,3):1, 'hello': 'world'}

# 2D dictionary

s = {
    'name': 'yogesh',
    'college': 'miet',
    'sem' : 6,
    'subjects' : {
        'python' : 90,
        'java' : 80,
        }
}

# using sequence and dict functions

d4 = dict([('name','nitish'),('age', 25), (3, 3)])

# duplicate keys

d5 = {'name': 'yogesh', 'name':'rahul'}

# mutable itesm as keys

d6 = {'name': 'yogesh', (1,2,3):2}

# accessing values

my_dict = {'name': 'yogesh', 'age': 20, 'city': 'delhi'}
print(my_dict['name'])
print(my_dict.get('age'))


# adding a key value pair

my_dict['country'] = 'india'
print(my_dict)


# remove a key value pair
d = {'name': 'yogesh', 'age': 20, 'city': 'delhi'}
# pop
d.pop('age')
print(d)

# popitem
d.popitem()
print(d)

# del
del d['name']
print(d)

# clear
d.clear()
print(d)

print(s['subjects']['python'])
s['subjects']['dsa'] = 93
print(s) 


del s['subjects']['java']
print(s)

# editing key value pair

s['subjects']['python'] = 95
print(s)