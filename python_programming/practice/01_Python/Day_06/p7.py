#write a program which can remove a particular charachter from a string

s = input('enter the string :')
char = input('enter the charachter you want to remove:')

# new_string = s.replace(char,'')
# print(new_string)

result = ''

for i in s :
    if i != char :
        result = result +i

print(result)