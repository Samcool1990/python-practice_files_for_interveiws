#Custom exceptions 
# Define a custom exception class
class InvalidTransactionError(Exception):
    """Exception raised for errors in the transaction process.

    Attributes:
        transaction_id -- ID of the transaction which caused the error
        amount -- amount involved in the transaction
        message -- explanation of the error
    """

    def __init__(self, transaction_id, amount, message="Invalid transaction"):
        self.transaction_id = transaction_id
        self.amount = amount
        self.message = f"{message}: Transaction ID {transaction_id} with amount ${amount:.2f}"
        super().__init__(self.message)

    def log_error(self):
        """Log the error details to a file or external system."""
        with open('transaction_errors.log', 'a') as log_file:
            log_file.write(f"ERROR: {self.message}\n")
        print(f"Logged error: {self.message}")

    def __str__(self):
        return self.message

# Example usage
try:
    # Simulate an invalid transaction scenario
    transaction_id = 12345
    amount = -100.50  # Negative amount is invalid
    if amount < 0:
        raise InvalidTransactionError(transaction_id, amount, "Negative amount not allowed")
except InvalidTransactionError as e:
    e.log_error()
    print(e)



#decorator with condition
def validate_input(func):
    def wrapper(a, b):
        if a == 0 or b == 0:
            print("Both numbers should be greater than 0. Please provide valid input.")
            while a <= 0:
                a = int(input("Enter the first number: "))
            while b <= 0:
                b = int(input("Enter the second number: "))
        return func(a, b)
    return wrapper

@validate_input
def add_numbers(a, b):
    return a + b

# Example usage
result = add_numbers(0, 7)
print("Result:", result)

#operator overloading & Nothing such under loading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Example usage
v1 = Vector(1, 2)
v2 = Vector(3, 4)

sum_vector = v1 + v2
diff_vector = v1 - v2
scaled_vector = v1 * 2

print(sum_vector)  # Output: Vector(4, 6)
print(diff_vector) # Output: Vector(-2, -2)
print(scaled_vector) # Output: Vector(2, 4)

#Explain type of inheritance
#Single Inheritance:
class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):
    pass

c = Child()
c.method()  # Output: "Parent method"


#Multiple Inheritance:
class Parent1:
    def method1(self):
        print("Parent1 method")

class Parent2:
    def method2(self):
        print("Parent2 method")

class Child(Parent1, Parent2):
    pass

c = Child()
c.method1()  # Output: "Parent1 method"
c.method2()  # Output: "Parent2 method"

#Multilevel Inheritance:
class Grandparent:
    def method(self):
        print("Grandparent method")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.method()  # Output: "Grandparent method"

#Hierarchical Inheritance:
class Parent:
    def method(self):
        print("Parent method")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()
c1.method()  # Output: "Parent method"
c2.method()  # Output: "Parent method"
#Hybrid (or Cyclic) Inheritance:
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass


'''The five types of inheritance in Python are single, multiple, multilevel, hierarchical, 
and hybrid inheritance'''

#Magic methods
'''Magic methods, also known as dunder methods (short for "double underscore" methods), are special 
methods in Python that start and end with double underscores (e.g., __init__, __str__, __add__). 
These methods provide a way to customize the behavior of classes and objects in specific situations. 
Here are some commonly used magic methods:

__init__(self, ...): The constructor method. It is called when a new instance of a class is created and 
allows you to perform any initialization necessary.

__str__(self): The string representation method. It is called when the str() function is used or when 
an object is printed with print(). It should return a human-readable string representation of the object.

__repr__(self): Similar to __str__, but provides a more unambiguous representation of the object. 
It is called when repr() is used.

__len__(self): Defines the behavior of the len() function for an object.

__getitem__(self, key): Defines behavior for indexing, i.e., obj[key].

__setitem__(self, key, value): Defines behavior for assigning a value to an index, i.e., obj[key] = value.

__delitem__(self, key): Defines behavior for deleting an index, i.e., del obj[key].

__iter__(self): Allows an object to be an iterable, enabling it to be used in a for loop.

__next__(self): Used in conjunction with __iter__ to define an iterator.

__contains__(self, item): Defines behavior for the in operator.

__call__(self, ...): Allows an instance to be called as a function.

__eq__(self, other), __ne__(self, other), __lt__(self, other), __le__(self, other), __gt__(self, other), 
__ge__(self, other): Comparison operators for equality, not equal, less than, less than or equal, 
greater than, and greater than or equal.

__add__(self, other), __sub__(self, other), __mul__(self, other), __truediv__(self, other): Arithmetic 
operators for addition, subtraction, multiplication, and division.

__enter__(self) and __exit__(self, exc_type, exc_value, traceback): Used in the context management 
protocol with the with statement.

__getattr__(self, name): Called when an attribute lookup fails.

__setattr__(self, name, value): Called when an attribute assignment is attempted.

__delattr__(self, name): Called when an attribute deletion is attempted.

These are just some of the commonly used magic methods. Depending on your needs, you may choose to 
implement different combinations of these methods in your classes to customize their behavior. 
Keep in mind that not all of these methods need to be implemented for every class; you should only 
implement the ones that are relevant to the functionality of your specific class.'''