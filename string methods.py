#strings are immutable
a="Harry"
print(len(a))          #len
print(a.upper())       #upper
print(a.lower())       #lower
b="harry!!!"
print(b.rstrip(" ! "))   #stripping @@
print(a.replace("Harry","john")) #replace
c="!!!Harry!!! "
print(c.split(" ! "))    #split @@
blogheading="introduvtion to js"
print(blogheading.capitalize()) #capitalize
d="Welcome to the console!!!"
print(len(d))
print(d.center(50))  #center
print(len(d.center(50))) #center
print(d.count("e"))      #count
print(d.endswith("!!!"))
print(d.endswith("to",4,10)) #endswith
e="this is a simple string 3"
print(e.find("is"))        #find
print(e.index("is"))       #index 
print(e.isalnum())        #isalnum @@
print(e.isalpha())       #isalpha @@
print(e.islower())      #islower 
f="      "
print(f.isspace())     #isspace 
print(e.isprintable())  #isprintable
g="This Is A Simple String"
print(g.istitle())      #istitle
print(g.startswith("This"))  #startswith
print(g.startswith("Is",5,7))  #startswith
h="hello"
print(h.swapcase())     #swapcase
print(h.title())        #title
i="hello world"
print(i.zfill(20))      #zfill
print(len(i.zfill(20)))  #zfill
print(i.encode())       #encode
print(type(i.encode()))  #encode

