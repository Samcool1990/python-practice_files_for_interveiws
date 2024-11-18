from random import randint

l = [randint(-50, 50) for i in range(1, 25)]
print(l)
if l[0] > l[1]:
    first = l[0]
    second = l[1]
else:
    first = l[1]
    second = l[0]
for i in range(2, len(l)):
    if l[i] > first:
        second = first
        first = l[i]
    elif l[i] > second and first != l[i]:
        second = l[i]
print(second)

# find second largest salary
# SELECT MAX(salary)
# FROM employees
# WHERE salary < (SELECT MAX(salary) FROM employees);
# or
# SELECT DISTINCT Salary
# FROM Employees
# ORDER BY Salary DESC
# LIMIT 1 OFFSET 1;

###What asyncio
"""asyncio is a library to write concurrent code using the async/await syntax. asyncio is used as a 
foundation for multiple Python asynchronous frameworks that provide high-performance network and 
web-servers, database connection libraries, distributed task queues, etc."""

##What is closure
"""A Closure is a function object that remembers values in enclosing scopes even if they are not 
present in memory."""
### what is list comprehension & generators
##difference between __str__ & __rprs__

"""The special method . __repr__() returns the official string representation, 
which is aimed at programmers as they develop and maintain a program. 
The special method . __str__() returns the informal string representation, 
a friendlier format for the program's user"""


##Difference between filter & get in ORM.
"""Notice the difference between the output of get() and filter() method. 
For the same parameter they both two different results. The get() method returns a instance of Author 
while filter() methods returns a QuerySet object. Lets see what happens, if get() method encounters 
multiple recor"""
