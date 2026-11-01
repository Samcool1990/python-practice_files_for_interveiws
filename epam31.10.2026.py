# metaclasses in python
# Answer: In Python, a metaclass is a class for a class; it defines how a class behaves and is constructed. 
#         Just as an object is an instance of a class, a class in Python is an instance of a metaclass. By default, 
#         Python uses the built-in type as its default metaclass to construct all classes.       
# 1. Define the metaclass by inheriting from 'type'
class LowercaseAttributesMeta(type):
    def __new__(cls, name, bases, dct):
        # Create a new dictionary with lowercase keys
        lowercase_dct = {}
        for key, value in dct.items():
            # Keep magic methods (like __init__) as they are
            if key.startswith("__") and key.endswith("__"):
                lowercase_dct[key] = value
            else:
                lowercase_dct[key.lower()] = value
        
        # Delegate the actual class creation to the base 'type' class
        return super().__new__(cls, name, bases, lowercase_dct)

# 2. Use the metaclass to create a new class
class User(metaclass=LowercaseAttributesMeta):
    ROLE = "Admin"
    EMAIL = "user@example.com"

    def __init__(self, username):
        self.username = username

# 3. Test the behavior
print(hasattr(User, "ROLE"))   # Output: False
print(hasattr(User, "role"))   # Output: True
print(User.role)               # Output: Admin



from collections import defaultdict
import bisect


class TimeObject:
    def __init__(self):
        # Maps key -> list of (timestamp, value) tuples
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Check if the key already exists in the dictionary
        if key in self.store:
            # Key exists: append the new (timestamp, value) history to the existing list
            self.store[key].append((timestamp, value))
        else:
            # Key does not exist: initialize it with a new list containing this first entry
            self.store[key] = [(timestamp, value)]
        print(f'Dictionary after set: {self.store}')  # Debugging output to show the current state of the dictionary

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        
        # Binary search to find the rightmost timestamp <= requested timestamp
        idx = bisect.bisect_right(values, (timestamp, chr(127)))
        
        if idx == 0:
            return ""  # No value existed at or before this timestamp
        print(f'Dictionary after get: {self.store}')
        return values[idx - 1][1]


# --- Verification & Usage Example ---
timeobj = TimeObject()

# 1. timeobj set foo bar 1
timeobj.set("foo", "bar", 1)

# 2. timeobj set sam car 2
timeobj.set("sam", "car", 2)

# 3. timeobj set foo bar 2
timeobj.set("foo", "bar 2", 2)

# 4. timeobj get foo 1 -> should return "bar"
print(f"get('foo', 1): {timeobj.get('foo', 1)}")  # Output: bar
# Extra checks to verify time-travel properties:
print(f"get('foo', 2): {timeobj.get('foo', 2)}")  # Output: bar 2
print(f"get('sam', 5): {timeobj.get('sam', 5)}")  # Output: car (latest before time 5)
print(f"get('foo', 0): {timeobj.get('foo', 0)}")  # Output: "" (nothing set yet)


# Dependency injection (DI) in FastAPI
# Dependency injection (DI) in FastAPI allows you to declare what your path operations need to run—such as database sessions, 
# security tokens, or configuration settings—without manually creating or managing those resources inside the endpoint.
# FastAPI provides native, first-class support for DI through its Depends() function. Instead of forcing you to write boilerplate 
# code in every route, FastAPI handles the lifecycle, validation, and resolution of these tools automatically.





# Blue/Green and Canary deployments
# Blue/Green and Canary deployments are two popular DevOps strategies used to release new software versions with minimal 
# downtime and lower risk

# Blue/Green Deployments
# • How it works: You run two identical production environments side-by-side (called Blue and Green). Blue serves the current 
#       live version, while Green sits idle or holds the new version.
# • The Switch: Once the new version is deployed and tested on Green, a load balancer or router instantly flips 100% of traffic 
#       from Blue to Green.
# • Rollback: If something breaks, you simply flip the load balancer switch right back to Blue.
# • Pros: Instantaneous cutover, zero downtime, and very fast, reliable rollbacks.
# • Cons: Resource-intensive because you must pay for and maintain two full-scale production environments at the same time.
# • Best used for: Major, critical updates where you are confident in the build stability and want an instant, all-or-nothing 
#       swap.

