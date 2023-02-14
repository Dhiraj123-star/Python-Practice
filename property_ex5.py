# getter and setter  methods helps us to secure our class
# getter and setter helps us to encapsulate our data in a single object
# using methods so that the data can't be modified by just using an object
# of the class

class Student:
    # constructor
    def __init__(self,name=" "):
        self.name=name
        # getter method 
    def get_name(self):
        return self.name
    # setter method 
    def set_name(self,new_value):
        self.name=new_value

if __name__=='__main__':
    Tom = Student()
    # setting the name of the student
    Tom.set_name('Tom Hardy')
    # getting the name of the student
    print(f"Name: {Tom.get_name()}") 