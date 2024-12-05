str1 = 'hi suman welcome'

def decorator(func):
    def wrapper(str):
        upper_str = str.upper()
        result = func(upper_str)
        return result
    return wrapper
    
@decorator
def main_func(str1):
    return str1[::-1]
print(main_func(str1))