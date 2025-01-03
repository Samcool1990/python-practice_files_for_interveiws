# Question: Create a API in Fastapi which will fetch all the records from the table & show it to UI.
# What steps you will take to optimize it & the records are in millions in size.
# Answer:
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

# Example Models
from models import YourTable  # Your SQLAlchemy ORM model

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

app = FastAPI()

# Async Database Engine and Session
engine = create_async_engine(DATABASE_URL, echo=False)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Pydantic Response Model
class RecordResponse(BaseModel):
    id: int
    name: str
    value: Optional[str]  # Example fields

    class Config:
        orm_mode = True


@app.get("/records", response_model=List[RecordResponse])
async def fetch_records(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    search: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: Optional[str] = Query("asc", regex="^(asc|desc)$"),
):
    """
    Fetch paginated, filterable, and sortable records.
    """
    async with async_session() as session:
        query = select(YourTable)

        # Add filtering
        if search:
            query = query.where(YourTable.name.ilike(f"%{search}%"))

        # Add sorting
        if sort_by:
            sort_column = getattr(YourTable, sort_by, None)
            if not sort_column:
                raise HTTPException(status_code=400, detail="Invalid sort field")
            query = query.order_by(
                sort_column.asc() if sort_order == "asc" else sort_column.desc()
            )

        # Apply pagination
        query = query.offset((page - 1) * size).limit(size)

        results = await session.execute(query)
        records = results.scalars().all()

    return records


# Question: Create a fastapi project structure
# Answer:
# fastapi_project/
# │
# ├── app/
# │   ├── __init__.py
# │   ├── main.py                 # Entry point of the application
# │   ├── core/                   # Core configurations and utilities
# │   │   ├── __init__.py
# │   │   ├── config.py           # Configuration settings
# │   │   ├── database.py         # Database connection setup
# │   │   ├── security.py         # Authentication and security logic
# │   ├── models/                 # Database models (SQLAlchemy)
# │   │   ├── __init__.py
# │   │   ├── user.py             # Example model
# │   │   ├── base.py             # Base class for ORM models
# │   ├── schemas/                # Pydantic models for request/response validation
# │   │   ├── __init__.py
# │   │   ├── user.py             # Example schema
# │   ├── api/                    # API routes and logic
# │   │   ├── __init__.py
# │   │   ├── v1/                 # Version 1 of the API
# │   │       ├── __init__.py
# │   │       ├── routes/
# │   │           ├── __init__.py
# │   │           ├── user.py     # User-specific API routes
# │   ├── services/               # Business logic for the application
# │   │   ├── __init__.py
# │   │   ├── user_service.py     # Example service logic
# │   ├── utils/                  # Helper functions
# │   │   ├── __init__.py
# │   │   ├── common.py           # Common utility functions
# │   ├── tests/                  # Test cases
# │       ├── __init__.py
# │       ├── test_main.py        # Tests for main app
# │       ├── test_user.py        # Tests for user routes/services
# │
# ├── requirements.txt            # Python dependencies
# ├── .env                        # Environment variables
# ├── alembic/                    # Database migrations (if using Alembic)
# │   ├── env.py
# │   ├── versions/
# │
# ├── README.md                   # Project documentation
# ├── Dockerfile                  # Docker configuration
# ├── docker-compose.yml          # Docker Compose configuration
# └── pyproject.toml              # Python project metadata (e.g., for Poetry)


# Question: lets say there are changes in your database or any schema changes happen. how will you migrate
# your database ??
# Answer:
# To manage and apply database schema changes or migrations effectively in a FastAPI project, you
# typically use Alembic or a similar migration tool. Alembic is well-suited for projects using
# SQLAlchemy and integrates seamlessly with both traditional and asynchronous database setups.

# Steps to Migrate the Database
# 1. Install Alembic
# First, install Alembic using pip:

# bash
# Copy code
# pip install alembic
# 2. Initialize Alembic
# Run the following command to set up Alembic in your project:

# bash
# Copy code
# alembic init alembic
# This will create an alembic directory with the following structure:

# bash
# Copy code
# alembic/
# ├── env.py                # Main configuration file
# ├── versions/             # Stores migration scripts
# ├── README
# ├── script.py.mako
# alembic.ini               # Alembic configuration file
# 3. Configure Alembic
# Edit alembic.ini: Update the sqlalchemy.url field with your database connection URL. For example:

