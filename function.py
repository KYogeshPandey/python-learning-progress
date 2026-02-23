# def calculategmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)

# calculategmean(2,2)


# def isgreater(a,b):
#     if(a>b):
#         print("first number is greater")
#     else:
#         print("second number is greater")


# isgreater(5,8)     #calling a function


#function arguments in python

# def average(a,b):
#     print("the average is :", (a+b)/2)

# average(4,8)


# def name(fname,mname='john',lname='whatson'):
#     print("hello",fname,mname,lname)

# name("Any","me","you")



#Variable length argument

#args

# def average(*numbers):
#     print(type(numbers))
#     total = 0
#     for num in numbers:
#         total += num
#     return total / len(numbers)

# c = average(5, 6, 7, 1)
# print("Average is:", c)


#Kwargs


def greet(**name):
    print(type(name))
    print("hello",name["fname"],name["mname"],name["lname"])

greet(mname="buchhan",lname="watson",fname="amitabh")




 