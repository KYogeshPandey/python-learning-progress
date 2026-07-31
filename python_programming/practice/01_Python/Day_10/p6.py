# tuple unpacking

a,b,c =(1,2,3)
print(a,b,c)


a = 1
b = 2
a,b = b,a

print(a,b)

a,b,*others = (1,2,3,4,5)
print(a,b,others)

