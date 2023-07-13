# Exceptions
numbers = [1, 2]
print(numbers[3])

age = int(input("Age: "))

# Handling Exceptions
try:
    age = int(input("Age: "))
except ValueError:
    print("You did not enter age")
else:
    print("No exception were thrown")
print("exceptions continue")

# handling diff Exception
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You did not enter age")
else:
    print("No exception were thrown")

# Cleaning up
try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You did not enter age")
else:
    print("No exception were thrown")
finally:
    file.close()

# The With Statement
try:
    with open("app.py") as file:
        print("File opened")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You did not enter age")
else:
    print("No exception were thrown")

# Raising Exceptions
def calculate(age):
    if age <= 0:
        raise ValueError ("Age cannot be 0 or less")
    return 10 / age
try:
    calculate(-1)
except ValueError as error:
    print(error)

# Cost of raising exceptions
from timeit import timeit
code1 = """
def calculate(age):
    if age <= 0:
        raise ValueError ("Age cannot be 0 or less")
    return 10 / age

try:
    calculate(-1)
except ValueError as error:
    print(error)
"""
print(timeit(code1, number=10000))
