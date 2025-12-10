# Explain CI/CD Implementation
# "In my current project, we use GitLab CI/CD. The pipeline is triggered on every code commit, running unit 
# tests using Pytest, followed by static code analysis via PyLint. If the tests pass, the application is 
# containerized using Docker and deployed to AWS ECS. Rollbacks are managed through versioned Docker images."


# Q1. Tell me a thing which you learned on your own and implemented it. What challenges did you face, and 
# how did you overcome them?

# "I learned Natural Language Processing (NLP) for a project requiring Named Entity Recognition (NER). 
# The challenge was understanding data preprocessing and tuning the model for accuracy. I overcame it by 
# taking a structured approach—reading documentation, practicing on datasets, and collaborating with the 
# AI/ML team."

# Q2. Tell me a challenge you faced in your project.
# "A major challenge was optimizing a slow API that fetched hierarchical data. It resulted from an N+1 query 
# issue. I resolved it by using Django's select_related and caching frequently accessed data."


# Q3. Tell me an example where you took the initiative when you were not asked.
# "In a project, I noticed we lacked detailed API documentation. I created and shared API specs using Swagger, 
# which helped the frontend team and reduced delays."


# Q4. You received critical feedback. How did you take it and work on the same?
# "I once received feedback about my lack of proactive communication in stand-ups. I acknowledged it, started 
# preparing concise updates, and ensured clarity in my progress reports, which improved team collaboration."


# For the team offsite, there is a draft where you can win a price if your number is picked first. 
# The game uses two integers x, y to generate a sequence.
# Given two integers x and y, construct an infinite sequence of integers A (a0, a1, ...} as follows:
# a0 = 0 and for every i >= 1, a(2i-1)=a (21-2)+x and a(21) = a(2-1) - y.
# Given three integers x, y, z, find the index of the first occurrence of z in A or report that z does not 
# appear in A.
# For example, if x=2, y=1 and z=3, then A=(0,2,1,3,2,4,3,...) and the answer is 3 (a(3)=3 and 
# this is the first occurrence of 3 in A). If x=2, y=0 and z=3, then A=(0,2,2,4,4,6,6,...) and 
# the answer is -1 (there is no occurrence of 3 in A).
# Additional info
# 0<= x, y, z <=1000

def generate_sequence(x,y,n,z):
    A = [0]
    
    for i in range(1,n):
        if i % 2 == 1:
            A.append(A[i-1] + x)
        else:
            A.append(A[i-1] - y)
            
    for i in range(len(A)):
        if A[i] == z:
            return A,i
    else:
        return A,-1
        
        
x = 2
y = 0
n = 10
z = 3

sequence , l = generate_sequence(x,y,n,z)

if l != -1:
    print("{} value is present at index {}".format(z,l))
else:
    print(-1)
print('Sequence is :', sequence)


# Let me walk you through the problem and solution systematically, highlighting key areas Fabien might focus 
# on during the interview.

# Problem Analysis
# The function generate_sequence:

# Generates a sequence starting with 0.
# Alternates between adding x and subtracting y for n terms.
# Checks if the sequence contains a specific value z.
# Returns the sequence and the index of z, or -1 if z is not found.
# Code Complexity
# Time Complexity:

# Generating the sequence: 
# 𝑂
# (
# 𝑛
# )
# O(n) because it iterates once to calculate 
# 𝑛
# n terms.
# Searching for 
# 𝑧
# z: 
# 𝑂
# (
# 𝑛
# )
# O(n) because it iterates through the sequence to check for 
# 𝑧
# z.
# Overall time complexity: 
# 𝑂
# (
# 𝑛
# )
# +
# 𝑂
# (
# 𝑛
# )
# =
# 𝑂
# (
# 𝑛
# )
# O(n)+O(n)=O(n).
# Space Complexity:

# Storing the sequence: 
# 𝑂
# (
# 𝑛
# )
# O(n), where 
# 𝑛
# n is the number of terms in the sequence.
# Best and Worst-Case Scenarios
# Best Case:

# The target value z is found early in the sequence. For example, at index 
# 0
# 0 or 
# 1
# 1. The search ends quickly.
# Worst Case:

