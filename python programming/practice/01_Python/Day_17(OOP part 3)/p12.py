#Polymorphism

# method overriding
# method Overloading
# operator overloading

# Method Overloadig
class Shape:
    
    def area(self,a,b=0):
        if b == 0:
            return 3.14*a*a
        else:
            return a*b
    
s = Shape()
print(s.area(3,4))
print(s.area(3))

# Operator Overloading

 