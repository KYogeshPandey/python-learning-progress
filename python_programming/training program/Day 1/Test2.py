# Section A — Lists, Tuples, Sets & Dictionaries (26 marks)

# Q1. Write a program that groups a list of employee dictionaries by department into a dictionary of lists, then
# computes the average salary per department. [Intermediate | 8 marks]
# Task: employees = [{'name':'A','dept':'IT','salary':50000}, {'name':'B','dept':'HR','salary':40000},
# {'name':'C','dept':'IT','salary':60000}, {'name':'D','dept':'Sales','salary':45000}]
employees = [
    {'name': 'A', 'dept': 'IT', 'salary': 50000},
    {'name': 'B', 'dept': 'HR', 'salary': 40000},
    {'name': 'C', 'dept': 'IT', 'salary': 60000},
    {'name': 'D', 'dept': 'Sales', 'salary': 45000}
]

grouped_by_department = {}
for emp in employees:
    dept = emp['dept']
    if dept not in grouped_by_department:
        grouped_by_department[dept] = []
    grouped_by_department[dept].append(emp)

average_salary_by_department = {}
for dept, emp_list in grouped_by_department.items():
    total_salary = 0
    for emp in emp_list:
        total_salary += emp['salary']
    average_salary_by_department[dept] = total_salary / len(emp_list)

print("Q1 - Grouped employees by department:")
print(grouped_by_department)
print("Q1 - Average salary by department:")
print(average_salary_by_department)
print()


# Q2. Write a program to merge two dictionaries such that if a key exists in both, the values (assumed numeric) are
# summed; otherwise, the key-value pair is carried over as-is. Do this without using the | merge operator (i.e., build it
# manually). [Intermediate | 8 marks]
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 40}

merged = {}

for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    if key in merged:
        merged[key] += dict2[key]
    else:
        merged[key] = dict2[key]

print("Q2 - Merged dictionary:")
print(merged)
print()


# Q3. Given a list of tuples representing (student_name, subject, marks), write a program that uses sets and dictionaries
# together to: (a) find all unique subjects, (b) build a nested dictionary of {student: {subject: marks}}, and (c) find the
# student with the highest total marks across all subjects. [Advanced | 10 marks]
# Do not hardcode student or subject names — the solution must work for any input list of this shape.
records = [
    ("Aman", "Math", 88),
    ("Aman", "Science", 91),
    ("Riya", "Math", 95),
    ("Riya", "Science", 89),
    ("Kabir", "Math", 84),
    ("Kabir", "Science", 90),
    ("Kabir", "English", 87)
]

unique_subjects = set()
student_marks = {}
student_totals = {}

for student, subject, marks in records:
    unique_subjects.add(subject)

    if student not in student_marks:
        student_marks[student] = {}
    student_marks[student][subject] = marks

    if student not in student_totals:
        student_totals[student] = 0
    student_totals[student] += marks

top_student = None
highest_total = None

for student, total in student_totals.items():
    if highest_total is None or total > highest_total:
        highest_total = total
        top_student = student

print("Q3 - Unique subjects:")
print(unique_subjects)
print("Q3 - Nested dictionary:")
print(student_marks)
print("Q3 - Student with highest total marks:")
print(top_student, highest_total)
print()


# Section B — Loops & Conditional Logic (14 marks)

# Q4. Write a program that takes a list of integers and, using loops and conditionals only (no sorting functions), finds
# the second largest and second smallest values in a single pass. [Intermediate | 6 marks]
numbers = [12, 5, 8, 19, 1, 7, 19, 3, 1]

smallest = float('inf')
second_smallest = float('inf')
largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif smallest < num < second_smallest:
        second_smallest = num

    if num > largest:
        second_largest = largest
        largest = num
    elif second_largest < num < largest:
        second_largest = num

print("Q4 - Numbers:", numbers)

if second_smallest == float('inf'):
    print("Q4 - Second smallest does not exist.")
else:
    print("Q4 - Second smallest:", second_smallest)

if second_largest == float('-inf'):
    print("Q4 - Second largest does not exist.")
else:
    print("Q4 - Second largest:", second_largest)
print()


# Q5. Write a program to validate a password string using nested loops/conditionals: it must be at least 8 characters,
# contain at least one uppercase letter, one lowercase letter, one digit, and one special character. Print exactly which
# rule(s) failed if invalid. [Advanced | 8 marks]
password = "Pass123"

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~\\"

for ch in password:
    if 'A' <= ch <= 'Z':
        has_upper = True
    elif 'a' <= ch <= 'z':
        has_lower = True
    elif '0' <= ch <= '9':
        has_digit = True
    else:
        for sp in special_characters:
            if ch == sp:
                has_special = True
                break

