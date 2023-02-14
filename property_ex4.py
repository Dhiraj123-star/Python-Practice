# python has deleter method which is used to delete the property of a class
# the syntax of declaring the deleter method is: property-name.deleter

class Person:
    # constructor 
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @property
    def person_name(self):
        return self.name
    @person_name.deleter
    def person_name(self):
        print(self.name,"is deleted")
        del self.name

if __name__=='__main__':
    John = Person('John',44)
    print("The name of the person is:  ",John.person_name)
    del John.person_name
    print("The name of the person is:  ",John.person_name)
        