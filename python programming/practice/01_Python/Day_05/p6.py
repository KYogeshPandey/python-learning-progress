#positive indexing

a = 'Hello World!'
print(a[6])

#negative indexing

a = 'Hello World!'
print(a[-4])

#slicing

a = 'Hello World'
print(a[0:5:2])
print(a[6:0:-1])
print(a[::-1])
print(a[-1:-6:-1])
del a[-1:-5:2]
print(a)
