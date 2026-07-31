# Using Context Manager (With)

with open("C:\\Users\\HP\\Desktop\\python progamming\\sample.txt","w")as f :
    f.write('with technique')


# read with with

with open("C:\\Users\\HP\\Desktop\\python progamming\\sample.txt","r")as f :
    s = f.read()
    print(s)

# moving with a file -> 10 char then next 10 char
with open("C:\\Users\\HP\\Desktop\\python progamming\\sample.txt","r")as f :
    print(f.read(10))
    print(f.read(10))

# benefit to load a big file in the memory
Big_l = ["hello world" for i in range(100000)]

with open('big.txt',"w") as f:
    f.writelines(Big_l)
    

with open('big.txt','r') as f:

    chunk_size = 10

    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size), end = "***")
        f.read(chunk_size)