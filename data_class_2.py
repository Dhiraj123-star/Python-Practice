from dataclasses import dataclass
@dataclass
class Point:
    x:int
    y:int 


@dataclass
class Circle:
    center :Point
    radius :int

p1 = Point(12,56)
c1 = Circle(center=p1,radius=23)

print(c1.center.x)

print(c1.radius)
