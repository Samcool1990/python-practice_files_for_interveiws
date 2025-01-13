from functools import wraps
import time
# from loguru import logger

def main_decorator(DEBUG = "Custom Logging"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            start = time.time()
            result = func(*args,**kwargs)
            end = time.time()
            total_time = end - start
            # logger.info(f"Total {total_time} time taken to run {__func__.__name__}")
            print(f"Total {total_time} time taken to run {func.__name__}")
            return result
        return wrapper
    return decorator


@main_decorator("Custom Logging")
def add(a,b):
    return a + b
    
print(add(5,3))



a = (1,2,3,4)
a = (1,2,3,4,5)
# To handle such cases where reassignment of variables (like tuples in your example) might lead to bugs or 
# unintended behavior, you can adopt the following best practices:


# 1. Use Constants for Immutable Data:
# In Python, you can follow a naming convention (e.g., all uppercase) for immutable values like tuples to 
# indicate they should not be reassigned.
# A = (1, 2, 3, 4)  # Indicates a constant
# This doesn't enforce immutability programmatically but communicates intent to other developers.


# 2. Implement Read-Only Attributes:
# Use classes to encapsulate the tuple and prevent reassignment by implementing read-only properties.
# class ImmutableTuple:
#     def __init__(self, values):
#         self._values = values

#     @property
#     def values(self):
#         return self._values

# a = ImmutableTuple((1, 2, 3, 4))
# # Access using a.values
# Any attempt to modify a.values directly will raise an error.


# 3. Static Analysis Tools:
# Use tools like mypy or Pyright to catch unintended reassignments. Define a with a specific type hint and 
# avoid reassigning variables of the same name to different types or lengths.

# from typing import Tuple

# a: Tuple[int, int, int, int] = (1, 2, 3, 4)
# If someone tries to reassign it to (1, 2, 3, 4, 5), the static type checker will throw an error.



# 4. Code Reviews:
# Ensure that your team follows strict code review practices to catch such mistakes. Use guidelines like 
# "Avoid reusing variable names for different purposes."


# 5. Linter Rules:
# Set up linters (e.g., Flake8, pylint) with custom rules to warn against variable reuse in the same scope.


# 6. Use Comments and Documentation:
# Clearly document the purpose and expected immutability of a. This reduces the likelihood of unintentional 
# reassignment.


# 7. Functional Programming Approach:
# Prefer creating new variables rather than mutating or reassigning existing ones.

# a = (1, 2, 3, 4)
# # Instead of reassigning
# b = (1, 2, 3, 4, 5)  # Use a new variable
# By adopting these practices, you can minimize the risk of bugs due to such reassignments in your codebase.








# try:
#     a = 10 % 0
# # except ZeroDivisioError as e:
# #     print(f"{ e.error}"")
    
# # else:
# #     print("Else block is running")
    
# finally:
#     print("Finally Block is running")






class CustomException(Exception):
    def __init__(self, amount, message, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id
        self.message = message
        # Use a formatted string for the error message
        error_message = f"Transaction ID: {self.transaction_id} with Amount: {self.amount} has failed. Reason: {self.message}"
        super().__init__(error_message)  # Pass the formatted error message to the base class

    def __str__(self):
        # Return a string representation of the error message
        return f"[CustomException] {self.message} (Transaction ID: {self.transaction_id}, Amount: {self.amount})"


# Example Usage:
amount = 100
message = "Failed"
transaction_id = "001"

try:
    if amount != 100:
        raise CustomException(amount, message, transaction_id)
    else:
        print(f"Transaction ID: {transaction_id} with Amount: {amount} was successful.")
except CustomException as e:
    print(str(e))




# To write a Python program that searches for elements containing "metal" in the array
# without changing the datatype, you can achieve this by iterating through the set elements and checking
# if any element contains the word "metal".
 
 
# Initial array of sets
arr = [{"metal", "rock"}, {"metallica", "masti"}, {"master", "masti"}, {"blaster", "rock"}]
search = 'metal'

# 1 way:
result = []
# Search for elements containing "metal"
result = [s for s in arr if any(search in element for element in s)]

# Output the result
print("Sets containing elements with 'metal':", result)
    



# 2nd way:
# Initialize an empty set to store the result
result = set()

# Iterate through the array of sets
for s in arr:
    # Check if the search term exists in the set
    if any(search in item for item in s):
        # Add all elements of the set to the result
        result.update(s)

# Remove the search term itself from the result if it exists
result.discard(search)

# Convert the set to a list and print the result
output = list(result)
print(output)



