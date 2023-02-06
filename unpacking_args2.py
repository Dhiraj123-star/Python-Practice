# unpacking argument with ** operator

def myFun(arg1,arg2,arg3):
    print("args 1: ",arg1)
    print("args 2: ",arg2)
    print("args 3: ",arg3)

# driver code

kwargs = {"arg1":"Python","arg2":"Interview","arg3":"Packing and Unpacking"}
myFun(**kwargs)
