# Ask user if they want to gen a password
# If yes, ask for length of pass, if no exit
# Generate pass
# print Pass

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Would you like to gen a password? Yes/No: ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program Term")
    quit()
else:
    print("Invalid Input, please try again")
    quit()

