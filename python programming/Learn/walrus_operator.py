a= True
print(a:=False)

n = [1,2,3,4,5]

while (i := (len(n))):
    print(n.pop())



# foods = list()
# while True:
#     food = input("What food do you like ?:")
#     if food == "quit":
#         break
#     foods.append(food)

# print(f"the list of foods you like is:{foods}")

#using walrus operator

foods = list()
while(food:= input("what food do you like ?:")) != "quit":
    foods.append(food)

print(f"the list of foods you like is:{foods}")