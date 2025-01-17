#Basic structure for FastAPI i
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
# from sqlaclhemy import CreateEngine

app = FastAPI()

class request_body(BaseModel):
    id: int
    name: str
    desc: str 

#database.py
# database_str = {'host', 'port', 'user', 'pass'}
# CreateEngine(database_str,)
# session(CreateEngine)

def get_db(session):
    try:
        session.db.connect()
    except:
        return {'message': 'failed'}
    finally:
        session.db.close()

@app.get('/index')
def func1(params: request_body):
    #business logic
    # db  = get_db()
    # db.execute()
    return {'status':200, 'message':'Success'}


#Decorator
def decorator(func):
    def wrapper(x,y):
        #add logic
        # print()
        print(f"{func.__name__} is running with arguments {x} and {y}")
        return func(x,y)
    return wrapper
    
@decorator
def add(x,y):
    return x + y
    
print(add(5,3))



#Custom exception using decorator
#Multithread & Multiprocessing when to use in reall life?
#Multithread is I/O bound & Multiprocessing is CPU bound.

# 2ndround F2F
# given a string find out the count of the possible combination between the string's elements.
# Example: given string 'abc'. 'abc', 'acb','bca','bac','cab','cba'. output = 6
import math

def count_permutations(string):
    # Calculate the length of the string
    n = len(string)
    # Return factorial of n
    return math.factorial(n)

# Example usage
input_string = "abc"
output = count_permutations(input_string)
print(f"The count of permutations for the string '{input_string}' is: {output}")


# same question but output should be all the combinations. 
# output = ['abc', 'acb','bca','bac','cab','cba']

from itertools import permutations

def generate_permutations(string):
    # Generate all permutations as tuples
    perm_tuples = permutations(string)
    # Convert each tuple into a string and return as a list
    return [''.join(perm) for perm in perm_tuples]

# Example usage
input_string = "abc"
output = generate_permutations(input_string)
print(f"All permutations of the string '{input_string}' are: {output}")





# Common elements in two sorted arrays 
array1 = [1,2,3,7,8]
array2 = [7,8]
array3 = [i for i in array1 if i in array2]
print(array3)   








