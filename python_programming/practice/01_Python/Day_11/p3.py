# adding

s = {1,2,3}
s.add(4)
s.update([5,6,7])
print(s)

 
# deleting
s = {1,2,3,4,5}
print(s)
del s
print(s)  # NameError: name 's' is not defined because we have deleted the set s using del keyword, so it is no longer defined in the current scope.

# discard

s = {1,2,3,4,5}
s.discard(5)
print(s)       # {1, 2, 3, 4} because discard method removes the specified element from the set if it is present, 
                # but does not raise an error if the element is not found in the set.

# remove
s1 = {1,2,3,4,5}
s1.remove(4)
print(s1)       # {1, 2, 3} because remove method removes the specified element from the set if it is present, 
                # and raises a KeyError if the element is not found in the set.