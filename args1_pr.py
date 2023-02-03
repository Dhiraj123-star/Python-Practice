# use of *args in python
def multiplyNumbers(*args):
    product=1
    for n in args:
        product*=n
    return product

# call the function

print("product: ",multiplyNumbers(1,2,4)) # returns multiply result