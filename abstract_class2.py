# Data abstraction in Python
from abc import ABC, abstractmethod

class Animal(ABC):

    # concrete method 
    def sleep(self):
        print("I'm going to sleep in a while")
    @abstractmethod
    def sound(self):
        print("This function is for defining the sound by any animal")
        pass

class Snake(Animal): # inheritance 
    def sound(self):
        print("I can hissss")
class Dog(Animal):
    def sound(self):
        print("I can bark")
class Lion(Animal):
    def sound(self):
        print("I can roar")
class Cat(Animal):
    def sound(self):
        print("I can meow")
class Rabbit(Animal):
    def sound(self):
        super().sound() # call the parent class's concrete method 
        print("I can squeak")

class Deer(Animal):
    # def sound(self):
       pass 

# creating objects

cat = Cat()
cat.sleep()
cat.sound()

dog= Dog()
dog.sleep()
dog.sound()

snake=Snake()
snake.sleep()
snake.sound()

rabbit = Rabbit()
rabbit.sound()

# deer =Deer() # throw error because we do not implement the abstract method sound
# deer.sound()
# deer.sleep()