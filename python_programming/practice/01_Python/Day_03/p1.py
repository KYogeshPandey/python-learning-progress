#menu driven calculator

fnum = int(input("enter the first number :"))
snum = int(input("enter the second number :"))

op = input('enter the operation :')

if op == '+':
    print(fnum + snum)
elif op == '-':
    print(fnum - snum)
elif op == '*':
    print(fnum*snum)
elif op == '/':
    print(fnum/snum)
else:
    print('this operation is not under work')