# ini
# Copy code
# sqlalchemy.url = postgresql+asyncpg://user:password@localhost/dbname
# Alternatively, you can load the URL dynamically from your FastAPI config.py by editing env.py.

# Modify env.py: Replace the default configuration with the one used in your FastAPI project.
# Here's an example for asynchronous databases:

# python
# Copy code
# from sqlalchemy import engine_from_config, pool
# from sqlalchemy.ext.asyncio import AsyncEngine
# from alembic import context
# from app.models.base import Base  # Import your SQLAlchemy Base
# from app.core.config import settings

# # Retrieve database URL from your settings
# config = context.config
# config.set_main_option('sqlalchemy.url', settings.DATABASE_URL)

# target_metadata = Base.metadata

# def run_migrations_offline():
#     """Run migrations in 'offline' mode."""
#     context.configure(
#         url=settings.DATABASE_URL,
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )
#     with context.begin_transaction():
#         context.run_migrations()

# async def run_migrations_online():
#     """Run migrations in 'online' mode."""
#     connectable = AsyncEngine(
#         engine_from_config(
#             config.get_section(config.config_ini_section),
#             prefix="sqlalchemy.",
#             poolclass=pool.NullPool,
#             future=True,
#         )
#     )
#     async with connectable.connect() as connection:
#         await connection.run_sync(
#             lambda conn: context.configure(
#                 connection=conn,
#                 target_metadata=target_metadata
#             )
#         )
#         await connection.run_sync(context.run_migrations)

# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     import asyncio
#     asyncio.run(run_migrations_online())
# 4. Generate a Migration Script
# Once you've updated your SQLAlchemy models or made schema changes:

# Run the following command to generate a new migration:

# bash
# Copy code
# alembic revision --autogenerate -m "Describe your change"
# This will create a new file in the alembic/versions/ directory. The file contains the changes Alembic detected in your SQLAlchemy models.

# 5. Review and Modify Migration Script
# Open the generated file in the alembic/versions/ directory. It will contain upgrade() and downgrade() functions, which define how to apply and roll back the changes.

# Verify that the script aligns with your intended changes. For example:

# python
# Copy code
# from alembic import op
# import sqlalchemy as sa

# # Revision identifiers, used by Alembic.
# revision = 'abcdef123456'
# down_revision = '123456abcdef'
# branch_labels = None
# depends_on = None

# def upgrade():
#     op.add_column('users', sa.Column('age', sa.Integer, nullable=True))

# def downgrade():
#     op.drop_column('users', 'age')
# 6. Apply the Migration
# Run the migration to update the database schema:

# bash
# Copy code
# alembic upgrade head
# This applies all unapplied migrations to bring the database schema to the latest state.

# 7. Roll Back Changes (if needed)
# If an error occurs or you need to revert changes, roll back the migration:

# bash
# Copy code
# alembic downgrade <revision_id>
# Replace <revision_id> with the target revision you want to revert to (e.g., 123456abcdef).

# 8. Automate Migration in CI/CD
# Integrate Alembic migrations into your CI/CD pipeline:

# Add a step in your deployment process to run migrations:
# bash
# Copy code
# alembic upgrade head
# Ensure that the migration runs before starting the application in production.
# Tips for Managing Migrations
# Test Locally:

# Always test your migrations on a local or staging database before applying them to production.
# Handle Downtime:

# For schema changes that may cause downtime (e.g., dropping columns), consider:
# Using a blue-green deployment strategy.
# Applying changes in stages (e.g., first add a column, migrate data, then drop the old column).
# Data Migrations:

# If you need to migrate data (e.g., populate a new column), handle it in the migration script or a separate job.
# Version Control:

# Commit migration files (alembic/versions/) to your repository to maintain a record of schema changes.
# With Alembic integrated into your FastAPI project, you'll have a robust way to manage database schema changes efficiently.









# Question: draw back of indexes in database table ?
# Answer:
# Indexes in a database table are essential for improving query performance, but they come with certain 
# drawbacks. Here are the key disadvantages:

# 1. Increased Storage Space
# Drawback: Indexes consume additional disk space because the database must store the index data alongside the 
# table data. Impact: For large datasets with many indexes, this can significantly increase storage 
# requirements.

# 2. Slower Write Operations
# Drawback: Operations like INSERT, UPDATE, and DELETE take longer because the database must update the indexes every time the data changes.
# Impact:
# In high write-intensive applications, excessive indexing can degrade performance.
# The more indexes a table has, the greater the overhead for maintaining them.

