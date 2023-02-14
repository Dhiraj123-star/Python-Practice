# property in Python
class Person:
    # constructor 
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    # function to get name of the person
    def person_name(self):
        return self.name
    
    # setting the person_name() function as a property using property() function
    name_property = property(person_name)

if __name__=="__main__":
    Jack = Person("Jack",25)
    print("The name of the person is : ",Jack.name_property)


