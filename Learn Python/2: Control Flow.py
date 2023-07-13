# Conditional Statements
temp = 35
if temp > 30:
    print("It's warm")
elif temp > 20:
    print("It's nice")
else:
    print("It's cold")

# Ternary Operations
age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# Logical Operators
high_income = True
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

# Chaining Comparison Operators
age = 22
if age >= 18 and age < 65:            # Turn this into
    # if 18 <= age < 65:              # This, Same thing
    print("Eligible")

# For Loops
print("Sending a message")
for number in range(1, 10, 2):
    print("Attempt", number + 1, number * ".")

# For Else
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Success")
        break  # jumps out of loop
    else:
        print("Failed")

# Nested Loops
for x in range(5):
    for y in range(3):
        print(f"(){x}, {y}")

# Iterables
print(type(5))
print(type(range(5)))
# Iterable, can change it
for x in range(5):
    print(f"")

# While Loops
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# Infinite Loop
command = ""
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() != "quit":
        break  # Stop
