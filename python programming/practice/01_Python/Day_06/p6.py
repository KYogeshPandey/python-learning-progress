#calcultae the frequency of a particular charachter in a given string

s = input('Enter your string :')
char = input('Enter the charchter you want to find the frequency of :')
print(s.count(char))


s = input('Enter your string :')
char = input('Enter the charchter you want to find the frequency of :')
count = 0
for i in s :
    if i == char :
        count = count +1
print('frequency' , count)