# The target value z is not present in the sequence, requiring a full traversal of the sequence (complexity 
# 𝑂
# (
# 𝑛
# )
# O(n)).
# Addressing Infinite Sequence
# Since the sequence is potentially infinite, we must impose a finite limit to make the problem solvable. 
# For example:

# Assume a maximum limit for 
# 𝑛
# n (like 1000).
# If 
# 𝑧
# z is beyond a practical range, handle it gracefully.

# Key Discussion Points in the Interview
# Complexity Explanation:

# Time complexity 
# 𝑂
# (
# 𝑛
# )
# O(n) for both sequence generation and search.
# Space complexity 
# 𝑂
# (
# 𝑛
# )
# O(n) due to storage of the sequence.
# Infinite Sequence Handling:

# Imposing a finite limit (e.g., 
# 𝑛
# =
# 1000
# n=1000).
# Practicality of breaking the loop after 
# 𝑧
# z is found.
# Best/Worst Case:

# Best: 
# 𝑧
# z found at the start.
# Worst: 
# 𝑧
# z not found, requiring a full traversal.
# Real-World Application:

# Patterns like this can be found in arithmetic sequences.
# Discuss scenarios where handling infinite sequences or cyclic patterns is required (e.g., simulations, calculations with limits).
# Let me know if you want additional details or practice scenarios for this!



# 1.
sequence = [2,0.5,7,"21" "x100", 100,"001x" ]
print(sequence[3:-2][0])
# 21x100

# 2.
def alert(*args, **kwargs):
    print(*args[0],kwargs.values()[0])
    
    
# alert("Hellow world", msg = 123)
# Will throw error


# 3.
# Numpy in not a standard library in python

# 4.
# which built in module is benefecial if you are adding support for python 3 is some legacy python 2 code ?
# py_compile, lib2to2,__legacy__, __future__
# Answer: __future__


# 5.
# in this code how can you ensure it prints the message only after both tasks have finished?
import time
from multiprocessing.pool import Pool

def task():
  time.sleep(1)

pool = Pool()
pool.apply_async(task)
pool.apply_async(task)


#print when both tasks have completed
print("all tasks are completed")

1. 
import time
from multiprocessing.pool import Pool

def task():
    time.sleep(1)

pool = Pool()

# Submit tasks asynchronously
result1 = pool.apply_async(task)
result2 = pool.apply_async(task)

result1.join()
result2.join()

print("all tasks are completed")

2.
import time
from multiprocessing.pool import Pool

def task():
    time.sleep(1)

with Pool(5) as pool:
     pool.apply_async(task)
     pool.apply_async(task)

print("all tasks are completed")

3.
import time
from multiprocessing.pool import Pool

def task():
    time.sleep(1)

pool = Pool()
pool.apply_async(task)
pool.apply_async(task)

pool.close()
pool.join()

print("all tasks are completed")


4.
# import time
# from multiprocessing.pool import Pool

# def task():
#     time.sleep(1)

# pool = Pool()
# pool.apply_async(task)
# pool.apply_async(task)

# pool.join()
# pool.terminate()

# print("all tasks are completed")

# # Answer:3

# sequence = [2, -100,0.0, 9.2, 1., 5, -.0, 12 ]
# print([num for num in sequence if type(num) == int])


# import unittest
# list1 = [1,2,3]

# # class TestLists(unittest.TestCase):
# #      def test_is_unique(self):
#            #assert that the list in unique here

# # unittest.main()

# # import unittest

# # list1 = [1, 2, 3]

# class TestLists(unittest.TestCase):
#     def test_is_unique(self):
#         # Check if the list has unique elements
#         self.assertEqual(len(list1), len(set(list1)), "The list contains duplicate elements")

# if __name__ == "__main__":
#     unittest.main()





# class Dog:
#     def __init__(self, name):
#         __name__ = name
        
#     def name(self):
#         return __name__
        
# dogobj = Dog("Scooby")
# print(dogobj.name())
# __main__




# How would you create a context manager generator for a mysql database ?
# import mysql.connector
# from contextlib import contextmanager

# @contextmanager
# def database_connection(db):
#     conn = mysql.connector.connect(user='username', password='password', database=db)
#     try:
#         yield conn
#     finally:
#         conn.close()



