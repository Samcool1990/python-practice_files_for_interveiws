class Person:
    def __init__(self,name):
        self.name = name
    
    def func1(self):
        print(f"Hello my name is {self.name}")

obj = Person("Suman")
obj.func1()


