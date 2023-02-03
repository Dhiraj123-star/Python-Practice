# polymorphism in Python
# polymorphism is - having different forms 

class cat :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am cat. My name is {self.name} and my age is {self.age}")
    
    def makesound(self):
        print("Meow!!")

class Cow:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def info(self):
        print(f"I am cow and my name is {self.name} and my age is {self.age}")
    
    def makesound(self):
        print("Moo!!")

# create objects 

cat1 = cat("Kitty",20)
cow1= Cow("Fluffy",9)

for animal in (cat1,cow1):
    animal.info()
    animal.makesound()