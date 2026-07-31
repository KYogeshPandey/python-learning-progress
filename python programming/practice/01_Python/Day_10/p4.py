#memory size

# tuple take less size as compare to list because tuple is immutable and list is mutable

import sys
l = list(range(1000))
t = tuple(range(1000))

print('list size :' , sys.getsizeof(l))
print('tuple size:' , sys.getsizeof(t))



