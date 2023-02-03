# multiple inheritance in python

class Mammal:
    def mammal_info(self):
        print("mammal can give direct birth.")

class WingeAnimal:
    def winged_animal_info(self):
        print("winged animal can flap.")

class Bat(Mammal,WingeAnimal):
    pass 

# create object 
b1= Bat()

b1.mammal_info()
b1.winged_animal_info()