# Accessing items from a list

# Indexing
l = [[1, 2, 3, [1, 2]], [1, 2, 3, 4, [1, 2, 3, 4]]]
print(l[-1][-1][-2])

# Slicing

l = [1,2,3,4,5,6]

print(l[1::2])
print(l[-5:-2:2])


#append

l= [1,2,3,4,5]
l.append(True)
l.append([6,7,8])
print(l)

#extend

l = [1,2,3,4,5]
l.extend([6,7,8])
l.extend('delhi')
print(l)


#insert

l = [1,2,3,4,5,6]
l.insert(1,100)
print(l)

# Editing items in a list

l = [1,2,3,4,5]

l[-1] = 800 
l[1:4] = [200, 300, 400]
print(l)

# deletion

l = [1,2,3,4,5]
print(l)
del l[0]       # index se delete
del l[1:3]     # slice se delete
print(l)


# remove

l = [1,2,3,4,5]
l.remove(5)      # value se delete
print(l)


# pop 
l = [1,2,3,4,5]
l.pop(2)        
print(l)


# clear
l = [1,2,3,4,5]
l.clear()       # list ko empty kar deta hai
print(l)
