list1 = [1, 2, 3, (5, 6), {7: 8, 8: 9}, {10, 12}]

def recursive_sum(items):
    total = 0
    for item in items:
        if isinstance(item, (list, tuple, set)):  # Handle iterable types
            total += recursive_sum(item)
        elif isinstance(item, dict):  # Handle dictionary values
            total += recursive_sum(item.values())
        else:  # Handle individual numbers
            total += item
    return total

summation = recursive_sum(list1)
print(summation)





#Call A through constructor
class A:
    def __init__(self, person):
        self.person = person
        print(f"A called with person: {self.person}")
        
class B(A):
    def func1(self):
        print("B called")
        
class C(B, A):
    def __init__(self, person, manager):
        super().__init__(person)  # Call the constructor of A (via B due to MRO)
        self.manager = manager
        print(f"C called with manager: {self.manager}")


# Create an instance of C, passing values to the A constructor and C-specific parameters
objc = C(person="John", manager="Jane")
objc.func1()  # Call func1 from class B



# React Frontend Questions:
# 1. What is the difference useState & useRef?
# Aspect	            useState	useRef
# Purpose	            Manages state in a React component.	Stores a mutable reference that doesn't trigger re-renders.
# Triggers Re-render	Yes, updates to state cause the component to re-render.	No, changes to the current value do not cause re-renders.
# Typical Use Cases	For dynamic values that affect UI rendering (e.g., user input, toggles).	For accessing DOM elements, persisting values between renders (e.g., timers, counters).
# Syntax Example	    const [count, setCount] = useState(0);	const ref = useRef(null); ref.current = 42;
# React Behavior	    Async updates to batch changes for performance.	Immediate updates without batching.




# 2. What is the difference between useEffect & useLayoutEffect?
# Aspect	            useEffect	useLayoutEffect
# Execution Timing	Runs after the render has been committed to the screen.	Runs synchronously after all DOM mutations but before the browser paints.
# Blocking Rendering	No, non-blocking; doesn’t block painting.	Yes, blocking; the browser waits for it to complete.
# Use Cases	        For non-blocking side effects like fetching data, setting timers.	For DOM measurement, animations, and layout adjustments.
# Example	            Updating a state after an API call.	Adjusting DOM size or position before the paint.
# Impact on UI	    Less immediate impact, won’t block updates.



# 3. What is the difference between useMemo & useCallback?
# Aspect	            useMemo	useCallback
# Purpose	            Memoizes a computed value to prevent expensive recalculations.	Memoizes a callback function to prevent unnecessary re-creations.
# Return Value	    Returns a value.	Returns a function.
# Use Cases	        For heavy computations or derived states.	For passing stable functions as props to child components.
# Syntax Example	    useMemo(() => computeExpensiveValue(a, b), [a, b]);	useCallback(() => handleClick(a), [a]);
# Performance Focus	Optimizes calculations.	Optimizes function references.



# 4. Type of Models in Django  
# In Django, models are classes representing database tables. While Django doesn’t explicitly categorize models, they can serve different roles in an application, such as:

# Abstract Models

# Defined with abstract = True in the Meta class.
# Serve as a base class for other models, not directly used to create database tables.
# Example:
# python
# Copy code
# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         abstract = True
# Concrete Models

# Standard models used to create database tables.
# Example:
# python
# Copy code
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
# Proxy Models

# Used to alter the behavior of an existing model without modifying the underlying database schema.
# Example:
# python
# Copy code
# class ProductProxy(Product):
#     class Meta:
#         proxy = True
#         ordering = ['name']
# Polymorphic Models

# Used in inheritance to enable querying across different types of child models. Achieved through third-party libraries like django-polymorphic.
# Manager Models

# Extend functionality with custom manager methods to encapsulate complex queries.
# Example:
# python
# Copy code
# class ProductManager(models.Manager):
#     def expensive_products(self):
#         return self.filter(price__gt=1000)
# Through Models

# Used in many-to-many relationships to store additional information in the relationship table.
# Example:
# python
# Copy code
# class Membership(models.Model):
#     person = models.ForeignKey('Person', on_delete=models.CASCADE)
#     group = models.ForeignKey('Group', on_delete=models.CASCADE)
#     date_joined = models.DateField()
# Let me know if you'd like more details or examples!



# Question: Type of Models in Django  
# Answer:               
# 1. Abstract Base Classes: An abstract base class is a class that provides structure and functionality but 
# isn’t meant to be instantiated. It’s used to define common attributes and methods that can be inherited by 
# other classes.


