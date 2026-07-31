# list comprehension

# add i  to 19 numbers  to a list

l = [i for i in range(1,11)]

print(l)



# scalar multiplication on a vector

v = [1,2,3,4,5]
s = -3

x = [ i*s for i in v ]
print(x)
  

# add squares

l = [1,2,3,4,5]
x = [i**2 for i in l]
print(x)


# print( all numbers divisible by 5 in the range of 1 to 50)

x = [ i for i in range(1,50) if i%5 == 0]
print(x)

# nested if with list comprehension

basket = ['apple', 'banana', 'grapes', 'mango', 'orange']
my_fruits = ['apple', 'grapes', 'mango']

# add new_list with fruit and items if the fruit exist in the basket and starts with a 

x = [i for i in my_fruits if i in basket and i.startswith('a')]
print(x)

# print a 3*3 matrix with list comprehension

x = [ [i*j for i in range(1,4)] for j in range(1,4)]
print(x)


# cartesian product list comprehension on two sets

l1 = [1,2,3]
l2 = [4,5,6]

x = [[i*j for i in l1] for j in l2]
print(x)