# set

s = set()    # empty set
print(type(s))

s1 = {1,2,3,4,5}
s2 = {2,3,4,4,5}
s3 = {1,4.5,True}
s4 = {1,1,2,2,3,3,4,4,5,5}
s5 = ([1,2,3])
# s6 = {1,2,3,[4,5]}  # unhashable type: 'list' because set is mutable and list is mutable
print(s2)
print(s1)
print(s3)
print(s4)
print(s5)
# print(s6)

s7 = {1,2,3}
s8 = {3,1,2}

print( s7 == s8)  # set is unordered collection of unique elements, so order does not matter and duplicates are not allowed


#accessing items is not allowes in set because set is unordered collection of unique elements, 
# so we cannot access items by index or key.
#  We can only iterate over the set or check for membership using 'in' keyword.