# Canary Deployments
# • How it works: You roll out the new version to a small subset of users or servers (e.g., 5% of traffic) while 
#   the majority (95%) stays on the old version.
# • The Switch: You monitor real-time telemetry (error rates, response times, logs). If metrics look good, you gradually scale up 
#   the traffic percentage (e.g., 25% -> 50% -> 100%).
# • Rollback: If errors spike, you route the small canary group back to the stable version immediately, limiting the 
#   "blast radius" of the bug.
# • Pros: Lower infrastructure cost (no need for a full duplicate environment), real-world testing with live users, and 
#   very low risk.
# • Cons: Complex routing and monitoring setup; tracking issues that only affect a tiny slice of users can take longer.
# • Best used for: Iterative releases, high-traffic apps, or situations where you want to test live user behavior before a 
#   full rollout.

# Key Comparison
# Feature	                Blue/Green Deployment	                Canary Deployment
# Traffic Split	            100% to Blue, then 100% to Green	    Gradual (e.g., 5% -> 25% -> 100%)
# Infrastructure Cost	    High (2 full environments)	            Medium/Low (fractional rollout)
# Rollback Speed	        Instant (flip the load balancer)	    Fast (shift traffic back)
# Risk / Blast Radius	Affects all users at once if Green fails	Limited to a small group initially










# AWS policy JSON structure
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualStudioCodeExample",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::123456789012:root" },
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-bucket-name",
        "arn:aws:s3:::my-bucket-name/*"
      ],
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        }
      }
    }
  ]
}

# Key Policy Elements:
# The official grammar defined in the AWS IAM JSON Policy Reference splits structural elements into two categories: top-level 
#   elements and statement elements.

# 1. Top-Level Elements
# • Version: Specifies the language rules. Always use "2012-10-17". Older versions (like 2008-10-17) do not support newer 
#   features like policy variables.
# • Statement: The core container. It is a JSON array holding one or more separate permission blocks.


# 2. Statement Blocks (Inside the Statement Array)
# • Sid (Optional): Statement ID. A user-defined string used to label or differentiate individual statements.
# • Effect (Required): Must be either "Allow" or "Deny". By default, access is denied. An explicit Deny always overrides an Allow.
# • Principal (Required ONLY in Resource-Based Policies): Specifies the user, account, role, or service allowed or denied access. 
#   Do not include this element in identity-based policies (attached to IAM users or roles), as the principal is implied.
# • Action / NotAction: The specific AWS API operations being allowed or restricted (e.g., s3:GetObject, ec2:StartInstances). 
#   Wildcards (*) are supported to match multiple API calls. You cannot combine Action and NotAction in the same statement.
# • Resource / NotResource: The targets of the actions specified using Amazon Resource Names (ARNs). You cannot combine 
#   Resource and NotResource in the same statement.
# • Condition (Optional): Defines advanced criteria for when the statement applies. You can control access using global 
#   condition keys (like IP addresses or multi-factor authentication requirements) or service-specific parameters.


# Document Size Limits
# Keep in mind that AWS enforces character limits on policy documents (excluding whitespace):
# • Managed Policies: Maximum of 6,144 characters.
# • Inline Policies: Up to 2,048 characters for users, 5,120 characters for groups, and 10,240 characters for roles.









# Difference between Iam policy S3 Policy and account policy with JSON structure
# The core difference lies in what the policy attaches to (the identity, the resource, or the entire organization/account) 
# and who it affects.

# Here is the breakdown of Identity-Based (IAM) Policies, Resource-Based (S3 Bucket) Policies, and Account-Level 
# (Service Control / SCP) Policies, complete with their distinctive JSON structural differences.


# Core Structural and Behavioral Differences:
# Feature	        1. IAM Policy (Identity-Based)	        2. S3 Policy (Resource-Based)	    3. Account Policy (SCP / Service Control Policy)
# Attached        To	IAM Users, Groups, or Roles.	    Directly to the S3 Bucket itself.	AWS Accounts or Organizational Units (OUs).
# Principal Block	❌ Forbidden. (The principal is implied by whoever the policy is attached to).	Required. (Must explicitly state who gets the permission).	❌ Forbidden. (Applies to all identities inside the targeted account).
# Resource Block	Required. (Specifies which AWS resources the identity can touch).	Required. (Usually the bucket ARN and its objects).	Required. Usually set to "*" to restrict the API globally across the account.
# Behavior	Grants permissions directly to a local identity.	Grants permissions to local or cross-account entities.	Does not grant permissions. It acts as a guardrail, setting the maximum allowed permission limit.