# 3. Maintenance Overhead
# Drawback: Indexes require regular maintenance to stay effective, especially for dynamic tables with frequent updates.
# Impact:
# Fragmentation: Indexes can become fragmented over time, leading to performance degradation.
# Rebuilding or reorganizing indexes is resource-intensive.

# 4. Overhead During Query Execution
# Drawback: Not all queries benefit from indexes. For small tables or queries that return a large portion of the data, using an index can be slower than a full table scan.
# Impact:
# Misused or unnecessary indexes can lead to query plan inefficiencies.
# Queries that involve complex conditions may not leverage existing indexes effectively.

# 5. Risk of Incorrect Index Usage
# Drawback: If the database query planner chooses a suboptimal index or the query doesn’t match the index structure, performance can degrade.
# Impact:
# Requires careful monitoring and fine-tuning of indexes.
# Multi-column indexes must align with the query’s column order for optimal performance.

# 6. Complexity in Index Management
# Drawback: Managing indexes in large systems can become complex, especially with:
# Composite indexes (multi-column).
# Partitioned tables with multiple indexes.
# Impact:
# Mismanagement can lead to redundant or unused indexes.
# Developers and DBAs need to regularly evaluate index usage.

# 7. Potential Locking Issues
# Drawback: Index updates can cause locking conflicts in concurrent environments.
# Impact:
# Increases the likelihood of deadlocks or lock contention during high concurrency.

# 8. Overhead During Bulk Operations
# Drawback: Bulk data operations (e.g., mass inserts or updates) are slower when indexes are present.
# Impact:
# Indexes must be updated for every inserted or modified row, significantly slowing down the process.

# 9. Limitations in Certain Scenarios
# Drawback: Indexes are less effective for:
# Queries with high cardinality (returning many rows).
# Columns with frequently changing values.
# Columns with low cardinality (e.g., boolean or enum types).
# Impact: The performance boost may not justify the overhead.

# 10. Cost of Creation and Initialization
# Drawback: Creating an index on a large table can be time-consuming and resource-intensive.
# Impact:
# During index creation, other database operations can slow down or be blocked, causing downtime in some systems.
# When to Use Indexes
# To minimize the drawbacks, consider using indexes only when:

# The indexed columns are frequently used in WHERE, JOIN, ORDER BY, or GROUP BY clauses.
# The benefit in read performance outweighs the overhead in write operations.
# There is sufficient disk space to accommodate the index structure.
# Best Practices to Mitigate Drawbacks
# Limit the Number of Indexes:
# Avoid creating indexes on columns that are rarely queried or updated frequently.
# Use Composite Indexes Wisely:
# Combine multiple columns into one index only when necessary.
# Monitor and Tune Regularly:
# Use database performance tools to identify unused or ineffective indexes.
# Defer Index Creation:
# Create indexes after bulk inserts to avoid unnecessary overhead during the operation.
# Indexes are powerful but must be used judiciously to balance the trade-offs between read and write performance.



# Question: create a decorator where you pass argument in the decorator ? In depth concept of advance
# decorator. create advance level decorator.
# Answer:
# Concept of Advanced Decorators in Python
# Decorators in Python allow you to modify the behavior of a function or a class. Advanced
# decorators can take arguments themselves and even handle complex logic. Here's an in-depth
# explanation followed by the creation of an advanced-level decorator.

# Key Concepts of Advanced Decorators
# Basic Decorators:

# A function that takes another function as input and returns a new function.
# python
#
def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

