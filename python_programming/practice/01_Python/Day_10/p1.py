t1 = ()
print(t1)
t2 = (2,)
print(t2)
print(type(t1)) 
print(type(t2))


t4 = (1,2,3,(4,5))  
print(t4)

#using type conversion

t6 = tuple('hello')
print(t6)


#indexing

print(t4)
print(t4[0])
print(t4[-1])


# tuples are immutable 

# adding items in tuple is not possible but we can concatenate two tuples

print(t4[-1:-3:-1])  # slicing in reverse order