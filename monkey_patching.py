# monkey.py
class A:
    def func(self):
        print("func is called")


# import monkey
class B:
    def monkey_func(self):
        print("Monkey function is called")


##replacing Adddress of func with monkey_func
A.func = B.monkey_func

obj = A()
# calling func whose address got replaced with monkey_func
obj.func()
# obj.monkey_func()
