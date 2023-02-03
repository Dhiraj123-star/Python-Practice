# python inheritance 

class Animal: # parent class 
    # attribute and method of the parent class
    name=""
    def eat(self):
        print("I can eat")

# child class 

class Dog(Animal):

    # new method in the child class
    def display(self):
        # access name attribute of superclass using self
        print("My name is: ",self.name)

# create an object of the subclass
labrador=Dog()

# access superclass attribute and method
labrador.name="Rohu"
labrador.eat()
# access subclass method
labrador.display()
