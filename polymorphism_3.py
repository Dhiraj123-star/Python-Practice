# polymorphism with functions and objects
class Beans:
    def type(self):
        print("Vegetable")
    def color(self):
        print("Green!!")
    
class Mango :
    def type(self):
        print("Fruit")
    def color(self):
        print("Yellow!!")

def func(obj):
    obj.type()
    obj.color()
# create objects

vege1 = Beans()
fruts = Mango()
func(vege1)
func(fruts)