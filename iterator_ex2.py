# custom iterator using __iter__() & __next__ () method 

class ModOfTwo:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<=self.max:
            result = self.n%2 
            self.n+=1
            return result
        else:
            raise StopIteration
        
# creating object 
numbers = ModOfTwo(3)

# creating an iterator object
i=iter(numbers)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
#print(next(i)) # it throws StopIteration Error
