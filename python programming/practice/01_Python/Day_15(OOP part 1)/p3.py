    # MAGIC METHODS (DUNDER METHODS)

# these are special methods in python that have double underscores before and after their names. 
# They are used to define the behavior of objects in certain situations, such as when they are printed, added together, or compared.

# class ke andr jo kuch bhi hai use sirf us class ke objects hi access kr skte hai.  (self)

class Fraction():

    # parameterized constructor
    def __init__(self,x,y):
        self.num = x
        self.den = y

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)
    
    def __add__(self,other):
        new_num = self.num*other.den + self.den*other.num
        new_den = self.den*other.den

        return '{}/{}'.format(new_num, new_den)
    
    def __sub__(self, other):
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den*other.den

        return '{}/{}'.format(new_num,new_den)
    
    def __mul__(self, other):
        new_num = self.num*other.num
        new_den = self.den*other.den

        return '{}/{}'.format(new_num,new_den)
    
    def __truediv__(self, other):
        new_num = self.num*other.den
        new_den = self.den*other.num

        return '{}/{}'.format(new_num,new_den)
    
    def convert_to_decimal(self):
        return self.num/self.den

fr1 = Fraction(1,2)
fr2 = Fraction(3,4)
print(fr1.convert_to_decimal())


print(fr1 +fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)