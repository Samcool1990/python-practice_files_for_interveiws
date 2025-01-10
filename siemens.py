str1 = "I am a Python Programmer"

d1 = {}
for i in str1:
    d1[i] = d1.get(i,0) +1

print(d1)

# class A:
#     # _instance = None
#     def __init__(self):
#         pass
    
#     def __func1(self):
#         # if _instance:
#         #     print('Instance is captured')
#         print("Func1 called")
    
#     def func2(self):
#         pass

# obj = A()
# print(obj.func1)
# # print(A.func1())



list1 = ['flower', 'floor', 'flow']
list2=['cat', 'rat', 'mice']

def longest_common_prefix(words):
    if not words:
        return 0

    # Find the shortest word in the list
    shortest_word = min(words, key=len)

    # Compare characters of the shortest word with all other words
    for i, char in enumerate(shortest_word):
        for word in words:
            if word[i] != char:
                # Return the prefix up to the point of mismatch
                return shortest_word[:i] if i > 0 else 0

    return shortest_word  # The entire shortest word is a common prefix
print(longest_common_prefix(list1))  # Output: 'flo'
print(longest_common_prefix(list2)) 


list4 =[1,[2,[3,[4,[5],6]]]]

def flatten_lst(lst):
    new_lst = []
    if not lst:
        return []
    
    for item in lst:
        if isinstance(item, list):
            new_lst.extend(flatten_lst(item))
        else:
            new_lst.append(item)
    return new_lst
    
print(flatten_lst(list4))







    


# AWS SERVICE S3 tier, type of s3
# Lambda Versioning



# Explain OOPS concept with code
# 1. Encapsulation:
# Encapsulation refers to bundling data (attributes) and methods (functions) that operate on the data into a 
# single unit called a class. It also involves restricting access to certain details (using private attributes).

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # Error: Accessing private attribute

    
# 2. Inheritance
# Inheritance allows a class (child) to acquire properties and behaviors of another class (parent). 
# This promotes code reuse.
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        return f"{self.brand} vehicle moves at {self.speed} km/h."

class Car(Vehicle):  # Inheriting Vehicle
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def describe(self):
        return f"{self.brand} car with {self.doors} doors moves at {self.speed} km/h."

# Usage
car = Car("Toyota", 180, 4)
print(car.describe())  # Output: Toyota car with 4 doors moves at 180 km/h.



# 3. Polymorphism
# Polymorphism allows methods in different classes to have the same name but behave differently based on the
#  object calling them. It supports method overriding and operator overloading.
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Usage
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())
# Output:
# Bark
# Meow
# Some generic sound



# 4. Abstraction
# Abstraction hides complex implementation details and exposes only essential features. It can be achieved 
# using abstract base classes.
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Base Class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Usage
rect = Rectangle(10, 20)
print(f"Area: {rect.area()}")        # Output: Area: 200
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 60



# Summary of OOP Principles
# Principle	Key Features
# Encapsulation	Protecting data and methods by bundling them inside classes.
# Inheritance	Reusing and extending existing code through a parent-child relationship.
# Polymorphism	Writing code that can work with objects of multiple types.
# Abstraction	Hiding implementation details and exposing essential features.
# OOP enhances modularity, reusability, and maintainability of the code.


