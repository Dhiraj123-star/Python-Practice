# operator overloading 

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    # add two objects 
    def __add__(self,other):
        return self.real+other.real,self.imag+other.imag


obj1=Complex(1,2)
obj2=Complex(3,4)
obj3=obj1+obj2

print(obj3)
