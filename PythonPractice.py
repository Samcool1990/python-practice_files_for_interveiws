#recurssion explain with function:
def reversed_lst(lst):
    if not lst:
        return []
    return [lst[-1]]+ reversed_lst(lst[:-1])


#multiple Inheritance:
class A:
    def abc(self):
        print("a")
class B(A):
    def abc(self):
        print("b")
class C(A):
    def abc(self):
        print("c")
class D(B,C):
    pass

d= D()
d.abc()


#decorator:
def decorator_func(func):
    def wrapper_func():
        print("wrapper")
        return func()
    print("decorator")
    return wrapper_func

def show():
    print("show")
deco = decorator_func(show)
deco()


#self keyword:
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"my name is {self.name} & I am {self.age} years old")

c = person("suman",34)
c.info()


#Monkey patching:
#monkey.py
class A:
    def func(self):
        print("func() is called")


#import monkey

def monkey_func(self):
    print("monkey_func is called")

A.func = monkey_func
obj = A()

#Dictionary item interchange:
d = {
    "a":1,
    "b":2
}
d2 = {k:v for v,k in d.items()}
print(d2)