# 1. IAM Policy Structure:
# Attached to a User or Role. It tells AWS: "This specific user can perform these actions on these resources." Notice that it does not contain a Principal key.
# json
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Sid": "IAMAllowS3Access",
#             "Effect": "Allow",
#             "Action": [
#                 "s3:ListBucket",
#                 "s3:GetObject"
#             ],
#             "Resource": [
#                 "arn:aws:s3:::my-company-bucket",
#                 "arn:aws:s3:::my-company-bucket/*"
#             ]
#         }
#     ]
# }


# 2. S3 Bucket Policy Structure:
# Attached directly to the S3 bucket. It tells AWS: "Allow this specific identity (Principal) to perform actions on this bucket." A Principal element is mandatory here to declare who is allowed or denied access.
# json
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Sid": "S3BucketPolicyCrossAccountAllow",
#             "Effect": "Allow",
#             "Principal": {
#                 "AWS": "arn:aws:iam::111122223333:root"
#             },
#             "Action": [
#                 "s3:GetObject",
#                 "s3:PutObject"
#             ],
#             "Resource": "arn:aws:s3:::my-company-bucket/*"
#         }
#     ]
# }


# 3. Account-Level Policy Structure (Service Control Policy / SCP)
# Attached at the AWS Organizations layer to an entire AWS Account. It establishes a hard boundary. Even if an IAM Administrator inside that account writes an IAM policy granting s3:*, this SCP overrides it and blocks it completely across the entire account.
# json
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Sid": "AccountLevelDenyS3Deletions",
#             "Effect": "Deny",
#             "Action": [
#                 "s3:DeleteBucket",
#                 "s3:DeleteObject"
#             ],
#             "Resource": "*"
#         }
#     ]
# }



# How They Interact Together
# 1. The Default is Deny: Everything is blocked by default.
# 2. Account Policy (SCP) Check: AWS checks if the action is filtered out at the account level. If an SCP denies it, it is 
#     permanently blocked (even for the root user).
# 3. IAM & Resource Evaluation: For requests within the same account, a matching Allow in either the IAM Policy or the S3 
#     Bucket Policy will grant access. For cross-account S3 requests, an Allow must exist in both the originating IAM policy and the receiving S3 bucket policy.





# SQL:
# StreakTracker
# user_id   timestamp
# 101	2026-01-01
# 101	2026-01-02
# 101	2026-01-03
# 101	2026-01-04
# 101	2026-01-05
# 101	2026-01-02
# 101	2026-01-06
# 101	2026-01-07

# Write a sql query to find the user id which has more than 3 timestamp and streak start time, streak end time
# example: 101
# user_id  streak_start_time	streak_end_time
# 101 	 2026-01-01  		2026-01-05

# Answer:
# -- create
# CREATE TABLE StreakTracker (
#     user_id INT,
#     timestamp DATE
# );

# -- insert
# INSERT INTO StreakTracker(user_id,timestamp) VALUES (101, '2026-01-01');
# INSERT INTO StreakTracker(user_id,timestamp) VALUES (101, '2026-01-02');
# INSERT INTO StreakTracker(user_id,timestamp) VALUES (101, '2026-01-03');
# INSERT INTO StreakTracker(user_id,timestamp) VALUES (101, '2026-01-04');
# INSERT INTO StreakTracker(user_id,timestamp) VALUES (101, '2026-01-05');
# INSERT INTO StreakTracker(user_id,timestamp) VALUES (102, '2026-01-01');
# INSERT INTO StreakTracker(user_id,timestamp) VALUES (103, '2026-01-01');

