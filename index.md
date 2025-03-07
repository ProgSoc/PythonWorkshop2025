---
marp: true
theme: uncover
class: lead
paginate: true
---

<style>
h1 {
  color: black;
}
section {
    font-size: 30px;
}
</style>

# Python Workshop for Beginners

Welcome to the Python Workshop!

---

### Introduction to Python

- Python is an easy-to-learn, powerful programming language.
- It was created by Guido van Rossum and released in 1991.
- Python is known for its simple syntax and readability.

---

### Why Python?

- Versatile and used in various fields like:
  - Web Development
  - Data Science
  - Machine Learning
  - Automation
- Beginner-friendly, even for non-programmers.

---

### Language Features

- **Dynamically Typed**: Variable types are determined at runtime, thus type checks are not required at compile-time in the intepreter.

- **Interpreted**: Compiles to bytecode which is then read and executed by a virtual machine (not the CPU directly like compiled languages). As this process is detached from the language there are multiple implementations of Python interpreters. (CPython, PyPy, Jython).

- **Garbage-collected**: Handles allocation and deallocation of memory for you, unlike languages like C, Rust. This is done in the virtual machine.

- Massive standard library

---

### Setting Up Python

1. Download and Install Python from [python.org](https://www.python.org/downloads/)
2. Install a code editor:
   - **VS Code**, **PyCharm**, or **Sublime Text**
3. Open your terminal/command prompt and type `python --version` to check your Python version.
4. Or just open up a python compiler online.

---

### Python Syntax Basics

```python
# This is a comment
print("Hello, World!")  # Prints text to the screen
```

---

### Variables and Data Types

    Variables store data values.
    Common data types in Python:
        int: Integer numbers
        float: Decimal numbers
        str: String (text)
        bool: Boolean (True/False)

```python
age = 25  # Integer
height = 5.9  # Float
name = "John"  # String
is_student = True  # Boolean
```

---

### Dictionaries

- Store key value pairs of data

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

---

### Lists

- Lists are mutable ordered collections that can store multiple items in a single variable

```python
# Creating a list
my_list = [1, 2, 3, 4, 5]

# Checking if an item exists in the list
print(4 in my_list)  # Output: True
```

---

### Control Flow: if/else Statements

```python
age = 18

if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor.")
```

---

### Loops: for and while

For Loop

```python
for i in range(5):
    print(i)  # Prints numbers 0 to 4
```

While Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

### Switch and Case

```python
match variable: # python 3.10 + only
    case pattern_1:
        # Code block for pattern_1
    case pattern_2:
        # Code block for pattern_2
    case _:
        # Code block for a default case (like `else`)

```

---

### Functions in Python

Functions are reusable blocks of code.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Calls the function
```

---

### Walrus Operator

- Walrus operator lets you assign a variable inside an expression

```python
# Using the walrus operator to assign and use a value inside an expression
if (n := len("Hello")) > 3:
    print(f"The length of 'Hello' is {n}.")  # Output: The length of 'Hello' is 5.

```

---

### Unpacking Operator

- Unpacking operators applies a function on each value in a list

```python
# List of strings
strings = ["Hello", "World", "This", "Is", "Unpacking", "Operator"]

# Print all strings using the unpacking operator
print(*strings)

```

---

### List Comprehension

- List comprehension is a cool way to generate a new list from a previous one.

```python
# List comprehension to create a new list from an existing one
original_list = [1, 2, 3, 4, 5]
new_list = [x * 2 for x in original_list]  # Multiplying each element by 2
print(new_list)  # Output: [2, 4, 6, 8, 10]
```

---

### List Slicing

- List slicing lets you extract a part of a list based on a range of indices

```python
# List slicing to extract a part of a list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to 5 (exclusive of index 5)
sliced_list = original_list[2:5]
print(sliced_list)  # Output: [3, 4, 5]

# Get elements from the start up to index 4 (exclusive of index 4)
sliced_list_start = original_list[:4]
print(sliced_list_start)  # Output: [1, 2, 3, 4]

# Get last element
sliced_list_end = original_list[-1]
print(sliced_list_end)  # Output: [9]
```

---

### Package Manager PIP

- PIP is the python package manager used to easily install packages.

- By default, PIP installs packages globally unless a virtual environment is used.

---

### Virtual Environments

- Virtual Environments are isolated sets of Python packages.

- Make it easy to share python projects with friends.

```bash
    python -m venv myenv
    cd myenv
    source myenv/bin/activate # execute the script to activate the env
```

```sh
(myenv) user@macbook:~/path/to/project$
```

---

## Rock Paper Scissors Project

- Okay let's do this!

---

### Conclusion

Practice is key to mastering Python.
Start small and build projects as you go!
Explore Python documentation: docs.python.org

---

### Questions?

Feel free to ask questions!
