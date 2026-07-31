# a = [1,2,3,4,"Hello"]
# a.insert(2, "World")
# print(a)

# a = "rahul"
# b= list(a)
# print(b)

# my_list = ['r','a', 'h', 'u', 'l']
# result = "".join(map(str, my_list))
# print(result)

# my_list = [1,3,2,2,5,6,5,8,9,9]
# print(list(set(my_list)))

# my_dict = {

#     "name" : "Rahul",
#     "roll_no" : 123,
#     "college" : "ABC",

# }

# print(my_dict.get("name"))

my_list = [1,2,3,4,5,6,7,7,7,55,67,66,88,98,78]
new_list = []
for i in my_list:
    if i%2 == 0:
        new_list.append(i)
print(new_list)


new_list = [i for i in my_list if i % 2 == 0]
print(new_list)

new_list = list(filter(lambda x: x%2 == 0, my_list))
print(new_list)