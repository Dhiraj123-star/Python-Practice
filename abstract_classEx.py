# in Python , we use abc module  which provides the base and
# necessary tools for defining Abstract BASE Classes(ABC).
# ABC give the feature of virtual subclasses, which are classes
# that don't inherit from a class.
from abc import ABC , abstractmethod

class Parent (ABC):
    # common function
    def common_fn(self):
        print("I'm the common method of Parent!!")
    @abstractmethod
    def abs_fn(self): # is supposed to have different implementation in child class
       pass

class Child1(Parent): # inheritance
    def abs_fn(self):
        print("In the abstract method of child1")

class Child2(Parent):
    def abs_fn(self):
        print("In the abstract method of Child2")

# creating objects

ch1 = Child1()
ch1.abs_fn()
ch2= Child2()
ch2.abs_fn()
# parent =Parent() # throw error because this is abstract class





