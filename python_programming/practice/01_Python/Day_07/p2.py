#write the program to count the number of words in a given string

s = input('enter the string :')

l = []
temp = ''

for i in s:
    if i != ' ':            # letter mila
        temp = temp + i     # word banao
    else:                   # space mila
        if temp != '':
            l.append(temp)
            temp = ''

# last word add karna zaroori hai
if temp != '':
    l.append(temp)

print(l)