name = 'abhishek'
for i in name :
    print(i,end ="")
    if (i=="b"):
        print("this is special")


# iteration

colors =["red","green","blue","yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

#range

for k  in range (5):
    print(k+1)

for k in range(1,20001):
    print(k)
    
for k in range(1,12,3):
    print(k)

# while loop

i=0
while(i<3):
    print(i)
    i+=1

while(i<=20):
    i=int(input("enter the number:"))
    print(i)


#count

count=5
while(count>0):
    print(count)
    count=count-1
else:
    print("i am inside else block")



#do while loop 

# execute at least one time 

#infinite loop

i=50
while True:
    print(i)
    if(i%100==0):
        break


#for loop with else            #it defines ki loop khtm hua hai successfully voh khin break nhi hua 

for i in range(5):
    print(i)

else:
    print('sorry, no I')


for i in range(6):
    print(i)
    if i==4:
        break

else:
    print('sorry, no I')   # not executed


i=0
while i<7:
    print(i)
    i=i+1
    if i==4:
        break

else:
    print('sorry,no I')



for x in range(5):
    print("iteration no {} info loop".format(x+1))

else:
    print("else block in loop")
print("out of loop")


