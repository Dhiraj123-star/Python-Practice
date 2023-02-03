# class with method

class Room:
    length=0.0
    breadth=0.0

    # method to calculate area
    def calculateArea(self):
        print("Area of Room = ",self.length*self.breadth)
    
# create object
room1= Room()
# access the attributes 
room1.length=10.4
room1.breadth=9.3

# call the class method
room1.calculateArea()