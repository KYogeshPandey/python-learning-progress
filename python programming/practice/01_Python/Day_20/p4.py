class SecurityError(Exception):

    def __init__(self,message):
        print(message)
    
    def logout(self):
        print('logout')

class Google:

    def __init__(self,name,email,password,device):
        self.name = name
        self.email = email
        self.password= password
        self.device= device
    
    def login(self,email,device,password):
        if device != self.device:
            raise SecurityError('your id is logging somewhere else')
        if email == self.email and password == self.password:
            print('Welcome')
        else:
            print('login error')

obj = Google('nitish','nitish@gmail.com','1234','android')

try:
    obj.login('nitish','nitish@gmail.com','1234','windows')
except SecurityError as e:
    e.logout()
else:
    print(obj.name)
finally:
    print('database connection closed')