# Decorators with Arguments:
# To pass arguments to a decorator, you add an additional layer of functions:
# python
# 
def decorator_with_args(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator argument: {arg}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Preserving Metadata:
# Use functools.wraps to preserve the original function's metadata.
# python
# 
from functools import wraps
# Chaining Decorators:

# Multiple decorators can be applied to a function.
# Class-Based Decorators:

# Decorators implemented as classes for more control and state management.
# Example of a Decorator with Arguments
# Below is an advanced decorator that Accepts arguments & Preserves metadata.

# Logs execution time of the function.
# Code Example: Advanced Decorator
# python
# 
import time
from functools import wraps

def log_execution_time(log_prefix="Execution Time"):
    """Advanced decorator to log execution time of a function."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{log_prefix}: Starting execution of '{func.__name__}'")
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{log_prefix}: '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
            return result
        return wrapper
    return decorator

# Applying the decorator with arguments
@log_execution_time(log_prefix="DEBUG")
def calculate_sum(n):
    """Calculate the sum of the first 'n' integers."""
    return sum(range(1, n + 1))

# Testing the function
print(calculate_sum(1000000))
# Explanation
# log_execution_time(log_prefix="Execution Time"):

# A decorator that accepts an argument log_prefix.
# It adds an additional layer to wrap the function with custom behavior.
# @wraps(func):

# Ensures the decorated function retains its name, docstring, and other metadata.
# Performance Logging:

# Measures the execution time of the decorated function.
# Reusable:

# The decorator can be reused with different arguments.
# Class-Based Advanced Decorator
# A class-based decorator is useful when you need state or logic that spans multiple calls.

# Code Example: Class-Based Decorator
# python
# 
class CountCalls:
    """A decorator class to count the number of times a function is called."""
    def __init__(self, func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"Call {self.call_count} to '{self.func.__name__}'")
        return self.func(*args, **kwargs)

# Applying the class-based decorator
@CountCalls
def greet(name):
    """Greets the user."""
    print(f"Hello, {name}!")

# Testing the function
greet("Alice")
greet("Bob")
# Chaining Multiple Advanced Decorators
# Decorators can be chained to combine functionality. The order matters because the decorators wrap functions in the order they are applied.

# python
# 
@log_execution_time("PERFORMANCE")
@CountCalls
def factorial(n):
    """Calculate factorial of 'n'."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Testing the chained decorators
print(factorial(5))
# Summary
# Advanced decorators:

# Allow arguments for customization.
# Use multiple layers of functions.
# Preserve metadata using functools.wraps.
# Can be implemented as classes for more control.
# Are composable, enabling multiple behaviors on a single function.
# These techniques allow you to create modular, reusable, and powerful enhancements to Python functions and methods.


# Question: Type of arguments in python & explain everything
# Answer:
# In Python, function arguments can be categorized into five types, based on how they are passed and used:

# 1. Positional Arguments
# The most common type of argument.
# Passed in the order they are defined in the function.
# Example:
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 30)  # Output: Hello, Alice! You are 30 years old.


# 2. Keyword Arguments
# Arguments are passed by explicitly naming the parameter.
# Order does not matter when using keyword arguments.
# Example:
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(age=30, name="Alice")  # Output: Hello, Alice! You are 30 years old.


# 3. Default Arguments
# Parameters that have default values if no value is passed.
# Must be declared after non-default arguments.
# Example:

def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice")        # Output: Hello, Alice! You are 25 years old.
greet("Bob", 30)      # Output: Hello, Bob! You are 30 years old.


# 4. Variable-length Arguments
# Allows functions to accept arbitrary numbers of arguments.
# (a) *args: Non-keyword variable-length arguments.
# Collects extra positional arguments as a tuple.
# Example
def add_numbers(*args):
    print(sum(args))

add_numbers(1, 2, 3)   # Output: 6
add_numbers(4, 5)      # Output: 9
# (b) **kwargs: Keyword variable-length arguments.
# Collects extra keyword arguments as a dictionary.
# Example
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30)  
# Output:
# name: Alice
# age: 30


# 5. Positional-only and Keyword-only Arguments
# Introduced in Python 3.8 with the use of / and *.
# (a) Positional-only Arguments (/):
# Arguments before / must be positional.
# Example:
def add(a, b, /, c):
    return a + b + c

