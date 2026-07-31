# extract username from a given email id

email = input('Enter your email:')
username = email.split('@')[0]
print('your username is :', username)