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


