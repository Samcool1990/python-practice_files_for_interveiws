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
    def decorated(*args,**kwargs):
        logging.info(f"Calling {func.__name__} with args = {args}, KWARGS = {kwargs}")
        #print(f"Calling {func.__name__} with args = {args}, KWARGS = {kwargs}")
        result =func(*args,**kwargs)
        logging.info(f"{func.__name__} returned {result}")
        #print(f"{func.__name__} returned {result}")
        return result
    print(f"{func.__name__} returned ")
    return decorated


@log_function_calling
def my_function(a,b):
    print(a+b)

obj = my_function(5,3)




def decorator(func):
    def wrapper(x, y):
        print("Before function execution>>>>>")
        #result = 
        print("After function execution>>>")
        return func(x, y)
    print('>>>>>>>>>>>>>>>>>>>>')
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