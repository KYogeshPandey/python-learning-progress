class Parent:

    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num
    
class Child(Parent):

    def show(self):
        print('this is a child class')

son = Child(100)
print(son.get_num())
son.show()