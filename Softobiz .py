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





#CalL A through constructor
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
# 2. What is the difference between useEffect & useLayoutEffect?
# 3. What is the difference between useMemo & useCallback?
# 4. Type of Models in Django  


# Question: Type of Models in Django  
# Answer:               
# 1. Abstract Base Classes: An abstract base class is a class that provides structure and functionality but 
# isn’t meant to be instantiated. It’s used to define common attributes and methods that can be inherited by 
# other classes.


