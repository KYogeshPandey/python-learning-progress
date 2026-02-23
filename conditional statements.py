#If-Else 

a=int(input("Enter your age:"))
print("your age is :",a)

if(a>=18):
    print("you can drive")
else:
    print("you cannot drive")

#Elif

num=int(input("enter the valuee of num:"))
if(num<0):
    print("number is negative")
elif(num==0):
    print("number is zero")
else:
    print("number is positive")
    if(num==999):
       print("number is special")


#nested if-else

num=int(input("enter the number"))
if(num<0):
    print("number is negative")
elif(num>0):
    print("number is positive")
    if(num%2==0):
        print("number is even")
    else:
        print("number is odd")
elif(num==0):
    print("number is zero")

