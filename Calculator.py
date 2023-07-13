# Define functions needed: add, sub, multi, div
# Print options to user
# Ask for values
# call the functions
# while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")
def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
def multi(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print("A: Add")
    print("B: Sub")
    print("C: Multi")
    print("D: Div")
    print("E Exit")

    choice = input("input you choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        multi(a, b)
    elif choice == "d" or choice == "C":
        print("Division")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Exited")
        quit()
