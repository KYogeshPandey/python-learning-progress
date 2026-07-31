# program find the sum of a three digit number entered by user

num = int (input('Enter a 3 digit number:'))
a = num%10
num = num // 10
b = num%10
num = num//10
c = num%10
result = a+b+c
print(result)