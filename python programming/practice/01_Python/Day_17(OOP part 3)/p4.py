class Phone:
    def __init__(self, price, Brand, camera):
        self.price = price 
        self.brand = Brand
        self.camera = camera

    def buy(self):
        print('Buying the phone')


class Smartphone(Phone):
    def __init__(self, OS, Ram):
        self.OS = OS
        self.Ram = Ram
        print('Inside the smartphone constructor')

s = Smartphone("Android", 2)
s.buy()

# Child can't access private members of the class 