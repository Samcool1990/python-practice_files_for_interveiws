# How would you deploy an application in lambda

# fibonacci_series using a Generator
def fibonacci_series(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

f1 = fibonacci_series(5)
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))

def fibonacci_series2(n):
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

f2 = fibonacci_series(5)
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))



#From a list create a new list with even numbers using lambda
l1 = [1,2,3,4,5,6,7,8,9,10]
sum = list(filter(lambda x: x%2==0, l1))
print(sum)



#Raise exception if element is 1 in a list
#EOF error
# An EOF error occurs when your program tries to read input, but there's no more data to read



# create a custom decorator which will take a function & 2 arguments & will return the sum of the arguments
def custom_decorator(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Calculate the sum of the arguments
            result = arg1 + arg2
            print(f"Sum of {arg1} and {arg2} is: {result}")
            # Call the original function (optional)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage
@custom_decorator(10, 20)
def my_function():
    print("Function executed!")

my_function()



# Delete a column in postgres
# What are DDL queries
# What is blob in sql