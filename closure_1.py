# closure in Python

def outer (x):
    def inner(y):
        return x*y
    return inner

# take user input 

num1 = int(input("Enter your  first number: "))
num2 = int(input("Enter your second number"))
outer1 = outer(num1)
inner1 = outer1(num2)

print(inner1)