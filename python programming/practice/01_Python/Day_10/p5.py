# list are error prone 

a = [1,2,3,4,5]
b = a

a.append(6) 
print(a)
print(b)  # b also changes because a and b are pointing to the same list in