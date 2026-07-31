def fun1():
    try:
        l=[1,3,5,7,9]
        i=int(input("enter the number:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    
    finally:
        print("i am always executed")

print(fun1())
        
