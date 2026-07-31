# super -> constructor

# cant use outside the class
# you cant to accesss the attributes

class Phone:
    def __init__(self, price, brand, camera):
        print('Inside the constructor')
        self.__price = price
        self.brand = brand
        self.camera = camera

class Smartphone(Phone):        
    def __init__(self,price, brand, Os, camera, Ram):
        print("inside the Smartphone constructor")
        super().__init__(price, brand, camera)
        self.Os = Os
        self.Ram = Ram
        print('Inside The Smartphone constructor')

s = Smartphone(20000, "Samsung", 'Android', 50, 8)

print(s.Os)
print(s.brand)