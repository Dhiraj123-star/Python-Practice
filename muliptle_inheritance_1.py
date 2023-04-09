# multiple inheritance in Python

class Base1:
    def first_method(self):
        print("This is the first base class")

class Base2:
    def second_method(self):
        print("This is the second base class")

# multiple inheritance 
class Child(Base1,Base2):
    pass

# create objects
obj = Child()

# call the methods
obj.first_method()
obj.second_method()