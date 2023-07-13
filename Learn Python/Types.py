
# Variable Types:

students_count = 1000   # integer = whole number
rating = 4.99           # float = decimal point number
is_published = False    # Boolean = True/False
course_name = "Python"  # String = text

# Strings:
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])      # print first 3 characters

# Escape Sequences
course = "Python \"Programming"  # \ is an escape character, will print " in text
# also do \' , \\ , \n
# \n will make a new line

# Formatted strings
first = "Mosh"
last = "Hamedani"
full = f"{first} {last}"    # prints value in function
print(full)

# String Methods
course = "Python Programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())       # Remove white space from start of string
print(course.find("pro"))   # Tells you where it is
print(course.replace("p", "j"))
print("pro" in course)       # Returns a boolean
print("Swift" not in course)

# Numbers
x = 1            # integer
x = 1.1          # float
x = 1 + 2j       # complex numbers

10 + 3
10 - 3
10 * 3
10 / 3
10 // 3        # Round the decided number
10 % 3         # remained of deviation
10 ** 3        # 10 power of 3
x += 3         # x = x + 3

# Working with numbers
import math
print(round(2.9))
print(abs(-2.9))

# Type conversions
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")
int(x)
str(x)
bool(x)
float(x)

