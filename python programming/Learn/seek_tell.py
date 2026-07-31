# with open ('file.txt', 'r') as f:
#     print(type(f))

#     f.seek(5)  # Move to the 5th character in the file

#     print(f.tell())
#     data=f.read()
#     print(data) 

with open('file.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(5)

with open('file.txt', 'r') as f:
    print(f.read())