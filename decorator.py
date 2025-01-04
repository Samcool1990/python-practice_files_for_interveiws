def decorator_func(func):
    def wrapper_func():
        print("CALL 2")
        return func()

    print("CALL 1")

    return wrapper_func


def show():
    print("CALL 3")


s = decorator_func(show)
s()

import logging


def log_function_calling(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args = {args}, KWARGS = {kwargs}")
        print(f"Calling {func.__name__} with args = {args}, KWARGS = {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        print(f"{func.__name__} returned {result}")
        return result

    print(f"{func.__name__} returned ")
    return decorated


@log_function_calling
def my_function(a, b):
    return a + b


print(":::::", my_function(5, 3))


obj = my_function(5, 3)


def decorator(func):
    def wrapper(x, y):
        print("Before function execution>>>>>")
        # result =
        print("After function execution>>>")
        return func(x, y)

    print(">>>>>>>>>>>>>>>>>>>>")
    return wrapper


@decorator
def add(x, y):
    return x + y


@decorator
def subtract(x, y):
    return x - y


result = add(5, 3)
print("Addition result:", result)

result = subtract(10, 4)
print("Subtraction result:", result)




# Create a decorator for custom exception in python.
import functools
import logging

# Define a custom exception
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Decorator for handling custom exceptions
def handle_custom_exception(default_message="An error occurred"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except CustomException as e:
                logging.error(f"CustomException caught: {e.message}")
                return {"error": e.message}
            except Exception as e:
                logging.error(f"Unexpected exception: {e}")
                return {"error": default_message}
        return wrapper
    return decorator

# Example usage
@handle_custom_exception(default_message="Something went wrong")
def risky_function(x):
    if x < 0:
        raise CustomException("Negative value error!")
    elif x == 0:
        raise ValueError("Zero value error!")
    return f"Success with {x}"

# Test the decorator
print(risky_function(5))  # Should print: Success with 5
print(risky_function(0))  # Should handle ValueError
print(risky_function(-1)) # Should handle CustomException
