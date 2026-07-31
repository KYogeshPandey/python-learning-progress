#nested loops

for i in range(1,5):
    for j in range(1,5):
        print(i,j)

#patterns

rows = int(input('enter the number of rows '))
for i in range(1, rows+1):
    for j in range(1,i+1):
        print('*',end ='' )
    print()