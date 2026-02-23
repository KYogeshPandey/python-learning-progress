letter='Hey my name is {} and I am from {}'
country ='India'
name ='harry'

print(letter.format(name,country))

print(f"hey my name is {name} and I am from {country}")

txt='for only {price: .2f } dollars!'
print(txt.format(price= 49.09999))
price = 49.09999
print(f'for only {price:.2f} dollars!')

print(f'we can use f-strings like this : hey my name is {{ name }} and i am from {{country}}')      # to print the curly braces we have to use double curly braces in f-strings


# Docstring  ( used  just below the function name or just above the function body )

def square (n):
    '''takes in a number n and returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)            # to print the docstring of the function square