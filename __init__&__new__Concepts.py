# __init__ and __new__ in Python class

class Student:
    def __new__(cls):
        print("creating a new instance of Student class")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self):
        print("Initialising the attributes of Student")
        self.attribute= "Initialised"

# create object 

student= Student()
print(student.attribute)