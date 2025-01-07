####Generators#########
def func(n):
    for i in range(1,n+1):
        yield i*i
    
obj = func(3)
print(next(obj))
print(next(obj))
print(next(obj))

'''In Python, a generator is a function that returns an iterator that produces a
sequence of values when iterated over. Generators are useful when we want to produce a large sequence of 
values, but we don't want to store all of them in memory at once.'''
###iterators#####

list1 = iter([1,6,9,4,5,3])
print(f"1iter==> {next(list1)}")
print(f"2iter==> {next(list1)}")
print(f"3iter==> {next(list1)}")



# fibonacci_series using a Generator
def fibonacci_series(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

f1 = fibonacci_series(5)
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))

def fibonacci_series2(n):
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

f2 = fibonacci_series(5)
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))