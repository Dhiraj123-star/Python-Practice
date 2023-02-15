# Python program to show how to use assert keyword

def squareNum(a):
    assert(a<0) ,"Give a positive number"
    return a**(1/2)

# calling function and passing the values
print(squareNum(25))
print(squareNum(-9))