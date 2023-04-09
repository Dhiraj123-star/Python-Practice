class Student :
    def __init__(self,name,age):
        self.name=name
        self.age =age 
    
    def __str__(self):
        return f"Student name is {self.name} and age is {self.age}"

# create object 
student = Student("Alice",23)

print(student)

# __repr__

class Person:
    def __init__(self,id,name):
        self.id =id
        self.name=name
    
    def __repr__(self) -> str:
        
        return f"Person({self.id},name= {self.name})"

# create object
person = Person(101,"John")
print(person)
        
