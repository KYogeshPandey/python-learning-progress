# common functions

print(len('hello world!'))
print(max('hello world!'))
print(min('hello world!'))
print(sorted('hello world!'))
print(sorted('hello world!', reverse = True))

s = "heLlo world"
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())


a = "my name is yogesh pandey"
print(a.count('i'))
print(a.find('i'))
print(a.find('x'))
print(a.endswith('pandey'))
print(a.startswith('my'))

name = 'yogesh'
gender = 'male'

print('Hi my name is {} and i am a {}'.format(name,gender))