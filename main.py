import pandas
print("hi")
print("hello world")
print(5)
print("hey i am a good boy \nand i love coding")
# this is a commnet
print("hey",6,7,sep="-",end="009\n" ) 
print("harry")
a=4
b="ram"
c=8.7
d=False
e=7
print(a)
print(b)
print(c)
print(d)
print(a+e)
print("the type of a is",type(a))
print("the type of b is",type(b))
print("the type of c is",type(c))   
print("the type of d is",type(d))
list=[8,"HARRY",9.7,False]
tuple=(8,"HARRY",9.7,False)
dict={"name":"harry","marks":90,"isgood":True}

#typecasting

a="1"
b="2"
print(int(a)+int(b))
print(a+b)

a=1.9
b=8
print(a+b)

#strings

apple='''he said i am a goof coder.
but he don'tknow about strings 
tell him the easy way to learn coding .'''
print(apple)

print(apple[1])
print(apple[0])
print("lets use a loop")
for character in apple:
    print(character)

    #slicing in String

names="harry,shubham"
print(names[0:5])
print(len(names))

fruit="Mango"
Mangolen=len(fruit)
print(Mangolen)
print(fruit[0:4])
print(fruit[1:4])
print(fruit[:5])
print(fruit[0:-3])
print(fruit[-3:-1])
nm="Harry"
print(nm[-4:-2])