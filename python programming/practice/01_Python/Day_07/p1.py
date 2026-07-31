#write a program that can check whether a program is palindrome or not

s = input('Enter the string :')
flag = True

for i in range(0,len(s)//2):
    if s[i] != s[len(s) - i - 1]:
        flag = False
        print('Not a palindrome')
        break
    
if flag :
    print('palindrome')

        