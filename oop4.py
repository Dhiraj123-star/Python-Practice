# parent class
class Animal:
    name=""
    def eat(self):
        print("I can eat")

# child class 
class Dog(Animal):
    def display(self):
        super().eat() # call the parent class method
        print("The name is: ",self.name)

# create object 

labrador= Dog()
labrador.name="Rohu"
# call the child class method
labrador.display()

