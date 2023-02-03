# operator overloading 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    # overload < operator
    def __lt__(self,other):
        return self.age<other.age


p1= Person("Alice",34)
p2=Person("Bob",18)

print(p1<p2) # False
print(p2<p1) # True 
