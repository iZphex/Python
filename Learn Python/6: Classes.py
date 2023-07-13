# Class: blueprint for creating new objects
# Object: instance of a class
# Class: Human
# Objects: John, Mary, Jack

# Creating a class
class Point:
    def draw(self):
        print("draw")
point = Point()

# Constructors
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
point.draw()

# Class vs Instance Attributes
class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")
point = Point(1, 2)
print(point.default_color)
point.z = 10
point.draw()

# Class vs Instance Methods
class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")
point = Point(0, 0)
point = Point.zero()
point.draw()

# Magic Methods
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(point)

# Comparing Objects
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

point = Point(1, 2)
other = Point(1, 2)
print(point == other)

# Making Custom Containers
class Tagcloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.tags(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        iter(self.tags)

cloud = Tagcloud()
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
print(cloud.tags)

# Properties
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")

product = Product(10)
print(product.price)

# Inheritance
class Animal:
    def __init__(self):
        self.age = 1

    def eat(selfself):
        print("eat")

class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

# Multi-level Inheritance
class Animal:
    def eat(self):
        print("eat")

class Bird(Animal):
        def fly(self):
            print("fly")

# Multiple Inheritance
class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee, Person):
    pass

manager = Manager()
manager.greet()

# Data Classes
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)