# -- fetch 
# WITH DistinctDates AS (
#     -- Remove duplicate dates
#     SELECT DISTINCT
#         user_id,
#         timestamp
#     FROM StreakTracker
# ),
# NumberedDates AS (
#     SELECT
#         user_id,
#         timestamp,
#         ROW_NUMBER() OVER (
#             PARTITION BY user_id
#             ORDER BY timestamp
#         ) AS rn
#     FROM DistinctDates
# ),
# StreakGroups AS (
#     SELECT
#         user_id,
#         timestamp,
#         DATEADD(DAY, -rn, timestamp) AS streak_group
#     FROM NumberedDates
# )
# SELECT
#     user_id,
#     MIN(timestamp) AS streak_start_time,
#     MAX(timestamp) AS streak_end_time,
#     COUNT(*) AS streak_days
# FROM StreakGroups
# GROUP BY
#     user_id,
#     streak_group
# HAVING COUNT(*) > 3
# ORDER BY
#     user_id,
#     streak_start_time;
# GO















# Database Sharding vs Partitioning vs Replication
# Answer: Database sharding, partitioning, and replication are distinct strategies used to scale and optimize database systems, 
#         though they solve very different engineering problems



# Feature	Sharding (Horizontal Partitioning)	Partitioning (Logical/Internal Division)	Replication (Data Copying)
# Primary Purpose	Horizontal write & storage scalability	Query optimization & table maintenance	Read scalability & high availability
# Where Data Lives	Across multiple independent database servers	Within the same single database instance	Copied across multiple identical nodes
# Dataset Size per Node	Split up (each shard holds a subset)	Whole table broken into chunks internally	Full dataset duplicated on every replica
# Query Complexity	High (cross-shard joins require routing)	Medium (contained within one DB)	Low (reads off local replicas)



# 1. Database Replication
# • What it is: Creating and maintaining exact, synchronized copies (replicas) of an entire database. Typically uses a primary node (handling writes) and one or more secondary/read replicas (handling reads).
# • How it works: Write operations go to the primary node and are then streamed or copied asynchronously/synchronously to the replicas.
# • Best used for: Read-heavy applications (e.g., e-commerce product browsing, news sites) and failover/disaster recovery.
# • Trade-offs: Does not scale write operations (all writes still hit the primary) and can suffer from replication lag or eventual consistency.
# • Learn more about architectures on VickyBytes.

# 2. Database Partitioning
# • What it is: Dividing a large table or index into smaller, more manageable pieces inside a single database server.
# • How it works:
# 	• Horizontal partitioning (Range/Hash/List): Splitting rows into separate partitions (e.g., splitting an orders table by year or region).
# 	• Vertical partitioning: Splitting columns (e.g., moving heavy text or binary blobs out of a frequently queried main table).
# • Best used for: Optimizing query performance, speeding up scans, and managing massive single-node tables (like time-series logs).
# • Trade-offs: Still constrained by the CPU, RAM, and disk limits of that single physical machine.
# • Read a detailed breakdown on GeeksforGeeks.

# 3. Database Sharding
# • What it is: A form of horizontal partitioning where the data is distributed across multiple independent database servers (shards), where each shard acts as an autonomous database containing a subset of the total data.
# • How it works: Uses a sharding key (e.g., user_id or tenant_id) and a routing proxy to direct queries to the correct physical node.
# • Best used for: Massive scale systems with heavy write throughput and datasets too large for a single machine (e.g., social media platforms, multi-tenant SaaS).
# • Trade-offs: High architectural complexity, difficult cross-shard joins, and risks of "hot shards" if the sharding key is chosen poorly.
# • Explore platform-specific tools like MongoDB Sharding or cloud options like Azure SQL Database.

# How They Work Together
# In production systems, these strategies are rarely mutually exclusive:
# • You might shard a massive database across 10 different servers to handle high write volume and storage.
# • Then, you might replicate each of those 10 shards so that they have read-replicas for high availability and fast read traffic.
# • Inside each shard's database, you might use internal partitioning to keep individual tables organized.
# Are you designing a system for a specific use case? Tell me about your approximate data size, read-to-write ratio, or current bottleneck so I can recommend the right approach.




























# Window functions in sql
# SQL window functions perform calculations across a set of table rows that are related to the current row, without 
# collapsing the rows into a single summary value. Unlike a standard GROUP BY clause which aggregates data and hides 
# individual row details, window functions allow you to retain the identity of every single row while simultaneously 
# displaying aggregate, ranking, or positional metrics


