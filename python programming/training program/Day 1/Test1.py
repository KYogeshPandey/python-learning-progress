# Section A â€” Lists, Tuples, Sets & Dictionaries (30 marks)

# Q1. Write a program that takes a list of integers and returns a new list containing only the even numbers.
# Task: Given nums = [12, 7, 18, 3, 24, 9, 30], print the filtered list.
nums = [12, 7, 18, 3, 24, 9, 30]
even_nums = [num for num in nums if num % 2 == 0]
print("Q1 - Even numbers:", even_nums)
print()

# Q2. Given a tuple of city names, write a program to find and print the name with the maximum length,
# without converting the tuple to a list.
# Task: cities = ('Delhi', 'Meerut', 'Bengaluru', 'Pune', 'Hyderabad')
cities = ('Delhi', 'Meerut', 'Bengaluru', 'Pune', 'Hyderabad')
longest_city = max(cities, key=len)
print("Q2 - City with maximum length:", longest_city)
print()

# Q3. Write a program that uses sets to find the common elements and the unique elements (present in only one)
# between two given lists.
# Task: list1 = [1,2,3,4,5,6], list2 = [4,5,6,7,8,9] â€” print intersection, and elements unique to each list.
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
set1 = set(list1)
set2 = set(list2)
intersection = set1 & set2
unique_to_list1 = set1 - set2
unique_to_list2 = set2 - set1
print("Q3 - Common elements:", intersection)
print("Q3 - Unique to list1:", unique_to_list1)
print("Q3 - Unique to list2:", unique_to_list2)
print()

# Q4. Write a program that counts the frequency of each word in a given sentence and stores the result in a dictionary,
# sorted by frequency in descending order.
# Ignore case and punctuation while counting.
import string

sentence = "Python is great, and Python is easy to learn. Easy things become great with practice!"
cleaned_sentence = sentence.lower().translate(str.maketrans('', '', string.punctuation))
words = cleaned_sentence.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
print("Q4 - Word frequency dictionary (sorted):", sorted_word_freq)
print()

# Q5. Given a list of dictionaries representing student records (each with keys 'name' and 'marks'), write a program to
# sort the list by marks in descending order and print the top 3 students with their rank.
# Task: students = [{'name':'Aman','marks':78}, {'name':'Riya','marks':92}, {'name':'Kabir','marks':85},
# {'name':'Zoya','marks':67}, {'name':'Neha','marks':92}]
students = [
    {'name': 'Aman', 'marks': 78},
    {'name': 'Riya', 'marks': 92},
    {'name': 'Kabir', 'marks': 85},
    {'name': 'Zoya', 'marks': 67},
    {'name': 'Neha', 'marks': 92}
]
sorted_students = sorted(students, key=lambda student: student['marks'], reverse=True)
print("Q5 - Top 3 students:")
for rank, student in enumerate(sorted_students[:3], start=1):
    print(f"Rank {rank}: {student['name']} - {student['marks']}")
print()

# Section B â€” Loops & Conditional Statements (16 marks)

# Q6. Write a program to print all prime numbers between 1 and 100 using nested loops and conditional statements.
primes = []
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print("Q6 - Prime numbers between 1 and 100:")
print(primes)
print()

# Q7. Write a program to check whether a given year is a leap year, and print an appropriate message.
# Task: Test with years: 2000, 1900, 2024, 2023.
years = [2000, 1900, 2024, 2023]
print("Q7 - Leap year check:")
for year in years:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
print()

