# Dictionary Comprehension

print({i:i**2 for i in range (1,11)})

# Using existance dictionary

distance = {"delhi":1000 , "mumbai": 2000, "rajasthan":3000}

print({key:value*0.62 for (key,value) in distance.items()})

# using zip
days = {"Sunday","Monday","tuesday","wednesssay","thrusday","friday","saturday"}
temp_C = {30.2,25,27,33.4,28.9,44,33}

print({i:j for (i,j) in zip(days,temp_C)})


# Using if condition

products = {'phone':4 , 'laptop': 0 , 'tablet': 0 , 'charger': 32}

print({key:value for (key,value) in products.items() if value <= 0})

# Nested comprehension

# print tables of number from 2 to 4

print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})