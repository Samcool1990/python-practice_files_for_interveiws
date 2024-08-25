class A:
    def display(self):
        print("A Display")

class B(A):
    def show(self):
        print("B Show")
    
d = B()
d.show()
d.display()

A.display(d)
# Desiredclass.method/function(created_class object)

#Explain type of inheritance
#Single Inheritance:
class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):
    pass

c = Child()
c.method()  # Output: "Parent method"
#Multiple Inheritance:
class Parent1:
    def method1(self):
        print("Parent1 method")

class Parent2:
    def method2(self):
        print("Parent2 method")

class Child(Parent1, Parent2):
    pass

c = Child()
c.method1()  # Output: "Parent1 method"
c.method2()  # Output: "Parent2 method"

#Multilevel Inheritance:
class Grandparent:
    def method(self):
        print("Grandparent method")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.method()  # Output: "Grandparent method"

#Hierarchical Inheritance:
class Parent:
    def method(self):
        print("Parent method")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()
c1.method()  # Output: "Parent method"
c2.method()  # Output: "Parent method"
#Hybrid (or Cyclic) Inheritance:
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass


'''The five types of inheritance in Python are single, multiple, multilevel, hierarchical, 
and hybrid inheritance'''