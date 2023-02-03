# write a code snippet to convert a string into list
str1 = "Python Programming" 
print(str1.split(' '))

# concept of __init__ 

class book_shop:
    # constructor
    def __init__(self,title):
        self.title=title
    # sample method 
    def book(self):
        print("The title of the book :",self.title)

# creating object 
obj = book_shop("Python Programming Language")
obj.book()

    
# tuple comprehension

mytuple= (i for i in range(1,10,2))
print(mytuple)# it generates the object generator 
# convert into the list to get output 
print("Tuple comprehension",list(mytuple))

# dictionary comprehension
dict1= {i for i in range(1,11,2)}
print("Dictionary comprehension:",dict1)

# list comprehension
mylist= [i for i in range(1,11,2)]
print("List comprehension:",mylist)