# A-Z basics of Python
# Questions that I could not answer
# Scope resolution in Python
# SOLID principles in Python
# Noramlization in SQL
# type of noramlization in sql & explain all
# How do you combine 2 different dictionaries where if any dictionary key matches then both values will be 
# added
# together. Sample dictionaries
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}

# Combine dictionaries with sum of values for matching keys
combined_dict = {
    key: dict1.get(key, 0) + dict2.get(key, 0) for key in dict1.keys() | dict2.keys()
}

print(combined_dict)
# Have you faced any technical blocker in your current role & how come you have overcome it ?
# How your role as a senior developer help the team?
# Draw the django architecture.
# Draw how viewes render template & model to render page
# numpy vs list for arithmetic operations
# Question: In AWS how many type of load balancer
# Answer: Amazon Web Services (AWS) offers four types of load balancers:
# Application Load Balancer (ALB)
# Good for managing HTTP and HTTPS traffic, and performing advanced routing. ALB can route traffic based on content, URL path, or host header.
# Network Load Balancer (NLB)
# Designed for high performance and low latency, NLB is good for handling TCP/UDP traffic. NLB routes requests to the closest Availability Zones to efficiently distribute global traffic.
# Gateway Load Balancer (GLB)
# Used to deploy, scale, and manage virtual appliances like firewalls and intrusion detection systems. GLB doesn't act as a proxy or terminate the connection, it forwards traffic directly.
# Classic Load Balancer (CLB)
# The legacy option, CLB is primarily for applications that haven't been migrated to newer load balancer types.
