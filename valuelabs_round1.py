l1 = ['a','b','c']
l2 = [1,2,3]
#outpu = {'a':3, 'b': 2, 'c':1}
ch = {}
l2.sort(reverse=True)
n = len(l1)
for i in range(n):
    if i not in ch:
        ch[l1[i]] = l2[i]
    
print(ch)
#########OR#################
l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]

output = {key: value for key, value in zip(l1, reversed(l2))}
print(output)

list = [5,3,2,1,4]
n = len(list)
for i in range(n):
    for j in range(i+1,n):
        if list[i] > list[j]:
            list[j],list[i] = list[i], list[j]
print(list)


##decorators#######################
def decorator(func):
    def wrapper(x, y):
        print("Before function execution")
        result = func(x, y)
        print("After function execution")
        return result
    return wrapper

@decorator
def add(x, y):
    return x + y

@decorator
def subtract(x, y):
    return x - y

result = add(5, 3)
print("Addition result:", result)

result = subtract(10, 4)
print("Subtraction result:", result)


# Testing the decorated functions

##MRO##################################
class A:
    def method(self):
        print("A's method")

class B(A):
    def method(self):
        print("B's method")

class C(A):
    def method(self):
        print("C's method")

class D(B, C):
    pass

d = D()
d.method()

#GIL
##Multithreading & multiprocessing
#Iterator & generator in Python with example
#all the geneerators are iterators. But, all iterators are not generators