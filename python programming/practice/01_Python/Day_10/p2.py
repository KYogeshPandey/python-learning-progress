#operations on tuples

# len/sum/max/min/sorted

t1 =(1,2,3,4,5)
t2 = (6,7,8,9,10)
print(len(t1))
print(sum(t1))
print(max(t1 + t2))
print(min(t1 + t2))
print(sorted(t1, reverse=True))  # sorted in reverse order 


# count

print(t1.count(2))  # count the number of occurrences of 2 in the tuple t
print(t1.index(3))  # find the index of the first occurrence of 3 in the tuple t