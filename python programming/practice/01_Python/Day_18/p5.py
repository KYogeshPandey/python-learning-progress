# problem with working in text mode 

# can't work with binary files like text or images
# not good for other data tyupes like int/float/list/tuple

# workin with binary files or images

with open(r"C:\Users\HP\Desktop\python progamming\practice\Day_18\s1.png",'rb') as f:
    with open('s1_copy.png', 'wb') as f1:
        f1.write(f.read())

d = {
    'name' : 'nitish',
    'age' : 33,
    'gender' : 'male'
}

with open ('sample.txt','w') as f :
    f.write(str(d))