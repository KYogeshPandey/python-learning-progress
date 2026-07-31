import os
folders=os.listdir("data")

print(os.getcwd())   # to get the current working directory we can use the os.getcwd() method, which returns the path of the current working directory as a string.
os.chdir("/Users")
print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))