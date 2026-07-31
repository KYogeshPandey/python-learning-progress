import ctypes

class Mylist:

    def __init__(self):
        self.size = 1
        self.n = 0
        # create a ctype array(static,referential) with size = self.size
        self.A = self.__make_array(self.size)

    # len
    def __len__(self):
        return self.n

    #append
    def append(self,item):
        if self.n == self.size:
            #resize
            self. __resize(self.size*2)

        self.A[self.n] = item
        self.n = self.n + 1

    # pop
    def pop(self):
        if self.n == 0:
            return 'Empty list'

        item = self.A[self.n - 1]
        self.n = self.n - 1
        return item

    # clear
    def clear(self):
        self.n = 0
        self.size = 1
        self.A = self.__make_array(self.size)

    # find
    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i

        return ValueError('Item not in list')

    # insert
    def insert(self,pos,item):
        if not (0<= pos <= self.n):
            raise IndexError('Index out of range')
        
        if self.size == self.n:
            self.__resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1

    # delete
    def __delitem__(self,pos):
        if not (0 <= pos < self.n):
            raise IndexError("Index out of range")
        
        for i in range(pos,self.n-1):
            self.A[i] = self.A[i+1]

        self.n = self.n - 1 

    # remove
    def remove(self,item):
        pos = self.find(item)
        self.__delitem__(pos)
        return pos

    # sort
    def sort(self):
        for i in range(self.n - 1):
            swapped = False
            for j in range(self.n - 1 - i):
                if self.A[j] > self.A[j+1]:
                    temp = self.A[j]
                    self.A[j] = self.A[j+1]
                    self.A[j+1] = temp

                    swapped = True

            if not swapped:
                break

    # reverse
    def reverse(self):
        for i in range(self.n // 2):
            # swap
            temp = self.A[i]
            self.A[i] = self.A[self.n-1-i]
            self.A[self.n-1-i] = temp

    # max
    def max(self):
        if self.n == 0:
            raise ValueError ("max() called on an empty list")

        curr_max = self.A[0]

        for i in range(1,self.n):
            if curr_max < self.A[i]:
                curr_max = self.A[i]

        return curr_max

    # min
    def min(self):
        if self.n == 0:
            raise ValueError ("min() called on an empty list")

        curr_min = self.A[0]

        for i in range(1,self.n):
            if curr_min > self.A[i]:
                curr_min = self.A[i]

        return curr_min

    # sum
    def sum(self):
        curr_sum = 0

        if self.n == 0:
            return 0
        
        for i in range(self.n):
            curr_sum = curr_sum + self.A[i]

        return curr_sum

    # Average
    def avg(self):

        if self.n == 0:
            raise ValueError('avg() called on empty list')

        return self.sum()/ self.n
        

    # resize
    def __resize(self,new_capacity):
        #create a new array with new_capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity

        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    # print
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'

    # indexing
    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        
        raise IndexError('Index out of range')
    
    # create array
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()

l = Mylist()

l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(8)
l.append(9)
l.append(0)
l.append(7)

l.insert(2, 6)
print(l)
l.reverse()
# l.sort()
# del l[4]

print(l)
print(type(l))