# cmd = '$ cd ../home'.split()
# match cmd:
#     case '$', _,_,'../home':
#         print('case1')
        
#     case _,'cd',*dir:
#         print('case2')
#     case '$ cd', *dir:
#         print('case3')
#     case _:
#         print('case4')
#case2



# What are Wheel & Egg ?
# Wheel and Egg are two types of Python packaging formats used for distributing Python libraries. Both formats aim to simplify the process of packaging and installing Python projects but have differences in design and usage.
# 1. Egg
# Introduced by: Setuptools
# Purpose: A format to package and distribute Python projects, widely used before the advent of Wheel.
# File Extension: .egg
# Characteristics of Egg:
# Features:

# Contains metadata about the project, such as dependencies and versioning.
# Can include Python code, compiled extensions, and resources.
# Implementation:

# Can be directly imported without unpacking.
# Often includes a PKG-INFO file for project metadata.
# Drawbacks:

# Lack of standardization (specific to Setuptools).
# Harder to use with other Python tools or modern standards like pip.
# Tied closely to the environment in which it was created (less portable).
# 2. Wheel
# Introduced by: PEP 427 (Python Enhancement Proposal)
# Purpose: A more modern and efficient binary distribution format for Python libraries.
# File Extension: .whl
# Characteristics of Wheel:
# Features:

# A standardized format recognized by the Python Packaging Authority (PyPA).
# Can be installed faster because it doesn't require compilation during installation.
# Contains all necessary files, including metadata, in a ZIP archive.
# Platform-independent for pure Python packages or platform-specific for compiled extensions.
# Implementation:

# Used with modern tools like pip and twine.
# Simplifies dependency management and installation.
# Compatible with Python's standard installation tools.
# Advantages:

# More portable than Egg.
# Designed for speed and efficiency.
# Works seamlessly with the Python packaging ecosystem.
# Key Differences Between Wheel and Egg
# Feature	Egg	Wheel
# Introduced By	Setuptools	PEP 427
# File Extension	.egg	.whl
# Standardization	No	Yes
# Performance	Slower installation	Faster installation
# Dependency Management	Less efficient	Better dependency handling
# Current Status	Deprecated	Widely adopted (default)
# Why Use Wheel?
# Wheel has become the standard for Python packaging and is recommended for most projects. Tools like pip prioritize Wheels over Eggs when both are available.
# Usage Examples:
# Build a Wheel:

# bash
# Copy code
# python setup.py bdist_wheel
# Install a Wheel:

# bash
# Copy code
# pip install your_package.whl



# correctly resamples the DataFrame 'df' with a a DateTime index to get the mean of the last five minutes every hour ?
# just give the sytax with resample & rolling
# df.resample('H').rolling('5min').mean()



# correctly resamples a DataFrame 'df' with a DateTime index and columns 'A', 'B','C','D' to a lower frequency ('30T' or 30 minutes), selects the maximum value in each sampling period, and computes an axponentially weighted moving average with half-life of 5 periods.
# just give the correct syntax resample, mean, max, rolling, 
# df.resample('30T').max().ewm(halflife=5).mean()

# reate a new Dataframe  df2 containing the 90th percentile of the rolling window of size 3for each column of the original dataframe df.
# just give the correct syntax using rolling quentile, percentile.
# df2 = df.rolling(window=3).quantile(0.9)


# df has a DateTime index & columns A. B C D. you have a specific Datetime t in mind and you want to find the index in dataframe that is closest to the time t. wheather it is before or after . 
# just give the syntax using index get_lock
# closest_index = df.index.get_loc(t, method='nearest')



# df that contains coluimns Date with dates in the format 'YYYY-MM-DD'. you want to create two new columns year & month by extracting the year & month from the date  column. however date coluumn is of object type & needs to be converted to datetome first. 
# just give the syntax using to_datetime, dt.year, datetimeindex

# df['Date'] = pd.to_datetime(df['Date'])
# df['year'] = df['Date'].dt.year
# df['month'] = df['Date'].dt.month



# convert date column in the dataframe df from string format to pandas datetime format
