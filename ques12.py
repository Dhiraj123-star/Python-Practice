# working of __init__in python 
class Student:
    def __init__(self,name,rollno,st_class,marks):
        self.name=name
        self.rollno =rollno
        self.st_class = st_class
        self.marks=marks

# creating object 
s1= Student("Dhiraj",1,"BCA",89)

print(s1.name)
print(s1.st_class)



    
        