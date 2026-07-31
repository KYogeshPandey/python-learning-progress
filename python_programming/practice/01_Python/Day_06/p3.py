print('yogesh1234%'.isalnum())
print('123'.isalnum())
print('yogesh1234'.isalpha())
print('1234'.isdigit())
print('1name'.isidentifier())
print('name1'.isidentifier())
print('first_name'.isidentifier())
print('first-name'.isidentifier())

#Split/Join
s = 'hi my name is Yogesh'
print(s.split())
print(s.split('i'))
print('i'.join(['h', ' my name ', 's Yogesh']))

#Replace/Strip

s = 'hi my name is Yogesh'
print(s.replace('Yogesh', 'pandey'))

b= 'yogesh      '
print(b.strip())