failed_rules = []

if len(password) < 8:
    failed_rules.append("At least 8 characters required.")
if not has_upper:
    failed_rules.append("At least one uppercase letter required.")
if not has_lower:
    failed_rules.append("At least one lowercase letter required.")
if not has_digit:
    failed_rules.append("At least one digit required.")
if not has_special:
    failed_rules.append("At least one special character required.")

print("Q5 - Password:", password)
if not failed_rules:
    print("Q5 - Password is valid.")
else:
    print("Q5 - Password is invalid. Failed rules:")
    for rule in failed_rules:
        print("-", rule)
print()


# Section C — Functions (24 marks)

# Q6. Write a higher-order function apply_operations(numbers, *funcs) that applies each function in funcs to every
# number in the list in sequence and returns the final transformed list. Demonstrate it with functions for squaring and
# adding 10. [Intermediate | 8 marks]
def square(x):
    return x * x

def add_ten(x):
    return x + 10

def apply_operations(numbers, *funcs):
    result = []
    for num in numbers:
        value = num
        for func in funcs:
            value = func(value)
        result.append(value)
    return result

nums = [1, 2, 3, 4]
final_result = apply_operations(nums, square, add_ten)

print("Q6 - Original numbers:", nums)
print("Q6 - After applying square and add_ten:", final_result)
print()


# Q7. Write a function memoize(func) (not using functools.lru_cache) that caches results of any function it wraps, using
# a dictionary keyed on the arguments. Apply it to a slow recursive Fibonacci function and show the performance
# difference using the time module. [Intermediate | 8 marks]
import time

def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    wrapper.cache = cache
    return wrapper

def slow_fibonacci(n):
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

@memoize
def fast_fibonacci(n):
    if n <= 1:
        return n
    return fast_fibonacci(n - 1) + fast_fibonacci(n - 2)

n = 30

start = time.time()
slow_result = slow_fibonacci(n)
slow_time = time.time() - start

start = time.time()
fast_result = fast_fibonacci(n)
fast_time = time.time() - start

print("Q7 - Slow fibonacci result:", slow_result)
print("Q7 - Slow fibonacci time:", slow_time)
print("Q7 - Memoized fibonacci result:", fast_result)
print("Q7 - Memoized fibonacci time:", fast_time)
print()


# Q8. Write a function chunk_list(data, size) that splits a list into sublists of a given size (last chunk may be smaller),
# implemented as a generator function using yield. Consume it in a loop and print each chunk. [Advanced | 8 marks]
def chunk_list(data, size):
    for i in range(0, len(data), size):
        yield data[i:i + size]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 4

print("Q8 - Chunks:")
for chunk in chunk_list(data, chunk_size):
    print(chunk)
print()


# Section D — Classes, Objects, Constructors & Inheritance (32 marks)

# Q9. Create a class BankAccount with a constructor that sets balance (default 0) and a private attribute __pin. Add
# methods deposit(), withdraw() (which checks sufficient balance), and check_balance(pin) which only reveals the
# balance if the pin matches. Demonstrate encapsulation by attempting direct access to __pin from outside the class.
# [Intermediate | 8 marks]
class BankAccount:
    def __init__(self, pin, balance=0):
        self.balance = balance
        self.__pin = pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self, pin):
        if pin == self.__pin:
            print(f"Balance: {self.balance}")
        else:
            print("Invalid PIN.")

account = BankAccount("1234", 1000)
account.deposit(500)
account.withdraw(300)
account.check_balance("1234")
account.check_balance("0000")

print("Q9 - Attempting direct access to __pin:")
try:
    print(account.__pin)
except AttributeError as e:
    print("Direct access failed:", e)
print()


# Q10. Design a class hierarchy: an abstract base class Shape (use the abc module) with an abstract method area(), and
# two subclasses Rectangle and Circle that implement it. Write a function total_area(shapes) that accepts a list of mixed
# Shape objects and returns the sum of their areas, without knowing their concrete types. [Advanced | 10 marks]
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

shapes = [Rectangle(10, 5), Circle(7), Rectangle(4, 6)]
print("Q10 - Total area:", total_area(shapes))
print()


