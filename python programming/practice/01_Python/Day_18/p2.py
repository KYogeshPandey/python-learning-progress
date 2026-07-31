# Read or Readlines

f = open("C:\\Users\\HP\\Desktop\\python progamming\\file1.txt", 'r')
s = f.read()
print(s)
f.close()

# reading upto n charachters
f = open("C:\\Users\\HP\\Desktop\\python progamming\\file1.txt", 'r')
s = f.read(10)
print(s)
f.close()

# readlines
f = open("C:\\Users\\HP\\Desktop\\python progamming\\file1.txt", 'r')
print(f.readline(), end ="")
print(f.readline(), end ="")
f.close()

# Reading entire using readlines
f = open("C:\\Users\\HP\\Desktop\\python progamming\\file1.txt", 'r')

while True:

    data = f.readline()

    if data == '':
        break
    else:
        print(data, end='')

f.close()
   