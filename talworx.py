# 1.
sequence = [2,0.5,7,"21" "x100", 100,"001x" ]
print(sequence[3:-2][0])
# 21x100

# 2.
def alert(*args, **kwargs):
    print(*args[0],kwargs.values()[0])
    
    
alert("Hellow world", msg = 123)
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
import time
from multiprocessing.pool import Pool

def task():
    time.sleep(1)

pool = Pool()
pool.apply_async(task)
pool.apply_async(task)

pool.join()
pool.terminate()

print("all tasks are completed")

# Answer:3

sequence = [2, -100,0.0, 9.2, 1., 5, -.0, 12 ]
print([num for num in sequence if type(num) == int])


import unittest
list1 = [1,2,3]

# class TestLists(unittest.TestCase):
#      def test_is_unique(self):
           #assert that the list in unique here

# unittest.main()

# import unittest

# list1 = [1, 2, 3]

class TestLists(unittest.TestCase):
    def test_is_unique(self):
        # Check if the list has unique elements
        self.assertEqual(len(list1), len(set(list1)), "The list contains duplicate elements")

if __name__ == "__main__":
    unittest.main()





class Dog:
    def __init__(self, name):
        __name__ = name
        
    def name(self):
        return __name__
        
dogobj = Dog("Scooby")
print(dogobj.name())
# __main__




# How would you create a context manager generator for a mysql database ?
import mysql.connector
from contextlib import contextmanager

@contextmanager
def database_connection(db):
    conn = mysql.connector.connect(user='username', password='password', database=db)
    try:
        yield conn
    finally:
        conn.close()



cmd = '$ cd ../home'.split()
match cmd:
    case '$', _,_,'../home':
        print('case1')
        
    case _,'cd',*dir:
        print('case2')
    case '$ cd', *dir:
        print('case3')
    case _:
        print('case4')
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
