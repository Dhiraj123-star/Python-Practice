# multilevel inheritance in python

class Superclass: 
    def super_method(self):
        print("Super class method called")

class DerivedClass1(Superclass):
    def derived_method1(self):
        print("Derived class 1 method called")

class DerivedClass2(DerivedClass1):
    def derived_method2(self):
        print("Derived class 2 method called")

# create object 
d2 = DerivedClass2()
# call the methods
d2.super_method()
d2.derived_method1()
d2.derived_method2() 
