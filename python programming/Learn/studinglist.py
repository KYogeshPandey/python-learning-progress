l=[3,8,0,34,'harry',True]
print(l)
print(type(l))
print(l[0])            #indexing
print(l[4])
print(l[-3])           #negative indexing
print(l[len(l)-3])     #positive indexing

if "harry" in l:
    print("yes")
else:
    print("no")


print(l)
print(l[1:5])



#List complrehension

list =[i for i in range(4)]
print(list)
list =[i*i for i in range(1,11) if i%2==0 ]
print(list)


#list methods

l=[1,5,4,6]
l.append(7)         #append adds an element at the end of the list 
l.sort()            #sorts the list in ascending order
l.reverse()         #reverses the list
print(l.index(4))   #returns the index of the first occurrence of the specified value
print(l.count(3))   #returns the number of occurrences of the specified value
m=l
m[0]=0              #this will change the value of l as well because m and l are pointing to the same list in memory
n=l.copy()          #this will create a new list n which is a copy of l, so changes in n will not affect l
n[2]=3              #this will change the value of n but not l
n.insert(1,800)     #this will insert 800 at index 1 in the list n
t=[88,90,98, 'yogesh']
n.extend(t)         #this will add the elements of list t to the end of list n
k=n+l+m+t           #this will concatenate the lists n, l, m and t and create a new list k

print(l)
print(n)
print(k)