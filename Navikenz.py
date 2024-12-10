# A-Z basics of Python
# Questions that I could not answer





# Question: Scope resolution in Python
# Answer:
# What are Namespaces in Python 
# A python namespace is a container where names are mapped to objects, they are used to avoid confusion in cases
# where the same names exist in different namespaces. They are created by modules, functions, classes, etc. 


# What is Scope in Python 
# A scope defines the hierarchical order in which the namespaces have to be searched in order to obtain the 
# mappings of name-to-object(variables). It is a context in which variables exist and from which they are 
# referenced. It defines the accessibility and the lifetime of a variable. Let us take a simple example as 
# shown below: 
pi = 'outer pi variable'

def print_pi(): 
	pi = 'inner pi variable'
	print(pi) 

print_pi() #inner pi variable
print(pi)  #outer pi variable


# Scope resolution LEGB rule In Python
# In Python, the LEGB rule is used to decide the order in which the namespaces are to be searched for scope resolution. The scopes are listed below in terms of hierarchy(highest to lowest/narrowest to broadest):

# Local(L): Defined inside function/class
# Enclosed(E): Defined inside enclosing functions(Nested function concept)
# Global(G): Defined at the uppermost level
# Built-in(B): Reserved names in Python builtin modules


# Local Scope in Python
# Local scope refers to variables defined in the current function. Always, a function will first look up a 
# variable name in its local scope. Only if it does not find it there, the outer scopes are checked. 
# Local Scope 
pi = 'global pi variable'
def inner(): 
	pi = 'inner pi variable'
	print(pi) 

inner()  #inner pi variable

# Local and Global Scopes in Python
# If a variable is not defined in the local scope, then, it is checked for in the higher scope, in this case,
#  the global scope. 
# Global Scope 
pi = 'global pi variable'
def inner(): 
	pi = 'inner pi variable'
	print(pi) 

inner()  #inner pi variable
print(pi)  #global pi variable


# Local, Enclosed, and Global Scopes in Python
# For the enclosed scope, we need to define an outer function enclosing the inner function, comment out the 
# local pi variable of the inner function and refer to pi using the nonlocal keyword. 
# Enclosed Scope 
pi = 'global pi variable'

def outer(): 
	pi = 'outer pi variable'
	def inner(): 
		# pi = 'inner pi variable' 
		nonlocal pi 
		print(pi) 
	inner() 

outer() #outer pi variable
print(pi) #global pi variable

# Local, Enclosed, Global, and Built-in Scopes
# The final check can be done by importing pi from math module and commenting on the global, enclosed, and 
# local pi variables as shown below: 
# Built-in Scope 
from math import pi 

# pi = 'global pi variable' 

def outer(): 
	# pi = 'outer pi variable' 
	def inner(): 
		# pi = 'inner pi variable' 
		print(pi) 
	inner() 

outer()  #3.141592653589793

# Since, pi is not defined in either local, enclosed or global scope, the built-in scope is looked up i.e the pi
# value imported from the math module. Since the program is able to find the value of pi in the outermost scope,
# the following output is obtained,











# Scope resolution LEGB rule In Python
# In Python, the LEGB rule is used to decide the order in which the namespaces are to be searched for scope resolution. The scopes are listed below in terms of hierarchy(highest to lowest/narrowest to broadest):

# Local(L): Defined inside function/class
# Enclosed(E): Defined inside enclosing functions(Nested function concept)
# Global(G): Defined at the uppermost level
# Built-in(B): Reserved names in Python builtin modules



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
