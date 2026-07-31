# Banking application

class ATM :

    __counter = 0

    # Constructor(special->function) -> super power
    def __init__(self):
        self.pin = ''
        self.__balance = 0
        self.cid = ATM.__counter
        ATM.__counter = ATM.__counter + 1          
        # self.menu()

    # Utility methods 
    @staticmethod             # to create utility methods
    def get_count():
        return ATM.__counter

    def get_balance(self):
        return self.__balance

    def set_balance(self,new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print('not possible')

    def menu (self):
        user_input = input("""
        Hi how can I help you ?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw 
        5. Anything else to exit 
        """)

        if user_input == '1' :
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.Withdraw()
        else :
            exit()

    def create_pin(self):
        user_pin = input ('enter your pin :')
        self.pin = user_pin

        user_balance = int(input('enter the balance'))
        self.__balance = user_balance 

        print('pin created successfully')
        self.menu()

    def change_pin(self):
        old_pin = input('enter your pin :')
         
        if old_pin == self.pin :
            # let him change the pin
            new_pin = input('enter new pin :')
            self.pin = new_pin
            print('pin changed successfully')

        else:
            print('not possible')
            self.menu()

    def check_balance(self):
        user_pin = input('enter the pin :')
        if user_pin == self.pin :
            print('your balance is : ', self.__balance)
        else:
            print('wrong pin')
        self.menu()

    def Withdraw(self):
        user_pin = input('enter the pin :')
        if user_pin == self.pin:
            amount = int(input('enter the amount to withdraw :'))
            if amount <= self.__balance:
                self.__balance = self.__balance-amount
                print('withdrawl successfully remaining balance is :', self.__balance)
            else:
                print('insufficient balance')
        else:
            print('wrong pin')
        self.menu() 

obj = ATM()
obj.get_balance()
obj.set_balance(100000)

c1 = ATM()
c2 = ATM()
c3 = ATM()

print(ATM.get_count())

print(c1.cid)
print(c2.cid)
print(c3.cid)
# print(type(obj))
