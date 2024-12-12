# Write function which will find the second lowest element without using indexing, sort, set method. Use min 
# & max to find the element

lst = [3,9,3,6,3,4]

min_val = min(lst)
max_val = max(lst)
print(min_val, max_val)
second_element = 0
for i in lst:
    if i > min_val and i < max_val:
        second_element = i
print(second_element)


# Second round:
# Find the duplicate values in a particular column
# SELECT name, COUNT(name) AS count_of_name
# FROM table
# GROUP BY name
# HAVING COUNT(name) > 1;




from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class RequestBody(BaseModel):
    A: int
    B: int


# Decorator to check B for zero
def zero_error(func):
    def wrapper(params: RequestBody):
        if params.B == 0:
            raise HTTPException(status_code=400, detail="Value of B should be greater than 0")
        return func(params)
    return wrapper


@app.post('/')
@zero_error
def post_request(params: RequestBody):
    a = params.A
    b = params.B
    return {"result": a + b}
