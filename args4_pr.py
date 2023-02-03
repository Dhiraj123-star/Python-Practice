# using three types of arguments in the function
# standard arguments,*args and **kwargs

def printData(codename,*args,**kwargs):
    print("I am ",codename)
    for arg in args:
        print("I am arg: ",arg)
    for keyword in kwargs.items():
        print(" I am kwargs: ",keyword)

printData("009",[90,90],Java=1,Python=2)