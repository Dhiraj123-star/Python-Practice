# property decorator using class
# it is used to modify the getters and setters of a class 
# attributes 

class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    @property
    def display(self):
        return self.name + " got grade "+ self.grade

# create an object 
obj = Student("Dhiraj","A1")
print(obj.display)
print("Name ",obj.name)
print("Grade ",obj.grade)