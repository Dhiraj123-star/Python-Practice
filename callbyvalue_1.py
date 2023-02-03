# call by value in Python

def info(num):
    print("value received ",num)
    num+=1
    print("Value changes to ",num)
    print("Address in the function ",id(num))

num=1
print("Address before function call ",id(num))
info(num)
print("value after function call ",num)
print("address after function call ",id(num))