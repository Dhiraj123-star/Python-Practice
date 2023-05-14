# data oriented programming with python

import numpy as np

class Point :
    def __init__(self,x,y) :
        self.x=x
        self.y=y 
    
    def __repr__(self):
        return "Point: {} , {}".format(self.x,self.y)

    def __add__(self,other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)
    
    def __mul__(self,other):
        return Point(self.x*other.x,self.y*other.y)
    def __truediv__(self,other):
        return Point(self.x/other.x,self.y/other.y)
    def __neg__(self):
        return Point(-self.x,-self.y)
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __ne__(self,other):
        return not(self==other)

def main():
    point1 = Point(1,2)
    point2 = Point(3,4)

    # add 
    point3 = point1+point2

    print("Add: ",point3)

    # subtract 
    point4 = point1-point2

    print("subtract: ",point4)

    # multiply 
    point5 = point1*point2

    print("Multiply: ",point5)

    # divide 
    point6 = point1/point2

    print("Division: ",point6)
    # negate 

    point7 = -point1

    print("Negate: ",point7)
    
    # compare the points 

    print(point1==point2)
    print(point1!=point2)


if __name__=="__main__":
    main()