# using property decorator

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    # setting the person_name() function as a property using @property decorator. 
    @property
    def person_name(self):
        return self.name

# driver code 

if __name__ == '__main__':
    Dravid = Person("Dravid",45)
    print("The name of the person is : ",Dravid.person_name)
