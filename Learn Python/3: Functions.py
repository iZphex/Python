# Defining functions
def greet():
    print("Hi there")
    print("Welcome")


greet()

# Arguments
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome")


greet("Mosh", "Hamedani")

# Types of functions
# Functions that Perform task
# Functions that return a value

def greet(name):
    print(f"Hello {name}")

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Mosh")
print(message)

# Keyword arguments
def increment(number, by):
    return number + by

print(increment(number=2, by=1)) # Makes code readable

# Default Arguments
def increment(number, by=1):
    return number + by


print(increment(2, 1))


# xargs
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

# xxargs
def save_user(**user):
    print(user)


save_user(id=1, name="John", age=22)

# Scope
# Global Var, Local Var

# Debugging
