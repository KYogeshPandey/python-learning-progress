#min of 3 numbers

a = int(input('Enter the first number :'))
b = int(input('Enter the second number :'))
c = int(input('Enter the third number :'))

if a<b and a<c :
    print('smallest is , a')
elif b<c :
    print('smallest is , b')
else :
    print('smallest is , c')