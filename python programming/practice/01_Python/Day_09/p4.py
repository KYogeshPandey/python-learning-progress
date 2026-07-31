# lists are mutable

a = [1, 2, 3]
# b = a
b = a.copy()   # shallow copy of a list
print(a)
print(b)
a.append(4)
print(a)  
print(b)   # b is not changed because it is a copy of a