# call by value and reference in Python

# call by value 
# it is a way of passing arguments to a function in which the arguments
# get copied to the formal parameters of a function and are stored in
# different memory locations

# call by value example 

def myFun(a):
    print("value received in a ",a)
    a+=2
    print("value of a changes to ",a)

num=13
print("Initial num ",num)
myFun(num)
print("value of number ",num)


