# static method is used to define a static method in the class
# it is called by instance of the class as well as class name

class Student:
    @staticmethod
    def show():
        print("I'm Student")

# create an object
stud= Student()
# call by instance of the class
stud.show()
# call by class name
Student.show()
