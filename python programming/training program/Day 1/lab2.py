num = int (input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is {result}.")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
a,b = b,a
print(f"After swapping: a = {a}, b = {b}")

km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
print(f"The distance in miles is: {miles}")

p = 200
t = 5
r = 5
si = (p * t * r) / 100
print(f"The simple interest is: {si}")