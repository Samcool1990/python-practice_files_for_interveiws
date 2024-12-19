def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for consistent comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if both strings have the same length
    if len(str1) != len(str2):
        return False

    # Create a dictionary to count the frequency of characters in str1
    count_dict = {}    
    # Count characters in str1
    for char in str1:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    # Subtract the count of characters in str2
    for char in str2:
        if char in count_dict:
            count_dict[char] -= 1
        else:
            return False

    # Check if all counts are zero
    for count in count_dict.values():
        if count != 0:
            return False

    return True

# Example usage
str1 = "listen"
str2 = "silent"
if are_anagrams(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")



def two_sum(nums, target):
    # Create a dictionary to store the numbers we have seen so far
    seen = {}
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement (the number that, when added to num, gives the target)
        complement = target - num        
        # If the complement is in the dictionary, we have found a solution
        if complement in seen:
            return [seen[complement], i]        
        # Otherwise, store the current number and its index in the dictionary
        seen[num] = i    
    # Return None if no solution is found
    return None

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)

if result:
    print(f"Indices of the numbers that add up to {target}: {result}")
else:
    print(f"No solution found for the target {target}.")




# Question: In AWS how would you create authorization
# Answer: 
# AWS provides several mechanisms for implementing authorization:

# IAM Policies: Grant access to resources based on attached permissions. These can be applied to users, groups, and roles.

# Example: Granting an IAM role access to an S3 bucket.
# Cognito:

# Use User Pools for user authentication and group-based access control.
# Use Identity Pools for federated identities (e.g., social login) and AWS resource access.
# API Gateway with Lambda Authorizers:

# A Lambda Authorizer validates tokens (JWT, OAuth) or custom headers and returns an IAM policy to allow/deny the request.
# Resource-based Policies:

# Directly attach policies to resources like S3 buckets, Lambda functions, or API Gateway endpoints.
# Example: Lambda Authorizer for API Gateway
# python

import jwt

def lambda_handler(event, context):
    token = event['headers']['Authorization']
    try:
        decoded_token = jwt.decode(token, "your-secret-key", algorithms=["HS256"])
        principal_id = decoded_token['sub']
        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "execute-api:Invoke",
                    "Resource": event['methodArn']
                }
            ]
        }
        return {
            'principalId': principal_id,
            'policyDocument': policy
        }
    except jwt.ExpiredSignatureError:
        raise Exception("Unauthorized")


# Question: How Would You Handle Rate Limiting at the Application Level?
# Answer: Rate limiting prevents abuse by controlling the number of requests a client can make.

# Techniques:

# Token Bucket Algorithm:
# Maintain a "bucket" of tokens per client.
# Each request consumes a token. Tokens are replenished at a defined rate.
# In-Memory Data Stores:
# Use Redis or similar to store rate-limiting data.
# Store request counts and timestamps keyed by client ID.


# Middleware Implementation:
# Add rate-limiting middleware in frameworks like Django, FastAPI, or Express.js.
# Example (Python - FastAPI with Redis):
# python
from fastapi import FastAPI, HTTPException
import aioredis

app = FastAPI()
redis = aioredis.from_url("redis://localhost")

@app.middleware("http")
async def rate_limiter(request, call_next):
    client_id = request.client.host
    limit = 100
    count = await redis.incr(client_id)
    if count == 1:
        await redis.expire(client_id, 60)
    if count > limit:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    return await call_next(request)




# Question: How Would You Test API Delay in Application Level?
# Answer: To simulate and test API delays:

# Introduce Artificial Delay:

# Use tools like Postman to add delay in mock servers.
# Simulate in test code with sleep:
# python

import time

def delayed_response():
    time.sleep(5)  # Simulates delay
    return "Delayed response"

# Chaos Engineering:

# Tools like Gremlin or AWS Fault Injection Simulator introduce latency to observe system behavior.
# Timeout Testing:

# Configure shorter timeouts in your application and observe behavior when an API takes longer to respond.





# Questions:
# How would you handle rate limiting in application level ?
# Circuit breaker pattern ?
# you have one lambda with 4GB ram then you increase the RAM to 8GB & then add another lambda to it. 
# What type of scaling is it horizontal or Vertical.
# Raw SQL queries
# Difference between POST, PUT & PATCH

# READ ABOUT all design Patterns:
# https://codefresh.io/learn/microservices/top-10-microservices-design-patterns-and-how-to-choose/
# How would you test a API delay in application level ?
# is it a good practive to return 500s status code ?