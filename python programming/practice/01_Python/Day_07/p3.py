# write a program to convert a string to title case without using title() method

s = input('enter the string:')

l = []
for i in s.split():
    l.append(i[0].upper() + i[1:].lower())

print(' '.join(l))

