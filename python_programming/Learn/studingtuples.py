tup=(1,2,6,3)
print(type(tup))                   #tuple is a collection which is ordered and unchangeable
print(tup[0])                      #indexing
tup1=(1,2,76,'yogesh',True)        
print(tup1[1])                     
print(len(tup1))                   #length of the tuple
print(tup1[-1])                    #negative indexing   
if 76 in tup1 :
    print('yes')
tup1=list(tup[1:4])                #slicing
print(tup1)                      
print(tup1[2:5:2])                 #tuple slicing with step


countries=('india','usa','japan','china')
temp=list(countries)               #tuples are immutable so we cannot change the value of a tuple but we can convert it to a list and then change the value and then convert it back to a tuple
temp[2]='russia'                   #this will change the value of the list temp but not the tuple countries
print(countries)               
print(type(countries)) 
temp.pop(3)                        #this will remove the element at index 3 from the list temp
countries=tuple(temp)
print(countries)
countries2=('germany','france')
countries=countries+countries2     #this will concatenate the tuples countries and countries2 and create a new tuple countries
print(countries)

countries.count('india')                   #this will return the number of occurrences of 'india' in the tuple countries
countries.index('usa')                    #this will return the index of the first occurrence of 'usa
res=countries.index('china')               #this will return the index of the first occurrence of 'china
tuple=(0,1,2,3,2,3,1,3,2)
res=tuple.index(2,1,3)                     #this will return the index of 'india' in countries tuple between indices 1 and 3
print(res)


