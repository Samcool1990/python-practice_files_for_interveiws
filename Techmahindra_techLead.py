# What is the difference between sql & No SQl. Which would you choose for which type of project??
# Django vs FastAPI vs Flask. Which would you choose for which type of projec ?
# If you have to make a game like Chess. How would you structure the code functionality wise ?
# Find the missing number from a sorted array.


# 1. Difference Between SQL and NoSQL. Which to Choose?
# SQL (Structured Query Language) Databases:

# Type: Relational Databases (RDBMS)
# Structure: Tables with rows and columns. Each table has a predefined schema.
# Examples: MySQL, PostgreSQL, Oracle
# When to Choose:
# Data is structured and requires relationships (i.e., foreign keys).
# Strong consistency and ACID (Atomicity, Consistency, Isolation, Durability) compliance are important.
# Examples: Financial systems, ERP (Enterprise Resource Planning) systems, applications where complex queries are common.
# NoSQL (Not Only SQL) Databases:

# Type: Non-relational Databases (Document-based, Key-value, Column-family, Graph)
# Structure: Flexible schema, can handle unstructured or semi-structured data.
# Examples: MongoDB (Document), Cassandra (Column), Redis (Key-Value), Neo4j (Graph)
# When to Choose:
# Large amounts of unstructured data.
# Horizontal scaling is crucial (distributed data over many servers).
# Flexibility in schema design is needed, or schema is likely to evolve.
# Examples: Real-time analytics, IoT applications, social media platforms.
# Summary:

# SQL is ideal for applications requiring strong consistency and relational data.
# NoSQL works best for scalability, handling large amounts of unstructured data, or when you need flexible schema design.


# 2. Django vs FastAPI vs Flask. Which to Choose?
# Django:
# Type: Full-stack, batteries-included web framework.
# Key Features: Built-in ORM, admin panel, authentication, middleware.
# Use Cases:
# Ideal for large, monolithic applications where you need everything out-of-the-box (e.g., admin interface, authentication, ORM).
# Projects where rapid development is important, like CMS (Content Management Systems) or eCommerce platforms.
# When to Choose: Large-scale applications requiring an all-inclusive framework with built-in features.
# FastAPI:
# Type: Modern, asynchronous web framework.
# Key Features: Asynchronous, high-performance, automatic OpenAPI documentation, pydantic-based data validation.
# Use Cases:
# Suitable for microservices, APIs, real-time systems, and applications where speed and performance are crucial.
# Examples include IoT systems, machine learning APIs, or any performance-critical API.
# When to Choose: Fast, high-performance applications, microservices, or systems where asynchronous features are important.
# Flask:
# Type: Lightweight, micro web framework.
# Key Features: Minimalistic, gives developers control over components.
# Use Cases:
# Good for small to medium projects where you need more control over libraries and architecture (e.g., simple web apps, REST APIs).
# Great for rapid prototyping, but less feature-rich than Django.
# When to Choose: Small to medium-sized projects where flexibility and simplicity are key. Good for microservices or developers comfortable assembling components.
# Summary:

# Django: Best for full-stack applications and large projects where built-in features are helpful.
# FastAPI: Ideal for building high-performance, asynchronous APIs or microservices.
# Flask: Great for small to medium-sized projects with more custom architecture.


# 3. Structuring Code for a Chess Game
# Here’s a typical way to structure the functionality of a Chess game:

# 1. Models (Classes):
# Board:
# Represents the 8x8 grid.
# Stores current state (positions of pieces, player turns).
# Piece (Abstract Base Class):
# Represents a chess piece.
# Subclasses: Pawn, Rook, Knight, Bishop, Queen, King.
# Each subclass defines its own movement logic (e.g., Pawn can move forward 1 square).
# Player:
# Represents a player (white/black).
# Stores player details (name, color).
# Game:
# Represents the actual game, manages players, and game state.
# Contains methods like start_game(), end_game(), checkmate(), stalemate().
# 2. Controller/Logic:
# Move Manager:
# Handles move validation and execution.
# Checks if a move is legal, handles special moves (castling, en passant).
# Updates the game state after each move.
# Game Manager:
# Controls game flow, alternates between players, checks for win conditions.
# Implements game rules such as checking for checkmate or stalemate.
# 3. Views:
# CLI/GUI:
# If you’re using a command-line interface (CLI), you could have a method to display the board state.
# For GUI, libraries like Pygame or Tkinter can be used to visualize the board and interact with the game.
# 4. Additional Functionalities:
# AI/Computer Opponent (Optional):
# Implement minimax algorithm or other strategies for the AI player.
# Networking (Optional):
# Add multiplayer support using websockets for real-time gameplay.
# Summary: Structure your code by separating responsibilities: Board and Pieces (Model), Move Management (Controller), and User Interface (View).


# 4. Find the Missing Number from an Unsorted Array
# This problem is commonly solved in O(n) time using the formula for the sum of an arithmetic series.

# Steps:
# Find the expected sum of numbers from 1 to n using the formula:
# sum
# (
# 1
#  to
# 𝑛
# )
# =
# 𝑛
# (
# 𝑛
# +
# 1
# )
# 2
# sum(1 to n)=
# 2
# n(n+1)
# ​

# Find the actual sum by summing up all elements in the array.
# The missing number is:
# Missing Number
# =
# Expected Sum
# −
# Actual Sum
# Missing Number=Expected Sum−Actual Sum
# Code Example:
# python
# Copy code
# def find_missing_number(arr, n):
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(arr)
#     return expected_sum - actual_sum

# # Example usage
# arr = [1, 2, 4, 5]  # Missing 3
# n = 5
# print(find_missing_number(arr, n))  # Output: 3


# 5. Suggested Interview Question: Explain How to Scale an Application?
# Answer:
# Scaling an application can be done either vertically or horizontally.

# Vertical Scaling (Scaling Up):

# Increase the resources (CPU, RAM, etc.) of your existing server.
# Simple to implement but has a limit based on hardware capacity.
# Horizontal Scaling (Scaling Out):

# Add more servers to distribute the load.
# Usually achieved by setting up load balancers and clustering your application.
# Examples: Adding more app servers, database replication (master-slave, sharding).
# Application Layer Strategies:
# Database: Use caching (Redis, Memcached), partitioning (sharding), or database replication for high availability and better performance.
# Web Servers: Use load balancers (Nginx, HAProxy) to distribute incoming requests across multiple servers.
# CDN (Content Delivery Network): For serving static files to offload work from the server.
