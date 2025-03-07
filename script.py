import dis

# ------------------------
# Python Code Examples
# ------------------------

# Variables and Data Types
age = 25  # Integer
height = 5.9  # Float
name = "John"  # String
is_student = True  # Boolean

print(f"Age: {age}, Height: {height}, Name: {name}, Is Student: {is_student}\n")

# Dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Dictionary:", thisdict, "\n")

# Lists
my_list = [1, 2, 3, 4, 5]
print("Is 4 in my_list?", 4 in my_list)  # Output: True
print("List:", my_list, "\n")

# Control Flow: if/else Statements
age = 18
if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor.")
print()

# Loops: for and while
print("For Loop:")
for i in range(5):
    print(i)  # Prints numbers 0 to 4
print()

print("While Loop:")
count = 0
while count < 5:
    print(count)
    count += 1
print()

# Functions in Python


def greet(name):
    print(f"Hello, {name}!")


greet("Alice")  # Calls the function
print()

# Walrus Operator
if (n := len("Hello")) > 3:
    # Output: The length of 'Hello' is 5.
    print(f"The length of 'Hello' is {n}.")
print()

# Unpacking Operator
strings = ["Hello", "World", "This", "Is", "Unpacking", "Operator"]
print("Unpacking operator output:", *strings)  # Prints all strings in the list
print()

# List Comprehension
original_list = [1, 2, 3, 4, 5]
new_list = [x * 2 for x in original_list]  # Multiplying each element by 2
print("List Comprehension Result:", new_list)  # Output: [2, 4, 6, 8, 10]
print()

# List Slicing
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to 5 (exclusive of index 5)
sliced_list = original_list[2:5]
print("List Slicing (2:5):", sliced_list)  # Output: [3, 4, 5]

# Get elements from the start up to index 4 (exclusive of index 4)
sliced_list_start = original_list[:4]
print("List Slicing (start:4):", sliced_list_start)  # Output: [1, 2, 3, 4]

# Get last element using negative indexing
sliced_list_end = original_list[-1]
print("Last Element:", sliced_list_end)  # Output: 9
print()


# Disassemble bytecode
def f(a, b):
    return a+b


dis.dis(f)

# python3 -m compileall script.py
