email = input('enter the email')
password = input('enter the password')

if email == 'yogesh.campusx.gmail.com' and password == '1234':
    print('welcome')
elif email=='yogesh.campusx.gmail.com' and password != '1234': 
    print('Incorrect Password')  
    password = input('Enter password again')
    if password == '1234':
        print('Welcome finally!')
    else :
        print('kuch toh gdbd hai dya')
else:
    print('incorrect')    