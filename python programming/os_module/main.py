import os

if(not os.path.exists("data")):   # to check if a directory exists or not we can use the os.path.exists() method, which takes the name of the directory as an argument and returns True if the directory exists and False if it does not exist.
    os.mkdir("data")

for i in range (0,100):
    os.mkdir(f"data/Day{i+1}")