# 🧱 Core Syntax Structure
# The fundamental mechanism of any window function is the OVER() clause. It defines the specific "window" of data that the function looks at.
# sql
# SELECT 
#     column_name,
#     FUNCTION() OVER (
#         PARTITION BY column_to_group
#         ORDER BY column_to_sort
#         ROWS/RANGE frame_specification
#     ) AS window_alias
# FROM table_name;
# Use code with caution.
# • PARTITION BY: Divides the rows into groups (or partitions). The function runs independently inside each group. If omitted, the entire dataset behaves as one large group.
# • ORDER BY: Dictates the sequence in which rows are processed within each partition. This is vital for running totals or sequential ranking.
# • ROWS / RANGE: Specifies a moving frame (e.g., "the last 3 rows up to the current row") for calculations like moving averages.


# 📂 The 3 Types of Window Functions
# 1. Aggregate Window Functions

# These are standard math operations applied dynamically across your window.
# • Functions: SUM(), AVG(), COUNT(), MAX(), MIN().
# • Common Use Case: Finding a running total or comparing an individual's salary against their specific department's average.
# sql
# -- Calculates department averages next to individual salaries
# SELECT name, department, salary,
#        AVG(salary) OVER(PARTITION BY department) AS avg_dept_salary
# FROM employees;
# Use code with caution.

# 2. Ranking Window Functions

# These assign sequential numbers or ranks to rows within your window partition.
# • ROW_NUMBER(): Gives every row a unique, sequential integer (1, 2, 3, 4...).
# • RANK(): Assigns ranks based on value ties, but leaves gaps in the sequence if ties happen (1, 2, 2, 4...).
# • DENSE_RANK(): Assigns ranks based on value ties without leaving gaps (1, 2, 2, 3...).

# Employee	Salary	ROW_NUMBER()	RANK()	DENSE_RANK()
# Alice	$10,000	1	1	1
# Bob	$9,000	2	2	2
# Charlie	$9,000	3	2	2
# David	$8,000	4	4	3


# 3. Value & Positional Window Functions

# These allow you to reach forward, backward, or target absolute positions relative to the current row without doing costly self-joins.
# • LAG(): Grabs a value from a previous row (great for calculating month-over-month growth).
# • LEAD(): Peeks ahead to grab a value from a subsequent row.
# • FIRST_VALUE() / LAST_VALUE(): Retrieves the absolute first or last value in the sorted window partition.
# sql
# -- Compares today's sales directly against yesterday's sales
# SELECT sale_date, daily_revenue,
#        LAG(daily_revenue, 1) OVER(ORDER BY sale_date) AS yesterdays_revenue
# FROM sales;
# Use code with caution.


# ⚠️ Common Gotcha: LAST_VALUE() and Default Frames
# When you introduce an ORDER BY statement inside an OVER() clause, SQL automatically applies a silent, hidden window frame constraint: ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW.
# Because the window frame stops moving at the current row, using LAST_VALUE() will frequently just return the current row's value rather than the actual "last" value of the whole partition. To fix this behavior, you must explicitly tell SQL to look through the whole window:
# sql
# -- Correct way to use LAST_VALUE across the entire partition
# LAST_VALUE(column) OVER (
#     PARTITION BY group_id ORDER BY sorting_id 
#     ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
# )
# Use code with caution.


# 💡 Summary Comparison
# Feature	Standard GROUP BY	Window Functions (OVER)
# Row Context	Collapses details; reduces row count.	Retains individual identity for every single row.
# Mix Aggregates	Cannot mix detail and total rows natively.	Seamlessly blends raw data alongside aggregate calculations.
# Execution Order	Filtered directly using HAVING.	Evaluated late; cannot be used inside WHERE or HAVING.








# How do you manage context in python:
# In Python, you manage context primarily using context managers and the with statement, which automate resource allocation and cleanup tasks like opening files, releasing locks, or closing database connections.
# Python also supports asynchronous context management and isolated context-local state storage.

# 1. Using Built-in Context Managers

# The with statement guarantees that cleanup code runs, even if exceptions occur inside the block. You can manage multiple resources in a single line or with parenthesized formatting.
# python
# # Managing a single file resource
# with open("data.txt", "r") as file:
#     content = file.read()
# # File is automatically closed here

# # Python 3.10+ Parenthesized context managers for multiple files
# with (
#     open("input.txt", "r") as infile,
#     open("output.txt", "w") as outfile
# ):
#     outfile.write(infile.read().upper())


# 2. Creating Custom Context Managers

# When you need to manage custom resources, you have two primary options:

