a= int(input('enter the number :'))
print(f'multiplication table of {a} is :')

try:
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")
except:
    print('Invalid input')

print('some important lines of code ')
print('end of program')


try:
    num=int(input('enter the number:'))
    a=[6,3]
    print(a[num])

except ValueError:
    print('number entered is not an integer')

except IndexError:
    print('Index error')


#finally keyword


try:
    l=[1,3,5,7,9]
    a=int(input('enter the index value :'))
    print(l[a])

except:
    print("some error occcured")
finally:
    print("I am always executed")


#custom errors

a=int(input("enter any value between 5 and 9: "))

if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")