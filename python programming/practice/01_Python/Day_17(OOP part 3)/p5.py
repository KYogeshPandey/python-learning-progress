# Child can't access private members of the class 

class Phone:
    def __init__(self, price, Brand, camera):
        self.__price = price 
        self.brand = Brand
        self.camera = camera
    
    #getter
    def __show(self):
        print(self.__price)


class Smartphone(Phone):
    def check (self):
        print(self.__price)

s = Smartphone(20000, "apple", 13)  
print(s.brand)
# s.check()
s.__show()