# Method A: Class-Based (__enter__ and __exit__)

# Define a class implementing the context manager protocol. The __exit__ method accepts exception arguments to handle or suppress errors.
# python
# class DatabaseConnection:
#     def __enter__(self):
#         print("Connecting to database...")
#         return self
        
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Closing database connection...")
#         if exc_type:
#             print(f"An error occurred: {exc_val}")
#         return True # Returning True suppresses the exception; False propagates it

# with DatabaseConnection() as db:
#     print("Executing query...")


# Method B: Generator-Based (@contextmanager)

# For simpler use cases, use the contextlib.contextmanager decorator from the standard library. Code before the yield handles setup, and code in the finally block handles cleanup.
# python
# from contextlib import contextmanager

# @contextmanager
# def managed_resource():
#     print("Setup resource")
#     try:
#         yield "RESOURCE_DATA"
#     finally:
#         print("Teardown resource") # Guaranteed to run

# with managed_resource() as res:
#     print(f"Using {res}")


# 3. Asynchronous Context Managers

# For concurrent programs (like those using asyncio), synchronous context managers can block the event loop. Instead, implement __aenter__ and __aexit__ and invoke them using async with.
# python
# class AsyncResource:
#     async def __aenter__(self):
#         await asyncio.sleep(0.1) # Non-blocking setup
#         return self

#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         await asyncio.sleep(0.1) # Non-blocking cleanup

# async def main():
#     async with AsyncResource() as res:
#         print("Processing inside async context")


# 4. Managing Context-Local State

# If by "context" you mean tracking data across asynchronous tasks or threads without explicitly passing arguments, use the built-in contextvars module. This prevents data leakage between concurrent operations.
# python
# from contextvars import ContextVar

# # Declare a context variable at the module level
# request_id: ContextVar[str] = ContextVar("request_id")

# # Set the variable unique to the current execution context
# token = request_id.set("REQ-12345")

# # Retrieve it later anywhere in the same execution path
# print(request_id.get()) # Output: REQ-12345

# # Reset it back to previous state if needed
# request_id.reset(token)










# What is Chain-of-thought?
# Answer:
# Chain-of-thought (CoT) is a prompt engineering and AI reasoning technique that guides large language models (LLMs) to break down complex problems into intermediate, step-by-step logical thoughts before delivering a final answer.
# Instead of jumping straight from a question to an immediate (and potentially flawed) output, the model is encouraged to "show its work"—simulating human-like problem-solving.

# How It Works

# • Standard Prompting: You ask a hard math or logic question → the LLM guesses the final answer directly.
# • Chain-of-Thought Prompting: You ask the question and guide the model to generate intermediate rationales, formulas, or sequence steps first → the LLM arrives at a much more reliable final conclusion.

# Main Types of Chain-of-Thought

# 1. Few-Shot CoT: You provide the model with a few example questions that explicitly include step-by-step reasoning rationales alongside the answers.
# 2. Zero-Shot CoT: You don't give any examples; instead, you simply append a trigger phrase to your prompt—such as "Let's think step by step".
# 3. Automatic CoT (Auto-CoT): The system automatically clusters and samples diverse questions to generate reasoning chains on the fly.
# 4. Multimodal CoT: Extends step-by-step reasoning to non-text inputs like images, audio, or video data.

# Common Use Cases

# • Mathematical and Algebraic Reasoning: Breaking down multi-step word problems or equations where order of operations matters.
# • Software Coding and Debugging: Mapping out algorithmic logic, tracing breakpoints, or identifying the root cause of a bug.
# • Commonsense and Logic Puzzles: Evaluating multiple contextual factors or constraints before making a decision.

# Benefits and Limitations

# • Benefits:
# 	• Higher Accuracy: Drastically reduces mistakes on multi-step reasoning tasks.
# 	• Transparency: Lets you see how the model reached its conclusion, making it easier to debug or spot errors.
# • Limitations:
# 	• Higher Latency and Cost: Generating extra text/tokens for intermediate steps takes more compute time and resources.
# 	• Model Size Requirement: It works best on larger LLMs (typically 100+ billion parameters); smaller models may output a convincing-looking chain of steps that still leads to the wrong answer.
# 	• Faithfulness Gaps: Sometimes the intermediate logic doesn't actually match or cause the final answer.






