# Guessing game

#generate a random integer between 1 and 100

import random
jackpot = random.randint(1,100)

guess = int(input('guess the number :'))
counter = 1

while guess != jackpot:
        
    if guess < jackpot:
        print('galat! guess higher')
    else:
        print('galat! guess lower')

    guess = int(input('guess again :'))
    counter += 1

else:
    print("correct guess")
    print(f"attempts : {counter}")
