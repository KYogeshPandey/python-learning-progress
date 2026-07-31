import time
timestamp=time.strftime("%H")

hour=int(input("enter the hour"))

if(hour>=0 and hour<12):
    print("good morning")
elif(hour>=12 and hour<18):
    print("good afternoon")
if(hour>18 and hour<=20):
    print("good evening")
else:
    print("good night")