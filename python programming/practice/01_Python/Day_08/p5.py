# functions for list

l = [1,2,3,4,5]
print(len(l))
print(min(l))
print(max(l))
print(sorted(l, reverse = True))


# count

l = [1,2,1,3,4,5,1]
print(l.count(1))

# index

l = [1,2,1,3,4,5,1]
print(l.index(5))

# Reverse

l = [2,1,7,5,0]
l.reverse()      # permanently change the list
print(l)

# sort (vs sorted)

l = [2,1,7,5,0]
print(l)
print(sorted(l))
print(l)
l.sort()             # permanent change
print(l)


# copy  -> shallow copy

l = [1,2,3,4,5]

print(l)
print(id(l))
l2 = l.copy()
print(l2)
print(id(l2))