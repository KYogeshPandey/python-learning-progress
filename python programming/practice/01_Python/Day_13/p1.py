# Creating a function

def is_even(num):
    """
    This function returns if a given number is odd or even .
    input - any valid integer
    output - odd/even
    """
    if type(num) == int:
        if num % 2 == 0:
            return 'even'
        else:
            return 'odd'
    else:
        return "pagal hai kya "

for i in range(1,11):
    x = is_even(i)
    print(i,x)