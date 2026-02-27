s={2,4,2,6}
print(type(s))                   #set is a collection which is unordered and unindexed. No duplicate members.
print(s)                          #sets are unordered so the output may be different every time you run the program
s.add(8)                          #this will add the element 8 to the set s

info ={'carla', 19,False,5.9,19}
print(info)                       #sets do not allow duplicate members so the output will not contain duplicate values

harry={}
print(type(harry))               #this will print <class 'dict'> because {} is used to create a dictionary in python, not a set. To create an empty set we can use set() function.

harry=set()
print(type(harry))               #this will print <class 'set'> because we have created an empty set using set() function   

for value in info :
    print(value)



    #set methods

# s1={1,2,5,7}
# s2={3,9,8}
# # print(s1.union(s2))
# # print(s1,s2)
# s1.update(s2)
# print(s1)



c1={1,2,3,4}
c2={3,4,5,6}
c3={4,5,6,7}
c4={2,4}

c1.intersection(c2)
# c1.intersection(c3)
print(c1.intersection(c2))
print(c1.intersection(c3).intersection(c2))


print(c1.isdisjoint(c2))
print(c1.issuperset(c4))
print(c4.issubset(c1))
c1.add(5)
c1.remove(3)
# c1.remove(9)
c1.discard(2)
c1.discard(9)
print(c1)
c2.pop()
print(c2)
c3.clear()
print(c3)
# del(c4)
print(c4)