# Q11. Model a diamond inheritance scenario: class A has a method greet() that prints 'Hello from A'. Classes B and C
# both inherit from A and override greet() to add their own message before calling super().greet(). Class D inherits from
# both B and C. Create a D object, call greet(), and explain (as a comment) the order of execution based on Python's
# MRO — print D.__mro__ to verify. [Advanced | 14 marks]
# Order of execution:
# D has no greet(), so Python looks at D's MRO.
# For class D(B, C), the MRO is D -> B -> C -> A -> object.
# Therefore, d.greet() starts from B.greet(), then B calls super().greet() which goes to C.greet(),
# then C calls super().greet() which goes to A.greet().

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()

class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()

class D(B, C):
    pass

d = D()
print("Q11 - Greeting from D object:")
d.greet()
print("Q11 - MRO of D:")
print(D.__mro__)
print()


# Section E — Decorators (18 marks)

# Q12. Write a decorator retry(n) that takes an argument n and retries the decorated function up to n times if it raises an
# exception, printing the attempt number each time, before finally re-raising the exception if all attempts fail.
# [Intermediate | 8 marks]
def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, n + 1):
                try:
                    print(f"Attempt {attempt}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Failed on attempt {attempt}: {e}")
                    last_exception = e
            raise last_exception
        return wrapper
    return decorator

counter = {"tries": 0}

@retry(3)
def unstable_task():
    counter["tries"] += 1
    if counter["tries"] < 3:
        raise ValueError("Temporary failure")
    return "Task succeeded"

print("Q12 - Retry decorator demo:")
print(unstable_task())
print()


# Q13. Write a class-based decorator CallCounter that tracks how many times a decorated function has been called
# (stored as an attribute on the wrapper), and write a second decorator validate_types(*types) that checks the types of
# positional arguments passed to a function before allowing it to run, raising a TypeError with a clear message
# otherwise. Stack both decorators on a single function and demonstrate the behavior. [Advanced | 10 marks]
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

def validate_types(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(len(types)):
                if i >= len(args):
                    break
                if not isinstance(args[i], types[i]):
                    raise TypeError(
                        f"Argument {i + 1} must be of type {types[i].__name__}, "
                        f"got {type(args[i]).__name__} instead."
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@CallCounter
@validate_types(int, int)
def add(a, b):
    return a + b

print("Q13 - Valid call result:", add(10, 20))
print("Q13 - Call count after valid call:", add.count)

try:
    print(add(10, "30"))
except TypeError as e:
    print("Q13 - Type error:", e)

print("Q13 - Call count after invalid call:", add.count)
print()


# Section F — Shallow Copy & Deep Copy (16 marks)

# Q14. Write a program using a dictionary of lists (e.g., a config dictionary where one value is a list of settings) to
# demonstrate why copy.copy() can silently corrupt data in real applications, and show how copy.deepcopy() prevents
# this. [Intermediate | 6 marks]
import copy

original_config = {
    "theme": "dark",
    "features": ["login", "dashboard", "reports"]
}

shallow_config = copy.copy(original_config)
deep_config = copy.deepcopy(original_config)

shallow_config["features"].append("analytics")

print("Q14 - After modifying shallow copy:")
print("Original config:", original_config)
print("Shallow copy:", shallow_config)
print("Deep copy:", deep_config)
print()

deep_config["features"].append("backup")

print("Q14 - After modifying deep copy:")
print("Original config:", original_config)
print("Shallow copy:", shallow_config)
print("Deep copy:", deep_config)
print()


# Q15. Create a class Team containing a list of Player objects (each Player has a name and score). Implement custom
# __copy__ and __deepcopy__ methods on the Team class so that copy.copy(team) shares the same Player objects,
# while copy.deepcopy(team) creates entirely independent Player objects. Write a driver that proves both behaviors with
# printed output. [Advanced | 10 marks]
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"Player(name={self.name}, score={self.score})"

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def __copy__(self):
        return Team(self.name, self.players[:])

    def __deepcopy__(self, memo):
        copied_players = [copy.deepcopy(player, memo) for player in self.players]
        return Team(self.name, copied_players)

    def show(self):
        print(f"Team: {self.name}")
        for player in self.players:
            print(player)

team_original = Team("Warriors", [Player("Aman", 50), Player("Riya", 70)])
team_shallow = copy.copy(team_original)
team_deep = copy.deepcopy(team_original)

team_shallow.players[0].score = 999
team_deep.players[1].score = 555

print("Q15 - Original team:")
team_original.show()
print()

print("Q15 - Shallow copied team:")
team_shallow.show()
print()

print("Q15 - Deep copied team:")
team_deep.show()
print()

print("Q15 - Object identity checks:")
print("Original first player is shallow first player:",
      team_original.players[0] is team_shallow.players[0])
print("Original first player is deep first player:",
      team_original.players[0] is team_deep.players[0])