# Multiple inheritance if you want to access parent class ellement
class Parent1:
    def method1(self):
        print("Method from Parent1")


class Parent2:
    def method2(self):
        print("Method from Parent2")


class Child(Parent1, Parent2):
    def method3(self):
        print("Method from Child")


# Example Usage
child_obj = Child()

# Accessing methods from Parent1 and Parent2
child_obj.method1()  # Output: Method from Parent1
child_obj.method2()  # Output: Method from Parent2

# Accessing method from Child
child_obj.method3()  # Output: Method from Child
Parent2.method2(child_obj)


# Class method & static method write function
class MyClass1:
    class_attribute = 0

    @classmethod
    def class_method(cls):
        cls.class_attribute += 1
        return cls.class_attribute


# Example Usage
print(MyClass1.class_method())  # Output: 1
print(MyClass1.class_method())  # Output: 2


class MyClass2:
    @staticmethod
    def static_method():
        return "This is a static method"


# Example Usage
print(MyClass2.static_method())  # Output: This is a static method
print(MyClass1.class_method())


# Given a string check in the string have any regular expression element in that
import re

s1 = "hello %$%$ world $^%$^$%"
cleaned_s = re.sub(r"[^a-zA-Z\s]", "", s1)
print(cleaned_s)
