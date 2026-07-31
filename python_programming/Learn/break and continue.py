#break

for i in range(12):
    if(i==10):
        break
    print("5 X", i+1 , "=" , 5*(i+1))


#Continue

for i  in range(1,12):
    if (i==10):
        print('skip the iteration')
        continue
    print("6 X", i+1 , "=" , 6*(i+1))