# class decorator 
class Power(object):
    def __init__(self,arg):
        self._arg= arg 
    
    def __call__(self,a,b):
        retval = self._arg(a,b)
        return retval**3

@Power
def multiply_together(a,b):
    return a*b


# take user input 

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

print(multiply_together(a,b))
