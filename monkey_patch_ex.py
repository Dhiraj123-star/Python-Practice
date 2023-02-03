from  monkey1 import Monkey

def monk_p(self):
    print("monk_p() is called")

Monkey.patch = monk_p # here we copy the address of monk_p to patch

obj = Monkey() 
obj.patch()


