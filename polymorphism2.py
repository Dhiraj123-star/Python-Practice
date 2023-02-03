# polymorphism with class inheritance 
from math import pi


class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass # just acts as like a placeholder
    def fact(self):
        print("I'm two dimensional Shape!!")
    def __str__(self):
        return self.name

class Square(Shape): # single inheritance
    def __init__(self,radius):
        super().__init__("Square") # call the base class constructor
        self.radius=radius
    def area(self):
        return pi*self.radius**2 
    
shape_square= Square(12)
print(shape_square)
print(shape_square.area()) 
shape_square.fact()


