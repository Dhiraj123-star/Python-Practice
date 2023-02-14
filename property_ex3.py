# setter method that helps in modifying the value of the function
# the syntax of declaring the setter method decorator is : @property-name.setter

class Person:
    # constructor 
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @property
    def person_name(self):
        return self.name
    
    # setting the person_name() as a setter decorator 
    @person_name.setter
    def person_name(self,new_name):
        self.name= new_name
    
if __name__=='__main__':
    Tim = Person('Tim',34)
    print("Old name of the person is: ",Tim.person_name)

    new_name= 'Tim David'
    # modifying the name of the person
    Tim.person_name=new_name
    print("The new name of the person is: ",Tim.person_name)