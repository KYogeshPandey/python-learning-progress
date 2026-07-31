 # Operations on list

# arithmetic operations(+ and *)

l1 = [1,2,3]
l2 = [4,5,6]
print(l1 +l2)

print(l1*3)


# membership operator

l1 = [1,2,3,4,5]
l2 = [4,5,6]

print(5 in l1)
print(5 in l2)
print(5 not in l2)


# Loops

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,[5,6,7]]
l3 = [[[1,2],[3,4]],[[5,6],[7,8]]]

for i in l3 :
    print(i)