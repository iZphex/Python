# Lists
from audioop import reverse

letters = ["a", "b", "c", "d", "e"]
matrix = [[0, 1], [1, 2]]
zeros = [0] * 100
combined = zeros + letters
numbers = list(range(20))
chars = list
print(len(chars))

# Accessing items
letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0:3])

# List unpacking
numbers = [1, 2, 3]
first, *other, last = numbers #Packs other numbers in list within a list
print(first, last)
print(other)

# Looping over lists
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)

# Adding/Removing items
letters = ["a", "b", "c"]
# Add
letters.append("d")
letters.insert(0, "-")

# Removing items
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()

# Finding items in list
letters = ["a", "b", "c"]
letters.count("d")
if "d" in letters:
    print(letters.index("a"))

# Sorting Lists
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(sorted(numbers))
print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

# Lambda Functions
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

items.sort(key=lambda item: item[1])
print(items)

# Map Functions
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = list(map(lambda item: item[1], items))
print(prices)

# Filter Function
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# List comprehension
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]      # Preferred way, use list comprehension

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item[1] for item in items if item[1] >= 10]    # Preferred way, use list comprehension

# Zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]
list(zip("abc", list1, list2))

# Stacks
# LIFO (Last in - First out)
browsing = []
browsing.append(1)
browsing.append(2)
browsing.append(3)
print(browsing)
lst = browsing.pop()
print(last)
print(browsing)
print("redirect", browsing)

# Queues
# FIFO (First in, First out)
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")

# Tuples
point = (1, 2) + (3, 4)
point2 = (1, 2) * 3
print(point[1])

# Swapping Variables
x = 10
y = 11
x, y = y, x

# Arrays
from array import array
array("i", [1, 2, 3])
numbers.append(4)

# Sets
numbers = [1, 1, 2, 2, 3, 4, 5, 6, 7]
first = set(numbers)
second = {1, 5}

print(first | second)
print(first and second)
print(first - second)
print(first ^ second)

# Dictionary
point = {"x": 1,  "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
del point["x"]

for key, value in point.items():
    print(key, value)

# Dictionary Comprehension
values = []
for x in range(5):
    values.append(x * 2)
# Same as above
values = {x: x * 2 for item in range(5)}
print(values)

# Generator Expression
from sys import getsizeof

values = (x * 2 for x in range(10))
print("gen", getsizeof(values))


# unpacking operator
numbers = [1, 2, 3]
print(*numbers)

first = [1, 2]
second = [3]
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
values = [*range(5), *"Hello"]
print(values)