print(add(1, 2, 3))   # Output: 6
# add(a=1, b=2, c=3)  # Raises TypeError
# (b) Keyword-only Arguments (*):
# Arguments after * must be passed as keywords.
# Example:
def greet(*, name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(name="Alice", age=30)  # Output: Hello, Alice! You are 30 years old.
# greet("Alice", 30)         # Raises TypeError



# Question: query to partition in sql & first 3 letter of name in sql
# Answer:
# 1. Query for Partitioning in SQL
# Definition:
# Partitioning is a way to group rows and apply aggregate functions or window functions over those
# groups without collapsing them into a single result. It’s commonly used with the OVER() clause.

# Query Example:
# Suppose you have a sales table with columns id, region, and amount, and you want to calculate the
# total sales for each region using partitioning.

# sql
# Copy code
# SELECT
#     id,
#     region,
#     amount,
#     SUM(amount) OVER (PARTITION BY region) AS total_sales_by_region
# FROM
#     sales;
# Explanation:
# PARTITION BY region: Groups rows by the region column.
# SUM(amount): Calculates the total for each group (region).
# The result includes all rows, with the aggregate total added as a new column.
# 2. Query to Extract the First 3 Letters of a Name
# Query Example:
# Suppose you have a users table with a name column and want to get the first three letters of each
# name.

# sql
# Copy code
# SELECT
#     id,
#     name,
#     SUBSTRING(name, 1, 3) AS first_three_letters
# FROM
#     users;
# Explanation:
# SUBSTRING(name, 1, 3): Extracts 3 characters starting from position 1.
# Alternative for MySQL:
# MySQL also supports the LEFT() function:

# sql
# Copy code
# SELECT
#     id,
#     name,
#     LEFT(name, 3) AS first_three_letters
# FROM
#     users;
# Combining Both Queries
# You can combine both queries to partition data and also extract the first three letters of a name.

# Example:
# sql
# Copy code
# SELECT
#     id,
#     region,
#     name,
#     LEFT(name, 3) AS first_three_letters,
#     SUM(amount) OVER (PARTITION BY region) AS total_sales_by_region
# FROM
#     sales;
# Key Notes:
# Partitioning works with window functions like SUM(), AVG(), ROW_NUMBER(), etc.
# Use SUBSTRING or LEFT for extracting parts of strings depending on your database.
# Let me know if you need further assistance!




# Question: Have you worked in any kind of scheduler in AWS ??
# Answer:
# Yes, I can guide you on implementing and using schedulers in AWS. Scheduling in AWS is typically
# achieved using various services depending on the requirement. Below is a breakdown of common use
# cases and corresponding AWS services used for scheduling:

# 1. AWS EventBridge (formerly CloudWatch Events)
# What it is:
# A serverless event bus that allows you to schedule tasks or trigger events based on time or other
# criteria.Supports cron expressions or rate-based scheduling.
# Use Cases:
# Run Lambda functions or start EC2/RDS instances on a schedule.
# Trigger pipelines or batch jobs at specific intervals.
# How to Use:

# Define a Rule:
# Specify the schedule using cron or rate expressions.
# Example: cron(0 12 * * ? *) for 12 PM UTC daily.
# Set a Target:
# Choose the service to trigger (e.g., Lambda, Step Functions, SNS, SQS).
# Deploy.
# Example: Trigger a Lambda Function Every Hour
# json
# Copy code
# {
#     "ScheduleExpression": "rate(1 hour)",
#     "State": "ENABLED",
#     "Targets": [
#         {
#             "Arn": "arn:aws:lambda:us-east-1:123456789012:function:my-function",
#             "Id": "Target1"
#         }
#     ]
# }


# 2. AWS Lambda Scheduled Functions
# What it is:
# Lambda functions triggered by an EventBridge schedule.
# No infrastructure management is required.
# Use Cases:
# Clean up resources like S3 buckets or DynamoDB tables.
# Perform periodic health checks or data aggregation tasks.
# How to Use:
# Create a rule in EventBridge and set Lambda as the target.
# Write your business logic in the Lambda function.
# Example:
# python
# Copy code
# import boto3

# def lambda_handler(event, context):
#     print("Scheduled Lambda executed!")
#     # Add your logic here



# 3. AWS Batch
# What it is:
# A service to run batch jobs at scale, with scheduling capabilities through EventBridge.
# Use Cases:
# Run data processing or machine learning jobs periodically.
# How to Use:
# Define a compute environment and job queue.
# Use EventBridge to submit jobs at specified times.
# Specify job parameters and environment variables.


# 4. AWS Step Functions
# What it is:
# A serverless orchestration service that can schedule tasks as part of state machine workflows.
# Use Cases:
# Schedule long-running workflows.
# Coordinate multiple Lambda functions or services.
# How to Use:
# Use an EventBridge rule to start the Step Functions state machine on a schedule.


# 5. Amazon RDS Maintenance Windows
# What it is:
# Scheduling for database maintenance tasks like backups or updates.
# Use Cases:
# Perform maintenance during off-peak hours.
# How to Use:
# Configure the maintenance window during database setup or via the AWS Management Console.


# 6. AWS Glue Workflows
# What it is:
# Used for ETL (Extract, Transform, Load) processes with scheduling capabilities.
# Use Cases:
# Schedule data pipeline workflows.
# How to Use:
# Define an AWS Glue workflow and trigger it with an EventBridge rule.


# 7. Custom EC2 Cron Jobs
# What it is:
# Use cron jobs in an EC2 instance for highly custom or specialized scheduling needs.
# Use Cases:
# Schedule tasks that cannot be easily handled by serverless solutions.
# How to Use:
# Install a cron scheduler (e.g., crontab) on the instance and define the tasks.
# Example crontab entry:
# bash
# Copy code
# 0 0 * * * /usr/bin/python3 /path/to/script.py


# 8. AWS CodePipeline
# What it is:
# A CI/CD service with scheduling capabilities.
# Use Cases:
# Schedule builds, tests, or deployments.
# How to Use:
# Use EventBridge to trigger a pipeline execution.



# Comparison of AWS Scheduling Services
# Service	Use Case	Cost	Scalability	Ease of Use
# EventBridge	General-purpose scheduling	Low	High	High
# Lambda	Lightweight periodic tasks	Pay-per-use	High	Very High
# AWS Batch	Compute-intensive batch jobs	Based on job runtime	Very High	Medium
# Step Functions	Complex workflows	Based on state transitions	High	Medium
# RDS Maintenance	Database maintenance	Free	N/A	Very High
# Glue Workflows	ETL pipelines	Based on processing	High	Medium
# EC2 Cron Jobs	Fully custom tasks	EC2 instance cost	Medium	Low
# Best Practices for Scheduling in AWS
# Use Serverless Options: Prefer EventBridge and Lambda for lightweight tasks to reduce costs and infrastructure overhead.
# Leverage IAM Roles: Ensure proper permissions for the services interacting with scheduled tasks.
# Monitor with CloudWatch: Track execution metrics and set alarms for failures.
# Optimize Costs: Use Spot Instances for batch jobs and control runtimes.
# Testing: Test schedules in non-production environments to avoid unexpected behavior.
# Let me know if you need help with implementation or specific AWS scheduler use cases!



# Question:In a class you have __init__ & a global object.How can you access the global object. DO you need 
# the self keyword.
# 
#Answer: In a Python class, you can access a global object from within the class methods, including the 
# __init__ method, without needing the self keyword. The self keyword is used to refer to instance variables 
# or methods specific to the instance of the class. However, for global objects (those declared outside the 
# class), you can access them directly by their name without using self.

# Here's an example to clarify the concept:

# Example:
# python
# Copy code
# # Global object
global_obj = "I am a global object"

class MyClass:
    def __init__(self):
        # Accessing the global object in the constructor (without 'self')
        print(global_obj)

    def some_method(self):
        # Accessing the global object in another method (without 'self')
        print(global_obj)

# # Create an instance of the class
obj = MyClass()  # This will print the global object
obj.some_method()  # This will print the global object again
# Key Points:
# Global object access: You access a global object directly by its name (e.g., global_obj), without needing 
# to use self. Self keyword: The self keyword is used for accessing instance variables or methods, but it is
#  not required for accessing global variables. If you want to modify the global object inside a class, you 
# can use the global keyword inside the method to indicate that you're working with the global variable, 
# rather than creating a local one.

# Example of modifying the global object:
# python
# Copy code
global_obj = "Initial value"

class MyClass:
    def __init__(self):
        global global_obj  # Declare that we are referring to the global variable
        global_obj = "Modified by class"
        
    def print_global(self):
        print(global_obj)

# # Create an instance
obj = MyClass()
obj.print_global()  # This will print "Modified by class"
# In this case, the global keyword is needed to modify the global object from inside the method.

# To summarize:

# You do not need self to access a global object inside a class.
# The self keyword is used to refer to instance variables and methods.



# Question: How would you create authorization in application. First tell how many types of authorization & 
# Authentication are there & then how would you implement each of them with code example.
# In application security, authentication and authorization are two crucial concepts that ensure only authorized users can access specific resources. Authentication verifies the identity of users, while authorization determines whether they can perform specific actions or access resources. Let’s break down the types of authentication and authorization, and how you can implement them.

# Types of Authentication
# Authentication is about verifying the identity of a user. Here are the common types:

# Password-based Authentication:
# The user proves their identity by providing a username and password.

# Multi-factor Authentication (MFA):
# An enhanced version of password authentication where users must provide two or more verification factors 
# (e.g., a password and a code sent to their phone).

# Token-based Authentication (JWT, OAuth):
# The user logs in once, and a token (usually a JSON Web Token - JWT) is generated for subsequent requests 
# to prove their identity.

# OAuth/OpenID Connect:
# A protocol for token-based authentication that enables third-party authentication without exposing 
# passwords.

# Biometric Authentication:
# Authentication based on unique biological traits like fingerprints, facial recognition, or iris scanning.

# Certificate-based Authentication:
# The user proves their identity with a digital certificate, which is commonly used for secure communications.
# Types of Authorization
# Authorization refers to the process of granting or denying access to resources based on the authenticated 

# identity. Here are common types of authorization:
# Role-Based Access Control (RBAC):
# Access to resources is granted based on user roles (e.g., Admin, User).
# Attribute-Based Access Control (ABAC):

# Access is based on attributes of the user (e.g., department, location).
# Discretionary Access Control (DAC):

# The owner of a resource decides who can access it and with what permissions.
# Mandatory Access Control (MAC):

# A system-enforced access control where users cannot modify access controls; access is determined by system 
# policies.
# Implementation of Authentication and Authorization


# 1. Password-based Authentication (Example using Flask)
# Let's implement Password-based Authentication using Flask.
# python
# Copy code
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Dummy user data (in real applications, use a database)
users_db = {
    "user1": generate_password_hash("password123"),
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users_db and check_password_hash(users_db[username], password):
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
# Login process: A POST request with a username and password is checked against a stored hash (password is hashed for security).



# 2. JWT Token-based Authentication
# Let's implement JWT Authentication.
# python
# Copy code
import jwt
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
SECRET_KEY = 'your_secret_key'

# Dummy user data
users_db = {
    "user1": "password123"
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users_db and users_db[username] == password:
        payload = {'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({"token": token}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Token is missing!"}), 403

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({"message": f"Hello, {payload['username']}!"}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired!"}), 403
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token!"}), 403

if __name__ == '__main__':
    app.run(debug=True)
# Login process: After successful authentication, a JWT token is issued. The /protected endpoint checks if the user provides a valid token.



# 3. Role-Based Access Control (RBAC) with Flask
# Here’s an implementation of Role-Based Authorization using Flask.
# python
# Copy code
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data with roles
users_db = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

def check_role(required_role):
    def wrapper(func):
        def inner(*args, **kwargs):
            username = request.json.get('username')
            password = request.json.get('password')

            if username in users_db and users_db[username]["password"] == password:
                if users_db[username]["role"] == required_role:
                    return func(*args, **kwargs)
                else:
                    return jsonify({"message": "Access denied, insufficient permissions!"}), 403
            else:
                return jsonify({"message": "Invalid credentials!"}), 401
        return inner
    return wrapper

@app.route('/admin', methods=['POST'])
@check_role('admin')
def admin():
    return jsonify({"message": "Welcome, Admin!"}), 200

@app.route('/user', methods=['POST'])
@check_role('user')
def user():
    return jsonify({"message": "Welcome, User!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
# RBAC Authorization: Users are assigned roles (admin, user). Only users with the appropriate role can access the protected routes.




# 4. Multi-factor Authentication (MFA) with Flask
# Implementing Multi-factor Authentication can involve sending a code (like an OTP) to the user’s phone or email.
# python
# Copy code
import random
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data
users_db = {
    "user1": {"password": "password123", "otp": None, "otp_expiry": None}
}

def send_otp():
    otp = random.randint(100000, 999999)
    return otp

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users_db and users_db[username]["password"] == password:
        otp = send_otp()
        users_db[username]["otp"] = otp
        users_db[username]["otp_expiry"] = time.time() + 300  # OTP expires in 5 minutes
        return jsonify({"message": "OTP sent to your phone", "otp": otp}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    username = request.json.get('username')
    otp = request.json.get('otp')

    if username in users_db and users_db[username]["otp"] == otp:
        if time.time() > users_db[username]["otp_expiry"]:
            return jsonify({"message": "OTP expired!"}), 400
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid OTP!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
# MFA Implementation: First, the user logs in with their credentials. If correct, an OTP is sent (here simulated) and must be verified.
# Summary
# Authentication: Verifies the identity of a user. We implemented password-based, JWT, and multi-factor authentication.
# Authorization: Grants or denies access to resources. We demonstrated role-based access control (RBAC) for different user roles.
# Each type has its strengths depending on the application's security requirements, and combining them (e.g., using both JWT and role-based access control) is common for enhanced security.



# Question: In Python what is class method, static method & abstract method. explain it like it was asked in 
# interview with reallife example.

#Answer:
# In Python, class methods, static methods, and abstract methods are all different types of methods that 
# serve unique purposes within a class. Here’s an explanation of each with real-life examples:

# 1. Class Method
# What it is:
# A class method is a method that is bound to the class rather than the instance. It can modify the class 
# state that applies across all instances of the class. Class methods take cls as the first parameter, which 
# refers to the class itself.

# Real-life Example:
# Imagine a Bank class where you want to keep track of the total balance across all customers (class-level 
# attribute). A class method can be used to calculate the total balance or perform operations affecting all 
# customers.

# Example Code:

class Bank:
    total_balance = 0  # Class-level attribute
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Bank.total_balance += balance  # Update total balance

    @classmethod
    def show_total_balance(cls):
        print(f"Total balance across all customers: {cls.total_balance}")

# Creating instances of Bank
customer1 = Bank("Alice", 1000)
customer2 = Bank("Bob", 1500)

# Calling class method
Bank.show_total_balance()  # Output: Total balance across all customers: 2500
# Key Points:
# @classmethod decorator is used.
# cls is used to refer to the class itself (not an instance).
# Can be used to modify class-level attributes.

# 2. Static Method
# What it is:
# A static method is a method that doesn't take a reference to the instance or class as its first parameter. 
# It behaves like a regular function that belongs to a class, but it doesn't need to access or modify the 
# class or instance data. Static methods are defined with the @staticmethod decorator.

# Real-life Example:
# Consider a Calculator class. If you want to implement basic operations like addition, subtraction, 
# multiplication, etc., they don't need access to the instance of the calculator, and they can be static 
# methods because they operate independently of any object state.


# Example Code:
class Calculator:
    
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Calling static methods without creating an instance
result1 = Calculator.add(5, 3)  # Output: 8
result2 = Calculator.multiply(4, 6)  # Output: 24

print(result1)
print(result2)
# Key Points:
# @staticmethod decorator is used.
# No reference to self or cls is needed.
# Works like a regular function, but logically grouped within the class.

# 3. Abstract Method
# What it is:
# An abstract method is a method that is declared in an abstract class (a class that cannot be instantiated) 
# and must be implemented by any subclass of that abstract class. Abstract methods define a blueprint for 
# the subclasses, but the actual implementation is left to the subclasses.

# Real-life Example:
# Think of an Employee class, where you have different types of employees, such as FullTimeEmployee and 
# PartTimeEmployee. You can define an abstract method calculate_salary() in the Employee class, but the 
# actual salary calculation will differ for full-time and part-time employees. Each subclass must implement 
# this method.

# Example Code:
from abc import ABC, abstractmethod

# Abstract class
class Employee(ABC):
    
    @abstractmethod
    def calculate_salary(self):
        pass

# Subclass for FullTimeEmployee
class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def calculate_salary(self):
        return self.salary  # For full-time, just return salary

# Subclass for PartTimeEmployee
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked  # For part-time, calculate by hours worked

# Trying to create an instance of the abstract class (Employee) will raise an error
# emp = Employee("John")  # This will raise TypeError: Can't instantiate abstract class

# Correct usage with subclasses
full_time_emp = FullTimeEmployee("Alice", 5000)
part_time_emp = PartTimeEmployee("Bob", 20, 80)

print(f"Full-time salary: {full_time_emp.calculate_salary()}")
print(f"Part-time salary: {part_time_emp.calculate_salary()}")
# Key Points:
# @abstractmethod decorator is used to define abstract methods.
# The abstract class cannot be instantiated directly.
# Any subclass must provide an implementation for the abstract methods.
# Summary:
# Class Method (@classmethod): A method that operates on the class itself and can modify class-level 
# attributes. It takes cls as the first argument.
# Example: A method to track the total balance across all customers in a Bank class.

# Static Method (@staticmethod): A method that doesn’t operate on class or instance-level attributes and 
# doesn't require access to self or cls. It's like a regular function but belongs to the class.
# Example: Simple mathematical operations in a Calculator class.

# Abstract Method (@abstractmethod): A method in an abstract class that must be implemented by any subclass. 
# It is used when you have a general blueprint, but the specific implementation is left to the subclasses.
# Example: Calculating salaries for different types of employees in an Employee class.
# In an interview, you might also be asked to show how to apply these methods in real-world scenarios, so be 
# ready with examples like the ones above, where these concepts are applied in practical situations.