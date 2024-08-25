l1 = ['a','b','c']
l2 = [1,2,3]
#output = {'a':3, 'b': 2, 'c':1}
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
print('output',output)

list1 = [5,3,2,1,4]
n = len(list1)
for i in range(n):
    for j in range(i+1,n):
        if list1[i] > list1[j]:
            list1[j],list1[i] = list1[i], list1[j]
print(list1)


##decorators#######################
def decorator(func):
    def wrapper(x, y):
        print("Before function execution")
        result = func(x, y)
        print("After function execution")
        return result
    print(">>>")
    return wrapper

@decorator
def add(x, y):
    print("<<<<<<<")
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
####Generators#########
def func(n):
    for i in range(1,n+1):
        yield i*i
    
obj = func(3)
print(next(obj))
print(next(obj))
print(next(obj))


###iterators#####

list1 = iter([1,6,9,4,5,3])
print(f"1iter==> {next(list1)}")
print(f"2iter==> {next(list1)}")
print(f"3iter==> {next(list1)}")
#all the geneerators are iterators. But, all iterators are not generators