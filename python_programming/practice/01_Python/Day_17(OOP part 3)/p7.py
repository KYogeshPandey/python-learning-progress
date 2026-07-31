# Method Overriding

class Phone:
    def __init__(self, brand, price, camera):
        print("Inside the constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('buy a Phone')

class Smartphone(Phone):
    def buy(self):
        print("Buy a Smartphone")

s = Smartphone(20000, 'Apple', 50)

s.buy()