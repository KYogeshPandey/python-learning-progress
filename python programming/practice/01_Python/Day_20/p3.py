# raise Exception

# raise IndexError('this is an index error')

class MyException(Exception):
    def __init__(self,message):
        print(message)
class Bank:

    def __init__(self,balance):
        self.balance = balance

    def withdraw(self,amount):
        if amount < 0:
            raise MyException('amount cannot be negative')
        if self.balance < amount:
            raise MyException('insufficient balance')
        self.balance = self.balance - amount
    
obj = Bank(10000)
try:
    obj.withdraw(-5000)
except MyException as e:
    pass
else:
    print(obj.balance)
