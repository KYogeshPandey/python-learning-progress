# Functions of Numpy

import numpy as np

a = np.random.randint(1,100,25)
b = np.random.randint(1,100,24).reshape(6,4)

print(a)
print(b)

'''np.sort() function is used to sort an array in ascending order.
Syntax: numpy.sort(a, axis=-1, kind='quicksort', order=None)'''

# print(np.sort(a))
# print(np.sort(b))
# print(np.sort(b,axis=0)[::-1])
# print(np.sort(a)[::-1])


'''np.append() function is used to append values to the end of an array.
Syntax: numpy.append(arr, values, axis=None)'''

# print(np.append(a,200))
# print(np.append(b,200))
# print(np.append(b,np.ones((b.shape[0],1)),axis=1))
# print(np.append(b,np.ones((1,b.shape[1])),axis=0))

'''np.concatenate() function is used to join two or more arrays of the same shape along a specified axis.
Syntax: numpy.concatenate((a1, a2, ...), axis=0, out=None'''

# c = np.arange(6).reshape(2,3)
# d = np.arange(6,12).reshape(2,3)

# print(c)
# print(d)

# print(np.concatenate((c,d),axis =0))
# print(np.concatenate((c,d),axis =1))

'''np.unique() function is used to find the unique elements of an array.
Syntax: numpy.unique(a, return_index=False, return_inverse=False, return_counts=False)'''

# e = np.array(([1,1,2,2,3,3,4,4,5,5,6]))
# print(np.unique(e))
# print(np.unique(e,return_counts=True))

'''np.expand_dims() function is used to expand the shape of an array by adding a new axis at the specified position.
Syntax: numpy.expand_dims(a, axis)'''

# print(np.expand_dims(a,axis=0))
# print(np.expand_dims(a,axis=1))
# print(np.expand_dims(b,axis = 0))
# print(np.expand_dims(b,axis = 1))

'''np.where() function is used to return the indices of elements in an input array that satisfy a given condition.
Syntax: numpy.where(condition[, x, y])'''

# print(np.where(a>50))
# print(np.where(a>50,0,a))

'''np.argmax() function is used to return the indices of the maximum values along an axis.
Syntax: numpy.argmax(a, axis=None, out=None)'''

# print(np.argmax(a))
# print(np.argmax(b,axis=0))
# print(np.argmax(b,axis=1))

'''np.argmin() function is used to return the indices of the minimum values along an axis.
Syntax: numpy.argmin(a, axis=None, out=None)'''

# print(np.argmin(a))
# print(np.argmin(b,axis=0))
# print(np.argmin(b,axis=1))

'''np.cumsum() function is used to return the cumulative sum of the elements along a given axis.
Syntax: numpy.cumsum(a, axis=None, dtype=None, out=None)'''

# print(np.cumsum(a))
# print(np.cumsum(b,axis=0))
# print(np.cumsum(b,axis=1))

'''np.cumprod() function is used to return the cumulative product of the elements along a given axis.
Syntax: numpy.cumprod(a, axis=None, dtype=None, out=None)'''

# print(np.cumprod(a))
# print(np.cumprod(b,axis=0))
# print(np.cumprod(b,axis=1))

'''np.percentile() function is used to compute the nth percentile of the elements along a given axis.
Syntax: numpy.percentile(a, q, axis=None, out=None, overwrite_input=False,'''

# print(np.percentile(a,100))
# print(np.percentile(a,50))
# print(np.percentile(a,0))

'''np.histogram() function is used to compute the histogram of a set of data.
Syntax: numpy.histogram(a, bins=10, range=None, normed=None, weights'''

# print(np.histogram(a,bins=[10,20,30,40,50,60,70,80,90,100]))

'''np.corrcoef() function is used to compute the correlation coefficient between two arrays.
Syntax: numpy.corrcoef(x, y=None, rowvar=True, bias=<no value'''

# salary = np.array(([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]))
# experience = np.array(([10,2,8,4,5,9,7,3,9,10]))

# print(np.corrcoef(salary,experience))

'''np.isin() function is used to test whether each element of an array is present in another array.
Syntax: numpy.isin(element, test_elements, assume_unique=False, invert=False)'''

# items = [10,20,30,40,50,60,70,80,90,100]
# print(np.isin(a,items))
# print(a[np.isin(a,items)])

'''np.flip() function is used to reverse the order of elements in an array along a specified axis.
Syntax: numpy.flip(m, axis=None)'''

# print(np.flip(a))
# print(np.flip(b))
# print(np.flip(b,axis = 0))
# print(np.flip(b,axis = 1))

'''np.put() function is used to set specific elements of an array to a given value.
Syntax: numpy.put(a, ind, v, mode='raise')'''

# np.put(a,[1,2], [100,200])
# print(a)

'''np.delete() function is used to delete specific elements from an array along a specified axis.
Syntax: numpy.delete(arr, obj, axis=None)'''

# print(np.delete(a,0))
# print(np.delete(a,[0,2,4]))

# Set functions 

'''Set functions are used to perform operations on sets, such as union, intersection, difference, and symmetric difference.'''

# m = np.array([1,2,3,4,5])
# n = np.array([4,5,6,7,8])

# print(np.union1d(m,n))
# print(np.intersect1d(m,n))
# print(np.setdiff1d(m,n))    
# print(np.setxor1d(m,n))
# print(np.in1d(m,1))

'''np.clip() function is used to limit the values in an array to a specified range.
Syntax: numpy.clip(a, a_min, a_max, out=None)'''

# print(np.clip(a,a_min = 25,a_max = 75))
