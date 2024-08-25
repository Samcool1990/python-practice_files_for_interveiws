# PROJECT Experience

# System Design how to approach the requirements given by clients.
'''Understand the Requirements:
Client Meetings: Schedule meetings with the client to discuss their needs and expectations. Make sure you understand their business goals and objectives.
Ask Questions: Ask open-ended questions to get a detailed understanding of their requirements. Clarify any ambiguities and gather as much information as possible.
Document Everything: Create detailed documentation of the requirements, including functional and non-functional aspects.
Identify User Stories and Use Cases:
User Stories: Break down the requirements into user stories. Each user story should represent a specific functionality from the perspective of an end user.
Use Cases: Define the interactions between the system and external entities (users, other systems, etc.) in the form of use cases.
Define the System Architecture:
High-Level Architecture: Decide on the high-level architecture of the system. Consider factors like scalability, reliability, and maintainability.
Components: Identify the major components of the system and how they will interact with each other.
Data Modeling:
Database Schema: Design the database schema based on the data requirements. Choose appropriate data storage technologies (e.g., relational databases, NoSQL, etc.).
Data Flow: Understand how data will flow through the system, including storage, retrieval, and processing.
API and Service Design:
Define APIs: Design the APIs that will be exposed by the system. Specify the endpoints, request/response formats, and authentication mechanisms.
Microservices vs Monolith: Decide if the system will be a monolith or if it will use microservices architecture.
Security and Authentication:
Authentication and Authorization: Define how users will authenticate themselves and what actions they are authorized to perform.
Data Security: Implement measures to secure sensitive data, both in transit and at rest.
Scalability and Performance:
Scalability: Plan for how the system will handle increased load. Consider horizontal scaling, load balancing, and caching strategies.
Performance Optimization: Identify potential bottlenecks and implement optimizations where needed.
Error Handling and Logging
Error Handling: Define how errors will be handled, including user-friendly error messages and appropriate HTTP status codes.
Logging: Implement logging to record important events and errors for debugging and monitoring.
Testing Strategy:
Unit Testing: Plan for unit tests to ensure individual components work as expected.
Integration Testing: Test interactions between different components.
Load Testing: Test the system's performance under load.
Monitoring and Analytics:
Monitoring: Implement monitoring solutions to track system health, performance, and usage.
Analytics: Set up tools to gather insights on user behavior and system usage.
Deployment and DevOps:
Deployment Strategy: Decide how the system will be deployed (e.g., cloud, on-premises).
Continuous Integration/Continuous Deployment (CI/CD): Implement CI/CD pipelines for automated testing and deployment.
Documentation and Knowledge Sharing:
Documentation: Create comprehensive documentation for developers, operators, and users.
Training: Conduct training sessions for relevant stakeholders on how to use and maintain the system.
Feedback and Iteration:
Client Feedback: Gather feedback from the client during development and after deployment. Use it to make necessary improvements.'''
# Drop Undrop time travel etc in snowflake


# Given a string find out by which elements can be remove to make it the string palindrome
def min_removals_to_make_palindrome(s):
    n = len(s)
    
    # Initialize a table to store LPS lengths
    dp = [[0] * n for _ in range(n)]
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = 1
    
    # Build the table in bottom-up manner
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if (s[i] == s[j] and cl == 2):
                dp[i][j] = 2
            elif (s[i] == s[j]):
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    
    # Length of longest palindromic subsequence
    lps_length = dp[0][n - 1]
    
    # Number of characters to be removed
    min_removals = n - lps_length
    
    return min_removals

# Example usage
s = "abcda"
result = min_removals_to_make_palindrome(s)
print(result)  # Output: 2