# Q8. Write a program using nested loops to print the following right-angled pyramid pattern for n = 5 rows, and then
# modify it to print an inverted pyramid for the same n.
# Row 1: * Row 2: * * Row 3: * * * ... and so on.
n = 5
print("Q8 - Right-angled pyramid:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
print()
print("Q8 - Inverted pyramid:")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# Section C â€” Functions (18 marks)

# Q9. Write a recursive function factorial(n) that returns the factorial of n.
# Handle the case where n is negative by raising a ValueError.
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Q9 - Factorial of 5:", factorial(5))
print()

# Q10. Write a function stats(*args) that accepts a variable number of numeric arguments and returns a dictionary
# containing their sum, average, and maximum value.
def stats(*args):
    if not args:
        return {"sum": 0, "average": 0, "maximum": None}
    return {
        "sum": sum(args),
        "average": sum(args) / len(args),
        "maximum": max(args)
    }

print("Q10 - Stats:", stats(10, 20, 30, 40, 50))
print()

# Q11. Write a function area(length, width=None, shape='rectangle') that calculates the area of a rectangle or a square
# using default and keyword arguments. If shape is 'square', only length is required.
# Call the function using positional, default, and keyword-argument styles and print each result.
def area(length, width=None, shape='rectangle'):
    if shape == 'square':
        return length * length
    if width is None:
        raise ValueError("Width is required for a rectangle.")
    return length * width

print("Q11 - Rectangle area (positional):", area(10, 5))
print("Q11 - Square area (keyword):", area(6, shape='square'))
print("Q11 - Rectangle area (keyword arguments):", area(length=8, width=4, shape='rectangle'))
print()

# Section D â€” Classes, Objects, Constructors & Inheritance (28 marks)

# Q12. Create a class Student with attributes name and marks, initialized through a constructor (__init__), and a method
# display() that prints the student's details. Create two Student objects and call display() on each.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

print("Q12 - Student details:")
student1 = Student("Garv", 91)
student2 = Student("Ananya", 88)
student1.display()
student2.display()
print()

# Q13. Create a base class Vehicle with attributes brand and speed, and a constructor to initialize them. Create a
# derived class Car that inherits from Vehicle, adds an attribute fuel_type, and uses super() to initialize the inherited
# attributes. Create a Car object and display all its details.
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def display_details(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h, Fuel Type: {self.fuel_type}")

print("Q13 - Car details:")
car = Car("Toyota", 180, "Petrol")
car.display_details()
print()

# Q14. Implement multiple inheritance: create a class Person (attributes: name, age) and a class Employee
# (attributes: emp_id, salary), then create a class Manager that inherits from both Person and Employee. Write a
# constructor in Manager that initializes all attributes, and print the Method Resolution Order (MRO) of the Manager
# class using Manager.__mro__.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.emp_id}, Salary: {self.salary}")

print("Q14 - Manager details:")
manager = Manager("Rahul", 35, "M101", 85000)
manager.display()
print("MRO of Manager class:", Manager.__mro__)
print()

# Section E â€” Decorators (14 marks)

# Q15. Write a decorator named timer that measures and prints the time taken by any function it decorates to execute.
# Apply it to a function that computes the sum of the first n natural numbers using a loop.
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@timer
def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("Q15 - Sum of first 100 natural numbers:", sum_natural_numbers(100))
print()

# Q16. Write a decorator named authenticate that checks a global boolean variable is_logged_in before allowing a
# function to run. If is_logged_in is False, the decorator should prevent the function from executing and print
# 'Access Denied'; otherwise it should run the function normally. Demonstrate the decorator on a function
# view_profile().
is_logged_in = False

def authenticate(func):
    def wrapper(*args, **kwargs):
        if not is_logged_in:
            print("Access Denied")
            return
        return func(*args, **kwargs)
    return wrapper

@authenticate
def view_profile():
    print("Welcome to your profile!")

print("Q16 - Authentication demo when user is not logged in:")
view_profile()

is_logged_in = True
print("Q16 - Authentication demo when user is logged in:")
view_profile()
print()

# Section F â€” Shallow Copy & Deep Copy (14 marks)

# Q17. Write a program to demonstrate the difference between shallow copy and deep copy using a nested list. Show,
# with print statements, that modifying a nested element through the shallow copy also changes the original list, while
# modifying it through the deep copy does not.
# Task: original = [1, 2, [3, 4]] â€” use copy.copy() for shallow copy and copy.deepcopy() for deep copy.
import copy

original = [1, 2, [3, 4]]
shallow_copied = copy.copy(original)
deep_copied = copy.deepcopy(original)

shallow_copied[2][0] = 99
print("Q17 - After modifying shallow copy:")
print("Original list:", original)
print("Shallow copy:", shallow_copied)
print("Deep copy:", deep_copied)
print()

deep_copied[2][1] = 100
print("Q17 - After modifying deep copy:")
print("Original list:", original)
print("Shallow copy:", shallow_copied)
print("Deep copy:", deep_copied)
print()

# Q18. Create a class Employee with an attribute skills (a list). Create an Employee object, then create one copy of it
# using copy.copy() and another using copy.deepcopy(). Modify the skills list through the original object and show,
# with printed output, how each copy is affected differently.
class EmployeeRecord:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def display(self):
        print(f"Name: {self.name}, Skills: {self.skills}")

employee_original = EmployeeRecord("Arjun", ["Python", "SQL"])
employee_shallow = copy.copy(employee_original)
employee_deep = copy.deepcopy(employee_original)

employee_original.skills.append("Machine Learning")

print("Q18 - Employee object copy demonstration:")
print("Original object:")
employee_original.display()
print("Shallow copy object:")
employee_shallow.display()
print("Deep copy object:")
employee_deep.display()