# File Handling

# case -1 (if the file is not present )
f = open("file1.txt", "w")
f.write("Hello World!")
f.close()
# f.write() # this will give an error because the file is closed


#Write Multiline strings

f = open("sample.txt", "w")
f.write("hello World!")
f.write("\nHow are You?")
f.close()


# Case - 2 #if the file already exists
f = open("sample.txt", "w")
f.write("this is a new line ")
f.close()

# using Append mode
f = open("C:\\Users\\HP\\Desktop\\python progamming\\file1.txt", "a")
f.write(" \nThis is append mode")
f.close()


# write Lines

l = ["hello\n","how are you?\n", "Hi\n", "I am fine"]

f = open("C:\\Users\\HP\\Desktop\\python progamming\\file1.txt", "w")
f.writelines(l)
f.close()