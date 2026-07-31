# write a program to add items of two list indexwise

l1 = [1,2,3]
l2 = [-1,-2,-3]

# l3 = [l1[i] + l2[i] for i in range(0,len(l1))] 
# print(l3)


l4 = list(zip(l1,l2))   # zip function to combine two list into a list of tuples
print(l4)
print([i+j for i,j in zip(l1,l2)])
