# Super Keyword

class Phone:
    def __init__(self, price, brand, camera):
        print("inside the constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying a phone')

class Smartphone(Phone):
    def buy(self):
        print("buying a smartphone")
        # syntax to call parent ka buy method
        super().buy()


s = Smartphone(20000,"Samsung", 50)

s.buy()



