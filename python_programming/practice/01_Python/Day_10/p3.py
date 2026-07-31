# tuples are faster than lists
 
import time 

l = list(range(10000000))
t = tuple(range(10000000))

start = time.time()

for i in l :
    i*5

print('list time:', time.time() - start)

start = time.time()

for i in t:
    i*5

print('tuple time:', time.time() - start)



