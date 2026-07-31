# Types of Inheritance

# Single inheritance
# multilevel Inheritance
# hierarchial Inheritance
"""single parent multiple child"""
# multiple Inheritancce
"""single child multiple parent"""
# Hybrid Inheritance

# multilevel

class Product:
    def review(self):
        print('Product customer Review')


class Phone(Product):
    def __init__(self, price, brand, camera):
        print("inside the phone class")
        print("inside the constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying a phone')

class Smartphone(Phone):
    pass

s = Smartphone(20000,"Samsung", 50)

s.buy()

# Hierarchial

class Phone():
    def __init__(self, price, brand, camera):
        print("inside the phone class")
        print("inside the constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying a phone')


class Smartphone(Phone):
    pass

class FeaturePhone(Phone):
    pass

Smartphone(20000,"Samsung", 50).buy()

FeaturePhone(210,"Lava", 50).buy()

# Multilevel

class Phone():
    def __init__(self, price, brand, camera):
        print("inside the phone class")
        print("inside the constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying a phone')

class Product:
    def review(self):
        print('Product customer Review')

class SmartPhone(Phone, Product):
    pass

Smartphone(20000,"Samsung", 50)

s.buy()
s.review()


# question(Method resolution Order)

class Phone():
    def __init__(self, price, brand, camera):
        print("inside the phone class")
        print("inside the constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying a phone')

class Product:
    def buy(self):
        print('Product customer Review')

class SmartPhone(Phone, Product):
    pass

s = SmartPhone(20000,"Samsung", 50)

s.buy( )


